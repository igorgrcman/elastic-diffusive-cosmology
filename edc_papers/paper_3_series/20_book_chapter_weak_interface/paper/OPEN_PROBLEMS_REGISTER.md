# Open Problems Register (OPR) — Part II: Weak Sector

**Version:** 1.12
**Date:** 2026-01-22
**Status:** Active research program

> **PMNS:** θ₂₃ closed; θ₁₃ closed by ε=λ/√2; θ₁₂ geometric origin arctan(1/√2) (8.6% off)—OPR-05 all now [Dc] or [BL→Dc].

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
| OPR-02 | KK tower truncation | **RED-C** [P] | BVP Work Package defined; solver skeleton exists | Physical potential V(z); BCs from physics | P1 | See §12 BVP Work Package |
| OPR-03 | Bulk topology π₁(M₅) = Z₃ | RED [P] | Speculative | EDC dynamics constraint on π₁ | P3 | Investigate topological constraints |

### Chapter 6: Neutrinos & Edge Modes

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-04 | Absolute neutrino masses | RED (open) | Suppression mechanism | First-principles m_νi values | P2 | Solve edge-mode BVP with Higgs profile |
| OPR-05a | PMNS θ₂₃ | **GREEN [Dc]** | sin²θ₂₃ = 0.564 from Z₆ geometry | — | P2 | Closed (Attempt 2) |
| OPR-05b | PMNS θ₁₃ / ε | **YELLOW [BL→Dc]** | ε = λ/√2 predicts sin²θ₁₃ = 0.025 (15% off) | √2 formal derivation | P2 | Attempt 4.1: no PDG-smuggling |
| OPR-05c | PMNS θ₁₂ | **YELLOW [Dc]** | arctan(1/√2) = 35.26° (8.6% off) | T1 vs T2 selection | P2 | Attempt 4.2: geometric origin |
| OPR-06 | PMNS CP phase δ | RED (open) | Not addressed | Rephasing-invariant phase | P2 | Apply Z₃ phase mechanism (cf. Ch7) |
| OPR-07 | Dirac vs Majorana | RED (open) | Both compatible | Discrimination criterion | P3 | Investigate Majorana mass term in 5D |
| OPR-08 | Z₃ breaking for PMNS | YELLOW [P] | Mechanism postulated | Explicit calculation | P2 | Quantify breaking perturbations |

### Chapter 7: CKM Matrix & CP Violation

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-09 | Quark profile ansatz | RED [P] | Exponential postulated | Derive from 5D Dirac BVP | P2 | Solve thick-brane fermion equation |
| OPR-10 | κ_q/κ_ℓ ≈ 0.4 | YELLOW [I] | Identified from data | First-principles mechanism | P2 | Derive localization asymmetry |
| OPR-11 | (ρ̄, η̄) derivation | **YELLOW [Dc]+[P]** | Odd sign-flip rule [Dc]; brane-reflection parity [P] | Specific element from BVP | P2 | See §7 Z₂ parity origin; BVP profiles needed |
| OPR-12 | CP phase δ | **YELLOW [Dc]+[I]** | Phase Cancellation Thm [Dc]; Z₂→δ=60° (5° from PDG) | Z₂ parity assignment [I] | P2 | **Attempt 4 DONE**: δ improved from 55° to 5° error |
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
| OPR-17 | SU(2)_L gauge embedding | **YELLOW [P]** | Where/how fixed (brane-localized) | Gauge origin + W/Z masses | P2 | Origin requires deriving gauge symmetry |
| OPR-18 | CKM/PMNS from Ch7/Ch6 | RED (open) | Flagged as dependency | See OPR-05, OPR-11 | P1 | Cross-reference |

### Chapter 11: Fermi Constant G_F

**Sanity skeleton established:** Chain map + dimensional checks + attack-surface analysis complete. See §11.8.
**Chain tightened (2026-01-22):** Canonical g₅ normalization + KK spectrum derivation spine added. See §11.9.

| ID | Item | Status | Established | Missing | Priority | Next Action |
|----|------|--------|-------------|---------|----------|-------------|
| OPR-19 | 5D gauge coupling g₅ | **RED-C** [Dc]+[OPEN] | $g_4 = g_5$ from 5D action + orthonormal modes [Dc] | $g_5$ value from underlying theory | P2 | Derive $g_5$ from 5D gauge theory |
| OPR-20 | Mediator mass m_φ | **RED-C** [Dc]+[OPEN] | $m_\phi = x_1/\ell$ from KK eigenvalue [Dc] | $\ell$ from membrane; BCs from physics | P2 | Derive $\ell$ from $(\sigma, r_e)$ |
| OPR-21 | Mode profiles f_L(z) | **RED-C** [P] | BVP Work Package + solver skeleton; I₄ computed | Physical BCs; potential from membrane params | P1 | See §12 BVP Work Package |
| OPR-22 | G_F first-principles | **YELLOW [Dc]+[OPEN]** | Closure spine: $G_F = g_5^2 \ell^2 I_4 / x_1^2$ [Dc]; no-smuggling guardrails; attack-surface map | Numeric values: $g_5$ (OPR-19), $\ell$ (OPR-20), $I_4$ (OPR-21) | P1 | See §11 Full Closure Plan |

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
3. ~~**OPR-11/12**: (ρ̄, η̄) and δ~~ → **Attempt 4 + Z₂ DONE**: Phase Cancellation Theorem [Dc], Z₂ sign-selection gives δ=60° (5° from PDG). **OPR-11 upgraded to YELLOW [Dc]+[P]** (odd sign-flip rule [Dc], brane-reflection parity [P]), OPR-12 upgraded to YELLOW [Dc]+[I]
4. ~~**OPR-17**: SU(2)_L embedding~~ → **PARTIAL (YELLOW [P])**: where/how fixed; origin+masses remain OPEN
5. **OPR-19–22**: G_F chain — sanity skeleton + **chain tightening** (g₅ canonical + KK spectrum [Dc]); first-principles numerics still RED-C

---

## Highest-Value Closure Targets

Based on the analysis, these are the research directions with maximum payoff:

### 1. Thick-Brane BVP Solver
**Appears in:** OPR-02, 09, 14, 15, 21
**Unlocks:** Generation counting, pion decay, G_F derivation, neutrino masses
**Effort:** High (requires numerical/analytic solution)
**Progress (2026-01-22):** BVP Work Package defined in §12; solver skeleton demonstrates bound states exist (Neumann/Mixed BCs); acceptance criteria + failure modes documented. Path forward: physical potential V(z) from membrane parameters + BC justification.

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

### Completed: PMNS Attempt 4 (OPR-05)

**Target:** Test structured perturbative approaches to reproduce the asymmetric PMNS pattern
**Result:** GREEN numerically, YELLOW epistemically

| Model | Track | sin²θ₁₂ | sin²θ₂₃ | sin²θ₁₃ | [Cal] | Status |
|-------|-------|---------|---------|---------|-------|--------|
| PDG 2024 | [BL] | 0.307 | 0.546 | 0.022 | — | — |
| A4-1 | A | 0.308 | 0.564 | 0.022 | None* | **GREEN** |
| A4-1 | B | 0.308 | 0.564 | 0.022 | ε | **GREEN** |
| A4-2 | A | 0.124 | 0.959 | 0.019 | None | YELLOW |
| A4-2 | B | 0.142 | 0.966 | 0.022 | r | YELLOW |
| A4-3 | A | 0.219 | 0.602 | 0.000 | None | RED |
| A4-3 | B | 0.281 | 0.624 | 0.007 | κ_e | YELLOW |

*Track A uses θ₁₂⁰ = 33.7° from discrete set; see epistemic note below.

**Best configuration (A4-1):**
- θ₂₃⁰ = arcsin√0.564 ≈ 48.7° — **[Dc]** from Z₆ geometry (Attempt 2)
- θ₁₂⁰ = 33.7° — **[I]** identified (matches PDG exactly, no geometric derivation)
- ε = 0.15 rad — **[I/Cal]** (produces sin²θ₁₃ = 0.022)

**Construction:**
```
U_PMNS = R₂₃(θ₂₃⁰) · R₁₃(ε) · R₁₂(θ₁₂⁰)
```

**Key findings:**
1. **Structure identified:** The asymmetric PMNS pattern can be produced by rank-2 baseline with reactor perturbation
2. **θ₂₃ preserved:** Geometric derivation from Attempt 2 (sin²θ₂₃ = 0.564) survives in A4-1
3. **θ₁₂ requires input:** No discrete geometric angle naturally produces θ₁₂ ≈ 33.7°
4. **θ₁₃ controllable:** Set by ε; ε ≈ 0.15 rad gives observed value (no geometric origin)
5. **Double-path fails (A4-2):** Breaks θ₂₃, pushing to ~0.96
6. **Flavor-κ insufficient (A4-3):** Cannot simultaneously fit all three angles

**Epistemic assessment:**
- θ₂₃: **GREEN [Dc]** — derived from Z₆ geometry
- θ₁₂: **YELLOW [I]** — structure works, value not derived
- θ₁₃: **YELLOW [I/Cal]** — controlled by ε, value not derived
- Overall OPR-05: **YELLOW [Dc/I]** — θ₂₃ derived; θ₁₂, θ₁₃ structure identified but values require derivation

**What remains open:**
- Geometric origin of θ₁₂⁰ ≈ 33.7°
- Geometric origin of ε ≈ 0.15 rad
- CP phase δ_PMNS (not addressed)

**Code:** `code/pmns_attempt4_menu_sweep.py`
**LaTeX:** `sections/ch6_pmns_attempt4_menu.tex`

---

### Completed: PMNS Attempt 4.1 (OPR-05)

**Target:** Derive ε from existing EDC quantities (λ, κ ratio) without smuggling PDG θ13
**Result:** ε = λ/√2 achieves 15% accuracy on θ13

| Candidate | ε (rad) | sin²θ13 | PDG | Error | Status |
|-----------|---------|---------|-----|-------|--------|
| C1: λ/√2 | 0.159 | 0.0253 | 0.022 | 15% | **YELLOW** |
| C2: λ×κ | 0.090 | 0.0081 | 0.022 | 63% | RED |

**Best result (C1 + discrete θ12 = 35°):**

| Angle | Model | PDG | Status |
|-------|-------|-----|--------|
| sin²θ12 | 0.329 | 0.307 | GREEN (7%) |
| sin²θ23 | 0.564 | 0.546 | GREEN (3%) |
| sin²θ13 | 0.025 | 0.022 | YELLOW (15%) |

**Key findings:**
1. **ε = λ/√2 works:** Predicts sin²θ13 = 0.025 (15% from PDG) without fitting
2. **No new [I] dependency:** Uses only λ [BL] + geometric √2 factor
3. **Discrete θ12 = 35° achieves GREEN:** No PDG-smuggling required for θ12
4. **C2 fails:** κ_q/κ_ℓ ≈ 0.4 is too small; would need ~0.66

**Epistemic assessment:**
- θ23: **GREEN [Dc]** — Z6 geometry (unchanged)
- θ13: **YELLOW [BL→Dc]** — ε = λ/√2, predicted not fit
- θ12: **YELLOW [I]** — 35° discrete or 33.7° identified (→ upgraded by Attempt 4.2)

**Code:** `code/pmns_attempt4_1_derive_epsilon.py`
**LaTeX:** `sections/ch6_pmns_attempt4_1_derive_epsilon.tex`

---

### Completed: PMNS Attempt 4.2 (OPR-05c)

**Target:** Derive θ12 from geometry without PDG-smuggling
**Result:** Two geometric mechanisms, both achieve GREEN (~8.6% error)

| Candidate | θ12 (deg) | sin²θ12 | PDG | Error | Status | Tag |
|-----------|-----------|---------|-----|-------|--------|-----|
| T1: arctan(1/√2) | 35.26 | 0.333 | 0.307 | 8.6% | **GREEN** | [Dc] |
| T2: 45° - arcsin(λ) | 32.00 | 0.281 | 0.307 | 8.5% | **GREEN** | [BL→Dc] |
| PDG target | 33.65 | 0.307 | — | — | — | [BL] |

**Key findings:**
1. **T1 (arctan(1/√2)) preferred:** Pure geometry [Dc], no baseline input
2. **PDG sits between T1 and T2:** T1 overshoots by 1.6°, T2 undershoots by 1.7°
3. **Unified √2 factor:** Same √2 appears in ε = λ/√2 (Attempt 4.1) and θ12 = arctan(1/√2)
4. **35° discrete origin:** T1 provides geometric origin for Attempt 4.1's 35° candidate

**Epistemic assessment:**
- θ23: **GREEN [Dc]** — Z6 geometry (unchanged)
- θ13: **YELLOW [BL→Dc]** — ε = λ/√2 (unchanged)
- θ12: **YELLOW [Dc]** — arctan(1/√2) = 35.26° (upgraded from [I])

**PMNS complete:** All three angles now have geometric mechanisms, none calibrated to PDG.

**Code:** `code/pmns_attempt4_2_theta12_origin.py`
**LaTeX:** `sections/ch6_pmns_attempt4_2_theta12_origin.tex`

---

### Completed: CKM Attempt 4 + Z₂ Parity (OPR-11/12)

**Target:** Improve δ from 120° (Z₃ minimal) to ~65° (PDG); derive (ρ̄, η̄) sign structure
**Constraint:** Preserve J ~ 3×10⁻⁵ (already within 6%)

**Mechanisms tested:**
- M1: Z₆ = Z₂×Z₃ "half-phase" selection → δ = 60° ✓
- M2: Non-uniform discrete charges → J = 0 (Phase Cancellation Theorem)
- **M3: Z₂-controlled sign flips → δ = 60° ✓ (SELECTED)**
- M4: Minimal holonomy/torsion → δ = 60° ✓

**Key results:**
| Claim | Status | Note |
|-------|--------|------|
| Phase Cancellation Theorem | **GREEN [Dc]** | Pure Z₃ gives J = 0 identically |
| Sign-flip count rule | **GREEN [Dc]** | Odd # of flips → δ = 60° |
| Brane-reflection parity | **YELLOW [P]** | Geometric interpretation |
| Specific element (V_cb/V_ub) | **[OPEN]** | Requires BVP profile computation |

**Numerical accuracy:**
- δ = 60° (PDG: 65°, error 5°)
- J = 2.9×10⁻⁵ (PDG: 3.08×10⁻⁵, error 6%)

**Code:** `tools/check_z2_parity_sign_rule.py`
**LaTeX:** `sections/ch7_z2_parity_origin.tex`

**Status:** COMPLETE — OPR-11: RED → YELLOW [Dc]+[P]; OPR-12: YELLOW [Dc]+[I]

---

### Completed: OPR-19/20 Value Closure Attempt

**Target:** Derive numeric values of $g_5$ and $\ell$ from membrane parameters $(\sigma, r_e)$ without SM input
**Result:** FAILED — No SM-free closure achieved; status remains RED-C [OPEN]

**Candidates surveyed:**

| Candidate | Formula | Value | Target | Status | SM-Free? |
|-----------|---------|-------|--------|--------|----------|
| G1 | $g^2 = 4\pi\sigma r_e^3/\hbar c$ | 0.37 | ~0.42 (SM) | YELLOW [P] | YES |
| G2 | $g_5^2 = (\hbar c)^2/\sigma r_e^2$ | 6650 | — | RED (too large) | YES |
| L1 | $\ell = \pi/M_W$ | 0.04 fm | 0.04 fm | [I] | **NO** |
| L2 | $\ell = (\hbar c/\sigma r_e^2) \times f$ | 34×f fm | 0.04 fm | [P] | YES (f open) |

**Key findings:**
1. **G1 promising:** $g^2 = 4\pi\sigma r_e^3/\hbar c \approx 0.37$ is 11% from SM $g_2^2$. Uses only membrane params.
2. **G2 fails numerically:** Dimensionally correct for $g_5^2$ but gives coupling too large for $G_F$ consistency.
3. **L1 forbidden:** Uses $M_W$ as input—violates no-smuggling guardrails.
4. **L2 requires tuning:** SM-free form but $f_{\text{geom}} \sim 10^{-3}$ is unexplained.
5. **No SM-free $\ell$:** The weak scale does not emerge naturally from $(\sigma, r_e)$ alone.

**What would close:**
- Derive the $4\pi$ coefficient in G1 from loop integral or geometric normalization
- Derive $\ell$ from membrane geometry without importing $M_W$
- OR derive $M_W$ itself from $(\sigma, r_e)$ first

**Code:** `tools/check_g5_ell_dimensions.py`, `tools/scan_ell_candidates.py`
**LaTeX:** `sections/ch11_g5_ell_value_closure_attempt.tex`

**Status:** RED-C [OPEN] — Value closure attempt documented; no upgrade achieved.

---

### Completed: OPR-19 Coefficient Provenance (Attempt 2)

**Target:** Derive the 4π coefficient in G1 from first principles (geometric integral, flux quantization, action normalization)

**Result:** Coefficient candidates enumerated; no unique derivation; status remains RED-C [OPEN]

**Coefficient candidates surveyed:**

| Rank | Coefficient | C value | g² | vs SM | Tag | Assessment |
|------|-------------|---------|-----|-------|-----|------------|
| 1 | 4π (solid angle) | 12.57 | 0.373 | -6% | [Dc] | **Best derived, closest to SM** |
| 2 | 12 (Z₆ × Z₂) | 12.00 | 0.356 | -10% | [P] | Group order match |
| 3 | √3 × 2π | 10.88 | 0.323 | -19% | [P] | If Z₃ contributes |
| 4 | 2π | 6.28 | 0.187 | -53% | [Dc] | Too small |
| 5 | 4π/3 | 4.19 | 0.124 | -69% | [Dc] | Too small |

**Key findings:**
1. **4π is best derived candidate:** g² = 0.373 (6% below SM g₂² ≈ 0.40)
2. **Geometrically natural:** 4π consistent with solid angle, sphere area, flux quantization
3. **NOT uniquely selected:** Alternatives (2π, 4π/3, π) are also derivable but give worse g²
4. **Tension-coupling relation [P]:** The relation g² ∝ σ is postulated, not derived from action

**What would close OPR-19:**
1. Derive g² = 4π σ r_e³/(ℏc) from 5D action KK reduction
2. Show flux quantization uniquely gives 4π coefficient
3. Derive tension-coupling relation from brane action principle

**Code:** `tools/check_g1_coefficient_sensitivity.py` → `code/output/g1_coefficient_sweep.txt`
**LaTeX:** `sections/ch11_g5_value_closure_attempt2_coefficient.tex`

**Status:** RED-C [OPEN] — Coefficient candidates enumerated; 4π is geometrically natural and numerically best, but not uniquely derived.

---

### In Progress: OPR-20 Suppression Mechanism (Attempt A2)

**Target:** Derive the dimensionless suppression factor $f_{\text{geom}} \sim 10^{-3}$ that explains why $\ell \ll r_e$ without using SM inputs

**Result:** PARTIAL — Candidate mechanism identified but with factor-8 discrepancy; status remains RED-C [OPEN]

**Candidates surveyed:**

| Candidate | Formula | Value | Target | m_φ (GeV) | Status | SM-Free? |
|-----------|---------|-------|--------|-----------|--------|----------|
| A (diffusion ratio) | $R_\xi / r_e$ | $10^{-3}$ | $\sim 10^{-3}$ | ~620 | YELLOW [P] | YES |
| A' (corrected) | $8 \times R_\xi / r_e$ | $8 \times 10^{-3}$ | — | ~80 | RED (ad-hoc) | YES* |
| B (BKT) | $\sqrt{c_\kappa / (\sigma r_e^2)}$ | — | — | ~80 | RED (unnatural) | YES |

*A' uses ad-hoc factor of 8; not derived.

**Key findings:**
1. **Candidate A promising:** $f = R_\xi / r_e \sim 10^{-3}$ uses ONLY EDC parameters (diffusion correlation length $R_\xi$ and lattice spacing $r_e$)
2. **Factor-of-8 discrepancy:** Candidate A predicts $m_\phi \approx 620$ GeV, overshooting $M_W \approx 80$ GeV by factor of ~8
3. **Candidate B problematic:** Brane kinetic term mechanism requires $c_\kappa \sim 10^4$ (unnaturally large)
4. **$R_\xi$ origin unresolved:** The diffusion correlation length $R_\xi \sim 10^{-3}$ fm is postulated [P], not derived

**Interpretation of factor-8 discrepancy:**
- Different boundary conditions (e.g., $x_1 \neq \pi$)
- $R_\xi$ should be ~8× larger than currently postulated
- Additional geometric factor from bulk/brane junction
- OR: Candidate A overshoots because it captures only the dominant scale; sub-leading corrections needed

**What would close OPR-20:**
- Derive $R_\xi$ from membrane dynamics (e.g., diffusion length in frozen-regime)
- OR derive the factor-of-8 correction from boundary condition analysis
- OR find alternative suppression mechanism with smaller residual

**Code:** `tools/check_dimensionless_fgeom.py`
**LaTeX:** `sections/ch11_g5_ell_suppression_attempt2.tex`

**Status:** RED-C [OPEN] — Suppression mechanism candidate exists [P]; factor-8 discrepancy unresolved.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-22 | Initial register from Part II scan |
| 1.1 | 2026-01-22 | OPR-05 upgraded to YELLOW (PMNS Attempt 2: θ₂₃ derived) |
| 1.2 | 2026-01-22 | PMNS Attempt 3: Z₆ discrete phases failed to fix θ₁₂, θ₁₃ |
| 1.3 | 2026-01-22 | **PMNS Attempt 4: Rank-2 + ε achieves GREEN numerically; OPR-05 → YELLOW [Dc/I]** |
| 1.4 | 2026-01-22 | **PMNS Attempt 4.1: ε = λ/√2 closes reactor scale (15% accuracy); no PDG-smuggling** |
| 1.5 | 2026-01-22 | **PMNS Attempt 4.2: θ₁₂ = arctan(1/√2) provides geometric origin (8.6% off); OPR-05c → [Dc]** |
| 1.6 | 2026-01-22 | **BVP Work Package: OPR-02/21 → RED-C; solver skeleton + acceptance criteria documented** |
| 1.7 | 2026-01-22 | **OPR-11 Z₂ Parity Origin: RED → YELLOW [Dc]+[P]**; Sign-flip rule [Dc], brane-reflection parity [P] |
| 1.8 | 2026-01-22 | **OPR-22 G_F Full Closure Plan: RED-C → YELLOW [Dc]+[OPEN]**; Closure spine + no-smuggling guardrails |
| 1.9 | 2026-01-22 | **OPR-19/20 Value Closure Attempt**: G1 ($g^2 = 4\pi\sigma r_e^3/\hbar c$) promising (11% from SM); L1/L2 for $\ell$ surveyed—no SM-free closure achieved. Status unchanged: RED-C [OPEN] |
| 1.10 | 2026-01-22 | **OPR-20 Suppression Mechanism (Attempt A2)**: Candidate A ($f = R_\xi/r_e \sim 10^{-3}$) identified; factor-8 discrepancy ($m_\phi \approx 620$ GeV vs $M_W \approx 80$ GeV). Status: RED-C [OPEN], mechanism [P] |
| 1.11 | 2026-01-22 | **OPR-20 Factor-8 Forensic Sweep (Attempt A3)**: 19 SM-free mechanisms surveyed; best [Dc] is $2\pi$ (19% off); $C=8$ numeric match (3.7%) but [P]. Status: RED-C [OPEN] |
| 1.12 | 2026-01-22 | **OPR-19 Coefficient Provenance (Attempt 2)**: 15 coefficients surveyed for $g^2 = C \cdot \sigma r_e^3/(\hbar c)$; best [Dc] is $4\pi$ giving $g^2 = 0.373$ (6% below SM). No unique derivation. Status: RED-C [OPEN] |
