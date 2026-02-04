# Derivation v35 — GUT BC Survivor Map

## Overview

This derivation establishes how boundary conditions (BCs) in 5D gauge theories
select the residual 4D gauge group. The **survivor rule** states that gauge
generators with Neumann/Neumann BCs (or orbifold parity $(+,+)$) retain massless
zero-modes, while Dirichlet or $(-)$ parity removes them.

**Export PDF**: `EDC_BLOCK003_DERIVATION_V35_GUT_BC_SURVIVOR_MAP.pdf`

## Main Results

### Survivor Rule (Theorem 3.5)

$$\text{Zero-mode exists} \quad \Leftrightarrow \quad \text{BC}(A_\mu^a) = (N,N) \text{ or } (\eta_0, \eta_L) = (+,+)$$

### Survivor Algebra (Theorem 5.1)

$$\mathfrak{h} = \mathfrak{g}^{(+,+)} = \{T \in \mathfrak{g} \mid P_0 T P_0^{-1} = +T,\; P_L T P_L^{-1} = +T\}$$

### Four GUT Tracks

| Track | $\dim G$ | Rank | Survivors | Broken |
|-------|----------|------|-----------|--------|
| SU(5) | 24 | 4 | 12 | 12 |
| SO(10) | 45 | 5 | 12 | 33 |
| Pati-Salam | 21 | 5 | 12 | 9 |
| $E_6$ | 78 | 6 | 12 | 66 |

All tracks have exactly 12 survivor generators corresponding to $SU(3)_c \times SU(2)_L \times U(1)_Y$.

## Contents

| Section | Topic |
|---------|-------|
| 1 | Reader Contract |
| 2 | 5D Gauge Theory Setup |
| 3 | Boundary Conditions: Survivor Rule |
| 4 | Orbifold Parities and Projectors |
| 5 | Projector Algebra: Survivor Subalgebra |
| 6 | Track 1: SU(5) |
| 7 | Track 2: SO(10) |
| 8 | Track 3: Pati-Salam |
| 9 | Track 4: $E_6$ |
| 10 | Scale Regime Map |
| 11 | Comparative Summary |
| 12 | BC → Breaking Dictionary |
| 13 | Connection to EDC Program |
| 14 | Reviewer Trap Checklist |
| 15 | Conclusions |
| App A-L | Supporting Material |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (21 pages, 108 equations) |
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

## Key Derivations

1. **Survivor Rule**: Zero-mode ⇔ $(N,N)$ or $(+,+)$ BCs [D]
2. **Projector Algebra**: $\mathfrak{h} = \mathfrak{g}^{(+,+)}$ [D]
3. **4 Tracks**: Explicit $(P_0, P_L)$ for each GUT [Dc]
4. **Matter Chirality**: Orbifold projection gives chiral 4D [D]
5. **BC Dictionary**: What must be N vs D for SM [D]

## Closure Status

| Component | Status | Tag |
|-----------|--------|-----|
| Survivor rule | Derived | [D] |
| Projector algebra | Derived | [D] |
| SU(5) breaking | Derived | [D] |
| SO(10) breaking | Derived | [D] |
| PS breaking | Derived | [D] |
| $E_6$ breaking | Derived | [D] |
| BC selection principle | Open | [OPEN] |
| Anomaly verification | Open | [OPEN] |

**Structural closure**: ACHIEVED for BC→survivor map
**Numerical closure**: NOT APPLICABLE (no numerics needed)

---

*Generated: 2026-02-03*
