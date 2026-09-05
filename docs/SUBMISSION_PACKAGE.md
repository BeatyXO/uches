# UCHES Submission Package

UCHES is a standalone Intelligent Contract. Its load-bearing property is consensus-backed authenticity verification before deterministic escrow release. External evidence is acquired inside nondeterministic execution; payout calculations and all state transitions are deterministic.

## Deployment

- Network: GenLayer StudioNet
- Chain ID: `61999`
- Contract address: `0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073`
- Explorer: https://explorer-studio.genlayer.com/address/0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073
- Deployment transaction: `0xaacae5c3e84377ff2e69d9906f547d4ea49e1514cbfa1902555a82a1cfc00c94`

The exact `contracts/uches.py` source was accepted by StudioNet deployment consensus in one round. Deployment transaction: `0xaacae5c3e84377ff2e69d9906f547d4ea49e1514cbfa1902555a82a1cfc00c94`.

## Live verification

The funded live lifecycle created intent `1`, submitted one authenticity evidence item, and executed `resolve()` with real validators. The final result was `INCONCLUSIVE` because the evidence was self-asserted and lacked external provenance; escrow remained safely held (`open_intents: 1`, `settled_intents: 0`, balance `10000000000000000`). The resolve transaction was `0x0c758b2776e79d4ec6d9e50d751bd5844e5a1f9f9355570e9ce728abeca42134`; validator votes included three agrees, one disagree, and one idle.

## Reproducible commands

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install genlayer gltest pytest
python -m py_compile contracts/uches.py
genvm-lint check contracts/uches.py --json
pytest -q tests/direct
pytest -q tests/integration/test_live_aase_cycle.py
pytest -q -s tests/integration/test_real_validator_cycle.py
```
