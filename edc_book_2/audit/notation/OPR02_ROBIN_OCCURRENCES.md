# OPR-02: Robin BC Occurrences in Book 2

**OPR**: OPR-02 (Robin α from action)
**Date**: 2026-01-25
**Branch**: book2-opr02-robin-alpha-from-action-v1

---

## Summary

Robin boundary condition `f' + αf = 0` appears throughout Book 2 in the context of
the scalar mediator BVP (boundary value problem) for weak sector physics. This
document catalogs all occurrences and their equation labels for derivation tracing.

## Canonical Form

**Robin BC at brane (ξ = 0):**
```
∂f/∂ξ + α·f = 0
```
where:
- `f(ξ)` = scalar field profile in 5th dimension
- `α` = Robin parameter (dimensionless in ξ ∈ [0,1] convention)
- Sign: **outward normal derivative + αf = 0** (inward: f' = αf would have opposite sign)

---

## Equation Label Index

| Label | Location | Form | Status | Notes |
|-------|----------|------|--------|-------|
| `eq:ch11_robin_bc` | ch11_opr20_factor8_forensic.tex:104 | `f'(0) + a·ℓ·f(0) = 0` | Definition | Parametric (a,b coefficients) |
| `eq:ch11_B_robin` | ch11_opr20_attemptD.tex:199 | `∂_ξφ + αφ = 0` | [Dc] | From boundary action variation |
| `eq:attemptF_Robin` | ch11_opr20_attemptF.tex:142 | `∂_nφ + (λ̃p²/2)φ = 0` | [Dc] | From BKT action |
| `eq:attemptF_alpha_BKT` | ch11_opr20_attemptF.tex:148 | `α = λ̃x₁²/2` | [P] | BKT coefficient λ̃ postulated |
| `eq:attemptF_alpha_tension` | ch11_opr20_attemptF.tex:159 | `α ~ κ₅²σℓ` | [P] | Tension-dominated case |
| `eq:attemptG_robin_dimensionless` | ch11_opr20_attemptG.tex:27 | `df/dξ + α·f = 0` | Definition | Dimensionless ξ ∈ [0,1] |
| `eq:attemptG_alpha_thick` | ch11_opr20_attemptG.tex:125 | `α_phys ~ C_geom/δ` | [Dc] | Thick-brane matching |
| `eq:attemptG_alpha_thick_dimensionless` | ch11_opr20_attemptG.tex:132 | `α = C_geom·ℓ/δ` | [Dc]+[P] | With δ = R_ξ postulated |
| `eq:attemptG_BC_robin_eigenvalue` | ch11_opr20_attemptG_BC.tex:123 | `tan(x) = 2αx/(x²−α²)` | [Dc] | Symmetric Robin eigenvalue eq |
| `eq:attemptH_robin_from_action` | ch11_opr20_attemptH.tex:73 | `∂_ξφ(0) + αφ(0) = 0` | [Dc] | From action variation |
| `eq:bvp:robin_bc` | ch14_bvp_closure_pack.tex:180 | Generic Robin form | Definition | BVP chapter |

---

## Chapter Locations

### Chapter 10 (Electroweak Bridge)
- **sec:ch10_opr20b** (§11.1.3): OPR-20b Summary
- First introduces Robin as BC interpolating Dirichlet ↔ Neumann
- Key equations: Robin eigenvalue equation for KK modes

### Chapter 11 (OPR-20 Attempts C–G)
- **sec:ch11_attemptD_B**: Part B — Robin from junction physics
- **sec:attemptF_junction_robin**: F3 — Junction → Robin derivation [Dc]
- **sec:attemptG_BC_robin**: G_BC.3 — Robin limiting cases
- **sec:ch11_opr20_attemptG**: Derive α from EDC brane physics

### Chapter 13 (Attempts H, H2)
- **sec:attemptH2_routeB**: H2.4 — Route B: Junction → Robin → Scale ID
- **sec:H2hard_routeB**: Route B: Junction/Variation → Robin → δ

### Chapter 14 (BVP Closure)
- General Robin BC treatment in BVP framework

---

## Sign Convention Audit

**All occurrences use CONSISTENT sign:**
- `f' + αf = 0` (outward derivative + positive α·f = 0)
- Equivalent: `f'(0) = −αf(0)` (derivative is proportional to −α times value)
- For α > 0: field derivative is opposite sign to field value at boundary

**Limiting cases (consistent across all files):**
- α → 0: Neumann BC (f' = 0)
- α → ∞: Dirichlet BC (f = 0)
- α = 2π: Natural value from δ = R_ξ identification

---

## Current Status per Attempt

| Attempt | Route | α derivation | Status |
|---------|-------|--------------|--------|
| D | Boundary action | Structure only | [Dc] |
| F | BKT + junction | α = λ̃x₁²/2 | [Dc]+[P] (λ̃ free) |
| G | Thick-brane | α = ℓ/δ | [Dc]+[P] (δ = R_ξ free) |
| H | Variation | Structure | [Dc] |
| H2 | Route B | α ~ ℓ/δ | [Dc]+[P] |

**Verdict**: Robin BC *form* is [Dc]; Robin parameter *value* requires one [P]:
either λ̃ (BKT coefficient) or δ = R_ξ (brane thickness identification).

---

## Files Referenced

```
src/sections/ch10_electroweak_bridge.tex
src/sections/ch11_opr20_factor8_forensic.tex
src/sections/ch11_opr20_attemptD_interpretation_robin_overcount.tex
src/sections/ch11_opr20_attemptF_mediator_bvp_junction.tex
src/sections/ch11_opr20_attemptG_BC_provenance.tex
src/sections/ch11_opr20_attemptG_derive_alpha_from_action.tex
src/sections/ch11_opr20_attemptH_delta_equals_Rxi.tex
src/sections/ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex
src/sections/ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex
src/sections/ch14_bvp_closure_pack.tex
```

---

*OPR-02 Step 1 Complete*
