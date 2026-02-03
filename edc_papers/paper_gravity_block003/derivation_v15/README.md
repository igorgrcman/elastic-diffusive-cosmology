# Derivation v15 — Calibrated Closure with ℓ_P and Error Budget

**Status:** CLOSED (calibrated)
**Date:** 2026-02-02

## Purpose

This note closes the BLOCK-003 program under the standard one-scale calibration
paradigm. Using the v13 normalization extractor and v14 Model A, we calibrate
with M_Pl^obs [BL] and derive the 5D Planck mass M₅ as a function of R_ξ.

## One-Line Outcome

> **CLOSED (calibrated):** BLOCK-003 closed under one-scale [BL] calibration; 5D scale inferred as M₅(R_ξ) = M_Pl^{2/3} R_ξ^{-1/3}.

## Key Results

### Structural Relation
```
M_Pl² = M₅³ R_ξ
```

### Calibration
Using M_Pl^obs [BL]:
```
M₅ = (M_Pl²/R_ξ)^{1/3} = M_Pl^{2/3} R_ξ^{-1/3}
```

### Scaling
```
M₅ ∝ R_ξ^{-1/3}
```
- Larger brane thickness → smaller 5D Planck mass
- R_ξ = ℓ_P → M₅ = M_Pl (minimal case)
- R_ξ = 10^15 ℓ_P → M₅ ~ 10^14 GeV (GUT scale)

## Error Budget

```
δM₅/M₅ = √[(2/3 δM_Pl/M_Pl)² + (1/3 δR_ξ/R_ξ)²]
```

- If R_ξ precise: dominated by M_Pl^obs (~10^-5)
- If R_ξ uncertain: dominated by R_ξ uncertainty

## Contents

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (6 pages) |
| `main.pdf` | Compiled PDF |
| `EDC_BLOCK003_DERIVATION_V15_CALIBRATED_CLOSURE_LP.pdf` | Canonical export |
| `README.md` | This file |
| `REPORT.md` | Build report with MD5s |
| `ACCEPTANCE.md` | P23 acceptance checklist |

## Epistemic Status

| Quantity | Tag | Source |
|----------|-----|--------|
| ℏ, c, e | [M] | SI exact |
| M_Pl^obs | [BL] | CODATA |
| R_ξ | [P]/[Dc] | EDC postulate |
| M₅ | [D] | This note |

## Open Research Directions

- Derive R_ξ from EDC internal dynamics
- Derive A(ξ) from membrane mechanics
- Independent test of M₅
