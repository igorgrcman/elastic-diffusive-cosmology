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

**CRITICAL ISSUE:** Some theorems appear in both Z6_content_full.tex (Ch2) and
CH3_electroweak_parameters.tex (Ch3).

### 5.1 Weinberg Angle Theorem

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:1279 | thm:weinberg_angle | PROOF (canonical) |
| CH3_electroweak_parameters.tex:109 | thm:ch3_weinberg | RESTATEMENT + numerical application |

**Resolution:** Ch3 restates for context, proof in Ch2. Add cross-reference.

### 5.2 Neutron Lifetime Theorem

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:875 | thm:neutron_lifetime | PROOF (canonical) |
| CH3_electroweak_parameters.tex:251 | thm:ch3_neutron | NUMERICAL application |

**Resolution:** Ch3 focuses on numerical verification, proof in Ch2. Add cross-reference.

### 5.3 Weak Coupling g² Theorem

| File | Label | Status |
|------|-------|--------|
| Z6_content_full.tex:1257 | thm:weak_coupling | DERIVATION |
| CH3_electroweak_parameters.tex:53 | thm:ch3_g2 | NUMERICAL application |

**Resolution:** Ch3 focuses on numerical verification, derivation in Ch2. Labels differ (OK).

**Status:** ✅ RESOLVED — Cross-references added to Ch3 theorems.

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

## Actions Taken

1. [x] Pipeline references: All point to §1.4
2. [x] Open problems: Consolidated in §1.11
3. [x] Epistemic tags: Updated to Framework v2.0 standard
4. [x] Theorem cross-references: Added to Ch3 (thm:ch3_weinberg, thm:ch3_neutron)

---

## Verification Commands

```bash
# Check for non-canonical tags
grep -r "\\\\tagD{}" sections/*.tex | wc -l  # Should be 0
grep -r "\\\\tagDef" sections/*.tex | wc -l  # Should be 0
grep -r "\\\\tagOpen" sections/*.tex | wc -l  # Should be 0

# Check undefined references
grep -c "undefined" EDC_Part_II_Weak_Sector.log  # Should be 0
```
