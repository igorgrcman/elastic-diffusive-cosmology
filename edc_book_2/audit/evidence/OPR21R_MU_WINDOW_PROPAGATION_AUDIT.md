# OPR-21R: μ-Window Propagation Audit Report

**Status**: COMPLETE
**Date**: 2026-01-25
**Sprint**: OPR-21R Propagation Sweep

---

## Executive Summary

This audit verifies that ALL universal μ-window claims ([25, 35)) have been either:
1. Removed entirely, or
2. Replaced with shape-dependent μ₃(V, κ, ρ) formulation, or
3. Explicitly labelled as "deprecated toy benchmark"

**Result**: ✓ PASS — 0 universal μ-window claims remain as unqualified statements.

---

## Search Patterns Used

```bash
# Primary search patterns
rg -n "\[25.*35\)|\[25,.*35\]" --type tex
rg -n "μ.*window|mu.*window|three.generation.*window" --type tex
rg -n "N_bound.*=.*3.*requires" --type tex
```

---

## Files Modified

| File | Lines Changed | Before | After |
|------|---------------|--------|-------|
| ch12_bvp_workpackage.tex | 39 | `[25, 35)` | `[μ₃⁻, μ₃⁺](V)` + OPR-21R reference |
| ch14_opr21_closure_derivation.tex | 408-421 | `[25, 35)`, `σΔ³ ∈ [52, 102]` | `[13, 17]` (physical), `σΔ³ ∈ [14, 24]` |
| ch14_bvp_closure_pack.tex | 357, 363 | `[25, 35)` | `[μ₃⁻, μ₃⁺](V)` + shape-dependent |
| ch15_opr01_sigma_anchor_derivation.tex | 16, 275-299, 330, 417-420 | `[25, 35)`, `σΔ³ ~ 75` | Shape-dependent, `σΔ³ ~ 19` |
| ch16_opr04_delta_derivation.tex | 574 | `[25,35]` | `[μ₃⁻, μ₃⁺]` |
| OPR_REGISTRY.md | 40, 302, 312 | `[25,35]` | Shape-dependent + OPR-21R note |

---

## Before/After Snippets

### ch15_opr01_sigma_anchor_derivation.tex (lines 273-275)

**BEFORE:**
```latex
The window for exactly three generations is $\mu \in [25, 35)$.
```

**AFTER:**
```latex
The window for exactly three generations is \textbf{shape-dependent}:
$\mu \in [\mu_3^-, \mu_3^+](V)$ where $\mu_3$ depends on the effective potential family.
For the physical domain wall $V_L = M^2 - M'$: $[\mu_3^-, \mu_3^+] \approx [13, 17]$ \tagDc{}.
For toy Pöschl--Teller benchmark: $[15, 18]$ \tagM{}.
```

### ch15_opr01_sigma_anchor_derivation.tex (lines 301-311)

**BEFORE:**
```latex
\sqrt{\sigma \Delta^3} \approx \frac{30}{0.866 \times 4} \approx 8.7
\sigma \Delta^3 \approx 75
```

**AFTER:**
```latex
\sqrt{\sigma \Delta^3} \approx \frac{15}{0.866 \times 4} \approx 4.3
\sigma \Delta^3 \approx 19 \quad \text{(physical V)}
```

### ch14_opr21_closure_derivation.tex (lines 408-421)

**BEFORE:**
```latex
$N_{\text{bound}} = 3$ for $\mu \in [25, 35)$
\sigma \Delta^3 \in [52, 102]
```

**AFTER:**
```latex
$N_{\text{bound}} = 3$ for $\mu \in [\mu_3^-, \mu_3^+](V)$
\textbf{Important (OPR-21R):} This window is \emph{shape-dependent}.
For the physical domain wall $V_L = M^2 - M'$: $[\mu_3^-, \mu_3^+] \approx [13, 17]$
\sigma \Delta^3 \in [14, 24] \quad \text{(physical V)}
```

### OPR_REGISTRY.md (line 40)

**BEFORE:**
```markdown
OPR-21 requirement (μ ∈ [25,35]) yields μ << 25
```

**AFTER:**
```markdown
OPR-21 requirement (μ ∈ [μ₃⁻, μ₃⁺](V)) yields μ << μ₃⁻
**Note (OPR-21R)**: μ₃ is shape-dependent. Physical domain wall: [13,17]. Toy PT: [15,18].
```

---

## Remaining [25, 35) References — Audit

| File | Line | Status | Reason |
|------|------|--------|--------|
| ch14_opr21_closure_derivation.tex | 506 | ✓ OK | Explicitly labelled "TOY BENCHMARK" |
| ch14_opr21_closure_derivation.tex | 515 | ✓ OK | Explicitly states "toy benchmark, not universal" |
| ch15_opr01_sigma_anchor_derivation.tex | 299 | ✓ OK | States "deprecated toy benchmark" |
| ch19_opr22_geff_from_exchange.tex | 683 | ✓ OK | Contrast statement: "not at [25,35] as estimated for PT" |
| code/output/*.md | multiple | ✓ OK | OPR-21R outputs correctly describe toy vs physical |
| audit/evidence/OPR21R_*.md | multiple | ✓ OK | Evidence reports correctly state shape-dependence |

---

## Final Checklist

- [x] **0 universal μ-window claims remain** — all [25,35) are now qualified
- [x] **Toy vs physical windows explicitly labelled** — every occurrence states potential family
- [x] **μ defined as μ = M₀ℓ everywhere** — verified in all chapters
- [x] **No new silent scale identifications introduced** — checked for δ/Δ/ℓ confusion
- [x] **σΔ³ constraint updated** — from ~75 (toy) to ~19 (physical)
- [x] **Build gate PASS** — 443 pages, XeLaTeX successful

---

## Canonical Statement (must appear in any three-generation discussion)

> "The three-generation condition is not a universal μ interval; it is determined by
> the spectral shape of the chosen effective potential family, hence μ₃ = μ₃(V, κ, ρ).
> For physical domain wall V_L = M² − M': [13, 17] [Dc].
> For toy Pöschl–Teller: [15, 18] [M].
> The oft-cited [25, 35) is deprecated."

---

## Files NOT Modified (and why)

| File | Reason |
|------|--------|
| ch19_opr22_geff_from_exchange.tex | Reference is already correctly contrasting with toy |
| 05_three_generations.tex | Chapter discusses existence of three generations, not μ-window |
| Z6_content_full.tex | Discusses generation counting concept, not BVP window |

---

## Gate Results

| Gate | Status | Evidence |
|------|--------|----------|
| Build | ✓ PASS | 443 pages, XeLaTeX |
| Notation | ✓ PASS | μ = M₀ℓ consistent throughout |
| No-smuggling | ✓ PASS | No SM observables introduced |
| Audit | ✓ PASS | 0 universal μ-window claims remain |

---

*Generated: 2026-01-25*
*Sprint: OPR-21R Propagation Sweep*
*Status: COMPLETE*
