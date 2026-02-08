# DATA GAPS (V7.3)

**Created**: 2026-01-31
**Purpose**: Document missing BL data and expansion candidates
**Status**: [Open] gaps requiring future resolution

---

## Critical Gaps

### Gap 1: H1/H2 Sample Size

| Class | Current | Target | Shortfall |
|-------|---------|--------|-----------|
| H1 | 4 | ≥8 | 4 nuclides |
| H2 | 2 | ≥3 | 1 nuclide |

**Impact**: Reduced statistical power for hindrance-controlled d(n) testing.

**Physics limitation**: Ground-state-to-ground-state α-decays with parity change (H1) or large ΔJ (H2) are intrinsically rare because:
1. Such transitions are kinetically suppressed
2. Competing decay modes (β, EC) often dominate
3. Pure α-emitters with these characteristics are uncommon

---

## Candidate Nuclides for H1 Expansion

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | Class | Issue |
|---------|-------|-------|----|----|-------|-------|
| ²⁴⁵Am | (5/2⁻?) | 5/2⁺ | 0 | Y | H1 | Jπ(P) uncertain |
| ²⁴⁷Am | (5/2⁻?) | 5/2⁺ | 0 | Y | H1 | Jπ(P) uncertain |
| ²⁵³Es | 7/2⁺ | (7/2⁺?) | 0? | ? | ? | Jπ(D) uncertain |
| ²⁴⁷Bk | (3/2⁻) | 7/2⁺ | 2 | Y | H1 | Low α-BR (needs check) |
| ²⁵⁵Fm | (7/2⁺) | (7/2⁺?) | 0? | ? | ? | Both Jπ uncertain |

**Required BL**: Firm Jπ assignments for these candidates from ENSDF evaluation.

---

## Candidate Nuclides for H2 Expansion

| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | Issue |
|---------|-------|-------|----|----|-------|
| ²¹³Bi | 9/2⁻ | 1/2⁺ | 4 | Y | α-BR = 2.14% (below threshold) |
| ²¹⁷Bi | (9/2⁻?) | ? | ? | ? | No BL data available |
| ²¹¹Rn | (1/2⁻?) | ? | ? | ? | Short-lived, data sparse |

**Challenge**: H2 candidates are rare because high-ΔJ α-transitions have extremely small partial widths.

---

## Intermediate Nuclides (Chain Members)

### U-238 Chain Gaps

| Nuclide | Role | Missing Data |
|---------|------|--------------|
| Th-234 | β-emitter | t₁/₂ verified, no α-decay |
| Pa-234m | Isomer | Complex decay scheme |
| At-218 | Minor branch | ✓ Added in V7.3 |
| Tl-210 | β-emitter | No α-decay mode |

### Th-232 Chain Gaps

| Nuclide | Role | Missing Data |
|---------|------|--------------|
| Ac-228 | β-emitter | No significant α-BR |
| Tl-208 | β-emitter | No α-decay mode |
| Po-212 | ✓ In dataset | Complete |

### U-235 Chain Gaps

| Nuclide | Role | Missing Data |
|---------|------|--------------|
| Th-231 | β-emitter | No significant α-BR |
| Pa-231 | α-emitter | Candidate for expansion |
| Ac-227 | Mixed | Candidate for expansion |
| Tl-207 | β-emitter | No α-decay mode |

---

## Expansion Candidates (High Priority)

### Group A: Known Jπ, Need Verification

| Nuclide | Z | A | Jπ(P) | Jπ(D) | H-class | Priority |
|---------|---|---|-------|-------|---------|----------|
| Pa-231 | 91 | 231 | 3/2⁻ | 5/2⁻ | H0 | High |
| Ac-227 | 89 | 227 | 3/2⁻ | 3/2⁺ | H1 | High |
| Np-239 | 93 | 239 | 5/2⁺ | 5/2⁺ | H0 | Medium |
| Es-254 | 99 | 254 | (7⁺) | ? | ? | Low |

### Group B: Need α-BR Verification

| Nuclide | Reported α-BR | Threshold | Status |
|---------|---------------|-----------|--------|
| Bi-213 | 2.14% | ≥5% | Excluded |
| Bk-249 | 0.001% | ≥5% | Excluded |
| Fm-255 | ~100% | OK | Jπ uncertain |
| Md-256 | ~90% | OK | Jπ uncertain |

---

## Power Analysis Implications

### Current Status
```
n = 45 nuclides
r = -0.28 (observed correlation)
Power at α=0.05: ~52%
```

### Required for 80% Power
```
n ≈ 100 nuclides
With similar effect size and variance
```

### Expansion Strategy

| Phase | Target n | Source |
|-------|----------|--------|
| V7.3 | 45 | Complete |
| V7.4 (proposed) | 60 | Add Pa, Ac, more Bk/Es/Fm |
| V7.5 (proposed) | 80 | Include isomer decays? |
| V7.6 (theoretical) | 100 | Requires relaxed criteria? |

---

## Data Quality Requirements

### Minimum Criteria (Maintained from V7.2)

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| α-BR | ≥ 5% | Reliable t₁/₂(α) calculation |
| Jπ(P) | Firm assignment | Hindrance classification |
| Jπ(D) | Firm assignment | ΔJ and ΔΠ determination |
| t₁/₂ uncertainty | < 10% | G-N fit quality |
| Qα uncertainty | < 0.1% | G-N fit quality |

### Relaxation Options (Not Recommended)

| Criterion | Relaxed value | Risk |
|-----------|---------------|------|
| α-BR | ≥ 1% | Higher t₁/₂ uncertainty |
| Jπ | Parenthetical () | Misclassification |
| t₁/₂ | ≤ 20% | G-N fit degradation |

---

## BL Source Limitations

### Available in NuDat3/ENSDF

| Data type | Coverage | Notes |
|-----------|----------|-------|
| Ground-state t₁/₂ | Excellent | For Z ≤ 102 |
| Qα values | Excellent | AME2020 complete |
| Jπ assignments | Good | Some parenthetical |
| α-BR | Good | Some uncertain |

### Not Available

| Data type | Issue |
|-----------|-------|
| Isomer-to-ground α-decay | Partial coverage |
| Jπ for Z > 102 | Largely uncertain |
| α-BR for minor branches | Often unmeasured |

---

## Recommendations

### For V7.3 Completion
No additional data required. Current 45-nuclide dataset is complete for specified analysis.

### For Future Expansion (V7.4+)

1. **Priority 1**: Add Pa-231 and Ac-227 (known Jπ, chain members)
2. **Priority 2**: Seek H1 candidates with firm Jπ (Am-245, Am-247 if confirmed)
3. **Priority 3**: Consider isomer decays if g.s.-g.s. pool exhausted

### For H2 Expansion
Acknowledge physics limitation: true H2 ground-state α-emitters are extremely rare. The 2 identified (Po-211, Cf-251) may represent most of the accessible population.

---

## Summary

| Gap Category | Count | Resolvable? |
|--------------|-------|-------------|
| H1 shortfall | 4 | Partially (2-3 candidates) |
| H2 shortfall | 1 | Unlikely (physics limited) |
| Chain intermediates | ~10 | Most are β-emitters |
| Power deficit | ~55 nuclides | Requires relaxed criteria |

Status: [Open] — gaps documented for future work

