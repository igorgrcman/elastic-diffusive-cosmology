# Phase 1 Integration Status — Book IV

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Epistemic consolidation after R4, R3, R1 completion

---

## Summary

Phase 1 partially closes three derivation routes in the metastable-lifetime
chain (σ → K_pin → S_E/ℏ → τ_n). The result τ_n ≈ 880 s is **assembled**,
not fully derived — it depends on one [P] hypothesis (L₀/δ = π²) and one
[Cal] prefactor (A ≈ 0.9).

---

## Route Outcomes

| Route | Target | Outcome | Status |
|-------|--------|---------|--------|
| **R4** | N_bonds = 3 | Local optimality on M₆ lattice | [Dc] |
| **R3** | V(q) from 5D | Geometric sector single-well [Dc]; full double-well [P] | Partial |
| **R1** | L₀/δ derivation | L₀/δ = F(η) continuous family [Dc\|model]; π² not uniquely selected | Partial |

---

## Epistemic Ledger (Metastable Sector)

| Claim | Tag | Chapter | Closure Gap |
|-------|-----|---------|-------------|
| κ = 2π | [Dc] | Ch.07 | None |
| V_geom(q) single-well | [Dc] | Ch.03, App.B | None |
| N_bonds = 3 local optimality | [Dc] | Ch.01, App.A | None |
| V(q) double-well structure | [P] | Ch.03 | Non-geometric terms not derived |
| V_B = 2 Δm_np | [P] | Ch.03 | E_arm ≡ Δm_np identification [OPEN] |
| L₀/δ = π² | [P] | Ch.08 | Candidate in continuous family |
| A ≈ 0.9 | [Cal] | Ch.09 | Fluctuation determinant [OPEN] |
| ω₀ = √(σ/m_p) | [P] | Ch.09 | Dimensional estimate only |
| S_E/ℏ = 2π³ | [Dc]×[P] | Ch.09 | Inherits [P] from L₀/δ |
| τ_n ≈ 880 s | [Dc]+[P]+[Cal] | Ch.09 | Two open steps |

---

## Open Problems (Ordered by Impact)

1. **L₀/δ from first principles** — Currently [P]. Model-dependent BVP
   (App. L₀/δ) shows F(η) is continuous; π² requires η ≈ 0.052, not
   naturally selected. Deriving η from 5D action would close the exponent.

2. **Full V(q) from S_5D** — Currently [P]. Geometric sector is [Dc], but
   non-geometric terms (V_node, V_bulk) needed for double-well are not derived.

3. **Prefactor A from fluctuation determinant** — Currently [Cal].
   Semiclassical formula A_sc = π(ω₀/ω_B)/√(L₀/δ) ≈ 0.84 exists [Der
   within 1D model], but gives τ_n ≈ 24,000 s with π², not 880 s.

4. **E_arm ≡ Δm_np identification** — Currently [OPEN]. Factor-of-2
   in V_B follows from Z₃ symmetry [Der], but the unit identification
   is a projection-level assumption.

5. **ω₀ from junction dynamics** — Currently [P] dimensional estimate.

---

## Files Modified in This Pass

| File | Changes |
|------|---------|
| `main.tex` | Preface: "derives" → "assembles"; added [P]+[Cal] caveat to τ_n item |
| `ch03_neutron_metastable.tex` | Abstract: added [BL] tag; preview: added [P]+[Cal] caveat; observerbox: softened "computed from"; summary: added partial-closure note |
| `ch06_instanton.tex` | Preview: added [P] emphasis + continuous-family note; forward ref: added [P]+[Cal] qualifiers |
| `ch09_tau_n_prediction.tex` | Summary: added contingency caveat; "Key insight": replaced "not from fitted parameters" with honest epistemic status; "Derivation chain complete" → "partially closed"; bridge: "now complete" → "partially closed" |

---

## What "Full Closure" Would Require

To upgrade τ_n from [Dc]+[P]+[Cal] to [Der]:
1. Derive η from 5D action → selects unique L₀/δ → removes [P]
2. Compute A from full 5D fluctuation determinant → removes [Cal]
3. Derive V(q) including non-geometric terms → upgrades double-well from [P] to [Dc] or [Der]

Until then, the <1% agreement with observation is **encouraging but not
independently confirmed** — it depends on parameter choices that are not
uniquely determined by the theory.
