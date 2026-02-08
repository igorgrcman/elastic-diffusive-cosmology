# ADDENDUM: V(r) Derivation from Thick-Brane BC — CORRECTED

**Date:** 2026-01-26
**Purpose:** Corrected update to M5_TO_Z6_PROOF.md based on rigorous re-analysis

---

## STATUS UPDATE (CORRECTED)

The original derivation attempt (`DERIVATION_V_r_FROM_BC.md`) contained an ERROR.

**The error:** Claimed that "BC force a minimum of V(d)" but the linearized potential (log + K₀ series) is **strictly monotonically increasing** for same-sign vortices. See `aside_p2_closure_v3/01_SIGN_AND_MONOTONICITY.md` for proof.

**Corrected analysis:** The minimum exists NOT from BC, but from:
1. Core overlap repulsion (topology + gradient energy) → V → +∞ as d → 0
2. Logarithmic growth → V → +∞ as d → ∞
3. Continuity → minimum at some d₀

See `aside_p2_closure_v3/` for complete rigorous analysis.

---

## CORRECTED RESULT

| Component of P2 | Original Claim | Corrected Status |
|-----------------|----------------|------------------|
| Defects exist | [P] | [P] (still requires field content) |
| V → +∞ as d → 0 | Claimed [Der] from BC | **[Der] from TOPOLOGY** (core overlap) |
| V → +∞ as d → ∞ | Not stated | **[Dc] from logarithmic growth** |
| "Attraction" at intermediate r | Claimed [Der] from BC | **WRONG** — (log + K₀) is monotone increasing |
| Minimum exists | Claimed [Der] from BC | **[Dc] from continuity** (Theorem 3) |
| Minimum at d₀ ~ δ | Claimed [Der] | **[OPEN]** — requires calculation |

---

## KEY CORRECTIONS

### Correction 1: BC Do NOT Create Attraction

The K₀ series contributes to the potential:
```
V_K(d) = -(2/π) n₁n₂ Σₘ (1/m²) K₀(mπd/δ)
```

For same-sign vortices: V_K < 0 (negative value).

BUT the FORCE is:
```
F_K = -dV_K/dd = +(2/δ) n₁n₂ Σₘ (1/m) K₁(mπd/δ) > 0
```

**Positive force = REPULSION.** The BC terms contribute to repulsion, not attraction.

### Correction 2: Minimum Comes from Topology, Not BC

The minimum exists because:
1. **Core overlap** (from winding number topology): V → +∞ as d → 0
2. **Logarithmic confinement** (from 2D geometry): V → +∞ as d → ∞
3. **Continuity**: minimum at interior point

BC provide the scale δ, but NOT the mechanism for the minimum.

### Correction 3: Location d₀ ~ δ Is NOT Derived

The derivation shows d₀ exists with a < d₀ < O(δ).

The specific claim d₀ ~ δ requires numerical calculation in the crossover regime.

---

## REVISED DERIVATION CHAIN

**Corrected chain:**
```
[P] A1-A4 (5D bulk + membrane + compact dim + tension)
      ↓
[P] A5: Complex scalar field Φ with U(1) symmetry
      ↓
[Dc] Topological defects (vortices) exist [from π₁(U(1)) = ℤ]
      ↓
[Der] V(d) → +∞ as d → 0 [from core overlap, Theorem 2]
      ↓
[P] Thick-brane BC (Neumann/Robin) [from Israel junction]
      ↓
[Dc] V(d) → +∞ as d → ∞ [from logarithmic growth]
      ↓
[Dc] Minimum exists at some d₀ [from continuity, Theorem 3]
      ↓
[P] d₀ ~ δ [NOT derived — postulated or calculated]
      ↓
[M] T2 (Kepler-Hales packing)
      ↓
[Dc] L1 (Hexagonal ground state)
      ↓
[Dc] L2 (Z6 emergence)
```

---

## REMAINING GAP

The derivation of "d₀ ~ δ" remains OPEN.

To close this gap would require:
1. Explicit calculation of V(d) in the crossover regime a < d < δ
2. Solving for V'(d₀) = 0 numerically or analytically
3. Verifying V''(d₀) > 0 (stability)

Without this, the claim "minimum at brane-thickness scale" remains [P] or [Cal].

---

## UPDATED HONEST CLAIM

> "Given a thick brane with complex scalar field (A5), topological defects exist [Dc] with interaction potential V(d). By core overlap [Der] and logarithmic growth [Dc], the potential diverges at d → 0 and d → ∞. By continuity, a minimum exists at some d₀ ∈ (a, O(δ)) [Dc]. The specific location d₀ ~ δ is postulated [P]. Combined with Kepler-Hales [M], this gives hexagonal packing and Z6 symmetry [Dc]."

---

## REFERENCES

- `aside_p2_closure_v3/01_SIGN_AND_MONOTONICITY.md` — Proof that (log + K₀) is monotone
- `aside_p2_closure_v3/02_CORE_REPULSION_FROM_FUNCTIONAL.md` — Derivation of core divergence
- `aside_p2_closure_v3/03_EXISTENCE_OF_MINIMUM_THEOREM.md` — Theorem on minimum existence
- `aside_p2_closure_v3/04_WHAT_BC_ACTUALLY_BUY_YOU.md` — Honest accounting of BC role
- `aside_p2_closure_v3/05_VERDICT.txt` — Summary verdict
