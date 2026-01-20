# Symmetry Layering and Defect Operations

**Companion E**

DOI: [10.5281/zenodo.18300199](https://doi.org/10.5281/zenodo.18300199)

---

## Description

Technical note on symmetry layering and defect operations in the EDC framework. Documents:
- Symmetry group structure
- Defect classification
- Process algebra for particle transitions
- Beta decay as symmetry operation

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

- `bib/references.bib` — bibliography
- `sections/` — modular section files
- `appendices/` — appendix files

---

## Author

Igor Grcman
