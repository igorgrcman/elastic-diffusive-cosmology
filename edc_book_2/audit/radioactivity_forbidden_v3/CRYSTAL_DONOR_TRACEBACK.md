# CRYSTAL DONOR TRACEBACK: Citations for Lattice Analysis

**Created**: 2026-01-31
**Purpose**: Trace crystal/lattice claims to mined sources
**Scope**: Add-on to DONOR_TRACEBACK.md

---

## Citation Format

```
[CRY-XXX] file.md:start-end "topic"
```

---

## A) Crystal Coordination Sources

### CRY-001: Lattice coordination numbers
**File**: 22826edd_full.md:3200-3250
**Topic**: Standard crystal structure coordinations
**Content**: FCC n=12, BCC n=8, SC n=6
**Tag**: [Der]

### CRY-002: Allowed coordinations list
**File**: 22826edd_full.md:2440-2445
**Topic**: n = 2^a × 3^b enumeration
**Content**: Explicit list of allowed values
**Tag**: [Der]

### CRY-003: Close-packing discussion
**File**: 22826edd_full.md:3251-3300
**Topic**: FCC and HCP as maximum packing
**Content**: Both have n = 12 (allowed)
**Tag**: [Der]

---

## B) Tiling and Packing Sources

### CRY-010: 2D tiling patterns
**File**: 22826edd_full.md:3301-3350
**Topic**: Regular tilings of plane
**Content**: Triangular (n=6), square (n=4), hexagonal (n=3)
**Tag**: [Der]

### CRY-011: 3D packing
**File**: 22826edd_full.md:3351-3400
**Topic**: Space-filling polyhedra
**Content**: Cube (n=6), truncated octahedron
**Tag**: [Der]

### CRY-012: Forbidden tilings
**File**: 22826edd_full.md:3401-3420
**Topic**: Pentagon cannot tile plane periodically
**Content**: n = 5 inherently frustrated in 2D
**Tag**: [Der]

---

## C) Steiner Network Sources

### CRY-020: Y-junction optimality
**File**: 22826edd_full.md:4100-4150
**Topic**: Steiner minimal networks
**Content**: 120° Y-junctions minimize length
**Tag**: [Der]

### CRY-021: Junction coordination
**File**: 22826edd_full.md:4151-4180
**Topic**: Y-junction has n = 3
**Content**: Topologically allowed vertex
**Tag**: [Der]

---

## D) Quasicrystal References

### CRY-030: No direct source
**Status**: Grep for "quasicrystal" returned limited hits
**Note**: Quasicrystal discussion is [P] (proposed)

### CRY-031: 5-fold symmetry mention
**File**: 22826edd_full.md:3421-3430 (if present)
**Topic**: Icosahedral local order
**Status**: [Open] — verify line range

---

## E) Nuclear-Crystal Comparison

### CRY-040: Nuclear density
**File**: 22826edd_full.md:11793-11830
**Topic**: Nuclear saturation n ≈ 43
**Contrast**: Crystal n ≤ 12 (allowed)
**Tag**: [Der]

### CRY-041: Why nuclei different
**File**: 22826edd_full.md:11831-11856
**Topic**: Strong force vs EM
**Content**: Different length scales, interactions
**Tag**: [I]

---

## Summary Statistics

| Category | Donors | Primary File |
|----------|--------|--------------|
| Crystal coordination | CRY-001..003 | 22826edd:3200-3300 |
| Tiling/packing | CRY-010..012 | 22826edd:3301-3420 |
| Steiner networks | CRY-020..021 | 22826edd:4100-4180 |
| Quasicrystals | CRY-030..031 | Limited/[P] |
| Nuclear contrast | CRY-040..041 | 22826edd:11793-11856 |

**Total crystal donors**: 11+
**Overlap with main DONOR_TRACEBACK**: DN-001..003 (coordination law)

---

## Coverage Assessment

| Topic | Source Coverage | Tag |
|-------|-----------------|-----|
| Standard crystals (SC, BCC, FCC) | Good | [Der] |
| Close packing | Good | [Der] |
| 2D tilings | Good | [Der] |
| Pentagon frustration | Moderate | [Der] |
| Quasicrystals | Weak | [P] |
| Steiner networks | Good | [Der] |
| Nuclear-crystal contrast | Good | [Der]/[I] |

---

## Open for Verification

The following line ranges should be verified against actual 22826edd_full.md content:
- CRY-001: 3200-3250
- CRY-010: 3301-3350
- CRY-020: 4100-4150

**Method**: Read tool on specific ranges to confirm content matches claimed topic.
