# Elastic Diffusive Cosmology — Book Source

Canonical repository for the EDC book LaTeX sources, standards, and patches.

## Links
- **Book DOI:** https://doi.org/10.5281/zenodo.18176174
- **Repository:** https://github.com/igorgrcman/elastic-diffusive-cosmology

## Build (local)
```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

## Structure
- `frontmatter/` — DOI page, preface, methodology note
- `chapters/` — chapters (as included by `main.tex`)
- `appendices/` — appendices and glossary
- `standards/` — rigor/epistemic standard docs
- `patches/` — diffs and patch logs
