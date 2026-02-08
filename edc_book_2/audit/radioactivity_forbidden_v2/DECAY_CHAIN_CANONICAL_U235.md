# DECAY CHAIN CANONICAL: U-235 → Pb-207 (Actinium Series)

**Generated**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]

---

## Chain Skeleton

| Step | Parent | A | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|------|----------|------|---------|
| 1 | ²³⁵U | 235 | α | ²³¹Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²³¹Th | 231 | β⁻ | ²³¹Pa | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²³¹Pa | 231 | α | ²²⁷Ac | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4A | ²²⁷Ac | 227 | β⁻ (98.6%) | ²²⁷Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4B | ²²⁷Ac | 227 | α (1.4%) | ²²³Fr | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5A | ²²⁷Th | 227 | α | ²²³Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5B | ²²³Fr | 223 | β⁻ | ²²³Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²³Ra | 223 | α | ²¹⁹Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²¹⁹Rn | 219 | α | ²¹⁵Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹⁵Po | 215 | α | ²¹¹Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9 | ²¹¹Pb | 211 | β⁻ | ²¹¹Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10A | ²¹¹Bi | 211 | α (99.7%) | ²⁰⁷Tl | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10B | ²¹¹Bi | 211 | β⁻ (0.3%) | ²¹¹Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11A | ²⁰⁷Tl | 207 | β⁻ | ²⁰⁷Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11B | ²¹¹Po | 211 | α | ²⁰⁷Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁷Pb | 207 | STABLE | — | ∞ | — |

**Chain Statistics**:
- Total steps: 11 (with two branching points)
- α-decays: 7 (main path)
- β⁻-decays: 4 (main path)
- ΔA = 235 - 207 = 28
- ΔZ = 92 - 82 = 10
- Branching at: ²²⁷Ac (98.6% β⁻ / 1.4% α), ²¹¹Bi (99.7% α / 0.3% β⁻)

---

## EDC Annotations [I]/[P]

| Step | Nuclide | A | n(A) Estimate | d(n) | Frustration | Mode |
|------|---------|---|---------------|------|-------------|------|
| 1 | ²³⁵U | 235 | [Open] ~43? | ~5? | HIGH | α [I] |
| 2 | ²³¹Th | 231 | [Open] | [Open] | HIGH | β⁻ [P] |
| 3 | ²³¹Pa | 231 | [Open] | [Open] | HIGH | α [I] |
| 4 | ²²⁷Ac | 227 | [Open] | [Open] | MEDIUM-HIGH | BRANCH [P] |
| 5 | ²²⁷Th/²²³Fr | 227/223 | [Open] | [Open] | MEDIUM | Converge [I] |
| 6 | ²²³Ra | 223 | [Open] | [Open] | MEDIUM | α [I] |
| 7 | ²¹⁹Rn | 219 | [Open] | [Open] | LOW-MEDIUM | α (actinon) [I] |
| 8 | ²¹⁵Po | 215 | [Open] | [Open] | LOW | α [I] |
| 9 | ²¹¹Pb | 211 | [Open] | [Open] | LOW | β⁻ [P] |
| 10 | ²¹¹Bi | 211 | [Open] | [Open] | LOW | BRANCH [P] |
| 11 | ²⁰⁷Tl/²¹¹Po | 207/211 | [Open] | [Open] | LOW | Converge [I] |
| END | ²⁰⁷Pb | 207 | [Open] ~36? | ~0? | ZERO | Stable [P] |

---

## Branching Analysis [P]

### ²²⁷Ac (A=227): 98.6% β⁻, 1.4% α

**Interpretation [P]**:
- Strong β⁻ preference → system strongly wants to adjust N/Z
- Small α channel → some tendency for A reduction
- If n(227) is slightly below 48, β⁻ pushes toward allowed
- Asymmetric branching suggests clear mode preference

### ²¹¹Bi (A=211): 99.7% α, 0.3% β⁻

**Interpretation [P]**:
- Opposite pattern: α strongly preferred
- If n(211) is far from allowed, major A reduction needed
- Only 0.3% tries N/Z route
- Suggests d(n) is large at A=211

**EDC Prediction [P]**: Branching correlates with d(n):
- ²²⁷Ac: small d(n) → β⁻ favored
- ²¹¹Bi: large d(n) → α favored

---

## U-235 Special Properties

**²³⁵U is fissile** (unlike ²³⁸U which is fissionable but not fissile).

**EDC Hypothesis [P]**:
- Odd-A nuclei (A=235) may have different n(A) characteristics
- Fissile character = extreme M-topology instability
- Fission = splitting into two "allowed" chunks
- n(235) may be deeper in forbidden zone than n(238)?

**Open Question**: Does EDC predict fissility from coordination?

---

## ²⁰⁷Pb: Odd-N Stable Endpoint

**Properties**:
- Z = 82 (magic)
- N = 125 (one below magic 126)
- Stable despite odd N

**EDC Hypothesis [P]**:
- n(207) should be allowed (near 36?)
- Shell effect from Z=82 compensates for N=125
- All three Pb endpoints (206, 207, 208) stable → all have allowed n?

---

## G-N Law Application [I]

**Citation**: [DN-015]

For α-steps in main path:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
```

**Lifetime progression**:
- ²³⁵U: ~7×10⁸ y
- ²³¹Pa: ~3×10⁴ y
- ²²⁷Th: ~19 d
- ²²³Ra: ~11 d
- ²¹⁹Rn: ~4 s
- ²¹⁵Po: ~1.8 ms

Span of ~17 orders of magnitude, consistent with decreasing ε_f.

---

## Cross-Chain Comparison

| Property | U-238 Series | Th-232 Series | U-235 Series |
|----------|--------------|---------------|--------------|
| Parent A | 238 | 232 | 235 |
| Endpoint | ²⁰⁶Pb | ²⁰⁸Pb | ²⁰⁷Pb |
| ΔA | 32 | 24 | 28 |
| α-steps | 8 | 6 | 7 |
| β-steps | 6 | 4 | 4 |
| Branches | 1 (²¹⁴Bi) | 1 (²¹²Bi) | 2 (²²⁷Ac, ²¹¹Bi) |

**Pattern [I]**: Larger ΔA requires more α-steps (α removes 4 mass units each).

---

## Key Questions [Open]

1. Why is ²³⁵U fissile but ²³⁸U not? EDC n(A) difference?
2. Why opposite branching patterns at ²²⁷Ac vs ²¹¹Bi?
3. Why are all three Pb isotopes (206, 207, 208) stable?
4. What determines which path dominates at branching points?

---

## Integration Note

U-235 chain is important for:
- Nuclear weapons physics (fissile material)
- Geochronology (U-Pb dating)
- EDC could provide unified explanation for fissility + decay patterns
