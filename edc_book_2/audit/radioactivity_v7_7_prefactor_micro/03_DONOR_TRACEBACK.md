# V7.7 DONOR TRACEBACK

**Created**: 2026-01-31
**Purpose**: Provenance for all borrowed statements

---

## V7.6.1 Results

### T1: Hindrance Interaction
**Source**: `audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md:45-65`
**Content**: g₀(H0) = -0.34, g₁(interaction H1) = +0.08, g₂(interaction H2) = +0.12
**Tag**: [Der]

### T2: Parity Control
**Source**: `audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md:85-105`
**Content**: g = -0.29 ± 0.12, p = 0.016 after EE/EO/OE/OO dummies
**Tag**: [Der]

### T3: Model Comparison
**Source**: `audit/radioactivity_v7_6_1_sign/01_TEST_BARRIER_vs_PREFACTOR.md:115-145`
**Content**: AIC(A) = 198.4, AIC(B) = 201.8, Δ = -3.4 favoring prefactor
**Tag**: [Der]

---

## V7.4/V7.5 Dataset

### Core Regression
**Source**: `audit/radioactivity_v7_4_alpha100/06_GN_FIT_V7_4.md`
**Content**: M2: g = -0.31 ± 0.11, p = 0.006, R² = 0.9933
**Tag**: [Der]

### Cross-Validation
**Source**: `audit/radioactivity_v7_5_generalization/04_CV_PREDICTIVE_GAIN.md:49-56`
**Content**: ΔRMSE = 0.043, all 10 folds favor M2
**Tag**: [Der]

### Permutation Test
**Source**: `audit/radioactivity_v7_5_generalization/05_PERMUTATION_TEST.md:73-79`
**Content**: p_perm = 0.006 (60/10000 as extreme)
**Tag**: [Der]

---

## Forbidden Topologies

### M1-M6 Mechanism Catalog
**Source**: `audit/radioactivity_forbidden_v5/04_FORBIDDEN_TOPOLOGIES_V5.md:44-97`
**Content**:
- M1: Domain mixing [I]
- M2: Defects [P]
- M3: α-Clusterization [I]
- M4: Metastable [P]
- M5: Quasicrystal [P]
- M6: Core-Mantle [P]
**Tag**: Per mechanism

### Forbidden Zone Table
**Source**: `audit/radioactivity_forbidden_v5/04_FORBIDDEN_TOPOLOGIES_V5.md:19-33`
**Content**: FT-37 through FT-47 with d(36), d(48), mechanisms
**Tag**: [Der] for structure, [P] for mechanisms

---

## Crystal Models

### Coordination Table
**Source**: `audit/radioactivity_forbidden_v5/05_BULK_CRYSTAL_NUCLEI_MODELS_V5.md:9-20`
**Content**: Diamond(4), SC(6), BCC(8), FCC(12), ... all n = 2^a × 3^b
**Tag**: [Der]

### Hexagonal Origin
**Source**: `audit/radioactivity_forbidden_v5/05_BULK_CRYSTAL_NUCLEI_MODELS_V5.md:44-56`
**Content**: Z₆ = Z₂ × Z₃ from hexagonal lattice geometry
**Tag**: [Der] (from DN-057, 22826edd:12444)

### Frustration Gradient
**Source**: `audit/radioactivity_forbidden_v5/05_BULK_CRYSTAL_NUCLEI_MODELS_V5.md:60-87`
**Content**: ε_f(n) = K × min(d(36,n), d(48,n))², K ≈ 0.94 MeV
**Tag**: [Der]

---

## Forbidden Alternatives Matrix

### Domain Mixing Recipes
**Source**: `audit/radioactivity_forbidden_v2/FORBIDDEN_ALTERNATIVES_MATRIX.md:49-64`
**Content**: n = w₁ × 36 + w₂ × 48 for each n ∈ [37,47]
**Tag**: [I]

### Mechanism Assignments
**Source**: `audit/radioactivity_forbidden_v2/FORBIDDEN_ALTERNATIVES_MATRIX.md:170-186`
**Content**: n → {mechanism, predicted decay, d(n)}
**Tag**: [P]

---

## Original Donor Sources

### DN-040 (Domain Mixing)
**Source**: 22826edd:2479-2492
**Content**: φ_domain boundary mixing order parameter
**Tag**: [I]

### DN-041..042 (Defects)
**Source**: 73d92ff5:517-530, 22826edd:41
**Content**: ρ_defect density, Y-junctions, walls
**Tag**: [P]

### DN-043..044 (α-Clusterization)
**Source**: 22826edd:2450-2478
**Content**: n_cluster = number of preformed α-clusters
**Tag**: [I]

### DN-050..058 (Crystal Mapping)
**Source**: 22826edd:2450, 11337, 11684, 16113
**Content**: Crystal → nuclear coordination analogy
**Tag**: [I]

---

## Summary

| Source Type | Count | Primary Tag |
|-------------|-------|-------------|
| V7.6.1 test results | 3 | [Der] |
| V7.4/V7.5 regression | 3 | [Der] |
| V5 forbidden topologies | 2 | [Der]/[P] |
| V5 crystal models | 3 | [Der] |
| V2 alternatives matrix | 2 | [I]/[P] |
| Original donors | 4 | [I]/[P] |

