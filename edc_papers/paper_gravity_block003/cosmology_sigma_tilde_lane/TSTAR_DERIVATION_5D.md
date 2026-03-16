# T_* Derivation from 5D Action

## Version: 2.0
## Date: 2026-03-16
## Status: STRUCTURAL DERIVATION (corrected dimensions per Task 1+2)
## Changelog: v2.0 — [σ] corrected from M³ to M⁴; T_* corrected from C·M₅³ to C·M₅³/ℓ
##            See DIMENSION_CONVENTION_SIGMA.md (Task 1) and TASK2_GEOMETRIC_FACTOR_C.md (Task 2)

---

## 1. Conventions

### 1.1 Metric Signature

**[Dc]** We adopt the mostly-plus signature convention:

```
η_AB = diag(-1, +1, +1, +1, +1)
```

where A, B = 0, 1, 2, 3, 5 are 5D indices and μ, ν = 0, 1, 2, 3 are 4D brane indices.

### 1.2 Fundamental Constants

**[Dc]** The 5D gravitational coupling is defined as:

```
κ₅² = 8π G₅ = 8π / M₅³
```

where M₅ is the 5D Planck mass with dimension [M₅] = [M]¹.

**[I]** Dimensional analysis:

```
[κ₅²] = [M]⁻³
[κ₅] = [M]^{-3/2}
```

### 1.3 Bulk Cosmological Constant

**[Dc]** The 5D cosmological constant Λ₅ has dimension:

```
[Λ₅] = [M]²
```

**[P]** The sign of Λ₅ (positive, zero, or negative) determines the bulk geometry:
- Λ₅ < 0: Anti-de Sitter bulk (AdS₅)
- Λ₅ = 0: Minkowski bulk
- Λ₅ > 0: de Sitter bulk (dS₅)

### 1.4 Brane Tension

**[Dc]** The covariant brane tension σ (3-brane in 5D) has dimension:

```
[σ_covariant] = [M]⁴
```

in natural units (ℏ = c = 1). This follows from the brane action
S = −σ∫d⁴x√{−h} being dimensionless: [σ]·[M]⁻⁴ = M⁰ → [σ] = M⁴.

**WARNING (v2.0):** The v1.0 of this document incorrectly stated [σ] = M³.
That dimension belongs to σ_BookI (energy per 2D area, nuclear membrane),
which is a DIFFERENT physical quantity. See DIMENSION_CONVENTION_SIGMA.md
for the proof that σ_BookI ≠ σ_covariant.

### 1.5 Induced Metric

**[Dc]** The induced metric on the brane is:

```
g_μν = G_AB e^A_μ e^B_ν
```

where G_AB is the 5D bulk metric and e^A_μ are the tangent vectors to the brane.

### 1.6 Extrinsic Curvature

**[Dc]** The extrinsic curvature of the brane is:

```
K_μν = -∇_μ n_ν = -e^A_μ e^B_ν ∇_A n_B
```

where n^A is the unit normal to the brane (n^A n_A = +1 for spacelike normal).

**[Dc]** The trace is:

```
K = g^{μν} K_μν
```

### 1.7 Jump Notation

**[Dc]** For a quantity Q evaluated on both sides of the brane:

```
[Q] = Q⁺ - Q⁻
```

denotes the jump across the brane.

### 1.8 Z₂ Symmetry

**[Dc]** We impose Z₂ symmetry across the brane:

```
y → -y  (reflection symmetry)
```

where y is the coordinate transverse to the brane.

**[I]** Under Z₂ symmetry:

```
[K_μν] = 2 K_μν⁺ = -2 K_μν⁻
```

---

## 2. 5D Action

### 2.1 Total Action

**[Dc]** The complete 5D gravitational action is:

```
S = S_bulk + S_brane + S_GHY
```

### 2.2 Bulk Action

**[Dc]** The 5D Einstein-Hilbert action with cosmological constant:

```
S_bulk = ∫ d⁵x √{-G} ( R₅/(2κ₅²) - Λ₅ )
```

where:
- G = det(G_AB) is the 5D metric determinant
- R₅ is the 5D Ricci scalar

**[I]** Dimensional check:

```
[d⁵x] = [M]⁻⁵
[√{-G}] = 1 (dimensionless)
[R₅] = [M]²
[R₅/κ₅²] = [M]² · [M]³ = [M]⁵
[S_bulk] = [M]⁻⁵ · [M]⁵ = [M]⁰ ✓
```

### 2.3 Brane Action

**[Dc]** The brane-localized tension term:

```
S_brane = -∫ d⁴x √{-g} σ
```

where:
- g = det(g_μν) is the induced 4D metric determinant
- σ is the brane tension

**[I]** Dimensional check (v2.0 corrected):

```
[d⁴x] = [M]⁻⁴
[√{-g}] = 1
[σ_covariant] = [M]⁴
[S_brane] = [M]⁻⁴ · [M]⁴ = [M]⁰ ✓
```

**NOTE (v2.0):** The v1.0 dimensional check was wrong — it used [σ] = M³,
getting [S] = M⁻¹, and then incorrectly claimed "proper 4D volume"
fixes it. The actual fix: [σ_covariant] = M⁴, not M³.

### 2.4 Gibbons-Hawking-York Boundary Term

**[Dc]** The GHY term for well-posed variational problem:

```
S_GHY = (1/κ₅²) ∫ d⁴x √{-g} K
```

**[I]** Dimensional check:

```
[K] = [M]¹
[K/κ₅²] = [M]¹ · [M]³ = [M]⁴
[S_GHY] = [M]⁻⁴ · [M]⁴ = [M]⁰ ✓
```

---

## 3. Israel Junction Conditions

### 3.1 Energy-Momentum on Brane

**[Dc]** For a pure-tension brane, the surface energy-momentum tensor is:

```
S_μν = -σ g_μν
```

**[I]** The trace is:

```
S = g^{μν} S_μν = -4σ
```

### 3.2 Israel Junction Equation

**[I]** The Israel junction conditions relate the jump in extrinsic curvature to the surface energy-momentum:

```
[K_μν] - g_μν [K] = -κ₅² ( S_μν - (1/3) S g_μν )
```

### 3.3 Reduction for Pure Tension

**[I]** Substituting S_μν = -σ g_μν and S = -4σ:

```
[K_μν] - g_μν [K] = -κ₅² ( -σ g_μν - (1/3)(-4σ) g_μν )
                   = -κ₅² ( -σ + (4/3)σ ) g_μν
                   = -κ₅² ( (1/3)σ ) g_μν
                   = -(κ₅² σ / 3) g_μν
```

### 3.4 Trace of Junction Condition

**[I]** Taking the trace (contracting with g^{μν}):

```
[K] - 4[K] = -4 (κ₅² σ / 3)
-3[K] = -(4κ₅² σ / 3)
[K] = (4κ₅² σ) / 9
```

### 3.5 Traceless Part

**[I]** The junction condition can be decomposed:

```
[K_μν] = g_μν [K] - (κ₅² σ / 3) g_μν
       = (4κ₅² σ / 9) g_μν - (κ₅² σ / 3) g_μν
       = (4κ₅² σ / 9 - 3κ₅² σ / 9) g_μν
       = (κ₅² σ / 9) g_μν
```

**[I]** With Z₂ symmetry ([K_μν] = 2K_μν⁺):

```
K_μν⁺ = (κ₅² σ / 18) g_μν
```

---

## 4. Route A: Junction/Geometry Derivation of T_*

### 4.1 Characteristic Curvature Scale (v2.0 corrected)

**[I]** From the junction condition, the extrinsic curvature is proportional to:

```
K ~ κ₅² σ
```

**[I]** Dimensional analysis (with corrected [σ] = M⁴):

```
[K] = [M]¹
[κ₅² σ] = [M]⁻³ · [M]⁴ = [M]¹ ✓  (matches [K])
```

This is now dimensionally consistent (v1.0 had [σ] = M³ → [κ₅²σ] = M⁰, wrong).

### 4.2 Bulk Curvature Length

**[Dc]** Define the AdS curvature length from Λ₅:

```
ℓ² = -6 / Λ₅   (for AdS₅, Λ₅ < 0)
```

**[I]** Dimensional check:

```
[ℓ²] = [M]⁻²  →  [ℓ] = [M]⁻¹
```

**[P]** For Λ₅ ≥ 0, an alternative characteristic length must be defined from the geometry.

### 4.3 Characteristic Tension Scale (Route A) — v2.0

**[Der]** From the RS fine-tuning condition (flat brane at y = 0 in warped AdS₅):

```
σ_RS = 6/(κ₅² ℓ) = 6M₅³/(8πℓ) = 3M₅³/(4πℓ)
```

**[I]** Dimensional verification:

```
[T_*^{(A)}] = [M₅³/ℓ] = [M]³ / [M]⁻¹ = [M]⁴ ✓
```

**[Dc]** Route A result (v2.0):

```
T_*^{(A)} = C_A · M₅³/ℓ = 3M₅³/(4πℓ) = σ_RS
```

where C_A = 3/(4π) ≈ 0.239 is determined by the Israel junction conditions.

**[I]** Final dimensional check:

```
[T_*^{(A)}] = [M₅³/ℓ] = [M]⁴ = [σ_covariant] ✓
```

**NOTE (v2.0):** The v1.0 struggled to get [T_*] = M³ from T_* = 6/(κ₅²ℓ),
which naturally gives M⁴. The "fix" of setting α = 0 and reverting to
T_* = C·M₅³ was incorrect — the natural M⁴ result was correct all along.
See TASK2_GEOMETRIC_FACTOR_C.md for the full derivation.

---

## 5. Route B: 4D Effective Reduction Derivation of T_* (v2.0)

### 5.1 Effective 4D Planck Mass

**[Der]** The 4D Planck mass is obtained by integrating the 5D action:

```
M₄² = M₅³ ∫_{-∞}^{+∞} dy e^{-2|y|/ℓ} = M₅³ ℓ
```

For single-brane RS with Z₂ symmetry and infinite extra dimension.

**[I]** Dimensional check:

```
[M₅³ ℓ] = [M]³ · [M]⁻¹ = [M]² ✓
```

### 5.2 Tension Scale from 4D Reduction (v2.0 corrected)

**[Dc]** Define T_*^{(B)} from the 4D effective theory:

```
T_*^{(B)} = M₄² / ℓ² = M₅³ℓ / ℓ² = M₅³ / ℓ
```

**[I]** Dimensional check:

```
[T_*^{(B)}] = [M]³ / [M]⁻¹ = [M]⁴ ✓
```

**NOTE (v2.0):** v1.0 used T_*^(B) = M₄²/ℓ with [M³], which was
forced by the incorrect [T_*] = M³ target. The corrected form uses
M₄²/ℓ² to get [M⁴].

### 5.3 Relation to Route A

**[I]** Comparing Route B (T_*^(B) = M₅³/ℓ) with Route A (T_*^(A) = 3M₅³/(4πℓ)):

```
T_*^{(B)} / T_*^{(A)} = [M₅³/ℓ] / [3M₅³/(4πℓ)] = 4π/3 ≈ 4.189
```

### 5.4 Interpretation

**[Der]** Routes A and B give different T_* values because they
capture different physical scales:

- **Route A:** T_* = σ_RS (the RS fine-tuning tension) → σ̃ = 1 at tuning
- **Route B:** T_* = M₅³/ℓ (the gravitational mass⁴ scale) → σ̃ = 3/(4π) at tuning

**[Dc]** We adopt Route A (T_* = σ_RS) as canonical because it gives
σ̃ = 1 a clear physical interpretation: exact RS fine-tuning.

See TASK2_GEOMETRIC_FACTOR_C.md §4 for the full comparison.

---

## 6. Route Comparison (v2.0)

### 6.1 The ratio of routes

**[I]** The ratio:

```
R_{AB} = T_*^{(A)} / T_*^{(B)} = [3M₅³/(4πℓ)] / [M₅³/ℓ] = 3/(4π)
```

### 6.2 Physical meaning

**[Der]** R_{AB} = 3/(4π) is NOT a correction — it is the geometric factor
from the Israel junction conditions (the factor 6 in σ_RS = 6/(κ₅²ℓ)
combined with the 8π from κ₅² = 8π/M₅³).

This ratio is FIXED by the warped geometry. It does not receive corrections
from higher-curvature terms unless the junction conditions themselves are
modified.

### 6.3 Structural Form (v2.0)

**[I]** Both routes give T_* ∝ M₅³/ℓ:

```
T_*^{(A)} = 3M₅³/(4πℓ) = σ_RS        [canonical]
T_*^{(B)} = M₅³/ℓ                      [alternative]

T_* = C · M₅³/ℓ
```

where C = 3/(4π) for Route A (canonical) or C = 1 for Route B.

---

## 7. Dimensional Checks (v2.0 corrected)

### 7.1 Brane Tension Dimension

**[I]** For a 3-brane (codimension-1 in 5D), the Nambu-Goto action
S = −σ∫d⁴x√{−h} requires [σ] = M^{p+1} = M⁴:

```
[σ_covariant] = [M]⁴     (3-brane tension = energy per 3-volume)
```

### 7.2 Characteristic Scale Dimension

**[I]** From the derivation (Route A):

```
[T_*] = [M₅³/ℓ] = [M]³ · [M]¹ = [M]⁴ = [σ_covariant]
```

### 7.3 Dimensionless Ratio

**[I]** The dimensionless brane tension:

```
σ̃ = σ_covariant / T_*

[σ̃] = [M]⁴ / [M]⁴ = [M]⁰ = dimensionless ✓
```

### 7.4 Summary Table (v2.0)

| Quantity | Dimension | Expression |
|----------|-----------|------------|
| σ_covariant | [M]⁴ | 3-brane tension |
| T_* | [M]⁴ | C · M₅³/ℓ (C = 3/(4π)) |
| σ̃ | [M]⁰ | σ_covariant / T_* |
| κ₅² | [M]⁻³ | 8π/M₅³ |
| Λ₅ | [M]² | Bulk cosmological constant |
| ℓ | [M]⁻¹ | √{-6/Λ₅} |
| σ_RS | [M]⁴ | 3M₅³/(4πℓ) = T_* |
| σ_BookI | [M]³ | 8.82 MeV/fm² (NOT brane tension) |

---

## 8. Export Semantics

### 8.1 Structural Result (v2.0)

**[Dc]** The characteristic tension scale is:

```
T_* = C · M₅³/ℓ = 3M₅³/(4πℓ) = σ_RS
```

where:
- M₅ is the 5D Planck mass
- ℓ = √{−6/Λ₅} is the AdS radius
- C = 3/(4π) ≈ 0.239 is the geometric factor from Israel junction
- T_* equals the RS fine-tuning tension σ_RS

### 8.2 Contract Reference

This derivation fulfills the requirements of `SIGMA_TILDE_EXPORT_CONTRACT.md`:
- T_* is derived from 5D action principles
- No external anchors are used
- The result is structural (symbolic)
- Dimensions are verified

### 8.3 JSON Export

When M₅ is determined from upstream cosmology, the export proceeds via:

```json
{
  "t_star": {
    "definition_ref": "TSTAR_DEFINITION.md",
    "derivation_ref": "TSTAR_DERIVATION_5D.md",
    "value": null,
    "units": null,
    "status": "TBD"
  }
}
```

---

## 9. No-Backflow Statement

### 9.1 Information Flow

**[Dc]** The derivation chain is strictly one-directional:

```
5D Action → Israel Junction → T_* = C·M₅³/ℓ → σ̃ = σ_cov/T_* → BLOCK-004
                                                            ↓
                                                       (read-only)
```

### 9.2 Forbidden Feedback

**[Dc]** The following feedback loops are PROHIBITED:

| Forbidden | Reason |
|-----------|--------|
| τ_p → T_* | Would create circular logic |
| σ̃ → M₅ | Would reverse information flow |
| BLOCK-004 → cosmology | Violates A-APIσ2 contract |
| External data → T_* | Violates Layer A firewall |

### 9.3 Contract Compliance

This document maintains full compliance with:
- `SIGMA_TILDE_EXPORT_CONTRACT.md` (interface APIs)
- `TSTAR_DEFINITION.md` (definitional contract)
- Layer A firewall (no external anchors)

---

## 10. Epistemic Status Summary

| Claim | Tag | Status |
|-------|-----|--------|
| Metric signature (-,+,+,+,+) | [Dc] | Definitional choice |
| κ₅² = 8π/M₅³ | [Dc] | Definition |
| [σ_covariant] = [M]⁴ | [I] | Invariant (v2.0 corrected from M³) |
| Israel junction equation | [I] | Mathematical identity |
| S_μν = -σ g_μν (pure tension) | [Dc] | Model assumption |
| Z₂ symmetry | [Dc] | Model assumption |
| ℓ² = -6/Λ₅ | [Dc] | AdS length definition |
| T_* = 3M₅³/(4πℓ) = σ_RS | [Der] | Derived from Israel junction (v2.0) |
| C = 3/(4π) | [I] | Geometric factor from junction |
| [T_*] = [M]⁴ | [I] | Dimensional identity (v2.0 corrected) |
| σ̃ = σ_cov/T_* dimensionless | [I] | Mathematical identity |
| σ̃ = 1 at RS fine-tuning | [I] | Follows from T_* = σ_RS |
| ℓ numerical value | [P] | Requires Λ₅ from Plenum |
| M₅ numerical value | [P] | Awaiting upstream |

---

## 11. References

| Document | Role |
|----------|------|
| TSTAR_DEFINITION.md | Definitional roadmap |
| SIGMA_TILDE_EXPORT_CONTRACT.md | Interface contract |
| sigma_tilde_schema.json | Export schema |
| v65 (c4e7f2a1b8d30965) | BLOCK-004 canonical |
| v67 (d8e9f0a1b2c34567) | σ̃ import contract |

---

**Document Hash:** TBD (to be set when geometric coefficients determined)
