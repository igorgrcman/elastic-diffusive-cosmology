# Part I G-Formula Correction Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Status:** Manifest complete; ready for future versioned action

---

## 1. Executive Verdict

The correction situation is **documented** and **ready for future versioned action**.

Five locations are flagged, classified, and recorded in the correction manifest.
The manifest is version-number agnostic and can guide a future Part I patch or
revision whenever one is undertaken. No further diagnosis is needed for these items.

---

## 2. Immediate vs Deferred Summary

| Class | Count | Items |
|-------|-------|-------|
| **Immediate** | 1 | F1: D11 claims table tag (`D` → `Dc`) |
| **Deferred** | 4 | F2: section title; F3: result box framing; F4: roadmap wording; F5: epilogue wording |

**Immediate** items should go into the next Part I version regardless of release scope.
**Deferred** items are desirable but can wait for a broader revision.

---

## 3. Highest-Priority Item

**F1: Chapter 0 claims table D11 — tag `D` → `Dc`**

This is the single most important correction because:
- It is a **formal tag** in the claims registry, the most structurally load-bearing
  epistemic label in Part I for Newton's constant
- The current tag (`D`) implies unconditional derivation, but the formula depends on
  postulate P6 — the dependencies column already says "P6, KK" but the status column
  does not reflect the conditionality
- The correction is minimal (one character) with no downstream ripple effects
- A reader consulting the claims table would currently conclude G is fully derived
  from first principles, which is stronger than warranted

---

## 4. Suitable Future Handling

The next correction should ideally be a **minimal versioned patch** — a small,
clean diff that corrects the D11 tag and increments the version. This is the
lowest-risk, highest-clarity approach.

However, a **broader revision** bundling F1–F5 together is also acceptable if a
larger Part I editorial pass is already planned.

An **erratum note** on the Zenodo record is acceptable as an interim measure if
a full version increment is not yet convenient.

The specific version number is left to editorial decision.

---

## 5. Recommended Next Step

**Stage a minimal Part I patch correcting F1 (D11 tag) with a version increment
and changelog entry.**

This is the single next operational step. It can be executed whenever the next
Part I editorial session occurs. The patch should:
1. Change D11 status from `D` to `Dc`
2. Add a one-line changelog entry
3. Increment the version number (editorial choice)
4. Upload to Zenodo as a new version

F2–F5 can ride along if desired, or be deferred.

---

## 6. Bottom Line

The Part I G-formula correction manifest is complete and action-ready. One immediate
correction (D11 tag: `D` → `Dc`) and four deferred enhancements are documented with
exact locations, current text, and recommended corrections. The manifest is
version-number agnostic and suitable for guiding the next Part I editorial pass.
No Part I text was modified. The epistemic chain from OPR-28 through the Part I
spot-check to this manifest is now closed at the documentation level.
