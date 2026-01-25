# OPR-07 I₄ Overlap Integral — Section Occurrence Audit

**Date**: 2026-01-25 (Updated)
**Task**: Remediate I₄ dimensional errors and profile formulas
**Branch**: book2-ch07-openq-remediation-v1

---

## Grep Patterns Used

```bash
grep -rn "I_4\|I₄" src/**/*.tex
grep -rn "dimension.*length\|has dimension of" src/**/*.tex
grep -rn "Gaussian.*overlap\|sigma_L\|mode overlap" src/**/*.tex
grep -rn "Wait—\|Let me re-examine" src/**/*.tex
```

---

## Complete Occurrence Inventory

| File | Lines | Context | Status |
|------|-------|---------|--------|
| `CH3_electroweak_parameters.tex` | 620-732 | "Quantitative Mode Overlap" section | **PATCHED** (commit 905830e) |
| `sections/11_gf_derivation.tex` | 68-78, 360-480 | I₄ overlap discussion | **PATCHED** (commits 865bdec, this) |
| `sections/ch12_bvp_workpackage.tex` | 220-247 | Gaussian toy model | **PATCHED** (this commit) |
| `sections/ch11_g5_ell_value_closure_attempt.tex` | 265-271 | σ_L heuristic | **PATCHED** (this commit) |
| `sections/ch10_electroweak_bridge.tex` | 122-125 | I₄ controls G_F | **PATCHED** (this commit) |
| `sections/ch11_gf_full_closure_plan.tex` | 53, 60, 92 | Closure spine | **COMPLIANT** ✓ |
| `sections/ch11_opr20_attemptE_prefactor8_derivation.tex` | 240, 247, 422 | BVP context | **COMPLIANT** ✓ |
| `sections/ch11_opr20_attemptF_mediator_bvp_junction.tex` | 51 | Formula reference | **COMPLIANT** ✓ |
| `sections/09_va_structure.tex` | 731 | BVP reference | **COMPLIANT** ✓ |

---

## Errors Identified and Fixed

### Error 1: Dimensional Statement Wrong (FIXED - commit 905830e)
- **Before**: "I₄ has dimension of length"
- **After**: "[I₄] = L⁻¹ = Energy (in natural units)" — eq:ch3_I4_dimension

### Error 2: Gaussian Half-Line Missing Factor (FIXED - commit 905830e)
- **Before**: I₄ = 1/(√(2π)σ) — full-line formula used without domain
- **After**: I₄ = 1/(2√(2π)σ) — half-line with factor 1/2 — eq:ch3_I4_gauss_halfline

### Error 3: σ_L Heuristic Dimensionally Wrong (FIXED - this commit)
- **Before**: σ_L⁻¹ ~ I₄^{1/4} in ch11_g5_ell_value_closure_attempt.tex
- **After**: Replaced with dimensionally correct I₄ = m₀ relation

### Error 4: Missing Domain Specifications (FIXED - this commit)
- **Before**: `∫|f_L|⁴dξ` without explicit domain
- **After**: `∫₀^∞ |f_L(ξ)|⁴ dξ` with dimension note

### Error 5: z instead of ξ (FIXED - this commit)
- **Before**: `f ∝ e^{-z²/2σ²}` in ch12_bvp_workpackage.tex
- **After**: `f ∝ e^{-ξ²/2σ²}` with domain caveat

### Error 6: G₅ Gap Not Marked (FIXED - commit 905830e)
- **Before**: Naive estimate presented without caveat
- **After**: Explicitly marked "illustrative only", OPR-19 referenced

---

## Labels Added

| Label | Location | Content |
|-------|----------|---------|
| `eq:ch3_I4_dimension` | CH3:642 | [I₄] = L⁻¹ = Energy |
| `eq:ch3_I4_gauss_halfline` | CH3:660 | I₄^Gauss = 1/(2√(2π)σ) |
| `eq:ch3_fL_exponential` | CH3:672 | f_L(ξ) = √(2m₀)e^{-m₀ξ} |
| `eq:ch3_I4_exponential_m0` | CH3:682 | I₄ = m₀ (exact) |
| `eq:ch3_I4_numerical` | CH3:692 | I₄ ~ 0.2 GeV |
| `eq:ch11_I4_required` | ch11_g5:263 | I₄ = 8 MeV (back-solved) |

---

## Cross-References to OPRs

| OPR | Description | Status | Blocking |
|-----|-------------|--------|----------|
| OPR-19 | G₅ from 5D action | OPEN | Quantitative G_F |
| OPR-21 | I₄ from BVP | OPEN | Profile derivation |
| OPR-22 | First-principles G_F | OPEN | Ultimate goal |

---

## Acceptance Criteria Verification

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Build PASS | ✓ | 385 pages, no errors |
| No "I₄ dimension of length" | ✓ | grep returns 0 hits |
| No I₄^{1/4} error | ✓ | grep returns 0 hits |
| No z in 5D context | ✓ | grep e^{-z^2} returns 0 hits |
| All Gaussian formulas have domain | ✓ | full-line/half-line specified |
| G_F estimates labeled "illustrative" | ✓ | OPR-19 referenced |
| ξ notation | ✓ | 951 uses |

---

## Commits

1. `865bdec` — Fix 11_gf_derivation.tex I₄ section
2. `905830e` — Fix CH3_electroweak_parameters.tex + symbol table
3. (this commit) — Fix ch12, ch11, ch10 remaining issues

---

*Audit complete: 2026-01-25*
