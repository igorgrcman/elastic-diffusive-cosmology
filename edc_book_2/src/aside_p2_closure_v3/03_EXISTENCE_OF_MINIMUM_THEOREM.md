# 03: EXISTENCE OF MINIMUM — THEOREM AND ANALYSIS

**Purpose:** Determine whether V(d) has a minimum by combining results from 01 and 02.

---

## 1. RECAPITULATION OF RESULTS

### From 01_SIGN_AND_MONOTONICITY.md:

**Linearized interaction potential (for d > a):**
```
V_lin(d) = n₁n₂ ln(d/L) - (2/π) n₁n₂ Σₘ₌₁^∞ (1/m²) K₀(mπd/δ)
```

**Key result (Lemma 1):** For same-sign vortices (n₁n₂ > 0):
```
V_lin'(d) > 0  for all d > 0
```

**Asymptotic behavior:**
- As d → 0 (linearized, d >> a): V_lin(d) → (1 - π/3) ln(d) ≈ -0.047 ln(d)
- As d → ∞: V_lin(d) → ln(d/L) → +∞

### From 02_CORE_REPULSION_FROM_FUNCTIONAL.md:

**Core overlap energy (for d < a):**
```
V_core(d) ~ 2πn²v² ln(a/d)
```

**Key result (Theorem 2):**
```
V_core(d) → +∞  as  d → 0
```

---

## 2. THE COMPLETE POTENTIAL

### 2.1 Domain Structure

The complete potential has two regimes:

| Region | Dominant physics | Expression |
|--------|-----------------|------------|
| d < a | Core overlap | V_core dominates |
| d > a | Linearized | V_lin dominates |
| d ~ a | Crossover | Both contribute |

### 2.2 Full Potential

**Definition:** [Dc]
```
V(d) = V_core(d) + V_lin(d)
```

where:
- V_core(d) is from Theorem 2 (Section 02)
- V_lin(d) is from Section 01

---

## 3. ANALYSIS OF EXTREME BEHAVIOR

### 3.1 As d → 0

**V_core contribution:**
```
V_core(d) ~ 2πn²v² ln(a/d) → +∞
```

**V_lin contribution:**
```
V_lin(d) → (1 - π/3) ln(d) → +∞  [since (1 - π/3) < 0]
```

Wait — let me recalculate this more carefully.

Actually from 01, for small d << δ:
```
V_lin(d) ≈ (1 - π/3) ln(d) + const
```

Since (1 - π/3) ≈ -0.047 < 0:
- As d → 0: ln(d) → -∞
- Therefore: V_lin(d) → (-0.047) × (-∞) = +∞

So V_lin → +∞ as d → 0 in the linearized model. But this is at d >> a where the linearization is valid.

**At d ~ a (crossover):**
The linearized model breaks down. The core overlap (from Theorem 2) takes over:
```
V_core(d) ~ 2πn²v² ln(a/d) → +∞  as d → 0
```

**Conclusion:** V(d) → +∞ as d → 0. ✓

### 3.2 As d → ∞

**V_core contribution:** Negligible (cores well separated)

**V_lin contribution:**
```
V_lin(d) ~ ln(d/L) → +∞
```

**Conclusion:** V(d) → +∞ as d → ∞. ✓

---

## 4. EXISTENCE OF MINIMUM — THE CRITICAL QUESTION

### 4.1 Naive Expectation

If:
- V(d) → +∞ as d → 0
- V(d) → +∞ as d → ∞
- V(d) is continuous

Then by the **intermediate value theorem**, V must have a global minimum at some d₀ ∈ (0, ∞).

### 4.2 The Problem

**But we also proved (Lemma 1):** V_lin'(d) > 0 for all d > 0.

This means V_lin is **strictly increasing** on (a, ∞).

And V_core'(d) = d/dd [2πn²v² ln(a/d)] = -2πn²v² / d < 0 for d > 0.

So V_core is **strictly decreasing** on (0, a].

### 4.3 Matching at d = a

At the crossover d ~ a:

**From left (d < a):** V_core is decreasing, approaching some finite value V_core(a).

**From right (d > a):** V_lin is increasing, starting from some value V_lin(a).

**Key question:** Is there a point d₀ where V'(d₀) = 0?

---

## 5. RIGOROUS ANALYSIS

### 5.1 Defining V Properly

The total energy functional gives:
```
V(d) = E[Φ_d] - 2E_1
```

where Φ_d is the two-vortex configuration at separation d, and E_1 is single-vortex energy.

This is a continuous function of d for d > 0.

### 5.2 Behavior of V'(d)

**For d << a:** V is dominated by core overlap.
```
V(d) ≈ 2πn²v² ln(a/d) + [subdominant]
V'(d) ≈ -2πn²v² / d < 0
```

**For d >> a:** V is dominated by linearized terms.
```
V(d) ≈ ln(d/L) + [K₀ corrections]
V'(d) ≈ 1/d + [K₁ corrections] > 0
```

### 5.3 Sign Change Lemma

**Lemma 4 (Sign change of V'):** [Dc]

Under the conditions:
1. V_core'(d) < 0 for d < a (core repulsion decreasing)
2. V_lin'(d) > 0 for d > a (linearized terms increasing)
3. V continuous on (0, ∞)

There exists at least one d₀ ∈ (0, ∞) where V'(d₀) changes sign.

**Proof:**
- At d << a: V'(d) < 0 (dominated by V_core')
- At d >> a: V'(d) > 0 (dominated by V_lin')
- By intermediate value theorem applied to V': there exists d₀ where V'(d₀) = 0. ∎

---

## 6. THE CRITICAL GAP

### 6.1 What Lemma 4 Actually Says

Lemma 4 proves: **V'(d₀) = 0 for some d₀.**

This means V has a **critical point** at d₀.

### 6.2 Is It a Minimum?

For d₀ to be a minimum, we need V''(d₀) > 0.

**Calculating V'':**
```
V''(d) = d²V_core/dd² + d²V_lin/dd²
       = 2πn²v² / d² + [terms from K₀ second derivatives]
```

At d ~ a, both terms are positive... but is the sum positive?

### 6.3 The Subtle Issue

The problem is that V_core and V_lin are derived in **different regimes**:
- V_core is valid for d < a
- V_lin is valid for d > a

In the crossover region d ~ a, **neither approximation is accurate**.

To prove V''(d₀) > 0, we need the **exact functional** evaluated at the critical point.

---

## 7. THEOREM: CONDITIONAL EXISTENCE OF MINIMUM

**Theorem 3 (Conditional minimum):** [Dc]

Let V(d) be the interaction potential for two same-sign vortices in a thick brane with Neumann BC. If:

(i) V(d) → +∞ as d → 0 (from Theorem 2) ✓

(ii) V(d) → +∞ as d → ∞ (from logarithmic growth) ✓

(iii) V(d) is continuous on (0, ∞) [P — requires functional regularity]

(iv) V_core'(d) < 0 for d < a [Der from Theorem 2]

(v) V_lin'(d) > 0 for d > a [Der from Lemma 1]

Then V(d) has **at least one local minimum** at some d₀ ∈ (0, ∞).

**Proof:**
1. By (i) and (ii), V is bounded below (has infimum)
2. By (iii), V is continuous, so infimum is attained
3. By (iv) and (v), the minimum is not at d = 0 or d = ∞
4. Therefore minimum is at interior point d₀ ∈ (0, ∞). ∎

---

## 8. WHAT THIS DOES AND DOES NOT PROVE

### 8.1 What Is Proven

| Statement | Status |
|-----------|--------|
| V → +∞ as d → 0 | [Der] (Theorem 2) |
| V → +∞ as d → ∞ | [Dc] (logarithmic) |
| V has at least one critical point | [Dc] (Lemma 4) |
| If continuous, V has global minimum | [Dc] (Theorem 3) |

### 8.2 What Is NOT Proven

| Statement | Status | Issue |
|-----------|--------|-------|
| d₀ ~ δ (minimum at brane thickness scale) | [OPEN] | Requires numerical calculation |
| V''(d₀) > 0 (stability) | [OPEN] | Requires exact functional |
| Uniqueness of minimum | [OPEN] | Could have multiple minima |

---

## 9. LOCATION OF MINIMUM — QUALITATIVE

### 9.1 Upper Bound

The minimum cannot be at d > δ because:
- For d >> δ, the K₀ terms are exponentially small
- V ≈ ln(d/L) which is monotonically increasing

So d₀ < O(δ).

### 9.2 Lower Bound

The minimum cannot be at d < a because:
- For d < a, core overlap dominates
- V_core ~ ln(a/d) is monotonically decreasing as d decreases

So d₀ > a.

### 9.3 Conclusion

```
a < d₀ < O(δ)
```

If a << δ (thin core compared to brane thickness), then d₀ ~ O(a to δ).

---

## 10. THE HONEST VERDICT

### 10.1 What We Can Claim

**Theorem 3 is VALID** and shows:
> "A minimum EXISTS, conditional on continuity of the energy functional."

### 10.2 What We Cannot Claim

We CANNOT claim:
> "The minimum is at d₀ ~ δ" (no derivation of location)
> "The BC force a minimum" (the BC only provide the long-range behavior)

### 10.3 Role of BC vs Core

| Effect | Source | Status |
|--------|--------|--------|
| Repulsion at d → 0 | Core overlap (topology + gradient energy) | [Der] |
| Monotonic increase for d > a | log + K₀ from BC mode sum | [Der] |
| Existence of minimum | Balance of above | [Dc] |
| Location of minimum | Crossover region physics | [OPEN] |

---

## 11. SUMMARY

**Main result:**

1. V(d) → +∞ as d → 0: DERIVED from core overlap (Theorem 2)
2. V(d) → +∞ as d → ∞: DERIVED from logarithmic growth
3. V continuous: POSTULATED (standard for energy functionals)
4. Minimum exists: DERIVED from (1)-(3) (Theorem 3)

**The minimum is NOT "forced by BC"** — it is forced by the combination of:
- Topological core repulsion (from winding)
- Logarithmic confinement (from 2D + finite brane)

The BC contribute the mode structure (K₀ terms) but these do NOT create attraction — they are monotonically increasing.

**Gap remaining:** The specific location d₀ and stability V''(d₀) > 0 require calculation in the crossover regime, which is beyond the asymptotic analysis.
