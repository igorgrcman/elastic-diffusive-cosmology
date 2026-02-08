# LAWS AND INVARIANTS: EDC Radioactivity Framework

**Generated**: 2026-01-31
**Source**: MTR chain + decay chain analysis

---

## 1. The Fundamental Coordination Law [Der]

**Citation**: MTR-001 (22826edd_full.md:2440-2540)

### Statement

```
COORDINATION LAW: A coordination number n is EDC-allowed iff n = 2^a × 3^b
for some non-negative integers a, b.
```

### Equivalent Formulations

1. **Factorization form**: n has no prime factors > 3
2. **Regular form**: n ∈ {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, ...}
3. **Forbidden form**: n is forbidden iff ∃ prime p > 3 such that p | n

### Origin [Der/Open]

The law derives from Z₆ = Z₂ × Z₃ brane symmetry:
- Z₂ factor → powers of 2 allowed (quantum doubling)
- Z₃ factor → powers of 3 allowed (Y-junction geometry)

**Gap**: Full derivation (GAP-R4) remains open.

---

## 2. The Forbidden Distance Metric [P]

### Definition

For any n, define the **forbidden distance** d(n):

```
d(n) = min{ |n - m| : m = 2^a × 3^b, a,b ≥ 0 }
```

This measures how far n is from the nearest allowed coordination.

### Examples

| n | Nearest Allowed | d(n) | Status |
|---|-----------------|------|--------|
| 36 | 36 | 0 | Allowed |
| 43 | 48 (or 36) | 5 (or 7) → min = 5 | Forbidden |
| 44 | 48 | 4 | Forbidden |
| 45 | 48 | 3 | Forbidden |
| 46 | 48 | 2 | Forbidden |
| 47 | 48 | 1 | Forbidden |
| 48 | 48 | 0 | Allowed |
| 50 | 48 (or 54) | 2 (or 4) → min = 2 | Forbidden |

### Hypothesis [P]

**Correlation with half-life**: For nuclei with effective coordination n(A):
```
log₁₀(t₁/₂) may correlate with d(n(A))
```

If d(n) → 0, system is stable.
If d(n) >> 0, frustration increases → decay required.

**Falsification test**: Plot t₁/₂ vs estimated d(n(A)) for actinide series.

---

## 3. The Frustration Energy Functional [I/Open]

**Citation**: MTR-002 (22826edd_full.md:2560-2660)

### Current Status

The frustration parameter ε_f appears in the corrected G-N law:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
```

But ε_f(A) is not explicitly defined as a function of A.

### Proposed Form [P] (GAP-R1)

**Minimal ansatz**:
```
ε_f(A) = κ × d(n(A))^α
```

Where:
- n(A) = effective coordination for nucleus of mass A
- d(n(A)) = forbidden distance metric
- κ, α = phenomenological constants

**Simplest case** (α = 1):
```
ε_f(A) ∝ d(n(A))
```

### Required for [Der] Status

1. Derive n(A) from nuclear density ρ(A) and geometry
2. Show that ε_f(A) = κ·d(n(A)) produces R² ≈ 0.9941
3. Explain the sign of fitted c = -2.40

---

## 4. The Barrier Formula [Der]

**Citation**: MTR-005 (22826edd_full.md:11862-11902)

### Statement

```
ΔV_eff = ΔV + 6K × q_barrier²
```

Where:
- ΔV = intrinsic barrier (e.g., 1.3 MeV from mass difference)
- K = pinning constant (≈ 0.8-0.94 MeV/bond)
- q_barrier = saddle point position (= 0.5 for symmetric barrier)

### Numerical Example

```
ΔV_eff ≈ 1.3 + 6 × 0.94 × (0.5)²
       = 1.3 + 6 × 0.94 × 0.25
       = 1.3 + 1.41
       ≈ 2.7 MeV
```

### Generalization to n ≠ 43 [Open]

If coordination deviates from 43.3 by δn, how does barrier change?

**Proposed [P]**:
```
ΔV_eff(n) = ΔV + 6K(n) × q_barrier²(n)
```

Where K(n) and q_barrier(n) might depend on coordination.

---

## 5. The Pinning-Surface Tension Law [Der/Cal]

**Citation**: MTR-004 (22826edd_full.md:11040-11200)

### Statement

```
K = f × σ × A_contact
```

Where:
- σ = 8.82 MeV/fm² (brane surface tension)
- A_contact = contact area between nucleon cells
- f ≈ 0.3 (geometric factor from Z₆ symmetry)

### Numerical Verification

```
K = 0.32 × 8.82 × 0.33 ≈ 0.93 MeV/bond
```

Consistent with observed nuclear binding.

### Gap [Open]

Origin of f ≈ 0.3 (GAP-R2) not derived.

---

## 6. Proposed Invariants (Speculative) [P]

### Invariant I1: Decay Chain Terminates at Allowed n

**Claim**: All decay chains terminate when n(A) reaches an allowed value (d(n) = 0).

**Evidence**: All three chains end at Pb isotopes:
- ²⁰⁶Pb, ²⁰⁷Pb, ²⁰⁸Pb

If n(206), n(207), n(208) ≈ 36 (allowed), this explains termination.

**Test**: Calculate n(Pb isotopes) and verify d(n) = 0.

### Invariant I2: α-Emission Reduces n by ~4-8

**Claim**: Each α-decay reduces effective coordination significantly.

**Reasoning**:
- α-particle removes 4 nucleons
- This reduces surface coordination by a geometric factor
- Estimated Δn per α ≈ 4-8 (needs calculation)

**Test**: Verify that chains with more α-steps have larger total n reduction.

### Invariant I3: Magic Numbers Correspond to Allowed n

**Claim**: Nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) may relate to allowed coordinations in M-topology.

**Speculative connection**:
- Z = 82 magic → n(Pb) in allowed zone?
- N = 126 magic → neutron coordination optimal?

**Status**: Purely [P], no evidence in chain.

---

## 7. Summary Table

| Law/Invariant | Status | Citation | Gap Needed |
|---------------|--------|----------|------------|
| Coordination Law n = 2^a × 3^b | [Der] | MTR-001 | GAP-R4 for proof |
| Forbidden Distance Metric d(n) | [P] | New | Correlation test |
| Frustration Functional ε_f(A) | [I/Open] | MTR-002 | GAP-R1 |
| Barrier Formula ΔV_eff | [Der] | MTR-005 | Generalization to n≠43 |
| Pinning K from σ | [Der]/[Cal] | MTR-004 | GAP-R2 for f |
| I1: Chains end at allowed n | [P] | Decay chains | Calculate n(Pb) |
| I2: α reduces n by ~4-8 | [P] | Logic | Geometry calculation |
| I3: Magic = allowed | [P] | Speculative | No evidence |

---

## 8. What Would Falsify the Framework?

| Claim | Falsified If |
|-------|--------------|
| n = 2^a × 3^b rule | Stable nucleus requires forbidden n |
| n ≈ 43 optimal | Nuclear saturation density gives different n |
| Frustration-corrected G-N | R² degrades with more data, or c > 0 |
| ε_f ∝ d(n) | No correlation when tested |
| Chains end at allowed n | n(Pb) is not allowed |
| Barrier formula | ΔV_eff doesn't match WKB extraction |

---

## 9. Next Steps for [Der] Upgrades

1. **Derive n(A)**: Formula linking mass number A to effective coordination
2. **Define ε_f(A)**: Explicit functional form
3. **Derive f ≈ 0.3**: From Z₆ contact geometry
4. **Prove n = 2^a × 3^b**: From Y-junction + quantum doubling
5. **Calculate n(Pb isotopes)**: Verify they're in allowed zone
6. **Test d(n) correlation**: With actual half-life data
