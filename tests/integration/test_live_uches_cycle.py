import inspect
import json
import os
from pathlib import Path

from gltest import get_validator_factory
from gltest.assertions import tx_execution_succeeded
from gltest_cli.config.general import get_general_config
from gltest.contracts.contract_factory import ContractFactory

RPC = "https://studio.genlayer.com/api"
CA = "0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073"
GEN = 10**16
ZERO = "0x0000000000000000000000000000000000000000"


def context(verdict="SATISFIED", ok=True, completed=None):
    validators = get_validator_factory().batch_create_mock_validators(count=5, mock_llm_response={
        "nondet_exec_prompt": {"GenLayer validator judging evidence": json.dumps({
            "ok": ok, "verdict": verdict, "reason": "agent evidence supports the service result",
            "evidence_summary": "service output reviewed", "missing_requirements": "", "safe_error": "",
            "completed_deliverables": completed or []
        })}
    })
    return {"validators": [v.to_dict() for v in validators]}


def test_live_aase_partial_cycle(default_account):
    os.chdir(Path(__file__).parents[2])
    get_general_config().set_contracts_dir(Path("contracts").resolve())
    factory = ContractFactory("AuthenticityChainEscrow", Path("contracts/uches.py").read_text())
    contract = factory.build_contract(contract_address=CA, account=default_account).connect(default_account)
    import gltest.contracts.contract as contract_module
    contract_module._fee_kwargs = lambda call, fees, fee_value: {}
    client = contract_module.get_gl_client()
    wait = client.wait_for_transaction_receipt
    if "wait_until" not in inspect.signature(wait).parameters:
        client.wait_for_transaction_receipt = lambda transaction_hash, interval, retries, **kwargs: wait(transaction_hash, interval=interval, retries=retries)
    agent = default_account.address
    base = int(json.loads(contract.stats(args=[]).call())["next_intent_id"])
    opened = contract.create_service_intent(args=[agent, "Autonomous research service", "TEXT evidence", '[{"id":"research","weight_bps":6000},{"id":"sources","weight_bps":4000}]', 1800, 1800, ZERO, ZERO, 0]).transact(value=GEN, transaction_context=context())
    assert tx_execution_succeeded(opened)
    evidence = contract.submit_agent_evidence(args=[base, "TEXT", "Research completed; sources pending.", "live test"]).transact(transaction_context=context())
    assert tx_execution_succeeded(evidence)
    resolved = contract.resolve(args=[base]).transact(transaction_context=context("PARTIAL", True, ["research"]))
    assert tx_execution_succeeded(resolved)
    assert contract.verdict_of(args=[base]).call() == "PARTIAL"
    result = json.loads(contract.get_intent(args=[base]).call())
    assert result["payout_to_requester"] == str(GEN * 4000 // 10000)
    assert result["payout_to_fulfiller"] == str(GEN * 6000 // 10000)
