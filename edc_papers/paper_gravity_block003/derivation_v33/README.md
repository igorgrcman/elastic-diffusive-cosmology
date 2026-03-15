# Derivation v33 — Matter + RG Dual-Track Program

## Overview

This derivation extends BLOCK-003 from the gravity bridge to a dual-track gauge+matter program:
- **Track M**: Chirality/Higgs emergence via 5D fermion BCs and gauge-Higgs unification
- **Track R**: RG/matching across KK thresholds with piecewise running

**Export PDF**: `EDC_BLOCK003_DERIVATION_V33_MATTER_AND_RG_PROGRAM.pdf`

## Two Tracks

| Track | Topic | Key Results |
|-------|-------|-------------|
| M | Matter/Chirality/Higgs | Chiral BCs, $A_5$ Higgs, Yukawa overlap |
| R | RG/Matching/Running | Gauge bridge, KK thresholds, piecewise running |

## Contents

### Track M (Sections 2-9)
| Section | Topic |
|---------|-------|
| 2 | 5D Dirac Action and Boundary Variation |
| 3 | Chiral Boundary Conditions |
| 4 | Chiral Zero Mode Condition |
| 5 | Warped Background Fermions |
| 6 | Anomaly Risk Assessment |
| 7 | Gauge-Higgs Unification: $A_5$ as Higgs |
| 8 | Yukawa from Overlap Integrals |
| 9 | BC Registry v33 |

### Track R (Sections 10-16)
| Section | Topic |
|---------|-------|
| 10 | Gauge Coupling Dimensional Analysis |
| 11 | KK Spectrum and Matching Scale |
| 12 | Piecewise Running and Threshold Matching |
| 13 | Scale Regime Map v33 |
| 14 | Track-to-RG Dictionary |
| 15 | Hypercharge Normalization |
| 16 | Matching Conditions |

### Shared (Sections 17-20, Appendices)
| Section | Topic |
|---------|-------|
| 17 | Reviewer Trap Checklist |
| 18 | Internal Closure Attempt |
| 19 | Epistemic Ledger |
| 20 | Conclusions |
| App A-L | Extended Derivations |

## Key Results

1. **Chiral Zero Mode Condition** (Lemma 4.1): $\Psi_L|_{\text{bdry}} = 0$ or $\Psi_R|_{\text{bdry}} = 0$ [D]
2. **Gauge-Higgs Unification**: $A_5$ as 4D Higgs via Hosotani mechanism [D] + [P]
3. **Yukawa Overlap**: $y_4 = y_5 \cdot I_{\text{overlap}}$ [D]
4. **Gauge Matching**: $g_4^{-2} = g_5^{-2} I_{\text{gauge}} + \Delta_{\text{brane}}$ [D]
5. **KK Scale**: $\mu_{\text{KK}} = \pi/L$ [D]
6. **Piecewise Running**: With tower corrections above $\mu_{\text{KK}}$ [D]
7. **Hypercharge**: $c_Y = 5/3$ for all tracks [Dc]

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (29 pages, 150 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (18 checks, ALL PASS) |
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
recompute.py: 18/18 CHECKS PASSED
```

## Forbidden Inputs (HARD RULE)

The following do **NOT** appear anywhere as numeric inputs:
- $M_Z$, $M_W$, $v_{\text{EW}}$ (electroweak scales)
- $\ell_P$, $G_N$ (Planck/Newton)
- $\alpha_{\text{EM}}$ (fine structure constant)

All test values are tagged [TEST].

## Epistemic Tags

- **[D]** — Derived from action/variational principle
- **[Dc]** — Derived with conventions
- **[P]** — Postulate (input assumption)
- **[I]** — Mathematical identity
- **[BL]** — Brane-localized term
- **[OPEN]** — Not yet closed

## Status

**Derivation v33**: COMPLETE (Dual-Track Program Note)

---

*Generated: 2026-02-03*
