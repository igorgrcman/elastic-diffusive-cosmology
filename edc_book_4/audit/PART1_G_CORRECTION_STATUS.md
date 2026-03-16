# Part I G-Formula Correction Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Status:** Amended 2026-03-16 — F6 added (OPR-33 Rξ nomenclature relic in Ch 0)

---

## 1. Executive Verdict

The correction situation is **documented** and **ready for future versioned action**.

**Amendment:** `EDC_Trijaza_v1.md` (private repo, Phase B.4) formally classified the
Chapter 7 formula `G = ℓ_P² c⁴/(σ r_e³)` as **circular** — `ℓ_P = √(ℏG/c³)` contains
`G`. This upgrades F2 (section title) and F3 (result box) from DEFERRED/MEDIUM to
**IMMEDIATE/HIGH**. OPR-33 (`RXI_AMBIGUITY_AUDIT.md`) found a sixth item: Ch 0 line
1523 uses superseded Paper 2 α formula with wrong variables. The manifest now has
four immediate corrections (F1, F2, F3, F6) and two deferred enhancements (F4, F5).

---

## 2. Immediate vs Deferred Summary

| Class | Count | Items |
|-------|-------|-------|
| **Immediate** | 4 | F1: D11 claims table tag (`D` → `Dc`); F2: Ch 7 section title (circular formula called "Derivation") ↑; F3: Ch 7 result box (circular formula in green "Main Result" box) ↑; F6: Ch 0 line 1523 α formula uses superseded σ, Rξ instead of σ_eff, r_e (NEW) |
| **Deferred** | 2 | F4: roadmap wording; F5: epilogue wording |

**Immediate** items should go into the next Part I version regardless of release scope.
F2 and F3 were upgraded from DEFERRED to IMMEDIATE after `EDC_Trijaza_v1.md` confirmed
the Chapter 7 formula is circular. **Deferred** items are desirable but can wait.

---

## 3. Highest-Priority Item

**F1 + F2 + F3 + F6 are co-equal immediate corrections.**

**F1: Chapter 0 claims table D11 — tag `D` → `Dc`**
- Formal tag in claims registry; `D` implies unconditional derivation but formula
  depends on postulate P6; correction is minimal (one character)

**F2 + F3: Chapter 7 circularity — section title and result box** (UPGRADED)
- The formula `G = ℓ_P² c⁴/(σ r_e³)` is **circular**: `ℓ_P = √(ℏG/c³)` contains `G`
- Formally classified as circular/rejected in `EDC_Trijaza_v1.md` (§4.6)
- The section title "Derivation of Newton's Constant" and the green "Main Result"
  box both present this circular formula as a derivation — this is structurally
  misleading, not merely rhetorically imprecise
- A future Part I version must not present this formula as a derivation
- These were previously MEDIUM/DEFERRED; upgraded to HIGH/IMMEDIATE

**F6: Chapter 0 Prediction Pr1 — superseded α formula** (NEW from OPR-33)
- Line 1523: `α = m_e c²/(σ Rξ²)` uses old Paper 2 variables
- Chapter 6 §6.4 "Important Correction" supersedes this: corrected formula is
  `α = m_e c²/(σ_eff r_e²)` (line 674)
- Using current Rξ ~ 10⁻¹⁸ m yields α ~ 10⁹ — catastrophically wrong
- The formula only "works" with the superseded Paper 2 value Rξ = 136 r_e
- Source: `RXI_AMBIGUITY_AUDIT.md` (OPR-33)

---

## 4. Suitable Future Handling

The next correction should be a **versioned patch** correcting F1, F2, F3, and F6
together. F1 is a one-character tag fix. F2 requires renaming the section title.
F3 requires relabeling and recoloring the result box with a circularity note.
F6 requires replacing σ Rξ² with σ_eff r_e² in the Ch 0 prediction box.

A **broader revision** bundling F1–F5 together is also acceptable if a larger
Part I editorial pass is already planned.

An **erratum note** on the Zenodo record is acceptable as an interim measure if
a full version increment is not yet convenient, but given the circularity issue
in F2/F3, a versioned patch is strongly preferred.

The specific version number is left to editorial decision.

---

## 5. Recommended Next Step

**Stage a versioned Part I patch correcting F1 + F2 + F3 + F6 with a version
increment and changelog entries.**

This is the single next operational step. It can be executed whenever the next
Part I editorial session occurs. The patch should:
1. Change D11 status from `D` to `Dc` (F1)
2. Rename Ch 7 section title to remove "Derivation" (F2)
3. Relabel Ch 7 result box, add circularity note and `[I]` tag (F3)
4. Correct Ch 0 line 1523 α formula: σ Rξ² → σ_eff r_e² (F6)
5. Add changelog entries documenting tag correction, circularity fix, and
   superseded formula correction
6. Increment the version number (editorial choice)
7. Upload to Zenodo as a new version

F4–F5 can ride along if desired, or be deferred.

---

## 6. Bottom Line

The Part I G-formula correction manifest is amended and action-ready. Four immediate
corrections (F1: D11 tag `D` → `Dc`; F2: Ch 7 section title; F3: Ch 7 result box;
F6: Ch 0 superseded α formula) and two deferred enhancements (F4, F5) are documented.
F2 and F3 were upgraded from DEFERRED/MEDIUM to IMMEDIATE/HIGH after
`EDC_Trijaza_v1.md` confirmed the Chapter 7 formula is circular. F6 was found by
OPR-33 (`RXI_AMBIGUITY_AUDIT.md`). No Part I text was modified. The epistemic chain
from OPR-28 through the Trijaza classification to this manifest, and from OPR-33
through the Rξ ambiguity audit, is now closed at the documentation level.
