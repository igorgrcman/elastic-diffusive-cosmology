# P47 / Derivation v46: Acceptance Criteria

## AC-P47-1: Only derivation_v46/ + PAPERS_INDEX modified ✓

- [x] derivation_v46/ created
- [x] PAPERS_INDEX.md updated
- [x] No other directories modified

## AC-P47-2: PDF builds, no undefined refs ✓

- [x] main.pdf builds successfully
- [x] 0 undefined references
- [x] 0 private paths in document

## AC-P47-3: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥26 | 26 |
| Equations | ≥160 | 228 |
| Labels | ≥240 | 350 |

## AC-P47-4: SoT Hash-Lock Check ✓

- [x] v45 hash verified: `a80b3886903152d3`
- [x] Hash check in recompute.py
- [x] Mismatch detection implemented

## AC-P47-5: Stage 0 Hard Gates ✓

- [x] G0: Forbidden inputs check
- [x] G1: Anomaly verification (all 6 + Witten)
- [x] G2: Hash-lock verification
- [x] Gate results tabled (T_sel_1)

## AC-P47-6: Stage 1 Admissibility ✓

- [x] PASS > CONDITIONAL ordering
- [x] AC-P47-17: PASS excludes CONDITIONAL
- [x] All 4 tracks classified
- [x] Results: SO(10)=PASS, PS=PASS, SU5=COND, E6=COND

## AC-P47-7: Stage 2 ΔE_vac^finite ✓

- [x] Computed from SoT components
- [x] BC_ref = "all-NN" declared
- [x] Regulator invariance noted (v37)
- [x] Score formula: (n_gauge_mix - n_gauge_NN) - 4*(n_ferm_mix - n_ferm_NN)
- [x] Results: PS=25, SO10=49, SU5=32, E6=82

## AC-P47-8: Stage 3 Burden Metric ✓

- [x] B = N_mech + N_params + N_tunings
- [x] Computed from mechanism dictionary
- [x] No prose-only definitions
- [x] Results: SO10=0, PS=1, SU5=5, E6=11

## AC-P47-9: Stage 4 Hook Score ✓

- [x] H computed per track
- [x] Hook catalog with prerequisites
- [x] Results: SU5=7, SO10=8, PS=8, E6=10

## AC-P47-10: Lexicographic Decision ✓

- [x] Scoring vector defined (8 components)
- [x] Comparison order: S0 > S1 > S2 > S3 > S4 > T1 > T2 > T3
- [x] T_sel_5 table produced
- [x] Winner: Pati-Salam at Stage 2

## AC-P47-11: Tie-Breakers ✓

- [x] T1: dim(G) implemented
- [x] T2: rank drop implemented
- [x] T3: exotic count implemented
- [x] T4: UNRESOLVED with criterion list

(Tie-breakers not reached; decision at Stage 2)

## AC-P47-12: Verification Checks ✓

- [x] 55 checks implemented
- [x] All 55 checks PASS
- [x] Requirement: ≥45 checks

## AC-P47-13: Reviewer Traps ✓

18 traps documented (≥18 required):
1. Vacuum energy absolute value
2. Regulator dependence
3. Weyl vs Dirac counting
4. BC to zero-mode mistakes
5. Hidden tuning in brane mass
6. Hosotani VEV assumption
7. PASS vs anomaly-free confusion
8. Stage ordering matters
9. Lexicographic vs weighted sum
10. Hash collision probability
11. Tie-breaker scope
12. UNRESOLVED is valid
13. Mechanism dictionary completeness
14. Fraction arithmetic precision
15. Score sign convention
16. Rank drop interpretation
17. Generator counting
18. Hard gate vs soft filter

## AC-P47-14: Inputs Used Table ✓

All inputs from SoT:
- SoT_TRACKS (v45)
- BC counts (gauge, fermion)
- Hypercharges (exact fractions)
- Hash reference

**No forbidden inputs used.**

## AC-P47-15: Export Filename ✓

- [x] `EDC_BLOCK003_DERIVATION_V46_NO_ESCAPE_TRACK_SELECTOR.pdf`

## AC-P47-16: PAPERS_INDEX Updated ✓

- [x] Row added for v46
- [x] Detailed entry included

## AC-P47-17: PASS Excludes CONDITIONAL ✓

- [x] Hard rule implemented
- [x] Applied in selection: SU5 and E6 excluded
- [x] Only PASS tracks (SO10, PS) considered

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 55/55 checks passed
v45 Hash: `a80b3886903152d3`
v46 Tables Hash: `2742edea37e863ac`
Selected Track: Pati-Salam (SELECTED at Stage 2)
