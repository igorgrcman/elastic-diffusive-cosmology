# DATA REQUESTS V5

**Created**: 2026-01-31
**Purpose**: Nuclear data needed for verification
**Status**: NO WEBFETCH — all marked [BL:SOURCE_TBD]
**Inherits**: V4 DATA_REQUESTS

---

## Overview

All nuclear data in V5 chain files marked [BL:SOURCE_TBD].
This file catalogs required data for future ingestion.

---

## Category A: Branching Ratios (Priority HIGH)

### Key Branch Points

| Nuclide | Chain | α% | β⁻% | Other | Priority |
|---------|-------|----|-----|-------|----------|
| ²¹²Bi | Th-232 | ~36% | ~64% | - | HIGH |
| ²¹¹Bi | U-235 | ~99.7% | ~0.3% | - | HIGH |
| ²²⁷Ac | U-235 | ~1.4% | ~98.6% | - | HIGH |
| ²¹⁴Bi | U-238 | ~0.02% | ~99.98% | - | MEDIUM |
| ²¹⁸Po | U-238 | ~99.98% | ~0.02% | - | MEDIUM |
| ²¹⁸At | - | ? | ? | EC? | LOW |
| ²¹⁹At | - | ? | ? | EC? | LOW |

**Total**: 7 branching ratios needed

---

## Category B: Half-Lives (Priority HIGH)

### U-238 Chain (14 nuclides)

| Nuclide | A | Status | Priority |
|---------|---|--------|----------|
| ²³⁸U | 238 | [BL:SOURCE_TBD] | HIGH |
| ²³⁴Th | 234 | [BL:SOURCE_TBD] | HIGH |
| ²³⁴Pa | 234 | [BL:SOURCE_TBD] | HIGH |
| ²³⁴U | 234 | [BL:SOURCE_TBD] | HIGH |
| ²³⁰Th | 230 | [BL:SOURCE_TBD] | HIGH |
| ²²⁶Ra | 226 | [BL:SOURCE_TBD] | HIGH |
| ²²²Rn | 222 | [BL:SOURCE_TBD] | HIGH |
| ²¹⁸Po | 218 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁴Pb | 214 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁴Bi | 214 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁴Po | 214 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁰Pb | 210 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁰Bi | 210 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁰Po | 210 | [BL:SOURCE_TBD] | HIGH |

### Th-232 Chain (10 nuclides)

| Nuclide | A | Status | Priority |
|---------|---|--------|----------|
| ²³²Th | 232 | [BL:SOURCE_TBD] | HIGH |
| ²²⁸Ra | 228 | [BL:SOURCE_TBD] | MEDIUM |
| ²²⁸Ac | 228 | [BL:SOURCE_TBD] | MEDIUM |
| ²²⁸Th | 228 | [BL:SOURCE_TBD] | MEDIUM |
| ²²⁴Ra | 224 | [BL:SOURCE_TBD] | MEDIUM |
| ²²⁰Rn | 220 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁶Po | 216 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹²Pb | 212 | [BL:SOURCE_TBD] | HIGH |
| ²¹²Bi | 212 | [BL:SOURCE_TBD] | HIGH |
| ²¹²Po | 212 | [BL:SOURCE_TBD] | MEDIUM |

### U-235 Chain (11 nuclides)

| Nuclide | A | Status | Priority |
|---------|---|--------|----------|
| ²³⁵U | 235 | [BL:SOURCE_TBD] | HIGH |
| ²³¹Th | 231 | [BL:SOURCE_TBD] | MEDIUM |
| ²³¹Pa | 231 | [BL:SOURCE_TBD] | MEDIUM |
| ²²⁷Ac | 227 | [BL:SOURCE_TBD] | HIGH |
| ²²⁷Th | 227 | [BL:SOURCE_TBD] | MEDIUM |
| ²²³Fr | 223 | [BL:SOURCE_TBD] | MEDIUM |
| ²²³Ra | 223 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁹Rn | 219 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹⁵Po | 215 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹¹Pb | 211 | [BL:SOURCE_TBD] | MEDIUM |
| ²¹¹Bi | 211 | [BL:SOURCE_TBD] | HIGH |

---

## Category C: Q-Values (Priority MEDIUM)

### α-Decay Q-Values

| Decay | Status | Priority |
|-------|--------|----------|
| ²³⁸U → ²³⁴Th | [BL:SOURCE_TBD] | HIGH |
| ²³⁴U → ²³⁰Th | [BL:SOURCE_TBD] | HIGH |
| ²³⁰Th → ²²⁶Ra | [BL:SOURCE_TBD] | HIGH |
| ²²⁶Ra → ²²²Rn | [BL:SOURCE_TBD] | HIGH |
| ²²²Rn → ²¹⁸Po | [BL:SOURCE_TBD] | MEDIUM |
| (all α-decays) | [BL:SOURCE_TBD] | MEDIUM |

**Total**: ~21 α-decay Q-values needed

### β-Decay Q-Values

| Decay | Status | Priority |
|-------|--------|----------|
| ²³⁴Th → ²³⁴Pa | [BL:SOURCE_TBD] | MEDIUM |
| ²³⁴Pa → ²³⁴U | [BL:SOURCE_TBD] | MEDIUM |
| (all β-decays) | [BL:SOURCE_TBD] | MEDIUM |

**Total**: ~14 β-decay Q-values needed

---

## Category D: Physical Constants

| Parameter | Purpose | Value | Status |
|-----------|---------|-------|--------|
| ρ₀ | Nuclear saturation | 0.16 fm⁻³ | [BL:literature] |
| r₀ | Radius constant | 1.2-1.3 fm | [BL:literature] |
| σ | Surface tension | 8.82 MeV/fm² | [DN-024] |
| B.E.(α) | α-binding | 28.3 MeV | [BL:literature] |

---

## Minimum Viable Dataset

For H1-H5 hypothesis testing:

1. **Branching ratios for 4 key nuclides**: ²¹²Bi, ²¹¹Bi, ²²⁷Ac, ²¹⁴Bi
2. **Q_α for 10 actinide α-emitters**
3. **t₁/₂ for same 10 emitters**

**Estimated minimum**: 24 data points

---

## Grouped by Chain

### U-238 Chain Data
- 14 half-lives
- 8 α Q-values
- 6 β Q-values
- 2 branching ratios

### Th-232 Chain Data
- 10 half-lives
- 6 α Q-values
- 4 β Q-values
- 1 branching ratio (²¹²Bi)

### U-235 Chain Data
- 11 half-lives
- 7 α Q-values
- 4 β Q-values
- 2 branching ratios (²²⁷Ac, ²¹¹Bi)

---

## Data Sources (If Approved)

| Source | URL | Access |
|--------|-----|--------|
| NNDC | https://www.nndc.bnl.gov/ | Public |
| IAEA NDS | https://www-nds.iaea.org/ | Public |
| ENSDF | https://www.nndc.bnl.gov/ensdf/ | Public |
| AME2020 | https://www-nds.iaea.org/amdc/ | Public |
| NUBASE2020 | - | Public |

---

## Ingestion Priority

1. **Phase 1**: Branching ratios (4-7 values) — enables H1-H5 testing
2. **Phase 2**: Q_α values (10-21 values) — enables G-N verification
3. **Phase 3**: t₁/₂ values (35 values) — enables lifetime predictions
4. **Phase 4**: Full dataset (~78 values) — complete verification

---

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Branching ratios | 7 | [BL:SOURCE_TBD] |
| Half-lives | 35 | [BL:SOURCE_TBD] |
| Q-values | ~35 | [BL:SOURCE_TBD] |
| Constants | 4 | Verify from literature |
| **Total** | **~81** | |

---

## Current Status

**NO WEBFETCH PERFORMED**
**Awaiting Igor approval for data ingestion**
