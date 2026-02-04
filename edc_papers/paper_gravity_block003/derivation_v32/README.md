# Derivation v32 — Unified Gauge Sector BC Breaking + Scale Map

## Overview

This derivation establishes how a single 5D parent gauge group can produce the
Standard Model gauge structure SU(3)c x SU(2)L x U(1)Y through boundary conditions
(BC) and orbifold projections. Four parallel breaking tracks are developed.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V32_UNIFIED_GAUGE_BC_BREAKING_SCALES.pdf`

## Four Tracks

| Track | Parent | Residual | Generators |
|-------|--------|----------|------------|
| Track S | SU(5) | SM | 24 -> 12 + 12 |
| Track O | SO(10) | SM | 45 -> 12 + 33 |
| Track P | Pati-Salam | SM | via Y = T_3R + (B-L)/2 |
| Track E | E_6 | SO(10) -> SM | 78 -> 45 + 33 |

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract and Epistemic Registry |
| 2 | 5D Gauge Action and Variational BC Derivation |
| 3 | KK Decomposition and BC-Dependent Spectra |
| 4 | Scale Regime Map |
| 5 | Gauge Coupling Bridge |
| 6 | Boundary Condition Registry |
| 7 | Track S: SU(5) Breaking |
| 8 | Track O: SO(10) Breaking |
| 9 | Track P: Pati-Salam Route |
| 10 | Track E: E_6 Breaking |
| 11 | A_5 Scalar Accounting |
| 12 | Unified Coupling Relations |
| 13 | Internal Closure Attempt |
| 14 | Epistemic Ledger |
| 15 | Reviewer Trap Checklist |
| 16 | Conclusions |
| App A-K | Extended Derivations |

## Key Results

1. **Gauge Bridge**: g_4^{-2} = g_5^{-2} I_gauge [D]
2. **BC Classes**: Neumann/Dirichlet/Robin derived from action variation [D]
3. **Generator Survival Matrices**: Complete for all four tracks
4. **Closure Proofs**: SM algebra emerges as direct sum [D]
5. **Hypercharge**: c_Y = 5/3 normalization [Dc]
6. **Pati-Salam**: Y = T_3R + (B-L)/2 [D]

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (26 pages, 126 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (16 checks, ALL PASS) |
| `README.md` | This file |
| `REPORT.md` | Detailed report with Inputs Used table |
| `ACCEPTANCE.md` | Acceptance criteria verification |

## Build

```bash
pdflatex main.tex
pdflatex main.tex  # second pass for TOC
python3 recompute.py
```

## Verification

```
recompute.py: 16/16 CHECKS PASSED
```

## Forbidden Inputs (HARD RULE)

The following do NOT appear anywhere in this derivation:
- M_Z, M_W, v_EW (electroweak scales)
- l_P, G_N (Planck/Newton)
- alpha_EM (fine structure constant)

All test values are tagged [TEST].

## Epistemic Tags

- **[D]** -- Derived from action/variational principle
- **[Dc]** -- Derived with conventions
- **[P]** -- Postulate (group choice)
- **[OPEN]** -- Not yet closed

## Status

**Derivation v32**: COMPLETE (Program Note)

---

*Generated: 2026-02-03*
