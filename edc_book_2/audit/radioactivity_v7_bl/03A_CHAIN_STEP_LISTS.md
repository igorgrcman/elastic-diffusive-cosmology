# CHAIN STEP LISTS (V7)

**Created**: 2026-01-31
**Purpose**: Canonical nuclide sequences for 3 decay chains
**Source**: NNDC/ENSDF chain data [BL:S1]

---

## U-238 Chain (Radium Series) — 14 Steps

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 1 | ²³⁸U | 238 | 92 | α | ²³⁴Th | [BL:S1] |
| 2 | ²³⁴Th | 234 | 90 | β⁻ | ²³⁴Pa | [BL:S1] |
| 3 | ²³⁴Pa | 234 | 91 | β⁻ | ²³⁴U | [BL:S1] |
| 4 | ²³⁴U | 234 | 92 | α | ²³⁰Th | [BL:S1] |
| 5 | ²³⁰Th | 230 | 90 | α | ²²⁶Ra | [BL:S1] |
| 6 | ²²⁶Ra | 226 | 88 | α | ²²²Rn | [BL:S1] |
| 7 | ²²²Rn | 222 | 86 | α | ²¹⁸Po | [BL:S1] |
| 8 | ²¹⁸Po | 218 | 84 | α(99.98%) | ²¹⁴Pb | [BL:S1] |
| 9 | ²¹⁴Pb | 214 | 82 | β⁻ | ²¹⁴Bi | [BL:S1] |
| 10 | ²¹⁴Bi | 214 | 83 | β⁻(99.98%) | ²¹⁴Po | [BL:S1] |
| 11 | ²¹⁴Po | 214 | 84 | α | ²¹⁰Pb | [BL:S1] |
| 12 | ²¹⁰Pb | 210 | 82 | β⁻ | ²¹⁰Bi | [BL:S1] |
| 13 | ²¹⁰Bi | 210 | 83 | β⁻(99.99%) | ²¹⁰Po | [BL:S1] |
| 14 | ²¹⁰Po | 210 | 84 | α | ²⁰⁶Pb | [BL:S1] |
| END | ²⁰⁶Pb | 206 | 82 | STABLE | - | [BL:S1] |

**Notes**: Minor branches at ²¹⁸Po (β⁻ 0.02%) and ²¹⁴Bi (α 0.02%) not included in main sequence.

---

## Th-232 Chain (Thorium Series) — 10 Steps + Branch

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 1 | ²³²Th | 232 | 90 | α | ²²⁸Ra | [BL:S1] |
| 2 | ²²⁸Ra | 228 | 88 | β⁻ | ²²⁸Ac | [BL:S1] |
| 3 | ²²⁸Ac | 228 | 89 | β⁻ | ²²⁸Th | [BL:S1] |
| 4 | ²²⁸Th | 228 | 90 | α | ²²⁴Ra | [BL:S1] |
| 5 | ²²⁴Ra | 224 | 88 | α | ²²⁰Rn | [BL:S1] |
| 6 | ²²⁰Rn | 220 | 86 | α | ²¹⁶Po | [BL:S1] |
| 7 | ²¹⁶Po | 216 | 84 | α | ²¹²Pb | [BL:S1] |
| 8 | ²¹²Pb | 212 | 82 | β⁻ | ²¹²Bi | [BL:S1] |
| 9 | **²¹²Bi** | 212 | 83 | **BRANCH** | - | [BL:S1] |

### Branch at ²¹²Bi (MANDATORY)

| Path | Mode | BR(%) | Daughter | Next | To Stable |
|------|------|-------|----------|------|-----------|
| A | β⁻ | 64.06 | ²¹²Po | ²¹²Po→α→²⁰⁸Pb | ²⁰⁸Pb |
| B | α | 35.94 | ²⁰⁸Tl | ²⁰⁸Tl→β⁻→²⁰⁸Pb | ²⁰⁸Pb |

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 10A | ²¹²Po | 212 | 84 | α | ²⁰⁸Pb | [BL:S1] |
| 10B | ²⁰⁸Tl | 208 | 81 | β⁻ | ²⁰⁸Pb | [BL:S1] |
| END | ²⁰⁸Pb | 208 | 82 | STABLE | - | [BL:S1] |

---

## U-235 Chain (Actinium Series) — 11 Steps + 2 Branches

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 1 | ²³⁵U | 235 | 92 | α | ²³¹Th | [BL:S1] |
| 2 | ²³¹Th | 231 | 90 | β⁻ | ²³¹Pa | [BL:S1] |
| 3 | ²³¹Pa | 231 | 91 | α | ²²⁷Ac | [BL:S1] |
| 4 | **²²⁷Ac** | 227 | 89 | **BRANCH** | - | [BL:S1] |

### Branch #1 at ²²⁷Ac (MANDATORY)

| Path | Mode | BR(%) | Daughter | Continue |
|------|------|-------|----------|----------|
| A | β⁻ | 98.62 | ²²⁷Th | Main path |
| B | α | 1.38 | ²²³Fr | Minor path |

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 5A | ²²⁷Th | 227 | 90 | α | ²²³Ra | [BL:S1] |
| 5B | ²²³Fr | 223 | 87 | β⁻ | ²²³Ra | [BL:S1] |
| 6 | ²²³Ra | 223 | 88 | α | ²¹⁹Rn | [BL:S1] |
| 7 | ²¹⁹Rn | 219 | 86 | α | ²¹⁵Po | [BL:S1] |
| 8 | ²¹⁵Po | 215 | 84 | α | ²¹¹Pb | [BL:S1] |
| 9 | ²¹¹Pb | 211 | 82 | β⁻ | ²¹¹Bi | [BL:S1] |
| 10 | **²¹¹Bi** | 211 | 83 | **BRANCH** | - | [BL:S1] |

### Branch #2 at ²¹¹Bi (MANDATORY)

| Path | Mode | BR(%) | Daughter | Next | To Stable |
|------|------|-------|----------|------|-----------|
| A | α | 99.724 | ²⁰⁷Tl | ²⁰⁷Tl→β⁻→²⁰⁷Pb | ²⁰⁷Pb |
| B | β⁻ | 0.276 | ²¹¹Po | ²¹¹Po→α→²⁰⁷Pb | ²⁰⁷Pb |

| Step | Nuclide | A | Z | Mode | Daughter | [BL:S#] |
|------|---------|---|---|------|----------|---------|
| 11A | ²⁰⁷Tl | 207 | 81 | β⁻ | ²⁰⁷Pb | [BL:S1] |
| 11B | ²¹¹Po | 211 | 84 | α | ²⁰⁷Pb | [BL:S1] |
| END | ²⁰⁷Pb | 207 | 82 | STABLE | - | [BL:S1] |

---

## Summary

| Chain | Steps | Branches | Endpoint |
|-------|-------|----------|----------|
| U-238 | 14 | 0 major | ²⁰⁶Pb |
| Th-232 | 10 | 1 (²¹²Bi) | ²⁰⁸Pb |
| U-235 | 11 | 2 (²²⁷Ac, ²¹¹Bi) | ²⁰⁷Pb |

All chains verified against NNDC standard decay chain data.
