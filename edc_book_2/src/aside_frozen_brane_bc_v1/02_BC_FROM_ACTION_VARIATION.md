# 02: BOUNDARY CONDITIONS FROM ACTION VARIATION

**Purpose:** Derive ξ-boundary conditions from variational principle, not by assumption.

---

## 1. BULK ACTION

### 1.1 Minimal Bulk Action [P]

```
S_bulk = ∫ d²r dξ [ ½|∇Φ|² + U(|Φ|) ]
```

where:
- |∇Φ|² = |∂_r Φ|² + |∂_θ Φ|²/r² + |∂_ξ Φ|²
- U(|Φ|) = symmetry-breaking potential with minimum at |Φ| = v

### 1.2 Expanded Form

For Φ = f(r, ξ) e^{inθ} with f ∈ ℝ≥0:
```
S_bulk = 2π ∫₀^∞ r dr ∫₀^δ dξ [ ½(∂_r f)² + n²f²/(2r²) + ½(∂_ξ f)² + U(f) ]
```

---

## 2. BOUNDARY/BRANE TERMS

### 2.1 General Brane-Localized Action [P]

At ξ = 0:
```
S_{∂,0} = ∫ d²r [ V_0(Φ) + ½ κ_0 |Φ|² + ... ]
```

At ξ = δ:
```
S_{∂,δ} = ∫ d²r [ V_δ(Φ) + ½ κ_δ |Φ|² + ... ]
```

### 2.2 Specific Cases

**(A) No boundary terms (natural BC):**
```
S_∂ = 0
```

**(B) Quadratic boundary potential:**
```
S_∂ = ∫ d²r [ ½ κ_0 |Φ|² ]_{ξ=0} + ∫ d²r [ ½ κ_δ |Φ|² ]_{ξ=δ}
```

**(C) Pinning potential (stiff limit):**
```
S_∂ = ∫ d²r [ ½ λ_0 (|Φ| - v_0)² ]_{ξ=0} + ∫ d²r [ ½ λ_δ (|Φ| - v_δ)² ]_{ξ=δ}
```

---

## 3. VARIATION OF TOTAL ACTION

### 3.1 Total Action

```
S = S_bulk + S_{∂,0} + S_{∂,δ}
```

### 3.2 Variation

Consider variation δΦ (and δΦ* independently for complex field).

**Bulk variation:**
```
δS_bulk = ∫ d²r dξ [ ∂_r Φ* ∂_r(δΦ) + ... + ∂_ξ Φ* ∂_ξ(δΦ) + ... ]
```

Integrate by parts in ξ:
```
∫₀^δ dξ (∂_ξ Φ*)(∂_ξ δΦ) = [Φ* ∂_ξ δΦ]₀^δ - ∫₀^δ dξ (∂²_ξ Φ*) δΦ
```

Wait, let me be more careful. For the kinetic term:
```
∫₀^δ dξ (∂_ξ Φ*)(∂_ξ δΦ) = [(∂_ξ Φ*) δΦ]₀^δ - ∫₀^δ dξ (∂²_ξ Φ*) δΦ
```

Hmm, this doesn't look right either. Let me redo this properly.

The kinetic term is:
```
½ |∂_ξ Φ|² = ½ (∂_ξ Φ*)(∂_ξ Φ)
```

Varying with respect to Φ* (treating Φ and Φ* as independent):
```
δ[½ (∂_ξ Φ*)(∂_ξ Φ)] / δΦ* = ½ ∂_ξ Φ × (something)
```

Actually, for real f, let me simplify: take Φ = f e^{inθ} with f real, and vary f.

### 3.3 Variation for Real Profile f

Action:
```
S = 2π ∫ r dr ∫₀^δ dξ [ ½(∂_r f)² + ½(∂_ξ f)² + n²f²/(2r²) + U(f) ]
    + 2π ∫ r dr [ V_0(f)|_{ξ=0} + V_δ(f)|_{ξ=δ} ]
```

Vary f → f + δf:
```
δS = 2π ∫ r dr ∫₀^δ dξ [ (∂_r f)(∂_r δf) + (∂_ξ f)(∂_ξ δf) + n²f δf/r² + U'(f) δf ]
   + 2π ∫ r dr [ V'_0(f) δf|_{ξ=0} + V'_δ(f) δf|_{ξ=δ} ]
```

Integrate by parts in ξ:
```
∫₀^δ dξ (∂_ξ f)(∂_ξ δf) = [(∂_ξ f) δf]_{ξ=0}^{ξ=δ} - ∫₀^δ dξ (∂²_ξ f) δf
                        = (∂_ξ f)|_{δ} δf|_{δ} - (∂_ξ f)|_{0} δf|_{0} - ∫₀^δ dξ (∂²_ξ f) δf
```

Similarly for r (assuming δf → 0 as r → ∞).

### 3.4 Euler-Lagrange Equations

**Bulk equation (setting coefficient of δf in bulk to zero):**
```
-∂²_r f - (1/r) ∂_r f - ∂²_ξ f + n²f/r² + U'(f) = 0
```

This is the standard vortex equation.

### 3.5 Boundary Conditions (from boundary terms)

**At ξ = 0:**

Collecting terms involving δf|_{ξ=0}:
```
- (∂_ξ f)|_{ξ=0} + V'_0(f)|_{ξ=0} = 0
```

Therefore:
```
∂_ξ f |_{ξ=0} = V'_0(f)|_{ξ=0}
```

**At ξ = δ:**
```
+ (∂_ξ f)|_{ξ=δ} + V'_δ(f)|_{ξ=δ} = 0
```

Therefore:
```
∂_ξ f |_{ξ=δ} = - V'_δ(f)|_{ξ=δ}
```

---

## 4. SPECIFIC BOUNDARY CONDITIONS

### 4.1 Case A: No Boundary Terms (V_0 = V_δ = 0)

**Result:** Neumann BC
```
∂_ξ f |_{ξ=0} = 0
∂_ξ f |_{ξ=δ} = 0
```

**Status:** [Der] — derived from action with no boundary terms.

**Interpretation:** "Natural" BC; no flux escapes through boundaries.

### 4.2 Case B: Quadratic Boundary Potential

Let V_0(f) = ½ κ_0 f², V_δ(f) = ½ κ_δ f².

Then V'_0(f) = κ_0 f, V'_δ(f) = κ_δ f.

**Result:** Robin BC
```
∂_ξ f |_{ξ=0} = κ_0 f|_{ξ=0}
∂_ξ f |_{ξ=δ} = - κ_δ f|_{ξ=δ}
```

**Status:** [Der] — derived from action with quadratic boundary terms.

**Sign convention note:** The signs come from the variation; κ > 0 means outward derivative proportional to field value.

### 4.3 Case C: Pinning Potential (Stiff Limit)

Let V_0(f) = ½ λ_0 (f - v_0)², V_δ(f) = ½ λ_δ (f - v_δ)².

Then V'_0(f) = λ_0 (f - v_0), V'_δ(f) = λ_δ (f - v_δ).

**Result:**
```
∂_ξ f |_{ξ=0} = λ_0 (f - v_0)|_{ξ=0}
∂_ξ f |_{ξ=δ} = - λ_δ (f - v_δ)|_{ξ=δ}
```

**Stiff limit λ_0, λ_δ → ∞:**

For the BC to remain finite, we need f|_{ξ=0} → v_0 and f|_{ξ=δ} → v_δ.

**Result in stiff limit:** Dirichlet BC
```
f|_{ξ=0} = v_0
f|_{ξ=δ} = v_δ
```

**Status:** [Der] — Dirichlet emerges as stiff limit of pinning potential.

---

## 5. SUMMARY OF BC DERIVATION

| Boundary Action | BC at ξ = 0 | BC at ξ = δ | Status |
|-----------------|-------------|-------------|--------|
| None (V = 0) | ∂_ξ f = 0 (Neumann) | ∂_ξ f = 0 (Neumann) | [Der] |
| Quadratic (½κf²) | ∂_ξ f = κf (Robin) | ∂_ξ f = -κf (Robin) | [Der] |
| Pinning, λ → ∞ | f = v_0 (Dirichlet) | f = v_δ (Dirichlet) | [Der] |

---

## 6. ISRAEL JUNCTION CONNECTION [P]/[Dc]

### 6.1 The Claim

**Claim [P]:** Israel junction conditions with brane stress-energy induce Robin-type BC for matter fields.

### 6.2 Argument Sketch

1. Israel junction: [K_ab] - g_ab[K] = -(1/M₅³) S_ab

2. For a scalar field contributing to S_ab:
   S_ab ∝ ∂_a Φ ∂_b Φ - ½ g_ab (∂Φ)² + g_ab U(Φ)

3. The jump in extrinsic curvature K_ξξ relates to ∂_ξ Φ jumps.

4. Effective result: The discontinuity/jump conditions can be recast as Robin-type BC for the field.

### 6.3 Status

This mapping is **not rigorously proven here**. The claim is:
- **[P]** if asserted without derivation
- **[Dc]** if one accepts the Israel formalism applies to scalar matter

A full derivation would require:
- Explicit 5D action including gravity + scalar
- GHY boundary terms
- Variation and matching at the brane

This is **out of scope** for this investigation, but the qualitative conclusion stands: brane-localized stress-energy induces Robin-type (or Dirichlet in stiff limit) BC.

---

## 7. WHAT "FROZEN ON BRANE" MEANS (DERIVED)

### 7.1 Interpretation

**"Frozen on brane" = Dirichlet BC in the stiff limit**

When brane-localized potentials strongly pin the field value:
```
f|_{ξ=0,δ} = fixed value (typically v)
```

The ξ-profile is "frozen" at the boundaries, meaning:
- The field cannot fluctuate freely at the brane surfaces
- The boundary values are locked

### 7.2 Bulk Behavior Under Dirichlet BC

If f|_{ξ=0} = f|_{ξ=δ} = v (same pinning value):

The bulk solution must interpolate between these fixed values.

For a vortex far from core (r >> a), the bulk equation becomes:
```
-∂²_ξ f + (small terms) = 0
```

Solution with f(0) = f(δ) = v:
```
f(ξ) = v  (constant)
```

**This is the frozen ξ-profile!** The field is constant in ξ when boundary values match.

### 7.3 Mode Structure Change

**Neumann:** Zero mode exists (constant in ξ allowed).

**Dirichlet with matching values:** Zero mode is the only allowed mode (constant = v).

**Dirichlet with mismatched values:** No zero mode; field must vary in ξ.

---

## 8. KEY RESULT

**Theorem (BC from Action):** [Der]

Starting from the bulk + boundary action:
```
S = S_bulk + ∫_{∂} V(Φ)
```

the boundary conditions follow from the variational principle:
```
∂_ξ Φ|_boundary = V'(Φ)|_boundary
```

Special cases:
- V = 0 → Neumann
- V = ½κΦ² → Robin
- V = ½λ(Φ - v₀)² with λ → ∞ → Dirichlet

The "frozen on brane" regime corresponds to Dirichlet (stiff pinning), where the ξ-profile is locked at boundary values.
