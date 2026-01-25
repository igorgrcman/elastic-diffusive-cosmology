# OPR-02: Robin α Derivation Chain

**OPR**: OPR-02 (Robin α from action)
**Date**: 2026-01-25 (Updated with OPR-04 verdict)
**Branch**: book2-opr04-delta-equals-Rxi-v1

---

## Dependency Statement

**Critical dependency on OPR-04**: Route C (the recommended path) depends on the
identification δ ≡ R_ξ, which is **[P]** and remains **OPEN** per OPR-04.

**OPR-02 cannot be CLOSED unless one of the following is satisfied:**
1. **OPR-04 is CLOSED** — derivation of δ = R_ξ from brane microphysics, OR
2. **λ̃ is derived** — BKT coefficient from membrane physics (removes Route C dependency)

See: `audit/evidence/OPR04_CLOSURE_REPORT.md` for full OPR-04 verdict.

---

## Closure Gates (from OPR-04)

```
┌──────────────────────────────────────────────────────────────┐
│  CLOSURE GATES FOR δ = R_ξ IDENTIFICATION                   │
│  (All must be satisfied OR alternative route found)          │
├──────────────────────────────────────────────────────────────┤
│  (i)   Derive R_ξ from 5D action without SM inputs   [OPEN] │
│  (ii)  Formal boundary-layer theorem: δ = f(R_ξ)     [OPEN] │
│  (iii) Unique-scale proof: R_ξ is only sub-EW scale  [OPEN] │
│  (iv)  δ-robustness: outputs insensitive to ±2×     [OPEN] │
├──────────────────────────────────────────────────────────────┤
│  Cross-reference: audit/evidence/OPR04_CLOSURE_REPORT.md    │
│  Cross-reference: audit/evidence/OPR04_DERIVATION_CHAIN.md  │
└──────────────────────────────────────────────────────────────┘
```

**Note**: Gate (iv) is a robustness test, not a derivation. If satisfied, it
demonstrates that the physics is insensitive to the exact δ/R_ξ ratio, reducing
the criticality of the identification without proving it.

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

**Requires one [P] input**: λ̃ (BKT coefficient)

**Note**: If λ̃ can be derived from membrane stiffness/conductivity, this route
would close OPR-02 WITHOUT requiring OPR-04 closure.

### Route B: Israel Junction [Dc]+[P]

From tension-dominated junction:
```
α ~ κ₅² σ ℓ
```
where κ₅² = 8πG₅ and σ is brane tension.

**Status**: [Dc]+[P]
- [Dc]: Structure from Israel matching
- [P]: κ₅, σ values require Part I closure

**Requires σ/κ₅ anchor from Part I** (OPR-01 related)

### Route C: Thick-Brane Smoothing — RECOMMENDED [P]

When delta-function brane is smoothed to width δ:
```
α = C_geom · ℓ/δ
```
where C_geom ~ O(1) is a geometric factor.

With identification **δ = R_ξ** (brane thickness = diffusion scale):
```
α = ℓ/δ = (2π R_ξ)/R_ξ = 2π ≈ 6.3
```

**Status**: [Dc]+[P] — **RECOMMENDED but cannot upgrade to [Dc] until OPR-04 CLOSED**
- [Dc]: α ~ ℓ/δ from inner/outer matching
- [P]: δ = R_ξ identification is postulated (OPR-04 verdict: OPEN)

**Blocking dependency**: OPR-04 (δ ≡ R_ξ teleport) — all four closure gates OPEN.
See `audit/evidence/OPR04_CLOSURE_REPORT.md`.

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

## δ-Robustness Plan (Closure Gate iv) [OPEN]

This section outlines a robustness test that, if passed, would demonstrate that
key physics outputs are insensitive to the exact δ/R_ξ identification.

**Status**: [OPEN] — Plan only, no computations performed.

### 1. Formulas Sensitive to δ

The following equations in Book 2 depend on δ (directly or via α = ℓ/δ):

| Equation | Location | Dependence |
|----------|----------|------------|
| eq:attemptH_alpha_ell_delta | CH13 §13.2.8 | α = C_geom · ℓ/δ |
| eq:attemptH_alpha_2pi | CH13 §13.2.8 | α = 2π (assumes δ = R_ξ) |
| Robin eigenvalue equation | CH13 §13.2.3 | tan(x) = 2αx/(x²−α²) |
| Ground state x₁ | BVP solution | x₁(α) monotonic in α |

### 2. Parameter Sweep Specification

**Sweep**: δ → δ × {1/2, 1, 2} (i.e., α → {2α, α, α/2})

**Invariants to monitor**:
- Ground state eigenvalue x₁
- Mediator mass m_φ = x₁/ℓ
- Overlap integral I₄ (if computed)
- Derived G_F (if chain complete)

### 3. Robustness Criterion

**Definition**: δ-robust iff key observables change by **< 5%** when δ varies by
factor of 2 in either direction.

**Acceptance**:
- If x₁ varies < 5%: PARTIAL robustness (eigenvalue stable)
- If G_F varies < 5%: STRONG robustness (observable stable)
- If variation > 20%: NOT robust — δ = R_ξ is critical and must be derived

**Note**: This test does NOT derive δ = R_ξ; it only quantifies sensitivity.
Passing Gate (iv) reduces urgency of OPR-04 closure but does not eliminate it.

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
│  Route C status: recommended [P]                             │
│    Cannot upgrade to [Dc] until OPR-04 CLOSED               │
│                                                              │
│  CLOSURE REQUIRES:                                           │
│    (a) OPR-04 CLOSED (derive δ = R_ξ), OR                   │
│    (b) λ̃ derivation (BKT route, bypasses δ = R_ξ)          │
│                                                              │
│  Cross-ref: audit/evidence/OPR04_CLOSURE_REPORT.md          │
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
