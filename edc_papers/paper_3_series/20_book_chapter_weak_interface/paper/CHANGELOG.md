# CHANGELOG — EDC Part II: Weak Sector

All notable changes to the Part II book are documented here.

---

## [2026-01-23] Half-Line BVP Numerical Pipeline Demo

**Commit:** 1c49324

### Added
- **New `code/bvp_halfline_toy_demo.py`** (~360 lines):
  - Half-line BVP solver with Pöschl-Teller toy potential
  - Robin/Neumann BC implementation at z=0
  - Robustness scan over (z_max, κ) parameter space
  - LaTeX table generator
- **New `code/output/bvp_halfline_toy_table.tex`**:
  - Auto-generated robustness table
  - N_bound = 2 stable across all tested (z_max, κ) combinations
- **New subsection** in `sections/ch14_bvp_closure_pack.tex`:
  - §14.X.Y: "Numerical Pipeline Demonstration"
  - Epistemic status box (Toy, no calibration)
  - Table~\ref{tab:bvp_toy_demo} with robustness results
  - Reproducibility instructions

### Build
- 375 pages (+2 from numerical demo)
- 0 undefined refs
- 14 bibliography entries (unchanged)

### Key Results (Toy potential V₀=10, a=1)
- $N_{\text{bound}} = 2$ (STABLE under z_max ∈ {10, 12, 14}, κ ∈ {0, 0.1, 0.5})
- $x_1 \approx 7.35$ (ground state binding energy, κ=0)
- $I_4 \approx 1.23$ (ground state concentration, κ=0)

### Guarantee
- **No calibration** to PDG, MW, GF, v=246 GeV
- Parameters chosen a priori (V0=10, a=1)
- **OPR-21 remains OPEN** (toy potential, not derived from 5D action)
- Framework 2.0 language intact

---

## [2026-01-23] OPR-02 Ngen Robustness Upgrade

**Commit:** 0071bb5

### Added
- **Expanded OPR-02 section** in `sections/ch14_bvp_closure_pack.tex`:
  - Essential spectrum threshold definition (intrinsic, no PDG input)
  - Gap criterion for finite-interval case
  - Admissible BC family definition (Robin/Dirichlet/Neumann)
  - Spectral Stability Lemma: $N_{\text{bound}}$ locally constant under BC deformation
  - OPR-02 Closure Condition box (5-point checklist)
  - Attack Surface box: "Why not 2 or 4?" + reviewer defense
- **7 new labels**: `def:bvp:threshold`, `eq:bvp:threshold_def`, `def:bvp:admissible_bc`,
  `eq:bvp:admissible_bc`, `lem:bvp:spectral_stability`, `box:opr02_closure`, `box:opr02_attack`

### Changed (pointer-only)
- Ch12 OPR Register: Updated OPR-02 "Next Action" to point to new closure criteria

### Build
- 373 pages (unchanged)
- 0 undefined refs
- 14 bibliography entries

### Guarantee
- No equations calibrated to PDG
- No claim that $N_{\text{bound}} = 3$ (explicitly marked OPEN)
- Framework 2.0 language intact

---

## [2026-01-23] OPR-21 BVP Closure Pack (57a93e8)

**Commit:** 57a93e8

### Added
- **New `sections/ch14_bvp_closure_pack.tex`** (~6 pages):
  - §14.X: "OPR-21: The BVP as Master Key"
  - Precise BVP statement (operator, domain, BCs, self-adjointness)
  - Output object definitions: $\psi_n$, $x_1$, $I_4$, $N_{\text{bound}}$, $R_{\text{LR}}$
  - Acceptance criteria + closure conditions table
  - Failure modes (F1–F6)
  - Integration pointers to Ch9, Ch12, Ch13
- **28 new labels** (namespace: `bvp:*`, `def:bvp:*`, `eq:bvp:*`, `thm:bvp:*`)

### Changed (pointer-only)
- Ch12 (OPR Register): Added reference to closure pack in P1-C section
- Ch13 ($G_F$ closure plan): Added pointer after $x_1$, $I_4$ definitions

### Build
- 373 pages (+6 from closure pack)
- 0 undefined refs
- 14 bibliography entries (unchanged)

### Guarantee
- No equations or numeric constants modified
- No calibration to PDG values (explicitly forbidden in closure pack)
- Framework 2.0 language intact
- Existing chapters unchanged except minimal cross-reference pointers

---

## [2026-01-23] References Backbone (25d4103)

**Commit:** 25d4103

### Added
- **New `bib/part2_backbone.bib`** with 25 reference entries:
  - CODATA 2022, PDG 2024 (empirical baseline)
  - Weinberg, Peskin, Schwartz, Zee (standard EW/QFT)
  - ADD, RS1/RS2, Rubakov-Shaposhnikov, Jackiw-Rebbi (brane physics)
  - Zettl, Teschl, Evans, Reed-Simon (BVP/spectral theory)
  - Nakahara (topology)
  - Tinkham, de Gennes, Manton-Sutcliffe (GL/vortices)
  - Osserman, Hwang-Richards-Winter (geometric theorems)
  - Landau-Lifshitz, Coleman (WKB/tunneling)
  - CC BY-NC-SA 4.0 legal code (license)
- **Citations at 4 key locations:**
  - Copyright page: CC BY-NC-SA 4.0
  - Preface: CODATA + PDG for \tagBL{} values
  - Ch2 §2.4: Tinkham/de Gennes for GL profile
  - Z6 ground mode lemma: Zettl/Teschl for BVP theory

### Build
- 367 pages (+2 from bibliography)
- 0 undefined refs
- 7 bibliography entries

### Guarantee
- No equations or numeric constants modified
- Framework 2.0 language intact

---

## [2026-01-23] Ch2 Baseline Boxes + Changelog

**Commit:** bd8689a

### Added
- **3D Baseline (empirical) boxes** in Ch2 (Frozen Regime Foundations):
  - §2.8: Mass ratio $m_p/m_e$ baseline (CODATA 2022)
  - §2.9: Fine-structure constant $\alpha$ baseline (CODATA 2022)
- This CHANGELOG file

### Changed
- None

### Guarantee
- No equations or numeric constants modified
- Framework 2.0 language intact

---

## [2026-01-23] Paper 2 Integration (c48120d)

**Commit:** c48120d

### Added
- **New Chapter 2: Frozen Regime Foundations** (+972 lines)
  - Ported verbatim from Paper 2 (DOI: 10.5281/zenodo.18211854)
  - 11 sections covering: EDC framework, Ice Wall analogy, Frozen vs GL comparison,
    electron/proton structure, mass ratio, fine-structure constant, numerical verification
  - Framework 2.0 "5D cause → 3D shadow" wrapper boxes in each section
  - Label namespace: `ch2:*` prefix

### Changed
- **Chapter renumbering:**
  | Old | New | Title |
  |-----|-----|-------|
  | Ch2 | Ch3 | The Z6 Program |
  | Ch3 | Ch4 | Electroweak Parameters |
  | Ch4+ | Ch5+ | (all shifted +1) |

- **Cross-reference updates:**
  - `CH3_electroweak_parameters.tex`: 4× "Chapter~2" → "Chapter~3"
  - `Z6_content.tex`: 2× self-ref → "this chapter"
  - `Z6_content_full.tex`: 1× self-ref → "this chapter"

### Build
- 365 pages (+16 from Paper 2 content)
- 0 errors
- 0 undefined refs

### Guarantee
- Z6 chapter content unchanged (only ref fixes)
- No existing equations or numeric constants modified

---

## [2026-01-23] Copyright + License + Preface (5e27e3c)

**Commit:** 5e27e3c

### Added
- Copyright page (Page 2) with CC BY-NC-SA 4.0 license
- DOI: 10.5281/zenodo.18328508 (clickable)
- Preface with Framework 2.0 reading convention
- "First edition: January 2026"

### Changed
- Title page: removed "REBUILD" language, set Version 1.0

---

## [2026-01-23] Electron Stability Bridge (b2e17aa)

**Commit:** b2e17aa

### Added
- **§1.5.4 bridge paragraph**: "Why is there no lower-energy charged state?"
- **Z6 Lemma**: Charged-sector ground mode (formal anchor)

### Guarantee
- No equations modified

---

## [2026-01-23] Framework 2.0 Language Compliance (908d3e9)

**Commit:** 908d3e9

### Added
- Framework 2.0 Language Compliance boxes in CH3, CH5–CH12
- EDC Projection Principle section in Reader Contract

### Changed
- CH3: Hexagonal angle claim corrected from [Dc] to [P] (mnemonic, not derivation)
- CH9: Clarified "zero-mode limit" context

### Guarantee
- No equation content changed
