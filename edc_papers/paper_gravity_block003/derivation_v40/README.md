# Derivation v40: Numerical ΔE_vac^finite Track Ranking

## Summary

Computes the finite part of vacuum energy for four GUT tracks using consistent
regularization protocols, producing a definitive ranking.

## Key Results

### Gauge-Only Ranking (Robust)
```
ΔE_vac(SU(5)) = ΔE_vac(PS) = ΔE_vac(E6) = 0 < ΔE_vac(SO(10)) = 3π/(4L)
```

### Track Comparison
| Track | dim(g) | n_NN | n_DD | n_mixed | ΔE_vac^gauge |
|-------|--------|------|------|---------|--------------|
| SU(5) | 24 | 12 | 12 | 0 | 0 |
| SO(10) | 45 | 12 | 29 | 4 | 3π/(4L) |
| PS | 21 | 12 | 9 | 0 | 0 |
| E_6 | 78 | 12 | 66 | 0 | 0 |

### Tiebreaker (for SU(5)/PS/E_6)
1. Symmetry: E_6 > PS > SU(5)
2. Simplicity: SU(5) > PS > E_6
3. Phenomenology: PS > SU(5) > E_6

Final selection: [OPEN] - requires experimental/theoretical input

## Verification

```bash
$ python3 recompute.py
# 17/17 CHECKS PASSED
```

Includes numerical computation of:
- Zeta-regularized Casimir energy per BC type
- Heat-kernel validation
- Track-by-track ΔE_vac computation
- Regulator invariance verification
- Convergence checks

## Build

```bash
$ pdflatex main.tex
$ pdflatex main.tex  # second pass for refs
# Output: 22 pages, 91 equations
```

## No Forbidden Inputs

This derivation contains NO forbidden numerical values:
- M_Z, M_W, v_EW, α_EM, G_N, ℓ_P

---
*Created: February 2026*
