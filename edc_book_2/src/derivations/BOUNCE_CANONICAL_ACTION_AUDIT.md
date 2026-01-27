# Bounce Action Canonical Audit

**Task D** — Formalization of the WKB exponent deficit for neutron lifetime.

**Date**: 2026-01-27
**Status**: COMPLETED
**Branch**: `taskD-bounce-scaling-audit-v1`

---

## Executive Summary

We computed the Euclidean bounce action $B$ for neutron $\beta$-decay in the 5D
junction-oscillation model using **canonical coordinates** $Q(q)$. The results are:

| Quantity | Value | Units | Tag |
|----------|-------|-------|-----|
| $q_B$ (barrier top) | 0.0948 | fm | [Dc] |
| $q_n$ (metastable min) | 0.3732 | fm | [Dc] |
| $V_{\rm barrier}$ | 2.867 | MeV | [Dc] |
| $B$ (canonical) | 1.765 | MeV·fm | [Dc] |
| $B/\hbar$ | 0.00894 | dimensionless | [Dc] |
| $B/\hbar$ required for $\tau_n=879\,$s | 60.7 | dimensionless | [Cal] |
| **Deficit** | 60.7 | dimensionless | [Dc] |
| **Multiplier needed** | $\sim 7 \times 10^3$ | — | [Dc] |

**Conclusion**: The 1D WKB channel with current $V(q)$, $M(q)$ is **not viable**
for reproducing $\tau_n = 879\,$s. The exponent is $\sim 6800\times$ too small.

**Epistemic verdict**: **[NO-GO]** for this specific mechanism unless:
- (a) New geometric factors $\gtrsim 10^4$ emerge from 5D→4D reduction [OPEN]
- (b) Barrier shape differs fundamentally from current ansatz [OPEN]
- (c) Non-WKB mechanism dominates (e.g., resonant tunneling) [OPEN]

---

## 1. Definitions and Unit Dictionary [Def]

| Symbol | Definition | Units |
|--------|------------|-------|
| $q$ | Junction separation (non-canonical) | fm |
| $Q$ | Canonical coordinate: $Q(q) = \int_0^q \sqrt{M(q')}\,dq'$ | MeV$^{1/2}$·fm |
| $M(q)$ | Effective mass: $M_{\rm kin} + M_{\rm curv}$ | MeV |
| $V(q)$ | Effective potential | MeV |
| $B$ | Euclidean bounce action | MeV·fm |
| $B/\hbar$ | Dimensionless action: $B/(\hbar c)$ with $\hbar c = 197.33$ MeV·fm | — |
| $\Gamma_0$ | WKB prefactor (attempt frequency) | Hz |
| $\tau$ | Lifetime: $\tau = \Gamma_0^{-1} \exp(B/\hbar)$ | s |

**Epistemic tags**:
- [Def] = Definition
- [Dc] = Derived/Computed from explicit formulas
- [Cal] = Calibrated to data
- [BL] = Baseline (PDG/CODATA)
- [NO-GO] = Mechanism ruled out
- [OPEN] = Unresolved, requires further work

---

## 2. Canonical Coordinate Method [Dc]

### 2.1 Variable-Mass Lagrangian

The 1D effective Lagrangian from the $S_{\rm 5D} \to S_{\rm eff}[q]$ reduction:
$$
L_{\rm eff} = \frac{1}{2} M(q)\,\dot{q}^2 - V(q)
$$
where $M(q) = M_{\rm kin}(q) + M_{\rm curv}(q)$.

### 2.2 Canonical Transformation

Define the canonical coordinate:
$$
Q(q) = \int_0^q \sqrt{M(q')}\,dq' \qquad \text{[Def]}
$$

In $Q$-space, the Lagrangian becomes:
$$
L = \frac{1}{2}\dot{Q}^2 - V(Q)
$$
which is a **unit-mass** system suitable for standard WKB.

### 2.3 Bounce Action Formulas

**In canonical coordinates** (primary):
$$
B = 2 \int_{Q_B}^{Q_n} dQ\,\sqrt{2\bigl[V(Q) - V_n\bigr]} \qquad \text{[Dc]}
$$

**In original coordinates** (cross-check):
$$
B = 2 \int_{q_B}^{q_n} dq\,\sqrt{2M(q)\bigl[V(q) - V_n\bigr]} \qquad \text{[Dc]}
$$

These must agree identically (verified numerically).

---

## 3. Numerical Implementation [Dc]

### 3.1 Model Parameters

From Task B/C (mechanism A3):

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| $C$ | 100 | MeV·fm$^{-2}$ | [Cal] |
| $\sigma$ | 8.82 | MeV·fm$^{-2}$ | [Dc] from $E_\sigma = m_e c^2/\alpha$ |
| $\delta$ | 0.1 | fm | [P] |
| $\tau$ (curvature) | 20 | MeV·fm$^{-2}$ | [P] |
| $L_0$ | 1.0 | fm | [P] |
| $k$ | 2.0 | — | [P] |

### 3.2 Extrema Finding

1. Sample $V(q)$ on grid $q \in [0.01, 2.0]$ fm with 2000 points
2. Find local extrema via sign changes in $dV/dq$
3. Identify barrier top ($q_B$) and metastable minimum ($q_n$)
4. Verify $V(q_B) > V(q_n)$ (metastability condition)

**Results**:
- $q_B = 0.0948$ fm
- $q_n = 0.3732$ fm
- $V_B = 50.31$ MeV
- $V_n = 47.44$ MeV
- $V_{\rm barrier} = V_B - V_n = 2.87$ MeV

### 3.3 Canonical Coordinate Computation

1. Compute $Q(q)$ via cumulative trapezoidal integration
2. Build interpolator $Q \leftrightarrow q$
3. Transform $V(q) \to V(Q)$

**Results**:
- $Q_B = Q(q_B) = 0.255$ MeV$^{1/2}$·fm
- $Q_n = Q(q_n) = 0.914$ MeV$^{1/2}$·fm
- $\Delta Q = Q_n - Q_B = 0.659$ MeV$^{1/2}$·fm

### 3.4 Bounce Integral

Trapezoidal integration with 1000 points in the under-barrier region.

**Canonical result**: $B = 1.765$ MeV·fm
**Non-canonical result**: $B = 1.765$ MeV·fm
**Relative difference**: $< 10^{-7}$ ✓

---

## 4. Results [Dc]

### 4.1 Bounce Action

$$
B = 1.765 \;\text{MeV·fm} \qquad \Rightarrow \qquad \frac{B}{\hbar} = \frac{B}{\hbar c} = \frac{1.765}{197.33} = 0.00894
$$

### 4.2 WKB Prefactor

From Task C:
$$
\Gamma_0 = \frac{\omega_B}{2\pi} \sqrt{\frac{B}{2\pi\hbar}} = 2.53 \times 10^{23}\;\text{Hz}
$$

### 4.3 Implied Lifetime

$$
\tau = \frac{1}{\Gamma_0} \exp\left(\frac{B}{\hbar}\right) = \frac{1}{2.53 \times 10^{23}} \times e^{0.00894} = 3.99 \times 10^{-24}\;\text{s}
$$

**Experimental**: $\tau_n = 879$ s [BL]

### 4.4 Required Exponent

For $\tau_n = 879$ s with $\Gamma_0 = 2.53 \times 10^{23}$ Hz:
$$
\frac{B}{\hbar}\Bigg|_{\rm req} = \ln(\tau_n \cdot \Gamma_0) = \ln(2.22 \times 10^{26}) = 60.7
$$

**Deficit**: $60.7 - 0.009 \approx 60.7$

---

## 5. Scaling Audit [Dc]

### 5.1 Why is $B/\hbar$ Small?

**Dimensional analysis**:
$$
B \sim \Delta Q \cdot \sqrt{2 V_{\rm barrier}} \sim 0.66 \times \sqrt{2 \times 2.87} \approx 1.6\;\text{MeV·fm}
$$
which matches the numerical result.

**The fundamental issue**: The barrier $V_{\rm barrier} = 2.87$ MeV is **small** compared to
$\hbar\omega \approx 1000$ MeV in the potential well. This gives:
$$
\frac{V_{\rm barrier}}{\hbar\omega} \approx 0.003
$$

In the quantum tunneling regime, $B/\hbar \sim V_{\rm barrier}/\hbar\omega \ll 1$
corresponds to **nearly-classical** escape, not exponentially suppressed tunneling.

### 5.2 Sensitivity Analysis

**Variation of $\delta$** (junction width):
- $\delta = 0.05$ fm: No metastability (barrier vanishes)
- $\delta = 0.10$ fm: $B/\hbar = 0.0089$
- $\delta = 0.15$ fm: $B/\hbar = 0.0061$
- $\delta = 0.20$ fm: $B/\hbar = 0.0046$

Increasing $\delta$ **reduces** $B/\hbar$ (shallower barrier).

**Variation of $L_0$** (characteristic length):
- $L_0 = 0.5$ fm: $B/\hbar = 0.0087$
- $L_0 = 1.0$ fm: $B/\hbar = 0.0089$
- $L_0 = 2.0$ fm: $B/\hbar = 0.0111$

Increasing $L_0$ gives modest gains but **far from sufficient**.

---

## 6. Large-Factor Hunt [OPEN]/[NO-GO]

### 6.1 Geometric Factors Available

From the 5D→4D reduction, potential dimensionless factors:

| Factor | Value | Expression |
|--------|-------|------------|
| $L_0/\delta$ | 10 | Length ratio |
| $(L_0/\delta)^2$ | 100 | Area ratio |
| $(L_0/\delta)^3$ | 1000 | Volume ratio |
| $Z_3$ (junction legs) | 3 | Topology |
| $4\pi$ (solid angle) | 12.6 | Spherical symmetry |

**Maximum plausible geometric factor**: $(L_0/\delta)^3 \times 4\pi \times Z_3 \approx 38{,}000$

### 6.2 Required Multiplier

To achieve $B/\hbar = 60$:
$$
\text{Multiplier} = \frac{60}{0.009} \approx 6{,}700
$$

### 6.3 Verdict

The required multiplier $\sim 7000$ is:
- **Larger** than $(L_0/\delta)^2 = 100$
- **Comparable to** $(L_0/\delta)^3 = 1000$ but still insufficient
- **Smaller** than maximum geometric stack $\sim 38{,}000$

**However**: There is no known derivation path that produces $(L_0/\delta)^3$
or higher powers in the action exponent. The reduction from $S_{\rm 5D}$ to
$S_{\rm eff}[q]$ preserves dimensions and does not generate such factors.

**Conclusion**: **[NO-GO]** for the current mechanism.

---

## 7. Final Status Map

### Claims Updated

| Claim | Previous Status | New Status | Evidence |
|-------|-----------------|------------|----------|
| "WKB gives $\tau_n$" | [P] | **[NO-GO]** | $B/\hbar = 0.009 \ll 60.7$ |
| "$V(q), M(q)$ from first principles" | [Dc] | [Dc] | Corridor B complete |
| "Barrier $V_B \approx 2.9$ MeV" | [Dc] | [Dc] | Verified |
| "Canonical vs non-canonical agree" | — | **[Dc]** | Verified to $10^{-7}$ |

### Open Questions

1. **[OPEN]** Is there a non-WKB mechanism (resonant tunneling, instanton sum)?
2. **[OPEN]** Does the full 5D→4D reduction produce missing factors?
3. **[OPEN]** Is the barrier shape qualitatively different at higher fidelity?
4. **[OPEN]** Do multi-dimensional effects (angular modes) modify $B$?

---

## Artifacts

| File | Description |
|------|-------------|
| `artifacts/bounce_results.json` | Full numerical results |
| `artifacts/bounce_results.csv` | Portable summary |
| `figures/bounce_action_audit.png` | Three-panel diagnostic figure |
| `code/derive_bounce_action_Q.py` | Reproducible computation |

---

## References

- **Task B**: `S5D_TO_SEFF_Q_REDUCTION.md` — $M(q)$, $V(q)$ derivation
- **Task C**: `gamma0_results.json` — Prefactor $\Gamma_0$
- **Framework v2.0, Remark 4.5** — Bulk–brane energy conservation
- **PDG 2024** — $\tau_n = 878.4 \pm 0.5$ s [BL]
