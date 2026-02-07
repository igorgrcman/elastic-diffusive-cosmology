# BLOCK-004 Canonical Single Document — Release Notes

## Release Information

- **Version:** v60
- **Date:** 2026-02-07
- **Status:** CLOSED (conditional)
- **Hash:** 4985a938f5558447

## What This Is

This release bundle contains the canonical reference document for BLOCK-004, the EDC strong coupling prediction from Planck to QCD scale.

## Contents

| File | Description |
|------|-------------|
| BLOCK004_CANONICAL_SINGLE_DOCUMENT.pdf | Main document (36 pages) |
| main.tex | LaTeX source |
| recompute.py | Verification script (98 checks) |
| README.md | Documentation |
| REPORT.md | Detailed report |
| ACCEPTANCE.md | Acceptance criteria |
| RELEASE_NOTES.md | This file |

## Quick Start

1. View the PDF document
2. Run verification: `python3 recompute.py`
3. Read the acceptance criteria

## Key Results

### Layer A (Hash-Locked)
```
α₃(μ*) = 1/σ̃ × (1 ± ε)
μ* = π/L
```

### Layer B (Quarantined)
```
Route Λ₁: Λ = μ × exp(-2π/(b₀αₛ))
Route Λ₂: Λ₂ = Λ₁ × (b₀αₛ/(2π))^(2c₁)
```

### Verification
```
98/98 CHECKS PASSED
BLOCK-004 STATUS: CLOSED (conditional on σ̃)
```

## Derivation Chain

| Version | Hash |
|---------|------|
| v55 | 1794377561879613 |
| v56 | 61869b6fddb68c16 |
| v57 | fadd71e1e0adfa69 |
| v58 | 67ce04beef9f7f79 |
| v59 | b07b904c96267465 |
| v60 | 4985a938f5558447 |

## Contact

EDC Collaboration
