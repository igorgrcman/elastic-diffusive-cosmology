# P50 / Derivation v49: Acceptance Criteria

## AC-P50-1: Only derivation_v49/ + PAPERS_INDEX modified ✓

- [x] derivation_v49/ created
- [x] PAPERS_INDEX.md updated
- [x] No other directories modified

## AC-P50-2: PDF builds, no undefined refs ✓

- [x] main.pdf builds successfully
- [x] 0 undefined references
- [x] 0 private paths in document

## AC-P50-3: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥26 | 26 |
| Equations | ≥170 | 362 |
| Labels | ≥280 | 301 |

## AC-P50-4: Hash-Lock Check ✓

- [x] v45 hash verified: `a80b3886903152d3`
- [x] v46 hash verified: `2742edea37e863ac`
- [x] v47 hash verified: `7a9682f333d5349e`
- [x] v48 hash verified: `c4f114aa0c662b66`
- [x] Hash checks in recompute.py

## AC-P50-5: PS Canonical Lock ✓

- [x] PS track explicitly locked
- [x] Track switching forbidden
- [x] Lock assertion in document

## AC-P50-6: Forbidden Inputs Gate ✓

- [x] grep-based scan implemented
- [x] Semantic gate in recompute.py
- [x] No forbidden tokens in formulas
- [x] Documentation exemption handled

## AC-P50-7: Zero-Handwave Gate (HR-P48-N0) ✓

- [x] Trace ledger complete
- [x] All coefficients derived (3/5, 4/5)
- [x] No "known from GUT" statements

## AC-P50-8: Ω1 Scale-Derived ✓

- [x] μ_* = π/L (derived from geometry)
- [x] No experimental scale used
- [x] Proposition in document
- [x] Check in recompute.py

## AC-P50-9: Ω2 Scheme-Invariant ✓

- [x] Two routes: T1 (zeta) and T2 (truncated)
- [x] Agreement verified
- [x] Lemma in document
- [x] Difference < 10⁻¹⁰

## AC-P50-10: Ω3 No-Alpha Gate ✓

- [x] No α_EM, α_em used
- [x] No fine structure constant
- [x] No electric charge e
- [x] Pattern scan passes

## AC-P50-11: Ω4 BKT-Bounded ✓

- [x] Parameterization: r_i (length)
- [x] Bound: |δ(sin²θ_W)| ≤ C_BKT·max(r_i/L)
- [x] C_BKT ≤ 2
- [x] Monte Carlo test: 100% in bound
- [x] Proposition in document

## AC-P50-12: Final Expression ✓

- [x] Closure formula: sin²θ_W = 1/(1 + (L+r_L)(3/(5(L+r_R)) + 4/(5(L+r_{B-L}))))
- [x] Simplified: 5/12 at unified point
- [x] Dimension check: [sin²θ_W] = 0 ✓
- [x] EDC-only inputs

## AC-P50-13: Dimension Sentinels ✓

| Quantity | Expected | Status |
|----------|----------|--------|
| g_L, g_R, g_{B-L}, g_Y | 0 | PASS |
| g_5² | -1 | PASS |
| L | -1 | PASS |
| μ, μ_KK | 1 | PASS |
| b_i | 0 | PASS |
| r_i | -1 | PASS |
| sin²θ_W | 0 | PASS |

## AC-P50-14: Verification Checks ✓

- [x] 55 checks implemented
- [x] All 55 checks PASS
- [x] Requirement: ≥55 checks

## AC-P50-15: Reviewer Traps ✓

20 traps documented (≥20 required):
1. Wrong PS hypercharge mixing (3/5, 4/5 not 1/2, 1/2)
2. Normalization drift under diagonalization
3. Missing factor in beta functions
4. μ_KK = π/L not 1/L
5. Using EM coupling indirectly
6. Hidden experimental scale in μ_*
7. BKT inconsistent treatment
8. Regulator-dependent finite piece
9. Gauge vs fermion thresholds
10. Double-counting zero modes
11. Wrong sign in RG
12. U(1)_{B-L} normalization
13. Assuming g_L = g_R always
14. Forgetting g_{B-L} running
15. Using measured Weinberg angle
16. 5D vs 4D coupling confusion
17. BKT shift formula
18. Threshold not relative
19. Two-loop without [OPEN]
20. Scale chosen to match experiment

## AC-P50-16: Export Filename ✓

- [x] `EDC_BLOCK003_DERIVATION_V49_PS_WEINBERG_ANGLE_NUMERICAL_CLOSURE.pdf`

## AC-P50-17: PAPERS_INDEX Updated ✓

- [x] Row added for v49
- [x] Detailed entry included

## AC-P50-18: Dependency DAG ✓

- [x] DAG is acyclic
- [x] Root inputs: σ, β, M̄_Pl, c_A/Λ_5, r_i
- [x] No circular dependencies
- [x] Audit in document

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 55/55 checks passed
v45 Hash: `a80b3886903152d3`
v46 Hash: `2742edea37e863ac`
v47 Hash: `7a9682f333d5349e`
v48 Hash: `c4f114aa0c662b66`
v49 Tables Hash: `81010ef2faedcefd`
