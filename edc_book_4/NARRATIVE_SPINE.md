# NARRATIVE SPINE: Book IV Structure

**Date:** 2026-02-09
**Title:** Nuclear Structure from Topological Pinning
**Source:** `edc_book_2/src/derivations/`

---

## BOOK IV IDENTITY

This is Book IV in the EDC series:
- **Book I:** Foundations (edc_book/, published v17.49)
- **Book II:** Weak Sector (edc_book_2/, in development)
- **Book III:** Gravity + GUT + Proton Decay (paper_gravity_block003/)
- **Book IV:** Nuclear Structure + Topological Pinning (THIS BOOK)

---

## NARRATIVE PHILOSOPHY

### What This Book Does:
- Derives nuclear binding from 5D brane topology
- Predicts τ_n = 880 s from instanton tunneling
- Predicts α-decay half-lives from coordination frustration
- Uses ONLY EDC-internal parameters (σ, δ, L₀, T*, M₅)

### What This Book Does NOT Do:
- NO 3D Standard Model language
- NO QCD, SU(3)×SU(2)×U(1), Pati-Salam
- NO CKM/PMNS matrices
- NO V-A, gauge, electroweak, fermion generations
- NO "quarks," "gluons," "W bosons" as fundamental
- Empirical data → "measurements/observables" ONLY

### Quarantine Policy:
- Fitting to external data → Appendix Q
- SM analogies (non-binding) → Appendix X
- Layer B numerics → clearly marked sections

---

## PART STRUCTURE

### PART A: TOPOLOGICAL FOUNDATIONS (Ch. 1-3)

**Learning Goal:** Establish proton as ground state, neutron as metastable excitation.

| Ch | Title | Core Claim | Epistemic |
|----|-------|------------|-----------|
| 1 | Proton as Topological Ground State | Proton = Z₆ minimal surface | [Der] |
| 2 | Junction Symmetries | Z₆ crystallizes from S⁵ topology | [Der] |
| 3 | Neutron as Metastable State | Neutron = Z₃ double-well excited state | [Dc] |

**Key Derivations:**
- Steiner tree geometry → Z₆ junction
- Z₃ ⊂ Z₆ subgroup structure
- Double-well V(q) from 5D

### PART B: PINNING MECHANISM (Ch. 4-5)

**Learning Goal:** Connect brane tension σ to observable nuclear binding K.

| Ch | Title | Core Claim | Epistemic |
|----|-------|------------|-----------|
| 4 | From σ to K | K = f × σ × A_contact | [Der] |
| 5 | M6 Coordination Lattice | Allowed n = 2^a × 3^b | [Der] |

**Key Derivations:**
- Contact geometry → pinning constant
- M6 lattice from junction topology
- Allowed/forbidden coordination numbers

### PART C: NEUTRON LIFETIME (Ch. 6-9)

**Learning Goal:** Derive τ_n = 880 s from first principles.

| Ch | Title | Core Claim | Epistemic |
|----|-------|------------|-----------|
| 6 | Instanton Derivation | S_E = κ × (L₀/δ) × V_B/E_barrier | [Der] |
| 7 | κ = 2π from Homotopy | π₁(S¹) = ℤ → winding number | [Der] |
| 8 | L₀/δ Scale Ratio | L₀/δ ≈ π² from 5D geometry | [P] |
| 9 | τ_n = 880 s Prediction | τ = A·exp(S_E) matches observation | [Der] |

**Key Derivations:**
- 5D → effective 1D reaction coordinate
- Homotopy argument for κ
- Instanton action formula
- Numerical evaluation → 880 s

### PART D: NUCLEAR BINDING (Ch. 10-12)

**Learning Goal:** Explain light nuclei binding from pinning.

| Ch | Title | Core Claim | Epistemic |
|----|-------|------------|-----------|
| 10 | Deuterium | B.E. = 3K (3 effective bonds) | [Dc] |
| 11 | Helium-4 | B.E. = confinement + pinning + surface + flux | [Der] |
| 12 | Light Nuclei | Systematic A ≤ 10 predictions | [Der] |

**Key Derivations:**
- Bond counting from topology
- He-4 four-term formula
- Li-6, Be-8 special cases

### PART E: ALPHA DECAY (Ch. 13-15)

**Learning Goal:** Predict superheavy α-decay from coordination frustration.

| Ch | Title | Core Claim | Epistemic |
|----|-------|------------|-----------|
| 13 | Geiger-Nuttall Baseline | Empirical log(t) = a×Z/√Q + b | [Empirical] |
| 14 | Coordination Frustration | d(n) = min_k |n - 2^a×3^b| | [Der] |
| 15 | Superheavy Predictions | Tables for Z = 114-120 | [Prediction] |

**Key Derivations:**
- Frustration distance d(n) formula
- Correction to GN baseline
- Out-of-sample validation

### PART F: SYNTHESIS (Ch. 16-17)

**Learning Goal:** Unify all predictions, establish reproducibility.

| Ch | Title | Content | Epistemic |
|----|-------|---------|-----------|
| 16 | Unified Picture | Derivation tree, open problems | [Summary] |
| 17 | Reproducibility | Step-by-step instructions | [Procedure] |

---

## CHAPTER DETAIL: NARRATIVE FLOW

### Chapter 1: Proton as Topological Ground State

**Opening hook:** Why is the proton stable? (No decay observed τ_p > 10³⁴ years)

**Narrative arc:**
1. Pose stability question
2. Introduce 5D brane topology
3. Show Z₆ as minimal-energy configuration
4. Derive Steiner geometry
5. Conclude: proton = topological ground state

**Source:** `04b_proton_anchor.tex`, `04c_routeB_z6_steiner.tex`

### Chapter 3: Neutron as Metastable State

**Opening hook:** Neutron decays in ~880 s. Why this particular lifetime?

**Narrative arc:**
1. Present the puzzle: τ_n ≈ 880 s
2. Introduce Z₃ as subgroup of Z₆
3. Derive double-well potential V(q)
4. Show neutron as excited state in well
5. Preview instanton tunneling (→ Part C)

**Source:** `Z3_SYMMETRY_ANALYSIS_NEUTRON.md`, `V_B_FROM_Z3_BARRIER_CONJECTURE.md`

### Chapter 6: Instanton Derivation

**Opening hook:** How does 5D geometry encode decay rate?

**Narrative arc:**
1. Start from 5D action S_5D
2. Reduce to effective 1D coordinate q
3. Identify instanton solution
4. Derive Euclidean action S_E
5. Formula: τ = A·(ℏ/ω₀)·exp(S_E)

**Source:** `INSTANTON_DERIVATION_CHAIN.md`, `S5D_TO_SEFF_Q_REDUCTION.md`

### Chapter 9: τ_n = 880 s Prediction

**Opening hook:** Does the formula actually give 880 s?

**Narrative arc:**
1. Assemble all parameters (κ, L₀/δ, V_B, ω₀, A)
2. Compute S_E numerically
3. Evaluate τ
4. Compare to measurement (Layer B only)
5. Cross-check with Kramers simulation

**Source:** `NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md`, `kramers_double_well_v2.py`

### Chapter 15: Superheavy Predictions

**Opening hook:** What do we predict for elements not yet synthesized?

**Narrative arc:**
1. Review coordination frustration model
2. Apply to Z = 114-120
3. Generate prediction tables
4. Discuss testability
5. List falsifiable predictions

**Source:** `superheavy_predictions.py`

---

## APPENDIX STRUCTURE

| Appendix | Content | Status |
|----------|---------|--------|
| A | superheavy_predictions.py (full listing) | Code |
| B | kramers_double_well_v2.py (full listing) | Code |
| C | Numerical Tables (from Python output) | Data |
| D | Provenance Index (Chapter.Section → Source) | Reference |
| Q | Quarantine: Fitting Procedures | External |
| X | Analogies (non-binding SM comparisons) | Disclaimer |

---

## DE-DUPLICATION RULES

| Content | Canonical Source | Alternates |
|---------|------------------|------------|
| K formula | M6_K_RIGOROUS_DERIVATION.md | M6_PINNING_CONSTANT (earlier) |
| τ_n chain | NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md | INSTANTON_DERIVATION_CHAIN (partial) |
| L₀/δ | DERIVE_L0_DELTA_PI_SQUARED_V2.md | V1 (earlier) |

---

## FORBIDDEN TERMS (grep scan targets)

Must NOT appear in main text:
- QCD, chromodynamics, gluon
- Standard Model, SM
- SU(3), SU(2), U(1) (as gauge groups)
- Pati-Salam, SO(10), E6
- CKM, PMNS, Kobayashi-Maskawa
- V-A, axial, electroweak
- fermion generation, family
- W boson, Z boson, Higgs (as fundamental)

Allowed in Appendix Q/X only:
- Empirical comparisons with SM predictions
- "In SM language, this would correspond to..."

---

## BUILD STRUCTURE

```
edc_book_4/
├── main.tex                    # Master document
├── preamble.tex                # Packages, macros
├── chapters/
│   ├── ch01_proton_ground.tex
│   ├── ch02_junction_symmetries.tex
│   ├── ch03_neutron_metastable.tex
│   ├── ch04_sigma_to_K.tex
│   ├── ch05_M6_lattice.tex
│   ├── ch06_instanton.tex
│   ├── ch07_kappa_homotopy.tex
│   ├── ch08_L0_delta_ratio.tex
│   ├── ch09_tau_n_prediction.tex
│   ├── ch10_deuterium.tex
│   ├── ch11_helium4.tex
│   ├── ch12_light_nuclei.tex
│   ├── ch13_geiger_nuttall.tex
│   ├── ch14_coordination_frustration.tex
│   ├── ch15_superheavy.tex
│   ├── ch16_unified_picture.tex
│   └── ch17_reproducibility.tex
├── appendices/
│   ├── appA_superheavy_code.tex
│   ├── appB_kramers_code.tex
│   ├── appC_tables.tex
│   ├── appD_provenance.tex
│   ├── appQ_quarantine.tex
│   └── appX_analogies.tex
├── figures/
├── tables/
└── CHRONOLOGY_MAP.md
```

---

## QUALITY GATES

Before each chapter is complete:

1. **Source traced:** Every formula has [Der]/[Dc]/[P] tag
2. **Provenance linked:** Source file cited
3. **SM scan passed:** No forbidden terms
4. **Numerics contained:** All values from Python scripts
5. **Layer B marked:** External comparisons clearly labeled

---

## NEXT STEPS

1. Create LaTeX directory structure
2. Write main.tex with chapter includes
3. Begin Part A chapters (topological foundations)
4. Generate tables from Python scripts
5. Run forbidden-term grep scan
6. Build and verify compilation

---

**NARRATIVE SPINE COMPLETE. Ready for LaTeX construction.**
