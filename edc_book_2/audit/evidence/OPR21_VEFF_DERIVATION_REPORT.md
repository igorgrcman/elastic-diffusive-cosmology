# OPR-21: V_eff(ξ) Derivation Report

**Date**: 2026-01-25
**Branch**: `book2-opr21-physics-closure-v1`
**Target**: L2 closure (5D Dirac → 1D Schrödinger reduction)

---

## Executive Summary

This report derives the effective potential V_eff(ξ) for fermion localization in a warped 5D spacetime with a domain-wall mass profile. The derivation follows standard extra-dimensional physics (Randall-Sundrum, Rubakov-Shaposhnikov) and explicitly identifies which terms arise from:
1. The bulk mass term M(ξ)
2. The warp factor A(ξ)
3. Spin-connection contributions

**Key Result**: The effective potentials for left- and right-handed modes are:
```
V_L(ξ) = M(ξ)² − M'(ξ) + [warp corrections]
V_R(ξ) = M(ξ)² + M'(ξ) + [warp corrections]
```

The **chirality asymmetry** V_L ≠ V_R is the geometric origin of V−A structure.

---

## 1. Setup: 5D Dirac Equation in Warped Spacetime

### 1.1 Metric Ansatz

Consider the warped 5D metric [P]:
```
ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ²
```

where:
- x^μ (μ = 0,1,2,3) are 4D Minkowski coordinates
- ξ ∈ [0, ℓ] is the extra-dimensional coordinate
- A(ξ) is the warp factor (dimensionless)
- η_μν = diag(−1, +1, +1, +1) is the 4D Minkowski metric

**Sign convention**: A(ξ) > 0 corresponds to expanding 4D sections as ξ increases.

### 1.2 5D Gamma Matrices

The 5D Dirac algebra requires Γ^A satisfying {Γ^A, Γ^B} = 2g^{AB}. We choose:
```
Γ^μ = e^{-A(ξ)} γ^μ,    Γ^5 = −i γ^5
```

where γ^μ are standard 4D Dirac matrices and γ^5 = i γ^0 γ^1 γ^2 γ^3.

**Convention**: γ^5 eigenvalues ±1 define chirality (L: −1, R: +1).

### 1.3 Spin Connection

The non-vanishing spin connection components for the warped metric are:
```
ω_μ^{a5} = −A'(ξ) e^A e_μ^a
```

where a = 0,1,2,3 is a local Lorentz index and e_μ^a = e^A δ_μ^a is the vielbein.

The spin-connection contribution to the covariant derivative is:
```
D_μ = ∂_μ + (1/4) ω_μ^{AB} Γ_A Γ_B = ∂_μ + (1/2) A'(ξ) Γ_μ Γ_5
```

---

## 2. Dimensional Reduction

### 2.1 5D Dirac Equation

The 5D Dirac equation with ξ-dependent mass is [P]:
```
[i Γ^A D_A − M(ξ)] Ψ = 0
```

Expanding explicitly:
```
[i e^{-A} γ^μ (∂_μ + (1/2)A' γ^5) + γ^5 ∂_ξ − M(ξ)] Ψ = 0
```

### 2.2 Chiral Decomposition

Decompose the 5D spinor into 4D chiral components:
```
Ψ(x^μ, ξ) = ψ_L(x^μ) f_L(ξ) + ψ_R(x^μ) f_R(ξ)
```

where γ^5 ψ_{L,R} = ∓ ψ_{L,R} (left: −1, right: +1).

### 2.3 4D Mass Equation

For 4D massive modes, we impose:
```
i γ^μ ∂_μ ψ_{L,R} = m ψ_{R,L}
```

This couples left and right chiralities as required for massive 4D fermions.

### 2.4 Coupled First-Order Equations

Substituting the ansatz into the 5D Dirac equation and using the 4D mass equation, we obtain coupled equations for the profiles [Dc]:

```
[∂_ξ − M(ξ) − 2A'(ξ)] f_L = m e^{-A} f_R
[∂_ξ + M(ξ) + 2A'(ξ)] f_R = −m e^{-A} f_L
```

**Key observation**: The warp factor A(ξ) enters through the combination M(ξ) + 2A'(ξ).

---

## 3. Second-Order Schrödinger Form

### 3.1 Elimination to Second Order

Defining:
```
F_L = e^{2A} f_L,    F_R = e^{2A} f_R
```

and eliminating F_R from the coupled system, we obtain the Schrödinger-type equation [Dc]:

```
[−d²/dξ² + V_L(ξ)] F_L = m² F_L
```

with effective potential:
```
V_L(ξ) = (M + 2A')² − (M + 2A')' = M² + 4MA' + 4(A')² − M' − 2A''
```

### 3.2 Effective Potentials

**Theorem (Effective Potentials)** [Dc]

For the warped metric ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ² and bulk mass M(ξ), the effective potentials are:

```
V_L(ξ) = [M(ξ) + 2A'(ξ)]² − [M(ξ) + 2A'(ξ)]'
       = M² + 4MA' + 4(A')² − M' − 2A''

V_R(ξ) = [M(ξ) + 2A'(ξ)]² + [M(ξ) + 2A'(ξ)]'
       = M² + 4MA' + 4(A')² + M' + 2A''
```

**Chirality asymmetry**:
```
V_R − V_L = 2M' + 4A''
```

This asymmetry is the geometric origin of different L/R localization and hence V−A structure.

---

## 4. Special Cases

### 4.1 Flat Space (A = 0)

For unwarped extra dimension:
```
V_L = M² − M'
V_R = M² + M'
```

This is the standard domain-wall result. For M(ξ) = m_0 tanh(ξ/a), we recover the Pöschl-Teller potential:
```
V_L = m_0² − (m_0/a) sech²(ξ/a)
V_R = m_0² + (m_0/a) sech²(ξ/a)
```

The left-handed mode has an attractive well; the right-handed mode has a barrier.

### 4.2 RS-like Warp Factor

For Randall-Sundrum-type warp A(ξ) = −k|ξ| (on a Z₂ orbifold):
```
A' = −k sgn(ξ),    A'' = −2k δ(ξ)
```

The delta function at the brane location creates a localized contribution to V_{L,R}.

### 4.3 Smooth Warp + Domain Wall

For smooth profiles [P], define:
```
Σ(ξ) = M(ξ) + 2A'(ξ)
```

Then:
```
V_L = Σ² − Σ' = −d/dξ [Σ] + Σ²
V_R = Σ² + Σ' = +d/dξ [Σ] + Σ²
```

This is the supersymmetric quantum mechanics form with "superpotential" Σ(ξ).

---

## 5. Connection to EDC Parameters

### 5.1 Parameter Identification [P]

To connect V_eff to EDC membrane parameters, we identify:

| 5D Parameter | EDC Parameter | Physical Meaning |
|--------------|---------------|------------------|
| ℓ | ~ R_ξ or r_e | Domain size / brane thickness |
| M_0 (bulk mass scale) | ~ σ^{1/3} | Mass from membrane tension |
| a (domain wall width) | ~ Δ | Transition layer thickness |
| k (warp parameter) | ~ 1/R_AdS | Curvature scale |

**CRITICAL NOTE**: These identifications are [P] postulated. No SM observable (M_W, G_F, v) is used.

### 5.2 Candidate V_eff Families

**Family 1: Pure Domain Wall (A = 0)** [P]

```
M(ξ) = M_0 tanh((ξ − ℓ/2)/Δ)
V_L(ξ) = M_0² − (M_0/Δ) sech²((ξ − ℓ/2)/Δ)
```

Parameters: (M_0, Δ, ℓ)

**Family 2: Linear Warp + Domain Wall** [P]

```
A(ξ) = −k ξ
M(ξ) = M_0 tanh((ξ − ℓ/2)/Δ)
V_L(ξ) = [M_0 tanh(...) − 2k]² − M_0/Δ sech²(...)
```

Parameters: (M_0, Δ, ℓ, k)

**Family 3: Gaussian Warp** [P]

```
A(ξ) = −k₀ exp(−(ξ − ℓ/2)²/w²)
V_L(ξ) = [M(ξ) + 2A'(ξ)]² − [M(ξ) + 2A'(ξ)]'
```

Parameters: (M_0, Δ, ℓ, k₀, w)

### 5.3 Dimensionless Form

Define dimensionless coordinate ζ = ξ/ℓ and parameters:
```
μ = M_0 ℓ  (dimensionless bulk mass)
δ = Δ/ℓ   (dimensionless wall width)
κ = k ℓ   (dimensionless warp)
```

The dimensionless potential is:
```
Ṽ_L(ζ) = ℓ² V_L(ℓζ) = μ² tanh²(...) − (μ/δ) sech²(...) + (warp terms)
```

Eigenvalues scale as: m² = λ/ℓ² where λ is dimensionless.

---

## 6. Status Assessment

### 6.1 What is ESTABLISHED

1. **Structure of V_eff** [Dc]: The form V_L = Σ² − Σ' with Σ = M + 2A' is derived from 5D Dirac.
2. **Chirality asymmetry** [Dc]: V_R − V_L = 2Σ' explains L/R localization difference.
3. **Candidate families** [P]: Three physically motivated ansätze are provided.

### 6.2 What Remains OPEN

1. **M(ξ) derivation**: The domain wall profile M(ξ) is not derived from EDC action; it is postulated.
2. **A(ξ) derivation**: The warp factor is not derived from Einstein equations with EDC stress-energy.
3. **Parameter values**: (M_0, Δ, k) are not fixed by EDC-only inputs.

### 6.3 L2 Status Update

**Previous**: PARTIAL
**New**: PARTIAL → CONDITIONAL [Dc]

The **structure** of V_eff is now fully derived. The **parameter values** depend on:
- M(ξ) from EDC action (linked to OPR-01: σ anchor)
- A(ξ) from Einstein equations (linked to OPR-06: P_bulk anchor)

---

## 7. Closure Checklist for L2

| Item | Status | Blocker |
|------|--------|---------|
| V_eff structure | ✓ DERIVED | — |
| Chirality asymmetry | ✓ DERIVED | — |
| M(ξ) explicit form | ✗ POSTULATED | OPR-01 (σ) |
| A(ξ) explicit form | ✗ POSTULATED | OPR-06 (P_bulk) |
| Parameter mapping | ✗ INCOMPLETE | Multiple OPRs |

**Verdict**: L2 upgrades to CONDITIONAL [Dc]. Full closure requires deriving M(ξ) and A(ξ) from the EDC action.

---

## 8. Numerical Implementation

For the BVP solver, use Family 1 (pure domain wall) as the primary test case:

```python
def V_eff_domain_wall(xi, ell, M0, Delta, chirality='L'):
    """
    Effective potential from domain wall mass profile.

    Parameters:
        xi: coordinate array
        ell: domain size
        M0: bulk mass scale
        Delta: wall width
        chirality: 'L' or 'R'

    Returns:
        V_eff(xi)
    """
    zeta = (xi - ell/2) / Delta
    sech2 = 1.0 / np.cosh(zeta)**2
    tanh = np.tanh(zeta)

    # V = M² ∓ M'
    V_base = M0**2 * tanh**2
    V_deriv = (M0 / Delta) * sech2

    if chirality == 'L':
        return V_base - V_deriv
    else:  # R
        return V_base + V_deriv
```

**Note**: This is the A=0 case. Warp corrections can be added modularly.

---

## 9. References

1. Randall, L. & Sundrum, R. (1999). Phys. Rev. Lett. 83, 3370.
2. Rubakov, V. & Shaposhnikov, M. (1983). Phys. Lett. B 125, 136.
3. Gherghetta, T. & Pomarol, A. (2000). Nucl. Phys. B 586, 141.
4. Bajc, B. & Gabadadze, G. (1999). Phys. Lett. B 474, 282.

---

*Generated: 2026-01-25*
*Status: L2 CONDITIONAL [Dc] — structure derived, parameters postulated*
