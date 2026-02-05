# P45 / Derivation v44: Acceptance Criteria

## AC-P45-1: SoT Lock Protocol ✓

- [x] SoT_FIELDS defined in recompute.py
- [x] All field data in single location
- [x] Exact rational arithmetic (Fraction class)
- [x] BC and zero-mode status explicit

## AC-P45-2: Auto-Generated Tables ✓

- [x] tables_generated.tex produced by generate_tables()
- [x] No manual number entry
- [x] Hash verification implemented
- [x] Hash: ea07022b108f0721

## AC-P45-3: All 6 Anomalies Computed ✓

- [x] SU(3)³ = 0
- [x] SU(2)²U(1) = 0
- [x] SU(3)²U(1) = 0
- [x] U(1)³ = 0
- [x] U(1)-gravitational = 0
- [x] Witten SU(2) parity = 0 mod 2

## AC-P45-4: Two-Route Verification ✓

- [x] U(1)³ verified by direct sum AND sector decomposition
- [x] SU(2)²U(1) verified by direct sum AND sector decomposition
- [x] Routes agree exactly (Fraction comparison)

## AC-P45-5: Forbidden Inputs Audit ✓

- [x] No M_Z (91.19 GeV)
- [x] No M_W (80.38 GeV)
- [x] No v_EW (246.2 GeV)
- [x] No α_EM (1/137)
- [x] No G_N (6.674×10⁻¹¹)
- [x] No ℓ_P (1.616×10⁻³⁵)

## AC-P45-6: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥24 | 30 |
| Equations | ≥140 | 155 |
| Labels | ≥180 | 242 |
| Checks | ≥25 | 26 |
| Reviewer traps | ≥14 | 16 |

## AC-P45-7: Documentation ✓

- [x] README.md created
- [x] REPORT.md created
- [x] ACCEPTANCE.md created
- [x] Export PDF named correctly

## AC-P45-8: Hash Lock Integrity ✓

- [x] tables_generated.tex hash matches regeneration
- [x] Manual edit detection working
- [x] Hash: ea07022b108f0721

## AC-P45-9: Cross-Validation ✓

- [x] Results match v43 (PS track)
- [x] Results match expected GUT track values
- [x] Quark + lepton partial sums cancel
- [x] Doublet + singlet partial sums cancel

## AC-P45-10: Reviewer Traps ✓

16 traps documented:
1. Hypercharge normalization c_Y = 5/3
2. Weyl vs Dirac multiplicity
3. Chirality BC mapping
4. Mixed BC → no zero-mode
5. LH vs RH sign convention
6. Charge conjugation flips Y
7. Witten SU(2) parity
8. Regulator invariance
9. No forbidden inputs audit
10. Color factor in doublets
11. SU(2) factor in triplets
12. Fraction arithmetic
13. Two-route verification
14. Generation independence
15. Hash lock compliance
16. SoT completeness

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 26/26 checks passed
Hash: ea07022b108f0721
