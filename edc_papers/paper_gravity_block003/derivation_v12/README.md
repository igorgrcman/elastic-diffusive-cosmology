# Derivation v12: Part I Gravity & Mercury Precession Audit

## Status

**NO BRIDGE** — Part I imports 4D gravity as [I]/[P]; BLOCK-003 remains open.

Canonical PDF: `EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf`

## What This Document Is

A back-reference audit of how gravity was introduced in EDC Book Part I, specifically examining:
1. What was assumed/identified/postulated to get a 4D Newtonian/GR-like limit
2. How Mercury perihelion precession was computed
3. Which steps can be derived from strict 5D setup (EH+GHY+Israel) vs "imported GR"

## Key Findings

| Element | Part I Approach | Epistemic Tag | 5D Derivation Status |
|---------|-----------------|---------------|---------------------|
| G formula | $G = \ell_P^2 c^4/(\sigma r_e^3)$ | [I] | Uses observed $\ell_P$ |
| Flow ansatz | $v = \sqrt{2GM/r}$ | [P] | Postulated, not derived |
| Schwarzschild | From acoustic metric | [D] | Conditional on ansatz |
| Mercury precession | Standard GR formula | [D]+[BL] | Uses observed G, M_☉ |
| ρ_Plenum | ~ρ_Planck | [P] | Not derived |

## Bridge Map Summary

- Part I does NOT use EH+GHY+Israel junction conditions
- Part I does NOT derive κ₅² from 5D action
- Part I uses observed ℓ_P as input, not output
- Mercury precession is a consistency check, not a prediction
- BLOCK-003 (derive G from EDC) remains OPEN

## Build Instructions

```bash
cd derivation_v12
xelatex main.tex
xelatex main.tex  # second pass for refs
cp main.pdf EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf
```

## Contents

- `main.tex` — LaTeX source (5-7 pages)
- `main.pdf` — Build artifact
- `EDC_BLOCK003_DERIVATION_V12_PART1_GRAVITY_AUDIT.pdf` — Canonical export
- `README.md` — This file
- `REPORT.md` — Build proof and findings summary
- `ACCEPTANCE.md` — AC-P20 checklist
