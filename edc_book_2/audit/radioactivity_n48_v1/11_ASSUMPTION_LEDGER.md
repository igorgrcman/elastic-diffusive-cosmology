# ASSUMPTION LEDGER (V6)

**Created**: 2026-01-31
**Purpose**: Track ALL [P] assumptions in N48 module
**Format**: AS-N48-XXX

---

## Ledger

### AS-N48-001: Coordination-Mass Mapping
- **Statement**: n(A) = c × A^(1/3) where c is a constant [P]
- **Range**: c ∈ [5.5, 8.0] (dimensionless)
- **Why Needed**: Maps mass number to effective coordination
- **Upgrade Path**: Derive c from nuclear radius r₀ × A^(1/3) and lattice geometry
- **Falsification**: If stable nuclei cluster at n values NOT near allowed set

### AS-N48-002: Coefficient c Default
- **Statement**: Default c = 6.1 for calculations [P]
- **Range**: Single value from middle of [5.5, 8.0]
- **Why Needed**: Produces n≈36 for Pb-208 (doubly magic)
- **Upgrade Path**: Calibrate against shell model or measured radii
- **Falsification**: If c = 6.1 fails to reproduce known stability patterns

### AS-N48-003: Frustration Energy Scaling
- **Statement**: ε_f(A) = k × d(n(A)) where k is dimensionless [P]
- **Range**: k ∈ [0.1, 2.0]
- **Why Needed**: Converts coordination distance to energy barrier
- **Upgrade Path**: Derive k from pinning constant K ≈ 0.94 MeV
- **Falsification**: If barrier heights uncorrelated with d(n)

### AS-N48-004: Frustration Coefficient k Default
- **Statement**: Default k = 0.94 (matching MeV pinning constant) [P]
- **Range**: Single value
- **Why Needed**: Dimensional consistency with LAW-4 barrier
- **Upgrade Path**: Derive from σ × contact area
- **Falsification**: If independent K measurement differs by >20%

### AS-N48-005: Local vs Global Coordination
- **Statement**: Effective n can be LOCAL (domain/cluster level), not global nucleus [P]
- **Range**: Local domain size ~ 10-50 nucleons
- **Why Needed**: Explains how n=48 can be relevant for A<300
- **Upgrade Path**: Show domain structure from imaging/spectroscopy
- **Falsification**: If no evidence of internal nuclear structure beyond shells

### AS-N48-006: Domain Mixing Weights
- **Statement**: n_eff = Σᵢ wᵢ × nᵢ with Σwᵢ = 1 [P]
- **Range**: wᵢ ∈ [0,1] per domain
- **Why Needed**: Mechanism M1 averaging formula
- **Upgrade Path**: Calculate weights from domain volume fractions
- **Falsification**: If no multi-domain structure observed

### AS-N48-007: Defect Correction to Coordination
- **Statement**: n_eff = n_bulk - ρ_defect × Δn_defect [P]
- **Range**: ρ_defect ∈ [0, 0.3], Δn_defect ∈ [1, 4]
- **Why Needed**: Mechanism M2 for defect-mediated n reduction
- **Upgrade Path**: Calculate from Y-junction density
- **Falsification**: If defects increase rather than decrease n_eff

### AS-N48-008: Alpha-Cluster n=4 Unit
- **Statement**: Each preformed α-cluster contributes n_local = 4 [P]
- **Range**: Exact value (4 nucleons per cluster)
- **Why Needed**: Mechanism M3; α = He-4 is allowed configuration
- **Upgrade Path**: This is nearly [Der] from α structure
- **Falsification**: If α-clustering doesn't produce n_eff = 4k

### AS-N48-009: Branching Channel Selection
- **Statement**: Preferred decay channel minimizes d(n(A_daughter)) [P]
- **Range**: N/A (binary choice)
- **Why Needed**: Hypothesis H-N48-01 for branching
- **Upgrade Path**: Test on 10+ branch points with real data
- **Falsification**: If branching uncorrelated with Δd(n)

### AS-N48-010: Core-Mantle Transition Mass
- **Statement**: Core-mantle (M6) becomes relevant for A > 250 [P]
- **Range**: A_threshold ∈ [200, 350]
- **Why Needed**: Explains superheavy element structure
- **Upgrade Path**: Spectroscopic evidence of layered structure
- **Falsification**: If SHE have uniform internal structure

### AS-N48-011: Half-Life Law Form
- **Statement**: log₁₀(t₁/₂) = a(Z/√Q) + b + c×ε_f [I/P]
- **Range**: a, b, c from G-N calibration (V4 DN-015..017)
- **Why Needed**: Connects coordination to observables
- **Upgrade Path**: Fully derive coefficients from 5D barrier
- **Falsification**: R² < 0.90 on actinide dataset

### AS-N48-012: Allowed Set Completeness
- **Statement**: S = {2^a × 3^b} is the COMPLETE allowed set [Der from V4]
- **Range**: N/A (mathematical)
- **Why Needed**: Foundation of entire framework
- **Upgrade Path**: Already [Der] in V4
- **Falsification**: Find stable configuration with n ∉ S

### AS-N48-013: n=48 as Second Target
- **Statement**: Heavy nuclei evolve toward n=48 rather than n=36 [P]
- **Range**: Applies for A > 280 approximately
- **Why Needed**: "Second island" concept
- **Upgrade Path**: Show decay chain endpoints cluster at n≈48
- **Falsification**: If all chains converge to n=36 regardless of A

### AS-N48-014: Metastable Coordination Freeze
- **Statement**: Isomeric states can have frozen n_eff ≠ ground state [P]
- **Range**: Δn_isomer ∈ [-2, +2]
- **Why Needed**: Mechanism M4 for anomalous branching
- **Upgrade Path**: Compare isomer vs ground state properties
- **Falsification**: If all isomers have same n as ground state

### AS-N48-015: Quasicrystal Exclusion
- **Statement**: Quasicrystalline n (irrational) not observed in nuclei [P]
- **Range**: N/A
- **Why Needed**: M5 remains speculative
- **Upgrade Path**: Search for 5-fold symmetry evidence
- **Falsification**: If quasicrystal signatures found

---

## Summary

| Category | Count |
|----------|-------|
| Mapping assumptions (AS-001..004) | 4 |
| Structure assumptions (AS-005..008) | 4 |
| Dynamics assumptions (AS-009..011) | 3 |
| Framework assumptions (AS-012..015) | 4 |
| **TOTAL** | **15** |

---

## Dependency Graph

```
AS-N48-012 (allowed set) [Der]
    |
    +---> AS-N48-001 (n(A) mapping) [P]
    |         |
    |         +---> AS-N48-002 (c default) [P]
    |         |
    |         +---> AS-N48-003 (ε_f scaling) [P]
    |                   |
    |                   +---> AS-N48-004 (k default) [P]
    |
    +---> AS-N48-005 (local vs global) [P]
              |
              +---> AS-N48-006 (domain mixing) [P]
              +---> AS-N48-007 (defect correction) [P]
              +---> AS-N48-008 (α-cluster unit) [P]

AS-N48-009 (branching) [P] ─┬─> H-N48-01
                            └─> Falsification tests

AS-N48-013 (n=48 target) [P] ─> Second island model
```
