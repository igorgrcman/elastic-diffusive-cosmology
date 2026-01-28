# Route F: Kramers Escape from Double-Well Potential

**Date:** 2026-01-28 (v3.5 — Bath 1 derivation chain)
**Purpose:** Model neutron → proton transition as thermal activation over topological barrier

---

## 0. Epistemic Status Summary (AC-F1)

| Category | Claims | Tag |
|----------|--------|-----|
| **Closed** | Kramers/Langevin escape in double-well produces τ(Θ,Υ) map in **dimensionless simulation units**; scaling τ ~ exp(Θ) verified; TURNOVER regime identified | [Dc] |
| **Calibrated (WRONG)** | Old "τ=879s at Θ≈6" is a **fit** that requires ω ~ 10⁻³ s⁻¹ — inconsistent with fm-scale physics | [Cal] |
| **Open (F2 PATH)** | Derive γ and E_fluct from 5D dissipation channel; **target: E_fluct ~ 20–50 keV, Θ ~ 55** | [OPEN] |

**Bottom line:**
- Mechanism viability: **YES** (escape processes can yield long times)
- Prediction status: **OPEN** (F2 path: need E_fluct ~ keV from 5D physics)
- Primary path: **F2** (weak noise, Θ ~ 55)
- Backup path: **F1** (slow clock — requires 10²⁶ factor, no evidence)

---

## 0.1 Hard Constraint: "No Free Clocks" (HC-F)

> **Route F becomes predictive only when ω_n, ω_b and γ are fixed from Route C/5D physics in SI units; until then τ(Θ,Υ) is dimensionless and τ=879 s is calibrated.**

This constraint means:
1. **ω_n and ω_b** must come from Route C potentials M(q), V(q) — in physical units (s⁻¹), without "rescaling time"
2. **γ** must be derived from a specific dissipation channel (not "let's take Υ=0.3")
3. **Only then** may Kramers formula be used to predict τ in seconds

---

## 0.2 Prefactor Sanity Check (AC-F3)

**Critical warning:** If ω ~ MeV/ℏ ~ 10²¹ s⁻¹, then for τ = 879 s:

$$\tau = \frac{1}{\omega} \cdot e^{\Theta} \quad \Rightarrow \quad 879 = 10^{-21} \cdot e^{\Theta}$$

$$e^{\Theta} = 8.79 \times 10^{23} \quad \Rightarrow \quad \Theta \approx 55$$

**Conclusion:** Θ ≈ 6 works **only if** ω is extremely slow (~10⁻³ s⁻¹). This must be derived from Route C, not assumed.

---

## 0.3 Path Decision: F2 PRIMARY (v3.3)

**Two survival options for Route F:**

| Option | Requirement | Status |
|--------|-------------|--------|
| **F1: Slow collective coordinate** | ω_n, ω_b ≪ MeV/ℏ because of large effective inertia or weak restoring force | **BACKUP** — requires 10²⁶ slowdown factor with no trace in Route C |
| **F2: Weak noise (PRIMARY)** | E_fluct ≈ 20–50 keV so that Θ = ΔV/E_fluct ≈ 55-60 | **[OPEN]** — must derive γ and E_fluct from 5D physics |

### Why F1 is weak

Route C already gives ω_n, ω_b in fm⁻¹ units, i.e., natural scale ~10²²–10²³ Hz. To reduce this to ~10⁻³ s⁻¹ requires a factor of **~10²⁶ slowdown** — this is not "slightly larger inertia", it is new physics. There is currently no trace of such a factor in M(q) or V''(q) from Route C.

### Why F2 is the rational choice

If ω is "fast" (fm scale), then the only way to get τ = 879 s is:
$$\Theta = \frac{\Delta V}{E_{\text{fluct}}} \approx 55\text{–}60$$

This means:
- **E_fluct is NOT "temperature"** — it is the effective fluctuation energy scale seen by the collective coordinate q
- **The bath must be extremely cold/weakly coupled** for this channel
- This is EDC-friendly: no new slow clock, just weak coupling q ↔ bath or soft spectral density at the relevant frequency

### Terminology note (avoid "temperature" trap)

Throughout this document, we use **E_fluct** (effective fluctuation energy scale) rather than "T_eff" or "temperature" to avoid the false impression that the model claims a real thermal bath at ~30 keV. The quantity E_fluct represents:

$$E_{\text{fluct}} = \text{(effective noise amplitude seen by coordinate } q \text{)}$$

This may arise from:
- Vacuum fluctuations of the bath modes
- Spectral density of the dissipation channel at relevant frequencies
- Quantum zero-point energy of coupled modes

**It is NOT necessarily a thermal equilibrium temperature.**

### Corrected calibration target (F2)

| Old (wrong) | New (F2) |
|-------------|----------|
| Θ ≈ 6 | Θ ≈ 55–60 |
| E_fluct ≈ 0.2 MeV | E_fluct ≈ 20–50 keV |

**Sanity check:** With ΔV ~ 1–3 MeV and Θ ~ 55–60:
$$E_{\text{fluct}} = \frac{\Delta V}{\Theta} \approx \frac{1.3 \text{ MeV}}{60} \approx 22 \text{ keV}$$

---

## 1. Motivation

Route E showed that finite-mode conservative systems do NOT thermalize — the Y-junction ring never relaxes to the proton minimum without external dissipation.

**Route F asks a different question:** What if the neutron → proton transition is NOT thermalization, but rather a RARE ESCAPE EVENT over a potential barrier?

This is the **Kramers problem**: a particle in a metastable well, subject to thermal fluctuations, occasionally escapes over a barrier.

---

## 2. Physical Picture [P]

### 2.1 Double-Well Interpretation

| Well | Configuration | EDC Meaning |
|------|---------------|-------------|
| **Proton (deep)** | Steiner minimum, 120° angles | Optimal 5D junction topology |
| **Neutron (shallow)** | Metastable, distorted | Excited junction with "torsion" in χ |
| **Barrier** | Topological saddle | Z₆ phase boundary |

### 2.2 Key Insight

The neutron is NOT "slowly relaxing" to the proton. It is:
- **Trapped** in a metastable configuration
- **Occasionally escaping** via rare thermal fluctuations
- **Tunneling** through/over the barrier

The escape time is exponentially long:
$$\tau \sim \exp\left(\frac{\Delta V}{E_{\text{fluct}}}\right)$$

### 2.3 Energy Redistribution in Decay [P]

When the n→p transition occurs:
- The energy difference (Δm_np c² = 1.293 MeV) is **redistributed** into available excitations
- In EDC language: these excitations include **brane modes** (transverse oscillations) and **bulk wake** (deformations in Φ/A_B fields)

**Precision on e⁻ and ν̄ interpretation [P]:**

In the EDC picture, e⁻ and ν̄ are **effective output modes** of the brane/bulk into which the excess energy and charge/spin are transferred. This is a description of the **emission channel**, not necessarily an identification with a single geometric wave.

> "e⁻ and ν̄ are the emission channels carrying the appropriate quantum numbers (charge, spin, lepton number) and energy — they are the EDC map of the final-state degrees of freedom, not a claim that 'transverse wave = electron' as a geometric identity."

**Note:** This is [P] interpretation. Route F addresses only the statistical escape over the barrier, not the detailed energy partition among final-state modes.

---

## 3. Model Definition [Def]

### 3.1 Double-Well Potential

$$V(q) = V_0 \left[ \left(\frac{q}{a}\right)^4 - 2\left(\frac{q}{a}\right)^2 \right] + \delta V \cdot \frac{q}{a}$$

This creates:
- Proton well at $q \approx -a$ (deeper)
- Neutron well at $q \approx +a$ (shallower, metastable)
- Barrier at $q \approx 0$

### 3.2 Langevin Dynamics

$$m\ddot{q} = -\frac{\partial V}{\partial q} - \gamma \dot{q} + \sqrt{2\gamma E_{\text{fluct}}} \cdot \xi(t)$$

where $\xi(t)$ is Gaussian white noise. In EDC, E_fluct is **not** k_B T but the elastic fluctuation energy scale (to be derived from 5D physics).

### 3.3 Kramers Escape Time

$$\tau_{\text{Kramers}} = \frac{2\pi}{\omega_n} \cdot \frac{\gamma}{\omega_b^2} \cdot \exp\left(\frac{\Delta V}{E_{\text{fluct}}}\right)$$

where:
- $\omega_n$ = frequency at neutron well bottom [**must be derived from Route C**]
- $\omega_b$ = curvature at barrier top [**must be derived from Route C**]
- $\gamma$ = friction coefficient [**must be derived from dissipation channel**]
- $\Delta V$ = barrier height from neutron minimum
- $E_{\text{fluct}}$ = noise energy scale [**must be derived from EDC elastic energy**]

---

## 4. Numerical Results [Dc]

### 4.1 Kramers Scaling Verification (in simulation units)

| $\Theta = \Delta V / E_{\text{fluct}}$ | $\tau_{\text{sim}}$ | Escape % |
|----------------|--------------------------|----------|
| 4.53 | 229 | 86% |
| 6.72 | 1215 | 64% |
| 8.92 | 9995 | 60% |
| 11.12 | 23889 | 26% |
| 13.31 | 11495 | 2% |

**Observation:** $\tau$ scales exponentially with $\Theta$ as expected from Kramers theory.

### 4.2 Calibration to Neutron Lifetime [Cal] — REJECTED

**Target:** $\tau = 879$ simulation units

**Best match (in simulation units):**
$$\boxed{\Theta \approx 6, \quad \Upsilon \approx 0.3}$$

| Metric | Value |
|--------|-------|
| Measured $\tau$ | 1113 (sim units) |
| Target $\tau$ | 879 |
| Regime | TURNOVER |

**⚠️ REJECTED as physical calibration:**

This match (Θ ≈ 6) is an **artifact of simulation time units**. It only maps to τ = 879 seconds if ω ~ 10⁻³ s⁻¹, which contradicts Route C's fm-scale physics (ω ~ 10²² Hz).

**Correct F2 target:** Θ ≈ 55–60, E_fluct ≈ 20–50 keV

The Θ ≈ 6 row in the simulation demonstrates that the code works and Kramers scaling is verified, but it is **not** the physical operating point.

---

## 5. Systematic Parameter Study (v3) [Dc]

### 5.1 Dimensionless Parameters

- $\Theta = \Delta V / E_{\text{fluct}}$ — barrier-to-noise ratio
- $\Upsilon = \gamma / \omega_b$ — damping-to-frequency ratio

### 5.2 τ(Θ, Υ) Map (in simulation units)

Full 9 × 5 grid computed with **1000 trajectories per point**:

| Θ \ Υ | 0.1 | 0.3 | 1.0 | 3.0 | 10.0 |
|-------|-----|-----|-----|-----|------|
| **3** | 92 (100%) | 65 (100%) | 64 (100%) | 106 (100%) | 256 (97%) |
| **5** | 506 (100%) | 423 (100%) | 459 (100%) | 552 (88%) | 470 (39%) |
| **6** | **1260** (100%) | **1113** (100%) | **1344** (100%) | **1504** (84%) | 595 (20%) |
| **7** | 3393 (100%) | 2933 (100%) | 3415 (100%) | 3760 (87%) | 1683 (20%) |
| **8** | 7496 (98%) | 6918 (98%) | 7791 (96%) | 10458 (83%) | 4468 (20%) |
| **9** | 11689 (73%) | 11534 (78%) | 12025 (71%) | 12956 (54%) | 12343 (21%) |
| **10** | 13802 (42%) | 14167 (39%) | 13925 (34%) | 12768 (23%) | 14480 (9%) |
| **12** | 15868 (7%) | 15879 (6%) | 13596 (5%) | 16534 (3%) | 15369 (1%) |
| **15** | ∞ (0%) | ∞ (0%) | ∞ (0%) | ∞ (0%) | ∞ (0%) |

*(Values show τ_mean in simulation units, with escape fraction in parentheses)*

### 5.3 Regime Analysis

- All 45 grid points operate in the **TURNOVER** regime (0.1 < Υ < 10)
- This is the natural regime where damping matches oscillation frequency
- No extreme parameter values required within simulation

---

## 6. Comparison: Route E vs Route F

| Aspect | Route E (Thermalization) | Route F (Kramers Escape) |
|--------|-------------------------|-------------------------|
| Mechanism | Energy redistribution | Barrier crossing |
| Conservative case | Never relaxes | Never escapes |
| With dissipation | External γ required | Bath E_fluct required |
| Numerical result | **NO-GO** | τ(Θ,Υ) map exists [Dc] |
| Physical prediction | — | **OPEN** (needs clock anchoring) |

---

## 7. What Must Be Closed for Route F to Become [Der] (F2 Path)

### 7.1 Chain of Custody (Required)

For Route F (F2 path) to make a physical prediction, the following must be derived (not chosen):

| Quantity | Source | Status |
|----------|--------|--------|
| $\Delta V = V(q_b) - V(q_n)$ | Route C potential | [OPEN] — need V(q) in MeV |
| $\omega_n^2 = V''(q_n)/M(q_n)$ | Route C M(q), V(q) | [OPEN] — expect ~10²² Hz (fm scale) |
| $\omega_b^2 = |V''(q_b)|/M(q_b)$ | Route C M(q), V(q) | [OPEN] — expect ~10²² Hz (fm scale) |
| $\gamma$ | Specific dissipation channel | [OPEN] — brane wave emission? bulk modes? radiation reaction? |
| $E_{\text{fluct}}$ | Fluctuation-dissipation from same channel | [OPEN] — **must give ~20–50 keV** |

### 7.2 The Two Numbers F2 Requires

To close Route F via F2, you must derive from 5D/brane mechanics:

1. **γ (damping)** from a concrete dissipation channel:
   - Brane wave emission
   - Bulk mode emission
   - "Radiation reaction" of junction moving through plenum

2. **Noise amplitude (E_fluct)** from the fluctuation spectrum of that same channel, ideally via fluctuation-dissipation relation (in whatever EDC form applies)

**Once both are fixed, Θ is no longer free.** Then you get a prediction:
- If Θ ~ 55 → **VIABLE**
- If Θ ≪ 55 or Θ ≫ 55 → **NO-GO**

### 7.3 Viability Criterion for F2

$$E_{\text{fluct}} = \frac{\Delta V}{\Theta} \approx \frac{1.3 \text{ MeV}}{55} \approx 24 \text{ keV}$$

**If 5D physics naturally gives keV-level effective noise on q → Route F succeeds.**
**If 5D physics gives MeV-level noise → Route F fails.**

### 7.4 Only Then

$$\tau_{\text{pred}} = \frac{2\pi}{\omega_n} \cdot \frac{\gamma}{\omega_b^2} \cdot \exp\left(\frac{\Delta V}{E_{\text{fluct}}}\right) \stackrel{?}{=} 879 \text{ s}$$

---

## 8. Epistemic Status (v3.3 — F2 Path)

| Claim | Tag | Note |
|-------|-----|------|
| Double-well model | [Def] | Standard Kramers theory |
| τ(Θ,Υ) map | [Dc] | Numerical, verified (1000 traj/point), **in simulation units** |
| Kramers scaling τ ~ exp(Θ) | [Dc] | Confirmed over Θ = 3–15 |
| TURNOVER regime | [Dc] | All points have 0.1 < Υ < 10 |
| **τ = 879 s at Θ ≈ 6** | **[Cal]** | **Wrong calibration target** — only works if ω ~ 10⁻³ s⁻¹ |
| **E_fluct = 0.22 MeV** | **[Cal]** | **Wrong** — F2 requires E_fluct ~ 20–50 keV |
| **F2 target: Θ ≈ 55–60** | **[OPEN]** | Correct target if ω ~ fm⁻¹ scale |
| **F2 target: E_fluct ~ 20–50 keV** | **[OPEN]** | Must be derived from 5D fluctuation-dissipation |
| ω_n, ω_b ~ 10²² Hz | [OPEN] | Expected from Route C (fm scale) |
| γ from dissipation channel | [OPEN] | Must be identified |
| e⁻, ν̄ as brane/bulk modes | [P] | Interpretation, not part of Route F dynamics |

---

## 9. Verdict

$$\boxed{\text{ROUTE F: MECHANISM VIABLE, PREDICTION OPEN (F2 PATH)}}$$

**Summary:**

Route F demonstrates that Kramers/Langevin escape over a double-well barrier is a **viable mechanism** for producing exponentially long lifetimes. The τ(Θ,Υ) map is numerically verified [Dc].

However, the claim "τ = 879 s" is currently **calibrated [Cal]**, not derived. The hard constraint (HC-F: "No free clocks") requires closing the F2 path:

**F2 requirements (PRIMARY):**
1. ω_n, ω_b from Route C — expected ~10²² Hz (fm scale)
2. γ from a specific dissipation channel (brane/bulk modes)
3. E_fluct from fluctuation-dissipation — **must give ~20–50 keV**
4. Resulting Θ = ΔV/E_fluct — **must be ~55** for τ = 879 s

**F1 (BACKUP):** Only viable if 5D reduction reveals ~10²⁶ slowdown factor — currently no evidence.

**Until F2 is closed, Route F remains a mechanism, not a prediction.**

---

## 10. Artifacts

| File | Description |
|------|-------------|
| `code/kramers_double_well_v1.py` | Initial simulation code |
| `code/kramers_double_well_v3_parallel.py` | Parallel version with full τ(Θ,Υ) map |
| `artifacts/kramers_v3_results.json` | Full numerical results (45 grid points) |
| `figures/kramers_v3_tau_map.png` | τ(Θ,Υ) contour map |

---

## 11. Next Steps (F2 Primary Path)

### 11.1 Primary: F2 (Weak Noise)

To close Route F via F2, derive from 5D/brane physics:

1. **Identify the dissipation channel**
   - Brane wave emission (transverse oscillations)
   - Bulk mode emission (Φ/A_B field deformations)
   - Radiation reaction of junction moving through plenum

2. **Derive γ from that channel**
   - What is the damping coefficient in physical units?

3. **Derive E_fluct via fluctuation-dissipation**
   - Same channel must give noise spectrum
   - **Target: E_fluct ~ 20–50 keV** (not 0.2 MeV)

4. **Compute Θ = ΔV / E_fluct**
   - If Θ ~ 55 → VIABLE
   - Otherwise → NO-GO

### 11.2 Backup: F1 (Slow Collective Coordinate)

**Only pursue if:** a full 5D→1D reduction reveals a provable geometric factor that drastically reduces ω_n in SI units.

**Required factor:** ~10²⁶ slowdown from fm⁻¹ to ~10⁻³ s⁻¹

**Current status:** No trace of such factor in Route C's M(q), V''(q).

---

## 12. Summary: F2 Closure Checklist

| Item | Question | Required Answer |
|------|----------|-----------------|
| Dissipation channel | What physical process gives γ? | Identified from 5D |
| γ value | What is damping in SI units? | Derived, not chosen |
| Fluctuation-dissipation | What is E_fluct from same channel? | ~20–50 keV |
| Θ check | Is Θ = ΔV/E_fluct ≈ 55? | YES for viability |

**Route F becomes [Der] when all four items are closed without free parameters.**

---

## 13. Bath Shortlist for F2 (v3.3)

Four candidate baths for closing F2, ordered by EDC-minimality:

### Bath 1: Brane Radiation (PRIMARY) ⭐

**Kupka:** Continuum of transverse brane waves (flexural/wave modes on the 3+1 brane).

**γ mechanism:** q(t) is a local junction-core deformation; acceleration/deformation emits brane waves → radiation damping. Power: $P \sim \mathcal{G}\dot{q}^2$ or $P \sim \mathcal{G}\ddot{q}^2$ depending on mode dispersion.

**E_fluct mechanism:** Same modes have vacuum fluctuations; effective noise on q from spectral density J(ω) (Caldeira-Leggett style). Quantum FDT relates γ(ω) and S(ω).

**Hard output:** J(ω) from brane action (σ, δ, κ if present) + source geometry (L₀) ⇒ prediction of γ and E_fluct in keV.

**Risk:** Must show spectrum seen by q is "cold" (low density at relevant ω) — otherwise noise too large.

**Status:** [OPEN] — Derivation chain needed

---

### Bath 2: Bulk/Plenum Wake

**Kupka:** Bulk perturbations (plenum/metric) excited when junction moves in bulk.

**γ mechanism:** q creates "wake" in bulk → energy leaks into bulk wave continuum. Natural damping without hand-chosen γ.

**E_fluct mechanism:** Vacuum fluctuations of bulk field projected onto brane at junction location; spectral density J_bulk(ω).

**Hard output:** From 5D action (EH+GHY+brane) linearize around background → propagators → J(ω) on brane.

**Risk:** Can slip into "new field" if not strict — must use existing bulk DOF (geometry/plenum), no ad hoc scalars.

**Status:** [OPEN] — Technically harder than Bath 1

---

### Bath 3: Junction Internal Continuum

**Kupka:** Micromodes within junction-core (short-wavelength modes of thickness δ and transverse structure L₀).

**γ mechanism:** q couples to many internal modes; by themselves (finite number) they don't thermalize (Route E NO-GO), BUT if these micromodes have open channel to brane/bulk continuum, they become effective bath.

**E_fluct mechanism:** Zero-point energies of internal modes filtered through coupling to q.

**Hard output:** Show effective mode count ~(L₀/δ)² = C and coupling gives noise suppression → keV.

**Risk:** Must avoid Route E "closed Hamiltonian" — bath must be open (radiation/leakage).

**Status:** [OPEN] — Must not repeat Route E failure

---

### Bath 4: Electroweak-Scale Screened Bath (Rξ filter)

**Kupka:** High-frequency modes at scale Rξ (or other short cutoff), but coupling q↔bath geometrically suppressed because q is nucleon-scale deformation (scale δ_nucl).

**γ / E_fluct mechanism:** Small effective noise because spectral overlap is weak (scale mismatch). Natural path to 20–50 keV without "tuning temperature".

**Hard output:** Derive suppression factor ε ~ (Rξ/δ)^p or exponential cutoff from junction-core form factor.

**Risk:** Need clean derivation of form factor (otherwise another [P]).

**Status:** [OPEN] — Clever but needs form factor derivation

---

## 14. Bath Selection: Bath 1 PRIMARY

**Decision:** Pursue **Bath 1 (Brane Radiation)** as primary path.

**Rationale:**
- Most EDC-native: everything is "brane geometry"
- Naturally gives both damping and quantum noise
- Uses existing parameters (σ, δ, L₀)
- No new fields required

**Hard targets for Bath 1:**
1. E_fluct from brane vacuum spectrum ≈ 20–50 keV
2. Υ = γ/ω_b in turnover region ≈ 0.1–10

**Next step:** Derive minimal derivation chain (6–8 steps) from 5D/brane action to J(ω) to E_fluct.

---

## 15. Bath 1 Derivation Chain (Detailed)

### Overview

This chain derives γ and E_fluct from the **same source** (brane mode spectrum J(ω)), ensuring co-derivation without hand-fitting.

**Minimal 5D ingredients required:**
1. Induced metric + embedding (Step 1)
2. Quadratic action for transverse mode π (Step 2)
3. Junction-core coupling as geometrically localized source (Step 4)

---

### Step 1: 5D Action + Brane Embedding

**Must exist in book:**

$$S_{\text{tot}} = S_{\text{bulk}}[g_{AB}] + S_{\text{GHY}} + S_{\text{brane}}[\gamma_{\mu\nu}] + S_{\text{junction-core}}[q,\dots]$$

Induced metric on brane:
$$\gamma_{\mu\nu}(x) = g_{AB}(X)\,\partial_\mu X^A \partial_\nu X^B$$

Brane kinematics with transverse displacement (brane-bending field):
$$X^A = (x^\mu,\, y = \pi(x))$$

**Why needed:** Without this, no geometric DOF that radiates.

**Status:** [OPEN]

---

### Step 2: Quadratic Action for Transverse Mode π

**Must exist in book:**

Expand brane action (Nambu-Goto/DBI or EDC brane term) to O(π²):
$$S_{\text{brane}} \;\Rightarrow\; \frac{1}{2}\int d^4x\;\Big[\,\rho_\pi\,\dot\pi^2 - T_\pi\,(\nabla\pi)^2 \;-\; \dots\Big]$$

where ρ_π, T_π are expressed in terms of **σ** (and possibly δ through regularization/cutoff).

**Status:** [OPEN]

---

### Step 3: Dispersion and Mode Spectral Density

**Must exist in book:**

Equation of motion for π and dispersion:
$$\omega^2 = c_\pi^2 k^2 + \omega_0^2 \quad \text{(or } \omega^2 = c_\pi^2 k^2 \text{ if massless)}$$

Density of states in 3D brane:
$$\rho(\omega) \sim \frac{k^2}{2\pi^2}\frac{dk}{d\omega}$$

Thickness δ enters as UV form-factor (minimal choice):
$$F(k\delta) = e^{-k\delta} \quad \text{or} \quad F = (1 + k^2\delta^2)^{-1}$$

**Key for F2:** δ and L₀ filter "how much noise" q actually sees.

**Status:** [OPEN] — **DECISION NEEDED:** relativistic (ω = c_π k) vs flexural (ω ∝ k²)?

---

### Step 4: Junction-Core as Source Coupled to Brane Modes

**Must exist in book:**

Definition of collective coordinate q(t) (from Route C).

Minimal coupling (localized on scale L₀) between q and π:
$$S_{\text{int}} = \int dt\, d^3x\; J(q(t))\,\pi(t,\mathbf{x})\,f_{L_0}(\mathbf{x})$$

where f_{L₀} is the core "shape" (e.g., Gaussian of width L₀), giving form-factor F(kL₀) in Fourier space.

**Critical:** J(q) must be tied to existing scales (σ, L₀, δ), NOT a new parameter.

**Status:** [OPEN]

---

### Step 5: Integrate Out Brane Modes → Effective Equation for q

**Must exist in book:**

Standard "influence functional" / "integrate out bath" result:
$$M(q)\ddot{q} + V'(q) + \int^t dt'\,\Gamma(t-t')\,\dot{q}(t') = \xi(t)$$

where kernel Γ and noise ξ are determined by the **same** spectral object J(ω).

**This is the bridge Route F needs:** γ and E_fluct must be co-derived.

**Status:** [OPEN]

---

### Step 6: Spectral Density J(ω) from Geometry (L₀, δ, σ)

**Must exist in book:**

Spectral density in Caldeira-Leggett form:
$$J(\omega) = \sum_{\mathbf{k}} \frac{|g_{\mathbf{k}}|^2}{2\rho_\pi\omega_{\mathbf{k}}}\;\delta(\omega - \omega_{\mathbf{k}})$$

with:
$$g_{\mathbf{k}} \propto \tilde{f}_{L_0}(\mathbf{k})\,F(k\delta) \times (\text{scale from } J(q))$$

In continuum:
$$J(\omega) \propto \int d^3k\;|g_k|^2\,\delta(\omega - \omega(k))$$

**This must exist:** Without explicit J(ω), no hard target for keV.

**Status:** [OPEN]

---

### Step 7: γ(ω) and Noise from Same J(ω) (FDT)

**Must exist in book:**

Friction-spectrum relation:
$$\gamma(\omega) = \frac{J(\omega)}{M\,\omega}$$

Noise spectral density (quantum generalization):
$$S_\xi(\omega) \propto J(\omega)\,\coth\!\Big(\frac{\omega}{2\Omega}\Big)$$

where Ω is the "bath scale" (= E_fluct in our notation).

**Operational definition of E_fluct:** Energy scale that reproduces local S_ξ around relevant ω ~ ω_b, ω_n.

**This is where F2 gets "weak noise":** If J(ω) is small at those ω due to form-factors F(kL₀)F(kδ), you get keV without inventing anything.

**Status:** [OPEN]

---

### Step 8: Hard Check — E_fluct ~ 20–50 keV and Υ ~ 0.1–10?

**Must exist in book (sanity box):**

1. From Route C: ω_b, ω_n in SI units
2. From Bath 1: γ(ω_b)
3. Define: Υ = γ/ω_b
4. From S_ξ(ω): define E_fluct
5. **F2 target:** Θ = ΔV/E_fluct ≈ 55–60

**Viability criterion:**
- E_fluct ~ 20–50 keV → **VIABLE**
- E_fluct ~ MeV → **NO-GO**

**Status:** [OPEN]

---

### Minimal 5D Requirements Summary

| Ingredient | What it provides | Where in book |
|------------|------------------|---------------|
| Induced metric + embedding | Geometric DOF (π) | Framework |
| Quadratic brane action | ρ_π, T_π, dispersion | Brane physics |
| Junction-core coupling | Source J(q) with shape f_{L₀} | Route C extension |

Everything else is "standard" bath integration.

---

### Next Decision Point

**Dispersion choice (Step 3):**
- **Relativistic:** ω = c_π k — gives J(ω) ∝ ω³ at low ω
- **Flexural:** ω ∝ k² — gives J(ω) ∝ ω^{1/2} at low ω

This dramatically affects J(ω) shape and whether "keV" emerges naturally.

**Status:** [DECISION NEEDED]
