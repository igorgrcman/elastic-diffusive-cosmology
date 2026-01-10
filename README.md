# Elastic Diffusive Cosmology (EDC)

This repository contains:

1) **The EDC book source (LaTeX)** — canonical book sources, standards, and patches  
2) **The EDC Python toolkit** — runnable scripts + a small library + tests for visualizations and sanity checks (with explicit epistemic labeling where relevant)

## Links
- **Book DOI (Zenodo):** https://doi.org/10.5281/zenodo.18176174
- **Repository:** https://github.com/igorgrcman/elastic-diffusive-cosmology
- **How to cite:** see `CITATION.cff`

---

## Repository layout

- `edc_book/` — **LaTeX book sources**
  - `edc_book/main.tex` is the main entrypoint
  - `edc_book/chapters/`, `edc_book/frontmatter/`, `edc_book/appendices/`
  - `edc_book/standards/` and `edc_book/patches/` (rigor + change tracking)
- `code/` — **Python toolkit**
  - `code/src/edc/` — importable library modules (constants, epistemic helpers, physics helpers)
  - `code/scripts/` — runnable scripts (including `experimentals/`)
  - `code/tests/` — unit tests (use `python -m pytest`)
  - `code/docs/` — public usage docs
  - `code/scripts/archive/` — archived script snapshots (book-version pinned)
- `CHANGELOG.md` — repository-level change log

---

## Build the book (local)

```bash
cd edc_book
latexmk -pdf -interaction=nonstopmode main.tex
