# BLOCK-004 Derivation v62: PS Breaking Scale M_X (Two-Route)

## Overview

This derivation establishes the Pati-Salam (PS) breaking scale $M_X$ from EDC-internal quantities
using two independent routes:
- **Route A:** Geometric/topological determination from brane configuration
- **Route B:** Effective field theory matching from gauge sector (v55-v60)

## Key Result

The PS breaking scale is:

$$M_X = 0.516 \cdot \mu_* \cdot \tilde{\sigma}^{1/2}$$

where:
- $\mu_* = \pi/L$ is the EDC reference scale
- $\tilde{\sigma} = \sigma L^2 / \bar{M}_{\rm Pl}^2$ is the dimensionless brane tension

## Two-Route Consistency

Both routes are algebraically consistent:

$$\frac{M_X^{(A)}}{M_X^{(B)}} = 1 \pm 0.1$$

within stated threshold corrections.

## Closure of v61

This derivation closes the open variable in v61 (proton decay program note):
- **Before v62:** v61 depended on both $M_X$ and $\tilde{\sigma}$
- **After v62:** v61 now depends only on $\tilde{\sigma}$

## Status

**CONDITIONAL CLOSURE** — $M_X$ is fully determined once $\tilde{\sigma}$ is derived from EDC cosmology.

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (canonical single document) |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (35+ checks) |
| `README.md` | This file |
| `REPORT.md` | Technical details and metrics |
| `ACCEPTANCE.md` | Acceptance criteria verification |
| `RELEASE_NOTES.md` | Release notes |
| `release/` | Export bundle with canonical PDF |

## Verification

```bash
python3 recompute.py
```

All checks must pass for release qualification.

## v62 SoT Hash

`7a3d22e813e05675`

## Dependencies

- v51: $\mu_* = \pi/L$ (log hygiene lock)
- v55: $\alpha_3(\mu_*) = 1/\tilde{\sigma}$ (PS → QCD structure)
- v60: Layer A/B architecture (canonical document)
- v61: Proton lifetime formula (API-PD1)

## Layer Architecture

- **Layer A (Hash-Locked):** Structural derivations, group theory, geometric factors
- **Layer B (Quarantined):** Experimental comparison hooks (isolated)

## No-Fit Policy

$M_X$ is NOT fitted to:
- Proton lifetime experimental bounds
- GUT-scale estimates from PDG couplings
- Any other experimental anchor
