# BOOK 2 PARAGRAPH VARIANTS (V7.7)

**Created**: 2026-01-31
**Purpose**: Sign-safe paragraph variants with prefactor interpretation
**Status**: [Der] for results, [P] for mechanism

---

## Variant A: Minimal (Pure Descriptive)

> Regression analysis of 102 α-emitting nuclides reveals a statistically significant correlation between the M-topology coordination distance d(n) and decay rate (g = −0.31 ± 0.11, p = 0.006). Nuclei with coordination indices farther from allowed values decay *faster*, not slower. This result survives cross-validation (ΔRMSE = 0.043), permutation testing (p_perm = 0.006), and control for parity classes. Model comparison favors an additive (prefactor-like) placement of d(n) in the rate equation over a multiplicative (barrier-like) placement by ΔAIC = 3.4.

**Word count**: 78
**Epistemic tag**: [Der]
**Phrases avoided**: ✓ No "impedes", "stabilizes", "longer half-life"

---

## Variant B: With Prefactor Interpretation

> Among 102 α-emitters from Po to Fm, the coordination distance d(n) correlates with enhanced decay rates: each unit increase in d(n) reduces half-life by a factor of approximately two. Statistical tests favor a prefactor interpretation — d(n) most likely modulates the α-preformation probability S_α rather than barrier penetrability. Physically, this is consistent with "frustration dynamics": nuclei deviating from allowed M-topology values experience enhanced surface reorganization, facilitating α-cluster formation. The effect is strongest in unhindered (H0) transitions, where it is not masked by angular momentum selection rules.

**Word count**: 89
**Epistemic tag**: [Der] + [P] for mechanism
**Note**: "frustration dynamics" and "preformation probability" are proposed interpretations.

---

## Variant C: With Alternatives and Caution

> The d(n) coefficient g = −0.31 (p = 0.006) indicates that α-decay proceeds faster, not slower, for nuclei farther from allowed M-topology values. Three interpretations remain viable: (i) frustration enhances preformation probability S_α through surface dynamics (supported by model comparison, AIC Δ = 3.4); (ii) d(n) proxies for unmeasured nuclear structure such as deformation or residual pairing; (iii) the correlation is statistical coincidence despite passing cross-validation and permutation tests. The first interpretation is currently favored but causation is not established.

**Word count**: 86
**Epistemic tag**: [Der] + [P]
**Note**: Explicitly lists alternatives and caveats.

---

## Phrase Guide

### Use These (Sign-Safe)

| Phrase | Reason |
|--------|--------|
| "decay faster" | Matches g < 0 |
| "enhanced decay rate" | Matches g < 0 |
| "shorter half-life" | Matches g < 0 |
| "frustration enhances" | Matches prefactor direction |
| "preformation probability" | Prefactor channel |
| "correlates with" | Honest (no causation claim) |

### Avoid These (Sign-Unsafe)

| Phrase | Problem |
|--------|---------|
| "impedes tunneling" | Wrong sign |
| "increases barrier" | Rejected by T3 |
| "stabilizes" | Wrong sign |
| "longer half-life" | Wrong sign |
| "forbidden zone protects" | Wrong sign |

---

## Key Numbers for Citation

| Quantity | Value | Source |
|----------|-------|--------|
| g | −0.31 ± 0.11 | V7.4 M2 |
| p-value | 0.006 | V7.4 |
| p_perm | 0.006 | V7.5 |
| ΔRMSE (CV) | 0.043 | V7.5 |
| ΔAIC (A vs B) | −3.4 | V7.6.1 |
| g after parity | −0.29, p = 0.016 | V7.6.1 |
| g in H0 | −0.34 | V7.6.1 |

---

## One-Sentence Summaries

### For Abstract
> "Topological frustration in heavy nuclei correlates with enhanced α-decay rates, consistent with preformation dynamics rather than barrier modification."

### For Introduction
> "The M-topology coordination distance d(n) predicts α-decay rates beyond Geiger-Nuttall, with nuclei farther from allowed values decaying faster."

### For Conclusion
> "The negative d(n) coefficient suggests that frustration accelerates decay, possibly by enhancing α-preformation."

---

## Recommendation

**For Book 2**: Use **Variant B** if mechanism interpretation is desired, or **Variant A** if pure description is preferred.

**Critical**: Do not use any phrases from the "Avoid" list. The sign matters.

