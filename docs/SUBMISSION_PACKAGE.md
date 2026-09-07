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
- Contract: `0x742db46384a3B683D930c05Ac646097b32Eb4C9f`.
- Deployment: `0x70201f30308bb9c40bab4318101031955bb536e529819b974496fd429f1a9405`.
- Register artifact: `0x215595cdfadeeb412f9b5cce75551d6b09059b0cf9ad1b558f89f61ffb1aadf6`.
- Add custody event: `0xc1f30523ae0cbed8d98f4253346a6613305b57fe09773cbf15024b98b6f4a8a6`.
- Submit provenance evidence: `0x24f2741a95ca7f2f5c69c97dc02db2ae887580d76f7874c786204be13f415b80`.
- Real-validator verification: `0xc841a8c5a4779a16ad3413220cb70a9e02cfe2b2243cdad566790db62c750cd4`.
- Final state: `INCONCLUSIVE`; validators independently retrieved the public source and evaluated the original provenance evidence without challenge evidence.
