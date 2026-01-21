# Selection Rules for Neutron Beta Decay

**Companion D**


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
