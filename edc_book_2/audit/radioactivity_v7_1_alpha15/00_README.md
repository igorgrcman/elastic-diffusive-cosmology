# RADIOACTIVITY V7.1: α-EMITTER DATASET + G-N RESIDUAL ANALYSIS

**Version**: 7.1
**Created**: 2026-01-31
**Parent**: V7 BL Audit (audit/radioactivity_v7_bl/)
**Purpose**: Build dedicated α-emitter dataset and test d(n) correlation with G-N residuals

---

## Executive Summary

V7.1 addresses the "BLOCKED" status of the G-N + d(n) fit from V7 by:

1. **Building a 17-nuclide α-emitter dataset** (α17) with BL data from NNDC/NuDat
2. **Computing Geiger-Nuttall baseline fit** and extracting per-nuclide residuals
3. **Testing residual vs d(n) correlation** (Pearson + Spearman)
4. **Auditing spin-parity data** for the three mandatory branchpoints
5. **Proposing H-N48-01c** (conditional d(n) rule gated by selection rules)

**Key Result**: [To be filled after analysis]

---

## File Index

| File | Description |
|------|-------------|
| 00_README.md | This index |
| 01_SESSION_LOG.md | Work chronology |
| 02_SOURCES_AND_VERSIONS.md | BL source whitelist (inherited from V7) |
| 03_ALPHA15_DATASET.md | Human-readable dataset + coverage scorecard |
| 03_ALPHA15_DATASET.csv | Machine-readable dataset |
| 04_GN_FIT_AND_RESIDUALS.md | Baseline G-N fit + residual analysis |
| 05_DN_MAPPING_CHECK.md | n(A) and d(n) computation for α17 |
| 06_BRANCHPOINT_SPIN_PARITY_AUDIT.md | Jπ data + H-N48-01c proposal |
| 07_BULK_CRYSTAL_N48_WORKED_EXAMPLES.md | Three concrete crystal models |
| 08_SUMMARY_AND_NEXT_ACTIONS.md | Conclusions + recommendations |

---

## Dataset Coverage (α17)

| Constraint | Required | Achieved | Status |
|------------|----------|----------|--------|
| Bucket A (Actinides) | 7-9 | 9 | ✓ |
| Bucket B (Po/Rn/Ra) | 6-8 | 8 | ✓ |
| Qα < 6.5 MeV | ≥5 | 14 | ✓ |
| Qα 6.5-8.0 MeV | ≥5 | 2 | ✗ Gap |
| Qα > 8.0 MeV | ≥3 | 1 | ✗ Gap |
| t₁/₂ < 1s | ≥4 | 3 | ~ Near |
| t₁/₂ 1s-30d | ≥4 | 4 | ✓ |
| t₁/₂ > 1y | ≥4 | 10 | ✓ |
| Odd-A nuclides | ≥3 | 3 | ✓ |

**Note**: High-Qα bins underrepresented due to natural decay chain limitations.

---

## Repro Checklist

1. Verify BL data against NNDC/NuDat entries
2. Compute n(A) = 6.1 × A^(1/3) for each nuclide
3. Compute d(n) = |n(A) - n*| where n* ∈ {36, 48, 54}
4. Fit log₁₀(t₁/₂) vs Z/√Qα (baseline G-N)
5. Compute residuals and correlate with d(n)
6. Verify Jπ assignments for branchpoints against ENSDF

