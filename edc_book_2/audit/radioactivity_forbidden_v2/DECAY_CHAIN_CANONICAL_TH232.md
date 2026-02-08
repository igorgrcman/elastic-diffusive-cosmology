# DECAY CHAIN CANONICAL: Th-232 → Pb-208 (Thorium Series)

**Generated**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]

---

## Chain Skeleton

| Step | Parent | A | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|------|----------|------|---------|
| 1 | ²³²Th | 232 | α | ²²⁸Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²²⁸Ra | 228 | β⁻ | ²²⁸Ac | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²²⁸Ac | 228 | β⁻ | ²²⁸Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4 | ²²⁸Th | 228 | α | ²²⁴Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5 | ²²⁴Ra | 224 | α | ²²⁰Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²⁰Rn | 220 | α | ²¹⁶Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²¹⁶Po | 216 | α | ²¹²Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹²Pb | 212 | β⁻ | ²¹²Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9A | ²¹²Bi | 212 | β⁻ (64%) | ²¹²Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9B | ²¹²Bi | 212 | α (36%) | ²⁰⁸Tl | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10A | ²¹²Po | 212 | α | ²⁰⁸Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10B | ²⁰⁸Tl | 208 | β⁻ | ²⁰⁸Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁸Pb | 208 | STABLE | — | ∞ | — |

**Chain Statistics**:
- Total steps: 10 (with branching at ²¹²Bi)
- α-decays: 6 (main path)
- β⁻-decays: 4 (main path)
- ΔA = 232 - 208 = 24
- ΔZ = 90 - 82 = 8

**Branching Point**: ²¹²Bi decays 64% via β⁻ and 36% via α

---

## EDC Annotations [I]/[P]

| Step | Nuclide | A | n(A) Estimate | d(n) | Frustration | Mode Explanation |
|------|---------|---|---------------|------|-------------|------------------|
| 1 | ²³²Th | 232 | [Open] ~43? | ~5? | HIGH | α (long-lived primordial) [I] |
| 2 | ²²⁸Ra | 228 | [Open] | [Open] | HIGH | β⁻ N/Z adjustment [P] |
| 3 | ²²⁸Ac | 228 | [Open] | [Open] | HIGH | β⁻ continues [P] |
| 4 | ²²⁸Th | 228 | [Open] | [Open] | MEDIUM-HIGH | α resumes [I] |
| 5 | ²²⁴Ra | 224 | [Open] | [Open] | MEDIUM | α continues [I] |
| 6 | ²²⁰Rn | 220 | [Open] | [Open] | MEDIUM | α (thoron gas) [I] |
| 7 | ²¹⁶Po | 216 | [Open] | [Open] | LOW-MEDIUM | α [I] |
| 8 | ²¹²Pb | 212 | [Open] | [Open] | LOW | β⁻ [P] |
| 9 | ²¹²Bi | 212 | [Open] | [Open] | LOW | **BRANCHING** [P] |
| 10 | ²¹²Po/²⁰⁸Tl | 212/208 | [Open] | [Open] | LOW | Converge to ²⁰⁸Pb [I] |
| END | ²⁰⁸Pb | 208 | [Open] ~36? | ~0? | ZERO | Doubly magic [P] |

---

## Branching Point Analysis [P]

**²¹²Bi (A=212)**: 64% β⁻, 36% α

**EDC Interpretation [P]**:
- If n(212) is near transition point d(n)=6 (equidistant from 36 and 48), both modes compete
- β⁻ (64%): system prefers to approach n=48 via N/Z change
- α (36%): system takes alternative route via A reduction

**Prediction [P]**: Branching ratio should correlate with d(n):
- If n(212) > 42 → β⁻ favored (push toward 48)
- If n(212) < 42 → α favored (push toward 36)

**Falsification**: Compare branching ratios across different Bi isotopes.

---

## ²⁰⁸Pb: Doubly Magic Endpoint

**Properties**:
- Z = 82 (magic)
- N = 126 (magic)
- Most stable heavy nucleus

**EDC Hypothesis [P]**:
- n(208) may be exactly 36 (allowed), explaining stability
- Magic numbers might correspond to allowed coordinations
- Double magic → double stability from shell + topology

---

## G-N Law Application [I]

For α-decay steps (1, 4, 5, 6, 7, 9B, 10A):

**Citation**: [DN-015]
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
```

**Observed pattern [I]**: Lifetime decreases along chain:
- ²³²Th: ~10¹⁰ y (primordial)
- ²²⁸Th: ~1.9 y
- ²²⁴Ra: ~3.7 d
- ²²⁰Rn: ~56 s
- ²¹⁶Po: ~0.15 s
- ²¹²Po: ~300 ns

This 18 orders of magnitude span is consistent with decreasing ε_f(A).

---

## Key Questions [Open]

1. Why is branching ratio 64:36 at ²¹²Bi?
2. Does n(A) have discontinuity at magic numbers?
3. Is ²⁰⁸Pb stability from shell effects, topology, or both?

---

## Integration Note

Thorium series is historically important (monazite sands). Book 2 could use this as example of:
- Multi-step frustration relaxation
- Branching as EDC mode competition
- Doubly magic endpoint as "allowed" coordination
