# Symmetry Layering and Defect Operations

**Companion E**


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
