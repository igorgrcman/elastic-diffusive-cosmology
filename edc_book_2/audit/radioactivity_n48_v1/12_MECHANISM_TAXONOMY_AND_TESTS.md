# MECHANISM TAXONOMY AND TESTS (V6)

**Created**: 2026-01-31
**Purpose**: M1-M6+ mechanisms for achieving effective n≈48
**Source**: V4 DN-040..048, V5 04_FORBIDDEN_TOPOLOGIES

---

## Mechanism Catalog

### M1: Domain Mixing
- **Definition**: Multiple coordination domains coexist; n_eff is weighted average
- **n=48 Pathway**: Mix n=36 and n=72 domains in ratio 1:1 → n_eff = 54; or n=36 + n=48 mix
- **Formula**: n_eff = Σᵢ wᵢ × nᵢ [P] (AS-N48-006)
- **Predicted Observables**:
  - Anisotropic α-emission (domains have preferred directions)
  - Broad nuclear resonances (multiple configurations)
- **Required Data**: Angular distribution of α-particles
- **Source**: DN-040, 22826edd:2479-2492

### M2: Defects (Y-Junctions, Domain Walls)
- **Definition**: Topological defects reduce effective coordination from bulk value
- **n=48 Pathway**: Start with n_bulk = 54 or 72; defects reduce to n_eff ≈ 48
- **Formula**: n_eff = n_bulk - ρ_d × Δn [P] (AS-N48-007)
- **Predicted Observables**:
  - Lifetime anomalies correlating with deformation
  - Isomer shifts larger than expected
- **Required Data**: Isomer branching ratios, quadrupole moments
- **Source**: DN-041..042, 73d92ff5:517-530

### M3: Alpha-Clusterization
- **Definition**: Preformed α-clusters act as n=4 units; nucleus = collection of α-clusters
- **n=48 Pathway**: 12 α-clusters → n_eff = 12 × 4 = 48 (if each is fully coordinated)
- **Formula**: n_eff = n_cluster × 4 [P] (AS-N48-008)
- **Predicted Observables**:
  - Enhanced α-branching for N≈Z nuclei
  - Cluster knockout reactions show preformation
- **Required Data**: α-spectroscopic factors
- **Source**: DN-043..044, 22826edd:2450-2478

### M4: Metastable M-Structures
- **Definition**: Kinetically trapped configurations with n_eff ≠ equilibrium value
- **n=48 Pathway**: Frozen at n=48 during formation; relaxation blocked
- **Formula**: n_eff(isomer) = n_formation [P] (AS-N48-014)
- **Predicted Observables**:
  - Isomers with different branching than ground state
  - Long-lived states despite high Q-value
- **Required Data**: Isomer excitation energies, spins
- **Source**: DN-045, 73d92ff5:442-450

### M5: Quasicrystal (Speculative)
- **Definition**: Aperiodic internal structure with irrational effective n
- **n=48 Pathway**: Not directly → n=48; provides alternative escape from forbidden zone
- **Formula**: n_eff = f(τ) where τ is quasiperiodicity [P] (AS-N48-015)
- **Predicted Observables**:
  - 5-fold symmetry in decay products
  - Novel cluster emission (14C, 24Ne)
- **Required Data**: Exotic decay searches
- **Source**: DN-046 (proposed, no direct donor)

### M6: Core-Mantle Structure
- **Definition**: Layered nucleus with different n in core vs mantle
- **n=48 Pathway**: Core at n=48 (stable), mantle at n=36-42 (relaxing)
- **Formula**: n_eff = α × n_core + (1-α) × n_mantle [P] (AS-N48-010)
- **Predicted Observables**:
  - Charge radius anomalies in SHE
  - Sequential decay patterns (mantle first, then core)
- **Required Data**: Isotope shift measurements for SHE
- **Source**: DN-047..048, 22826edd:4847-4925

### M7: Coordination Saturation (New for V6)
- **Definition**: At high A, n naturally saturates near n=48 regardless of mechanism
- **n=48 Pathway**: Geometric limit as nucleus grows; surface/volume ratio stabilizes
- **Formula**: n(A) → n_sat as A → ∞, with n_sat ∈ [42, 50] [P]
- **Predicted Observables**:
  - Decreasing variation in n for A > 300
  - Convergence of decay patterns
- **Required Data**: SHE properties extrapolated
- **Source**: Inferred from crystal close-packing limits (no direct donor)

### M8: Collective Mode Renormalization (New for V6)
- **Definition**: Collective vibrations effectively increase coordination through dynamic averaging
- **n=48 Pathway**: Static n=42 + vibrational enhancement → n_eff ≈ 48
- **Formula**: n_eff = n_static + Δn_vib where Δn_vib ~ T/ω [P]
- **Predicted Observables**:
  - Temperature-dependent decay rates
  - Giant resonance coupling to decay
- **Required Data**: Excited state decay systematics
- **Source**: Conceptual extension (no direct donor)

---

## Test Registry

### TEST-N48-01: Domain Anisotropy
- **Mechanism Tested**: M1 (Domain Mixing)
- **Protocol**: Measure α-emission angular distribution for A > 230 α-emitters
- **Success Criterion**: Anisotropy > 5% for nuclei predicted to have M1 active
- **Failure Mode**: Isotropic emission despite M1 prediction
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-02: Defect-Lifetime Correlation
- **Mechanism Tested**: M2 (Defects)
- **Protocol**: Compare half-lives of deformed vs spherical nuclei at same A
- **Success Criterion**: Deformed nuclei show t₁/₂ anomaly correlating with ε_defect
- **Failure Mode**: No correlation between deformation and lifetime deviation
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-03: Cluster Preformation
- **Mechanism Tested**: M3 (α-Clusterization)
- **Protocol**: Measure α-spectroscopic factors for N=Z vs N≠Z nuclei
- **Success Criterion**: S_α(N=Z) > S_α(N≠Z) by factor > 2
- **Failure Mode**: Spectroscopic factors uncorrelated with N/Z
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-04: Isomer Branching Anomaly
- **Mechanism Tested**: M4 (Metastable)
- **Protocol**: Compare branching ratios of isomers vs ground states
- **Success Criterion**: Find ≥3 cases where isomer branching differs by >10% from ground
- **Failure Mode**: All isomers match ground state branching
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-05: Exotic Cluster Search
- **Mechanism Tested**: M5 (Quasicrystal)
- **Protocol**: Search for 14C, 24Ne emission in trans-actinide region
- **Success Criterion**: Detect exotic cluster decay with pattern inconsistent with M3
- **Failure Mode**: All cluster emission explainable by α-multiples
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-06: SHE Charge Radius
- **Mechanism Tested**: M6 (Core-Mantle)
- **Protocol**: Measure isotope shifts for Z > 100 elements
- **Success Criterion**: Radius anomaly pattern consistent with core-mantle structure
- **Failure Mode**: Smooth radius systematics with no layering signature
- **Data Status**: [BL:SOURCE_TBD]

### TEST-N48-07: n(A) Saturation Check
- **Mechanism Tested**: M7 (Coordination Saturation)
- **Protocol**: Calculate n(A) for A = 200, 300, 400, 500; check convergence
- **Success Criterion**: |n(500) - n(400)| < |n(300) - n(200)|
- **Failure Mode**: n(A) diverges or oscillates at high A
- **Data Status**: Can test with toy model (no external data needed)

### TEST-N48-08: d(n) Branching Correlation
- **Mechanism Tested**: All (via H-N48-01)
- **Protocol**: For branch points, calculate Δd(n) for each channel; correlate with branching ratio
- **Success Criterion**: Channel with smaller d(n_daughter) has higher branching >70% of cases
- **Failure Mode**: Branching uncorrelated or anti-correlated with Δd(n)
- **Data Status**: [BL:SOURCE_TBD] for ratios; n(A) from toy model

---

## Mechanism-to-n=48 Summary

| Mechanism | How n≈48 Achieved | Testability |
|-----------|-------------------|-------------|
| M1 | Weighted average of domains | Medium |
| M2 | Defects reduce from higher n | Medium |
| M3 | 12 α-clusters × 4 | High |
| M4 | Frozen during formation | Medium |
| M5 | Irrational n escape | Low |
| M6 | Core at n=48, mantle varies | Medium |
| M7 | Geometric saturation limit | High |
| M8 | Vibrational renormalization | Low |

---

## Test Summary

| Test | Mechanism | Data Needed | Status |
|------|-----------|-------------|--------|
| TEST-N48-01 | M1 | Angular distribution | [BL] |
| TEST-N48-02 | M2 | t₁/₂ + deformation | [BL] |
| TEST-N48-03 | M3 | Spectroscopic factors | [BL] |
| TEST-N48-04 | M4 | Isomer branching | [BL] |
| TEST-N48-05 | M5 | Exotic decay | [BL] |
| TEST-N48-06 | M6 | Isotope shifts | [BL] |
| TEST-N48-07 | M7 | None (toy model) | Ready |
| TEST-N48-08 | All | Branching ratios | [BL] |

---

## Counts

| Category | Count |
|----------|-------|
| Mechanisms (M1-M8) | 8 |
| Tests (TEST-N48-01..08) | 8 |
| With direct donor | 6 (M1-M6) |
| New for V6 | 2 (M7, M8) |
