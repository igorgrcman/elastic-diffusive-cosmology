# Derivation: Prefactor A from Fluctuation Determinant

**Date:** 2026-01-28
**Status:** IN PROGRESS
**Goal:** Derive the O(1) prefactor A from quantum fluctuations around the instanton

---

## 1. The Problem

In the instanton lifetime formula:

$$\tau = A \cdot \frac{\hbar}{\omega_0} \cdot \exp\left[2\pi\frac{L_0}{\delta}\right]$$

we have treated A as an **O(1) calibration factor** [Cal]:

$$A \approx 0.75 - 0.94$$

**Question:** Can we DERIVE A from first principles?

---

## 2. Origin of the Prefactor

### 2.1 In Instanton Theory

The full decay rate formula is:

$$\Gamma = \frac{\omega_0}{2\pi} \sqrt{\frac{S_E}{2\pi\hbar}} \left(\frac{\det'(-\partial^2 + V''_{\text{false}})}{\det(-\partial^2 + V''_{\text{inst}})}\right)^{1/2} e^{-S_E/\hbar}$$

where:
- det' = determinant with zero mode removed
- V''_false = curvature at false vacuum (neutron state)
- V''_inst = curvature along instanton path

The prefactor A contains:
1. The factor 1/2π
2. The √(S_E/2πℏ) factor
3. The ratio of determinants

### 2.2 Simplified Form

For many instantons, the prefactor simplifies to:

$$A = \frac{1}{2\pi}\sqrt{\frac{S_E}{2\pi\hbar}} \times (\text{determinant ratio})$$

With S_E/ℏ ≈ 60:

$$\frac{1}{2\pi}\sqrt{\frac{60}{2\pi}} = \frac{1}{2\pi}\sqrt{\frac{60}{6.28}} = \frac{1}{6.28} \times 3.09 = 0.49$$

So the "bare" prefactor from S_E alone is ~0.5.

---

## 3. The Fluctuation Determinant

### 3.1 General Theory

The determinant ratio measures quantum fluctuations:
- Fluctuations at false vacuum (oscillation modes)
- Fluctuations along instanton (including zero modes)

For a 1D system:

$$\frac{\det'(-\partial_\tau^2 + V''_{\text{false}})}{\det(-\partial_\tau^2 + V''_{\text{inst}})} = \left(\frac{\omega_0}{\omega_b}\right)^{-1} \times (\text{finite corrections})$$

where ω_b is the barrier frequency.

### 3.2 Typical Values

For symmetric double-well potentials:
- Determinant ratio ≈ 1 to 2

For asymmetric potentials (like neutron → proton):
- May differ from 1

---

## 4. Estimate for EDC Instanton

### 4.1 Collecting Factors

$$A = \frac{1}{2\pi} \times \sqrt{\frac{S_E}{2\pi\hbar}} \times \sqrt{\text{det ratio}}$$

With S_E/ℏ ≈ 58.8 (for L₀/δ ≈ 9.36):

$$A = \frac{1}{2\pi} \times \sqrt{\frac{58.8}{2\pi}} \times \sqrt{R}$$

where R is the determinant ratio.

### 4.2 For R = 1 (naive)

$$A = \frac{1}{2\pi} \times \sqrt{9.37} = \frac{3.06}{6.28} = 0.49$$

### 4.3 For R = 4 (correction factor 4)

$$A = 0.49 \times 2 = 0.98$$

### 4.4 Required Value

To match τ_exp = 879 s with L₀ = r_p + δ = 0.980 fm:

We need A ≈ 0.94 (from EPISTEMIC_CORRECTION_L0_MAP.md)

This corresponds to R ≈ 3.7:

$$A = 0.49 \times \sqrt{3.7} = 0.49 \times 1.92 = 0.94$$

---

## 5. Physical Interpretation of R

### 5.1 What Determines R?

The determinant ratio R depends on:
1. **Shape of the potential** — asymmetry between neutron and proton wells
2. **Zero mode structure** — translational mode of instanton
3. **Collective coordinates** — how many degrees of freedom participate

### 5.2 Expected Value of R

For a simple 1D tunneling problem:
- Symmetric: R ≈ 1
- Asymmetric: R ≈ 1-4
- With multiple modes: R can be larger

R ≈ 4 is plausible for the neutron → proton + e + ν system.

---

## 6. Alternative: Direct Calculation

### 6.1 From ω₀ and ω_b

If we define:
- ω₀ = oscillation frequency at neutron minimum
- ω_b = curvature at barrier top (imaginary frequency)

Then:

$$A \propto \frac{|\omega_b|}{\omega_0}$$

### 6.2 Estimate

If the barrier is "sharper" than the well:
$$\frac{|\omega_b|}{\omega_0} \sim 1-2$$

Combined with the 1/2π factor:
$$A \sim \frac{1}{2\pi} \times (1-2) \times \sqrt{S_E/2\pi} \sim 0.5 - 1$$

This is consistent with A ≈ 0.94.

---

## 7. Summary of Prefactor Estimation

| Factor | Value | Source |
|--------|-------|--------|
| 1/(2π) | 0.159 | Instanton normalization |
| √(S_E/2π) | 3.06 | From S_E ≈ 59 |
| √(det ratio) | ~1.9 | Estimated for asymmetric potential |
| **Total A** | **~0.94** | Product |

---

## 8. Epistemic Status

| Statement | Status | Reason |
|-----------|--------|--------|
| A contains 1/(2π) factor | [M] | Standard instanton theory |
| A contains √(S_E/2πℏ) | [Dc] | From Gaussian integral |
| Determinant ratio R ≈ 4 | [Cal] | Fitted to τ_exp |
| A ≈ 0.94 | [Cal] | Combined estimate |

**Verdict:** A ≈ 0.94 is **[Cal]** — calibrated, not derived.

To upgrade to [Dc]:
1. Calculate det ratio explicitly from 5D potential
2. Derive the shape of V(q) at neutron minimum and barrier
3. Include zero mode properly

---

## 9. Bounds on A

Even without exact calculation, we can bound A:

**Lower bound:** A > 0.1 (from 1/2π alone)
**Upper bound:** A < 10 (typical instanton range)
**Expected:** A ~ 0.5-2 (most instantons)

The required A ≈ 0.94 is **within expected range** — no fine-tuning needed.

---

## 10. Conclusion

$$\boxed{A \approx 0.94 \quad \text{[Cal] — O(1), within expected range}}$$

The prefactor A:
- Is **O(1)** as expected for instantons
- Contains known factors (1/2π, √(S_E/2π))
- Requires determinant ratio R ≈ 4 to match experiment
- Is NOT fine-tuned — falls in natural range

**Status:** [Cal] — calibrated on τ_exp, but within theoretically expected bounds.

---

## 11. Version History

- 2026-01-28 v1.0: Initial estimate
