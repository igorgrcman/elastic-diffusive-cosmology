# OPR-21: BVP Mode Profiles — Lemma Chain

**Status**: OPEN → Working draft
**Branch**: `book2-opr21-bvp-foundation-v1`
**Date**: 2026-01-25
**Blocks**: E-CH08-OPEN-003, E-CH08-P-003, OPR-22

---

## Executive Summary

OPR-21 is the **master unlock** for Book 2's weak sector quantitative claims. Without solved BVP mode profiles, the following remain circular or undefined:

1. **I₄ overlap integral** — needed for G_F spine
2. **Generation count N_bound** — needed for OPR-02 closure
3. **Chirality ratio R_LR** — needed for V−A consistency

This document provides the **lemma chain** establishing the mathematical structure of the thick-brane BVP, specifying what must be derived vs. what is already proven.

---

## Lemma Chain Overview

```
L1: Domain Definition
    ↓
L2: 5D Dirac → 1D Schrödinger Reduction
    ↓
L3: Robin BC from Variational Principle
    ↓
L4: Sturm-Liouville Self-Adjointness
    ↓
L5: Toy Model Validation (Pöschl-Teller)
    ↓
[OUTPUT]: Mode profiles f_L(ξ), eigenvalues λ_n, overlap I₄
```

---

## L1: Domain Definition

### Statement

**Definition L1.1** (BVP Domain) [M]
The thick-brane coordinate ξ lives on one of three domains:

| Domain | Notation | Physical Interpretation | Spectrum Type |
|--------|----------|------------------------|---------------|
| Finite interval | [0, ℓ] | Brane with finite thickness | Pure discrete |
| Half-line | [0, ∞) | Semi-infinite bulk | Discrete + continuous |
| Full line | (−∞, ∞) | Symmetric domain wall | Depends on V asymptotics |

### Status: ESTABLISHED [M]

**Evidence**: Definition documented in `ch14_bvp_closure_pack.tex:135-153`.

**EDC choice**: For Part II weak sector, **finite interval [0, ℓ]** is primary (thick brane with defined boundaries). Half-line appears in Ch9 (chirality suppression).

### Open Question

**OPEN-L1-Q1**: What sets ℓ?
- Candidates: ℓ ~ R_ξ (diffusion scale), ℓ ~ r_e (electron radius), ℓ ~ 1/m_φ (mediator Compton)
- Current status: ℓ is [P] postulated, not derived from membrane action

---

## L2: 5D Dirac → 1D Schrödinger Reduction

### Statement

**Lemma L2.1** (Dimensional Reduction) [Dc]
Starting from 5D Dirac equation in warped spacetime:
```
[i Γ^A D_A − M(ξ)] Ψ = 0
```
where Γ^A are 5D gamma matrices, D_A is covariant derivative, M(ξ) is ξ-dependent mass.

**IF** one assumes:
1. Warped metric: ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ²
2. KK ansatz: Ψ(x^μ, ξ) = ψ(x^μ) ⊗ f(ξ)
3. 4D massless limit for ψ: i γ^μ ∂_μ ψ = m_4D ψ

**THEN** the profile function f(ξ) satisfies Schrödinger-type equation:
```
[-d²/dξ² + V_eff(ξ)] f(ξ) = m² f(ξ)
```

where effective potential:
```
V_eff(ξ) = M(ξ)² + M'(ξ) + corrections from warp factor
```

### Status: PARTIAL [Dc]

**Evidence**:
- Structure established: `ch12_bvp_workpackage.tex:147-162`
- Derivation skeleton: `ch14_bvp_closure_pack.tex:239-344`

**OPEN-L2-Q1**: Explicit V(ξ) form
- The potential V_eff(ξ) is NOT yet derived from EDC action
- Currently using toy ansätze (sech², box, exponential)
- Closure requires completing 5-step pipeline in §14.2.2

**OPEN-L2-Q2**: Connection to membrane parameters
- Must express V(ξ) in terms of (σ, r_e, R_ξ)
- No SM smuggling: V(ξ) parameters cannot be tuned to match M_W or G_F

---

## L3: Robin BC from Variational Principle

### Statement

**Lemma L3.1** (General Robin Form) [M]
For self-adjoint Sturm-Liouville operator on [0, ℓ], BCs take general Robin form:
```
α₀ f(0) + β₀ f'(0) = 0
α_ℓ f(ℓ) + β_ℓ f'(ℓ) = 0
```
where (α_j, β_j) are real, separated, and non-degenerate.

### Status: ESTABLISHED [M]

**Evidence**: Theorem documented in `ch14_bvp_closure_pack.tex:169-201`, Theorem L3.1 at lines 212-228.

**Lemma L3.2** (BC from Israel Junction) [OPEN]
The Robin parameters (α, β) should be derivable from Israel junction conditions:
```
[K_ab] − g_ab [K] = −(1/M_{5,Pl}³) S_ab
```
where S_ab is brane stress-energy.

### Status: OPEN

**Evidence**:
- Skeleton provided: `ch14_bvp_closure_pack.tex:293-309`
- NOT yet completed with explicit calculation

**OPEN-L3-Q1**: Derive (α₀, β₀) from junction matching
**OPEN-L3-Q2**: Show result is compatible with self-adjointness

---

## L4: Sturm-Liouville Self-Adjointness

### Statement

**Theorem L4.1** (Self-Adjointness Criterion) [M]
The operator L̂ = −d²/dξ² + V(ξ) on [0, ℓ] with Robin BCs is self-adjoint IFF:
1. V(ξ) is real-valued and locally integrable on (0, ℓ)
2. BC parameters α_j, β_j ∈ ℝ
3. BCs are separated (each endpoint has its own condition)

### Status: ESTABLISHED [M]

**Evidence**: Theorem 14.2.3 in `ch14_bvp_closure_pack.tex:212-228`. Proof sketch via integration by parts.

**Corollary L4.2** (Spectral Properties) [M]
Under self-adjointness:
- Eigenvalues λ_n are real and discrete (for confining V)
- Eigenfunctions ψ_n are orthogonal: ⟨ψ_m, ψ_n⟩ = δ_mn
- Spectrum bounded below: ∃ λ₀ = min_n λ_n

### Status: ESTABLISHED [M]

---

## L5: Toy Model Validation (Pöschl-Teller)

### Statement

**Proposition L5.1** (Pöschl-Teller Spectrum) [M]
For potential V(ξ) = −V₀ sech²(ξ/a):
- Bound state count: N_bound = ⌊λ⌋ + 1 where λ = (−1 + √(1 + 4V₀a²))/2
- Ground state energy: E₀ = −λ²
- Ground state profile: ψ₀ ∝ sech^λ(ξ/a)

### Status: ESTABLISHED [M]

**Evidence**:
- Documented in `ch14_bvp_closure_pack.tex:444-464`
- Numerical demo: `code/bvp_halfline_toy_demo.py`
- Table verification: `ch14_bvp_closure_pack.tex:1055-1078` (N_bound stable across BC variations)

### Validation Results (V₀=10, a=1)

| ξ_max | κ (Robin) | N_bound | E₀ | x₁ = |E₀| | I₄^(0) |
|-------|-----------|---------|-----|---------|--------|
| 10.0 | 0.0 | 2 | −7.35 | 7.35 | 1.23 |
| 12.0 | 0.1 | 2 | −7.02 | 7.02 | 1.17 |
| 14.0 | 0.5 | 2 | −5.98 | 5.98 | 1.00 |

**Key observation**: N_bound is stable across truncation and BC variations, confirming Lemma L4.2 (spectral stability under admissible BC deformation).

---

## Output Objects

### O1: Normalized Eigenfunctions ψ_n(ξ)

**Definition** [Def]:
- L̂ψ_n = λ_n ψ_n (eigenvalue equation)
- ⟨ψ_n, ψ_n⟩ = 1 (unit normalization)
- BCs satisfied at both endpoints

**Status**: Computable once V(ξ) is specified [OPEN for physical V]

### O2: First Eigenvalue x₁

**Definition** [Def]:
```
x₁ = min{λ̃_n : λ̃_n > 0}
```
This is the lowest positive eigenvalue of dimensionless BVP.

**Role**: In G_F spine, x₁ sets the scale: G_F ∝ 1/(x₁ · scale²)

**Status**: Output from BVP, not input [OPEN for physical V]

### O3: Overlap Integral I₄

**Definition** [Def]:
```
I₄ = ∫_Ω |ψ₀(ξ)|⁴ dξ
```

**Physical interpretation**:
- Measures "concentration" of ground state
- Delta-like profile → I₄ → ∞ (strong coupling)
- Uniform profile → I₄ ~ 1/ℓ (weak coupling)

**Status**:
- Toy model: I₄ = 1.23 (V₀=10, a=1)
- Physical model: OPEN (requires derived V(ξ))

### O4: Generation Count N_bound

**Definition** [Def]:
```
N_bound = #{n : λ_n < λ_th and ψ_n ∈ L²(Ω)}
```

**Threshold definition**:
- Half-line: λ_th = inf σ_ess(L̂) = lim_{ξ→∞} V(ξ)
- Finite interval: Use gap criterion (spectral gap separation)

**OPR-02 link**: If N_bound = 3 robustly → explains three generations

**Status**: OPEN (requires physical V(ξ) + robustness scan)

---

## Closure Conditions

### Full Closure (OPR-21 → CLOSED)

1. **Derive V(ξ)** from membrane parameters (σ, r_e, R_ξ)
2. **Derive BC parameters** (α, β) from Israel junction
3. **Solve BVP numerically** with physical inputs
4. **Compute outputs**: ψ_n, x₁, I₄, N_bound
5. **Show robustness**: N_bound stable under admissible BC variations

### Partial Closure (OPR-21 → STRONG PARTIAL)

1. Specify V(ξ) ansatz family motivated by membrane physics
2. Show infrastructure works (current status via toy model)
3. Document dependency on V(ξ) derivation

**Current status**: STRONG PARTIAL (infrastructure complete, physics inputs missing)

---

## Cross-References

| Item | Status | Location |
|------|--------|----------|
| BVP Work Package | Infrastructure defined | ch12_bvp_workpackage.tex |
| BVP Closure Pack | Formal definitions | ch14_bvp_closure_pack.tex |
| Toy Demo Script | Validated | code/bvp_halfline_toy_demo.py |
| OPR-02 (generations) | OPEN, blocked by OPR-21 | OPR_REGISTRY.md |
| OPR-22 (G_F first-principles) | OPEN, blocked by OPR-21 | OPR_REGISTRY.md |

---

## Next Steps

1. **Immediate**: Create `code/opr21_bvp_demo.py` extending toy demo
2. **Short-term**: Derive V(ξ) from 5D action (OPR-21 main work)
3. **Medium-term**: Numerical scan over (V₀, a, α, β) parameter space
4. **Closure test**: Physical V(ξ) gives N_bound = 3 robustly

---

*Generated: 2026-01-25*
*Status: Working draft*
*Canon: NO (becomes canon after closure)*
