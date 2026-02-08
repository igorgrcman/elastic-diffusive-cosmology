# DECAY CHAIN: U-235 → Pb-207 (Actinium Series)

**Created**: 2026-01-31
**Data Status**: All t₁/₂ and Q marked [BL:SOURCE_TBD]
**EDC Interpretation**: [I]/[P] tags per claim

---

## Chain Skeleton

| Step | Parent | A | Z | Mode | Daughter | t₁/₂ | Q (MeV) |
|------|--------|---|---|------|----------|------|---------|
| 1 | ²³⁵U | 235 | 92 | α | ²³¹Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 2 | ²³¹Th | 231 | 90 | β⁻ | ²³¹Pa | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 3 | ²³¹Pa | 231 | 91 | α | ²²⁷Ac | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4A | ²²⁷Ac | 227 | 89 | β⁻ (98.6%) | ²²⁷Th | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 4B | ²²⁷Ac | 227 | 89 | α (1.4%) | ²²³Fr | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5A | ²²⁷Th | 227 | 90 | α | ²²³Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 5B | ²²³Fr | 223 | 87 | β⁻ | ²²³Ra | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 6 | ²²³Ra | 223 | 88 | α | ²¹⁹Rn | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 7 | ²¹⁹Rn | 219 | 86 | α | ²¹⁵Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 8 | ²¹⁵Po | 215 | 84 | α | ²¹¹Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 9 | ²¹¹Pb | 211 | 82 | β⁻ | ²¹¹Bi | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10A | ²¹¹Bi | 211 | 83 | α (99.7%) | ²⁰⁷Tl | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 10B | ²¹¹Bi | 211 | 83 | β⁻ (0.3%) | ²¹¹Po | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11A | ²⁰⁷Tl | 207 | 81 | β⁻ | ²⁰⁷Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| 11B | ²¹¹Po | 211 | 84 | α | ²⁰⁷Pb | [BL:SOURCE_TBD] | [BL:SOURCE_TBD] |
| END | ²⁰⁷Pb | 207 | 82 | STABLE | — | ∞ | — |

---

## Chain Statistics

| Metric | Value |
|--------|-------|
| Total steps | 11 (with 2 branching points) |
| α-decays | 7 (main path) |
| β⁻-decays | 4 (main path) |
| ΔA (mass loss) | 28 |
| ΔZ (charge loss) | 10 |
| Branching points | 2 (²²⁷Ac, ²¹¹Bi) |

---

## Branching Point Analysis

### Branch 1: ²²⁷Ac (A=227, Z=89)

| Mode | Fraction | Interpretation [P] |
|------|----------|-------------------|
| β⁻ | 98.6% | Dominant: strong N/Z preference |
| α | 1.4% | Minor: some A reduction |

**EDC Hypothesis [P]**:
- n(227) slightly below 48 → β⁻ pushes toward allowed
- Highly asymmetric ratio indicates clear mode preference
- Small α channel = residual alternative pathway

### Branch 2: ²¹¹Bi (A=211, Z=83)

| Mode | Fraction | Interpretation [P] |
|------|----------|-------------------|
| α | 99.7% | Dominant: strong A reduction |
| β⁻ | 0.3% | Minor: N/Z alternative |

**EDC Hypothesis [P]**:
- n(211) far from allowed → major Δn needed via α
- Opposite pattern from ²²⁷Ac
- Only 0.3% tries N/Z route

**Contrast**:
| Nuclide | Dominant | Interpretation |
|---------|----------|----------------|
| ²²⁷Ac | β⁻ (98.6%) | Near allowed, fine-tune |
| ²¹¹Bi | α (99.7%) | Far from allowed, large step |

---

## EDC Annotations

| Step | Nuclide | A | n(A) | d(n) | Frustration | Mode Rationale |
|------|---------|---|------|------|-------------|----------------|
| 1 | ²³⁵U | 235 | [Open] | [Open] | HIGH [P] | α: fissile parent [I] |
| 2 | ²³¹Th | 231 | [Open] | [Open] | HIGH [P] | β⁻: N/Z [P] |
| 3 | ²³¹Pa | 231 | [Open] | [Open] | HIGH [P] | α: chain [I] |
| 4 | ²²⁷Ac | 227 | [Open] | [Open] | MED-HIGH [P] | BRANCH 1 [P] |
| 5 | ²²⁷Th/²²³Fr | — | [Open] | [Open] | MEDIUM [P] | Converge [I] |
| 6 | ²²³Ra | 223 | [Open] | [Open] | MEDIUM [P] | α: chain [I] |
| 7 | ²¹⁹Rn | 219 | [Open] | [Open] | LOW-MED [P] | α: actinon [I] |
| 8 | ²¹⁵Po | 215 | [Open] | [Open] | LOW [P] | α: chain [I] |
| 9 | ²¹¹Pb | 211 | [Open] | [Open] | LOW [P] | β⁻: pre-branch [P] |
| 10 | ²¹¹Bi | 211 | [Open] | [Open] | LOW [P] | BRANCH 2 [P] |
| 11 | ²⁰⁷Tl/²¹¹Po | — | [Open] | [Open] | LOW [P] | Converge [I] |
| END | ²⁰⁷Pb | 207 | ~36? [P] | ~0? [P] | ZERO [P] | Stable |

---

## ²³⁵U: Fissile Nucleus

**Key property**: ²³⁵U is FISSILE (unlike ²³⁸U which is only fissionable)

**Conventional explanation**: Odd neutron number enhances fission probability

**EDC Hypothesis [P]**:
- Odd-A nuclei may have different n(A) topology
- n(235) possibly deeper in forbidden zone than n(238)?
- Fissile = extreme M-topology instability
- Fission = splitting into two "allowed" chunks

**Open**: Does EDC predict fissility from coordination?

---

## ²⁰⁷Pb: Odd-N Stable Endpoint

| Property | Value |
|----------|-------|
| Z | 82 (magic) |
| N | 125 (one below magic 126) |
| Stability | Stable despite odd N |

**EDC Hypothesis [P]**:
- n(207) ≈ 36 (allowed)
- Z=82 magic compensates for N=125 odd
- All three Pb endpoints (206, 207, 208) stable → all have allowed n

---

## Cross-Chain Comparison

| Property | U-238 | Th-232 | U-235 |
|----------|-------|--------|-------|
| Parent A | 238 | 232 | 235 |
| Endpoint | ²⁰⁶Pb | ²⁰⁸Pb | ²⁰⁷Pb |
| ΔA | 32 | 24 | 28 |
| α-steps | 8 | 6 | 7 |
| β-steps | 6 | 4 | 4 |
| Branches | 0 | 1 | 2 |

**Pattern [I]**: Larger ΔA requires more α-steps (α removes 4 mass units each).

---

## Key Questions

1. Why opposite branching patterns at ²²⁷Ac vs ²¹¹Bi?
2. Why is ²³⁵U fissile but ²³⁸U not? EDC n(A) difference?
3. Why are all three Pb isotopes (206, 207, 208) stable?
4. What determines which path dominates at branching?

---

## Cross-Reference

- Fissility: OQ-V3-005
- Branching: OQ-V3-003
- Pb stability: OQ-V3-004
- G-N law: LAW-3 in LAW_REGISTRY.md
