# Derivation of the Effective Lagrangian from the 5D Einstein-Hilbert Action

**Companion A**


---

## Description

Technical note deriving the effective Lagrangian L_eff[q] from the 5D Einstein-Hilbert action. Shows how the kinetic term M(q) and potential V(q) emerge from bulk and brane contributions.

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

- `bib/refs_Leff.bib` — bibliography

---

## Author

Igor Grcman
