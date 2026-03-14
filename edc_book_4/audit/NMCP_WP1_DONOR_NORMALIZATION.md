# Non-Monotone Core Profiles WP1 — Donor Normalization

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Normalization task — no derivation, no implementation
**Governing documents:**
- `audit/MINIMAL_CLASS_CLOSURE_MEMO_AFTER_N1_N7_N2.md` (commit `dbe1a56`)
- `appendices/app_P2_N7_core_nodewell.tex` (N7 bounded insufficiency)
- `audit/N7_WP1_DONOR_NORMALIZATION.md` (N7 donor normalization)
- `PHASE2_NEXTSTEP_PLAN_V1.md` (lane selection)

---

## 1. Executive Verdict

This lane survives **only because** the monotone/separable core profile
class failed to produce metastability (N7 bounded insufficiency). It is
not a preferred mechanism. It is not physically motivated. It is the
residual loophole that was not ruled out — nothing more.

The non-monotone core profile lane is **high-risk for smuggling**. It
can collapse into a disguised phenomenological node well at every step:
a displaced peak is trivially tunable to produce any desired V_B, and
the "non-monotone" label can dress up a fitted Gaussian under a new
name. Any future WP2 implementation must demonstrate **provenance** —
a physical mechanism that breaks the q = 0 monotone structure — before
numerical results carry weight.

This document normalizes the lane: defines what "non-monotone" means,
lists the minimal donor material, draws the boundary between admissible
structure and forbidden phenomenology, and establishes anti-smuggling
rules strict enough to make fake closure fail quickly.

---

## 2. Scope

This document normalizes the non-monotone core-profile lane only.

- It is **not** a derivation or implementation.
- It is **not** a claim that this lane is viable.
- It produces no code, no appendix, no equations.
- It is downstream of the N7 bounded insufficiency
  (`app_P2_N7_core_nodewell.tex`, §Outcome Classification).

**What this document decides:**
1. What counts as admissible non-monotone structure.
2. What is forbidden.
3. What donor material exists.
4. What would make this lane legitimate vs fake.
5. What fail-fast conditions apply before any implementation.

---

## 3. Lane Definition

### 3.1 What Was Ruled Out by N7

The N7 bounded insufficiency proved (Theorem in `app_P2_N7_core_nodewell.tex`):

> If the core profile f(q/δ) satisfies (i) f(0) = max f and
> (ii) f'(u) ≤ 0 for u > 0, then V(q) = V_geom(q) + V_core(q) has
> no secondary minimum. V'(q) > 0 for all q > 0.

This eliminates the **monotone class**: profiles peaked at q = 0 and
non-increasing thereafter. The no-go is structural [Dc] and does not
depend on profile parameters.

### 3.2 What "Non-Monotone" Means

A non-monotone core profile is a function f(q/δ) that violates the
monotone conditions — specifically, there exists some q* > 0 such that
f(q*/δ) > f(0), or f has a local maximum at q* > 0.

In the parameterization V_core(q) = −E₀ f(q/δ) with E₀ > 0, this
means the core energy is **lower** (more negative, more attractive)
at q = q* than at the Steiner equilibrium q = 0.

### 3.3 Vocabulary: Types of Non-Monotone Profiles

| Type | Definition | Physical Meaning | Status |
|------|-----------|-----------------|--------|
| **Displaced peak** | f has global maximum at q* > 0, not at q = 0 | Core energy minimum is away from Steiner | Admissible in principle — see §7 |
| **Oscillatory** | f has multiple local maxima at q₁, q₂, ... > 0 | Core energy has multiple local minima | Admissible in principle — but requires specific provenance |
| **Sign-changing** | f changes sign: f > 0 in some region, f < 0 elsewhere | Core contribution switches from attractive to repulsive | Admissible — but V_core form V = −E₀ f would require careful sign accounting |
| **Non-separable correction** | ρ_core(r⊥, q) does not factor as g⊥ × f | Transverse-longitudinal coupling modifies effective f_eff(q) | Admissible — and physically the most plausible route to non-monotonicity |
| **Monotone with displaced peak** | f(0) = max, f' ≤ 0, but shifted origin | Relabeling q → q − q* of a monotone profile | **NOT admissible** — this is just a displaced monotone profile, which amounts to choosing where to center the well |

### 3.4 Critical Distinction

**Not every non-monotone function is admissible.** The N7 no-go
eliminates monotone profiles on physical grounds: both binding energy
(maximal overlap at q = 0) and strain energy (minimized by Z₃-symmetric
stress at q = 0) favor q = 0 as the core energy minimum.

A non-monotone profile must **contradict** this physical argument. It
must identify a specific mechanism by which the core energy **decreases**
when the junction node moves away from Steiner. Without such a
mechanism, the non-monotone profile is an arbitrary function chosen
for its numerical consequences — i.e., a phenomenological node well.

---

## 4. Why This Lane Survives At All

The N7 bounded insufficiency applies to monotone, separable core
profiles. Three things were **not** tested:

1. **Non-monotone profiles**: f(q*/δ) > f(0) for some q* > 0. The
   theorem does not apply.
2. **Non-separable core physics**: ρ_core(r⊥, q) ≠ g⊥ × f. The
   separable ansatz is [P]; a non-separable core could yield an
   effective f_eff(q) that is non-monotone after transverse integration.
3. **Internal core dynamics**: A qualitative structural change inside
   the core (e.g., Z₃ → Z₂ symmetry transition at critical displacement)
   could produce non-monotone V_core(q).

These survive **as residual loopholes**, not as preferred theory. The
N7 appendix explicitly states: "A non-monotone profile would require
a mechanism that makes the core energy decrease with increasing
asymmetry, which has no obvious elastic-medium analogue."

The lane is open. It is not promising.

---

## 5. Central Donors

| ID | Source | Relevance | Epistemic Quality | Reusable? |
|----|--------|-----------|-------------------|-----------|
| **D-NM-1** | N7 monotone no-go theorem (`app_P2_N7_core_nodewell.tex`, Theorem) | Defines exactly what was ruled out; the non-monotone lane exists only in the theorem's complement | [Dc] | Yes — constraint |
| **D-NM-2** | N7 escape route discussion (`app_P2_N7_core_nodewell.tex`, §Escape Route) | Identifies f(q*/δ) > f(0) as the formal condition and Z₃→Z₂ transition as possible mechanism | [OPEN] — speculative | Yes — defines the lane |
| **D-NM-3** | N7 sign argument (`app_P2_N7_core_nodewell.tex`, §Physical Argument for Profile Shape) | Binding energy + strain energy favor q = 0 minimum. Any non-monotone profile must contradict this. | [Dc+I] | Yes — constraint against non-monotonicity |
| **D-NM-4** | Separable core ansatz structure (D-N7-1 from `N7_WP1_DONOR_NORMALIZATION.md`) | ρ_core = σ g⊥ f framework; V_core = −E₀ f; E₀ = σ L₀² | [Dc] structural | Yes — but separability itself is the question |
| **D-NM-5** | V_geom(q) = τ L_tot(q) (D-NM-2 from N7 WP1) | Geometric single-well baseline | [Dc] | Yes — central |
| **D-NM-6** | Minimal-class closure memo (`MINIMAL_CLASS_CLOSURE_MEMO_AFTER_N1_N7_N2.md`) | Establishes that S_EH + S_NG is exhausted for monotone/separable/linear-backreaction | [Dc] summary | Yes — framing constraint |

**Notably absent:** There is no donor material that positively supports
non-monotone core profiles. No branch contains a computation of
non-monotone f(q/δ). No physical mechanism for off-center core energy
has been demonstrated. The donor base for this lane is entirely
constraints and formal definitions — no positive evidence.

---

## 6. Forbidden / Dead-End Imports

| # | Forbidden Import | Why Forbidden | Smuggling Type |
|---|-----------------|--------------|----------------|
| **F-NM-1** | Phenomenological Gaussian node well (Put C Variant 3: V_node = −V₀ exp(−(q−q*)²/2w²)) | [P/Cal]. Parameters fitted to produce V_B ≈ 2.8 MeV. No physical derivation. | CR2: relabeling |
| **F-NM-2** | "Choose q* to get metastability" — any profile whose displaced peak q* is selected to place a secondary minimum at the desired location | The peak position must follow from core physics, not from the desired V(q) shape. Choosing q* is fitting, not deriving. | CR9: target-driven profile selection |
| **F-NM-3** | "Choose width w to match V_B" — any profile whose width parameter is adjusted to produce V_B ≈ 2.6 MeV | Width must follow from the core scale δ or internal dynamics, not from the barrier-height target. | CR1: calibration dressed as derivation |
| **F-NM-4** | "Choose amplitude A to match τ_n" — any profile whose amplitude is calibrated backward from the observed lifetime | The amplitude must follow from E₀ = σ L₀² [Dc] and the profile normalization. | CR5: output used as input |
| **F-NM-5** | C = 100 as independent evidence | Circular: C = (L₀/δ)² uses L₀ [I] and δ [I]. The value is [I]-dependent. | CR4: circular parameterization |
| **F-NM-6** | Archive items AR-01, AR-02, AR-03 imported as V(q) terms | These are preserved references not connected to V(q). AR-02 (Chern–Simons) and AR-03 (Λ pinning) are conceptual only with no reduction to V(q). | Importing untested conceptual items as functional contributions |
| **F-NM-7** | Any relabeling of old dead ends as "non-monotone" — e.g., Helfrich bending reframed as "core curvature effect" or ξ-BC reframed as "non-separable correction" | These mechanisms have been independently falsified. The non-monotone label does not revive them. | ARR-4, ARR-5 from closure memo: anti-regression |
| **F-NM-8** | Lorentzian or Gaussian profiles imported as [Dc] from junction-core-derive-C-v1 scan | [P] postulated profiles. Comparison targets only. | CR2 variant: importing scan profiles as derived |
| **F-NM-9** | Double-well structure assumed as premise | The non-monotone lane tests whether a double-well can emerge from non-monotone core physics. It cannot assume the answer. | Circular: assuming what is to be derived |
| **F-NM-10** | τ_n, V_B, Δm_np, ω₀ as derivation inputs | These are comparison targets [BL] or postulated [P] downstream quantities. They may appear only in a final [Check] comparison, never in the derivation of f(q/δ). | CR5/CR9: backward calibration |

---

## 7. Admissible Model-Class Boundary

### 7.1 Admissible in Principle

A non-monotone core profile is admissible **only if** it satisfies all
of the following:

1. **Identified provenance.** The non-monotone structure arises from a
   stated physical mechanism — not from choosing a function that produces
   the desired numerical result. The mechanism must be named, not
   implicit.

2. **Contradicts the sign argument explicitly.** The N7 sign argument
   (binding energy + strain energy favor q = 0) must be addressed. An
   admissible non-monotone profile must identify which assumption of
   the sign argument fails and why.

3. **Not a relabeled phenomenological well.** The profile must not be
   equivalent (after parameter identification) to the Put C Variant 3
   Gaussian or to any fitted function whose parameters are chosen from
   the downstream target.

4. **Reduces to thin-junction limit.** In the δ → 0 limit, V_core → 0
   (D-NM-1 constraint). The non-monotone structure must vanish in this
   limit.

5. **Falsifiable.** The mechanism must make predictions that can be
   checked against the existing no-go results. If the mechanism is
   unfalsifiable within the current framework, it is [P] at best.

Candidate mechanisms that could in principle satisfy these conditions:

| Mechanism | How It Breaks Monotonicity | Sign-Argument Failure Mode | Status |
|-----------|--------------------------|---------------------------|--------|
| **Z₃ → Z₂ internal symmetry transition** | At critical q*, the three-fold symmetric core reorganizes to a two-fold configuration, releasing stress energy | Strain energy argument assumes Z₃ symmetry is maintained for all q; if Z₃ breaks at q*, strain energy could decrease | [OPEN] — purely speculative. No computation exists. |
| **Non-separable transverse-longitudinal coupling** | ρ_core(r⊥, q) has a cross-term that makes the effective f_eff(q) non-monotone after transverse integration | Separability [P] is violated; transverse profile g⊥ itself depends on q, allowing off-center effective minimum | [OPEN] — requires solving full 2D core equations |
| **Core topology change** | At critical q*, the core topology changes (e.g., from connected to disconnected junction) releasing topological energy | Continuous deformation assumption fails; energy is non-analytic at q* | [OPEN] — highly speculative. No framework exists. |

### 7.2 Forbidden in Practice

| Profile Type | Why Forbidden |
|-------------|--------------|
| Any f(q/δ) with displaced peak at q* chosen to produce metastability, without a physical mechanism selecting q* | This is fitting, not deriving. The profile is a phenomenological node well relabeled as "non-monotone core physics." |
| Any f(q/δ) whose parameters are scanned until V_B ≈ 2.6 MeV | Parameter scanning is calibration [Cal]. Scanning profiles is the same as fitting the Variant 3 Gaussian. |
| Any f(q/δ) whose only justification is "it is not monotone, and non-monotone is not ruled out" | Formal non-exclusion is not positive evidence. The burden is on the profile to demonstrate physical provenance. |
| Any "effective f_eff" obtained from non-separable physics whose non-separable corrections are freely adjustable | If the non-separable correction has free parameters, and those parameters are chosen to produce metastability, the result is [Cal]. |
| Any profile motivated by analogy to systems outside EDC (e.g., "in condensed matter, junctions do X") | External analogies are illustrative but not derivations. The profile must follow from the EDC 5D action, not from a different physics. |

### 7.3 The Provenance Test

**A non-monotone profile is not enough. It must have provenance.**

Provenance means: the profile shape is determined by solving equations
that follow from the 5D action (or a declared regularization thereof),
not by choosing a function and computing its consequences.

The test is simple:

> Remove all knowledge of V_B, τ_n, Δm_np, and the Variant 3 Gaussian.
> Does the non-monotone profile still emerge from the stated physics?
> Is q* still at the same location? Is the amplitude still the same?

If yes: provenance is established.
If no: the profile is calibrated, and the lane is fake.

---

## 8. Canonical Anti-Smuggling Rules

These rules govern any future WP2 implementation of the non-monotone
core profile lane. They are stronger than the N7 WP2 rules because
the non-monotone lane is higher-risk.

| Rule | Statement |
|------|-----------|
| **ARR-NM-1** | **No free displaced minimum inserted by hand.** The location q* of any off-center extremum in f(q/δ) must follow from the stated physical mechanism. If q* is a free parameter, the result is [Cal], not [Dc]. |
| **ARR-NM-2** | **No profile parameter chosen to reproduce V_B or τ_n.** The profile f(q/δ) must be fully determined before V_B is computed. V_B is an output to be compared with 2Δm_np as [Check], never an input. |
| **ARR-NM-3** | **No shape function whose only justification is "it works numerically."** Numerical success (V_B ≈ 2.6 MeV, τ_n ≈ 880 s) is not evidence for a profile. The profile must be derived or constrained from physics. Numerical agreement without provenance is [Cal]. |
| **ARR-NM-4** | **No relabeling phenomenological node-well parameters as internal-core physics.** If the derived non-monotone f(q/δ) is equivalent (after parameter mapping) to the Variant 3 Gaussian with fitted parameters, flag as CR2 violation and reject unless the coincidence is independently explained. |
| **ARR-NM-5** | **No importing topological rhetoric without reduction to V(q).** References to Chern–Simons terms, winding numbers, or topological quantization are admissible only if they produce a computable contribution to V(q). Conceptual invocations without functional form are forbidden. |
| **ARR-NM-6** | **No calibration rescue presented as derivation.** If the non-monotone profile produces V_B within a factor of 2–3 of 2Δm_np only after adjusting a free parameter, the adjustment is calibration [Cal] and must be tagged as such. |
| **ARR-NM-7** | **Any admissible profile must identify what physical mechanism breaks the q = 0-centered monotone structure.** The N7 sign argument (binding energy + strain energy favor q = 0) is the default. Any non-monotone claim must state which premise of the sign argument fails, how, and why. |
| **ARR-NM-8** | **If provenance is absent, the route remains [P] and cannot back-promote the neutron line.** A non-monotone profile without derived provenance is a postulate [P]. It is not worse than the current V(q) [P], but it is not better. It cannot elevate τ_n above [Dc]+[P]+[Cal]. |
| **ARR-NM-9** | **The non-monotone profile must reduce to zero in the δ → 0 limit.** Consistency with the WP2 thin-junction no-go requires V_core → 0 as δ → 0. Any non-monotone structure that persists in the thin-junction limit contradicts N1 and is rejected. |
| **ARR-NM-10** | **No selective profile-family shopping.** If multiple physical mechanisms are tested and only one produces metastability, the selection must be justified on physical grounds, not on the basis of which mechanism gave the "right" V_B. |

---

## 9. Circularity Risk Register

| Risk ID | Description | Why Dangerous | Prevention Rule |
|---------|-------------|--------------|-----------------|
| **CRR-NM-1** | **Profile-center tuning.** The peak position q* is adjusted until a secondary minimum appears in V(q). | q* is the single most powerful tuning knob. Any q* in the range [0.5δ, 5δ] can produce metastability with appropriate amplitude. | ARR-NM-1: q* must follow from physics, not from V(q) scan. |
| **CRR-NM-2** | **Width tuning.** The profile width w is adjusted to control barrier shape. | Width directly determines V_B: wider profile → lower barrier, narrower → higher. Continuous knob. | ARR-NM-2, ARR-NM-3: w must be set by δ or internal dynamics, not by V_B target. |
| **CRR-NM-3** | **Amplitude tuning.** The profile amplitude (effectively E₀ × f_max) is adjusted to match V_B ≈ 2.6 MeV. | Amplitude is the third independent tuning knob. Three knobs (q*, w, amplitude) make any V_B achievable. | ARR-NM-2: amplitude is set by E₀ = σ L₀² [Dc]. Any deviation must be physically justified. |
| **CRR-NM-4** | **Selective profile-family choice.** Multiple profile families are tested; only the one that produces metastability is reported. | Survivorship bias disguised as model selection. | ARR-NM-10: report all tested families. Selection must be justified on physical grounds. |
| **CRR-NM-5** | **Using τ_n agreement as justification for the profile itself.** "This profile gives τ_n = 880 s, therefore it is correct." | Classic circular reasoning. τ_n is a downstream prediction, not evidence for the profile shape. | ARR-NM-2, ARR-NM-3: τ_n is [BL] comparison target only. |
| **CRR-NM-6** | **Importing non-minimal structure after seeing the target barrier height.** Knowing V_B ≈ 2.6 MeV and then choosing a mechanism that produces exactly that. | Post-hoc mechanism selection. The mechanism is chosen to fit, not to explain. | ARR-NM-7: mechanism must be stated before V_B is computed. The derivation of f must not reference V_B. |
| **CRR-NM-7** | **Non-separable correction as free parameter.** Introducing a non-separable term with adjustable coupling that is tuned to produce the desired V(q). | The non-separable correction becomes a disguised phenomenological parameter. | ARR-NM-6: if the non-separable coupling is free, the result is [Cal]. |
| **CRR-NM-8** | **Sign-argument dismissal without replacement.** Claiming "the sign argument is only [Dc+I], therefore we can ignore it" without providing a physical mechanism that contradicts it. | The sign argument is the strongest physical constraint against non-monotonicity. Dismissing it without explanation is evasion. | ARR-NM-7: must identify which premise fails and why. |

---

## 10. Allowed Inputs

### Central Allowed Inputs

| Input | Source | Tag | How It May Be Used |
|-------|--------|-----|--------------------|
| Separable core ansatz structure | D-N7-1 | [Dc] structural | Starting framework. Non-monotone lane may extend or modify separability. |
| V_geom(q) = τ L_tot(q) | D-N7-2 | [Dc] | Single-well baseline for combination with V_core. |
| σ = 8.82 MeV/fm² | Book I | [Dc] | Brane tension. Sets E₀. |
| δ = ℏ/(2m_p c) ≈ 0.105 fm | Delta audit | [I] | Core decay scale. |
| L₀ ≈ 1.0 fm | Phase 1 | [I] | Transverse junction extent. |
| E₀ = σ L₀² ≈ 8.82 MeV | D-N7-1 + Delta audit | [Dc] | Core energy scale. |
| N7 monotone no-go theorem | D-NM-1 | [Dc] | Defines the complement in which this lane operates. |
| N7 sign argument | D-NM-3 | [Dc+I] | Default expectation: q = 0 is core minimum. Must be contradicted for non-monotone lane. |
| N1 Israel no-go | S-N7-3 | [Dc] | Thin-junction limit constraint: V_core → 0 as δ → 0. |

### Supporting Allowed Inputs

| Input | Source | Tag | How It May Be Used |
|-------|--------|-----|--------------------|
| N7 WP2 computation infrastructure | S-N7-2 (code) | [Cal] | V(q) scanner. Extend, don't rewrite. |
| Junction-core scan results | S-N7-1 | [Cal] | Comparison baseline only. Not [Dc] evidence. |
| Δm_np ≈ 1.293 MeV | PDG | [BL] | Comparison target only. NOT derivation input. |

### Unsettled Assumptions That Must Remain Tagged

| Assumption | Tag | Why Unsettled |
|-----------|-----|--------------|
| Separability of ρ_core(r⊥, q) | [P] | If separability is violated, the effective f_eff(q) could be non-monotone. But separability violation is assumed, not derived. |
| Core scale δ = ℏ/(2m_p c) | [I] | Factor-50 ambiguity with R_ξ unresolved. |
| Transverse extent r₀ = L₀ | [I] | Identification, not derivation. |
| Any regularization model for the junction core | [P] or [Dc\|model] | No unique regularization exists. Choice of model is the central [P] input. |
| Z₃ → Z₂ transition mechanism | [OPEN] → [P] if assumed | No computation demonstrates this transition occurs. |

---

## 11. Quick-Falsification Conditions

The following conditions would quickly falsify or strongly downgrade
this lane in any subsequent WP2 attempt. If any of these is met, the
lane should be abandoned or reclassified before further computation.

| # | Condition | Effect |
|---|-----------|--------|
| **QF-1** | No plausible physical mechanism can be identified for an off-center core energy extremum after examination of the regularized junction equations of motion. | Lane is falsified within the accessible model class. Non-monotonicity is formally possible but physically empty. |
| **QF-2** | Every admissible non-monotone profile reduces to a disguised phenomenological fit after parameter identification (i.e., the profile parameters map onto {V₀, q*, w} of the Variant 3 Gaussian with no additional physical content). | Lane is CR2-contaminated. The non-monotone label adds no epistemic value over the [P/Cal] Variant 3. |
| **QF-3** | Metastability appears only after target-driven parameter selection — i.e., q*, w, or amplitude must be tuned to produce V_B in the right range. | Lane is [Cal], not [Dc\|model]. Downgrade to "non-monotone profiles are not excluded but require calibration." |
| **QF-4** | The route cannot produce a non-monotone V_core without importing a mechanism that smuggles a preferred q*. | Lane is circular. The non-monotone structure is an output of fitting, not an output of physics. |
| **QF-5** | The physical sign logic (binding + strain favor q = 0) holds for all physically reasonable core models, including non-separable models. | The sign argument extends beyond the separable class. Non-monotonicity is ruled out at the physical-argument level, not just the theorem level. No escape route remains within S_EH + S_NG. |
| **QF-6** | The only mechanism that breaks monotonicity (e.g., Z₃ → Z₂ transition) requires physics not present in S_EH + S_NG (e.g., additional fields, topological terms, or curvature corrections). | The lane is reclassified from "non-monotone within S_EH + S_NG" to "non-minimal extension required." The minimal-class closure memo verdict stands. |
| **QF-7** | The non-monotone V_core(q) does not reduce to zero in the δ → 0 limit, contradicting the N1 thin-junction no-go. | Internal inconsistency. The model violates an established [Dc] constraint. Reject. |

**Design intent:** These conditions are ordered so that the cheapest
checks (QF-1: can a mechanism be identified at all?) come first. A WP2
attempt should check QF-1 before investing in any computation.

---

## 12. Bottom Line

The non-monotone core profile lane remains open only as a tightly
constrained loophole in the N7 bounded insufficiency theorem. It is
not a preferred mechanism. No donor material positively supports it.
No physical mechanism for off-center core energy has been demonstrated
or even concretely proposed beyond the speculative Z₃ → Z₂ transition
label.

The lane has three tuning knobs (peak position q*, width w, amplitude)
that can trivially produce any desired V_B. This makes it the
highest-risk lane for fake closure in the entire Phase 2 program.

Any future WP2 attempt must:
1. Identify a physical mechanism that breaks the q = 0 monotone
   structure (QF-1).
2. Demonstrate that the mechanism contradicts the N7 sign argument
   explicitly (ARR-NM-7).
3. Derive the profile f(q/δ) from that mechanism before computing
   V_B (ARR-NM-2).
4. Pass the provenance test (§7.3): remove knowledge of V_B, τ_n,
   Δm_np, and the Variant 3 Gaussian; confirm the profile still emerges.

**Provenance before numerical success.** Without provenance, this lane
is indistinguishable from a phenomenological node well with a different
name. The anti-smuggling rules (ARR-NM-1 through ARR-NM-10) and the
quick-falsification conditions (QF-1 through QF-7) are designed to make
fake closure fail fast and visibly.
