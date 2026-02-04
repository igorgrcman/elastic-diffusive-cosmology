# Derivation v31 — Gauge Sector Normalization, BC Registry, and Scale Regime Map

## Overview

This derivation extends the BLOCK-003 epistemic ledger discipline to the gauge sector.
It derives the 5D→4D gauge kinetic normalization, establishes the Boundary Condition
Registry across field types, and constructs a Scale Regime Map showing UV/KK/IR transitions.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V31_GAUGE_NORMALIZATION_BC_SCALEMAP.pdf`

## Contents

| Section | Topic |
|---------|-------|
| §1 | Reader Contract and Epistemic Registry |
| §2 | 5D Gauge Action and Variational Principle |
| §3 | KK Decomposition and Zero-Mode Survival |
| §4 | 5D→4D Gauge Kinetic Normalization |
| §5 | Boundary/Brane Conditions Registry |
| §6 | Scale Regime Map |
| §7 | Chern-Simons Terms and Topological Constraints |
| §8 | Coupling Running and Threshold Corrections |
| §9 | Candidate Unification Route (Toy Example) |
| §10 | Epistemic Ledger and Dependency Audit |
| §11 | Reviewer Trap Checklist |
| §12 | Conclusions |
| App A | Dimensional Analysis |
| App B | Mode Function Details |
| App C | Warped Geometry Details |
| App D | Group Theory Supplement |
| App E | Extended Derivations |
| App F | Fermion BC Considerations |
| App G | Numerical Examples |
| App H | Comparison with Gravity Sector |

## Key Results

1. **Gauge Bridge Slot**: g₄⁻² = g₅⁻² · I_gauge [D]
2. **BC Registry**: Unified table across graviton, gauge, scalar, fermion fields
3. **Scale Regime Map**: TikZ diagram with explicit thresholds
4. **Generator Survival Matrix**: SU(3) → SU(2) × U(1) toy example
5. **CS Quantization**: k ∈ ℤ from large gauge invariance

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (15 checks) |
| `README.md` | This file |
| `REPORT.md` | Detailed report |
| `ACCEPTANCE.md` | Acceptance criteria verification |

## Build

```bash
pdflatex main.tex
pdflatex main.tex  # second pass for TOC
python3 recompute.py
```

## Verification

```
recompute.py: 15/15 CHECKS PASSED
```

## Epistemic Tags Used

- **[D]** — Derived from first principles
- **[Dc]** — Derived with conventions
- **[P]** — Postulate
- **[I]** — Identification
- **[BL]** — Baseline input
- **[OPEN]** — Not yet closed

## Status

**Derivation v31**: COMPLETE (Program Note)

---

*Generated: 2026-02-03*
