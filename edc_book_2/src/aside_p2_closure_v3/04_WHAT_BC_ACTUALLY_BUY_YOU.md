# 04: WHAT BOUNDARY CONDITIONS ACTUALLY BUY YOU

**Purpose:** Precisely characterize what thick-brane Neumann/Robin BC contribute to the physics, versus what they do NOT contribute.

---

## 1. COMPARISON: INFINITE BULK vs THICK BRANE

### 1.1 Infinite 2D System (No Brane)

For vortices in an infinite 2D plane (no ξ dimension):

**Green's function:**
```
G(r) = -(1/2π) ln(r/L)
```

**Vortex interaction:**
```
V(d) = n₁n₂ ln(d/L)
```

**Properties:**
- Purely logarithmic
- NO characteristic length scale (except IR cutoff L)
- Same-sign vortices: repel at all distances
- Opposite-sign: attract at all distances

### 1.2 Infinite 3D System (No Brane)

For vortex lines in 3D:

**Green's function:**
```
G(r) = 1/(4πr)
```

**Vortex line interaction (per unit length):**
```
V(d) ~ n₁n₂ / d
```

**Properties:**
- Power law decay
- Same-sign: repel
- Falls off faster than 2D

### 1.3 Thick Brane (Finite ξ ∈ [0, δ])

For vortices in thick brane with Neumann BC:

**Green's function (from mode expansion):**
```
G(r) = -(δ²/2π) ln(r/L) + (δ²/π²) Σₘ₌₁^∞ (1/m²) K₀(mπr/δ)
```

**Vortex interaction:**
```
V(d) = n₁n₂ ln(d/L) - (2/π) n₁n₂ Σₘ₌₁^∞ (1/m²) K₀(mπd/δ)
```

**Properties:**
- Logarithmic at long range (d >> δ)
- Modified at short range (d ~ δ) by K₀ terms
- Characteristic length scale: δ (brane thickness)

---

## 2. WHAT THE BC PROVIDE

### 2.1 A Characteristic Scale

**Infinite systems:** No natural length scale (only IR cutoff).

**Thick brane:** The brane thickness δ sets a physical scale.

This is important because:
- Mode masses: mₘ = mπ/δ
- K₀ terms cut off at d ~ δ
- Physics changes character at d ~ δ

### 2.2 Mode Discretization

**Infinite ξ:** Continuous spectrum in ξ-momentum.

**Finite ξ with Neumann BC:** Discrete modes cos(mπξ/δ).

This gives the sum Σₘ K₀(mπd/δ) instead of an integral.

### 2.3 Modified Interaction at d ~ δ

The K₀ terms contribute:
```
V_BC(d) = -(2/π) n₁n₂ Σₘ (1/m²) K₀(mπd/δ)
```

For d << δ: K₀(x) ~ -ln(x), so V_BC ~ -ln(d) × [convergent sum]

For d >> δ: K₀(x) ~ e^{-x}, so V_BC → 0 exponentially

**Effect:** The K₀ terms reduce the interaction at d < δ compared to pure logarithm.

---

## 3. WHAT THE BC DO NOT PROVIDE

### 3.1 NOT Attraction

**Claim (often misunderstood):** "BC create effective attraction at intermediate range."

**Reality (from Section 01):**

The K₀ contribution to the potential is:
```
V_K(d) = -(2/π) n₁n₂ Σₘ (1/m²) K₀(mπd/δ)
```

For same-sign vortices (n₁n₂ > 0): V_K < 0.

This means V_K is **negative** (below zero), which might suggest "attraction."

But the **force** is:
```
F_K = -dV_K/dd = +(2/δ) n₁n₂ Σₘ (1/m) K₁(mπd/δ) > 0
```

Positive force = **repulsion** (vortices pushed apart).

**Conclusion:** The K₀ terms contribute to **repulsion**, not attraction. They just repel less strongly than the logarithm alone.

### 3.2 NOT a Minimum (Alone)

From Section 01, Theorem 1:
> The linearized interaction V_lin = V_log + V_K has NO local minimum.

The BC terms modify the logarithm but do not create a minimum.

### 3.3 NOT the Core Physics

The BC affect the long-range (d > a) behavior.

The short-range (d < a) behavior is dominated by **core overlap**, which comes from:
- Topology (winding additivity)
- Gradient energy
- Potential U(|Φ|)

These are NOT from BC — they are from the field theory at the core.

---

## 4. THE HONEST ACCOUNTING

### 4.1 Table: Source of Each Effect

| Physical Effect | Source | BC Role |
|-----------------|--------|---------|
| Repulsion at d → 0 | Core overlap (topology) | NONE |
| Logarithmic growth | 2D Coulomb (zero mode) | Sets coefficient |
| Scale δ in potential | Mode discretization | YES |
| K₀ corrections | Higher modes | YES |
| Minimum existence | Core repulsion + log growth | INDIRECT |
| Minimum location | Crossover physics | PARTIAL |

### 4.2 What Would Change Without BC

**If ξ were infinite (no BC):**
- Continuous spectrum, no mode sum
- V(d) ~ ln(d) for 2D, ~ 1/d for 3D
- No characteristic scale δ
- Still: core repulsion exists (from topology)
- Still: minimum could exist (if 3D)

**If different BC (e.g., Dirichlet):**
- Different mode structure (sin instead of cos)
- Different coefficients in K₀ sum
- Same qualitative behavior (still monotonic for same-sign)

---

## 5. COMPARISON: MYTH vs REALITY

### Myth 1: "BC Force a Minimum"

**Reality:** BC modify the long-range potential but do not create a minimum. The minimum comes from the balance of:
- Core repulsion (from topology)
- Logarithmic confinement (from 2D + compactification)

BC contribute the scale δ, not the mechanism.

### Myth 2: "K₀ Terms Are Attractive"

**Reality:** K₀ terms contribute negative values to V (below pure log), but positive force (repulsion). "Less repulsive" ≠ "attractive."

### Myth 3: "Minimum at d₀ ~ δ Is Derived"

**Reality:** We can show:
- d₀ > a (above core size)
- d₀ < O(δ) (below scale where K₀ dies)

But the exact location requires calculation, not derivation.

---

## 6. WHAT BC ACTUALLY BUY (HONEST VERSION)

### 6.1 Dimensional Reduction

The thick brane effectively reduces 5D to 2D+finite for vortex physics.

Without BC: Would need to treat full 5D problem.

With BC: Can use mode expansion, reducing to countable sum of 2D problems.

### 6.2 IR Regularization

The brane thickness δ provides a physical IR scale.

This replaces the arbitrary cutoff L in many formulas.

### 6.3 Connection to Israel Junction

Neumann BC (∂_ξ Φ = 0) means "no flux escapes the brane."

This is consistent with Israel junction conditions for a domain wall.

The BC are not arbitrary — they follow from the brane structure.

### 6.4 Mode Mass Spectrum

The discrete masses mₘ = mπ/δ mean:
- Lightest mode is m₁ = π/δ
- Heavier modes are suppressed at d > δ

This gives exponential screening at large distances (from K₀ decay).

---

## 7. IMPLICATION FOR P2 DERIVATION

### 7.1 What P2 Claims

> "Flux tubes have V(r) = V_rep(r) + V_att(r) with minimum at r₀"

### 7.2 What We Can Derive

From A1-A4 + field content + BC:
- V has repulsion at d → 0 [Der]
- V has logarithmic growth at d → ∞ [Dc]
- V has a minimum at some d₀ ∈ (0, ∞) [Dc]

### 7.3 What We Cannot Derive

- The "attraction" language is misleading — there is no attractive force
- The specific form V_rep + V_att is not derived
- The value of d₀ is not derived

### 7.4 Honest Restatement of P2

**Old P2:** "V(r) has repulsion + attraction with minimum"

**Derived version:** "V(d) → +∞ as d → 0 (from topology) and V(d) → +∞ as d → ∞ (from log). By continuity, minimum exists at some d₀."

The word "attraction" is replaced by "continuity argument."

---

## 8. SUMMARY

### 8.1 BC Provide:
- Scale δ in the problem
- Mode discretization (cos series)
- K₀ corrections to logarithm
- Connection to brane physics (Israel conditions)

### 8.2 BC Do NOT Provide:
- Attraction (K₀ terms are repulsive)
- The minimum directly (comes from core + log balance)
- Core physics (topology of field, not BC)

### 8.3 Bottom Line

**The boundary conditions are necessary but not sufficient for the minimum.**

- Without BC: No scale δ, no mode structure
- With BC alone: Monotonic potential (no minimum)
- With BC + core physics: Minimum exists

The derivation of the minimum requires BOTH ingredients. Neither alone suffices.
