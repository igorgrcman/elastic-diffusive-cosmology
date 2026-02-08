# BULK CRYSTAL STRUCTURES: Allowed vs Forbidden Lattices

**Created**: 2026-01-31
**Purpose**: Crystal add-on for M-topology coordination analysis
**Citation**: DN-040, DN-041 from DONOR_TRACEBACK.md

---

## Coordination Law Applied to Crystals

### LAW-1 Recap [Der]
```
n is ALLOWED iff n = 2^a × 3^b
```

**Allowed coordination numbers**: 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, ...

**Forbidden**: 5, 7, 10, 11, 13, 14, 15, 17, 19, 20, 21, 22, 23, ...

---

## Part A: Standard Crystal Structures

### A1: Simple Cubic (SC)

| Property | Value | Status |
|----------|-------|--------|
| Coordination | n = 6 | ALLOWED (2 × 3) |
| Space group | Pm-3m | |
| Packing efficiency | 52% | |
| Examples | Po (α), CsCl-type | |

**EDC Status**: ✓ Topologically allowed

---

### A2: Body-Centered Cubic (BCC)

| Property | Value | Status |
|----------|-------|--------|
| Coordination | n = 8 | ALLOWED (2³) |
| Space group | Im-3m | |
| Packing efficiency | 68% | |
| Examples | Fe, Cr, W, Na, K | |

**EDC Status**: ✓ Topologically allowed

---

### A3: Face-Centered Cubic (FCC)

| Property | Value | Status |
|----------|-------|--------|
| Coordination | n = 12 | ALLOWED (4 × 3 = 2² × 3) |
| Space group | Fm-3m | |
| Packing efficiency | 74% | |
| Examples | Cu, Al, Au, Ag, Pb | |

**EDC Status**: ✓ Topologically allowed

**Note**: Maximum packing efficiency for spheres (with HCP)

---

### A4: Hexagonal Close-Packed (HCP)

| Property | Value | Status |
|----------|-------|--------|
| Coordination | n = 12 | ALLOWED (2² × 3) |
| Space group | P6₃/mmc | |
| Packing efficiency | 74% | |
| Examples | Mg, Zn, Ti, Co | |

**EDC Status**: ✓ Topologically allowed

---

### A5: Diamond Cubic

| Property | Value | Status |
|----------|-------|--------|
| Coordination | n = 4 | ALLOWED (2²) |
| Space group | Fd-3m | |
| Packing efficiency | 34% | |
| Examples | C (diamond), Si, Ge | |

**EDC Status**: ✓ Topologically allowed

---

### A6: Graphite (2D layers)

| Property | Value | Status |
|----------|-------|--------|
| In-plane coordination | n = 3 | ALLOWED (3) |
| 3D coordination | n = 3 (weak interlayer) | |
| Examples | C (graphite), BN | |

**EDC Status**: ✓ Topologically allowed

---

## Part B: Forbidden Coordinations

### B1: n = 5 (Pentagon-based)

**Status**: FORBIDDEN (5 is prime > 3)

**Where it appears**:
- Icosahedral local order (liquids, glasses)
- Quasicrystals (5-fold symmetry)
- Fullerenes (C₆₀ has pentagons)

**Consequence [P]**:
- Cannot form periodic crystal with n = 5 everywhere
- Pentagons require topological defects to tile
- Frank-Kasper phases avoid pure n = 5

---

### B2: n = 7 (Heptagon-based)

**Status**: FORBIDDEN (7 is prime > 3)

**Where it appears**:
- Defects in graphene (Stone-Wales)
- Grain boundaries
- Negative curvature surfaces

**Consequence [P]**:
- Heptagons destabilize planar structures
- Pair with pentagons to maintain average n = 6

---

### B3: n = 10

**Status**: FORBIDDEN (10 = 2 × 5)

**Where it might appear**:
- No standard crystal structure
- Some molecular crystals?

---

### B4: n = 11

**Status**: FORBIDDEN (11 is prime > 3)

**Physical occurrence**: Very rare, no standard crystal

---

## Part C: Coordination Summary Table

| n | Factorization | Status | Crystal Examples |
|---|---------------|--------|------------------|
| 3 | 3 | ALLOWED | Graphite (in-plane) |
| 4 | 2² | ALLOWED | Diamond, Si, Ge |
| 5 | 5 | FORBIDDEN | (local order only) |
| 6 | 2 × 3 | ALLOWED | SC, graphite |
| 7 | 7 | FORBIDDEN | (defects only) |
| 8 | 2³ | ALLOWED | BCC metals |
| 9 | 3² | ALLOWED | (rare, some borides) |
| 10 | 2 × 5 | FORBIDDEN | (no crystal) |
| 11 | 11 | FORBIDDEN | (no crystal) |
| 12 | 2² × 3 | ALLOWED | FCC, HCP (most metals) |

---

## Part D: Quasicrystals [P]

### The 5-fold Problem

Quasicrystals (discovered 1984, Nobel 2011) exhibit:
- 5-fold, 10-fold rotational symmetry
- No translational periodicity
- Local n = 5 coordination (icosahedral)

**EDC Interpretation [P]**:
- Quasicrystals exist in "topologically forbidden" regime
- Stabilized by electronic effects (Hume-Rothery rules)
- Not true ground state? Metastable?

**Open question**: Does EDC predict quasicrystal instability?

---

### Penrose Tiling Analogy

Penrose tilings (2D quasicrystal analog):
- Use two tile types with specific matching rules
- No periodic repeat
- Average coordination involves 5-fold vertices

**EDC Hypothesis [P]**:
- Penrose tiling = "frustrated" 2D structure
- Requires long-range order to avoid forbidden local n
- Stability from entropy? Electronic stabilization?

---

## Part E: Nuclear vs Crystal Coordination

| Property | Nuclear | Crystal |
|----------|---------|---------|
| Scale | fm (10⁻¹⁵ m) | Å (10⁻¹⁰ m) |
| Interaction | Strong force | EM (metallic, covalent) |
| Optimal n | ~43 (forbidden!) | 12 (FCC/HCP, allowed) |
| Stability | Frustrated | Stable |

**Key difference**:
- Crystals can achieve allowed n → stable
- Heavy nuclei stuck near forbidden n ≈ 43 → radioactive

---

## Part F: Steiner Networks [Der]

**Citation**: DN-041

Steiner minimal networks for point sets:
- Optimal topology uses Y-junctions (120° angles)
- n = 3 at junction vertices
- 3 is allowed

**EDC connection [Der]**:
- Y-junctions are topologically preferred
- Networks avoiding Y-junctions have higher energy
- Soap bubbles, biological branching follow this

---

## Summary

| Category | Coordination | EDC Status |
|----------|--------------|------------|
| SC | 6 | ✓ Allowed |
| BCC | 8 | ✓ Allowed |
| FCC/HCP | 12 | ✓ Allowed |
| Diamond | 4 | ✓ Allowed |
| Graphite | 3 | ✓ Allowed |
| Quasicrystal | 5 (local) | ✗ Forbidden [P] |
| Nuclear (heavy) | ~43 | ✗ Forbidden [Der] |

**Pattern [I]**: Stable bulk crystals have allowed coordination; heavy nuclei do not.
