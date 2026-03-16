# Cosmological Constant Constraint on σ̃ and AdS Radius

## Status: DERIVED — σ̃ constrained to 1 + O(10⁻⁵⁶) by Λ₄
## Date: 2026-03-16
## Layer: B (uses measured Λ₄, M₅ from v23)
## Depends on: v68 (σ_RS formula), v23 (M₅), PATH-C analysis

---

## 1. RS Detuning Formula

### 1.1 Setup

In the Randall-Sundrum model, the 4D cosmological constant arises from
the mismatch between the brane tension σ and the bulk cosmological
constant Λ₅:

```
Λ₄ = (κ₅⁴σ²/12) − κ₅²|Λ₅|/6
```

At RS fine-tuning, Λ₄ = 0 when σ = σ_RS and |Λ₅| = κ₅²σ_RS²/2.

### 1.2 Detuned brane

Writing σ_covariant = σ̃ · σ_RS and keeping Λ₅ fixed at its RS value:

```
Λ₄ = (κ₅⁴σ_RS²/12)(σ̃² − 1)
```

### 1.3 Simplification

Using σ_RS = 3M₅³/(4πℓ) and κ₅² = 8π/M₅³, the prefactor simplifies
exactly:

```
κ₅⁴σ_RS²/12 = (8π/M₅³)² · (3M₅³/(4πℓ))² / 12
             = (64π²/M₅⁶) · (9M₅⁶/(16π²ℓ²)) / 12
             = 3/ℓ²
```

Therefore:

```
┌─────────────────────────────────────────┐
│                                         │
│    Λ₄ = (3/ℓ²)(σ̃² − 1)     [EXACT]    │
│                                         │
└─────────────────────────────────────────┘
```

This is the clean RS detuning formula. [Der]

For small detuning (σ̃ ≈ 1, ε = σ̃ − 1 ≪ 1):

```
Λ₄ ≈ (6/ℓ²) · ε
```

---

## 2. Solving for ℓ from M₅

The RS hierarchy relation (single-brane, Z₂ symmetry):

```
M̄_Pl² = M₅³ · ℓ
```

Using M₅ = 5.6 × 10¹² GeV (v23, [I]+[BL]) and M̄_Pl = 2.435 × 10¹⁸ GeV:

```
ℓ = M̄_Pl² / M₅³
  = (2.435 × 10¹⁸)² / (5.6 × 10¹²)³
  = 5.929 × 10³⁶ / 1.756 × 10³⁸
  = 3.376 × 10⁻² GeV⁻¹
  = 6.66 × 10⁻¹⁸ m
```

| Quantity | Value | Units | Status |
|----------|-------|-------|--------|
| ℓ | 3.376 × 10⁻² | GeV⁻¹ | [I]+[BL] |
| ℓ | 6.66 × 10⁻¹⁸ | m | [I]+[BL] |

Note: ℓ ≈ L = π/M_Z = 3.445 × 10⁻² GeV⁻¹. The near-coincidence
ℓ ≈ L is expected since both are set by the same mass hierarchy.

---

## 3. Computing σ_RS and T_*

From v68 (Task 2):

```
σ_RS = T_* = 3M₅³/(4πℓ)
     = 3 × (5.6 × 10¹²)³ / (4π × 3.376 × 10⁻²)
     = 3 × 1.756 × 10³⁸ / (4.240 × 10⁻¹)
     = 1.242 × 10³⁹ GeV⁴
```

| Quantity | Value | Units | Status |
|----------|-------|-------|--------|
| σ_RS = T_* | 1.242 × 10³⁹ | GeV⁴ | [Der] |
| 3/ℓ² | 2.632 × 10³ | GeV² | [I] |

---

## 4. σ̃ from Λ₄ (Independent of α_s)

### 4.1 Direct inversion

From the exact RS detuning formula:

```
σ̃² = 1 + Λ₄ℓ²/3
```

Substituting Λ₄ = 1.11 × 10⁻⁵² GeV² and ℓ = 3.376 × 10⁻² GeV⁻¹:

```
Λ₄ · ℓ² / 3 = (1.11 × 10⁻⁵²) × (3.376 × 10⁻²)² / 3
              = (1.11 × 10⁻⁵²) × (1.140 × 10⁻³) / 3
              = 4.22 × 10⁻⁵⁶
```

Therefore:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│    σ̃² = 1 + 4.22 × 10⁻⁵⁶                          │
│    σ̃  = 1 + 2.11 × 10⁻⁵⁶                          │
│    ε   = σ̃ − 1 = 2.11 × 10⁻⁵⁶                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**The cosmological constant constrains σ̃ to be 1 to 55 decimal places.**

### 4.2 Physical interpretation

The brane tension must be fine-tuned to the RS value to 1 part in
2.4 × 10⁵⁵. This is the **cosmological constant problem** expressed
in Randall-Sundrum language:

```
|σ_covariant − σ_RS| / σ_RS = |σ̃ − 1| = 2.11 × 10⁻⁵⁶
```

This is not a new problem — it is the well-known CC fine-tuning
problem, which exists in any framework where Λ₄ arises from
cancellation between large energy scales.

### 4.3 Dimensional check

```
[Λ₄] = GeV²    ✓
[3/ℓ²] = GeV²  ✓
[σ̃² − 1] = M⁰  ✓
```

---

## 5. Consistency Check with PATH-C Result

### 5.1 The two constraints on σ̃

| Source | σ̃ value | Layer | Method |
|--------|---------|-------|--------|
| Λ₄ (this analysis) | 1 + 2.11 × 10⁻⁵⁶ | B | RS detuning formula |
| α_s(M_Z) (PATH-C) | 8.47 | B | 1/α_s(M_Z) with μ* = M_Z |
| RS fine-tuning (v68) | 1 | A | Geometric identity |

### 5.2 Incompatibility

The two Layer B constraints are **catastrophically incompatible**:

```
σ̃(Λ₄)   = 1 + 2 × 10⁻⁵⁶
σ̃(α_s)  = 8.47
```

If σ̃ = 8.47 (from α_s), the implied cosmological constant is:

```
Λ₄(σ̃=8.47) = (3/ℓ²)(8.47² − 1)
             = 2632 × 70.74
             = 1.86 × 10⁵ GeV²
```

This exceeds the measured Λ₄ by a factor of **1.68 × 10⁵⁷**.

### 5.3 Anti-circularity verification

| Check | Status |
|-------|--------|
| σ̃(Λ₄) derived without using α_s(M_Z) | ✓ PASS |
| σ̃(α_s) derived without using Λ₄ | ✓ PASS |
| The two constraints are independent | ✓ PASS |
| They are compared, not mixed | ✓ PASS |

The incompatibility is genuine — it comes from two independent
experimental inputs making contradictory demands on the same parameter.

---

## 6. Epistemic Status

| Claim | Tag | Source |
|-------|-----|--------|
| Λ₄ = (3/ℓ²)(σ̃² − 1) | [Der] | RS model, exact |
| ℓ = M̄_Pl²/M₅³ = 3.376 × 10⁻² GeV⁻¹ | [I]+[BL] | v23 + RS hierarchy |
| σ_RS = 1.242 × 10³⁹ GeV⁴ | [Der] | v68 Task 2 |
| σ̃(Λ₄) = 1 + 2.11 × 10⁻⁵⁶ | [Der]+[BL] | This analysis |
| σ̃(α_s) = 8.47 | [Der]+[BL] | PATH-C analysis |
| Incompatibility: 57 orders of magnitude | [Der] | This analysis |
| Λ₄ = 1.11 × 10⁻⁵² GeV² | [Exp] | Planck 2018, Layer B |
| M₅ = 5.6 × 10¹² GeV | [I]+[BL] | v23 |
| α_s(M_Z) = 0.118 | [Exp] | PDG, Layer B |

---

## 7. What Remains Open

### 7.1 The σ̃ trilemma

EDC now faces three mutually inconsistent constraints:

```
(A)  σ̃ = 1 + 10⁻⁵⁶         [from Λ₄]
(B)  σ̃ = 8.47               [from α_s(M_Z)]
(C)  σ̃ = 1                  [RS fine-tuning, structural]
```

Constraints (A) and (C) are compatible: Λ₄ essentially demands
exact RS fine-tuning, consistent with the v68 structural result.

Constraint (B) is incompatible with both (A) and (C) by O(10) in
σ̃ and O(10⁵⁷) in Λ₄.

### 7.2 Possible resolutions

1. **The v56 formula α₃ = 1/σ̃ is wrong or incomplete.**
   The relation α₃(μ*) = 1/σ̃ comes from Route A/C in v56 with
   specific assumptions (PS unification hook, g₅² = 4π/M₅). If these
   assumptions are incorrect, σ̃ need not equal 1/α₃(μ*), and
   constraint (B) is modified or eliminated. This is the most likely
   resolution.

2. **The RS detuning formula receives EDC corrections.**
   The Plenum field, brane bending, or other EDC-specific effects
   may modify the Λ₄-σ̃ relation beyond the standard RS formula.
   The formula Λ₄ = (3/ℓ²)(σ̃² − 1) assumes pure RS geometry with
   no additional brane dynamics.

3. **M₅ is different from the v23 value.**
   If M₅ ≈ 1.6 × 10³ GeV instead of 5.6 × 10¹² GeV, then ℓ
   changes dramatically and σ̃ = 8.47 becomes compatible with Λ₄.
   But M₅ ~ TeV contradicts the v21 identification L = π/M_Z and
   the v23 derivation chain entirely.

4. **The CC problem is unsolved and cuts across all these relations.**
   The 10⁵⁵ fine-tuning in σ̃ IS the cosmological constant problem.
   No framework — RS, EDC, or otherwise — has solved the CC problem.
   It may be that σ̃ is set by some mechanism (anthropic, dynamical,
   or otherwise) that gives the tiny Λ₄ while also determining α₃,
   but this is beyond current EDC scope.

### 7.3 Impact on OPR-31

This analysis adds a fourth constraint to OPR-31:

| Path | Status |
|------|--------|
| PATH-A (Plenum enhancement) | OPEN — but now constrained by Λ₄ |
| PATH-B (Helfrich bending) | OPEN — but now constrained by Λ₄ |
| PATH-C (RG running) | CLOSED (FAILS) |
| **NEW: Λ₄ constraint** | σ̃ = 1 + 10⁻⁵⁶ — any enhancement mechanism must also solve the CC problem |

Any mechanism (PATH-A or PATH-B) that pushes σ̃ to ~8.5 must
simultaneously explain why Λ₄ ≈ 10⁻⁵² GeV² and not ~10⁵ GeV².
This couples the σ̃ problem directly to the cosmological constant problem.

### 7.4 The honest assessment

The σ̃ situation is now clear:

- **Structurally**: σ̃ = 1 at RS fine-tuning (v68, Layer A). Clean and honest.
- **From Λ₄**: σ̃ = 1 to 55 decimals (this analysis, Layer B). Consistent with structure.
- **From α_s**: σ̃ ≈ 8.5 (PATH-C, Layer B). Inconsistent with Λ₄.
- **From v56**: α₃ = 1/σ̃ (Layer A, assuming PS hook). The weak link.

The most likely resolution is that the v56 relation α₃ = 1/σ̃ is
not the complete story. The PS unification hook and Route A assumptions
in v56 may need modification when the full EDC brane dynamics are
included. The Λ₄ constraint strongly favors σ̃ ≈ 1, not σ̃ ≈ 8.5.

---

## 8. Layer A/B Boundary

| Element | Layer |
|---------|-------|
| Λ₄ = (3/ℓ²)(σ̃² − 1) | A (structural RS formula) |
| ℓ = M̄_Pl²/M₅³ | A (RS hierarchy) |
| σ_RS = 3M₅³/(4πℓ) | A (v68) |
| Λ₄ = 1.11 × 10⁻⁵² GeV² | **B** (Planck 2018) |
| M₅ = 5.6 × 10¹² GeV | **B** (v23 via M_Z) |
| α_s(M_Z) = 0.118 | **B** (PDG) |
| σ̃(Λ₄) = 1 + 10⁻⁵⁶ | **B** (derived, this analysis) |
| σ̃(α_s) = 8.47 | **B** (derived, PATH-C) |

---

## 9. Guard Compliance

| Check | Status |
|-------|--------|
| Layer B inputs explicitly flagged | PASS |
| No Layer A contamination from Layer B | PASS |
| Anti-circularity between Λ₄ and α_s constraints | PASS |
| All claims epistemically tagged | PASS |
| Incompatibility honestly documented | PASS |
| CC problem acknowledged, not claimed solved | PASS |

---

**Sealed: Λ₄ constrains σ̃ = 1 + 2.11 × 10⁻⁵⁶. The α_s(M_Z) target
σ̃ ≈ 8.5 is incompatible with measured Λ₄ by 57 orders of magnitude.
This is the cosmological constant problem in RS/EDC language.**
