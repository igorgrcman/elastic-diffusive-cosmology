# N48 ALLOWED SET AND GEOMETRY (V6)

**Created**: 2026-01-31
**Purpose**: Define allowed coordination set and local vs global interpretation
**Source**: V4 DN-001..005, 22826edd:2440-2540, 12444

---

## Allowed Coordination Set

### Definition [Der]
```
S = {n : n = 2^a × 3^b, a ≥ 0, b ≥ 0}
```

**Source**: DN-001, 22826edd:2440-2540

### Explicit Members
```
S = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, ...}
```

### Nuclear-Relevant Subset
For nuclei with A ∈ [4, 500]:
```
S_nuclear = {4, 6, 8, 12, 24, 36, 48, 72}
```

**Source**: DN-004, 22826edd:7307

---

## Z₆ Origin [Der]

The allowed set arises from Z₆ = Z₂ × Z₃ brane symmetry:
- Z₂ factor → powers of 2
- Z₃ factor → powers of 3
- Combined → products 2^a × 3^b

**Source**: DN-005, 22826edd:12444

---

## Distance Function

### Definition [Der]
For any n, the distance to allowed set is:
```
d(n) = min_{m ∈ S} |n - m|
```

### Properties
- d(n) = 0 iff n ∈ S
- For n ∈ [37, 47]: d(n) ∈ [1, 6]
- Maximum frustration: d(42) = 6 (equidistant from 36 and 48)

---

## V6: Local vs Global Coordination

### The Problem
The n(A) = c × A^(1/3) mapping gives:
- n(208) ≈ 36.2 (near allowed n=36)
- n(294) ≈ 40.6 (forbidden zone)
- n(488) ≈ 48.1 (near allowed n=48)

But nuclei with A ~ 250-350 have n(A) in [38, 44] — all forbidden.

**Question**: How do these nuclei exist as metastable entities?

### Resolution: Local Effective Coordination [P]

**Assumption AS-N48-005**: Effective coordination can be LOCAL (domain/cluster level), not global.

A nucleus may have:
1. **Global average n**: n_global = c × A^(1/3) — may be forbidden
2. **Local domain n**: n_local(i) — each domain has allowed n
3. **Effective n**: n_eff = function of local structure

### Three Interpretations

| Interpretation | n_eff Definition | Applicable When |
|----------------|------------------|-----------------|
| Global | n_eff = n(A) directly | Small nuclei, A < 100 |
| Domain Average | n_eff = Σ wᵢ nᵢ | Heavy nuclei with domains |
| Local Cluster | n_eff = 4 × n_α | α-clustered nuclei |

---

## Targets: n=36 vs n=48

### n=36 Island (Primary)
- Corresponds to A ~ 200-220 with c ≈ 6.1
- Pb-206, Pb-207, Pb-208 terminate here
- Shell closures Z=82, N=126 align

### n=48 Island (Secondary)
- Corresponds to A ~ 450-500 with c ≈ 6.1
- OR local n=48 in superheavy elements
- Predicted "island of stability" around Z=114, N=184

### Transition Zone
For A ∈ [230, 400]:
- Global n(A) ∈ [37, 45] — ALL forbidden
- Nucleus survives via:
  - M1: Domain mixing
  - M3: α-clusterization
  - M6: Core-mantle structure

---

## Geometry of Allowed Configurations

### Crystal Analog [I]

| n | Crystal Structure | Nuclear Analog |
|---|-------------------|----------------|
| 4 | Diamond | α-cluster core |
| 6 | Simple Cubic | Light nuclei |
| 8 | BCC | Pauli-limited |
| 12 | FCC/HCP | Close-packed |
| 24 | Complex | Extended shell |
| 36 | Superlattice | Pb-region |
| 48 | Hyperlattice | SHE-region |
| 72 | Extended | Theoretical limit |

**Source**: DN-050..058, 22826edd:2450, 16113

### Why n=48 is Special
- 48 = 2⁴ × 3 = 16 × 3 = largest practical allowed value below saturation
- Represents maximum stability for very heavy nuclei
- Crystal analog: 48-fold coordination in complex lattice

---

## Implications for Decay

### Toward n=36
Nuclei with n(A) > 36 but < 42:
- Decay reduces A → reduces n(A) → approaches 36
- Chain terminates when n ≈ 36

### Toward n=48
Nuclei with n(A) > 44:
- May be closer to n=48 than to n=36
- Especially if local n > n_global due to clustering

### Decision Boundary [P]
At n(A) = 42 (equidistant), both targets equally attractive.

For n(A) > 42: n=48 may be closer
For n(A) < 42: n=36 is closer

---

## Summary Table: Key n Values

| n | Status | Role | Example A |
|---|--------|------|-----------|
| 36 | Allowed | Primary target | 206-210 |
| 37-41 | Forbidden | Forbidden zone (low) | 220-260 |
| 42 | Forbidden | Maximum frustration | ~285 |
| 43 | Forbidden | Saturation optimum | ~300 |
| 44-47 | Forbidden | Forbidden zone (high) | 310-400 |
| 48 | Allowed | Secondary target | 450-500 |
