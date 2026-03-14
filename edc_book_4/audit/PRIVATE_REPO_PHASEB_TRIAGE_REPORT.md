# Private Repo Phase B Triage Report

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration` (main repo)
**Target repo:** `EDC_Research_PRIVATE` at `https://github.com/igorgrcman/EDC_Research.git`
**Scope:** Targeted triage — cache noise, 5D branch inspection, research cluster assessment
**Governing inputs:** `PRIVATE_REPO_WAVE1_EXECUTION_REPORT.md`, `PRIVATE_REPO_WAVE1_STATUS.md`

---

## 1. Executive Verdict

**What was triaged:** Cache/build noise, the 5D-action derivation question, untracked
research clusters in `derivations/mass_difference/`, and 15 tracked modifications.

**What was safely reduced:** Nothing committed or ignored. All items were assessed but
deferred — the working tree is too mixed (source + build artifacts) for safe narrow action
without manual review.

**What remains ambiguous:** The untracked clusters in `derivations/analytic/` (~73 files
including 11 failure certificates) and `releases/paper_3_private/` (~80 entries) need
individual assessment.

**Critical correction from Wave 1:** The `.cache/` directory (reported as 4,152 files)
**does not exist** in the private repo. The Wave 1 count was erroneous. The actual
untracked count is 256 directory-collapsed entries (git status), not 5,181 individual
files.

**`research/5d-action-derivation` finding:** This branch **does not exist** in the
private repo. The closest 5D-related branches (`research/neutron-proton-mass-difference-5D`
and `research/neutron-5D-oscillator-pathB`) focus on the weak sector (neutron-proton
mass difference), not G exponents. However, the mass-difference branch contains a
**documented negative result** for the G-exponent problem: `task_b5_power_derivation.md`
explicitly concludes "DERIVATION NOT ACHIEVED" — the powers 12, 13 remain [I] (Identified),
not [D] (Derived). An untracked file `08_gravity_topological_ops.tex` presents standard
KK reduction but does not derive G₅ from first principles.

---

## 2. Governing Inputs

| Document | Location | Role |
|----------|----------|------|
| `PRIVATE_REPO_WAVE1_EXECUTION_REPORT.md` | `edc_book_4/audit/` | 12-section execution report from Wave 1 |
| `PRIVATE_REPO_WAVE1_STATUS.md` | `edc_book_4/audit/` | 6-section status summary from Wave 1 |

**Wave 1 established:** All 26 branches tracked and synced, 1 stash deferred, complex
working tree (49 deletions + 15 modifications + untracked files).

---

## 3. Reconfirmed Baseline

| Dimension | Wave 1 Report | Phase B Reconfirmed | Correction |
|-----------|---------------|---------------------|------------|
| Tracked modified | 15 | **15** | No change |
| Tracked deleted | 49 | **49** | No change |
| Untracked (git status entries) | "5,181" | **256** (directory-collapsed) | **MAJOR CORRECTION:** Wave 1 counted recursively; `.cache/` does not exist |
| Cache/build-like untracked | "4,152 .cache/" | **0** (`.cache/` does not exist) | **MAJOR CORRECTION** |
| Non-cache untracked | "1,029" | **256 entries** (directories collapsed) | Corrected — actual count is lower |
| Stash count | 1 | **1** | No change |
| Current branch | `restructure/paper3-companion-doi-split` | Confirmed | — |

**Untracked entries by top-level directory (256 total):**

| Directory | Entries | Type |
|-----------|---------|------|
| `derivations/` | 106 | Research (analytic, mass_difference, critical, archive) |
| `releases/` | 80 | Paper releases, companions, bundles |
| `kb/` | 51 | Knowledge base (5d_universe, neutron, open_problems) |
| `P7_derivation/` | 3 | 5D geometry / harmonic / dictionary |
| `docs/` | 1 | Documentation directory |
| `archive/` | 1 | Archive directory |
| `code/` | 1 | Code directory |
| `EDC_KB/` | 1 | Knowledge base (alternate) |
| `EDC_Units/` | 1 | Units reference |
| `EDC_5D_Research/` | 1 | 5D research code |
| `.claude/` | 1 | Claude config |
| Other (files) | 8 | Misc (DELETED_FILES_INVENTORY.md, tools/, templates/, research_tasks/) |

---

## 4. Cache / Build Noise Assessment

| # | Cluster ID | Path / Pattern | Count | Type | Safe to Ignore? | Action | Notes |
|---|-----------|----------------|-------|------|-----------------|--------|-------|
| 1 | `.cache/` | `.cache/` | 0 | N/A | N/A | None needed | **Does not exist.** Wave 1 report was erroneous. |
| 2 | LaTeX .log files | `*.log` (untracked) | ~8 | Build artifact | Partially | Deferred | Some .log files document build issues; existing .gitignore does NOT cover `*.log` |
| 3 | LaTeX .bbl/.blg | `*.bbl`, `*.blg` (untracked) | ~4 | Build artifact | Yes | Deferred | Always regenerable from .bib; but mixing ignore changes with active research work risks confusion |
| 4 | LaTeX .bcf/.run.xml | `*.bcf`, `*.run.xml` | ~2 | Build artifact | Yes | Deferred | Biber intermediates; safe to ignore but not urgent |
| 5 | Compiled PDFs | Various `*.pdf` | ~15+ | Build output | No | Deferred | Some PDFs are final outputs (published papers), not all are regenerable |

**Existing `.gitignore` coverage:**
```
.venv/
.DS_Store
*.pyc
__pycache__/
texput.log
*.aux
*.out
*.toc
*.fls
*.fdb_latexmk
*.synctex.gz
```

**Not yet covered but safe to add:** `*.bbl`, `*.blg`, `*.bcf`, `*.run.xml`

**Why deferred:** The working tree is on an active restructuring branch with 49 tracked
deletions. Adding .gitignore changes now would create a commit that mixes housekeeping
with restructuring state. Safer to make .gitignore additions in a dedicated housekeeping
commit after the restructuring work is resolved.

---

## 5. `research/5d-action-derivation` Branch Inspection

### 5.1 Branch Existence

**`research/5d-action-derivation` does NOT exist in the private repo.**

The branch was listed in the CC PROMPT based on the Wave 1 report, which appears to have
mixed main-repo and private-repo branch inventories. The private repo has 26 branches,
none named `research/5d-action-derivation`.

The main repo was also checked — the branch does not exist there either.

### 5.2 Closest 5D-Related Branches

The private repo contains two 5D-related research branches:

| Branch | Files | Focus | Relevance to G Exponents |
|--------|-------|-------|--------------------------|
| `research/neutron-proton-mass-difference-5D` | 1,710 | Weak sector: Δm = 1.293 MeV from Z₆ symmetry | **Indirect** — contains G-exponent failure certificate |
| `research/neutron-5D-oscillator-pathB` | ~40 | Neutron oscillation model | Low — narrower subset |

### 5.3 Key Files on `research/neutron-proton-mass-difference-5D`

| File | Content | Relevance |
|------|---------|-----------|
| `derivations/critical/task_b5_power_derivation.md` | **Explicit investigation of G powers 12, 13, 128π²** | **HIGH** — documented negative result |
| `derivations/mass_difference/GAP1_COMPLETE_DERIVATION_SUMMARY.md` | Z₆ symmetry → δθ = 60° → Δm derivation | Low — weak sector, not gravity |
| `derivations/mass_difference/GAP5_Prefactor_5D_Topology_Origin.md` | Prefactor 1/6 from 5D topology | Low — neutron prefactor, not G |

### 5.4 `task_b5_power_derivation.md` — Critical G-Exponent Document

This file (on the committed `research/neutron-proton-mass-difference-5D` branch) is the
most direct evidence regarding the G-exponent derivation problem. Key findings:

**Title:** "Task B5: Derivation of Powers 12, 13, and 128π² from First Principles"

**Status:** "INVESTIGATION COMPLETE — DERIVATION NOT ACHIEVED"

**Key conclusions:**
1. "No known physical mechanism generates power 12 from 5D integration"
2. "Standard Kaluza-Klein predicts power -1, not +12"
3. "The powers are NOT unique — other combinations also fit G_CODATA"
4. "Epistemic status: I (Identified), NOT D (Derived)"

**Self-assessment:** "We performed **curve fitting** to match G_CODATA [...] This is
NOT a derivation. It is parameter fitting with one data point."

### 5.5 Untracked `08_gravity_topological_ops.tex`

An untracked file at `derivations/mass_difference/paper/framework/sections/08_gravity_topological_ops.tex`
(471 lines) presents:
- Standard KK reduction: G₄ = G₅/(2πR_ξ)
- Layered symmetry structure (Diff(M₄), U(1)_ξ, Z₆, su(3))
- Process operator formalism for topological transitions

This section does NOT derive G₅ from first principles. It explicitly tags the KK result
as [Dc] (derived-conditional) and notes: "Upgrade to [Der] requires: Derivation of G₅
from EDC first principles (brane tension σ, Plenum elasticity)."

### 5.6 Classification

**Classification: DOCUMENTED NEGATIVE RESULT**

The private repo does not contain an active derivation lane for the G exponents. It
contains:
- A frank failure certificate (`task_b5_power_derivation.md`) confirming the powers
  remain identified/fitted, not derived
- Standard KK framework that provides G₄ = G₅/(2πR_ξ) but does not derive G₅
- No alternative route or partial progress toward first-principles G derivation

**The G-exponent problem remains fully open.** The private repo's contribution to this
problem is a well-documented negative result, which is valuable for preventing redundant
investigation.

---

## 6. `derivations/mass_difference/` Triage

### 6.1 Cluster Description

The `derivations/mass_difference/` directory contains **21 untracked files** (plus 9
tracked modifications) spanning the neutron-proton mass difference research program.

### 6.2 Untracked File Classification

| Type | Count | Files | Assessment |
|------|-------|-------|------------|
| Research .md | 11 | AUDIT_Neutron_Proton_Derivation, COMPANION_STRUCTURE, H2_MOLECULE_5D_Investigation, HYDROGEN_5D_Investigation, HYPOTHESIS_Antimatter_5D_Conservation_Artifact, Mass_As_Inflow_Resistance_Investigation, PATCH_SUMMARY_NEUTRON_OSCILLATION_MODEL, SYNTHESIS_Mass_Inflow_Complete_Picture, + 3 others | **Valuable research content** |
| Research .tex | 3 | EDC_Neutron_Junction_Oscillation_Model, EDC_Neutron_Proton_Derivation, EDC_Proton_Junction_Model | **Valuable source** |
| LaTeX .log | 4 | Build logs for the .tex files above | **Build artifacts** (regenerable) |
| Compiled .pdf | 3 | Compiled versions of the .tex files + "5D Brane-World Framework" PDF | **Mixed** — some are canonical outputs |
| Framework section | 1 | `08_gravity_topological_ops.tex` (471 lines) | **Valuable** — gravity/topology section |

### 6.3 Assessment

**Clearly valuable research:** YES — the .md files are research notes, hypotheses,
synthesis documents, and audit notes. The .tex files are LaTeX source for derivation
papers. The `08_gravity_topological_ops.tex` is a substantive framework section.

**Commit-ready?** NO — the cluster mixes source files with build artifacts (.log, .pdf).
A clean commit would need to:
1. Separate source (.md, .tex, .bib) from artifacts (.log)
2. Decide which .pdf files are canonical outputs vs regenerable
3. Handle the file with a space in its name ("5D Brane-World Framework...")
4. Ensure the commit doesn't accidentally include the 9 tracked modifications

**Recommended action:** DEFER — preserve in next dedicated commit session after
source/artifact separation.

---

## 7. Tracked Modification Assessment

### 7.1 Cluster 1: `derivations/mass_difference/` (9 files)

| File | Type | Change Size | Assessment |
|------|------|-------------|------------|
| `EDC_5D_Complete_Mathematical_Framework.tex` | Source | Modified | Active research edits |
| `paper/EDC_Weak_Interactions_5D_Model.tex` | Source | Modified | Paper edits |
| `paper/EDC_Weak_Interactions_5D_Model.pdf` | Binary | Modified | Recompiled paper |
| `paper/framework/bib/references.bib` | Source | Modified | Bibliography updates |
| `paper/framework/main.tex` | Source | Modified (21 lines) | Framework paper edits |
| `paper/framework/main.pdf` | Binary | Modified (785K→295K) | Recompiled (significant size change) |
| `paper/framework/main.bbl` | Build artifact | Modified | Regenerable |
| `paper/framework/main.blg` | Build artifact | Modified (66 lines) | Regenerable |
| `paper/framework/main.log` | Build artifact | Modified (791 lines) | Regenerable |

**Total:** 568 insertions, 453 deletions across 9 files.

**Assessment:** Active research edits to 4 source files (framework .tex, paper .tex,
5D framework .tex, references .bib) mixed with 3 build artifacts (.bbl, .blg, .log)
and 2 compiled PDFs.

**Recommendation:** DEFER — the source edits are coherent research work, but committing
them requires separating source from artifacts. The significant PDF size reduction
(785K→295K) suggests structural changes worth reviewing.

### 7.2 Cluster 2: `releases/paper_3_private/` (6 files)

| File | Type | Change Size | Assessment |
|------|------|-------------|------------|
| `paper_journal/main_journal.tex` | Source | Modified (118 lines) | Journal paper edits |
| `paper_journal/body_journal/main_body_journal.tex` | Source | Modified (18 lines) | Body text edits |
| `paper_journal/main_journal.pdf` | Binary | Modified (176K→235K) | Recompiled |
| `paper_journal/main_journal.log` | Build artifact | Modified (318 lines) | Regenerable |
| `paper/main_pathB.pdf` | Binary | Modified | Recompiled |
| `paper/main_pathB.log` | Build artifact | Modified | Regenerable |

**Total:** 457 insertions, 9,511 deletions across 6 files (note: deletion count dominated
by the full diff including binary changes).

**Assessment:** Active journal paper editing — 2 source files modified with substantive
edits. The 9,511-deletion count is misleading (binary diff artifacts).

**Recommendation:** DEFER — coherent journal editing work but mixed with build artifacts.
Would benefit from a dedicated commit that separates `.tex` source from `.log` and `.pdf`.

### 7.3 Overall Tracked Modification Verdict

| Cluster | Source Files | Build Artifacts | Commit Now? | Recommendation |
|---------|-------------|-----------------|-------------|----------------|
| derivations/mass_difference | 4 (.tex, .bib) | 5 (.bbl, .blg, .log, 2x .pdf) | NO | Defer |
| releases/paper_3_private | 2 (.tex) | 4 (.log, 2x .pdf, .log) | NO | Defer |
| **Total** | **6** | **9** | **NO** | **Defer all** |

**Why not commit:** Both clusters mix source edits with build artifacts. A clean
preservation commit should separate these. Additionally, the working tree has 49 tracked
deletions from the same restructuring branch — a partial commit of modifications without
the deletions would create an inconsistent state.

---

## 8. Preservation / Ignore Actions Taken

**No commits were made.**
**No .gitignore changes were made.**
**No files were deleted, moved, merged, or modified.**

All actions in this Phase B pass were **read-only inspection**. The working tree was
assessed but not modified.

**Rationale:** Every candidate action (cache ignore, research commit, modification
commit) had at least one disqualifying factor:
1. Cache ignore: `.cache/` doesn't exist; remaining build artifacts are mixed with source
2. Research commit: source/artifact separation needed first
3. Modification commit: source/artifact separation needed; inconsistent with 49 tracked deletions

---

## 9. Remaining Ambiguous Areas

| # | Area | Nature of Ambiguity | Priority |
|---|------|---------------------|----------|
| 1 | `derivations/analytic/` (73+ untracked files) | Contains 11 failure certificates, 11 derivation ledger versions, multiple .tex derivations — unclear which are current vs superseded | MEDIUM |
| 2 | `releases/paper_3_private/` (80+ untracked entries) | Large cluster of reports, companions, submission bundles — unclear what is canonical vs draft | MEDIUM |
| 3 | `kb/` (51 entries) | Knowledge base with diagrams, open problems, glossary — unclear commit policy | LOW |
| 4 | PDFs as tracked/untracked | Multiple PDFs appear in both tracked modifications and untracked — need policy decision on whether compiled PDFs belong in git | LOW |
| 5 | `archive/` (untracked directory) | Contents unknown — may contain archived research worth preserving | LOW |
| 6 | 49 tracked deletions | Intentional restructuring, but not yet committed — creates inconsistent tree state | MEDIUM |
| 7 | Wave 1 data correction | The "5,181 files / 4,152 cache" numbers from Wave 1 were wrong — actual counts are much lower (256 entries, 0 cache) | Documentation fix needed |

---

## 10. Recommended Next Step

**Recommended exactly one next step:**

**Execute a source-only preservation commit for `derivations/mass_difference/`.**

This means:
1. In the private repo, on the current branch (`restructure/paper3-companion-doi-split`)
2. Stage ONLY the `.md` and `.tex` source files from the untracked `derivations/mass_difference/` cluster (exclude `.log`, `.pdf`, build artifacts)
3. Include the `08_gravity_topological_ops.tex` section file
4. Commit with a descriptive message identifying this as research preservation
5. Push to origin

This is the narrowest, safest, highest-value action available:
- 15 research files (.md + .tex) that are clearly valuable
- No ambiguity about their nature (all are research source)
- No risk of including build artifacts
- Small, coherent commit

The 9 tracked modifications and 49 tracked deletions should remain deferred until the
restructuring work on `restructure/paper3-companion-doi-split` is intentionally resolved.

---

## 11. Bottom Line

Phase B triage corrected the Wave 1 baseline (no `.cache/` exists, actual untracked
count is 256 entries not 5,181), confirmed that `research/5d-action-derivation` does not
exist in the private repo, and identified a documented negative result for the G-exponent
problem (`task_b5_power_derivation.md` — "DERIVATION NOT ACHIEVED"). The working tree
remains too mixed (source + build artifacts) for safe broad action. The 15 tracked
modifications are coherent research edits but should be deferred until source/artifact
separation is performed. No commits, no ignores, no deletions were made — this was a
read-only triage pass. The private repo is better understood but not yet cleaned.
