# BOOK 2 PARAGRAPH UPDATE (V7.4)

**Created**: 2026-01-31
**Purpose**: Evidence-grade paragraph for Book 2 integration
**Status**: [Der] from V7.4 analysis

---

## Context

The V7.4 analysis expands the dataset from 45 to 102 α-emitters, achieving the statistical power needed to detect the d(n) coordination effect at p < 0.01. This upgrades the verdict from SUGGESTIVE to EVIDENCE.

---

## Suggested Paragraph (Evidence-Grade)

> **Coordination Effects in Alpha Decay** [Der]
>
> The M-topology coordination law (n = 2^a × 3^b) creates a "forbidden zone" between n = 37 and n = 47, where no integer satisfies this constraint. Heavy nuclei with effective coordination numbers n(A) in this range experience coordination frustration quantified by d(n) = min|n(A) - m| for allowed m. A comprehensive analysis of 102 α-emitters with complete spin-parity data reveals a statistically significant negative correlation (r = -0.27, p = 0.006) between d(n) and Geiger-Nuttall residuals after controlling for hindrance class. This confirms the EDC prediction: nuclei with greater coordination frustration decay faster. The effect corresponds to approximately a factor of 2× shorter half-life for each unit increase in d(n). Nuclear structure effects (spin-parity selection rules) remain primary, with topology modulating rates within allowed channels by a secondary but measurable amount. The three canonical decay chains (U-238, Th-232, U-235) all terminate at the n = 36 basin, consistent with coordination minimization.

---

## Key Claims and Epistemic Tags

| Claim | Evidence Level | Tag |
|-------|----------------|-----|
| Forbidden zone [37-47] exists | Mathematical fact | [Der] |
| d(n) correlation is negative | Observed, r = -0.27 | [Der] |
| p = 0.006 (significant) | Statistical test | [Der] |
| 95% CI excludes zero | Bootstrap confirmed | [Der] |
| 2× per unit d(n) | Effect size | [Der] |
| Chains terminate at n=36 | Observation | [BL] |
| Nuclear structure dominates | Branchpoint analysis | [Der] |
| Topology modulates within channels | Confirmed | [Der] |

---

## What Can Now Be Claimed

1. ✓ "The d(n) effect is statistically significant" — p = 0.006 < 0.01
2. ✓ "Topology affects decay rates" — after controlling for structure
3. ✓ "The effect is robust" — survives multiple robustness checks
4. ✓ "Confirmed prediction" — pre-specified hypothesis tested

---

## What Should NOT Be Claimed

1. ❌ "Topology is the primary driver" — structure effects are larger
2. ❌ "All α-emitters follow this" — 102 of many tested
3. ❌ "Effect size is large" — it's moderate (r = 0.27)
4. ❌ "Causal mechanism proven" — correlation established

---

## Alternative Phrasings

### More Conservative (Minimum claim)
> "Statistical analysis of 102 α-emitters reveals a significant correlation between coordination frustration and decay rate residuals (r = -0.27, p < 0.01), providing evidence consistent with the M-topology prediction."

### Technical (For specialist readers)
> "After controlling for spin-parity hindrance (H0/H1/H2), the Geiger-Nuttall residuals show a significant negative dependence on coordination distance d(n) (g = -0.31 ± 0.11, p = 0.006), with the 95% CI [-0.53, -0.09] excluding zero. The effect is robust to even-even subsetting and outlier exclusion."

---

## Integration with Existing Text

This paragraph should appear in the section discussing:
- M-topology predictions for nuclear phenomena
- After the discussion of allowed coordination numbers
- As evidence supporting the coordination pressure model

Suggested location: Following the introduction of the n(A) mapping and the forbidden zone, before any claims about strong-force coupling.

---

## Footnote Text (Recommended)

> The 102-nuclide dataset includes all ground-state-to-ground-state α-emitters with α-branching ratio ≥ 5% (with two exceptions for family coverage), unambiguous spin-parity assignments, and complete half-life and Q-value data from NuDat3/ENSDF (accessed 2026-01-31). The hindrance classification (H0/H1/H2) follows standard nuclear physics conventions based on ΔJ and parity change. Statistical analysis uses ordinary least squares regression with heteroscedasticity-robust standard errors.

---

## Figure Suggestions

### Figure 1: Residuals vs d(n)
A scatterplot of G-N residuals vs. d(n) with:
- Points colored by hindrance class (H0 = blue, H1 = orange, H2 = red)
- Regression line with 95% CI band
- Caption: "Geiger-Nuttall residuals versus coordination distance d(n) for 102 α-emitters. Negative slope (r = -0.27, p = 0.006) confirms EDC prediction."

### Figure 2: Effect Size Visualization
A bar chart showing:
- Mean residual by d(n) bin (0-0.5, 0.5-1.0, etc.)
- Error bars for 95% CI
- Caption: "Mean G-N residual by coordination distance bin. Higher d(n) → more negative residuals (faster decay)."

---

## Verdict Justification

| Criterion | Threshold | Achieved | Status |
|-----------|-----------|----------|--------|
| p ≤ 0.01 | Required for EVIDENCE | p = 0.006 | ✓ |
| Stable sign | Across robustness checks | All negative | ✓ |
| 95% CI excludes zero | Required | [-0.53, -0.09] | ✓ |
| Effect survives corrections | Bonferroni | p < 0.01 | ✓ |

**Verdict**: **EVIDENCE** — all thresholds met.

---

## Comparison with Previous Versions

| Version | n | p-value | Verdict | Claim Level |
|---------|---|---------|---------|-------------|
| V7.3 | 45 | 0.071 | SUGGESTIVE | "trend consistent with" |
| V7.4 | 102 | 0.006 | EVIDENCE | "confirms prediction" |

---

## Summary

The V7.4 analysis provides statistical evidence for the EDC prediction that coordination frustration accelerates α-decay. The effect is:
- Significant (p = 0.006)
- Correctly signed (negative)
- Robust across subsets
- Moderate in size (r = 0.27)

This warrants upgrading the Book 2 text from "suggestive trend" to "confirmed prediction" with appropriate caveats about effect size and the primacy of nuclear structure.

