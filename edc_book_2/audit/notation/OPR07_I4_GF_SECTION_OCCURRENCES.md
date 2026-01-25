# OPR-07 I₄ Overlap Integral — Section Occurrence Audit

**Date**: 2026-01-25
**Task**: Remediate I₄ dimensional errors and profile formulas
**Branch**: book2-ch07-openq-remediation-v1

---

## Grep Pattern Used

```bash
grep -rn "I_4\|overlap.*integral\|Quantitative Mode Overlap" src/
```

---

## Occurrences Found

| File | Line | Context | Status |
|------|------|---------|--------|
| `src/CH3_electroweak_parameters.tex` | 620 | Section "Quantitative Mode Overlap" | **PATCHED** |
| `src/sections/11_gf_derivation.tex` | ~200-280 | I₄ overlap discussion | **PATCHED** (commit 865bdec) |

---

## Errors Identified and Fixed

### Error 1: Dimensional Statement Wrong
- **Before**: "I₄ has dimension of length"
- **After**: "[I₄] = L⁻¹ = Energy (in natural units)" — eq:ch3_I4_dimension

### Error 2: Gaussian Half-Line Missing Factor
- **Before**: I₄ = 1/(√(2π)σ) — full-line formula
- **After**: I₄ = 1/(2√(2π)σ) — half-line with factor 1/2 — eq:ch3_I4_gauss_halfline

### Error 3: σ_L = λ/(2m₀) Dimensionally Problematic
- **Before**: Presented as meaningful heuristic
- **After**: REMOVED entirely; exponential profile is the physical model

### Error 4: Missing Exact Exponential Result
- **Before**: No clean closure
- **After**: I₄ = m₀ exactly for f(ξ) = √(2m₀)e^{-m₀ξ} — eq:ch3_I4_exponential_m0

### Error 5: G₅ Gap Not Marked
- **Before**: Naive estimate presented without caveat
- **After**: Explicitly marked as "illustrative only", OPR-19 referenced

---

## Labels Added

| Label | Location | Content |
|-------|----------|---------|
| `eq:ch3_I4_dimension` | CH3:642 | [I₄] = L⁻¹ = Energy |
| `eq:ch3_I4_gauss_halfline` | CH3:660 | I₄^Gauss = 1/(2√(2π)σ) |
| `eq:ch3_fL_exponential` | CH3:672 | f_L(ξ) = √(2m₀)e^{-m₀ξ} |
| `eq:ch3_I4_exponential_m0` | CH3:682 | I₄ = m₀ (exact) |
| `eq:ch3_I4_numerical` | CH3:692 | I₄ ~ 0.2 GeV |

---

## Cross-References

- **OPR-19**: G₅ derivation — OPEN (blocks quantitative closure)
- **OPR-21**: I₄ from BVP — OPEN (profile derivation)
- **OPR-22**: First-principles G_F — OPEN (ultimate goal)

---

## Verification

```bash
# Gates all PASS
latexmk -xelatex main.tex  # 387 pages
grep -c "\\[Dc\\]" src/**/*.tex  # 574 tags
grep -c "\\\\xi" src/**/*.tex  # 959 uses
```

---

*Audit complete: 2026-01-25*
