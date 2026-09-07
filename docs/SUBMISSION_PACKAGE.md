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
- Contract: `0x543B988Bd0b031aCa0d42c326DBCB65856d2eC2c`.
- Deployment: `0x81d94b104c0668b8a7f97cef66155f4123a61583e31bc8fd8a75d9009ff5929b`.
- Register artifact: `0x13a252cd806cb6602ec68aa426259b2f2f363ece8c88e34190c006ce9f9e8811`.
- Add custody event: `0xc1f30523ae0cbed8d98f4253346a6613305b57fe09773cbf15024b98b6f4a8a6`.
- Submit provenance evidence: `0x6c470c4fffb7550fbf13c2a96f996e547563dc3225cbf3cfcee2c701c3f6fabf`.
- Real-validator verification: `0x0237b6dde97f0027252a6a7698a66c7a155b9c6820145dd3c58846e45709b619`.
- Final state: `INCONCLUSIVE`; one custody event and one evidence record. Validators independently retrieved `https://genlayer.com/` and refused unsupported artifact and origin claims.
