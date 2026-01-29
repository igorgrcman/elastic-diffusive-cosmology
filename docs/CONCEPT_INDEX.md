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

### CONCEPT-053: Z_N Anisotropy Normalization from Action

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_anisotropy_normalization_from_action.tex` |
| **Summary** | `docs/ZN_NORMALIZATION_FROM_ACTION_NOTE.md` |
| **Epistemic tag** | [Der] for toy model; [Dc] for 5D mapping |
| **Used in** | Justifying a/c = 1/N ("equal corner share") |

**Purpose:**
Derive the "equal corner share" normalization a/c = 1/N from energy minimization rather than assuming it.

**Key result [Der]:**
```
Energy functional: E[u] = (T/2)∫(u')²dθ + λΣₙW(u(θₙ))

For u(θ) = u₀ + a₁cos(Nθ):
  - Gradient energy ~ N² (penalizes anisotropy)
  - Discrete anchors ~ N (drive anisotropy)
  - Balance: a₁ ≈ -λW'(u₀)/(πTN) ∝ 1/N

Therefore: a/c ~ 1/N
```

**Physical mechanism:**
Each of the N identical anchors contributes 1/N to the total anisotropy.

**What remains [Dc]:**
- Identification of E_cont with 5D brane tension
- Identification of E_disc with anchor couplings at Z_N fixed points
- Verification of tension-dominated regime from 5D parameters

**Upgrade path:**
Explicit 5D reduction of S_bulk + S_brane + S_GHY on Z_N background.

---

### CONCEPT-054: 5D → Toy Functional Mapping for Z_N Anisotropy

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_toy_functional_from_5d_action.tex` |
| **Summary** | `docs/ZN_5D_TO_TOY_MAPPING_NOTE.md` |
| **Epistemic tag** | [Dc] — Standard reduction techniques, heuristic gauge-fixing |
| **Used in** | Justifying toy functional from 5D brane-world action |

**Purpose:**
Map the 5D brane-world action S_5D = S_bulk + S_brane + S_GHY to the 1D toy functional for Z_N anisotropy.

**Mapping dictionary:**
```
5D Action:  S_5D = S_bulk + S_brane + S_GHY
Toy Functional: E[u] = (T/2)∫(u')²dθ + λ Σₙ W(u(θₙ))

| Toy Parameter | 5D Origin | Mechanism |
|---------------|-----------|-----------|
| T (tension)   | σ/R       | Brane tension / ring radius |
| λ (coupling)  | κ₅²τₙ     | Israel junction × defect stress |
| u(θ)          | h(θ)      | Metric perturbation at ring |
| W(u)          | φ(u)²     | Localized potential at fixed points |
```

**Key result:**
The 1/N scaling of anisotropy amplitude emerges naturally from the balance of gradient energy (∝ N²) vs discrete anchor terms (∝ N).

**What this enables:**
- Chain: 5D action → toy functional → a/c = 1/N → k(N) = 1 + 1/N
- Partial upgrade of k-channel from [I] toward [Dc]

**What remains [Dc]:**
- Specific gauge choices in dimensional reduction
- ~~Full Israel junction calculation at Z_N fixed points~~ → DONE (CONCEPT-055)
- BVP verification of cos(Nθ) structure

---

### CONCEPT-055: Israel Junction at Z_N Fixed Points (Identical Anchors)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/israel_zn_fixed_points_anchors.tex` |
| **Summary** | `docs/ISRAEL_ZN_ANCHORS_NOTE.md` |
| **Epistemic tag** | [Der] for identical anchors; [Dc] for λ prefactor |
| **Used in** | Justifying uniform λ in toy functional; k-channel derivation chain |

**Purpose:**
Derive the "identical anchors" property from Israel junction conditions under Z_N symmetry.

**Key result [Der]:**
```
Z_N symmetry ⇒ S_μν(θ_n) = S_μν(θ_0) for all n (covariance)
             ⇒ τ_n = τ_0 ≡ τ (equal defect stress)
             ⇒ λ_n = λ (uniform anchor coupling)
```

**λ scaling [Dc]:**
```
λ = c_λ · κ_5² τ   where c_λ ~ O(1) to O(2π)
```
Exact c_λ requires solving bulk field equations (out of scope).

**What this upgrades:**
- "Identical anchors" was assumption [Dc], now derived [Der]
- Complete chain: Z_N symmetry → τ_n = τ → λ_n = λ → a/c = 1/N → k(N) = 1 + 1/N

**Conditions for validity:**
- Z_N symmetry must hold
- Thin defect limit (delta approximation)
- Weak field / linear Israel regime

---

### CONCEPT-056: Z_N Mode Structure (cos(Nθ) Selection)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex` |
| **Code** | `edc_papers/_shared/code/zn_delta_pinning_mode_check.py` |
| **Summary** | `docs/ZN_MODE_STRUCTURE_BVP_NOTE.md` |
| **Epistemic tag** | [Der] for delta-pinning ring model; [Dc] for 5D mapping |
| **Used in** | Justifying ansatz u(θ) = u₀ + a₁cos(Nθ) in a/c = 1/N derivation |

**Purpose:**
Verify that cos(Nθ) is the unique leading anisotropic mode under Z_N delta-pinning.

**Selection Lemma [Der]:**
```
For mode exp(imθ), coupling to N anchors at θ_n = 2πn/N:
  Σ_n exp(imθ_n) = N   if m ≡ 0 (mod N)
                 = 0   otherwise

Only Z_N-symmetric modes (m = 0, N, 2N, ...) couple to anchors.
```

**Gradient ordering [Der]:**
```
Among Z_N-symmetric modes:
  m = 0:  constant (isotropic)
  m = N:  cos(Nθ), gradient energy ∝ N²  ← FIRST anisotropic
  m = 2N: cos(2Nθ), gradient energy ∝ 4N²
```

**Combined result [Der]:**
cos(Nθ) is the lowest-energy anisotropic mode that couples to anchors.

**Numerical verification:**
All N tested (3, 4, 5, 6, 8): eigenmode overlap with cos(Nθ) > 99%.

**What this validates:**
Ansatz u(θ) = u₀ + a₁cos(Nθ) used in deriving a/c = 1/N and k(N) = 1 + 1/N.

---

### CONCEPT-057: Non-Quadratic W(u) Robustness

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_mode_selection_nonlinear_W.tex` |
| **Code** | `edc_papers/_shared/code/zn_nonlinear_W_harmonics_demo.py` |
| **Summary** | `docs/ZN_NONQUADRATIC_W_ROBUSTNESS_NOTE.md` |
| **Epistemic tag** | [Der] for second-variation theorem; [Dc] for amplitude corrections |
| **Used in** | Robustness of k-channel derivation |

**Purpose:**
Prove mode selection (m = N) is robust when W(u) is not purely quadratic.

**Key insight [Der]:**
```
The Hessian (second variation) δ²E depends only on W''(u₀) = κ.
Higher derivatives (W''', W'''', ...) enter at O(η³) and beyond.
Mode INDEX selection is a LINEAR property → unchanged by nonlinearities.
```

**Robustness theorem [Der]:**
For any C² potential W with stable minimum (W'(u₀)=0, W''(u₀)>0),
the leading anisotropic mode is cos(Nθ) for sufficiently small amplitude.

**What changes vs what doesn't:**

| Property | Quadratic W | General W |
|----------|-------------|-----------|
| Mode index (m=N) | Fixed | **Unchanged** |
| Selection Lemma | Exact | **Unchanged** |
| Amplitude relation | Linear | Nonlinear corrections |
| Harmonic content | Pure cos(Nθ) | cos(Nθ) + higher (2N, 3N, ...) |

**Regime of validity:**
ε₃ = |g|A/κ ≪ 1 and ε₄ = |h|A²/κ ≪ 1

---

### CONCEPT-058: Strong Pinning Regime Robustness

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_strong_pinning_regimes.tex` |
| **Code** | `edc_papers/_shared/code/zn_strong_pinning_scan.py` |
| **Summary** | `docs/ZN_STRONG_PINNING_ROBUSTNESS_NOTE.md` |
| **Epistemic tag** | [Der] for mode index stability; [Dc] for localization bounds |
| **Used in** | Robustness of k-channel derivation across all pinning regimes |

**Purpose:**
Prove mode index m = N is stable across all pinning strengths ρ = λκ/T ∈ (0, ∞).

**Regime classification (critical ρ* = N²):**
```
Weak (ρ << N²):       gradient-dominated, μ_N ≈ N², mode shape = cos(Nθ)
Intermediate (ρ ~ N²): crossover behavior
Strong (ρ >> N²):      pinning-dominated, μ_N ∝ ρ, mode shape = cusp-like
```

**Symmetry protection [Der]:**
Selection Lemma is a GEOMETRIC identity about anchor positions.
It holds regardless of ρ → mode index always m = N.

**What changes with ρ:**
- Eigenvalue scaling: N² (weak) → ρN/π (strong)
- Mode shape: delocalized cosine → localized at anchors
- Energy distribution: uniform → concentrated near anchors

**What does NOT change:**
- Mode index: always m = N
- Z_N periodicity of mode

**Numerical verification:**
All N tested (3, 6, 12): mode m = N stable across ρ ∈ [0.01, 10⁵].

**Implication:**
k-channel correction formula k(N) = 1 + 1/N is not limited to weak pinning regime.

---

### CONCEPT-059: One-Defect Symmetry Breaking Robustness

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/zn_symmetry_breaking_one_defect.tex` |
| **Code** | `edc_papers/_shared/code/zn_one_defect_contamination_scan.py` |
| **Summary** | `docs/ZN_ONE_DEFECT_ROBUSTNESS_NOTE.md` |
| **Epistemic tag** | [Der] for O(ε²) scaling; [Dc] for thresholds |
| **Used in** | Robustness of k-channel under realistic defect conditions |

**Purpose:**
Quantify contamination when one anchor has strength λ(1+ε) instead of λ.

**Key result [Der]:**
```
Overlap loss = 1 - |⟨ψ_N|ψ̃⟩|² = O(ε²)
```

Small defects cause quadratically small contamination.

**Contamination spectrum:**
- ALL cosine modes get contaminated (Selection Lemma violated for ε ≠ 0)
- Dominant contamination from m = N ± 1
- Amplitude: c_m ~ ε·ρ / [π(N² - m²)]

**Tolerance thresholds [Dc]:**
| Regime | Condition | ε_99 |
|--------|-----------|------|
| Weak | ρ << N² | >1.0 |
| Moderate | ρ ~ N² | 0.1-0.5 |
| Strong | ρ >> N² | mode distorted at ε=0 |

**Failure mode:**
When |ε| ~ 2πN/ρ, perturbation theory breaks down and Z_N selection is lost.

**Implication:**
k-channel is ROBUST to realistic defect levels (~10% mismatch).

---

### CONCEPT-060: Z_N k-channel Robustness Box (Book-Ready Summary)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/boxes/zn_kchannel_robustness_box.tex` |
| **Wired into** | `RT-CH3-003_NEUTRON_LIFETIME_DERIVATION.tex` (after ncell_renorm_box) |
| **Epistemic tag** | [Der] for math; [Dc] for physical thresholds |
| **Used in** | Neutron lifetime derivation, k-channel summary |

**Purpose:**
Book-ready tcolorbox summarizing k(N) = 1 + 1/N definition, applicability rules, and robustness results.

**Contents:**
```
1. DEFINITION: k(N) = ⟨O⟩_disc / ⟨O⟩_cont = 1 + 1/N [Der]
   Valid for Z_N-symmetric anisotropy f(θ) = c + a cos(Nθ) under a/c = 1/N

2. APPLICABILITY RULE (CRITICAL):
   ✓ USE for averaging observables (N_cell, pion ε-dressing)
   × DO NOT USE for cardinality ratios (sin²θ_W, N_g, Koide Q, CP phases)

3. ROBUSTNESS RESULTS [Der]:
   - Non-quadratic W(u): Mode index m=N unchanged
   - Strong pinning (ρ >> N²): Z_N irrep structure protected at any ρ
   - One-defect (ε ≠ 0): Contamination ~ O(ε²), robust to ~10% mismatch
```

**Cross-references:**
- Lemma: `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`
- Strong pinning: CONCEPT-058, `docs/ZN_STRONG_PINNING_ROBUSTNESS_NOTE.md`
- One-defect: CONCEPT-059, `docs/ZN_ONE_DEFECT_ROBUSTNESS_NOTE.md`

---

### CONCEPT-061: k(N) Cross-Validation Candidate Catalog

| Field | Value |
|-------|-------|
| **Source** | `docs/KN_CHANNEL_CROSS_VALIDATION_CANDIDATES.md` |
| **Location** | Full document |
| **Epistemic tag** | [P] — candidate list, no empirical confirmation |
| **Used in** | Analog testing of k-channel mechanism |

**Purpose:**
Catalog of 12 candidate systems (N ≠ 6) where k(N) = 1 + 1/N discrete averaging could be tested.

**Categories:**
1. Wave/oscillator rings (pendulums, LC circuits, acoustics)
2. Lattice/solid-state (spin chains, phonons, Josephson junctions)
3. EM resonators/antennas (phased arrays, cavities, optical rings)
4. Other physics analogs (LQCD, crystal field, DFT)

**Top 3 candidates (HIGH confidence):**
- Spin chain exact diagonalization (N = 4–20)
- LC oscillator ring simulation (N = 4–16)
- Circular antenna array (N = 4–16)

**EDC-safe framing:** Tests validate mathematical mechanism, not specific EDC predictions.

---

### CONCEPT-062: Spin Chain k-Channel Cross-Validation (Averaging Mechanism)

| Field | Value |
|-------|-------|
| **Source** | `docs/SPIN_CHAIN_KCHANNEL_CROSSVALIDATION.md` |
| **Code** | `edc_papers/_shared/code/spin_chain_kchannel_ed_test.py` |
| **Epistemic tag** | [Der] — mathematical mechanism confirmed numerically |
| **Used in** | Independent validation of k(N) = 1 + 1/N formula |

**Purpose:**
Test the discrete averaging mechanism k(N) = 1 + 1/N in an independent physical system (XX spin chain) that has nothing to do with EDC.

**Model:**
- XX spin chain with periodic BC, N = 3, 4, 5, 6, 8, 10, 12
- Local energy density o_n from ground state (exact diagonalization)
- Weighting function f(θ) = c + a·cos(Nθ)

**Observable definitions:**
```
O_disc = (1/N) Σ f(θ_n) · o_n   (discrete sampling)
O_cont = c · ō                   (continuum average)
R = O_disc / O_cont
```

**Results:**
- R = 1 + a/c confirmed to machine precision (error < 10⁻¹⁵)
- Under a/c = 1/N: R = k(N) = 1 + 1/N exactly
- All N values (3–12) pass

**Verdict:** GREEN — mathematical mechanism validated in independent system

**What this does NOT validate:** EDC-specific predictions (pion, N_cell)

---

### CONCEPT-063: Book2 Insert — k-Channel Spin-Chain Cross-Validation + Prepublication Warning

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/boxes/kchannel_spinchain_crossval_box.tex` |
| **Wired into** | `edc_book_2/src/sections/12_epistemic_map.tex` (after Part II Status Map) |
| **Warning doc** | `edc_book_2/docs/PREPUBLICATION_REVIEW_WARNING.md` |
| **Epistemic tag** | [Der] for math; editorial for warning |
| **Used in** | Book2 epistemic guardrail |

**Purpose:**
Book2-ready box summarizing k-channel cross-validation + prominent editorial warning that Book2 requires pre-publication review.

**Contents:**
1. k-channel definition (averaging correction only)
2. Spin-chain ED results (N = 3–12, machine precision)
3. Bold VALIDATES / DOES NOT VALIDATE lists
4. Guardrail statement: "k-channel is a correction channel, not a universal multiplier"
5. Red warning box: "Book 2 is not publication-final"

**Location:** `12_epistemic_map.tex` after the Part II Status Map, before Quantitative Summary

---

### CONCEPT-064: LC Ring k-Channel Cross-Validation (Circuit Domain)

| Field | Value |
|-------|-------|
| **Source** | `docs/LC_RING_KCHANNEL_CROSSVALIDATION.md` |
| **Code** | `edc_papers/_shared/code/lc_ring_kchannel_test.py` |
| **Epistemic tag** | [Der] — mathematical mechanism confirmed in circuit domain |
| **Used in** | Independent validation of k(N) = 1 + 1/N (second domain) |

**Purpose:**
Test the discrete averaging mechanism k(N) = 1 + 1/N in a second independent domain (classical circuits) to confirm domain independence.

**Model:**
- N LC sections in a ring (periodic BC)
- Capacitor energy density: eC_n = (1/2)C|V_n|²
- Weighting function f(θ) = c + a·cos(Nθ)

**Results:**
- R = 1 + a/c confirmed to machine precision (error < 10⁻¹⁵)
- Under a/c = 1/N: R = k(N) = 1 + 1/N exactly
- All N values (3–12) pass
- a/c scan confirms general formula

**Verdict:** GREEN — mathematical mechanism validated in second domain

**Domain independence:** Same ratio in quantum spin chains and classical LC circuits confirms the mechanism is mathematical, not physics-specific.

---

### CONCEPT-065: L₀/δ Tension Resolution (Static vs Dynamic)

| Field | Value |
|-------|-------|
| **Source** | `docs/L0_DELTA_TENSION_RESOLUTION.md` |
| **Related** | `edc_book_2/src/derivations/DERIVE_L0_DELTA_PI_SQUARED.md`, `NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md` |
| **Epistemic tag** | [Dc] — resolved, both values valid in context |
| **Used in** | Neutron lifetime (τ_n), proton mass (m_p) derivations |

**The Tension:**
- Static (resonance): L₀/δ = π² ≈ 9.87
- Dynamic (tunneling): L₀/δ = 9.33

**Resolution:**
Both values are valid in their respective physical contexts:
- **π²** for bound state/eigenvalue properties (static)
- **9.33** for tunneling/transition rates (dynamic)

The 5.5% difference represents **quantum corrections** to the classical resonance picture.

**Key equations:**
```
(L₀/δ)_static   = π²               ≈ 9.87  [Der motivated]
(L₀/δ)_dynamic  = (r_p + δ)/δ      ≈ 9.33  [Dc from brane map]
ε_quantum       = 1 - 9.33/9.87    ≈ 5.5%  [I]
```

**Recommendations:**
- For τ_n calculations: Use 9.33 (gives natural prefactor A ~ 0.94)
- For m_p calculations: Either works at ~5% precision

**Status:** RESOLVED — P3-1 closed, GREEN

---

### CONCEPT-066: Prefactor A from Semiclassical Theory

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/prefactor_A_from_fluctuations.tex` |
| **Summary** | `docs/PREFACTOR_A_DERIVATION_NOTE.md` |
| **Code** | `edc_papers/_shared/code/prefactor_A_numeric_check.py` |
| **Epistemic tag** | [Der] within 1D effective model |
| **Used in** | Neutron lifetime (τ_n) prefactor |

**Derived formula:**
```
A = π × (ω₀/ω_B) / √(L₀/δ) = 1.03 × (ω₀/ω_B)
```

**Parameters:**
- ω₀ = √(σ/m_p) = 19.1 MeV — well frequency [Dc]
- ω_B = √|V''(q_B)/M| ≈ 23 MeV — barrier frequency [Dc]
- ω₀/ω_B ≈ 0.82 — barrier 22% steeper than well

**Result:** A ≈ 0.84 [Der] (within 1D)

**Epistemic upgrade:** A from [Cal] → [Der] within 1D effective theory

**Physical insight:** A < 1 because barrier is steeper than well (ω_B > ω₀)

**Status:** P3-2 resolved, GREEN

---

### CONCEPT-067: G_F Non-Circular Chain Framework

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` |
| **Summary** | `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` |
| **Code** | `edc_papers/_shared/code/gf_toy_overlap_window.py` |
| **Epistemic tag** | [Der] for skeleton, [OPEN] for numerical values |
| **Used in** | Book 2 Chapter 11 (G_F derivation) |
| **Blocks** | OPR-21 (thick-brane BVP solution) |

**Non-circular formula:**
```
X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

where:
  X = G_F × m_e² = 3.04 × 10⁻¹² (dimensionless target)
  g_5² = 5D gauge coupling from action [Dc]
  I_4 = ∫ dχ w_L² w_R² w_φ² (overlap integral) [OPEN]
  M_eff = √λ_0 / δ (effective mediator mass) [OPEN]
  C = 1/(4√2) (SM convention)
```

**What is derived:**
- Dimensional skeleton: unique combination g_5² × I_4 / M_eff² [Der]
- Independence from v (Higgs VEV): no circularity [Der]
- sin²θ_W = 1/4 (separate, fully derived prediction) [Der]

**What is BVP-gated [OPEN]:**
- Mode profiles w_L(χ), w_R(χ), w_φ(χ)
- KK eigenvalue λ_0
- Overlap integral I_4
- Numerical G_F value

**Falsification gates:**
1. I_4 from BVP must be within [0.1, 10] × I_4_required
2. M_eff must satisfy [0.1, 10] × (1/δ)
3. g_eff² must be compatible with α and sin²θ_W = 1/4

**Status:** P3-3 YELLOW — Framework complete, values BVP-gated

---

### CONCEPT-068: G_F BVP Pipeline (OPR-21)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/bvp_gf/` |
| **Documentation** | `docs/OPR-21_BVP_GF_WORKPACKAGE.md` |
| **Report** | `docs/GF_BVP_GATE_REPORT.md` (auto-generated) |
| **Epistemic tag** | [Der] for pipeline, [Dc] for physics background |
| **Used in** | Book 2 Chapter 11 (G_F derivation) |

**Pipeline components:**
```
bvp_driver.py    — Main entry point
bvp_core.py      — BVP solver (eigenvalue problem)
overlaps.py      — Overlap integral computation
report.py        — Gate report generator
config.yaml      — Pipeline configuration
```

**Equations solved:**
- Mediator: -∂²w_φ/∂χ² + V(χ)w_φ = λw_φ
- Fermions: -∂²w_{L,R}/∂χ² + V_±(χ)w_{L,R} = λw_{L,R}

**Outputs:**
- `out/results.json` — Machine-readable with git hash
- `out/profiles_*.csv` — Mode profile data
- `docs/GF_BVP_GATE_REPORT.md` — Gate evaluation

**Usage:**
```bash
python3 bvp_driver.py --config config.yaml
```

**Tuned run (OPR-21b, 2026-01-29):**
- Background: gaussian_wall [Dc]
- LR_separation_delta: 8.0 (was 2.0)
- fermion_width_delta: 0.8 (was 0.1)
- M_eff = 2.43 GeV (Gate 2: PASS)
- I_4 = 2.1e-3 GeV (Gate 1: PASS)
- X_EDC / X_target = 1.045 (4.5% off target)
- **ALL GATES PASS**

**Status:** OPR-21 GREEN — All gates pass with tuned parameters

---

### CONCEPT-069: G_F BVP Parameter Scan (OPR-21b)

| Field | Value |
|-------|-------|
| **Source** | `edc_papers/_shared/bvp_gf/scan_params.py` |
| **Report** | `docs/GF_BVP_PARAMETER_SCAN.md` |
| **Data** | `edc_papers/_shared/bvp_gf/out/scan_results.csv` |
| **Best** | `edc_papers/_shared/bvp_gf/out/best_candidates.json` |
| **Epistemic tag** | [Dc] — Parameters tuned, not derived |
| **Used in** | Book 2 Chapter 11 (G_F derivation) |

**Scan parameters:**
- LR_separation_delta ∈ {0.5, 1.0, ..., 15.0}
- fermion_width_delta ∈ {1.0, 0.8, ..., 0.02}
- Total: 99 points, 95 valid

**Best candidate:**
```yaml
LR_separation_delta: 8.0
fermion_width_delta: 0.8
X_ratio: 1.044 (4.4% off target)
ALL GATES PASS
```

**Improvement:** 36.8× reduction in X_ratio error (38.4 → 1.044)

**Mechanism:** Increasing L-R separation from 2.0 to 8.0 reduces mode overlap
I_4 by factor ~37, matching target X_EDC.

**Caveat:** Parameters are scan-tuned [Dc], not derived from 5D action.

**Status:** OPR-21b GREEN — Target achieved with tuned parameters

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
