# V7.8 MEDIATION AND INTERPRETATION

**Created**: 2026-01-31
**Purpose**: Mechanistic interpretation of V7.8 results

---

## Executive Summary

V7.8 tested whether the d(n) effect (g < 0, faster decay for higher coordination distance) is:
1. Confounded with nuclear deformation
2. Mediated by α-preformation probability
3. Independent of both

**Result**: d(n) is **ROBUST** — it survives inclusion of both proxies, suggesting it captures genuine topological information beyond standard nuclear structure parameters.

---

## Scenario Analysis

### Scenario A: Deformation Collapse ❌

**Hypothesis**: d(n) is just a proxy for nuclear deformation.

**Expected signature**:
- In M5, g becomes non-significant when proxy_deform is added
- proxy_deform remains significant

**Observed**:
- g = -1.46, p = 0.001 (still significant)
- proxy_deform: p = 0.67 (NOT significant)

**Verdict**: **REJECTED** — d(n) is not simply a deformation proxy. In fact, the opposite occurs: proxy_deform becomes non-significant when d(n) is included, suggesting d(n) captures deformation-related variance (and more).

---

### Scenario B: S_α Mediation ❌ (Partial)

**Hypothesis**: d(n) effect is mediated by preformation probability.

**Expected signature**:
- In M6, g shrinks substantially (>30%)
- proxy_Salpha significant and g reduced

**Observed**:
- g = -1.53, p < 0.001 (essentially unchanged)
- proxy_Salpha: p = 0.05 (marginally significant)
- Δg = 7.2% (minimal reduction)

**Verdict**: **PARTIAL SUPPORT** — proxy_Salpha adds marginal predictive value independent of d(n), but does not mediate the d(n) effect. The V7.7 hypothesis that d(n) acts through S_α is not falsified, but the Royer proxy doesn't fully capture the mechanism.

---

### Scenario C: Robust Independence ✓

**Hypothesis**: d(n) captures topological information beyond standard proxies.

**Expected signature**:
- g remains significant in M7 (full model)
- Minimal change in g magnitude

**Observed**:
- g = -1.71, p < 0.001
- Change from M2: -4.2% (actually slightly stronger!)

**Verdict**: **CONFIRMED** — d(n) is robust to both deformation and S_α controls.

---

## Mechanistic Interpretation

### What d(n) Captures

Based on V7.8 results, d(n) encapsulates information that is:

1. **Not just deformation**
   - proxy_deform (shell distance product) becomes non-significant with d(n)
   - d(n) absorbs deformation-related variance
   - But d(n) contains additional information

2. **Not fully S_α**
   - Royer S_α formula captures some independent variance (p = 0.05)
   - But doesn't explain the d(n) effect
   - V7.7 prefactor hypothesis still plausible via non-Royer S_α mechanism

3. **Possibly topological/geometric**
   - The 2^a × 3^b constraint is geometric (hexagonal lattice origin)
   - d(n) measures distance from allowed coordination
   - Effect may be genuine "coordination frustration"

---

## Updated Mechanism Status

| Mechanism | V7.7 Status | V7.8 Status | Reason |
|-----------|-------------|-------------|--------|
| Barrier modification | Disfavored | Disfavored | T3 still applies |
| S_α enhancement (Royer-type) | [P] | Partial [P] | Royer proxy doesn't fully mediate |
| S_α enhancement (other) | [P] | [P] | Compatible with results |
| Deformation confound | [Open] | Rejected | proxy_deform absorbed by d(n) |
| Topological frustration | [P] | Strengthened [P] | Survives controls |

---

## Physical Picture (Updated)

### Before V7.8

```
d(n) → ??? → S_α ↑ → faster decay
```

### After V7.8

```
d(n) → geometric frustration → surface dynamics ↑ → S_α ↑ → faster decay
                ↓
      (not just deformation)
      (not just Royer S_α)
```

The d(n) effect operates through a mechanism that:
- Correlates with but is distinct from deformation
- May enhance S_α, but not via the simple Royer formula
- Is genuinely related to coordination geometry

---

## What This Means for EDC

### Strengthened Claims

1. The n = 2^a × 3^b coordination law has observable consequences
2. Distance from allowed values correlates with decay dynamics
3. The correlation is not a trivial proxy for known nuclear structure

### Remaining Uncertainties

1. **Mechanism**: How does coordination distance affect preformation?
2. **Causation**: Correlation established; causal pathway still [P]
3. **Alternative**: Could there be another structural variable that d(n) proxies?

---

## Falsification Update

### Tests Passed

| Test | Result |
|------|--------|
| d(n) predicts beyond GN | ✓ (p < 0.001) |
| Robust to deformation control | ✓ (g stable, p = 0.001) |
| Robust to S_α control | ✓ (g stable, p < 0.001) |
| Sign consistent (g < 0) | ✓ (all models) |

### Tests Still Open

| Test | Status |
|------|--------|
| Independent S_α measurement | [Open] — Royer is a proxy |
| True β₂ deformation | [Open] — Used shell distance proxy |
| Causal mechanism | [P] — Still hypothetical |

---

## Implications for Book 2

### Can Now Say (with V7.8 backing)

- d(n) effect is robust to standard structure controls
- Not simply a deformation proxy
- Compatible with (but not proven by) topological mechanism

### Should Not Say

- "Proves topological frustration" — still correlation
- "Deformation doesn't matter" — it does, but d(n) captures more
- "S_α mechanism confirmed" — Royer proxy doesn't fully support

---

## Quantitative Summary

| Quantity | M2 | M7 | Change |
|----------|-----|-----|--------|
| g(d(n)) | -1.643 | -1.711 | -4.2% |
| SE(g) | 0.142 | 0.467 | +229% (expected with collinearity) |
| p(g) | <0.001 | <0.001 | Stable |
| R² | 0.9805 | 0.9812 | +0.07% |

**Key finding**: Adding proxies increases SE (collinearity) but g remains significant and stable.

