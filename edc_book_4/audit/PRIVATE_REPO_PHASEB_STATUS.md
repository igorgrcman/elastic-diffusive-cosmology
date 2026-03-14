# Private Repo Phase B Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration` (main repo)
**Target repo:** `EDC_Research_PRIVATE`
**Status:** Triage complete, no actions taken, read-only pass

---

## 1. Executive Verdict

The private repo is now **better triaged** and **partially visible** but **not yet
cleaned**. Phase B corrected significant Wave 1 data errors (no `.cache/` exists,
actual untracked count is 256 entries not 5,181) and completed deep inspection of the
5D research branches and the mass-difference research cluster.

**Not ready for broad cleanup** — the working tree mixes source with build artifacts
across all clusters, and 49 tracked deletions from active restructuring work create
an inconsistent state that should be resolved intentionally, not as part of triage.

**Ready for a narrow source-only preservation commit** in `derivations/mass_difference/`
if desired.

---

## 2. Phase B Outcome Table

| Area | Before (Wave 1) | After (Phase B) | Status | Notes |
|------|-----------------|-----------------|--------|-------|
| Cache/build visibility | "4,152 .cache/ files" | `.cache/` does not exist; 0 cache files | **CORRECTED** | Wave 1 count was erroneous |
| Untracked count | "5,181 files" | 256 directory-collapsed entries | **CORRECTED** | Actual scale is ~5x smaller than reported |
| Untracked research visibility | "~1,029 non-cache" | 256 entries classified by top-level dir (106 derivations, 80 releases, 51 kb, etc.) | **IMPROVED** | Clusters identified and sized |
| Tracked modification clarity | "15 files, 2 clusters" | 6 source + 9 build artifacts across 2 clusters | **IMPROVED** | Source/artifact separation identified |
| `research/5d-action-derivation` visibility | "Listed as branch #19" | **Does not exist** in private repo | **CORRECTED** | Branch was from main repo inventory |
| Closest 5D branches | Not inspected | `research/neutron-proton-mass-difference-5D` (1,710 files) inspected; contains G-exponent failure certificate | **INSPECTED** | Weak sector focus, not gravity exponents |
| `derivations/mass_difference/` visibility | "~18 untracked files" | 21 untracked files classified (11 .md, 3 .tex, 4 .log, 3 .pdf) | **IMPROVED** | Source/artifact separation identified |
| Preservation readiness | "Phase B session needed" | Source-only commit possible; full commit deferred | **PARTIALLY READY** | Narrow action safe; broad action not |
| .gitignore coverage | Partial (no .bbl/.blg/.bcf) | Same — no changes made | **UNCHANGED** | Safe additions identified but deferred |

---

## 3. Can Safe Cleanup Now Proceed?

**Partially.**

**What CAN proceed safely:**
- A narrow source-only commit of untracked `.md` and `.tex` files in `derivations/mass_difference/`
- Adding `*.bbl`, `*.blg`, `*.bcf`, `*.run.xml` to `.gitignore` (always regenerable)

**What CANNOT proceed safely yet:**
- Committing the 15 tracked modifications (mixed source + artifacts)
- Committing the 49 tracked deletions (active restructuring, needs intentional resolution)
- Broad untracked file triage (106 derivation entries, 80 release entries need individual assessment)
- Stash conversion (working tree still dirty)

**Why:** The fundamental blocker is that the working tree is on an active restructuring
branch (`restructure/paper3-companion-doi-split`) with intentional deletions and
in-progress modifications. Cleanup actions risk entangling with restructuring state.

---

## 4. Is `research/5d-action-derivation` a Higher-Priority Research Audit Target?

**No — because it does not exist.**

The branch `research/5d-action-derivation` is not present in the private repo (26 branches
checked) or the main repo. The prompt's reference was based on a Wave 1 inventory error
that mixed main-repo and private-repo branch lists.

**However, the G-exponent question has a clear answer from existing evidence:**

The closest 5D branch (`research/neutron-proton-mass-difference-5D`) contains
`derivations/critical/task_b5_power_derivation.md`, which documents an explicit
investigation of G powers 12, 13, and 128π². The investigation concluded:

> "DERIVATION NOT ACHIEVED — Powers remain IDENTIFIED (I), not DERIVED (D)"
>
> "No known physical mechanism generates power 12 from 5D integration.
>  Standard Kaluza-Klein predicts power -1, not +12."

The G-exponent problem remains **fully open**. The private repo's contribution is a
well-documented negative result (honest failure certificate), not a derivation lane.
An untracked file (`08_gravity_topological_ops.tex`, 471 lines) presents standard KK
reduction G₄ = G₅/(2πR_ξ) but explicitly marks G₅ derivation as an open problem.

**Research audit recommendation:** The `task_b5_power_derivation.md` failure certificate
should be cross-referenced in any future G-derivation effort to avoid redundant work.

---

## 5. Recommended Next Safe Step

**Execute a narrow source-only preservation commit for the `derivations/mass_difference/`
untracked research files.**

Specifically:
1. In `EDC_Research_PRIVATE`, on `restructure/paper3-companion-doi-split`
2. Stage only the 14 research source files: 11 `.md` + 3 `.tex` (exclude `.log`, `.pdf`)
3. Include `08_gravity_topological_ops.tex` (framework section, 471 lines)
4. Commit with message: `preserve: untracked mass-difference research sources + gravity topology section`
5. Push to origin

This is the safest, narrowest, highest-value action: 15 clearly valuable research files,
no build artifacts, no ambiguity.

---

## 6. Bottom Line

Phase B corrected Wave 1's data errors (no cache directory, ~20x fewer untracked entries
than reported), confirmed the G-exponent derivation branch does not exist (documented
negative result found instead), and classified all major clusters. The private repo is
better understood but not yet cleaned — the working tree's mix of restructuring deletions,
research edits, and build artifacts requires intentional resolution, not automated triage.
The single recommended next step is a narrow 15-file source-only preservation commit in
`derivations/mass_difference/`.
