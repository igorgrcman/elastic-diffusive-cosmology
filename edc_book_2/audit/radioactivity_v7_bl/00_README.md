# RADIOACTIVITY V7 BL AUDIT

**Version**: 7.2
**Created**: 2026-01-31
**Purpose**: BL-grounded testing of M-topology coordination hypotheses
**Status**: COMPLETE — H-N48-01 partially falsified (1/3)

---

## Executive Summary

This audit tested the **H-N48-01 branching hypothesis**:
> At branch points, the channel that reduces d(n) is preferred.

**Result**: 1/3 success (33%). The hypothesis is **partially falsified**.

The coordination distance d(n) does NOT reliably predict branching ratios. However, the monotonic decrease of d(n) along decay chains WAS confirmed (3/3 chains).

---

## File Index

| File | Description | Status |
|------|-------------|--------|
| 00_README.md | This index file | Complete |
| 00_SOURCES_AND_VERSIONS.md | BL source whitelist and version control | Complete |
| 01_SESSION_LOG.md | Chronological work log | Complete |
| 02_BL_TABLES.md | Raw BL data from NNDC/ENSDF | Complete |
| 03_NA_DN_TABLES.md | n(A) and d(n) calculations for all chain nuclides | Complete |
| 03A_CHAIN_STEP_LISTS.md | Step-by-step chain decomposition | Complete |
| 04_BRANCHPOINT_SCORECARD.md | **KEY**: H-N48-01 test results | Complete |
| 04A_BRANCHPOINT_RAW_BL.md | Authoritative BL data for 3 branchpoints | Complete |
| 05_HYPOTHESES_UPDATE.md | Status changes for H-N48-01/02/03 | Complete |
| 06_FIT_RESULTS.md | G-N + d(n) regression (BLOCKED) | Complete |
| 08_BULK_CRYSTAL_MODEL_V7.md | Crystal analogy with falsification | Complete |
| 10_DRAFT_BOOK2_SECTION_V7.md | Reader-ready summary for Book 2 | Complete |
| DATA_GAPS_V7.md | Missing BL data documentation | Complete |
| FINAL_SUMMARY.md | Final conclusions and next steps | Complete |

---

## Scope Lock (V7.2)

### Three Canonical Chains
- **U-238 Series**: ²³⁸U → ²⁰⁶Pb (14 steps, 8α + 6β⁻)
- **Th-232 Series**: ²³²Th → ²⁰⁸Pb (10 steps, 6α + 4β⁻)
- **U-235 Series**: ²³⁵U → ²⁰⁷Pb (11 steps, 7α + 4β⁻)

### Three Mandatory Branchpoints
1. **²¹²Bi** (Th-232): α=35.94%, β⁻=64.06%
2. **²²⁷Ac** (U-235): α=1.38%, β⁻=98.62%
3. **²¹¹Bi** (U-235): α=99.724%, β⁻=0.276%

### Model Family Lock
- **M-A**: n(A) = 6.1 × A^(1/3) — V6 default
- **M-B**: n(A) = 7.2 × A^(1/3) — Alternative
- **M-C**: n(A) = 6.08 × A^(1/3) — Calibrated to n(208)=36

---

## BL Source Whitelist

| Source | Authority | URL |
|--------|-----------|-----|
| NNDC/ENSDF | Primary | nndc.bnl.gov |
| NuDat 3.0 | Derived | nndc.bnl.gov/nudat3 |
| NUBASE2020 | Masses/t₁/₂ | DOI:10.1088/1674-1137/abddae |
| AME2020 | Atomic masses | DOI:10.1088/1674-1137/abddaf |
| IAEA LiveChart | Cross-check | www-nds.iaea.org/livechart |

---

## Key Results

### Confirmed [I]
1. **H-N48-02**: d(n) decreases monotonically along all 3 chains
2. **H-N48-03**: Stable endpoints (Pb isotopes) are at d ≈ 0

### Falsified or Partially Falsified
1. **H-N48-01**: d(n) does NOT predict branching (1/3 = 33%)
2. **H-N48-01b**: Q-threshold gating does NOT rescue H-N48-01

### Open
1. **H-N48-04**: n=48 target for A > 350 (no data)
2. **H-N48-05**: Island ladder 36→48→54 (theoretical)
3. **H-N48-01c**: Conditional d(n) rule with spin-parity (untested)

---

## Epistemic Status Legend

| Tag | Meaning |
|-----|---------|
| [Der] | Mathematically derived from axioms |
| [I] | Inferred from data with high confidence |
| [P] | Proposed; testable but not yet tested |
| [Cal] | Calibrated parameter |
| [BL] | Baseline data from authoritative source |
| [Open] | Unresolved question |

---

## How to Use This Audit

1. **For Book 2 integration**: See `10_DRAFT_BOOK2_SECTION_V7.md`
2. **For raw BL data**: See `02_BL_TABLES.md` and `04A_BRANCHPOINT_RAW_BL.md`
3. **For hypothesis testing**: See `04_BRANCHPOINT_SCORECARD.md` and `05_HYPOTHESES_UPDATE.md`
4. **For future work**: See `DATA_GAPS_V7.md` and `FINAL_SUMMARY.md`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V7.0 | 2026-01-31 | Initial BL-grounded audit |
| V7.1 | 2026-01-31 | Addendum: Scope lock on 3 chains |
| V7.2 | 2026-01-31 | Addendum: BL source whitelist |

