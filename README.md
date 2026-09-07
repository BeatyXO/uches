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

Live deployment: `0x742db46384a3B683D930c05Ac646097b32Eb4C9f` on GenLayer StudioNet (chain ID `61999`). [Studio Explorer](https://explorer-studio.genlayer.com/address/0x742db46384a3B683D930c05Ac646097b32Eb4C9f). Deployment transaction: `0x70201f30308bb9c40bab4318101031955bb536e529819b974496fd429f1a9405`.

Live verification: registration `0x215595cdfadeeb412f9b5cce75551d6b09059b0cf9ad1b558f89f61ffb1aadf6`; evidence `0x24f2741a95ca7f2f5c69c97dc02db2ae887580d76f7874c786204be13f415b80`; normal verification `0xc841a8c5a4779a16ad3413220cb70a9e02cfe2b2243cdad566790db62c750cd4`. Final status: `INCONCLUSIVE`.
