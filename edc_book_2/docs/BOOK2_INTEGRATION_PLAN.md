# Book 2 Integration Plan for Orphan Derivations

**Created:** 2026-01-29
**Status:** Planning

This document maps orphan derivations from `edc_papers/_shared/` to their target Book2 chapters.

---

## Priority 1: G_F / Weak Sector (Chapter 11, 12, 14)

These derivations directly support the G_F closure chain.

| Orphan | Target Chapter | Integration Notes |
|--------|----------------|-------------------|
| `delta_from_5d_action_proton_scale.tex` | ch16 (δ derivation) | Supports OPR-04; energy minimization |
| `dlr_from_chiral_localization.tex` | ch14 (BVP closure) | Explains d_LR ≈ 8δ ≈ r_p coincidence |
| `fw_from_stability_and_spectrum.tex` | ch14 (BVP closure) | Explains fw ∈ [0.5, 1.2] window |
| `gf_noncircular_chain_framework.tex` | ch11 (G_F pathway) | Non-circular G_F derivation framework |
| `gf_potential_shapes_from_5d.tex` | ch12 (BVP workpackage) | Potential V(χ) shapes from bulk |
| `prefactor_A_from_fluctuations.tex` | ch11 or ch14 | Connects A ≈ 0.84 to fluctuations |

**Boxes:**
| Box | Target | Notes |
|-----|--------|-------|
| `delta_from_5d_action_box.tex` | ch16 | Summary box for δ derivation |
| `dlr_chiral_localization_box.tex` | ch14 | Summary box for d_LR |
| `gf_bvp_allgates_physical_priors_box.tex` | ch14 | **MISSING** - needs creation |
| `gf_bvp_pipeline_box.tex` | ch12 | Pipeline summary |
| `gf_bvp_tuning_box.tex` | ch14 | Tuning decomposition |
| `gf_constraint_box.tex` | ch11 | **MISSING** - referenced but not found |
| `prefactor_A_box.tex` | ch11 | Summary for A derivation |

---

## Priority 2: Z_N / k-Channel (Chapter 12 Epistemic Map)

The k(N) = 1 + 1/N mechanism for discrete averaging.

| Orphan | Target Chapter | Integration Notes |
|--------|----------------|-------------------|
| `israel_zn_fixed_points_anchors.tex` | ch12 or new section | Israel junction → Z_N anchors |
| `zn_toy_functional_from_5d_action.tex` | ch12 | Toy model from 5D action |
| `zn_anisotropy_normalization_from_action.tex` | ch12 | a/c = 1/N from gradient energy |
| `zn_ring_delta_pinning_modes.tex` | ch12 | BVP for cos(Nθ) mode |
| `zn_mode_selection_nonlinear_W.tex` | ch12 | Robustness under nonlinear W(u) |
| `zn_strong_pinning_regimes.tex` | ch12 | ρ >> N² regime |
| `zn_symmetry_breaking_one_defect.tex` | ch12 | O(ε²) defect tolerance |

**Boxes:**
| Box | Target | Notes |
|-----|--------|-------|
| `kchannel_spinchain_crossval_box.tex` | ch12 | **MISSING** - referenced but not found |
| `ncell_renorm_box.tex` | ch12 | N_cell = 12 × (6/7) ≈ 10 |
| `zn_kchannel_robustness_box.tex` | ch12 | Summary of robustness tests |

**Lemmas:**
| Lemma | Target | Notes |
|-------|--------|-------|
| `projection_reduction_lemma.tex` | ch11 or ch12 | Core lemma for G_F |
| `z6_discrete_averaging_lemma.tex` | ch12 | Z_6 specific version |
| `zn_discrete_averaging_lemma.tex` | ch12 | General Z_N version |

---

## Missing Files (Need Creation)

The following files are referenced in Book2 but do not exist:

1. `gf_constraint_box.tex` - Create from `docs/GF_CONSTRAINT_NOTE.md`
2. `kchannel_spinchain_crossval_box.tex` - Create from `docs/SPIN_CHAIN_KCHANNEL_CROSSVALIDATION.md`
3. `gf_bvp_allgates_physical_priors_box.tex` - Create from `docs/GF_BVP_PHYSICAL_PRIORS.md`

---

## Integration Procedure

For each orphan:

1. **Verify content** - Ensure derivation is [Der] or [Dc], not [P]
2. **Check dependencies** - Does target chapter have required prerequisites?
3. **Add \input** - Insert at appropriate location in target chapter
4. **Verify compilation** - `latexmk -xelatex main.tex`
5. **Update manifest** - Re-run `book2_manifest.py`

---

## Recommended Order

1. Create missing boxes (gf_constraint_box, kchannel_spinchain_crossval_box)
2. Integrate G_F derivations into ch11/ch14
3. Integrate Z_N derivations into ch12 (epistemic map)
4. Integrate lemmas as appendix or inline
5. Re-run manifest to verify all orphans resolved

---

*Created 2026-01-29 by book2_manifest.py integration planning*
