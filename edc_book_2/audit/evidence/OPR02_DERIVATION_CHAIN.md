# OPR-02: Robin α Derivation Chain

**OPR**: OPR-02 (Robin α from action)
**Date**: 2026-01-25
**Branch**: book2-opr02-robin-alpha-from-action-v1

---

## Goal

Derive the Robin boundary condition parameter α from the 5D action without
importing Standard Model values (no-smuggling policy).

---

## Minimal Action Used in Book 2

### Total Action

```
S = S_bulk + S_brane
```

### Bulk Action [Dc]

```
S_bulk = -1/2 ∫ d⁵x √(-g) (∂_M φ)²
```
- Standard 5D Klein-Gordon action
- No SM inputs
- Status: **[Dc]** (textbook QFT in curved spacetime)

### Brane Action [P]

```
S_brane = -λ/2 ∫ d⁴x √(-h) (∂_μ φ)² δ(ξ - ξ_*)
```
- Brane kinetic term (BKT)
- λ is dimensionless coefficient
- Status: **[P]** (BKT ansatz; λ value not derived from first principles)

---

## Derivation Chain

### Step 1: Action Variation [Dc]

Starting from total action S = S_bulk + S_brane:

```
δS = ∫ d⁵x √(-g) φ □₅ δφ + boundary terms + brane term
```

After integration by parts, the bulk contribution gives:
```
δS_bulk = ∫ d⁵x √(-g) (□₅ φ) δφ + ∫ d⁴x √(-h) (∂_n φ) δφ |_boundary
```

### Step 2: Brane Contribution [Dc]

The BKT variation gives at ξ = ξ_*:
```
δS_brane = λ ∫ d⁴x √(-h) (□₄ φ) δφ |_{ξ=ξ_*}
```

For a 4D mode with momentum p^μ: □₄ φ → -p² φ.

### Step 3: Matching Condition [Dc]

Combining bulk boundary term and brane contribution, stationarity requires:
```
∂_ξ φ|_{ξ_*⁺} - ∂_ξ φ|_{ξ_*⁻} = λ □₄ φ |_{ξ_*} = -λ p² φ
```
**Equation label**: eq:attemptF_matching (13.127)

### Step 4: Z₂ Orbifold Symmetry [Dc]

For Z₂ orbifold (z ↔ -z identification), the field is even under reflection:
```
φ(-ξ) = φ(ξ) ⟹ ∂_ξ φ|_{0⁺} = -∂_ξ φ|_{0⁻}
```

Therefore the jump becomes:
```
2 ∂_ξ φ|_{0⁺} = -λ p² φ|_{0}
```

### Step 5: Robin BC Form [Dc]

Rearranging:
```
∂_ξ φ|_0 + (λ p²/2) φ|_0 = 0
```

This is the **Robin boundary condition**:
```
┌─────────────────────────────────────┐
│  f' + α f = 0   at ξ = 0           │
│                                     │
│  where α = λ p²/2 = λ m²/2         │
└─────────────────────────────────────┘
```
**Equation label**: eq:attemptF_Robin (13.137)

---

## Parameter α: Three Derivation Routes

### Route A: BKT Coefficient [Dc]+[P]

From BKT action variation:
```
α = λ̃ x₁²/2
```
where λ̃ is the dimensionless BKT coefficient and x₁ = mℓ.

**Status**: [Dc]+[P]
- [Dc]: α formula follows from variation
- [P]: λ̃ value is postulated (λ̃ ~ 2-4 needed for target α ~ 8)

### Route B: Israel Junction [Dc]+[P]

From tension-dominated junction:
```
α ~ κ₅² σ ℓ
```
where κ₅² = 8πG₅ and σ is brane tension.

**Status**: [Dc]+[P]
- [Dc]: Structure from Israel matching
- [P]: κ₅, σ values require Part I closure

### Route C: Thick-Brane Smoothing [Dc]+[P]

When delta-function brane is smoothed to width δ:
```
α = C_geom · ℓ/δ
```
where C_geom ~ O(1) is a geometric factor.

With identification **δ = R_ξ** (brane thickness = diffusion scale):
```
α = ℓ/δ = (2π R_ξ)/R_ξ = 2π ≈ 6.3
```

**Status**: [Dc]+[P]
- [Dc]: α ~ ℓ/δ from inner/outer matching
- [P]: δ = R_ξ identification is postulated

---

## No-Smuggling Verification

### Forbidden Inputs (NOT used)

| Input | Value | Status |
|-------|-------|--------|
| M_W | 80 GeV | ✗ NOT USED |
| G_F | 1.17×10⁻⁵ GeV⁻² | ✗ NOT USED |
| v | 246 GeV | ✗ NOT USED |
| g₂ | 0.65 | ✗ NOT USED |
| sin²θ_W | 0.23 | ✗ NOT USED |

### Allowed Inputs (used)

| Input | Source | Status |
|-------|--------|--------|
| ℓ = 2π R_ξ | EDC geometry | [Dc] (Attempt E) |
| δ = R_ξ | EDC diffusion | [P] (postulated) |
| C_geom ~ 1 | Matching theory | [Dc] |

**Verdict**: ✓ No-smuggling compliant

---

## Proof Obligations Checklist

| Obligation | Status | Evidence |
|------------|--------|----------|
| Action → variation is mathematically valid | ✓ [Dc] | Standard calculus of variations |
| Boundary term correctly identified | ✓ [Dc] | eq:attemptF_matching |
| Z₂ symmetry correctly applied | ✓ [Dc] | Orbifold standard |
| Robin form is consequence, not ansatz | ✓ [Dc] | eq:attemptF_Robin |
| α coefficient derived (not smuggled) | △ [Dc]+[P] | Requires one [P] choice |
| No SM values used in α | ✓ | No-smuggling verified |

---

## OPR-02 Closure Assessment

### What Is DERIVED [Dc]

1. Robin BC **form** f' + αf = 0 follows from action variation
2. Robin BC **structure** (mixed derivative + value) is a consequence of BKT
3. α has dimensional form α ~ ℓ/δ from thick-brane matching
4. α has parametric form α = λ̃m²/2 from BKT coefficient

### What Is POSTULATED [P]

**ONE of the following is required to fix α numerically:**

| Route | Postulate | Natural α |
|-------|-----------|-----------|
| A | λ̃ ~ 2-4 (BKT coefficient) | α ~ 8 |
| B | κ₅²σℓ ~ 10 (junction params) | α ~ 10 |
| C | δ = R_ξ (brane thickness) | α = 2π ≈ 6.3 |

### What Remains OPEN

- Unique derivation of δ = R_ξ from brane microphysics
- Derivation of BKT coefficient λ̃ from membrane stiffness
- Connection to Part I diffusion/conductivity

---

## OPR-02 VERDICT

```
┌──────────────────────────────────────────────────────────────┐
│  OPR-02: PARTIAL [Dc]+[P]                                    │
│                                                              │
│  Robin BC FORM is derived from 5D action.                    │
│  Robin BC PARAMETER α requires ONE postulate:                │
│    • Route C (recommended): δ = R_ξ → α = 2π                 │
│                                                              │
│  Upgrade condition:                                          │
│    Derive δ = R_ξ from Part I brane physics                  │
│    OR derive λ̃ from membrane properties                     │
└──────────────────────────────────────────────────────────────┘
```

---

## Equation Labels Referenced

| Label | Eq Number | Location |
|-------|-----------|----------|
| eq:attemptF_BKT | 13.120 | ch11_opr20_attemptF |
| eq:attemptF_Israel | 13.111 | ch11_opr20_attemptF |
| eq:attemptF_matching | 13.127 | ch11_opr20_attemptF |
| eq:attemptF_Robin | 13.137 | ch11_opr20_attemptF |
| eq:attemptF_alpha_BKT | 13.138 | ch11_opr20_attemptF |
| eq:attemptG_alpha_thick | 13.125 | ch11_opr20_attemptG |
| eq:attemptH_robin_from_action | 13.162 | ch11_opr20_attemptH |

---

*OPR-02 Derivation Chain Complete*
*Status: PARTIAL — Robin form [Dc], coefficient requires [P]*
