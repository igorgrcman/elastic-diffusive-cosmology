# Route F: Neutron Lifetime — Status Box

**Version:** 3.12 (2026-01-28)
**Mechanism:** 5D instanton / topological transition

---

## Quick Status

| Layer | What it provides | Tag | Notes |
|-------|------------------|-----|-------|
| **5D geometry** | Dimensionless action $S_E = \kappa(L_0/\delta)$ | [P] | κ, $L_0/\delta$ not derived |
| **Brane clock** | Conversion $\tau = (\hbar/\omega_0) \times \exp(S_E)$ | [P] | $\omega_0$ ansatz |
| **Brane metrology** | Map $L_0 = r_p + \delta$ | [P] | Uses $r_p$ [BL] |

**Result:** $\tau_{\text{theory}} \approx 700\text{–}950$ s vs $\tau_{\exp} = 879$ s (within factor 1.25)

---

## What is [Dc] vs [P] vs [OPEN]

```
[Dc] DERIVED/DEDUCED:
  • σ = m_e³c⁴/(α³ℏ²) — conditional on E_σ hypothesis
  • δ = ℏ/(2m_p c) — Compton regularization

[P] PROPOSED (ansatz):
  • L₀ = r_p + δ — brane→5D map
  • κ = 2π — topological winding factor
  • ω₀ = √(σ/m_p) — barrier frequency
  • A ~ O(1) — prefactor

[OPEN] NOT PROVEN:
  • Derivation of κ from 5D homotopy
  • Derivation of r_p ↔ L₀ from 5D projection
  • Fluctuation determinant → A
  • "Brane tax" from boundary conditions
```

---

## Formula (current working form)

$$\boxed{\tau = A \cdot \frac{\hbar}{\omega_0} \cdot \exp\left[2\pi\frac{r_p + \delta}{\delta}\right]}$$

| Symbol | Value | Status |
|--------|-------|--------|
| $r_p$ | 0.875 fm | [BL] PDG |
| $\delta$ | 0.105 fm | [Dc] |
| $\omega_0$ | 19.1 MeV | [P] |
| $A$ | 0.75–0.94 | [P]/[Cal] |

---

## Verdict

**CANDIDATE** — numerically viable, epistemically incomplete.

The formula reproduces $\tau_n$ within 25% using O(1) coefficients, but multiple components remain [P] or [OPEN]. Not "parameter-free" until $A$, $\omega_0$, and the $r_p \to L_0$ map are derived from 5D.
