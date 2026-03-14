# PG-8 Book II Resolution Status

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Protection Gate PG-8 reassessment after standalone vs repo Book II comparison
**Status:** PG-8 PASS

---

## 1. Executive Verdict

**PG-8 status: PASS.**

The standalone and repo Book II have been compared with forensic depth. The result
is unambiguous: they are **entirely different manuscripts** covering different EDC
physics sectors. There is no content duplication, no merge risk, no overwrite risk,
and no ambiguity about their relationship.

The standalone is a gravitational-sector manuscript ("Emergent Gravity from Plenum
Dynamics") with 9 chapters. The repo Book II is a weak-sector manuscript ("Part II:
Weak Sector") with 17 chapters. Zero chapters overlap.

---

## 2. Resolution Basis

The PG-8 PASS determination is based on the following evidence:

| Evidence | Finding |
|----------|---------|
| **Title comparison** | Different: "Emergent Gravity from Plenum Dynamics" vs "Part II: Weak Sector" |
| **Physics sector** | Different: gravitational sector vs weak sector |
| **Chapter inventory** | 0 shared chapters out of 9 (standalone) and 17 (repo) |
| **Section inventory** | 0 shared sections out of 49 (standalone) and ~100+ (repo) |
| **Include structure** | Incompatible: monolithic (standalone) vs modular (repo) |
| **Document class** | Different: 12pt openany vs 11pt twoside |
| **Shared macros** | None: standalone is self-contained, repo uses EDC_MACROS_COMPLETE |
| **DOI** | Standalone has placeholder; repo has real DOI (10.5281/zenodo.18328508) |
| **Key derivations** | Non-overlapping: flow velocity/G/viscosity (standalone) vs ontology/GF/CKM (repo) |

**Conclusion:** The "Book II" naming collision is a labeling artifact. The manuscripts
are distinct works with no content overlap that requires merge, reconciliation, or
deduplication.

---

## 3. Book II Safety / Surfacing Status

### 3.1 Repo Book II (Weak Sector)

| Dimension | Status |
|-----------|--------|
| **Content safety** | SAFE — fully backed up on `origin/main` (PG-1 PASS) |
| **Branch protection** | SAFE — all OPR branches pushed to origin (PG-2 PASS) |
| **Surfacing readiness** | READY — 17-chapter modular manuscript with real DOI, audit infrastructure, OPR register |
| **Identity clarity** | CLEAR — "Part II: Weak Sector" is unambiguous |
| **Known as** | `M-edc-main-002` (existing catalog ID) |

### 3.2 Standalone "Book II" (Gravitational Sector)

| Dimension | Status |
|-----------|--------|
| **Content safety** | SAFE — archived in `archive/nonrepo-local-research` (PG-5 PASS), original on disk |
| **Surfacing readiness** | NOT YET — monolithic, Version 1.0, placeholder DOI, no audit infrastructure |
| **Identity clarity** | AMBIGUOUS — "Book II" label collides with repo Book II; content is gravitational, not weak |
| **Unique value** | HIGH — only known book-length gravitational-sector EDC manuscript |
| **Recommended rename** | "EDC Gravitational Sector Manuscript" or "EDC Book I (Gravity)" |

### 3.3 Overall Book II Understanding

Book II (weak sector) is now **sufficiently understood for later surfacing**:
- Its content, structure, and relationship to the standalone are fully characterized
- No ambiguity remains about what it contains or how it relates to the standalone
- The standalone is confirmed as a different work, not a competing version

---

## 4. Remaining Open Questions

| # | Question | Priority | When to Resolve |
|---|----------|----------|-----------------|
| 1 | Does the standalone gravitational-sector content exist in any other form in the repo (e.g., Paper 1, Paper 2, derivation folders)? | LOW | Phase B catalog expansion |
| 2 | Should the standalone be formally cataloged as a separate manuscript (e.g., "Book I" or "Gravity Companion")? | LOW | Phase B |
| 3 | Should the standalone's naming be corrected in the archive to avoid future "Book II" confusion? | LOW | Phase B or housekeeping |

**None of these questions block the Protection Gate or reorganization.**

---

## 5. Recommended Next Step

**Commit PG-6 untracked files** to resolve the last PARTIAL gate criterion.

The 44 untracked files on the working branch (`research/topological-pinning-v7_8-integration`)
should be reviewed, categorized (source vs build artifact), and either committed or
added to `.gitignore`. This would bring the Protection Gate to 7/8 PASS (with PG-7
already PASS), leaving only catalog expansion (Phase B) before reorganization can
proceed.

---

## 6. Bottom Line

PG-8 is resolved. The standalone and repo Book II are different manuscripts — one
covers gravity, the other covers the weak sector. The naming collision is documented
and presents no risk to either manuscript's integrity. Both copies are now safely
backed up (repo on `origin/main`, standalone in `archive/nonrepo-local-research`).

**Updated Protection Gate: 7/8 PASS, 1/8 PARTIAL (PG-6 untracked files).**
