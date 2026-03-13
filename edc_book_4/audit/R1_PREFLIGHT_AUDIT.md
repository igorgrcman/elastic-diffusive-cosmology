# R1 Preflight Audit

**Date:** 2026-03-13
**Branch:** `research/topological-pinning-v7_8-integration`
**Status:** AUDIT ONLY — no R1 implementation

---

## 1. Executive Verdict

R1 cannot produce a unique value L_0/delta = pi^2 from current donor content.
The compactification radius R_5 is **never derived or independently
constrained** anywhere in the repo — every route to L_0/delta assumes an R_5
value without justification. The strongest honest outcome is a
**model-dependent functional relation** L_0/delta = F(R_5/delta, eta), where
eta is a dimensionless well-strength parameter built from sigma, delta, and M.
The Sturm-Liouville eigenvalue lane proposed in the canonical plan is
well-structured and executable, but it produces a curve (L_0/delta vs R_5/delta),
not a point. Selecting R_5 to recover pi^2 and tau_n = 878 s would be
calibration [Cal], not derivation. **Recommended execution mode: B (partial
closure only)** — implement the localization-model eigenvalue problem,
report L_0/delta = F(R_5/delta), identify which R_5 (if any) recovers pi^2,
and explicitly flag the R_5 choice as the residual [P] input.

---

## 2. Scope of Audit

### Files Inspected

| File | Purpose |
|------|---------|
| `edc_book_4/PHASE1_PLAN_REVISED.md` | Canonical plan (source of truth) |
| `edc_book_4/chapters/ch08_L0_delta_ratio.tex` | Target chapter: L_0/delta |
| `edc_book_4/chapters/ch09_tau_n_prediction.tex` | Target chapter: tau_n assembly |
| `edc_book_2/src/derivations/DERIVE_L0_DELTA_PI_SQUARED.md` | L_0/delta exploration v1 |
| `edc_book_2/src/derivations/DERIVE_L0_DELTA_PI_SQUARED_V2.md` | L_0/delta exploration v2 |
| `edc_book_2/src/derivations/DERIVE_KAPPA_FROM_5D_HOMOTOPY.md` | kappa = 2pi derivation |
| `edc_book_2/src/derivations/DERIVE_L0_RP_FROM_5D_ELECTROSTATICS.md` | L_0 = r_p + delta |
| `edc_book_2/src/derivations/DERIVE_OMEGA0_FROM_5D.md` | omega_0 dimensional estimate |
| `edc_book_2/src/derivations/DERIVE_PREFACTOR_A.md` | Prefactor A calibration |
| `edc_book_2/src/derivations/INSTANTON_DERIVATION_CHAIN.md` | Full derivation chain |
| `edc_book_2/src/derivations/EPISTEMIC_CORRECTION_L0_MAP.md` | L_0 epistemic correction |
| `edc_book_4/appendices/app_Vq_chosen_path.tex` | R3 output: M(q) status |
| `edc_book_4/chapters/ch06_instanton.tex` | Instanton: S_E dependence |
| `edc_book_4/code/kramers_double_well_v2.py` | Kramers escape code |
| `edc_book_4/code/r3_vq_verify.py` | R3 geometric verification |

---

## 3. Donor Inventory

| Asset | Location | Relevance to R1 | Epistemic Quality | Reusable? |
|-------|----------|-----------------|-------------------|-----------|
| L_0/delta v1 exploration | `edc_book_2/.../DERIVE_L0_DELTA_PI_SQUARED.md` | Central — 8 routes explored | All [P] heuristic, no [Dc] | Partial — physical intuition reusable, no formal result |
| L_0/delta v2 exploration | `edc_book_2/.../DERIVE_L0_DELTA_PI_SQUARED_V2.md` | Central — 7 routes, pi^2 vs 3pi tension | All [P], best: "two independent pi" | Partial — comparison framework reusable |
| kappa = 2pi derivation | `edc_book_2/.../DERIVE_KAPPA_FROM_5D_HOMOTOPY.md` | Indirect — fixes kappa in S_E | [Dc] conditional on S^1 topology | Yes — kappa is settled for R1 purposes |
| L_0 = r_p + delta | `edc_book_2/.../DERIVE_L0_RP_FROM_5D_ELECTROSTATICS.md` | Consistency check | [Dc] conditional on boundary-charge model | Yes — as comparison target only |
| omega_0 estimate | `edc_book_2/.../DERIVE_OMEGA0_FROM_5D.md` | Prefactor in tau_n | [P] dimensional, two competing mass scales | Partial — dimensional estimate reusable |
| Prefactor A | `edc_book_2/.../DERIVE_PREFACTOR_A.md` | Prefactor in tau_n | [Cal] A ~ 0.94, O(1) natural | Yes — as calibration reference |
| Instanton chain | `edc_book_2/.../INSTANTON_DERIVATION_CHAIN.md` | Full dependency graph | Mixed [Dc]/[P]/[Cal] | Yes — dependency structure |
| Ch.8 L_0/delta | `ch08_L0_delta_ratio.tex` | Current chapter text | [P] for pi^2, three approaches | Yes — structure, not claims |
| Ch.9 tau_n | `ch09_tau_n_prediction.tex` | Assembly chapter | [Dc]+[P]+[Cal] composite | Yes — sensitivity analysis |
| R3 M(q) status | `app_Vq_chosen_path.tex` | Mass scaling for eigenvalue eq | [P] scaling M ~ tau*R/c^2 only | Partial — scaling only, no coefficient |
| Kramers code | `kramers_double_well_v2.py` | Root-finding machinery | [Dc] framework | Partial — brentq reusable |

---

## 4. Existing L_0/Delta Route Inventory

### From DERIVE_L0_DELTA_PI_SQUARED.md (v1)

| Route | Description | Classification | Reusable? |
|-------|-------------|---------------|-----------|
| **1. Geometric origins** | Analysis of why pi appears in circles/spheres | Heuristic only | No — motivational, not derivation |
| **2. Resonance cavity** | Standing wave in 5th dim, assumes R_5 = pi*delta | **Circular**: R_5 assumed | Partial — framework yes, R_5 assumption no |
| **3. Flux quantization** | Three attempts at topological flux | Dead end | No — three attempts, none succeeded |
| **4. Optimal packing** | Energy minimization + topology | Heuristic only | No — too schematic |
| **5. Dimensional transmutation** | Quantum scale generation | Heuristic only | No — suggestive, not computable |
| **6. Two-scale structure** | Radial extent vs depth matching | Partial donor | Yes — identifies key structure (radial x angular) |
| **7. Mode counting** | DOF in junction volume | Heuristic only | No — counting argument, no eigenvalue |
| **8. Resonance + Phase** | Combined standing wave + winding | **Best in v1** | Partial — motivates pi*pi but still assumes R_5 |

### From DERIVE_L0_DELTA_PI_SQUARED_V2.md (v2)

| Route | Description | Classification | Reusable? |
|-------|-------------|---------------|-----------|
| **1. Flux balance** | Three-tube Y-junction flux redistribution | Heuristic only | No — qualitative |
| **2. Standing wave** | Mode-matching in 5th dim | Same as v1 Route 2 | Same — R_5 assumed |
| **3. Phase space** | Momentum-position uncertainty | Heuristic only | No — dimensional argument |
| **4. Two-step winding** | Radial (pi) x angular (pi) = pi^2 | **Best in v2** | Partial — cleanest factorization but still [P] |
| **5. Steiner tree** | Y-junction arm geometry → 3pi | **Alternative** | Yes — provides competing prediction |
| **6. Dimensional analysis** | Available parameters (alpha, pi) | Heuristic only | No — not predictive |
| **7. Synthesis** | Two independent pi factors | Summary of Route 4 | Same as Route 4 |

### Key Finding: pi^2 vs 3pi Tension

| Candidate | Value | Optimizes | tau_n (A=0.9) | Status |
|-----------|-------|-----------|---------------|--------|
| pi^2 | 9.87 | m_p (-1.6% error) | ~30,000 s (too long, need A~0.03) | [P] |
| 3pi | 9.42 | r_p (+1.1% error) | ~1,700 s (need A~0.5) | [P] |
| Empirical | 9.33 | tau_n match | ~880 s (A~0.9) | [Cal] if selected by tau_n fit |

**Critical observation from v2:** Neither pi^2 nor 3pi gives tau_n = 878 s
with a natural prefactor A ~ 1. The empirical value L_0/delta ~ 9.33 does,
but selecting it by tau_n agreement is calibration. The v2 document
explicitly notes this tension.

---

## 5. Localization-Model Assessment

### What Is Justified

The canonical plan proposes a **square-well localization model**:

```
V_loc(xi) = -V_0    for |xi - xi_0| < delta/2
V_loc(xi) = 0       otherwise
```

on a compact circle S^1 of radius R_5 (periodic BC).

**Justified as:**
- **Effective localization ansatz** — the junction defect creates a potential
  well in the compact dimension. This is a standard physics construction
  (particle in a well on a circle).
- The square-well profile is the simplest such model.

**NOT justified as:**
- A derivation from the 5D action. The well shape, depth, and width are
  all model inputs, not computed from S_EDC.
- The "natural" or only possible profile. A Gaussian, triangular, or
  other shape could give different eigenvalues.

### How V_0 Should Be Treated

The plan proposes V_0 ~ sigma/delta as "model-scaling":
- sigma (brane tension, [Dc]) / delta (thickness, [I]) has dimensions of
  energy/length^2, which after multiplication by delta^2 gives energy.
- This is **dimensional analysis within the EDC parameter set** — it's
  the natural energy scale but the proportionality constant is unknown.

**Honest tag:** [P] — model scaling ansatz. Not [Dc], because the
coefficient and functional form are not derived from the action.

### Square-Well Limitation

The square well is a **convenience model**. Its eigenvalues depend on:
1. Well depth V_0 (unknown coefficient)
2. Well width delta (known: [I])
3. Compactification radius R_5 (unknown: [P])
4. Effective mass M (unknown coefficient: [P] from R3)

The product V_0 * delta^2 * M / hbar^2 = eta (dimensionless well-strength)
is the key parameter. Both V_0 and M have undetermined coefficients, so
eta itself has an unknown overall factor. This means the eigenvalue
equation gives L_0/delta = F(R_5/delta, eta), but eta is not fully
determined.

---

## 6. R_5 Assessment

### Existing Assumptions

| Candidate | Value | Provenance | Support Level |
|-----------|-------|-----------|---------------|
| **A** | R_5 = 3delta/pi | Y-junction arm count heuristic | [P] — "3 arms times delta each" |
| **B** | R_5 = pi*delta | Standing-wave resonance (Ch.8 Approach 1) | [P] — legacy, no derivation |
| **C** | R_5 = free parameter | Sensitivity scan | Not an assumption — parametric study |

### Provenance Analysis

- **Candidate A** (3delta/pi): Appears in v1/v2 exploration files. Motivation:
  the Y-junction has 3 arms, each of length ~delta, so the "circumference"
  is ~3delta, giving R_5 = 3delta/(2pi)... but this is then rounded/adjusted
  to 3delta/pi. The geometric argument is loose.

- **Candidate B** (pi*delta): Used in Ch.8 standing-wave approach. If
  R_5 = pi*delta, then the first standing-wave mode has wavelength
  lambda = 2pi*R_5 = 2pi^2*delta, and the localization length is
  L_0 = lambda/(2pi) = pi*delta... wait, this gives L_0 = pi*delta,
  not pi^2*delta. The chain from R_5 to L_0/delta is model-dependent.

- **Candidate C** (free): The honest approach. Compute L_0/delta = F(R_5/delta)
  and report the curve.

### Independent Constraint?

**No.** There is no independent measurement or derivation of R_5 anywhere
in the repo. Every R_5 value is either:
- assumed from geometric heuristic [P], or
- implicitly selected to give L_0/delta ~ pi^2 [circular].

The EPISTEMIC_CORRECTION_L0_MAP.md file notes that L_0 = r_p + delta
is itself [P] (a map from brane observable r_p to 5D quantity L_0).
Using L_0/delta ~ (r_p + delta)/delta ~ 9.33 to constrain R_5 would
import r_p as baseline [BL], making R_5 empirically calibrated.

**Bottom line:** R_5 is the dominant free parameter and no current route
constrains it without importing observational data or assuming the answer.

---

## 7. R3 Dependency / M(q) Assessment

### What R1 Can Honestly Inherit from R3

1. **V_geom(q) curvature at Steiner minimum:** V''(0) = 3*tau/(2R) [Dc]
   - This provides the geometric restoring force
   - Usable as one contribution to the oscillation frequency

2. **M(q) scaling:** M ~ tau*R/c^2 [P]
   - Dimensional estimate only
   - Numerical coefficient undetermined
   - q-independence assumed, not verified

3. **V_geom is single-well** [Dc]
   - The full potential requires non-geometric terms [P]

### What R1 Cannot Inherit

1. **Numerical M value** — no coefficient computed
2. **V''(q_n) at the metastable minimum** — requires full V(q) [P]
3. **omega_0 from R3** — V''(q_n)/M requires both unknowns

### Circularity Risk

The R1 transcendental equation in the canonical plan requires:

```
eta = V_0 * delta^2 * M / hbar^2
```

Both V_0 and M have undetermined coefficients from R3. If R1 uses:
- V_0 = c_1 * sigma/delta (unknown c_1)
- M = c_2 * sigma*delta^2/c^2 (unknown c_2)

Then eta = c_1 * c_2 * sigma^2 * delta^3 / (hbar^2 * c^2), and the
product c_1*c_2 is undetermined. The eigenvalue L_0/delta = F(R_5/delta, eta)
then depends on c_1*c_2, which is a second free parameter alongside R_5.

**Impact:** R1 produces L_0/delta = F(R_5/delta, c_1*c_2), a two-parameter
family of solutions. Recovering pi^2 requires choosing both R_5 and c_1*c_2 —
which is a two-parameter fit, not a derivation.

**Mitigation:** If R1 treats eta as a single dimensionless parameter and
reports L_0/delta = F(R_5/delta, eta), the result is honest: it shows how
the ratio depends on model inputs. The user can then check which (R_5, eta)
pairs give pi^2 and whether those values are physically reasonable.

---

## 8. Eigenvalue / Sturm-Liouville Lane

### What Is Actually Feasible

The canonical plan's Sturm-Liouville approach is well-defined:

1. **Square well on S^1** with periodic BC:
   ```
   -psi''(xi) + V_loc(xi) * psi(xi) = E * psi(xi)
   psi(0) = psi(2*pi*R_5)
   ```

2. **Inside well** (|xi - xi_0| < delta/2):
   psi = A cos(k_w * xi), where k_w^2 = 2M(V_0 - |E|)/hbar^2

3. **Outside well:**
   psi = B exp(-kappa_0 * |xi|), where kappa_0^2 = 2M|E|/hbar^2

4. **Matching condition:**
   k_w * tan(k_w * delta/2) = kappa_0

5. **Localization length:**
   L_0 = 1/kappa_0

### What It Would Produce

- **Transcendental equation** relating L_0 to delta, R_5, V_0, M [Dc within model]
- **L_0/delta = F(R_5/delta, eta)** as a computed function [Dc within model]
- **Numerical scan** of L_0/delta over R_5/delta and eta parameter space [Check]
- **Identification of (R_5, eta) pairs** that give L_0/delta = pi^2 [Check]

### What It Would NOT Produce

- A unique L_0/delta value (two free parameters: R_5 and eta)
- A derivation of R_5 from first principles
- A derivation of eta (product c_1*c_2) from first principles
- Proof that the square-well profile is the correct localization potential

### Boundary Conditions

The periodic BC on S^1 is standard. The junction creates a localized
potential well. The eigenvalue problem is mathematically well-posed.
However:
- The well width = delta is an assumption (could be wider/narrower)
- The well depth V_0 is parametric (coefficient unknown)
- The circle radius R_5 is unknown

### What Is Missing

1. **Derivation of V_loc from 5D action** — shapes, depths, widths
2. **Independent R_5 determination** — from geometry or topology
3. **M(q) coefficient** — from Put C completion
4. **Profile sensitivity** — how much does L_0/delta change for
   non-square-well profiles?

### Code Infrastructure

No Sturm-Liouville solver exists in the codebase. R1 would need to
implement one (straightforward with scipy). The existing `brentq`
root-finding in kramers code is reusable for the transcendental equation.

---

## 9. Tau_n Risk Assessment

### What Breaks If L_0/delta != pi^2

The tau_n formula is:
```
tau_n = A * (hbar/omega_0) * exp(2*pi * L_0/delta)
```

Sensitivity (from Ch.9):

| L_0/delta | S_E/hbar | tau_n (A=0.9) | Deviation |
|-----------|----------|---------------|-----------|
| 0.95*pi^2 = 9.38 | 58.9 | ~280 s | -68% |
| pi^2 = 9.87 | 62.0 | ~880 s | baseline |
| 1.05*pi^2 = 10.36 | 65.1 | ~2900 s | +230% |
| 3pi = 9.42 | 59.2 | ~350 s | -60% |
| 9.33 (empirical) | 58.6 | ~270 s | -69% |

**5% change in L_0/delta causes factor ~16 in tau_n.**

This means:
- If R1 derives L_0/delta = 9.5 (instead of 9.87), tau_n ~ 500 s
  (need A ~ 1.7 to match 878 s — still O(1) but stretched)
- If R1 derives L_0/delta = 10.5, tau_n ~ 5000 s (A ~ 0.2 needed —
  uncomfortably small)
- The "sweet spot" for A ~ 1 is L_0/delta ~ 9.3-9.5 (closer to 3pi
  than pi^2)

### Where Calibration/Circularity Risk Enters

1. **R_5 selection:** If R_5 is chosen to give L_0/delta = pi^2 because
   pi^2 gives the right tau_n, this is calibration with extra steps.

2. **eta tuning:** If the product c_1*c_2 is adjusted to give the desired
   eigenvalue, this is an additional calibration parameter.

3. **Profile choice:** If the square-well is replaced by a different
   profile to get a better eigenvalue, this is model selection bias.

4. **Prefactor absorption:** Currently A ~ 0.9 [Cal] absorbs residual
   uncertainty. If R1 shifts L_0/delta away from pi^2, A must compensate.
   The question is whether A stays in the O(1) natural range.

### Honest Framing

The strongest honest statement R1 can make is:
"Within the square-well localization model, L_0/delta = F(R_5/delta, eta).
For the parameter range eta in [X, Y] (physically motivated) and R_5 in
[A, B] (bracketed by candidates), L_0/delta lies in [lower, upper]. The
value pi^2 falls within/outside this range. The corresponding tau_n range
is [tau_low, tau_high]."

This is a **model-dependent sensitivity map**, not a prediction.

---

## 10. Chapter Impact Assessment

### Ch.08 (L_0/delta Ratio)

| Section | Current State | If R1 Delivers Mode B |
|---------|--------------|----------------------|
| §2: Two length scales | [Dc]/[I] definitions | No change — definitions sound |
| §3: pi^2 hypothesis | [P] — central claim | Must be reframed: pi^2 is one point on F(R_5, eta) curve |
| §4.1: Standing wave | [P] — assumes R_5 = pi*delta | Demote to "one candidate R_5 assumption" |
| §4.2: Two-fold winding | [P] — assumes resonance | Demote to "motivational heuristic" |
| §4.3: Steiner / 3pi | [P] — alternative | Elevate to "equally supported alternative" |
| §5: Potential-theoretic | Sketch only | Replace with appendix reference |
| §6: Tension | pi^2 vs 3pi | Expand: now a computed curve with tension made explicit |
| §7: Epistemic table | L_0/delta = [P] | Update: F(R_5, eta) = [Dc(model)], pi^2 = [P] (R_5 choice) |

**Likely rollback needs:**
- §3 title "The pi^2 Hypothesis" may need softening to "The L_0/delta Ratio"
- §4 approaches should be presented as motivation, not near-derivation
- §6 tension section should be expanded rather than smoothed over

### Ch.09 (tau_n Prediction)

| Section | Current State | If R1 Delivers Mode B |
|---------|--------------|----------------------|
| §2: Exponent S_E/hbar | Uses L_0/delta = pi^2 [P] | Must note: conditional on R_5 choice |
| §3: Prefactor block | omega_0 [P], A [Cal] | No change from R1 |
| §5: Numerical prediction | tau_n = 880 s | Must add: "for L_0/delta = pi^2; see sensitivity" |
| §6: Sensitivity | Already has +-5% table | Expand: add R_5-dependent curve from R1 appendix |
| §7: Baseline comparison | < 1% agreement | Must caveat: agreement holds for pi^2 + A ~ 0.9 |

**Wording at risk:**
- "Result preview: ... the formula gives tau_n ~ 880 s" (Ch.9 §5) needs
  qualification that this uses the [P] value pi^2
- "Deviation < 1%" celebration needs caveat that L_0/delta is [P]

---

## 11. Recommended R1 Execution Mode

### Mode B: Partial Model-Dependent Closure

**Justification:**

1. **Mode A (full R1) is not realistic** because:
   - R_5 is unconstrained — no donor content derives it
   - eta (well-strength) has two undetermined coefficients
   - Result is inherently a two-parameter family, not a unique value
   - Claiming L_0/delta = pi^2 as [Dc] requires inputs that don't exist

2. **Mode C (split) is unnecessary** — the eigenvalue problem and
   sensitivity scan are a single coherent calculation.

3. **Mode D (delay) is wrong** — the eigenvalue calculation IS executable
   now and produces genuinely useful structure (the functional relation),
   even though it doesn't pin a unique value.

### What Mode B Delivers

| Subtarget | Achievable? | Target Tag |
|-----------|-------------|------------|
| Eigenvalue equation for L_0/delta | **YES** | [Dc(model)] |
| L_0/delta = F(R_5/delta, eta) as computed function | **YES** | [Dc(model)] |
| Numerical scan over parameter space | **YES** | [Check] |
| Identification of (R_5, eta) pairs giving pi^2 | **YES** | [Check] |
| Unique value L_0/delta = pi^2 | **NO** | Requires R_5 [P] |
| Independent R_5 derivation | **NO** | [OPEN] |
| eta from first principles | **NO** | Requires M, V_0 coefficients |
| tau_n sensitivity map over L_0/delta | **YES** | [Check] |

### What Mode B Does NOT Deliver

- A unique L_0/delta prediction
- Promotion of pi^2 beyond [P]
- Closure of the tau_n derivation chain
- Independent R_5 or eta determination

---

## 12. Proposed Next Prompt Scope

### In Scope

1. **Appendix** (`app_L0delta_localization_model.tex`):
   - Define square-well localization model on S^1 with periodic BC
   - Derive transcendental matching condition [Dc(model)]
   - Solve for L_0/delta = F(R_5/delta, eta) analytically where possible
   - State all model assumptions explicitly with [P] tags
   - Report which (R_5, eta) pairs give L_0/delta = pi^2
   - Discuss whether those pairs are physically reasonable
   - State R_5 as residual [P] input
   - Include profile-sensitivity discussion (what if not square well?)
   - Summary table: what R1 closed vs what remains open

2. **Verification script** (`r1_L0delta_verify.py`):
   - Solve transcendental equation numerically (scipy brentq/shooting)
   - Scan R_5/delta in [0.5, 5.0]
   - For each R_5, compute L_0/delta
   - Mark pi^2 on output; identify which R_5 recovers it
   - Compute tau_n for each L_0/delta point (sensitivity map)
   - Report whether A stays in O(1) range for viable (R_5, eta) pairs
   - Tag: [Check]

3. **Chapter updates** (ch08, ch09):
   - Graded: eigenvalue relation [Dc(model)], pi^2 remains [P(R_5)]
   - Ch.08: reference appendix, reframe pi^2 as one point on curve
   - Ch.09: add sensitivity to R_5 choice, caveat the < 1% agreement

### Out of Scope

- Derivation of R_5 from 5D action or topology
- Derivation of V_0 or M coefficients from Put C
- Non-square-well eigenvalue computations (beyond qualitative discussion)
- Promotion of L_0/delta = pi^2 beyond [P]
- Promotion of tau_n beyond [Dc]+[P]+[Cal]
- Any Put C work

### Key Constraint

The implementation prompt must explicitly forbid selecting R_5 by
tau_n fit and calling it a derivation. If the natural parameter range
happens to include pi^2, that is a [Check] consistency finding. If it
doesn't, that is a genuine finding, not a failure.

---

## 13. Red Flags

- **Inflation risk 1:** Calling the eigenvalue result "derivation of
  L_0/delta = pi^2" when it actually derives L_0/delta = F(R_5, eta) with
  pi^2 as one point on the curve. The word "derivation" should be reserved
  for the functional relation, not the numerical value.

- **Inflation risk 2:** Selecting R_5 = pi*delta because it gives pi^2,
  then presenting this as a geometric result. R_5 = pi*delta is an
  assumption, not a derivation.

- **Inflation risk 3:** Treating the product c_1*c_2 (coefficients of V_0
  and M) as "order 1" and setting it to a specific value that gives the
  desired eigenvalue. This is a hidden calibration.

- **Inflation risk 4:** Citing the close agreement tau_n ~ 880 s as
  "confirmation" of the model when tau_n agreement was used (implicitly or
  explicitly) to motivate the parameter choices.

- **Circularity risk:** The chain L_0/delta → S_E → tau_n is the
  primary falsifiability target. If R_5 is tuned to make tau_n work,
  the chain becomes self-confirming and unfalsifiable.

- **Profile sensitivity risk:** The square-well eigenvalue is specific to
  the square-well shape. A Gaussian or triangular well of the same depth
  and width gives a different eigenvalue. If the result is profile-sensitive,
  the [Dc(model)] tag applies to the square-well model specifically, not
  to "the localization model" generically.

- **pi^2 vs 3pi risk:** The v2 exploration clearly shows that 3pi (from
  Steiner geometry) is competitive with pi^2 and actually gives a more
  natural prefactor A. If the eigenvalue calculation favors a region
  near 3pi rather than pi^2, this should be reported honestly, not
  suppressed.

---

## 14. Bottom Line

R1 has enough structure for a **genuine model-dependent partial closure**:
the Sturm-Liouville eigenvalue problem on S^1 is well-posed, executable,
and produces a computed functional relation L_0/delta = F(R_5/delta, eta)
[Dc(model)]. This is a real upgrade from the current naked postulate [P].
However, the result is a **curve, not a point** — it maps how L_0/delta
depends on the model inputs (R_5, eta), and neither input is independently
derived. The value pi^2 is one point on this curve; whether it's the
physically correct point depends on R_5, which remains [P]. Execute R1
as Mode B with explicit scope limits: derive the functional relation,
report the parameter scan, and resist the temptation to select R_5 by
tau_n agreement. The partial result is valuable — it replaces "pi^2
because it works" with "pi^2 requires R_5 ~ X and eta ~ Y; here is why
those values are/are not geometrically natural."

---

**Audit completed:** 2026-03-13
