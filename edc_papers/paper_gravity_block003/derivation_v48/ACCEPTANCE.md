# P49 / Derivation v48: Acceptance Criteria

## AC-P49-1: Only derivation_v48/ + PAPERS_INDEX modified ✓

- [x] derivation_v48/ created
- [x] PAPERS_INDEX.md updated
- [x] No other directories modified

## AC-P49-2: PDF builds, no undefined refs ✓

- [x] main.pdf builds successfully
- [x] 0 undefined references
- [x] 0 private paths in document

## AC-P49-3: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥26 | 27 |
| Equations | ≥170 | 333 |
| Labels | ≥240 | 297 |

## AC-P49-4: Hash-Lock Check ✓

- [x] v45 hash verified: `a80b3886903152d3`
- [x] v46 hash verified: `2742edea37e863ac`
- [x] v47 hash verified: `7a9682f333d5349e`
- [x] Hash checks in recompute.py

## AC-P49-5: PS Canonical Lock ✓

- [x] PS track explicitly locked
- [x] Track switching forbidden
- [x] Lock assertion in document

## AC-P49-6: Forbidden Inputs Gate ✓

- [x] grep-based scan implemented
- [x] Semantic gate in recompute.py
- [x] No forbidden tokens in formulas
- [x] Listings-only exemption for documentation

## AC-P49-7: Zero-Handwave Gate (HR-P48-N0) ✓

- [x] Factor ledger complete (5 factors)
- [x] All factors have derivation source
- [x] No "known from SU(5)" statements

## AC-P49-8: g_5 Fixing ✓

- [x] Route A (Tension): ADMISSIBLE
- [x] Route C (Cutoff): ADMISSIBLE
- [x] Route B (GUT): CONDITIONAL
- [x] Consistency check provided
- [x] Routes scoreboard in document

## AC-P49-9: L Determination ✓

- [x] Primary relation: L = M̄_Pl √(β/σ)
- [x] Dimension check verified
- [x] Forbidden-free: YES
- [x] Status: STRUCTURALLY_CLOSED

## AC-P49-10: KK Sum Convergence ✓

- [x] Zeta regulator: π²/6
- [x] Exponential/heat kernel: π²/6
- [x] Pauli-Villars: π²/6
- [x] Status: REGULATOR_INVARIANT

## AC-P49-11: BKT Sensitivity ✓

- [x] Parameterization: r_B (length)
- [x] Modified g_4: g_5²/(L+r_B)
- [x] Limit r_B→0: recovers standard
- [x] Bound: r_B/L < 0.01 for sub-2%
- [x] Status: BOUNDED_PERTURBATION

## AC-P49-12: Final G_F Expression ✓

- [x] Closure ladder (6 steps)
- [x] Final formula: G_F = (√2/48) g_5² L
- [x] Dimension check: [G_F] = -2 ✓
- [x] EDC-only inputs

## AC-P49-13: Dimension Sentinels ✓

| Quantity | Expected | Status |
|----------|----------|--------|
| g_5² | -1 | PASS |
| g_4² | 0 | PASS |
| L | -1 | PASS |
| m_n | 1 | PASS |
| G_F | -2 | PASS |
| r_B | -1 | PASS |
| σ | 4 | PASS |
| σ̃ | 0 | PASS |
| β | 0 | PASS |
| M_5 | 1 | PASS |
| Λ_5 | 1 | PASS |

## AC-P49-14: Verification Checks ✓

- [x] 49 checks implemented
- [x] All 49 checks PASS
- [x] Requirement: ≥45 checks

## AC-P49-15: Reviewer Traps ✓

18 traps documented (≥18 required):
1. Factor 1/8 in G_F sum
2. Missing √2 convention
3. KK mass: nπ/L not n/L
4. ζ(2) = π²/6 not π²/12
5. [g_5²] = -1 not 0
6. [σ] = 4 for brane tension
7. Regulator finite part invariant
8. BKT shifts g_4 not g_5
9. r_B→0 limit check
10. Overlap integral assumption
11. Route A vs C consistency
12. β dimensionless
13. σ̃ normalization
14. M_5³ relation
15. Forbidden inputs gate
16. PS canonical lock
17. Zero-handwave rule
18. Sum starts at n=1

## AC-P49-16: Export Filename ✓

- [x] `EDC_BLOCK003_DERIVATION_V48_PS_GF_NUMERICAL_CLOSURE_G5_L_KK_CONVERGENCE.pdf`

## AC-P49-17: PAPERS_INDEX Updated ✓

- [x] Row added for v48
- [x] Detailed entry included

## AC-P49-18: Closure Report ✓

- [x] Closure report in recompute.py output
- [x] CLOSED items listed
- [x] REMAINING OPEN (numeric only) listed
- [x] Forbidden status confirmed

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 49/49 checks passed
v45 Hash: `a80b3886903152d3`
v46 Hash: `2742edea37e863ac`
v47 Hash: `7a9682f333d5349e`
v48 Tables Hash: `c4f114aa0c662b66`
