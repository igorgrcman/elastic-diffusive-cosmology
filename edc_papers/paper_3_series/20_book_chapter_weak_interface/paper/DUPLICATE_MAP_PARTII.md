# DUPLICATE_MAP_PARTII.md

Duplicate content map for EDC Part II: The Weak Sector.
Created: 2026-01-21 during Framework v2.0 alignment.

## Summary

This document tracks content duplications in Part II and their resolution strategy.

---

## 1. Pipeline Definition (Absorption → Dissipation → Release)

**Canonical Source:** `sections/03_unified_pipeline.tex` (§1.4)

**Found in:**
- `sections/01_how_we_got_here.tex:107` — Reference only (OK)
- `sections/02_geometry_interface.tex:116` — Reference only (OK)
- `sections/04a_unified_master_figure.tex:11,21` — Application (OK)
- `sections/05_neutron_story.tex:36` — Application (OK)
- `sections/07_case_tau.tex:501` — Application (OK)
- `sections/08_case_pion.tex:96` — Application (OK)
- `sections/13_summary.tex:17` — Summary reference (OK)
- `chapter_weak_interface.tex:247` — OLD FILE (not included in book)

**Status:** ✅ RESOLVED — All references point to §1.4 as canonical.

---

## 2. Frozen Projection Operator (P_frozen)

**Canonical Source:** `sections/03_unified_pipeline.tex` (eq. in §1.4)

**Found in:** Multiple case study files (05-10) — legitimate applications.

**Status:** ✅ RESOLVED — Canonical definition in §1.4, applied in case studies.

---

## 3. Ledger Closure Requirement

**Canonical Source:** `sections/03_unified_pipeline.tex:154-160` (§1.4)

**Found in:**
- `sections/02_geometry_interface.tex:56-58` — Prerequisite mention (OK)
- Case study files (05-10) — Applications (OK)
- `EDC_Part_II_Weak_Sector.tex:282` — Helper macro (OK)

**Status:** ✅ RESOLVED — Canonical definition in §1.4.

---

## 4. Open Problems Lists

**Canonical Source:** `sections/12_epistemic_map.tex` (§1.11)

**Found in:**
- `sections/13_summary.tex:46-55` — Forward reference only (OK)
- Case study files — Local open questions (per-case, OK)
- `CH3_electroweak_parameters.tex:831,853` — Chapter-specific (OK)
- `Z6_content_full.tex:999` — Chapter-specific (OK)

**Status:** ✅ RESOLVED — Consolidated list in §1.11, chapter-specific lists are scoped.

---

## 5. Theorem Duplication between Ch2 and Ch3

**RESOLVED (2026-01-22):** Ch3 restated theorems have been demoted to Corollaries.

### 5.1 Weinberg Angle

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:1279 | thm:weinberg_angle | PROOF (canonical) |
| CH3_electroweak_parameters.tex:109 | cor:ch3_weinberg | COROLLARY (numerical evaluation) |

**Resolution:** ✅ Ch3 now uses `\begin{corollary}` with cross-reference to Ch2.

### 5.2 Neutron Lifetime

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:875 | thm:neutron_lifetime | PROOF (canonical) |
| CH3_electroweak_parameters.tex:253 | cor:ch3_neutron | COROLLARY (numerical evaluation) |

**Resolution:** ✅ Ch3 now uses `\begin{corollary}` with cross-reference to Ch2.

### 5.3 Weak Coupling g²

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:1257 | thm:weak_coupling | DERIVATION |
| CH3_electroweak_parameters.tex:53 | thm:ch3_g2 | NUMERICAL application |

**Resolution:** ✅ Labels differ — no duplication issue.

**Status:** ✅ RESOLVED — Ch3 theorems demoted to Corollaries with cross-references.

---

## 6. Duplicate Content Files (Not Included in Book)

These files exist but are NOT included in EDC_Part_II_Weak_Sector.tex:

- `Z6_content.tex` — Condensed version (not included)
- `Z6_PROGRAM_COMPLETE_DERIVATION.tex` — Older version (not included)
- `Z6_PROGRAM_EXECUTIVE_SUMMARY.tex` — Standalone summary (not included)
- `chapter_weak_interface.tex` — Old Chapter 1 (not included)

**Status:** ✅ These files are archival/developmental; no action needed.

---

## 7. Epistemic Tag Definitions

**Canonical Source:** `EDC_Part_II_Weak_Sector.tex:79-105` (preamble)

Book-level legend in frontmatter (lines 366-389) matches canonical definitions.

**Status:** ✅ RESOLVED — Framework v2.0 compliant.

---

## 8. Invalid Bracket Tags (Framework v2.0 Compliance)

**RESOLVED (2026-01-22):** All invalid bracket tags eliminated from included sources.

### Framework v2.0 Rules
- Allowed evidence tags ONLY: `[BL]`, `[Der]`, `[Dc]`, `[I]`, `[Cal]`, `[P]`, `[M]`
- "open" must be plain text `(open)`, never a bracket status-tag
- No `[Def]` bracket tag — use `[M]` or no tag for definitions
- One evidence label per statement

### Files Fixed

| File | Issue | Fix Applied |
|------|-------|-------------|
| sections/05_neutron_story.tex | `[Def]/[Dc]`, `[Def]/[BL]` | → `[Dc]`, `[BL]` |
| sections/06_case_muon.tex | `[Def]`, `[Def]/[Dc]`, `[Def]/[P]` | → `{}`, `[Dc]`, `[P]` |
| sections/07_case_tau.tex | `[Def]/[P]`, `[Def]/[Dc]`, `[P]/[OPEN]` | → `[P]`, `[Dc]`, `[P] (open)` |
| sections/08_case_pion.tex | `[P]/[OPEN]`, `[Def]/[Dc]` | → `[P] (open)`, `[Dc]` |
| sections/04b_proton_anchor.tex | `[P]/[Dc]`, `[OPEN]` | Split to separate boxes, `(open)` |
| Z6_content_full.tex | `[OPEN]`, `[P]/[OPEN]` | → `(open)`, `[P] (open)` |
| CH3_electroweak_parameters.tex | `[OPEN]` | → `(open)` |
| figures/fig_pion_process_pipeline.tex | `[OPEN]` | → `(open)` |

**Status:** ✅ RESOLVED — All invalid tags eliminated.

---

## Actions Taken

1. [x] Pipeline references: All point to §1.4
2. [x] Open problems: Consolidated in §1.11
3. [x] Epistemic tags: Updated to Framework v2.0 standard
4. [x] Theorem cross-references: Added to Ch3 (cor:ch3_weinberg, cor:ch3_neutron)
5. [x] Invalid bracket tags: Eliminated `[OPEN]`, `[Def]`, combined statuses
6. [x] Ch3 theorem demotion: Converted restatements to Corollaries

---

## Verification Commands

```bash
# Check for invalid Framework v2.0 tags (should all return 0)
grep -r "\[OPEN\]" sections/*.tex Z6_content_full.tex CH3_electroweak_parameters.tex figures/*.tex | wc -l
grep -r "\[Def\]" sections/*.tex Z6_content_full.tex CH3_electroweak_parameters.tex | wc -l
grep -r "\\\\tagOpen" sections/*.tex | wc -l
grep -r "\\\\tagDef" sections/*.tex | wc -l

# Check for combined statuses (]/[ pattern) — expect only [E]/[t] dimensional analysis
grep -rE "\]/\[" sections/*.tex

# Check undefined references after build
grep -c "undefined" EDC_Part_II_Weak_Sector.log  # Should be 0
```
