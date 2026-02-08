# BULK CRYSTAL N48 WORKED EXAMPLES (V7.1)

**Created**: 2026-01-31
**Purpose**: Concrete crystal-nucleus mappings with falsifiable signatures
**Status**: [P] — Conceptual models, not verified predictions

---

## Framework

The crystal-nucleus analogy maps:
- **Coordination number n** → Effective nuclear topology
- **Allowed set S** → Crystal packings with n ∈ {2^a × 3^b}
- **Forbidden zone** → Frustrated geometries requiring defects

We work three examples at representative A values:
1. A ≈ 294 (deep forbidden zone)
2. A ≈ 350 (near saturation zone)
3. A ≈ 488 (approaching n = 48 target)

---

## Example 1: A = 294 (Deep Forbidden Zone)

### Parameters [P]
```
A = 294
n(A) = 6.1 × 294^(1/3) = 6.1 × 6.653 = 40.58
Nearest allowed: n* = 36 (d = 4.58) or n* = 48 (d = 7.42)
Zone: DEEP FORBIDDEN (maximum frustration region)
```

### Crystal Analog

**Situation**: n = 40.58 is midway between allowed packings (36 and 48). No simple crystal structure has coordination 40-41.

**Proposed Model**: **Polycrystalline with mixed domains**

| Domain Type | Local n | Crystal Structure | Volume Fraction |
|-------------|---------|-------------------|-----------------|
| FCC cores | 12 × 3 = 36 | Face-centered cubic + 2nd neighbors | 60% |
| BCC regions | 8 × 6 = 48 | Body-centered cubic + extended shell | 40% |
| Weighted average | 36×0.6 + 48×0.4 = **40.8** | — | — |

**Defect Signature**: Domain walls between 36 and 48 regions create:
- Stacking faults
- Grain boundary energy
- Internal stress

### Falsifiable Nuclear Signature [P]

1. **Enhanced isomerism**: Domain boundaries should trap excitations → more isomeric states near A ≈ 294

2. **Anomalous fission barriers**: Mixed-domain structure may lower fission saddle points

3. **Branching anomalies**: If different domains favor different decay channels, effective BR may show non-monotonic behavior

**Specific Prediction**: Nuclides in the A = 290-300 range should show higher isomer density than A = 260-270 or A = 320-330.

**Test**: Compare isomer counts per mass number in NUBASE2020 for these ranges.

**Status**: [Open] — Not yet tested

---

## Example 2: A = 350 (Near Saturation Zone)

### Parameters [P]
```
A = 350
n(A) = 6.1 × 350^(1/3) = 6.1 × 7.047 = 42.99
Nearest allowed: n* = 48 (d = 5.01) or n* = 36 (d = 6.99)
Zone: FORBIDDEN — closer to 48 than 36
```

### Crystal Analog

**Situation**: n = 43 is near the "saturation peak" (n_sat ≈ 43.3 from nuclear physics). This is the maximum frustration point — exactly between 36 and 48, and coincidentally near the nuclear saturation density coordination.

**Proposed Model**: **Quasicrystalline or icosahedral local order**

Quasicrystals achieve forbidden coordinations through:
- 5-fold local symmetry
- Long-range aperiodic order
- No translational invariance

**Nuclear Interpretation**: At A ≈ 350, the nucleus may have quasi-ordered domains that do not map to any simple crystal structure.

| Property | Crystal Analog | Nuclear Manifestation |
|----------|----------------|----------------------|
| Local order | Icosahedral clusters | α-like tetrahedral units |
| Long-range | Quasiperiodic tiling | Non-spherical deformation |
| Frustration | Phason defects | Fission instability |

### Falsifiable Nuclear Signature [P]

1. **Short half-lives**: Nuclides near A = 350 should have unusually short t₁/₂ compared to smooth trends

2. **High fission probabilities**: Quasicrystalline frustration may favor spontaneous fission over α-decay

3. **Non-axial deformation**: Ground state shapes may be triaxial rather than prolate/oblate

**Specific Prediction**: The ratio SF/α (spontaneous fission to α branching) should peak near A ≈ 350.

**Test**: Plot BR(SF) vs A for known superheavy elements.

**Status**: [Open] — Limited experimental data in this region

---

## Example 3: A = 488 (Approaching n = 48 Target)

### Parameters [P]
```
A = 488
n(A) = 6.1 × 488^(1/3) = 6.1 × 7.872 = 48.02
Nearest allowed: n* = 48 (d = 0.02)
Zone: NEAR-ALLOWED (at secondary target)
```

### Crystal Analog

**Situation**: n = 48 is an allowed coordination. The nucleus is at the "secondary island" target.

**Proposed Model**: **BCC + extended coordination**

The n = 48 coordination can be achieved by:
```
n = 48 = 8 (1st neighbors) + 6 (2nd neighbors) + 12 (3rd neighbors) + 22 (4th neighbors)?
```

More realistically:
```
n = 48 = 2^4 × 3^1 = 16 × 3
```

This could correspond to a **superlattice** with:
- 16-fold local symmetry
- 3-fold stacking along one axis

**Nuclear Interpretation**: At A ≈ 488, the nucleus achieves optimal packing at the n = 48 target. This should be a region of enhanced stability.

| Property | Expected Behavior |
|----------|-------------------|
| Half-life | Local maximum (longer than neighbors) |
| Fission barrier | Local maximum |
| Deformation | Near-spherical (magic-like) |

### Falsifiable Nuclear Signature [P]

1. **"Island of stability"**: If n = 48 is a real attractor, nuclides near A ≈ 488 should show enhanced stability

2. **Smooth extrapolation**: Half-lives should follow G-N law with small residuals (d ≈ 0)

3. **Spherical shape**: Reduced quadrupole deformation compared to A = 350 region

**Specific Prediction**: If a nuclide with A ≈ 488 is ever synthesized, its t₁/₂ should exceed extrapolation from A = 290-300 trend by at least 10×.

**Test**: Await experimental synthesis (currently beyond reach).

**Status**: [P] — Theoretical prediction for future validation

---

## Summary of Worked Examples

| A | n(A) | Zone | Crystal Model | Key Signature | Testability |
|---|------|------|---------------|---------------|-------------|
| 294 | 40.6 | Deep forbidden | Polycrystal (36/48 domains) | High isomerism | Medium |
| 350 | 43.0 | Max frustration | Quasicrystal | Peak SF/α ratio | Low |
| 488 | 48.0 | Near-allowed | BCC superlattice | Enhanced stability | Future |

---

## Falsification Criteria

The crystal-nucleus analogy would be **falsified** if:

1. **No isomer enhancement at A ≈ 294**: Isomer density is flat across the forbidden zone

2. **SF/α ratio does NOT peak near A ≈ 350**: Fission follows smooth A-dependence

3. **No stability island near A ≈ 488**: Half-lives decrease monotonically with A

4. **Spherical nuclei in forbidden zone**: If A ≈ 300 nuclei are not deformed, the frustration-induced strain model fails

---

## Epistemic Status

| Component | Status | Confidence |
|-----------|--------|------------|
| n(A) = 6.1 × A^(1/3) mapping | [P] | Medium — calibrated to ²⁰⁸Pb |
| S = {2^a × 3^b} constraint | [Der] | High — mathematical |
| Crystal structure analogs | [P] | Low — metaphorical |
| Falsifiable signatures | [P] | Medium — testable but speculative |

**Overall**: The crystal-nucleus analogy provides a **vocabulary** and **geometric intuition**, but NOT quantitative predictions. It remains a conceptual tool.

