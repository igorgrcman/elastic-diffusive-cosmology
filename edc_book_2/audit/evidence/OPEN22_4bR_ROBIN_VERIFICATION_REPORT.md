# OPEN-22-4b-R: Robin BC Verification Report

**Status**: RESOLVED — FD implementation bug identified
**Date**: 2026-01-26
**Sprint**: OPEN-22-4b.2

---

## Executive Summary

The Robin BC (κ > 0) behavior observed in OPEN-22-4b.1 was **NOT physical decoupling** but rather a **BUG in the finite-difference implementation**. The original FD solver gives Neumann-like eigenvalues regardless of κ̂, failing to properly implement Robin boundary conditions.

**Impact on canonical results**: NONE. The Neumann (κ = 0) canonical path is correctly implemented and all G_eff tables remain valid.

---

## 1. Toy Verification Setup

### Problem Statement
Solve the eigenvalue problem for V = 0 on [0, ℓ]:
```
-f'' = λf
```
with symmetric Robin BC:
```
f'(0) + κf(0) = 0
f'(ℓ) - κf(ℓ) = 0
```

### Analytic Solution
General solution: f(ξ) = A cos(kξ) + B sin(kξ), where λ = k².

Applying BCs yields the **eigenvalue equation**:
```
(κ̂² - x²) tan(x) = 2κ̂ x    where x = √λ·ℓ, κ̂ = κℓ
```

**Special cases**:
- κ̂ = 0 (Neumann): tan(x) = 0 → x_n = nπ → x₁ = π ≈ 3.14159
- κ̂ → ∞ (Dirichlet): x_n = nπ (n ≥ 1)

---

## 2. Verification Results

### Analytic vs scipy.integrate.solve_bvp

| κ̂ | x₁(analytic) | x₁(scipy) | Error |
|----|--------------|-----------|-------|
| 0.0 | 3.14159 | 3.14159 | 0.000% |
| 1.0 | 2.33112 | 2.33112 | 0.000% |
| 10.0 | 3.88222 | 3.88222 | 0.000% |
| 100.0 | 3.20568 | 3.20567 | 0.000% |

**Verdict**: ✓ Analytic eigenvalue equation is CORRECT.

### Original FD Solver vs Analytic

| κ̂ | x₁(analytic) | x₁(FD) | Error | Status |
|----|--------------|--------|-------|--------|
| 0.0 | 3.14159 | 3.14002 | 0.05% | ✓ OK |
| 1.0 | 2.33112 | 3.13845 | 34.6% | ✗ BROKEN |
| 10.0 | 3.88222 | 3.13847 | 19.2% | ✗ BROKEN |
| 100.0 | 3.20568 | 3.13860 | 2.1% | ✗ BROKEN |

**Verdict**: ✗ Original FD solver Robin BC is BROKEN. Eigenvalues converge to ~π regardless of κ̂.

---

## 3. Bug Analysis

### Original FD Code (from open22_4b1_slice_family_sweep.py)
```python
if kappa_left == 0:
    H[0, 0] = 1.0 / h**2 + V[0]  # Neumann
else:
    H[0, 0] += kappa_left / h    # Robin (BUG!)
```

### Issues Identified

1. **Wrong base for Robin**: Code adds κ/h to the interior diagonal (2/h²) instead of the Neumann base (1/h²).

2. **Wrong sign**: The variational formulation gives +κ contribution, but the physical effect on eigenvalues requires proper ghost-point implementation with -2κ/h correction.

3. **Negligible correction**: With N = 2000, h ≈ 0.0005, κ = 1:
   - κ/h = 2000
   - 2/h² = 8 × 10⁶
   - Ratio: 0.025% — the Robin correction is negligible!

4. **Missing off-diagonal modification**: Ghost-point method requires H[0,1] = -2/h², but original code leaves it at -1/h².

### Root Cause
The FD discretization does not correctly implement the Robin BC constraint. The boundary modification affects only a tiny fraction of the matrix diagonal, while the eigenvalue should change by ~20-35% for κ̂ ∈ [1, 10].

---

## 4. Physical Implications

### What Robin BC Means Physically
- κ = 0 (Neumann): f' = 0 at boundary — mode is "flat" at edge, fully contained.
- κ > 0 (Robin): f' ∝ -κf at left, f' ∝ +κf at right — mode is "pushed" toward center.
- κ → ∞ (Dirichlet): f = 0 at boundary — mode completely suppressed at edges.

### Expected Eigenvalue Behavior
From the analytic formula, Robin BC eigenvalues depend non-monotonically on κ̂:
- For small κ̂: x₁ decreases from π (softer BC, lower eigenvalue)
- For κ̂ ≈ 1: x₁ ≈ 2.33 (minimum)
- For large κ̂: x₁ → π (Dirichlet limit)

This was completely masked by the FD bug, which gave x₁ ≈ π for all κ̂.

---

## 5. Impact Assessment

### Canonical Path (Neumann κ = 0)
**STATUS: UNAFFECTED**

The Neumann BC is correctly implemented in the FD solver:
- x₁(analytic) = π = 3.14159
- x₁(FD, N=2000) = 3.14002
- Error: 0.05% — well within tolerance

All G_eff tables computed with κ = 0 remain **VALID**.

### Robin Path (κ > 0)
**STATUS: INVALID — requires FD fix**

The Robin BC results from OPEN-22-4b.1 showing "N_bound → ∞" and "|f₁(0)|² → 0" were **artifacts of the FD bug**, not physical decoupling.

Proper Robin BC implementation is required to explore this regime.

---

## 6. Resolution

### For Canonical Path (DONE)
- OPEN-22-4b.1a marked Neumann as PASS
- Robin flagged as OPEN-22-4b-R
- No changes needed to G_eff tables

### For Robin Path (FUTURE)
1. Implement correct ghost-point Robin BC in FD solver
2. Or use scipy.integrate.solve_bvp for eigenvalue problems
3. Re-run physical (V ≠ 0) sweeps with corrected solver
4. Document if Robin BC has physical significance

### Tracking Item
**OPEN-22-4b-R** status updated:
- Previous: "Plausible causes: κ scaling, stiffness, decoupling"
- Current: "RESOLVED — FD implementation bug; canonical path unaffected"

---

## 7. Files Generated

| File | Description |
|------|-------------|
| `code/open22_4bR_robin_toy_verification.py` | Toy verification script |
| `code/output/open22_4bR_robin_toy_verification.json` | Full results JSON |
| `audit/evidence/OPEN22_4bR_ROBIN_VERIFICATION_REPORT.md` | This report |

---

## 8. Conclusions

1. **BUG CONFIRMED**: Original FD Robin BC implementation is broken.
2. **ANALYTIC VERIFIED**: Eigenvalue equation (κ̂² - x²)tan(x) = 2κ̂x is correct.
3. **CANONICAL SAFE**: Neumann (κ = 0) path is correctly implemented.
4. **ROBIN INVALID**: All κ > 0 results from OPEN-22-4b.1 are artifacts.

**Recommendation**: Close OPEN-22-4b-R as "resolved (bug)" and note that Robin exploration requires FD fix.

---

*Generated by OPEN-22-4b.2 sprint on 2026-01-26*
