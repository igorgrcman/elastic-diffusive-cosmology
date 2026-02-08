# Epistemic Correction: L₀ = r_p + δ is a brane→5D map, not a derivation

**Date:** 2026-01-28
**Applies to:** Route F / Neutron Lifetime Package (v3.11–v3.12)
**Status:** CORRECTION NOTICE

---

## Why this correction matters

In v3.11–v3.12 analysis we introduced the relation

$$L_0 = r_p + \delta$$

and (incorrectly) labeled it as **[Der]**. This is **not** a derivation: it uses the measured proton charge radius $r_p$, which is a brane observable. Therefore $L_0 = r_p + \delta$ is a **mapping from brane metrology into the 5D parameter set**, i.e. an ansatz, until proven from 5D geometry.

> **Key distinction:** Physical interpretation ≠ geometric derivation.

---

## Correct epistemic ledger (current)

| Component | Formula | Status | Reason |
|-----------|---------|--------|--------|
| Proton charge radius | $r_p$ (PDG) | **[BL]** | Brane measurement |
| Brane thickness | $\delta = \hbar/(2m_p c)$ | **[Dc]** | Used as Compton regularization in the package |
| Junction size | $L_0 = r_p + \delta$ | **[P]** | Brane→5D map (not derived from 5D) |
| Instanton action | $S_E = \kappa(L_0/\delta)$ | **[P]** | Form assumed; κ not derived |
| Topological factor | $\kappa = 2\pi$ | **[P]** | Motivated by winding, not derived in EDC |
| Attempt frequency | $\omega_0 \sim \sqrt{\sigma/m_p}$ | **[P]** | Dimensional estimate (5D→1D reduction not done) |
| Prefactor | $A \sim O(1)$ | **[P]/[Cal]** | Needs fluctuation determinant |
| Tension | $\sigma$ | **[Dc]** | Conditional on the package's $E_\sigma$ hypothesis |

---

## Current working lifetime formula and status

We can write the working expression as

$$\tau = A \frac{\hbar}{\omega_0} \exp\left[\kappa\left(\frac{L_0}{\delta} - \text{brane\_tax}\right)\right]$$

and in the specific "brane-mapped" variant,

$$\tau = A \frac{\hbar}{\omega_0} \exp\left[2\pi \frac{(r_p + \delta)}{\delta}\right]$$

**Status:** This formula is **[P]** with one **[BL]** input ($r_p$). It is **not** "pure 5D" and **not** "parameter-free," because $A$ and $\omega_0$ remain non-derived.

---

## What improved (and what did not)

**Improved:**
- Replaced the arbitrary identification $L_0 = 1.0\,\mathrm{fm}$ **[I]** with a physically motivated brane→5D mapping $L_0 = r_p + \delta$ **[P]**.

**Not improved:**
- We still do not have a 5D derivation of:
  1. The map $r_p \leftrightarrow L_0$
  2. $\kappa$
  3. Brane tax
  4. $\omega_0$
  5. The prefactor $A$

---

## Upgrade roadmap to promote tags

**To promote $L_0 = r_p + \delta$ from [P] to [Dc]**, we must derive from 5D geometry that the measured charge radius corresponds to a projected junction envelope radius reduced by a boundary layer of thickness $\delta$:

$$r_p \stackrel{5D}{=} L_0 - \delta \quad (\text{or an equivalent geometric relation})$$

**To promote the full lifetime to [Dc]/[Der] status** we additionally need:

1. **κ** from 5D homotopy / flux-class change
2. **Brane tax** from 5D boundary conditions (GHY/Israel sector)
3. **ω₀** from explicit 5D→1D reduction (derive $M(q)$, $V(q)$)
4. **A** from the fluctuation determinant around the instanton

---

## Bottom line

Strong numerical alignment remains interesting, but the correct epistemic status is **candidate-level** until these derivations are completed.

---

## Numerical summary

| Variant | $L_0$ (fm) | $S_E$ | $A$ needed | $\tau$ with $A=0.75$ |
|---------|-----------|-------|------------|---------------------|
| $r_p + \delta$ | 0.980 | 58.57 | 0.94 | 702 s (−20%) |
| $(π² − 0.5)δ$ | 0.985 | 58.87 | 0.69 | 953 s (+8%) |
| 1.0 fm [I] | 1.000 | 59.75 | 0.29 | 2299 s |
| Required | 0.984 | 58.79 | — | 879 s |

**Experimental value:** $\tau_{\exp} = 879.4 \pm 0.6$ s (PDG 2024)
