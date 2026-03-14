# Book II OPR G-Exponent Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Status:** OPR layer corrected

---

## 1. Executive Verdict

The OPR layer for the G-exponent problem is now **corrected**, with no downstream
tag inconsistencies remaining in the Book II canonical chapters.

OPR-28 has been created in `edc_book_2/reorganized/appendices/opr_register.tex` with
status `[I]`, capturing the negative KK result, the non-uniqueness of the exponent
pair, and the exact upgrade condition. All existing G-formula references in Book II
(monograph BLOCK-003 and CLAIM-G-001) were already correctly tagged `[I]`.

---

## 2. Registry Status

| Dimension | Value |
|-----------|-------|
| **Entry** | OPR-28: G Formula Exponent Derivation |
| **Action** | Created (did not previously exist) |
| **Current status tag** | `[I]` (Identified by fitting; derivation not achieved) |
| **Negative result captured?** | YES — KK gives power −1, not +12 |
| **Non-uniqueness captured?** | YES — multiple exponent pairs fit G_CODATA |
| **Upgrade condition stated?** | YES — first-principles derivation from 5D action |
| **Priority** | Critical |
| **Summary table updated?** | YES |
| **Priority order updated?** | YES |

---

## 3. Canonical Text Status

Book II canonical chapters (reorganized) contain **no G-formula references** — the
G formula belongs to Part I (gravity sector), and Book II covers the weak sector.

The monograph (`src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex`) contains three
G-formula references (BLOCK-003 at two locations, CLAIM-G-001), all already correctly
tagged `[I]`. No corrections needed.

**No downstream tag inconsistencies were found.**

---

## 4. Upgrade Condition

The exact condition required for upgrade from `[I]` is:

> A first-principles derivation from the 5D EDC action that **uniquely** produces
> powers 12 and 13 and the factor $128\pi^2$ in the gravitational constant formula
> $G = c^4 R_\xi^{12}/(128\pi^2 \sigma r_e^{13})$.
>
> Alternatively: a proof that these are the unique exponents consistent with
> EDC postulates and dimensional constraints beyond the bare requirement $n + m = -1$.

Until this condition is met, the exponent structure remains `[I]`.

---

## 5. Recommended Next Step

**Spot-check Part I canonical text for G-formula tag consistency.**

OPR-28 is locked in Book II. The G formula's primary home is Part I. A read-only
spot-check of Part I should verify that the canonical gravity presentation also uses
`[I]` for the exponent structure, and flag any locations that might use `[Dc]` or
`[Cal]` for the exponents themselves.

---

## 6. Bottom Line

The G-exponent problem is now epistemically locked at OPR registry level. OPR-28
captures the negative KK result, the non-uniqueness finding, and the `[I]` status
with an explicit upgrade condition. No tag corrections were needed in Book II canonical
text — all existing references were already consistent. The registry gap is closed.
