# UCHES — Authenticity Chain Registry

UCHES is a standalone GenLayer Intelligent Contract for registering artifact identity and verifying provenance. It records an artifact hash, issuer, origin claim, timestamped custody events, and public evidence; GenLayer validators then assess whether the evidence supports authenticity, rejection, or an inconclusive result.

UCHES does not hold funds. Its reusable output is an authenticity record that certificate registries, collectible platforms, supply-chain systems, media archives, and credential issuers can consume.

## Lifecycle

`OPEN → EVIDENCE_SUBMITTED → AUTHENTIC / REJECTED / INCONCLUSIVE → CHALLENGED or REVOKED`

The registry preserves bounded custody history, provenance evidence, validator results, challenge records, revocation, and source timestamps. Validators inspect the artifact identity, issuer claim, provenance chain, and evidence together; they must not invent missing custody facts or rely on a single operator’s assertion.

## Interface

- `register_artifact(...)` — register an artifact identity and origin claim.
- `add_custody_event(...)` — append a bounded, hash-identified custody event.
- `submit_provenance_evidence(...)` — attach bounded source evidence.
- `verify_authenticity(...)` — obtain a consensus-backed authenticity result.
- `challenge_authenticity(...)` — submit an independent challenge.
- `revoke_artifact(...)` — revoke a registered artifact.
- `get_artifact(...)`, `get_entry(...)`, `stats()` — read state.

## Development

```powershell
python -m py_compile contracts/provenance.py
genvm-lint check contracts/provenance.py --json
```

## Deployment

Live deployment: `0x543B988Bd0b031aCa0d42c326DBCB65856d2eC2c` on GenLayer StudioNet (chain ID `61999`). [Studio Explorer](https://explorer-studio.genlayer.com/address/0x543B988Bd0b031aCa0d42c326DBCB65856d2eC2c). Deployment transaction: `0x81d94b104c0668b8a7f97cef66155f4123a61583e31bc8fd8a75d9009ff5929b`.

Live verification: registration `0x13a252cd806cb6602ec68aa426259b2f2f363ece8c88e34190c006ce9f9e8811`; custody `0xc1f30523ae0cbed8d98f4253346a6613305b57fe09773cbf15024b98b6f4a8a6`; provenance evidence `0x6c470c4fffb7550fbf13c2a96f996e547563dc3225cbf3cfcee2c701c3f6fabf`; real-validator verification `0x0237b6dde97f0027252a6a7698a66c7a155b9c6820145dd3c58846e45709b619`. Final status: `INCONCLUSIVE`; validators independently retrieved the public source and refused unsupported claims.
