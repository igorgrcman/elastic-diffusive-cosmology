# Private Repo Phase B.3 Status

**Date:** 2026-03-14
**Branch (private repo):** `restructure/paper3-companion-doi-split`
**Branch (main repo):** `research/topological-pinning-v7_8-integration`
**Status:** Complete

---

## 1. One-Line Verdict

Phase B.3 preserved 85 source-only files (29,509 lines) from `derivations/analytic/`,
including 11 failure certificates and 9 derivation ledgers; 41 build artifacts excluded.

---

## 2. What Was Done

- Inventoried 126 files in `derivations/analytic/` (including `archive/` and `derivations/` subdirectories)
- Classified each file as source (85) or build artifact (41)
- Committed 85 source-only files to private repo branch `restructure/paper3-companion-doi-split`
- Pushed commit `8c26d30` to origin (29,509 insertions)
- Created preservation report and status documents in main repo

---

## 3. Key Numbers

| Metric | Value |
|--------|-------|
| Total files in cluster | 126 |
| Source files committed | 85 |
| Build artifacts excluded | 41 |
| Lines committed | 29,509 |
| Failure certificates preserved | 11 (v1–v11) |
| Derivation ledgers preserved | 9 (v3–v11) |
| Archived earlier versions preserved | 17 |
| Private repo commit | `8c26d30` |

---

## 4. What Was NOT Done

- No build artifacts (.pdf, .log, .aux, .out, .fls, .fdb_latexmk, .toc, .DS_Store) were committed
- No scope expansion beyond `derivations/analytic/`
- No files were modified — only previously untracked files were added
- No Part I or Book II source files were touched

---

## 5. Remaining Exposure

Combined with Phase B.2 (`derivations/mass_difference/`, 12 files), the two largest
`derivations/` research clusters are now fully source-preserved on origin.

Remaining untracked research clusters identified in Phase B triage:
- `derivations/critical/` — smaller cluster, recommended for next preservation pass
- `releases/`, `kb/`, and smaller clusters (~160 entries total)

---

## 6. Recommended Next Step

Assess `derivations/critical/` for a Phase B.4 narrow preservation pass, or perform a
broader triage of the remaining ~160 untracked entries across `releases/`, `kb/`, and
smaller clusters.
