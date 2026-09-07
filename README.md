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

Live deployment: `0x65737a541D425a852962454fe5Bad0d124CA8b0b` on GenLayer StudioNet (chain ID `61999`). [Studio Explorer](https://explorer-studio.genlayer.com/address/0x65737a541D425a852962454fe5Bad0d124CA8b0b). Deployment transaction: `0x7f973dbd19225d6eca113cdc64bab2f61b52cc78ee9d8597ec206e7b9ff3cab1`.

Live verification: registration `0x62aeec87d1610ac5953d46e3863014b2dd6c9203d707abf0dda257603e4c85de`; evidence `0xcf6bdf3701355c0329967c56e716d9782d09323b247ade371317fafac93516db`; verification `0x59735d90a90859b2e3062e6e1aba825ddf1def9cf4bcc8ebff8ce87951255e95`; challenge `0xf8266c10ab026f978e4b52d0055785db58882e98a6976d9f3cef5d0671893f54`; reassessment `0x4605d439ab3e7022df2ee3f5fb3031544b38b82f183c0fe805f379e1a75abfee`. Final status: `INCONCLUSIVE`.
