# EDC Frozen Criterion From Action v1.3

**Date:** 2026-01-13
**Author:** Claude Code (Opus 4.5)
**Purpose:** Derive frozen criterion τ_relax >> τ_obs from 5D EDC action — promote Gap 1 to [Dc]

**DOI:** [10.5281/zenodo.18211854](https://doi.org/10.5281/zenodo.18211854)

---

## Abstract

This document derives the **frozen criterion** from first principles, promoting it from postulate [P] to conditional derivation [Dc]. Two independent routes are provided: (A) large-σ instanton barrier giving exponential suppression, and (B) topological protection via winding number conservation. With QCD string tension, Route A gives marginal suppression (S/ℏ ~ 1–2); robust freezing requires either σ >> σ_QCD or topological protection (Route B).

---

## Changelog

### v1.2 → v1.3 (2026-01-13)

- **DOI added:** 10.5281/zenodo.18211854 (visible + PDF metadata)
- **PDF bookmark hygiene:** `\texorpdfstring` added to all section headings with math
- **Notation & Units box added:** Section 1 defines σ, ΔA_min, Γ₀, τ_obs with dimensions and units
- **Citations added:** Nambu–Goto action [1,2], WKB/instanton method [3,4], topological sectors [5,6]
- **Numerical verification synchronized:** Corrected to S/ℏ ~ 1–2 for QCD tension (marginal suppression)
- **Route A caveat clarified:** Robust freezing requires P-σ (σ >> σ_QCD) OR Route B
- **P-σ postulate explicit:** Listed as required dependency for Route A

### v1.1 → v1.2 (2026-01-13)

- **FIX 1:** Transition rate Γ definition corrected from `lim_{t→∞}` to `lim_{t→0+}`
- **FIX 2:** Route B restructured into B1[M] + B2[P] + B3[Dc]
- **FIX 3:** Units discipline added (natural units ℏ = c = 1)
- **FIX 4:** Part I numerical check clarified as order-of-magnitude estimate

### v1.0 → v1.1 (2026-01-12)

- T1 classification fixed: [D]/[P] → [P]
- Numerical verification Part I added
- Dimensional fix for natural units

---

## Section 1: Notation and Units

> **Notation & Units Box**
>
> **Symbols:**
> - σ — membrane tension; dimensions [Energy]² = [Length]⁻² in natural units
> - ΔA_min — minimum worldsheet area swept during an orientation change; dimensions [Length]²
> - Γ₀ — attempt frequency (prefactor); dimensions [Time]⁻¹
> - τ_obs — observation timescale; dimensions [Time]
> - τ_relax = 1/Γ_max — relaxation time
>
> **Unit system:**
> - Natural units: ℏ = c = 1
> - In natural units, σ · ΔA is *dimensionless* (= action in units of ℏ)
> - SI conversion: σ_SI = σ × (ℏc) with [σ_SI] = J/m²
>
> **Reference values (QCD string tension):**
> - √σ_QCD ≈ 440 MeV, so σ_QCD ≈ 0.19 GeV²
> - Flux tube radius: r ~ 0.3–0.5 fm
> - Typical ΔA ~ 0.3 fm²

---

## Executive Summary

**Main Result:**
$$
\boxed{\tau_{\mathrm{relax}} \gg \tau_{\mathrm{obs}} \quad \Leftarrow \quad \sigma \Delta A \gg \hbar \quad \text{OR} \quad \text{topological protection}}
$$

**Two independent derivation routes:**
- **Route A:** Large-σ instanton barrier → exponential suppression of transition rates
- **Route B:** Topological protection → winding number conservation blocks transitions

**Important caveat (Route A):** With QCD string tension alone, S/ℏ ~ 1–2, giving only marginal suppression (e⁻¹·⁴ ≈ 0.25). Robust exponential freezing requires:
1. σ >> σ_QCD (P-σ postulate), OR
2. Topological protection (Route B)

---

## Part A: Definitions [D]

### A.1 Configuration Space Transitions

**Definition A.1 (θ-sector) [D]:**
A θ-sector is a connected component of configuration space Q = S³ × S³ × S³ distinguished by the orientation state of the three quark flux tubes.

**Definition A.2 (Transition Rate) [D]:**
The transition rate from sector θ to sector θ' is defined via the small-time limit:
$$
\Gamma(\theta \to \theta') := \lim_{t \to 0^+} \frac{P(\theta' | \theta, t)}{t}
$$
where P(θ'|θ,t) is the probability of finding the system in θ' at time t given it started in θ at t = 0.

This definition matches the Fermi golden rule rate and the off-diagonal generator of a master equation [3].

### A.2 Relaxation Time

**Definition A.3 (Relaxation Time) [D]:**
$$
\tau_{\mathrm{relax}} := \frac{1}{\Gamma_{\mathrm{max}}}
$$
where Γ_max := max_{θ,θ'} Γ(θ → θ') is the maximum transition rate over all sector pairs.

### A.3 Observation Time

**Definition A.4 (Observation Time) [D]:**
$$
\tau_{\mathrm{obs}} := \text{characteristic measurement window}
$$

### A.4 Frozen Criterion

**Definition A.5 (Frozen Criterion) [D]:**
A system is frozen if:
$$
\Gamma_{\mathrm{max}} \cdot \tau_{\mathrm{obs}} \ll 1 \quad \Leftrightarrow \quad \tau_{\mathrm{relax}} \gg \tau_{\mathrm{obs}}
$$

---

## Part B: What Is "Relaxation" in EDC Y-Junction?

### B.1 Physical Picture

**Definition B.1 (Y-Junction Configuration) [D]:**
The proton consists of three quarks connected by flux tubes meeting at a central Y-junction. Each flux tube has:
- Position in 4D spacetime
- Orientation in the 5D bulk (parameterized by θ_i ∈ S³)

**Definition B.2 (Relaxation Event) [D]:**
A relaxation event is a change in the orientation sector:
$$
(\theta_1, \theta_2, \theta_3) \to (\theta_1', \theta_2', \theta_3')
$$

### B.2 Types of Relaxation

**Type 1: Continuous Rotation [D]:**
Smooth rotation of flux tube orientation with action cost proportional to angular velocity.

**Type 2: Reconnection ("String Breaking") [D]:**
Discontinuous topology change; costs action proportional to new area created.

**Proposition B.1 (Dominant Mechanism) [P]:**
In the large-σ limit, relaxation is dominated by continuous rotation with barrier from membrane tension.

---

## Part C: Route A — Large-σ Instanton Barrier

### C.0 Units Convention

**Convention [D]:** Throughout Route A, we work in **natural units** where ℏ = c = 1. In these units, σ · ΔA is dimensionless.

### C.1 Action for Configuration Change

**Postulate C.1 (Membrane Action) [P]:**
The 5D EDC action for the flux tube membrane is the Nambu–Goto action [1,2]:
$$
S_{\mathrm{membrane}} = \sigma \int d^2\xi \sqrt{-\det h_{ab}}
$$
where σ is the membrane tension and h_ab is the induced metric on the worldsheet.

**Theorem C.1 (Action Difference) [Dc]:**
A transition from configuration θ to θ' requires additional worldsheet area ΔA:
$$
\Delta S = \sigma \cdot \Delta A
$$

### C.2 Euclidean Path Integral

**Theorem C.2 (Semiclassical Approximation) [M]:**
For large action barriers, the transition rate is dominated by the saddle point (WKB/instanton method [3,4]):
$$
\Gamma(\theta \to \theta') \sim \Gamma_0 \, e^{-\Delta S / \hbar}
$$

### C.3 Frozen Condition from Large σ

**Theorem C.3 (Large-σ Freezing) [Dc]:**
If σ · ΔA_min >> ℏ (i.e., >> 1 in natural units), then:
$$
\Gamma \ll \Gamma_0 \quad \Rightarrow \quad \tau_{\mathrm{relax}} \to \infty
$$

### C.4 Explicit Bound

**Corollary C.1 (Frozen Criterion from σ) [Dc]:**
The frozen criterion is satisfied if:
$$
\boxed{\sigma \cdot \Delta A_{\mathrm{min}} > \hbar \cdot \ln(\Gamma_0 \cdot \tau_{\mathrm{obs}})}
$$

---

## Part D: Route B — Topological Protection

Route B is structured into three logically distinct parts.

### D.1 Part B1: Mathematical Invariance [M]

**Theorem D.1 (Homotopy Invariance) [M]:**
Winding numbers are invariants under continuous deformations. This is a standard result in algebraic topology [5].

### D.2 Part B2: Physical Admissibility Postulate [P]

**Postulate D.1 (No Topology-Changing Processes) [P]:**
During τ_obs, EDC dynamics forbids membrane cutting, flux tube reconnection, and creation/annihilation of topological defects.

### D.3 Part B3: Consequence — Superselection [Dc]

**Theorem D.2 (Topological Freezing) [Dc]:**
If Postulate D.1 holds:
$$
\Gamma(\theta \to \theta') = 0 \quad \text{if} \quad \mathbf{n}(\theta) \neq \mathbf{n}(\theta')
$$

This gives *exact* superselection, not just exponential suppression [6].

### D.4 Classification Summary for Route B

| Step | Statement | Status | Dependencies |
|------|-----------|--------|--------------|
| B1 | Winding numbers are homotopy invariants | [M] | Algebraic topology |
| B2 | No topology-changing processes during τ_obs | [P] | Physical postulate |
| B3 | Different winding ⇒ Γ = 0 | [Dc] | B1 + B2 |

---

## Part E: Synthesis — Frozen Criterion as [Dc]

### E.1 Combined Statement

**Theorem E.1 (Frozen Criterion from Action/Topology) [Dc]:**
The frozen criterion τ_relax >> τ_obs is satisfied if EITHER:

**(Route A) Large-σ barrier:**
$$
\sigma \cdot \Delta A_{\mathrm{min}} \gg \hbar
$$

**(Route B) Topological protection:**
$$
\text{Winding numbers } \mathbf{n} = (n_1, n_2, n_3) \text{ are conserved}
$$

### E.2 Dependency Chain

| Step | Statement | Status | Dependencies |
|------|-----------|--------|--------------|
| F1 | Γ(θ→θ') = Γ₀ exp(-ΔS/ℏ) | [M] | Instanton calculus |
| F2 | ΔS = σ · ΔA | [Dc] | Membrane action |
| F3 | σ large ⇒ Γ → 0 | [Dc] | F1 + F2 |
| **F5** | **τ_relax >> τ_obs (frozen)** | **[Dc]** | F3 + definition |
| B1 | Winding is homotopy invariant | [M] | Topology |
| B2 | No topology change during τ_obs | [P] | Physical postulate |
| **B3** | **Γ = 0 (exact)** | **[Dc]** | B1 + B2 |

### E.3 What Route A Requires

**Dependencies for Route A [Dc]:**
1. [P] Membrane action with tension σ
2. [P] Large-σ limit: σΔA >> ℏ (P-σ postulate)
3. [M] Instanton/WKB approximation
4. [D] Definition of Γ (small-time limit), τ_relax

---

## Part F: Connection to τ_obs

**Definition F.1 (Observation Time) [D]:**
In EDC, τ_obs is the timescale over which the energy measurement integrates:
$$
E_{\mathrm{measured}} = \frac{1}{\tau_{\mathrm{obs}}} \int_0^{\tau_{\mathrm{obs}}} E(t) \, dt
$$

---

## Part G: Updated Classification

### G.1 Status Change

| Item | v4 Status | v1.3 Status | Change |
|------|-----------|-------------|--------|
| **Frozen criterion** | [P] Postulate | **[Dc] Derived** | **PROMOTED** |
| Dependencies | None stated | σΔA >> ℏ OR B2 | Explicit |

### G.2 Remaining Postulates After v1.3

1. **P-loc** (electron localization) — unchanged
2. **P-ε** (core density form) — unchanged
3. ~~P-frozen-criterion~~ → **L-frozen-criterion [Dc]**
4. **P-SU2-sym** (SU(2)³ isotropy) — unchanged
5. **P-scale** (τL = σa²) — unchanged
6. **P-σ** (large membrane tension) — **Required for Route A**
7. **ΔΩ** (state-cell) — unchanged [P]

**Net change:** Frozen criterion promoted, but requires P-σ for Route A.

---

## Part H: Summary

### H.1 Main Achievement

**Before (v4):**
> "P-frozen-criterion: τ_relax >> τ_obs" [P] — just assumed

**After (v1.3):**
> "L-frozen-criterion: τ_relax >> τ_obs" [Dc] — derived from:
> - Route A: Large membrane tension σΔA >> ℏ ⇒ exponential suppression
> - Route B: Topological winding conservation (B1[M] + B2[P]) ⇒ exact superselection

### H.2 Key Formulas

**Transition rate (corrected definition):**
$$
\Gamma(\theta \to \theta') := \lim_{t \to 0^+} \frac{P(\theta' | \theta, t)}{t}
$$

**Route A (Instanton barrier):**
$$
\Gamma = \Gamma_0 \, e^{-\sigma \Delta A / \hbar} \ll \frac{1}{\tau_{\mathrm{obs}}}
$$

**Route B (Topological protection):**
$$
\Delta \mathbf{n} = 0 \quad \Rightarrow \quad \Gamma = 0
$$

**Frozen criterion (either route):**
$$
\boxed{\tau_{\mathrm{relax}} \gg \tau_{\mathrm{obs}}}
$$

### H.3 What Remains

| Gap | v4 Status | v1.3 Status |
|-----|-----------|-------------|
| Gap 1: Frozen criterion | [P] | **[Dc]** (closed) |
| Gap 2: S³ independence | [P] | [P] (open) |
| Gap 3: SU(2)³ symmetry | [P] | [P] (open) |
| Gap 4: P-loc | [P] | [P] (open) |
| Gap 5: P-ε | [P] | [P] (open) |
| Gap 6: P-scale | [P] | [P] (open) |
| Gap D1: ΔΩ | [P] | [P] (open) |

---

## Part I: Numerical Verification (Order-of-Magnitude)

**Purpose:** Check whether S/ℏ = σΔA/ℏ >> 1 is plausible.

**Caveat:** This is an order-of-magnitude estimate, not a precision calculation.

### I.1 Estimate σ (String/Membrane Tension)

From QCD string tension (natural units ℏ = c = 1):
$$
\sqrt{\sigma_{\mathrm{QCD}}} \approx 440 \text{ MeV} \quad \Rightarrow \quad \sigma_{\mathrm{QCD}} \approx 0.19 \text{ GeV}^2
$$

### I.2 Estimate ΔA_min

- Flux tube radius: r ~ 0.3–0.5 fm
- Minimum angular sweep: Δθ ~ π
- Swept area: ΔA ~ πr² ~ 0.3 fm²

### I.3 Compute S/ℏ

Using 1 fm ≈ 5 GeV⁻¹:
$$
S = \sigma \cdot \Delta A \approx (0.9 \text{ GeV/fm}) \times (0.3 \text{ fm}^2) = 0.27 \text{ GeV·fm}
$$

In natural units:
$$
\frac{S}{\hbar} \approx 0.27 \times 5 \approx 1.4
$$

### I.4 Suppression Factor

$$
e^{-S/\hbar} \approx e^{-1.4} \approx 0.25
$$

This gives Γ ≈ 0.25 Γ₀ — **marginal suppression** with QCD tension alone.

### I.5 Verdict

| Scenario | S/ℏ | Frozen? |
|----------|-----|---------|
| QCD tension, small ΔA | ~1–2 | Marginal (e⁻¹·⁴ ≈ 0.25) |
| Full rotation (ΔA ~ 1 fm²) | ~5 | Moderate (e⁻⁵ ≈ 0.007) |
| Large σ (EDC regime, P-σ) | >> 10 | **Exponential freezing** |

**Conclusion:**
1. Route A with QCD tension gives *marginal* suppression (S/ℏ ~ 1–2).
2. Robust freezing via Route A requires P-σ: σ >> σ_QCD.
3. Alternatively, Route B (topological protection) gives exact Γ = 0.

---

## References

[1] Y. Nambu, "Duality and hydrodynamics," Lectures at the Copenhagen Symposium (1970).

[2] T. Goto, "Relativistic quantum mechanics of one-dimensional mechanical continuum and subsidiary condition of dual resonance model," *Prog. Theor. Phys.* **46**, 1560 (1971).

[3] S. Coleman, *Aspects of Symmetry*, Cambridge University Press (1985), Ch. 7: "The uses of instantons."

[4] R. Rajaraman, *Solitons and Instantons*, North-Holland (1982).

[5] M. Nakahara, *Geometry, Topology and Physics*, 2nd ed., CRC Press (2003), Ch. 4: "Homotopy groups."

[6] S. Weinberg, *The Quantum Theory of Fields*, Vol. II, Cambridge University Press (1995), Ch. 23: "Extended field configurations."

---

**END OF EDC FROZEN CRITERION FROM ACTION v1.3**

*Claude Code, 2026-01-13*

**DOI:** [10.5281/zenodo.18211854](https://doi.org/10.5281/zenodo.18211854)
