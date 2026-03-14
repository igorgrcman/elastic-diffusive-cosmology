# Direct Shape-Source Exhaustion Memo

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Forensic exhaustion memo — no new derivations
**Governing action class:** S_EH + S_NG (Einstein–Hilbert bulk + Nambu–Goto branes)
**Supersedes:** Extends `MINIMAL_CLASS_CLOSURE_MEMO_AFTER_N1_N7_N2.md`
(commit `dbe1a56`) with NMCP WP2 result (commit `9a663b3`).

---

## 1. Executive Verdict

The direct shape-source search for the missing node-well inside
S_EH + S_NG is **effectively exhausted**.

Eight routes have been tested. All return no-go, bounded insufficiency,
or falsification. The final loophole — non-monotone core profiles —
was closed by NMCP WP2: the physical sign argument extends to the
general (non-separable) case, and no admissible mechanism within
S_EH + S_NG generates off-center core attraction.

No natural node-well source remains active within the minimal action
class. The double-well postulate [P] cannot be resolved by any direct
shape-source route inside S_EH + S_NG. Continuation of the V(q)
program requires entering a genuinely **non-minimal action category**
— terms not present in Einstein–Hilbert + Nambu–Goto.

---

## 2. Scope

This memo is about **direct shape-source routes** for generating the
missing non-geometric second minimum in V(q) within the minimal
action class S_EH + S_NG.

This memo is **not**:
- A verdict on all of EDC
- A verdict on the neutron-line assembly (which remains [Dc]+[P]+[Cal]
  regardless of V(q) closure status)
- A verdict on non-minimal model classes (higher-order brane terms,
  topological sectors, form-field couplings)
- A claim that the double-well is impossible — only that it cannot be
  sourced by S_EH + S_NG

---

## 3. What Counts as a Direct Shape-Source Route

A **direct shape-source route** is any mechanism whose purpose is to
generate a q-dependent contribution to V(q) that creates or enables
a secondary minimum at q > 0 (metastable state).

The routes in this closure picture share a common target: produce
V_node(q) or V_bulk(q) such that V(q) = V_geom(q) + V_node(q) +
V_bulk(q) has double-well structure, starting from S_EH + S_NG.

The following belong in this picture because each was an attempt to
directly generate the missing attractive term:

| Route | What it tried to generate |
|-------|--------------------------|
| N1 (Israel thin-junction) | V_node from junction matching conditions |
| N7 (thick-junction monotone) | V_core from regularized core energy (peaked at q=0) |
| NMCP (non-monotone core) | V_core with off-center peak (f(q*/δ) > f(0)) |
| N2 (bulk backreaction) | V_bulk from linearized gravitational response |
| Helfrich | V_bend from bending rigidity |
| ξ-BC (frozen-brane) | V_BC from compact-direction boundary conditions |
| Put C V1 | V(q) from flat-bulk Nambu–Goto |
| Put C V2 | V(q) from warped/RS-metric backgrounds |

---

## 4. Route-by-Route Outcome Summary

| Route | Mechanism Class | Outcome | Status Now | Why No Longer Active |
|-------|----------------|---------|------------|---------------------|
| **N1** | Israel thin-junction matching | Bounded no-go [Dc] | **Dead end** | Deficit angle ≡ 0 (geometric identity); arm-interior energy ∝ V_geom; single-well. Valid for all thin Y-junctions in any warped 5D background. |
| **N7** | Thick-junction monotone core | Bounded insufficiency [Dc] | **Dead end** (monotone class) | Energy scale correct (E₀ ~ 10 MeV) but monotone profiles reinforceSteiner minimum. Theorem: V'(q) > 0 for all q > 0. |
| **NMCP** | Non-monotone core profiles | Bounded no-go [Dc] | **Dead end** | General sign theorem extends beyond separability. All three candidate mechanisms (Z₃→Z₂, non-separable, topology change) fail provenance test. QF-5 and QF-6 triggered. |
| **N2** | Bulk gravitational backreaction | Bounded insufficiency [Dc] | **Dead end** | Cross-term and LO self-energy reduce to tension renormalization. NLO shape correction κ₅²-suppressed; competitive only if M₅ ≲ 100 MeV (far below electroweak). |
| **Helfrich** | Bending rigidity | Falsified [Dc] | **Dead end** | 260/260 configurations: V_bend ~ +κq²/a² reinforces stretching. Zero metastable wells with c₀ = 0. |
| **ξ-BC** | Compact-direction BCs | Falsified [Der] | **Dead end** | V'_lin(d) > 0 for all BC types (Neumann, Robin, Dirichlet). Seven independent checks. |
| **Put C V1** | Flat bulk, Nambu–Goto | No metastability [Dc] | **Dead end** | V(q) monotonically increasing. |
| **Put C V2** | Warped/RS metric | No metastability [Dc] | **Dead end** | 125 parameter combinations scanned; zero metastability found. |

**Total: 8 routes tested. 0 surviving.**

---

## 5. Strongest Closed Findings

The accumulated investigations establish:

1. **The Steiner configuration is the unique energy minimum of V(q)
   within S_EH + S_NG.** Every tested mechanism either reinforces
   the geometric restoring force or is quantitatively negligible. No
   mechanism produces an attractive term centered away from q = 0.

2. **Tension renormalization is the universal low-order effect.**
   N1 (arm-interior Israel), N2 (cross-term), and N2 (LO self-energy)
   all reduce to multiplicative corrections to V_geom. The minimal
   action renormalizes brane tension but does not change potential shape.

3. **The sign argument is general, not restricted to separable models.**
   NMCP WP2 extended the N7 sign argument to arbitrary (non-separable)
   core energy densities via the General Core Sign Theorem. The
   argument is local in r⊥ — separability was mathematical convenience,
   not a physical requirement. This closes the non-separable loophole.

4. **No overlooked donor changes this verdict.** The JSONL archive
   rediscovery (16 sessions, ~724 MB) found no genuinely overlooked
   content. Three marginal items (AR-01 through AR-03) are preserved
   references, none actionable for V(q).

5. **The provenance test is definitive for the NMCP lane.** All three
   WP1 candidate mechanisms fail: Z₃→Z₂ transition requires
   non-minimal physics (QF-6), non-separable coupling is covered by
   the extended sign theorem (QF-5), topology change has no framework
   in S_EH + S_NG (QF-6).

---

## 6. What Remains Merely Insufficient (Not Fully Closed)

Two routes are classified as **bounded insufficiency** rather than
full no-go. The distinction matters:

### N7 (Thick-Junction Monotone Core)

**What is closed:** Monotone, separable core profiles cannot produce
a secondary minimum (Theorem, [Dc]).

**What technically remains:** A non-elastic core model — one that
violates assumption (D) of the General Core Sign Theorem (overlap
monotonicity) — could in principle evade the sign argument. This
would require asymmetric binding to be more efficient than symmetric
binding, contradicting the generic principle for identical components.
No such model exists within S_EH + S_NG.

**Practical status:** Effectively closed. The residual loophole
requires abandoning the elastic brane model, which is the natural
reduction of S_NG.

### N2 (Bulk Gravitational Backreaction)

**What is closed:** Cross-term and LO self-energy reduce to tension
renormalization. NLO shape correction is κ₅²-suppressed for any
M₅ ≳ 1 GeV.

**What technically remains:** The extreme low-M₅ regime
(M₅ ≲ 100 MeV). At such low 5D Planck mass, bulk backreaction
becomes competitive with V_geom.

**Practical status:** Effectively closed. M₅ ~ 100 MeV is far below
the electroweak scale. No physical motivation exists within EDC for
such a low 5D Planck mass. Invoking it would be parameter tuning
[Cal], not derivation.

### Summary of residual loopholes

| Route | Residual Loophole | Physical Motivation | Practical Status |
|-------|------------------|--------------------|-----------------|
| N7 | Non-elastic core model violating assumption (D) | None within S_EH + S_NG | Effectively closed |
| N2 | M₅ ≲ 100 MeV regime | None — far below electroweak | Effectively closed |

Neither residual loophole is actionable without new physics input.

---

## 7. What Is Now Closed Enough for Canonical Use

The following closures may be treated as canonical by future work:

1. **N1 is permanently closed** within S_EH + S_NG. Do not reopen
   thin-junction Israel matching for V_node without adding new terms
   to the action.

2. **N7 + NMCP together close the entire core-profile sector**
   (monotone and non-monotone) within the elastic brane model. Do not
   reopen core-profile routes without changing the physical model of
   the junction core.

3. **N2 is closed for M₅ ≳ 1 GeV.** Do not invoke bulk backreaction
   as a V_node source without specifying and justifying M₅ < 100 MeV.

4. **Helfrich and ξ-BC are permanently falsified.** Do not revisit
   bending rigidity (c₀ = 0) or compact-direction BCs as standalone
   node-well mechanisms.

5. **Put C V1 and V2 are exhausted.** Do not re-scan flat or RS
   backgrounds within S_EH + S_NG without new action terms.

6. **Archive rediscovery is closed.** Do not re-mine the ~724 MB
   JSONL corpus for V(q) donors unless a specific dedicated reason
   appears. The archive is not an active donor pool.

---

## 8. What the Program Has Now Learned

The accumulated negative results teach three structural lessons:

### 8.1 The Steiner restoring force is robust

Every mechanism tested within S_EH + S_NG either adds to or is
proportional to V_geom(q) = τ L_tot(q). The geometric restoring
force — pulling the junction node back to the Steiner equilibrium —
is the dominant q-dependent energy in all investigated sectors:
thin-junction matching, thick-junction core, bulk backreaction,
bending rigidity, compact-direction BCs. No tested mechanism opposes
this restoring force.

### 8.2 The minimal action lacks internal vertex degrees of freedom

The Nambu–Goto action describes worldsheets with no internal structure
at the junction vertex. The Einstein–Hilbert action couples to
stress-energy but introduces no vertex order parameters. As a result,
there is nothing within S_EH + S_NG that can undergo a phase
transition, instability, or symmetry change at the vertex when the
node displaces. The vertex responds continuously and monotonically
to displacement.

This is the structural reason why all shape-source routes fail: they
all attempt to create an attractive region at q > 0, but the minimal
action has no mechanism to prefer a displaced configuration over the
symmetric equilibrium.

### 8.3 The node-well requires new physics

The direct shape-source search has converged on a clear negative
conclusion: the secondary minimum in V(q) cannot be generated by
S_EH + S_NG. If the double-well exists, its source is a term not
present in the minimal action. This narrows the search from "any
mechanism within EDC" to "what non-minimal action extension produces
a q-dependent attractive term?"

---

## 9. Remaining Frontier After Exhaustion

The direct shape-source program inside S_EH + S_NG is exhausted.
The remaining frontier consists of **non-minimal action extensions**
— terms that modify or supplement Einstein–Hilbert + Nambu–Goto.

### Identified non-minimal categories

| Category | What it adds to S_EH + S_NG | Status |
|----------|---------------------------|--------|
| **Higher-order brane terms** (DBI, Gauss–Bonnet) | UV corrections to Nambu–Goto; curvature-dependent contributions to V(q) | Untested. Standard in string/M-theory. Coefficients are new [I] parameters. |
| **Topological contributions** (Chern–Simons, winding) | Quantized energy terms from topological invariants | Untested. AR-02 and AR-03 in archive are conceptual only. No reduction to V(q) exists. |
| **Form-field / extra-sector coupling** | Bulk gauge field or form field to which the brane is charged | Untested. Standard in string compactifications. Introduces new sector with unconstrained parameters. |
| **Non-elastic core physics** | Core model violating elastic brane assumptions (A)-(D) | Untested. Would require abandoning the natural reduction of S_NG. No concrete model proposed. |

### What is not on the frontier

- Direct shape-source routes inside S_EH + S_NG (exhausted)
- Archive re-mining (closed)
- Profile scanning / calibration (forbidden — amounts to phenomenological well)
- Reviving dead ends under new names (anti-regression rules apply)

---

## 10. Anti-Regression Rules

These rules prevent backsliding into closed territory.

| Rule | Statement |
|------|-----------|
| **ARR-E-1** | Do not reopen any direct shape-source route inside S_EH + S_NG without explicit new model-class input. The eight routes in §4 are closed within their stated scope. |
| **ARR-E-2** | Do not reintroduce profile tuning under new labels. Any V_core(q) with freely adjustable peak position, width, or amplitude is a phenomenological node well regardless of what it is called. |
| **ARR-E-3** | Do not call bounded insufficiency a "surviving natural mechanism." N7 and N2 are effectively closed — their residual loopholes require physically unmotivated parameter regimes or model-class changes. |
| **ARR-E-4** | Do not treat marginal archive items (AR-01 through AR-03) as active donors. They may re-enter active research only through a dedicated audit with explicit epistemic classification. |
| **ARR-E-5** | Do not claim "the double-well is falsified." The direct shape-source search inside S_EH + S_NG is exhausted, but non-minimal extensions are untested. |
| **ARR-E-6** | Do not claim "the neutron line is dead." The τ_n assembly remains [Dc]+[P]+[Cal]. The [P] component (V(q) double-well) is constrained but not eliminated — it requires non-minimal physics, which has not been tested. |
| **ARR-E-7** | Do not re-scan flat/RS/warped metric backgrounds within S_EH + S_NG. Put C V1 and V2 exhausted this parameter space. New backgrounds require new action terms. |
| **ARR-E-8** | Any future V(q) attempt must state which non-minimal action extension it uses, and tag the new terms with their epistemic status. The extension must be declared before V_B is computed. |

---

## 11. Recommended Next Category

**Recommended next category: higher-order brane terms.**

**Rationale:**

1. **Most conservative extension.** Higher-order brane terms (DBI
   action, Gauss–Bonnet curvature corrections) are the standard UV
   completion of the Nambu–Goto action. They are the next terms in a
   derivative/curvature expansion and are physically well-motivated
   in string/M-theory contexts.

2. **Direct relevance to the failure mode.** The Nambu–Goto action
   has no internal vertex structure — this is why all shape-source
   routes fail. Higher-order terms introduce curvature-dependent
   energy at the vertex, potentially providing the q-dependent
   structure the minimal action lacks.

3. **Bounded scope.** The DBI and Gauss–Bonnet corrections are
   well-studied, with known functional forms. A computation of
   V_DBI(q) or V_GB(q) for the displaced Y-junction is a bounded
   task with a clear deliverable.

4. **Falsifiable.** If higher-order brane terms also fail to produce
   a secondary minimum, the double-well postulate is further
   constrained. If they succeed, the new terms and their coefficients
   are identifiable.

**Backup categories** (if higher-order brane terms also fail):
topological contributions, form-field coupling. These are more
speculative and less constrained within EDC.

---

## 12. Bottom Line

The direct shape-source search for the missing node-well inside
S_EH + S_NG is effectively exhausted. Eight routes have been tested
across Phase 1 dead ends (Helfrich, ξ-BC, Put C V1/V2), Phase 2
investigations (N1, N7, N2), and the NMCP provenance test. All
return no-go, bounded insufficiency, or falsification. The final
core-profile loophole (NMCP) was closed by extending the sign argument
to the general non-separable case.

No natural node-well source remains active within the minimal action
class. The residual loopholes (non-elastic core, low-M₅ backreaction)
are physically unmotivated and effectively closed.

The next category of work is **non-minimal action extensions** —
specifically higher-order brane terms (DBI, Gauss–Bonnet) as the
most conservative first step beyond S_EH + S_NG. This is not yet a
detailed plan; it is the identification of the next frontier after
direct shape-source exhaustion.
