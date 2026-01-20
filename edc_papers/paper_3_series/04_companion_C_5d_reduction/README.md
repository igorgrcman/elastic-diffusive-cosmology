# 5D Action Reduction Pipeline

**Companion C**

DOI: [10.5281/zenodo.18299751](https://doi.org/10.5281/zenodo.18299751)

---

## Description

Technical note documenting the 5D to 4D action reduction pipeline. Shows the Kaluza-Klein reduction and how effective 4D physics emerges from the 5D brane-world setup.

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

- `bib/refs_5d.bib` — bibliography

---

## Author

Igor Grcman
