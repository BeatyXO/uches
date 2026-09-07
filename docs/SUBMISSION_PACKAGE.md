# UCHES Submission Package

UCHES is a standalone authenticity and provenance registry. It records artifact identity, issuer claims, timestamped custody events, and source evidence, then uses GenLayer validator consensus to produce a structured authenticity result. It has no escrow, payment, bond, or payout mechanism.

## Trust model

The registrant supplies claims and evidence, but cannot author the authenticity result alone. Validators independently inspect the artifact hash, provenance chain, and public sources. Stable status and derivative flags are compared; explanations remain descriptive.

## Commands

```powershell
python -m py_compile contracts/provenance.py
genvm-lint check contracts/provenance.py --json
```

## Live deployment and measured lifecycle

- Network: GenLayer StudioNet; chain ID `61999`.
- Contract: `0x65737a541D425a852962454fe5Bad0d124CA8b0b`.
- Deployment: `0x7f973dbd19225d6eca113cdc64bab2f61b52cc78ee9d8597ec206e7b9ff3cab1`.
- Register artifact: `0x62aeec87d1610ac5953d46e3863014b2dd6c9203d707abf0dda257603e4c85de`.
- Add custody event: `0xc1f30523ae0cbed8d98f4253346a6613305b57fe09773cbf15024b98b6f4a8a6`.
- Submit provenance evidence: `0xcf6bdf3701355c0329967c56e716d9782d09323b247ade371317fafac93516db`.
- Real-validator verification: `0x59735d90a90859b2e3062e6e1aba825ddf1def9cf4bcc8ebff8ce87951255e95`.
- Challenge: `0xf8266c10ab026f978e4b52d0055785db58882e98a6976d9f3cef5d0671893f54`; reassessment: `0x4605d439ab3e7022df2ee3f5fb3031544b38b82f183c0fe805f379e1a75abfee`. Final state: `INCONCLUSIVE`; validators compared independently retrieved original and challenge sources.
