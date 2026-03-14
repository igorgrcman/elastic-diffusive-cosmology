# Master Catalog and Reorganization Plan

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Preservation-first planning — no file deletion, no branch deletion,
no history collapse, no overwrite
**Status:** Planning document only — no execution

---

## 1. Executive Verdict

Reorganization is now necessary because the forensic inventory revealed an
ecosystem that is architecturally sound but operationally fragile: 61 local-only
branches with no remote backup, 14 unpushed commits on `main`, a separate
private repo of unknown backup status, research material outside any version
control, and a full 17-chapter Book II manuscript that has been confirmed as
developed but not yet surfaced as a first-class asset.

**Deletion is forbidden** because buried material may be more valuable than
current canonical material, and because provenance is irreplaceable once lost.

**Overwrite is forbidden** because 97 files share the basename `main.tex`, and
silent overwrite would destroy identity, provenance, and the ability to compare
parallel versions.

**Protection must precede execution** because the immediate-risk assets
(local-only branches, unpushed main, untracked research) could be lost at any
time. No reorganization is safe if the material it operates on is not first
secured.

This plan will accomplish:
1. An explicit immediate-risk inventory with preservation urgency rankings
2. A protection gate that must be passed before any physical moves
3. A preservation-class taxonomy for all discovered material
4. A reorganization architecture that can hold the full ecosystem
5. Anti-loss rules preventing accidental destruction during future execution
6. Explicit treatment of Book II as a first-class surfacing priority

---

## 2. Governing Inputs

This plan depends on the following forensic reports, all on branch
`research/topological-pinning-v7_8-integration`:

| Document | Commit | Role |
|----------|--------|------|
| `FULL_FORENSIC_DISCOVERY_AND_INVENTORY.md` | `4af3f9e` | Primary factual base: repo inventory, branch inventory, local disk findings, risk assessment |
| `PARTICLE_ANATOMY_AND_DECAY_REDISCOVERY_INDEX.md` | `a0881fc` | Content-level index of particle anatomy and decay ontology across all sources |
| `DIRECT_SHAPE_SOURCE_EXHAUSTION_MEMO.md` | `2991aec` | Shape-source closure state within S_EH + S_NG |
| `MINIMAL_CLASS_CLOSURE_MEMO_AFTER_N1_N7_N2.md` | `dbe1a56` | Pre-NMCP closure state |
| `NMCP_WP1_DONOR_NORMALIZATION.md` | `2b81976` | NMCP donor normalization |
| `JSONL_REDISCOVERY_AUDIT_V1.md` | on branch | Archive rediscovery audit |
| `ARCHIVE_REDISCOVERY_TRACKER.md` | on branch | Archive item tracker |
| `CHAPTER_MAP.md` | on branch | Book IV chapter-level map |

All findings from these reports are treated as authoritative. This plan does
not re-derive them; it operates on them.

---

## 3. Preservation-First Principles

The following rules are non-negotiable and govern all future execution phases.

**P-1.** No file shall be deleted during reorganization. Files may be moved,
copied, or re-housed, but never removed from the ecosystem.

**P-2.** No git branch shall be deleted until its content has been fully
cataloged, assigned a preservation ID, and confirmed as either integrated into
a canonical location or explicitly archived with provenance.

**P-3.** No git history shall be collapsed (no rebase, no squash, no
force-push) on any branch containing unique research content.

**P-4.** No stash shall be dropped until its content has been inspected,
cataloged, and either integrated or archived.

**P-5.** Local-only content (branches, untracked files, non-git folders) is
treated as inventory, not junk. Its absence from remote does not reduce its
value.

**P-6.** Parallel versions of the same conceptual document are preserved as
distinct items until explicit provenance comparison confirms one supersedes the
other.

**P-7.** Files with the same basename (`main.tex`, `main.pdf`, `README.md`,
`STATUS.md`) shall NEVER be copied over one another. Identity is determined by
full path + repo + branch, not by basename alone. See §12 for handling rules.

**P-8.** Buried manuscripts may be more valuable than current surface canon.
The default assumption is preserve-and-surface, not discard-as-old.

**P-9.** Protection precedes reorganization. No physical re-housing shall
begin until the Protection Gate (§5) is passed.

**P-10.** Book II is a first-class surfacing priority, not background material.
See §7.

---

## 4. Immediate Risk Table

Ranked by preservation urgency.

| Rank | Asset / Area | Type | Why at risk | Loss mode | Urgency | Must protect before reorg? |
|------|-------------|------|------------|-----------|---------|---------------------------|
| **1** | `main` 14 commits ahead of `origin/main` | Branch (default) | Unpushed canonical commits on the default branch | Disk failure, accidental reset | CRITICAL | YES |
| **2** | 61 local-only branches | Branches (no remote) | No remote backup exists for any of them. One branch (`junction-core-well-v1`) has +72k lines. Total: hundreds of thousands of lines of unique research. | Disk failure | CRITICAL | YES |
| **3** | `EDC_Research_PRIVATE/` | Separate git repo | Backup status unknown. Contains 30+ KB files, organized derivations, canon PDFs, P7 derivation program — all unique | Disk failure, unknown remote | CRITICAL | YES |
| **4** | `current/` (12 files) | Non-git folder | No version control. Contains Croatian-language personal analysis, working notes, task derivations — all unique | Any disk event, accidental deletion | HIGH | YES |
| **5** | `aside_proof_audit/` (5 files) | Non-git folder | No version control. Proof ledger, missing lemmas, consistency checklist — unique audit infrastructure | Any disk event, accidental deletion | HIGH | YES |
| **6** | 4 stashes | Git stashes | Stashes are fragile — any `git stash drop` or careless `git stash clear` destroys them permanently | Accidental stash operation | HIGH | YES |
| **7** | 42+ untracked files in `edc_book_4/` | Untracked in git | Not committed; invisible to remote. Includes appendices, code, PDFs, audit reports | `git clean`, accidental deletion | HIGH | YES |
| **8** | `EDC_Book_2/` standalone copy | Non-git folder | 53 KB tex + 368 KB PDF. May be an earlier/alternate Book II version not present elsewhere | Overwrite, deletion | MEDIUM | YES |
| **9** | `edc_paper_2_archive/` | Non-git folder | Frozen Paper 2 release with private assumption ledgers, traceability matrices | Deletion | MEDIUM | YES (for private components) |
| **10** | Standalone planning docs | Non-git files | `EDC_Clean_Core_Paper_Structure...txt`, `EDC_Path_Forward_Claim_Ledger...md` | Deletion | LOW-MEDIUM | YES |
| **11** | `obsolite/` (2 files) | Non-git folder | Superseded but may contain unique reasoning | Deletion | LOW | Recommended |
| **12** | `build/` dated PDFs | Non-git folder | `EDC_Book2_2026-01-25_OPEN22-4b.pdf` — dated build snapshot | Deletion | LOW | Optional |

---

## 5. Protection Gate

### Definition

The **Protection Gate** is a mandatory checkpoint that must be passed before
any future physical reorganization phase (moving files, re-housing directories,
rationalizing branches, archiving content) begins.

### Gate Criteria

The Protection Gate is passed when ALL of the following are true:

**PG-1.** `main` has been pushed to `origin/main` (no commits ahead).

**PG-2.** All 61 local-only branches have been pushed to `origin` as backup
(using their current names, no renaming).

**PG-3.** All 4 stashes have been inspected, their contents recorded in the
catalog with stash IDs and descriptions, and optionally converted to named
branches for durability.

**PG-4.** `EDC_Research_PRIVATE` backup status has been verified. If no remote
exists, one has been created and pushed.

**PG-5.** `current/`, `aside_proof_audit/`, and other non-git research folders
have been either (a) committed into a preservation branch of the main repo,
or (b) copied into a dedicated backup location with checksums.

**PG-6.** All 42+ untracked files in `edc_book_4/` have been either committed
to the current branch or explicitly cataloged with checksums.

**PG-7.** The `MASTER_CATALOG_SCHEMA.md` has been populated with at least
seed records for all Rank 1-6 items from the Immediate Risk Table.

**PG-8.** The standalone `EDC_Book_2/` copy has been compared against
`edc_book_2/` to determine whether it contains unique content.

### Evidence of Gate Passage

A short verification document (`PROTECTION_GATE_PASSAGE.md`) shall be created
confirming each criterion, with dates and commit SHAs where applicable.

### Forbidden Until Gate Passage

- No branch deletion
- No stash dropping
- No file relocation across repo boundaries
- No archival re-housing
- No manuscript consolidation
- No "cleanup" operations of any kind

---

## 6. What Must Be Preserved

| Preservation Class | What it contains | Why it matters | Risk level | Must snapshot before reorg? |
|-------------------|-----------------|---------------|------------|---------------------------|
| **PC-CANON** | Published papers (DOI), released Book I, locked ontology canon, OPR registry | Authoritative references; loss would break citation chains | LOW (already remote) | NO (already backed up) |
| **PC-ACTIVE** | Current branch Book IV work, active appendices, audit docs | Active development; loss would lose weeks of work | MEDIUM (partially untracked) | YES (untracked portions) |
| **PC-BOOK** | Books I, II, IV complete manuscripts | Full-length manuscripts; Book II especially underappreciated | MEDIUM | YES (Book II comparison needed) |
| **PC-LOCAL-BRANCH** | 61 local-only branches | Unique computation, derivation attempts, forensic records totaling hundreds of thousands of lines | CRITICAL | YES |
| **PC-STASH** | 4 git stashes | WIP states from OPR, notation, reorganization work | HIGH | YES |
| **PC-UNTRACKED** | 42+ untracked files in edc_book_4/ | Appendices, code, PDFs, audit reports not yet committed | HIGH | YES |
| **PC-PRIVATE** | EDC_Research_PRIVATE repo contents | 30+ KB files, organized derivations, canon PDFs, P7 program — unique | CRITICAL | YES |
| **PC-NONREPO** | `current/`, `aside_proof_audit/`, standalone files | Personal analysis, proof infrastructure — outside any VCS | HIGH | YES |
| **PC-SNAPSHOT** | Standalone Book II copy, edc_paper_2_archive, build PDFs | Dated snapshots that may capture states not in git history | MEDIUM | YES (for comparison) |
| **PC-DEADEND** | Dead-end branches (Helfrich NO-GO, junction core well, etc.) | Documented negative results; forensic value for future researchers | LOW-MEDIUM | YES (push to remote) |
| **PC-DRAFT** | Draft companions M/T/P/L/V/N (v0.1-v0.3) | Per-particle decay derivations; pipeline toward canonical status | MEDIUM | NO (already in repo) |
| **PC-GRAVITY** | 67 gravity derivation versions | Complete derivation evolution; v67 is REAL CLOSED but history matters | LOW | NO (already in repo) |

---

## 7. Book II Surfacing Priority

### Why Book II has special status

Book II (`edc_book_2/reorganized/main.tex`) is not a speculative lead or a
collection of notes. The forensic inventory confirms it as a **developed
17-chapter manuscript** with:

- `\documentclass{book}` with 3 parts and 17 chapters
- Part 1 (Ch 1-5): Foundations — Weak Interface, Ontology, Frozen Projection,
  Z₆ Program, Case Studies
- Part 2 (Ch 6-11): Electroweak — Leptons, Generations, Neutrinos, V-A, CKM/PMNS
- Part 3 (Ch 12-16): BVP/G_F — G_F Chain, Foundation Parameters, BVP, M_W/G_F,
  Epistemic Summary
- Epilogue (Ch 17): Beyond
- 3 appendices (OPR register, notation, numerical standards)
- Per-particle case studies covering neutron, muon, tau, pion, electron, neutrino
- Five-category particle classification with TikZ diagram
- Extensive OPR registry (22+ entries) and audit infrastructure
- 16 Python computation scripts
- Multiple build PDFs including a verified 387-page state
- Canon bundle and evidence directory

### Forensic evidence of maturity

- The `PARTICLE_ANATOMY_AND_DECAY_REDISCOVERY_INDEX.md` (commit `a0881fc`)
  identifies `edc_book_2/src/sections/04_ontology.tex` as the single best
  "what is what" file for all EDC particles
- The same report identifies Book 2 case studies (sections 05-10) as the
  primary narrative source for each particle
- The `FULL_FORENSIC_DISCOVERY_AND_INVENTORY.md` (commit `4af3f9e`) confirms
  Book II as a "developed manuscript" and the "closest thing to a buried
  whole book"

### Why it must be surfaced before broader consolidation

Book II contains the particle anatomy, decay ontology, and weak-sector
derivations that are being actively searched for in the current research
program. Surfacing it means making its content retrievable, navigable, and
citable from within the current canonical workflow — not rewriting it.

### Future role in umbrella structure

Book II should occupy a first-class position alongside Books I and IV in any
future umbrella structure, with its own canonical entry point, chapter map,
and cross-reference links.

---

## 8. Master Reorganization Concept

### Proposed umbrella structure (conceptual — not yet executed)

```
EDC_ECOSYSTEM/
├── canon/                          # Published, DOI'd, locked material
│   ├── books/
│   │   ├── book_I/                 # Released v17.49
│   │   ├── book_II/                # Weak-sector manuscript (SURFACING PRIORITY)
│   │   └── book_IV/                # Cluster structure (active)
│   ├── papers/
│   │   ├── paper_2/                # Fine-structure constant
│   │   ├── paper_3_series/         # NJSR + 9 Zenodo companions
│   │   └── paper_gravity/          # v67 REAL CLOSED
│   └── ontology/                   # Locked ontology canon, OPR registry
│
├── active/                         # Current working material
│   ├── book_IV_dev/                # Active Book IV development
│   ├── draft_companions/           # M, T, P, L, V, N (v0.1-v0.3)
│   └── weak_program/               # Paper 3 entries 14-20
│
├── research_archive/               # Completed investigations (positive + negative)
│   ├── derivation_branches/        # Cataloged branch snapshots
│   ├── dead_ends_preserved/        # Helfrich NO-GO, junction core, etc.
│   ├── forensic_investigations/    # Factor-8, OPR attempts, CKM/PMNS
│   └── gravity_evolution/          # v1-v66 derivation history
│
├── local_recovered/                # Material recovered from local-only sources
│   ├── branches/                   # 61 local-only branch catalogs
│   ├── stashes/                    # 4 stash snapshots
│   ├── untracked/                  # Untracked research files
│   ├── private_repo/               # EDC_Research_PRIVATE content
│   ├── nonrepo_notes/              # current/, aside_proof_audit/
│   └── standalone_copies/          # EDC_Book_2/, edc_paper_2_archive/
│
├── infrastructure/                 # Shared tools and standards
│   ├── code/                       # Python computation library
│   ├── shared_style/               # LaTeX style, macros
│   ├── shared_derivations/         # 8 standalone derivation PDFs
│   └── bvp_solvers/                # BVP/G_F numerical infrastructure
│
├── catalogs/                       # Indexes, maps, registries
│   ├── master_catalog/             # Populated MASTER_CATALOG_SCHEMA records
│   ├── audit_reports/              # All audit/forensic reports
│   └── migration_logs/             # Re-housing provenance records
│
└── build_artifacts/                # Dated PDF snapshots, build outputs
    ├── book_II_builds/
    ├── book_IV_builds/
    └── paper_builds/
```

### Bucket definitions

| Bucket | What goes there | What does NOT | Status |
|--------|----------------|---------------|--------|
| `canon/` | Published (DOI), released, or locked material | Drafts, attempts, WIP | Archival (read-only) |
| `active/` | Current development targets | Completed/closed work | Active (read-write) |
| `research_archive/` | Completed investigations with results | Active WIP, canonical material | Archival (read-only) |
| `local_recovered/` | Material surfaced from local-only sources | Already-canonical material | Transitional (moves to canon/ or archive/ after review) |
| `infrastructure/` | Shared tools, styles, solvers | Research content | Active (maintained) |
| `catalogs/` | Indexes, maps, registries, audit reports | Research content | Active (maintained) |
| `build_artifacts/` | Dated PDF snapshots | Source files | Archival |

### Coexistence rule

This umbrella structure must coexist with the current repo structure during
any transition period. It is a logical overlay, not a forced physical
restructuring. Physical moves happen only in Phase C (§13) and only after the
Protection Gate is passed.

---

## 9. Catalog Layers

The ecosystem requires five layers of cataloging:

| Layer | Scope | Purpose | Example entry |
|-------|-------|---------|--------------|
| **Repo-level** | Entire repositories | Track which repos exist, their remotes, backup status | `elastic-diffusive-cosmology_repo` → origin at GitHub |
| **Branch-level** | All branches per repo | Track branch purpose, unique content, local/remote status, preservation class | `junction-core-well-v1` → local-only, +72k lines, dead-end preserved |
| **Manuscript-level** | Books, papers, companions | Track multi-file manuscripts as coherent units | Book II → 17 chapters, 3 parts, OPR registry, builds |
| **File-level** | Individual files | Track identity, provenance, basename conflicts, content summary | `edc_book_2/reorganized/main.tex` → Book II driver, \documentclass{book} |
| **Topic-level** | Cross-cutting themes | Track where content on a topic lives across files/branches/repos | "pion decay" → Companion P (draft), Book II §08, Framework v2.0 §15 |

Each layer answers a different question:
- **Repo-level:** "What repos exist and are they backed up?"
- **Branch-level:** "What branches exist and what is unique to each?"
- **Manuscript-level:** "What complete works exist and what is their status?"
- **File-level:** "Where is file X and how do I distinguish it from files with the same name?"
- **Topic-level:** "Where do I find everything about topic Y?"

---

## 10. Material Classes

| Class | Meaning | Handling rule | Destination | Consolidation priority |
|-------|---------|--------------|-------------|----------------------|
| **CANONICAL** | Published (DOI), released, or locked | Preserve as-is; never modify without versioning | `canon/` | N/A (already canonical) |
| **ACTIVE-DRAFT** | Current development target | Continue development; track in active catalog | `active/` | HIGH (ongoing) |
| **BURIED-HIGH-VALUE** | Discovered material of significant research value not yet surfaced | Surface via catalog; promote to canon or active after review | `local_recovered/` → `canon/` or `active/` | HIGH |
| **LOCAL-ONLY-CRITICAL** | Branch/file existing only locally with no backup | Push/commit immediately; catalog with preservation ID | `local_recovered/branches/` | CRITICAL (backup first) |
| **STASH-CRITICAL** | Git stash with non-trivial research content | Convert to named branch or commit; catalog | `local_recovered/stashes/` | HIGH |
| **DUPLICATE-KEEP** | Copy of material that exists elsewhere, but keep for provenance comparison | Catalog with link to primary; do not delete | `local_recovered/standalone_copies/` | LOW |
| **SUPERSEDED-PRESERVE** | Older version replaced by newer, but preserved for historical record | Catalog with supersession link; archive | `research_archive/` | LOW |
| **DEAD-END-PRESERVE** | Completed investigation with negative result | Catalog with outcome summary; archive as forensic record | `research_archive/dead_ends_preserved/` | LOW |
| **BUILD-ARTIFACT** | Compiled PDF, dated snapshot | Catalog with date and source link; archive | `build_artifacts/` | LOW |
| **UNKNOWN-REVIEW** | Material of uncertain value or status | Inspect, classify, then reassign to another class | Temporary holding in `local_recovered/` | MEDIUM |

---

## 11. Reorganization Targets

### 11A. Book I (`edc_book/`)
- **Current condition:** Released v17.49. Stable. 12 chapters + appendices.
- **Fragmentation:** None — self-contained.
- **Future home:** `canon/books/book_I/`
- **Risk if unmanaged:** LOW — already released.

### 11B. Book II (`edc_book_2/`)
- **Current condition:** Developed 17-chapter manuscript. Multiple internal
  structures (`reorganized/`, `src/`, `build/`). OPR registry. Case studies.
  Code. Multiple build PDFs. One standalone external copy (`EDC_Book_2/`).
- **Fragmentation:** MEDIUM — material split between `reorganized/`, `src/`,
  `build/`, and 20+ local-only OPR branches.
- **Future home:** `canon/books/book_II/` (SURFACING PRIORITY)
- **Risk if unmanaged:** HIGH — the full weak-sector ontology is here but not
  easily navigable; OPR derivation branches are local-only.

### 11C. Book IV (`edc_book_4/`)
- **Current condition:** Active development. 17 chapters, 11 appendices,
  ~228 pages. 42+ untracked files.
- **Fragmentation:** LOW — well-organized on current branch.
- **Future home:** `active/book_IV_dev/` (active) → `canon/books/book_IV/` (when released)
- **Risk if unmanaged:** MEDIUM — untracked files need committing.

### 11D. Paper 3 series
- **Current condition:** 22 entries. 10 published with DOIs. 12 at draft/follow-on stage.
- **Fragmentation:** LOW — well-organized within `edc_papers/paper_3_series/`.
- **Future home:** Published → `canon/papers/paper_3_series/`. Drafts → `active/draft_companions/`.
- **Risk if unmanaged:** LOW.

### 11E. Weak-sector / decay ontology
- **Current condition:** Distributed across Book II (case studies, ontology hub),
  Companion H (process catalog), Companions D/E (selection rules, operators),
  draft companions M/T/P/L/V/N, Framework v2.0.
- **Fragmentation:** HIGH — spread across 3 books, 10+ companions, multiple layers.
- **Future home:** Topic-level catalog entry linking all sources.
- **Risk if unmanaged:** MEDIUM — the indexing report already maps this.

### 11F. Proton/neutron anatomy
- **Current condition:** Canonical in Companions F/G, Book IV ch01/ch03,
  Framework v2.0. Supplemented by Book II ontology hub.
- **Fragmentation:** MEDIUM — well-sourced but distributed.
- **Future home:** Topic-level catalog entry.
- **Risk if unmanaged:** LOW — already indexed.

### 11G. OPR / BVP / gravity program
- **Current condition:** OPR registry in Book II canon. 20+ local-only OPR
  branches. 67 gravity derivation versions. 6 factor-8 forensic branches.
  BVP code in multiple locations.
- **Fragmentation:** HIGH — OPR history spread across many local-only branches.
- **Future home:** OPR branches → `research_archive/forensic_investigations/`.
  Gravity → `canon/papers/paper_gravity/` (v67) + `research_archive/gravity_evolution/` (v1-v66).
- **Risk if unmanaged:** HIGH — local-only branches at risk.

### 11H. Private repo KB / derivations
- **Current condition:** `EDC_Research_PRIVATE/` with 30+ KB files, organized
  derivations, P7 program. Backup status unknown.
- **Fragmentation:** Self-contained but disconnected from main repo.
- **Future home:** `local_recovered/private_repo/` (transitional).
- **Risk if unmanaged:** CRITICAL — backup status unknown.

### 11I. Audits and canon documents
- **Current condition:** 33+ audit files in `edc_book_4/audit/`. Additional
  audit infrastructure in `edc_book_2/audit/`. Style guide and shared canon
  in `edc_papers/_shared/`.
- **Fragmentation:** LOW — well-organized within each book.
- **Future home:** `catalogs/audit_reports/`.
- **Risk if unmanaged:** LOW.

---

## 12. Versioning and Same-Name File Strategy

### The problem

97 files share the basename `main.tex`. Dozens share `main.pdf`. Other
common basenames include `README.md`, `STATUS.md`, `references.bib`.
Silent overwrite during any reorganization would be catastrophic.

### Identity rule

**A file's identity is NEVER its basename alone.** Identity is the tuple:

```
(repo, branch, relative_path, basename)
```

Example: the file commonly called "main.tex" for Book II is identified as:

```
(elastic-diffusive-cosmology_repo, main, edc_book_2/reorganized/main.tex, main.tex)
```

This is distinct from:

```
(elastic-diffusive-cosmology_repo, main, edc_book_4/main.tex, main.tex)
```

### Naming rule for re-housed files

If files with the same basename must be placed in the same directory during
reorganization, they SHALL be disambiguated by prepending the source context:

| Original path | Re-housed name |
|--------------|----------------|
| `edc_book/main.tex` | `book_I__main.tex` |
| `edc_book_2/reorganized/main.tex` | `book_II__main.tex` |
| `edc_book_4/main.tex` | `book_IV__main.tex` |
| `edc_papers/paper_2/paper/main.tex` | `paper_2__main.tex` |

The double-underscore `__` separator is reserved for provenance disambiguation.

### Foldering rule

The preferred approach is to keep files in their original directory structure
rather than flattening into a single directory. If the original structure is
preserved, no renaming is needed.

### Provenance rule

Every re-housed file must have a provenance record in the catalog containing:
- original full path
- original repo and branch
- original commit SHA (if in git)
- original file checksum (SHA256)
- re-housed destination path
- reason for move
- date of move

### Display/title rule

When listing same-name files in catalogs or reports, always use the full
relative path, never the basename alone.

---

## 13. Proposed Reorganization Phases

### Phase A: Protection and Freeze

**Objective:** Secure all immediate-risk assets. Pass the Protection Gate.

**Allowed actions:**
- Push `main` to `origin/main`
- Push all 61 local-only branches to `origin`
- Convert 4 stashes to named branches or commit them
- Verify `EDC_Research_PRIVATE` backup; create remote if needed
- Commit or archive `current/`, `aside_proof_audit/`, other non-git research
- Commit untracked files in `edc_book_4/`
- Create `PROTECTION_GATE_PASSAGE.md` confirming all criteria met

**Forbidden actions:**
- No branch deletion
- No file deletion
- No file moves across directories
- No manuscript consolidation
- No renaming

**Output:** All material backed up to at least one remote. Protection Gate
passed.

### Phase B: Catalog Population

**Objective:** Populate the master catalog with records for all discovered
material.

**Allowed actions:**
- Create catalog records (repo, branch, manuscript, file level)
- Assign preservation classes
- Assign unique IDs
- Link duplicates and supersession chains
- Mark surfacing priorities (Book II first)
- Compare `EDC_Book_2/` standalone vs `edc_book_2/` canonical

**Forbidden actions:**
- No physical file moves
- No deletions
- No content changes to research files

**Output:** Populated catalog with records for all Rank 1-10 risk items.

### Phase C: Archival Re-housing

**Objective:** Move completed, closed, or archival material into the umbrella
structure.

**Allowed actions:**
- Create new directories in the umbrella structure
- Copy (not move) material into canonical locations
- Create provenance records for all copies
- Apply same-name disambiguation rules

**Forbidden actions:**
- No deletion of originals until provenance confirmed
- No overwrite of same-name files
- No branch deletion

**Output:** Umbrella structure populated with archival content. Originals
intact.

### Phase D: Canonical Surfacing

**Objective:** Surface buried high-value material (especially Book II) into
active canonical access paths.

**Allowed actions:**
- Create cross-reference links from Book IV audit space to Book II
- Create topic-level catalog entries linking all sources on a subject
- Update retrieval paths in existing index documents
- Create navigation aids (chapter maps, reading orders)

**Forbidden actions:**
- No rewriting of Book II content
- No consolidation of parallel versions
- No deletion of draft material

**Output:** Book II and other buried manuscripts accessible via canonical
retrieval paths.

### Phase E: Later Consolidation / Branch Rationalization

**Objective:** Rationalize the branch landscape and consolidate parallel
versions where appropriate.

**Allowed actions:**
- Merge completed branches that have been fully cataloged
- Archive branches as tags before deletion
- Consolidate duplicate files where provenance confirms identity
- Create consolidated topic documents from scattered sources

**Forbidden actions:**
- No deletion without prior archival tag
- No consolidation without provenance comparison

**Output:** Reduced branch count. Consolidated topic documents. Clean
umbrella structure.

**Note:** Phase E is the LAST phase and should not begin until Phases A-D
are complete.

---

## 14. Anti-Loss Rules

**AL-1.** No branch shall be deleted before a catalog record exists with
its unique ID, content summary, preservation class, and a confirming
`git tag archive/<branch-name>` has been created.

**AL-2.** No stash shall be dropped before its content has been committed
to a named branch or cataloged with a content diff snapshot.

**AL-3.** No untracked file shall be moved or deleted before its full path,
checksum (SHA256), and content summary are recorded in the catalog.

**AL-4.** No "duplicate removal" shall occur before an explicit provenance
comparison confirms byte-level identity or documented supersession.

**AL-5.** No manuscript consolidation (merging chapters from different
sources into one) shall occur before the include-tree of each source has
been independently mapped and compared.

**AL-6.** No same-name file copy shall proceed without the disambiguation
rules in §12. Silent overwrite is always a policy violation.

**AL-7.** No branch merge shall occur during Phases A-D. Merges are
Phase E only.

**AL-8.** No `git clean`, `git checkout -- .`, or `git reset --hard` shall
be run on any branch containing uncataloged untracked research files.

**AL-9.** No non-git folder (`current/`, `aside_proof_audit/`, etc.) shall
be deleted or moved before its contents are committed to a preservation
branch or archived with checksums.

**AL-10.** No physical re-housing of files shall begin before the
Protection Gate (§5) is confirmed passed via `PROTECTION_GATE_PASSAGE.md`.

**AL-11.** No file shall be moved from its original location until a
provenance record exists at the destination documenting the original path,
repo, branch, and commit SHA.

**AL-12.** When in doubt, copy — do not move. Originals remain until
the catalog confirms the copy is complete and verified.

---

## 15. What Should NOT Yet Be Done

The following actions are explicitly premature and forbidden until the
corresponding phase allows them:

1. **Do not merge all branches.** Branches are historical containers with
   unique provenance. Merging destroys this.

2. **Do not flatten all books into one tree.** Books I, II, and IV have
   different architectures, vocabularies, and maturity levels.

3. **Do not discard obsolete drafts before catalog links exist.** Even
   dead-end branches (Helfrich NO-GO, junction core well) have forensic
   value.

4. **Do not treat local-only branches as junk.** Many contain the only
   record of extensive computation and investigation.

5. **Do not rewrite Book II or companions just because a new umbrella
   exists.** Surface them as they are; rewriting is a separate decision.

6. **Do not overwrite files with the same basename.** See §12.

7. **Do not begin archival relocation before the Protection Gate is
   passed.** See §5.

8. **Do not push `EDC_Research_PRIVATE` content to the public repo
   without explicit authorization.** It is a private repo for a reason.

9. **Do not treat stashes as temporary noise.** Stash 3 contains WIP on
   OPR-20 suppression, which is active research.

10. **Do not create a "cleaned up" version of any manuscript by silently
    dropping sections.** Any version reduction must be explicit and the
    original preserved.

---

## 16. Recommended First Execution Wave

The first execution wave focuses on **immediate protection and catalog seeding
only**. No restructuring.

### Wave 1 actions (in order):

1. **Push `main` to `origin/main`.**
   Command: `git push origin main`
   Urgency: CRITICAL. Do this first.

2. **Push all 61 local-only branches to `origin`.**
   Command: `for branch in $(git branch --format='%(refname:short)' | grep -v HEAD); do git push origin "$branch" 2>/dev/null; done`
   Urgency: CRITICAL. Do this immediately after main.

3. **Verify `EDC_Research_PRIVATE` remote status.**
   Command: `cd EDC_Research_PRIVATE && git remote -v`
   If no remote, create one and push.
   Urgency: CRITICAL.

4. **Commit all untracked research files in `edc_book_4/`.**
   Review the 42+ files. Commit research-relevant ones to current branch.
   Urgency: HIGH.

5. **Archive `current/` and `aside_proof_audit/` into a preservation branch.**
   Create branch `archive/local-nonrepo-research`, copy files, commit.
   Urgency: HIGH.

6. **Convert 4 stashes to named branches.**
   For each stash: `git stash branch stash-archive/<name> stash@{N}`
   Then push each to origin.
   Urgency: HIGH.

7. **Create `PROTECTION_GATE_PASSAGE.md`** confirming all PG-1 through PG-8
   criteria are met.
   Urgency: Required before any Phase B work.

### What Wave 1 does NOT do:
- No file moves
- No directory creation (beyond preservation branch)
- No catalog population (that is Wave 2 / Phase B)
- No manuscript consolidation
- No branch deletion

---

## 17. Success Criteria for the Future Reorganization

The reorganization will be considered successful when:

**SC-1.** No material loss has occurred. Every file, branch, stash, and
untracked item cataloged in the forensic inventory is accounted for.

**SC-2.** Every Rank 1-6 item from the Immediate Risk Table has been
secured with at least one remote backup.

**SC-3.** All local-only branches are pushed to origin.

**SC-4.** All stash content is preserved in durable form.

**SC-5.** Book II is surfaced as a first-class manuscript with a canonical
entry point, chapter map, and retrieval path.

**SC-6.** The master catalog contains records for all discovered manuscripts
(Books I, II, IV; Papers 2, 3 series, gravity; draft companions; private KB).

**SC-7.** Every same-name file (`main.tex`, `main.pdf`, etc.) is cataloged
with its full identity tuple and has a provenance-preserving destination in
the umbrella structure.

**SC-8.** The canonical vs archive vs dead-end distinction is clear for
every cataloged item.

**SC-9.** Future branch count is rationalizable (via Phase E) without
knowledge loss, because all content has been cataloged first.

**SC-10.** The `PROTECTION_GATE_PASSAGE.md` exists and is complete.

---

## 18. Bottom Line

Protection first. The 61 local-only branches, unpushed main, unverified
private repo, and non-git research folders represent an immediate data-loss
risk that must be resolved before any planning is executed.

Catalog second. Once material is secured, the master catalog schema can be
populated systematically — repo by repo, branch by branch, file by file —
with preservation classes, provenance records, and surfacing priorities.

Surfacing and archival re-housing third. Book II is the highest-priority
surfacing target: a full 17-chapter weak-sector manuscript that is already
developed but not yet treated as a first-class asset. Buried local-only
branches with forensic value (junction core well, Helfrich NO-GO, factor-8
investigation) should be archived with provenance.

Consolidation last. Branch rationalization, duplicate resolution, and
manuscript merging happen only after everything is cataloged, backed up,
and surfaced. Never before.
