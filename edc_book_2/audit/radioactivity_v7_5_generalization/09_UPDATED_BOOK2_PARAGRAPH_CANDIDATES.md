# UPDATED BOOK 2 PARAGRAPH CANDIDATES (V7.5)

**Created**: 2026-01-31
**Purpose**: Draft paragraphs incorporating V7.4/V7.5 results for potential Book 2 inclusion
**Status**: [Der] — Candidate text only (no Book 2 edits per G2)

---

## Context

These paragraphs summarize the α-decay analysis from V7.4 (n=102 nuclides) and V7.5 (generalization tests). They are candidates for future Book 2 revision, pending author review.

---

## Variant A: Technical Summary

> The M-topology coordination law predicts that nuclear decay rates should depend on the distance $d(n)$ from the coordination index $n(A) = 6.1 \times A^{1/3}$ to the nearest allowed value under $\mathbb{Z}_6$ symmetry. Testing this on 102 α-emitting nuclides from Po to Fm, we find that adding $d(n)$ to the Geiger-Nuttall law with hindrance corrections yields $g = -0.31 \pm 0.11$ (p = 0.006), explaining an additional 0.8% of variance in $\log_{10}(t_{1/2})$. Cross-validation confirms out-of-sample improvement ($\Delta\text{RMSE} = 0.043$), permutation testing excludes chance ($p_\text{perm} = 0.006$), and the effect is robust to outliers, alternative $n(A)$ calibrations, and within-element versus between-element decomposition. The negative sign of $g$ indicates that nuclei with coordination indices farther from allowed values (closer to the forbidden zone) exhibit enhanced decay rates.

**Word count**: 134

**Epistemic tag**: [Der] — Statistical analysis of BL-sourced nuclear data

---

## Variant B: Narrative Emphasis

> Among the 102 α-emitters studied—spanning polonium through fermium—the coordination distance $d(n)$ shows a statistically significant relationship with half-life that persists after controlling for the classical Geiger-Nuttall parameters and nuclear hindrance. Nuclei whose coordination index $n(A)$ falls farther from allowed M-topology values exhibit systematically shorter half-lives, with each unit of $d(n)$ associated with roughly a factor of two increase in decay rate. This effect survives rigorous generalization tests: 10-fold cross-validation, permutation analysis, robust regression, and sensitivity to calibration choices all confirm that the $d(n)$ signal is not an artifact of fitting noise. The within-element analysis further demonstrates that the effect operates among isotopes of the same element, ruling out elemental confounding.

**Word count**: 122

**Epistemic tag**: [Der] — Statistical finding with generalization validation

---

## Variant C: Minimal/Conservative

> Regression analysis of 102 α-emitting nuclides (Z = 84–100) reveals a modest but statistically significant correlation between the M-topology coordination distance $d(n)$ and $\log_{10}(t_{1/2})$, beyond what is explained by the Geiger-Nuttall law and hindrance factors. The coefficient $g = -0.31$ (p = 0.006) indicates that nuclei farther from allowed $n$ values decay more quickly. This finding passes pre-registered generalization criteria including cross-validation, permutation testing, and calibration sensitivity analysis. The effect size corresponds to roughly $\Delta R^2 = 0.008$ (0.8 percentage points of explained variance).

**Word count**: 91

**Epistemic tag**: [Der] — Conservative statement of statistical result

---

## Key Statistics for Any Variant

| Metric | Value | Source |
|--------|-------|--------|
| Sample size | 102 nuclides | V7.4 |
| g coefficient | -0.31 ± 0.11 | V7.4 M2 |
| p-value (OLS) | 0.006 | V7.4 |
| p-value (permutation) | 0.006 | V7.5 |
| CV ΔRMSE | +0.043 | V7.5 |
| ΔR² | 0.0084 | V7.4 |
| Calibration sensitivity | Stable | V7.5 |
| Within-element g | -0.28 (p=0.032) | V7.5 |

---

## Recommended Variant

**Variant B** is recommended for Book 2 as it:
- Provides narrative context without sacrificing rigor
- Mentions all key robustness checks
- Emphasizes the within-element finding (strongest evidence against confounding)
- Uses accessible language while maintaining precision

---

## Critical Note on Sign Interpretation

**Observed**: g = -0.31 (negative)

**Meaning**: Higher d(n) (farther from allowed M-values) → SHORTER half-life → FASTER decay

**Theoretical expectation**: If forbidden zones impede tunneling, we would expect LONGER half-lives (g > 0)

**Discrepancy**: The measured sign is **opposite** to the naive M-topology prediction.

**Possible interpretations**:
1. Forbidden zones *facilitate* rather than impede tunneling (theory revision needed)
2. d(n) correlates with another physical variable that drives the effect
3. The M-topology mechanism operates differently than initially hypothesized

This sign discrepancy is a **key open question** for theoretical development.

---

## Caveats to Include

Any paragraph should be accompanied by appropriate caveats:

1. **Effect size**: The d(n) effect explains only 0.8% of variance beyond G-N + hindrance (which together explain 99.1%)

2. **Correlation vs causation**: Statistical association does not prove M-topology mechanism

3. **Whitelist limitation**: Analysis uses only BL-approved nuclear data sources; deformation and pairing effects not included

4. **Physical mechanism**: The connection between coordination geometry and tunneling barrier remains theoretical

---

## Do Not Include

Per guardrails, the following should NOT appear:

- Claims of "proven" or "confirmed" M-topology (use "consistent with" or "supports")
- Comparisons to supernova nucleosynthesis or r-process (per G7)
- Fission rate predictions (per G7)
- Any material not sourced from BL whitelist

---

## Integration Notes

If incorporated into Book 2:
- Place after Geiger-Nuttall law derivation
- Reference 04_ALPHA100_DATASET.csv for data provenance
- Link to V7.4/V7.5 audit folders for full methodology
- Ensure [Der] epistemic tag is preserved

