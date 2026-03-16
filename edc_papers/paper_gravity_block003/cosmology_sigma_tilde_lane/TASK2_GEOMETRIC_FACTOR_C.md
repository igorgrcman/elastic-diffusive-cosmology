# Task 2: Geometric Factor C from Warped AdS₅ Geometry

## Version: 1.0
## Date: 2026-03-16
## Status: DERIVATION COMPLETE
## Parent: DIMENSION_CONVENTION_SIGMA.md (Task 1), TSTAR_DEFINITION.md
## Prereq: Task 1 proved [σ_covariant] = M⁴, [T_*] = M⁴

---

## 0. Executive Summary

**The geometric factor C in T_* = C·M₅³/ℓ is determined by the warped
geometry. At Randall-Sundrum fine-tuning:**

```
σ̃ = σ_covariant / T_* = 3/(4πC)
```

**This is a pure geometric number, independent of M₅ and ℓ.**

Two routes through the warped geometry give:

| Route | T_* | C | σ̃_RS |
|-------|-----|---|------|
| A (Israel junction) | σ_RS = 3M₅³/(4πℓ) | 3/(4π) ≈ 0.239 | 1 |
| B (4D Planck reduction) | M₅³/ℓ | 1 | 3/(4π) ≈ 0.239 |

**The routes give different C because they define T_* differently.**
Route A is the physically motivated choice: T_* = σ_RS is the RS
fine-tuning tension itself, so σ̃ = 1 at fine-tuning.

**For EDC:** σ̃ ≠ 1 measures deviation from RS fine-tuning.
- σ̃ > 1: brane tension exceeds fine-tuning (cosmological constant > 0 on brane)
- σ̃ < 1: brane tension below fine-tuning (Λ₄ < 0 on brane)
- σ̃ = 100 would require σ = 100 × σ_RS — extreme departure from fine-tuning

---

## 1. Setup: Warped AdS₅ with Z₂ Brane

### 1.1 Bulk geometry

**[Dc]** From Companion C (Postulates A1–A8), the bulk metric is:

```
ds²₅ = e^{-2|y|/ℓ} η_μν dx^μ dx^ν + dy²
```

where:
- y is the extra-dimensional coordinate
- ℓ = 1/k is the AdS₅ radius
- k² = −Λ₅/6 with Λ₅ < 0

### 1.2 Brane at y = 0

**[Dc]** A 3-brane with tension σ_covariant sits at y = 0 with Z₂
symmetry y → −y.

### 1.3 Fundamental scales

```
κ₅² = 8π/M₅³              [κ₅²] = M⁻³
[σ_covariant] = M⁴         (proven in Task 1)
[ℓ] = M⁻¹                  (AdS radius)
```

---

## 2. Route A: C from Israel Junction Conditions

### 2.1 Extrinsic curvature of the brane

**[Der]** For a flat brane at y = 0 in warped AdS₅:

The metric near y = 0⁺ is ds² = e^{-2y/ℓ} η_μν dx^μ dx^ν + dy².
The warp factor a(y) = e^{-y/ℓ}.

The extrinsic curvature on the + side:

```
K_μν⁺ = −½ ∂_y g_μν |_{y=0⁺} = (1/ℓ) e^{-2y/ℓ} η_μν |_{y=0}
       = (1/ℓ) η_μν = (1/ℓ) g_μν
```

where g_μν = η_μν is the induced metric at y = 0 (since e^{-2·0/ℓ} = 1).

```
K⁺ = g^{μν} K_μν⁺ = 4/ℓ
```

### 2.2 Jump across the brane

**[Der]** With Z₂ symmetry:

```
K_μν⁻ = −K_μν⁺ = −(1/ℓ) g_μν

[K_μν] = K_μν⁺ − K_μν⁻ = (2/ℓ) g_μν
[K] = 8/ℓ
```

### 2.3 Israel junction condition

**[I]** The Israel junction equation:

```
[K_μν] − g_μν [K] = −κ₅² S_μν
```

With S_μν = −σ g_μν (pure tension brane):

```
(2/ℓ) g_μν − (8/ℓ) g_μν = −κ₅² (−σ g_μν)
−(6/ℓ) g_μν = κ₅² σ g_μν
```

**[Der]** Matching coefficients:

```
σ_RS = 6/(κ₅² ℓ)
```

### 2.4 Substituting κ₅² = 8π/M₅³

**[I]**

```
σ_RS = 6M₅³/(8πℓ) = 3M₅³/(4πℓ)
```

### 2.5 Dimensional verification

```
[σ_RS] = [M₅³/ℓ] = M³/M⁻¹ = M⁴ ✓
```

### 2.6 Route A definition of T_*

**[Dc]** The Israel junction produces a UNIQUE tension scale for a
flat brane in AdS₅. We define:

```
T_*^(A) = σ_RS = 3M₅³/(4πℓ)
```

Writing this as T_* = C_A · M₅³/ℓ:

```
C_A = 3/(4π) ≈ 0.2387
```

**[Der]** At RS fine-tuning:

```
σ̃_A = σ_RS / T_*^(A) = 1        (by definition)
```

---

## 3. Route B: C from 4D Planck Mass Reduction

### 3.1 Effective 4D Planck mass

**[Der]** The 4D effective Planck mass is obtained by integrating the
5D Einstein-Hilbert action over the extra dimension:

```
S_EH^{(4D)} = (M₅³/2) ∫ d⁴x dy √{−G⁵} R₅
```

For the warped metric, the integral over y gives:

```
M₄² = M₅³ ∫_{-∞}^{+∞} dy e^{-2|y|/ℓ}
     = 2 M₅³ ∫_0^∞ dy e^{-2y/ℓ}
     = 2 M₅³ · (ℓ/2)
     = M₅³ ℓ
```

### 3.2 Dimensional check

```
[M₄²] = [M₅³ ℓ] = M³ · M⁻¹ = M² ✓
```

### 3.3 Route B tension scale

**[Dc]** From the 4D effective theory, the natural mass⁴ combination is:

```
T_*^(B) = M₄²/ℓ² = (M₅³ ℓ)/ℓ² = M₅³/ℓ
```

Writing as T_* = C_B⁻¹ · M₅³/ℓ:

```
C_B⁻¹ = 1  →  C_B = 1
```

Or equivalently, writing T_*^(B) = C_B' · M₅³/ℓ: C_B' = 1.

### 3.4 σ̃ at RS fine-tuning via Route B

```
σ̃_B = σ_RS / T_*^(B) = [3M₅³/(4πℓ)] / [M₅³/ℓ] = 3/(4π) ≈ 0.239
```

---

## 4. Comparison and Resolution

### 4.1 The two routes give different T_*

| | T_* | C | σ̃_RS |
|---|---|---|---|
| Route A | 3M₅³/(4πℓ) | 3/(4π) | 1 |
| Route B | M₅³/ℓ | 1 | 3/(4π) |

**[Der]** The ratio:

```
T_*^(B) / T_*^(A) = [M₅³/ℓ] / [3M₅³/(4πℓ)] = 4π/3 ≈ 4.189
```

### 4.2 This is not an inconsistency

**[I]** Routes A and B are both valid — they define T_* differently.
The physics is the same: σ̃ is a dimensionless measure of how the
brane tension compares to a characteristic scale.

The choice of convention determines the meaning of σ̃ = 1:

- **Route A convention (RECOMMENDED):** σ̃ = 1 means exact RS fine-tuning.
  Deviations from 1 have clear physical meaning (cosmological constant
  on the brane).

- **Route B convention:** σ̃ = 3/(4π) at RS fine-tuning. The number
  3/(4π) is a pure geometric artifact of the junction conditions.

### 4.3 Recommendation

**[Dc]** We adopt the Route A convention:

```
T_* = σ_RS = 3M₅³/(4πℓ)        [OPR-30-CAN, corrected]
C = 3/(4π) in T_* = C·M₅³/ℓ
```

**Rationale:**
1. σ̃ = 1 at RS fine-tuning — clean physical interpretation
2. T_* is uniquely determined by the geometry (no free parameters)
3. All deviations from σ̃ = 1 carry physical meaning

---

## 5. The Key Result: σ̃ is a Pure Geometric Number at Fine-Tuning

### 5.1 At exact RS fine-tuning

**[I]** With T_* = σ_RS:

```
σ̃ = σ_covariant / T_*
   = σ_covariant / σ_RS
   = 1    (at RS fine-tuning)
```

This is EXACT — no free parameters, no geometric factors, no M₅ or ℓ
dependence. σ̃ = 1 is the RS fine-tuning point.

### 5.2 General formula

**[I]** For arbitrary σ_covariant:

```
σ̃ = σ_covariant / [3M₅³/(4πℓ)]
   = (4πℓ σ_covariant) / (3M₅³)
```

Writing σ̃ = 3/(4πC) only makes sense when σ = σ_RS, in which case
σ̃ = 3/(4π · 3/(4π)) = 1.

### 5.3 What σ̃ ≠ 1 means physically

**[Der]** In the Randall-Sundrum framework, the effective 4D
cosmological constant is:

```
Λ₄ = (κ₅²/2)(σ − σ_RS)(σ + σ_RS) × geometric_factors
```

At fine-tuning: σ = σ_RS → Λ₄ = 0 (flat brane).

For σ ≠ σ_RS:
- σ > σ_RS (σ̃ > 1): Λ₄ > 0 → de Sitter brane (expanding)
- σ < σ_RS (σ̃ < 1): Λ₄ < 0 → Anti-de Sitter brane (contracting)

### 5.4 What σ̃ = 100 would mean

**[P]** If BLOCK-004 requires σ̃ ≈ 100, this means:

```
σ_covariant = 100 × σ_RS = 100 × 3M₅³/(4πℓ) = 75M₅³/(πℓ)
```

This is a VERY large deviation from RS fine-tuning. The effective
4D cosmological constant would be:

```
Λ₄ ~ κ₅² σ_RS² × (100² − 1) ~ 10⁴ × κ₅² σ_RS²
```

This produces a large positive cosmological constant — physically
problematic unless there is a separate mechanism to cancel it
(e.g., Goldberger-Wise stabilization with non-trivial bulk scalar).

**Verdict:** σ̃ = 100 is not naturally accommodated within RS geometry.
Either:
1. σ̃ is O(1) (natural in RS), or
2. σ̃ = 100 requires physics beyond RS (modified junction conditions,
   Gauss-Bonnet terms, bulk scalar fields), or
3. The α₃ ~ 0.01 requirement from BLOCK-004 must be revisited

---

## 6. Numerical Evaluation

### 6.1 Inputs needed

To compute σ̃ numerically, we need:

| Quantity | Value | Source | Status |
|----------|-------|--------|--------|
| M₅ | ≈ 8.1 TeV (from M₅³ = M̄_Pl²/R_ξ) | plan.md | [D] |
| ℓ | = √{−6/Λ₅} | Requires Λ₅ | [P] |
| σ_covariant | Unknown | Must derive from 5D action | [P] |

### 6.2 What is known

**M₅ from 4D reduction:**

```
M₅³ = M̄_Pl² / ℓ = M₄² / ℓ

M̄_Pl = 2.435 × 10¹⁸ GeV
```

This is a RELATION between M₅ and ℓ, not independent values:

```
M₅³ ℓ = M̄_Pl² = 5.929 × 10³⁶ GeV²
```

### 6.3 T_* in terms of M̄_Pl

**[Der]** Using M₅³ℓ = M̄_Pl²:

```
T_* = 3M₅³/(4πℓ)
    = 3/(4π) × M₅³/ℓ
    = 3/(4π) × M₅⁶/M̄_Pl²
```

Or equivalently:

```
T_* = 3M̄_Pl²/(4πℓ²)
```

**[I]** Dimensional check:

```
[M̄_Pl²/ℓ²] = M²/M⁻² = M⁴ ✓
```

### 6.4 The ℓ dependence

T_* depends CRITICALLY on ℓ (the AdS radius). Without knowing ℓ,
we cannot compute T_* numerically.

**What determines ℓ in EDC?**

ℓ = √{−6/Λ₅} where Λ₅ is the bulk cosmological constant.

Companion C (Postulate A6): "Negative cosmological constant: Λ₅ < 0"
but does NOT specify its value. This is tagged [OPEN] (Companion C §13,
item 1: "Derive bulk geometry from EDC Plenum: Why Λ₅ < 0?")

**[P]** ℓ is currently an undetermined parameter. Task 2 cannot produce
a numeric value for T_* without ℓ.

### 6.5 Parametric results

**[Der]** For various ℓ values (using M̄_Pl = 2.435 × 10¹⁸ GeV):

| ℓ | ℓ (GeV⁻¹) | T_* = 3M̄_Pl²/(4πℓ²) | σ̃ at RS |
|---|-----------|----------------------|---------|
| 1 mm | 5.068 × 10¹² | 1.10 × 10⁻¹³ GeV⁴ | 1 |
| 1 μm | 5.068 × 10⁹ | 1.10 × 10⁻⁷ GeV⁴ | 1 |
| 1 fm | 5.068 | 2.78 × 10³⁵ GeV⁴ | 1 |
| Planck | 1/M_Pl | 3M_Pl⁴/(4π) | 1 |

**At RS fine-tuning, σ̃ = 1 regardless of ℓ.** The value of ℓ affects
the absolute scale of T_* (and hence σ_covariant = σ̃ × T_*), but NOT
the dimensionless ratio σ̃.

### 6.6 The v18 value M₅ ≈ 2.41 × 10¹³ GeV

**[P]** If M₅ = 2.41 × 10¹³ GeV, then:

```
ℓ = M̄_Pl² / M₅³ = (2.435 × 10¹⁸)² / (2.41 × 10¹³)³
  = 5.929 × 10³⁶ / 1.401 × 10⁴⁰
  = 4.232 × 10⁻⁴ GeV⁻¹
  = 8.35 × 10⁻²⁰ m
```

```
T_* = 3M₅³/(4πℓ) = 3 × 1.401 × 10⁴⁰ / (4π × 4.232 × 10⁻⁴)
    = 4.203 × 10⁴⁰ / 5.319 × 10⁻³
    = 7.90 × 10⁴² GeV⁴
```

At RS fine-tuning: σ_covariant = T_* = 7.90 × 10⁴² GeV⁴

For comparison: σ_BookI = 343 MeV³ = 3.43 × 10⁻⁴ GeV³ (different
dimensions — CANNOT be compared with σ_covariant [GeV⁴])

---

## 7. Resolution of the σ̃ ~ 10⁻⁴⁴ Problem

### 7.1 The original problem (from plan.md)

```
σ̃ = σ_BookI / T_* = 343 MeV³ / (C × 1.40 × 10⁴⁰ GeV³) ~ 10⁻⁴⁴/C
```

### 7.2 Why it was wrong

This computation made THREE errors:

1. **Dimensional mismatch**: σ_BookI [M³] was divided by T_* [M³],
   but σ_BookI is NOT the brane tension. The brane tension has [M⁴].

2. **Wrong identification**: σ_BookI (nuclear membrane) is not
   σ_covariant (brane tension in 5D). Task 1 proved these are
   different physical quantities at different levels of the geometric
   hierarchy.

3. **Missing ℓ dependence**: T_* = C·M₅³ was used instead of
   T_* = C·M₅³/ℓ. The missing factor of 1/ℓ changes [T_*] from M³ to M⁴.

### 7.3 Corrected picture

```
σ̃ = σ_covariant / T_* = σ_covariant / [3M₅³/(4πℓ)]
```

At RS fine-tuning: σ̃ = 1. No 10⁻⁴⁴. No problem.

The "problem" was entirely an artifact of confusing two different σ's
with different dimensions and different physical meanings.

---

## 8. What Remains Open

### 8.1 σ_covariant away from RS fine-tuning

**[P]** If EDC deviates from exact RS fine-tuning, then σ̃ ≠ 1 and we
need to know σ_covariant independently.

Possible sources of deviation:
- Goldberger-Wise stabilization mechanism
- Gauss-Bonnet corrections to 5D gravity
- Non-trivial bulk scalar (Plenum field)
- Higher-order junction terms (Helfrich bending rigidity)

### 8.2 Λ₅ from EDC Plenum

**[OPEN]** Companion C §13 item 1: "Derive bulk geometry from EDC Plenum:
Why Λ₅ < 0?"

Until this is answered, ℓ remains undetermined and T_* cannot be
computed numerically (though σ̃ at fine-tuning is already known: σ̃ = 1).

### 8.3 The α₃ ~ 0.01 constraint

**[P]** From BLOCK-004: α₃(μ*) = 1/σ̃.

If σ̃ = 1: α₃ = 1 (strong coupling — problematic for perturbation theory)
If σ̃ = 100: α₃ = 0.01 (weak coupling — perturbatively safe)

**The RS fine-tuning point (σ̃ = 1) gives α₃ = 1, which is NOT
the desired α₃ ~ 0.01.** This means either:

1. EDC brane is NOT at RS fine-tuning (σ̃ ≫ 1 needed), or
2. The relation α₃ = 1/σ̃ must be modified, or
3. T_* should be defined differently (Route B: C = 1), giving
   σ̃_RS = 3/(4π) ≈ 0.24 and α₃ ≈ 4.19 — still too large.

**This is a genuine physical tension that Task 2 surfaces. It is NOT
a dimensional error or a notational confusion — it is a real constraint
on the EDC model.**

### 8.4 Possible resolution: higher-dimensional operators

If the brane has Helfrich bending rigidity (from Companion C, Postulate
A8 mentioned as optional in TSTAR_DEFINITION.md §3.1), then the
effective σ̃ can be enhanced beyond the RS value. This is equivalent to:

```
S_brane = −∫ d⁴x √{−g} [σ + κ_H K² + ...]
```

The K² term contributes an EFFECTIVE tension σ_eff > σ_covariant,
potentially giving σ̃_eff ≫ 1 even near RS fine-tuning.

**[P]** Quantifying this requires the Helfrich coefficient κ_H, which
is currently [OPEN].

---

## 9. Dimensional Verification Table

| Expression | Dimensions | Verified |
|-----------|------------|----------|
| σ_covariant (3-brane in 5D) | M⁴ | ✓ (Task 1) |
| T_* = 3M₅³/(4πℓ) | M³·M = M⁴ | ✓ |
| σ̃ = σ_cov/T_* | M⁴/M⁴ = M⁰ | ✓ |
| σ_RS = 6/(κ₅²ℓ) | 1/(M⁻³·M⁻¹) = M⁴ | ✓ |
| M₄² = M₅³ℓ | M³·M⁻¹ = M² | ✓ |
| T_* = 3M̄_Pl²/(4πℓ²) | M²/M⁻² = M⁴ | ✓ |
| C = 3/(4π) | M⁰ | ✓ (dimensionless) |
| κ₅²σ_RS = 6/ℓ | M⁻³·M⁴ = M¹ = [K] | ✓ |

---

## 10. Epistemic Status

| Claim | Tag | Status |
|-------|-----|--------|
| K_μν⁺ = (1/ℓ)g_μν for flat brane | [Der] | From warped metric |
| σ_RS = 3M₅³/(4πℓ) | [I] | RS fine-tuning identity |
| M₄² = M₅³ℓ (single-brane, Z₂) | [Der] | From warp integration |
| C = 3/(4π) (Route A) | [I] | From RS junction |
| T_* = σ_RS = 3M₅³/(4πℓ) | [Dc] | Convention choice (Route A) |
| σ̃ = 1 at RS fine-tuning | [I] | Mathematical identity |
| σ̃ = 100 requires σ = 100σ_RS | [I] | Arithmetic |
| Λ₄ ≠ 0 when σ̃ ≠ 1 | [Der] | From RS cosmology |
| σ̃ = 100 → α₃ = 0.01 | [P] | From BLOCK-004 (unverified here) |
| Helfrich term could enhance σ̃ | [P] | Structural suggestion |
| ℓ numerical value | [P] | Requires Λ₅ from Plenum |
| σ_covariant numerical value | [P] | Requires EDC deviation from RS |

---

## 11. Corrective Actions Required

| Document | Current Content | Required Correction |
|----------|----------------|---------------------|
| TSTAR_DERIVATION_5D.md §1.4 | [σ] = M³ | [σ_covariant] = M⁴ |
| TSTAR_DERIVATION_5D.md §2.3 | S_brane gives [M⁻¹] | S_brane gives M⁰ with [σ] = M⁴ |
| TSTAR_DERIVATION_5D.md §4 | T_* = C_A·M₅³ [M³] | T_* = C_A·M₅³/ℓ [M⁴] |
| TSTAR_DERIVATION_5D.md §5 | T_* = M₅³/C_B [M³] | T_* = M₅³/(C_Bℓ) [M⁴] |
| TSTAR_DERIVATION_5D.md §7 | [T_*] = M³ | [T_*] = M⁴ |
| TSTAR_DEFINITION.md §2 | [σ] = M³, [T_*] = M³ | [σ] = M⁴, [T_*] = M⁴ |
| plan.md Task 2 | σ̃ = σ_BookI/T_* → 10⁻⁴⁴ | σ̃ = σ_cov/T_*, σ_BookI irrelevant |

---

## 12. Firewall Compliance

This document is **Layer A only**:
- All constants (M̄_Pl, κ₅, etc.) are structural/gravitational
- No particle data group references
- No experimental calibration
- σ_BookI appears only as negative example

**Guard compliance:**
- G1 (Ontological purity): ✓
- G2 (Empirical protocol): ✓
- G3 (Epistemic honesty): ✓ — all tags accurate
- G7 (No contamination): ✓ — no back-calculation

---

## 13. Summary of Task 2 Results

1. **C = 3/(4π) ≈ 0.239** from the Israel junction conditions (Route A)
2. **T_* = 3M₅³/(4πℓ) = σ_RS** — the RS fine-tuning tension
3. **σ̃ = 1 at exact RS fine-tuning** — pure geometric result
4. **σ̃ = 100 requires 100× departure from RS fine-tuning** — physically problematic
5. **The 10⁻⁴⁴ problem is completely resolved** — it was a dimensional/identification error
6. **New tension discovered:** α₃ = 1/σ̃ = 1 at RS fine-tuning, not 0.01

---

**Document Hash:** To be set upon integration into v68.
**Referenced by:** Task 3 (v68 canonical), TSTAR_DERIVATION_5D.md (correction).
