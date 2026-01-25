# BUILD_BASELINE.md

Build verification for edc_book_2 workspace.

## Baseline Source

| Property | Value |
|----------|-------|
| Source baseline | 387-page rebuild from `edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper/` |
| Source PDF SHA256 | `c94f92faa60552663cfb620e2761422ca4cad7be376b08d39218ba71e51c5374` |
| Source TEX SHA256 | `91f5e857957d8df0a53b49be584ede26bae908722720ba624805210410f0c94d` |

## Build Verification

| Property | Value |
|----------|-------|
| Build date | 2026-01-24 |
| Engine | XeLaTeX via latexmk |
| Command | `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex` |
| Output PDF | `build/main.pdf` |
| Output SHA256 | `5736d1d80390bab52c8f18c622663b4f683c4b291db99201a5f7aa1462fb7bda` |
| Page count | **387** (matches baseline) |
| Build status | **PASS** |

## Path Modifications

One path was updated from the original to work in the new directory structure:

| Original | Updated |
|----------|---------|
| `\input{../../../../../_shared/meta/edc_meta_macros}` | `\input{_shared/meta/edc_meta_macros}` |
| `\input{../../../../../_shared/meta/edc_stoplight_legend}` | `\input{_shared/meta/edc_stoplight_legend}` |

All other paths (`sections/`, `bib/`, etc.) work unchanged because files were copied preserving relative structure.

## File Inventory

| Category | Count |
|----------|-------|
| Root .tex | 4 |
| sections/*.tex | 55 |
| figures/*.tex | 6 |
| meta_part2/*.tex | 6 |
| _shared/meta/*.tex | 2 |
| bib/*.bib | 1 |
| frontmatter/*.tex | 1 |
| code/output/*.pdf | 1 |
| **Total** | **76** |

## Reproducibility

To reproduce the build:

```bash
cd edc_book_2/src
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected output: 387 pages.
