# Red-Team QA Memo — Book IV

**Date:** 2026-02-10
**Reviewer:** Adversarial Analysis

---

## Executive Summary

Book IV presents a coherent EDC-native derivation chain from topological axioms to
quantitative predictions. However, several "boss dependencies" carry high falsification
risk. This memo identifies the weakest links for external review.

---

## 1. Hidden Assumptions

### 1.1 L₀/δ ≈ π² [P]+[OPEN]
**Assumption:** The ratio of junction length to thickness equals π².
**Hiding mechanism:** Introduced as "geometric constraint" without full 5D derivation.
**Impact:** τ scales as exp(κ · L₀/δ · ...), so ±10% in L₀/δ → orders of magnitude in τ.
**Red-team question:** Why π² and not 3π or π³/3? What constrains this ratio?

### 1.2 Barrier Height Quantization
**Assumption:** V_B = 2 × 1.293 MeV derived from "one Δm unit per arm."
**Hiding mechanism:** The "one unit per arm" rule is stated as geometric, but justification is thin.
**Impact:** Entire instanton action depends on V_B.
**Red-team question:** Where is the quantization condition proven? Is it 1, 2, or 3 units?

### 1.3 Prefactor A (ω₀)
**Assumption:** Attempt frequency ω₀ ≈ 10²¹ s⁻¹.
**Hiding mechanism:** Stated as "characteristic 5D oscillation frequency" with dimensional analysis.
**Impact:** τ = A × exp(S_E), so A is a direct multiplicative factor.
**Red-team question:** Can A be derived from M₅ and L₀, or is it a free parameter?

### 1.4 Closed-4 Optimality
**Assumption:** A = 4 is the minimal closed unit with maximal per-junction efficiency.
**Hiding mechanism:** Stated as "geometric observation" rather than proven theorem.
**Impact:** Entire "release bias" interpretation rests on this.
**Red-team question:** Prove that A = 3 or A = 5 cannot form closed units, or that they are suboptimal.

---

## 2. Narrative Jumps

### 2.1 S⁵ → Z₆ Crystallization (Ch 2)
**Jump:** From 5D membrane topology to discrete Z₆ symmetry at junction.
**Issue:** The map between continuous S⁵ homotopy and discrete crystallization is gestured at, not derived.
**Severity:** Medium — affects foundational interpretation.

### 2.2 Steiner Geometry → M₆ Lattice (Ch 2 → Ch 5)
**Jump:** 120° angles at Y-junction immediately yield hexagonal faces and n = 6 coordination.
**Issue:** The "minimal faces are hexagons" step needs careful Euler-characteristic accounting.
**Severity:** Low — the duality argument is sound, but could be more explicit.

### 2.3 Baseline → Frustration Correction (Ch 13 → Ch 14)
**Jump:** Residuals from GN lane are attributed to coordination frustration via d(n).
**Issue:** Why d(n) = min|n - k| for k ∈ S? Could other metrics (e.g., weighted, log-scaled) fit better?
**Severity:** Medium — affects predictive model choice.

---

## 3. Sensitivity Vulnerabilities

### 3.1 Exponential Sensitivity to L₀/δ
**Mechanism:** τ ∝ exp(2π · π² · V_B/T*) — the exponent is ~55–60.
**Vulnerability:** 1% change in L₀/δ → ~1 unit in exponent → factor of ~3 in τ.
**Falsification:** If observed τ_n deviates by > 5%, model is in tension.

### 3.2 Prefactor Sensitivity
**Mechanism:** n(A) = p × A^(1/3) with p = 6.1 [Cal].
**Vulnerability:** p is fitted, not derived. Different p gives systematically shifted predictions.
**Falsification:** If derived p ≠ 6.1 by > 10%, current predictions need revision.

### 3.3 Frustration Coefficient g
**Mechanism:** Δ = g · d(n) with g ≈ -1.76 [Cal].
**Vulnerability:** g is fitted on training set. Out-of-sample test needed.
**Falsification:** If new superheavy data shows g outside [-2.5, -1.0], model is stressed.

---

## 4. Falsification Criteria

### 4.1 Metastable Junction Lifetime
**Prediction:** τ_n ≈ 880 s
**Falsification:** |τ_observed - 880| / 880 > 5% after accounting for experimental error.

### 4.2 Forbidden Zone
**Prediction:** No cluster with n(A) ∈ [37, 47] exhibits standard release behavior.
**Falsification:** Discovery of such a cluster with normal release kinetics.

### 4.3 High-Coordination Residuals
**Prediction:** |Δ| < 2.0 dex for all benchmark cases.
**Falsification:** Any case with |Δ| > 2.5 dex indicates model breakdown.

### 4.4 Z = 120+ Blind Tests
**Prediction:** Extrapolation to A > 304 should match future measurements within 1.5 dex.
**Falsification:** Systematic bias in extrapolation zone.

---

## 5. Recommendations

1. **L₀/δ Derivation:** Highest priority. Without this, the τ_n prediction is semi-empirical.
2. **Closed-4 Minimality Proof:** Formal proof (or disproof) needed to close the logical gap.
3. **Prefactor Derivation:** Attempt frequency should emerge from 5D action, not be fitted.
4. **S⁵ → Z₆ Formalization:** Add explicit mathematical statement of the crystallization theorem.
5. **d(n) Uniqueness:** Justify why absolute difference is the natural metric for frustration.

---

## 6. Adversarial Summary

| Claim | Confidence | Weakness |
|-------|------------|----------|
| κ = 2π | High | Topologically grounded |
| L₀/δ = π² | Low | [P]+[OPEN], no 5D proof |
| V_B from Δm | Medium | Quantization rule unclear |
| Closed-4 minimal | Medium | Needs formal proof |
| τ_n ≈ 880 s | Medium | Depends on above |
| d(n) frustration | Medium | Metric choice not unique |
| Superheavy predictions | Medium | Extrapolation risk |

**Overall Assessment:** The derivation chain is logically coherent but rests on 2–3 unproven
pillars. A rigorous external review would focus on L₀/δ and the Closed-4 minimality claim.
