# UCHES Submission Package

UCHES is a standalone authenticity and provenance registry. It records artifact identity, issuer claims, timestamped custody events, and source evidence, then uses GenLayer validator consensus to produce a structured authenticity result. It has no escrow, payment, bond, or payout mechanism.

## Trust model

The registrant supplies claims and evidence, but cannot author the authenticity result alone. Validators independently inspect the artifact hash, provenance chain, and public sources. Stable status and derivative flags are compared; explanations remain descriptive.

## Commands

```powershell
python -m py_compile contracts/provenance.py
genvm-lint check contracts/provenance.py --json
pytest -q tests/direct
```

## Live deployment and measured lifecycle

- Network: GenLayer StudioNet; chain ID `61999`.
- Contract: `0x37C14D19be3E62775e8a528bb9d1923deFFF5d16`.
- Deployment: `0x89c67c44e58c49e16b109d6afb645078008e230524f41e5f53da953a0a059773`.
- Register artifact: `0xbb1c0eba01a6fd43c49fc3298ab4d344af932052f3b20e4bd0267d2b11c72607`.
- Add custody event: `0x890cd269e2afc91e07a4bb76284a6c1428aa56af0d03a3e9d66fd4e586b3fcdc`.
- Submit provenance evidence: `0x3973484de85ac71f28d5f35a502b68f610bd51f2d6edca3bb6bef6e87f7e91bf`.
- Real-validator verification: `0x071b39446ffae77ef0d51e80f259756a450f319a6498e76ef81c68028c4a96f0`.
- Final state: `INCONCLUSIVE`; one custody event and one evidence record. Validators correctly refused to authenticate unsupported issuer, origin, and hash claims.
