from pathlib import Path

from conftest import set_value

CONTRACT = str(Path(__file__).parents[2] / "contracts" / "uches.py")
GEN = 10**18
ZERO = "0x0000000000000000000000000000000000000000"


def test_create_service_intent_records_terms(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    set_value(direct_vm, GEN)
    intent_id = contract.create_service_intent(
        direct_bob,
        "Return a research brief with cited primary sources.",
        "Evidence must include the delivered brief and public source URLs.",
        '[{"id":"brief","weight_bps":7000},{"id":"sources","weight_bps":3000}]',
        1800, 1800, ZERO, ZERO, 0,
    )
    assert intent_id == 1
    assert '"status": "OPEN"' in contract.get_intent(intent_id)


def test_agent_evidence_is_bounded_and_typed(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    set_value(direct_vm, GEN)
    intent_id = contract.create_service_intent(direct_bob, "Do work", "Provide evidence", '[{"id":"work","weight_bps":10000}]', 1800, 1800, ZERO, ZERO, 0)
    direct_vm.sender = direct_bob
    contract.submit_agent_evidence(intent_id, "WEB_TEXT", "https://example.com", "public source")
    assert 'WEB_TEXT' in contract.get_evidence(intent_id, 0)
