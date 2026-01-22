# Open Problems Register (OPR) — Part II: Weak Sector

**Version:** 1.0
**Date:** 2026-01-22
**Status:** Active research program

---

## Purpose

This register enumerates all claims in Part II that are explicitly marked as
RED (not derived), YELLOW (partially resolved), or (open). Each entry is
tracked with:
- Unique ID (OPR-XX)
- Current epistemic status
- What is established vs. what is missing
- Priority and expected payoff
- Concrete next actions

**Philosophy:** Open problems are not weaknesses—they are precisely enumerated
targets for future work. A theory with well-defined gaps is stronger than one
with hidden assumptions.

---

## Priority Legend

| Priority | Meaning |
|----------|---------|
| **P1** | Critical for Part II closure; blocks major claims |
| **P2** | Important for quantitative predictions; high reviewer impact |
| **P3** | Desirable refinement; lower urgency |

---

## OPR Items by Chapter

### Chapter 5: Three Generations

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-01 | N_gen = 3 from Z₃ | YELLOW [I] | Numerical matching |Z₃| = 3 | Dynamical derivation linking fermion modes to Z₃ | P2 | Derive mode-symmetry coupling from action |
| OPR-02 | KK tower truncation | RED [P] | Plausible mechanism | Explicit thick-brane potential V(z); mode lifetimes | P1 | Solve thick-brane BVP |
| OPR-03 | Bulk topology π₁(M₅) = Z₃ | RED [P] | Speculative | EDC dynamics constraint on π₁ | P3 | Investigate topological constraints |

### Chapter 6: Neutrinos & Edge Modes

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-04 | Absolute neutrino masses | RED (open) | Suppression mechanism | First-principles m_νi values | P2 | Solve edge-mode BVP with Higgs profile |
| OPR-05 | PMNS mixing angles | **YELLOW [Dc]** | **θ₂₃ derived (3%)** | θ₁₂, θ₁₃ require additional physics | P2 | Attempt 2/3 DONE; discrete Z₆ phases insufficient; need non-abelian extension |
| OPR-06 | PMNS CP phase δ | RED (open) | Not addressed | Rephasing-invariant phase | P2 | Apply Z₃ phase mechanism (cf. Ch7) |
| OPR-07 | Dirac vs Majorana | RED (open) | Both compatible | Discrimination criterion | P3 | Investigate Majorana mass term in 5D |
| OPR-08 | Z₃ breaking for PMNS | YELLOW [P] | Mechanism postulated | Explicit calculation | P2 | Quantify breaking perturbations |

### Chapter 7: CKM Matrix & CP Violation

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-09 | Quark profile ansatz | RED [P] | Exponential postulated | Derive from 5D Dirac BVP | P2 | Solve thick-brane fermion equation |
| OPR-10 | κ_q/κ_ℓ ≈ 0.4 | YELLOW [I] | Identified from data | First-principles mechanism | P2 | Derive localization asymmetry |
| OPR-11 | (ρ̄, η̄) derivation | RED (open) | Structure Aλ³ correct | Complex prefactor | P1 | **Attempt 4: Z₆ refinement** |
| OPR-12 | CP phase δ (120° vs 65°) | YELLOW [I] | J magnitude correct (6%) | Phase angle factor 2 off | P1 | **Attempt 4: Z₆ = Z₂×Z₃ selection** |
| OPR-13 | Jarlskog J | YELLOW [Dc] | J = 2.9×10⁻⁵ (no calibration) | δ refinement | P2 | Already partial success |

### Chapter 8: Pion Decay

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-14 | m_ℓ² scaling from BCs | RED (open) | Postulated mechanism | Explicit BC computation | P2 | Specify pion wavefunction, compute overlap |
| OPR-15 | Pion composite structure | RED (open) | Not specified | Quark-defect wavefunction | P2 | Define composite in brane layer |
| OPR-16 | Pion mass m_π | RED (open) | Not derived | Quark/defect binding theory | P3 | Requires QCD-EDC interface |

### Chapter 9: V-A Structure

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-17 | SU(2)_L gauge embedding | RED (open) | V-A derived at interface | Full non-abelian structure | P1 | 5D gauge theory; W±, Z⁰ masses |
| OPR-18 | CKM/PMNS from Ch7/Ch6 | RED (open) | Flagged as dependency | See OPR-05, OPR-11 | P1 | Cross-reference |

### Chapter 11: Fermi Constant G_F

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-19 | 5D gauge coupling g₅ | RED-C (open) | Postulated | Derive from canonical normalization | P1 | Specify 5D gauge kinetic term |
| OPR-20 | Mediator mass m_φ | RED-C (open) | Postulated | KK reduction of throat geometry | P1 | Identify lowest massive mode |
| OPR-21 | Mode profiles f_L(z) | RED-C (open) | Not solved | Thick-brane fermion BVP | P1 | Solve with explicit BCs |
| OPR-22 | G_F first-principles | RED-C (open) | Numerical consistency | Complete derivation chain | P1 | Closure of OPR-19,20,21 |

### Neutron Decay (Ch5 subsection)

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-23 | Barrier height V_B | RED (open) [Cal] | Calibrated to τ_n | Derive from junction geometry | P2 | First-principles V_B |
| OPR-24 | Junction charge q_n | YELLOW [I] | q_n ≈ 1/3 from Z₆ | Reconcile with calculation | P3 | Verify Z₆ assignment |

---

## Summary Statistics

| Category | Count | Key Bottleneck |
|----------|-------|----------------|
| **RED (not derived)** | 15 | Thick-brane BVP; SU(2)_L embedding |
| **YELLOW (partial)** | 9 | OPR-05 upgraded; δ refinement; κ asymmetry |
| **Total OPR items** | 24 | — |

**Recent progress:** OPR-05 upgraded from RED to YELLOW (Attempt 2: θ₂₃ derived)

---

## Critical Path Items (P1)

The following items block major claims and should be prioritized:

1. **OPR-02**: KK tower truncation — needed for N_gen = 3
2. ~~**OPR-05**: PMNS mixing angles~~ → **PARTIAL SUCCESS (Attempt 2)**: θ₂₃ derived [Dc], θ₁₂/θ₁₃ remain open (downgraded to P2)
3. **OPR-11/12**: (ρ̄, η̄) and δ — needed for CKM closure → **Attempt 4**
4. **OPR-17**: SU(2)_L embedding — needed for gauge structure
5. **OPR-19–22**: G_F chain — needed for weak coupling closure

---

## Highest-Value Closure Targets

Based on the analysis, these are the research directions with maximum payoff:

### 1. Thick-Brane BVP Solver
**Appears in:** OPR-02, 09, 14, 15, 21
**Unlocks:** Generation counting, pion decay, G_F derivation, neutrino masses
**Effort:** High (requires numerical/analytic solution)

### 2. CP Violation Mechanism Refinement
**Appears in:** OPR-06, 11, 12, 13
**Unlocks:** Full CKM closure, PMNS CP phase
**Effort:** Medium (Z₆ = Z₂×Z₃ analysis) → **Attempt 4**

### 3. KK Reduction of 5D Geometry
**Appears in:** OPR-19, 20
**Unlocks:** g₅, m_φ, quantitative G_F
**Effort:** Medium-High

### 4. Z₃ Dynamical Coupling
**Appears in:** OPR-01, 08
**Unlocks:** Flavor structure foundation
**Effort:** Medium

---

## Active Research

### Completed: PMNS Attempt 2 (OPR-05)

**Target:** Derive PMNS mixing angles from Z₃/Z₆ geometry
**Result:** PARTIAL SUCCESS

| Angle | Model | PDG | Status |
|-------|-------|-----|--------|
| sin²θ₂₃ | 0.564 | 0.546 | **GREEN (3%)** |
| sin²θ₁₂ | 0.137 | 0.307 | RED |
| sin²θ₁₃ | 0.008 | 0.022 | RED |

**Key finding:** Z₆ submixing naturally produces maximal atmospheric mixing.
**Code:** `code/pmns_attempt2_overlap.py`
**LaTeX:** `sections/ch6_pmns_attempt2.tex`

---

### Completed: PMNS Attempt 3 (OPR-05)

**Target:** Fix θ₁₂ and θ₁₃ using discrete Z₆ phases on A3 overlap magnitudes
**Result:** FAILED

| Track | Method | sin²θ₁₂ | sin²θ₂₃ | sin²θ₁₃ | Status |
|-------|--------|---------|---------|---------|--------|
| PDG 2024 | — | 0.307 | 0.546 | 0.022 | — |
| A (baseline) | No phases | 0.137 | 0.564 | 0.008 | θ₂₃ GREEN, others RED |
| A (best phys.) | Z₆ diagonal | 0.075 | 0.733 | 0.001 | ALL WORSE |
| B1 | Scale O[0,2] ×0.65 | 0.155 | 0.585 | 0.022 | θ₂₃, θ₁₃ GREEN; θ₁₂ YELLOW |

**Key finding:** Discrete Z₆ phases are either removable by rephasing (gauge artifacts) or make the fit worse. The asymmetric PMNS pattern (large θ₁₂, θ₂₃; small θ₁₃) cannot emerge from exponential localization with discrete phases alone.

**Conclusion:** Additional physics required:
1. Non-abelian flavor symmetry (A₄, S₄)
2. Higgs profile anisotropy
3. Charged lepton corrections

**Code:** `code/pmns_attempt3_z6_phase_sweep.py`
**LaTeX:** `sections/ch6_pmns_attempt3_z6_refinement.tex`

---

### Pending: Attempt 4 (CKM δ Refinement)

**Target:** Improve δ from 120° (Z₃ minimal) to ~65° (PDG)
**Constraint:** Preserve J ~ 3×10⁻⁵ (already within 6%)

**Mechanisms to test:**
- M1: Z₆ = Z₂×Z₃ "half-phase" selection
- M2: Non-uniform discrete charges for u/d sectors
- M3: Z₂-controlled sign flips in overlaps
- M4: Minimal holonomy/torsion

**Status:** Pending implementation

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-22 | Initial register from Part II scan |
| 1.1 | 2026-01-22 | OPR-05 upgraded to YELLOW (PMNS Attempt 2: θ₂₃ derived) |
| 1.2 | 2026-01-22 | PMNS Attempt 3: Z₆ discrete phases failed to fix θ₁₂, θ₁₃ |
