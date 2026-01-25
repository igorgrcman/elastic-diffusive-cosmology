# OPR-07 I₄ Overlap Integral — Patch Report

**Date**: 2026-01-25 (Updated)
**Author**: Claude (AI assistant)
**Branch**: book2-ch07-openq-remediation-v1

---

## Summary

Comprehensive remediation of I₄/G_F/G_5 logic across Book 2.
Three commits, 6 files patched, all acceptance criteria PASS.

---

## Commits

| SHA | Description |
|-----|-------------|
| `865bdec` | Initial 11_gf_derivation.tex I₄ fix |
| `905830e` | CH3_electroweak_parameters.tex comprehensive fix + symbol table |
| (this) | Comprehensive sweep: ch12, ch11, ch10 remaining issues |

---

## Files Modified

### Commit 1 (865bdec)
- `src/sections/11_gf_derivation.tex` — I₄ section rewrite

### Commit 2 (905830e)
- `src/CH3_electroweak_parameters.tex` — Lines 602-724 rewritten
- `canon/notation/GLOBAL_SYMBOL_TABLE.md` — I₄ entry added

### Commit 3 (this)
- `src/sections/ch12_bvp_workpackage.tex` — z→ξ, Gaussian domain fix
- `src/sections/ch11_g5_ell_value_closure_attempt.tex` — σ_L dimensional error fix
- `src/sections/ch10_electroweak_bridge.tex` — Domain specification added
- `src/sections/11_gf_derivation.tex` — Domain + exponential reference

---

## Before/After Comparison

### Dimensional Analysis

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Dimension of I₄ | "length" or unstated | L⁻¹ = Energy everywhere |
| Dimensional check | Missing in most places | [G₅]×[I₄] = [G_F] verified |

### Gaussian Formula

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Domain specification | Missing | "full-line" / "half-line" explicit |
| Factor of 1/2 | Missing for half-line | Included where applicable |
| Variable | z in some places | ξ everywhere |

### σ_L Heuristic

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| σ_L⁻¹ ~ I₄^{1/4} | Present (dimensionally wrong) | REMOVED |
| Localization scale | Confusing | m₀ = I₄ for exponential (exact) |

### Exponential Profile

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Existence | Missing in early chapters | f(ξ) = √(2m₀)e^{-m₀ξ} |
| I₄ result | Unknown | I₄ = m₀ exactly |
| Cross-references | None | §ch3_electroweak throughout |

### G₅ Status

| Aspect | BEFORE | AFTER |
|--------|--------|-------|
| Status | Implied as solvable | Explicitly OPEN (OPR-19) |
| Estimates | Presented as meaningful | Marked "illustrative only" |

---

## Acceptance Criteria Verification

| Criterion | Status | Command/Evidence |
|-----------|--------|------------------|
| gate_build.sh PASS | ✓ | 385 pages, no errors |
| gate_notation.sh PASS | ✓ | 951 ξ uses, 0 forbidden z |
| grep "I₄ dimension of length" = 0 | ✓ | No matches |
| grep I₄^{1/4} = 0 | ✓ | No matches |
| All Gaussian with domain | ✓ | full-line/half-line stated |
| G_F estimates "illustrative" | ✓ | OPR-19 referenced |

---

## Key Equations Now Correct

```latex
% Dimensional analysis (eq:ch3_I4_dimension)
[I_4] = L^{-1} = \text{Energy}

% Gaussian half-line (eq:ch3_I4_gauss_halfline)
I_4^{\text{Gauss}} = \frac{1}{2\sqrt{2\pi}\,\sigma_L}  \quad \text{(half-line)}

% Gaussian full-line (ch12_bvp_workpackage)
I_4^{\text{full}} = \frac{1}{\sqrt{2\pi}\sigma}  \quad \text{(full-line domain)}

% Exponential exact (eq:ch3_I4_exponential_m0)
f_L(\xi) = \sqrt{2m_0} \, e^{-m_0\xi}  \implies  I_4 = m_0  \quad \text{EXACT}

% Localization interpretation (ch11_g5_ell)
m_0 \equiv I_4 \approx 8 \text{ MeV}  \implies  \text{length} \sim m_0^{-1}
```

---

## Epistemic Tags Applied

| Claim | Tag | Justification |
|-------|-----|---------------|
| [I₄] = Energy | [M] | Pure dimensional analysis |
| I₄^Gauss (full/half) | [M] | Gaussian integral |
| I₄^exp = m₀ | [Dc] | Conditional on exponential profile |
| G₅ undetermined | OPEN | OPR-19 blocks closure |
| G_F formula structure | [Dc] | Form derived, numerics OPEN |

---

## OPR Cross-References

| OPR | Status | What's Blocked |
|-----|--------|----------------|
| OPR-19 | OPEN | G₅ value from 5D action |
| OPR-21 | OPEN | I₄ from BVP solution |
| OPR-22 | OPEN | First-principles G_F |

---

## Regression Prevention

All I₄/G_F content now follows these rules:
1. Every I₄ integral states its domain explicitly
2. Every dimensional claim includes [X] = ... check
3. Gaussian formulas distinguish full-line vs half-line
4. Exponential profile is the canonical physical model
5. G₅ closure is OPEN (OPR-19) — no pretense of derivation

---

*Patch complete: 2026-01-25*
