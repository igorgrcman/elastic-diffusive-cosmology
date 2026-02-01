# V7.9 CLAIM LEDGER

**Created**: 2026-01-31
**Purpose**: Traceability for all claims in integrated document

---

## Format

| ID | Claim (1-2 lines) | Tag | Source File | Lines |
|----|-------------------|-----|-------------|-------|

---

## Section 1: Introduction and M6 Foundation

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C1.1 | M6 = 6-coordinated topological graph embedded in 5D bulk | [Der] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 21-28 |
| C1.2 | Coordination number = 6 from Z₆ symmetry of Steiner minimum | [Der] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 25-37 |
| C1.3 | q = 0 represents proton-like state, q = 1 represents neutron-like state | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 47-50 |
| C1.4 | Pinning term H_pin = K Σ (q_i - q_j)² | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 256-261 |

---

## Section 2: Free vs Bound Neutron

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C2.1 | Free neutron: S_E/ℏ ≈ 60 → τ ≈ 880 s | [Der] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 335-338 |
| C2.2 | Bound neutron: pinning raises effective barrier, S_E/ℏ ≈ 88 → stable | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 340-346 |
| C2.3 | Pinning constant K ≈ 1 MeV needed for stability | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 305-311 |
| C2.4 | K ~ σ × (0.3 fm)² ≈ 0.8 MeV from brane tension | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 320-328 |
| C2.5 | Deuterium binding energy ~3 MeV from pinning reduction | [P] | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 353-365 |

---

## Section 3: Alpha-Decay Empirical Audit

### 3.1 Coordination Law

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C3.1 | n(A) = 6.1 × A^(1/3) calibrated so n(208) ≈ 36 for Pb-208 | [Der] | V7.4/07_RESIDUALS_DN_CORRELATION_V7_4.md | 8-15 |
| C3.2 | d(n) = distance from n(A) to nearest allowed 2^a × 3^b value | [Der] | V7.4/07_RESIDUALS_DN_CORRELATION_V7_4.md | 18-25 |
| C3.3 | Zone [37, 47] contains 11 consecutive forbidden integers | [Der] | V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | 17-29 |

### 3.2 Regression Results

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C3.4 | V7.4 M2: g = -0.31 ± 0.11, p = 0.006, 95% CI [-0.53, -0.09] | [Der] | V7.4/06_GN_FIT_V7_4.md | 88, 97-103 |
| C3.5 | V7.8 M2: g = -1.64 ± 0.14, p < 0.001, R² = 0.9805 | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 68-70 |
| C3.6 | V7.8 M7: g = -1.71 ± 0.47, p < 0.001, 4.2% change from M2 | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 168, 183 |
| C3.7 | GN baseline (M0): R² = 0.9522 (V7.8) | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 35 |
| C3.8 | Adding d(n) improves AIC by 88.7 units (M2 vs M0) | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 213 |

### 3.3 Sign Resolution

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C3.9 | Negative g means higher d(n) → shorter half-life (faster decay) | [Der] | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 14-15 |
| C3.10 | Test T3: Additive model (prefactor) wins over multiplicative (barrier) by ΔAIC = 3.4 | [Der] | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 138-149 |
| C3.11 | Most consistent interpretation: frustration → S_α enhancement | [I] | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 209-216 |
| C3.12 | Standard rate: λ = ν × P_tunnel × S_α | [Der] | V7.7/04_PREFACTOR_MECHANISM_MODEL.md | 13-21 |
| C3.13 | Physical picture: frustration → enhanced surface dynamics → easier α preformation | [P] | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 180-186 |

### 3.4 Robustness Tests

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C3.14 | Cross-validation: d(n) term improves out-of-sample prediction | [Der] | V7.5/04_CV_PREDICTIVE_GAIN.md | 15-30 |
| C3.15 | Permutation test: p_perm < 0.001 | [Der] | V7.5/05_PERMUTATION_TEST.md | 20-35 |
| C3.16 | Huber robust regression: g stable within 10% | [Der] | V7.5/06_ROBUST_REGRESSION.md | 25-40 |
| C3.17 | Deformation proxy absorbed by d(n): p(proxy_deform) = 0.67 in M5 | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 127, 131 |
| C3.18 | S_α proxy marginally significant with d(n): p = 0.05 in M6 | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 148, 152 |
| C3.19 | d(n) coefficient stable: 4.2% change from M2 to M7 | [Der] | V7.8/07_FIT_RESULTS_V7_8.md | 196 |

### 3.5 Interpretation

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C3.20 | d(n) captures variance beyond standard deformation and S_α proxies | [I] | V7.8/07_FIT_RESULTS_V7_8.md | 232 |
| C3.21 | d(n) is not simply a deformation proxy | [Der] | V7.8/08_MEDIATION_AND_INTERPRETATION.md | 30-33 |
| C3.22 | Correlation, not causation: causal pathway still hypothetical | [P] | V7.8/08_MEDIATION_AND_INTERPRETATION.md | 141 |
| C3.23 | Crystal defect analogy: defects enhance dynamics | [P] | V7.7/06_CRYSTAL_DEFECT_ANALOGY.md | 20-40 |

---

## Section 4: Falsification Framework

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C4.1 | Tests passed: robust regression, permutation, CV, deformation control | [Der] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 199-204 |
| C4.2 | Remaining tests: independent S_α, causation, superheavy | [Open] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 203-206 |
| C4.3 | Path to [Der]: 4/7 complete → Strong [P], approaching [I] | [I] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 207 |

---

## Section 5: Open Questions

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| C5.1 | K2 (experimental S_α): HIGH priority | [Open] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 41-51 |
| C5.2 | K10 (causation mechanism): HIGH priority | [Open] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 140-149 |
| C5.3 | K1 (true β₂ deformation): partially resolved | [Open] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 27-37 |
| C5.4 | K12 (collinearity diagnostics): MEDIUM priority | [Open] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 164-171 |

---

## Appendix: Forbidden Alternatives

| ID | Claim | Tag | Source | Lines |
|----|-------|-----|--------|-------|
| CA.1 | n = 42 has maximum frustration (equidistant from 36 and 48) | [I] | V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | 24, 31 |
| CA.2 | Mechanism matrix: M1 (domain) primary for n = 37, 38, 39, 42 | [P] | V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | 37-48 |
| CA.3 | Mechanism matrix: M3 (α-cluster) primary for n = 40, 44, 45 | [P] | V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | 37-48 |
| CA.4 | Mechanism matrix: M6 (core-mantle) primary for n = 46, 47 | [P] | V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | 37-48 |

---

## Summary Statistics

| Epistemic Tag | Count |
|---------------|-------|
| [Der] | 21 |
| [I] | 6 |
| [P] | 11 |
| [Open] | 4 |
| **Total** | **42** |

---

## Verification Notes

1. **V7.4 vs V7.8 g values**: Different because V7.8 uses different d(n) scaling (direct coordination distance vs normalized). Both are correct for their respective analyses.

2. **R² discrepancy**: Abstract says 0.9941, V7.8 M7 gives 0.9812. The 0.9941 may be from earlier version or different model specification. Flag for review.

3. **All line ranges verified**: Each source file was read and line numbers confirmed during session.

