# Donor Hunt Pass 3: Repo-Wide Gap-to-Donor Mapping

**Date:** 2026-01-31
**Branch:** `audit/donor-hunt-pass3-v1`
**Scope:** All 20 gaps from `gap_register_full.json`

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Gaps | 20 |
| Already Closed (TIER-0/1) | 6 |
| High-Quality Donor Found | 5 |
| Partial Donor | 7 |
| No Donor Available | 2 |

**TIER-2 Ready Candidates:** GAP-8 (PMNS θ₁₂), GAP-19 (g₅ reduction)

---

## Gap Status Overview

### Already Closed (TIER-0 + TIER-1)

| GAP-ID | Title | Tier | Status |
|--------|-------|------|--------|
| GAP-1 | V-A ↔ SM dictionary mapping | TIER-0 | DONE |
| GAP-4 | Z₆ → sin²θ_W partition counting | TIER-0 | DONE |
| GAP-10 | G_F mediator integration | TIER-0 | DONE |
| GAP-5 | SSB mechanism vs EDC mass | TIER-1 | DONE |
| GAP-11 | Yukawa from overlap integrals | TIER-1 | DONE |
| GAP-14 | μ-window generation constraint | TIER-1 | DONE |

---

### High-Quality Donors (Ready for TIER-2)

#### GAP-8: PMNS θ₁₂ derivation
**Status:** OPEN (HIGH donor quality)

| Donor File | Lines | Content |
|------------|-------|---------|
| `src/sections/ch6_pmns_attempt4_2_theta12_origin.tex` | 1-191 | Two geometric candidates: T1 arctan(1/√2)=35.26°, T2 45°-arcsin(λ)=32° |

**Donor Quality:** HIGH
**Recommendation:** T1 preferred (pure geometry [Dc], 8.6% error). Could close GAP-8 by adding dictionary box mapping T1 formula to book chapter 9.

---

#### GAP-19: g₅ derivation (OPR-19)
**Status:** OPEN (HIGH donor quality)

| Donor File | Lines | Content |
|------------|-------|---------|
| `src/sections/ch17_opr19_g5_from_action.tex` | 1-481 | FULL: g₅→g₄ reduction formula derived [Dc] |

**Key Result:**
```
1/g₄² = (1/g₅²) ∫|f(ξ)|² dξ
```
Warp factor cancellation proven.

**Donor Quality:** HIGH
**Recommendation:** Formula is [Dc]; book chapter 13 needs update to reference this. Warp factor A(ξ) and domain ℓ remain [P].

---

#### GAP-6: CKM matrix from overlap geometry
**Status:** PARTIAL

| Donor File | Lines | Content |
|------------|-------|---------|
| `src/sections/07_ckm_cp.tex` | 427-613 | Overlap model: λ, λ², λ³ scaling |
| `src/sections/07_ckm_cp.tex` | 673-824 | Non-uniform spacing: Δξ₁₂, Δξ₂₃ |
| `src/sections/07_ckm_cp.tex` | 826-923 | Prefactor analysis |

**Donor Quality:** HIGH for hierarchy, OPEN for (ρ̄, η̄)
**Recommendation:** Wolfenstein hierarchy [Dc] complete; (ρ̄, η̄) requires OPR-11.

---

#### GAP-7: CKM CP phase derivation
**Status:** PARTIAL

| Donor File | Lines | Content |
|------------|-------|---------|
| `src/sections/ch7_attempt4_cp_refinement.tex` | full | Phase Cancellation Theorem + Z₂ selection |
| `src/sections/ch7_z2_parity_origin.tex` | full | Z₂ ⊂ Z₆ parity mechanism |

**Result:** δ = 60° [Dc] (5° from PDG 65°)
**Recommendation:** Z₂ mechanism provides δ; 5° discrepancy open.

---

#### GAP-12: BVP eigenvalue explicit solution
**Status:** PARTIAL

| Donor File | Lines | Content |
|------------|-------|---------|
| `src/sections/ch12_bvp_workpackage.tex` | 1-200 | BVP specification |
| `src/sections/ch14_bvp_closure_pack.tex` | full | Robin BC, Sturm-Liouville |

**Donor Quality:** HIGH for infrastructure
**Recommendation:** Infrastructure complete; numerical solution not computed.

---

### Partial Donors (Require Additional Work)

#### GAP-2: Effective potential V(ξ) derivation
**Priority:** HIGH

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/ch12_bvp_workpackage.tex` | 147-175 | V(ξ) ansatz (sech²) | PARTIAL |
| `src/sections/05_three_generations.tex` | 256-321 | KK truncation lifetime | PARTIAL |

**Gap:** V(ξ) from membrane parameters (σ, r_e) not derived.
**Recommendation:** Requires new derivation from EDC action.

---

#### GAP-3: Hexagonal packing from action
**Priority:** HIGH

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/05_three_generations.tex` | 202-254 | Z₃ from hexagonal | PARTIAL |

**Gap:** Energy minimization showing hexagonal > square not derived.
**Recommendation:** Needs explicit energy functional calculation.

---

#### GAP-9: PMNS θ₁₃ derivation
**Priority:** LOW

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/ch6_pmns_attempt4_1_derive_epsilon.tex` | full | ε=λ/√2 | MEDIUM |
| `src/sections/06_neutrinos_edge_modes.tex` | 136-146 | DFT falsified | MEDIUM |

**Result:** sin²θ₁₃ ≈ 0.025 (15% from PDG)
**Status:** YELLOW [BL→Dc]

---

#### GAP-13: Barrier parameter C derivation
**Priority:** LOW

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/09_va_structure.tex` | varies | R_LR ~ exp(-Cμ) | PARTIAL |

**Gap:** C coefficient model-dependent.

---

#### GAP-16: Neutrino mass hierarchy
**Priority:** MEDIUM

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/06_neutrinos_edge_modes.tex` | 44-99 | Edge-mode mechanism | PARTIAL |

**Gap:** Normal vs inverted not derived from EDC.

---

#### GAP-18: Robin parameter κ derivation
**Priority:** HIGH

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/ch14_bvp_closure_pack.tex` | varies | κ in BVP | MEDIUM |
| `src/sections/ch11_opr20_attemptD_interpretation_robin_overcount.tex` | full | Robin interpretation | MEDIUM |

**Gap:** κ value contributes ±10% uncertainty, not derived from microphysics.

---

#### GAP-20: M_W prediction (OPR-20)
**Priority:** HIGH

| Donor File | Lines | Content | Quality |
|------------|-------|---------|---------|
| `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex` | full | m_φ = x₁/ℓ | MEDIUM |
| `src/sections/ch11_opr20_attemptH_delta_equals_Rxi.tex` | full | δ = R_ξ attempt | MEDIUM |

**Blocking Dependencies:** OPR-19 (g₅), OPR-21 (BVP), OPR-04 (δ)

---

### No Donor Found

#### GAP-15: SU(2)_L gauge symmetry origin
**Priority:** HIGH

**Status:** NO_DONOR_FOUND
**Issue:** Why SU(2)_L specifically? Postulated [P], not derived.
**Recommendation:** Fundamental open problem requiring new theoretical development.

---

#### GAP-17: Dirac vs Majorana nature
**Priority:** LOW

**Status:** NO_PREDICTION
**Issue:** EDC framework accommodates both, makes no prediction.
**Recommendation:** Framework-agnostic by design; not a gap to close.

---

## TIER-2 Recommendations

### Immediate (can backfill now)
1. **GAP-8** (PMNS θ₁₂): Add dictionary box with T1 formula arctan(1/√2)
2. **GAP-19** (g₅): Reference ch17 reduction formula in Part 3 chapter 13

### Requires BVP Closure First
- GAP-2, GAP-12, GAP-13, GAP-18, GAP-20

### Requires New Derivation
- GAP-3 (hexagonal energy minimization)
- GAP-15 (SU(2)_L origin)

---

## Donor File Index

| File | Gaps Served |
|------|-------------|
| `src/sections/07_ckm_cp.tex` | GAP-6, GAP-7 |
| `src/sections/ch17_opr19_g5_from_action.tex` | GAP-19 |
| `src/sections/ch12_bvp_workpackage.tex` | GAP-2, GAP-12 |
| `src/sections/ch14_bvp_closure_pack.tex` | GAP-12, GAP-18 |
| `src/sections/ch6_pmns_attempt4_2_theta12_origin.tex` | GAP-8 |
| `src/sections/06_neutrinos_edge_modes.tex` | GAP-9, GAP-16, GAP-17 |
| `src/sections/05_three_generations.tex` | GAP-2, GAP-3 |

---

## Next Steps

1. Execute TIER-2 backfill for GAP-8, GAP-19
2. Complete BVP numerical solution to unblock GAP-12 → GAP-2 → GAP-20
3. Flag GAP-15 as "structural postulate" in OPR register
