# Derivation v14 — EDC Candidates for Warp Profile and Zero-Mode

**Status:** PARTIAL BRIDGE
**Date:** 2026-02-02

## Purpose

Building on v13's normalization extractor (M_Pl² = M₅³ I), this note investigates
whether EDC's internal structure can determine the warp factor A(ξ) and zero-mode
profile ψ₀(ξ), thereby computing the integral I from first principles.

## One-Line Outcome

> **PARTIAL BRIDGE:** I computed up to one EDC parameter (R_ξ or k); requires 1 calibration scale (ℓ_P or M_Pl).

## Candidate Models

### Model A (Compact)

- **Ansatz:** L = R_ξ (EDC correlation length), A(ξ) = 0 (flat)
- **Result:** I = R_ξ
- **G_N formula:** G_N = 1/(8π M₅³ R_ξ)
- **Open:** M₅ not determined by EDC
- **Circularity risk:** LOW (R_ξ independent of G_N)

### Model B (Warped)

- **Ansatz:** A(ξ) = -k|ξ| (RS-type warp)
- **Result:** I = 1/k
- **G_N formula:** G_N = k/(8π M₅³)
- **Open:** k and M₅ not determined
- **Circularity risk:** MEDIUM (k might be fit to G_N)

## Preferred Model

**Model A** is preferred due to lower circularity risk. R_ξ is already defined
in EDC from stiffness σ via R_ξ ~ σ^(-1/4), independent of gravitational measurements.

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (6 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V14_I_FROM_EDC_WARP_CANDIDATES.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P22 acceptance checklist |

## Figure

Section 7 contains a TikZ schematic with three panels:
- (A) Candidate warp profiles: linear and Gaussian
- (B) Zero-mode localization: flat vs warped
- (C) Convergence status: both models yield finite I

## Key Insight

Both models have the structure M_Pl² = M₅³ × (EDC length scale).
EDC provides ratios of length scales, but cannot fix the absolute scale
without one external input. Best calibration choice: ℓ_P^obs.
