# FORBIDDEN ALTERNATIVES BEYOND M43 (V7.7)

**Created**: 2026-01-31
**Purpose**: Systematically catalog n ∈ [37,47] mechanisms excluding M43 storyline
**Status**: [I]/[P] by mechanism

---

## Overview

The M43 case (n = 43, nuclear saturation optimum) receives special attention in EDC. This document catalogs **all other forbidden n** with their mechanisms.

---

## Complete Forbidden Zone Table

| n | Prime Factorization | d(36) | d(48) | d_min | Closest Allowed | Primary Mechanism |
|---|---------------------|-------|-------|-------|-----------------|-------------------|
| 37 | 37 (prime) | 1 | 11 | 1 | 36 | M1/M2 |
| 38 | 2×19 | 2 | 10 | 2 | 36 | M1/M2 |
| 39 | 3×13 | 3 | 9 | 3 | 36 | M1/M2 |
| 40 | 2³×5 | 4 | 8 | 4 | 36 | M1/M3 |
| 41 | 41 (prime) | 5 | 7 | 5 | 36 | M1/M2 |
| 42 | 2×3×7 | 6 | 6 | 6 | Either | M1/M4 [MAX] |
| ~~43~~ | ~~43 (prime)~~ | ~~7~~ | ~~5~~ | ~~5~~ | ~~48~~ | ~~[Excluded]~~ |
| 44 | 2²×11 | 8 | 4 | 4 | 48 | M3/M5 |
| 45 | 3²×5 | 9 | 3 | 3 | 48 | M3/M6 |
| 46 | 2×23 | 10 | 2 | 2 | 48 | M3/M6 |
| 47 | 47 (prime) | 11 | 1 | 1 | 48 | M6 |

**[MAX]** = Maximum frustration (equidistant from 36 and 48)

---

## Mechanism × n Matrix

| n | M1 Domain | M2 Defect | M3 α-Cluster | M4 Metastable | M5 Quasi | M6 Core-Mantle |
|---|-----------|-----------|--------------|---------------|----------|----------------|
| 37 | **Primary** | Secondary | — | — | — | — |
| 38 | **Primary** | Secondary | — | — | — | — |
| 39 | **Primary** | Secondary | Possible | — | — | — |
| 40 | Secondary | — | **Primary** | — | — | — |
| 41 | Secondary | **Primary** | Possible | — | — | — |
| 42 | **Primary** | — | — | Secondary | — | — |
| 44 | — | — | **Primary** | — | Possible | — |
| 45 | — | — | **Primary** | — | — | Secondary |
| 46 | — | — | Secondary | — | — | **Primary** |
| 47 | — | — | — | — | — | **Primary** |

---

## Detailed Mechanism Analysis

### n = 37: Near-Boundary [I]

**Position**: Just outside allowed 36
**d_min**: 1 (very close)
**Primary mechanism**: M1 (domain mixing)

**Construction**:
```
n_eff = 0.917 × 36 + 0.083 × 48 = 37.0
```
Interpretation: Mostly 36-like with 8% 48-like domains.

**Secondary**: M2 (single defect per 36 sites)
```
n_eff = 36 + 1/36 coordination deficiency ≈ 37
```

**Observable**:
- α-decay rate slightly faster than n=36 prediction
- Possible weak anisotropy

**Falsification**: If t₁/₂ matches pure n=36 → mechanisms inactive

---

### n = 38: Domain Mix [I]

**Position**: 2 units from 36
**Primary mechanism**: M1

**Construction**:
```
n_eff = 0.833 × 36 + 0.167 × 48 = 38.0
```
~17% of volume in 48-like domains.

**Observable**:
- Enhanced α-rate (higher S_α from frustration)
- Possible bimodal Q-value spectrum

**Falsification**: If Q-spectrum is unimodal → single domain

---

### n = 39: Mixed Regime [I]

**Position**: 3 units from 36
**Primary mechanism**: M1 with M3 contribution

**Construction**:
```
n_eff = 0.75 × 36 + 0.25 × 48 = 39.0
```
Quarter of volume in 48-like domains, or:
```
n_eff = 6 × 6.5 (cluster-cluster coordination shift)
```

**Observable**:
- Strong α-preference (M3 clustering)
- d(n) = 3 gives 10^(0.31×3) ≈ 8× S_α enhancement

---

### n = 40: α-Clusterization [I]

**Position**: 4 units from 36
**Primary mechanism**: M3

**Rationale**:
- 40 = 2³ × 5 contains factor 5 (outside {2,3})
- But 40 = 10 × 4 suggests clustering of α-particles
- Each α has internal n = 4 (allowed)

**Construction**:
```
10 α-clusters with inter-cluster coordination
n_cluster = 4 (internal), n_external varies
```

**Observable**:
- Strong α-decay preference
- High α-branching ratio

**Falsification**: If α-branching < 50% → M3 disfavored

---

### n = 41: Deep Forbidden [P]

**Position**: 5 units from 36 (approaching center)
**Primary mechanism**: M2 (defects in 48-like base)

**Rationale**:
- 41 is prime (no decomposition)
- Could be 48 - 7 defects

**Construction**:
```
n_eff = 48 - 7 (defect coordination loss)
```

**Observable**:
- Short-lived (high frustration ε_f)
- Rapid α or exotic decay

---

### n = 42: Maximum Frustration [I]

**Position**: Equidistant from 36 and 48
**d_min**: 6 (maximum in zone)
**Primary mechanism**: M1 (50/50 domain mix)

**Construction**:
```
n_eff = 0.5 × 36 + 0.5 × 48 = 42.0
```
Equal volumes of 36-like and 48-like domains.

**Observable**:
- Very short-lived (maximum ε_f)
- Strong domain boundary effects
- Possibly mixed decay modes

**Special status**: M4 (metastable) also possible — frozen non-equilibrium configuration.

---

### n = 44: Approaching 48 [I]

**Position**: 4 units from 48
**Primary mechanism**: M3 (α-clusterization)

**Rationale**:
- 44 = 4 × 11 suggests 11 α-clusters
- Moving toward 48-like stability

**Construction**:
```
11 α-clusters with tightening packing
n_cluster = 4, n_intercluster → 48/11 ≈ 4.4
```

**Observable**:
- β⁻ decay preferred (move toward N-rich, approach 48)
- Moderate α-branching

---

### n = 45: Near 48 [I]

**Position**: 3 units from 48
**Primary mechanism**: M3 with M6

**Rationale**:
- 45 = 9 × 5 = 3² × 5
- Close to 48, could have core-mantle structure

**Construction**:
```
Core: n = 48 (stable)
Mantle: n ≈ 36-40 (frustrated surface)
Weighted average: 45
```

**Observable**:
- Longer-lived than 42-44
- Possible charge radius anomaly

---

### n = 46: Near-Boundary to 48 [P]

**Position**: 2 units from 48
**Primary mechanism**: M6 (core-mantle)

**Construction**:
```
Core: n = 48
Surface layer: n < 48
```
Core-dominated with frustrated surface.

**Observable**:
- Long-lived (approaching stability)
- β⁻ preferred

---

### n = 47: Almost Allowed [P]

**Position**: 1 unit from 48
**Primary mechanism**: M6

**Construction**:
```
n_eff = 48 - 1 (minimal surface frustration)
```

**Observable**:
- Longest-lived in forbidden zone (after 37)
- β⁻ strongly preferred

**Falsification**: If t₁/₂ doesn't match n=48 trend → surface effect significant

---

## Decay Mode Predictions

| n | d_min | Direction | Predicted Primary Mode | Reasoning |
|---|-------|-----------|------------------------|-----------|
| 37 | 1 | → 36 | α or β⁺/EC | Small jump, α possible |
| 38 | 2 | → 36 | β⁺/EC | Decrease N/Z toward 36 |
| 39 | 3 | → 36 | α or β⁺/EC | Medium jump |
| 40 | 4 | → 36 | α | Large jump, favor α |
| 41 | 5 | → 36 | α | Favor α clustering |
| 42 | 6 | Either | Mixed | Transition point |
| 44 | 4 | → 48 | β⁻ | Increase N toward 48 |
| 45 | 3 | → 48 | β⁻ | Increase N toward 48 |
| 46 | 2 | → 48 | β⁻ | Almost at 48 |
| 47 | 1 | → 48 | β⁻ | One step from 48 |

---

## Falsification Conditions by Mechanism

| Mechanism | Test | Rejection Criterion |
|-----------|------|---------------------|
| M1 Domain | α-anisotropy measurement | Isotropic emission |
| M2 Defect | τ vs defect density | No correlation |
| M3 α-Cluster | α-branch vs N/Z | No correlation |
| M4 Metastable | Isomer spectroscopy | No isomer signatures |
| M5 Quasi | Exotic emission search | None found |
| M6 Core-Mantle | Charge radius measurement | Normal radii |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Forbidden n analyzed | 10 (excl. 43) |
| With M1 as primary | 4 (37, 38, 39, 42) |
| With M3 as primary | 3 (40, 44, 45) |
| With M6 as primary | 2 (46, 47) |
| With M2 as primary | 1 (41) |
| Falsification tests defined | 6 |

