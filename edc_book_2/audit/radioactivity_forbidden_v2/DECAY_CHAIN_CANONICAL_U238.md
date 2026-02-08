# DECAY CHAIN CANONICAL: U-238 → Pb-206 (Radium Series)

**Generated**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]

---

## Chain Skeleton

| Step | Parent | A | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|------|----------|------|---------|
| 1 | ²³⁸U | 238 | α | ²³⁴Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²³⁴Th | 234 | β⁻ | ²³⁴Pa | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²³⁴Pa | 234 | β⁻ | ²³⁴U | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4 | ²³⁴U | 234 | α | ²³⁰Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5 | ²³⁰Th | 230 | α | ²²⁶Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²⁶Ra | 226 | α | ²²²Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²²²Rn | 222 | α | ²¹⁸Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹⁸Po | 218 | α | ²¹⁴Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9 | ²¹⁴Pb | 214 | β⁻ | ²¹⁴Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10 | ²¹⁴Bi | 214 | β⁻ | ²¹⁴Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11 | ²¹⁴Po | 214 | α | ²¹⁰Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 12 | ²¹⁰Pb | 210 | β⁻ | ²¹⁰Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 13 | ²¹⁰Bi | 210 | β⁻ | ²¹⁰Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 14 | ²¹⁰Po | 210 | α | ²⁰⁶Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁶Pb | 206 | STABLE | — | ∞ | — |

**Chain Statistics**:
- Total steps: 14
- α-decays: 8
- β⁻-decays: 6
- ΔA = 238 - 206 = 32
- ΔZ = 92 - 82 = 10

---

## EDC Annotations [I]/[P]

| Step | Nuclide | A | n(A) Estimate | d(n) | Frustration Trend | Mode Explanation |
|------|---------|---|---------------|------|-------------------|------------------|
| 1 | ²³⁸U | 238 | [Open] ~43+ | ~5+ | HIGH | α to reduce frustration [I] |
| 2 | ²³⁴Th | 234 | [Open] | [Open] | HIGH | β⁻ to adjust N/Z [P] |
| 3 | ²³⁴Pa | 234 | [Open] | [Open] | HIGH | β⁻ continues [P] |
| 4 | ²³⁴U | 234 | [Open] | [Open] | HIGH | α resumes [I] |
| 5 | ²³⁰Th | 230 | [Open] | [Open] | MEDIUM-HIGH | α chain [I] |
| 6 | ²²⁶Ra | 226 | [Open] | [Open] | MEDIUM | α continues [I] |
| 7 | ²²²Rn | 222 | [Open] | [Open] | MEDIUM | α (radon gas) [I] |
| 8 | ²¹⁸Po | 218 | [Open] | [Open] | MEDIUM | α [I] |
| 9 | ²¹⁴Pb | 214 | [Open] | [Open] | LOW-MEDIUM | β⁻ fine-tuning [P] |
| 10 | ²¹⁴Bi | 214 | [Open] | [Open] | LOW-MEDIUM | β⁻ continues [P] |
| 11 | ²¹⁴Po | 214 | [Open] | [Open] | LOW | Ultra-short α [I] |
| 12 | ²¹⁰Pb | 210 | [Open] | [Open] | LOW | β⁻ [P] |
| 13 | ²¹⁰Bi | 210 | [Open] | [Open] | LOW | β⁻ [P] |
| 14 | ²¹⁰Po | 210 | [Open] | [Open] | LOW | Final α [I] |
| END | ²⁰⁶Pb | 206 | [Open] ~36? | ~0? | ZERO | Stable (allowed?) [P] |

---

## G-N Law Application [I]

**Citation**: [DN-015] 22826edd_full.md:2555-2567

For α-decay steps:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
```

Where a = 1.63, c = -2.40, b = -42.1 [DN-017]

**Prediction [I]**: As chain progresses:
1. Z decreases (92 → 82)
2. ε_f decreases (frustration relieved)
3. Combined effect: t₁/₂ generally decreases along chain

This is consistent with observed pattern: heavy parents (U) have long lives, light daughters (Po) have short lives.

---

## Key Questions [Open]

1. What is n(238)? Required to compute initial d(n).
2. Does n(A) decrease monotonically with A?
3. Is n(206) ≈ 36 (allowed), explaining stability?
4. Why do β⁻ steps alternate with α? EDC mode selection unclear.

---

## Integration Note

If this chain is to be integrated into Book 2 Ch. 7:
- Need n(A) formula from OQ-V2-007
- Need actual t₁/₂ data from NNDC for G-N verification
- Mark all predictions as [I] or [P] in LaTeX
