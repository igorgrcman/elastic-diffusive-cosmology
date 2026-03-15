# BLOCK-004 Derivation v63: Proton Decay τ_p Structural Interface

## Overview

This derivation establishes the proton lifetime $\tau_p$ as a structural function of $\tilde{\sigma}$
by combining:
- **v61:** Proton decay program note (operator catalog, lifetime formula)
- **v62:** PS breaking scale $M_X(\tilde{\sigma})$ derivation

## Key Result

The proton lifetime as a function of the brane tension parameter:

$$\tau_p(\tilde{\sigma}) = \frac{C_X^4}{16\pi^2} \cdot \frac{\mu_*^4 \cdot \tilde{\sigma}^4}{\mathcal{H}_p^{(\text{sym})}}$$

where:
- $C_X = \sqrt{4/15} \approx 0.516$ is the derived geometric constant
- $\mu_* = \pi/L$ is the EDC reference scale
- $\tilde{\sigma}$ is the dimensionless brane tension (single free parameter)
- $\mathcal{H}_p^{(\text{sym})}$ is the symbolic hadronic factor

## Scaling Law

$$\tau_p \propto \tilde{\sigma}^4$$

Larger $\tilde{\sigma}$ (stronger brane tension) → heavier leptoquarks → longer proton lifetime.

## v61 Closure

This derivation closes v61's open variable $M_X$ by importing v62's result:
- **Before:** $\tau_p = \tau_p(M_X, g_X, \ldots)$
- **After:** $\tau_p = \tau_p(\tilde{\sigma})$ (single parameter + symbolic hadronic)

## Status

**STRUCTURAL INTERFACE** — Provides $\tau_p(\tilde{\sigma})$ for future numeric predictions.

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (canonical) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (52 checks) |
| `README.md` | This file |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | Release notes |
| `release/` | Export bundle |

## Verification

```bash
python3 recompute.py
```

All 52 checks must pass.

## v63 SoT Hash

`1eb0b781afa6bb6a`

## Layer Architecture

- **Layer A (Hash-Locked):** Operator catalog, rate structure, M_X import, scaling law
- **Layer B (Quarantined):** Parameter sweep, experimental comparison

## No-Fit Policy

$\tilde{\sigma}$ is swept, NOT fitted. Comparison with experiment occurs only in Layer B.
