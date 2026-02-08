# DATA REQUESTS: External Nuclear Data Needed

**Generated**: 2026-01-31
**Purpose**: List all external data required for verification
**Status**: NO WEB FETCH without Igor approval

---

## Overview

The decay chain skeletons and G-N law verification require nuclear data not present in mined sources.

---

## Request Categories

### Category A: Half-Lives (t₁/₂)

| Priority | Nuclide | Chain | Current Status | Source |
|----------|---------|-------|----------------|--------|
| HIGH | ²³⁸U | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³⁴Th | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³⁴Pa | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³⁴U | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³⁰Th | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁶Ra | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²²Rn | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁸Po | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁴Pb | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁴Bi | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁴Po | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁰Pb | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁰Bi | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁰Po | U-238 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³²Th | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁸Ra | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁸Ac | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁸Th | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁴Ra | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²²⁰Rn | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹⁶Po | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹²Pb | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹²Bi | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹²Po | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²⁰⁸Tl | Th-232 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²³⁵U | U-235 | [BL:SOURCE_TBD] | NNDC |
| HIGH | ... (remaining U-235 chain) | U-235 | [BL:SOURCE_TBD] | NNDC |

**Total**: ~45 nuclides across 3 chains

---

### Category B: Q-Values (Q_α, Q_β)

| Priority | Decay | From→To | Current Status | Source |
|----------|-------|---------|----------------|--------|
| HIGH | α | ²³⁸U→²³⁴Th | [BL:SOURCE_TBD] | NNDC |
| HIGH | α | ²³⁴U→²³⁰Th | [BL:SOURCE_TBD] | NNDC |
| HIGH | α | ²³⁰Th→²²⁶Ra | [BL:SOURCE_TBD] | NNDC |
| ... | ... | ... | ... | NNDC |

**Need**: All α-decay Q values for G-N law verification

---

### Category C: Branching Ratios

| Priority | Nuclide | Modes | Current Status | Source |
|----------|---------|-------|----------------|--------|
| HIGH | ²¹⁴Bi | α/β⁻ | [BL:SOURCE_TBD] | NNDC |
| HIGH | ²¹²Bi | α/β⁻ | 64%/36% (approx) | NNDC |
| HIGH | ²²⁷Ac | α/β⁻ | 1.4%/98.6% (approx) | NNDC |
| HIGH | ²¹¹Bi | α/β⁻ | 99.7%/0.3% (approx) | NNDC |

---

### Category D: Nuclear Density Data

| Priority | Parameter | Purpose | Source |
|----------|-----------|---------|--------|
| MEDIUM | ρ₀ | Saturation density | Literature |
| MEDIUM | r₀ | Nuclear radius constant | Literature |
| MEDIUM | n(A) formula | Coordination from density | DERIVED |

---

## Data Sources

| Source | URL | Access |
|--------|-----|--------|
| NNDC | https://www.nndc.bnl.gov/ | Public |
| IAEA NDS | https://www-nds.iaea.org/ | Public |
| ENSDF | https://www.nndc.bnl.gov/ensdf/ | Public |
| AME2020 | https://www-nds.iaea.org/amdc/ | Public |

---

## Ingestion Plan (If Approved)

### Option 1: Manual Lookup
- Igor manually looks up key values
- Enters into DATA_VALUES.md
- CC uses for calculations

### Option 2: WebFetch (Requires Approval)
- CC fetches from NNDC
- Parses and stores in structured format
- **Requires explicit Igor approval**

### Option 3: Dataset File
- Igor provides nuclear_data.csv or similar
- CC ingests and uses

---

## Minimum Viable Dataset

For initial verification, need at minimum:

1. **t₁/₂ for 10 actinide α-emitters** (for G-N fit verification)
2. **Q_α for same 10** (for G-N calculation)
3. **Branching ratios for 4 key nuclides** (for mode selection test)

Estimated: ~50 data points total

---

## Status

| Category | Count | Status |
|----------|-------|--------|
| Half-lives needed | ~45 | [BL:SOURCE_TBD] |
| Q-values needed | ~25 | [BL:SOURCE_TBD] |
| Branching ratios | ~4 | [BL:SOURCE_TBD] |
| Density parameters | ~3 | [BL:SOURCE_TBD] |

**No web fetch performed. Awaiting Igor approval.**
