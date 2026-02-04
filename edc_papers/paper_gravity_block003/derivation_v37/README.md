# Derivation v37 — BC Selection Principle Sketch

## Overview

This derivation establishes a hierarchical principle for selecting boundary
conditions (BCs) in 5D field theories. Rather than cataloging BCs, we derive
a four-stage pipeline that progressively narrows the allowed BC space to a
unique (or small set of) selected values.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V37_BC_SELECTION_PRINCIPLE.pdf`

## Main Results

### Four Selection Stages

1. **Variational Principle**: BCs must make the action stationary
   $$\left[ \frac{\partial\mathcal{L}}{\partial(\partial_y\Phi)} \delta\Phi \right]_0^L = 0$$

2. **Self-Adjointness**: Differential operator must be self-adjoint
   $$[f^* \partial_y g - (\partial_y f)^* g]_0^L = 0 \quad \forall f,g \in \text{Dom}$$

3. **Topological Pinning**: Discrete constraints from winding/homotopy
   $$m_b L \in \mathbb{Z} \cdot \pi \quad \text{or} \quad \lambda = |k|/(2\pi)$$

4. **Vacuum Energy Minimization**: Select minimum energy configuration
   $$\text{BC}^* = \arg\min_{\text{BC} \in \mathcal{B}_{\text{topo}}} \mathcal{E}_{\text{vac}}(\text{BC})$$

### BC Selection Pipeline

$$\mathcal{B} \xrightarrow{\text{var}} \mathcal{B}_{\text{var}} \xrightarrow{\text{SA}} \mathcal{B}_{\text{SA}} \xrightarrow{\text{topo}} \mathcal{B}_{\text{topo}} \xrightarrow{\text{vac}} \text{BC}^*$$

### Prediction Hooks

| Hook | BC Input | Observable Output |
|------|----------|-------------------|
| Gap | Robin parameter $m_b$ | $m_{\text{gap}}$ |
| Survivors | Parities $(P_0, P_L)$ | Gauge group $H$ |
| $G_F$ | Full BC pattern | Fermi constant |
| Higgs | $A_5$ BC + vacuum | EW scale |

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract |
| 2 | BC Registry Recap |
| 3 | Selector 1: Variational Principle |
| 4 | Selector 2: Self-Adjointness |
| 5 | Selector 3: Topological Pinning |
| 6 | Selector 4: Vacuum Energy Minimization |
| 7 | BC Selection Pipeline |
| 8 | Prediction Hooks |
| 9 | Multiple Field Interplay |
| 10 | Connection to EDC Framework |
| 11 | Dimensional Analysis of BC Parameters |
| 12 | Explicit Spectrum Formulas |
| 13 | Vacuum Energy Expansions |
| 14 | Selection Principle Unification |
| 15 | BC Selection in Warped Space |
| 16 | Anomaly Constraints on BC |
| 17 | Reviewer Trap Checklist |
| 18 | Conclusions |
| App A-H | Supporting Material |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (25 pages, 113 equations) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (15 checks, ALL PASS) |
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

## Forbidden Inputs (HARD RULE)

The following do **NOT** appear anywhere as numeric inputs:
- $M_Z$, $M_W$, $v_{\text{EW}}$ (electroweak scales)
- $\ell_P$, $G_N$ (Planck/Newton)
- $\alpha_{\text{EM}}$ (fine structure constant)

## Closure Status

| Component | Status | Tag |
|-----------|--------|-----|
| Variational selector | Derived | [D] |
| SA selector | Derived | [D] |
| Topological selector | Derived | [Dc/P] |
| Vacuum selector | Postulate | [P] |
| Pipeline structure | Derived | [D] |
| Prediction hooks | Derived | [D] |
| Vacuum minimum location | Open | [OPEN] |

---

*Generated: 2026-02-03*
