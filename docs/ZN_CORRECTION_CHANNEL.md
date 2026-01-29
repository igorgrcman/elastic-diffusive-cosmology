# Z_N Correction Channel — Prediction Fork

**Date:** 2026-01-29
**Status:** Generalization of Z₆ discrete averaging
**Source:** `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`

---

## A. Executive Summary (5 Bullets)

1. **Generalized result:** k(N) = 1 + 1/N for any cyclic group Z_N [Der]+[Dc]
2. **Mathematical part [Der]:** R_N = 1 + a/c for f(θ) = c + a cos(Nθ)
3. **Physical part [Dc]:** Equal corner share normalization a/c = 1/N (hypothesis)
4. **Z₆ recovery:** N = 6 → k = 7/6, matching pion observation (0.07%)
5. **Falsification:** If different sectors prefer different N, Z₆ universality fails

---

## B. Channel Definition

### B.1 Mathematical Component [Der]

For test function f(θ) = c + a cos(Nθ):
```
Discrete average:  <f>_disc = c + a  (samples at cos = 1)
Continuum average: <f>_cont = c      (cos integrates to 0)
Ratio: R_N = 1 + a/c
```

### B.2 Physical Component [Dc]

**Equal Corner Share Hypothesis:**
```
a/c = 1/N
```

**Interpretation:** Z_N anisotropy has amplitude equal to 1/N of the mean — each corner's "excess" is 1/N.

### B.3 Combined Result [Der]+[Dc]

```
k(N) = 1 + 1/N
```

---

## C. Prediction Fork Table

| N | k(N) | Fraction | Group | EDC Quantities Affected |
|---|------|----------|-------|-------------------------|
| 3 | 4/3 = 1.333 | Z₃ | Flavor/generations | N_g counting, CKM phases? |
| 4 | 5/4 = 1.250 | Z₄ | Dirac components | Spinor sums, 4α terms? |
| 5 | 6/5 = 1.200 | Z₅ | (not in EDC) | — |
| **6** | **7/6 = 1.167** | **Z₆** | **Ring structure** | **Δm_np, pion, N_cell** |
| 8 | 9/8 = 1.125 | Z₈ | Octonions? | — |
| 12 | 13/12 = 1.083 | Z₁₂ | HCP, 2×Z₆ | N_cell = 12 corrections? |

### C.1 Fork: Which N Governs Each Sector?

| Sector | Observed Pattern | Implied N | k(N) |
|--------|------------------|-----------|------|
| Pion splitting | r_π/(4α) = 1.166 | N = 6 | 7/6 ✓ |
| N_cell bridge | 12/10 = 1.20 | N = 5? | 6/5 ✗ |
| N_cell bridge | 12 × (6/7) = 10.3 | N = 6 | 7/6 ~ ✓ |
| Δm_np ε-dressing | ε = 0.679% | TBD | TBD |

### C.2 Implication for Δm_np

The ε = 0.679% connects bare (8/π) and dressed (5/2+4α) models:
```
(8/π)(1 - ε) = 5/2 + 4α
```

**If ε carries a k(N) factor:**
```
ε_eff = ε_bare × k(N)

For N = 6: ε_eff = ε_bare × (7/6)
→ ε_bare = ε × (6/7) = 0.679% × 0.857 = 0.582%
```

**Test:** Does 0.582% have a cleaner form than 0.679%?
- 0.582% ≈ 4α/5 = 0.584% (0.3% match!)
- Suggests: ε_bare = 4α/5, ε_dressed = (4α/5) × (7/6) = 14α/15 ≈ 0.68%

### C.3 Implication for N_cell

The N_cell = 12 vs 10 tension:
```
E_σ = 70 MeV = N_cell × (σr_e²)_Z6 = N_cell × 5.856 MeV
→ N_cell = 70/5.856 = 11.96 ≈ 12
```

But τ_n calculation uses N_cell = 10. If k(6) = 7/6 applies:
```
N_cell_eff = 12 / k(6) = 12 × (6/7) = 10.29 ≈ 10 ✓
```

**Interpretation:** The "bare" cell count is 12; discrete averaging correction gives effective count ~10.

---

## D. Falsification Criteria

### D.1 Universality Test

**Hypothesis:** All Z₆-symmetric EDC quantities carry k(6) = 7/6.

**Falsification:** If any sector requires k ≠ 7/6 (equivalently, N ≠ 6) for the same discrete-averaging mechanism, Z₆ universality fails.

### D.2 Specific Failure Modes

| Mode | Criterion | Status |
|------|-----------|--------|
| Wrong N | Sector needs N = 3 or N = 12 instead of 6 | Open |
| Sign flip | Sector needs (1 - 1/N) instead of (1 + 1/N) | Not observed |
| No pattern | Corrections appear random | Not observed |

### D.3 Critical Test: Δm_np

If Δm_np ε-dressing uses N = 6:
```
ε = (4α/5) × (7/6) = 14α/15 ≈ 0.68%
```

If Δm_np ε-dressing uses N = 4 (Dirac):
```
ε = (4α/5) × (5/4) = α ≈ 0.73%
```

Observed: ε = 0.679%. Closer to N = 6 prediction. **Supports Z₆ universality.**

---

## E. Summary

| Component | Status | Note |
|-----------|--------|------|
| k(N) = 1 + 1/N formula | [Der] | Mathematical derivation |
| Equal corner share (a/c = 1/N) | [Dc] | Physical hypothesis |
| Pion match (N = 6) | [I] | 0.07% agreement |
| N_cell explanation | [Dc] | 12 × (6/7) ≈ 10 |
| Δm_np ε-dressing | [P] | Candidate: ε = 14α/15 |

---

## F. Reference Anchors

| Document | Content |
|----------|---------|
| `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex` | General Z_N lemma |
| `edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex` | Z₆ specialization |
| `docs/Z6_CORRECTION_FACTOR_7over6.md` | Original hypothesis note |
| `docs/PION_SPLITTING_EPSILON_CHECK.md` | Pion observation |
| `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md` | N_cell = 12 vs 10 |
| `docs/DELTA_MNP_RECONCILIATION.md` | ε = 0.679% bridge |

---

*This document generalizes the Z₆ discrete averaging correction to Z_N and establishes a prediction fork for testing universality.*
