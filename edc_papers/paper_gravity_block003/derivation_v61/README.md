# EDC BLOCK-004: Proton Decay Program Note (PS)
## Canonical Derivation v61

### Overview

This derivation establishes the structural framework for proton decay predictions
within the EDC Pati-Salam (PS) unification program. It provides the group-theoretic
and operator structure needed to compute proton lifetime once the PS breaking
scale $M_X$ is derived from EDC field equations.

### Status

**PROGRAM NOTE — OPEN** until $M_X$ derived from EDC cosmology.

### Layer Architecture

| Layer | Content | Status |
|-------|---------|--------|
| Layer A | Structural derivations (group theory, operators, scaling) | CLOSED |
| Layer B | Experimental comparison framework (quarantined) | DEFINED |

### Key Results

1. **PS Gauge Group**: $G_{PS} = SU(4)_C \times SU(2)_L \times SU(2)_R$
2. **Leptoquark Bosons**: $X_\mu^\alpha$ with $Q_X = \pm 4/3$
3. **Dimension-6 Operators**: $\mathcal{O}_6 \sim (\bar{q}q)(\bar{q}\ell)$
4. **Lifetime Scaling**: $\tau_p \propto M_X^4 / (g_{PS}^4 \alpha_H^2 m_p^5)$

### API Definitions

- **API-PD1**: Proton lifetime from PS parameters
- **API-PD2**: Dimension-6 operator coefficients from group theory

### Required Future Inputs

| Parameter | Source | Status |
|-----------|--------|--------|
| $M_X$ | EDC PS breaking | Future block |
| $\alpha_H$ | Hadronic physics | Layer B / future |
| Flavor mixing | CKM-like structure | Future block |

### Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled document |
| `recompute.py` | Verification script |
| `README.md` | This file |
| `REPORT.md` | Technical report |
| `ACCEPTANCE.md` | Acceptance criteria |
| `release/` | Release bundle |

### Build Instructions

```bash
# Compile PDF
pdflatex main.tex
pdflatex main.tex  # Run twice for references

# Run verification
python3 recompute.py
```

### Hash Chain

| Version | Content | Hash | Status |
|---------|---------|------|--------|
| v55 | PS → QCD Structural | `1794377561879613` | CLOSED |
| v56 | α₃ Numerical Closure | `61869b6fddb68c16` | CLOSED |
| v57 | Layer B Adapter | `fadd71e1e0adfa69` | CLOSED |
| v58 | Λ Two-Route | `67ce04beef9f7f79` | CLOSED |
| v59 | Formal Two-Route | `b07b904c96267465` | CLOSED |
| v60 | Canonical Single Document | `4985a938f5558447` | CLOSED |
| v61 | Proton Decay Program (PS) | [this document] | OPEN |

### Firewall Rules

- No experimental proton lifetime bounds in Layer A
- No numeric values for $m_p$, $\alpha_H$, or $M_X$ bounds
- No fitting of parameters to match observations
- Hadronic matrix elements remain symbolic

### Author

EDC Collaboration

### License

Part of the EDC theoretical physics project.
