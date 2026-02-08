# 01: SIGN AND MONOTONICITY ANALYSIS

**Purpose:** Rigorous derivation of V(d) from Green's function with consistent sign conventions.

---

## 1. CONVENTIONS

**Convention 1 (Energy reference):** [M]
V(d) is the interaction energy of two defects at separation d, with V(∞) = 0.

**Convention 2 (Force):** [M]
Force F = -dV/dd. Positive V'(d) means repulsive force at distance d.

**Convention 3 (Winding):** [M]
Vortex i has winding nᵢ ∈ ℤ. Same-sign means n₁n₂ > 0.

---

## 2. SETUP

### 2.1 Geometry

- 2D transverse plane: coordinates (x, y) or polar (r, θ)
- 5th dimension: ξ ∈ [0, δ] (thick brane)
- Two vortices at positions r₁ = 0 and r₂ = d (separation d)

### 2.2 Field Theory

Complex scalar field Φ(r, θ, ξ) with:
```
S = ∫ d²r dξ [ ½|∇Φ|² + U(|Φ|) ]
```
where U(|Φ|) has minimum at |Φ| = v > 0. [P]

### 2.3 Boundary Conditions

Neumann BC in ξ direction: [P]
```
∂ξΦ|_{ξ=0} = 0,    ∂ξΦ|_{ξ=δ} = 0
```

---

## 3. GREEN'S FUNCTION DERIVATION

### 3.1 Mode Expansion

With Neumann BC, the ξ-modes are: [M]
```
φₘ(ξ) = cos(mπξ/δ),    m = 0, 1, 2, ...
```

Orthonormality: [M]
```
∫₀^δ φₘ(ξ) φₙ(ξ) dξ = δ (1 + δₘ₀)/2 × δₘₙ
```

### 3.2 Mode Masses

Each mode has effective 2D mass: [Dc]
```
μₘ = mπ/δ
```

The m = 0 mode is massless; m ≥ 1 modes are massive.

### 3.3 2D Green's Functions

**Zero mode (m = 0):** [M]
```
G₀(r) = -(1/2π) ln(r/L)
```
where L is an IR cutoff (system size).

**Massive modes (m ≥ 1):** [M]
```
Gₘ(r) = (1/2π) K₀(μₘ r)
```

Properties of K₀(x): [M]
- K₀(x) > 0 for all x > 0
- K₀(x) → -ln(x/2) - γ as x → 0
- K₀(x) → √(π/2x) e^{-x} as x → ∞
- K₀'(x) = -K₁(x) < 0 for all x > 0

### 3.4 Full Green's Function

Integrating over ξ, ξ' with equal weight: [Dc]
```
G(r) = ∫₀^δ dξ ∫₀^δ dξ' G(r; ξ, ξ')
     = δ² G₀(r) + 2δ² Σₘ₌₁^∞ (1/m²π²) Gₘ(r)
     = -(δ²/2π) ln(r/L) + (δ²/π²) Σₘ₌₁^∞ (1/m²) K₀(mπr/δ)
```

---

## 4. INTERACTION ENERGY

### 4.1 Vortex-Vortex Interaction

For two vortices with windings n₁, n₂, the interaction energy is: [Dc]
```
V(d) = -2π n₁ n₂ × G(d) / δ²
     = n₁ n₂ ln(d/L) - (2/π) n₁ n₂ Σₘ₌₁^∞ (1/m²) K₀(mπd/δ)
```

### 4.2 Sign Analysis for Same-Sign Vortices (n₁n₂ = 1)

**Term 1: Logarithmic**
```
V_log(d) = ln(d/L)
```
- For d < L: V_log < 0
- For d = L: V_log = 0
- For d > L: V_log > 0
- Derivative: V_log'(d) = 1/d > 0 for all d > 0

**Term 2: K₀ series**
```
V_K(d) = -(2/π) Σₘ₌₁^∞ (1/m²) K₀(mπd/δ)
```
- Since K₀(x) > 0 for all x > 0: V_K(d) < 0 for all d > 0
- Derivative: V_K'(d) = +(2/δ) Σₘ₌₁^∞ (1/m) K₁(mπd/δ) > 0

**Total:**
```
V(d) = V_log(d) + V_K(d)
V'(d) = V_log'(d) + V_K'(d) = 1/d + (2/δ) Σₘ₌₁^∞ (1/m) K₁(mπd/δ)
```

---

## 5. MONOTONICITY LEMMA

**Lemma 1 (Monotonicity of Linearized Potential):** [Der]

For same-sign vortices (n₁n₂ > 0) in a thick brane with Neumann BC, the linearized interaction potential satisfies:
```
V'(d) > 0    for all d > 0
```

**Proof:** [M]

1. V_log'(d) = 1/d > 0 for all d > 0.

2. K₁(x) > 0 for all x > 0 (standard property of Bessel functions).

3. Therefore V_K'(d) = (2/δ) Σₘ (1/m) K₁(mπd/δ) > 0.

4. Sum of positive terms: V'(d) = V_log'(d) + V_K'(d) > 0. ∎

---

## 6. CONSEQUENCE: NO MINIMUM FROM (log + K₀) ALONE

**Theorem 1 (No Minimum in Linearized Model):** [Der]

The linearized interaction potential V(d) = V_log(d) + V_K(d) for same-sign vortices has NO local minimum for d ∈ (0, ∞).

**Proof:** [M]

1. By Lemma 1, V'(d) > 0 for all d > 0.

2. A local minimum at d₀ requires V'(d₀) = 0.

3. Since V'(d) > 0 everywhere, no such d₀ exists. ∎

---

## 7. ASYMPTOTIC BEHAVIOR

**At small d (d << δ):** [Dc]

Using K₀(x) ~ -ln(x/2) - γ for small x:
```
V_K(d) ~ -(2/π) Σₘ (1/m²) [-ln(mπd/2δ) - γ]
       = (2/π) Σₘ (1/m²) ln(mπd/2δ) + (2γ/π) × (π²/6)
```

The leading term is:
```
V_K(d) ~ (2/π) × (π²/6) × ln(d) + const = (π/3) ln(d) + const
```

So total:
```
V(d) ~ ln(d) - (π/3) ln(d) + const = (1 - π/3) ln(d) + const
     ≈ -0.047 ln(d) + const
```

For d → 0: ln(d) → -∞, so V(d) → +∞ (if coefficient is positive) or V(d) → -∞ (if negative).

With coefficient (1 - π/3) ≈ -0.047 < 0: **V(d) → -∞ as d → 0** in the linearized model!

**At large d (d >> δ):** [Dc]

K₀ terms decay exponentially, so:
```
V(d) ~ ln(d/L)
```
For d > L: V(d) → +∞.

---

## 8. CRITICAL OBSERVATION

**The linearized model is UNPHYSICAL at d → 0.**

The result V(d) → -∞ as d → 0 indicates that the linear superposition ansatz breaks down when vortex cores overlap.

The core overlap introduces NONLINEAR corrections that the Green's function method misses.

These corrections must provide:
1. A lower bound that prevents V → -∞
2. Sufficient repulsion to create a minimum (if one exists)

---

## 9. SUMMARY

| Statement | Status | Reference |
|-----------|--------|-----------|
| V'(d) > 0 for linearized model | [Der] | Lemma 1 |
| No minimum in linearized model | [Der] | Theorem 1 |
| V(d) → -∞ as d → 0 (linearized) | [Dc] | Section 7 |
| V(d) → +∞ as d → ∞ | [Dc] | Section 7 |
| Core overlap corrections needed | [REQUIRED] | Section 8 |

**Conclusion:** The (log + K₀) terms from Neumann BC are strictly monotonically increasing. They do NOT create a minimum. The linearized model is unphysical at small d, requiring nonlinear core corrections.
