# Derivation v6: Collective Bulk Dimple and Auto-Trapping Threshold

## Status

**OPEN** — Definitions and hypothesis only; no quantitative prediction; BLOCK-003 remains open.

Canonical PDF: `EDC_BLOCK003_DERIVATION_V6_AUTOTRAP_THRESHOLD.pdf`

## What This Document Is

A paper-grade formalization of the "collective bulk dimple + auto-trapping threshold" concept:

- **Defines:** Ξ_N(r), h_N, R_N, τ_μν^(N), ΔE(N), N*
- **Articulates:** Israel junction conditions as the bridge between nucleon binding and bulk geometry
- **Illustrates:** 2-panel TikZ schematic (embedding profiles + threshold diagram)

## What This Document Is NOT

- NOT a 5D back-reaction computation
- NOT a normalization for κ₅² (constant C remains unfixed)
- NOT a numerical prediction for N*
- NOT a closure of BLOCK-003

## Key Definitions

| Symbol | Meaning |
|--------|---------|
| Ξ_N(r) | Embedding function for N-nucleon cluster |
| h_N | Dimple depth: max_r Ξ_N(r) |
| R_N | Characteristic cluster radius |
| ΔE(N) | Energy gain for test nucleon to join cluster |
| N* | Auto-trapping threshold: ΔE(N*) = 0 |

## Hypothesis [OPEN]

There exists N* such that for N > N*, the collective brane deformation makes accretion of additional nucleons energetically favorable (ΔE > 0) without external driving.

## Contents

- `main.tex` — LaTeX source (5 pages)
- `main.pdf` — Build artifact
- `EDC_BLOCK003_DERIVATION_V6_AUTOTRAP_THRESHOLD.pdf` — Canonical export
- `REPORT.md` — Build proof and MD5 table
- `ACCEPTANCE.md` — P17 acceptance criteria checklist
