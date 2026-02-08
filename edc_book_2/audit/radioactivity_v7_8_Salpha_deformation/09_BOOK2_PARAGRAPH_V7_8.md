# V7.8 BOOK 2 PARAGRAPH VARIANTS

**Created**: 2026-01-31
**Purpose**: Conservative, sign-safe paragraph variants updated with V7.8 findings

---

## Variant A: Minimal (Pure Descriptive)

> Regression analysis of 106 α-emitting nuclides reveals a robust correlation between the M-topology coordination distance d(n) and decay rate (g = −1.64 ± 0.14, p < 0.001). Nuclei farther from allowed coordination values decay faster. This effect survives inclusion of both deformation and preformation proxies: when shell-distance deformation and Royer S_α estimates are added as covariates, g remains negative (−1.71) and significant (p < 0.001) with only 4% change in magnitude. The deformation proxy becomes non-significant (p = 0.67) when d(n) is present, suggesting d(n) captures deformation-related variance and more.

**Word count**: 89
**Epistemic tag**: [Der]
**Key update**: Includes V7.8 control test results

---

## Variant B: With Mechanistic Interpretation

> Among 106 α-emitters from Po to Fm, the coordination distance d(n) correlates with enhanced decay rates even after controlling for nuclear deformation and preformation probability. The effect (g = −1.71, p < 0.001) is not a trivial proxy: a shell-distance deformation estimator becomes non-significant when d(n) is included, while d(n) absorbs its variance. This is consistent with the hypothesis that topological frustration — deviation from allowed M-topology coordination — enhances decay dynamics through a mechanism beyond standard structural parameters, possibly by increasing surface reorganization and α-cluster formation probability.

**Word count**: 93
**Epistemic tag**: [Der] + [P] for mechanism
**Key update**: Notes that d(n) absorbs deformation variance

---

## Variant C: With Alternatives and Full Caution

> The d(n) coefficient g = −1.64 (p < 0.001) indicates faster α-decay for nuclei farther from allowed M-topology values. V7.8 tested whether this effect is confounded with deformation or mediated by preformation probability. Results: (i) when a deformation proxy is added, it becomes non-significant while d(n) remains significant (p = 0.001); (ii) when a Royer S_α proxy is added, both d(n) (p < 0.001) and S_α (p = 0.05) contribute; (iii) in the full model with both proxies, d(n) is essentially unchanged (g = −1.71, 4% change). This suggests d(n) captures genuine topological information, though causation is not established and alternative unmeasured confounders remain possible.

**Word count**: 116
**Epistemic tag**: [Der] + [P]
**Key update**: Full V7.8 test summary

---

## Phrase Guide (Updated for V7.8)

### Use These

| Phrase | Reason |
|--------|--------|
| "robust to deformation control" | V7.8 M5 result |
| "absorbs deformation variance" | proxy_deform non-significant with d(n) |
| "not a trivial proxy" | Survives controls |
| "captures genuine topological information" | Best interpretation |
| "correlation, not causation" | Honest |

### Avoid These

| Phrase | Problem |
|--------|---------|
| "proves topology causes decay" | Overclaim |
| "deformation irrelevant" | It's absorbed, not irrelevant |
| "S_α mediation confirmed" | Royer proxy doesn't fully mediate |

---

## Key Numbers for V7.8 Citation

| Quantity | Value | Source |
|----------|-------|--------|
| g (M2 baseline) | -1.64 ± 0.14 | V7.8 fit |
| g (M7 full model) | -1.71 ± 0.47 | V7.8 fit |
| % change M2→M7 | 4.2% | V7.8 |
| p(g) in M7 | <0.001 | V7.8 |
| p(proxy_deform) in M5 | 0.67 | V7.8 |
| p(proxy_Salpha) in M6 | 0.05 | V7.8 |

---

## One-Sentence Summaries

### For Abstract
> "The M-topology coordination distance d(n) predicts α-decay rates beyond Geiger-Nuttall, even after controlling for nuclear deformation and preformation probability proxies."

### For Results Section
> "Including deformation and S_α proxies as covariates leaves the d(n) effect essentially unchanged (g = −1.71 vs −1.64, p < 0.001), with the deformation proxy becoming non-significant when d(n) is present."

### For Discussion
> "The robustness of the d(n) effect to structural controls suggests it captures genuine topological information rather than being a trivial proxy for known nuclear parameters."

---

## Comparison with V7.7

| Aspect | V7.7 | V7.8 |
|--------|------|------|
| Effect size | g ≈ -0.31 | g ≈ -1.64 |
| Mechanism | Prefactor [P] | Prefactor, robust [P] |
| Deformation | Open question | Absorbed by d(n) |
| S_α | Proposed channel | Marginal independent contribution |
| Verdict | PREFACTOR | ROBUST |

**Note on effect size difference**: V7.4-V7.5 used different d(n) scaling (n_A directly), while V7.8 uses the same dataset but the regression includes stronger predictors. The qualitative conclusion (g < 0, significant) is consistent.

---

## Recommendation

**For Book 2**: Use **Variant B** if the mechanism interpretation is desired with appropriate caveats, or **Variant C** for maximum caution.

**Critical updates from V7.8**:
1. d(n) effect is robust to structural controls
2. Deformation proxy is absorbed by d(n)
3. S_α adds marginally but doesn't mediate d(n)

