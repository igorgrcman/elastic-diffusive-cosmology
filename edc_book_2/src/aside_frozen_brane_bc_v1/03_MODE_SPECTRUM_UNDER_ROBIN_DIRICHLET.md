# 03: MODE SPECTRUM UNDER ROBIN AND DIRICHLET BC

**Purpose:** Solve for ξ-eigenmodes under various BC and determine how the zero mode (crucial for log term) behaves.

---

## 1. EIGENVALUE PROBLEM

### 1.1 Setup

We seek modes φ_m(ξ) satisfying:
```
-d²φ_m/dξ² = μ_m² φ_m    on ξ ∈ [0, δ]
```

with boundary conditions at ξ = 0 and ξ = δ.

The μ_m are the mode masses (or inverse characteristic lengths).

### 1.2 General Solution

```
φ_m(ξ) = A cos(μ_m ξ) + B sin(μ_m ξ)
```

The BC determine the allowed values of μ_m and the ratio A/B.

---

## 2. CASE 1: NEUMANN–NEUMANN (Baseline)

### 2.1 Boundary Conditions

```
dφ/dξ |_{ξ=0} = 0
dφ/dξ |_{ξ=δ} = 0
```

### 2.2 Solution

At ξ = 0: dφ/dξ = -A μ sin(0) + B μ cos(0) = B μ = 0

Therefore B = 0 (assuming μ ≠ 0) or μ = 0.

At ξ = δ: dφ/dξ = -A μ sin(μδ) = 0

Therefore sin(μδ) = 0, giving μ_m δ = mπ for m = 0, 1, 2, ...

### 2.3 Eigenvalues and Eigenfunctions

**Eigenvalues:** [M]
```
μ_m = mπ/δ,    m = 0, 1, 2, ...
```

**Eigenfunctions:** [M]
```
φ_m(ξ) = cos(mπξ/δ)
```

**Zero mode (m = 0):** μ₀ = 0, φ₀(ξ) = 1 (constant)

**The zero mode EXISTS under Neumann BC.**

---

## 3. CASE 2: DIRICHLET–DIRICHLET

### 3.1 Boundary Conditions

```
φ|_{ξ=0} = 0
φ|_{ξ=δ} = 0
```

### 3.2 Solution

At ξ = 0: φ(0) = A = 0

At ξ = δ: φ(δ) = B sin(μδ) = 0

For non-trivial solution (B ≠ 0): sin(μδ) = 0, giving μδ = mπ for m = 1, 2, 3, ...

Note: m = 0 is excluded because it would give φ ≡ 0.

### 3.3 Eigenvalues and Eigenfunctions

**Eigenvalues:** [M]
```
μ_m = mπ/δ,    m = 1, 2, 3, ...
```

**Eigenfunctions:** [M]
```
φ_m(ξ) = sin(mπξ/δ)
```

**CRITICAL: No zero mode under Dirichlet–Dirichlet BC!**

The m = 0 mode (constant) does not satisfy φ(0) = φ(δ) = 0.

---

## 4. CASE 3: ROBIN–ROBIN (General)

### 4.1 Boundary Conditions

```
dφ/dξ |_{ξ=0} = κ_0 φ|_{ξ=0}
dφ/dξ |_{ξ=δ} = -κ_δ φ|_{ξ=δ}
```

### 4.2 Solution

General: φ(ξ) = A cos(μξ) + B sin(μξ)

**At ξ = 0:**
```
dφ/dξ|_0 = Bμ = κ_0 A
```
Therefore: B = κ_0 A / μ (for μ ≠ 0)

**At ξ = δ:**
```
dφ/dξ|_δ = -Aμ sin(μδ) + Bμ cos(μδ) = -κ_δ [A cos(μδ) + B sin(μδ)]
```

Substituting B = κ_0 A / μ:
```
-Aμ sin(μδ) + (κ_0 A/μ) μ cos(μδ) = -κ_δ [A cos(μδ) + (κ_0 A/μ) sin(μδ)]
```

Simplify (divide by A):
```
-μ sin(μδ) + κ_0 cos(μδ) = -κ_δ cos(μδ) - (κ_0 κ_δ/μ) sin(μδ)
```

Rearrange:
```
-μ sin(μδ) + (κ_0 κ_δ/μ) sin(μδ) = -κ_δ cos(μδ) - κ_0 cos(μδ)
```

```
sin(μδ) [κ_0 κ_δ/μ - μ] = -(κ_0 + κ_δ) cos(μδ)
```

```
sin(μδ) (κ_0 κ_δ - μ²) = -μ(κ_0 + κ_δ) cos(μδ)
```

### 4.3 Eigenvalue Equation (Robin)

**Transcendental equation:** [M]
```
tan(μδ) = μ(κ_0 + κ_δ) / (μ² - κ_0 κ_δ)
```

This must be solved numerically in general.

### 4.4 Special Limits

**Limit κ_0, κ_δ → 0 (Robin → Neumann):**
```
tan(μδ) → 0  ⟹  μδ = mπ
```
Recovers Neumann spectrum. ✓

**Limit κ_0, κ_δ → ∞ (Robin → Dirichlet):**

The RHS → (κ_0 + κ_δ)/μ × μ/(μ² - κ_0 κ_δ) → 0 as κ → ∞

More carefully: tan(μδ) → -μ(κ_0 + κ_δ)/(κ_0 κ_δ) → -μ/κ → 0

So μδ → mπ but with m ≥ 1 (no zero mode).

### 4.5 Zero Mode Under Robin?

For μ = 0, the general solution is φ(ξ) = A + Bξ.

At ξ = 0: dφ/dξ|_0 = B = κ_0 A

At ξ = δ: dφ/dξ|_δ = B = -κ_δ (A + Bδ) = -κ_δ A - κ_δ B δ

From first equation: B = κ_0 A

Substitute into second: κ_0 A = -κ_δ A - κ_δ κ_0 A δ

```
κ_0 A = -κ_δ A (1 + κ_0 δ)
```

For A ≠ 0:
```
κ_0 = -κ_δ (1 + κ_0 δ)
```

This has a solution only for specific κ_0, κ_δ relations.

**Generic Robin BC: NO zero mode** (μ = 0 not allowed generically).

**Exception:** If κ_0 = κ_δ = 0, then B = 0 and φ = const is allowed (Neumann limit).

---

## 5. CASE 4: DIRICHLET WITH MATCHING VALUES

### 5.1 Boundary Conditions

```
φ|_{ξ=0} = v
φ|_{ξ=δ} = v
```

(same value at both boundaries)

### 5.2 Decomposition

Write φ(ξ) = v + ψ(ξ) where ψ satisfies homogeneous Dirichlet:
```
ψ|_{ξ=0} = 0
ψ|_{ξ=δ} = 0
```

The constant part v is the "zero mode" contribution.

### 5.3 Interpretation

**The constant function φ = v satisfies the Dirichlet BC with matching values.**

This is effectively a "zero mode" but it's a particular solution, not part of the homogeneous spectrum.

For Green's function purposes, the field can have a constant (frozen) part plus fluctuating modes.

---

## 6. SUMMARY TABLE

| BC Type | Zero Mode? | Lowest Mode | Effect on log term |
|---------|------------|-------------|-------------------|
| Neumann–Neumann | YES (m=0) | μ₀ = 0 | Log term PRESENT |
| Dirichlet–Dirichlet | NO | μ₁ = π/δ | Log term ABSENT |
| Robin–Robin (generic) | NO | μ₁ > 0 | Log term ABSENT |
| Dirichlet (matching v) | YES* | Constant v | Log term PRESENT* |

*For Dirichlet with matching boundary values, the constant v acts like a zero mode.

---

## 7. IMPLICATIONS FOR V(d)

### 7.1 Recall: Log Term Origin

The logarithmic term in V(d) comes from the zero mode Green's function:
```
G₀(r) = -(1/2π) ln(r/L)
```

### 7.2 If Zero Mode Is Removed (Dirichlet or Robin)

**No zero mode → No log term → V_lin(d) changes character!**

The interaction becomes:
```
V_lin(d) = Σ_{m≥1} (coefficients) × K₀(μ_m d)
```

All terms are Yukawa-like (exponentially screened).

### 7.3 Is This "Attractive"?

Let's check the sign for the massive-mode-only case:
```
V_lin(d) = -(2/π) n₁n₂ Σ_{m≥1} w_m K₀(μ_m d)
```

where w_m > 0 are positive weights.

For same-sign vortices (n₁n₂ > 0): V_lin(d) < 0.

**BUT** the derivative:
```
dV_lin/dd = (2/π) n₁n₂ Σ_{m≥1} w_m μ_m K₁(μ_m d) > 0
```

**Still monotonically increasing** (since K₁ > 0).

---

## 8. KEY RESULT

**Theorem (Mode Spectrum and Zero Mode):** [Der]

1. **Neumann BC:** Zero mode exists → log term in V(d)
2. **Dirichlet BC (homogeneous):** No zero mode → no log term
3. **Robin BC (generic):** No zero mode → no log term
4. **Dirichlet (matching values):** Constant mode acts as zero mode → effective log term

**Removing the zero mode does NOT create attraction.** The remaining K₀ sum is:
- Negative in value (V < 0)
- But has positive derivative (V' > 0)
- Therefore still monotonically increasing

**The no-go result (V'(d) > 0) persists even without the log term!**
