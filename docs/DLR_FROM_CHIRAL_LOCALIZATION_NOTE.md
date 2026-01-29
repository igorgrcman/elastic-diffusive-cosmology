# d_LR from Chiral Localization: Executive Summary

**Created:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/dlr_from_chiral_localization.tex`
**Status:** [Dc/Cal] — Constrained by G_F gate, not derived from 5D

---

## Key Results

1. **Single domain wall gives d_LR = 0** [Der]
   - For m(χ) = μ tanh(χ/δ), only ONE chirality has normalizable zero mode
   - That mode peaks at wall center χ = 0
   - No L-R separation from standard domain-wall fermions

2. **Non-zero d_LR requires additional structure** [Der]
   - Two walls at different positions, OR
   - Yukawa coupling to Higgs profile, OR
   - Y-junction geometry (EDC-specific)

3. **G_F gate constraint** [Dc]
   - I_4 ~ 10⁻³ GeV requires d_LR/δ ~ 5–10 (exponential suppression)
   - BVP scan found d_LR/δ = 8 passes all gates [Cal]
   - This is NOT arbitrary — it's the center of the allowed window

4. **The r_p coincidence** [I]
   - d_LR = 8δ = 0.84 fm ≈ r_p = 0.841 fm (0.1% match)
   - Suggestive of Y-junction geometry, but NOT derived

---

## Defendable Claim

> **d_LR/δ must be O(5–10) to satisfy the I_4 gate,** unless additional
> chiral suppression mechanisms exist. The specific value 8 is the center
> of this constrained window, not a fine-tuned choice.

---

## The r_p Coincidence: Derived or Still Coincidence?

**Status: STILL COINCIDENCE [I]**

What we have:
- d_LR ≈ r_p numerically (0.1% match)
- Both are O(QCD scale) ~ 1 fm
- Junction geometry could explain it [P]

What we lack:
- Derivation of d_LR from junction physics
- Derivation of r_p itself from 5D geometry
- Proof that the same mechanism sets both scales

**Upgrade path:** Derive proton radius r_p from Y-junction geometry in 5D,
then show chiral localization positions are set by junction arm length.

---

## Mechanism Options (ranked by plausibility in EDC)

| Mechanism | d_LR Expression | Status |
|-----------|-----------------|--------|
| Two walls at ±d/2 | d_LR = d (free parameter) | [Dc] |
| Yukawa + Higgs profile | d_LR depends on φ(χ) | [Dc] |
| Y-junction geometry | d_LR ~ r_p | [P] (hypothesis) |

The Y-junction mechanism is most natural in EDC (proton = Y-junction is
established), but no derivation exists showing that it produces the required
localization pattern.

---

## Integration with OPR-21

| Parameter | Value | Origin | Status |
|-----------|-------|--------|--------|
| d_LR/δ | 8.0 | BVP scan | [Cal] |
| d_LR | 0.84 fm | = 8δ | [Cal] |
| Elasticity | -6.5 | Sensitivity analysis | [Der] |
| Allowed window | [7, 9] | Gate 1 constraint | [Dc] |

---

## Verdict

**YELLOW [Dc/Cal]** — The value d_LR ≈ 8δ is:
- Constrained by G_F gate (not arbitrary) ✓
- NOT derived from 5D action ✗
- Coincident with r_p (suggestive, not proven) ~

---

*Full derivation in LaTeX source. See also: GF_BVP_DEFENSE_NOTES.md Q6.*
