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

## 8. Artifacts

| File | Description |
|------|-------------|
| `code/yjunction_ring_relax.py` | Simulation code |
| `artifacts/yjunction_relax_results.json` | Full results (180 runs) |
| `artifacts/yjunction_relax_summary.csv` | Summary table |
| `figures/yjunction_energy_vs_time.png` | Energy decay plots |
| `figures/yjunction_q_vs_time.png` | Collective coordinate evolution |
| `figures/yjunction_mode_energy_partition.png` | Energy partition between modes |
| `figures/yjunction_trelax_vs_gamma.png` | Relaxation time scaling |

---

## 9. Epistemic Status

| Claim | Tag | Note |
|-------|-----|------|
| Model definition | [Def] | Standard Hamiltonian mechanics |
| Numerical results | [Dc] | Computational, verified energy conservation |
| Physical interpretation | [I] | Identification with neutron (not derivation) |
| Thermalization absence | [Dc] | Demonstrated computationally |

---

**Verdict:** This toy model demonstrates that finite-mode internal DOF do NOT provide true relaxation in a conservative system. The neutron lifetime problem requires a different mechanism.
