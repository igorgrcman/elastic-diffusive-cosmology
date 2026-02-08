# BULK CRYSTAL NUCLEI MODELS V5

**Created**: 2026-01-31
**Purpose**: Map crystal structures to nuclear coordination
**Source**: DN-050..058, 22826edd:2450, 11337, 11684, 16113

---

## Crystal Coordination Table

| Crystal | n | Formula | Allowed? | Nuclear Analog | Notes |
|---------|---|---------|----------|----------------|-------|
| Diamond | 4 | 2² | YES | α-cluster core | He-4 building block |
| Simple Cubic | 6 | 2×3 | YES | Light nuclei | Li-6, C-12 |
| BCC | 8 | 2³ | YES | Pauli limit | Shell closure |
| FCC/HCP | 12 | 2²×3 | YES | Close packing | Magic numbers |
| Complex | 24 | 2³×3 | YES | Extended shell | Ni-78 |
| Superlattice | 36 | 2²×3² | YES | Actinide target | Near Pb-208 |
| Hyperlattice | 48 | 2⁴×3 | YES | SHE target | Island of stability |
| Quasicrystal | τ(5-fold) | Irrational | NO | M5 mechanism | Not observed |

---

## n-Rule Application

### Rule Statement [Der]
For stable nuclear configuration: n = 2^a × 3^b

### Crystal → Nucleus Mapping

| Crystal Family | a | b | n | Nuclear Example |
|----------------|---|---|---|-----------------|
| Diamond-like | 2 | 0 | 4 | ⁴He (α-particle) |
| SC-like | 1 | 1 | 6 | ⁶Li, ¹²C (3α) |
| BCC-like | 3 | 0 | 8 | ⁸Be (unstable) |
| FCC/HCP-like | 2 | 1 | 12 | ¹²C, ²⁴Mg |
| Extended-1 | 3 | 1 | 24 | ⁴⁸Ca, ⁷⁸Ni |
| Extended-2 | 2 | 2 | 36 | Light actinides |
| Extended-3 | 4 | 1 | 48 | Heavy actinides |
| Extended-4 | 3 | 2 | 72 | Superheavy |

---

## Hexagonal Lattice Origin

**Source**: DN-057, 22826edd:12444

The Z₆ = Z₂ × Z₃ symmetry originates from hexagonal lattice geometry:
- Z₂: Binary reflection symmetry
- Z₃: Ternary rotation symmetry
- Combined: 6-fold symmetry of hexagonal close packing

This constrains allowed coordination to:
n ∈ {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, ...}

Practically relevant for nuclei: {4, 6, 8, 12, 24, 36, 48, 72}

---

## Frustration Gradient

### Concept [Der]
Frustration energy ε_f(n) increases with distance from allowed values.

For forbidden n in [37,47]:
```
ε_f(n) = K × min(d(36,n), d(48,n))²
```

where K ≈ 0.94 MeV is the pinning constant.

### Frustration Table

| n | d(36) | d(48) | min(d) | ε_f (MeV) |
|---|-------|-------|--------|-----------|
| 37 | 1 | 11 | 1 | 0.94 |
| 38 | 2 | 10 | 2 | 3.76 |
| 39 | 3 | 9 | 3 | 8.46 |
| 40 | 4 | 8 | 4 | 15.04 |
| 41 | 5 | 7 | 5 | 23.50 |
| 42 | 6 | 6 | 6 | 33.84 |
| 43 | 7 | 5 | 5 | 23.50 |
| 44 | 8 | 4 | 4 | 15.04 |
| 45 | 9 | 3 | 3 | 8.46 |
| 46 | 10 | 2 | 2 | 3.76 |
| 47 | 11 | 1 | 1 | 0.94 |

Note: n=42 has MAXIMUM frustration (equidistant from both targets).

---

## M6 Topological Model

**Source**: DN-025, 22826edd:11684

The M6 model uses n=6 local coordination with global topology from domain structure.

### Key Parameters
- Local: n_local = 6 (SC-like)
- Global: n_effective = f(topology)
- Interface: Domain wall energy τ×L

### Pinning Constant Derivation
From DN-023..026:
```
K = f × σ × A
```
where:
- f ≈ 0.3 (geometric factor from Z₆)
- σ = 8.82 MeV/fm² (surface tension)
- A = effective contact area

---

## Circle Packing Connection

**Source**: DN-056, 22826edd:16113

2D circle packing coordination numbers:
- Hexagonal: n = 6 (optimal)
- Square: n = 4
- Random: n ~ 5.5

The optimal 2D value n=6 maps to Z₆ symmetry origin.

Extension to 3D:
- Random close packing: n ~ 8.5
- FCC/HCP: n = 12
- BCC: n = 8

All allowed by n = 2^a × 3^b rule.

---

## Y-Junction Lattice

**Source**: DN-053, 22826edd:11337

Dual Y-junction lattice has:
- 3 domains per junction
- 120° angles (Steiner-optimal)
- Domain wall tension τ

Nuclear application:
- α-decay: 3-body final state constraint
- β-decay: Junction reconfiguration
- Fission: Multiple junction breaking

---

## Local vs Lattice Coordination

**Source**: DN-055, 22826edd:15540

Distinction between:
1. **Local coordination**: Nearest-neighbor count for single nucleon
2. **Lattice coordination**: Average coordination in periodic structure

Nuclear relevance:
- Surface nucleons: n_local < n_lattice
- Core nucleons: n_local ≈ n_lattice
- Cluster nucleons: n_local = 4 (α-cluster)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Crystal families mapped | 8 |
| Allowed n values (practical) | 8 |
| Forbidden zone size | 11 (37-47) |
| Maximum frustration | n=42 |
| Key donors used | 9 (DN-050..058) |
