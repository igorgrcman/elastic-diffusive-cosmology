# Elastic Diffusive Cosmology — Complete Discovery Report

**Repository**: `elastic-diffusive-cosmology`
**Date**: 2026-03-13
**Scope**: Full read-only analysis of all books, papers, code, audit, and reproducibility infrastructure

---

## 1. Repository Architecture

```
elastic-diffusive-cosmology/
├── edc_book/          # Book 1: Core theory (13 chapters + appendices)
├── edc_book_2/        # Book 2: Weak sector & closure (20 chapters)
│   ├── src/           #   LaTeX source
│   ├── audit/         #   4-phase audit infrastructure
│   ├── canon/         #   OPR registry, symbol canon
│   ├── code/          #   Python validation scripts (OPR-01 to OPR-22)
│   └── repro/         #   Reproducibility manifest & checksums
├── edc_papers/
│   ├── paper_2/       # α derivation paper
│   └── paper_3_series/  # 20 companion papers on weak sector
│       └── code/      #   WKB, soliton, lifetime scripts
└── code/src/edc/      # Python package (epistemic tagging, constants, lensing)
```

**Total scope**: ~500+ files, ~50,000+ lines of LaTeX, ~15,000+ lines of Python.

---

## 2. The EDC Theory in Brief

EDC proposes a **5D membrane cosmology** that derives quantum mechanics and gravity from a single action:

$$S_{\text{EDC}} = \int d^5X \sqrt{|G|}\left[-\rho_{\text{Plenum}} - \tfrac{1}{4}F_{AB}F^{AB} - \tfrac{1}{4}G^a_{AB}G_a^{AB}\right] - \sigma\int d^4x\sqrt{|g|}$$

### Three Fundamental Scales

| Scale | Symbol | Value | Role |
|-------|--------|-------|------|
| Intrinsic (Planck) | ℓ_P | ~10⁻³⁵ m | 5D curvature |
| Extrinsic (thickness) | R_ξ | ~10⁻¹⁸ m | Brane thickness |
| Topological (knot) | r_e | ~10⁻¹⁵ m | Defect radius |

### Core Mechanism

- The universe is a 4D membrane (brane) embedded in a 5D bulk (Plenum)
- Speed of light emerges: c = v_scan (scanning velocity of a vibrating brane)
- Particles = topological defects on the brane surface
- Quarks = string endpoints anchored to a Y-junction (proton)
- Electron = surface defect (genus-1 knot)
- Gravity = emergent from Plenum density ρ_Plenum

---

## 3. Book 1 — Core Theory (`edc_book/`)

**13 chapters + preface + epilogue + 5 appendices**

| Ch. | Title | Key Content |
|-----|-------|-------------|
| 0 | Theory Core V17.49 | Central action S_EDC, Maxwell & Yang-Mills from 5D |
| 1 | Introduction | Historical context, motivation |
| 2 | Foundations | 5D geometric arena, 5 postulates, pullback (c = v_scan) |
| 3 | Confinement | Quarks as string endpoints, confinement theorem, charge quantization |
| 4 | Leptons | Electron as surface defect, m_p/m_e = 6π⁵, mass spectrum |
| 5 | Spin & Pauli | Spin from brane torsion |
| 6 | Quantum Constants | ℏ = σ_eff·r_e³/c, α = m_e c²/(σ_eff r_e²) |
| 7 | Gravity | G from ρ_Plenum, hierarchy problem resolution |
| 8 | River Model | Schwarzschild from hydrodynamics, Mercury precession |
| 9 | Electroweak V17.48 | m_Z = (19/2)·E_scale, sin²θ_W |
| 10 | Strong Force | Asymptotic freedom |
| 11 | Cosmology | Hubble tension hypothesis |
| 12 | Open Problems | Roadmap |
| Epilogue | | Dark matter/energy speculation, 3 future continents |

### Headline Results from Book 1

- **Fine-structure constant**: α = (4π + 5/6)/(6π⁵) ≈ 1/137.027 — **6.7 ppm** from CODATA
- **Proton-electron mass ratio**: m_p/m_e = 6π⁵ — **1.8 ppm** from experiment
- **Weak mixing angle**: sin²θ_W = 1/4 — **[Der]** (tree-level, before RG running)
- **Z boson mass**: m_Z = (19/2)·m_e/α² — **0.03%** from experiment — **[Dc]**
- **Neutron lifetime**: τ_n ≈ 830 s — **6% error** — **[Dc]**

---

## 4. Book 2 — Weak Sector & Closure (`edc_book_2/`)

**20 chapters** extending EDC into the full electroweak sector.

### Structure

| Block | Chapters | Focus |
|-------|----------|-------|
| Foundations | 1–4 | Review, Z₆ symmetry, sin²θ_W, lepton masses |
| Weak Pipeline | 5–8 | Absorption → Dissipation → Release mechanism |
| Boson Sector | 9–10 | W/Z/Higgs mass derivations |
| Decay Physics | 11–12 | β-decay, neutron lifetime |
| BVP Closure | 13–16 | Sturm-Liouville eigenvalue problem, OPR-21, frozen projection |
| Attempt Series | 17 | CP violation, PMNS matrix, lepton mass candidates |
| Synthesis | 18–20 | Epistemic summary, closure status |

### Key Concept: Unified Weak Pipeline

```
Absorption → Dissipation → Release
(W⁻ capture)   (ξ-channel)   (e⁻ + ν̄_e emission)
```

All weak decays follow this 3-stage pattern through the extra dimension ξ.

### Key Concept: Z₆ = Z₂ × Z₃ Symmetry

The hexagonal lattice symmetry of the brane yields:
- **Z₃**: 3 generations of fermions
- **Z₂**: Chirality (left/right)
- **sin²θ_W = 1/4**: Directly from Z₆ geometry
- **CP phase**: From Z₆ orientation reversal

### Key Concept: BVP (Boundary Value Problem)

The central mathematical challenge is a **Sturm-Liouville eigenvalue problem** in the compact ξ-direction:

```
−ψ″(ξ) + V(ξ)ψ(ξ) = μψ(ξ),   ξ ∈ [0, R_ξ]
```

With Robin boundary conditions. The **frozen projection operator**:

```
P_frozen = P_energy ∘ P_mode ∘ P_chir
```

selects physical modes from the KK tower.

### Epistemic Tagging System

Every claim carries a tag:
- **[Der]** — Derived: follows from S_EDC alone (12 claims)
- **[Dc]** — Derived-conditional: requires auxiliary input (184 claims)
- **[I]** — Identified: pattern noted, not derived
- **[P]** — Proposed: speculative
- **[BL]** — Baseline: external data
- **[Cal]** — Calibrated: fitted parameter
- **[M]** — Mathematics: purely formal result (5 claims)

**Total classified claims**: 201

---

## 5. Paper Portfolio (`edc_papers/`)

### Paper 2: Fine-Structure Constant

- Derives α = (4π + 5/6)/(6π⁵) from geometric arguments
- 6.7 ppm agreement with CODATA 2018
- Derives m_p/m_e = 6π⁵ (1.8 ppm)
- Introduces frozen criterion for mode selection
- 19 ppm correction path identified

### Paper 3 Series: 20 Companion Papers

| # | Code | Focus | Status |
|---|------|-------|--------|
| 01 | A | Geometric foundations | Complete |
| 02 | B | Kaluza-Klein tower | Complete |
| 03 | C | Lattice symmetry Z₆ | Complete |
| 04 | D_sin2 | sin²θ_W = 1/4 | Complete |
| 05 | D_mZ | m_Z derivation | Complete |
| 06 | E | Electron mass | Complete |
| 07 | F | **Proton Y-junction** (backbone) | Complete |
| 08 | G | W± mass | Complete |
| 09 | H | β-decay pipeline | Complete |
| 10 | I | Neutron lifetime | Complete |
| 11 | J | Higgs sector | Complete |
| 12 | K | Neutrino masses | Complete |
| 13 | L | CP violation | Attempt |
| 14 | M | PMNS matrix | Attempt |
| 15 | N | Three generations | Complete |
| 16 | O | Dark matter candidate | Speculative |
| 17 | P | Hubble tension | Speculative |
| 18 | — | Paper 3 v2.0 "Mechanistic Dimensions" | Journal synthesis |
| 19 | — | Zenodo canonical article | Published |
| 20 | — | Supplementary material | Reference |

**Companion F (Proton Y-junction)** is the backbone paper — all others reference it.

---

## 6. Open Problem Registry (OPR)

**22 registered open problems** tracking blocking issues for closure:

| OPR | Title | Status |
|-----|-------|--------|
| OPR-01 | 19 ppm residual in α | Active — requires BVP |
| OPR-02 | Neutron lifetime 6% gap | Active |
| OPR-03 | W mass correction | Active |
| OPR-04 | Higgs mass from BVP | Active |
| OPR-05 | CP violation mechanism | Attempt |
| OPR-06 | PMNS matrix derivation | Attempt |
| OPR-07 | Strong CP problem | Open |
| OPR-08 | Neutrino mass hierarchy | Open |
| OPR-09 | Baryon asymmetry | Open |
| OPR-10 | Dark matter candidate | Speculative |
| OPR-11 | Cosmological constant | Open |
| OPR-12–18 | Various precision targets | Mixed |
| OPR-19 | Higgs self-coupling | Active |
| OPR-20 | Yukawa from geometry | Active |
| OPR-21 | **BVP master closure** | Critical — shape-dependent |
| OPR-22 | Physical μ-sweep | Active |

### Critical Discovery: OPR-21R

The BVP analysis revealed that the **three-generation window** (μ₃) is **shape-dependent**:
- Original estimate: μ₃ ∈ [25, 35)
- Physical domain-wall potential: μ₃ ∈ [13, 17]
- This means the generation count depends on the exact form of V(ξ)

---

## 7. Code Infrastructure

### Python Package (`code/src/edc/`)

- **epistemic.py**: Programmatic epistemic tagging ([Der], [Dc], etc.)
- **constants/registry.py**: Physical constants with provenance
- **physics/lensing.py**: Gravitational lensing calculations

### OPR Validation Scripts (`edc_book_2/code/`)

Each OPR has a dedicated Python script:
- `opr01_alpha_residual.py` — Computes 19 ppm gap
- `opr04_higgs_mass.py` — Higgs mass from BVP eigenvalue
- `opr19_higgs_self_coupling.py` — λ_H prediction
- `opr20_yukawa_geometry.py` — Yukawa coupling from topology
- `opr21_bvp_specification.py` — BVP Sturm-Liouville solver
- `opr22_physical_mu_sweep.py` — μ parameter space scan

### OPEN-22 Series (Critical)

A dedicated series of scripts for the physical BVP:
- `open22_4b_physical_bvp.py` — Full BVP with domain-wall potential
- `open22_4b_robin_bc.py` — Robin boundary condition implementation
- `open22_4b_slice_families.py` — Slice family analysis
- `open22_4b_mu_sweep.py` — μ parameter sweep

**Key finding**: The μ-sweep revealed shape-dependence of the generation count.

### Reproducibility Infrastructure

- **REPRO_MANIFEST.yml**: Maps every claim to its validation script
- **SHA256 checksums**: All script outputs are checksummed
- **Gate enforcement**: Claims cannot advance epistemic status without passing gates
- **Deterministic execution**: All scripts use fixed seeds where applicable

---

## 8. Audit Infrastructure (`edc_book_2/audit/`)

### 4-Phase Audit

| Phase | Scope | What It Checks |
|-------|-------|----------------|
| 1. Mechanical | Equations | Dimensional consistency, sign conventions |
| 2. Context | References | Cross-reference accuracy, citation validity |
| 3. Narrative | Text | Claim-evidence alignment, logical flow |
| 4. Evidence | Data | Numerical reproduction, script verification |

### Master Audit Ledger

- **393 pages** of systematic auditing
- Every equation checked for dimensional consistency
- Every cross-reference verified
- Every numerical claim traced to a script

### Claim Evidence Index

- **201 claims** fully classified:
  - 12 **[Der]** — Pure derivations from S_EDC
  - 184 **[Dc]** — Conditional derivations (need auxiliary input)
  - 5 **[M]** — Pure mathematics

### Symbol Collision Resolution

The audit identified and resolved symbol collisions across Book 1 → Book 2:
- σ (brane tension vs. cross-section)
- μ (BVP eigenvalue vs. chemical potential)
- R (Ricci scalar vs. R_ξ)
- Each resolution documented in the symbol canon

---

## 9. Theory Status Summary

### What EDC Derives (Strong Claims)

| Quantity | Formula | Accuracy | Tag |
|----------|---------|----------|-----|
| α⁻¹ | 6π⁵/(4π + 5/6) | 6.7 ppm | [Der] |
| m_p/m_e | 6π⁵ | 1.8 ppm | [Der] |
| sin²θ_W | 1/4 (tree) | Exact | [Der] |
| Charge quantization | From topology | Exact | [Der] |
| c = v_scan | From pullback | Structural | [Der] |
| ℏ | σ_eff·r_e³/c | Structural | [Der] |

### What EDC Derives Conditionally

| Quantity | Formula | Accuracy | Tag | Condition |
|----------|---------|----------|-----|-----------|
| m_Z | (19/2)·m_e/α² | 0.03% | [Dc] | Z-scale identification |
| τ_n | ~830 s | 6% | [Dc] | Pipeline model |
| m_W | From m_Z, sin²θ_W | ~0.1% | [Dc] | Tree-level |
| G_N | From ρ_Plenum | Structural | [Dc] | Plenum EOS |

### What Remains Open

1. **BVP closure** (OPR-21) — The central mathematical challenge
2. **3-generation proof** — Currently shape-dependent (OPR-21R)
3. **CP violation** — Attempted but not closed
4. **PMNS matrix** — Attempted but not closed
5. **Lepton mass ratios** — Candidate formulas at [P] level
6. **19 ppm α correction** — Path identified, BVP needed
7. **Neutron lifetime 6% gap** — Pipeline refinement needed
8. **Dark matter/energy** — Speculative level only

---

## 10. Architecture Insights

### Strengths
1. **Rigorous epistemic discipline** — Every claim tagged, no overclaiming
2. **Reproducibility-first** — Scripts, checksums, gates
3. **Systematic audit** — 4-phase, 393 pages
4. **Single action principle** — Everything from S_EDC
5. **Remarkable numerical agreement** — α at 6.7 ppm from pure geometry

### Risks / Open Questions
1. **BVP shape-dependence** — Generation count not yet universal
2. **Large [Dc] fraction** — 184/201 claims need auxiliary input
3. **Frozen projection** — Selection rule needs independent justification
4. **Z-scale identification** — The factor 19/2 is [I], not [Der]
5. **No experimental predictions** — Unique to EDC, testable, not yet proposed

### Dependencies

```
S_EDC (Action)
  ├── Pullback → c = v_scan → ℏ, α [Der]
  ├── Topology → charge quantization, m_p/m_e [Der]
  ├── Z₆ lattice → sin²θ_W, 3 generations [Der/Dc]
  ├── KK reduction → BVP → masses [Dc]
  │     └── OPR-21 (BLOCKING)
  ├── Plenum EOS → G_N [Dc]
  └── Weak pipeline → τ_n, β-decay [Dc]
```

---

*This report is a read-only discovery analysis. No files were modified.*
