# 01: MODEL AND DEFINITION — Frozen on Brane via ξ-BC

**Date:** 2026-01-26
**Purpose:** Define precisely what "frozen on brane" means in the context of ξ-boundary conditions, distinguishing it clearly from "radial step frozen."

---

## 1. GEOMETRY

### 1.1 Coordinates

The thick brane occupies:
- **Transverse 2D:** (r, θ) or (x, y) — the plane where vortices live
- **Fifth dimension:** ξ ∈ [0, δ] — brane thickness

Full coordinates: (r, θ, ξ) with metric:
```
ds² = dr² + r²dθ² + dξ²
```

### 1.2 Field Content

Complex scalar field Φ(r, θ, ξ) representing the order parameter.

Vortex ansatz:
```
Φ(r, θ, ξ) = f(r, ξ) · e^{inθ}
```
where n ∈ ℤ is winding number, f(r, ξ) ∈ ℝ≥0 is the profile.

---

## 2. TWO DISTINCT "FROZEN" CONCEPTS

### 2.1 Radial Step Frozen (Chapter 2)

**Definition:** The radial profile f(r) is a step function:
```
f(r) = Θ(r - a) = { 0,  r < a
                  { 1,  r ≥ a
```

**Where it appears:** Chapter 2 of EDC Book, Paper 2.

**What it does:**
- Gives parameter-free geometric coefficients (4π/3, 2π², etc.)
- Eliminates GL coherence length as adjustable parameter
- Required for m_p/m_e = 6π⁵ derivation

**This is NOT about ξ-boundary conditions.** It is an ansatz for the r-dependence.

### 2.2 Frozen on Brane (ξ-BC) — THIS INVESTIGATION

**Definition:** The ξ-profile is pinned or stiff due to boundary terms at ξ = 0 and ξ = δ.

**Possible meanings:**

**(A) ξ-profile pinned to boundary values:**
```
Φ(r, θ, ξ=0) = Φ_0(r, θ)   [fixed at left boundary]
Φ(r, θ, ξ=δ) = Φ_δ(r, θ)   [fixed at right boundary]
```
This is Dirichlet BC in ξ.

**(B) ξ-fluctuations suppressed (stiff limit):**
```
∂ξΦ → 0  throughout the bulk
```
meaning Φ(r, θ, ξ) ≈ Φ(r, θ) independent of ξ (zero mode dominance).

**(C) Piecewise constant in ξ:**
```
Φ(r, θ, ξ) = { Φ_L(r, θ),  ξ ∈ [0, δ/2)
             { Φ_R(r, θ),  ξ ∈ [δ/2, δ]
```
A step function in ξ (not r).

**(D) Surface-localized weight:**

The effective interaction uses boundary-localized sampling:
```
G_eff(r) = ∫₀^δ dξ ∫₀^δ dξ' w(ξ) w(ξ') G(r; ξ, ξ')
```
where w(ξ) = δ(ξ) + δ(ξ - δ) instead of uniform weight.

---

## 3. EPISTEMIC TAGS (UPFRONT)

| Symbol | Meaning |
|--------|---------|
| [M] | Mathematical theorem (no physics input) |
| [P] | Postulate (assumed, not derived) |
| [Dc] | Derived conditional (needs assumptions) |
| [Der] | Derived from action/equations |
| [OPEN] | Not resolved |
| [BL] | Baseline (experimental reference) |

---

## 4. WHAT WE WANT TO DETERMINE

### 4.1 Questions

**Q1:** Can ξ-BC (Neumann/Robin/Dirichlet) enforce a "frozen" ξ-profile?
- If yes: derive from action variation
- If no: explain why

**Q2:** Does frozen-on-brane change the interaction V(d) monotonicity?
- Recall: aside_p2_closure_v3 showed V'(d) > 0 for Neumann BC with uniform weight
- Does Dirichlet or surface-weight change this?

**Q3:** Can frozen-on-brane create a minimum in V_lin(d)?
- Or does the minimum still require core overlap (topology)?

### 4.2 Prior Result to Build On

From `aside_p2_closure_v3/`:
- **Lemma 1:** V'_lin(d) > 0 for all d > 0 under Neumann BC with uniform ξ-weight
- **Theorem 2:** Core overlap gives V → +∞ as d → 0 (topology)
- **Theorem 3:** Minimum exists from continuity (core + log growth)

The question now: Does changing BC or weight affect Lemma 1?

---

## 5. RELATION TO ISRAEL JUNCTION

### 5.1 Israel Junction Conditions (General)

At a hypersurface Σ separating bulk regions:
```
[K_ab] - g_ab [K] = -(1/M₅³) S_ab
```

where:
- K_ab = extrinsic curvature
- [X] = jump across Σ
- S_ab = stress-energy on Σ

### 5.2 How This Maps to Φ-BC

**Claim [P]:** Israel junction with brane-localized matter induces Robin-type BC for bulk fields.

**Argument (heuristic):**
1. Brane stress-energy S_ab includes contributions from Φ
2. Matching across ξ = 0 gives derivative condition on Φ
3. Result: ∂ξΦ|_{ξ=0} = κ Φ|_{ξ=0} (Robin)

**Status:** This mapping is [P]/[Dc] — motivated but requires explicit derivation in each case.

---

## 6. SCOPE OF THIS INVESTIGATION

### 6.1 In Scope

- Derive BC from action variation (Section 02)
- Mode spectrum under different BC (Section 03)
- Green's function with weight options (Section 04)
- Sign analysis for V'(d) (Section 05)
- Comparison with radial frozen (Section 06)
- Verdict (Section 07)

### 6.2 Out of Scope

- Full 5D GHY + Israel calculation (too complex)
- Numerical lattice simulations
- Gauge field extensions (focus on scalar)

---

## 7. NOTATION SUMMARY

| Symbol | Meaning |
|--------|---------|
| ξ | 5D depth coordinate, ξ ∈ [0, δ] |
| δ | Brane thickness |
| r | Radial coordinate in transverse 2D |
| θ | Angular coordinate in transverse 2D |
| Φ(r, θ, ξ) | Complex scalar field |
| f(r, ξ) | Profile amplitude (Φ = f e^{inθ}) |
| n | Winding number |
| V(d) | Inter-vortex potential at separation d |
| V_lin(d) | Linearized potential (log + K₀ terms) |
| G(r; ξ, ξ') | Green's function |
| K₀, K₁ | Modified Bessel functions |
| κ | Robin BC parameter |

---

## 8. KEY DISTINCTION EMPHASIZED

**Radial frozen (Chapter 2):**
- Ansatz: f(r) = Θ(r - a)
- Effect: removes r-dependence freedom → geometric coefficients
- NOT about ξ-BC

**Brane frozen (this investigation):**
- BC: Dirichlet/Robin at ξ = 0, δ
- Effect: pins or stiffens ξ-profile
- Question: does this change V(d) behavior?

These are **independent** concepts. Both could be true simultaneously:
- f(r) = Θ(r - a) (radial frozen)
- ∂ξf = 0 or f|_boundary = fixed (ξ frozen)

The radial frozen is well-established. The ξ-frozen via BC is what we investigate here.
