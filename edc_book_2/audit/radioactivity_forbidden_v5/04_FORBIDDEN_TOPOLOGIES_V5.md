# FORBIDDEN TOPOLOGIES V5

**Created**: 2026-01-31
**Purpose**: Enhanced FT table with M1-M6 mechanisms and falsification tests
**Inherits**: V4 FT-37..47

---

## Coordination Law (LAW-1)

**Statement**: n is ALLOWED iff n = 2^a × 3^b (a,b ≥ 0)

**Source**: DN-001..005, 22826edd:2440-2540, 12444

**Origin**: Z₆ = Z₂ × Z₃ brane symmetry from hexagonal lattice

---

## Forbidden Zone Table

| FT-ID | n | Prime Factorization | Why Forbidden | d(36) | d(48) | Mechanism |
|-------|---|---------------------|---------------|-------|-------|-----------|
| FT-37 | 37 | prime | Prime > 3 | 1 | 11 | M1/M2 |
| FT-38 | 38 | 2×19 | 19 > 3 | 2 | 10 | M1/M2 |
| FT-39 | 39 | 3×13 | 13 > 3 | 3 | 9 | M1/M2 |
| FT-40 | 40 | 2³×5 | 5 > 3 | 4 | 8 | M1/M3 |
| FT-41 | 41 | prime | Prime > 3 | 5 | 7 | M1/M2 |
| FT-42 | 42 | 2×3×7 | 7 > 3 | 6 | 6 | M1/M4 [MAX] |
| FT-43 | 43 | prime | Prime > 3 | 7 | 5 | M1/M2 [SAT] |
| FT-44 | 44 | 2²×11 | 11 > 3 | 8 | 4 | M3/M5 |
| FT-45 | 45 | 3²×5 | 5 > 3 | 9 | 3 | M3/M6 |
| FT-46 | 46 | 2×23 | 23 > 3 | 10 | 2 | M3/M6 |
| FT-47 | 47 | prime | Prime > 3 | 11 | 1 | M6 |

**Key**:
- d(36) = |n - 36|, d(48) = |n - 48|
- [MAX] = Maximum frustration (equidistant from 36,48)
- [SAT] = Near nuclear saturation optimum (n_opt ≈ 43.3)

---

## Mechanism Catalog

### M1: Domain Mixing [I]
- **Source**: DN-040, 22826edd:2479-2492
- **State Variable**: φ_domain(r) = boundary mixing order parameter
- **n_eff Modification**: n_eff = Σᵢ wᵢ × nᵢ (weighted average)
- **ε_f Scaling**: ε_f(mix) < ε_f(pure)
- **Decay Mode**: Favors α (lower barrier)
- **Observable**: Anisotropic α-emission
- **Falsification**: Measure angular distribution; isotropic → exclude M1

### M2: Defects [P]
- **Source**: DN-041..042, 73d92ff5:517-530, 22826edd:41
- **State Variable**: ρ_defect = defect density (Y-junctions, walls)
- **n_eff Modification**: n_eff = n_bulk - Δn_defect
- **ε_f Scaling**: ε_f → ε_f × (1 - f_defect)
- **Decay Mode**: Mixed (defect-mediated tunneling)
- **Observable**: Lifetime anomalies in isomers
- **Falsification**: Compare ground-state vs isomer lifetimes

### M3: α-Clusterization [I]
- **Source**: DN-043..044, 22826edd:2450-2478
- **State Variable**: n_cluster = number of preformed α-clusters
- **n_eff Modification**: n_eff = 4 × n_cluster (α = n=4 allowed)
- **ε_f Scaling**: ε_f(α) = 0 for preformed cluster
- **Decay Mode**: α only
- **Observable**: Enhanced α-branching for N=Z nuclei
- **Falsification**: Measure α-branching vs N/Z ratio

### M4: Metastable [P]
- **Source**: DN-045, 73d92ff5:442-450
- **State Variable**: ΔG_meta = metastable free energy excess
- **n_eff Modification**: n_eff frozen at formation value
- **ε_f Scaling**: ε_f time-dependent
- **Decay Mode**: Delayed (isomeric transition first)
- **Observable**: Isomer ratios, delayed γ
- **Falsification**: Map isomer systematics

### M5: Quasicrystal [P]
- **Source**: DN-046 (no direct source - proposed)
- **State Variable**: τ = quasiperiodicity parameter
- **n_eff Modification**: n_eff = f(τ) irrational
- **ε_f Scaling**: ε_f undefined (aperiodic)
- **Decay Mode**: Novel (cluster emission?)
- **Observable**: New decay modes
- **Falsification**: Search for exotic emissions in heavy nuclei

### M6: Core-Mantle [P]
- **Source**: DN-047..048, 22826edd:4847-4925
- **State Variable**: R_core/R_total = core fraction
- **n_eff Modification**: n_eff = α × n_core + (1-α) × n_mantle
- **ε_f Scaling**: ε_f = ε_f(core) + ε_f(interface)
- **Decay Mode**: Depends on α-cluster location
- **Observable**: Charge radius anomalies
- **Falsification**: Compare measured vs predicted radii

---

## Beyond M43 Question (D-V5-003)

**Question**: Can heavy nuclides form structures besides M43 and forbidden 44-47?

**Answer**:

| Structure | Condition | Predicted Signature |
|-----------|-----------|---------------------|
| n=36 | A < 200 stable | Closed shell behavior |
| n=48 | A > 250 actinides | Maximum stability |
| n=42 | Any A | Maximum frustration, rapid decay |
| n=43 | A ~ 200 | Saturation optimum, forbidden |
| Mixed (M1) | Heavy actinides | Anisotropic emission |
| Core-mantle (M6) | SHE (Z > 100) | Shell-like + continuum |

**Discriminants**:
1. If Q_α < 6 MeV AND t₁/₂ > 10⁶ yr → n near 36 or 48
2. If Q_α > 8 MeV AND t₁/₂ < 1 μs → n in [40,44]
3. If α-anisotropy > 10% → M1 active
4. If isomer ratio anomalous → M4 active

---

## Falsification Test Registry

| Test-ID | Claim | Test | Threshold | Status |
|---------|-------|------|-----------|--------|
| FT-TEST-001 | n=2^a×3^b only | Find stable n=7,11 | Any example | Open |
| FT-TEST-002 | n≈43 optimal | Measure saturation curve | n_opt ≠ 43±2 | [I] |
| FT-TEST-003 | G-N + ε_f | R² on actinides | R² < 0.95 | [I] |
| FT-TEST-004 | M1 mixing | α-anisotropy | Aniso > 5% | Open |
| FT-TEST-005 | M3 clustering | α-branch vs N/Z | Correlation r < 0.8 | Open |
| FT-TEST-006 | K ≈ 0.94 MeV | Independent K measure | |K - 0.94| > 0.2 | Open |

---

## Summary

| Metric | Count |
|--------|-------|
| Forbidden n values | 11 (FT-37..47) |
| Mechanisms | 6 (M1-M6) |
| [I] mechanisms | 2 (M1, M3) |
| [P] mechanisms | 4 (M2, M4, M5, M6) |
| Falsification tests | 6 |
