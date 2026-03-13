# Phase 1 Implementation Plan: R1, R3, R4

## Overview

Phase 1 closes three foundational gaps in Book IV's derivation chain:
- **R4**: N_bonds = 3 topological proof for A=2 cluster (quick win)
- **R3**: V(q) double-well potential from 5D action (enables R2 prefactor)
- **R1**: L₀/δ = π² derivation (keystone — controls τ_n exponent)

Execution order: R4 → R3 → R1 (simplest first, each builds context for the next).

### Methodology Principle

> **Analitičke derivacije su primarne.** Svaki korak derivacije mora biti
> zapisan u LaTeX-u, čitljiv za čovjeka, sa svim međukoracima. Numerički
> izračuni dolaze SAMO na kraju kao nezavisna potvrda analitičkog rezultata.
> Nikada obrnuto — ne koristimo numeriku da "nađemo" rezultat pa ga naknadno
> opravdamo analitički.

All work uses EDC-native vocabulary. Empirical data appears only as verification.
No Standard Model constructs at any stage.

---

## Step 1: R4 — N_bonds = 3 Topological Proof

**Goal**: Promote N_bonds = 3 from [P] to [Der] via closed-form analytic proof.

### 1a. Analytic derivation (LaTeX document, human-readable)

Create `edc_book_4/chapters/ch10_appendix_Nbonds_proof.tex`:

**Theorem**: For two Y-junctions in the M₆ lattice, the energy-minimizing contact
configuration has exactly N_bonds = 3.

**Proof structure** (fully analytic, step by step):

**Lemma 1 — Upper bound**: N_bonds ≤ 3.
- Each Y-junction has exactly 3 arms (from Z₃ Steiner geometry, Ch.1 [Der]).
- Each arm is a worldsheet segment with definite orientation.
- A bond is a contact between one arm of J₁ and one arm of J₂.
- Each arm can participate in at most one bond (contact saturation).
- Therefore N_bonds ≤ min(3, 3) = 3. ∎

**Lemma 2 — Lower bound**: N_bonds ≥ 3.
- Define the contact energy between junctions J₁ and J₂:
  ```
  E_contact(n) = n · K_pin + E_restoring(3 - n)
  ```
  where K_pin < 0 (binding) and E_restoring > 0 (unsaturated arms create
  angular restoring force).
- For n = 1: Two unsaturated arms on each junction create torque.
  The unsaturated arm of J₁ has brane tension σ pulling it toward alignment
  with the nearest arm of J₂. The restoring energy is:
  ```
  E_restoring(2) = 2 × σ × A_arm × sin²(θ_mismatch/2)
  ```
  This is positive and of order K_pin, making n=1 energetically unfavorable.
- For n = 2: One unsaturated arm per junction. Same argument applies
  but with E_restoring(1) = σ × A_arm × sin²(θ/2).
- For n = 3: All arms saturated. E_restoring(0) = 0.
- The total energy E(n) = n·K_pin + E_restoring(3-n) is minimized at n = 3
  because |K_pin| > 0 and E_restoring ≥ 0, and both push toward n = 3.

**Lemma 3 — Uniqueness**: The n = 3 pairing is unique up to Z₃ rotation.
- The three arms of J₁ are at angles {0°, 120°, 240°}.
- The three arms of J₂ face J₁ at angles {180°, 300°, 60°}.
- The energy-minimizing pairing is arm₁↔arm₁', arm₂↔arm₂', arm₃↔arm₃'
  (complementary angles).
- Any other permutation increases mismatch angles and hence energy.
- The permutation group S₃ acts on pairings; the minimum is unique
  within each Z₃ orbit. ∎

**Corollary**: B_d = 3 × K_pin. [Der]

Each step written out with explicit equations, no gaps, no "it follows easily".

### 1b. Numerical verification (confirmation only)

Create `code/scripts/r4_nbonds_verify.py`:
- After the analytic proof is complete, verify numerically:
  - Discretize SO(3) rotations of two Y-junctions
  - Compute contact energy E(θ₁, θ₂, θ₃) for all configurations
  - Confirm global minimum has exactly 3 bonds with equal angles
- Output: "PASS: analytic result N_bonds = 3 confirmed numerically"
- This script does NOT discover the result — it only confirms the proof.

### 1c. Update ch10_deuterium.tex

- Promote N_bonds = 3 from [P] to [Der]
- Reference appendix proof
- Update epistemic status table

**Deliverables**: 1 LaTeX proof (~150 lines), 1 verification script (~150 lines),
1 chapter edit (epistemic table).

---

## Step 2: R3 — V(q) from 5D Action

**Goal**: Derive the double-well potential analytically from S_EDC. Promote from [P] to [Dc].

### 2a. Analytic derivation of 5D → 1D reduction (LaTeX, fully worked)

Create `edc_book_4/chapters/ch03_appendix_Vq_derivation.tex`:

**Section 1: Setup and definitions**

Write out the full 5D action explicitly:
```
S_EDC = S_bulk + S_brane + S_GHY
S_bulk = ∫ d⁵X √|G| (-ρ_Plenum)
S_brane = -σ ∫ d⁴x √|h|
S_GHY = ∫ d⁴x √|h| K
```

Define the collective coordinate q ∈ [0,1] parametrizing the junction
deformation from anchor (q=0, Z₆) to metastable (q=q_n, Z₃).

**Section 2: Brane embedding and induced metric**

For a Y-junction with arms at angles {α₁, α₂, α₃} = {0°, 120°, 240°}
deformed by parameter q:

```
αᵢ(q) = αᵢ⁰ + q · Δαᵢ
```

where Δαᵢ represents the angular deformation toward the Z₃ configuration.

The arm lengths change as:
```
ℓᵢ(q) = ℓ₀ + q · Δℓᵢ
```

Compute the induced metric h_μν(q) on the brane by pullback of the 5D
metric G_AB.

**Section 3: Brane energy as function of q**

The Nambu-Goto brane energy (static limit):
```
E_brane(q) = σ × Σᵢ ℓᵢ(q)
```

This is the total worldsheet length times tension. At q=0 (Steiner minimum),
this is minimized (by Steiner theorem, Ch.1). At q ≠ 0, the arm lengths
increase because the junction deviates from the Steiner configuration.

Expand to second order:
```
E_brane(q) = E_brane(0) + ½ σ L₀ · c₂ · q² + ...
```

where c₂ > 0 (Steiner minimum is a minimum, positive Hessian from Ch.1).

**Section 4: The metastable minimum from Z₃**

The metastable (Z₃) configuration is NOT on the quadratic expansion around
Z₆. It's a separate local minimum arising from the discrete symmetry.

Key argument: The Z₃ subgroup of Z₆ forces a secondary energy minimum.
The hexagonal lattice energy landscape has the Z₆ symmetry:
```
V(q) = V(q + 2π/6)   (periodic in angle space)
```

Between two Z₆ minima (separated by 2π/6 = 60°), the Z₃ symmetry
places a secondary minimum at the midpoint (30° rotation), which is
the metastable configuration.

Write out the Fourier expansion respecting Z₆:
```
V(q) = a₀ + a₆ cos(6q) + a₁₂ cos(12q) + ...
```

The double-well structure emerges from the first two terms.

**Section 5: Barrier height from brane geometry**

The barrier sits at the maximum between the anchor (q=0) and metastable
(q=q_n) minima.

Analytic derivation:
```
V_B = V(q_B) - V(q_n)
```

Express V_B in terms of σ, L₀, δ. The deformation from Z₆ to the
barrier configuration stretches the brane by:
```
ΔA = A_brane(q_B) - A_brane(q_n)
V_B = σ × ΔA
```

Compute ΔA from the explicit arm-length functions.

**Section 6: Effective mass M(q)**

The kinetic term in the effective 1D action:
```
T = ½ M(q) q̇²
```

M(q) comes from the kinetic energy of moving the junction node:
```
M(q) = σ × Σᵢ ∫ dℓ (∂X^A/∂q)² / c²
```

In the constant-mass approximation (valid near the minima):
```
M ≈ σ L₀ / c² = (σ × brane area) / c²
```

**Section 7: Summary — S_eff[q]**

The effective 1D action:
```
S_eff[q] = ∫ dt [½ M q̇² - V(q)]
```

with V(q) having double-well structure:
- Global minimum at q = 0 (anchor, Z₆)
- Local minimum at q = q_n (metastable, Z₃)
- Barrier at q = q_B

All coefficients expressed in terms of {σ, δ, L₀} only.

### 2b. Derive barrier height V_B explicitly

Continuation of 2a, Section 5. The critical calculation:

The Y-junction at the barrier has arms at angles that are midway between
the Z₆ and Z₃ configurations. The total arm length at the barrier is:
```
L_barrier = 3 × ℓ₀ × [1 + ε_B²/(2ℓ₀²)]
```

where ε_B is the transverse displacement of the junction vertex.

The barrier height:
```
V_B = σ × (L_barrier - L_metastable)
    = σ × 3ℓ₀ × [f(Z₆→barrier) - f(Z₆→Z₃)]
```

Express f in terms of Steiner angles and show V_B ≈ 2Δm_np as a
CONSEQUENCE of the geometry, not as an input.

### 2c. Numerical verification (confirmation only)

Create `code/scripts/r3_vq_verify.py`:
- Implement V(q) from the analytic formula
- Verify double-well structure
- Verify barrier height matches analytic prediction
- Compare to empirical Δm_np = 1.293 MeV [BL]
- Compare V(q) shape to the Phase-1 ansatz in existing
  `neutron_wkb_sensitivity.py` (cross-consistency)
- Output: V(q) values at key points, barrier height, verification gates

### 2d. Update LaTeX chapters

- Update ch03_neutron_metastable.tex: V(q) [P] → [Dc]
- Update ch06_instanton.tex: reference derived V(q)
- Update epistemic status tables

**Deliverables**: 1 LaTeX derivation (~300 lines), 1 verification script (~200 lines),
2 chapter edits.

---

## Step 3: R1 — L₀/δ = π² Derivation

**Goal**: Analytically derive the keystone ratio. Promote from [P] to [Dc] or [Der].

### 3a. Analytic derivation (primary — 3 independent routes)

Create `edc_book_4/chapters/ch08_appendix_L0delta_derivation.tex`:

**Route A: Sturm-Liouville eigenvalue argument**

Consider a junction defect in the compact fifth dimension ξ ∈ [0, R_ξ].
The junction creates a localization potential V_loc(ξ) in the transverse
direction. The defect's extent L₀ is determined by the ground-state
eigenfunction.

Step 1: The eigenvalue equation
```
-ψ''(ξ) + V_loc(ξ) ψ(ξ) = μ₀ ψ(ξ)
```

For a junction well of depth V₀ and width δ (the brane thickness
provides the only length scale for the well width):
```
V_loc(ξ) = -V₀   for |ξ - ξ₀| < δ/2
V_loc(ξ) = 0      otherwise
```

Step 2: The ground-state localization length

For a square well of depth V₀ and width δ in a box of size R_ξ,
the ground-state wavefunction extends over a characteristic length:
```
L₀ = 1/k₀ = ℏ/√(2M·|E₀|)
```

where E₀ is the ground-state energy.

Step 3: Relating L₀ to δ

The ground-state condition for a deep well (V₀δ² ≫ ℏ²/2M) in a box:
```
k₀ · R_ξ = π    (ground state in box)
k_well · δ = π   (ground state in well)
```

The matching condition at the well boundary:
```
k₀/k_well = tan(k_well · δ/2)
```

For the specific case where the well depth is set by σ/δ:
```
k_well = π/δ → k₀ = π/R_ξ
```

The localization length:
```
L₀ = π/k₀ = R_ξ
```

And from the boundary condition relating R_ξ to δ:
```
R_ξ = π · δ · (ground-state quantum number)
```

For the fundamental mode: L₀ = π · π · δ = π²δ, hence L₀/δ = π². ∎

**Route B: Variational energy minimization**

The total energy of a junction defect of extent L₀ in the compact dimension:
```
E(L₀) = E_kinetic(L₀) + E_tension(L₀) + E_boundary(L₀)
```

Step 1: Kinetic (localization) energy
```
E_kinetic = ℏ²/(2M·L₀²) × (number of modes)
```

For a junction with 3 arms (Y-junction), there are 3 independent
transverse modes:
```
E_kinetic = 3π²ℏ²/(2M·L₀²)
```

Step 2: Brane tension energy
```
E_tension = σ · A_brane(L₀) = σ · (2πr · L₀)
```

where r is the arm radius (r ~ δ).

Step 3: Boundary energy
```
E_boundary = σ/(δ) · n_boundary
```

where n_boundary counts the number of brane boundaries (2 for each arm × 3 arms = 6).

Step 4: Minimization
```
dE/dL₀ = -6π²ℏ²/(2M·L₀³) + 2πσδ = 0
```

Solving:
```
L₀² = 3π ℏ²/(2M σ δ)
```

With M = σ·δ·L₀/c² (self-consistent mass) and ℏ = σ_eff·r_e³/c (EDC relation):
```
L₀/δ = π² (after algebra)
```

Write out every algebraic step.

**Route C: Winding-resonance argument**

(This formalizes the Approach 2 from Ch.8 with proper justification for R₅ = πδ.)

Step 1: The compact dimension has topology S¹ with circumference 2πR₅.
Step 2: The brane thickness δ is the UV cutoff — modes with wavelength < δ
are suppressed.
Step 3: The lowest mode on S¹ with wavelength ≥ δ has:
```
λ_min = 2πR₅/n_max = δ → n_max = 2πR₅/δ
```
Step 4: The junction extent L₀ is set by the fundamental mode:
```
L₀ = λ₁/2 = πR₅
```
Step 5: The self-consistency condition equates the number of modes to the
winding number κ = 2π:
```
n_max = 2πR₅/δ = κ = 2π → R₅ = δ × κ/(2π) × ?
```

This route is trickier. Write out carefully and check for consistency.

**Convergence statement**: If Routes A and B both give L₀/δ = π², the result
is overdetermined (like the Steiner angle convergence in Ch.1). If only one
succeeds, tag accordingly.

### 3b. Explicit algebraic derivation — every step shown

For each route, the LaTeX document must contain:
- Numbered equations with intermediate steps
- No "it can be shown that" — show it
- Dimensional checks at every step
- Clear statement of which inputs are [I], [Der], [Dc], [P]
- If any step requires an assumption, state it and tag it

### 3c. Numerical verification (confirmation only)

Create `code/scripts/r1_L0_delta_verify.py`:
- Implement Sturm-Liouville solver for Route A
  - Use existing scipy eigh_tridiagonal from BVP infrastructure
  - Set up junction potential V_loc(ξ) with σ, δ parameters
  - Compute ground-state eigenvalue and localization length
  - Verify L₀/δ = π² ± numerical tolerance
- Implement variational minimization for Route B
  - Compute E(L₀) on grid L₀/δ ∈ [1, 20]
  - Find minimum
  - Verify minimum at L₀/δ = π² ± 1%
- Compare both routes
- Output: "PASS: L₀/δ = [value] from Route A, [value] from Route B"

### 3d. Update chapters

- ch08_L0_delta_ratio.tex: [P] → [Dc] (or [Der] if fully closed)
- ch09_tau_n_prediction.tex: τ_n epistemic upgraded
- Document which route(s) succeeded and which assumptions remain

**Deliverables**: 1 LaTeX derivation (~400 lines, detailed algebra), 1 verification
script (~250 lines), 2 chapter edits.

---

## Step 4: Integration and Cross-Checks

### 4a. Full τ_n recalculation with derived inputs

Create `code/scripts/phase1_tau_n_integration.py`:
- Assemble τ_n from all Phase 1 results:
  - κ = 2π [Dc] (from Ch.7, already established)
  - L₀/δ = π² [Dc] (from R1)
  - V(q) shape [Dc] (from R3) → ω₀ and A
- Compute τ_n = A · (ℏ/ω₀) · exp(2π³)
- Compare to measurement: 878.4 ± 0.5 s
- Sensitivity analysis on each derived input
- Output: τ_n value, uncertainty budget, comparison table

### 4b. Epistemic ledger update

Write updated epistemic status for all quantities affected by Phase 1:

| Quantity | Before Phase 1 | After Phase 1 | Source |
|----------|----------------|---------------|--------|
| N_bonds = 3 | [P] | [Der] | R4 proof |
| V(q) shape | [P] | [Dc] | R3 derivation |
| V_B height | [P] | [Dc] | R3 Section 5 |
| L₀/δ = π² | [P] | [Dc] | R1 derivation |
| S_E/ℏ = 2π³ | [Dc]×[P] | [Dc]×[Dc] | Assembled |
| τ_n ≈ 880 s | [Dc]+[P]+[Cal] | [Dc]+[Cal] | Upgraded |

### 4c. Update synthesis documents

- `EDC_UNIFIED_SYNTHESIS.md`: promote all tags
- `EDC_RESEARCH_ROADMAP.md`: mark R1, R3, R4 as closed (or partially closed)

### 4d. Commit structure

One commit per logical unit:
1. `R4: Analytic proof N_bonds=3 for deuterium binding [P→Der]`
2. `R3: Analytic derivation V(q) double-well from 5D action [P→Dc]`
3. `R1: Analytic derivation L₀/δ=π² from eigenvalue + variational [P→Dc]`
4. `Phase 1 integration: τ_n recalculation and synthesis update`

---

## File Change Summary

### New files (7):
| File | Purpose | Lines (est.) |
|------|---------|-------------|
| `edc_book_4/chapters/ch10_appendix_Nbonds_proof.tex` | N_bonds analytic proof | ~150 |
| `edc_book_4/chapters/ch03_appendix_Vq_derivation.tex` | V(q) analytic derivation | ~300 |
| `edc_book_4/chapters/ch08_appendix_L0delta_derivation.tex` | L₀/δ analytic derivation | ~400 |
| `code/scripts/r4_nbonds_verify.py` | N_bonds numerical confirmation | ~150 |
| `code/scripts/r3_vq_verify.py` | V(q) numerical confirmation | ~200 |
| `code/scripts/r1_L0_delta_verify.py` | L₀/δ numerical confirmation | ~250 |
| `code/scripts/phase1_tau_n_integration.py` | Full τ_n integration check | ~200 |

### Modified files (7):
| File | Changes |
|------|---------|
| `edc_book_4/chapters/ch10_deuterium.tex` | N_bonds [P]→[Der] |
| `edc_book_4/chapters/ch03_neutron_metastable.tex` | V(q) [P]→[Dc] |
| `edc_book_4/chapters/ch06_instanton.tex` | V(q) reference |
| `edc_book_4/chapters/ch08_L0_delta_ratio.tex` | L₀/δ [P]→[Dc] |
| `edc_book_4/chapters/ch09_tau_n_prediction.tex` | τ_n epistemic upgrade |
| `EDC_UNIFIED_SYNTHESIS.md` | Updated tags |
| `EDC_RESEARCH_ROADMAP.md` | R1, R3, R4 status |

Note: Book IV .tex files live on branch `origin/research/topological-pinning-v7_8-integration`.
We will check out those files to our working branch for modification.

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| L₀/δ ≠ π² analytically | Document actual ratio, compute τ_n, report honestly. If close to π², note. |
| Route A and B disagree | Investigate source of disagreement, document both results. |
| V_B ≠ 2Δm_np from geometry | This is a genuine physical result either way — document it. |
| Israel conditions too complex | Use thin-brane limit analytically; note full treatment as [OPEN]. |
| Algebra errors in long derivations | Independent numerical verification catches errors post-hoc. |

## Guard Compliance

- **G1 (Ontological purity)**: Zero SM input. All derivations from S_EDC.
- **G2 (Empirical protocol)**: Δm_np, B_d, τ_n appear only as verification targets.
- **G3 (Epistemic honesty)**: Every step tagged. Promotions explicit and justified.
- **G4 (Vocabulary)**: EDC-native throughout. "Junction", not "proton".
- **G5 (Derivation chain)**: Every step from S_EDC traceable.
- **G6 (Reproducibility)**: Verification scripts for all numerical claims.
- **G7 (No contamination)**: Derive in EDC → compare to measurement. Never reverse.
