# CHANGELOG — EDC Part II: Weak Sector

All notable changes to the Part II book are documented here.

---

## [2026-01-24] V(z) Toy Catalogue + V–A Suppression Inequality Chain

### Added (Task A: V(z) Candidates Catalogue in ch14)
- **New subsection** `§14.X: V(z) Candidates Catalogue (Toy Shapes, Not Derived)`
  - 5 candidate potentials: Volcano, Kink/PT, Compact well, Double-well, Exponential
  - Each with formula, spectral behavior, 5D origin, epistemic status
  - Summary table mapping shape → N_bound scaling → status
  - No-Smuggling Guardrail box with cross-references
- **9 new labels**: `subsec:bvp_vz_catalogue`, `box:bvp_vz_catalogue_status`,
  `eq:bvp:vz_volcano`, `eq:bvp:vz_kink`, `eq:bvp:vz_box`, `eq:bvp:vz_double`,
  `eq:bvp:vz_exp`, `box:bvp_vz_guardrail`, plus subsubsection labels

### Added (Task B: V–A Suppression Inequality Chain in ch9)
- **New subsection** `§9.X: Quantitative Suppression Target (Inequality Chain, No Calibration)`
  - Definition: Chirality asymmetry ratio $R_{\text{LR}}$
  - 3D empirical baseline: $R_{\text{LR}} < 10^{-3}$ (from PDG)
  - Inequality chain: $\mu > \frac{1}{2}\ln(10^3) \approx 3.45$ (barrier parameter)
  - Closure condition box: derive μ from membrane parameters (OPEN)
  - Reader Takeaway box: "Not a fit, but a closure target"
  - Cross-references to BVP closure pack
- **10 new labels**: `subsec:va_inequality_chain`, `box:va_inequality_status`,
  `def:va:RLR`, `eq:va:RLR_def`, `eq:va:RLR_exact`, `eq:va:empirical_bound`,
  `eq:va:mu_def`, `eq:va:RLR_mu`, `eq:va:mu_bound`, `box:va_mu_closure`, `box:va_takeaway`

### Build
- 385 pages (+4 from catalogue + inequality chain)
- 0 undefined refs
- 14 bibliography entries (unchanged)

### Epistemic Audit
- OPEN tags: 8 in ch14 (unchanged), 2 in ch9 (added for μ derivation)
- No calibration to PDG/MW/GF (only empirical baseline cited)
- No parameter tuning to achieve N_bound=3 or R_LR<10^{-3}
- Framework 2.0 compliance maintained

### Guarantee
- V(z) candidates are explicitly marked toy/[P]/[M]
- Inequality chain states closure TARGET, not achievement
- No claim that μ ≳ 3.5 is derived from membrane physics (OPEN)

### Parametric Hardening (follow-up patch)
- **Why:** Original μ > 3.45 looked like "hidden calibration" (implicit C=2)
- **Fix:** Replaced with μ > ln(10³)/C → μ = O(5–10) for C = O(1)
- **Moved:** 3.45 to footnote as "Illustration only (Toy)"
- **Added:** "We do not assume C; determining C is delegated to OPR-21"
- **Result:** 100% parametric, no fixed numbers, recenzent-proof

---

## [2026-01-24] V(z) Derivation Skeleton + OPR-20 Hardening

**Commit:** f3d0b1c

### Added (Task A: V(z) Skeleton in ch14)
- **New subsection** `§14.X: From 5D Action to Effective Potential: What Must Be Derived`
  - Required inputs: bulk action, brane action, GHY+Israel junction terms
  - 5-step derivation pipeline: background → perturbation → reduction → V(z) → BCs
  - V(z) structure equation: $V = V_{\text{warp}} + V_{\text{mass}} + V_{\text{coupling}}$
  - OPR-21 closure condition box with downstream unlocks
  - Connection to Part I membrane parameters table
- **3 new equations**: bulk action skeleton, brane action skeleton, V(z) structure
- **2 new boxes**: Epistemic Status (OPEN), OPR-21 Closure Condition

### Added (Task B: OPR-20 Hardening in ch11)
- **New subsubsection** `H.8: What Mathematical Result is Missing`
  - Lemma stub for $\delta = R_\xi$ from matched asymptotic analysis
  - 4-step path to [Dc] upgrade: inner expansion → outer → matching → identification
  - Explicit "Required mathematical ingredients" list
- **New subsubsection** `H.9: Fail-Safe Narrative`
  - "Even without $\delta = R_\xi$, the structure remains valid"
  - What survives vs what changes
  - Bottom line: microphysical identification, not structural postulate

### Build
- 381 pages (+4 from skeleton + hardening)
- 0 undefined refs
- 14 bibliography entries (unchanged)

### Epistemic Audit
- OPEN tags: 8 in ch14 (increased), 2 in ch11 (added)
- No forbidden fits/calibration language
- Framework 2.0 compliance maintained

### Guarantee
- No numerical claims about V(z), spectrum, or masses
- All new content explicitly tagged [OPEN] or [P]
- Fail-safe narrative isolates OPR-20 risk

---

## [2026-01-23] Half-Line BVP Numerical Pipeline Demo + Phase Diagram

**Commit:** dfd8f15

### Added
- **`code/bvp_halfline_toy_demo.py`** (~450 lines):
  - Half-line BVP solver with Pöschl-Teller toy potential
  - Robin/Neumann BC implementation at z=0
  - Robustness scan over (z_max, κ) parameter space
  - Phase diagram sweep over V0 (stepwise N_bound counting)
  - Figure generator (V(z) and ψ_0 plot)
  - LaTeX table generators (robustness + phase diagram)
- **Generated outputs**:
  - `code/output/bvp_halfline_toy_table.tex` — robustness table
  - `code/output/bvp_halfline_phase_table.tex` — phase diagram table
  - `code/output/bvp_halfline_toy_figure.pdf` — V(z) and ψ_0 visualization
- **Expanded subsection** in `sections/ch14_bvp_closure_pack.tex`:
  - §14.X.Y: "Numerical Pipeline Demonstration"
  - Epistemic status box (Toy, no calibration)
  - Robustness table (Table~\ref{tab:bvp_toy_demo})
  - Phase diagram table (Table~\ref{tab:bvp_phase_diagram})
  - Figure~\ref{fig:bvp_toy_profile}: V(z) and ψ_0 plot
  - "Why N=3 is non-trivial" box
  - Reproducibility box with run instructions
- **Symlink** `rebuild_part2_snapshot/paper/code -> ../../code`

### Build
- 377 pages (+4 from phase diagram + figure)
- 0 undefined refs
- 14 bibliography entries (unchanged)

### Key Results (Toy potential, NO calibration)
- **Robustness table**: $N_{\text{bound}} = 2$ STABLE under $(z_{\max}, \kappa)$ variations
- **Phase diagram**: $N_{\text{bound}} \in \{1, 2, 3\}$ as $V_0$ increases
  - $V_0 \lesssim 6$: $N_{\text{bound}} = 1$
  - $V_0 \in [7, 20]$: $N_{\text{bound}} = 2$
  - $V_0 \gtrsim 25$: $N_{\text{bound}} = 3$
- This demonstrates **stepwise spectral counting** — N_bound is OUTPUT of BVP

### Guarantee
- **No calibration** to PDG, MW, GF, v=246 GeV
- Parameters chosen a priori
- **OPR-21 and OPR-02 remain OPEN** (toy potential, not derived from 5D action)
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
