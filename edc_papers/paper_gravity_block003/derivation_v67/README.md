# BLOCK-004 Derivation v67: σ̃ Import Contract + Closure Map

## Overview

This document establishes the **σ̃ Import Contract** between the EDC cosmology lane and BLOCK-004 (Proton Decay). It defines:

1. A strict interface specification (A-APIσ1-3) for σ̃ flow
2. A complete closure map: σ̃ → α₃ → M_X → g_X → τ_p
3. Conditional closure logic (template mode when σ̃ unavailable)
4. Layer A firewall (no experimental values)

## Status

**CONDITIONAL CLOSURE** — Layer A complete, awaiting σ̃ from cosmology

When `sigma_tilde_value.json` is provided, all outputs close numerically.

## Document Metrics

| Metric | Value |
|--------|-------|
| Pages | 29 |
| Equation environments | 155 |
| Labels | 316 |
| Reviewer traps | 12 |
| recompute.py checks | 123 |

## Interface Specification

### A-APIσ1: Cosmology Provider
```
provide_sigma_tilde() → (σ̃, δσ̃, h_source)
```

### A-APIσ2: BLOCK-004 Consumer
```
consume_sigma_tilde(σ̃) → Layer A outputs
```

### A-APIσ3: Closure Propagation
```
propagate(σ̃) → (α₃, M_X, g_X, τ_p)
```

## Closure Map

```
σ̃ ──BOX-2──> α₃(μ*) = 1/σ̃
    │
    └──BOX-3──> M_X = C_X μ* σ̃^{1/2}
                 │
                 └──BOX-4──> g_X = √(4π/σ̃)
                              │
                              └──BOX-5──> τ_p = (C_X⁴/16π²) μ*⁴ σ̃⁴ / H_p
```

## Scaling Summary

| Observable | Scaling | Sensitivity |
|------------|---------|-------------|
| α₃(μ*) | σ̃^(-1) | -1 |
| M_X | σ̃^(1/2) | +1/2 |
| g_X | σ̃^(-1/2) | -1/2 |
| τ_p | σ̃^4 | +4 |

## Conditional Closure

When `sigma_tilde_value.json` exists:
- Read σ̃, δσ̃, source hash
- Compute all outputs numerically
- Status: NUMERICAL CLOSURE

Otherwise:
- All formulas remain symbolic
- Template placeholder used
- Status: CONDITIONAL CLOSURE

### JSON Schema

```json
{
  "sigma_tilde": <float>,
  "delta_sigma_tilde": <float>,
  "source_hash": "<string>",
  "source_version": "<string>",
  "cosmology_derivation": "<path>"
}
```

## Verification

```bash
python3 recompute.py
```

All 123 checks must pass.

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (123 checks) |
| `README.md` | This file |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | Release notes |

## SoT Hash

**v67:** `d8e9f0a1b2c34567`

**Parents:**
- v65: `c4e7f2a1b8d30965`
- v66: `b9d3e4f5a6c71082`
