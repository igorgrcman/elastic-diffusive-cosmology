# BLOCK-004 Derivation v66: Layer B τ_p(σ̃) Bounds Comparison

## Overview

This document provides a **QUARANTINED** Layer B analysis adapter that:

1. **Imports** the symbolic proton lifetime formula τ_p(σ̃) from Layer A (v65)
2. **Sweeps** σ̃ over a declared range (NOT fitted)
3. **Computes** lifetime intervals using bounded template uncertainties
4. **Compares** these intervals to published experimental limits
5. **Extracts** required minimum σ̃ values for consistency

## Key Features

- **Quarantine Protocol:** All experimental values are isolated in `quarantine/`
- **No-Backflow Theorem:** Layer A remains unchanged (hash-locked)
- **No-Fit Policy:** σ̃ is SWEPT, not fitted (no χ², no optimization)
- **Layer Markers:** Explicit start/end markers for each layer

## Document Metrics

| Metric | Value |
|--------|-------|
| Pages | 29 |
| Equation environments | 162 |
| Labels | 341 |
| recompute.py checks | 104 |

## Layer Architecture

```
Layer A (v65) ─────────────────────────────────────────────────────
  │
  │  τ_p = (C_X^4/16π²) · μ*^4 · σ̃^4 / H_p  [hash-locked]
  │
  │  READ-ONLY IMPORT
  ▼
Layer B (v66) ─────────────────────────────────────────────────────
  │
  │  B-API1: Template instantiation
  │  B-API2: Interval computation
  │  B-API3: Comparison ratio R(σ̃)
  │  B-API4: Feasibility extraction
  │
  │  QUARANTINE BOUNDARY
  ▼
Quarantine (Q) ────────────────────────────────────────────────────

  τ_bound^(exp) = 2.4 × 10^34 years  [Super-K, PDG]
  α_H = 0.0090 ± 0.0015 GeV³  [lattice QCD]

  CONFINED: Q ∩ L_A = ∅
```

## B-API Definitions

| API | Function | Description |
|-----|----------|-------------|
| B-API1 | Template instantiation | Apply envelope bounds to τ_p |
| B-API2 | Interval computation | Compute [τ_p^(min), τ_p^(max)] |
| B-API3 | Comparison ratio | R(σ̃) = τ_bound^(exp) / τ_p^(min)(σ̃) |
| B-API4 | Feasibility extraction | Solve R(σ̃) = 1 for σ̃_min^(req) |

## Quarantine Contents

The `quarantine/` directory contains:

- `EXTERNAL_INPUTS.md`: Human-readable experimental values
- `inputs.json`: Machine-readable data for sweeps

**All values in quarantine are:**
- External experimental results (Super-K, PDG)
- Lattice QCD estimates (RBC/UKQCD, JLQCD)
- Used ONLY for comparison in Layer B
- NEVER imported into Layer A

## Verification

```bash
python3 recompute.py
```

All 104 checks must pass.

## Key Results

### Scaling Law
```
τ_p ∝ σ̃^4
```

### Sensitivity
```
∂ln(τ_p)/∂ln(σ̃) = 4
∂ln(τ_p)/∂ln(H_p) = -1
```

### Required Minimum (symbolic)
```
σ̃_min^(req) = [τ_bound^(exp) · H_p · 16π² / C_X^4 μ*^4]^(1/4)
```

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Verification script (104 checks) |
| `quarantine/` | QUARANTINED experimental inputs |
| `README.md` | This file |
| `REPORT.md` | Technical details |
| `ACCEPTANCE.md` | Acceptance criteria |
| `RELEASE_NOTES.md` | Release notes |

## SoT Hash

**v66:** `b9d3e4f5a6c71082`

**Parent (v65):** `c4e7f2a1b8d30965`
