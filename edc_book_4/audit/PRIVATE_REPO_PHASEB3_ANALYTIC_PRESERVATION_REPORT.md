# Private Repo Phase B.3 Analytic Preservation Report

**Date:** 2026-03-14
**Branch (private repo):** `restructure/paper3-companion-doi-split`
**Branch (main repo):** `research/topological-pinning-v7_8-integration`
**Scope:** Narrow source-only preservation of `derivations/analytic/`
**Status:** Complete

---

## 1. Executive Verdict

The analytic preservation commit was **completed successfully**. 85 source-only files
(29,509 lines) were committed and pushed to origin. This includes **11 failure
certificates** (v1–v11) preserving negative derivation history, **9 derivation ledgers**
(v3–v11) tracking derivation state evolution, and **17 archived earlier-version files**.

41 build artifacts (14 PDFs, 27 build files) were excluded. No ambiguity remains in
the committed set — all 85 files are clearly source-only textual research documents.

---

## 2. Governing Inputs

| Document | Location | Role |
|----------|----------|------|
| `PRIVATE_REPO_WAVE1_EXECUTION_REPORT.md` | `edc_book_4/audit/` | Wave 1 baseline |
| `PRIVATE_REPO_PHASEB_TRIAGE_REPORT.md` | `edc_book_4/audit/` | Phase B triage (identified cluster) |
| `PRIVATE_REPO_PHASEB2_PRESERVATION_REPORT.md` | `edc_book_4/audit/` | Phase B.2 precedent (mass_difference commit) |

---

## 3. Target Cluster

| Property | Value |
|----------|-------|
| **Path** | `derivations/analytic/` (including `archive/` and `derivations/` subdirectories) |
| **Why selected** | Phase B identified this as the next-largest untracked research cluster (~73 entries); Phase B.2 established the source-only preservation pattern |
| **Why high-value** | Contains 11 failure certificates documenting what did NOT work — essential forensic/epistemic records that prevent redundant investigation; 9 versioned derivation ledgers tracking the evolution of derivation attempts; 8 action-from-principle derivation pairs |
| **Total files in cluster** | 126 (85 source + 41 build artifacts) |
| **Source-only subset** | 85 files |
| **Excluded** | 41 files (14 PDFs + 27 build artifacts) |

---

## 4. Candidate File Register

### 4.1 Source Files — INCLUDED (85 files)

| Category | Count | File Pattern | Type | Included | Reason |
|----------|-------|-------------|------|----------|--------|
| Failure certificates | 11 | `FAILURE_CERTIFICATE_*.md` | Negative-result records | **YES** | High forensic value — documents what failed and why |
| Derivation ledgers | 9 | `DERIVATION_LEDGER_v*.md` | State-evolution records | **YES** | Tracks derivation progress across iterations |
| Audit notes | 6 | `AUDIT_NOTE*.md` | Quality assessments | **YES** | Documents derivation quality evaluations |
| Research iterations | 5 | `RESEARCH_ITERATION_1_*.md` | Research reports | **YES** | Iteration-level research summaries |
| Derivation .md files | 8 | `EDC_*_From_Action_v1.md` + others | Derivation documents | **YES** | Core research content |
| Other .md | 6 | `ANALYSIS_*.md`, `ASSUMPTION_*.md`, `EDC_5D_*.md` | Research notes | **YES** | Source research documents |
| Root .tex files | 12 | `EDC_*.tex`, `appendix_*.tex`, `neutron_*.tex` | LaTeX source | **YES** | Derivation paper source |
| Subdirectory .tex | 9 | `derivations/EDC_*.tex` | LaTeX source | **YES** | Action-from-principle derivations |
| Archive .md | 11 | `archive/*.md` | Earlier versions | **YES** | Historical provenance |
| Archive .tex | 6 | `archive/*.tex` | Earlier versions | **YES** | Historical provenance |
| Python script | 1 | `appendix_gl_frozen_numerics.py` | Computation code | **YES** | Supporting numerics (46 lines) |
| .gitignore | 1 | `.gitignore` | Config | **YES** | Directory-level ignore rules |

### 4.2 Build Artifacts — EXCLUDED (41 files)

| Category | Count | File Pattern | Reason |
|----------|-------|-------------|--------|
| PDFs (compiled) | 1 | `EDC_FROZEN_Criterion_From_Action_v1.pdf` | Regenerable from committed .tex |
| PDFs (versioned copies) | 11 | `Geometric_Structure_*.pdf`, `.pdf.1.pdf`–`.pdf.10.pdf` | Multiple copies of same compiled output |
| PDFs (other) | 2 | `main (2).pdf`, `paper_published_original.pdf` | Compiled / external reference PDFs |
| Build logs | 13 | `build*.log`, `EDC_FROZEN_*.log`, `main (2).log` | LaTeX build logs — regenerable |
| LaTeX aux files | 5 | `*.aux`, `*.out`, `*.fls`, `*.fdb_latexmk` | LaTeX intermediates — regenerable |
| LaTeX toc | 1 | `main (2).toc` | Table of contents — regenerable |
| .DS_Store | 1 | `.DS_Store` | macOS metadata — never committed |
| **Other build** | 7 | `build_table*.log`, `build_micro*.log`, `build_appendix*.log` | Build process logs |

---

## 5. Preservation Commit Performed

| Property | Value |
|----------|-------|
| **Repository** | `EDC_Research_PRIVATE` |
| **Branch** | `restructure/paper3-companion-doi-split` |
| **Commit hash** | `8c26d30` |
| **Commit message** | `preserve: untracked analytic derivation sources, failure certificates, and research ledgers` |
| **Files committed** | 85 |
| **Total lines** | 29,509 insertions |
| **Push status** | SUCCESS (`203771e..8c26d30`) |
| **Push target** | `origin/restructure/paper3-companion-doi-split` |

---

## 6. Failure Certificate Preservation

**11 failure certificates found and preserved:**

| # | File | Content (from first line) |
|---|------|--------------------------|
| 1 | `FAILURE_CERTIFICATE_Analytic_v1.md` | Failure certificate for EDC 5D Analytic Derivation v1 |
| 2 | `FAILURE_CERTIFICATE_v2.md` | Failure certificate v2 |
| 3 | `FAILURE_CERTIFICATE_v3.md` | Failure certificate v3 |
| 4 | `FAILURE_CERTIFICATE_v4.md` | Failure certificate v4 |
| 5 | `FAILURE_CERTIFICATE_v5.md` | Failure certificate v5 |
| 6 | `FAILURE_CERTIFICATE_v6.md` | Failure certificate v6 |
| 7 | `FAILURE_CERTIFICATE_v7.md` | Failure certificate v7 |
| 8 | `FAILURE_CERTIFICATE_v8.md` | Failure certificate v8 |
| 9 | `FAILURE_CERTIFICATE_v9.md` | Failure certificate v9 |
| 10 | `FAILURE_CERTIFICATE_v10.md` | Failure certificate v10 |
| 11 | `FAILURE_CERTIFICATE_v11.md` | P-ε Derived, ALL GAPS CLOSED (v11) |

**Additionally, 3 archived failure certificates** were preserved in the `archive/`
subdirectory (earlier versions of v1, v2, v3).

**Why they matter:** Failure certificates document derivation attempts that did NOT
succeed. They prevent redundant investigation by recording:
- What was attempted
- What specific gap or error was found
- Why the attempt failed
- What the residual open problems are

The v11 failure certificate is especially notable: its title indicates "ALL GAPS CLOSED"
for the P-ε parameter, suggesting the derivation series progressed from initial failure
(v1) through iterative refinement to eventual closure (v11). This version history is
itself a valuable research artifact.

---

## 7. Excluded Files

| # | Category | Count | Reason |
|---|----------|-------|--------|
| 1 | Compiled PDFs | 14 | Build outputs — regenerable from committed .tex source or external references |
| 2 | Build logs (.log) | 13 | LaTeX compilation logs — always regenerable |
| 3 | LaTeX intermediates (.aux, .out, .fls, .fdb_latexmk, .toc) | 6 | Build process intermediates — always regenerable |
| 4 | .DS_Store | 1 | macOS metadata — never belongs in git |
| **Total excluded** | **41** | All are build artifacts or system metadata |

No research source files were excluded. Every `.md`, `.tex`, and `.py` file in the
cluster was included.

---

## 8. Remaining Ambiguities

**None in the committed set.** All 85 committed files are clearly source-only textual
research documents.

**Minor remaining item:** The file `paper_published_original.pdf` (excluded) may be an
external reference rather than a compiled output. If it is the only copy of an external
paper, it has reference value. However, its name suggests it is a published paper that
exists elsewhere, so exclusion is safe.

---

## 9. Effect on Private Repo Safety

**Materially improved.**

| Dimension | Before | After |
|-----------|--------|-------|
| `derivations/analytic/` untracked source files | 85 untracked | 0 untracked (all committed) |
| Research content at risk of local disk loss | 29,509 lines in 85 files | 0 lines at risk |
| Failure certificates preserved | 0 (all untracked) | 11 committed + 3 archived versions |
| Derivation ledgers preserved | 0 (all untracked) | 9 committed |
| Remaining untracked in cluster | 126 files | 41 files (all build artifacts) |

Combined with Phase B.2, the two largest `derivations/` research clusters are now
fully source-preserved on origin.

---

## 10. Recommended Next Step

**Assess `derivations/critical/` for a similar narrow preservation pass.**

The Phase B triage identified `derivations/critical/` as a smaller untracked cluster
containing files like `EDC_Alpha_5D_Derivation_v1.md`, `task_b5_power_derivation.md`
(related to OPR-28), and other critical derivation documents. A similar source-only
pass would further reduce the private repo's untracked research exposure.

Alternatively, a broader assessment of the remaining ~160 untracked entries (across
`releases/`, `kb/`, and smaller clusters) could be the next target if a wider triage
is preferred.

---

## 11. Bottom Line

Phase B.3 preserved 85 source-only files (29,509 lines) from `derivations/analytic/`,
including 11 failure certificates with high forensic value and 9 derivation ledgers
tracking the full evolution of analytic derivation attempts. 41 build artifacts were
excluded. The narrow-preservation rule held — only source files were committed, no
scope expansion occurred. Combined with Phase B.2, the two largest `derivations/`
clusters are now durably preserved on origin.
