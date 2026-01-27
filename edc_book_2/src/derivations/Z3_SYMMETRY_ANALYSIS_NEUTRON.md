# Z₃ Symmetry Analysis for Neutron Configuration

**Date:** 2026-01-27
**Status:** [P]+[OPEN] — Framework for rigorous Z₃ analysis
**Purpose:** Determine whether neutron is Z₃-symmetric or Z₃-broken

---

## 0. Key Finding from Codebase

**The three Y-junction arms have IDENTICAL boundary conditions.**

Evidence:
- Lemma B3 (04c_routeB_z6_steiner.tex): "τ₁ = τ₂ = τ₃ = τ" from Z₃ permutation invariance
- Steiner theorem requires equal tensions
- No explicit symmetry-breaking terms documented

**Consequence:** Analysis follows path (2B) — spontaneous symmetry breaking possible, not explicit breaking.

---

## 1. Setup: Z₃ Group Action

### 1.1 Configuration Space

Let C = {L₁, L₂, L₃, θ₁₂, θ₂₃, θ₃₁} denote a Y-junction configuration where:
- Lᵢ = length of arm i
- θᵢⱼ = angle between arms i and j

Constraint: θ₁₂ + θ₂₃ + θ₃₁ = 2π

### 1.2 Z₃ Action

Define generator g ∈ Z₃ by cyclic permutation:
```
g · (L₁, L₂, L₃) = (L₂, L₃, L₁)
g · (θ₁₂, θ₂₃, θ₃₁) = (θ₂₃, θ₃₁, θ₁₂)
```

The Z₃ group is {e, g, g²} with g³ = e.

### 1.3 Energy Functional

Assume the energy functional has the form:
```
E[C] = τ(L₁ + L₂ + L₃) + U(θ₁₂, θ₂₃, θ₃₁) + E_BC[C]
```

where:
- τ = string tension (equal for all arms by Z₆ crystallization)
- U = angular interaction energy
- E_BC = boundary condition contribution (same for all arms)

**Claim [Dc]:** E[g·C] = E[C] for all C (Z₃ invariance)

**Proof:** Since τ is the same for all arms and BC are identical:
- Length term: Σ Lᵢ is invariant under permutation
- Angular term: U is a symmetric function of angles (no preferred arm)
- BC term: Same BC ⇒ same contribution under permutation ∎

---

## 2. Irreducible Representations of Z₃

### 2.1 Character Table

| Irrep | e | g | g² | Dimension |
|-------|---|---|----|-----------|
| A (singlet) | 1 | 1 | 1 | 1 |
| E₊ (doublet) | 1 | ω | ω² | 1 |
| E₋ (doublet) | 1 | ω² | ω | 1 |

where ω = e^(2πi/3).

### 2.2 Basis for Perturbations

**Singlet mode (A):**
```
δL_A = (1, 1, 1) · (δL₁, δL₂, δL₃)ᵀ / √3
```
= Symmetric breathing mode (all arms stretch equally)

**Doublet modes (E):**
```
δL_E₊ = (1, ω, ω²) · (δL₁, δL₂, δL₃)ᵀ / √3
δL_E₋ = (1, ω², ω) · (δL₁, δL₂, δL₃)ᵀ / √3
```
= Asymmetric deformation modes

**Real basis for doublet:**
```
Δ₁ = L₁ - L₂
Δ₂ = L₂ - L₃
```

Z₃ symmetry ⟺ Δ₁ = Δ₂ = 0

---

## 3. Order Parameter and Landau Expansion

### 3.1 Energy Near Critical Point

Expand energy around the Z₃-symmetric configuration:
```
E(q, Δ) = E₀(q) + a(q)·Δ² + b(q)·Δ⁴ + O(Δ⁶)
```

where:
- q = collective coordinate (singlet mode)
- Δ² = Δ₁² + Δ₂² (invariant under Z₃)
- a(q), b(q) = Landau coefficients

### 3.2 Stability Criterion

**At proton (q=0):**
- Steiner theorem ⇒ Hessian is positive definite
- Therefore: a(0) > 0 ✓
- Proton IS Z₃-symmetric (stable)

**At neutron (q=q_n):**
- If a(q_n) > 0: Neutron is Z₃-symmetric
- If a(q_n) < 0: Neutron is Z₃-broken (spontaneously)

### 3.3 Critical Question [OPEN]

**What is sign(a(q_n))?**

This determines:
1. Whether neutron is symmetric or has 3 degenerate states
2. The interpretation of q as singlet-only or singlet+doublet
3. The geometric meaning of barrier crossing

---

## 4. Connection to V_B = 2×Δm_np

### 4.1 Scenario A: Neutron is Z₃-Symmetric (a(q_n) > 0)

If neutron preserves Z₃ symmetry:
- q is a singlet coordinate throughout
- Barrier is also Z₃-symmetric
- Factor 2 must arise from singlet dynamics alone

**Possible mechanism:** The barrier corresponds to a Z₃-symmetric excited state where all three arms are equally stressed.

Energy levels:
| State | Energy | Z₃ status |
|-------|--------|-----------|
| Proton | 0 | Symmetric (minimum) |
| Neutron | Δm_np | Symmetric (local min) |
| Barrier | 3×Δm_np | Symmetric (saddle) |

V_B = 3×Δm_np - Δm_np = 2×Δm_np ✓

**Why 3×Δm_np?** If each arm contributes Δm_np/3 to the neutron excess, then the fully-stressed symmetric barrier has 3× that contribution.

### 4.2 Scenario B: Neutron is Z₃-Broken (a(q_n) < 0)

If neutron spontaneously breaks Z₃:
- Neutron exists in one of three degenerate states C_n^(1), C_n^(2), C_n^(3)
- Barrier crossing involves domain-wall-like transitions
- Factor 2 might arise from pair creation/annihilation

**Possible mechanism:** Transition between degenerate minima requires crossing two domain walls.

**Problem:** This scenario would predict observable differences between the three neutron states — not consistent with single neutron species.

### 4.3 Assessment

**Scenario A (Z₃-symmetric neutron) is more consistent** with:
1. Single neutron species observed
2. No Z₃-breaking observables (e.g., threefold multiplicity)
3. The clean factor-2 relationship

### 4.4 Observational Constraint on Doublet Mode [BL]+[M]

**Observation [BL]:** No low-lying "neutron partners" are observed that would
correspond to a Z₃-multiplet structure (i.e., no near-degenerate doublet
companions in the baryon spectrum at accessible energies).

**Mathematics [M]:** In a Z₃-symmetric quantum system with three equivalent
classical minima, quantization typically yields:
- 1 singlet state (symmetric superposition of three minima)
- 2 doublet states (near-degenerate partners)
- Splitting between singlet and doublet: Δ ~ e^{-S/ℏ} (tunnel-suppressed)

If doublet instability (a(q_n) < 0) were present, we would expect either:
- Visible multiplet structure (singlet + doublet states)
- Observable splitting or transitions between Z₃ sectors
- Low-lying "partner" modes in the neutron excitation spectrum

**Conclusion [BL]+[M] (constraint, not proof):**

> The absence of observed low-lying doublet partners constrains the doublet
> mode to be either:
> (a) stable in the accessible energy domain (a(q_n) > 0), OR
> (b) present but with splitting/partners pushed above observable range.

Within the EDC effective framework, interpretation (a) is the natural choice:
**a(q_n) > 0, doublet mode stable, neutron remains Z₃-symmetric.**

**Important caveat:** This is a [BL]+[M] constraint, NOT a strict mathematical
proof that a(q_n) > 0. A rigorous proof would require either:
- Explicit Hessian calculation in doublet directions, OR
- Convexity/symmetrization lemma showing energy minimum is in Z₃ fixed-point set

---

## 5. Minimal Proof Package for Book

To rigorously establish neutron Z₃ symmetry:

### Step 1: Define Z₃ action [M]
```latex
\textbf{Definition.} The Z₃ action on Y-junction configurations is:
g \cdot (L_1, L_2, L_3) = (L_2, L_3, L_1)
```

### Step 2: Prove energy invariance [Dc]
```latex
\textbf{Lemma.} E[g \cdot \mathcal{C}] = E[\mathcal{C}] for all configurations.
\textit{Proof:} Follows from identical BC on all three arms (no preferred direction).
```

### Step 3: Introduce order parameter [M]
```latex
\textbf{Definition.} The asymmetry order parameter is:
\Delta = |\Delta_1|^2 + |\Delta_2|^2, \quad \Delta_i = L_i - L_{i+1}
Z₃ symmetry ⟺ Δ = 0.
```

### Step 4: Verify stability [OPEN — needs calculation]
```latex
\textbf{Proposition.} The second variation δ²E in the doublet direction
has positive eigenvalue at q = q_n (neutron).

\textit{To prove:} Show a(q_n) > 0 in the Landau expansion.
```

### Step 5: Derive V_B = 2×Δm_np [Dc]
```latex
\textbf{Corollary.} If neutron is Z₃-symmetric with energy Δm_np above proton,
and the Z₃-symmetric barrier has energy 3×Δm_np above proton,
then V_B = 2×Δm_np.
```

---

## 6. Open Questions

### Q1: What determines 3×Δm_np for barrier?

**Ansatz [P]:** At the barrier, all three arms are equally stressed, each contributing one "unit" of Z₆-breaking energy.

**Needed:** Explicit calculation from 5D action showing barrier configuration has E = 3×Δm_np.

### Q2: What is the geometric meaning of Δm_np?

**Two options for Δm_np:**
- **Option B [BL]:** Δm_np = 1.2933 MeV (PDG baseline)
- **Option A [Dc]:** Δm_np = (5/2 + 4α) m_e = 1.2924 MeV (Book formula)

Where 5/2 = D_bulk/D_membrane is a dimensional projection factor.

**Note:** A previous version incorrectly stated "Δm_np = 8 m_e c² / π [Der]".
This formula was not supported by the codebase and has been corrected.

**Interpretation:** The geometric/dimensional projection of 5D→2D (factor 5/2)
plus electromagnetic correction (4α) gives the neutron excess energy.

### Q3: Why does one unit = Δm_np?

This connects to the deeper question: what is the microscopic origin of the neutron-proton mass difference?

---

## 7. Summary

| Question | Answer | Status |
|----------|--------|--------|
| Are BC identical for all arms? | YES | [Dc] from codebase |
| Is explicit Z₃ breaking present? | NO | — |
| Is spontaneous breaking constrained? | YES — no low-lying doublet partners observed | [BL]+[M] constraint |
| Is neutron Z₃-symmetric? | Favored interpretation within EDC | [Dc] (constrained by [BL]+[M]) |
| Why V_B = 2×Δm_np? | Barrier at 3×Δm_np, neutron at 1×Δm_np | [Dc] |
| What determines "3"? | Z₃ symmetry: one unit per arm | [Dc] — **OPEN: needs 5D verification** |

**Key insight:** Absence of low-lying doublet partners [BL] constrains the doublet mode,
favoring a(q_n) > 0 within the EDC framework. This is a constraint, not a strict proof.

**Remaining OPEN:** "One unit per leg = Δm_np" requires 5D action verification;
Z₃ symmetry implies equal partition but does not determine the quantized unit.

---

## 8. Route C Corridor (5D→1D Reduction)

**Link:** See `derivations/S5D_TO_SEFF_Q_REDUCTION.md`

The formal pathway from 5D action to effective 1D dynamics:
```
S_5D → S_eff[q] = ∫ dt (½ M(q) q̇² − V(q))
```

**Relevance to Z₃ analysis:**
- V(q) shape determines whether Z₃ saddle exists
- Route C can validate/derive the "3×Δm_np" barrier structure
- "One unit per leg = Δm_np" remains OPEN until V(q) is computed

---

## 9. References

- 04b_proton_anchor.tex: Proton stability proof
- 04c_routeB_z6_steiner.tex: Z₆ crystallization and equal tensions
- 05b_neutron_dual_route.tex: Neutron metastability
- V_B_FROM_Z3_BARRIER_CONJECTURE.md: V_B = 2×Δm_np conjecture
- S5D_TO_SEFF_Q_REDUCTION.md: Route C corridor (5D→1D reduction)
