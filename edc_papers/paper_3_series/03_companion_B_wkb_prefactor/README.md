# WKB Prefactor and Neutron Lifetime Calculation

**Companion B**


---

## Description

Technical note deriving the WKB prefactor A_0 for the neutron decay rate calculation. Includes:
- Determinant ratio R_det computation
- Gaussian integral evaluation for M(q), V(q)
- Sensitivity analysis

---

## Build

```bash
cd paper/
cp ../bib/*.bib .
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

---

## Dependencies

- `bib/refs_wkb.bib` — bibliography

---

## Reproducibility Code

See `../../code/companion_B_wkb/`:
- `gaussian_step9.py` — Gaussian integral evaluation
- `compute_Rdet_v2.py` — R_det calculation

---

## Author

Igor Grcman
