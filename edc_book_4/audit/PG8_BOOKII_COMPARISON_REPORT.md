# PG-8 Book II Comparison Report

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Deep comparison of standalone Book II vs repo Book II
**Status:** Comparison complete — manuscripts are structurally and topically distinct

---

## 1. Executive Verdict

**These are entirely different manuscripts.** They share only the "Book II" label.

- **Standalone Book II** covers the **gravitational sector** of EDC: emergent gravity
  from plenum dynamics, flow velocity derivation, superposition, viscosity bounds,
  Newton's constant derivation.
- **Repo Book II** covers the **weak sector** of EDC: particle ontology, frozen regime,
  Z₆ program, electroweak parameters, leptons, neutrinos, CKM matrix, Fermi constant.

There is **zero chapter overlap**. Not a single chapter title, section topic, or
physics derivation appears in both manuscripts.

The standalone has **unique recovery value** as the only known self-contained
gravitational-sector manuscript in the EDC corpus. It is not a duplicate, snapshot,
or parallel state of the repo Book II — it is a distinct work.

---

## 2. Scope and Inputs

### Sources Compared

| Label | Source Used | Path | Accessibility |
|-------|-----------|------|---------------|
| **Standalone Book II** | Original on local disk | `/Users/igor/ClaudeAI/EDC_Project/EDC_Book_2/EDC_Book_II_main.tex` | Direct file read |
| **Standalone Book II (PDF)** | Original on local disk | `/Users/igor/ClaudeAI/EDC_Project/EDC_Book_2/EDC_Book_II_Emergent_Gravity.pdf` | Present (not read — .tex is authoritative) |
| **Repo Book II (reorganized)** | In-repo, current branch | `edc_book_2/reorganized/main.tex` + included chapter files | Direct file read |
| **Repo Book II (src)** | In-repo, current branch | `edc_book_2/src/main.tex` + included section files | Partial read (driver + structure) |

### Governing Documents

| Document | Commit | Relevance |
|----------|--------|-----------|
| `PHASE_A_IMMEDIATE_RISK_CATALOG.md` | `3a56fa8` | Catalog ID for standalone Book II: NR-018, NR-019 |
| `WAVE1_EXECUTION_REPORT.md` | `dacd7c3` | Archive location: `archive/nonrepo-local-research` at `_archive_nonrepo/EDC_Book_2/` |
| `MASTER_CATALOG_AND_REORG_PLAN.md` | `ed13756` | Book II surfacing priority: `first_class` |

---

## 3. Compared Artifacts

| Artifact ID | Path | Type | Role | Notes |
|------------|------|------|------|-------|
| SA-1 | `EDC_Book_2/EDC_Book_II_main.tex` | Monolithic .tex | Standalone driver + all content | 1,637 lines, 53 KB, self-contained |
| SA-2 | `EDC_Book_2/EDC_Book_II_Emergent_Gravity.pdf` | Compiled PDF | Built output | 368 KB |
| RB-1 | `edc_book_2/reorganized/main.tex` | Modular driver | Repo driver (reorganized edition) | 234 lines, includes 17 chapter files |
| RB-2 | `edc_book_2/reorganized/part1/` | Chapter files (5) | Part I: Foundations | Weak interface through case studies |
| RB-3 | `edc_book_2/reorganized/part2/` | Chapter files (6) | Part II: Predictions | Electroweak through CKM |
| RB-4 | `edc_book_2/reorganized/part3/` | Chapter files (5) | Part III: Technical | GF chain through epistemic summary |
| RB-5 | `edc_book_2/reorganized/epilogue/` | Chapter file (1) | Epilogue | "Beyond the Weak Sector" |
| RB-6 | `edc_book_2/reorganized/appendices/` | Appendix files (3) | Support | OPR register, notation, numerical standards |
| RB-7 | `edc_book_2/src/main.tex` | Modular driver | Repo driver (original edition) | First edition, DOI: 10.5281/zenodo.18328508 |
| RB-8 | `edc_book_2/reorganized/main.pdf` | Compiled PDF | Built output | ~1.2 MB |

---

## 4. Driver-Level Comparison

| Property | Standalone | Repo (reorganized) | Repo (src) |
|----------|-----------|-------------------|------------|
| **Title** | "Elastic Diffusive Cosmology — Book II: Emergent Gravity from Plenum Dynamics" | "Elastic Diffusive Cosmology Part II: Weak Sector" | "Elastic Diffusive Cosmology — Part II: Weak Sector" |
| **Subtitle** | "Mathematical Derivations with Full Rigor" | Version 2.0 - Reorganized | First Edition |
| **Author** | Igor Grčman (with Claude/Anthropic) | Igor Grčman | Igor Grčman |
| **Date** | January 11, 2026 (Version 1.0) | \today (Version 2.0) | January 2026 |
| **DOI** | 10.5281/zenodo.XXXXXXX (placeholder) | — | 10.5281/zenodo.18328508 (real) |
| **License** | CC BY-NC-SA 4.0 | — | — |
| **Document class** | book (12pt, a4, openany) | book (11pt, a4, twoside) | book (11pt, a4) |
| **Structure** | Monolithic (all content in one file) | Modular (17 \input chapters) | Modular (~20 \input sections) |
| **Physics sector** | **Gravitational** | **Weak** | **Weak** |
| **Total lines** | 1,637 | 234 (driver only) | ~600+ (driver only) |
| **Shared macros** | None — self-contained | `includes/EDC_MACROS_COMPLETE` | `_shared/meta/edc_meta_macros` |

**Key finding:** The drivers have different titles, different physics sectors, different
document structures, and no shared include files. They are not versions of the same
manuscript.

---

## 5. Include-Tree / TOC Comparison

### 5.1 Standalone Chapter Inventory

The standalone is monolithic — no \input commands. All content is inline.

| Ch # | Title | Physics Topic |
|------|-------|---------------|
| * | Preface | Epistemic framework introduction |
| 1 | Foundations and Notation | EDC framework, symbol definitions, dimensional analysis |
| 2 | Derivation of Plenum Flow Velocity | Laplace equation, Euler equation, boundary conditions → v(r) = √(2GM/r) |
| 3 | Superposition of Gravitational Sources | Linearity proof, N-body applicability |
| 4 | Upper Bound on Plenum Viscosity | Navier-Stokes perturbation, Mercury orbit constraint |
| 5 | Connection to Quantum Mechanics | ℏ from membrane tension, α, electron mass from vortex energy |
| 6 | Newton's Gravitational Constant | G = σ r_e² / (4π ρ_∞ R_ξ³), dimensional analysis, numerical verification |
| 7 | The Two Radii of a Particle | Topological radius vs gravitational radius, hierarchy |
| 8 | Summary and Epistemic Status | Derived/Identified/Proposed classification of all results |
| A1 | Notation Reference | Symbol table |
| A2 | Dimensional Analysis Reference | [L], [M], [T] reference |

**Total:** 9 numbered chapters + preface + 2 appendix chapters = 11 logical units.
**Sections:** 49 \section commands.
**Equations:** ~22 equation/align environments.

### 5.2 Repo (Reorganized) Chapter Inventory

| Ch # | Title | Physics Topic |
|------|-------|---------------|
| * | Preface to Reorganized Edition | Reorganization notes, version history |
| * | Baseline Constants | Shared constants table |
| 0 | Bridge (chapter_0_bridge) | Connection from Part I |
| * | Epistemic Standard | Tag system definition |
| **Part I: Foundations & Mechanisms** | | |
| 1 | The Weak Interface | 5D–4D interface geometry |
| 2 | Particle Ontology in 5D | Five-category particle classification |
| 3 | The Frozen Regime | Bulk-core projection boundary |
| 4 | The Z₆ Program | Hexagonal symmetry framework |
| 5 | Case Studies: Decay Processes | Neutron, muon, tau, pion, electron, neutrino |
| **Part II: Predictions & Observables** | | |
| 6 | Electroweak Parameters from Geometry | sin²θ_W, M_W, M_Z |
| 7 | Lepton Masses and Hierarchy | Mass ratios from 5D geometry |
| 8 | Three Generations: Why Not Four? | Generation structure |
| 9 | Neutrinos as Edge Modes | Edge-mode classification |
| 10 | V–A Structure from 5D Chiral Localization | Chirality from extra dimension |
| 11 | CKM Matrix Origin | Mixing matrix from topology |
| **Part III: Technical Derivations** | | |
| 12 | The Coupling Chain: g₅ → G_F | Fermi constant derivation chain |
| 13 | Foundation Parameters | Parameter extraction |
| 14 | BVP Framework | Boundary value problem setup |
| 15 | M_W and G_F Derivation | Technical derivation details |
| 16 | Epistemic Summary | Full epistemic status assessment |
| **Epilogue** | | |
| 17 | Beyond the Weak Sector | Future directions |

**Total:** 17 numbered chapters + bridge + 2 unnumbered + 3 appendices = 22 logical units.
**Appendices:** OPR Register, Notation, Numerical Standards.

### 5.3 Structural Comparison Summary

| Dimension | Standalone | Repo (reorganized) |
|-----------|-----------|-------------------|
| Chapter count | 9 + 2 appendix | 17 + 3 appendix |
| Part structure | None | 3 parts + epilogue |
| Physics sector | Gravitational | Weak |
| Shared chapters | **0** | **0** |
| Build type | Monolithic | Modular |
| Page count (approx) | ~50–80 pages (inferred from 53KB .tex) | ~145 pages (stated in preface) |

**There is zero overlap in chapter inventory.**

---

## 6. Content-Level Difference Summary

### 6.1 Content Only in Standalone

| Topic | Location | Recovery Value |
|-------|----------|----------------|
| Complete Plenum flow velocity derivation (v = √(2GM/r)) | Ch. 2 (lines 372–725) | HIGH — step-by-step from Laplace eq through Euler eq to final result |
| Superposition theorem (linearity proof) | Ch. 3 (lines 726–896) | HIGH — formal proof of N-body gravitational superposition in EDC |
| Viscosity upper bound from Mercury orbit | Ch. 4 (lines 897–1093) | HIGH — Navier-Stokes perturbative analysis with observational constraint |
| ℏ from membrane tension derivation | Ch. 5, §5.1 (lines 1098–1139) | HIGH — connects quantum mechanics to elastic membrane |
| α from geometry | Ch. 5, §5.2 (lines 1140–1175) | MEDIUM — fine structure constant identification |
| Electron mass from vortex energy | Ch. 5, §5.3 (lines 1176–1279) | HIGH — m_e = σr_e²/c² derivation |
| G = σr_e²/(4πρ_∞R_ξ³) derivation | Ch. 6 (lines 1280–1395) | HIGH — Newton's constant from EDC parameters |
| Topological vs gravitational radius analysis | Ch. 7 (lines 1396–1478) | MEDIUM — hierarchy between scales |
| Complete epistemic ledger (D/I/P classification) | Ch. 8 (lines 1479–1558) | MEDIUM — systematic status of all gravitational results |

### 6.2 Content Only in Repo

| Topic | Location | Notes |
|-------|----------|-------|
| Weak interface geometry | Ch. 1 | 5D–4D interface framework |
| Five-category particle ontology | Ch. 2 | Core classification system for all particles |
| Frozen regime foundations | Ch. 3 | Bulk-core projection boundary physics |
| Z₆ hexagonal symmetry program | Ch. 4 | Symmetry framework for particle structure |
| Per-particle case studies (6 particles) | Ch. 5 | Neutron, muon, tau, pion, electron, neutrino |
| Electroweak parameter derivation | Ch. 6 | sin²θ_W, M_W, M_Z from geometry |
| Lepton mass hierarchy | Ch. 7 | Mass ratios from 5D |
| Three-generation structure | Ch. 8 | Why not four generations |
| Neutrino edge modes | Ch. 9 | Neutrino classification |
| V–A chiral structure | Ch. 10 | Chirality from 5D |
| CKM matrix origin | Ch. 11 | Flavor mixing from topology |
| G_F derivation chain | Ch. 12–15 | Complete Fermi constant derivation |
| OPR register | Appendix | Open problem registry |

### 6.3 Clearly Shared Content

**None at the chapter or section level.** The two manuscripts cover entirely different
physics sectors with different fundamental questions, different derivation targets,
and different mathematical methods.

The only shared elements are:
- Author (Igor Grčman)
- Framework name (Elastic Diffusive Cosmology)
- Some common parameters (σ, R_ξ, r_e)
- Epistemic tagging convention (D/I/P)

---

## 7. Manuscript Identity Assessment

**Are these the same manuscript state?**
NO. They are different manuscripts entirely.

**Is one a later revision of the other?**
NO. They address different physics sectors and have no shared chapter content.

**Is one a parallel path?**
NO — "parallel path" implies they started from the same root. These manuscripts have
different roots, different topics, and different purposes.

**What is their actual relationship?**
They are two volumes of a multi-volume EDC series that were both given the "Book II"
label at different times:

- The **standalone** was written as "Book II: Emergent Gravity from Plenum Dynamics"
  (Version 1.0, January 11, 2026). It covers the gravitational sector — what one
  might expect to be Book I content in a physics series that typically starts with
  gravity before moving to particle physics.

- The **repo version** was written as "Part II: Weak Sector" and has been developed
  extensively with a real Zenodo DOI (10.5281/zenodo.18328508), modular architecture,
  17 chapters, OPR register, and full audit infrastructure. This is the operational
  "Book II" in the current research workflow.

The "Book II" naming collision appears to be a numbering artifact: the standalone
gravitational manuscript was likely numbered as "Book II" in a different numbering
scheme (perhaps chronological by writing order), while the repo "Part II" was
numbered relative to the EDC series structure.

---

## 8. Unique Recovery Value

**Does the standalone contain unique material worth preserving as distinct?**

**YES — categorically.** The standalone contains 9 chapters of gravitational-sector
derivations that do not appear anywhere in the repo Book II (weak sector). Specifically:

| Derivation | Unique? | Recovery Value |
|-----------|---------|----------------|
| Plenum flow velocity (full step-by-step) | YES — not in any repo Book II chapter | HIGH |
| Gravitational superposition proof | YES — not in repo Book II | HIGH |
| Viscosity bound from Mercury orbit | YES — not in repo Book II | HIGH |
| ℏ from membrane tension | YES — not in repo Book II | HIGH |
| G from EDC parameters | YES — not in repo Book II | HIGH |
| Two radii analysis | YES — not in repo Book II | MEDIUM |

**Note:** Some of this gravitational-sector content may exist in other forms elsewhere
in the repo (e.g., in Paper 1, Paper 2, or derivation folders). The standalone
represents the only known **book-length, self-contained, pedagogically structured**
presentation of the gravitational sector. Its recovery value is as a coherent
manuscript, not just as a collection of individual derivations.

---

## 9. Same-Name / Provenance Risk Note

**The "Book II" naming collision is the primary provenance risk.**

Both manuscripts use "Book II" in their titles, but they are different works:

| Label | Standalone | Repo |
|-------|-----------|------|
| Title contains "Book II" | YES — "BOOK II" | NO — "Part II" |
| File name contains "Book_II" | YES — `EDC_Book_II_main.tex` | NO |
| Directory named "Book_2" | YES — `EDC_Book_2/` | YES — `edc_book_2/` |

This naming collision creates a risk that future users might assume they are
versions of the same manuscript. **They are not.**

**Recommended resolution:** In Phase B catalog expansion, assign distinct manuscript
IDs to each:
- Standalone: `M-standalone-gravity-001` (gravitational sector manuscript)
- Repo: `M-edc-main-002` (weak-sector manuscript, existing catalog ID)

Document the naming collision in both catalog entries.

---

## 10. Recommended Book II Handling

**Primary classification: HISTORICALLY DISTINCT PRESERVED COPY**

The standalone is not a duplicate, not a parallel state, and not a recovery source
for the repo Book II. It is a **distinct manuscript** covering different physics that
was coincidentally given the same "Book II" label.

**Justification:**
1. Zero chapter overlap — different topics, different derivations, different physics
2. Different titles — "Emergent Gravity" vs "Weak Sector"
3. Different maturity — standalone is Version 1.0 monolithic; repo is Version 2.0 modular with DOI
4. Different build architecture — self-contained vs shared-macro modular
5. Unique content — standalone gravity derivations are not duplicated in repo Book II

**Recommended actions:**
1. **Preserve the standalone as-is** in `archive/nonrepo-local-research` (already done in Wave 1)
2. **Do NOT merge** into repo Book II — they are different books
3. **Rename in catalog** to reflect true content: "EDC Gravitational Sector Manuscript (standalone)"
4. **Consider future surfacing** as a candidate for "Book I" or "Gravity Companion"
   in any multi-volume EDC series reorganization
5. **Document the naming collision** in both catalog entries to prevent future confusion

---

## 11. Bottom Line

PG-8 required comparing standalone and repo Book II to determine their relationship.
The comparison reveals they are **entirely different manuscripts** covering different
EDC physics sectors (gravitational vs weak). The "Book II" naming collision is a
labeling artifact, not a content overlap.

The standalone has high unique recovery value as the only known book-length
gravitational-sector manuscript. It should be preserved as a distinct work, not
treated as a duplicate or merged into the weak-sector Book II. No merge, overwrite,
or relocation is warranted or recommended.
