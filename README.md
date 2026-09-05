# UCHES — Authenticity Chain Escrow

UCHES is a standalone GenLayer Intelligent Contract primitive for releasing authenticity funding only when validator consensus confirms that submitted evidence supports provenance, identity, and chain-of-custody claims. Sponsors fund an authenticity commitment, providers submit bounded evidence, and validators independently assess the result.

## Live deployment

- Network: GenLayer StudioNet
- Chain ID: `61999`
- Contract: `0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073`
- [Open UCHES in Studio Explorer](https://explorer-studio.genlayer.com/address/0xF8BDAE4d4966bB93A0Da6F529984C3c4915A9073)
- Deployment transaction: `0xaacae5c3e84377ff2e69d9906f547d4ea49e1514cbfa1902555a82a1cfc00c94`

Live verification: a real-validator resolve correctly returned `INCONCLUSIVE` for self-asserted authenticity evidence, leaving the escrow protected and unsettled.

The exact source in `contracts/aase.py` was deployed successfully to StudioNet. The deployment transaction was accepted with a one-round majority consensus result and five revealed validator votes.

Validators independently acquire public evidence, attach visual evidence to vision-capable model calls, and return a structured verdict. Deterministic contract code handles the state machine, weighted deliverables, partial payout calculation, timeout recovery, bonds, fees, cancellation, callbacks, bilateral settlement, and zero-before-transfer escrow safety.

UCHES is reusable for digital goods, certificates, media provenance, supply-chain records, collectibles, and creator royalties. It is intentionally contract-only: downstream applications can consume its machine-readable verdict and payout state without trusting a backend operator.

## Interface

- `create_service_intent(...)` — create and fund an agent service intent.
- `add_agent_bond(...)` — post an optional agent bond.
- `submit_agent_evidence(...)` — submit bounded work evidence.
- `resolve(...)` — run validator consensus and settle.
- `timeout_refund(...)`, `cancel_before_evidence(...)` — recovery paths.
- `accept_mutual_agent_settlement(...)` — bilateral split after inconclusive review.

## Documentation basis

https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle

https://docs.genlayer.com/developers/intelligent-contracts/features/web-access

https://docs.genlayer.com/developers/intelligent-contracts/features/image-processing

https://skills.genlayer.com/
