# Flavor Skeleton v0.1 — Minimal Breadth Deliverable

**Version:** 0.1
**Date:** 2026-01-29
**Status:** Minimal Structure Established
**Purpose:** Document what EDC flavor sector actually achieves (no PDFs, no wishful thinking)

---

## A. Executive Summary (5 Bullets)

1. **N_g = 3 DERIVED** — Generation count from Z₆ = Z₂ × Z₃ discrete structure: |Z₃| = 3 [Der]

2. **sin²θ_W = 1/4 (bare) DERIVED** — From |Z₂|/|Z₆| = 2/6 = 1/4 [Der], runs to 0.2314 at M_Z [Dc]

3. **θ₂₃ ≈ 45° DERIVED** — Atmospheric mixing angle from Z₆ overlap geometry [Dc]

4. **CKM HIERARCHY MECHANISM** — Wolfenstein λ, λ², λ³ from localization overlap [Dc/P]

5. **CP PHASE PARTIAL** — δ = 60° from Z₂ selection (5° off PDG 65°) [Dc]; full (ρ̄,η̄) is OPEN

---

## B. Minimal Structural Claims

| Claim | Formula/Value | Status | Anchor | Notes |
|-------|---------------|--------|--------|-------|
| N_g = 3 | \|Z₃\| = 3 | **[Der]** | `05_three_generations.tex:Theorem` | Direct counting |
| sin²θ_W = 1/4 | \|Z₂\|/\|Z₆\| = 2/6 | **[Der]** | `05_three_generations.tex:eq:ch3_sin2_bare` | True EDC prediction |
| sin²θ_W(M_Z) | 0.2314 | [Dc] | `05_three_generations.tex:Table 3.1` | Standard RG, not EDC |
| θ₂₃ (PMNS) | ≈ 45° | **[Dc]** | `ch6_pmns_attempt2.tex` | Z₆ overlap geometry |
| θ₁₂ (PMNS) | ~33° | [I] | `ch6_pmns_attempt4_menu.tex` | Rank-2 + ε structure |
| θ₁₃ (PMNS) | ~8.5° | [I] | `ch6_pmns_attempt4_menu.tex` | Reactor perturbation |
| CKM hierarchy | λ, λ², λ³ | [Dc/P] | `07_ckm_cp.tex:Attempt 2` | Single-parameter calibration |
| CP phase δ | 60° | [Dc] | `ch7_attempt4_cp_refinement.tex` | Z₂ sign selection |
| κ_q/κ_ℓ | ≈ 0.4 | [I] | `07_ckm_cp.tex:eq:ch7_kappa_ratio` | CKM vs PMNS asymmetry |

---

## C. Skeleton Diagram

```
                    Z₆ = Z₂ × Z₃
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    |Z₂|/|Z₆|=1/4    |Z₃|=3       Z₆ phases
          │              │              │
          ▼              ▼              ▼
    sin²θ_W=1/4      N_gen=3        δ≈60°
        [Der]          [Der]         [Dc]
          │              │              │
          │              │              │
          ▼              ▼              ▼
    ┌─────┴─────┐  ┌─────┴─────┐  ┌────┴────┐
    │ Electroweak│  │  PMNS     │  │   CKM   │
    │ (GREEN)   │  │  (YELLOW) │  │ (YELLOW)│
    └───────────┘  └───────────┘  └─────────┘

    LEGEND:
    GREEN  = Derived with explicit calculation
    YELLOW = Mechanism identified, closure incomplete
    RED    = Not yet derived
```

### Sub-structure: Mixing Matrices

```
PMNS:                              CKM:
┌────────────────────┐            ┌────────────────────┐
│ θ₂₃≈45° [Dc]      │            │ Vus~λ     [Dc/Cal] │
│ θ₁₂~33° [I]       │            │ Vcb~λ²    [Dc/Cal] │
│ θ₁₃~8.5° [I]      │            │ Vub~λ³    [Dc]     │
│ δ_PMNS: OPEN      │            │ δ=60°     [Dc]     │
└────────────────────┘            └────────────────────┘
   Broad κ_ℓ                         Narrow κ_q
   (delocalized)                     (localized)
```

---

## D. NO-GO Section (Falsified Approaches)

### D.1. Z₃ DFT Baseline for CKM — **FALSIFIED**

```yaml
id: NO-GO-1
claim: "Z₃ DFT gives |V_ij|² = 1/3 for all elements"
anchor: "07_ckm_cp.tex:eq:ch7_dft_ckm"
result: "×144 off for |V_ub|, ×14 off for |V_cb|"
conclusion: "Pure Z₃ symmetry insufficient; strong breaking required"
commit: "a2e9a6e"
```

### D.2. Z₃ DFT Baseline for PMNS — **FALSIFIED**

```yaml
id: NO-GO-2
claim: "Z₃ DFT gives |U_αi|² = 1/3, hence sin²θ₁₃ = 1/3"
anchor: "ch6_pmns_attempt1.tex"
result: "×15 off for θ₁₃ (predicted 0.333, observed 0.022)"
conclusion: "~25% Z₃ breaking needed in ν_e-ν₃ sector"
```

### D.3. Pure Z₃ Charges → CP Phase — **FALSIFIED**

```yaml
id: NO-GO-3
claim: "Z₃ charge assignment gives nonzero Jarlskog J"
anchor: "ch7_attempt3_cp_phase.tex"
result: "Phase Cancellation Theorem: pure Z₃ gives J = 0"
conclusion: "Z₂ sublattice (parity selection) required for CP"
```

### D.4. Gaussian Overlap Profile — **FALSIFIED**

```yaml
id: NO-GO-4
claim: "Gaussian profile O_ij ∝ exp(-d²) for CKM"
anchor: "07_ckm_cp.tex:eq:ch7_gaussian_corner"
result: "|V_ub| prediction ~10⁻⁴, far too small"
conclusion: "Exponential profile O_ij ∝ exp(-d/2κ) required"
```

---

## E. Open Problems (Flavor Sector)

| ID | Problem | Priority | Blocking? |
|----|---------|----------|-----------|
| OPR-05 | Derive PMNS angles θ₁₂, θ₁₃ from geometry | P1 | Yes for full PMNS |
| OPR-06 | PMNS CP phase δ | P2 | No |
| OPR-09 | Derive f_i(z) profiles from 5D BVP | P1 | Yes for predictions |
| OPR-10 | Derive κ_q/κ_ℓ ≈ 0.4 from QCD-EDC coupling | P2 | No |
| OPR-11 | CKM (ρ̄, η̄) from 5D geometry | P2 | Yes for full CKM |
| OPR-12 | Resolve δ = 60° vs PDG 65° (5° gap) | P2 | No |
| OPR-13 | Koide formula from Z₆? | P3 | No |

---

## F. Next 3 Tests

### Test 1: BVP Solution for Quark Profiles

**Goal:** Solve 5D Dirac equation with boundary conditions to get f_i(z) profiles.

**Expected outcome:** Explicit κ_q, κ_ℓ values; Wolfenstein calibration becomes parameter-free.

**Anchor:** `ch12_bvp_workpackage.tex`

### Test 2: θ₁₂ Origin from Double-Path Mechanism

**Goal:** Derive θ₁₂ ≈ 33° from rank-2 Z₆ mass matrix structure.

**Expected outcome:** Convert [I] tag to [Dc] for solar angle.

**Anchor:** `ch6_pmns_attempt4_2_theta12_origin.tex`

### Test 3: Koide-Phase Connection

**Goal:** Test if Koide formula m_e + m_μ + m_τ = 2/3(√m_e + √m_μ + √m_τ)² emerges from Z₆.

**Expected outcome:** Either derive [Dc] or falsify connection.

**Anchor:** `RT-CH3-006_KOIDE_PHASE.tex`

---

## G. File References

| Topic | Primary Source | Backup |
|-------|---------------|--------|
| N_g = 3 | `sections/05_three_generations.tex` | CANON_BUNDLE CL-5.1 |
| sin²θ_W | `sections/05_three_generations.tex` | CLAIM_LEDGER CL-3.1 |
| PMNS attempts | `sections/06_neutrinos_edge_modes.tex` | ch6_pmns_attempt*.tex |
| CKM attempts | `sections/07_ckm_cp.tex` | ch7_attempt*.tex |
| CP refinement | `sections/ch7_attempt4_cp_refinement.tex` | — |
| BVP workpackage | `sections/ch12_bvp_workpackage.tex` | — |

---

## H. Consistency Checks

### H.1. Cross-Sector Verification

| Parameter | Electroweak | Flavor | Consistent? |
|-----------|-------------|--------|-------------|
| Z₆ structure | sin²θ_W = 1/4 | N_g = 3 | ✓ Same Z₆ |
| Z₂ factor | Chirality (V-A) | CP phase δ | ✓ Both use Z₂ |
| Localization κ | — | κ_q ≠ κ_ℓ | — (no EW test) |

### H.2. Numerical Sanity

| Observable | EDC | PDG 2024 | Error |
|------------|-----|----------|-------|
| sin²θ_W(M_Z) | 0.2314 | 0.2312 | 0.08% |
| θ₂₃ | 45° | 48.6° | ~7% |
| δ (CKM) | 60° | 65° | ~8% |
| |V_ub| structure | A λ³ | 0.0037 | Structure ✓ |

---

## I. Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-01-29 | Initial skeleton: N_g, sin²θ_W, θ₂₃, CKM hierarchy, NO-GOs |

---

*Flavor Skeleton v0.1 — Minimal breadth deliverable for EDC flavor sector. Next: Upgrade OPR-05 (PMNS angles) to [Dc].*
