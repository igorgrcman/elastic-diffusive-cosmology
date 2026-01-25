# OPR-07 I₄ Overlap Integral — Patch Report

**Date**: 2026-01-25
**Author**: Claude (AI assistant)
**Branch**: book2-ch07-openq-remediation-v1

---

## Summary

Fixed dimensional errors and profile formula issues in I₄ overlap integral sections.
Two files patched:
1. `src/sections/11_gf_derivation.tex` — Commit 865bdec
2. `src/CH3_electroweak_parameters.tex` — This commit

---

## Before/After Comparison

### Dimensional Analysis

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Dimension of I₄ | "length" (WRONG) | L⁻¹ = Energy (CORRECT) |
| Dimensional check | Missing | [G₅]×[I₄] = E⁻³×E = E⁻² = [G_F] ✓ |

### Gaussian Formula

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Integration domain | Full line assumed | Half-line [0,∞) explicit |
| Factor of 1/2 | Missing | Included |
| Formula | 1/(√(2π)σ) | 1/(2√(2π)σ) |

### Exponential Profile

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Existence | Not presented | f(ξ) = √(2m₀)e^{-m₀ξ} |
| I₄ result | Unknown | I₄ = m₀ exactly |
| Derivation | — | Full step-by-step |

### σ_L Heuristic

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Formula σ_L = λ/(2m₀) | Presented as meaningful | REMOVED |
| Justification | None | N/A (exponential is physical) |

### G₅ Gap

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Status | Implied as solvable | Explicitly OPEN (OPR-19) |
| Estimate | Presented as meaningful | Marked "illustrative only" |

---

## Key Equations Added

```latex
% Dimensional analysis
[I_4] = L^{-1} = \text{Energy}  % eq:ch3_I4_dimension

% Gaussian half-line (toy model)
I_4^{\text{Gauss}} = \frac{1}{2\sqrt{2\pi}\,\sigma_L}  % eq:ch3_I4_gauss_halfline

% Exponential profile (physical)
f_L(\xi) = \sqrt{2m_0} \, e^{-m_0\xi}  % eq:ch3_fL_exponential

% Exact result
I_4^{\text{exp}} = m_0  % eq:ch3_I4_exponential_m0
```

---

## Epistemic Tags Applied

| Claim | Tag | Justification |
|-------|-----|---------------|
| [I₄] = Energy | [M] | Pure dimensional analysis |
| I₄^Gauss = 1/(2√(2π)σ) | [M] | Gaussian integral |
| I₄^exp = m₀ | [Dc] | Conditional on exponential profile |
| G₅ undetermined | [P]/OPEN | OPR-19 blocks closure |

---

## Gate Verification

| Gate | Status | Evidence |
|------|--------|----------|
| Build | PASS | 387 pages, no errors |
| Notation | PASS | 959 ξ uses, 0 z violations |
| Canon | PASS | 574 [Dc] tags |

---

## Symbol Table Update

Added to `canon/notation/GLOBAL_SYMBOL_TABLE.md`:

```
| I₄ | `I_4` | Overlap integral | Mode overlap ∫|f_L|⁴dξ, [I₄]=Energy | 5D bulk | GeV | WORKING | — | eq:ch3_I4_exponential_m0 | NONE | I₄=m₀ for exponential |
```

---

## Files Modified

1. `src/CH3_electroweak_parameters.tex` — Lines 602-724 rewritten
2. `src/sections/11_gf_derivation.tex` — I₄ section (commit 865bdec)
3. `canon/notation/GLOBAL_SYMBOL_TABLE.md` — I₄ entry added

---

## Open Problems Linked

- **OPR-19**: Derive G₅ from 5D action — OPEN
- **OPR-21**: Derive I₄ from BVP solution — OPEN
- **OPR-22**: First-principles G_F derivation — OPEN (ultimate goal)

---

*Patch complete: 2026-01-25*
