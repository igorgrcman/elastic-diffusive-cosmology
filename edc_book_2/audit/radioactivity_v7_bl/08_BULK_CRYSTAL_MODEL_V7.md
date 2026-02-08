# BULK CRYSTAL MODEL (V7)

**Created**: 2026-01-31
**Purpose**: Crystal-nucleus analogy with explicit falsification
**Status**: [P] — Analogy only; not a predictive model

---

## Mapping: Crystal → Nucleus

### Allowed Coordination Numbers [Der]

| n | Crystal Structure | Nuclear Analog | Status |
|---|-------------------|----------------|--------|
| 4 | Diamond | α-cluster (⁴He) | [I] |
| 6 | Simple Cubic | Light nuclei | [P] |
| 8 | BCC | Pauli-limited | [P] |
| 12 | FCC/HCP | Close-packed core | [I] |
| 24 | Complex metallic | Extended shell | [P] |
| 36 | Superlattice | Pb-region (A~200) | [I] |
| 48 | Hyperlattice | SHE-region (A~500) | [P] |

**Source**: V6 08_BULK_CRYSTAL_ANALOGY_N48.md, DN-050..058

---

## Mechanism-to-Crystal Mapping

### M1: Domain Mixing → Polycrystal

**Crystal Analog**: Polycrystalline material with domains of different structures.

**Nuclear Application** [P]:
- Heavy nucleus contains multiple coordination domains
- n_eff = Σ wᵢ × nᵢ (weighted average)
- Can produce "forbidden" average from allowed domains

**Falsification Test**:
- If nuclei show anisotropic α-emission → supports domain structure
- If emission is isotropic → no domain evidence

**V7 Status**: Untested — requires angular distribution data [BL:SOURCE_NEEDED]

---

### M2: Defects → Dislocations/Y-Junctions

**Crystal Analog**: Point defects, line defects, grain boundaries reduce local coordination.

**Nuclear Application** [P]:
- Y-junction defects in nuclear interior
- n_eff = n_bulk - ρ_defect × Δn

**Falsification Test**:
- If deformed nuclei have systematically different half-lives → supports defect model
- If no deformation correlation → defect model fails

**V7 Status**: Untested — requires deformation data [BL:SOURCE_NEEDED]

---

### M3: α-Clustering → Cluster Compounds

**Crystal Analog**: Some crystals have tetrahedral cluster units (n=4 per cluster).

**Nuclear Application** [I]:
- Preformed α-clusters act as n=4 units
- 12 α-clusters → n_eff = 48

**Falsification Test**:
- If α-spectroscopic factors correlate with A/4 ratio → supports clustering
- If no correlation → clustering not relevant

**V7 Status**: Partial support — ²¹¹Bi shows strong α-dominance (99.7%)

---

### M4: Metastable → Kinetically Trapped

**Crystal Analog**: Amorphous or metastable phases.

**Nuclear Application** [P]:
- Isomeric states may have different effective n
- Frozen configuration from formation

**Falsification Test**:
- If isomers have different branching than ground states → supports M4
- If identical branching → M4 not relevant

**V7 Status**: Untested — requires isomer branching data [BL:SOURCE_NEEDED]

---

### M6: Core-Mantle → Core-Shell Nanoparticles

**Crystal Analog**: Core-shell nanoparticles with different core and surface structures.

**Nuclear Application** [P]:
- Heavy nuclei (A > 250) may have layered structure
- Core at n ≈ 48, surface at n ≈ 36-42

**Falsification Test**:
- If SHE show anomalous charge radii → supports layering
- If radii follow smooth A^(1/3) → no layering

**V7 Status**: Untested — requires SHE spectroscopy [BL:SOURCE_NEEDED]

---

## What the Crystal Analogy DOES NOT Explain

### 1. Branching Ratios
V7 BL testing showed that d(n) does NOT predict branching.
Crystal analogy offers no improvement.

### 2. Absolute Half-Lives
Half-lives are determined by Q-values and barrier penetration, not coordination.
Crystal coordination is not a substitute for quantum tunneling calculations.

### 3. Magic Numbers
Shell closures (Z=82, N=126) are quantum effects.
Crystal coordination is geometric, not quantum.

---

## Explicit Falsification Section

### What Would Falsify the Crystal Analogy?

| Claim | Falsification Criterion | Status |
|-------|------------------------|--------|
| n ∈ 2^a × 3^b only | Find stable nucleus with n = 5, 7, 10, 11 | Open |
| d(n) correlates with stability | Chain d(n) increases toward stable | ✗ Confirmed decrease |
| Domain structure exists | Isotropic emission in all heavy nuclei | Open |
| α-clustering relevant | No α-spectroscopic factor correlation | Partial support |
| Core-mantle in SHE | Smooth radii in SHE region | Open |

### Current Status

| Claim | Tested? | Result |
|-------|---------|--------|
| n = 2^a × 3^b | No | - |
| d(n) chain decrease | Yes | ✓ Confirmed |
| d(n) predicts branching | Yes | ✗ Failed |
| d(n) predicts half-life | Partial | Inconclusive |

---

## Summary

The crystal-nucleus analogy provides:

1. **A vocabulary** for describing nuclear coordination
2. **A geometric framework** for the allowed set S
3. **Mechanistic ideas** (domains, defects, clustering)

But it does NOT provide:

1. **Quantitative predictions** for branching or half-lives
2. **An explanation** for why β⁻ dominates in some cases
3. **A replacement** for nuclear structure calculations

**Status**: The crystal analogy is a **conceptual tool**, not a **predictive model**.
