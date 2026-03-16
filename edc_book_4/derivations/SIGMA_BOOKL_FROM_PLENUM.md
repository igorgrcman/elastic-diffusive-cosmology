# Prove-or-Fail: σ_BookI from Plenum Energetics

## Status: FAIL — ρP cannot be derived from the 5D action
## Date: 2026-03-16
## Layer: A (structural analysis; Layer B for numerical cross-checks)
## Depends on: P1-P5 (EDC postulates), v21 (KK gap), v68 (σ̃ = 1),
##             Paper 2 App. D.9, G5C_DERIVATION_AUDIT.md

---

## 1. Executive Verdict

**σ_BookI CANNOT be derived from the 5D EDC action.**

The formula σ = 2πRξ²ρP (Paper 2, App. D.9) is structurally [Dc] —
the derivation is valid given inputs — but ρP itself is an irreducible
free parameter (Postulate 5). Every route attempting to derive ρP
from the 5D action fails:

| Route | Formula | σ_predicted | σ_target | Factor off |
|-------|---------|-------------|----------|------------|
| P1 (bulk Λ₅) | ρP = 2\|Λ₅\|M₅³ | ~10⁴⁰ GeV³ | 0.227 GeV³ | 10⁴¹ |
| P2 (Casimir) | ρP = π²/(720 L⁵) | ~10³ GeV³ | 0.227 GeV³ | 10⁴ |
| P3 (back-reaction) | σ_covariant [M⁴] | wrong dimensions | [M³] target | N/A |

**Root cause:** σ_BookI is a nuclear-scale quantity (~MeV). The 5D
gravitational action operates at the scale M₅ ~ 5.6 × 10¹² GeV.
No mechanism in the action bridges 40 orders of magnitude from
gravitational to nuclear scales. This is a variant of the hierarchy
problem.

**Additionally:** The Rξ identification is ambiguous. Paper 2 uses
Rξ = 136 r_e ≈ 383 fm; the KK gap identification (v21) gives
Rξ = π/M_Z ≈ 0.007 fm — a factor of 56,000 discrepancy. This
ambiguity makes the formula σ = 2πRξ²ρP doubly underdetermined.

**Impact:** σ_BookI remains [Cal] (computed from α, m_e, r_e) or
equivalently [P] (postulated in P6). The V2 priority map's
highest-value derivation target is blocked. The next priority
should shift to Rξ reconciliation or acceptance of σ as [P].

---

## 2. Route P1: ρP from Bulk Cosmological Constant

### 2.1 The route

In RS geometry, the bulk is anti-de Sitter with:

```
Λ₅ = -6/ℓ²     (AdS₅ curvature)
```

The 5D vacuum energy density (the "Plenum" energy):

```
ρP = 2|Λ₅| M₅³ = 12 M₅³/ℓ²
```

Using ℓ = L = π/M_Z (from v21) and M₅³ = M̄_Pl²/L:

```
ρP = 12 M̄_Pl² / L³ = 12 M̄_Pl² M_Z³ / π³
```

### 2.2 Resulting σ

```
σ_P1 = 2π Rξ² ρP = 2π (π/M_Z)² × 12 M̄_Pl²/L³
     = 24π M₅³
     = 24π × (5.56 × 10¹²)³
     = 1.30 × 10⁴⁰ GeV³
```

### 2.3 Numerical comparison

```
σ_P1     = 1.30 × 10⁴⁰ GeV³
σ_target = 0.227 GeV³ (= 8.82 MeV/fm²)

Ratio: 5.7 × 10⁴⁰ — off by 41 orders of magnitude.
```

### 2.4 Diagnosis

Route P1 fails because it identifies ρP with the AdS₅ vacuum energy,
which is at the gravitational scale:

```
ρP ~ M₅⁵ ~ (10¹² GeV)⁵ ~ 10⁶³ GeV⁵
```

But σ_BookI requires:

```
ρP_needed ~ σ/(2πRξ²) ~ 0.227/(2π × 0.0345²) ~ 30 GeV⁵
```

The gravitational vacuum energy exceeds the needed ρP by 10⁴⁰.
This is the hierarchy problem: the bulk gravitational sector
operates at M₅, not at the MeV scale.

**Structural insight:** The formula σ_P1 = 24π M₅³ shows that
any route connecting σ to the 5D gravitational action produces
σ ~ M₅³ ~ 10³⁸ GeV³. The target σ_BookI ~ 0.23 GeV³ is 10³⁸
times smaller. No O(1) coefficient adjustment can bridge this gap.

---

## 3. Route P2: ρP from Casimir Energy

### 3.1 The route

Compactification on S¹ of radius R produces Casimir vacuum energy:

```
ρ_Casimir = -C_N × π²/(720 L⁵)     per degree of freedom
```

where L = 2πR is the circumference and C_N depends on boundary
conditions (C = 1 for periodic scalar, C = 7/8 for fermion, etc.).

### 3.2 Resulting σ

With L = Rξ = π/M_Z:

```
σ_P2 = 2π Rξ² × π²/(720 Rξ⁵) = π³/(360 Rξ³)
     = π³/(360) × (M_Z/π)³
     = M_Z³/360
     = 758,241 / 360 GeV³
     = 2.1 × 10³ GeV³
```

### 3.3 Numerical comparison

```
σ_P2     = 2.1 × 10³ GeV³     (single dof, exact Casimir coeff)
σ_target = 0.227 GeV³

Ratio: 9.3 × 10³ — off by ~4 orders of magnitude.
```

### 3.4 Diagnosis

Route P2 is interesting because it gives σ ~ M_Z³, which is
much closer to σ_BookI than Route P1 (M₅³). The scale hierarchy
is "only" 10⁴ rather than 10⁴¹.

However:
- The Casimir energy is the wrong sign (negative → repulsive)
- Multiple degrees of freedom would increase, not decrease, the gap
- The coefficient 1/360 is not adjustable
- Even with favorable signs, the 10⁴ gap cannot be bridged by O(1) factors

**Structural insight:** σ_P2 ~ M_Z³/N where N is a small number.
Since M_Z³ ~ 7.6 × 10⁵ GeV³ and σ_BookI ~ 0.23 GeV³, we need
N ~ 3.3 × 10⁶ — far too large for any coefficient from field theory.

### 3.5 What if we use Paper 2's Rξ = 136 r_e?

With Rξ = 136 r_e = 1.94 GeV⁻¹ (much larger than π/M_Z):

```
σ_P2' = π³/(360 × 1.94³)
      = π³/(360 × 7.30)
      = 0.0118 GeV³ = 11.8 MeV³
```

This is closer (factor ~19 off from 227 MeV³) but:
- Uses the Paper 2 Rξ, not the KK gap Rξ
- Still the wrong sign
- Still requires fine-tuning of the coefficient
- Casimir energy is a quantum correction, not the leading ρP

---

## 4. Route P3: Back-Reaction Energy

### 4.1 The route

The brane back-reacts on the bulk geometry through the Israel
junction conditions. The bulk near-brane energy might contribute
to σ_BookI.

### 4.2 Why it fails

The back-reaction produces σ_covariant [M⁴] through the Israel
junction:

```
σ_RS = 3M₅³/(4πℓ) = 1.19 × 10³⁹ GeV⁴
```

This is a [M⁴] quantity (energy per 3-volume), not a [M³] quantity
(energy per 2-area). It is σ_covariant, not σ_BookI.

**The two σ's are different physical objects** (proven in Task 1 of
the σ̃ audit):

| Symbol | Dimensions | Physical meaning |
|--------|-----------|------------------|
| σ_covariant | [M⁴] | 4D brane tension (RS/Israel) |
| σ_BookI | [M³] | 2D nuclear membrane tension |

No dimensional manipulation converts M⁴ to M³ without introducing
a new scale. The back-reaction is inherently a gravitational-sector
quantity and cannot produce the nuclear-scale σ_BookI.

---

## 5. Numerical Comparison Table

### 5.1 All routes with Rξ = π/M_Z (v21)

| Route | ρP formula | ρP (GeV⁵) | σ = 2πRξ²ρP (GeV³) | σ_target (GeV³) | Factor off |
|-------|-----------|-----------|---------------------|-----------------|------------|
| P1 | 2\|Λ₅\|M₅³ | 1.74 × 10⁴² | 1.30 × 10⁴⁰ | 0.227 | 5.7 × 10⁴⁰ |
| P2 (per dof) | π²/(6L⁵) | 3.39 × 10⁷ | 2.53 × 10⁵ | 0.227 | 1.1 × 10⁶ |
| P2 (exact) | π²/(720L⁵) | 2.82 × 10⁵ | 2.11 × 10³ | 0.227 | 9.3 × 10³ |
| P3 | σ_RS/L | [M⁴] | wrong dims | — | N/A |
| **Needed** | — | **30.4** | **0.227** | **0.227** | **1** |

### 5.2 With Rξ = 136 r_e (Paper 2)

| Route | ρP needed (GeV⁵) | ρP from action | Factor off |
|-------|-------------------|----------------|------------|
| P1 | 9.56 × 10⁻³ | 1.74 × 10⁴² | 1.8 × 10⁴⁴ |
| P2 (exact) | 9.56 × 10⁻³ | 1.02 × 10⁻¹ | ~11 |
| **Needed** | **9.56 × 10⁻³** | — | — |

### 5.3 Rξ ambiguity

The formula σ = 2πRξ²ρP is doubly underdetermined because Rξ
itself has two incompatible identifications:

| Identification | Rξ value | Source | Status |
|---------------|----------|--------|--------|
| KK mass gap | π/M_Z = 0.007 fm | v21 [I+BL] | Used in BLOCK-003/004 |
| Geometric ratio | 136 r_e = 383 fm | Paper 2 [Dc] | Used in α derivation |

These differ by a factor of 56,000. **Any derivation of σ from ρP
inherits this ambiguity.** The two Rξ values cannot both be correct;
they refer to different physical length scales:

- Rξ (KK) = compactification radius of the extra dimension
- Rξ (Paper 2) = correlation length of the membrane fluid

The formula σ = 2πRξ²ρP uses "Rξ" in the Paper 2 sense (membrane
thickness ≈ correlation length), not the KK compactification sense.

---

## 6. Epistemic Status

### 6.1 What the formula σ = 2πRξ²ρP actually is

The derivation (Paper 2, App. D.9) proceeds:

1. ρP is the 5D Plenum energy density [P5 — Postulate 5]
2. Pressure integrated over compact dimension: P_eff = 2πRξ ρP [M]
3. Membrane thickness δ = Rξ [P — Postulate]
4. Tension = Pressure × Thickness: σ = P_eff × δ = 2πRξ²ρP [Dc]

**Step 3 is the critical weak point.** The identification δ = Rξ is
a postulate. It converts one free parameter (ρP) into another
(σ/Rξ²), without reducing the parameter count.

### 6.2 Is ρP derivable?

**No.** The Plenum energy density is introduced as Postulate 5 in
EDC's axiomatic structure. It is:

> "a fundamental parameter of the theory" (Chapter 2, Postulate 3)

The 5D action contains no term that fixes ρP at the MeV scale.
The gravitational sector operates at M₅ ~ 10¹² GeV, producing
ρP values 40 orders of magnitude too large.

### 6.3 Classification

```
σ = 2πRξ²ρP

Input ρP:  [P] — Postulate 5 (irreducible)
Input Rξ:  [I+BL] or [P] — identification dependent
Input δ=Rξ: [P] — Postulate
Formula:   [Dc] — conditional on inputs
Result σ:  [P] — cannot exceed [P] status of inputs
```

### 6.4 Comparison with g₅^(C)

σ_BookI has the same epistemic status as g₅^(C) (see OPR-32):

| Parameter | Why irreducible | What fixes it |
|-----------|----------------|---------------|
| g₅^(C) | Gauge/gravity sectors independent | α_s(M_Z) = 0.118 |
| σ_BookI | Gravitational action at M₅ scale; nuclear physics at MeV scale | σ = m_e³c⁴/(α³ℏ²) [Cal] |
| ρP | Postulate 5; no 5D action term fixes it at MeV⁵ | Inferred from σ and Rξ |

---

## 7. Impact on Downstream Claims

### 7.1 What this means for the V2 priority map

The V2 priority map (commit e1fa539) identified σ_BookI derivation
as the highest-value next step. This prove-or-fail shows:

**σ_BookI is an irreducible [P] parameter of EDC, analogous to
g₅^(C).** It cannot be derived from the 5D action.

### 7.2 What changes

| Priority item | V2 status | Updated status |
|--------------|-----------|----------------|
| σ_BookI from Plenum | Rank 1 (highest) | BLOCKED — ρP is [P] |
| Rξ from 5D diffusion | Rank 2 | Now Rank 1 (highest remaining) |
| V(q) from 5D action | Rank 3 | Now Rank 2 |

### 7.3 Rξ ambiguity as the new critical problem

The discovery that Rξ (KK) and Rξ (Paper 2) differ by factor
56,000 is arguably more important than the σ derivation failure.
It suggests that:

1. Rξ in σ = 2πRξ²ρP is NOT the compactification radius
2. The Paper 2 framework and the BLOCK-003/004 framework use
   "Rξ" for different physical quantities
3. Reconciling these two Rξ identifications is a prerequisite
   for any consistent parameter closure

### 7.4 EDC free parameter count

After today's audit and the g₅ audit, the irreducible free
parameters of EDC are:

| Parameter | Status | Fixed by |
|-----------|--------|----------|
| σ_BookI | [P] | α, m_e, r_e (calculation) |
| ρP | [P] | σ and Rξ (inferred) |
| g₅^(C) | [P] | α_s(M_Z) (measurement) |
| Rξ | [I+BL] | M_Z (identification) or r_e/α (calculation) |
| M₅ | [I+BL] | M̄_Pl, ℓ (hierarchy relation) |

Of these, σ_BookI and g₅^(C) are genuinely irreducible: no EDC
axiom or 5D action term determines them. ρP is determined by
σ and Rξ but not independently.

---

## 8. OPR Update

### OPR-32 update (minor)

Add σ_BookI to the list of irreducible parameters:

> g₅^(C) and σ_BookI are both irreducible free parameters of EDC.
> The gauge coupling requires α_s(M_Z); the nuclear tension requires
> {α, m_e, r_e} or equivalently σ = m_e³c⁴/(α³ℏ²).

### New finding: Rξ ambiguity

The two incompatible Rξ identifications should be flagged:

| ID | Rξ value | Source | Used in |
|----|----------|--------|---------|
| Rξ-KK | π/M_Z = 0.007 fm | v21 KK gap [I+BL] | BLOCK-003/004, RS geometry |
| Rξ-P2 | 136 r_e = 383 fm | Paper 2 α derivation [Dc] | σ formula, α formula |

**These cannot both be the compactification radius.** Either:
- Rξ-P2 is a different physical scale (correlation length, not compactification), or
- The Paper 2 geometric ratio α = r_e/(Rξ+r_e) uses a non-compact "Rξ", or
- One of the identifications is wrong

This merits investigation but is beyond the scope of this prove-or-fail.

---

## 9. What Survives

Despite the FAIL verdict, several structural results survive:

| Result | Status | Why it survives |
|--------|--------|-----------------|
| σ = 2πRξ²ρP | [Dc] | Formula is correct given inputs; inputs are [P] |
| [ρP] = M⁵ | [I] | Dimensional analysis is identity |
| σ_BookI [M³] ≠ σ_covariant [M⁴] | [Der] | Proven in Task 1 of σ̃ audit |
| ρP ~ M₅⁵ would give σ ~ M₅³ | [Der] | Any gravitational ρP fails by 10⁴⁰ |
| Casimir ρP ~ 1/L⁵ gives σ ~ M_Z³ | [Der] | Closest route but still 10⁴ off |

---

## 10. Verdict

**FAIL.** ρP is an irreducible free parameter of EDC (Postulate 5).
No route from the 5D action produces ρP at the correct scale.
The gravitational sector operates at M₅ ~ 10¹² GeV; the nuclear
membrane operates at MeV. The gap of ~10⁴⁰ cannot be bridged by
any mechanism within the current 5D action.

σ_BookI = 8.82 MeV/fm² is a [Cal] quantity computed from
{α, m_e, r_e}, or equivalently a [P] quantity (Postulate 6).
It cannot be promoted to [Der] within the current EDC framework.

The formula σ = 2πRξ²ρP is valid [Dc] but merely redistributes
the free parameter: instead of postulating σ [P6], one postulates
ρP [P5]. The parameter count is not reduced.
