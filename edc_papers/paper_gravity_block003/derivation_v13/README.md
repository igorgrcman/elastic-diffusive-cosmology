# Derivation v13 — Weak-Field 5D→4D Matching: The Normalization Extractor

**Status:** BRIDGE SLOT FOUND
**Date:** 2026-02-02

## Purpose

This note establishes the functional form by which the 4D Newton constant G_N
emerges from a 5D gravitational theory with a compact or warped extra dimension.
We derive the **normalization extractor**: an explicit integral I such that
M_Pl² = M₅³ × I, from which G_N = 1/(8π M_Pl²).

## One-Line Outcome

> **BRIDGE SLOT FOUND:** G_N reduces to M₅³ I; EDC must compute I or provide one calibration scale.

## Key Results

1. **Non-compact failure:** 5D Green's function gives 1/r² potential (excluded by observation)
2. **Compact/warped recovery:** Normalizable zero-mode produces 1/r (Newtonian)
3. **Normalization Extractor:**
   ```
   M_Pl² = M₅³ × I    where    I = ∫ dξ e^{4A(ξ)} |ψ₀(ξ)|²
   ```
4. **Bridge Slot:** EDC must supply A(ξ), L, M₅, or one calibration scale

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (5 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V13_WEAKFIELD_MATCHING.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P21 acceptance checklist |

## Figure

Section 6 contains a TikZ schematic with two panels:
- (A) Zero-mode profile ψ₀(ξ): flat vs warped
- (B) Effective 4D potential: 1/r² (non-compact, excluded) vs 1/r (compact/warped)

## Epistemic Tags Used

- [M] Mathematical identity
- [D] Derived in this note
- [P] Postulate
- [I] Imported from literature (RS, KK, GHY)
- [BL] Baseline (observational constraint)

## Citations

1. Randall & Sundrum (1999) — RS I and RS II
2. Gibbons & Hawking (1977) — GHY boundary term
3. York (1972) — Boundary value problem in GR
4. Maartens (2004) — Brane-world gravity review
