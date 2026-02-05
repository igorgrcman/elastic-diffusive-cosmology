# P46 / Derivation v45: Acceptance Criteria

## AC-P46-1: SoT Schema ✓

- [x] SoT_TRACKS defined with 4 tracks
- [x] Each track has: gauge_sector, matter_fields, exotics
- [x] Gauge sector: generator counts by BC class (NN/DD/mixed)
- [x] Matter sector: LH Weyl basis with BC, zero-mode, Y, reps
- [x] Exotics: decoupling mechanism specified
- [x] Epistemic tags per item

## AC-P46-2: Auto Tables ✓

8 tables auto-generated from Python:
- [x] T1: Track overview
- [x] T2: Field inventory
- [x] T3: Anomaly coefficients
- [x] T4: ΔE_vac ingredients
- [x] T5: Exotics and mass gating
- [x] T6: Track admissibility
- [x] T7: Detailed U(1)³
- [x] T8: Two-route verification

## AC-P46-3: Hash Lock ✓

- [x] Hash computed: `a80b3886903152d3`
- [x] Mismatch detection implemented
- [x] Tables regeneration verified deterministic

## AC-P46-4: Anomalies ✓

All 6 + Witten computed per track:

| Track | SU(3)³ | SU(2)²U(1) | SU(3)²U(1) | U(1)³ | grav | Witten |
|-------|--------|------------|------------|-------|------|--------|
| SU(5) | 0 | 0 | 0 | 0 | 0 | 0 |
| SO(10) | 0 | 0 | 0 | 0 | 0 | 0 |
| PS | 0 | 0 | 0 | 0 | 0 | 0 |
| E6 | 0 | 0 | 0 | 0 | 0 | 0 |

## AC-P46-5: Two-Route Verification ✓

- [x] U(1)³: direct sum vs sector grouping (all 4 tracks)
- [x] SU(2)²U(1): direct sum vs sector grouping (all 4 tracks)
- [x] All routes match exactly

## AC-P46-6: ΔE_vac^finite ✓

- [x] Computed inputs per track
- [x] BC_ref = "all-NN" declared
- [x] Regulator invariance noted (v37 protocol)
- [x] Score formula: (n_gauge_mixed - n_gauge_NN) - 4*(n_ferm_mixed - n_ferm_NN)

## AC-P46-7: Mass Gating ✓

- [x] Exotics list with decouple mechanism
- [x] Mechanisms: Mixed BC, Brane mass, Hosotani
- [x] PASS/CONDITIONAL table produced

| Track | Status | Reason |
|-------|--------|--------|
| SU(5) | CONDITIONAL | BRANE_MASS_TUNING |
| SO(10) | PASS | ALL_CRITERIA_MET |
| PS | PASS | ALL_CRITERIA_MET |
| E6 | CONDITIONAL | HOSOTANI_REQUIRED |

## AC-P46-8: Consistency Checks ✓

- [x] Zero-mode counts match SM survivors
- [x] Mixed BC → no zero-mode enforced (all tracks)
- [x] Total multiplicity = 15 per generation (all tracks)

## AC-P46-9: Forbidden Inputs ✓

- [x] No M_Z (91.19 GeV)
- [x] No M_W (80.38 GeV)
- [x] No v_EW (246.2 GeV)
- [x] No α_EM (1/137)
- [x] No G_N (6.674×10⁻¹¹)
- [x] No ℓ_P (1.616×10⁻³⁵)

## AC-P46-10: Reviewer Traps ✓

18 traps documented (≥16 required):
1. Hypercharge normalization c_Y = 5/3
2. Weyl vs Dirac multiplicity
3. Chirality BC mapping
4. Mixed BC → no zero-mode
5. LH vs RH sign convention
6. Charge conjugation flips Y
7. Witten SU(2) parity
8. Regulator invariance
9. Color factor in doublets
10. SU(2) factor in triplets
11. Fraction arithmetic
12. Two-route verification
13. Generation independence
14. Hash lock compliance
15. Exotic gating mechanism
16. Admissibility vs anomaly freedom
17. BC reference choice
18. Track-specific exotics

## AC-P46-11: Size Requirements ✓

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥28 | 28 |
| Equations | ≥160 | 192 |
| Labels | ≥220 | 291 |

## AC-P46-12: Verification Checks ✓

- [x] 56 checks implemented
- [x] All 56 checks PASS
- [x] Requirement: ≥30 checks

## AC-P46-13: Documentation ✓

- [x] README.md complete
- [x] REPORT.md complete
- [x] ACCEPTANCE.md complete
- [x] Reproduction instructions included

## AC-P46-14: Epistemic Ledger ✓

- [x] [D] Derived: anomaly calculations, BC projections
- [x] [Dc] Derived with convention: ΔE_vac, mass gating mechanisms
- [x] [P] Postulate: track definitions as starting point
- [x] [I] Identity: group theory formulas
- [x] [BL] Borrowed: GUT representations, anomaly polynomial

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

Date: February 2026
Verification: 56/56 checks passed
Hash: `a80b3886903152d3`
