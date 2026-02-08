# BLOCK-004 Derivation v64: Proton Decay Coupling Lane g_X(M_X)

## Overview

This derivation closes the proton decay gauge coupling lane by deriving $g_X(M_X)$
structurally from the $\alpha_3$-chain (v55-v60) and $M_X(\tilde{\sigma})$ (v62),
thereby absorbing $g_X$ into the $\tau_p(\tilde{\sigma})$ interface from v63.

## Key Result

The proton lifetime as a function of $\tilde{\sigma}$ only:

$$\tau_p(\tilde{\sigma}) = \frac{C_X^4}{16\pi^2} \cdot \frac{\mu_*^4 \cdot \tilde{\sigma}^4}{\mathcal{H}_p^{(\text{sym})}}$$

where:
- $C_X = \sqrt{4/15} \approx 0.516$ is the derived geometric constant
- $\mu_* = \pi/L$ is the EDC reference scale
- $\tilde{\sigma}$ is the dimensionless brane tension (single free parameter)
- $\mathcal{H}_p^{(\text{sym})}$ is the symbolic hadronic factor

## Coupling Derivation

The $g_X$ coupling at $M_X$ is derived via two routes:

**Route T1 (QCD RG):**
$$g_X^{(T1)} = \sqrt{\frac{4\pi}{\tilde{\sigma}}} \cdot (1 + \Delta_{\text{match}} + \tfrac{1}{2}\delta_{\text{RG}})$$

**Route T2 (PS Direct RG):**
$$g_X^{(T2)} = \sqrt{\frac{4\pi}{\tilde{\sigma}}} \cdot (1 + \epsilon_{\text{brane}} + \tfrac{1}{2}\delta_{\text{RG}}^{(4C)})$$

The two routes agree within 5% (consistency theorem).

## Scaling Law

$$\tau_p \propto \tilde{\sigma}^4$$

The $\tilde{\sigma}^4$ scaling arises from:
- $M_X^4 \propto \tilde{\sigma}^2$ (from v62)
- $g_X^4 \propto \tilde{\sigma}^{-2}$ (from v55 + this derivation)

## Status

**COUPLING LANE CLOSED** — $g_X$ absorbed into $\tau_p(\tilde{\sigma})$.

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (canonical) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (104 checks) |
| `README.md` | This file |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | Release notes |
| `release/` | Export bundle |

## Verification

```bash
python3 recompute.py
```

All 104 checks must pass.

## v64 SoT Hash

`a7f3e2d9c8b10456`

## Layer Architecture

- **Layer A (Hash-Locked):** Coupling identity, matching, RG running, consistency
- **Layer B (Quarantined):** Illustrative sweeps only

## No-Fit Policy

$\tilde{\sigma}$ is swept, NOT fitted. Beta coefficient $b_{4C}$ is a template.
