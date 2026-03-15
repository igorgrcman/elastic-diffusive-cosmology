# Derivation v39: BC Selector Applied to GUT Survivor Map

## Summary

This derivation operationally connects:
- **v37**: BC selection pipeline (ΔE_vac^finite scoring)
- **v35**: GUT BC survivor map (parity → zero-mode rule)
- **v34**: G_F from KK exchange formula
- **v36**: g_5 tracks (dimensional normalization)

## Key Results

1. **BC Candidate Class**: Discrete space B_G for each GUT track
2. **Scoring Function**: ΔE_vac^finite(C) - ΔE_vac^finite(C_ref) = S[C]
3. **Selection Results**: Standard BC giving 12 SM survivors per track
4. **G_F Hook**: Charged tower formula G_F/√2 = Σ(g_4^(n))²/(8m_n²)
5. **Free Knobs Catalog**: β, λ, track coefficients (c_A, c_B, c_C)

## GUT Tracks Covered

| Track | Parent Group | Dim | Rank | Survivors |
|-------|--------------|-----|------|-----------|
| SU(5) | SU(5) | 24 | 4 | 12 |
| SO(10) | SO(10) | 45 | 5→4 | 12 |
| Pati-Salam | SU(4)×SU(2)_L×SU(2)_R | 21 | 5→4 | 12 |
| E_6 | E_6 | 78 | 6→4 | 12 |

## Verification

```bash
$ python3 recompute.py
# 15/15 CHECKS PASSED
```

## Build

```bash
$ pdflatex main.tex
$ pdflatex main.tex  # second pass for refs
# Output: 23 pages, 93 equations
```

## Files

- `main.tex` — LaTeX source
- `main.pdf` — Compiled document
- `recompute.py` — Verification script (15 checks)
- `README.md` — This file
- `REPORT.md` — Detailed inputs/outputs
- `ACCEPTANCE.md` — Acceptance criteria verification

## No Forbidden Inputs

This derivation contains NO forbidden numerical values:
- M_Z, M_W, v_EW, α_EM, G_N, ℓ_P

---
*Created: February 2026*
