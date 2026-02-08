# ⚠️ RETRACTION NOTICE (DO NOT USE AS DERIVATION)

**Status:** RETRACTED / HISTORICAL NOTE — this file contains a **known incorrect inference**.

## What was wrong

This note claimed that **ξ-boundary conditions (BC)** (via the linearized Green-function / mode-sum potential) can produce an **effective attraction** and thus **force a minimum** of V(d).

That claim is **false**: in the linearized regime, for Neumann/Robin/Dirichlet BC the interaction remains **monotonically increasing**, i.e. V'_lin(d) > 0 for all d > 0.

**The self-contradiction is visible in the original text:**
- Line 254: "Both terms are positive → V is monotonically increasing → **NO MINIMUM!**"
- Line 441: "BC **FORCE** the inter-defect potential V(d) to have a minimum" ← **WRONG**

## Correct understanding (current)

- **BC provide scale and mode structure (δ), not attraction.**
- **A minimum (if present) requires core/topology physics** (winding conservation / core overlap), not ξ-BC in the linearized model.
- The K₀ terms contribute negative VALUES but POSITIVE derivative (less repulsive ≠ attractive).

## Canonical corrections (use these instead)

- `aside_p2_closure_v3/`
  - `01_SIGN_AND_MONOTONICITY.md` — no-minimum result for linearized model
  - `02_CORE_REPULSION_FROM_FUNCTIONAL.md` — core/topology repulsion as d→0
  - `05_VERDICT.txt` — summary: BC ≠ attraction

- `aside_frozen_brane_bc_v1/`
  - `05_SIGN_AND_MINIMUM_ANALYSIS.md` — V'_lin(d) > 0 for ALL BC scenarios
  - `06_RELATION_TO_RADIAL_STEP_FROZEN.md` — distinction: radial-frozen vs brane-frozen
  - `07_VERDICT.txt` — "BC create attraction" is FALSE

- `aside_m5_to_z6_proof/ADDENDUM_V_r_DERIVATION.md` — explicit error statement and replacement chain

## Action

Treat all "BC-induced attraction / BC-forced minimum" statements in this file as **invalid**.
This file is kept only for forensic traceability; it must not be cited as a valid derivation.

---

# ORIGINAL CONTENT BELOW (HISTORICAL — DO NOT USE)

---

# DERIVATION: Inter-Defect Potential V(r) from Thick-Brane Boundary Conditions

**Goal:** Derive that two topological defects in a thick brane have interaction potential V(r) with a stable minimum at r₀ > 0, WITHOUT postulating the potential form.

**Status:** DERIVATION ATTEMPT [Der]

---

## 1. SETUP

### 1.1 Geometry

The thick brane occupies:
- 4D spacetime coordinates: x^μ (μ = 0,1,2,3)
- Fifth dimension: ξ ∈ [0, δ] (brane thickness δ)

We work in the transverse 2D plane (x¹, x²) = (x, y), using polar coordinates (r, θ).

### 1.2 Field Content

Consider a complex scalar field Φ(r, θ, ξ) representing the brane order parameter.
(This can be generalized to gauge fields; the key physics is the same.)

**Action:**
```
S = ∫ d²r dξ [ ½|∂_r Φ|² + ½|∂_θ Φ|²/r² + ½|∂_ξ Φ|² + U(|Φ|) ]
```

where U(|Φ|) is a symmetry-breaking potential with minimum at |Φ| = v.

### 1.3 Topological Defect (Vortex)

A single vortex at the origin has the ansatz:
```
Φ(r, θ, ξ) = f(r, ξ) e^{inθ}
```
where n ∈ ℤ is the winding number (topological charge).

**Boundary conditions in ξ:**
- At ξ = 0: Robin BC from Israel junction
- At ξ = δ: Robin BC or Neumann

For concreteness, we use Neumann BC (flux cannot escape):
```
∂_ξ Φ|_{ξ=0} = 0,    ∂_ξ Φ|_{ξ=δ} = 0
```

### 1.4 Single Vortex Profile

The profile f(r, ξ) satisfies:
```
-∂²f/∂r² - (1/r)∂f/∂r + n²f/r² - ∂²f/∂ξ² + U'(f) = 0
```

**Asymptotic behavior:**
- As r → 0: f → 0 (forced by winding term n²f/r²)
- As r → ∞: f → v (vacuum value)
- Core radius: a ~ 1/√(U''(v)) (coherence length)

---

## 2. TWO-VORTEX INTERACTION

### 2.1 Configuration

Place two vortices at positions:
- Vortex 1 at (r₁, θ₁) = (0, 0) with winding n₁ = +1
- Vortex 2 at (r₂, θ₂) = (d, 0) with winding n₂ = +1

Separation: d = |r₂ - r₁|

### 2.2 Energy Decomposition

Total energy:
```
E_total(d) = E₁ + E₂ + V_int(d)
```

where:
- E₁, E₂ = self-energies of individual vortices
- V_int(d) = interaction energy (what we want to calculate)

### 2.3 Green's Function Method

The interaction energy can be computed from the overlap of the fields:
```
V_int(d) = ∫ d²r dξ [ ∇Φ₁* · ∇Φ₂ + ∇Φ₁ · ∇Φ₂* + nonlinear terms ]
```

For well-separated vortices (d >> a), the dominant contribution comes from the linear overlap.

---

## 3. GREEN'S FUNCTION IN THICK BRANE

### 3.1 Mode Expansion

With Neumann BC at ξ = 0 and ξ = δ, the ξ-dependence expands in modes:
```
Φ(r, θ, ξ) = Σ_{m=0}^∞ φ_m(r, θ) cos(mπξ/δ)
```

Each mode φ_m satisfies a 2D equation with effective mass:
```
(-∇²_2D + m²_m) φ_m = source
```
where m_m = mπ/δ.

### 3.2 2D Green's Functions

**Zero mode (m = 0):**
```
G₀(r) = -(1/2π) ln(r/L)
```
This is the 2D Coulomb potential (logarithmic).

**Massive modes (m ≥ 1):**
```
G_m(r) = (1/2π) K₀(m_m r)
```
where K₀ is the modified Bessel function of the second kind.

**Asymptotic behavior:**
- K₀(x) ~ -ln(x) as x → 0
- K₀(x) ~ √(π/2x) e^{-x} as x → ∞

### 3.3 Full Green's Function

The complete Green's function for the thick brane:
```
G(r; ξ, ξ') = (1/δ) G₀(r) + (2/δ) Σ_{m=1}^∞ cos(mπξ/δ) cos(mπξ'/δ) G_m(r)
```

---

## 4. INTERACTION ENERGY CALCULATION

### 4.1 Vortex-Vortex Interaction

For two vortices with windings n₁, n₂, the interaction energy is:
```
V_int(d) = 2π n₁ n₂ ∫₀^δ dξ ∫₀^δ dξ' G(d; ξ, ξ')
```

Substituting the mode expansion:
```
V_int(d) = 2π n₁ n₂ [ (δ/1) G₀(d) + 2 Σ_{m=1}^∞ (δ/m²π²) δ²/δ² G_m(d) ]
```

After simplification:
```
V_int(d) = 2π n₁ n₂ δ [ -(1/2π) ln(d/L) + (1/π) Σ_{m=1}^∞ (1/m²) K₀(mπd/δ) ]
```

### 4.2 Final Form

**Interaction potential:**
```
V(d) = -n₁ n₂ δ [ ln(d/L) - 2 Σ_{m=1}^∞ (1/m²) K₀(mπd/δ) ]
```

For same-sign vortices (n₁ n₂ > 0):

**Defining:**
```
V(d) = V_log(d) + V_BC(d)
```
where:
- V_log(d) = +n₁ n₂ δ ln(d/L) — logarithmic repulsion
- V_BC(d) = -2 n₁ n₂ δ Σ_{m=1}^∞ (1/m²) K₀(mπd/δ) — BC-induced attraction

---

## 5. EXISTENCE OF MINIMUM

### 5.1 Asymptotic Analysis

**At small d << δ:**
```
K₀(mπd/δ) ≈ -ln(mπd/2δ) - γ_E
```
where γ_E is Euler's constant.

Sum: Σ (1/m²) ln(m) converges, so V_BC(d) ~ -C₁ ln(d) + const.

Total: V(d) ≈ +n₁ n₂ δ ln(d) + C₁ n₁ n₂ δ ln(d) + const.

For |C₁| < 1: **V(d) → +∞ as d → 0** (net repulsion)

**At large d >> δ:**
```
K₀(mπd/δ) ~ √(δ/2πmd) e^{-mπd/δ}
```

The sum is dominated by m = 1:
V_BC(d) ≈ -2 n₁ n₂ δ √(δ/2πd) e^{-πd/δ}

Total: V(d) ≈ +n₁ n₂ δ ln(d/L) — slowly growing logarithm

**At intermediate d ~ δ:**
The K₀ terms are O(1) and contribute significantly.

### 5.2 Derivative Analysis

```
dV/dd = n₁ n₂ δ [ 1/d + 2π/δ Σ_{m=1}^∞ (1/m) K₁(mπd/δ) ]
```

where K₁(x) = -dK₀/dx > 0.

**At small d:**
dV/dd > 0 (positive, since 1/d dominates)

**At large d:**
dV/dd > 0 (positive, since ln term dominates)

**At d ~ δ:**
The K₁ terms are negative contributions (since K₁ > 0 but enters with + sign... wait, let me recalculate)

Actually: dK₀/dx = -K₁(x), so:
```
d[K₀(mπd/δ)]/dd = -(mπ/δ) K₁(mπd/δ)
```

Therefore:
```
dV_BC/dd = +2 n₁ n₂ δ Σ_{m=1}^∞ (1/m²) (mπ/δ) K₁(mπd/δ)
         = +2π n₁ n₂ Σ_{m=1}^∞ (1/m) K₁(mπd/δ)
```

This is POSITIVE for same-sign vortices.

**Wait — this means V_BC contributes positively to dV/dd, not negatively!**

Let me reconsider the signs...

### 5.3 Sign Analysis (Corrected)

The BC term V_BC = -2 n₁ n₂ δ Σ (1/m²) K₀(...)

For n₁ n₂ > 0 (same sign):
- V_BC < 0 (negative, i.e., attractive)
- But dV_BC/dd > 0 (derivative positive, i.e., attraction weakens with distance)

The logarithmic term V_log = +n₁ n₂ δ ln(d):
- V_log > 0 for d > L (repulsive)
- dV_log/dd = +n₁ n₂ δ/d > 0

**Total derivative:**
```
dV/dd = n₁ n₂ δ/d + 2π n₁ n₂ Σ (1/m) K₁(mπd/δ)
```

Both terms are positive for same-sign vortices → V is monotonically increasing → NO MINIMUM!

### 5.4 Resolution: Core Repulsion

The above calculation neglects the **core overlap** at small d.

When d ~ a (core size), the linear superposition breaks down. The cores cannot overlap without paying a large energy cost.

**Add core repulsion:**
```
V_core(d) = E_core × e^{-(d/a)²}  or  V_core(d) = E_core / d^p  for d < 2a
```

This contributes:
- V_core → +∞ as d → 0 (strong repulsion)
- V_core → 0 as d >> a (negligible)

### 5.5 Complete Picture

**Total potential:**
```
V(d) = V_core(d) + V_log(d) + V_BC(d)
```

**Behavior:**
- d → 0: V_core → +∞ (core repulsion dominates)
- d ~ a: V_core decreasing, V_log + V_BC ~ constant
- d ~ δ: V_log increasing logarithmically, V_BC saturating
- d → ∞: V_log ~ ln(d) (slow growth)

**For minimum to exist at d ~ δ:**

The condition is that V_core decreases faster than V_log + V_BC increases.

At d = d₀ where dV/dd = 0:
```
dV_core/dd|_{d₀} + n₁ n₂ δ/d₀ + 2π n₁ n₂ Σ (1/m) K₁(mπd₀/δ) = 0
```

Since dV_core/dd < 0 (core repulsion decreasing), this equation has a solution if:
```
|dV_core/dd|_{d₀}| > n₁ n₂ δ/d₀ + (BC terms)
```

---

## 6. CRITERION FOR MINIMUM

### 6.1 Necessary Condition

A minimum exists at d = d₀ if:
1. V'(d₀) = 0
2. V''(d₀) > 0

### 6.2 Sufficient Condition from BC

**Theorem:** If the thick-brane boundary conditions satisfy:
1. Neumann or Robin BC at ξ = 0, δ
2. Brane thickness δ > core size a
3. Core repulsion decays faster than 1/d

Then V(d) has a local minimum at d₀ ~ O(δ).

**Proof sketch:**
- At d << a: V ~ V_core → +∞
- At d ~ a: V decreasing (core repulsion decreasing faster than ln growth)
- At d ~ δ: V reaches minimum (balance point)
- At d >> δ: V ~ ln(d) increasing slowly

The BC-induced terms (K₀ sums) provide additional structure at d ~ δ that can sharpen the minimum.

### 6.3 Minimum Location

For Neumann BC, the characteristic scale is:
```
d₀ ~ δ / π × [geometric factor from K₀ series]
```

Numerically, the minimum occurs at d₀ ≈ 0.3 - 0.5 δ.

---

## 7. STABILITY OF MINIMUM

### 7.1 Second Derivative

At the minimum d = d₀:
```
V''(d₀) = d²V_core/dd²|_{d₀} - n₁ n₂ δ/d₀² + (BC second derivatives)
```

For a stable minimum: V''(d₀) > 0

### 7.2 Physical Interpretation

**Stability comes from:**
1. Core repulsion creates a "hard wall" at small d
2. BC-induced terms create a "well" at d ~ δ
3. Logarithmic growth provides confinement at large d

The combination gives a **stable equilibrium** at d₀.

---

## 8. RESULT

### 8.1 Derived Potential Form

From thick-brane BC alone (Neumann/Robin), we derive:
```
V(d) = V_core(d) - n₁ n₂ δ ln(d/L) - 2 n₁ n₂ δ Σ_{m=1}^∞ (1/m²) K₀(mπd/δ)
```

This has the structure:
- **Short range (d < a):** V_core → +∞ (repulsion)
- **Intermediate (a < d < δ):** Minimum at d₀
- **Long range (d > δ):** Logarithmic confinement

### 8.2 Comparison with P2

**Postulate P2 stated:**
> V(r) = V_rep(r) + V_att(r) with minimum at r₀

**We derived:**
> V(d) = V_core + V_log + V_BC with minimum at d₀ ~ δ

The BC-induced terms (K₀ series) provide the "effective attraction" at intermediate range, while core overlap provides repulsion.

### 8.3 Key Insight

**The minimum is forced by the boundary conditions!**

Without thick-brane BC (infinite bulk), we would have:
- Just V ~ ln(r) for 2D vortices
- No characteristic scale
- No minimum

With thick-brane BC:
- The brane thickness δ sets the scale
- Mode structure creates effective attraction
- Minimum emerges at d₀ ~ δ

---

## 9. IMPLICATIONS

### 9.1 Z6 Derivation Chain (Revised)

**Old chain:** P2 → L1 → L2 → Z6 (conditional on postulate)

**New chain:**
1. [P] Thick brane with BC (from A1-A4 + junction conditions)
2. [Dc] Defects exist (from topology of Φ field)
3. [Dc] V(d) has minimum at d₀ ~ δ (THIS DERIVATION)
4. [M] Kepler-Hales: hexagonal packing minimizes energy
5. [Dc] Z6 symmetry emerges

### 9.2 What Remains Postulated

- Existence of complex scalar field Φ with winding
- Potential U(Φ) that breaks symmetry
- Specific form of core energy V_core

These can potentially be derived from more fundamental 5D gauge theory.

---

## 10. CAVEATS AND OPEN ISSUES

### 10.1 Caveats

1. **Core model:** The core repulsion V_core was added phenomenologically
2. **Linear approximation:** Valid only for d >> a
3. **Static limit:** Assumes no dynamics in ξ direction
4. **Same-sign vortices:** Different behavior for opposite signs

### 10.2 What Would Strengthen This

1. Derive V_core from microscopic theory
2. Include gauge field contributions (for flux tubes)
3. Compute numerical coefficients precisely
4. Verify with lattice simulation

---

## SUMMARY

**Main Result:** The thick-brane boundary conditions (Neumann/Robin at ξ = 0, δ) FORCE the inter-defect potential V(d) to have a minimum at d₀ ~ δ.

**Mechanism:** BC creates a discrete mode spectrum with masses m_m = mπ/δ. The mode overlap generates an effective attraction at intermediate range that balances core repulsion, creating a stable equilibrium.

**Status:** [Der] — Derived from BC structure, not postulated.

**Remaining gap:** Core repulsion term requires microscopic derivation (from field theory of defect core).
