# Put C: S_5D → S_eff[q] Reduction Corridor

**Date:** 2026-01-27
**Status:** [P]+[Dc] — Formal structure established; actual M(q), V(q) computation OPEN
**Purpose:** Establish the mathematical corridor from 5D action to effective 1D collective coordinate dynamics

---

## 1. Executive Summary

**What Put C is:**
A formal derivation pathway showing how the effective 1D action
```
S_eff[q] = ∫ dt ( ½ M(q) q̇² − V(q) )
```
emerges from the full 5D action (bulk + brane + boundary terms).

**What Put C does NOT yet do:**
- Compute explicit functional forms of M(q) and V(q)
- Derive V_B numerically from first principles
- Close the "unit-per-leg = Δm_np" gap

**Output object:** S_eff[q] with M(q), V(q) as derived functionals of the 5D geometry.

**Why this matters:**
When completed, Put C upgrades the current status:
- V(q): [P] → [Der]
- M(q): [P] → [Der]
- V_B: [Cal] → [Der] (via V_B = V(q_B) − V(q_n))
- τ_n: [Cal] → [Der] (via WKB with derived barrier)

Currently, the neutron lifetime calculation uses phenomenological M(q), V(q).
Put C provides the rigorous 5D foundation.

---

## 2. The 5D Action in EDC

### 2.1 Modular Decomposition [Def]

The total 5D action consists of:

```
S_total = S_bulk + S_brane + S_GHY + S_junction
```

where:

**S_bulk — Einstein-Hilbert + matter in 5D:**
```
S_bulk = (1/2κ₅²) ∫_M d⁵x √(-g) (R − 2Λ₅) + S_bulk,matter
```
[Def] Standard 5D gravity action. κ₅² = 8πG₅ is the 5D gravitational coupling.

**S_brane — Brane tension term:**
```
S_brane = −σ ∫_Σ d⁴x √(-h)
```
[Def] where σ is the membrane tension and h_μν is the induced metric on brane Σ.
Current repo value: σ ≈ 8.82 MeV/fm² [Dc] (see sections/ch15_opr01_sigma_anchor_derivation.tex).

**S_GHY — Gibbons-Hawking-York boundary term:**
```
S_GHY = (1/κ₅²) ∫_∂M d⁴x √(-h) K
```
[Def] where K = h^μν K_μν is the trace of the extrinsic curvature.
Required for well-defined variational principle with Dirichlet BC.

**S_junction — Junction/matching terms:**
```
S_junction = junction energy functional at Y-junction node
```
[P] Form depends on the specific junction model (Nambu-Goto strings, etc.).
See aside_neutron_dual_route/STATUS_MAP.md for current status.

### 2.2 Junction Sector (Y-Junction) [P]+[Dc]

For the nucleon (proton/neutron), the relevant configuration is a **Y-junction**:
three flux tubes (edges) meeting at a central node.

**Edge contribution (Nambu-Goto):**
```
S_edge,i = −τ ∫ d²ζ √(-γ_i)
```
[Der] where τ is string tension and γ_i is the induced worldsheet metric on edge i.
In static limit: E_edge,i = τ L_i (see sections/04b_proton_anchor.tex, Lemma 2).

**Node contribution:**
```
S_node = ∫ dt E_node(configuration)
```
[P] The node energy depends on junction geometry (angles, curvature at vertex).

**Total junction sector:**
```
S_junc = Σᵢ₌₁³ S_edge,i + S_node
```
[Dc] Additivity follows from locality; equal tensions from Z₃ symmetry.

---

## 3. Geometric Setup and Ansatz

### 3.1 5D Metric Ansatz [Def]

We use a warped product ansatz:
```
ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ²
```
[Def] where:
- ξ ∈ [0, δ] is the fifth (compact) coordinate
- A(ξ) is the warp factor
- η_μν is the 4D Minkowski metric (or dS/AdS as appropriate)
- δ is the brane thickness

**Repo reference:** The frozen regime uses A(ξ) ≈ const over the brane layer
(see sections/02_frozen_regime_foundations.tex).

### 3.2 Brane Embedding [Def]

The brane is located at a hypersurface Σ defined by:
```
ξ = ξ_brane(x^μ)
```

For a collective coordinate description, we parametrize:
```
ξ_brane(x^μ, t) = ξ₀ + q(t) · f(x^μ)
```
[Def] where:
- ξ₀ is the equilibrium position
- q(t) is the slow collective coordinate (junction displacement)
- f(x^μ) is a spatial profile (typically f = 1 for uniform displacement)

### 3.3 Y-Junction Embedding [Dc]

The Y-junction consists of three worldsheets Σ₁, Σ₂, Σ₃ meeting at a 1D curve (the junction line).

**Parametrization:**
- Each edge i has embedding X^A_i(σ, τ) where σ ∈ [0, L_i] and τ is worldsheet time
- At σ = 0: all three edges meet (junction condition)
- At σ = L_i: edge i terminates at brane boundary

**Junction coordinate q(t):**
```
q(t) = ξ_node(t) − ξ₀
```
[Def] The displacement of the junction node along the ξ-direction.

For proton: q = 0 (Steiner equilibrium)
For neutron: q = q_n > 0 (metastable displaced position)

---

## 4. Formal Reduction Steps

### Step C1: Choose Ansatz Class [Def]+[I]

**Input:** 5D metric (warped), brane embedding, Y-junction embedding
**Output:** Configuration space parametrized by q(t) and "fast" modes {φ_α}

```
Configuration = { g_AB(q, φ_α), X_i(q, φ_α) }
```

**Identification [I]:**
- q = junction node ξ-displacement (slow collective coordinate)
- {φ_α} = transverse fluctuations, brane shape modes, etc. (fast modes)

**Status:** [Def]+[I] — ansatz choice, not derived from first principles.

### Step C2: Insert Ansatz into S_total [Dc]

**Input:** S_total with ansatz substituted
**Output:** Lagrangian as functional of q, q̇, {φ_α}, {φ̇_α}

```
S_total[q, φ_α] = ∫ dt L(q, q̇, φ_α, φ̇_α)
```

**Procedure:**
1. Substitute metric ansatz into S_bulk → obtain bulk contribution
2. Evaluate induced metric h_μν on brane → obtain S_brane contribution
3. Compute extrinsic curvature K_μν → obtain S_GHY contribution
4. Evaluate junction worldsheet areas → obtain S_junc contribution

**Explicit form (schematic):**
```
L = L_bulk(q, φ) + L_brane(q, q̇, φ) + L_GHY(q, φ) + L_junc(q, q̇, φ)
```

The q̇ dependence comes from:
- Time derivatives of brane position → kinetic energy
- Junction node velocity → junction kinetic term

**Status:** [Dc] — follows from substitution; explicit integrals are OPEN.

### Step C3: Integrate Out Fast Modes [Dc]

**Input:** L(q, q̇, φ_α, φ̇_α)
**Output:** L_eff(q, q̇)

**Procedure (Born-Oppenheimer / Adiabatic Approximation):**

For each fixed q, minimize over fast modes:
```
φ_α*(q) = argmin_φ L(q, 0, φ, 0)
```

Then:
```
L_eff(q, q̇) = L(q, q̇, φ*(q), φ̇*(q))
```

where φ̇*(q) accounts for adiabatic following.

**Physical interpretation:**
Fast modes (membrane shape, transverse oscillations) relax instantaneously
compared to slow collective motion q(t).

**Status:** [Dc] — standard adiabatic reduction; validity requires timescale separation.

### Step C4: Canonical Form [Dc]

**Input:** L_eff(q, q̇)
**Output:** M(q), V(q)

The effective Lagrangian takes the form:
```
L_eff(q, q̇) = ½ M(q) q̇² − V(q)
```

**Definitions:**

**Effective mass (kinetic coefficient):**
```
M(q) := ∂²L_eff / ∂q̇²
```
[Dc] Arises from junction inertia + brane kinetic energy + bulk contributions.

**Effective potential:**
```
V(q) := −L_eff(q, q̇=0)
```
[Dc] Static energy of configuration with junction at position q.

**Where σ enters:**
The membrane tension σ contributes to V(q) via:
```
V(q) ⊃ σ · A_brane(q)
```
where A_brane(q) is the effective area of brane deformation.

**Where junction geometry enters:**
```
V(q) ⊃ τ Σᵢ Lᵢ(q) + E_node(q)
```
String tension × total length + node energy.

**Status:** [Dc] — form follows from Lagrangian structure; coefficients are OPEN.

---

## 5. Bridge to V_B

### 5.1 Barrier Definition [Def]

```
V_B := V(q_B) − V(q_n)
```

where:
- q_n = neutron metastable minimum: V'(q_n) = 0, V''(q_n) > 0
- q_B = barrier saddle point: V'(q_B) = 0, V''(q_B) < 0

### 5.2 Current Status

**From Z₃ analysis (see V_B_FROM_Z3_BARRIER_CONJECTURE.md):**
```
V_B = 2 × Δm_np ≈ 2.59 MeV   [Dc]
```

This is conditional on:
1. Barrier is Z₃-symmetric (minimal saddle) [Dc]
2. "One unit per leg = Δm_np" [Dc] — OPEN

### 5.3 Put C Target

When Put C is completed:
1. V(q) is explicitly computed from S_5D
2. q_n and q_B are found from V'(q) = 0
3. V_B = V(q_B) − V(q_n) becomes [Der]

The Z₃ barrier picture provides a constraint/check:
if Put C gives V_B ≈ 2Δm_np, the Z₃ interpretation is validated.

---

## 6. OPEN Steps for Put C Completion

| Step | What is needed | Current status |
|------|----------------|----------------|
| C1 | Explicit bulk Lagrangian choice | [I] — ansatz |
| C1 | Junction worldsheet embedding | [P] — assumed |
| C2 | Evaluate S_bulk integral | OPEN |
| C2 | Compute induced metric h_μν(q) | OPEN |
| C2 | Compute extrinsic curvature K(q) | OPEN |
| C2 | Evaluate S_junc(q) for Y-junction | OPEN |
| C3 | Identify fast modes | [P] — assumed transverse |
| C3 | Solve fast-mode minimization | OPEN |
| C4 | Extract M(q) functional form | OPEN |
| C4 | Extract V(q) functional form | OPEN |
| C4 | Find q_n, q_B from V'(q)=0 | OPEN |

### 6.1 Specific Requirements

**For S_bulk:**
- Specify Λ₅ (cosmological constant) — currently [P]
- Any bulk matter fields — currently minimal (none)

**For S_brane:**
- σ value: 8.82 MeV/fm² [Dc] (from E_σ = m_e c²/α hypothesis)
- Brane thickness δ — currently [P] or [Cal]

**For S_GHY:**
- Where is ∂M located? At ξ = 0, ξ = δ, or both?
- This determines which boundary terms contribute

**For S_junction:**
- Nambu-Goto for edges: τ = σ or separate string tension?
- Node energy E_node: functional form? [P]

**Optional: Helfrich term**
```
S_Helfrich = κ_b ∫ d⁴x √(-h) (K − K₀)²
```
Bending rigidity term. May be needed if minimal action doesn't produce barrier.
Status: [P] — optional extension.

---

## 7. Guardrail Statement

**No overclaim policy:**

This document establishes the **formal reduction corridor** — the mathematical
pathway from 5D to 1D. It does **not** yet compute M(q), V(q) explicitly.

The current neutron lifetime calculations use:
- V(q): [P] phenomenological shape
- M(q): [P] assumed constant or simple q-dependence
- V_B: [Cal] ≈ 2.6 MeV from τ_n fit

Put C is the next true 5D step. Until Steps C2-C4 are executed with explicit
integrals, the effective model remains [P]+[Cal].

**Consistency with 5D Forensic Audit:**
The STATUS_MAP in aside_neutron_dual_route confirms:
> "the full 5D derivation (derive S_eff[q], M(q), V(q), V_B from 5D action)
> is **not yet implemented**."

Put C addresses this gap systematically.

---

## 8. Model-to-Geometry Dictionary

| Model quantity | Geometric definition | Status |
|----------------|----------------------|--------|
| q | Junction node ξ-displacement from equilibrium | [Def] |
| M(q) | ∂²L_eff/∂q̇² (kinetic coefficient) | [Dc] form, OPEN value |
| V(q) | −L_eff(q, 0) (static energy) | [Dc] form, OPEN value |
| q_n | Neutron metastable position: V'(q_n)=0, V''>0 | [I] identified, OPEN derived |
| q_B | Barrier saddle: V'(q_B)=0, V''<0 | [Dc] assumed, OPEN derived |
| V_B | V(q_B) − V(q_n) | [Cal] now, [Der] target |
| σ | Membrane tension (brane Lagrangian coefficient) | [Dc] 8.82 MeV/fm² |
| τ | String/edge tension | [P] = σ or independent |
| δ | Brane thickness / ξ extent | [P] or [Cal] |

**Degrees integrated out:**
- Transverse brane fluctuations (shape modes)
- High-frequency junction oscillations
- Bulk field modes (if any)

**Assumptions for reduction:**
- Adiabatic approximation (timescale separation)
- q is the dominant slow coordinate
- Fast modes relax to minimum for each q

---

## 9. Status Map

| Quantity | Current status | Put C target | What is needed |
|----------|----------------|--------------|----------------|
| S_total | [Def] | — | Already defined |
| M(q) | [P] | [Der] | Execute C2-C4 |
| V(q) | [P] | [Der] | Execute C2-C4 |
| V_B | [Cal] 2.6 MeV | [Der] | V(q) → find extrema |
| Γ₀ | [Cal] | [Der] | Mode spectrum at q_n |
| τ_n | [Cal] 879 s | [Der] | V_B + Γ₀ via WKB |

---

## 10. References

**Internal repo:**
- sections/04b_proton_anchor.tex — Nambu-Goto, Steiner theorem
- sections/ch15_opr01_sigma_anchor_derivation.tex — σ value
- aside_neutron_dual_route/STATUS_MAP.md — current M(q), V(q) status
- sections/ch10_electroweak_bridge.tex — Israel junction discussion
- sections/ch11_opr20_factor8_forensic.tex — Israel matching factors

**Linked derivation docs:**
- V_B_FROM_Z3_BARRIER_CONJECTURE.md — Z₃ barrier picture
- Z3_SYMMETRY_ANALYSIS_NEUTRON.md — Z₃ symmetry analysis

---

## 11. Executed Variants (Appendix)

**Execution date:** 2026-01-27
**Full report:** `derivations/PUTC_EXECUTION_REPORT.md`
**Code:** `derivations/code/putC_compute_MV.py`

### Summary of Implemented Models

| Variant | Description | Result | Status |
|---------|-------------|--------|--------|
| 1 | Flat bulk, Nambu-Goto only | NO metastability | [Dc] |
| 2 | Warped (RS-like), Nambu-Goto + brane | NO metastability | [Dc/P] |
| 3 | Warped + phenomenological node well | Metastability FOUND | [P/Cal] |

### Best Match for Variant 3

| Quantity | Value | Target | Error |
|----------|-------|--------|-------|
| q_B (barrier) | 1.22 fm | — | — |
| q_n (neutron) | 1.86 fm | — | — |
| V_B | 2.82 MeV | 2.6 MeV [Cal] | +8.3% |
| V_B | 2.82 MeV | 2.587 MeV [Dc] | +8.8% |

### Critical Finding

**V_B = 2 × Δm_np does NOT emerge from minimal 5D models.**

The Z₃ barrier conjecture [Dc] remains unvalidated:
- Flat bulk: V(q) monotonically increasing
- Warped bulk alone: insufficient for barrier structure
- Warped + node well: CAN produce barrier, but V_B depends on fitted parameters

### What Remains OPEN

1. **Node energy origin:** V_node(q) is phenomenological [P], not derived from action
2. **Parameter fixing:** (V_{node,0}, q*, width) require independent physics
3. **V_B = 2×Δm_np:** Not naturally produced — needs mechanism
4. **M(q) derivation:** Current estimate is simplified [Dc/P]

### Output Artifacts

- `derivations/artifacts/putC_results.json` — full numerical results
- `derivations/artifacts/putC_results.csv` — summary table
- `derivations/figures/putC_Vq_*.png` — potential plots
- `derivations/figures/putC_Mq_*.png` — effective mass plots

---

## 12. Version History

- 2026-01-27: Initial skeleton created (Put C corridor structure)
- 2026-01-27: Executed Variants 1-3, added execution report and artifacts
