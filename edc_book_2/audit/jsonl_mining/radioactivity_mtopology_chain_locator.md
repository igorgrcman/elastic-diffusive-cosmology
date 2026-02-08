# Radioactivity + M-Topology Chain Locator

**Generated**: 2026-01-31
**Source Directory**: `audit/jsonl_mining/`
**Primary Source**: `reports/22826edd_full.md` (17,562 lines)

---

## Summary

The M-topology → Radioactivity derivation chain is concentrated in **one primary file** with supporting equation references in the equations registry.

| Metric | Value |
|--------|-------|
| Primary source file | `22826edd_full.md` |
| Total chain blocks | 6 |
| Line coverage | ~1,100 lines across 4 regions |
| Key epistemic tags | [Der], [I], [Cal], [P], [M] |

---

## Block Index

| Block ID | Source File | Line Range | Tags | Component Covered |
|----------|-------------|------------|------|-------------------|
| MTR-001 | 22826edd_full.md | 2440-2540 | [Der], [M] | Coordination rules: n = 2^a × 3^b allowed; {5,7,11,13...43} forbidden |
| MTR-002 | 22826edd_full.md | 2560-2660 | [I], [Cal] | Frustration-Corrected Geiger-Nuttall Law: log₁₀(t₁/₂) = a(Z/√Q) + c·ε_f + b; R² = 0.9941 |
| MTR-003 | 22826edd_full.md | 7280-7430 | [Der], [P] | Geometric Frustration: n ≈ 43 forbidden → nuclear matter instability mechanism |
| MTR-004 | 22826edd_full.md | 11040-11290 | [Der], [Cal] | Pinning constant K ≈ 0.8 MeV/bond from σ = 8.82 MeV/fm²; M6 complete picture |
| MTR-005 | 22826edd_full.md | 11790-11990 | [Der], [Cal] | n ≈ 43.3 optimal saturation; barrier ΔV_eff ≈ 2.7 MeV; q_barrier = 0.5 |
| MTR-006 | 22826edd_equations.md | EQ-0493-0497 | [I] | Key equations: Frustration-Corrected G-N, n≈43 forbidden statements |

---

## Detailed Block Descriptions

### MTR-001: Coordination Rules (Allowed vs Forbidden)
**Location**: `22826edd_full.md:2440-2540`
**Content**:
- Allowed coordination numbers: n = 2^a × 3^b → {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128...}
- Forbidden (primes > 3): {5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, **43**, 47, 53...}
- EDC constraint from 5D brane geometry: only smooth-form coordinations propagate
- Physical basis: M43 forbidden geometry creates frustration in nuclear packing

### MTR-002: Frustration-Corrected Geiger-Nuttall Law
**Location**: `22826edd_full.md:2560-2660`
**Content**:
- Standard G-N: log₁₀(t₁/₂) = a(Z/√Q_α) + b
- EDC-corrected: log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
- Frustration parameter ε_f encodes deviation from allowed coordination
- Fit results: R² = 0.9941 (vs 0.69 standard), 44.7% improvement
- Applies to α-decay across actinide series

### MTR-003: Geometric Frustration Mechanism
**Location**: `22826edd_full.md:7280-7430`
**Content**:
- Nuclear matter saturation requires n ≈ 43.3 nearest neighbors
- 43 is prime → forbidden in M-topology
- System cannot achieve ideal packing → geometric frustration
- Frustration energy contributes to nuclear binding systematics
- Links to liquid drop model corrections

### MTR-004: Pinning Constant Derivation
**Location**: `22826edd_full.md:11040-11290`
**Content**:
- Surface tension σ = 8.82 MeV/fm² (nuclear data)
- Pinning K = σ × geometric_factor ≈ 0.8 MeV/bond
- M6 model geometry: hexagonal close-packing frustrated by forbidden coordinations
- Complete picture: K determines barrier heights for nucleon tunneling
- Links topological constraint to measurable nuclear properties

### MTR-005: Nuclear Matter Saturation Analysis
**Location**: `22826edd_full.md:11790-11990`
**Content**:
- Optimal coordination n_opt ≈ 43.3 from nuclear density
- Nearest allowed: n = 36 (2² × 3²) or n = 48 (2⁴ × 3)
- Frustration penalty ΔE_f from mismatch
- Barrier calculation: ΔV_eff ≈ 2.7 MeV
- Tunneling parameter q_barrier = 0.5
- Connects to neutron lifetime τ_n ≈ 880 s via WKB

### MTR-006: Equation Registry Entries
**Location**: `22826edd_equations.md`
**Key Equations**:
- EQ-22826edd-0493: Frustration-Corrected Geiger-Nuttall Law
- EQ-22826edd-0496: `n ≈ 43.3 but 43 is forbidden`
- EQ-22826edd-0497: `n≈43 for nuclear matter saturation but 43 is prime (forbidden)`

---

## Cross-References

### To Other Mined Files
| File | Relevance |
|------|-----------|
| `master_equation_registry.md` | Contains ~95 equations, several reference nuclear/topology |
| `master_claims_registry.md` | Claim about frustration mechanism listed |
| `special/f_bulk_full.md` | F_bulk derivation uses similar geometric constraints |

### To Book 2 Chapters
| Chapter | Mapping |
|---------|---------|
| Ch. 7 (Nuclear Scales) | Direct target for MTR-001 through MTR-005 |
| Ch. 3 (Core Geometry) | M-topology rules foundation |
| Ch. 10 (Synthesis) | Integration of radioactivity predictions |

---

## Extraction Priority

For TASK -2 (verbatim chain reconstruction), extract in order:
1. MTR-001 → MTR-003 → MTR-004 → MTR-005 → MTR-002 → MTR-006

This follows the logical derivation flow:
```
Coordination Rules → Frustration Mechanism → Pinning Constant →
Saturation Analysis → G-N Law Correction → Equation Summary
```

---

## Keywords Located

| Keyword | Blocks Found |
|---------|--------------|
| M43 / M-43 | MTR-001, MTR-003, MTR-005 |
| forbidden | MTR-001, MTR-003, MTR-005, MTR-006 |
| coordination | MTR-001, MTR-003, MTR-004 |
| frustration | MTR-001, MTR-002, MTR-003, MTR-005 |
| half-life / t₁/₂ | MTR-002 |
| WKB | MTR-005 |
| Geiger-Nuttall | MTR-002, MTR-006 |
| pinning | MTR-004, MTR-005 |
| nuclear matter | MTR-003, MTR-004, MTR-005 |
| barrier | MTR-004, MTR-005 |

---

**STATUS**: TASK -1 COMPLETE
**NEXT**: TASK -2 - Extract verbatim chain content
