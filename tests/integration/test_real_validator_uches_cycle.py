import json
import os
from pathlib import Path

from gltest.assertions import tx_execution_succeeded
from gltest.contracts.contract_factory import ContractFactory
from gltest_cli.config.general import get_general_config
import gltest.contracts.contract as contract_module

CA = "0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073"
ZERO = "0x0000000000000000000000000000000000000000"
GEN = 10**16


def test_real_validator_funded_cycle(default_account):
    os.chdir(Path(__file__).parents[2])
    get_general_config().set_contracts_dir(Path("contracts").resolve())
    factory = ContractFactory("AuthenticityChainEscrow", Path("contracts/uches.py").read_text())
    contract = factory.build_contract(contract_address=CA, account=default_account).connect(default_account)
    contract_module._fee_kwargs = lambda call, fees, fee_value: {}
    client = contract_module.get_gl_client()
    original_wait = client.wait_for_transaction_receipt
    client.wait_for_transaction_receipt = lambda transaction_hash, interval, retries, **kwargs: original_wait(transaction_hash, interval=interval, retries=retries)
    intent_id = int(json.loads(contract.stats(args=[]).call())["next_intent_id"])
    created = contract.create_service_intent(args=[default_account.address, "Return a concise research report", "Use the submitted report as evidence", '[{"id":"report","weight_bps":10000}]', 1800, 1800, ZERO, ZERO, 0]).transact(value=GEN)
    assert tx_execution_succeeded(created)
    evidence = contract.submit_agent_evidence(args=[intent_id, "TEXT", "Research report: GenLayer is an optimistic execution network. Source: https://genlayer.com", "credible public-source report"]).transact()
    assert tx_execution_succeeded(evidence)
    resolved = contract.resolve(args=[intent_id]).transact()
    assert tx_execution_succeeded(resolved)
    result = json.loads(contract.get_intent(args=[intent_id]).call())
    tx_hash = lambda tx: tx.get("hash", tx.get("tx_id", str(tx))) if isinstance(tx, dict) else str(tx)
    record = {"create": tx_hash(created), "evidence": tx_hash(evidence), "resolve": tx_hash(resolved), "final": result}
    Path("docs/live-real-validator-result.json").write_text(json.dumps(record, indent=2, default=str), encoding="utf-8")
    print(json.dumps(record, default=str), flush=True)
    assert result["status"] == "RESOLVED"
