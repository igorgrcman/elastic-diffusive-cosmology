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

---

## Priority 1: Infrastructure (Blocking)

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

## Priority 2: Book 2 Blocking Issues

- [ ] **Resolve L_0/delta tension** — Why static prefers pi^2, dynamic prefers 9.33?
- [ ] **Derive prefactor A** from fluctuation determinant (currently [Cal])
- [ ] **Derive G_F** without circular input (currently uses measured v)

---

## Priority 3: Model Completion

- [ ] Derive geometric factor f = sqrt(delta/L_0) from first principles
- [ ] Derive frustration energy epsilon_f(A) from 5D action
- [ ] Include spin/isospin in topological pinning model

---

## Priority 4: Documentation

- [ ] Audit all "<1%" vs "~20%" claims for consistency
- [ ] Update turning points with frustration-corrected G-N law
- [ ] Complete Companion N (Neutron backbone) — plan ready in CANON_BUNDLE Section 14

---

## Priority 5: Extensions

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
