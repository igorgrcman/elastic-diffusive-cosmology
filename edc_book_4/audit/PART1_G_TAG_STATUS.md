# Part I G-Formula Tag Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Status:** Mostly consistent; 5 locations flagged for versioned correction

---

## 1. Executive Verdict

Part I is **partially inconsistent** with OPR-28, but the inconsistencies are
**moderate, not severe**.

The OPR-28 exponent formula (`G = c⁴ R_ξ¹²/(128π² σ r_e¹³)`) does not appear in
Part I. Part I uses different G formulas, and Chapter 7's treatment is internally
well-caveated. However, 5 locations were flagged: 1 formal tag issue (D11 in the
claims table should be `Dc`, not `D`) and 4 rhetorical overstatements in titles,
boxes, and summaries.

A versioned correction pass is warranted but not urgent.

---

## 2. Flagged Locations Summary

**Total locations inspected:** 9 load-bearing G-formula appearances
**Consistent:** 4 (Chapter 7 internal caveats — red box, gray box, discussion, challenges)
**Partially consistent:** 2 (Chapter 0 D11, Chapter 7 green box)
**Inconsistent:** 3 (Chapter 7 section title, Chapter 6 roadmap, epilogue)

**Breakdown:**

| Severity | Count | Locations |
|----------|-------|-----------|
| HIGH | 1 | D11 claims table tag: `D` → should be `Dc` |
| MEDIUM | 2 | Chapter 7 section title ("Derivation"); green "Main Result" box (no `[I]` tag) |
| LOW | 2 | Chapter 6 roadmap ("is derived"); epilogue ("emerges from") |

---

## 3. Nature of the Problem

The issue is **both** explicit tag inconsistency **and** implicit rhetorical
overstatement.

- **Explicit tag:** D11 in the Chapter 0 claims table assigns status `D` (Derived)
  to `G_N = c²/(4πσ)`. This should be `Dc` because the formula depends on postulate
  P6 for the relationship between G₅ and membrane tension σ. The KK reduction step
  is mathematically derived, but the full chain is conditional.

- **Implicit rhetoric:** Chapter 7's section title says "Derivation" while its own
  body text says "not rigorously derived." Chapter 6 says "is derived" for a result
  that Chapter 7 frames as a "consistency check." The epilogue says "emerges from"
  which implies a completed mechanism.

- **Not a factual error:** The numerical result (6.71 × 10⁻¹¹ vs 6.674 × 10⁻¹¹,
  ~0.5% match) is correctly presented as a consistency check in Chapter 7. The physics
  content is not wrong — the labeling is imprecise.

---

## 4. Recommended Next Step

**Create a versioned correction manifest for Part I.**

Since Part I is published under DOI `10.5281/zenodo.18176174`, corrections must be
handled as:
- A new versioned release (v2) on Zenodo, or
- An explicit errata/annotation document, or
- A revision note appended to a future edition

The manifest should list all 5 candidate corrections with exact locations, current
text, proposed corrections, and severity. This ensures corrections are tracked as a
coherent set and applied through a proper versioning workflow.

---

## 5. Bottom Line

Part I's G treatment is internally honest in Chapter 7 (explicit caveats, consistency-
check framing, remaining-challenges list) but has 5 locations where tags or rhetoric
are stronger than warranted. The most significant is D11 in the claims table (`D`
should be `Dc`). These warrant a future versioned correction but do not constitute
false physics claims. The specific OPR-28 exponent formula does not appear in Part I.
