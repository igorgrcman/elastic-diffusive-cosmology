# V7.8 SOURCES AND VERSIONS

**Created**: 2026-01-31
**Purpose**: Whitelist of approved data sources for V7.8

---

## Inherited from V7.4

| ID | Source | Content | Status |
|----|--------|---------|--------|
| S1 | NNDC/ENSDF | Nuclear structure, t₁/₂, Jπ | BL |
| S2 | NuDat3 | Q-values, branching ratios | BL |
| S3 | NUBASE2020 | Evaluated masses and halflives | BL |
| S4 | AME2020 | Atomic masses | BL |
| S5 | IAEA LiveChart | Decay data | BL |

---

## New Sources for V7.8

| ID | Source | Content | Access Date | Status |
|----|--------|---------|-------------|--------|
| S6 | FRDM2012 | β₂ deformation parameters | 2026-01-31 | [BL:PENDING] |
| S7 | Möller et al. 2016 | Theoretical β₂, masses | 2026-01-31 | [BL:PENDING] |
| S8 | RIPL-3 | Deformation, level density | 2026-01-31 | [BL:PENDING] |
| S9 | Buck et al. cluster model | S_α estimates | 2026-01-31 | [BL:PENDING] |
| S10 | Royer 2010 | α-preformation systematics | 2026-01-31 | [BL:PENDING] |

---

## Source Details

### S6: FRDM2012 (Finite Range Droplet Model)

**Reference**: P. Möller, J.R. Nix, W.D. Myers, W.J. Swiatecki, At. Data Nucl. Data Tables 59, 185 (1995); updated 2012
**URL**: https://t2.lanl.gov/nis/data/astro/molnix96/
**Content**: Ground-state deformations (β₂, β₄, β₆) for nuclei Z=8-130
**Format**: ASCII table with columns Z, N, β₂, β₄, ...
**Coverage**: Complete for actinides

### S7: Möller et al. 2016

**Reference**: Möller, Sierk, Ichikawa, Sagawa, At. Data Nucl. Data Tables 109-110, 1 (2016)
**Content**: Updated FRDM, includes β₂ for all nuclei in our dataset

### S8: RIPL-3

**Reference**: IAEA Reference Input Parameter Library
**URL**: https://www-nds.iaea.org/RIPL-3/
**Content**: Deformations, optical model parameters
**Coverage**: Good for actinides

### S9: Buck Cluster Model

**Reference**: Buck, Merchant, Perez, Phys. Rev. Lett. 72, 1326 (1994)
**Content**: α-cluster preformation factors from cluster model
**Coverage**: Limited to selected nuclei

### S10: Royer Preformation Systematics

**Reference**: Royer, J. Phys. G: Nucl. Part. Phys. 37, 015102 (2010)
**Content**: Empirical S_α formula: log₁₀(P_α) ≈ f(Z,N,A)
**Coverage**: Systematics applicable to all actinides

---

## Derived Proxies (No External Source Required)

### Proxy D1: N-Z Neutron Excess

**Definition**: N - Z = A - 2Z
**Source**: Derived from dataset columns A, Z
**Physical meaning**: Correlates with neutron skin thickness and deformation
**Status**: [Der]

### Proxy D2: (N-Z)/A Relative Asymmetry

**Definition**: (A - 2Z) / A
**Source**: Derived
**Physical meaning**: Normalized isospin asymmetry
**Status**: [Der]

### Proxy D3: Royer S_α Estimate

**Definition**: log₁₀(P_α) ≈ a + b×Z + c×A
**Source**: Royer 2010 formula applied to dataset
**Coefficients**: a = -0.127, b = 0.0148, c = -0.0122 (for actinides)
**Status**: [I] (formula from literature)

### Proxy D4: Shell Distance

**Definition**: |N - 126| + |Z - 82| (distance from doubly magic Pb-208)
**Source**: Derived
**Physical meaning**: Distance from shell closures affects deformation
**Status**: [Der]

---

## Data Availability Matrix

| Nuclide Range | β₂ (FRDM) | S_α (Buck) | E(2+) | N-Z | Royer P_α |
|---------------|-----------|------------|-------|-----|-----------|
| Po (Z=84) | Yes | Partial | Yes (ee) | Yes | Yes |
| At (Z=85) | Yes | No | No (odd) | Yes | Yes |
| Rn (Z=86) | Yes | Partial | Yes (ee) | Yes | Yes |
| Fr-Ra (Z=87-88) | Yes | No | Partial | Yes | Yes |
| Ac-Th (Z=89-90) | Yes | Partial | Partial | Yes | Yes |
| Pa-U (Z=91-92) | Yes | Yes | Yes | Yes | Yes |
| Np-Pu (Z=93-94) | Yes | Yes | Yes | Yes | Yes |
| Am-Cm (Z=95-96) | Yes | Yes | Yes | Yes | Yes |
| Bk-Cf (Z=97-98) | Yes | Partial | Partial | Yes | Yes |
| Es-Fm (Z=99-100) | Yes | No | No | Yes | Yes |

---

## Priority for V7.8

**Primary proxy (deformation)**: Use Royer-derived or (N-Z)/A as available proxy; β₂ from FRDM if obtainable.

**Primary proxy (S_α)**: Use Royer formula (D3) as systematic proxy applicable to all nuclides.

**Fallback**: If external data unavailable, use derived proxies D1-D4 which require no external lookup.

