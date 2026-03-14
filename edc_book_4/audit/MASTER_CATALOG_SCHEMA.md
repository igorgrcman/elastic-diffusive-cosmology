# Master Catalog Schema

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Purpose:** Define the canonical record schema for cataloging all rediscovered
EDC research material
**Status:** Schema definition only — no population yet

---

## 1. Purpose

This schema defines the record types, required fields, controlled vocabularies,
and identity conventions needed to catalog the entire EDC research ecosystem.

The catalog must support:
- Distinguishing 97+ files named `main.tex` without ambiguity
- Tracking material across 2+ repos, 83+ branches, 4 stashes, and non-git folders
- Preserving provenance during any future re-housing
- Marking surfacing priorities (Book II first)
- Linking duplicates without deleting either copy
- Preventing accidental overwrite of same-name files

The catalog is populated in Phase B of the reorganization plan. This document
defines what the records look like; it does not create them.

---

## 2. Required Record Types

| Record Type | Scope | What it catalogs | When to create |
|-------------|-------|-----------------|----------------|
| **REPO** | Entire repository | A git repo or non-git research folder | Phase B: one per discovered repo/folder |
| **BRANCH** | Git branch | A single branch within a repo | Phase B: one per branch (83+ needed) |
| **MANUSCRIPT** | Multi-file work | A book, paper, or companion as a coherent unit | Phase B: one per identified manuscript |
| **FILE** | Individual file | A single `.tex`, `.py`, `.pdf`, `.md` file | Phase B: priority files first, then exhaustive |
| **STASH** | Git stash | A single stash entry | Phase A/B: one per stash (4 needed) |
| **UNTRACKED** | Untracked file | A file present in working tree but not in git | Phase A/B: one per significant untracked file |
| **ARTIFACT** | Build output | A compiled PDF, dated snapshot, or build byproduct | Phase B: one per significant artifact |

---

## 3. Required Fields

### 3.1 REPO Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID (see §5) |
| `label` | string | YES | Human-readable name |
| `path` | string | YES | Local filesystem path |
| `is_git` | boolean | YES | Whether it is a git repository |
| `remotes` | list | YES | Remote URLs (empty if none) |
| `backup_status` | enum | YES | `backed_up` / `local_only` / `unknown` |
| `branch_count` | integer | YES | Number of local branches |
| `local_only_branch_count` | integer | YES | Branches with no remote tracking |
| `relevance` | enum | YES | See §4 |
| `preservation_class` | enum | YES | See §4 |
| `risk_level` | enum | YES | See §4 |
| `notes` | string | NO | Free-text notes |

### 3.2 BRANCH Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `name` | string | YES | Branch name |
| `local_remote` | enum | YES | `local_only` / `remote_tracked` / `remote_only` |
| `tracking_remote` | string | NO | Remote branch name if tracked |
| `ahead_behind` | string | NO | Ahead/behind status vs remote |
| `latest_commit_sha` | string | YES | HEAD commit SHA |
| `latest_commit_date` | string | YES | HEAD commit date |
| `latest_commit_msg` | string | YES | HEAD commit message |
| `diff_stat_vs_main` | string | NO | `git diff --stat main..<branch>` summary |
| `topic_domain` | enum | YES | See §4 |
| `maturity` | enum | YES | See §4 |
| `canonicality` | enum | YES | See §4 |
| `preservation_class` | enum | YES | See §4 |
| `risk_level` | enum | YES | See §4 |
| `unique_content_summary` | string | YES | What is unique to this branch |
| `related_items` | list | NO | IDs of related branches/manuscripts |
| `retrieval_priority` | enum | YES | See §4 |
| `notes` | string | NO | Free-text notes |

### 3.3 MANUSCRIPT Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `branch_id` | string | YES | Branch where canonical version lives |
| `title` | string | YES | Manuscript title |
| `type` | enum | YES | `book` / `paper` / `companion` / `program_note` / `framework` / `monograph` |
| `driver_path` | string | YES | Path to main `.tex` driver file |
| `document_class` | string | YES | LaTeX document class |
| `chapter_count` | integer | NO | Number of chapters/sections |
| `appendix_count` | integer | NO | Number of appendices |
| `include_count` | integer | YES | Number of `\input`/`\include` commands |
| `page_count_estimate` | integer | NO | Estimated page count from PDF if available |
| `doi` | string | NO | DOI if published |
| `topic_domain` | enum | YES | See §4 |
| `maturity` | enum | YES | See §4 |
| `canonicality` | enum | YES | See §4 |
| `preservation_class` | enum | YES | See §4 |
| `surfacing_priority` | enum | YES | See §4 and §7 |
| `related_items` | list | NO | IDs of related manuscripts, branches, files |
| `duplicates` | list | NO | IDs of known duplicates or parallel versions |
| `build_artifacts` | list | NO | IDs of associated ARTIFACT records |
| `retrieval_priority` | enum | YES | See §4 |
| `notes` | string | NO | Free-text notes |

### 3.4 FILE Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `branch_id` | string | YES | Branch ID |
| `manuscript_id` | string | NO | Parent manuscript ID if part of one |
| `basename` | string | YES | Filename only (e.g., `main.tex`) |
| `relative_path` | string | YES | Path relative to repo root |
| `full_identity` | string | YES | `(repo, branch, relative_path)` tuple |
| `file_type` | string | YES | Extension (`.tex`, `.py`, `.pdf`, `.md`) |
| `size_bytes` | integer | NO | File size |
| `checksum_sha256` | string | NO | SHA256 checksum |
| `topic_domain` | enum | YES | See §4 |
| `maturity` | enum | YES | See §4 |
| `canonicality` | enum | YES | See §4 |
| `preservation_class` | enum | YES | See §4 |
| `same_name_conflicts` | list | NO | IDs of other FILE records with same basename |
| `duplicates` | list | NO | IDs of byte-identical or content-identical files |
| `provenance_notes` | string | NO | Origin, history, supersession info |
| `retrieval_priority` | enum | YES | See §4 |
| `notes` | string | NO | Free-text notes |

### 3.5 STASH Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `stash_ref` | string | YES | Git stash reference (e.g., `stash@{0}`) |
| `parent_branch` | string | YES | Branch the stash was created on |
| `description` | string | YES | Stash message |
| `content_summary` | string | YES | What files are modified/added |
| `preservation_class` | enum | YES | See §4 |
| `risk_level` | enum | YES | See §4 |
| `converted_to_branch` | string | NO | Branch name if converted |
| `notes` | string | NO | Free-text notes |

### 3.6 UNTRACKED Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `relative_path` | string | YES | Path relative to repo root |
| `basename` | string | YES | Filename |
| `file_type` | string | YES | Extension |
| `size_bytes` | integer | NO | File size |
| `checksum_sha256` | string | NO | SHA256 checksum |
| `content_summary` | string | YES | Brief description of content |
| `preservation_class` | enum | YES | See §4 |
| `risk_level` | enum | YES | See §4 |
| `committed_to` | string | NO | Branch name if later committed |
| `notes` | string | NO | Free-text notes |

### 3.7 ARTIFACT Record

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | YES | Unique ID |
| `repo_id` | string | YES | Parent repo ID |
| `relative_path` | string | YES | Path relative to repo root |
| `basename` | string | YES | Filename |
| `artifact_type` | string | YES | `pdf_build` / `dated_snapshot` / `build_log` |
| `source_manuscript_id` | string | NO | Manuscript this was built from |
| `build_date` | string | NO | Date of build if known |
| `page_count` | integer | NO | Page count for PDFs |
| `size_bytes` | integer | NO | File size |
| `preservation_class` | enum | YES | See §4 |
| `notes` | string | NO | Free-text notes |

---

## 4. Canonical Controlled Vocabularies

### 4.1 Maturity

| Value | Meaning |
|-------|---------|
| `released` | Published, with DOI or version-stamped release |
| `canonical` | Accepted as authoritative within the project |
| `developed_draft` | Substantially complete manuscript or derivation |
| `active_draft` | Under current development |
| `exploratory_draft` | Early-stage exploration, may not be viable |
| `dead_end` | Completed investigation with negative or null result |
| `superseded` | Replaced by a newer version |
| `unknown` | Not yet assessed |

### 4.2 Canonicality

| Value | Meaning |
|-------|---------|
| `canon_published` | Published with DOI; externally citable |
| `canon_locked` | Locked within the project (e.g., ontology canon v1.0) |
| `canon_active` | Current canonical working version |
| `draft` | Not yet canonical; may become so |
| `historical` | Was canonical at one point; now superseded |
| `never_canonical` | Was never intended as canonical (exploration, attempt) |

### 4.3 Preservation Class

| Value | Meaning |
|-------|---------|
| `PC-CANON` | Published/released/locked material |
| `PC-ACTIVE` | Active development targets |
| `PC-BOOK` | Complete manuscript |
| `PC-LOCAL-BRANCH` | Local-only branch content |
| `PC-STASH` | Git stash content |
| `PC-UNTRACKED` | Untracked research files |
| `PC-PRIVATE` | Private repo material |
| `PC-NONREPO` | Non-git research material |
| `PC-SNAPSHOT` | Dated snapshot or standalone copy |
| `PC-DEADEND` | Dead-end with forensic value |
| `PC-DRAFT` | Draft-stage companion or paper |
| `PC-GRAVITY` | Gravity derivation program |

### 4.4 Risk Level

| Value | Meaning |
|-------|---------|
| `critical` | Material exists only locally with no backup; loss is permanent |
| `high` | Material has limited backup or is in fragile state |
| `medium` | Material is partially backed up but not fully secured |
| `low` | Material is fully backed up to at least one remote |
| `none` | Material is published externally (DOI) |

### 4.5 Topic Domain

| Value | Scope |
|-------|-------|
| `proton_anatomy` | Proton 5D structure, Y-junction, Steiner |
| `neutron_anatomy` | Neutron 5D structure, metastable junction, half-Steiner |
| `decay_ontology` | Neutron decay, beta processes, weak catalog |
| `particle_ontology` | General particle classification, five-category |
| `pion` | Pion anatomy and decay |
| `muon` | Muon anatomy and decay |
| `tau` | Tau anatomy and decay |
| `electron` | Electron anatomy and stability |
| `neutrino` | Neutrino anatomy, edge mode |
| `weak_sector` | Weak interactions, OPR, BVP, G_F |
| `cluster_binding` | Pinning, cluster structure, Book IV |
| `metastable_lifetime` | Neutron lifetime, instanton, WKB |
| `gravity` | Gravity derivation program |
| `fine_structure` | Fine-structure constant, Paper 2 |
| `symmetry` | Z₆, Z₃, Z₂, SU(3), junction symmetries |
| `ontology_meta` | Ontology dictionaries, canon documents |
| `audit` | Audit reports, forensic memos, closure states |
| `infrastructure` | Code, styles, BVP solvers, shared tools |
| `mixed` | Spans multiple domains |

### 4.6 Retrieval Priority

| Value | Meaning |
|-------|---------|
| `immediate` | Needed for current active work |
| `high` | Should be surfaced in the next planning cycle |
| `medium` | Useful but not blocking |
| `low` | Archival interest only |
| `reference` | Useful as background but not actionable |

### 4.7 Surfacing Priority

| Value | Meaning |
|-------|---------|
| `first_class` | Must be surfaced as a named priority (e.g., Book II) |
| `standard` | Normal surfacing via catalog |
| `archival` | Surface only into archive, not active workspace |
| `none` | Already surfaced or not applicable |

### 4.8 Reorganization Destination

| Value | Target in umbrella structure |
|-------|------------------------------|
| `canon/books/` | Canonical book manuscripts |
| `canon/papers/` | Published papers and companions |
| `canon/ontology/` | Locked ontology and canon documents |
| `active/` | Current development material |
| `research_archive/` | Completed investigations |
| `local_recovered/` | Material recovered from local-only sources |
| `infrastructure/` | Shared tools and standards |
| `catalogs/` | Indexes, maps, registries |
| `build_artifacts/` | Compiled outputs |

---

## 5. ID Convention

### Format

```
<type>-<repo_slug>-<branch_slug>-<running_number>
```

### Type prefixes

| Prefix | Record type |
|--------|------------|
| `R` | REPO |
| `B` | BRANCH |
| `M` | MANUSCRIPT |
| `F` | FILE |
| `S` | STASH |
| `U` | UNTRACKED |
| `A` | ARTIFACT |

### Repo slugs

| Slug | Repo |
|------|------|
| `edc` | `elastic-diffusive-cosmology_repo` |
| `prv` | `EDC_Research_PRIVATE` |
| `loc` | Local non-git folder |

### Branch slugs

For branches, use a shortened form:
- `main` → `main`
- `research/topological-pinning-v7_8-integration` → `topo-v78`
- `junction-core-well-v1` → `jcw-v1`
- `book2-opr20-mediator-mass-v1` → `opr20-mm`

For non-git items, use `nogit`.

### Examples

| ID | Meaning |
|----|---------|
| `R-edc-001` | Main EDC repo |
| `R-prv-001` | Private research repo |
| `B-edc-main-001` | Main branch of EDC repo |
| `B-edc-jcw-v1-001` | Junction core well branch |
| `M-edc-main-001` | Book I manuscript |
| `M-edc-main-002` | Book II manuscript |
| `M-edc-topo-v78-003` | Book IV manuscript |
| `F-edc-main-001` | A specific file in main branch |
| `S-edc-001` | Stash #0 |
| `U-edc-001` | An untracked file |
| `A-edc-001` | A build artifact |

---

## 6. Same-Name File Handling Rule

### Core rule

**Basename is NEVER sufficient identity.** Two files with the same basename
are distinct catalog entries with distinct IDs unless provenance comparison
confirms byte-level identity.

### Full identity

A file's identity is the tuple:

```
(repo_id, branch_id, relative_path, basename)
```

This tuple is stored in the `full_identity` field of every FILE record.

### Catalog behavior

- Every FILE record with a non-unique basename must have its
  `same_name_conflicts` field populated with the IDs of all other FILE
  records sharing that basename.

- The catalog search interface must never return a file by basename alone.
  Queries must specify at least one additional disambiguator (repo, branch,
  path prefix, or topic domain).

### Re-housing behavior

- If two same-name files must coexist in one directory during re-housing,
  they are disambiguated by prepending the source context with a `__`
  separator: `book_II__main.tex`, `book_IV__main.tex`.

- The provenance record for each re-housed file links back to the original
  FILE record ID and full identity tuple.

### No-overwrite enforcement

- Any re-housing operation that would place a file at a destination where a
  file already exists with the same name is BLOCKED until the operator
  confirms one of:
  (a) The files are byte-identical (checksum match) — proceed with link, not copy.
  (b) The files are distinct — apply disambiguation naming.
  (c) The existing file is to be archived first — create archive copy, then proceed.

- Option (a) requires SHA256 confirmation. Option (c) requires a catalog
  record for the archived file.

---

## 7. Book II Priority Marker

### Schema support

The MANUSCRIPT record includes a `surfacing_priority` field (§4.7). Book II
is marked `first_class`.

### Distinction from risk level

Surfacing priority is NOT the same as risk level:

| Field | Question it answers |
|-------|-------------------|
| `risk_level` | "How likely is this to be lost?" |
| `surfacing_priority` | "How important is it to make this accessible?" |

Book II has `risk_level: medium` (it exists in the repo, just not prominently)
but `surfacing_priority: first_class` (it contains the full weak-sector
particle ontology that current work needs).

### Effect on execution ordering

Items marked `surfacing_priority: first_class` are processed in Phase D
before any `standard` items. In practice, this means:

1. Book II gets a canonical chapter map before other buried manuscripts
2. Book II gets cross-reference links from Book IV audit space first
3. Book II's retrieval path is created before other topic-level catalogs

### Example MANUSCRIPT record for Book II

```
id: M-edc-main-002
title: "EDC Book II: Weak Sector"
type: book
driver_path: edc_book_2/reorganized/main.tex
document_class: book
chapter_count: 17
appendix_count: 3
include_count: 26
page_count_estimate: 387
doi: null
topic_domain: weak_sector
maturity: developed_draft
canonicality: canon_active
preservation_class: PC-BOOK
surfacing_priority: first_class
retrieval_priority: high
duplicates: [F-loc-nogit-001]   # standalone EDC_Book_2/ copy
notes: "17-chapter weak-sector manuscript with 3 parts, OPR registry,
        per-particle case studies, BVP/G_F infrastructure. Confirmed
        as developed by FULL_FORENSIC_DISCOVERY_AND_INVENTORY.md
        (commit 4af3f9e). Surfacing priority per §7 of
        MASTER_CATALOG_AND_REORG_PLAN.md."
```

---

## 8. Minimal Example Records

### 8.1 Canonical book (Book I)

```
id: M-edc-main-001
title: "EDC Theory Book v17.49"
type: book
driver_path: edc_book/main.tex
document_class: book
chapter_count: 12
appendix_count: 3
include_count: 20
page_count_estimate: ~200
doi: null
topic_domain: mixed
maturity: released
canonicality: canon_published
preservation_class: PC-CANON
surfacing_priority: none
retrieval_priority: reference
notes: "Released v17.49. PDF at edc_book/releases/v17.49/."
```

### 8.2 Book II (surfacing-priority manuscript)

See §7 above.

### 8.3 Buried local-only branch item

```
id: B-edc-jcw-v1-001
repo_id: R-edc-001
name: junction-core-well-v1
local_remote: local_only
latest_commit_sha: [to be captured]
topic_domain: metastable_lifetime
maturity: dead_end
canonicality: never_canonical
preservation_class: PC-LOCAL-BRANCH
risk_level: critical
unique_content_summary: "+72k lines, 27 files. Junction core well
    computation and artifacts. Result integrated as no-go in
    MINIMAL_CLASS_CLOSURE_MEMO."
retrieval_priority: low
notes: "Forensic record of extensive computation. Dead-end but
    valuable as provenance for the N7 closure."
```

### 8.4 Stash

```
id: S-edc-001
repo_id: R-edc-001
stash_ref: stash@{3}
parent_branch: part2-gf-opr20-suppression-attempt2
description: "WIP on OPR-20 suppression mechanism"
content_summary: "Modified files related to OPR-20 factor-8
    suppression investigation."
preservation_class: PC-STASH
risk_level: high
notes: "Active research WIP. Must not be dropped without catalog."
```

### 8.5 Untracked manuscript

```
id: U-edc-001
repo_id: R-edc-001
relative_path: edc_book_4/main_final.pdf
basename: main_final.pdf
file_type: .pdf
content_summary: "Final build PDF of Book IV, ~228 pages."
preservation_class: PC-UNTRACKED
risk_level: high
notes: "Not in git. Would be lost by git clean."
```

### 8.6 PDF build artifact

```
id: A-edc-001
repo_id: R-edc-001
relative_path: edc_book_4/main_228_pages.pdf
basename: main_228_pages.pdf
artifact_type: dated_snapshot
source_manuscript_id: M-edc-topo-v78-003
page_count: 228
preservation_class: PC-SNAPSHOT
notes: "Dated Book IV build. May capture a state not in current HEAD."
```

### 8.7 Same-name `main.tex` file

```
id: F-edc-main-042
repo_id: R-edc-001
branch_id: B-edc-main-001
basename: main.tex
relative_path: edc_papers/paper_3_series/13_companion_P_pion_decay/paper/main.tex
full_identity: (R-edc-001, B-edc-main-001, edc_papers/paper_3_series/13_companion_P_pion_decay/paper/main.tex)
file_type: .tex
topic_domain: pion
maturity: exploratory_draft
canonicality: draft
preservation_class: PC-DRAFT
same_name_conflicts: [F-edc-main-001, F-edc-main-002, ..., F-edc-main-097]
retrieval_priority: medium
notes: "Companion P: Pion Decay, v0.3 QA-hardened. One of 97 files
    named main.tex. Identity requires full path."
```

---

## 9. Population Rules

### Ordering

1. **Immediate-risk assets first.** Populate records for all Rank 1-6 items
   from the Immediate Risk Table before any other entries.
2. **Manuscripts second.** Create MANUSCRIPT records for all identified books,
   papers, and companions.
3. **Branches third.** Create BRANCH records for all 83 local branches.
4. **Files fourth.** Create FILE records for high-value files, starting with
   same-name conflicts (`main.tex` instances).
5. **Artifacts last.** Create ARTIFACT records for significant PDFs.

### Mandatory rules

- **No guessing.** Every field must be populated from direct inspection or
  left as `null` / `unknown`. Do not infer content from filenames alone.
- **Path + provenance mandatory.** Every FILE, UNTRACKED, and ARTIFACT record
  must include the full relative path and repo ID.
- **Duplicates linked, not erased.** When two records represent the same
  content, populate the `duplicates` field on both. Do not delete either.
- **Same-name files cataloged as separate identities.** Each `main.tex` gets
  its own FILE record with a unique ID and full identity tuple.
- **Preservation class mandatory.** Every record must have a preservation
  class assigned before any Phase C re-housing is attempted.

### Quality gate

The catalog is considered minimally viable when:
- All REPO records exist
- All MANUSCRIPT records exist
- All BRANCH records for local-only branches exist
- All STASH records exist
- All same-name `main.tex` FILE records exist (97+)
- Book II has a complete MANUSCRIPT record with `surfacing_priority: first_class`

---

## 10. Bottom Line

This schema is a preservation tool, not a cleanup tool. It exists to ensure
that every piece of rediscovered EDC research material can be identified,
located, compared, and re-housed without loss of identity or provenance. The
controlled vocabularies prevent ambiguity. The ID convention prevents
collision. The same-name handling rule prevents overwrite. The surfacing
priority field ensures Book II is treated as a first-class asset.

Population follows the Protection Gate. No catalog entry justifies deletion
of its source. The catalog maps the territory; it does not reshape it.
