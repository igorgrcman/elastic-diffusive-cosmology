# Radioactivity + M-Topology Chain: Mapping to Book 2 / Gap Register

**Generated**: 2026-01-31
**Source**: Chain reconstructed from `audit/jsonl_mining/`

---

## Chain → Book 2 Chapter Mapping

| Chain Block | Primary Chapter | Secondary Chapters | Integration Status |
|-------------|-----------------|-------------------|-------------------|
| MTR-001: Coordination Rules | Ch. 3 (Core Geometry) | Ch. 7 (Nuclear Scales) | ⚠️ Partial - Z₆ mentioned, n rules implicit |
| MTR-002: Frustration-Corrected G-N | Ch. 7 (Nuclear Scales) | Ch. 10 (Synthesis) | ❌ Not yet in Book 2 |
| MTR-003: n ≈ 43 Forbidden | Ch. 7 (Nuclear Scales) | Ch. 3 (Core Geometry) | ⚠️ Mentioned but not grounded |
| MTR-004: Pinning Constant K | Ch. 7 (Nuclear Scales) | — | ⚠️ K ≈ 0.8 MeV stated, derivation incomplete |
| MTR-005: Saturation Analysis | Ch. 7 (Nuclear Scales) | — | ❌ Not in current draft |
| MTR-006: Equation Summary | Appendix Equations | — | ⚠️ Some equations present |

---

## Chain → Gap Register Mapping

### Relevant Gaps from Current Register

| Gap ID | Gap Description | Chain Block | Resolution Potential |
|--------|-----------------|-------------|---------------------|
| GAP-7 | Nuclear binding from 5D | MTR-004, MTR-005 | **HIGH** - K derivation provides mechanism |
| GAP-8 | Quark mixing angles | MTR-001 | Medium - Coordination rules connect |
| GAP-14 | Generations μ-window | MTR-001, MTR-003 | Medium - Same Z₆ origin |
| GAP-19 | g₅ reduction | MTR-004 | Low - Indirect via σ |
| NEW | Frustration-Corrected G-N | MTR-002 | **HIGH** - Ready for integration |
| NEW | n ≈ 43 forbidden grounding | MTR-003, MTR-005 | **HIGH** - Core prediction |

### Proposed New Gaps to Register

| Proposed ID | Description | Epistemic Status | Blocking |
|-------------|-------------|-----------------|----------|
| GAP-R1 | Frustration parameter ε_f(A) formula | [I] | MTR-002 integration |
| GAP-R2 | f ≈ 0.3 geometric factor origin | [Open] | MTR-004 closure |
| GAP-R3 | Prefactor A in τ_n derivation | [Dc] | Full [Der] status |
| GAP-R4 | Y-junction + quantum doubling → n = 2^a × 3^b | [Open] | MTR-001 grounding |

---

## Chapter Integration Plan

### Chapter 3: Core Geometry (M-Topology Foundation)

**Current State**: Z₆ symmetry discussed, coordination rules implicit
**Required Additions**:
```
Section 3.X: Coordination Topology
- Theorem: Allowed coordinations n = 2^a × 3^b from Y-junction geometry
- Proof sketch: Z₆ = Z₂ × Z₃ → only {2,3} factors propagate
- Table: Allowed = {1,2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96...}
- Table: Forbidden (primes > 3) = {5,7,11,13,17,19,23,29,31,37,41,43,47...}
- Forward reference to Ch. 7 nuclear applications
```

**Epistemic Upgrade**: [Der] → needs Y-junction derivation (GAP-R4)

### Chapter 7: Nuclear Scales (Primary Target)

**Current State**: Nuclear binding discussed, some K values mentioned
**Required Additions**:
```
Section 7.X: Geometric Frustration in Nuclear Matter
- n_opt ≈ 43.3 from saturation density
- 43 is prime → FORBIDDEN
- Nearest allowed: n = 36 (error +8.6 MeV), n = 48 (error -5.6 MeV)
- Physical consequence: inherent instability of heavy nuclei

Section 7.Y: Pinning Constant Derivation
- σ = 8.82 MeV/fm² (input from brane tension)
- K = f × σ × A_contact
- f ≈ 0.3 (geometric factor, needs grounding)
- Result: K ≈ 0.8 MeV/bond

Section 7.Z: Frustration-Corrected Geiger-Nuttall Law [I]
- Standard G-N: log₁₀(t₁/₂) = a(Z/√Q) + b
- EDC-corrected: log₁₀(t₁/₂) = a(Z/√Q) + c·ε_f + b
- Fitted: a = 1.63, c = -2.40, b = -42.1
- Result: R² = 0.9941 (44.7% improvement)
- Status: [I] - Inferred, awaiting independent confirmation
```

**Epistemic Upgrades**:
- K derivation: [Cal] → [Der] if f is grounded
- G-N correction: [I] stays until experimental verification

### Chapter 10: Synthesis

**Current State**: Summary of predictions
**Required Additions**:
```
Table 10.X: Radioactivity Predictions
| Observable | EDC Prediction | Observed | Error | Status |
|------------|----------------|----------|-------|--------|
| τ_n (free) | ~10³ s | 879 s | O(1) | [Dc/Cal] |
| G-N fit | R² = 0.9941 | - | - | [I] |
| n_opt | 43.3 (forbidden) | - | - | [Der] |
| K | 0.8 MeV | - | - | [Der/Cal] |
```

---

## Derivation Flow Diagram

```
                    ┌──────────────────┐
                    │   5D Brane       │
                    │   Geometry       │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
      ┌───────────┐  ┌───────────┐  ┌───────────┐
      │    Z₆     │  │    σ      │  │  δ = R_ξ  │
      │ Symmetry  │  │ Tension   │  │  Scale    │
      └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
            │              │              │
            ▼              │              │
    ┌───────────────┐      │              │
    │ n = 2^a × 3^b │      │              │
    │   ALLOWED     │      │              │
    └───────┬───────┘      │              │
            │              │              │
            ▼              ▼              │
    ┌───────────────┐  ┌───────────────┐  │
    │ n = 43        │  │ K = f·σ·A    │◄─┘
    │  FORBIDDEN    │  │  ≈ 0.8 MeV   │
    └───────┬───────┘  └───────┬───────┘
            │                  │
            ▼                  ▼
    ┌───────────────┐  ┌───────────────┐
    │   GEOMETRIC   │  │   BARRIER     │
    │  FRUSTRATION  │  │  ΔV ≈ 2.7 MeV │
    └───────┬───────┘  └───────┬───────┘
            │                  │
            └────────┬─────────┘
                     │
                     ▼
            ┌───────────────────┐
            │ FRUSTRATION-      │
            │ CORRECTED G-N LAW │
            │ R² = 0.9941       │
            └───────────────────┘
```

---

## Priority Integration Order

1. **IMMEDIATE** (for current Book 2 draft):
   - Add coordination rules table to Ch. 3
   - Add n ≈ 43 forbidden discussion to Ch. 7
   - Update summary table in Ch. 10

2. **NEAR-TERM** (requires writing):
   - Full Section 7.Z on Frustration-Corrected G-N Law
   - K derivation pathway in Section 7.Y

3. **REQUIRES RESEARCH** (GAP resolution):
   - GAP-R4: Y-junction → n = 2^a × 3^b proof
   - GAP-R2: f ≈ 0.3 geometric factor derivation
   - GAP-R3: Prefactor A from fluctuation determinant

---

## Cross-Reference Index

| From Chain | To Book 2 File | Line/Section |
|------------|----------------|--------------|
| MTR-001 (coordination) | `sections/ch03_core_geometry.tex` | TBD |
| MTR-002 (G-N law) | `sections/ch07_nuclear_scales.tex` | NEW Section |
| MTR-003 (n=43) | `sections/ch07_nuclear_scales.tex` | Existing mention, expand |
| MTR-004 (K pinning) | `sections/ch07_nuclear_scales.tex` | Existing mention, expand |
| MTR-005 (saturation) | `sections/ch07_nuclear_scales.tex` | NEW Section |
| Chain equations | `backmatter/equation_index.tex` | Update required |

---

## Blockers for Full Integration

| Blocker | Description | Affects | Resolution Path |
|---------|-------------|---------|-----------------|
| BL-R1 | f ≈ 0.3 factor not derived | K derivation | Derive from Z₆ contact geometry |
| BL-R2 | ε_f(A) formula not explicit | G-N law section | Define frustration energy functional |
| BL-R3 | Prefactor A ad-hoc | τ_n claim | Compute fluctuation determinant |
| BL-R4 | n = 2^a × 3^b not proven | Coordination chapter | Y-junction + doubling proof |

---

**STATUS**: TASK -2B COMPLETE (chain_map.md)
**NEXT**: TASK -3 - Create Book 2 integration plan
