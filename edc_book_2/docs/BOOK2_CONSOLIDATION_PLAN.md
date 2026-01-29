# Book 2 Consolidation Plan

**Generated:** 2026-01-29
**Purpose:** KORAK 6-7 output - spine design, single-source map, duplication hotspots

## A) Proposed Spine Sections

### Current "Front Door" Locations

| Section | File | Lines | Purpose |
|---------|------|-------|---------|
| Reader Contract | main.tex (front matter) | ~80 | Epistemic standard, projection principle |
| Reader Contract | 00_reader_contract.tex | 33 | Tag definitions |
| Chapter Map | main.tex | ~30 | Chapter overview |
| Epistemic Map | 12_epistemic_map.tex | 569 | OPR consolidation, k-channel box |
| Closure Status | ch20_epistemic_summary_closure_status.tex | 589 | Final summary |

### Recommended Spine Structure

**Target:** Unify reader orientation in ONE place (preferably expanded Reader Contract in main.tex front matter or §12).

```
SPINE SECTIONS (in order):

1. Reader Contract (existing, expand)
   - Epistemic tags (existing)
   - Projection principle (existing)
   - ADD: "How to read this book" flowchart
   - ADD: Gate Registry pointer

2. Gate Registry (NEW - add to §12)
   - Consolidated table of all gates
   - Cross-reference to chapter locations
   - Status for each gate

3. Scale Disambiguation (NEW - add to §12 or BVP workpackage)
   - Clarify δ_nucl vs δ_EW
   - Single source of truth for all δ scales

4. k-channel Applicability (existing in §12)
   - Already has Box ref - OK
   - Add pointer from other k-channel mentions

5. Overall Verdict (NEW - add to ch20)
   - Book 2 overall stoplight
   - Summary of GREEN/YELLOW/RED counts
```

## B) Single-Source Map

| Topic | Canon Location | Current Refs | Action |
|-------|----------------|--------------|--------|
| **Epistemic Tags** | main.tex lines 94-108 | 00_reader_contract.tex | OK - main.tex is canon |
| **Stoplight Legend** | _shared/meta/edc_stoplight_legend.tex | Included in main.tex | OK |
| **k-channel** | §12 + Box kchannel_spinchain_crossval | Derivation Library | OK - already consolidated |
| **Overlap Integral** | ch12_bvp_workpackage.tex §12.2 | ~40 mentions | ADD: Single definition box, pointer elsewhere |
| **δ (brane thickness)** | 05b_neutron_dual_route.tex Box | ~35 mentions | ADD: Scale disambiguation in §12 |
| **GF Gates** | 11_gf_derivation.tex §11.3 | ch11_*, ch12_* | ADD: Gate registry table |
| **BVP Gates** | ch14_opr21_closure_derivation.tex | ch14_* | ADD: to Gate registry |
| **Projection Principle** | main.tex Reader Contract | 01_how_we_got_here | OK |

## C) Duplication Hotspots

### 1. Overlap Integral Explanations (HIGH - ~40 mentions)

**Files with substantial explanations:**
- `06_neutrinos_edge_modes.tex` (lines 68, 86, 110, 155, 411, 591)
- `ch12_bvp_workpackage.tex` (lines 59, 123, 142, 228, 267, 308, 353, 403)
- `09_va_structure.tex` (lines 732, 848, 859, 861)
- `07_ckm_cp.tex` (lines 61, 744, 749, 905)
- `ch11_gf_full_closure_plan.tex` (lines 37, 70, 138)

**Recommendation:**
- Create `\ref{def:overlap-integral}` definition in ch12_bvp_workpackage.tex
- Replace other explanations with: "The overlap integral $I$ (Definition~\ref{def:overlap-integral}) controls..."

### 2. Brane Thickness δ Explanations (MEDIUM - ~35 mentions)

**Scale confusion identified:**
- `δ_nucl ≈ 0.1 fm` (nucleon/junction scale, proton Compton)
- `δ_EW ≈ 0.002 fm` (electroweak scale, MZ)
- `δ ≈ 1 fm` (sometimes used loosely for r_e)

**Files with δ definitions:**
- `05b_neutron_dual_route.tex` - Box with decision tree (best source)
- `ch10_electroweak_bridge.tex` - mentions δ ~ r_e ~ 1 fm
- `ch16_opr04_delta_derivation.tex` - kink width derivation
- `ch11_g5_ell_value_closure_attempt.tex` - δ ~ R_ξ ~ 10⁻³ fm

**Recommendation:**
- Add "Scale Disambiguation" subsection to §12 or BVP workpackage
- Define: δ_nucl, δ_EW, ℓ_brane clearly
- Add table: "Which δ for which calculation"

### 3. GF Constraint/Window Explanations (MEDIUM)

**Files:**
- `11_gf_derivation.tex` - main explanation
- `ch11_gf_sanity_skeleton.tex` - sanity checks
- `ch11_gf_full_closure_plan.tex` - closure plan
- `ch12_bvp_workpackage.tex` - BVP context

**Recommendation:**
- Keep main explanation in 11_gf_derivation.tex
- Other files: use `\ref` pointers

### 4. Book 3 Teaser Guardrails (LOW)

**Current:** `XX_teaser_book3_nuclear_mn_gn.tex` has preamble boxes

**Status:** OK - guardrails present

## D) Minimal Patch Set

### Immediate Patches (Safe to Apply)

1. **Add Gate Registry Table to §12** (ch12_epistemic_map.tex)
   ```latex
   \subsection{Consolidated Gate Registry}
   % Table with all gates, locations, status
   ```

2. **Add "How to Read" to Reader Contract** (main.tex front matter)
   ```latex
   \section*{How to Read This Book}
   \begin{enumerate}
   \item Start with Reader Contract (this section)
   \item Core claims: Chapters 1-7
   \item GF derivation: Chapters 8-10
   \item Open problems: Chapters 11-13
   \item OPR closures: Chapters 14-20
   \item Nuclear teaser: Appendix
   \end{enumerate}
   ```

3. **Add Overall Verdict Box to ch20**
   ```latex
   \begin{tcolorbox}[title=Book 2 Overall Verdict]
   GREEN: sin²θ_W, g², M_W, V-A structure
   YELLOW: G_F (self-consistent), τ_n (6%), masses
   RED: First-principles G_F, PMNS derivation
   \end{tcolorbox}
   ```

### Deferred Patches (Need Human Review)

1. **Overlap integral consolidation** - requires checking each mention
2. **δ scale disambiguation** - requires physics review
3. **Case chapter stoplights** - requires deciding specific verdicts

## E) Implementation Priority

| Priority | Task | Files | Est. Lines |
|----------|------|-------|------------|
| 1 | Gate Registry Table | 12_epistemic_map.tex | +30 |
| 2 | Overall Verdict Box | ch20_epistemic_summary_closure_status.tex | +20 |
| 3 | "How to Read" section | main.tex | +20 |
| 4 | Case chapter stoplights (6) | 05-10_case_*.tex | +60 each |
| 5 | Scale Disambiguation | 12_epistemic_map.tex | +40 |
| 6 | Overlap integral definition | ch12_bvp_workpackage.tex | +15 |

## F) Verification Checklist

After patches:
- [ ] `latexmk -xelatex main.tex` passes
- [ ] No new undefined references
- [ ] Gate Registry complete
- [ ] All case chapters have stoplights
- [ ] ch20 has overall verdict
- [ ] Reader Contract has "How to Read"

---
*Generated by Book 2 Consolidation Plan (KORAK 6-7)*
