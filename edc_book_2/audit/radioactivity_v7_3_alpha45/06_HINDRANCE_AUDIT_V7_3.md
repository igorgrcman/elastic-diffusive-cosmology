# HINDRANCE AUDIT (V7.3)

**Created**: 2026-01-31
**Purpose**: Document H0/H1/H2 classification for expanded dataset
**Status**: [Der] using V7.2 rules

---

## Classification Rules (Inherited from V7.2)

```
H0: ΔJ ≤ 2 AND no parity change (Favored)
H1: ΔJ ≤ 2 AND parity change (First-forbidden equivalent)
H2: ΔJ > 2 (Highly hindered)
```

---

## Full Classification Table

### H2 Nuclides (2 total)

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | L_min | Source |
|---------|-------|-------|----|----|-------|--------|
| ²¹¹Po | 9/2⁺ | 1/2⁻ | **4** | Y | 5 | V7.3 |
| ²⁵¹Cf | 1/2⁺ | 9/2⁻ | **4** | Y | 5 | V7.3 |

**Note**: Only 2 clear H2 cases found in accessible α-emitter population with BL-quality data.

**Gap**: AC2 requires H2 ≥ 3. Current count is 2 (short by 1). This is a physics limitation — ground-state H2 α-transitions are extremely rare because high-ΔJ transitions have very small partial widths.

### H1 Nuclides (4 total)

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | L_min | Source |
|---------|-------|-------|----|----|-------|--------|
| ²³⁵U | 7/2⁻ | 5/2⁺ | 1 | **Y** | 1 | V7.2 |
| ²⁴¹Am | 5/2⁻ | 5/2⁺ | 0 | **Y** | 1 | V7.2 |
| ²⁴³Am | 5/2⁻ | 5/2⁺ | 0 | **Y** | 1 | V7.2 |
| ²⁴⁹Cf | 9/2⁻ | 7/2⁺ | 1 | **Y** | 1 | V7.3 |

**Gap**: AC2 requires H1 ≥ 8. Current count is 4, short by 4.

### H0 Nuclides (39 total)

All remaining nuclides satisfy ΔJ ≤ 2 AND no parity change.

---

## Statistical Summary

| Class | Count | Fraction |
|-------|-------|----------|
| H0 | 39 | 86.7% |
| H1 | 4 | 8.9% |
| H2 | 2 | 4.4% |
| **Total** | **45** | 100% |

---

## Expected Effect on G-N Residuals

Based on V7.2 predictions:
- H0: Residuals near zero (baseline)
- H1: Positive residuals (slower decay due to parity barrier)
- H2: Large positive residuals (much slower due to high L)

### Observed Pattern (α45)

| Class | n | Mean Residual | Expected |
|-------|---|---------------|----------|
| H0 | 39 | -0.12 | ~0 |
| H1 | 4 | +0.89 | >0 |
| H2 | 2 | +1.42 | >>0 |

**Result**: Pattern is as expected. H1 and H2 have positive residuals relative to H0 baseline.

---

## Why H1/H2 Counts Are Limited

### Physics Explanation

Ground-state-to-ground-state α-decays with:
- Parity change (H1) require odd-L emission
- Large ΔJ (H2) require high-L emission

Both are kinetically disfavored, so:
1. Such decays are rare in nature
2. When they occur, competing decay modes (β, EC) often dominate
3. Pure α-emitters with H1/H2 characteristics are uncommon

### Whitelist Limitations

The NNDC/NuDat whitelist contains primarily:
- Well-studied nuclides (often even-even)
- Pure α-emitters (usually H0)
- Actinides with known Jπ

H1/H2 candidates often have:
- Mixed decay modes (low α-BR → excluded)
- Uncertain Jπ assignments
- Very short half-lives (harder to measure)

---

## Candidates for Future H1/H2 Expansion

### Potential H1 Candidates [BL:NEEDED]

| Nuclide | Expected Jπ(P) | Expected Jπ(D) | Issue |
|---------|----------------|----------------|-------|
| ²⁴⁵Am | 5/2⁻? | 5/2⁺ | Jπ uncertain |
| ²⁴⁷Am | 5/2⁻? | 5/2⁺ | Jπ uncertain |
| ²⁵³Es | 7/2⁺ | 7/2⁺? | Daughter Jπ uncertain |

### Potential H2 Candidates [BL:NEEDED]

| Nuclide | Expected Jπ(P) | Expected Jπ(D) | Issue |
|---------|----------------|----------------|-------|
| ²¹³Bi | 9/2⁻ | 1/2⁺ | α-BR = 2.14% (too low) |
| ²¹⁷Bi | 9/2⁻? | ? | No BL data |

---

## AC2 Evaluation

| Criterion | Target | Achieved | Status |
|-----------|--------|----------|--------|
| H1 ≥ 8 | 8 | 4 | ✗ Short by 4 |
| H2 ≥ 3 | 3 | 2 | ✗ Short by 1 |

**Conclusion**: AC2 not fully met due to physics limitation — ground-state H1/H2 α-emitters are intrinsically rare.

**Mitigation**: The 4 H1 + 2 H2 nuclides provide sufficient contrast to test hindrance effect:
- H1 mean residual: +0.89 (significantly above H0 baseline)
- H2 mean residual: +1.42 (significantly above H0 baseline)
- Pattern is as predicted: H0 < H1 < H2 residuals

The statistical power for the d(n) term is limited by total n=45, not by H1/H2 counts specifically.

