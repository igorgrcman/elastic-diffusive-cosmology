# CHAIN VERIFICATION PLAN V5

**Created**: 2026-01-31
**Purpose**: Upgrade path for epistemic tags
**Format**: Claim → Current → Target → Requirements

---

## Upgrade Path Legend

```
[P] → [I]   : Gather supporting data/observations
[I] → [Cal] : Calibrate against reference dataset
[Cal] → [Dc]: Derive conditional formula
[Dc] → [Der]: Remove all conditionals
```

---

## LAW Upgrades

### LAW-1: Coordination Selection [Der]
- **Current**: [Der]
- **Target**: N/A (already derived)
- **Status**: ✓ Complete
- **Citation**: DN-001..005

### LAW-2: Nuclear Saturation [Der]
- **Current**: [Der]
- **Target**: N/A
- **Status**: ✓ Complete
- **Citation**: DN-010..013

### LAW-3: Geiger-Nuttall + Frustration
- **Current**: [I] (R² = 0.9941)
- **Target**: [Der]
- **Requirements**:
  1. Derive ε_f(A) from first principles
  2. Show G-N + ε_f follows from barrier formula
  3. Calculate a, b, c coefficients from theory
- **Blocking**: OQ-V5-002 (ε_f(A) formula)

### LAW-4: Barrier Formula
- **Current**: [Der]
- **Target**: N/A
- **Status**: ✓ Complete
- **Citation**: DN-020..022

### LAW-5: Pinning Constant
- **Current**: [Der]/[Cal]
- **Target**: [Der]
- **Requirements**:
  1. Derive f ≈ 0.3 from Z₆ geometry
  2. Show A_contact formula from domain structure
- **Blocking**: OQ-V5-003 (f origin)

### LAW-6: α-Cluster Binding
- **Current**: [I]
- **Target**: [Der]
- **Requirements**:
  1. Show n_eff = 4 for preformed cluster
  2. Calculate cluster formation probability
- **Blocking**: Cluster model derivation

---

## INV Upgrades

### INV-1: Frustration Energy
- **Current**: [Der]
- **Target**: N/A
- **Status**: ✓ Complete

### INV-2: Distance to Allowed
- **Current**: [Der]
- **Target**: N/A
- **Status**: ✓ Complete

### INV-3: n(A) Formula
- **Current**: [P]
- **Target**: [I] → [Der]
- **Path**:
  1. [P] → [I]: Verify n(A) ≈ 6.1 × A^(1/3) against shell model data
  2. [I] → [Dc]: Connect to r = r₀ × A^(1/3) radius formula
  3. [Dc] → [Der]: Derive from nuclear geometry
- **Blocking**: OQ-V5-001

---

## CONS Upgrades

### CONS-1: n Monotonicity
- **Current**: [P]
- **Target**: [I]
- **Requirements**:
  1. Verify d(n) decreases on 10+ decay chains
  2. Document any exceptions with mechanism
- **Data Needed**: All chain data from 12_DATA_REQUESTS

### CONS-2: Mode Selection
- **Current**: [P]
- **Target**: [I]
- **Requirements**:
  1. Compute correlation between d(n) and α-branching
  2. r > 0.7 for upgrade to [I]
- **Data Needed**: Branching ratios from 12_DATA_REQUESTS

---

## Hypothesis Upgrades

### H1: Proximity Rule
- **Current**: [P]
- **Target**: [I]
- **Requirements**:
  1. Plot α% vs d(n) for 10+ branch points
  2. Show monotonic relationship
- **Data Needed**: 7 branching ratios

### H2: Asymmetry Rule
- **Current**: [P]
- **Target**: [I]
- **Requirements**:
  1. Plot β% vs N/Z for branch points
  2. Show correlation
- **Data Needed**: Same branching ratios

### H3: Cluster Preformation
- **Current**: [I]
- **Target**: [Dc]
- **Requirements**:
  1. Derive cluster probability from n(A)
  2. Show even-even enhancement from formula
- **Data Needed**: Even-even vs odd-A comparison

### H4: Energy Threshold
- **Current**: [Der]
- **Target**: N/A
- **Status**: ✓ Complete (follows from LAW-4)

### H5: Metastability
- **Current**: [P]
- **Target**: [I]
- **Requirements**:
  1. Find 3+ isomers with different branching
  2. Document systematic pattern
- **Data Needed**: Isomer branching data

---

## Mechanism Upgrades

| Mechanism | Current | Target | Requirements |
|-----------|---------|--------|--------------|
| M1 | [I] | [Dc] | Derive mixing formula |
| M2 | [P] | [I] | Find defect signatures |
| M3 | [I] | [Dc] | Derive cluster formula |
| M4 | [P] | [I] | Document isomer systematics |
| M5 | [P] | [P] | Search for quasicrystal nuclei |
| M6 | [P] | [I] | Find SHE core-mantle evidence |

---

## Verification Milestones

### Milestone 1: Core Laws Verified
- LAW-1, LAW-2, LAW-4 at [Der] ✓
- LAW-3 at [I] ✓
- Target: Complete by Phase 1

### Milestone 2: Branching Hypotheses Tested
- H1-H3 at [I]
- H4 at [Der]
- Target: Requires branching data

### Milestone 3: n(A) Formula Validated
- INV-3 at [I]
- CONS-1, CONS-2 at [I]
- Target: Requires chain data

### Milestone 4: Mechanism Formalization
- M1, M3 at [Dc]
- M2, M4, M6 at [I]
- Target: Extended research

---

## Data-Blocked Upgrades

| Upgrade | Data Needed | Source | Status |
|---------|-------------|--------|--------|
| LAW-3 [I]→[Der] | ε_f(A) derivation | Theory | Blocked |
| LAW-5 [Cal]→[Der] | f origin | Theory | Blocked |
| INV-3 [P]→[I] | n(A) comparison | Shell model | Blocked |
| CONS-1 [P]→[I] | Chain analysis | Nuclear data | Blocked |
| H1 [P]→[I] | Branching ratios | NNDC | Blocked |
| H2 [P]→[I] | Branching ratios | NNDC | Blocked |

---

## Summary

| Category | At [P] | At [I] | At [Dc]/[Cal] | At [Der] |
|----------|--------|--------|---------------|----------|
| Laws | 0 | 2 | 1 | 3 |
| Invariants | 1 | 0 | 0 | 2 |
| Conservation | 2 | 0 | 0 | 0 |
| Hypotheses | 2 | 2 | 0 | 1 |
| Mechanisms | 4 | 2 | 0 | 0 |
| **Total** | **9** | **6** | **1** | **6** |
