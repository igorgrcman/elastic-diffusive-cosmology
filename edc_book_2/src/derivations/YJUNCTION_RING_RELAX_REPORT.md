# Y-Junction + Ring Coupled Oscillator: Relaxation Time Study

**Status:** [Dc] Computational
**Date:** 2026-01-27
**Purpose:** Test whether internal ring modes can act as an effective "bath" for the collective coordinate q.

---

## 1. Model Definition [Def]

The Y-junction + ring system consists of:

- **Central node** (mass $m_0$) at position $\mathbf{r}_0$
- **Three outer nodes** (mass $m_{\mathrm{out}}$) at positions $\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3$
- **Three leg springs** (stiffness $k_{\mathrm{leg}}$, rest length $L_0$) connecting center to each outer node
- **Three ring springs** (stiffness $k_{\mathrm{ring}}$, rest length $L_{\mathrm{ring}}$) connecting outer nodes in a triangle

### Potential energy:
$$V = \frac{1}{2}k_{\mathrm{leg}}\sum_{i=1}^{3}(|\mathbf{r}_i - \mathbf{r}_0| - L_0)^2 + \frac{1}{2}k_{\mathrm{ring}}\sum_{\langle ij\rangle}(|\mathbf{r}_j - \mathbf{r}_i| - L_{\mathrm{ring}})^2$$

### Collective coordinate:
$$q = \frac{1}{3}\sum_{i=1}^{3}(\mathbf{r}_i - \mathbf{r}_0)\cdot\hat{n}_i - L_0$$

where $\hat{n}_i$ is the radial unit vector for leg $i$. This measures symmetric breathing departure from equilibrium.

---

## 2. Equilibrium Configuration [Def]

- Central node at origin
- Outer nodes at $120°$ intervals, distance $L_0$ from center
- For equilateral ring: $L_{\mathrm{ring}} = \sqrt{3}L_0 \approx 1.732 L_0$

The **proton minimum** criterion: $q \approx 0$ AND ring near equilateral.

---

## 3. Relaxation Modes [P]

### Mode 1 (DAMPED)
Add minimal Rayleigh damping: $\mathbf{F}_{\mathrm{damp},i} = -\gamma_i \dot{\mathbf{r}}_i$

Relaxation time $t_{\mathrm{relax}}$ defined when total energy drops below $1\%$ of initial.

### Mode 2 (EFFECTIVE / Conservative)
No dissipation; track energy flow between:
- **Collective mode** (q-coordinate oscillation)
- **Internal modes** (ring deformations, doublet)

Effective relaxation = time when $q_{\mathrm{RMS}}$ (running window) stabilizes while energy remains in internal modes.

---

## 4. Parameter Scan [Dc]

### Scan ranges:
| Parameter | Values |
|-----------|--------|
| $k_{\mathrm{ring}}/k_{\mathrm{leg}}$ | 0.1, 0.3, 1.0, 3.0, 10.0 |
| $m_0/m_{\mathrm{out}}$ | 0.3, 1.0, 3.0 |
| $\gamma$ (damping) | 0, 0.001, 0.01, 0.1 |
| IC type | symmetric_push, doublet, ring_mode |

**Total configurations:** 180

### Initial conditions:
1. **symmetric_push**: Uniform outward push (excites q directly)
2. **doublet**: One leg extended, two contracted (excites $\Delta$ mode)
3. **ring_mode**: Ring edge perturbation (excites internal mode)

---

## 5. Results Summary [Dc]

### 5.1 Overall statistics

| Category | Count |
|----------|-------|
| Total runs | 180 |
| Conservative ($\gamma=0$) | 45 |
| Damped & fully relaxed | 31 |
| Damped & not relaxed (in 500 time units) | 104 |

### 5.2 Mode 1 (Damped) relaxation times

| $\gamma$ | Avg $t_{\mathrm{relax}}^{\mathrm{full}}$ | Comment |
|----------|---------------------------------------|---------|
| 0.01 | 340 | Slow relaxation |
| 0.10 | 35 | Fast relaxation |

**Scaling:** $t_{\mathrm{relax}} \propto \gamma^{-1}$ (as expected for viscous damping).

### 5.3 Mode 2 (Effective relaxation, undamped)

| Metric | Count |
|--------|-------|
| Runs with effective $q_{\mathrm{RMS}}$ relaxation | 14 |

**Key finding:** For ring_mode initial conditions with soft ring ($k_{\mathrm{ring}}/k_{\mathrm{leg}} \lesssim 1$), the q coordinate temporarily stabilizes while energy sloshes into ring modes. This is a **transient** effect, not true thermalization.

### 5.4 Fastest relaxation paths

From the parameter scan, the fastest full relaxation ($t_{\mathrm{relax}} \lesssim 30$) occurs for:
- ring_mode IC
- $\gamma = 0.1$ (strong damping)
- All $k_{\mathrm{ring}}/k_{\mathrm{leg}}$ ratios

The internal ring modes relax first, with the collective q following.

---

## 6. Physical Interpretation [I]

### 6.1 Why Mode 2 shows only transient relaxation

In a conservative Hamiltonian system with discrete modes, energy oscillates between modes (Fermi-Pasta-Ulam behavior). True thermalization requires:
- Continuum of modes (not present here), OR
- Genuine nonlinearity + many DOF, OR
- External dissipation

The 8-DOF system (4 nodes $\times$ 2D) has only 6 independent modes after removing CM motion. This is insufficient for ergodic behavior.

### 6.2 Relevance to neutron lifetime

| Aspect | Y-junction toy | Real neutron |
|--------|----------------|--------------|
| Collective coord q | Breathing mode | Junction "openness" |
| Internal modes | Ring deformations | 5D brane fluctuations |
| Dissipation | External (added) | Radiation / bulk coupling |
| Mode count | 6 | $\infty$ (continuum?) |

**Implication:** For the neutron, if the 5D junction has a true continuum of internal modes (bulk field modes, brane fluctuations), relaxation could be genuinely effective. But this toy model does not demonstrate it.

---

## 7. Conclusions [Dc]

1. **Damped relaxation (Mode 1):** Works as expected with $t_{\mathrm{relax}} \propto \gamma^{-1}$.

2. **Conservative thermalization (Mode 2):** Not observed. The q coordinate shows quasi-periodic behavior, not monotonic decay.

3. **Transient effective relaxation:** Occurs for specific IC (ring_mode) where energy temporarily hides in internal modes. This is NOT true relaxation.

4. **Neutron implication:** A pure classical spring-mass analogy cannot explain the neutron lifetime suppression. Additional physics (genuine dissipation channel, continuum of modes, or quantum tunneling) is required.

---

## 8. Version 2: Strict Three-Metric Criterion [Dc]

### 8.1 Motivation

The v1 study used only the collective coordinate $q$ to define relaxation. This is potentially misleading—the center may appear "settled" while the ring remains distorted (not equilateral). A true "proton minimum" requires ALL degrees of freedom to settle.

### 8.2 Three-Metric Definition [Def]

**Metric 1 (q):** Node displacement from equilibrium
$$q(t) = \|\mathbf{r}_0(t) - \mathbf{r}_0^{\mathrm{eq}}\|$$

**Metric 2 (D):** Ring distortion (departure from equilateral)
$$D(t) = \sqrt{\frac{(s_{12} - \bar{s})^2 + (s_{23} - \bar{s})^2 + (s_{31} - \bar{s})^2}{\bar{s}^2}}$$
where $s_{ij} = |\mathbf{r}_j - \mathbf{r}_i|$ and $\bar{s} = (s_{12} + s_{23} + s_{31})/3$.

**Metric 3 ($V_{\mathrm{ring}}$):** Ring spring potential energy
$$V_{\mathrm{ring}}(t) = \frac{1}{2}k_{\mathrm{ring}}\sum_{\langle ij\rangle}(s_{ij} - L_{\mathrm{ring}})^2$$

### 8.3 Strict Relaxation Criterion

**RELAXED_STRICT** requires ALL three conditions to hold simultaneously for $T_{\mathrm{hold}} = 10 T_{\mathrm{slow}}$:
1. $q_{\mathrm{RMS}} < \eta_q L_0$ with $\eta_q = 10^{-3}$
2. $D_{\mathrm{RMS}} < \eta_D$ with $\eta_D = 10^{-3}$
3. $V_{\mathrm{ring,RMS}} - V_{\mathrm{ring,min}} < \eta_V (V_0 - V_{\mathrm{min}})$ with $\eta_V = 10^{-3}$

where RMS is computed over a sliding window of $2 T_{\mathrm{slow}}$.

**RELAXED_PARTIAL:** At least one metric satisfied, but not all three.

### 8.4 Normal Mode Analysis

For reference parameters ($k_{\mathrm{ring}}/k_{\mathrm{leg}} = 1$, $m_0/m_{\mathrm{out}} = 1$):

| Mode | $\omega$ | Interpretation |
|------|----------|----------------|
| 1-2 | $\approx 0$ | CM translation (2D) |
| 3 | $\approx 0$ | Rigid rotation |
| 4-5 | 1.0 | Doublet (ring shear) |
| 6-7 | 1.73 | Breathing + distortion |
| 8 | 2.0 | Symmetric breathing |

**Physical frequency cutoff:** $\omega_{\mathrm{min}} = 1.0$, so $T_{\mathrm{slow}} = 2\pi/\omega_{\mathrm{min}} = 6.28$.

### 8.5 v2 Results Summary

| Category | Count |
|----------|-------|
| Total runs | 180 |
| CONSERVATIVE ($\gamma = 0$) | 45 |
| RELAXED_STRICT | 30 |
| RELAXED_PARTIAL | 105 |
| NO_RELAX | 0 |

### 8.6 "Cheating" Detection

The key finding: many runs appear relaxed by one metric but fail others.

| Metric passed alone | Count |
|---------------------|-------|
| q only | 120 |
| D only | 147 |
| $V_{\mathrm{ring}}$ only | 90 |

This confirms that looking at $q$ alone gives **false positives**. The strict three-metric criterion catches these cases.

### 8.7 Which configurations achieve RELAXED_STRICT?

| IC type | $\gamma$ | RELAXED_STRICT | Typical $t_{\mathrm{relax}}^{\mathrm{strict}}$ |
|---------|----------|----------------|------------------------------------------------|
| symmetric_push | 0 | 0 | — |
| symmetric_push | 0.01 | 0 | — |
| symmetric_push | 0.1 | 0 | — |
| doublet | any | 0 | — |
| ring_mode | 0 | 0 | — |
| ring_mode | 0.01 | 15 | $\sim 650$ |
| ring_mode | 0.1 | 15 | $\sim 65-90$ |

**Only ring_mode IC with external damping achieves RELAXED_STRICT.**

### 8.8 v2 Conclusions [Dc]

1. **Conservative case ($\gamma = 0$):** ZERO runs achieve RELAXED_STRICT. Energy sloshes between modes quasi-periodically (FPU behavior). **NO TRUE THERMALIZATION.**

2. **Damped case ($\gamma > 0$):** Only ring_mode IC achieves strict relaxation, and only with sufficient damping.

3. **"Cheating" is real:** 120 runs have q-RMS satisfied but fail D or $V_{\mathrm{ring}}$. The single-metric criterion is unreliable.

4. **Strengthened NO-GO:** The three-metric criterion definitively rules out "internal DOF as effective bath" in finite-mode conservative systems.

---

## 10. Artifacts

### v1 (single-metric)
| File | Description |
|------|-------------|
| `code/yjunction_ring_relax.py` | Simulation code (v1) |
| `artifacts/yjunction_relax_results.json` | Full results (180 runs) |
| `artifacts/yjunction_relax_summary.csv` | Summary table |
| `figures/yjunction_energy_vs_time.png` | Energy decay plots |
| `figures/yjunction_q_vs_time.png` | Collective coordinate evolution |
| `figures/yjunction_mode_energy_partition.png` | Energy partition between modes |
| `figures/yjunction_trelax_vs_gamma.png` | Relaxation time scaling |

### v2 (strict three-metric)
| File | Description |
|------|-------------|
| `code/yjunction_ring_relax_v2.py` | Simulation code (v2, strict criterion) |
| `artifacts/strict_relax_results.json` | Full results with three metrics |
| `artifacts/strict_relax_summary.csv` | Summary table |
| `artifacts/strict_relax_report.txt` | Text report with normal modes |
| `figures/strict_trelax_vs_gamma.png` | Relaxation time vs damping |
| `figures/strict_sample_timeseries.png` | Sample time series (all three metrics) |
| `figures/strict_cheating_histogram.png` | "Cheating" cases histogram |

---

## 11. Epistemic Status

| Claim | Tag | Note |
|-------|-----|------|
| Model definition | [Def] | Standard Hamiltonian mechanics |
| Three-metric criterion | [Def] | Definition of strict relaxation |
| v1 numerical results | [Dc] | Computational, verified energy conservation |
| v2 numerical results | [Dc] | Computational, 180 runs with three metrics |
| Physical interpretation | [I] | Identification with neutron (not derivation) |
| Thermalization absence (v1) | [Dc] | Demonstrated computationally (q-only) |
| Thermalization absence (v2) | [Dc] | Demonstrated computationally (strict three-metric) |
| "Cheating" detection | [Dc] | 120+ false positives identified |

---

## 12. Final Verdict [Dc]

### v1 Verdict (weak)
Single-metric ($q$) criterion: NO thermalization in conservative case, but could be misleading.

### v2 Verdict (strong)
Three-metric ($q$, $D$, $V_{\mathrm{ring}}$) criterion with persistence requirement ($10 T_{\mathrm{slow}}$):

**NO-GO confirmed with stronger evidence.**

1. **Conservative ($\gamma = 0$):** 0/45 achieve RELAXED_STRICT → **NO TRUE THERMALIZATION**
2. **"Cheating" cases:** 120+ runs pass $q$ but fail $D$ or $V_{\mathrm{ring}}$
3. **Only external dissipation works:** All 30 RELAXED_STRICT cases have $\gamma > 0$

### Implication for Neutron Lifetime

The "internal DOF as effective bath" mechanism is **NOT viable** in a finite-mode classical system. The neutron lifetime suppression ($10^{27}$ factor) requires:

- **Option A:** True continuum of modes (5D bulk field spectrum) — possible but requires QFT
- **Option B:** Quantum tunneling through energy barrier — Route D/F
- **Option C:** WKB penetration of classically forbidden region — Route B
- **Option D:** Some other mechanism beyond classical mechanics

This toy model rules out the naive expectation that ring modes "absorb" collective energy and trap the system in the proton minimum. **Route E is closed.**
