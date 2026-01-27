# 06: RELATION TO RADIAL STEP FROZEN

**Purpose:** Compare "brane-frozen (ξ)" with "radial step core (r)" and clarify which addresses which physics.

---

## 1. TWO DISTINCT FROZEN CONCEPTS — FINAL CLARIFICATION

### 1.1 Radial Step Frozen (Chapter 2)

**Definition:**
```
f(r) = Θ(r - a) = { 0,  r < a  (core)
                  { v,  r ≥ a  (vacuum)
```

**What it does:**
- Eliminates GL coherence length ξ_GL as adjustable parameter
- Gives exact geometric coefficients: Vol(B³) = 4π/3, Area(S³) = 2π²
- Required for m_p/m_e = 6π⁵ derivation

**Physical justification:**
- High membrane tension σ → ∞ forces sharp boundary
- Topological protection: step function cannot be continuously deformed
- Stability: particle lifetimes τ > 10²⁸ years require global minimum

### 1.2 Brane-Frozen (ξ-BC)

**Definition:**
```
∂_ξ f|_{boundaries} = 0   (Neumann)
or
f|_{boundaries} = v        (Dirichlet/stiff)
```

**What it does:**
- Pins the ξ-profile at brane boundaries
- Determines mode spectrum (zero mode existence)
- Affects long-range interaction structure

**Physical justification:**
- Israel junction conditions imply BC for bulk fields
- Brane-localized matter creates effective Robin/Dirichlet terms

---

## 2. WHICH ADDRESSES WHICH NO-GO?

### 2.1 The No-Go Result (aside_p2_closure_v3)

**Problem:** Linearized V_lin(d) is monotonically increasing → no minimum without core physics.

**Question:** Does radial-frozen or brane-frozen resolve this?

### 2.2 Radial-Frozen Contribution

**YES — radial-frozen addresses the no-go!**

Here's why:

The radial step function f(r) = Θ(r - a) creates:
1. **Sharp core boundary** at r = a
2. **Core energy** ∝ σ × Vol(core) that diverges as cores overlap
3. **Theorem 2** in aside_p2_closure_v3: V_core → +∞ as d → 0

This is exactly what creates the minimum:
- V_core diverges at d → 0 (from radial-frozen)
- V_lin diverges at d → ∞ (from log growth)
- Continuity → minimum at some d₀

**Radial-frozen provides V_core, which resolves the no-go.**

### 2.3 Brane-Frozen Contribution

**NO — brane-frozen does NOT resolve the no-go.**

From this investigation (Sections 03-05):
- Changing BC (Neumann → Robin → Dirichlet) does not change V'_lin sign
- Changing weight (uniform → surface) does not create attraction
- The monotonicity V'_lin > 0 is robust

**Brane-frozen affects V_lin but does not fix the no-go.**

---

## 3. COMPARISON TABLE

| Aspect | Radial-Frozen f(r) | Brane-Frozen (ξ-BC) |
|--------|-------------------|---------------------|
| **Definition** | f(r) = Θ(r-a) | BC at ξ = 0, δ |
| **Direction** | Radial (r) | Fifth dimension (ξ) |
| **Creates core energy?** | YES | NO |
| **V_core → +∞ at d→0?** | YES (Theorem 2) | NO |
| **Affects V_lin?** | Indirectly | YES (mode spectrum) |
| **Changes V'_lin sign?** | N/A | NO |
| **Resolves no-go?** | YES | NO |
| **Needed for minimum?** | YES (essential) | NO (helpful but not essential) |

---

## 4. WHY THE CONFUSION?

### 4.1 Both Called "Frozen"

The word "frozen" is used for two different things:
1. **Radial frozen:** Sharp r-boundary (step function)
2. **ξ-frozen:** Stiff ξ-profile (Dirichlet BC)

### 4.2 Both Involve Stiff Limits

Both arise from stiff/tension limits:
- Radial frozen: σ → ∞ (membrane tension)
- ξ-frozen: λ → ∞ (boundary pinning strength)

### 4.3 But They Address Different Physics

- Radial frozen → core structure → V_core
- ξ-frozen → mode spectrum → V_lin structure

**They are independent and serve different purposes.**

---

## 5. WHAT IS TRULY DERIVED VS PHENOMENOLOGICAL

### 5.1 Fully Derived [Der]

1. **BC from action variation** (Section 02)
   - Neumann if no boundary terms
   - Robin if quadratic boundary terms
   - Dirichlet in stiff limit

2. **Mode spectrum under BC** (Section 03)
   - Eigenvalues and eigenfunctions for each BC type

3. **V'_lin(d) > 0 for all BC** (Section 05)
   - Rigorous sign analysis

4. **Core divergence from topology** (aside_p2_closure_v3, Theorem 2)
   - V_core → +∞ as d → 0 from winding + gradient energy

### 5.2 Derived Conditional [Dc]

1. **Minimum exists** (Theorem 3)
   - Conditional on continuity of energy functional

2. **Israel junction → Robin BC**
   - Conditional on specific matter coupling

### 5.3 Postulated [P]

1. **Radial step profile f(r) = Θ(r-a)**
   - Motivated by σ → ∞ limit, but not derived from action

2. **Specific form of core energy V_core(d)**
   - Theorem 2 gives divergence but not exact functional form

3. **Minimum location d₀ ~ δ**
   - Requires numerical calculation or additional assumptions

---

## 6. INTEGRATION WITH CHAPTER 2

### 6.1 Chapter 2's Approach

Chapter 2 uses radial-frozen (step function) profiles to derive:
- Vol(B³) = 4π/3 for electron
- Area(S³)³ = (2π²)³ for proton
- m_p/m_e = 6π⁵

This is **correct and consistent** — Chapter 2 needs radial-frozen for geometric coefficients.

### 6.2 This Investigation's Contribution

This investigation shows:
- ξ-BC (brane-frozen) do NOT create attraction
- ξ-BC do NOT resolve the no-go for V_lin
- The minimum relies on radial-frozen (core physics)

**Chapter 2's use of radial-frozen is ESSENTIAL and CORRECT.**

### 6.3 No Contradiction

There is no contradiction between:
- Chapter 2's radial frozen → geometric coefficients
- This investigation's brane frozen → mode spectrum

Both can be true simultaneously:
- Particles have step function r-profiles (radial frozen)
- The brane has Neumann/Robin/Dirichlet ξ-BC (brane frozen)

---

## 7. IMPLICATIONS FOR P2 DERIVATION

### 7.1 What P2 Claims

> "Flux tubes have V(r) with repulsion at small r and minimum at r₀"

### 7.2 What Is Now Clear

1. **Repulsion at small r:** Comes from radial-frozen core (topology), NOT from ξ-BC

2. **Minimum existence:** Comes from core + log balance, NOT from ξ-BC attraction

3. **Minimum location r₀ ~ δ:** NOT derived; requires calculation or assumption

### 7.3 Updated Status of P2

| Component | Status | Source |
|-----------|--------|--------|
| V → +∞ at d → 0 | [Der] | Radial-frozen core, Theorem 2 |
| V → +∞ at d → ∞ | [Dc] | Log growth (2D) |
| Minimum exists | [Dc] | Continuity (Theorem 3) |
| Minimum at d₀ ~ δ | [P] or [Cal] | NOT derived |
| "BC create attraction" | **FALSE** | This investigation |

---

## 8. CONCLUSION

### 8.1 The Key Distinction

**Radial-frozen (r):** Creates core energy, resolves no-go, essential for minimum.

**Brane-frozen (ξ):** Affects mode spectrum, does NOT resolve no-go, helpful but not essential.

### 8.2 What This Investigation Achieved

1. **Clarified** the distinction between two types of "frozen"
2. **Proved** that ξ-BC cannot create attraction in V_lin
3. **Confirmed** that the minimum mechanism is topological (core), not from BC
4. **Validated** Chapter 2's reliance on radial-frozen profiles

### 8.3 The Honest Statement

> "The frozen regime in EDC involves two independent aspects: (1) radial step profiles f(r) = Θ(r-a) for particle cores, which provide the short-range repulsion essential for the interaction minimum; and (2) brane boundary conditions in ξ, which affect the mode spectrum but do not create attraction. The minimum in V(d) arises from the balance of topological core repulsion [Der] and logarithmic confinement [Dc], not from ξ-BC effects."
