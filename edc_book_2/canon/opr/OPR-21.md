# OPR-21: BVP Mode Profiles — Lemma Chain

**Status**: CONDITIONAL [Dc] — structure derived, parameters [P]
**Branch**: `book2-opr21-physics-closure-v1`
**Date**: 2026-01-25 (Updated)
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

### Status: CONDITIONAL [Dc]

**Evidence**:
- Structure established: `ch12_bvp_workpackage.tex:147-162`
- Derivation skeleton: `ch14_bvp_closure_pack.tex:239-344`
- **V_eff derivation**: `audit/evidence/OPR21_VEFF_DERIVATION_REPORT.md`

**DERIVED [Dc]**: V_eff structure from 5D Dirac equation
```
V_L(ξ) = (M + 2A')² - (M + 2A')' = M² + 4MA' + 4(A')² - M' - 2A''
V_R(ξ) = (M + 2A')² + (M + 2A')'
```
For flat space (A = 0): V_L = M² - M', V_R = M² + M'.
Chirality asymmetry V_R - V_L = 2M' is the geometric origin of V−A.

**POSTULATED [P]**: Parameter values
- M(ξ) profile is postulated as domain wall: M(ξ) = M_0 tanh((ξ − ℓ/2)/Δ)
- M_0, Δ, ℓ values not derived from membrane action (blocks on OPR-01: σ anchor)

**REMAINING for full closure**:
- Derive M(ξ) from 5D action with membrane stress-energy
- Express (M_0, Δ) in terms of (σ, r_e, R_ξ)

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

**Lemma L3.2** (BC from Israel Junction) [CONDITIONAL [Dc]]
The Robin parameters (α, β) are derivable from Israel junction conditions combined
with brane-localized fermion mass terms.

### Status: CONDITIONAL [Dc]

**Evidence**:
- Skeleton provided: `ch14_bvp_closure_pack.tex:293-309`
- **Full derivation**: `audit/evidence/OPR21_BC_ISRAEL_REPORT.md`

**DERIVED [Dc]**: BC structure from variational principle
```
f'(0) + κ f(0) = 0    where κ = m_b/2
```
The brane-localized mass m_b sets the Robin parameter. This is α₀ = m_b/2, β₀ = 1.

**Self-adjointness verified**: For real m_b, BCs are automatically self-adjoint.

**POSTULATED [P]**: m_b value
- m_b is not derived from first principles; it requires OPR-01 (σ anchor)
- Candidate: m_b ~ σ/(M₅³) or m_b ~ 1/Δ

**REMAINING for full closure**:
- Derive m_b from EDC action
- Show m_b(σ, M₅) connection explicitly

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
- Domain wall: λ_th = M_0² (asymptotic potential value)

**OPR-02 link**: If N_bound = 3 robustly → explains three generations

**Status**: CONDITIONAL [Dc] — computed for physical V(ξ)

**Numerical results** (domain wall, flat space):
| μ = M₀ℓ | N_bound | Regime |
|---------|---------|--------|
| 2-3     | 0→1     | transition |
| 10-15   | 1→2     | transition |
| 25-35   | 3       | **TARGET** |
| >35     | 4+      | over-counting |

**Key finding**: N_bound = 3 is achieved for μ ∈ [25, 35). This is STABLE under BC
variations (kappa scan). However, μ = M_0 ℓ is [P] postulated, not derived.

**Evidence**: `code/opr21_bvp_physical_run.py`, `code/output/opr21_physical_summary.json`

---

## Closure Conditions

### Full Closure (OPR-21 → CLOSED)

1. ✓ **V(ξ) structure** derived from 5D Dirac (L2)
2. ✓ **BC structure** derived from Israel junction (L3.2)
3. ✓ **BVP numerically solved** with physical potential
4. ✓ **Outputs computed**: ψ_n, x₁, I₄, N_bound
5. ✓ **Robustness verified**: N_bound stable under BC variations
6. ✗ **Parameter values** (M_0, Δ, ℓ) derived from EDC action ← BLOCKS FULL CLOSURE

### CONDITIONAL Closure (Current Status)

1. ✓ V(ξ) = M² − M' structure derived [Dc]
2. ✓ BC κ = m_b/2 structure derived [Dc]
3. ✓ N_bound = 3 achieved for μ ∈ [25, 35) — PROMISING
4. ✓ Robustness: N_bound stable across (ℓ, κ) variations
5. ✗ Parameter values remain [P] postulated

**Current status**: CONDITIONAL [Dc]
- Structure derived, parameters postulated
- Blocking item: Derive (M_0, Δ, ℓ) from membrane tension σ (OPR-01)

---

## Cross-References

| Item | Status | Location |
|------|--------|----------|
| BVP Work Package | Infrastructure defined | ch12_bvp_workpackage.tex |
| BVP Closure Pack | Formal definitions | ch14_bvp_closure_pack.tex |
| V_eff Derivation | CONDITIONAL [Dc] | audit/evidence/OPR21_VEFF_DERIVATION_REPORT.md |
| BC Israel Report | CONDITIONAL [Dc] | audit/evidence/OPR21_BC_ISRAEL_REPORT.md |
| Foundation Report | Infrastructure validated | audit/evidence/OPR21_BVP_FOUNDATION_REPORT.md |
| Toy Demo Script | Validated | code/opr21_bvp_demo.py |
| Physical BVP Script | CONDITIONAL [Dc] | code/opr21_bvp_physical_run.py |
| OPR-01 (σ anchor) | OPEN, blocks OPR-21 closure | OPR_REGISTRY.md |
| OPR-02 (generations) | PARTIAL, uses OPR-21 N_bound | OPR_REGISTRY.md |
| OPR-22 (G_F) | OPEN, uses OPR-21 I₄ | OPR_REGISTRY.md |

---

## Next Steps

1. ✓ **DONE**: Derive V(ξ) structure from 5D Dirac
2. ✓ **DONE**: Derive BC structure from Israel junction
3. ✓ **DONE**: Numerical BVP with physical potential
4. ✓ **DONE**: Show N_bound = 3 achievable (μ ∈ [25, 35))
5. **NEXT**: Derive parameter values from EDC action (OPR-01 dependency)
6. **NEXT**: Connect μ = M₀ℓ to membrane tension σ

---

*Generated: 2026-01-25*
*Updated: 2026-01-25 (Physics closure sprint)*
*Status: CONDITIONAL [Dc]*
*Canon: Partial (structure is canon, parameters are [P])*
