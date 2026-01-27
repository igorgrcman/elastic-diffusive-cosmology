# Route D: 2D Bounce in (q, Δ) Configuration Space

**Date:** 2026-01-27
**Status:** [NO-GO] for minimal 2D coupled-mode tunneling
**Code:** `derivations/code/routeD_2D_bounce.py`
**Artifacts:** `derivations/artifacts/routeD_results.{json,csv}`

---

## 1. Executive Summary

Route D tests whether the Z₃ doublet asymmetry coordinate Δ provides an alternative
tunneling channel that could enhance the bounce action B/ℏ from ~0.01 to ~60.

**Key Result:**

| Quantity | Value | Status |
|----------|-------|--------|
| B₁D/ℏ | 0.00895 | [Dc] from Route C |
| B₂D/ℏ | 0.00895 | [Dc]/[P] this work |
| B₂D/B₁D | 1.0000 | [Dc] |
| Required | 60.7 | [BL] for τ_n = 879 s |
| Decision | **NO-GO** | [NO-GO] |

**Critical Finding:**
The 2D channel does NOT provide additional suppression. The optimal tunneling path
stays at Δ = 0 throughout. No shortcut through Δ ≠ 0 exists.

---

## 2. Model Definition [Dc]/[P]

### 2.1 Coordinates

- **q ≥ 0:** Node depth into bulk (existing collective coordinate)
- **Δ:** Z₃ doublet asymmetry ("which leg is special")
  - Δ = 0 is the Z₃-symmetric point
  - |Δ| measures departure from equal arm lengths

### 2.2 Z₃ Symmetry Constraints [M]

The Z₃ group acts by cyclic permutation of the three junction arms.
This constrains the potential to even powers of Δ:

```
V(q, Δ) = V₀(q) + ½ a(q) Δ² + ¼ b(q) Δ⁴ + O(Δ⁶)
```

**Why no odd powers:**
- Z₃ symmetry: Δ → ωΔ where ω = e^(2πi/3)
- Only |Δ|² is invariant under this transformation
- Combined with reflection symmetry Δ → −Δ, only even powers survive

### 2.3 Potential and Mass Matrix

**Potential [Dc]/[P]:**
```
V(q, Δ) = V₀(q) + ½ a(q) Δ² + ¼ b(q) Δ⁴
```

where:
- V₀(q) = V_NG(q) + V_core(q) [Dc] from Route C
- a(q) = a_coeff × σ × δ × (1 + 0.5(q/δ)²) [P]
- b(q) = b_coeff × σ × (δ/L₀) [P]

**Mass matrix [Dc]/[P]:**
```
G = [[M_qq(q),  0      ],
     [0,        M_ΔΔ(q)]]
```

where:
- M_qq(q) = M(q) [Dc] from Route C
- M_qΔ(q) = 0 [P] (no cross-coupling in first approximation)
- M_ΔΔ(q) = μ_Δ × τ_eff / (1 + (q/δ)²) [P]

---

## 3. Acceptance Criteria Results

### AC-D7: Model Sanity ✓

```
V(q_n, 0) = 47.439 MeV
V_1D(q_n) = 47.439 MeV
Relative difference: < 10⁻⁶
```
**Status: PASS**

### AC-D8: Z₃ Invariants ✓

Documented in Section 2.2. Only Δ², Δ⁴ terms present.
**Status: DOCUMENTED**

### AC-D9: No Partner Contradiction ✓

```
a(q_n) = 7.02 MeV/fm² > 0
```

The doublet mode is stable at q = q_n. No low-lying partners.
**Status: PASS**

### AC-D10: Numerical Convergence ✓

| N points | B₂D/ℏ | Converged |
|----------|-------|-----------|
| 25 | 0.00894 | Yes |
| 50 | 0.00895 | Yes |
| 100 | 0.00895 | Yes |
| 200 | 0.00895 | Yes |

Relative difference (last two): < 10⁻⁵
**Status: PASS (<1%)**

### AC-D11: Benchmark Comparison ✓

┌───────────────────────────────────────────────────────┐
│           BOUNCE ACTION COMPARISON TABLE              │
├───────────────────────────────────────────────────────┤
│  B₁D/ℏ (Route C)    =       0.008945                  │
│  B₂D/ℏ (Route D)    =       0.008945                  │
│  Required for τ_n   =           60.7                  │
├───────────────────────────────────────────────────────┤
│  B₂D / B₁D          =         1.0000                  │
│  B₂D / B_required   =       0.000147                  │
│  Deficit            =           60.7                  │
└───────────────────────────────────────────────────────┘

**Status: PRINTED**

### AC-D12: Decision Outcome

**DECISION: NO-GO [NO-GO]**

The 2D coupled-mode tunneling with minimal Z₃ coupling does NOT achieve B/ℏ ≳ 60.
- Best achieved: B/ℏ = 0.00895
- Required multiplier: ~6800×
- The Δ direction does not provide a shorter tunneling path.

---

## 4. Physical Analysis

### 4.1 Why Does 2D Not Help?

The 2D bounce B₂D ≈ B₁D because:

1. **The optimal path stays at Δ = 0 [Dc]**
   - No shortcut through Δ ≠ 0 region exists
   - The potential V(q, Δ) increases with |Δ|
   - Detour into Δ ≠ 0 adds both path length AND barrier height

2. **For Δ ≠ 0 to help, we would need [M]:**
   - A saddle point at (q*, Δ* ≠ 0) with V(q*, Δ*) < V(q_B, 0)
   - But Z₃ symmetry + a(q) > 0 prevents this
   - The barrier is LOWEST at Δ = 0

3. **The Δ mode adds stiffness but no new escape route [Dc]**
   - M_ΔΔ > 0 means Δ motion has inertia
   - a(q) > 0 means Δ = 0 is stable throughout
   - The 1D picture (Δ = 0) is already optimal

### 4.2 Mathematical Proof Sketch

**Claim:** If a(q) > 0 for all q ∈ [q_B, q_n], then the minimum action path
has Δ(s) = 0 for all s.

**Proof sketch:**
- Consider any path (q(s), Δ(s)) from well to barrier
- The action is S_E = ∫ ds √(2V × |dx|²_G)
- At each point, V(q, Δ) ≥ V(q, 0) because a(q) > 0
- At each point, |dx|²_G = M_qq dq² + M_ΔΔ dΔ² ≥ M_qq dq²
- Therefore any detour into Δ ≠ 0 increases both V and |dx|
- The minimum is achieved by Δ = 0 throughout ∎

---

## 5. Parameter Scan Summary

Scanned:
- a_coeff ∈ {0.1, 0.5, 1.0, 2.0, 5.0, 10.0}
- b_coeff ∈ {0.1, 1.0, 10.0}
- μ_Δ ∈ {0.1, 0.5, 1.0, 2.0, 5.0}

Total configurations: 90

**Results:**
- All configurations with a(q_n) > 0 give B₂D ≈ B₁D
- Configurations with a(q_n) < 0 are rejected (violate AC-D9)
- Maximum B₂D/ℏ achieved: 0.00895 (same as 1D)

---

## 6. Epistemic Status Map

| Claim | Status | Justification |
|-------|--------|---------------|
| V(q, Δ) functional form | [Dc]/[P] | Z₃ symmetry constrains to Δ², Δ⁴ |
| a(q), b(q) profiles | [P] | Phenomenological; provenance: σ, δ |
| M_ΔΔ profile | [P] | Dimensional closure via τ_eff |
| B₂D ≈ B₁D | [Dc] | Computed; path optimization shows Δ=0 optimal |
| No-shortcut theorem | [M] | Follows from a(q) > 0 and convexity |
| **Decision: NO-GO** | **[NO-GO]** | Minimal 2D (q, Δ) channel insufficient |

---

## 7. Conclusions

1. **Route D tested the minimal 2D extension** [Dc]/[P]
   Adding the Z₃ doublet coordinate Δ with stability constraint a(q) > 0.

2. **The 2D bounce equals the 1D bounce** [Dc]
   B₂D/B₁D = 1.0000 — no enhancement from the second dimension.

3. **Physical reason: no shortcut exists** [M]
   V(q, Δ) increases monotonically with |Δ|, so tunneling prefers Δ = 0.

4. **Status: [NO-GO] for minimal 2D (q, Δ) coupling**
   The doublet mode cannot provide the missing 6800× factor.

5. **OPEN: Alternative mechanisms needed**
   - 3D modes (all three leg lengths independent)
   - Angular modes (junction orientation in the brane)
   - Bulk field coupling providing negative contribution
   - Non-WKB quantum effects (instantons, domain walls)
   - Different topological transition entirely

---

## 8. Artifacts

- `derivations/code/routeD_2D_bounce.py` — computation script
- `derivations/artifacts/routeD_results.json` — full results
- `derivations/artifacts/routeD_results.csv` — summary table
- `derivations/figures/routeD_2D_bounce.png` — contour plot with path
- `derivations/figures/routeD_comparison.png` — B comparison

---

## 9. Version History

- 2026-01-27: Initial execution and NO-GO determination

---

## 10. References

**Internal:**
- `derivations/TASK_D_CANONICAL_BOUNCE_REPORT.md` — 1D bounce audit (Route C)
- `derivations/Z3_SYMMETRY_ANALYSIS_NEUTRON.md` — Z₃ symmetry framework
- `derivations/S5D_TO_SEFF_Q_REDUCTION.md` — Route C corridor

**External:**
- Coleman, S. "The Fate of the False Vacuum" (1977) — WKB instanton methods
