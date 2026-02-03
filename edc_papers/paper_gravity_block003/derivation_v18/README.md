# Derivation v18 — Gravity Sector Closure Summary + Reader Contract

**Status:** CONSOLIDATION / CLOSED (calibrated)
**Date:** 2026-02-02

## Purpose

This note consolidates derivations v13–v17 into a single reader-friendly summary of the
BLOCK-003 gravity sector closure. **No new results are claimed**; this is a consolidation document.

## One-Line Outcome

> **CLOSED (calibrated):** M₅ = 2.41 × 10¹³ GeV under minimal [BL] inputs (M_Pl^obs, M_Z^obs).
> **NOT fully predictive:** R_ξ identification is [I]+[BL], not [D].

## Reader Contract

| Category | Status | Description |
|----------|--------|-------------|
| **[D] Derived** | ✅ | M_Pl² = M₅³ I from 5D→4D reduction |
| **[I] Identified** | ⚠️ | R_ξ = ℏc/M_Z (not derived from axioms) |
| **[BL] Baseline** | ✅ | M_Pl^obs, M_Z^obs from experiment |
| **NO-GO** | ❌ | Internal derivation of R_ξ impossible |

## Key Results

### Canonical Derivation Chain

1. **v13:** M_Pl² = M₅³ I (normalization extractor) [D]
2. **v14:** I = R_ξ (Model A, compact) [Dc]
3. **v16:** R_ξ = ℏc/M_Z^obs [I]+[BL]
4. **v15:** M₅ = (M_Pl²/R_ξ)^{1/3} [D]
5. **v17:** Robustness verified [D]

### Numerical Closure

| Quantity | Value | Tag |
|----------|-------|-----|
| R_ξ | 2.165 × 10⁻¹⁸ m | [I]+[BL] |
| M₅ | 2.41 × 10¹³ GeV | [D] |
| δM₅/M₅ | 1.1 × 10⁻⁵ | — |

### Robustness (v17)

All EW-scale choices (M_Z, M_W, v_EW) yield M₅ in the same decade (2.3–3.4 × 10¹³ GeV).

## What Remains Open

- **Track A NO-GO:** R_ξ cannot be derived from EDC axioms alone
- **Full closure would require:** deriving R_ξ without EW input

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (4 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V18_GRAVITY_CLOSURE_SUMMARY.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P26 acceptance checklist |

## Build

```bash
cd edc_papers/paper_gravity_block003/derivation_v18
xelatex main.tex && xelatex main.tex
```

---

**No new results; consolidation of v13–v17.**
