# Selection Rules for Neutron Beta Decay

**Companion D**

DOI: [10.5281/zenodo.18299855](https://doi.org/10.5281/zenodo.18299855)

---

## Description

Technical note deriving selection rules for neutron beta decay from defect topology. Shows how decay channels are constrained by the topological structure of brane junctions.

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

- `bib/refs_topology_note.bib` — bibliography

---

## Author

Igor Grcman
