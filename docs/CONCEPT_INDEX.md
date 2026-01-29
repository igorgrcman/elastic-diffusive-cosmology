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
