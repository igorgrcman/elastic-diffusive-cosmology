# P52 / Derivation v51: Acceptance Criteria

## AC-P52-1: Scope-only ✓

- [x] Only derivation_v51/ created
- [x] PAPERS_INDEX.md to be updated
- [x] No other directories modified

## AC-P52-2: FROZEN unchanged ✓

- [x] Parent spine files not modified
- [x] Previous derivations unchanged

## AC-P52-3: Build ✓

- [x] main.pdf builds successfully
- [x] 0 undefined references
- [x] 0 private paths in document

## AC-P52-4: Size ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥24 | 27 |
| Equations | ≥180 | 195 |
| Labels | ≥240 | 346 |

## AC-P52-5: recompute.py ✓

- [x] 52 checks implemented
- [x] All 52 checks PASS
- [x] Requirement: ≥45 checks

## AC-P52-6: Forbidden gate ✓

- [x] Automated grep scan in recompute.py
- [x] No forbidden tokens in main.tex
- [x] No forbidden tokens in REPORT.md

Evidence:
```
[PASS] F1: Forbidden tokens in tex: CLEAN
[PASS] F2: Forbidden tokens in python: CLEAN
```

## AC-P52-LOG-1: Dimensionless Log Invariance ✓

- [x] Log scan implemented
- [x] 103 logs scanned
- [x] 0 "bad log" flags

Evidence:
```
[PASS] LOG1: Dimensionless log arguments: ALL VALID (103 logs)
```

## AC-P52-LOG-2: Single Reference Scale ✓

- [x] Exactly 1 boxed μ_* definition
- [x] All logs reference μ_* or explicit ratios

Evidence:
```
[PASS] LOG2: Single mu_* definition (boxed): COUNT: 1
```

## AC-P52-LOG-3: Unit-change invariance ✓

- [x] Tested with S = 10^{-9}, 10^3, 10^6, 10^9, 10^{12}
- [x] Dimensionless outputs invariant (tolerance 1e-12)
- [x] Dimensional outputs scale correctly

Evidence:
```
[PASS] UI1: S=1e+03 invariants: INVARIANT
[PASS] UI2: S=1e+06 invariants: INVARIANT
[PASS] UI3: S=1e+09 invariants: INVARIANT
[PASS] UI4: S=1e+12 invariants: INVARIANT
[PASS] UI5: S=1e-09 invariants: INVARIANT
[PASS] UI6: L scales as 1/S: L' = L/S
[PASS] UI7: mu_* scales as S: mu' = S*mu
[PASS] UI8: sigma scales as S^4: sigma' = S^4*sigma
[PASS] UI9: G_F scales as 1/S^2: G_F' = G_F/S^2
```

## AC-P52-IN-1: Inputs used table ✓

- [x] Table in REPORT.md
- [x] Every numeric-valued symbol listed
- [x] Source and tag for each
- [x] NO forbidden anchors appear

## AC-P52-HASH-1: Hash lock ✓

- [x] v51 hash computed: `ed8fa089897b2d8c`
- [x] Hash chain verified (v45-v50)

## AC-P52-TRAPS-1: Reviewer traps ≥18 ✓

18 traps documented:
1. Writing ln(μ) without reference scale
2. Using ln(L) alone
3. Multiple μ_0 definitions
4. Forgetting [g_5²] = M^{-1}
5. Unit-dependent predictions
6. Using M_Z, M_W as inputs
7. Implicit GeV units
8. Wrong scaling: G_F → S·G_F
9. Treating β as dimensional
10. BKT logs: ln(r_i) instead of ln(r_i/L)
11. KK sum without regulator specification
12. Regulator-dependent finite parts
13. Two-loop without [OPEN] tag
14. Confusing μ_* = π/L vs μ_* = 1/L
15. Scale-dependent matching coefficients
16. Mixing 5D and 4D coupling dimensions
17. Using α_EM to fix g_Y
18. Implicit fine-tuning

## AC-P52-EXPORT-1: Export PDF filename ✓

- [x] `EDC_BLOCK003_DERIVATION_V51_LOG_HYGIENE_LOCK_UNIT_INVARIANCE.pdf`

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 52/52 checks passed

Hash Chain:
- v45: `a80b3886903152d3`
- v46: `2742edea37e863ac`
- v47: `7a9682f333d5349e`
- v48: `c4f114aa0c662b66`
- v49: `81010ef2faedcefd`
- v50: `cebf3e5baf0de863`
- v51: `ed8fa089897b2d8c`
