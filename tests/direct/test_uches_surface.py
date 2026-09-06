from pathlib import Path

CONTRACT = str(Path(__file__).parents[2] / "contracts" / "provenance.py")
ZERO = "0x0000000000000000000000000000000000000000"


def test_artifact_registration_records_identity(direct_vm, direct_deploy, direct_alice):
    contract = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    artifact_id = contract.register_artifact("sha256:1234567890abcdef", "certificate", "issuer-1", "issued in 2026", ZERO)
    assert artifact_id == 1
    assert '"status": "OPEN"' in contract.get_artifact(artifact_id)


def test_only_registrant_can_add_custody(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    artifact_id = contract.register_artifact("sha256:1234567890abcdef", "certificate", "issuer-1", "issued in 2026", ZERO)
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("only registrant"):
        contract.add_custody_event(artifact_id, "holder", "TRANSFER", "sha256:abcdef1234567890", "2026-01-01T00:00:00Z")
