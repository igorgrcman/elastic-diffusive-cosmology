# CONCEPT INDEX (EDC_Project)

**Purpose:** Lookup table for canonical definitions of key EDC concepts.
**Usage:** When asked "how did we define X" or "find X in the book", consult THIS FILE FIRST.
**Rule:** If concept not found here, search in relevant source root, then UPDATE this file.

---

## Core Particles

### CONCEPT-001: Proton Definition (Canonical)

| Field | Value |
|-------|-------|
| **Source** | Book 1: `elastic-diffusive-cosmology_repo/edc_book/chapters/chapter_3_confinement.tex` |
| **Location** | Section 3.1.1 `\label{subsec:quarks_strings}`, lines 24-33 |
| **Secondary** | CANON_BUNDLE Section 7.2 |
| **Epistemic tag** | [Der] |
| **Used in** | Book 1 Ch.3, Book 2 (Topological Pinning), Paper 3, Companion F |

**Definition:**
```
Topology: Y-junction (3 arms at 120deg)
- Three vortex filaments meet at a junction
- Configuration: S^3 x S^3 x S^3 -> (2pi^2)^3
- Charge: W = +1 (total winding number)
- Color: 3 arms = 3 QCD colors (8 normal modes = 8 gluons)
- Stability: Steiner theorem guarantees 120deg is UNIQUE minimum
```

**Key quote (Book 1 chapter_3_confinement.tex:31-32):**
> "Join with two other vortices in a Y-junction -> Baryon (qqq)"

**Equation labels:**
- `\label{subsec:quarks_strings}` - quarks as string endpoints
- `\label{subsec:proton_neutron}` - proton vs neutron stability

---

### CONCEPT-002: Neutron Definition (Canonical)

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 7.3 |
| **Source (model)** | `EDC_Research_PRIVATE/derivations/mass_difference/EDC_Neutron_Junction_Oscillation_Model.tex` |
| **Location** | `\label{post:neutron-excited}` (line 253) |
| **Epistemic tag** | [Dc] (object), [P/OPEN] (thick-brane pumping) |
| **Used in** | Book 2 (Neutron Lifetime), Paper 3, Companion N (planned) |

**Definition:**
```
Topology: Asymmetric Y-junction (theta = 60deg, not 120deg)
- Same three-arm junction core as proton
- Parameter: q = 1/3 (half-Steiner deviation)
- Charge: W = 0, Q = 0
- Instability: Can relax theta: 60deg -> 0deg (toward proton)
- Z_6 formula: theta = (1 - Q) x 60deg
```

**Key insight (CANON_BUNDLE Section 7.3):**
> "Neutron = excited junction state, displaced from local Steiner minimum"

**Relationship to proton:**
- SAME topological junction
- DIFFERENT angular configuration (metastable vs stable)
- Decay = relaxation toward 120deg minimum

---

### CONCEPT-003: Electron Definition (Canonical)

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 7.1 |
| **Location** | Turning points document TP-2026-01-20 |
| **Epistemic tag** | [Der] |
| **Used in** | Book 1 Ch.4, mass ratio derivations |

**Definition:**
```
Topology: B^3 (3D ball) - simple vortex
Configuration: Vol(B^3) = 4pi/3
Charge: W = -1 (winding number)
Stability: Isoperimetric theorem -> UNIQUE minimum
```

---

## Core Parameters

### CONCEPT-010: Brane Tension sigma

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 5 (Sigma Derivation) |
| **Epistemic tag** | [Dc] - Conditional on hypothesis E_sigma = m_e c^2 / alpha |
| **Used in** | Neutron lifetime, topological pinning, nuclear binding |

**Formula:**
```
sigma = m_e^3 c^4 / (alpha^3 hbar^2) = 8.82 MeV/fm^2
```

**Hypothesis [P]:**
```
E_sigma = m_e c^2 / alpha = 70.0 MeV
```

**WARNING:** sigma formula is [Dc], NOT [Der]. Depends on unproven hypothesis.

---

### CONCEPT-011: Brane Thickness delta

| Field | Value |
|-------|-------|
| **Source** | Book 2: `BOOK_SECTION_NEUTRON_LIFETIME.tex:54` |
| **Epistemic tag** | [Dc] |
| **Used in** | Neutron lifetime, junction extent |

**Formula:**
```
delta = hbar / (2 m_p c) = 0.105 fm
```

**Note:** Factor 2 is conventional (Compton regularization).

---

### CONCEPT-012: Junction Extent L_0

| Field | Value |
|-------|-------|
| **Source** | Book 2: `BOOK_SECTION_NEUTRON_LIFETIME.tex:153-154` |
| **Epistemic tag** | [P] |
| **Used in** | Neutron lifetime instanton action |

**Formula:**
```
L_0 = r_p + delta = 0.875 + 0.105 = 0.980 fm
```

**Alternative:** L_0/delta = pi^2 from standing wave argument (tension with 9.33).

---

### CONCEPT-013: Pinning Constant K

| Field | Value |
|-------|-------|
| **Source** | Book 2: `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:306-312` |
| **Epistemic tag** | [Dc/I] |
| **Used in** | Nuclear binding energies, bound neutron stability |

**Formula:**
```
K = f x sigma x A_contact = 0.32 x 8.82 x 0.33 ~ 0.93 MeV

where:
  f = sqrt(delta/L_0) ~ 0.32 [I]
  A_contact = pi x delta x L_0 ~ 0.33 fm^2 [Dc]
```

---

## Key Mechanisms

### CONCEPT-020: Projection Principle (EM -> 3D Observation)

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 3 (Epistemology) |
| **Secondary** | Book 1 chapter_2_foundations |
| **Epistemic tag** | [P] |
| **Used in** | All 5D->3D mappings, Hopf fibration |

**Definition:**
```
5D BULK (Plenum) --> BRANE (delta) --> 3D UNIVERSE (Observable)
     CAUSE                              EFFECT

5D geometry      ->  Observed particles
Bulk + brane action -> Masses, charges, lifetimes
Topological defects  -> Electron, proton, neutron
Junction dynamics    -> Weak decay
```

**Causal direction:** ONE-WAY (5D -> 3D). 3D cannot change 5D.

**Note:** This projection is reused in neutron->proton mapping:
- Neutron relaxation (5D) -> beta decay products (3D)

---

### CONCEPT-021: Frozen Boundary Criterion

| Field | Value |
|-------|-------|
| **Source** | Paper 2: `EDC_FROZEN_Criterion_From_Action_v1.tex` |
| **Location** | `elastic-diffusive-cosmology_repo/edc_papers/paper_2/paper/derivations/` |
| **Epistemic tag** | [Dc] (two independent routes) |
| **Used in** | Particle stability, frozen projection |

**Route A (Large-sigma Instanton Barrier) [Dc]:**
```
Gamma ~ Gamma_0 exp(-sigma * Delta_A / hbar)
Frozen criterion: sigma * Delta_A_min > hbar * ln(Gamma_0 * tau_obs)
```

**Route B (Topological Superselection) [Dc]:**
```
B1 [M]: Winding numbers are topological invariants
B2 [P]: No topology-changing processes during tau_obs
B3 [Dc]: Gamma = 0 (exact, not approximate)
```

---

### CONCEPT-022: Z_6 Symmetry

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 7.4 |
| **Epistemic tag** | [Dc] |
| **Used in** | Proton/neutron relationship, mass difference |

**Definition:**
```
Z_6 = Z_3 x Z_2
- Z_3: Cyclic permutation of 3 arms (theta -> theta + 120deg)
- Z_2: Oscillation phase (phi -> phi + pi)

Proton: theta = 0deg (minimum)
Neutron: theta = 60deg (metastable)
Formula: theta = (1 - Q) x 60deg
```

---

## Derived Results

### CONCEPT-030: Mass Ratio m_p/m_e

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 1 |
| **Epistemic tag** | [Der] |
| **Formula** | m_p/m_e = 6pi^5 |
| **Predicted** | 1836.12 |
| **Observed** | 1836.15 |
| **Error** | 0.002% |

---

### CONCEPT-031: Fine Structure Constant alpha

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 1 |
| **Epistemic tag** | [Der] |
| **Formula** | alpha^-1 = 6pi^5 / (4pi + 5/6) |
| **Predicted** | 136.92 |
| **Observed** | 137.04 |
| **Error** | 0.08% |

---

### CONCEPT-032: Neutron-Proton Mass Difference

| Field | Value |
|-------|-------|
| **Source** | CANON_BUNDLE Section 1 |
| **Epistemic tag** | [Der] |
| **Formula** | Delta_m_np = 8 m_e / pi |
| **Predicted** | 1.301 MeV |
| **Observed** | 1.293 MeV |
| **Error** | 0.6% |

---

### CONCEPT-033: Neutron Lifetime

| Field | Value |
|-------|-------|
| **Source** | Book 2: `BOOK_SECTION_NEUTRON_LIFETIME.tex:79-81` |
| **Epistemic tag** | [Dc/Cal] |
| **Used in** | Paper 3, Companion H |

**Formula:**
```
tau_n = A x (hbar/omega_0) x exp(S_E/hbar)

Uncalibrated (A=1): tau_n ~ 1050 s
Calibrated (A=0.84): tau_n ~ 879 s [Cal]
```

**WARNING:** Prefactor A = 0.84 is [Cal], not [Der]. Needs derivation from fluctuation determinant.

---

### CONCEPT-034: Weinberg Angle

| Field | Value |
|-------|-------|
| **Source** | Paper 3 |
| **Epistemic tag** | [Der] |
| **Formula** | sin^2(theta_W) = 1/4 |
| **Note** | Exact at tree level; radiative corrections not included |

---

### CONCEPT-035: M6/Mn Topological Model

| Field | Value |
|-------|-------|
| **Source** | Book 2: `edc_book_2/src/derivations/m_coordination_full_test.py` |
| **Epistemic tag** | [Der] |
| **Used in** | Nuclear structure, magic numbers |

**Definition:**
```
Constraint: n = 2^a × 3^b (coordination numbers)
- Factor 3: Y-junction trivalent structure
- Factors 2: Quantum doubling
Result: n = 43 is FORBIDDEN geometrically
Verification: All known magic numbers satisfy constraint
```

---

### CONCEPT-036: Frustration-Corrected Geiger-Nuttall

| Field | Value |
|-------|-------|
| **Source** | Book 2: `edc_book_2/src/derivations/frustration_geiger_nuttall.py` |
| **Epistemic tag** | [Dc] |
| **Used in** | Alpha decay half-lives |

**Formula:**
```
log_10(tau) = A(Z-2)/sqrt(Q) + B + C × frustration_factor
R^2 = 0.9941 (vs 0.6921 uncorrected, 45% improvement)
```

---

### CONCEPT-037: Three Generations N_g = 3

| Field | Value |
|-------|-------|
| **Source** | Paper 3: `CLAIM_LEDGER.md` CL-5.1 |
| **Epistemic tag** | [Der] |
| **Used in** | Generation counting, flavor physics |

**Derivation:**
```
N_g = |Z_6/Z_2| = |Z_3| = 3
Interpretation: Flavor = Z_3 cyclic label on S^1_xi positions
```

---

### CONCEPT-038: V-A Structure (Chirality)

| Field | Value |
|-------|-------|
| **Source** | Paper 3: `CLAIM_LEDGER.md` CL-9.1, CL-9.2 |
| **Epistemic tag** | [Der] |
| **Used in** | Weak interactions, parity violation |

**Derivation:**
```
V-A from Boundary: Chirality projection at epsilon-boundary produces (1-gamma_5) structure
RH Currents Forbidden: Right-handed currents suppressed by epsilon-boundary Neumann BC
Result: Parity violation EMERGES from geometry, not postulated
```

---

### CONCEPT-039: Koide Relation Q = 2/3

| Field | Value |
|-------|-------|
| **Source** | Paper 3: `LEPTON_MASS_ATTEMPT_1.md` |
| **Epistemic tag** | [I] |
| **Used in** | Lepton masses, generation hierarchy |

**Identification:**
```
Observation: Koide Q = 2/3 = |Z_2|/|Z_3|
Interpretation: Direct ratio of subgroup cardinalities in Z_6 = Z_2 × Z_3
Result: Using Koide with derived m_e, m_mu gives m_tau = 1763 MeV (exp: 1777 MeV, 0.8% error)
Status: NOT coincidence - connects to N_g = 3 via Z_3
```

---

### CONCEPT-040: Projection-Reduction Lemma

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` |
| **Location** | Lemma \ref{lem:projection-reduction}, Definition \ref{def:projection-operator} |
| **Epistemic tag** | [Der] for individual cases; [P] for universal operator unification |
| **Used in** | EM projection, V-A chirality, Nuclear tunneling, Cross-sector breadth |

**Definition:**
```
Projection Operator: φ(x) = ∫ dχ w(χ) Φ(x,χ)

Case (A): Effective Lagrangian — Z, V_eff as bulk integrals
Case (B): Chirality Selection — ε = ∫w_L w_R ≪ 1 → V-A
Case (C): Barrier/Tunneling — κ_eff = ⟨κ⟩_w → pinning
```

**One-liner:**
> "Bulk → brane observation is linear projection; all 4D observables are weighted averages of bulk structure."

**Cross-sector power:**
- EM ↔ Weak ↔ Nuclear connected via single formalism 𝒫_w

---

### CONCEPT-041: Δm_np Derivation Anchor (8/π)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex:964-1028` |
| **Location** | Theorems: `\label{thm:brane-tension}`, `\label{thm:v3-derived}`, `\label{thm:mass-diff-derived}` |
| **Epistemic tag** | [Dc] |
| **Used in** | Nuclear-leptonic bridge, cross-sector breadth |

**Derivation chain:**
```
1. σr_e² = (36/π)m_e     [Dc] — Z_6 + ring normalization
2. q_n = 1/3             [Der] — geometry of θ = 60°
3. V_3 = σr_e² × q_n²    [Dc] — elastic energy ansatz
4. Δm_np = 2|V_3|        [M]  — potential analysis
   → Δm_np = (8/π)m_e = 1.301 MeV (0.6% error)
```

**Sensitivity analysis:** `docs/DELTA_MNP_SENSITIVITY.md`
- ROBUST to: σ, δ, L_0, w(χ) — they don't enter independently
- FRAGILE to: Z_6 structure, charge-angle coupling [Dc], elastic ansatz [Dc]

**Alternative derivation:** `edc_book/chapters/chapter_9_electroweak_v17.48_patched.tex:829-876`
- Formula: (5/2 + 4α)m_e = 1.292 MeV
- Different physical model (dimensional counting)
- 0.7% tension with 8/π model

---

### CONCEPT-042: σ Dependency Audit (Master Parameter Map)

| Field | Value |
|-------|-------|
| **Source** | `docs/SIGMA_DEPENDENCY_AUDIT.md` |
| **Location** | Full audit document |
| **Epistemic tag** | [Dc] for σ definition; OPEN for 70 vs 5.856 MeV tension |
| **Used in** | Nuclear (barriers), EM (E_σ scale), Cosmology (Λ) |

**Canonical σ definition:**
```
σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm² [Dc]
From hypothesis: E_σ = σr_e² = m_ec²/α = 70 MeV [P]
```

**Key invariant:**
```
E_σ = σ·r_e² = m_ec²/α = 70 MeV
```

**Critical tension:**
```
Nuclear/EM:  σr_e² = m_ec²/α = 70 MeV
Z_6 Ring:   σr_e² = 36m_e/π = 5.856 MeV
Ratio: ~12× — OPEN PROBLEM
```

**Sector dependencies:**
- Nuclear: V_0, K, τ_n explicitly depend on σ
- EM: σ cancels via E_σ = const
- Cosmology: Λ ∝ σ explicitly

---

### CONCEPT-045: Book2 Insert: G_F Constraint Box

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/boxes/gf_constraint_box.tex` |
| **Companion** | `docs/BOOK2_INSERT_GF.md` |
| **Insertion** | `edc_book_2/src/sections/11_gf_derivation.tex` (after Stoplight Verdict) |
| **Epistemic tag** | [Dc] for constraint; falsification channel documented |
| **Used in** | Book 2 Chapter 11 (Fermi Constant from Geometry) |

**Content:**
- 3-sentence canon summary (constraint status, naive overlap, falsification)
- Falsification box with target window and fail criteria
- Cross-references to GF_CONSTRAINT_NOTE.md and Projection Lemma Case (B)

---

### CONCEPT-044: G_F Constraint (Fermi Constant)

| Field | Value |
|-------|-------|
| **Source** | `docs/GF_CONSTRAINT_NOTE.md` |
| **Location** | Full document |
| **Epistemic tag** | [Dc] for constraint; [P] for first-principles; sin²θ_W = 1/4 is [Der] |
| **Used in** | Weak interactions, electroweak unification |

**Baseline [BL]:**
```
G_F = 1.1663787 × 10⁻⁵ GeV⁻²
G_F = g²/(4√2 M_W²) (tree-level W-exchange)
v = (√2 G_F)^{-1/2} = 246.22 GeV
```

**Constraint window [Dc]:**
```
g_eff² / M_eff² ∈ [0.9, 1.1] × G_F
Dimensionless check: X = G_F m_e² = 3.04 × 10⁻¹²
```

**Projection mapping [P]:**
```
g_eff² = g₅² × ⟨K_g⟩_w   (overlap integral)
M_eff² = ⟨K_M⟩_w         (projected curvature)
Source: Projection-Reduction Lemma (edc_papers/_shared/lemmas/)
```

**True EDC prediction [Der]:**
```
sin²θ_W = |Z₂|/|Z₆| = 2/6 = 1/4 (bare)
sin²θ_W(M_Z) = 0.2314 (0.08% from PDG)
```

**Circularity caveat:**
```
G_F "exact agreement" is CONSISTENCY IDENTITY, not independent prediction.
Higgs VEV v is DEFINED from G_F: v = (√2 G_F)^{-1/2}
```

---

### CONCEPT-043: Flavor Skeleton v0.1 (Breadth Deliverable)

| Field | Value |
|-------|-------|
| **Source** | `docs/FLAVOR_SKELETON_v0.1.md` |
| **Location** | Full document |
| **Epistemic tag** | Mixed: [Der] for N_g, sin²θ_W; [Dc] for θ₂₃, CKM hierarchy; [I] for θ₁₂, θ₁₃ |
| **Used in** | Cross-sector validation, flavor physics |

**What is DERIVED [Der]:**
```
N_g = 3 from |Z₃| = 3 (Z₆ = Z₂ × Z₃ structure)
sin²θ_W = 1/4 (bare) from |Z₂|/|Z₆| = 2/6 = 1/4
```

**What is DERIVED CONDITIONAL [Dc]:**
```
θ₂₃ ≈ 45° (atmospheric) from Z₆ overlap geometry
CKM hierarchy λ, λ², λ³ from localization overlap (single parameter)
CP phase δ = 60° from Z₂ sign selection (5° from PDG 65°)
sin²θ_W(M_Z) = 0.2314 after standard RG (0.08% from PDG)
```

**NO-GO Results (Falsified approaches):**
```
1. Z₃ DFT for CKM: |V_ij|² = 1/3 → ×144 off for |V_ub|
2. Z₃ DFT for PMNS: sin²θ₁₃ = 1/3 → ×15 off
3. Pure Z₃ charges → CP: Phase Cancellation Theorem gives J = 0
4. Gaussian overlap profile: over-suppresses corners (×100)
```

**Open problems:**
- OPR-05: Derive PMNS angles θ₁₂, θ₁₃ from geometry
- OPR-09: Derive f_i(z) profiles from 5D BVP
- OPR-11: CKM (ρ̄, η̄) from 5D geometry

---

### CONCEPT-046: Breadth Synthesis 2026-01-29 (Front Door)

| Field | Value |
|-------|-------|
| **Source** | `docs/BREADTH_SYNTHESIS_2026-01-29.md` |
| **Location** | Full document |
| **Epistemic tag** | Summary document — no new claims |
| **Used in** | Session onboarding, cross-sector overview |

**Purpose:**
Front-door document for EDC cross-sector breadth work. Summarizes:
- Universal mechanism (Projection-Reduction Lemma)
- 3 GREEN anchors (N_g=3, sin²θ_W=1/4, Δm_np)
- 2 falsification channels (G_F constraint, N_cell=12)
- σ robustness map (where cancels vs fragile)
- Next 3 tests (ranked cheap→expensive)

**Cross-references:**
- Projection Lemma: `edc_papers/_shared/lemmas/projection_reduction_lemma.tex`
- Flavor Skeleton: `docs/FLAVOR_SKELETON_v0.1.md`
- G_F Constraint: `docs/GF_CONSTRAINT_NOTE.md`
- σ Audit: `docs/SIGMA_DEPENDENCY_AUDIT.md`

---

### CONCEPT-047: Pion Splitting ε-Check (Breadth Test)

| Field | Value |
|-------|-------|
| **Source** | `docs/PION_SPLITTING_EPSILON_CHECK.md` |
| **Location** | Full document |
| **Epistemic tag** | [I] — pattern identification, not derivation |
| **Used in** | Breadth validation, EM dressing pattern |

**Purpose:**
Cheap breadth test: Does pion mass splitting (r_π = 3.40%) match ε ≈ 0.679% EM dressing pattern?

**Key findings:**
```
r_π / ε ≈ 5.0 — same order of magnitude
Alternative: r_π ≈ (7/6) × 4α — near-unity factor with 4α
```

**Verdict:** YELLOW — order-of-magnitude match but factor ~5 (or 7/6) needs geometric explanation

**Cross-references:**
- ε source: `docs/DELTA_MNP_RECONCILIATION.md`
- Test motivation: `docs/BREADTH_SYNTHESIS_2026-01-29.md` (Test 1)

---

### CONCEPT-048: Z₆ Correction Factor k = 7/6 (Hypothesis + Partial Derivation)

| Field | Value |
|-------|-------|
| **Source** | `docs/Z6_CORRECTION_FACTOR_7over6.md` |
| **Location** | Full document |
| **Epistemic tag** | [Der]+[Dc] — math derived, normalization hypothesized |
| **Used in** | Discrete correction formalism, breadth links |

**Result:**
Z₆ discrete averaging introduces multiplicative correction (1 + 1/|Z₆|) = 7/6 under equal corner share normalization.

**Mathematical derivation [Der]:**
```
For f(θ) = c + a cos(6θ):
  <f>_disc = c + a (samples at corners where cos=1)
  <f>_cont = c     (cos term integrates to 0)
  R = 1 + a/c
Under a/c = 1/6: R = 7/6 ✓
```

**Physical normalization [Dc]:**
Equal corner share hypothesis (a/c = 1/N) not derived from 5D action.

**Pion match:** r_π/(4α) = 1.166 ≈ 7/6 (0.07% agreement)

---

### CONCEPT-049: Z₆ Discrete Averaging Lemma

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex` |
| **Code** | `edc_papers/_shared/code/z6_discrete_average_check.py` |
| **Epistemic tag** | [Der] — mathematical derivation |
| **Used in** | Z₆ correction factor, discrete vs continuum averaging |

**Lemma statement:**
For f(θ) = c + a cos(Nθ) with Z_N symmetry, the discrete-to-continuum ratio is:
```
R = <f>_disc / <f>_cont = 1 + a/c
```

Under equal corner share normalization (a/c = 1/N):
```
R = 1 + 1/N
```

For Z₆: R = 7/6.

**Key insight:** Discrete sampling "sees" the Z_N Fourier mode that continuum averaging washes out.

---

### CONCEPT-050: Z_N Correction Channel (Prediction Fork)

| Field | Value |
|-------|-------|
| **Source** | `docs/ZN_CORRECTION_CHANNEL.md` |
| **Lemma** | `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex` |
| **Epistemic tag** | [Der]+[Dc] — generalized from Z₆ |
| **Used in** | Cross-sector universality tests, N_cell explanation |

**General result:**
```
k(N) = 1 + 1/N   (under equal corner share normalization)
```

**Prediction fork:**

| N | k(N) | EDC Application |
|---|------|-----------------|
| 6 | 7/6 | Pion (confirmed), N_cell (candidate) |
| 4 | 5/4 | Dirac components? |
| 3 | 4/3 | Flavor counting? |

**Key implication for N_cell:**
```
N_cell_bare = 12
N_cell_eff = 12 / k(6) = 12 × (6/7) = 10.3 ≈ 10 ✓
```
Explains why τ_n uses N_cell = 10 while E_σ/σr_e² gives 12.

**Falsification:** If any sector needs N ≠ 6, Z₆ universality fails.

---

### CONCEPT-051: Z_N Channel Universality Audit

| Field | Value |
|-------|-------|
| **Source** | `docs/ZN_CHANNEL_UNIVERSALITY_AUDIT.md` |
| **Location** | Full document |
| **Epistemic tag** | [I] — audit result, not derivation |
| **Used in** | Constraining k(N) applicability |

**Purpose:**
Audits whether k(N) = 1 + 1/N applies universally across EDC sectors.

**Key finding:**
```
PARTIAL UNIVERSALITY — k applies to averaging processes, NOT to cardinality ratios

APPLY:
  - N_cell renormalization (12 → 10)
  - Pion splitting (r_π/4α ≈ 7/6)

DOES-NOT-APPLY:
  - sin²θ_W = |Z₂|/|Z₆| = 1/4 (cardinality ratio, no averaging)

UNCLEAR:
  - Δm_np ε-dressing (speculative k connection)
```

**Applicability criterion:**
- k(N) applies when: Observable = ⟨O⟩_discrete / ⟨O⟩_continuum
- k(N) does NOT apply when: Observable = |G₁| / |G₂| (cardinality ratio)

**Constraint:**
Do NOT apply k blindly to sin²θ_W, N_g, Koide Q = 2/3, or CP phases.

---

### CONCEPT-052: Toy Overlap k-Channel Test

| Field | Value |
|-------|-------|
| **Source** | `docs/TOY_OVERLAP_KCHANNEL_TEST.md` |
| **Code** | `edc_papers/_shared/code/toy_overlap_kchannel_check.py` |
| **Epistemic tag** | [Der] — mathematical demonstration |
| **Used in** | k(N) mechanism confirmation |

**Purpose:**
Explicit toy model demonstrating k(N) = 1 + 1/N arises in overlap-type observables.

**Profile:**
```
|f(θ)|⁴ = c + a·cos(Nθ)   (Z_N symmetric)
```

**Key results [Der]:**
```
I₄_cont = c                      (cos integrates to 0)
I₄_disc = c + a                  (cos(N·θₙ) = 1 at corners)
R = I₄_disc / I₄_cont = 1 + a/c

Under equal corner share (a/c = 1/N):
  R = k(N) = 1 + 1/N
  For N = 6: k(6) = 7/6 ✓
```

**Third confirmation:**
1. Pion splitting: r_π/(4α) = 1.166 [I]
2. N_cell renormalization: 12→10 [Dc]
3. Toy overlap: explicit demo [Der]

---

## Anti-Patterns (Reference)

See CANON_BUNDLE Section "Anti-Patterns: 3D Traps to Avoid" for 15 critical traps:
- KB-TRAP-001: Wrong Volume Formula (4pi/3 vs 2pi^2)
- KB-TRAP-002: Wrong Surface Area (4pi vs 2pi^2)
- KB-TRAP-010: "Obviously 4pi" without derivation
- (etc.)

**Golden Rule:** NEVER trust 3D intuition in 5D calculations.

---

## Template for New Entries

```markdown
### CONCEPT-XXX: [Name]

| Field | Value |
|-------|-------|
| **Source** | [relative path] |
| **Location** | section/subsection + equation labels |
| **Epistemic tag** | [Der]/[Dc]/[I]/[P]/[Cal]/[BL] |
| **Used in** | Book/Paper references |

**Definition/Formula:**
```
[content]
```

**Notes:** [any caveats or warnings]
```

---

*Last updated: 2026-01-29*
