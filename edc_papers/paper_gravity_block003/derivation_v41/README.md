# Derivation v41 — Matter-Augmented ΔE_vac^finite Ranking

## Purpose

Break the SU(5)/PS/E₆ tie from v40 by including fermion contributions with chiral boundary conditions.

## Key Result

**Unique ranking (tie fully broken):**

```
E₆ < PS < SU(5) < SO(10)
```

Numerical values (units of π/L):
- E₆: -2.25
- PS: -0.375
- SU(5): 0
- SO(10): +0.5625

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (28 pages, 152 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (23/23 checks) |
| `EDC_BLOCK003_DERIVATION_V41_MATTER_AUGMENTED_DELTA_EVAC_RANKING.pdf` | Canonical export |

## Dependencies

- **v33**: Chiral BC for 5D fermions
- **v37**: ΔE_vac^finite subtraction protocol
- **v39**: GUT track BC patterns
- **v40**: Gauge-only ranking (baseline)

## Key Physics

1. **Fermion spin-statistics**: χ_F = -χ_B (opposite to bosons)
2. **Chiral BC coefficients**:
   - χ_F(L,L) = χ_F(R,R) = +1
   - χ_F(L,R) = χ_F(R,L) = -1/2
3. **Exotic fermions get mixed BCs**: No zero-modes for GUT-broken partners

## Why E₆ Wins

E₆ has the most exotic fermions (36 with mixed BC), contributing the largest negative ΔE_ferm.

## Build

```bash
pdflatex main.tex
python3 recompute.py
```

## Acceptance

All AC-P41 criteria met. See ACCEPTANCE.md for details.

---
*Created: 2026-02-04*
