# Dimension Convention for σ: Surface Tension vs Brane Tension

## Version: 1.0
## Date: 2026-03-15
## Status: DERIVATION COMPLETE — Task 1 of σ̃ Canonical Closure
## Parent: OPR-30_SIGMA_TILDE_RESOLUTION.md, TSTAR_DEFINITION.md

---

## 0. Executive Summary

**σ_BookI and σ_covariant are dimensionally inequivalent and represent
different physical quantities. They CANNOT be directly identified.**

| Quantity | Definition | Dimensions | Object |
|----------|-----------|------------|--------|
| σ_BookI | m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm² | [M³] | 2D surface energy density |
| σ_covariant | Tension in S = −σ∫d⁴x√{−h} | [M⁴] | 3-brane Nambu-Goto tension |

**Conversion formula (if related):**

```
σ_covariant = σ_BookI / Δ
```

where Δ is the domain-wall thickness in the extra dimension, [Δ] = M⁻¹.

**If unrelated:** σ_BookI is a defect within the brane (nuclear membrane),
while σ_covariant is the brane itself (our 3D universe). These are
geometrically distinct objects at different levels of the hierarchy.

---

## 1. The Two σ-Quantities

### 1.1 σ_BookI: Surface Energy Density

**[Der]** From Companion H (09_companion_H_weak_interactions), the
membrane tension is derived from the energy-scale hypothesis:

```
E_σ = m_e c²/α       [Hypothesis]
σ_BookI = E_σ / r_e²  [Definition]
```

where r_e = αℏ/(m_e c) is the classical electron radius.

Substituting:

```
σ_BookI = (m_e c²/α) × (m_e²c²)/(α²ℏ²) = m_e³c⁴/(α³ℏ²)
```

**Numerical value:**

```
σ_BookI = (0.511)³ / [(7.297 × 10⁻³)³ × (197.3)²]  MeV/fm²
        = 8.82 MeV/fm²
        = 1.41 × 10¹⁸ J/m²
```

**Dimensions in natural units (ℏ = c = 1):**

```
[σ_BookI] = [Energy] / [Area]
           = [M]¹ / [M]⁻²
           = [M]³
```

**SI to natural units conversion:**

```
1 J/m² = 1 kg/s²

1 J   = 6.242 × 10⁹ GeV
1 m   = 5.068 × 10¹⁵ GeV⁻¹
1 m²  = 2.568 × 10³¹ GeV⁻²

1 J/m² = 6.242 × 10⁹ / 2.568 × 10³¹  GeV³
       = 2.431 × 10⁻²² GeV³

σ_BookI = 1.41 × 10¹⁸ × 2.431 × 10⁻²² GeV³
        = 3.43 × 10⁻⁴ GeV³
        ≈ 343 MeV³
```

**Conclusion:** [σ_BookI] = M³. This is energy per unit 2D area.

### 1.2 σ_covariant: 3-Brane Tension in 5D

**[I]** The EDC membrane Σ³ is a 3-dimensional spatial hypersurface
embedded in 5D spacetime (x⁰, x¹, x², x³, y). Its worldvolume is
4-dimensional (3 spatial + 1 time). The brane action is:

```
S_brane = −σ_covariant ∫ d⁴x √{−h}
```

where h_μν is the induced 4D metric on the brane worldvolume.

**[I]** Dimensional analysis:

```
[S_brane] = [M]⁰              (action is dimensionless in ℏ=1)
[d⁴x]    = [M]⁻⁴             (4D coordinate volume)
[√{−h}]  = [M]⁰              (metric determinant, dimensionless)

∴ [σ_covariant] = [M]⁰ / [M]⁻⁴ = [M]⁴
```

**Conclusion:** [σ_covariant] = M⁴. This is energy per unit 3D volume.

### 1.3 Dimensional Gap

```
[σ_covariant] / [σ_BookI] = [M]⁴ / [M]³ = [M]¹
```

**The two quantities differ by exactly one mass dimension.**

They cannot be numerically equal in any unit system. Equating them
produces a dimensionally inconsistent expression.

---

## 2. Proof: The Brane Action Requires [σ] = M⁴

### 2.1 Direct proof

**[I]** For ANY p-brane in D-dimensional spacetime, the Nambu-Goto action is:

```
S = −T_p ∫ d^{p+1}ξ √{−det(h_{ab})}
```

where T_p is the p-brane tension and h_{ab} is the induced metric on the
(p+1)-dimensional worldvolume.

For S to be dimensionless:

```
[T_p] × [M]^{−(p+1)} = [M]⁰
∴ [T_p] = [M]^{p+1}
```

For a 3-brane (p = 3): [T₃] = M⁴.
For a 2-brane (p = 2): [T₂] = M³.

### 2.2 Identification of the EDC brane

The EDC brane Σ³ is a codimension-1 hypersurface in 5D:

```
dim(Σ³) = 5 − 1 = 4  (worldvolume dimensions)
p = 4 − 1 = 3         (spatial dimensions on the brane)
```

Therefore Σ³ is a 3-brane, and its tension has [M⁴].

### 2.3 The TSTAR_DERIVATION_5D.md dimensional error

The existing 5D derivation document writes:

```
S_brane = −∫ d⁴x √{−g} σ
```

and then checks:

```
[S_brane] = [M]⁻⁴ × [M]³ = [M]⁻¹  ← WRONG
```

It then states: "For action to be dimensionless in natural units, we
interpret S_brane as integrated over proper 4D volume, giving [S] = M⁰ ✓"

**This is incorrect.** The "proper 4D volume" interpretation does not
change the dimensional analysis. The coordinates x^μ always contribute
[M]⁻⁴ (whether "proper" or not), because the metric determinant √{−g}
is dimensionless in natural units (it is a pure number rescaling the
coordinate volume element).

**The actual resolution:** [σ] = M⁴ in the brane action, not M³.

---

## 3. Geometric Distinction

### 3.1 Two different geometric objects

**σ_BookI describes a domain wall WITHIN 4D spacetime:**

```
4D spacetime: (t, x¹, x², x³)

Domain wall extends in:  (x¹, x²)     ← 2 spatial dimensions
Localized in:            x³            ← kink profile, thickness Δ

Surface tension = energy per (x¹,x²)-area = ∫ dx³ ρ^{(4D)}(x³)
[σ_wall] = [M]⁻¹ × [M]⁴ = [M]³ ✓
```

**σ_covariant describes the ENTIRE 3D space as a brane in 5D:**

```
5D spacetime: (t, x¹, x², x³, y)

3-brane extends in:  (x¹, x², x³)    ← 3 spatial dimensions
Localized in:        y                ← extra dimension

Brane tension = energy per (x¹,x²,x³)-volume
[σ_brane] = [M]⁴
```

### 3.2 Hierarchy of objects

```
5D BULK
  │
  └── 3-brane Σ³ at y = 0  (tension σ_covariant, [M⁴])
        │
        └── Our 3D space (x¹, x², x³)
              │
              └── Domain wall / membrane  (tension σ_BookI, [M³])
                    │
                    └── 2D surface in 3D space
                          (nuclear membrane, elastic defect)
```

**σ_covariant** is a property of the brane AS A WHOLE — the energy cost
of the brane existing in the bulk.

**σ_BookI** is a property of a DEFECT WITHIN the brane — the energy cost
of a 2D membrane existing within our 3D space.

These are objects at different levels of the geometric hierarchy.

---

## 4. Conversion Formula (If They Are Related)

### 4.1 Under what conditions can they be related?

If the nuclear membrane (domain wall in 4D) is a manifestation of
extra-dimensional physics — specifically, if it corresponds to a
variation in the brane profile in the y-direction — then a conversion
formula exists.

### 4.2 Derivation

Consider a thick brane with y-dependent profile. The 5D energy density is:

```
ρ^{(5D)}(x³, y) = localized near x³ = x³₀  and  y = 0
```

The covariant brane tension is defined by integrating over y:

```
σ_covariant = ∫ dy ρ^{(5D)}(x³₀, y)
```

But ρ^{(5D)} is also localized in x³ with width Δ. The surface
energy density (seen by a 4D observer looking at the 2D domain wall)
is obtained by integrating over BOTH x³ and y:

Wait — no. σ_BookI integrates over x³ only (in 4D):

```
σ_BookI = ∫ dx³ ρ^{(4D)}(x³)
```

The 4D energy density ρ^{(4D)} is itself obtained by integrating the
5D energy density over y:

```
ρ^{(4D)}(x³) = ∫ dy ρ^{(5D)}(x³, y)
```

Therefore:

```
σ_BookI = ∫ dx³ ∫ dy ρ^{(5D)}(x³, y)
```

This is the TOTAL energy per unit 2D area, integrated over both the
kink direction x³ AND the extra dimension y.

Meanwhile, σ_covariant is the energy per unit 3D volume on the brane:

```
σ_covariant = ∫ dy ρ^{(5D)}(y)    [evaluated away from the kink]
```

If the kink adds a PERTURBATION to the brane energy density, then:

```
ρ^{(5D)}(x³, y) = ρ₀^{(5D)}(y) + δρ^{(5D)}(x³, y)
```

where ρ₀ is the homogeneous brane profile and δρ is the kink contribution.

The brane tension is:

```
σ_covariant = ∫ dy ρ₀^{(5D)}(y)
```

The domain wall tension is:

```
σ_BookI = ∫ dx³ ∫ dy δρ^{(5D)}(x³, y) = ∫ dx³ δρ^{(4D)}(x³)
```

**In this decomposition, σ_BookI and σ_covariant are INDEPENDENT quantities.**

σ_covariant is the background brane tension.
σ_BookI is the energy cost of a domain-wall defect on the brane.

### 4.3 Simplified conversion for uniform-in-y kink

If the kink profile is uniform in y (no y-dependence) and the extra
dimension has characteristic length L_y, then:

```
δρ^{(5D)}(x³, y) = δρ^{(4D)}(x³) × δ(y) / 1    [localized at y = 0]
```

In this case the kink is a purely 4D phenomenon on the brane, and
σ_BookI is unrelated to σ_covariant by any simple formula.

### 4.4 The only scenario where conversion exists

If we (incorrectly) identify the domain wall AS the brane itself —
i.e., claim that the kink in x³ IS the mechanism that localizes gravity
in y — then the two would be related by:

```
σ_covariant = σ_BookI / L_⊥
```

where L_⊥ is the characteristic length relating the 2D and 3D extents.

But this identification requires the domain wall to have 3 spatial
dimensions (extend in x¹, x², AND y), which contradicts the definition
of σ_BookI as energy per 2D area (only x¹, x² extent).

---

## 5. Verdict

### 5.1 Primary conclusion

**[Der] σ_BookI and σ_covariant are unrelated physical quantities.**

| Property | σ_BookI | σ_covariant |
|----------|---------|-------------|
| Geometric object | 2D defect within brane | The brane itself |
| Dimensions | [M³] | [M⁴] |
| Physical meaning | Energy per 2D area | Energy per 3D volume |
| Source | m_e³c⁴/(α³ℏ²) | 5D gravity (Israel junction) |
| Role in EDC | Nuclear membrane tension | Cosmological brane tension |
| Role in BLOCK-004 | **None** (does not enter σ̃) | σ in σ̃ = σ/T_* |

### 5.2 Consequence for σ̃

The dimensionless brane tension is:

```
σ̃ = σ_covariant / T_*        [OPR-30-CAN]
```

where:
- σ_covariant has [M⁴]
- T_* must have [M⁴] for σ̃ to be dimensionless

**σ_BookI = 8.82 MeV/fm² does NOT enter this ratio.**

The TSTAR_DEFINITION.md claim that [σ] = [T_*] = M³ is based on the
incorrect identification of σ_BookI with σ_covariant.

### 5.3 Required corrections

| Document | Current | Correction |
|----------|---------|------------|
| TSTAR_DEFINITION.md | [σ] = M³ | [σ_covariant] = M⁴ |
| TSTAR_DERIVATION_5D.md | T_* = C·M₅³ ([M³]) | T_* must have [M⁴]; see §6 |
| OPR-30 §5.3 | "2-brane" | "3-brane (codimension-1 in 5D)" |
| plan.md Task 2 | σ̃ = σ_BookI/T_* → 10⁻⁴⁴ | σ̃ = σ_covariant/T_*, σ_BookI irrelevant |

---

## 6. Corrected T_* Dimension

### 6.1 From Israel junction conditions

With [σ_covariant] = M⁴, the Israel junction condition gives:

```
K_μν⁺ = (κ₅² σ / 18) g_μν

[K] = [M]¹
[κ₅²] = [M]⁻³
[κ₅² σ] = [M]⁻³ × [M]⁴ = [M]¹ ✓
```

Dimensional consistency confirmed.

### 6.2 Characteristic tension scale

For σ̃ = σ_covariant / T_* to be dimensionless:

```
[T_*] = [σ_covariant] = [M⁴]
```

From the Israel junction and bulk cosmological constant:

```
T_* = 6 M₅³ / (8π ℓ)

[T_*] = [M]³ × [M] = [M]⁴ ✓
```

where ℓ is the AdS curvature length, [ℓ] = M⁻¹.

### 6.3 Route B confirmation

From 4D effective theory:

```
M₄² = M₅³ ℓ / C_B          [M²] = [M³·M⁻¹] = [M²] ✓

T_*^{(B)} = M₄² / ℓ²

[T_*^{(B)}] = [M²] / [M⁻²] = [M⁴] ✓
```

### 6.4 Corrected structural form

```
T_* = C · M₅³ / ℓ = C · M₅³ · √{|Λ₅|/6}
```

where C is a dimensionless O(1) geometric factor.

**This replaces the incorrect T_* = C·M₅³ from TSTAR_DERIVATION_5D.md.**

---

## 7. The σ̃ ~ 10⁻⁴⁴ Problem: Resolved

### 7.1 The original problem

Plan.md computed:

```
σ̃ = σ_BookI / T_* = 3.43 × 10⁻⁴ GeV³ / (C × 1.40 × 10⁴⁰ GeV³)
   ≈ 2.45 × 10⁻⁴⁴ / C
```

This used σ_BookI (M³) divided by T_* (M³) — dimensionally consistent
but PHYSICALLY WRONG (σ_BookI is not the brane tension).

### 7.2 Corrected computation

With [σ_covariant] = M⁴ and [T_*] = M⁴:

```
σ̃ = σ_covariant / T_*
```

σ_covariant is NOT known from Book I. It must be determined from the
5D action independently. σ_BookI = 8.82 MeV/fm² is irrelevant to this
computation.

The 10⁻⁴⁴ discrepancy arose from confusing a nuclear surface energy
(energy per 2D area) with a cosmological brane tension (energy per 3D
volume). These are different quantities that should never have been
compared.

### 7.3 What determines σ_covariant?

**[P]** σ_covariant must be derived from the 5D EDC action:

```
S_5D = S_bulk + S_brane + S_GHY

S_bulk = ∫ d⁵x √{−G} (R₅/(2κ₅²) − Λ₅)
S_brane = −σ_covariant ∫ d⁴x √{−g}
S_GHY = (1/κ₅²) ∫ d⁴x √{−g} K
```

The RS fine-tuning condition (flat brane) gives:

```
σ_covariant = 6 M₅³ / (κ₅² ℓ) = 6 M₅³ / (8π ℓ / M₅³)
            = (6 M₅⁶) / (8π ℓ)
            = (3 M₅⁶) / (4π ℓ)
```

Wait — let me redo this. The RS fine-tuning condition is:

```
σ = 6/(κ₅² ℓ)       [Randall-Sundrum 1999]
```

where κ₅² = 8π/M₅³ and ℓ = √{−6/Λ₅}.

```
σ_RS = 6 M₅³ / (8π ℓ) = 3 M₅³ / (4π ℓ)
```

[σ_RS] = M³ × M = M⁴ ✓

**Then T_* = σ_RS is the fine-tuning value itself, giving σ̃ = 1 at
exact RS tuning.** Deviations from fine-tuning give σ̃ ≠ 1.

This is a fundamentally different picture from σ̃ ~ 100.

**[P]** Whether σ̃ = O(1) or σ̃ = O(100) depends on how far the EDC brane
deviates from the RS fine-tuning point. This is an open question for
Task 2.

---

## 8. Dimensional Verification Table

| Expression | Dimensions | Verified |
|-----------|------------|----------|
| σ_BookI = m_e³c⁴/(α³ℏ²) | M³ | ✓ |
| σ_covariant (3-brane in 5D) | M⁴ | ✓ |
| S_brane = −σ_cov ∫ d⁴x √{−h} | M⁴ × M⁻⁴ = M⁰ | ✓ |
| κ₅² σ_cov = (8π/M₅³) × σ_cov | M⁻³ × M⁴ = M¹ | ✓ (= [K]) |
| T_* = C · M₅³/ℓ | M³ × M = M⁴ | ✓ |
| σ̃ = σ_cov / T_* | M⁴/M⁴ = M⁰ | ✓ |
| σ_RS = 6/(κ₅²ℓ) = 3M₅³/(4πℓ) | M³ × M = M⁴ | ✓ |
| K_μν = (κ₅²σ/18) g_μν | M⁻³ × M⁴ = M¹ | ✓ |

All entries pass dimensional analysis.

---

## 9. Epistemic Status

| Claim | Tag | Status |
|-------|-----|--------|
| [σ_BookI] = M³ | [I] | Invariant — from unit conversion |
| [σ_covariant] = M⁴ | [I] | Invariant — from brane action |
| σ_BookI ≠ σ_covariant | [Der] | Proven — dimensional mismatch |
| σ_BookI does not enter σ̃ | [Der] | Consequence of above |
| [T_*] = M⁴ | [I] | From [σ̃] = M⁰ |
| T_* = C·M₅³/ℓ | [Dc] | Structural form (C pending) |
| σ_RS = 3M₅³/(4πℓ) | [I] | RS fine-tuning identity |
| σ_covariant numerical value | [P] | Pending — must derive from 5D action |
| σ̃ numerical value | [P] | Pending — depends on σ_covariant |

---

## 10. Impact on Plan

### 10.1 Task 1 deliverable: COMPLETE

This document answers the question:

> "Task 1 mora derivirati eksplicitnu konverzijsku formulu između
> σ_BookI i σ_covariant, ili dokazati da su nesrodne veličine."

**Answer: They are proven to be dimensionally inequivalent and
represent different geometric objects. No conversion formula exists
without introducing an additional bridging scale.**

### 10.2 Consequence for Task 2

Task 2 (T_* numerical evaluation) must now:

1. Use [T_*] = M⁴ (not M³)
2. Use the corrected structural form T_* = C·M₅³/ℓ
3. Determine σ_covariant from the 5D action (NOT from σ_BookI)
4. The RS fine-tuning point gives σ_covariant = 3M₅³/(4πℓ), hence
   σ̃ = 1 at exact tuning. Deviations need the full EDC action.

### 10.3 Consequence for BLOCK-004

The closure chain α₃ → M_X → g_X → τ_p is UNCHANGED in structure.
Only the input σ̃ is affected:

- OLD: σ̃ was (implicitly or explicitly) computed from σ_BookI
- NEW: σ̃ must be computed from σ_covariant (a 5D gravitational quantity)

σ_BookI = 8.82 MeV/fm² has no role in the BLOCK-004 closure chain.

---

## 11. Firewall Compliance

This document is **Layer A only**:
- No experimental data (PDG, CODATA) used in the dimensional proof
- σ_BookI = 8.82 MeV/fm² appears only as a labeled example
- No SM observables constrain any conclusion

**Guard compliance:**
- G1 (Ontological purity): ✓ — pure dimensional analysis
- G2 (Empirical protocol): ✓ — no experimental calibration
- G3 (Epistemic honesty): ✓ — all tags accurate
- G7 (No contamination): ✓ — no back-calculation

---

**Document Hash:** To be set upon integration into v68.
**Referenced by:** Task 2 (T_* numeric), Task 3 (v68 canonical).
