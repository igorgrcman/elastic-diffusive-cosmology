# DATA REQUESTS V4

**Created**: 2026-01-31
**Purpose**: Nuclear data needed for verification
**Status**: NO WEBFETCH — all marked [BL:SOURCE_TBD]

---

## Overview

All nuclear data in V4 chain files marked [BL:SOURCE_TBD].
This file catalogs required data for future ingestion.

---

## Category A: Half-Lives (t₁/₂)

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

## Category B: Q-Values (MeV)

### α-Decay Q-Values

| Decay | Status | Priority |
|-------|--------|----------|
| ²³⁸U → ²³⁴Th | [BL:SOURCE_TBD] | HIGH |
| ²³⁴U → ²³⁰Th | [BL:SOURCE_TBD] | HIGH |
| ²³⁰Th → ²²⁶Ra | [BL:SOURCE_TBD] | HIGH |
| ²²⁶Ra → ²²²Rn | [BL:SOURCE_TBD] | HIGH |
| ²²²Rn → ²¹⁸Po | [BL:SOURCE_TBD] | MEDIUM |
| ... (all α-decays) | [BL:SOURCE_TBD] | MEDIUM |

**Total**: ~21 α-decay Q-values needed

### β-Decay Q-Values

| Decay | Status | Priority |
|-------|--------|----------|
| ²³⁴Th → ²³⁴Pa | [BL:SOURCE_TBD] | MEDIUM |
| ²³⁴Pa → ²³⁴U | [BL:SOURCE_TBD] | MEDIUM |
| ... (all β-decays) | [BL:SOURCE_TBD] | MEDIUM |

**Total**: ~14 β-decay Q-values needed

---

## Category C: Branching Ratios

| Nuclide | Modes | Ratio | Status | Priority |
|---------|-------|-------|--------|----------|
| ²¹²Bi | β⁻/α | ~64:36 | [BL:SOURCE_TBD] | HIGH |
| ²¹¹Bi | α/β⁻ | ~99.7:0.3 | [BL:SOURCE_TBD] | HIGH |
| ²²⁷Ac | β⁻/α | ~98.6:1.4 | [BL:SOURCE_TBD] | HIGH |
| ²¹⁴Bi | β⁻/α | ~100:0 | [BL:SOURCE_TBD] | MEDIUM |

---

## Category D: Physical Constants

| Parameter | Purpose | Status | Priority |
|-----------|---------|--------|----------|
| ρ₀ | Nuclear saturation density | 0.16 fm⁻³ [literature] | Verify |
| r₀ | Nuclear radius constant | 1.2-1.3 fm [literature] | Verify |
| σ | Surface tension | 8.82 MeV/fm² [DN-024] | Verify |
| B.E.(α) | α-particle binding | 28.3 MeV [literature] | Verify |

---

## Minimum Viable Dataset

For initial G-N law verification:

1. **t₁/₂ for 10 actinide α-emitters** (U, Th, Pa, Ra)
2. **Q_α for same 10** (for G-N calculation)
3. **Branching ratios for 3 key nuclides** (²¹²Bi, ²¹¹Bi, ²²⁷Ac)

**Estimated**: ~26 data points minimum

---

## Data Sources (If Approved)

| Source | URL | Access |
|--------|-----|--------|
| NNDC | https://www.nndc.bnl.gov/ | Public |
| IAEA NDS | https://www-nds.iaea.org/ | Public |
| ENSDF | https://www.nndc.bnl.gov/ensdf/ | Public |
| AME2020 | https://www-nds.iaea.org/amdc/ | Public |

---

## Ingestion Options

### Option 1: Manual Lookup
- Igor looks up key values
- Enters into DATA_VALUES.md
- CC uses for calculations

### Option 2: WebFetch (Requires Approval)
- CC fetches from NNDC
- Parses and stores
- **Currently blocked by G1 guardrail**

### Option 3: Dataset File
- Igor provides nuclear_data.csv
- CC ingests and uses

---

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Half-lives | ~35 | [BL:SOURCE_TBD] |
| Q-values | ~35 | [BL:SOURCE_TBD] |
| Branching ratios | ~4 | [BL:SOURCE_TBD] |
| Constants | ~4 | Verify from literature |
| **Total** | **~78** | |

---

## Current Status

**NO WEBFETCH PERFORMED**
**Awaiting Igor approval for data ingestion**
