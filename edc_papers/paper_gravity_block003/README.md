# EDC Gravity Sector (BLOCK-003): A 5D-First Derivation Program

## Status

**FROZEN** (reviewer-ready) — This is a derivation roadmap, not completed results.

Canonical PDF: `EDC_BLOCK003_GRAVITY_PROGRAM.pdf` (MD5: `ba290a5bf3ebe7d6609de53802990ae4`)

## Purpose

This mini-paper outlines a research program for addressing BLOCK-003 (gravity sector) within the EDC framework. It does NOT solve the gravity problem; it structures the derivation path.

## Contents

- `main.tex` — LaTeX source
- `main.pdf` — Build artifact (direct xelatex output)
- `EDC_BLOCK003_GRAVITY_PROGRAM.pdf` — **Canonical export** (for sharing/uploading)
- `figures/` — TikZ figures (inline in main.tex)
- `REPORT.md` — Build report

This paper is indexed in `edc_papers/PAPERS_INDEX.md`.

## Key Features

1. **5D-First Approach**: Start from bulk action, derive junction conditions, extract 4D gravity
2. **Anti-Circularity Ledger**: Explicit separation of allowed vs prohibited inputs
3. **Acceptance Criteria**: AC-G1 through AC-G10 define closure requirements

## Relationship to Nuclear Monograph

This paper is a **standalone companion**. The nuclear pinning monograph remains gravity-out-of-scope. No modifications to the monograph are made by this paper.

## Build

```
xelatex main.tex
xelatex main.tex
```

Requires: standard LaTeX with amsmath, tikz, tcolorbox, hyperref.

## License

Same as parent repository.
