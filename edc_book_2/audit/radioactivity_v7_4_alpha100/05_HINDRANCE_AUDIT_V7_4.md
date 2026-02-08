# HINDRANCE AUDIT (V7.4)

**Created**: 2026-01-31
**Purpose**: Document H0/H1/H2 classification for α100 dataset
**Status**: [Der] using V7.2/V7.3 rules

---

## Classification Rules (Inherited)

```
H0: ΔJ ≤ 2 AND no parity change (Favored)
H1: ΔJ ≤ 2 AND parity change (First-forbidden equivalent)
H2: ΔJ > 2 (Highly hindered)
```

Where:
- ΔJ = |J(parent) - J(daughter)|
- Parity change = one + and one − between parent and daughter

---

## Classification Summary

| Class | V7.3 | V7.4 Added | V7.4 Total | Fraction |
|-------|------|------------|------------|----------|
| H0 | 39 | 43 | 82 | 80.4% |
| H1 | 4 | 4 | 8 | 7.8% |
| H2 | 2 | 10 | 12 | 11.8% |
| **Total** | **45** | **57** | **102** | 100% |

---

## H2 Nuclides (12 total)

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | L_min | Source |
|---------|-------|-------|----|----|-------|--------|
| Po-211 | 9/2⁺ | 1/2⁻ | 4 | Y | 5 | V7.3 |
| Cf-251 | 1/2⁺ | 9/2⁻ | 4 | Y | 5 | V7.3 |
| Bi-211 | 9/2⁻ | 1/2⁺ | 4 | Y | 5 | V7.4 |
| Bi-212 | 1⁻ | 5⁺ | 4 | Y | 5 | V7.4 |
| At-212 | 1⁻ | 5⁺ | 4 | Y | 5 | V7.4 |
| Rn-213 | 9/2⁺ | 1/2⁻ | 4 | Y | 5 | V7.4 |
| Np-236 | 6⁻ | 2⁻ | 4 | N | 4 | V7.4 |
| Es-250 | 6⁺ | 2⁻ | 4 | Y | 5 | V7.4 |
| Es-252 | 5⁻ | 1⁺ | 4 | Y | 5 | V7.4 |
| Es-254 | 7⁻ | 2⁻ | 5 | N | 5 | V7.4 |
| Fm-253 | 1/2⁺ | 9/2⁻ | 4 | Y | 5 | V7.4 |
| Fm-255 | 7/2⁺ | 1/2⁺ | 3 | N | 3 | V7.4 |

**L_min calculation**: L_min = ΔJ if no parity change; L_min = ΔJ+1 if parity change and L must be odd.

---

## H1 Nuclides (8 total)

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | L_min | Source |
|---------|-------|-------|----|----|-------|--------|
| U-235 | 7/2⁻ | 5/2⁺ | 1 | Y | 1 | V7.2 |
| Am-241 | 5/2⁻ | 5/2⁺ | 0 | Y | 1 | V7.2 |
| Am-243 | 5/2⁻ | 5/2⁺ | 0 | Y | 1 | V7.2 |
| Cf-249 | 9/2⁻ | 7/2⁺ | 1 | Y | 1 | V7.3 |
| Fr-220 | 1⁺ | 1⁻ | 0 | Y | 1 | V7.4 |
| Ac-224 | 0⁻ | 1⁺ | 1 | Y | 1 | V7.4 |
| Cm-247 | 9/2⁻ | 7/2⁺ | 1 | Y | 1 | V7.4 |
| Es-255 | 7/2⁺ | 3/2⁻ | 2 | Y | 3 | V7.4 |

---

## H0 Nuclides (82 total)

All nuclides satisfying ΔJ ≤ 2 AND no parity change.

### By Element

| Element | H0 Count | Examples |
|---------|----------|----------|
| Po | 11 | Po-206, Po-208, Po-210, Po-212, Po-214, Po-216, Po-218 |
| At | 8 | At-207, At-209, At-210, At-211, At-213, At-215, At-217, At-219 |
| Rn | 12 | Rn-210, Rn-211, Rn-212, Rn-214, Rn-215, Rn-216, Rn-218, Rn-220, Rn-222 |
| Fr | 4 | Fr-212, Fr-217, Fr-218, Fr-221 |
| Ra | 6 | Ra-220, Ra-221, Ra-222, Ra-223, Ra-224, Ra-226 |
| Ac | 2 | Ac-223, Ac-225 |
| Th | 6 | Th-226, Th-227, Th-228, Th-229, Th-230, Th-232 |
| Pa | 2 | Pa-227, Pa-231 |
| U | 6 | U-230, U-232, U-233, U-234, U-236, U-238 |
| Np | 1 | Np-237 |
| Pu | 6 | Pu-236, Pu-238, Pu-239, Pu-240, Pu-242, Pu-244 |
| Cm | 7 | Cm-242, Cm-243, Cm-244, Cm-245, Cm-246, Cm-248, Cm-250 |
| Bk | 3 | Bk-245, Bk-246, Bk-247 |
| Cf | 2 | Cf-250, Cf-252 |
| Es | 2 | Es-251, Es-253 |
| Fm | 4 | Fm-252, Fm-254, Fm-256, Fm-257 |
| **Total** | **82** | — |

---

## Expected Effect on G-N Residuals

Based on V7.3 predictions:
- H0: Residuals near zero (baseline)
- H1: Positive residuals (slower decay due to parity barrier)
- H2: Large positive residuals (much slower due to high L)

### Observed Pattern (α102)

| Class | n | Mean Residual | SD | Expected |
|-------|---|---------------|-----|----------|
| H0 | 82 | -0.08 | 0.72 | ~0 |
| H1 | 8 | +0.76 | 0.48 | >0 |
| H2 | 12 | +1.28 | 0.65 | >>0 |

**Result**: Pattern is as expected. H1 and H2 have positive residuals relative to H0 baseline.

---

## Comparison with V7.3

| Metric | V7.3 | V7.4 | Change |
|--------|------|------|--------|
| H1 count | 4 | 8 | +4 |
| H2 count | 2 | 12 | +10 |
| H1+H2 total | 6 | 20 | +14 |
| H1+H2 target | ≥12 | ≥12 | — |
| Status | ✗ Short | ✓ Met | **Resolved** |

---

## Key H2 Sources

### How H2 expanded from 2 to 12:

1. **Transuranics with high ΔJ**: Np-236, Es-250, Es-252, Es-254, Fm-253, Fm-255
2. **Lighter elements in chains**: Bi-211, Bi-212, At-212, Rn-213
3. **Original V7.3**: Po-211, Cf-251

The transuranics (Z ≥ 93) are particularly rich in H2 candidates because:
- Odd-odd ground states often have unusual Jπ
- Daughters may have very different Jπ due to shell effects
- Many are sufficiently long-lived for measurement

---

## AC4 Evaluation

| Criterion | Target | Achieved | Status |
|-----------|--------|----------|--------|
| H1+H2 ≥ 12 | 12 | 20 | ✓ PASS |

**Conclusion**: AC4 fully met with 67% margin.

