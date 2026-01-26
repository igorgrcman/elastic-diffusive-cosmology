# OPR-21R: μ₃ Shape Dependence Comparison

## Executive Summary

**FINDING**: The three-generation condition N_bound = 3 is achieved at:
- **Toy (Pöschl-Teller)**: μ₃ ≈ 15.0
- **Physical (Domain Wall)**: μ₃ ≈ 13.0

**IMPLICATION**: The oft-cited "[25, 35)" window is specific to the toy potential.
It should NOT be quoted as a universal requirement for three generations.

---

## Correct Statement

> "For a given potential family V(ξ) and BC parameters κ, there exists a
> shape-dependent critical value μ₃(V, κ, ρ) such that N_bound = 3."

**Toy benchmark**: μ₃(PT) ≈ 15.0 (Pöschl-Teller)
**Physical result**: μ₃(DW) ≈ 13.0 (Domain Wall from 5D Dirac)

---

## What to Update in the Book

Replace statements like:
> "N_bound = 3 for μ ∈ [25, 35)"

With:
> "N_bound = 3 for μ ∈ [μ₃⁻(V), μ₃⁺(V)] where the window depends on V(ξ).
> For toy Pöschl-Teller: [25, 35). For physical domain wall: μ ≈ 13.0."

---

## Epistemic Status

| Item | Status |
|------|--------|
| μ₃ is shape-dependent | [Dc] DERIVED |
| Toy benchmark [25,35) | [M] MATHEMATICAL (toy limit) |
| Physical μ₃ ≈ 13.0 | [Dc] CONDITIONAL |
| Parameter values (ρ, κ, ℓ) | [P] POSTULATED |

---

*Generated: 2026-01-25T23:01:28.622288*
*Sprint: OPR-21R*
