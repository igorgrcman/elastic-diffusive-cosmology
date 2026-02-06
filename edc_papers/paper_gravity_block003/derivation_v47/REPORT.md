# P48 / Derivation v47: PS Canonicalization — Final Report

## Objective

Convert Pati-Salam into canonical working track after v46 selection:
1. Derive exact gauge-coupling matching relations PS → SM
2. Construct Weinberg-angle hook formula (structural, no numbers)
3. Build PS-specialized G_F closure readiness map

## Zero-Handwave Normalization (HR-P48-N0)

**Hard Rule:** No factor may appear without derivation from:
- Generator normalization: Tr(T^a T^b) = (1/2)δ^ab
- Embedding map: Y = T_3R + (1/2)(B-L)
- Kinetic term matching
- Explicit rescaling

## Trace Ledger

| Generator | Tr(G^2) | Source |
|-----------|---------|--------|
| T_L | 1/2 | SU(2)_L fundamental |
| T_R | 1/2 | SU(2)_R fundamental |
| T_3R | 1/2 | SU(2)_R component |
| (B-L) | 4/3 | SU(4)_C fundamental |
| Y | 5/6 | Embedding sum |

## Coupling Matching

### Final Formula
```
1/g_Y^2 = 3/(5g_R^2) + 4/(5g_{B-L}^2)
```

### Factor Derivation
- `3/5` = Tr(T_3R^2) / Tr(Y^2) = (1/2) / (5/6) = 3/5
- `4/5` = (1/2) * Tr((B-L)^2) / Tr(Y^2) = (1/2) * (4/3) / (5/6) = 4/5

### Two-Route Verification
- Route 1 (Current-sum): MATCH
- Route 2 (Kinetic diagonalization): MATCH

## Weinberg Hook

### Structural Formula
```
sin^2(theta_W) = 1 / (1 + g_L^2 * (3/(5g_R^2) + 4/(5g_{B-L}^2)))
```

### Prerequisites (6 items)
1. g_L(μ_match)
2. g_R(μ_match)
3. g_{B-L}(μ_match)
4. μ_match (from L)
5. KK threshold corrections
6. Brane kinetic terms (if present)

## G_F Readiness Map

| Component | Status | Blocking? |
|-----------|--------|-----------|
| PS track selection | FIXED (v46) | No |
| Hypercharge matching | DERIVED (v47) | No |
| G_F sum structure | DERIVED (v34) | No |
| g_5 → g_4 relation | DERIVED (v36) | No |
| g_5 fixing | OPEN | Yes |
| L from β,λ | OPEN | Yes |
| KK sum convergence | OPEN | Yes |
| Brane kinetic terms | OPEN | Maybe |

## Dimension Sentinels

| Quantity | Expected | Computed | Status |
|----------|----------|----------|--------|
| g_4 | 0 | 0 | PASS |
| g_5^2 | -1 | -1 | PASS |
| G_F | -2 | -2 | PASS |
| L | -1 | -1 | PASS |
| m_n | 1 | 1 | PASS |
| I_overlap | 0 | 0 | PASS |

## Verification Results

```
Total: 38/38 CHECKS PASSED
Check count requirement (>=35): PASS

v45 hash: a80b3886903152d3
v46 hash: 2742edea37e863ac
v47 tables hash: 7a9682f333d5349e
```

## Metrics Achieved

| Metric | Required | Achieved | Status |
|--------|----------|----------|--------|
| Pages | ≥24 | 26 | ✓ |
| Equations | ≥160 | 194 | ✓ |
| Labels | ≥240 | 303 | ✓ |
| Checks | ≥35 | 38 | ✓ |
| Traps | ≥18 | 18 | ✓ |

## Reviewer Traps (18)

1. Trace normalization convention
2. (B-L) not canonically normalized
3. Factor of 1/2 in embedding
4. Cross-term vanishing
5. 3/5 and 4/5 factors (not SU(5))
6. Kinetic vs current matching
7. Weinberg angle at matching scale
8. LR symmetry assumption
9. g_5 dimension
10. g_4 from g_5
11. KK mass spectrum
12. G_F sum convergence
13. Overlap integral normalization
14. Brane kinetic terms
15. PS vs SU(5) normalization
16. Two U(1) mixing
17. Trace in which rep
18. No numerical Weinberg angle

## Files Produced

- `main.tex` — Main document (1300+ lines)
- `main.pdf` — Compiled PDF (26 pages)
- `recompute.py` — Verification engine + 38 checks
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V47_PS_COUPLING_MATCHING_WEINBERG_HOOK_GF_READINESS.pdf` — Export
- `README.md`, `REPORT.md`, `ACCEPTANCE.md` — Documentation

## Conclusion

Pati-Salam is now the canonical working track with:
1. **Coupling matching:** Complete with zero-handwave trace audit
2. **Weinberg hook:** Structural formula ready for numerical evaluation
3. **G_F readiness:** Clear path with 3 blocking items identified

The weak sector closure path:
```
v47 → g_5 fix → routes A/B/C → L fix → v30 → G_F sum → numerical closure
```
