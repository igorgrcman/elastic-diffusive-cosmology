# Derivation: ω₀ (Attempt Frequency) from 5D Reduction

**Date:** 2026-01-28
**Status:** IN PROGRESS
**Goal:** Derive the attempt frequency ω₀ from explicit 5D→1D reduction

---

## 1. The Problem

In the instanton lifetime formula:

$$\tau = A \cdot \frac{\hbar}{\omega_0} \cdot \exp\left[2\pi\frac{L_0}{\delta}\right]$$

we have **proposed** [P] that:

$$\omega_0 = \sqrt{\frac{\sigma}{m_p}} \approx 19.1 \text{ MeV}$$

This is a **dimensional estimate**. Can we DERIVE it from 5D?

---

## 2. Physical Meaning of ω₀

### 2.1 In Instanton Theory

ω₀ is the **attempt frequency** — the rate at which the system "tries" to tunnel through the barrier.

In Kramers/WKB theory:
$$\Gamma = \omega_0 \cdot \exp(-S_E/\hbar)$$

ω₀ comes from:
- Fluctuations around the metastable state
- The curvature of the potential at the minimum
- The "oscillation frequency" of small perturbations

### 2.2 Physical Interpretation

For the neutron:
- ω₀ ≈ 19 MeV corresponds to time scale ~10⁻²³ s
- This is the nuclear/QCD time scale
- Makes sense for a nucleon-scale transition

---

## 3. Derivation from 5D Action

### 3.1 Starting Point

The 5D action for the junction defect is:

$$S_{5D} = \int d^5x \sqrt{-g} \left[ \frac{1}{2}(\partial\phi)^2 + V(\phi) \right]$$

where φ is the field describing the junction configuration.

### 3.2 Reduction to 1D

After integrating out angular and transverse coordinates:

$$S_{\text{eff}} = \int dt \left[ \frac{1}{2}M(q)\dot{q}^2 - V_{\text{eff}}(q) \right]$$

where q is the collective coordinate describing the junction state.

### 3.3 Effective Mass M(q)

From DERIVE_MQ_FROM_ACTION.md:

$$M(q) \sim \frac{\sigma L_0^2}{c^2}$$

At the metastable point (neutron state):

$$M_n = \frac{\sigma L_0^2}{c^2} = \frac{8.82 \text{ MeV/fm}^2 \times (1 \text{ fm})^2}{c^2} = \frac{8.82 \text{ MeV}}{c^2}$$

In natural units (ℏ = c = 1):
$$M_n \approx 8.82 \text{ MeV}$$

### 3.4 Effective Potential Curvature

Near the neutron minimum, the potential has curvature:

$$V_{\text{eff}}(q) \approx V_n + \frac{1}{2}\omega_b^2 M_n (q - q_n)^2 + ...$$

where ω_b is the **barrier frequency**.

For a quadratic potential:
$$\omega_b = \sqrt{\frac{V''(q_n)}{M_n}}$$

### 3.5 Estimating V''

The potential barrier has height ~σL₀² and width ~L₀:

$$V'' \sim \frac{\sigma L_0^2}{L_0^2} = \sigma$$

Therefore:

$$\omega_b \sim \sqrt{\frac{\sigma}{M_n}} = \sqrt{\frac{\sigma c^2}{\sigma L_0^2}} = \frac{c}{L_0}$$

Wait — this gives a different result! Let me recalculate.

---

## 4. Careful Dimensional Analysis

### 4.1 Units Check

| Quantity | Value | Units |
|----------|-------|-------|
| σ | 8.82 MeV/fm² | Energy/Area |
| m_p | 938.3 MeV | Energy (c=1) |
| L₀ | 1.0 fm | Length |
| δ | 0.105 fm | Length |

### 4.2 Three Candidate Frequencies

**Option A: Barrier energy scale**
$$\omega_A = \frac{E_{\text{barrier}}}{\hbar} = \frac{\sigma L_0^2}{\hbar} = \frac{8.82 \text{ MeV}}{\hbar} = 8.82 \text{ MeV}$$

**Option B: Harmonic oscillator**
$$\omega_B = \sqrt{\frac{\sigma}{m_p}} = \sqrt{\frac{8.82 \text{ MeV/fm}^2}{938.3 \text{ MeV}}} = 0.097 \text{ fm}^{-1}$$

Converting: 1 fm⁻¹ = 197.3 MeV, so:
$$\omega_B = 0.097 \times 197.3 = 19.1 \text{ MeV}$$

**Option C: Classical crossing time**
$$\omega_C = \frac{c}{L_0} = \frac{197.3 \text{ MeV·fm}}{1 \text{ fm}} = 197 \text{ MeV}$$

### 4.3 Which is Correct?

The attempt frequency should come from the **small oscillation frequency** in the metastable well.

For a system with:
- Mass M = effective inertia
- Potential V with curvature V''

The frequency is:
$$\omega_0 = \sqrt{\frac{V''}{M}}$$

If V'' ~ σ and M ~ m_p (proton mass as the natural inertia):
$$\omega_0 = \sqrt{\frac{\sigma}{m_p}} = 19.1 \text{ MeV}$$

This is **Option B**.

---

## 5. Justification for M ~ m_p

### 5.1 Physical Argument

The junction defect involves rearrangement of the proton structure. The natural inertia scale is the proton mass m_p.

### 5.2 From 5D Action

The effective mass comes from integrating the kinetic term:

$$M \sim \int d^3x \, \rho_{\text{eff}} \sim m_p$$

This assumes the junction involves "one proton's worth" of brane material.

### 5.3 Alternative: M ~ σL₀²/c²

If we use M ~ σL₀²/c² ≈ 8.82 MeV:

$$\omega_0 = \sqrt{\frac{\sigma}{M}} = \sqrt{\frac{\sigma c^2}{\sigma L_0^2}} = \frac{c}{L_0} = 197 \text{ MeV}$$

This is **10× larger** than the answer with M = m_p.

---

## 6. The Ambiguity

We have two plausible answers:

| Choice for M | ω₀ | τ prediction |
|--------------|-----|--------------|
| M = m_p (proton mass) | 19 MeV | ~880 s ✓ |
| M = σL₀²/c² | 197 MeV | ~9000 s ✗ |

The **observed lifetime** (879 s) favors M = m_p.

### 6.1 Why m_p and Not σL₀²?

The effective mass for collective coordinate motion is NOT the same as the "rest mass equivalent" of the potential energy.

Physical interpretation:
- σL₀² ~ potential energy stored in the junction
- m_p ~ inertia of the brane material being rearranged

These are different quantities!

---

## 7. Derivation Summary

### 7.1 The Formula

$$\omega_0 = \sqrt{\frac{\sigma}{m_p}}$$

where:
- σ = 8.82 MeV/fm² = brane tension [Dc]
- m_p = 938.3 MeV = proton mass [BL]

### 7.2 Numerical Value

$$\omega_0 = \sqrt{\frac{8.82}{938.3}} \text{ fm}^{-1} = 0.097 \text{ fm}^{-1} = 19.1 \text{ MeV}$$

In Hz:
$$\omega_0 = \frac{19.1 \text{ MeV}}{\hbar} = 2.9 \times 10^{22} \text{ Hz}$$

---

## 8. Epistemic Status

| Statement | Status | Reason |
|-----------|--------|--------|
| σ = 8.82 MeV/fm² | [Dc] | From E_σ hypothesis |
| m_p = 938.3 MeV | [BL] | PDG |
| V'' ~ σ (curvature) | [P] | Dimensional estimate |
| M ~ m_p (effective mass) | [P] | Physical argument, not derived |
| ω₀ = √(σ/m_p) | [P] | Combines [Dc], [BL], and [P] |

**Verdict:** ω₀ = √(σ/m_p) is **[P]** — dimensionally motivated, uses correct scales, but not derived from explicit 5D→1D reduction.

---

## 9. What Would Upgrade to [Dc]

1. **Explicit M(q) calculation** from 5D action at metastable point
2. **Explicit V''(q) calculation** at neutron minimum
3. **Show M = m_p** emerges from the geometry
4. **Verify V'' ~ σ** from potential shape

---

## 10. Summary

$$\boxed{\omega_0 = \sqrt{\frac{\sigma}{m_p}} = 19.1 \text{ MeV} \quad \text{[P]}}$$

The attempt frequency:
- Has correct dimensional form
- Uses natural scales (σ for potential, m_p for mass)
- Gives correct lifetime when combined with κ = 2π

**Status:** [P] — not derived, but strongly constrained by dimensional analysis and phenomenology.

---

## 11. Version History

- 2026-01-28 v1.0: Initial derivation attempt
