# CRYSTAL DEFECT ANALOGY (V7.7)

**Created**: 2026-01-31
**Purpose**: Map bulk crystal concepts → nuclear α-decay
**Status**: [I] for mapping, [P] for mechanism

---

## Core Analogy

| Crystal Concept | Nuclear Analog | Mapping Quality |
|-----------------|----------------|-----------------|
| Coordination number n | M-topology n(A) | [Der] |
| Allowed coordinations | n = 2^a × 3^b | [Der] |
| Lattice defects | Deviation from allowed n | [I] |
| Defect-enhanced diffusion | Frustration-enhanced S_α | [P] |
| Grain boundary | Domain wall (M1) | [I] |
| Vacancy | Missing coordination (M2) | [P] |
| Strain field | Frustration energy ε_f | [I] |

---

## Crystal Coordination Systems

### From V5 Crystal Models [Der]

| Crystal | n | Formula | Allowed? |
|---------|---|---------|----------|
| Diamond | 4 | 2² | YES |
| Simple Cubic | 6 | 2×3 | YES |
| BCC | 8 | 2³ | YES |
| FCC/HCP | 12 | 2²×3 | YES |
| Complex | 24 | 2³×3 | YES |
| Superlattice | 36 | 2²×3² | YES |
| Hyperlattice | 48 | 2⁴×3 | YES |

### Non-Allowed (Quasicrystals)

| System | n | Status |
|--------|---|--------|
| Penrose tiling | τ (irrational) | Forbidden |
| Icosahedral | 12 (but 5-fold) | Marginal |

---

## Defect Physics Parallel

### In Crystals [Der]

**Observation**: Defects (vacancies, dislocations, grain boundaries) generally **enhance** atomic mobility, not reduce it.

| Defect Type | Effect on Diffusion | Mechanism |
|-------------|---------------------|-----------|
| Vacancy | Enhanced | Easier hopping |
| Dislocation | Enhanced | Pipe diffusion |
| Grain boundary | Enhanced | Fast paths |
| Strain field | Enhanced | Lowered activation |

### In Nuclei [P]

**Proposed parallel**: Frustration (deviation from allowed n) enhances α-preformation.

| Nuclear "Defect" | Effect on S_α | Proposed Mechanism |
|------------------|---------------|-------------------|
| d(n) > 0 | Enhanced | Surface reorganization |
| Domain boundaries (M1) | Enhanced | Cluster nucleation sites |
| Structural strain | Enhanced | Lower formation barrier |

---

## Quantitative Scaling (Order of Magnitude)

### Crystal Defect Diffusion

Typical enhancement factor:
```
D_defect / D_bulk ≈ 10² - 10⁶
```
depending on defect type and temperature.

### Nuclear S_α Enhancement

From g = 0.31 per unit d:
```
S_α(d=3) / S_α(d=0) ≈ 10^(0.31×3) ≈ 8
```

**Comparison**: Nuclear enhancement (factor ~10) is at the low end of crystal defect enhancement (10²-10⁶).

**Interpretation**: Either:
1. Nuclear "defects" are weaker than crystal defects
2. S_α is already partially saturated
3. Analogy is qualitative, not quantitative

---

## Domain Wall / Grain Boundary Parallel

### Crystal Grain Boundaries [Der]

- High-energy interfaces
- Accumulate impurities
- Sites for nucleation
- Enhance diffusion along boundary

### Nuclear Domain Walls (M1) [I]

From V5 04_FORBIDDEN_TOPOLOGIES:
- φ_domain(r) = boundary mixing order parameter
- n_eff = Σᵢ wᵢ × nᵢ (weighted average across domains)
- Boundary energy adds to ε_f

**Proposed parallel**:
- Domain walls are high-energy surfaces
- α-clusters preferentially form at domain boundaries
- This enhances S_α

---

## Y-Junction Network

### Crystal Y-Junctions [Der]

From V5 05_BULK_CRYSTAL_NUCLEI_MODELS:
- Steiner-optimal 120° angles
- 3 domains per junction
- Tension τ along walls

### Nuclear Y-Junctions [I]

- 3-body final state constraint (α + daughter + recoil)
- Junction reconfiguration during decay
- α emission at Y-junction vertex

---

## Where Analogy Can Fail

### Failure Mode 1: Quantum Effects

**Crystal**: Classical diffusion, thermal activation
**Nucleus**: Quantum tunneling, zero-point motion

**Risk**: Quantum coherence may invalidate classical defect picture.

**Test**: If S_α shows temperature dependence → classical contribution exists.

### Failure Mode 2: Scale Mismatch

**Crystal**: 10⁸ - 10²³ atoms
**Nucleus**: 100-300 nucleons

**Risk**: Finite-size effects dominate; "bulk" concepts may not apply.

**Test**: If S_α effect disappears for A < 100 → scale matters.

### Failure Mode 3: Bonding Type

**Crystal**: Electromagnetic bonds (covalent, ionic, metallic)
**Nucleus**: Strong force (short-range, saturating)

**Risk**: Strong force saturation means "coordination" works differently.

**Test**: Compare light (surface-dominated) vs heavy (volume-dominated) nuclei.

### Failure Mode 4: Defect Stability

**Crystal**: Defects are metastable, can anneal
**Nucleus**: "Defects" may be instantaneous configurations

**Risk**: Nuclear configurations too transient for defect concept.

**Test**: If isomers show different d(n) correlation → configuration matters.

### Failure Mode 5: No Lattice Periodicity

**Crystal**: Periodic lattice defines coordination
**Nucleus**: Liquid drop / shell model, no strict periodicity

**Risk**: "Coordination" in nucleus is statistical average, not geometric.

**Test**: If shell closure modifies d(n) effect → periodicity analog exists.

---

## Falsification Tests

| Test-ID | Claim | Observable | Threshold |
|---------|-------|------------|-----------|
| CDA-01 | Defects enhance dynamics | S_α vs d(n) | r > 0.5 |
| CDA-02 | Grain boundary nucleation | α-anisotropy | > 5% |
| CDA-03 | Strain field effect | ε_f correlates with t₁/₂ residual | r > 0.3 |
| CDA-04 | Scale independence | Effect persists A < 200 | g still significant |
| CDA-05 | Not purely quantum | T-dependence of S_α | Some T-dependence |

---

## Summary

| Aspect | Crystal | Nucleus | Mapping Status |
|--------|---------|---------|----------------|
| Coordination | Well-defined | n(A) proxy | [Der] |
| Allowed values | Crystallographic | 2^a × 3^b | [Der] |
| Defect = frustration | Yes | Proposed | [P] |
| Defects enhance dynamics | Yes | Proposed | [P] |
| Quantitative match | — | Factor ~10 vs 10²-10⁶ | Qualitative only |

**Verdict**: Crystal analogy provides useful intuition but should not be pushed quantitatively. Key testable prediction: frustration enhances rather than impedes decay dynamics.

