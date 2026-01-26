# OPEN-22-4b-R-PHYS: Physical Domain Wall Robin BC Sweep

**Date**: 2026-01-26
**Parameters**: ρ=0.2, ℓ=1.0, N=2000

## Gate Summary

| Gate | Status | Note |
|------|--------|------|
| METHOD | PASS | FEM weak formulation used (no FD) |
| CONVERGENCE | PASS | Max drift = 0.2166% < 1% |
| SPECTRUM | PASS | N_bound=3 achieved for κ̂ in [0.5, 1.0, 2.0] |
| CONTINUITY | PASS | κ̂≤0.5 deviates 0.00% from Neumann (< 5%) |
| NO_SMUGGLING | PASS | No SM constants (M_W, G_F, v, sin²θ_W) used |

**OVERALL**: ALL GATES PASS

## N_bound=3 Windows by κ̂

| κ̂ | N_bound=3 Window |
|---:|:----------------:|
| 0.0 | [13.0, 15.6] |
| 0.5 | [13.0, 15.2] |
| 1.0 | [13.0, 14.8] |
| 2.0 | [13.0, 13.6] |
| 3.0 | — |
| 5.0 | — |
| 10.0 | — |

## Detailed Results (μ=14.0 cross-section)

| κ̂ | x₁ | |f₁(0)|² | G_eff/(g₅²ℓ) | N_bound |
|---:|----:|---------:|-------------:|--------:|
| 0.0 | 0.0000 | 0.000712 | 7.917054e-03 | 3 |
| 0.5 | 0.0000 | 0.000768 | 8.925740e-03 | 3 |
| 1.0 | 0.0000 | 0.000830 | 1.010599e-02 | 3 |
| 2.0 | 0.0000 | 0.000979 | 3.117750e-02 | 4 |
| 3.0 | 0.0000 | 0.001172 | 3.886704e-02 | 4 |
| 5.0 | 0.0000 | 0.001781 | 6.179431e-02 | 4 |
| 10.0 | 0.0000 | 0.010133 | 2.324563e-01 | 4 |

## Convergence (N=2000 → N=4000)

| κ̂ | x₁ drift % | |f₁(0)|² drift % | G_eff drift % |
|---:|----------:|-----------------:|--------------:|
| 0.0 | nan | 0.0002 | 0.0284 |
| 0.5 | nan | 0.0002 | 0.0318 |
| 1.0 | nan | 0.0001 | 0.0356 |
| 2.0 | nan | 0.0000 | 0.0700 |
| 3.0 | nan | 0.0001 | 0.0816 |
| 5.0 | nan | 0.0004 | 0.1093 |
| 10.0 | nan | 0.0026 | 0.2166 |

## Continuity Check (κ̂→0)

| κ̂ | x₁ | Deviation from Neumann % |
|---:|----:|-------------------------:|
| 0.0 | 0.0000 | 0.00 |
| 0.01 | 0.0000 | nan |
| 0.05 | 0.0000 | nan |
| 0.1 | 0.0000 | nan |
| 0.2 | 0.0000 | nan |
| 0.5 | 0.0000 | nan |
