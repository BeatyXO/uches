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
pytest -q tests/direct
```

## Deployment

Live deployment: `0x37C14D19be3E62775e8a528bb9d1923deFFF5d16` on GenLayer StudioNet (chain ID `61999`). [Studio Explorer](https://explorer-studio.genlayer.com/address/0x37C14D19be3E62775e8a528bb9d1923deFFF5d16). Deployment transaction: `0x89c67c44e58c49e16b109d6afb645078008e230524f41e5f53da953a0a059773`.

Live verification: registration `0xbb1c0eba01a6fd43c49fc3298ab4d344af932052f3b20e4bd0267d2b11c72607`; custody `0x890cd269e2afc91e07a4bb76284a6c1428aa56af0d03a3e9d66fd4e586b3fcdc`; provenance evidence `0x3973484de85ac71f28d5f35a502b68f610bd51f2d6edca3bb6bef6e87f7e91bf`; real-validator verification `0x071b39446ffae77ef0d51e80f259756a450f319a6498e76ef81c68028c4a96f0`. Final status: `INCONCLUSIVE`, with one custody event and one evidence record.
