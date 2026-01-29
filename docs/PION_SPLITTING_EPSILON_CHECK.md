# Pion Splitting ε-Check — Cheap Breadth Test

**Date:** 2026-01-29
**Purpose:** Test whether ε ≈ 0.679% EM dressing pattern applies to pion mass splitting
**Status:** BREADTH TEST
**Motivation:** `docs/BREADTH_SYNTHESIS_2026-01-29.md` Test 1 (cheap)

---

## A. Executive Summary (5 Bullets)

1. **Pion relative splitting r_π = 3.40%** — about 5× larger than Δm_np's ε = 0.679%
2. **Order-of-magnitude match** — r_π/ε ≈ 5.0 is within [0.1, 10] range
3. **Structural factor k ~ 5 required** — plausible from combinatorics (e.g., N_Dirac + 1 = 5)
4. **Alternative pattern: r_π ≈ 4α × 1.17** — connects directly to the 4α term in Δm_np
5. **Verdict: YELLOW** — same-order match but factor ~5 needs geometric explanation

---

## B. Baseline [BL]: Pion Masses

### B.1 PDG Values

| Quantity | Value | Source |
|----------|-------|--------|
| m_π± | 139.570 MeV | PDG 2024 [BL] |
| m_π0 | 134.977 MeV | PDG 2024 [BL] |
| Δm_π = m_π+ − m_π0 | **4.593 MeV** | PDG 2024 [BL] |

### B.2 Relative Splitting

```
r_π = Δm_π / m_π0 = 4.593 / 134.977 = 0.03403 = 3.403%
```

Alternative (using average mass):
```
m_π_avg = (139.570 + 134.977)/2 = 137.27 MeV
r_π' = Δm_π / m_π_avg = 4.593 / 137.27 = 0.03346 = 3.35%
```

**Working value:** r_π ≈ 3.40%

---

## C. Comparison to ε = 0.679%

### C.1 ε Reference

From `docs/DELTA_MNP_RECONCILIATION.md`:
```
ε = 0.00679 = 0.679%

Interpretation: ε bridges bare geometry (8/π) and EM-dressed result (5/2+4α)
```

### C.2 Ratio Computation

```
r_π / ε = 3.403% / 0.679% = 5.01 ≈ 5
```

**Assessment:**
- r_π is about **5× larger** than ε
- This is within one order of magnitude (ratio ∈ [0.1, 10])
- Suggests **same-family** EM correction with a structural multiplier

### C.3 Alternative: Compare to 4α

The Δm_np dimensional formula contains 4α as the EM correction term:
```
4α = 4 × 0.007297 = 0.02919 = 2.919%
```

Compare:
```
r_π / (4α) = 3.403% / 2.919% = 1.166 ≈ 7/6
```

**Observation:** r_π ≈ (7/6) × 4α, remarkably close to unity!

This suggests the pion splitting may share the same 4α EM origin as Δm_np, with a geometric factor ~7/6.

---

## D. Structural Mappings (No Derivations)

### D.1 Multiplicative Dressing: m = m_bare(1 + kε)

If pion mass splitting arises from ε-type dressing:
```
Δm_π = m_π0 × k × ε
4.593 = 134.977 × k × 0.00679
k = 4.593 / (134.977 × 0.00679) = 5.01
```

**Result:** k ≈ 5 (O(1–10), acceptable)

**Candidate meanings of k = 5:**
- N_Dirac + 1 = 4 + 1 = 5 (spinor components + scalar)
- Combinatorial factor from double-well (n = 2) × geometry

### D.2 Additive Dressing: Δm ~ kε × E_scale

#### Using E_σ = m_e/α = 70 MeV (EDC hadronic scale)

```
Δm_π = k × ε × E_σ
4.593 = k × 0.00679 × 70.03
k = 4.593 / 0.475 = 9.67
```

**Result:** k ≈ 10 (O(1–10), acceptable)

#### Using m_π0 as E_scale

```
k = 4.593 / (0.00679 × 134.977) = 5.01
```

**Result:** k ≈ 5 (same as multiplicative)

### D.3 Alternative: Use 4α Directly

If the EM dressing factor is 4α (not ε):
```
Δm_π = k' × (4α) × m_π0
4.593 = k' × 0.02919 × 134.977
k' = 4.593 / 3.941 = 1.166
```

**Result:** k' ≈ 7/6 (very close to unity!)

This is the most economical mapping:
```
Δm_π ≈ (7/6) × 4α × m_π0   [I]
```

### D.4 Summary Table

| Mapping | E_scale | k required | Plausibility |
|---------|---------|------------|--------------|
| m_bare(1 + kε) | m_π0 | k = 5 | MEDIUM (needs k explanation) |
| kε × E_σ | 70 MeV | k = 10 | MEDIUM |
| k' × 4α × m_π | m_π0 | k' = 7/6 | HIGH (near-unity) |

---

## E. Consistency with Δm_np Pattern

### E.1 Both Contain 4α

| Quantity | Formula | 4α Role |
|----------|---------|---------|
| Δm_np | (5/2 + 4α)m_e | Additive EM correction |
| Δm_π | (7/6) × 4α × m_π0 [?] | Multiplicative EM correction |

### E.2 Ratio of Splittings

```
Δm_π / Δm_np = 4.593 / 1.293 = 3.55

Compare to:
m_π0 / m_e = 134.977 / 0.511 = 264.1
(m_π0/m_e) × (7/6)/(5/2+4α) = 264.1 × 1.167/2.529 = 122

Not matching — different structural origin
```

**Conclusion:** Pion and nucleon splittings share 4α as EM scale but have different geometric prefactors.

---

## F. Conclusion

### F.1 Verdict: **YELLOW**

| Criterion | Status |
|-----------|--------|
| r_π within order of magnitude of ε | YES (ratio = 5) |
| k factor is O(1–10) | YES (k = 5–10) |
| Near-unity factor exists | YES (k' = 7/6 with 4α) |
| Geometric explanation for k | NO (open) |

### F.2 Why Not GREEN

The factor k = 5 (or k' = 7/6) lacks first-principles derivation. Two interpretations exist:
1. ε-based with k = 5 (needs combinatorial explanation)
2. 4α-based with k' ≈ 1 (more economical but needs geometric grounding)

### F.3 Next Refinement

1. Check if factor 7/6 appears elsewhere in EDC (e.g., as 1 + 1/|Z_6| = 1 + 1/6)
2. Look for pion mass formula in existing EDC canon (Book 1 Ch.9, Companion H)
3. Test whether Δm_π / Δm_np ratio has clean form in Z_6 geometry

---

## G. Reference Anchors

| Document | Content |
|----------|---------|
| `docs/DELTA_MNP_RECONCILIATION.md` | ε = 0.679%, 4α interpretation |
| `docs/BREADTH_SYNTHESIS_2026-01-29.md` | Test 1 motivation |
| `docs/OP-SIGMA-2_NCELL12_RESOLUTION.md` | N_cell = 12 bridge context |
| `docs/SIGMA_DEPENDENCY_AUDIT.md` | E_σ = 70 MeV scale |

---

*This document tests whether the ε ≈ 0.68% EM dressing pattern from Δm_np applies to pion splitting. Result: YELLOW — same order of magnitude but structural factor needs explanation.*
