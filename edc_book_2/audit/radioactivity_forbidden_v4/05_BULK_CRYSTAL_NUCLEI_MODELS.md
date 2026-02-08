# BULK CRYSTAL → NUCLEI MODELS V4

**Created**: 2026-01-31
**Purpose**: Treat nuclei as finite, defect-rich bulk packings
**Citation**: DN-050..057, DN-070..074

---

## Part C1: Crystal Family → Nucleus Mapping

| Crystal | n | Allowed? | Nuclear Analog | Stress/Frustration |
|---------|---|----------|----------------|-------------------|
| SC | 6 | ✓ (2×3) | Light nuclei surface | Low (allowed) |
| BCC | 8 | ✓ (2³) | α-cluster interface | Low (allowed) |
| FCC | 12 | ✓ (2²×3) | α-cluster interior | Low (allowed) |
| HCP | 12 | ✓ (2²×3) | Close-packed core | Low (allowed) |
| Diamond | 4 | ✓ (2²) | Tetrahedral bonding | Low (allowed) |
| --- | 43 | ✗ (prime) | Heavy nucleus bulk | HIGH (M43 paradox) |

**Key insight**: Crystals can reach allowed n → stable. Nuclei stuck at ~43 → unstable.

---

## Part C2: Why Periodic Crystals Can't Realize n=5, 7, 11

### The Crystallographic Restriction

**Statement [Der]**: Periodic tilings in 2D/3D require rotational symmetry n ∈ {1,2,3,4,6}.

**Consequence**:
- n=5 (pentagon): Cannot tile plane periodically
- n=7 (heptagon): Requires negative curvature
- n=11: No periodic structure exists

**Citation**: DN-056 (22826edd:16113) "circle packing, a classical result"

### Connection to Forbidden Zone

| n | Crystal Status | Nuclear Status |
|---|----------------|----------------|
| 5 | No periodic structure | Forbidden (LAW-1) |
| 7 | Defects only | Forbidden (LAW-1) |
| 11 | Impossible | Forbidden (LAW-1) |
| 43 | Impossible | Forbidden but n_opt |

**Pattern [I]**: LAW-1 (n = 2^a × 3^b) aligns with crystallographic restriction for small n.

---

## Part C3: Aperiodic/Quasicrystal Possibility [P]

### What Quasicrystals Do

- 5-fold, 10-fold rotational symmetry
- No translational periodicity
- Local n = 5 coordination (icosahedral)
- Stabilized by electronic effects (Hume-Rothery)

### Nuclear Analog [P]

**Hypothesis**: Heavy nuclei might have quasicrystalline-like internal structure

| Property | Quasicrystal | Heavy Nucleus |
|----------|--------------|---------------|
| Periodicity | None | None (finite) |
| Local n | 5 (forbidden) | ~43 (forbidden) |
| Stability | Metastable? | Metastable (decays) |
| Escape | Phase transition | Radioactive decay |

**Mechanism M5 application**: Aperiodic packing allows average n in forbidden zone

**Falsification**: If nuclear structure is proven periodic-like, reject M5

---

## Part C4: Nucleus as Defect-Rich Crystal

### Model [P]

Heavy nucleus = finite "crystal" with:
1. **Core**: Attempts n ≈ 43 (bulk saturation) — forbidden
2. **Surface**: Lower coordination (n < 43) — still forbidden?
3. **Defects**: α-clusters (n=12 locally), domain walls

### Defect Types

| Defect | Local n | Effect | Citation |
|--------|---------|--------|----------|
| α-cluster | 12 (allowed) | Relieves frustration | DN-074 |
| Domain wall | Variable | Interface energy | DN-051 |
| Y-junction | 3 (allowed) | Minimal network | DN-041 |
| Disclination | ±1 | Topological charge | [P] |

### Defect Energy [I]

**Citation**: DN-050 (22826edd:41)
```
E_defect ≈ τ × L  (Nambu-Goto in static limit)
```

**Interpretation**: Defect energy proportional to defect length/area

---

## Part C5: Coordination → Stress → Decay Mode Map [P]

### Logic Chain

```
n_bulk ≈ 43 (forbidden)
    ↓
Frustration energy: ε_f ∝ d(n)
    ↓
Stress accumulates at:
    - α-cluster interfaces
    - Core-mantle boundary
    - Domain walls
    ↓
Decay = stress relief:
    - α: Removes cluster, Δn ≈ -1 to -2
    - β: Adjusts N/Z, small Δn
    - SF: Splits into allowed fragments
```

### Mode Selection [P]

| Stress Level | d(n) | Preferred Mode | Mechanism |
|--------------|------|----------------|-----------|
| Low | 1-2 | β | M1 (domain mixing) |
| Medium | 3-4 | α/β competitive | M3 (α-cluster) |
| High | 5-6 | α | M3, M6 (core-mantle) |
| Extreme | >6 | SF | M3 (fission) |

---

## Part C6: Core-Mantle Structure [P] (M6)

### Model

```
     ┌──────────────────┐
     │  MANTLE (n~38)   │  Surface layer, lower density
     │  ┌────────────┐  │
     │  │  CORE      │  │  Dense interior, n~43
     │  │  (n~43)    │  │
     │  └────────────┘  │
     └──────────────────┘
          INTERFACE
          (frustrated)
```

### Interface Properties

| Property | Value |
|----------|-------|
| n_core | ~43 (forbidden) |
| n_mantle | ~38-40 (forbidden) |
| n_interface | Varies (frustrated transition) |
| Interface width | ~1-2 fm [Open] |
| Interface energy | σ_interface × A_interface |

### Decay Implications [P]

- α-emission preferentially from interface
- β-decay adjusts mantle composition
- Core remains frustrated until small enough

---

## Part C7: Donor Citations (10+ new)

| ID | File:Line | Topic |
|----|-----------|-------|
| DN-050 | 22826edd:41 | Defect energy τ×L |
| DN-051 | 22826edd:4847 | Domain-wall physical |
| DN-052 | 22826edd:4925 | Domain-wall V_L |
| DN-053 | 22826edd:2452 | α-cluster model |
| DN-054 | 22826edd:2450 | Close packing n=12 |
| DN-055 | 22826edd:11363 | Z₆ packing factor |
| DN-056 | 22826edd:16113 | Circle packing |
| DN-057 | 22826edd:15558 | α-cluster overestimate |
| DN-070 | 22826edd:2450 | BCC n=8 |
| DN-071 | 22826edd:2450 | FCC n=12 |
| DN-072 | 22826edd:41 | Defect scaling |
| DN-073 | 22826edd:2479-2492 | Domain mixing |
| DN-074 | 22826edd:2465-2478 | α-clusterization |

---

## Part C8: Falsification Tests

| Test | Prediction | Falsification |
|------|------------|---------------|
| F1 | No stable periodic n=5 crystal | Find one |
| F2 | Heavy nuclei have n~43 | Measure n≠43 |
| F3 | α-clusters have n=12 | n≠12 in cluster |
| F4 | Defect energy ∝ length | Non-linear scaling |
| F5 | Core denser than mantle | Uniform density |
| F6 | Interface frustration | No interface layer |

---

## Summary

| Aspect | Crystal (stable) | Nucleus (unstable) |
|--------|-----------------|-------------------|
| n achieved | Allowed (6,8,12) | Forbidden (~43) |
| Periodicity | Yes | No (finite) |
| Defects | Rare | Abundant |
| Stress | Low | High |
| Lifetime | ∞ | Finite (decay) |

**Core insight [I]**: Nuclei are "frustrated crystals" that relax via radioactive decay.
