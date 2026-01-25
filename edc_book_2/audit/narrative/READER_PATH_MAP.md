# READER PATH MAP — Book 2 Narrative Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-24
**Status**: Phase N1 COMPLETE

---

## Overview

This document maps the **reader's journey** through Book 2 (Weak Sector), identifying:
- Key concepts introduced per chapter
- Core equations with labels
- Cross-chapter dependencies
- Epistemic flow (what depends on what)

Target reader: **Graduate physicist** familiar with QFT and SM basics.

---

## CH01: The Weak Interface

### Key Concepts (10)
1. **EDC Epistemic Standard** — Evidence labels: [BL], [Der], [Dc], [I], [Cal], [P], [M]
2. **Unified weak-sector pipeline** — Absorption → Dissipation → Release
3. **Thick brane** — Finite-thickness layer with bulk-facing and observer-facing sides
4. **Proton-Anchor Stability Principle** — Proton as topological minimum
5. **Frozen projection operator** — P_frozen = P_energy ∘ P_mode ∘ P_chir
6. **Particle ontology** — Five categories (junction, brane-dominant, defect, edge, composite)
7. **Generative Closure Principle** — {p, e±, ν, ν̄} as closed substrate
8. **Regime parameter Ξ(t)** — Ξ ≡ Π_pump/Π_release
9. **Collective coordinate q** — Junction departure from Steiner
10. **Viability Filter Conditions** — Proton stability, ledger closure, leakage suppression

### Key Equations
- `\label{eq:brane_energy_balance}` — dE_brane/dt = Π_pump - Π_release - Π_other
- `\label{eq:pump_power_def}` — Π_pump(t) ≡ -q̇(t)·∂_q V(q(t))
- `\label{eq:Xi_def}` — Ξ(t) ≡ Π_pump(t)/Π_release(t)
- `\label{eq:Pfrozen_def}` — Frozen projection operator decomposition
- `\label{eq:ledger_closure}` — ΔE_available = Σ K_i + E_other
- `\label{eq:n_q_def}` — Collective coordinate for neutron
- `\label{eq:n_damped_motion}` — M q̈ + Γ q̇ + ∂_q V(q) = 0
- `\label{eq:n_frozen_projection}` — φ(y=+δ/2,t) → {e⁻, e⁺, νₑ, ν̄ₑ, γ,...}_3D

### Dependencies
- ← CH02/CH03: Z₆ proton stability proof
- → CH03: G_F structural derivation path
- → CH09: V-A structure connection

---

## CH02: Frozen Regime Foundations

### Key Concepts (10)
1. **Frozen vs Fluid regimes** — Sharp step-function vs smooth GL profiles
2. **5D bulk manifold M⁵** — Physical reality as 5D with Plenum energy fluid
3. **3D membrane Σ³** — Observable universe embedded in M⁵
4. **Membrane tension σ** — Surface tension [J/m²] resisting deformation
5. **Particles as topological defects** — Stable localized bulk energy regions
6. **Compact fifth dimension ξ** — Topology ξ ≅ S¹ with R_ξ ≪ 1 mm
7. **GL coherence length ξ_GL** — Smooth profile transition scale
8. **Isoperimetric theorem** — Electron: V_excl/a³ = 4π/3
9. **Steiner equilibrium** — Proton: Area(S³)³ = (2π²)³
10. **Ice Wall Analogy** — Plenum=water, membrane=ice wall, particles=frozen droplets

### Key Equations
- m_p/m_e = 6π⁵ = 1836.118... (0.0018% error)
- α = (4π + 5/6)/6π⁵ = 1/137.027... (0.0067% error)
- `\label{eq:ch2_gl_profile}` — f(r) = tanh(r/√2 ξ_GL)
- `\label{eq:ch2_frozen_profile}` — f(r) = Θ(r-a)

### Dependencies
- → CH03: Frozen regime enables Z₆ parameter-free geometry
- → CH04+: Topological protection explains particle stability
- IF-THEN: IF Frozen THEN Z₆ proofs THEN weak-sector derivations

---

## CH03: The Z₆ Program

### Key Concepts (10)
1. **Z₆ symmetry hypothesis** — Hexagonal lattice on thick brane
2. **Z₆ = Z₂ × Z₃ factorization** — Z₃→color, Z₂→electroweak
3. **Steiner problem** — Three equal tensions → 120° angles
4. **Equal tensions from Z₆** — Discrete symmetry guarantees τ₁=τ₂=τ₃
5. **Hexagonal packing** — Kepler-Hales: densest 2D packing
6. **Flux tube interactions** — Short-range repulsion + long-range confinement
7. **Proton as Y-junction** — Three flux tubes at 120°
8. **Neutron as dislocation** — Lattice defect in hexagonal structure
9. **Topological energy minimum** — Proton configuration space minimum
10. **Excluded volume** — Core prevents flux tube overlap

### Key Equations
- `\label{eq:steiner_equilibrium}` — n̂₁ + n̂₂ + n̂₃ = 0
- Equal tension: τ₁ n̂₁ + τ₂ n̂₂ + τ₃ n̂₃ = 0
- Flux tube potential: V(r) = V_rep(r) + V_att(r)
- Equilibrium spacing: r₀ ~ ℏc/σ^(1/2) ~ 1 fm

### Dependencies
- ← CH02: Frozen regime justification
- → CH01: Proton Z₃ fixed point proof [P]→[Dc]
- → CH04: Z₆ factorization enables EW parameters

---

## CH04: Electroweak Parameters from Geometry

### Key Concepts (10)
1. **Coupling normalization map** — g'²/g² = |Z₂|/|Z₆| [P]
2. **Weinberg angle from geometry** — sin²θ_W = 1/4 from Z₆
3. **Electroweak unification** — e = g sinθ_W = g' cosθ_W
4. **RG running to M_Z** — Bridges lattice (~200 MeV) to Z-pole (91 GeV)
5. **Derived-conditional status** — IF coupling map THEN sin²θ_W
6. **Subgroup counting → coupling ratios** — Symmetry volume = coupling
7. **Photon/Z orthogonal mixing** — γ and Z as rotated basis
8. **Membrane tension origin of g²** — σ r_e³/ℏc = 0.0297
9. **Consistency check vs prediction** — G_F exact from EW relations
10. **What NOT derived** — 5D gauge action, Higgs sector, why Z₆

### Key Equations
- `\label{thm:ch3_g2}` — g² = 4πα/sin²θ_W = 0.4246 (1.1%)
- `\label{cor:ch3_weinberg}` — sin²θ_W = |Z₂|/(|Z₂|+|Z₆|) = 1/4
- g'²/g² = |Z₂|/|Z₆| = 2/6 = 1/3
- sin²θ_W = g'²/(g² + g'²) = 1/4
- M_W = gv/2 = 80.2 GeV (0.2%)
- G_F = g²/(4√2 M_W²) = 1.166×10⁻⁵ GeV⁻² (exact)

### Dependencies
- ← CH03: Z₆ = Z₂ × Z₃ factorization
- ← CH02: σ as origin of coupling
- → Weak sector: EW parameters for decay rates
- → OPR-17: Derive coupling map from 5D action

---

## CH05: Candidate Lepton Mass Relations

### Key Concepts (7)
1. **Candidate electron mass formula** — m_e = π√(ασΔℏc)
2. **Candidate muon/electron ratio** — m_μ/m_e = (3/2)/α
3. **Koide relation** — Q = 2/3
4. **Koide Z₆ identification** — Q = 2/3 ↔ |Z₂|/|Z₃|
5. **1/α enhancement problem** — Factor ~137, not typical α corrections
6. **Thomson limit α** — α = 1/137.036
7. **Attempt 3B framework** — α = (4π+5/6)/(6π⁵)

### Key Equations
- `\label{eq:electron_candidate}` — Candidate electron mass formula
- `\label{eq:muon_ratio_candidate}` — m_μ/m_e ratio
- `\label{eq:koide_ch4}` — Koide relation definition
- `\label{eq:koide_z6}` — Koide Z₆ identification

### Dependencies
- ← CH02: Z₆ symmetry [Dc]
- → CH06: Three neutrino generations for PMNS
- → CH07: Three quark generations for CKM

---

## CH06: Why Exactly Three Generations?

### Key Concepts (5)
1. **Generation count problem** — SM takes N_gen=3; EDC seeks derivation
2. **Z₆ = Z₂ × Z₃** — Z₂=matter/antimatter, Z₃=generation index
3. **Three-channel toy model** — V(ξ) with minima at 0, 2π/3, 4π/3
4. **Mode indices** — n=0 (e), n=1 (μ), n=2 (τ)
5. **Overlap suppression** — Off-diagonal mixing suppressed

### Key Equations
- `\label{eq:ch5_z6_factor}` — Z₆ = Z₂ × Z₃ ⟹ |Z₃| = 3
- `\label{eq:ch5_lifetime}` — τ_n ∝ exp(S_n/ℏ)
- `\label{eq:ch5_prediction}` — N_gen = 3 (falsifiability)

### Dependencies
- ← CH02: Hexagonal packing → Z₆ [Dc]
- ← CH04: Mode indices n=0,1,2 [I]
- → CH06/CH07: PMNS/CKM structure

---

## CH07: Neutrinos as Edge Modes

### Key Concepts (7)
1. **Edge mode ontology** — ν at bulk-brane interface
2. **Mass suppression mechanism** — m_eff from overlap suppression
3. **Exponential mass ratio** — m_ν/m_e ~ exp(-Δξ/κ⁻¹)
4. **Three neutrino flavors** — (ν_e, ν_μ, ν_τ) ↔ Z₃ elements
5. **PMNS from wavefunction overlap** — U_PMNS ∝ ∫ψ*_α ψ_i
6. **Z₃ DFT baseline** — |U_αi|² = 1/3 → FALSIFIED
7. **Left-handed selection** — V-A from boundary conditions

### Key Equations
- `\label{eq:ch6_edge_profile}` — |ψ_ν(ξ)|² ∝ exp(-2κ|ξ-ξ_interface|)
- `\label{eq:ch6_mass_ratio}` — m_ν/m_e ~ exp(-Δξ/κ⁻¹)
- `\label{eq:ch6_pmns}` — PMNS matrix
- `\label{eq:ch6_pmns_overlap}` — PMNS from overlaps

### Dependencies
- ← CH05: Z₃ structure, three generations
- ← CH09: Chirality selection [Dc]
- → CH08: G_F overlap formalism

---

## CH08: CKM Matrix and CP Violation

### Key Concepts (9)
1. **CKM hierarchy** — |V_us|~λ, |V_cb|~λ², |V_ub|~λ³
2. **Z₃ DFT baseline for CKM** — STRONGLY FALSIFIED (×140 off)
3. **Overlap model ansatz** — f_i(ξ) with CKM from overlap
4. **Wolfenstein from single parameter** — Δξ/(2κ) ≈ 1.49
5. **Non-uniform generation spacing** — Δξ₁₂ ≠ Δξ₂₃
6. **V_ub prefactor discrepancy** — Factor 2.5 = 1/|ρ̄-iη̄|
7. **Quark vs lepton localization** — κ_q/κ_ℓ ≈ 0.4
8. **Jarlskog invariant** — J ≈ 3.0×10⁻⁵
9. **Phase cancellation theorem** — Pure Z₃ gives J=0

### Key Equations
- `\label{eq:ch7_ckm_def}` — CKM definition
- `\label{eq:ch7_wolfenstein}` — Wolfenstein parametrization
- `\label{eq:ch7_overlap_def}` — O_ij = ∫f_i f_j dξ
- `\label{eq:ch7_calibration}` — Δξ/(2κ) = -ln λ
- `\label{eq:ch7_jarlskog}` — Jarlskog invariant

### Dependencies
- ← CH05: |Z₃|=3 generation identification
- ← Localized profile ansatz [P]
- → CH08: G_F overlap structure
- → OPR-09–12: Flavor sector open problems

---

## CH09: V-A Structure from 5D Chiral Localization

### Key Concepts (10)
1. **5D Dirac equation** — m(ξ) position-dependent mass
2. **Chiral projectors** — P_L, P_R split chiralities
3. **Domain wall localization** — Jackiw-Rebbi-Kaplan mechanism
4. **Plenum inflow direction** — J^z > 0 determines mass sign
5. **Mass-from-stress coupling** — m(ξ) ~ κ T^zz
6. **Mode profiles f_L, f_R** — Chiral mode distribution in ξ
7. **Half-line domain** — ξ ∈ [0,∞)
8. **Chirality asymmetry ratio** — R_LR quantifies RH suppression
9. **Barrier parameter μ** — Cumulative mass barrier measure
10. **Brane-localized gauge fields** — SU(2)_L at ξ=0

### Key Equations
- `\label{eq:ch9_5d_dirac}` — (iγ^μ∂_μ + iγ^5∂_ξ - m(ξ))Ψ = 0
- `\label{eq:ch9_projectors}` — P_L = (1-γ^5)/2
- `\label{eq:ch9_fL_sol}`, `\label{eq:ch9_fR_sol}` — Mode solutions
- `\label{eq:ch9_inflow}` — J^z > 0
- `\label{eq:ch9_mass_profile}` — m(ξ) = m_0(1 - e^(-z/λ))
- `\label{eq:va:RLR_def}` — R_LR ≡ |f_R(0)|²/|f_L(0)|²
- `\label{eq:ch9_va_derived}` — V-A Lagrangian

### Dependencies
- ← Framework v2.0 Remark 4.5: Bulk-brane conservation
- → CH11: G_F derivation
- → CH14: BVP chirality criterion
- → OPR-17: Gauge ontology

---

## CH10: Electroweak Bridge

### Key Concepts (10)
1. **Brane thickness δ** — ~r_e ~ 1 fm
2. **Israel junction conditions** — Metric discontinuity → stress-energy
3. **Robin boundary condition** — f' + αf = 0
4. **Robin parameter α** — ~ℓ/δ
5. **Eigenvalue x₁** — Determines m_φ = x₁/ℓ
6. **Electroweak scale R_ξ** — ≈ 2.2×10⁻³ fm
7. **δ = R_ξ identification** — Postulated [P]
8. **Overlap integral I₄** — ∫|f_L|⁴ dξ
9. **Mediator candidates** — KK mode, brane scalar, A₅
10. **Orbifold parity Z₂** — Even/odd fields, BC type

### Key Equations
- `\label{eq:ch10_robin_interpolation}` — k cot(kL) = -α

### Dependencies
- ← CH03: sin²θ_W = 1/4
- ← CH09: Chirality selection
- → CH11: BC form + α value
- → CH14: Physical inputs for BVP

---

## CH11: The Fermi Constant from Geometry

### Key Concepts (10)
1. **Fermi constant G_F** — Effective weak coupling strength
2. **Mediator field φ** — Brane-layer localized, mass gap m_φ
3. **5D coupling g₅** — Bulk-brane interaction
4. **Effective contact interaction** — Low-energy 4D four-fermion
5. **Overlap operator** — Wavefunction overlap + BC effects
6. **Effective coupling g_eff** — g₅ × O_overlap × O_BC
7. **Mode overlap I₄** — ∫|f_L(ξ)|⁴ dξ
8. **Higgs VEV v** — 246.2 GeV (circularity caveat)
9. **sin²θ_W = 1/4** — Bare from Z₆
10. **Chiral suppression** — Exponential RH suppression

### Key Equations
- `\label{eq:ch11_GF_value}` — G_F = 1.1663787×10⁻⁵ GeV⁻² [BL]
- `\label{eq:ch11_GF_SM}` — G_F = g²/(4√2 M_W²)
- `\label{eq:ch11_GEDC}` — G_EDC ~ g_eff²/m_φ²
- `\label{eq:ch11_overlap}` — I₄ mode overlap
- `\label{eq:ch11_chiral_suppression}` — RH/LH ~ e^(-m_0 λ)

### Dependencies
- ← CH03: sin²θ_W [Der]
- ← CH09: V-A chirality filter [Dc]
- ← CH10: Electroweak unification
- → Paper 3: Neutron lifetime
- → OPR-19–22: G_F first-principles

---

## CH12: Epistemic Landscape and Open Problems

### Key Concepts (8)
1. **Epistemic tags** — [BL/P/Dc/(open)]
2. **Q-gates** — Kinematic thresholds for decay
3. **OPR system** — Open Problems Register
4. **Framework 2.0 language** — 5D cause → 3D shadow
5. **Baseline facts [BL]** — 3D shadows to reproduce
6. **Generation threshold λ_th** — Essential spectrum onset
7. **Admissible BC family B** — Allowed Robin parameters
8. **OPR closure plan** — P1-A/B/C + P2/P3

### Dependencies
- Meta-chapter: references all prior chapters
- → OPR-19–22: G_F chain

---

## CH13: G_F Chain Closure Attempts

### Key Concepts (8)
1. **Closure spine** — G_F = (g₅² ℓ² I₄)/x₁²
2. **No-smuggling guardrails** — Forbidden vs allowed inputs
3. **Attack-surface map** — Circularity defense
4. **Canonical g₅ normalization** — g₄ = g₅
5. **KK eigenvalue problem** — m_φ = x₁/ℓ
6. **Factor-by-factor status** — Each G_F component
7. **Electroweak consistency** — Validation ≠ derivation
8. **Circularity firewall** — Where SM-help enters

### Key Equations
- `\label{eq:ch11_closure_spine}` — G_F = (g₅² ℓ² I₄)/x₁²
- `\label{eq:ch11_g4_g5_relation}` — g₄² = g₅²
- `\label{eq:ch11_mphi_scale}` — m_φ = x₁/ℓ
- `\label{eq:ch11_kk_eigenvalue}` — KK eigenvalue equation

### Dependencies
- ← CH09: SU(2)_L embedding
- ← CH12: I₄ definition
- → OPR-19/20/21/22

---

## CH14: BVP Work Package

### Key Concepts (11)
1. **BVP operator Ĥ** — [-d²/dξ² + V(ξ)]f = λf
2. **Robin boundary conditions** — αf + βf' = 0
3. **Self-adjointness criterion** — Real BCs + real V
4. **Dimensionless reduction** — ζ = ξ/ℓ
5. **First eigenvalue x₁** — Ground state
6. **Overlap integral I₄** — ∫|ψ₀|⁴ dξ
7. **Generation count N_bound** — Bound states below threshold
8. **Essential spectrum threshold λ_th** — inf σ_ess
9. **Admissible BC family B** — Allowed Robin space
10. **Spectral stability** — N_bound locally constant
11. **V(ξ) derivation pipeline** — 5D action → warp → reduction

### Key Equations
- `\label{eq:bvp:operator}` — Ĥf = -d²f/dξ² + V(ξ)f = λf
- `\label{eq:bvp:robin_bc}` — Robin BC form
- `\label{eq:bvp:I4_def}` — I₄ definition
- `\label{eq:bvp:nbound_def}` — N_bound definition
- `\label{eq:bvp:threshold_def}` — λ_th = inf σ_ess
- `\label{eq:bvp:vz_structure}` — V = V_warp + V_mass + V_coupling

### Dependencies
- ← CH08/CH09: V-A motivation
- ← CH11: G_F closure spine
- → OPR-02: Generation counting
- → OPR-20: BC provenance
- → OPR-21: Mode overlap
- → OPR-22: Quantitative G_F

---

## Statistics

| Chapter | Concepts | Equations | Dependencies |
|---------|----------|-----------|--------------|
| CH01 | 10 | 8 | 3 |
| CH02 | 10 | 4 | 2 |
| CH03 | 10 | 4 | 3 |
| CH04 | 10 | 7 | 4 |
| CH05 | 7 | 4 | 3 |
| CH06 | 5 | 3 | 3 |
| CH07 | 7 | 4 | 3 |
| CH08 | 9 | 5 | 4 |
| CH09 | 10 | 7 | 4 |
| CH10 | 10 | 1 | 4 |
| CH11 | 10 | 5 | 5 |
| CH12 | 8 | 0 | 2 |
| CH13 | 8 | 4 | 3 |
| CH14 | 11 | 6 | 6 |
| **TOTAL** | **125** | **62** | **49** |

---

*Generated: 2026-01-24*
*Audit Protocol: book2-narrative-audit-v1*
