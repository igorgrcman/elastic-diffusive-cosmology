# TODO.md — EDC_Project Workspace Actions

**Last updated:** 2026-01-29

---

## Priority 0: Breadth Strategy (NEW — 2026-01-29)

- [x] **Formalize Projection Lemma in LaTeX** — `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` (2026-01-29)
- [x] **Δm_np sensitivity analysis** — `docs/DELTA_MNP_SENSITIVITY.md` (2026-01-29)
      Result: ROBUST to σ/δ/L_0/w; FRAGILE to Z_6 structure
- [x] **Δm_np model reconciliation** — `docs/DELTA_MNP_RECONCILIATION.md` (2026-01-29)
      Result: ε = 0.679% connects (8/π) and (5/2+4α); 8/π = bare, 5/2+4α = EM-renormalized
- [x] **σ dependency audit** — `docs/SIGMA_DEPENDENCY_AUDIT.md` (2026-01-29)
      Result: σ is master parameter; CRITICAL: 70 vs 5.856 MeV tension (factor ~12)
- [x] **Flavor Skeleton v0.1** — `docs/FLAVOR_SKELETON_v0.1.md` (2026-01-29)
      Result: N_g=3 [Der], sin²θ_W=1/4 [Der], θ_23≈45° [Dc], CKM hierarchy [Dc/P], δ=60° [Dc]
      NO-GO: Z₃ DFT for CKM (×144), Z₃ DFT for PMNS (×15), pure Z₃→CP (J=0)
- [x] **G_F constraint note** — `docs/GF_CONSTRAINT_NOTE.md` (2026-01-29)
      Result: Constraint window g_eff²/M_eff² ∈ [0.9,1.1]×G_F; X = G_F m_e² = 3×10⁻¹²
      True prediction: sin²θ_W = 1/4 [Der]; First-principles G_F remains RED-C (open)
- [x] **Book2 G_F insert** — `edc_papers/_shared/boxes/gf_constraint_box.tex` (2026-01-29)
      LaTeX box + companion MD for Chapter 11; falsification channel documented
- [x] **Pion splitting ε-check** — `docs/PION_SPLITTING_EPSILON_CHECK.md` (2026-01-29)
      Result: r_π/(4α) = 1.166 ≈ 7/6; YELLOW (order-of-magnitude match, factor ~5 needs explanation)
- [x] **Z₆ correction factor 7/6 hypothesis** — `docs/Z6_CORRECTION_FACTOR_7over6.md` (2026-01-29)
      Hypothesis: k = 1 + 1/|Z₆| = 7/6 from discrete averaging
- [x] **Z₆ discrete averaging lemma** — `edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex` (2026-01-29)
      Math derivation [Der]: R = 1 + a/c for f(θ) = c + a cos(Nθ)
- [x] **Z_N generalization + prediction fork** — `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`, `docs/ZN_CORRECTION_CHANNEL.md` (2026-01-29)
      General k(N) = 1 + 1/N; prediction fork for N = 3, 4, 6, 12
- [x] **N_cell renorm canonicalization** — `docs/BREADTH_SYNTHESIS_2026-01-29.md` Section D.3, `edc_papers/_shared/boxes/ncell_renorm_box.tex` (2026-01-29)
      Result: N_cell_eff = 12 × (6/7) = 10.29 ≈ 10; explains τ_n using N_cell = 10
      **Status note:** Math is [Der], physical normalization (a/c = 1/N) remains [Dc]; keep YELLOW until 5D normalization is derived.

---

## Priority 1: Z₆ Correction Channel (Mostly Complete)

**Status:** k(N) = 1 + 1/N fully derived [Der] in toy model; 5D mapping [Dc] remains open.

- [x] **Derive physical normalization a/c = 1/N** — `edc_papers/_shared/derivations/zn_anisotropy_normalization_from_action.tex` (2026-01-29)
      Result: Energy minimization with N identical anchors gives a₁ ∝ 1/N [Der]
      Mechanism: Gradient energy ~ N² vs discrete anchors ~ N → balance ~ 1/N
      Summary: `docs/ZN_NORMALIZATION_FROM_ACTION_NOTE.md`
- [ ] **Explicit 5D reduction (optional upgrade)** ← OPEN for future
      Show S_5D = S_bulk + S_brane + S_GHY reduces to toy functional
      Would upgrade [Dc] → [Der] for physical identification
- [x] **Sector-universality audit** — `docs/ZN_CHANNEL_UNIVERSALITY_AUDIT.md` (2026-01-29)
      Result: PARTIAL — k applies to averaging processes, NOT cardinality ratios
      APPLY: N_cell (12→10), pion (r_π/4α≈7/6)
      DOES-NOT-APPLY: sin²θ_W = |Z₂|/|Z₆| (cardinality ratio)
      UNCLEAR: Δm_np ε-dressing
- [x] **Toy overlap k-channel test** — `docs/TOY_OVERLAP_KCHANNEL_TEST.md` (2026-01-29)
      Third confirmation: explicit mathematical demonstration [Der]
      Code: `edc_papers/_shared/code/toy_overlap_kchannel_check.py` (5/5 tests pass)
      R = I₄_disc/I₄_cont = 1 + a/c; under a/c=1/N gives k(N)=1+1/N

---

## Priority 2: Infrastructure (Complete)

- [x] Create workspace-level CANON_BUNDLE.md (2026-01-28)
- [x] Create WORKSPACE_MAP.md (2026-01-28)
- [x] Create CONCEPT_INDEX.md (2026-01-28)
- [x] Create root STATUS.md (2026-01-28)
- [x] Create root TODO.md (2026-01-28)
- [x] Create root CLAUDE.md with workspace canon enforcement (2026-01-28)
- [x] Update SESSION_LOG.md (2026-01-28)
- [x] Workflow hardening: repo-relative paths (2026-01-28)
- [x] Breadth Strategy + BREADTH_MAP (2026-01-29)

---

## Priority 3: Book 2 Blocking Issues

- [ ] **Resolve L_0/delta tension** — Why static prefers pi^2, dynamic prefers 9.33?
- [ ] **Derive prefactor A** from fluctuation determinant (currently [Cal])
- [ ] **Derive G_F** without circular input (currently uses measured v)

---

## Priority 4: Model Completion

- [ ] Derive geometric factor f = sqrt(delta/L_0) from first principles
- [ ] Derive frustration energy epsilon_f(A) from 5D action
- [ ] Include spin/isospin in topological pinning model

---

## Priority 5: Documentation

- [ ] Audit all "<1%" vs "~20%" claims for consistency
- [ ] Update turning points with frustration-corrected G-N law
- [ ] Complete Companion N (Neutron backbone) — plan ready in CANON_BUNDLE Section 14

---

## Priority 6: Extensions

- [ ] Connect topological pinning to drip lines
- [ ] Test superheavy predictions against experimental data
- [ ] Investigate QCD duality (is topological pinning dual to lattice QCD?)

---

## Completed (Recent)

- [x] Workspace canon infrastructure (2026-01-28)
- [x] Book 2 memory infrastructure (2026-01-28)
- [x] Red team patches: precision consistency (2026-01-28)
- [x] Red team patches: barrier calculation (2026-01-28)
- [x] Red team patches: coordination constraint grounding (2026-01-28)
- [x] Rename M6 -> Topological Pinning Model (2026-01-28)
- [x] Frustration-Corrected Geiger-Nuttall Law (2026-01-28)

---

*Last updated: 2026-01-29*
