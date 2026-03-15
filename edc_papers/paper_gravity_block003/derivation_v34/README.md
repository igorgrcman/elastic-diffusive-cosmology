# Derivation v34 — Fermi Constant from KK Tower Exchange

## Overview

This derivation establishes $G_F$ from 5D→4D dimensional reduction via KK exchange,
**without identification** with electroweak observables. The Fermi constant emerges
from integrating out the charged Kaluza-Klein tower.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V34_GF_FROM_KK_EXCHANGE.pdf`

## Main Result

$$\frac{G_F}{\sqrt{2}} = \sum_{n \in \text{charged}} \frac{(g_4^{(n)})^2}{8\, m_n^2}$$

where:
- $m_n$ = KK masses from BC-dependent spectrum [D]
- $g_4^{(n)}$ = effective 4D couplings from overlap integrals [D]
- Factor 1/8 from SU(2) structure and Fierz [D]

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract |
| 2 | 5D Gauge-Fermion Action |
| 3 | Boundary Conditions from Variation |
| 4 | Kaluza-Klein Decomposition |
| 5 | Fermion KK Decomposition |
| 6 | 4D Effective Coupling (Overlap Integral) |
| 7 | Tree-Level Exchange and Four-Fermion Operator |
| 8 | Tower Summation and Dominant Mode |
| 9 | Explicit Formulas |
| 10 | Connection to EDC Parameters |
| 11 | What Remains Open |
| 12 | Epistemic Ledger |
| 13 | Reviewer Trap Checklist |
| 14 | Conclusions |
| App A-L | Extended Derivations |

## Key Derivations

1. **4D Coupling from 5D**: $g_4^{(n)} = g_5 \int_0^L dy\, w(y) |\chi_0(y)|^2 f_n(y)$ [D]
2. **Factor of 8**: $8 = 2 \times 2 \times 2$ (CC × SU(2) × Fierz) [D]
3. **Tower Convergence**: $\sum 1/n^2 = \pi^2/6$ [I]
4. **Dominant Mode**: First mode contributes ~61% [D]

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (24 pages, 118 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (15 checks, ALL PASS) |
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
recompute.py: 15/15 CHECKS PASSED
```

## Forbidden Inputs (HARD RULE)

The following do **NOT** appear anywhere as numeric inputs:
- $M_Z$, $M_W$, $v_{\text{EW}}$ (electroweak scales)
- $\ell_P$, $G_N$ (Planck/Newton)
- $\alpha_{\text{EM}}$ (fine structure constant)

Postdiction section compares to measured $G_F$ but this is **verification only**, not input.

## Closure Status

| Component | Status | Tag |
|-----------|--------|-----|
| $G_F$ formula | Derived | [D] |
| Overlap integral | Derived | [D] |
| Factor 1/8 | Derived | [D] |
| Tower convergence | Proven | [I] |
| $g_5$ value | Open | [OPEN] |
| $\beta$ value | Open | [OPEN] |
| Branch $k$ | Open | [OPEN] |

**Structural closure**: ACHIEVED
**Numerical closure**: NOT ACHIEVED (requires $g_5$, $\beta$, $k$)

---

*Generated: 2026-02-03*
