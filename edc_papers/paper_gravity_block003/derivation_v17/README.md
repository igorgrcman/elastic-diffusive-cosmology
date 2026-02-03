# Derivation v17 — EW-Scale Calibration Robustness for R_ξ and M₅

**Status:** ROBUST (calibration stable)
**Date:** 2026-02-02

## Purpose

This note stress-tests the Track B calibrated closure from v16 by replacing the single
identification R_ξ = ℏc/M_Z^obs with a calibration family R_ξ = ℏc/M_*^obs where
M_* ∈ {M_Z, M_W, v_EW}.

## One-Line Outcome

> **ROBUST:** All EW-scale choices yield M₅ within the same decade (2.3–3.4 × 10¹³ GeV).
> **Canonical:** M_Z preferred for metrological precision and definitional stability.

## Key Results

### Calibration Family Table

| M_* | Value (GeV) | R_ξ (m) | M₅ (GeV) | Δlog₁₀M₅ | Tag |
|-----|-------------|---------|----------|----------|-----|
| M_Z | 91.1876 | 2.165 × 10⁻¹⁸ | 2.41 × 10¹³ | 0 (ref) | [BL] |
| M_W | 80.379 | 2.455 × 10⁻¹⁸ | 2.31 × 10¹³ | −0.018 | [Dc] |
| v_EW | 246.22 | 8.01 × 10⁻¹⁹ | 3.35 × 10¹³ | +0.143 | [BL] |

### Robustness Verdict

**ROBUST:** Maximum shift |Δlog₁₀M₅| = 0.143 (factor ~1.4), well within same order of magnitude.

### Why M_Z is Canonical

1. **Metrological precision:** δM_Z/M_Z ≈ 2.3 × 10⁻⁵ (best among candidates)
2. **Definitional stability:** Z pole mass is scheme-independent at leading order
3. **Independence:** Direct observable, unlike M_W which is derived in EDC
4. **Consistency:** Used throughout v2–v16 and Part II

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (4 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V17_EW_CALIBRATION_ROBUSTNESS.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P25 acceptance checklist |

## What Remains Open

- Full [D] derivation of R_ξ from EDC axioms (Track A NO-GO remains)
- Physical explanation for why compactification scale coincides with EW length
