# Part I G-Formula Correction Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Status:** Amended 2026-03-14 — circularity finding upgrades F2/F3 to IMMEDIATE

---

## 1. Executive Verdict

The correction situation is **documented** and **ready for future versioned action**.

**Amendment:** `EDC_Trijaza_v1.md` (private repo, Phase B.4) formally classified the
Chapter 7 formula `G = ℓ_P² c⁴/(σ r_e³)` as **circular** — `ℓ_P = √(ℏG/c³)` contains
`G`. This upgrades F2 (section title) and F3 (result box) from DEFERRED/MEDIUM to
**IMMEDIATE/HIGH**. The manifest now has three immediate corrections (F1, F2, F3) and
two deferred enhancements (F4, F5).

---

## 2. Immediate vs Deferred Summary

| Class | Count | Items |
|-------|-------|-------|
| **Immediate** | 3 | F1: D11 claims table tag (`D` → `Dc`); F2: Ch 7 section title (circular formula called "Derivation") ↑; F3: Ch 7 result box (circular formula in green "Main Result" box) ↑ |
| **Deferred** | 2 | F4: roadmap wording; F5: epilogue wording |

**Immediate** items should go into the next Part I version regardless of release scope.
F2 and F3 were upgraded from DEFERRED to IMMEDIATE after `EDC_Trijaza_v1.md` confirmed
the Chapter 7 formula is circular. **Deferred** items are desirable but can wait.

---

## 3. Highest-Priority Item

**F1 + F2 + F3 are co-equal immediate corrections.**

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

---

## 4. Suitable Future Handling

The next correction should be a **versioned patch** correcting F1, F2, and F3
together. F1 is a one-character tag fix. F2 requires renaming the section title.
F3 requires relabeling and recoloring the result box with a circularity note.

A **broader revision** bundling F1–F5 together is also acceptable if a larger
Part I editorial pass is already planned.

An **erratum note** on the Zenodo record is acceptable as an interim measure if
a full version increment is not yet convenient, but given the circularity issue
in F2/F3, a versioned patch is strongly preferred.

The specific version number is left to editorial decision.

---

## 5. Recommended Next Step

**Stage a versioned Part I patch correcting F1 + F2 + F3 with a version increment
and changelog entries.**

This is the single next operational step. It can be executed whenever the next
Part I editorial session occurs. The patch should:
1. Change D11 status from `D` to `Dc` (F1)
2. Rename Ch 7 section title to remove "Derivation" (F2)
3. Relabel Ch 7 result box, add circularity note and `[I]` tag (F3)
4. Add changelog entries documenting both the tag correction and circularity fix
5. Increment the version number (editorial choice)
6. Upload to Zenodo as a new version

F4–F5 can ride along if desired, or be deferred.

---

## 6. Bottom Line

The Part I G-formula correction manifest is amended and action-ready. Three immediate
corrections (F1: D11 tag `D` → `Dc`; F2: Ch 7 section title; F3: Ch 7 result box) and
two deferred enhancements (F4, F5) are documented. F2 and F3 were upgraded from
DEFERRED/MEDIUM to IMMEDIATE/HIGH after `EDC_Trijaza_v1.md` confirmed the Chapter 7
formula `G = ℓ_P² c⁴/(σ r_e³)` is circular (`ℓ_P` contains `G`). No Part I text was
modified. The epistemic chain from OPR-28 through the Trijaza classification to this
manifest is now closed at the documentation level.
