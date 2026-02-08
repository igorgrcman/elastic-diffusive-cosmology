# LAW REGISTRY V5

**Created**: 2026-01-31
**Purpose**: Laws, invariants, and falsification tests
**Source**: DN-001..085, V4 baseline

---

## Primary Laws

### LAW-1: Coordination Selection Rule
- **Statement**: n is ALLOWED iff n = 2^a × 3^b (a,b ≥ 0)
- **Source**: DN-001..005
- **Status**: [Der]
- **Origin**: Z₆ = Z₂ × Z₃ brane symmetry
- **Falsification**: Find stable nucleus with n = 5, 7, 10, 11, 13...

### LAW-2: Nuclear Saturation Constraint
- **Statement**: Optimal coordination n_opt ≈ 43.3 at nuclear density ρ₀
- **Source**: DN-010..013
- **Status**: [Der]
- **Implication**: n=43 is forbidden (prime > 3)
- **Falsification**: Measure n_opt ≠ 43 ± 2 from saturation data

### LAW-3: Geiger-Nuttall + Frustration
- **Statement**: log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
- **Source**: DN-015..019
- **Status**: [I] (R² = 0.9941 inferred from fit)
- **Parameters**: a, c, b from actinide calibration
- **Falsification**: R² < 0.95 on independent dataset

### LAW-4: Effective Barrier Formula
- **Statement**: ΔV_eff = ΔV + 6K × q²
- **Source**: DN-020..022
- **Status**: [Der]
- **Parameters**: K ≈ 0.94 MeV (pinning constant)
- **Falsification**: Independent K measurement |K - 0.94| > 0.2 MeV

### LAW-5: Pinning Constant Origin
- **Statement**: K = f × σ × A_contact
- **Source**: DN-023..026
- **Status**: [Der]/[Cal]
- **Parameters**: f ≈ 0.3, σ = 8.82 MeV/fm²
- **Falsification**: Derive f from first principles

### LAW-6: α-Cluster Binding
- **Statement**: Preformed α-clusters have n_eff = 4 (allowed)
- **Source**: DN-030..033
- **Status**: [I]
- **Implication**: α-decay preferred when clustering favorable
- **Falsification**: α-branching not correlated with N/Z

---

## Derived Invariants

### INV-1: Frustration Energy
- **Formula**: ε_f(n) = K × min(|n-36|, |n-48|)²
- **Source**: LAW-4, LAW-5
- **Status**: [Der]
- **Range**: ε_f ∈ [0, 33.84] MeV for n ∈ [37,47]

### INV-2: Distance to Allowed
- **Formula**: d(n) = min(d(36,n), d(48,n))
- **Source**: FT table
- **Status**: [Der]
- **Property**: d(n) = 0 for allowed n

### INV-3: Coordination from Mass Number [P]
- **Formula**: n(A) ≈ 6.1 × A^(1/3)
- **Source**: Candidate formula
- **Status**: [P]
- **Verification**: Compare to shell model predictions

---

## Conservation Laws

### CONS-1: n Monotonicity Along Chain
- **Statement**: d(n) decreases along decay chain toward stable isotope
- **Source**: Observed in U-238, Th-232, U-235 chains
- **Status**: [P]
- **Falsification**: Chain with increasing d(n)

### CONS-2: Mode Selection from d(n)
- **Statement**: α-decay preferred when n → allowed; β when n stable
- **Source**: GEN-3, branching observations
- **Status**: [P]
- **Falsification**: Branch ratios uncorrelated with d(n)

---

## Falsification Test Registry

| Test-ID | Law | Prediction | Threshold | Data Needed | Status |
|---------|-----|------------|-----------|-------------|--------|
| F-001 | LAW-1 | No stable n=7,11,13 | Any counter-example | Nuclear stability chart | Open |
| F-002 | LAW-2 | n_opt = 43±2 | |n_opt - 43| > 2 | Saturation curve | [I] |
| F-003 | LAW-3 | G-N R² > 0.95 | R² < 0.95 | α-emitter dataset | [I] |
| F-004 | LAW-4 | K ≈ 0.94 MeV | |K - 0.94| > 0.2 | Independent K | Open |
| F-005 | LAW-5 | f ≈ 0.3 | f derived ≠ 0.3 | Z₆ geometry | Open |
| F-006 | LAW-6 | α-branch ~ N/Z | No correlation | Branching data | Open |
| F-007 | INV-1 | ε_f(42) max | 42 not max | Frustration map | [Der] |
| F-008 | CONS-1 | d(n) monotonic | Counter-example | Chain analysis | [P] |
| F-009 | CONS-2 | Mode ~ d(n) | No correlation | Branching data | [P] |

---

## Hierarchy of Claims

### Tier 1: Derived [Der]
- LAW-1: Coordination selection (Z₆ origin)
- LAW-2: Saturation constraint (43 forbidden)
- LAW-4: Barrier formula (ΔV_eff)
- INV-1: Frustration energy (quadratic)

### Tier 2: Inferred [I]
- LAW-3: G-N + frustration (R² = 0.9941)
- LAW-5: Pinning constant (K formula)
- LAW-6: α-cluster binding (preformed)

### Tier 3: Proposed [P]
- INV-3: n(A) formula
- CONS-1: n monotonicity
- CONS-2: Mode selection rule
- M1-M6 mechanisms (escape routes)

---

## Upgrade Paths

| Claim | Current | Target | Requirement |
|-------|---------|--------|-------------|
| LAW-3 | [I] | [Der] | Derive ε_f(A) from first principles |
| LAW-5 | [Cal] | [Der] | Derive f from Z₆ geometry |
| INV-3 | [P] | [I] | Compare n(A) to shell model |
| CONS-1 | [P] | [I] | Verify on 10+ chains |
| CONS-2 | [P] | [I] | Branching ratio analysis |

---

## Summary

| Category | Count |
|----------|-------|
| Primary Laws | 6 |
| Derived Invariants | 3 |
| Conservation Laws | 2 |
| Falsification Tests | 9 |
| [Der] claims | 4 |
| [I] claims | 3 |
| [P] claims | 4 |
