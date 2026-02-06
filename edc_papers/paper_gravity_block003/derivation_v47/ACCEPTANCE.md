# P48 / Derivation v47: Acceptance Criteria

## AC-P48-1: Only derivation_v47/ + PAPERS_INDEX modified ✓

- [x] derivation_v47/ created
- [x] PAPERS_INDEX.md updated
- [x] No other directories modified

## AC-P48-2: PDF builds, no undefined refs ✓

- [x] main.pdf builds successfully
- [x] 0 undefined references
- [x] 0 private paths in document

## AC-P48-3: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥24 | 26 |
| Equations | ≥160 | 194 |
| Labels | ≥240 | 303 |

## AC-P48-4: SoT Hash-Lock Check ✓

- [x] v45 hash verified: `a80b3886903152d3`
- [x] v46 hash verified: `2742edea37e863ac`
- [x] Hash check in recompute.py
- [x] Mismatch detection implemented

## AC-P48-5: Trace Ledger Complete ✓

- [x] T_L trace: 1/2 (SU(2)_L fundamental)
- [x] T_R trace: 1/2 (SU(2)_R fundamental)
- [x] T_3R trace: 1/2 (component)
- [x] (B-L) trace: 4/3 (SU(4)_C fundamental)
- [x] Y trace: 5/6 (embedding sum)

## AC-P48-6: Hypercharge Matching Derived ✓

- [x] 10-step derivation in main.tex
- [x] Final formula: `1/g_Y^2 = 3/(5g_R^2) + 4/(5g_{B-L}^2)`
- [x] No handwaving

## AC-P48-7: Two-Route U(1) Mixing Verification ✓

- [x] Route 1: Current-sum method
- [x] Route 2: Kinetic diagonalization
- [x] Routes match: factor = 2/3
- [x] Verification box in document

## AC-P48-8: Weinberg Hook Formula ✓

- [x] Structural formula present
- [x] PS expression derived
- [x] No numerical values in formula
- [x] Prerequisites listed (6 items)

## AC-P48-9: G_F Readiness Map ✓

- [x] 10 items in readiness map
- [x] PS track marked as FIXED
- [x] Blocking items identified (3)
- [x] Integration with v34/v36/v29/v30

## AC-P48-10: Mass-Dimension Sentinels ✓

| Quantity | Expected | Status |
|----------|----------|--------|
| g_4 | 0 | PASS |
| g_5^2 | -1 | PASS |
| G_F | -2 | PASS |
| L | -1 | PASS |
| m_n | 1 | PASS |
| I_overlap | 0 | PASS |

## AC-P48-11: Forbidden Inputs Check ✓

- [x] No forbidden tokens in main.tex
- [x] No forbidden tokens in recompute.py
- [x] Identification gate passed

## AC-P48-12: Verification Checks ✓

- [x] 38 checks implemented
- [x] All 38 checks PASS
- [x] Requirement: ≥35 checks

## AC-P48-13: Reviewer Traps ✓

18 traps documented (≥18 required):
1. Trace normalization convention
2. (B-L) not canonically normalized
3. Factor of 1/2 in embedding
4. Cross-term vanishing
5. 3/5 and 4/5 factors (not SU(5))
6. Kinetic vs current matching
7. Weinberg angle at matching scale
8. LR symmetry assumption
9. g_5 dimension
10. g_4 from g_5
11. KK mass spectrum
12. G_F sum convergence
13. Overlap integral normalization
14. Brane kinetic terms
15. PS vs SU(5) normalization
16. Two U(1) mixing
17. Trace in which rep
18. No numerical Weinberg angle

## AC-P48-14: PS Coupling Dictionary ✓

- [x] 5 couplings defined
- [x] g_L, g_R, g_{B-L}, g_Y, g_4

## AC-P48-15: Export Filename ✓

- [x] `EDC_BLOCK003_DERIVATION_V47_PS_COUPLING_MATCHING_WEINBERG_HOOK_GF_READINESS.pdf`

## AC-P48-16: PAPERS_INDEX Updated ✓

- [x] Row added for v47
- [x] Detailed entry included

## AC-P48-17: Zero-Handwave Compliance (HR-P48-N0) ✓

- [x] All factors derived from traces
- [x] No "known from SU(5)" statements
- [x] No "by convention" without proof
- [x] Complete factor ledger in document

## AC-P48-18: PS Canonical Lock ✓

- [x] PS track marked as canonical
- [x] v46 selection referenced
- [x] Lock status documented

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 38/38 checks passed
v45 Hash: `a80b3886903152d3`
v46 Hash: `2742edea37e863ac`
v47 Tables Hash: `7a9682f333d5349e`
