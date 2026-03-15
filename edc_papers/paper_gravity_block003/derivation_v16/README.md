# Derivation v16 — R_ξ Determination: Internal vs Minimal-Baseline

**Status:** Track A: NO-GO | Track B: CLOSED
**Date:** 2026-02-02

## Purpose

This note addresses the final missing piece for fully predictive closure:
determination of R_ξ. Two tracks are pursued:
- **Track A:** Attempt to derive R_ξ from EDC internal geometry
- **Track B:** Constrain R_ξ via minimal-baseline input

## One-Line Outcome

> **Track A: NO-GO** (R_ξ not derivable from EDC axioms)
> **Track B: CLOSED** (R_ξ = ℏc/M_Z^obs = 2.165 × 10⁻¹⁸ m; M₅ = 2.4 × 10¹³ GeV)

## Key Results

### Track A (Internal Derivation)

**Result: NO-GO**

All candidate relations in the repo either:
1. Use R_ξ as input, not output
2. Are postulates [P], not derivations
3. Relocate the unknown to another undetermined quantity

The fundamental definition R_ξ = ℏc/M_Z is phenomenological, not derived.

### Track B (Minimal Baseline)

**Result: CLOSED**

| Quantity | Value | Tag |
|----------|-------|-----|
| R_ξ | 2.165 × 10⁻¹⁸ m | [BL] |
| M₅ | 2.4 × 10¹³ GeV | [D] |
| δM₅/M₅ | ~10⁻⁵ | — |

### Physical Interpretation

M₅ ≈ 2 × 10¹³ GeV is at the **GUT scale**, approximately 10⁻⁶ M_Pl.

## Error Budget

```
δM₅/M₅ = √[(2/3 δM_Pl/M_Pl)² + (1/3 δR_ξ/R_ξ)²]
       = √[(0.73×10⁻⁵)² + (0.77×10⁻⁵)²]
       ≈ 1.1 × 10⁻⁵
```

**Dominant contribution:** M_Z (via R_ξ) slightly dominates.

## Candidate Relations Table

| Formula | Location | Dependencies | Tag | Circularity |
|---------|----------|--------------|-----|-------------|
| R_ξ = ℏc/M_Z | Ch.6, Ch.13 | M_Z^obs | [BL] | LOW |
| ℓ = 2π R_ξ | ch11_opr20 | R_ξ | [M] | — |
| α = r_e/R_ξ | Ch.6 EW | r_e, R_ξ | [Dc] | LOW |
| δ = R_ξ (A2) | Ch.13 | postulate | [P] | — |
| R_ξ ~ σ^{-1/4} | v14, v15 | σ | [P] | MED |

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (7 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V16_R_XI_DETERMINATION.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P24 acceptance checklist |

## What Would Remove Last [BL] Beyond M_Pl

1. Derive M_Z from membrane dynamics
2. Derive R_ξ directly from EDC action
3. Find independent observable constraining R_ξ
