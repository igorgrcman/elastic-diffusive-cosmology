# BL NUCLEAR DATA TABLES (V7)

**Created**: 2026-01-31
**Purpose**: Authoritative baseline data for 3 canonical chains
**Source**: NNDC/NuDat (S1/S2) per V7.2

---

## Chain Parents

| Nuclide | A | Z | t₁/₂ | Mode | BR(%) | Q (keV) | [BL:S#] |
|---------|---|---|------|------|-------|---------|---------|
| ²³⁸U | 238 | 92 | 4.468×10⁹ y | α | 100 | 4269.7 | [BL:S1] |
| ²³²Th | 232 | 90 | 1.40×10¹⁰ y | α | 100 | 4081.6 | [BL:S1] |
| ²³⁵U | 235 | 92 | 7.04×10⁸ y | α | 100 | 4678.2 | [BL:S1] |

---

## Key Branchpoint Nuclides (MANDATORY)

| Nuclide | A | Z | t₁/₂ | Mode | BR(%) | Q (keV) | [BL:S#] |
|---------|---|---|------|------|-------|---------|---------|
| ²¹²Bi | 212 | 83 | 60.55 min | β⁻ | 64.06±0.6 | 2251.5 | [BL:S1] |
| ²¹²Bi | 212 | 83 | 60.55 min | α | 35.94±0.6 | 6207.26 | [BL:S1] |
| ²²⁷Ac | 227 | 89 | 21.772 y | β⁻ | 98.62±0.36 | 44.8 | [BL:S1] |
| ²²⁷Ac | 227 | 89 | 21.772 y | α | 1.38±0.36 | 5042.19 | [BL:S1] |
| ²¹¹Bi | 211 | 83 | 2.14 min | α | 99.724±0.004 | 6750.3 | [BL:S1] |
| ²¹¹Bi | 211 | 83 | 2.14 min | β⁻ | 0.276±0.004 | 574 | [BL:S1] |

---

## Key Daughter Nuclides (from branchpoints)

| Nuclide | A | Z | t₁/₂ | Mode | BR(%) | Q (keV) | [BL:S#] |
|---------|---|---|------|------|-------|---------|---------|
| ²¹²Po | 212 | 84 | 294.3 ns | α | 100 | 8954.20 | [BL:S1] |
| ²⁰⁸Tl | 208 | 81 | 3.053 min | β⁻ | 100 | 4998.9 | [BL:S1] |

---

## Chain Endpoints (Stable)

| Nuclide | A | Z | Status | Chain |
|---------|---|---|--------|-------|
| ²⁰⁶Pb | 206 | 82 | STABLE | U-238 |
| ²⁰⁸Pb | 208 | 82 | STABLE | Th-232 |
| ²⁰⁷Pb | 207 | 82 | STABLE | U-235 |

---

## Data Gaps (Require Additional Fetch)

The following nuclides need BL data for complete chain coverage:

### U-238 Chain
| Nuclide | Fields Needed | Priority |
|---------|---------------|----------|
| ²³⁴Th | t₁/₂, Q(β⁻) | HIGH |
| ²³⁴Pa | t₁/₂, Q(β⁻) | HIGH |
| ²³⁴U | t₁/₂, Q(α) | HIGH |
| ²³⁰Th | t₁/₂, Q(α) | MEDIUM |
| ²²⁶Ra | t₁/₂, Q(α) | MEDIUM |
| ²²²Rn | t₁/₂, Q(α) | MEDIUM |
| ²¹⁸Po | t₁/₂, Q(α), BR | MEDIUM |
| ²¹⁴Pb | t₁/₂, Q(β⁻) | MEDIUM |
| ²¹⁴Bi | t₁/₂, Q(α), Q(β⁻), BR | HIGH |
| ²¹⁴Po | t₁/₂, Q(α) | MEDIUM |
| ²¹⁰Pb | t₁/₂, Q(β⁻) | MEDIUM |
| ²¹⁰Bi | t₁/₂, Q(β⁻) | MEDIUM |
| ²¹⁰Po | t₁/₂, Q(α) | HIGH |

### Th-232 Chain
| Nuclide | Fields Needed | Priority |
|---------|---------------|----------|
| ²²⁸Ra | t₁/₂, Q(β⁻) | MEDIUM |
| ²²⁸Ac | t₁/₂, Q(β⁻) | MEDIUM |
| ²²⁸Th | t₁/₂, Q(α) | MEDIUM |
| ²²⁴Ra | t₁/₂, Q(α) | MEDIUM |
| ²²⁰Rn | t₁/₂, Q(α) | MEDIUM |
| ²¹⁶Po | t₁/₂, Q(α) | MEDIUM |
| ²¹²Pb | t₁/₂, Q(β⁻) | MEDIUM |

### U-235 Chain
| Nuclide | Fields Needed | Priority |
|---------|---------------|----------|
| ²³¹Th | t₁/₂, Q(β⁻) | MEDIUM |
| ²³¹Pa | t₁/₂, Q(α) | MEDIUM |
| ²²⁷Th | t₁/₂, Q(α) | MEDIUM |
| ²²³Fr | t₁/₂, Q(β⁻) | MEDIUM |
| ²²³Ra | t₁/₂, Q(α) | MEDIUM |
| ²¹⁹Rn | t₁/₂, Q(α) | MEDIUM |
| ²¹⁵Po | t₁/₂, Q(α) | MEDIUM |
| ²¹¹Pb | t₁/₂, Q(β⁻) | MEDIUM |
| ²⁰⁷Tl | t₁/₂, Q(β⁻) | MEDIUM |

---

## Status Summary

| Category | Count | Status |
|----------|-------|--------|
| Chain parents | 3 | COMPLETE |
| Mandatory branchpoints | 3 | COMPLETE |
| Key daughters | 2 | COMPLETE |
| Chain endpoints | 3 | COMPLETE |
| Intermediate nuclides | ~30 | PARTIAL |
