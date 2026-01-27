# 05: SIGN AND MINIMUM ANALYSIS

**Purpose:** Comprehensive analysis of V'(d) sign under all BC scenarios and determination of whether brane-frozen regime changes the no-go result.

---

## 1. RECAP: THE ORIGINAL NO-GO RESULT

From `aside_p2_closure_v3/01_SIGN_AND_MONOTONICITY.md`:

**Lemma 1 (Monotonicity):** For same-sign vortices under Neumann BC with uniform ξ-weight:
```
V'_lin(d) = 1/d + (2/δ) Σₘ₌₁^∞ (1/m) K₁(mπd/δ) > 0  for all d > 0
```

**Theorem 1 (No Minimum):** The linearized potential has no local minimum.

**Theorem 2 (Core Divergence):** V_core(d) → +∞ as d → 0 from topology.

**Theorem 3 (Minimum Exists):** Combining core + log growth → minimum at some d₀.

---

## 2. NEW ANALYSIS: DOES CHANGING BC HELP?

### 2.1 The Question

Can we find BC (Robin, Dirichlet, stiff limit) such that:
```
V'_lin(d) < 0  for some d > 0  ?
```

This would indicate an "attractive" regime in the linearized potential.

### 2.2 General Structure of V_lin(d)

Under any BC with mode spectrum {μ_m}, the linearized potential has the form:
```
V_lin(d) = Σ_m c_m × G_m(d)
```

where:
- c_m = (n₁n₂) × (W_m² / N_m) × (coupling factor)
- G_0(d) = -(1/2π) ln(d/L) if zero mode exists
- G_m(d) = (1/2π) K₀(μ_m d) for massive modes

### 2.3 Sign of Coefficients

For same-sign vortices (n₁n₂ > 0):
- c_m has definite sign (positive for repulsion convention)
- W_m² ≥ 0 always (squared quantity)
- N_m > 0 always (integral of positive quantity)

**No coefficient can be negative.** This is fundamental.

### 2.4 Derivatives

**Zero mode contribution:**
```
d/dd [ln(d)] = 1/d > 0
```

**Massive mode contribution:**
```
d/dd [K₀(μd)] = -μ K₁(μd) < 0
```

But this enters V_lin with a negative overall coefficient:
```
V_lin ∝ -c_m K₀(μ_m d)  →  V'_lin ∝ +c_m μ_m K₁(μ_m d) > 0
```

**Every term in V'_lin is positive!**

---

## 3. EXPLICIT CALCULATION: DIRICHLET BC

### 3.1 Mode Spectrum

```
μ_m = mπ/δ,    m = 1, 2, 3, ...   (no zero mode)
```

### 3.2 Effective Green's Function

With uniform weight and sin modes:
```
W_m = ∫₀^δ (1/δ) sin(mπξ/δ) dξ = (1/δ) × [δ/(mπ)][-cos(mπξ/δ)]₀^δ
    = (1/mπ) [(-1)^m - 1]/(-1)
    = (1/mπ) [1 - (-1)^m]
```

For odd m: W_m = 2/(mπ)
For even m: W_m = 0

### 3.3 Linearized Potential (Dirichlet)

```
V_lin(d) = -n₁n₂ Σ_{m odd} (W_m² / N_m) K₀(mπd/δ)
         = -n₁n₂ Σ_{k=0}^∞ [4/((2k+1)²π²)] × (2/δ) × K₀((2k+1)πd/δ)
```

(since N_m = δ/2 for sin modes)

### 3.4 Derivative (Dirichlet)

```
V'_lin(d) = n₁n₂ Σ_{k=0}^∞ [8/((2k+1)²π²δ)] × (2k+1)π/δ × K₁((2k+1)πd/δ)
          = n₁n₂ × (8/πδ²) Σ_{k=0}^∞ [1/(2k+1)] K₁((2k+1)πd/δ)
```

**Every term is positive for n₁n₂ > 0!**

**V'_lin(d) > 0 under Dirichlet BC.** No change from Neumann.

---

## 4. EXPLICIT CALCULATION: ROBIN BC

### 4.1 Setup

Robin BC: ∂_ξφ|_0 = κφ|_0, ∂_ξφ|_δ = -κφ|_δ (symmetric case)

### 4.2 Mode Equation

The transcendental equation (from Section 03):
```
tan(μδ) = 2κμ / (μ² - κ²)
```

### 4.3 Low-κ Expansion

For small κ (nearly Neumann):
- μ₀ ≈ √(2κ/δ) (small mass, not zero)
- μ_m ≈ mπ/δ + O(κ) for m ≥ 1

### 4.4 High-κ Limit (Nearly Dirichlet)

For large κ:
- μ_m → mπ/δ with m ≥ 1
- Zero mode disappears

### 4.5 Derivative Structure

In all cases:
```
V'_lin(d) = Σ_m (positive coefficient) × μ_m × K₁(μ_m d) > 0
```

**No regime of κ creates V' < 0.**

---

## 5. WHAT ABOUT "FROZEN" (STIFF) LIMIT?

### 5.1 Definition

"Frozen on brane" = Dirichlet with matching boundary values:
```
φ|_{ξ=0} = v,    φ|_{ξ=δ} = v
```

### 5.2 Effective Behavior

The constant v acts as a zero mode: φ(ξ) = v + [fluctuations].

The fluctuations satisfy homogeneous Dirichlet.

### 5.3 Interaction

The constant part gives the dominant contribution for large d:
```
V_lin(d) ∝ ln(d)    (from the "frozen" constant mode)
```

**This is the SAME as Neumann!** The stiff frozen limit does not change the log behavior.

### 5.4 Derivative

```
V'_lin(d) ∝ 1/d + [K₁ terms] > 0
```

**Still monotonically increasing.**

---

## 6. COULD SURFACE WEIGHT HELP?

### 6.1 Idea

If we sample only at boundaries (w(ξ) = surface delta functions), maybe the effective interaction changes?

### 6.2 Analysis (From Section 04)

Under Neumann with boundary weight:
- Only even modes contribute
- Zero mode still present
- V'_lin > 0 persists

Under Dirichlet with boundary weight:
- All projections vanish (unphysical)
- No meaningful interaction

**Surface weight does not help.**

---

## 7. THE FUNDAMENTAL REASON

### 7.1 Mathematical Obstruction

The Green's function G(r) for the Laplacian (or screened Laplacian) in 2D is:
- Monotonically decreasing in r for the log (goes to -∞ as r → 0)
- Monotonically decreasing in r for K₀ (goes to +∞ as r → 0)

But the **interaction energy** V(d) involves:
```
V(d) ∝ -G(d)    or    V(d) ∝ +G(d)
```

depending on sign conventions.

For same-sign charges (vortices):
- Repulsion → V(d) increases as d decreases
- The coefficient structure ensures V' > 0

### 7.2 No Way to Flip the Sign

To get V' < 0 would require:
1. Negative squared weights (impossible: W_m² ≥ 0)
2. Negative normalization (impossible: N_m > 0)
3. Changing the Green's function derivative sign (impossible: K₁ > 0, d(ln)/dx = 1/x > 0)

**The monotonicity is built into the mathematics of 2D Green's functions.**

---

## 8. COMPARISON WITH CORE OVERLAP

### 8.1 Where the Minimum Actually Comes From

From `aside_p2_closure_v3/02_CORE_REPULSION_FROM_FUNCTIONAL.md`:

**Theorem 2:** V_core(d) → +∞ as d → 0 from gradient energy + winding.

This is NOT a BC effect — it's a topological effect from winding number conservation.

### 8.2 The Complete Picture

```
V(d) = V_core(d) + V_lin(d)

V_core(d): +∞ as d → 0, decreasing to 0 as d → ∞
V_lin(d): (finite or -∞) as d → 0, +∞ as d → ∞

Sum: +∞ as d → 0, +∞ as d → ∞ → minimum at some d₀
```

The minimum exists because:
- V_core provides divergence at d → 0 (topology)
- V_lin provides divergence at d → ∞ (log growth or accumulated K₀)
- Continuity guarantees a minimum

**BC determine the character of V_lin but NOT the existence of the minimum.**

---

## 9. VERDICT ON SIGN STRUCTURE

### 9.1 Summary Table

| BC Type | Zero Mode | V_lin(d → 0) | V_lin(d → ∞) | V'_lin(d) |
|---------|-----------|--------------|--------------|-----------|
| Neumann | Yes | -∞ (linearized) | +∞ | **> 0** |
| Dirichlet | No | finite | +∞ | **> 0** |
| Robin | No | finite | +∞ | **> 0** |
| Frozen (Dirichlet+v) | Yes* | -∞ (linearized) | +∞ | **> 0** |

### 9.2 Conclusion

**V'_lin(d) > 0 for all BC scenarios analyzed.**

The brane-frozen regime (Dirichlet with stiff pinning) does NOT:
- Create an attractive window
- Change the monotonicity of V_lin
- Move the minimum location significantly

**The minimum in V(d) comes from core overlap (topology), not from BC.**

---

## 10. WHAT BC ACTUALLY CONTRIBUTE

### 10.1 Positive Contributions

1. **Scale δ:** BC set the brane thickness scale
2. **Mode spectrum:** BC determine eigenvalues μ_m
3. **Screening:** Higher modes provide exponential screening at d > δ

### 10.2 What BC Do NOT Contribute

1. **Attraction:** No BC creates V' < 0
2. **Minimum mechanism:** Comes from topology, not BC
3. **Sign reversal:** Impossible with standard Green's functions

### 10.3 The Honest Statement

> "Thick-brane boundary conditions provide the characteristic scale δ and mode structure, but do not create attraction or a minimum in V_lin(d). The minimum in the full potential V(d) = V_core + V_lin arises from the balance of topological core repulsion and logarithmic/Yukawa growth at large d."
