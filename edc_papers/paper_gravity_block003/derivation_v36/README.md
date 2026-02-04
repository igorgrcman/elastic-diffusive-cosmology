# Derivation v36 — G_F Numerical Closure Step: g_5 Fixing

## Overview

This derivation establishes candidates for the 5D gauge coupling $g_5$ from
first principles, without using electroweak observables as inputs. Three
mechanism tracks are developed, each providing an explicit formula relating
$g_5$ to fundamental 5D parameters.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V36_GF_NUMERICAL_CLOSURE_STEP_G5.pdf`

## Main Results

### Dimensional Structure
$$[g_5^2] = M^{-1}, \quad [g_4^2] = M^0 \text{ (dimensionless)}$$

### Track A: Stiffness Scaling
$$g_5^2 = \frac{c_A}{M_5} = c_A \left(\frac{\kappa_5^2}{\sigma}\right)^{1/3}$$

### Track B: Topological Level
$$g_5^2 = \frac{2\pi c_B L}{\lambda} = \frac{c_B L}{|k|/(2\pi)}$$

### Track C: Self-Consistency
$$g_5^2 = \frac{4\pi c_C}{\Lambda_5}$$

### Bridge to G_F
For each track, the 4D coupling feeds into:
$$\frac{G_F}{\sqrt{2}} = \sum_{n} \frac{(g_4^{(n)})^2}{8 m_n^2} |\mathcal{I}_n|^2$$

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract |
| 2 | 5D Gauge Action and Conventions |
| 3 | KK Reduction and Normalization |
| 4 | Track A: Stiffness/Brane-Tension |
| 5 | Track B: Topological Level |
| 6 | Track C: Loop/Self-Consistency |
| 7 | Comparison of Tracks |
| 8 | Brane-Localized Terms |
| 9 | Bridge to G_F Formula |
| 10 | EDC Parameter Relations |
| 11 | π-Map Invariance |
| 12 | No Hidden Planck Trap |
| 13 | Dimensional Audit |
| 14 | Open Items |
| App A-H | Supporting Material |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (25 pages, 140 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (17 checks, ALL PASS) |
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
recompute.py: 17/17 CHECKS PASSED
```

## Forbidden Inputs (HARD RULE)

The following do **NOT** appear anywhere as numeric inputs:
- $M_Z$, $M_W$, $v_{\text{EW}}$ (electroweak scales)
- $\ell_P$, $G_N$ (Planck/Newton)
- $\alpha_{\text{EM}}$ (fine structure constant)

## Closure Status

| Component | Status | Tag |
|-----------|--------|-----|
| [g_5^2] dimension | Derived | [D] |
| Track A formula | Derived | [Dc] |
| Track B formula | Derived | [Dc/P] |
| Track C formula | Derived | [P→Dc] |
| Bridge to G_F | Derived | [D] |
| π-map invariance | Proven | [D] |
| Planck trap check | Verified | [D] |
| Coefficients c_A, c_B, c_C | Open | [OPEN] |
| Scale L or M_5 | Open | [OPEN] |

---

*Generated: 2026-02-03*
