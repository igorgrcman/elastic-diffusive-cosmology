# DECAY CHAIN: U-238 → Pb-206 (Radium Series)

**Generated**: 2026-01-31
**Purpose**: Standard decay chain with EDC interpretation
**Data Status**: Nuclear data marked [BL] (external NNDC/IAEA required)

---

## 1. Decay Chain Table

| Step | Parent | Decay Mode | Daughter | Half-Life | Q (MeV) | Notes |
|------|--------|------------|----------|-----------|---------|-------|
| 1 | ²³⁸U | α | ²³⁴Th | [BL] 4.47×10⁹ y | [BL] | Start of chain |
| 2 | ²³⁴Th | β⁻ | ²³⁴Pa | [BL] 24.1 d | [BL] | |
| 3 | ²³⁴Pa | β⁻ | ²³⁴U | [BL] 6.7 h | [BL] | |
| 4 | ²³⁴U | α | ²³⁰Th | [BL] 2.45×10⁵ y | [BL] | |
| 5 | ²³⁰Th | α | ²²⁶Ra | [BL] 7.54×10⁴ y | [BL] | |
| 6 | ²²⁶Ra | α | ²²²Rn | [BL] 1600 y | [BL] | Radium |
| 7 | ²²²Rn | α | ²¹⁸Po | [BL] 3.82 d | [BL] | Radon gas |
| 8 | ²¹⁸Po | α | ²¹⁴Pb | [BL] 3.1 min | [BL] | |
| 9 | ²¹⁴Pb | β⁻ | ²¹⁴Bi | [BL] 27 min | [BL] | |
| 10 | ²¹⁴Bi | β⁻ | ²¹⁴Po | [BL] 20 min | [BL] | |
| 11 | ²¹⁴Po | α | ²¹⁰Pb | [BL] 164 μs | [BL] | |
| 12 | ²¹⁰Pb | β⁻ | ²¹⁰Bi | [BL] 22.3 y | [BL] | |
| 13 | ²¹⁰Bi | β⁻ | ²¹⁰Po | [BL] 5.0 d | [BL] | |
| 14 | ²¹⁰Po | α | ²⁰⁶Pb | [BL] 138 d | [BL] | |
| END | ²⁰⁶Pb | STABLE | — | ∞ | — | End of chain |

**Note**: All half-life and Q values marked [BL] require external nuclear data verification.

---

## 2. EDC Attributes per Step

Based on MTR-001..005 framework. Coordination number n(A) estimated from nuclear density.

| Step | Nuclide | A | Estimated n(A) | Allowed/Forbidden | ε_f Trend | ΔV_eff Trend |
|------|---------|---|----------------|-------------------|-----------|--------------|
| 1 | ²³⁸U | 238 | [Open] ≈ 43-45? | Forbidden | High | High → long τ |
| 2 | ²³⁴Th | 234 | [Open] | [Open] | [Open] | β⁻, not α |
| 3 | ²³⁴Pa | 234 | [Open] | [Open] | [Open] | β⁻, not α |
| 4 | ²³⁴U | 234 | [Open] ≈ 43? | Forbidden | High | α dominates |
| 5 | ²³⁰Th | 230 | [Open] | [Open] | Medium | α chain |
| 6 | ²²⁶Ra | 226 | [Open] | [Open] | Medium | α chain |
| 7 | ²²²Rn | 222 | [Open] | [Open] | Medium | α, gas |
| 8 | ²¹⁸Po | 218 | [Open] | [Open] | Medium | α |
| 9 | ²¹⁴Pb | 214 | [Open] | [Open] | Lower | β⁻ mode |
| 10 | ²¹⁴Bi | 214 | [Open] | [Open] | Lower | β⁻ mode |
| 11 | ²¹⁴Po | 214 | [Open] | [Open] | Low | Ultra-short α |
| 12 | ²¹⁰Pb | 210 | [Open] | [Open] | Low | β⁻ |
| 13 | ²¹⁰Bi | 210 | [Open] | [Open] | Low | β⁻ |
| 14 | ²¹⁰Po | 210 | [Open] | [Open] | Low | Final α |
| END | ²⁰⁶Pb | 206 | [Open] ≈ 36? | Allowed? | Zero | Stable |

**Key Hypothesis [P]**: As A decreases, effective coordination n(A) moves from forbidden zone toward allowed, reducing frustration and enabling stability at ²⁰⁶Pb.

---

## 3. EDC Law Application: Frustration-Corrected G-N

**Citation**: MTR-002 (22826edd_full.md:2560-2660)

For each α-decay step, the EDC law applies:

```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f(A) + b

With: a = 1.63, c = -2.40, b = -42.1
```

### Application Example [Open]

For ²³⁸U → ²³⁴Th:
- Z = 92
- Q_α = [BL] external data required
- ε_f(238) = [Open] - requires n(238) formula (GAP-R1)

**Predicted trend**: Higher A nuclei (near n ≈ 43) have higher ε_f, which with c < 0 gives longer half-lives.

### Pattern Across Chain

| α-Step | Parent | Z | Q (MeV) | ε_f(A) | Predicted t₁/₂ Trend |
|--------|--------|---|---------|--------|---------------------|
| 1 | ²³⁸U | 92 | [BL] | High | Very long (10⁹ y) |
| 4 | ²³⁴U | 92 | [BL] | High | Long (10⁵ y) |
| 5 | ²³⁰Th | 90 | [BL] | Medium-High | Long (10⁴ y) |
| 6 | ²²⁶Ra | 88 | [BL] | Medium | Medium (10³ y) |
| 7 | ²²²Rn | 86 | [BL] | Medium | Short (days) |
| 8 | ²¹⁸Po | 84 | [BL] | Lower | Very short (min) |
| 11 | ²¹⁴Po | 84 | [BL] | Lower | Ultra-short (μs) |
| 14 | ²¹⁰Po | 84 | [BL] | Low | Short (days) |

**Observation [I]**: The G-N law predicts lifetime decrease as Z decreases and ε_f decreases. Consistent with chain pattern.

---

## 4. Open Questions for This Chain

1. **What is n(238) exactly?** [Open]
   - Need formula linking A, ρ to effective coordination
   - GAP-R1 blocking

2. **Why does β⁻ alternate with α?** [Open]
   - EDC currently focuses on α; β⁻ mechanism needs development
   - Hypothesis [P]: β⁻ fine-tunes n toward allowed

3. **Is ²⁰⁶Pb at allowed n?** [Open]
   - If n(206) ≈ 36 (allowed), explains stability
   - Requires calculation

---

## 5. Data TODO

- [ ] Ingest NNDC data for all half-lives
- [ ] Ingest Q values for all α-decays
- [ ] Calculate n(A) from nuclear density formula
- [ ] Compute ε_f(A) once GAP-R1 is resolved
- [ ] Verify G-N fit for this chain specifically
