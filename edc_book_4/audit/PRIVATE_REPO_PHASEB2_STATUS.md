# Private Repo Phase B.2 Status

**Date:** 2026-03-14
**Branch (private repo):** `restructure/paper3-companion-doi-split`
**Branch (main repo):** `research/topological-pinning-v7_8-integration`
**Status:** Complete

---

## 1. Executive Verdict

This narrow source-only preservation step is **complete**.

12 research source files (8 `.md` + 4 `.tex`, 6,575 lines total) from
`derivations/mass_difference/` were committed (`203771e`) and pushed to origin.
No build artifacts, no reorganization, no scope expansion. The narrow-commit rule
held without exception.

---

## 2. Preservation Outcome Table

| Area | Before | After | Status | Notes |
|------|--------|-------|--------|-------|
| Target cluster preservation | 12 source files untracked | 12 source files committed + pushed | **COMPLETE** | All research .md/.tex now on origin |
| Ambiguous-file exposure | 21 untracked files in cluster | 9 remaining (all build artifacts) | **REDUCED** | Only .log and .pdf files remain untracked |
| Private repo working-tree clarity | 256 untracked entries | 245 untracked entries (~11 fewer) | **SLIGHTLY IMPROVED** | One cluster resolved; ~10 clusters remain |
| Preservation readiness for next step | `derivations/analytic/` identified as next target | Ready for similar narrow pass | **READY** | ~73 files, same source/artifact separation pattern |
| `08_gravity_topological_ops.tex` | Untracked (471-line gravity/KK section) | Committed and pushed | **PRESERVED** | Standard KK reduction + process operator formalism |
| Tracked modifications (15 files) | Deferred | Still deferred | **UNCHANGED** | Source/artifact separation still needed |
| Tracked deletions (49 files) | Deferred | Still deferred | **UNCHANGED** | Active restructuring, intentional |

---

## 3. Did the Narrow Commit Rule Hold?

**Yes.**

The commit included exactly 12 files, all `.md` or `.tex`, all clearly research source.
Zero build artifacts (.log, .pdf, .aux, .bbl, .blg) were included. Zero files outside
`derivations/mass_difference/` were included. No .gitignore changes, no opportunistic
additions, no scope expansion.

---

## 4. Remaining Critical Exposures

| # | Exposure | Risk Level | Mitigation |
|---|----------|------------|------------|
| 1 | `derivations/analytic/` (~73 untracked files) | MEDIUM | Next preservation target; contains failure certificates and derivation attempts |
| 2 | `releases/paper_3_private/` (~80 untracked entries) | MEDIUM | Companion papers, submission bundles; needs individual assessment |
| 3 | `kb/` (51 untracked entries) | LOW | Knowledge base; lower urgency |
| 4 | 15 tracked modifications (source + artifacts mixed) | MEDIUM | Need source/artifact separation before commit |
| 5 | 49 tracked deletions | LOW | Intentional restructuring; branch is pushed |
| 6 | 1 deferred stash (build artifacts) | LOW | Parent branch pushed; stash in reflog |

---

## 5. Recommended Next Safe Step

**Execute a narrow source-only preservation pass for `derivations/analytic/`.**

This cluster contains ~73 untracked files including:
- 11 failure certificates (documenting what did NOT work — high forensic value)
- 11 derivation ledger versions (documenting derivation state evolution)
- Multiple `.tex` derivation files (action-from-principle attempts)
- Research notes and analysis documents

The same source/artifact separation pattern applies: commit `.md` and `.tex` source
files, exclude `.pdf` and build artifacts. This would preserve the next most valuable
untracked research cluster.

---

## 6. Bottom Line

Phase B.2 achieved its single goal: 12 research source files (6,575 lines) from
`derivations/mass_difference/` are now durably versioned and pushed to origin in the
private repo. The narrow-commit rule held. The private repo's most clearly defined
research cluster is preserved. The next target is `derivations/analytic/` (~73 files),
following the same narrow source-only pattern.
