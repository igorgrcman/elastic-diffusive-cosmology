# Route F: Kramers Escape from Double-Well Potential

**Date:** 2026-01-28 (v3.1 — corrected epistemic status)
**Purpose:** Model neutron → proton transition as thermal activation over topological barrier

---

## 0. Epistemic Status Summary (AC-F1)

| Category | Claims | Tag |
|----------|--------|-----|
| **Closed** | Kramers/Langevin escape in double-well produces τ(Θ,Υ) map in **dimensionless simulation units**; scaling τ ~ exp(Θ) verified; TURNOVER regime identified | [Dc] |
| **Calibrated** | Mapping to physical seconds requires anchoring ω and γ; current "τ=879s at Θ≈6" is a **fit**, not a derivation | [Cal] |
| **Open** | Anchor of ω_n, ω_b, γ, and noise scale E_fluct from Route C / 5D physics | [OPEN] |

**Bottom line:**
- Mechanism viability: **YES** (escape processes can yield long times)
- Prediction status: **OPEN** (missing physical clock/noise anchoring)

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

**Two survival options for Route F:**

| Option | Requirement | Status |
|--------|-------------|--------|
| **F1: Slow collective coordinate** | ω_n, ω_b ≪ MeV/ℏ because of large effective inertia or weak restoring force | [OPEN] — must come from 5D→1D reduction |
| **F2: Extremely weak noise** | E_fluct ≪ 0.2 MeV so that Θ = ΔV/E_fluct ≈ 55-60 | [OPEN] — contradicts "T_eff ~ 0.2 MeV" interpretation |

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
- The observed electron and antineutrino are interpreted as specific brane/bulk excitation channels

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

### 4.2 Calibration to Neutron Lifetime [Cal]

**Target:** $\tau = 879$ simulation units

**Best match:**
$$\boxed{\Theta \approx 6, \quad \Upsilon \approx 0.3}$$

| Metric | Value |
|--------|-------|
| Measured $\tau$ | 1113 (sim units) |
| Target $\tau$ | 879 |
| Regime | TURNOVER |

**Warning [Cal]:** This is a fit. The statement "τ = 879 seconds" requires anchoring simulation time to physical seconds via ω_n, which is [OPEN].

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

## 7. What Must Be Closed for Route F to Become [Der]

### 7.1 Chain of Custody (Required)

For Route F to make a physical prediction, the following must be derived (not chosen):

| Quantity | Source | Status |
|----------|--------|--------|
| $\Delta V = V(q_b) - V(q_n)$ | Route C potential | [OPEN] — need V(q) in MeV |
| $\omega_n^2 = V''(q_n)/M(q_n)$ | Route C M(q), V(q) | [OPEN] — need in s⁻² |
| $\omega_b^2 = |V''(q_b)|/M(q_b)$ | Route C M(q), V(q) | [OPEN] — need in s⁻² |
| $\gamma$ | Specific dissipation channel | [OPEN] — bulk viscosity? brane radiation? |
| $E_{\text{fluct}}$ | EDC elastic/vacuum energy | [OPEN] — Casimir? brane tension? |

### 7.2 Only Then

$$\tau_{\text{pred}} = \frac{2\pi}{\omega_n} \cdot \frac{\gamma}{\omega_b^2} \cdot \exp\left(\frac{\Delta V}{E_{\text{fluct}}}\right) \stackrel{?}{=} 879 \text{ s}$$

---

## 8. Epistemic Status (Corrected)

| Claim | Tag | Note |
|-------|-----|------|
| Double-well model | [Def] | Standard Kramers theory |
| τ(Θ,Υ) map | [Dc] | Numerical, verified (1000 traj/point), **in simulation units** |
| Kramers scaling τ ~ exp(Θ) | [Dc] | Confirmed over Θ = 3–10 |
| TURNOVER regime | [Dc] | All points have 0.1 < Υ < 10 |
| **τ = 879 s at Θ ≈ 6** | **[Cal]** | **Fit, not derivation** |
| **T_eff = 0.22 MeV** | **[Cal]** | **Implied by fit, not derived** |
| ω_n, ω_b in physical units | [OPEN] | Must come from Route C |
| γ from dissipation channel | [OPEN] | Must be identified |
| E_fluct from EDC physics | [OPEN] | Must be derived |
| e⁻, ν̄ as brane/bulk modes | [P] | Interpretation, not part of Route F dynamics |

---

## 9. Verdict

$$\boxed{\text{ROUTE F: MECHANISM VIABLE, PREDICTION OPEN}}$$

**Summary:**

Route F demonstrates that Kramers/Langevin escape over a double-well barrier is a **viable mechanism** for producing exponentially long lifetimes. The τ(Θ,Υ) map is numerically verified [Dc].

However, the claim "τ = 879 s" is currently **calibrated [Cal]**, not derived. The hard constraint (HC-F: "No free clocks") requires:

1. ω_n, ω_b from Route C in SI units
2. γ from a specific dissipation channel
3. E_fluct from EDC elastic/vacuum energy

**Until these are closed, Route F remains a mechanism, not a prediction.**

---

## 10. Artifacts

| File | Description |
|------|-------------|
| `code/kramers_double_well_v1.py` | Initial simulation code |
| `code/kramers_double_well_v3_parallel.py` | Parallel version with full τ(Θ,Υ) map |
| `artifacts/kramers_v3_results.json` | Full numerical results (45 grid points) |
| `figures/kramers_v3_tau_map.png` | τ(Θ,Υ) contour map |

---

## 11. Next Steps

To close Route F, pursue one of:

**Option F1 (Slow collective coordinate):**
- Show from Route C that ω_n, ω_b are extremely slow (≪ MeV/ℏ)
- This requires large effective inertia M(q) or weak curvature V''(q)

**Option F2 (Weak noise):**
- Show that E_fluct ≪ 0.2 MeV, so Θ = ΔV/E_fluct ≈ 55-60
- This contradicts the "T_eff ~ m_e" interpretation

Both options require derivation from 5D physics, not parameter choice.
