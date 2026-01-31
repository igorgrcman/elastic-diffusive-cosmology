# TIER-1 Backfill Report

**Date:** 2026-01-31
**Branch:** `backfill/tier1-v1`
**Build Status:** PASS (153 pages, up from 149)

---

## Summary

Three TIER-1 gaps backfilled with minimal donor content:

| GAP-ID | Description | Target File | Insertion Location | Lines Added | Dictionary Box |
|--------|-------------|-------------|-------------------|-------------|----------------|
| GAP-5  | SSB mechanism vs EDC mass | chapter_06_electroweak.tex | After Mediator Identity box | ~38 | Y |
| GAP-11 | Yukawa from overlap integrals | chapter_07_leptons.tex | After mass hierarchy section | ~40 | Y |
| GAP-14 | μ-window generation constraint | chapter_08_generations.tex | After KK truncation discussion | ~38 | N |

---

## GAP-5: Mass Mechanism Dictionary (EDC vs SSB)

**Problem:** Chapter 6 mentioned mediator masses from BVP but lacked explicit comparison to SM Higgs mechanism.

**Donor:** `src/sections/ch11_opr20_attemptG_BC_provenance.tex:168` (Higgs mechanism reference)

**Backfill:** Added dictionary box "Mass Generation Mechanisms":
- SM SSB pathway: Higgs VEV → gauge boson masses → Yukawa couplings [BL]
- EDC pathway: BVP eigenvalue → geometric mass → overlap integrals [Dc]
- Explicit comparison table showing these are distinct frameworks

**Epistemic Tags:**
- SM mechanism: [BL]
- EDC mechanism: [Dc]
- Distinction: clearly stated as alternative, not equivalent

**Tag Changes:** None (new content only)

---

## GAP-11: Yukawa from Overlap Integrals

**Problem:** Chapter 7 described lepton mass hierarchy from mode tower but lacked explicit bridge to SM Yukawa concept.

**Donor:** `src/sections/ch11_opr20_attemptE_prefactor8_derivation.tex:238-250` (overlap integral I_4)

**Backfill:** Added mechanism box + dictionary box:
- Overlap integral formula: $I_4^{(n)} = \int |f_n(\xi)|^4 d\xi$ [Der]
- Physical meaning: higher modes → more nodes → smaller overlap
- Dictionary: SM Yukawa $y_f$ ↔ EDC overlap $I_4$ [I]

**Epistemic Tags:**
- Overlap integral formula: [Der]
- Physical interpretation: [Dc]
- SM mapping: [I] (structural identification, not derivation)

**Tag Changes:** None (new content only)

---

## GAP-14: μ-Window Generation Constraint

**Problem:** Chapter 8 mentioned KK truncation mechanism but lacked explicit barrier parameter constraint.

**Donor:** `src/sections/05_three_generations.tex:273-289` (lifetime/barrier parameter)

**Backfill:** Added mechanism box "Barrier Parameter Constraint":
- Definition: $\mu = \int m_{\text{eff}}(\xi')/\Lambda \, d\xi'$ [Der]
- Stability window: $\mu_0, \mu_1, \mu_2 \gtrsim 5$ (stable); $\mu_3 \lesssim 1$ (unstable)
- Closure target: derive $V(\xi)$ producing this "cliff" between n=2 and n=3

**Epistemic Tags:**
- Barrier definition: [Der]
- Window values: [P] (closure target, not derived)
- Status: [Open] (requires OPR-12)

**Tag Changes:** None (new content only)

---

## Verification

```
pdflatex -interaction=nonstopmode main.tex
Output written on main.pdf (153 pages)
```

No new errors. Build increased by 4 pages from TIER-0.

---

## Files Modified

1. `part2/chapter_06_electroweak.tex` - GAP-5 backfill (+38 lines)
2. `part2/chapter_07_leptons.tex` - GAP-11 backfill (+40 lines)
3. `part2/chapter_08_generations.tex` - GAP-14 backfill (+38 lines)

---

## Safety Checks Performed

1. **"predict"/"therefore" scan:** No new unqualified predictions introduced
2. **[Der] for SM matches:** Verified—no [Der] used for SM identifications; all SM mappings use [Dc] or [I]
3. **SM term pairing:** All SM terms (Higgs, Yukawa, SSB) paired with [BL] and dictionary [Dc]

---

## Commit Message

```
backfill(tier1): GAP-5 SSB + GAP-11 Yukawa overlaps + GAP-14 generations mu-window

- GAP-5: Add EDC vs SM mass mechanism dictionary box
- GAP-11: Add overlap integral formula for fermion masses
- GAP-14: Add μ-window barrier constraint for mode stability

All with clear epistemic tags: [Der], [Dc], [I], [BL].
Build: 153 pages, no new errors.
```

---

## Cumulative Status

| TIER | Gaps Backfilled | Pages Added |
|------|-----------------|-------------|
| TIER-0 | GAP-1, GAP-4, GAP-10 | 4 pages (145→149) |
| TIER-1 | GAP-5, GAP-11, GAP-14 | 4 pages (149→153) |
| **Total** | 6 gaps | 8 pages |

---

## Next Steps (TIER-2)

Remaining gaps requiring deeper derivation or new content:
- GAP-2: Effective potential $V(\xi)$ derivation
- GAP-6: CKM matrix from overlap geometry
- GAP-12: BVP eigenvalue explicit solution
