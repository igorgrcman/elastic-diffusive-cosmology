# Derivation v38 — Hosotani Closure Roadmap

## Overview

This derivation establishes the roadmap for achieving Hosotani closure: deriving
electroweak symmetry breaking and the Higgs mass from 5D gauge theory with
compact extra dimension. The Hosotani mechanism identifies the 4D Higgs with
the Wilson line phase $\langle A_5 \rangle$.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V38_HOSOTANI_CLOSURE_ROADMAP.pdf`

## Main Results

### Six-Stage Roadmap

1. **5D Gauge Theory**: Start with gauge group $G$ on $[0, L]$
2. **Wilson Line**: Parametrize $W = e^{i\theta^a T^a}$
3. **Effective Potential**: Compute $V_{\text{eff}}(\theta)$ at one-loop
4. **Vacuum Selection**: Find $\theta^* = \arg\min V$
5. **EW Scale**: $v = \theta^*/(g_4 L)$
6. **Higgs Mass**: $m_H^2 = V''(\theta^*)/v^2$

### Key Formulas

**Wilson Line VEV**:
$$\langle A_5 \rangle = \frac{\theta^a T^a}{g_5 L}$$

**EW Scale**:
$$v_{\text{EW}} = \frac{\theta^*}{g_4 L}$$

**Higgs Mass**:
$$m_H^2 = \frac{1}{v^2} \frac{\partial^2 V_{\text{eff}}}{\partial \theta^2}\bigg|_{\theta^*}$$

### EDC Connection

$$v_{\text{EW}} = \frac{\theta^*}{g_4} \cdot \sqrt{\frac{\sigma}{\beta \bar{M}_{\text{Pl}}^2}}$$

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract |
| 2 | Hosotani Mechanism Overview |
| 3 | Wilson Line Parametrization |
| 4 | Effective Potential: Structure |
| 5 | Effective Potential: Computation |
| 6 | Vacuum Selection |
| 7 | EW Scale from Wilson Line |
| 8 | Higgs Mass Prediction |
| 9 | Connection to EDC Parameters |
| 10 | Roadmap Diagram |
| 11 | Matter Content Requirements |
| 12 | Gauge Coupling Unification |
| 13 | Specific Models |
| 14 | Numerical Estimates |
| 15 | Warped Hosotani |
| 16 | Detailed Potential Minimization |
| 17 | Fermion Loop Contributions |
| 18 | Gauge Loop Contributions |
| 19 | Competition and Symmetry Breaking |
| 20 | Electroweak Precision |
| 21 | Closure Status Summary |
| 22 | Reviewer Trap Checklist |
| 23 | Conclusions |
| App A-E | Supporting Material |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (23 pages, 93 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (16 checks, ALL PASS) |
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
recompute.py: 16/16 CHECKS PASSED
```

## Forbidden Inputs (HARD RULE)

The following do **NOT** appear anywhere as numeric inputs:
- $M_Z$, $M_W$, $v_{\text{EW}}$ (electroweak scales)
- $\ell_P$, $G_N$ (Planck/Newton)
- $\alpha_{\text{EM}}$ (fine structure constant)

## Closure Status

| Component | Status | Tag |
|-----------|--------|-----|
| Wilson line parametrization | Derived | [D] |
| Effective potential structure | Derived | [D] |
| EW scale formula | Derived | [D] |
| Higgs mass formula | Derived | [D] |
| EDC connection | Derived | [D] |
| Roadmap diagram | Derived | [D] |
| $\theta^*$ determination | Open | [OPEN] |
| $g_4$ from v36 | Open | [OPEN] |
| $L$ from v30 | Open | [OPEN] |

---

*Generated: 2026-02-03*
