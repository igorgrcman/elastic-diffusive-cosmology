# DMINING DERIVATIONS REPORT

**Date:** 2026-01-31
**Source:** `/Users/igor/ClaudeAI/EDC_Project/dmining/projects/`
**Files Scanned:** 88 JSONL files (~700 MB total)

---

## Executive Summary

Comprehensive search through Claude Code session transcripts revealed extensive derivation content across multiple categories:

| Category | Files Found | Key Content |
|----------|-------------|-------------|
| Proton/Neutron | 60+ files | Y-junction, Steiner, mass ratio 6π⁵ |
| Instanton/WKB | 18 files | Tunneling, semiclassical, 879s lifetime |
| SU(3)/SU(2) | 60+ files | Gauge symmetry, color confinement |
| Z₆ Symmetry | 10+ files | Hexagonal packing, discrete symmetry |
| M₅ / 5D | 60+ files | Bulk-brane, Nambu-Goto action |

---

## 1. DERIVATION FILES IDENTIFIED

### Core Derivations (from session content)
```
003_NEUTRON_LIFETIME_DERIVATION
026_electron_soliton_full_EOM_derivation
box_pathB_flavor_f_of_n_derivation
box_pathB_spin_helicity_mapping_derivation
box_pathB_Z3_quantization_PROOF
ch11_E_ell_derivation
ch11_opr20_attemptE_prefactor8_derivation
ch11_opr20_robin_derivation_attemptB
check_opr19_4pi_derivation
effective_lagrangian_derivation
main_Leff_derivation
MEFF_COEFFICIENT_C_DERIVATION
opr19_4pi_derivation_verification
TIER2_1_ALPHA_DERIVATION
verify_task_b3_G_derivation
Z6_PROGRAM_COMPLETE_DERIVATION
```

### Companion Documents (Paper 3 Series)
```
companion_A_5D_action_to_Seff
companion_A_effective_lagrangian
companion_B_wkb_prefactor
companion_C_5d_reduction
companion_D_selection_rules
companion_E_symmetry_ops
companion_F_proton_junction
companion_G_neutron_proton_mass_split
companion_H_weak_interactions
companion_L_electron_brane_defect
companion_M_muon_decay_tomography
companion_N_neutron_junction
companion_P_pion_
```

---

## 2. OPEN PROBLEM REFERENCES (OPR)

Found OPR-01 through OPR-25 referenced across files:

| OPR | Topic (inferred from context) |
|-----|-------------------------------|
| OPR-01 | 5D Action foundation |
| OPR-04 | δ (brane thickness) derivation |
| OPR-19 | 4π factor / g₅ derivation |
| OPR-20 | M_W / G_F prediction |

---

## 3. KEY PHYSICS CONTENT

### 3.1 Proton Y-Junction (120° Steiner)

**Source files:**
- `98cc5184-b172-4833-9b17-b923ac34b0c1.jsonl` (211 MB - largest)
- `22826edd-2441-4230-bbfc-5bbb12e57e39.jsonl` (202 MB)

**Key content found:**
- Y-Junction on brane with 3 flux tubes meeting
- Topological invariant: Baryonic winding number W = +1
- Collective coordinate q ≡ |ê₁ + ê₂ + ê₃| / 3 ∈ [0, 1]
- q = 0: Symmetric (120°) = proton
- q > 0: Asymmetric = neutron

### 3.2 Neutron Lifetime Derivation

**Key findings:**
- "879 s from WKB tunneling in the 5D effective potential"
- "neutron lifetime kao kombinacija WKB"
- "5D tunneling rate through potential barrier"
- "Asymmetric junction tunnels → Symmetric junction"

**Derivation chain:**
```
Junction asymmetry (q) → 5D barrier → WKB integral → τ_n ~ 879s
```

### 3.3 Instanton/WKB Content

**Key patterns found:**
- "WKB fazni integral gdje kvantizacija daje"
- "830 s from WKB tunneling"
- "879 s from WKB tunneling in the 5D effective potential"
- "effective 1D semiclassical tunneling problem"
- "Compute WKB tunneling action S_n"
- "Compute tunneling rate from 5D junction dynamics"

### 3.4 Z₆ Symmetry Program

**Key findings:**
- `Z6_PROGRAM_COMPLETE_DERIVATION`
- `Z6_PROGRAM_EXECUTIVE_SUMMARY`
- "hexagonal lattice structure determines the coefficient"
- "Z_6 boundary conditions select odd modes"
- "Mass eigenstates at Z6 positions"
- "forces hexagonal packing"

**Derivation chain:**
```
[P] Flux-tube interactions → [M] Kepler-Hales → [Dc] hexagonal lattice →
[Dc] equal tensions → [M] Steiner 120°
```

### 3.5 SU(3)/SU(2) and Color Confinement

**Key findings:**
- "3 arms → 3 QCD colors"
- "8 junction modes → 8 gluons"
- "Z₃ charge conservation → color confinement"
- Gauge group emergence from junction topology

### 3.6 5D Action / M₅ Manifold

**Key diagram found:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                      PLENUM (ξ > 0)                                 │
│                    5D bulk spacetime                                │
│                        P_bulk > 0                                   │
│  ═══════════════════════════════════════════════════════════════   │
│                         BRANE (ξ = 0)                               │
│                    3D observable universe                           │
│                      Our membrane Σ                                 │
│  ═══════════════════════════════════════════════════════════════   │
│                      ANTI-PLENUM (ξ < 0)                            │
│                    (mirror structure)                               │
└─────────────────────────────────────────────────────────────────────┘
```

**Coordinates:** (t, x, y, z, ξ) where ξ is the 5th dimension
**Key principle:** All observable matter lives on the brane Σ at ξ = 0

---

## 4. LARGEST FILES (Priority for Deep Mining)

| Size | File ID | Content Type |
|------|---------|--------------|
| 211 MB | 98cc5184-b172-4833-9b17-b923ac34b0c1 | EDC-Research-PRIVATE main |
| 202 MB | 22826edd-2441-4230-bbfc-5bbb12e57e39 | EDC-Research-PRIVATE main |
| 106 MB | 73d92ff5-39ec-459c-a15f-10648db8fe6d | EDC-Research-PRIVATE |
| 50 MB | a921f1e0-bbc8-4406-89f5-bb5bacde9ea4 | EDC-Research-PRIVATE |
| 32 MB | 19828e96-1702-4d28-825a-c69c31ea1b2b | EDC-Research-PRIVATE |
| 17 MB | agent-a4e7413 | Subagent (proton) |
| 16 MB | 5251e090-59dc-46a4 | EDC-Research public |

---

## 5. EXTRACTION RECOMMENDATIONS

### High Priority (for book backfill)
1. **Z6_PROGRAM_COMPLETE_DERIVATION** - Full hexagonal→Steiner chain
2. **003_NEUTRON_LIFETIME_DERIVATION** - WKB tunneling τ_n
3. **companion_B_wkb_prefactor** - Prefactor calculation
4. **companion_F_proton_junction** - Y-junction formal proof
5. **companion_G_neutron_proton_mass_split** - Δm_np derivation

### Medium Priority
1. **companion_A_5D_action_to_Seff** - Action reduction
2. **companion_C_5d_reduction** - Dimensional reduction
3. **companion_D_selection_rules** - Mode selection
4. **companion_E_symmetry_ops** - Symmetry operations

### To Extract
Run targeted extraction on each companion document:
```bash
grep -A100 "companion_X" <file>.jsonl | head -200
```

---

## 6. FILE PATHS FOR REFERENCED CONTENT

Based on session content, these files exist in the repo:

```
EDC_Research_PRIVATE/derivations/mass_difference/
EDC_Research_PRIVATE/releases/paper_2_private/
EDC_Research_PRIVATE/releases/paper_3_private/
EDC_Research_PRIVATE/releases/paper_3_private/companion/companion_E_symmetry_ops/
```

---

## 7. NEXT STEPS

1. **Deep extraction** from 211 MB file for complete derivation chains
2. **Cross-reference** with existing `src/derivations/` content
3. **Identify gaps** between JSONL content and current book
4. **Extract LaTeX** from companion documents for direct inclusion

---

## Appendix: Search Commands Used

```bash
# Find proton derivations
find /path/to/dmining -name "*.jsonl" -exec grep -l "proton" {} \;

# Find instanton content
find /path/to/dmining -name "*.jsonl" -exec grep -l "instanton\|WKB" {} \;

# Find Z6 symmetry
grep -i "Z_6\|Z6.*symmetry\|hexagonal" file.jsonl

# Extract derivation names
grep -i "DERIVATION_\|DERIVE_" file.jsonl | grep -oE '[A-Za-z0-9_]+derivation'
```
