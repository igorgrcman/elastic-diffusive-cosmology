# Full Forensic Discovery and Inventory

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Forensic discovery across local disk, local git state, and all branches
**Classification:** No new derivations, no new ontology — inventory only

---

## 1. Executive Verdict

The EDC research ecosystem is **larger, more structured, and more at-risk than
it may appear from the current branch alone**.

**What was searched:** Local disk under `/Users/igor/ClaudeAI/EDC_Project/`
(sandbox boundary prevented broader disk search), all git branches (83 local,
24 remote), 4 stashes, untracked files, and a second private repo.

**Buried major material exists.** The most significant findings:

1. **61 local-only branches** with no remote backup. If this machine's disk
   fails, all that research is lost. One branch (`junction-core-well-v1`)
   contains +72k lines of unique computation.

2. **`main` is 14 commits ahead of `origin/main`** — unpushed canonical work.

3. **EDC_Research_PRIVATE** — a separate private git repo at
   `/Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE/` containing a
   knowledge base (30+ files), organized derivations (`critical/`, `valuable/`,
   `archive/`), canon PDFs, and unique material not in the main repo.

4. **Book II (`edc_book_2/`) is a full 17-chapter book** with 3 parts, OPR
   registry, extensive BVP/G_F infrastructure, and per-particle case studies.
   This is not a draft — it is a developed manuscript.

5. **No Book III exists.** The numbering goes I, II, IV. Either Book III was
   never started, or it exists under a different name.

6. **22 entries in paper_3_series** (not just the 10 priority companions), plus
   67 gravity derivation versions.

7. **Local-only working notes** in Croatian (`current/`) and a standalone proof
   audit (`aside_proof_audit/`) exist outside any git repo.

**The current canonical branch is the best state for Book IV work**, but the
broader EDC ecosystem extends far beyond it.

---

## 2. Scope and Method

### Local disk scope
- Searched: `/Users/igor/ClaudeAI/EDC_Project/` and all subdirectories
- Sandbox prevented: `/Users/igor/Downloads`, `/Users/igor/Desktop`,
  `/Users/igor/Documents`, and broader home directory
- Found: 12 distinct locations with EDC material

### Local repo scope
- Primary repo: `elastic-diffusive-cosmology_repo/` (single remote: `origin` at
  GitHub `igorgrcman/elastic-diffusive-cosmology`)
- Secondary repo: `EDC_Research_PRIVATE/` (access limited during this session)

### Stash/untracked scope
- 4 stashes inspected
- 42+ untracked files in `edc_book_4/`
- Untracked files in other directories cataloged

### GitHub/branch scope
- `git fetch --all --prune` executed
- 83 local branches enumerated
- 24 remote branches enumerated
- 61 local-only branches identified (no remote tracking)
- Key branches content-inspected via `git log` and `git diff --stat`

### File types scanned
- All `.tex` (97 `main.tex` files found and classified)
- All `.pdf` (significant manuscripts identified by size)
- All `.py` (computation code mapped)
- All `.md` (governance/audit/ontology files mapped)
- Generic names (`main.tex`, `main.pdf`) resolved by path context and
  `\documentclass` inspection

---

## 3. Repo Inventory

| # | Repo/Path | Local/Remote | Relevance | Notes |
|---|-----------|-------------|-----------|-------|
| 1 | `elastic-diffusive-cosmology_repo/` | Both (origin at GitHub) | PRIMARY | 3 books, 22 papers, 67 gravity versions, 83 branches |
| 2 | `EDC_Research_PRIVATE/` | Local git repo (access limited) | HIGH | KB, derivations, canon PDFs, private releases |
| 3 | `EDC_Book_2/` (standalone) | Local only, no git | MEDIUM | Standalone Book II copy: `EDC_Book_II_main.tex` (53 KB) + PDF (368 KB) |
| 4 | `build/` | Local only, no git | LOW | Build output: `EDC_Book2_2026-01-25_OPEN22-4b.pdf` (1.96 MB) |
| 5 | `edc_paper_2_archive/` | Local only, no git | MEDIUM | Frozen Paper 2 release archive with private/public bundles |
| 6 | `current/` | Local only, no git | HIGH | 12 working notes, many in Croatian (personal analysis) |
| 7 | `obsolite/` | Local only, no git | LOW | 2 superseded derivation tasks |
| 8 | `aside_proof_audit/` | Local only, no git | HIGH | Proof ledger, missing lemmas, consistency checklist, source map |
| 9 | `Literatura/` | Local only, no git | LOW | External reference PDF only |
| 10 | `dmining/` | Local only, no git | LOW | Claude Code session JSONL logs |
| 11 | Standalone files | Local only | MEDIUM | `EDC_Clean_Core_Paper_Structure...txt`, `EDC_Path_Forward_Claim_Ledger...md` |

---

## 4. Local-Only / Hidden Material

### 4A. Critical: 61 local-only git branches

**61 of 83 local branches have no remote tracking.** These exist only on this
machine. Grouped by research area:

| Cluster | Branches | Key content | Risk |
|---------|----------|------------|------|
| **Audit/Gap Register** (9) | `audit/donor-hunt-pass3-v1`, `audit/gap-register-full-v1`, `audit/prelet-scan-v1`, `backfill/tier0-v1`, `backfill/tier1-v1`, `backfill/tier2-v1`, `backfill/top5-v1`, `backfill/pmns-theta23-v1`, `audit/donor-hunt-pmns-v1` | Systematic gap registers (90 entries), tier-0/1/2 backfill derivations, PMNS theta_23 success case | HIGH — unique audit infrastructure |
| **Book 2 OPR** (20+) | `book2-opr01-*` through `book2-opr22-*`, `book2-opr-registry-v1` | OPR-01 to OPR-22 derivation attempts, registry, physical path lock | HIGH — OPR derivation history |
| **CKM/PMNS** (5) | `part2-ckm-attempt4-*`, `part2-pmns-attempt4-*` | CKM delta refinement, Z₂ parity origin, theta_12 geometric origin | MEDIUM — attempt history |
| **G_F closure** (8) | `part2-gf-opr19-*`, `part2-gf-opr20-*`, `part2-gf-opr22-*` | g₅ derivation, factor-8 forensic sweep (6 attempts), G_F full closure plan | HIGH — detailed forensic record |
| **Notation/Canon** (5) | `part2-notation-*`, `book2-global-symbol-table-v1`, `delta-audit-anchor-v1` | Global symbol table, xi vs z mapping, notation unification | MEDIUM |
| **Junction/Core/Derivation** (8) | `junction-core-well-v1` (+72k lines), `helfrich-well-from-action-v1` (+12k), `putC-computation-v1`, `taskB-derive-Mq-v1`, `taskC-derive-Gamma0-v1`, `taskD-bounce-scaling-audit-v1` | Node-well computations, Helfrich NO-GO, Put C reduction, prefactor derivation | HIGH — unique computation artifacts |
| **Epistemic/Reorg** (3) | `reorganization-epistemic-framework` (+16k, 46 files), `book2-ch1-asset-inventory-v1`, `book2-neutron-dual-route-v1` | v2.0 epistemic framework, asset inventories, dual-route audit | MEDIUM |
| **Other** (3) | `book-routeC-narrative-cleanup-v1`, `frozen-brane-bc-v1`, `junction-core-derive-C-v1` | Narrative cleanup, frozen brane dual-route, C derivation | LOW-MEDIUM |

### 4B. Stashes

| # | Branch | Description | Risk |
|---|--------|-------------|------|
| 0 | `book-routeC-narrative-cleanup-v1` | WIP before reorganization | LOW |
| 1 | `book2-opr04-delta-derivation-v1` | Build artifacts | LOW |
| 2 | `part2-notation-canon-xi` | WIP before merge | MEDIUM |
| 3 | `part2-gf-opr20-suppression-attempt2` | WIP on OPR-20 suppression | MEDIUM |

### 4C. Non-git local-only material

| Location | Items | Why it matters | Status |
|----------|-------|---------------|--------|
| `current/` | 12 files incl. `EDC_Kompletni_Sazetak_Igor.md` (Croatian summary), `EDC_Quick_Reference.md`, task derivations a1-a3, b2-b5 | Personal analysis and working notes in native language; unique perspective not in any repo | NOT BACKED UP |
| `aside_proof_audit/` | `PROOF_LEDGER.md`, `MISSING_LEMMAS.md`, `CONSISTENCY_CHECKLIST.md`, `CLAIM_SITE_LOCATOR.md`, `SOURCE_MAP.csv` | Systematic proof audit infrastructure | NOT BACKED UP |
| `EDC_Book_2/` | `EDC_Book_II_main.tex` + PDF | May be an earlier/alternate Book II version | NOT BACKED UP |
| `edc_paper_2_archive/` | Full Paper 2 release bundle with private versions | Contains assumption ledgers, traceability matrices not in main repo | NOT BACKED UP |
| Standalone files | `EDC_Clean_Core_Paper_Structure...txt`, `EDC_Path_Forward_Claim_Ledger...md` | Structural planning documents | NOT BACKED UP |

### 4D. Unpushed main branch

**`main` is 14 commits ahead of `origin/main`.** This is unpushed canonical work
on the default branch.

### 4E. EDC_Research_PRIVATE

A separate git repo at `/Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE/`
containing:
- `canon/` — canonical source PDFs with SHA256 checksums
- `EDC_KB/` — 30+ knowledge base files (Complete Relations, Gold Mine Archive,
  Proton, 3 Vortex, 5D Topological, Neutron Decay, Generations, Z Boson,
  Cosmology, Entanglement, Gravity, Muon/Pion, Epistemology, Tier analyses)
- `derivations/` — organized `critical/`, `valuable/`, `value added/`, `archive/`
- `releases/` — private/public release bundles for Papers 2 and 3
- `P7_derivation/` — electron/proton energy, variational, stability Hessian,
  H2 bulk-bridge, frozen-vs-GL analysis, 5D geometry audit
- `docs/`, `simulations/`, `templates/`, `tools/`, `code/`

Access was limited during this session. **This repo's backup status is unknown.**

---

## 5. High-Value Book / Manuscript Candidates

| ID | Repo | Branch | File/Path | Type | Why book-like | Maturity | Canon | Priority |
|----|------|--------|-----------|------|-------------|----------|-------|----------|
| BK-1 | main | current | `edc_book/main.tex` | **Full Book (Book I)** | `\documentclass{book}`, 12 chapters + epilogue + 3 appendices + glossary, released PDF v17.49 | Released | YES | Reference |
| BK-2 | main | current | `edc_book_2/reorganized/main.tex` | **Full Book (Book II)** | `\documentclass{book}`, 17 chapters in 3 parts + epilogue + 3 appendices, OPR registry, per-particle case studies, BVP/G_F infrastructure | Developed manuscript | YES | HIGH |
| BK-3 | main | current | `edc_book_4/main.tex` | **Full Book (Book IV)** | `\documentclass{book}`, 17 chapters in 6 parts + 11 appendices + glossary, ~228 pages, active development | Active draft | YES | ACTIVE |
| BK-4 | main | current | `edc_papers/paper_3_series/` (22 entries) | **Companion paper set** | 10 published (DOI), 12 additional entries including draft companions M/T/P/L/V/N + program overview + weak sector consolidations | Mixed canonical/draft | Partial | HIGH |
| BK-5 | main | current | `edc_papers/paper_gravity_block003/` | **Gravity derivation program** | 67 versioned derivations + program note, v67 "REAL CLOSED" | Closed program | YES | Reference |
| BK-6 | local only | — | `EDC_Research_PRIVATE/` | **Private research repo** | KB (30+ files), organized derivations, canon PDFs, P7 derivation program | Active private | Unknown | HIGH |
| BK-7 | local only | — | `EDC_Book_2/EDC_Book_II_main.tex` | **Standalone Book II** | 53 KB tex + 368 KB PDF | Snapshot | Likely superseded | LOW |
| BK-8 | main | current | `edc_papers/paper_3_series/20_book_chapter_weak_interface/` | **Book chapter: Weak Interface** | Full chapter with rebuild snapshot, bridging papers → Book II | Developed | YES | MEDIUM |
| BK-9 | main | current | `edc_book_2/src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.pdf` | **Topological Pinning Monograph** | Standalone PDF in Book II derivations | Unknown | Unknown | MEDIUM |

### Assessment

**Three full books exist** (I, II, IV). **No Book III.** Book II is the most
underappreciated — it is a full 17-chapter manuscript with extensive OPR
infrastructure, not just a collection of notes. The paper_3_series is effectively
a fourth "book" spread across 22 companion papers.

---

## 6. High-Value Topic Clusters

### 6A. Proton / Neutron Anatomy

| Source | Location | Uniqueness | Integrated? |
|--------|----------|-----------|-------------|
| Companion F (proton variational) | `paper_3_series/07_companion_F/` | Canonical derivation, zero calibrated params | YES — published DOI |
| Companion G (mass split) | `paper_3_series/08_companion_G/` | Z₆ ring, q parameter, Δm derivation | YES — published DOI |
| Book IV ch01 (anchor junction) | `edc_book_4/chapters/ch01_proton_ground.tex` | EDC-native vocabulary | YES — current branch |
| Book IV ch03 (metastable junction) | `edc_book_4/chapters/ch03_neutron_metastable.tex` | EDC-native vocabulary | YES — current branch |
| Book II §04 (ontology) | `edc_book_2/src/sections/04_ontology.tex` | Five-category classification | YES — Book II |
| Companion N (neutron junction) | `paper_3_series/10_companion_N/` | Draft v0.1 | Partially |
| Private KB: Proton, 3 Vortex, 5D | `EDC_Research_PRIVATE/EDC_KB/` | Unique KB files | NOT integrated |
| P7 derivation | `EDC_Research_PRIVATE/P7_derivation/` | Electron/proton energy, Hessian | NOT integrated |

**Best files:** Companions F and G (derivation), Book IV ch01/ch03 (narrative),
Book II §04 (classification).
**Buried:** Private KB files and P7 derivation — unique, not integrated.

### 6B. Decay Ontology / Weak Sector

| Source | Location | Uniqueness | Integrated? |
|--------|----------|-----------|-------------|
| Companion H (weak catalog) | `paper_3_series/09_companion_H/` | Complete 6-process catalog | YES — published DOI |
| Companion D (selection rules) | `paper_3_series/05_companion_D/` | Two-output theorem | YES — published DOI |
| Companion E (symmetry ops) | `paper_3_series/06_companion_E/` | E/R/M operators, beta ledger | YES — published DOI |
| Book II full manuscript | `edc_book_2/reorganized/` | 17-chapter weak-sector book | YES — developed |
| Book II case studies | `edc_book_2/src/sections/05-10` | Per-particle narratives | YES |
| Draft companions M/T/P/L/V | `paper_3_series/11-16/` | Muon, tau, pion, electron, neutrino | Draft stage |
| Weak Program Overview | `paper_3_series/14/` | Unified pipeline registry | YES |
| 20+ local-only OPR branches | Local branches `book2-opr*` | OPR derivation history | LOCAL ONLY |
| 8 G_F closure branches | Local branches `part2-gf-*` | Factor-8 forensic investigation | LOCAL ONLY |

**Best files:** Companion H (catalog), Book II reorganized (full book),
case studies (narratives).
**Buried:** 28+ local-only branches with OPR and G_F derivation history.

### 6C. Neutron Line / Book IV / Put C

| Source | Location | Uniqueness | Integrated? |
|--------|----------|-----------|-------------|
| Book IV full manuscript | `edc_book_4/` | 17 chapters, 11 appendices, ~228pp | YES — active |
| Paper 3 NJSR | `paper_3_series/01/` | Neutron lifetime calculation | YES — published DOI |
| Companions A/B/C | `paper_3_series/02-04/` | L_eff, WKB, reduction pipeline | YES — published DOI |
| Put C computation | Local branch `putC-computation-v1` | S₅D→S_eff[q] reduction with figures | LOCAL ONLY |
| Junction core well | Local branch `junction-core-well-v1` | +72k lines of computation | LOCAL ONLY |
| Helfrich NO-GO | Local branch `helfrich-well-from-action-v1` | +12k lines, NO-GO documentation | LOCAL ONLY |
| Task B/C/D branches | Local branches `taskB/C/D-*` | M(q), Γ₀, bounce scaling | LOCAL ONLY |
| Closure memos | `edc_book_4/audit/` | Exhaustion memo, NMCP, minimal-class | YES — current branch |

**Best files:** Book IV (active), Paper 3 + companions A-C (published).
**Buried:** `junction-core-well-v1` (+72k lines), `putC-computation-v1`,
`helfrich-well-from-action-v1` — all local-only with unique computation artifacts.

### 6D. OPR-19..22 / BVP / Weak Program

| Source | Location | Uniqueness | Integrated? |
|--------|----------|-----------|-------------|
| OPR Registry | `edc_book_2/canon/opr/OPR_REGISTRY.md` | Master registry | YES |
| OPR-19 (g₅ from action) | `edc_book_2/canon/opr/OPR-19.md` + branch `book2-opr19-*` | Definition + derivation attempts | Partial |
| OPR-20 (mediator mass) | `edc_book_2/canon/opr/OPR-20.md` + 6 factor-8 branches | Definition + extensive forensics | LOCAL branches |
| OPR-21 (BVP closure) | `edc_book_2/canon/opr/OPR-21.md` + branches | Definition + closure writeup | Partial |
| OPR-22 (G_eff) | `edc_book_2/canon/opr/OPR-22.md` + branch | Definition + derivation | Partial |
| BVP code | `edc_book_2/code/` (16 scripts) + `edc_papers/_shared/bvp_gf/` | Numerical infrastructure | YES |
| Audit evidence | `edc_book_2/audit/evidence/` (17+ reports) | Per-OPR derivation reports | YES |
| G_F toy derivation | `paper_3_series/17_open_W1_GF_toy_derivation/` | Open W1 | YES |
| Shared derivations | `edc_papers/_shared/derivations/` (8 PDFs) | Standalone results | YES |

**Best files:** OPR Registry + individual OPR files (definitions), Book II
chapters 12-16 (BVP/G_F chain), audit evidence reports.
**Buried:** 6 factor-8 forensic branches for OPR-20 — detailed investigation
record, all local-only.

### 6E. Broader Particle Ontology

| Source | Location | Uniqueness | Integrated? |
|--------|----------|-----------|-------------|
| Framework v2.0 | `paper_3_series/00/` + released PDF | Full EDC reference (37pp) | YES — DOI |
| Book II ontology hub | `edc_book_2/src/sections/04_ontology.tex` | Five-category classification + TikZ | YES |
| Book IV ontology canon | `edc_book_4/ontology/EDC_ONTOLOGY_CANON.md` | LOCKED v1.0 dictionary | YES |
| Draft companions (M/T/P/L/V/N) | `paper_3_series/10-16/` | Per-particle derivations | Draft |
| Private KB | `EDC_Research_PRIVATE/EDC_KB/` | 30+ topical KB files | NOT integrated |
| Muon/Pion KB entry | `EDC_Research_PRIVATE/EDC_KB/` | Dedicated muon/pion file | NOT integrated |

**Best files:** Framework v2.0 (comprehensive), Book II ontology (classification),
Ontology Canon (dictionary).
**Buried:** Private KB files — unique topical analyses not in main repo.

---

## 7. Branch-Level Findings

### Remote-tracked branches (22)

| Branch | Dominant Topic | Unique Value | Status |
|--------|---------------|-------------|--------|
| `main` | Canonical baseline | All integrated work | Canonical (14 ahead of origin!) |
| `research/topological-pinning-v7_8-integration` | Book IV active | Current active work | Active canonical |
| `feat/book4-ch01-fill` through `feat/book4-ch04-sigma-K` | Book IV chapter fills | Chapter content | Merged/integrated |
| Various `audit/*`, `feat/*` | Book IV development | Historical | Mostly merged |

### Key local-only branches (61 total, top 20 by value)

| Branch | Topic | Unique Value | Usefulness | Status |
|--------|-------|-------------|-----------|--------|
| `junction-core-well-v1` | Node-well computation | +72k lines, 27 files of junction core analysis | HIGH — historical record | Dead-end (result integrated as no-go) |
| `helfrich-well-from-action-v1` | Helfrich route | +12k lines, NO-GO result documentation | HIGH — forensic record | Dead-end (falsified) |
| `audit/gap-register-full-v1` | Gap register | +18k lines, systematic 17-gap search | HIGH — audit infrastructure | Valuable reference |
| `audit/prelet-scan-v1` | Prioritized gaps | 90-entry gap register | HIGH — planning tool | Valuable reference |
| `backfill/tier0-v1` | Critical gap fills | GAP-4 sin²θ_W, GAP-10 G_F chain, GAP-1 V-A | HIGH — derivation attempts | Valuable reference |
| `book2-opr-registry-v1` | OPR registry | Verified 387-page state | MEDIUM — superseded by current | Historical |
| `reorganization-epistemic-framework` | Epistemic reorg | +16k lines, 46 files, v2.0 framework | HIGH — structural work | Valuable reference |
| `book2-global-symbol-table-v1` | Symbol table | Global symbol extraction + tools | HIGH — unique infrastructure | Valuable reference |
| `part2-gf-opr20-factor8-forensic` | Factor-8 investigation | Forensic BC eigenvalue sweep | HIGH — research record | Investigation record |
| `part2-gf-opr20-factor8-attempt3` | Factor-8 attempt 3 | Factor-8 forensic route | MEDIUM — attempt history | Investigation record |
| `part2-gf-opr20-factor8-geometric-attemptC` | Geometric factor-8 | Geometric route attempt | MEDIUM — attempt history | Investigation record |
| `part2-pmns-attempt4-2-theta12-origin` | θ₁₂ origin | arctan(1/√2) geometric derivation | MEDIUM — specific result | Investigation record |
| `backfill/pmns-theta23-v1` | θ₂₃ success | PMNS theta_23 successful case | HIGH — positive result | Valuable |
| `putC-computation-v1` | Put C S₅D→S_eff | +3.4k lines with figures | MEDIUM — computation record | Historical |
| `book2-opr04-delta-derivation-v1` | Delta derivation | OPR-04 + TikZ figures | MEDIUM | Historical |
| `book2-opr21-closure-writeup-v1` | OPR-21 closure | 387→393 page expansion | MEDIUM | Historical |
| `frozen-brane-bc-v1` | Dual-route proof | Route A anchor + Route B Z₆→Steiner | MEDIUM | Valuable |
| `taskB-derive-Mq-v1` | M(q) derivation | Supermetric from 5D | MEDIUM | Historical |
| `taskC-derive-Gamma0-v1` | Γ₀ prefactor | Local mode spectrum derivation | MEDIUM | Historical |
| `delta-audit-anchor-v1` | Delta anchor | Delta anchor map with Compton anchor | LOW-MEDIUM | Reference |

---

## 8. Canonical vs Buried vs Duplicate

### Truly canonical (published, DOI, or locked)

| Item | Location | Status |
|------|----------|--------|
| Book I v17.49 | `edc_book/releases/v17.49/` | Released with PDF |
| Framework v2.0 | `paper_3_series/00/` + Zenodo PDF | Published, DOI |
| Paper 3 NJSR | `paper_3_series/01/` + Zenodo PDF | Published, DOI |
| Companions A-H | `paper_3_series/02-09/` + Zenodo PDFs | Published, DOI |
| Ontology Canon | `edc_book_4/ontology/EDC_ONTOLOGY_CANON.md` | LOCKED v1.0 |
| OPR Registry | `edc_book_2/canon/opr/OPR_REGISTRY.md` | Canon for Book II |
| Gravity v67 | `paper_gravity_block003/derivation_v67/` | REAL CLOSED |

### Buried but valuable

| Item | Location | Why valuable |
|------|----------|-------------|
| 61 local-only branches | Local git only | Unique computation, derivation attempts, forensic records |
| EDC_Research_PRIVATE KB | `EDC_Research_PRIVATE/EDC_KB/` | 30+ topical knowledge base files |
| EDC_Research_PRIVATE derivations | `EDC_Research_PRIVATE/derivations/` | Organized critical/valuable/archive |
| P7 derivation program | `EDC_Research_PRIVATE/P7_derivation/` | Electron/proton energy, Hessian, H2 bulk-bridge |
| Croatian working notes | `current/` | Personal analysis, unique perspective |
| Proof audit infrastructure | `aside_proof_audit/` | Systematic proof verification |
| Draft companions M/T/P/L/V/N | `paper_3_series/10-16/` | Per-particle decay derivations |
| Book II full manuscript | `edc_book_2/reorganized/` | 17-chapter developed book |

### Duplicate / superseded

| Item | Location | Superseded by |
|------|----------|--------------|
| `EDC_Book_2/` standalone | `EDC_Book_2/EDC_Book_II_main.tex` | `edc_book_2/reorganized/main.tex` |
| `build/` PDFs | `build/EDC_Book2_2026-01-25_OPEN22-4b.pdf` | Current Book II builds |
| `edc_paper_2_archive/` | Frozen archive | Main repo `edc_papers/paper_2/` + private releases |
| `obsolite/` tasks | 2 .md files | Current derivation branches |
| Gravity v1-v66 | `paper_gravity_block003/derivation_v1-v66/` | v67 (REAL CLOSED) |
| Framework v1.0 (if exists) | `paper_3_series/00/` | Framework v2.0 |

---

## 9. Most Important Recovery Targets

| Rank | Item | Location | Why it matters | What it gives | Urgency |
|------|------|----------|---------------|-------------|---------|
| **1** | Push `main` to origin | Local `main` branch | 14 unpushed commits on default branch | Backup of canonical work | CRITICAL |
| **2** | Push 61 local-only branches | Local git | +72k lines of unique computation, forensic records, no backup | Disaster recovery | CRITICAL |
| **3** | EDC_Research_PRIVATE backup status | `EDC_Research_PRIVATE/` | Unknown whether this repo is pushed anywhere | 30+ KB files, derivations, canon | HIGH |
| **4** | Back up `current/` | `current/` (no git) | Croatian analysis, working notes, no backup | Unique personal material | HIGH |
| **5** | Back up `aside_proof_audit/` | `aside_proof_audit/` (no git) | Proof infrastructure, no backup | Systematic verification | HIGH |
| **6** | Book II full assessment | `edc_book_2/reorganized/` | 17-chapter book may be more complete than realized | Full weak-sector manuscript | MEDIUM |
| **7** | Private KB integration assessment | `EDC_Research_PRIVATE/EDC_KB/` | 30+ topical files not in main repo | Knowledge base consolidation | MEDIUM |
| **8** | Draft companions (M/T/P/L/V/N) assessment | `paper_3_series/10-16/` | Per-particle decay derivations at draft stage | Particle ontology completion | MEDIUM |
| **9** | Gap register branches | `audit/gap-register-full-v1`, `audit/prelet-scan-v1` | Systematic gap tracking, 90+ entries | Research planning | MEDIUM |
| **10** | Factor-8 forensic branches | `part2-gf-opr20-factor8-*` (6 branches) | Detailed G_F investigation record | Research history preservation | LOW-MEDIUM |

---

## 10. Does a Buried "Whole Book" Exist?

**Yes.**

**Book II (`edc_book_2/reorganized/main.tex`) is a full, developed 17-chapter
book** that may be underappreciated. It has:
- `\documentclass{book}` with 3 parts and 17 chapters
- Part 1 (Ch 1-5): Foundations — Weak Interface, Ontology, Frozen Projection,
  Z₆ Program, Case Studies
- Part 2 (Ch 6-11): Electroweak — Leptons, Generations, Neutrinos, V-A,
  CKM/PMNS
- Part 3 (Ch 12-16): BVP/G_F — G_F Chain, Foundation Parameters, BVP, M_W/G_F,
  Epistemic Summary
- Epilogue (Ch 17): Beyond
- 3 appendices (OPR register, notation, numerical standards)
- Per-particle case studies (neutron, muon, tau, pion, electron, neutrino)
- Extensive code infrastructure (16 Python scripts)
- OPR registry with 22+ entries
- Audit infrastructure with 17+ evidence reports
- Multiple build PDFs (387-page verified state)

This is not a sketch or outline — it is a **developed manuscript** covering
exactly the particle anatomy and decay ontology that the previous task was
searching for. It is the closest thing to a "buried whole book" in the repo.

Additionally, the **paper_3_series** (22 entries) functions as a de facto book
spread across companion papers. If the 10 published companions (DOI) plus the
12 draft/follow-on entries were consolidated, they would form a comprehensive
reference volume.

The **EDC_Research_PRIVATE** repo may also contain book-like material (the
`theory_book/` directory was listed but not inspected due to access limitations).

**Strongest candidate:** Book II at `edc_book_2/reorganized/main.tex` — a real
book that is already built and has been through extensive OPR and audit cycles.

---

## 11. Recommended Retrieval Order

### Immediate (disaster recovery)

1. **Push `main` to origin** — 14 unpushed commits
2. **Push all 61 local-only branches to origin** — prevent data loss
3. **Verify EDC_Research_PRIVATE backup** — check if pushed to any remote

### Near-term (surface buried value)

4. **Back up `current/` and `aside_proof_audit/`** — add to a repo or archive
5. **Read Book II `reorganized/main.tex`** — understand full scope of the
   17-chapter weak-sector book
6. **Inspect `EDC_Research_PRIVATE/EDC_KB/`** — determine which KB files add
   value not present in the main repo

### Medium-term (integration assessment)

7. **Assess draft companions M/T/P/L/V/N** — determine which are ready for
   promotion toward canonical status
8. **Review gap register branches** — determine if the 90-entry gap register
   is still current and useful
9. **Review factor-8 forensic branches** — determine if the G_F investigation
   produced any recoverable results

### Low priority (archival)

10. **Clean up duplicates** — `EDC_Book_2/` standalone, `build/`, `obsolite/`,
    gravity v1-v66

---

## 12. Bottom Line

The EDC research ecosystem contains **three full books** (I, II, IV), **22
paper_3_series entries** (10 with DOIs), **67 gravity derivation versions**, a
**separate private repo** with 30+ KB files, and **61 local-only branches with
no remote backup**.

The most critical finding is the **backup risk**: 61 branches exist only on this
machine, `main` has 14 unpushed commits, and multiple research folders
(`current/`, `aside_proof_audit/`) exist outside any version control. Pushing
these to remote should be the immediate priority.

The most important content finding is that **Book II is a real, developed
17-chapter book** covering the full weak-sector particle ontology — exactly the
material that was being searched for in the previous task. It is not buried in
the sense of being hidden, but it may be underappreciated as a coherent
manuscript.

The repo landscape is architecturally sound but operationally fragile. The
research content is extensive and well-organized where it exists, but too much
of it lives only on local disk with no remote backup.
