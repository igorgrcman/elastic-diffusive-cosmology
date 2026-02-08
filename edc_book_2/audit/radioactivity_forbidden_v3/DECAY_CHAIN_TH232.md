# DECAY CHAIN: Th-232 → Pb-208 (Thorium Series)

**Created**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]
**EDC Interpretation**: [I]/[P] tags per claim

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³²Th | 232 | 90 | α | ²²⁸Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²²⁸Ra | 228 | 88 | β⁻ | ²²⁸Ac | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²²⁸Ac | 228 | 89 | β⁻ | ²²⁸Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4 | ²²⁸Th | 228 | 90 | α | ²²⁴Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5 | ²²⁴Ra | 224 | 88 | α | ²²⁰Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²⁰Rn | 220 | 86 | α | ²¹⁶Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²¹⁶Po | 216 | 84 | α | ²¹²Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹²Pb | 212 | 82 | β⁻ | ²¹²Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9A | ²¹²Bi | 212 | 83 | β⁻ (64%) | ²¹²Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9B | ²¹²Bi | 212 | 83 | α (36%) | ²⁰⁸Tl | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10A | ²¹²Po | 212 | 84 | α | ²⁰⁸Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10B | ²⁰⁸Tl | 208 | 81 | β⁻ | ²⁰⁸Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁸Pb | 208 | 82 | STABLE | — | ∞ | — |

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 10 (with branching) |
| α-decays | 6 (main path) |
| β⁻-decays | 4 (main path) |
| ΔA (mass loss) | 24 |
| ΔZ (charge loss) | 8 |
| Branching points | 1 (²¹²Bi) |

---

## Branching Point Analysis

### ²¹²Bi (A=212, Z=83)

| Mode | Fraction | Interpretation [P] |
|------|----------|-------------------|
| β⁻ | 64% | Dominant: adjust N/Z toward 48 |
| α | 36% | Secondary: reduce A toward 36 |

**EDC Hypothesis [P]**:
- n(212) near transition point (equidistant from 36 and 48)
- Both modes competitive because d(n) similar for both directions
- 64:36 ratio reflects slight preference for N/Z path

**Falsification**: If n(212) calculable, predict ratio from d(n) analysis.

---

## EDC Annotations

| Step | Nuclide | A | n(A) | d(n) | Frustration | Mode Rationale |
|------|---------|---|------|------|-------------|----------------|
| 1 | ²³²Th | 232 | [Open] | [Open] | HIGH [P] | α: primordial [I] |
| 2 | ²²⁸Ra | 228 | [Open] | [Open] | HIGH [P] | β⁻: N/Z adjust [P] |
| 3 | ²²⁸Ac | 228 | [Open] | [Open] | HIGH [P] | β⁻: continue [P] |
| 4 | ²²⁸Th | 228 | [Open] | [Open] | MED-HIGH [P] | α: resume [I] |
| 5 | ²²⁴Ra | 224 | [Open] | [Open] | MEDIUM [P] | α: chain [I] |
| 6 | ²²⁰Rn | 220 | [Open] | [Open] | MEDIUM [P] | α: thoron [I] |
| 7 | ²¹⁶Po | 216 | [Open] | [Open] | LOW-MED [P] | α: chain [I] |
| 8 | ²¹²Pb | 212 | [Open] | [Open] | LOW [P] | β⁻: pre-branch [P] |
| 9 | ²¹²Bi | 212 | [Open] | [Open] | LOW [P] | BRANCH [P] |
| 10 | ²¹²Po/²⁰⁸Tl | — | [Open] | [Open] | LOW [P] | Converge [I] |
| END | ²⁰⁸Pb | 208 | ~36? [P] | ~0? [P] | ZERO [P] | Doubly magic |

---

## ²⁰⁸Pb: Doubly Magic Endpoint

| Property | Value |
|----------|-------|
| Z | 82 (magic) |
| N | 126 (magic) |
| Shell closure | Yes (both) |
| EDC n(A) | ~36? [P] (allowed) |

**Hypothesis [P]**: Stability from:
1. Shell effects (conventional nuclear physics)
2. Topological allowedness (EDC: n = 36 = 2² × 3²)

**Both mechanisms may reinforce each other.**

---

## Lifetime Progression [I]

| Nuclide | t₁/₂ (qualitative) | Trend |
|---------|---------------------|-------|
| ²³²Th | ~10¹⁰ y | Primordial |
| ²²⁸Th | ~2 y | |
| ²²⁴Ra | ~4 d | |
| ²²⁰Rn | ~1 min | |
| ²¹⁶Po | ~0.1 s | |
| ²¹²Po | ~10⁻⁷ s | Ultra-short |

**Pattern [I]**: 17 orders of magnitude span, consistent with decreasing ε_f(A).

---

## Key Questions

1. Why is branching ratio 64:36 at ²¹²Bi?
2. Does doubly-magic status enhance n(A) allowedness?
3. Is n(208) = 36 exactly, or approximately?

---

## Historical Note

Thorium series historically important (monazite sands).
²²⁰Rn called "thoron" to distinguish from ²²²Rn (radon).

---

## Cross-Reference

- Branching analysis: OQ-V3-003
- Doubly-magic: OQ-V3-004
- G-N law: LAW-3 in LAW_REGISTRY.md
