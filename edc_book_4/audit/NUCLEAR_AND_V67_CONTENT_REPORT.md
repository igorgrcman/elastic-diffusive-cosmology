# Nuclear Predictions and v67 Closure — Content Report

**Date:** 2026-03-15
**Branch:** `archive/nuclear-topology-discovery`
**Scope:** Content assessment of three key research artifacts

---

## 1. superheavy_predictions.csv — Summary

**Location:** `edc_book_2/src/derivations/tables/superheavy_predictions.csv`
**Format:** 9 rows × 16 columns

### Content

Nine superheavy isotopes (Z = 114–120) with α-decay predictions from the V7.8 M2
frustration-corrected Geiger–Nuttall model:

| Element | Z | A | d(n) | Q (MeV) | log₁₀t (GN) | log₁₀t (full) | log₁₀t (exp) | Δ (dex) | Status |
|---------|---|---|------|----------|-------------|---------------|--------------|---------|--------|
| Fl | 114 | 289 | 4.33 | 9.82 | 7.6 | −0.1 | −0.4 | 0.38 | ✓ |
| Fl | 114 | 290 | 4.38 | 9.19 | 9.5 | 1.8 | — | — | pred |
| Mc | 115 | 290 | 4.38 | 10.41 | 6.4 | −1.3 | −0.2 | 1.12 | ✓ |
| Lv | 116 | 293 | 4.52 | 10.67 | 6.2 | −1.8 | −1.3 | 0.53 | ✓ |
| Ts | 117 | 294 | 4.56 | 10.81 | 6.3 | −1.7 | −1.8 | 0.12 | ✓ |
| Og | 118 | 294 | 4.56 | 11.65 | 4.7 | −3.3 | −3.1 | 0.17 | ✓ |
| 119 | 119 | 298 | 4.74 | 10.5 | 8.2 | −0.2 | — | — | pred |
| 120 | 120 | 302 | 4.93 | 10.0 | 10.2 | 1.5 | — | — | pred |
| 120 | 120 | 304 | 5.02 | 9.5 | 11.7 | 2.9 | — | — | pred |

**Key columns:**
- `d_n`: coordination distance = min|n(A) − 2ᵃ3ᵇ|, the frustration proxy
- `log_t_GN`: baseline Geiger–Nuttall prediction (no frustration correction)
- `log_t_full`: V7.8 M2 prediction (with d(n) correction)
- `log_t_exp`: experimental half-life (where available)
- `delta_GN`, `delta_d`: residuals for baseline and corrected models

**Validation:** 6/6 experimentally tested isotopes pass the |Δ| < 1.5 dex criterion.
Mean |Δ| = 0.48 dex (frustration-corrected) vs. 7.56 dex (baseline GN) — 16× improvement.
Og-294 highlight: predicted 0.5 ms vs. experimental 0.7 ms (Δ = 0.17 dex).

**Sources cited:** NUBASE2020, Dubna 2024, Berkeley 2025, FRDM/WS4+RBF predictions.

**Three isotopes are pure predictions** (Z = 119, 120) awaiting synthesis.

---

## 2. Topological Pinning Monograph — Summary

**Location:** `edc_book_2/src/derivations/topological_pinning_standalone_UPDATED_v3.tex`
**Size:** 1,461 lines, standalone LaTeX document
**Title:** "Topological Pinning, Geometric Frustration, and a Frustration-Corrected Geiger–Nuttall Law"
**Author:** Igor Grčman

### Structure

1. **Epistemic ledger** — Reader contract with [BL], [I], [Dc], [Cal], [P] tags
2. **Motivation** — Neutron-in-a-nucleus paradox (free τ ≈ 880s vs. bound → ∞)
3. **Topological nuclear structure** — Graph model: baryons = Y-junction nodes, flux tubes = edges, deformation coordinate q ∈ {0,1}
4. **Pinning Hamiltonian** — H = Σ V(qᵢ) + K Σ(qᵢ−qⱼ)², single new constant K
5. **K from σ** — K = f·σ·A_contact ≈ 0.93 MeV/bond (f = √(δ/L₀) ≈ 0.32 [I], A_contact = πδL₀ ≈ 0.33 fm² [Dc])
6. **Light nuclei tests** — Free vs. bound neutron, deuterium (2.4 vs. 2.2 MeV, +9%), He-4 (29 vs. 28.3 MeV, +3%), Li-6 (32.1 vs. 31.99 MeV, +0.3%), Be-8 instability (correct sign)
7. **Allowed coordinations** — n = 2ᵃ3ᵇ rule; forbidden zone n ∈ [37, 47] (11 integers); optimal n ≈ 43 is prime → geometric frustration
8. **V7.8 M2 Frustration-Corrected GN Law** — log₁₀(t) = a·Z_d/√Q + g·d(n) + c₁I_H1 + c₂I_H2 + b; R² = 0.980, CV R² = 0.971
9. **V7.4–V7.8 audit trail** — Full regression evolution, sign resolution (g < 0 → prefactor not barrier), mediation analysis, permutation tests
10. **Superheavy validation** — 6/6 pass OOS, mean |Δ| = 0.48 dex
11. **α-cluster model** — C-12 (92.0 vs. 92.2 MeV), O-16 (127.3 vs. 127.6 MeV), both < 1% error
12. **Appendix: ALPHA100 dataset** — Complete 106-nuclide table (Z = 83–100, A = 206–257)

### One-parameter claim

All energetic scales trace to brane tension σ ≈ 8.82 MeV/fm² and the induced K.
The coordination prefactor p = 6.1 is [Cal] (calibrated to Pb-208 anchor, validated by 5-fold CV).

### Epistemic status

| Result | Tag | Confidence |
|--------|-----|-----------|
| K = 0.93 MeV/bond | [Dc]/[I] | f factor is [I], rest derived |
| Light nuclei B.E. | [I] | 0.3%–9% errors |
| Be-8 instability | [Dc] | Correct sign (topology argument) |
| V7.8 M2 regression | [Cal] | R² = 0.980, CV validated |
| Superheavy OOS | [P] | 6/6 pass, strongest test |
| Geometric frustration | [P] | Hypothesis-level, supported by data |

### Key open items

- Derive f = √(δ/L₀) from 5D action (currently [I])
- Derive prefactor p = 6.1 from coordination geometry (currently [Cal])
- Refine odd-Z treatment (Mc, Ts show larger residuals ~1.1 dex)
- Include spin/isospin structure explicitly
- Derive frustration energy ε_f(A) from 5D action

---

## 3. v67 σ̃ Import Contract — Summary

**Location:** `edc_papers/paper_gravity_block003/derivation_v67/`
**Key files:** `README.md` (Import Contract), `REPORT.md` (Layer A firewall report)
**Size:** 29 pages, 155 equations, 316 labels, 123 recompute checks

### What v67 is

v67 is the BLOCK-004 proton decay derivation. It defines how the dimensionless
parameter σ̃ (sigma-tilde) flows from the cosmology lane into the proton decay
prediction chain.

### Import Contract (A-APIσ1–3)

The contract specifies three interface points:
1. **A-APIσ1:** σ̃ input format (dimensionless, from cosmology)
2. **A-APIσ2:** Validation constraints on σ̃
3. **A-APIσ3:** Output contract (what v67 produces given σ̃)

### Closure chain

```
σ̃ → α₃ = 1/σ̃ → M_X → g_X → τ_p
```

All four outputs (α₃, M_X, g_X, τ_p) are **pure functions of σ̃**. No additional
free parameters enter after σ̃ is provided.

### Status: CONDITIONAL CLOSURE

- **Layer A firewall:** VERIFIED — no PDG values, no experimental bounds, no fitted
  parameters inside the derivation. All experimental input is quarantined behind
  the σ̃ interface.
- **σ̃ itself:** NOT YET DERIVED. The cosmology lane that will produce σ̃ is not
  complete. The file `sigma_tilde_value.json` does not yet exist.
- **"REAL CLOSED"** means: the algebraic structure is complete; when σ̃ arrives,
  numerical closure is automatic. It does NOT mean the parameter is closed.

### What this means

v67 is a **structural interface**, not a completed derivation. The proton decay
prediction τ_p will become a genuine EDC prediction only when σ̃ is derived from
the cosmology lane. Until then, τ_p = f(σ̃) is a conditional result.

---

## 4. Key Research Findings

### 4.1 The topological pinning model is the most empirically tested EDC prediction

With 106 in-sample nuclides, 6 out-of-sample superheavy validations, and 3 pure
predictions awaiting synthesis, the V7.8 M2 frustration-corrected GN law represents
the largest body of empirical contact in the EDC program.

### 4.2 The frustration mechanism has a resolved sign

g < 0 means frustration accelerates decay via enhanced α-preformation (prefactor),
not via barrier modification. This was resolved through model comparison (AIC),
interaction tests, and robust regression. The crystal defect analogy (defects
enhance mobility) provides physical intuition.

### 4.3 v67 conditional closure is a structural achievement, not parameter closure

The clean separation of σ̃ as the sole free parameter demonstrates that the BLOCK-004
derivation chain has no hidden dependencies. But σ̃ itself remains underived — the
cosmology lane is the critical path.

### 4.4 Three predictions await experimental test

- Z = 119, A = 298: predicted log₁₀t ≈ −0.2 (≈ 0.6 s)
- Z = 120, A = 302: predicted log₁₀t ≈ 1.5 (≈ 30 s)
- Z = 120, A = 304: predicted log₁₀t ≈ 2.9 (≈ 800 s) — N = 184 shell candidate

These are genuine out-of-sample predictions that can be tested when these isotopes
are synthesized.

### 4.5 The [I] vs [Dc] boundary in the pinning model is well-mapped

The geometric factor f = √(δ/L₀) and the coordination prefactor p = 6.1 are the
two main items separating the model from fully derived status. Both are identified
([I]) or calibrated ([Cal]) rather than derived from the 5D action.

---

## 5. What This Changes in the EDC Knowledge Map

### Nuclear topology is preserved and inventoried

The emergency preservation (commit `2644710`) plus this assessment establishes that:
- The pinning monograph (1,461 lines) is tracked in git
- The superheavy predictions CSV is tracked in git
- 15 previously unprotected nuclear source files from Downloads are now in `_archive_nonrepo/`

### The σ → K → nuclear predictions chain is documented

```
σ ≈ 8.82 MeV/fm²  [Dc]
    ↓
K = f·σ·A_contact ≈ 0.93 MeV/bond  [Dc/I]
    ↓
Light nuclei B.E. (d, He-4, Li-6, Be-8)  [I/Dc]
    ↓
V7.8 M2 GN correction: d(n) frustration proxy  [Cal]
    ↓
Superheavy predictions (Z = 114–120)  [P]
```

### The σ̃ → τ_p chain is documented but incomplete

```
σ̃ (from cosmology, NOT YET DERIVED)
    ↓
α₃ = 1/σ̃  →  M_X  →  g_X  →  τ_p  [Dc, conditional on σ̃]
```

### Priority implications

1. **Cosmology lane (σ̃ derivation)** is the single highest-value open task — it
   would simultaneously close BLOCK-004 proton decay AND provide a second
   independent anchor for σ.
2. **Deriving f from 5D action** would promote the pinning model from [I] to [Dc].
3. **Z = 119/120 synthesis experiments** at RIKEN/Dubna would provide the sharpest
   test of the frustration hypothesis.
