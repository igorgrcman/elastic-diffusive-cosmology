# DECAY CHAIN: U-238 → Pb-206 (Radium Series)

**Created**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]
**EDC Interpretation**: [I]/[P] tags per claim

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³⁸U | 238 | 92 | α | ²³⁴Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²³⁴Th | 234 | 90 | β⁻ | ²³⁴Pa | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²³⁴Pa | 234 | 91 | β⁻ | ²³⁴U | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4 | ²³⁴U | 234 | 92 | α | ²³⁰Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5 | ²³⁰Th | 230 | 90 | α | ²²⁶Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²⁶Ra | 226 | 88 | α | ²²²Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²²²Rn | 222 | 86 | α | ²¹⁸Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹⁸Po | 218 | 84 | α | ²¹⁴Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9 | ²¹⁴Pb | 214 | 82 | β⁻ | ²¹⁴Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10 | ²¹⁴Bi | 214 | 83 | β⁻ | ²¹⁴Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11 | ²¹⁴Po | 214 | 84 | α | ²¹⁰Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 12 | ²¹⁰Pb | 210 | 82 | β⁻ | ²¹⁰Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 13 | ²¹⁰Bi | 210 | 83 | β⁻ | ²¹⁰Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 14 | ²¹⁰Po | 210 | 84 | α | ²⁰⁶Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁶Pb | 206 | 82 | STABLE | — | ∞ | — |

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 14 |
| α-decays | 8 |
| β⁻-decays | 6 |
| ΔA (mass loss) | 32 |
| ΔZ (charge loss) | 10 |
| Branching points | 0 (main path linear) |

---

## EDC Annotations

| Step | Nuclide | A | n(A) | d(n) | Frustration | Mode Rationale |
|------|---------|---|------|------|-------------|----------------|
| 1 | ²³⁸U | 238 | [Open] | [Open] | HIGH [P] | α: large Δn relief [I] |
| 2 | ²³⁴Th | 234 | [Open] | [Open] | HIGH [P] | β⁻: N/Z adjust [P] |
| 3 | ²³⁴Pa | 234 | [Open] | [Open] | HIGH [P] | β⁻: N/Z continue [P] |
| 4 | ²³⁴U | 234 | [Open] | [Open] | HIGH [P] | α: resume Δn [I] |
| 5 | ²³⁰Th | 230 | [Open] | [Open] | MED-HIGH [P] | α: chain [I] |
| 6 | ²²⁶Ra | 226 | [Open] | [Open] | MEDIUM [P] | α: chain [I] |
| 7 | ²²²Rn | 222 | [Open] | [Open] | MEDIUM [P] | α: radon gas [I] |
| 8 | ²¹⁸Po | 218 | [Open] | [Open] | MEDIUM [P] | α: chain [I] |
| 9 | ²¹⁴Pb | 214 | [Open] | [Open] | LOW-MED [P] | β⁻: fine-tune [P] |
| 10 | ²¹⁴Bi | 214 | [Open] | [Open] | LOW-MED [P] | β⁻: continue [P] |
| 11 | ²¹⁴Po | 214 | [Open] | [Open] | LOW [P] | α: ultra-short [I] |
| 12 | ²¹⁰Pb | 210 | [Open] | [Open] | LOW [P] | β⁻: final adjust [P] |
| 13 | ²¹⁰Bi | 210 | [Open] | [Open] | LOW [P] | β⁻: continue [P] |
| 14 | ²¹⁰Po | 210 | [Open] | [Open] | LOW [P] | α: final step [I] |
| END | ²⁰⁶Pb | 206 | ~36? [P] | ~0? [P] | ZERO [P] | Stable: allowed n |

---

## G-N Law Application [I]

**Citation**: DN-015, DN-017

For α-decay steps:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
a = 1.63, c = -2.40, b = -42.1
```

**Prediction [I]**: As chain progresses:
1. Z decreases (92 → 82): reduces barrier
2. ε_f decreases: frustration relieved
3. Combined: t₁/₂ generally decreases

**Lifetime progression** (qualitative):
- ²³⁸U: ~10⁹ y (primordial)
- ²³⁴U: ~10⁵ y
- ²³⁰Th: ~10⁴ y
- ²²⁶Ra: ~10³ y
- ²²²Rn: ~days
- ²¹⁸Po: ~minutes
- ²¹⁴Po: ~10⁻⁴ s (ultra-short)
- ²¹⁰Po: ~days

---

## Mode Selection Pattern

| Pattern | Interpretation [P] |
|---------|-------------------|
| α-β-β-α-α-α-α-α-β-β-α-β-β-α | Alternation pattern |
| α after β-pair | N/Z corrected, α resumes |
| β-pairs | N/Z fine-tuning between α-steps |

**Hypothesis [P]**: β-decays adjust N/Z ratio to enable next α-decay.

---

## Key Questions

1. What is n(238)? Required for initial d(n).
2. Does n(A) decrease monotonically with A?
3. Why do β⁻ steps cluster in pairs?
4. Is n(206) ≈ 36, explaining stability?

---

## Cross-Reference

- n(A) formula: OQ-V3-001 in OPEN_QUESTIONS.md
- G-N law: LAW-3 in LAW_REGISTRY.md
- Endpoint stability: OQ-V3-004
