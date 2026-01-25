# OPR-20 Evidence Report: Mediator Mass from ξ-Geometry

**Date**: 2026-01-25
**Sprint**: OPR-20 (Mediator mass from eigenvalue)
**Branch**: book2-opr20-mediator-mass-v1

---

## Executive Summary

This report documents the derivation of the mediator mass scale m_med from the Sturm–Liouville eigenvalue problem on the ξ-domain. The key result is that the mediator mass equals the first nonzero eigenvalue divided by the domain size:

**Main Result**:
$$\boxed{m_{\text{med}} = m_1 = \frac{x_1}{\ell}}$$

where $x_1$ is the dimensionless first eigenvalue and $\ell$ is the domain size.

**Status**: CONDITIONAL [Dc] — eigenvalue structure derived; V(ξ), ℓ, and BC parameters remain [P].

---

## 1. Starting Point: 5D Gauge Action

### Definition (Eq. 20.1)

From OPR-19, the 5D gauge action:

$$S_{\text{gauge}}^{(5D)} = -\frac{1}{4g_5^2} \int d^5x \sqrt{-G} \, G^{MA} G^{NB} F_{MN} F_{AB}$$

**Epistemic status**: [M] — standard gauge theory definition.

---

## 2. Mode Expansion

### Kaluza-Klein Decomposition (Eq. 20.2)

$$A_\mu(x,\xi) = \sum_n a_\mu^{(n)}(x) f_n(\xi)$$

where:
- $a_\mu^{(n)}(x)$ are 4D gauge fields satisfying $(\Box + m_n^2) a_\mu^{(n)} = 0$
- $f_n(\xi)$ are mode profiles on $\xi \in [0, \ell]$
- $m_n$ are the 4D mass eigenvalues

**Epistemic status**: [Dc] — standard KK technique.

---

## 3. Derivation of the Eigenvalue Equation

### Step 3.1: Substitute into Action

The $F_{\mu\nu}F^{\mu\nu}$ term (after warp cancellation, cf. OPR-19):

$$S_{\text{kinetic}} = -\frac{1}{4g_5^2} \sum_{n,m} \int d^4x \, f_{\mu\nu}^{(n)} f^{(m)\mu\nu} \int_0^\ell d\xi \, f_n(\xi) f_m(\xi)$$

### Step 3.2: The F_{μ5}F^{μ5} Term

This term, with warp factor weight $e^{2A}$ (cf. OPR-19, §4.4):

$$S_{\text{mass}} = -\frac{1}{2g_5^2} \sum_{n,m} \int d^4x \, a_\mu^{(n)} a^{(m)\mu} \int_0^\ell d\xi \, e^{2A(\xi)} f_n'(\xi) f_m'(\xi)$$

### Step 3.3: Integration by Parts

Integrating by parts on the ξ-integral:

$$\int_0^\ell d\xi \, e^{2A} f_n' f_m' = \left[ e^{2A} f_n' f_m \right]_0^\ell - \int_0^\ell d\xi \, f_m \frac{d}{d\xi}(e^{2A} f_n')$$

### Step 3.4: Self-Adjoint Form

Define the operator:
$$\mathcal{L} f := -\frac{1}{w(\xi)} \frac{d}{d\xi}\left( p(\xi) \frac{df}{d\xi} \right) + q(\xi) f$$

With:
- $p(\xi) = e^{2A(\xi)}$ (from integration by parts)
- $w(\xi) = 1$ (from kinetic term normalization — warp cancellation!)
- $q(\xi) = V(\xi)$ (effective potential from bulk mass terms)

### Step 3.5: The Sturm-Liouville Equation (Eq. 20.3)

For flat warp ($A = 0$, i.e., $p = 1$) or after appropriate redefinition:

$$\boxed{-\frac{d^2 f_n}{d\xi^2} + V(\xi) f_n(\xi) = m_n^2 f_n(\xi)}$$

**Epistemic status**: [Dc] — derived from 5D action.

---

## 4. Boundary Conditions

### Robin BC from Variational Principle (Eq. 20.4)

The boundary terms from δS = 0 yield Robin conditions (cf. OPR-21, L3):

$$f'(0) + \kappa_0 f(0) = 0$$
$$f'(\ell) - \kappa_\ell f(\ell) = 0$$

**Sign convention**: Outward-pointing derivative at both boundaries.

### Physical Interpretation

- $\kappa = 0$: Neumann (no flux across boundary)
- $\kappa \to \infty$: Dirichlet (field vanishes at boundary)
- $\kappa \in (0, \infty)$: Robin (partial reflection/transmission)

**Epistemic status**: Structure [Dc]; parameter values [P].

---

## 5. Dimensionless Formulation

### Rescaling (Eq. 20.5)

Define:
$$\tilde{\xi} := \frac{\xi}{\ell} \in [0,1]$$

$$\lambda_n := \ell^2 m_n^2, \quad x_n := \sqrt{\lambda_n} = \ell \, m_n$$

$$\tilde{V}(\tilde{\xi}) := \ell^2 V(\ell \tilde{\xi})$$

### Dimensionless Eigenvalue Equation (Eq. 20.6)

$$\left[ -\frac{d^2}{d\tilde{\xi}^2} + \tilde{V}(\tilde{\xi}) \right] \tilde{f}_n(\tilde{\xi}) = \lambda_n \tilde{f}_n(\tilde{\xi})$$

### Physical Mass Recovery (Eq. 20.7)

$$\boxed{m_n = \frac{x_n}{\ell}}$$

**Dimensional check**: $[x_n] = 1$, $[\ell] = L$, $[m_n] = L^{-1} = \text{mass}$ ✓

**Epistemic status**: [Dc] — pure coordinate transformation.

---

## 6. Zero Mode Analysis

### Zero Eigenvalue ($\lambda_0 = 0$)

For flat potential ($\tilde{V} = 0$) with Neumann BC ($\kappa = 0$):

$$\tilde{f}_0'' = 0 \Rightarrow \tilde{f}_0 = \text{const}$$

This is the **massless zero mode**.

### Physical Interpretation

- For U(1): This is the photon (remains massless)
- For SU(2)_L: This is eaten by Higgs mechanism to give W/Z longitudinal modes
- The mediator of weak interactions is the **first massive mode** $m_1$, not $m_0$

**Epistemic status**: [Dc] (mathematics) + [P] (physics identification).

---

## 7. First Massive Mode (Mediator)

### Definition (Eq. 20.8)

$$\boxed{m_{\text{med}} := m_1 = \frac{x_1}{\ell}}$$

### Eigenvalue Table (Flat Potential, V = 0)

| BC at ξ=0 | BC at ξ=ℓ | $x_1$ | $m_1$ |
|-----------|-----------|-------|-------|
| Neumann ($\kappa_0 = 0$) | Neumann ($\kappa_\ell = 0$) | $\pi$ | $\pi/\ell$ |
| Dirichlet ($\kappa_0 \to \infty$) | Dirichlet ($\kappa_\ell \to \infty$) | $\pi$ | $\pi/\ell$ |
| Neumann | Dirichlet | $\pi/2$ | $\pi/(2\ell)$ |
| Dirichlet | Neumann | $\pi/2$ | $\pi/(2\ell)$ |
| Robin ($\kappa_0 = \kappa$) | Robin ($\kappa_\ell = \kappa$) | $x_1(\kappa)$ | $x_1(\kappa)/\ell$ |

### Robin Eigenvalue Equation (Flat Potential)

For symmetric Robin ($\kappa_0 = \kappa_\ell = \kappa$), the eigenvalues satisfy:

$$\tan(x_n) = \frac{2 \kappa \ell x_n}{\kappa^2 \ell^2 - x_n^2}$$

(for even modes) or similar transcendental equation for odd modes.

**Epistemic status**: [Dc] — Sturm-Liouville theory.

---

## 8. Connection to OPR-19 (g₅ → g₄)

### Effective 4D Coupling (Eq. 20.9)

From OPR-19, Eq. 19.8:

$$\frac{1}{g_{4,n}^2} = \frac{1}{g_5^2} \int_0^\ell d\xi \, |f_n(\xi)|^2$$

### Normalization Convention

For the natural normalization $\int_0^\ell |f_n|^2 d\xi = \ell$ (flat zero mode has $f_0 = 1$):

$$g_{4,n}^2 = \frac{g_5^2}{\ell}$$

**Dimensional check**: $[g_5^2/\ell] = L/L = 1$ ✓

### Effective Contact Strength (Eq. 20.10)

The 4D effective Fermi-like coupling structure (before fermion overlaps):

$$\boxed{C_{\text{eff}} = \frac{g_{4,1}^2}{m_1^2} \times (\text{overlap factors})}$$

This invariant structure does not depend on normalization conventions.

### Derivation in 5D Parameters

Using $g_{4,1}^2 = g_5^2/\ell$ and $m_1 = x_1/\ell$:

$$C_{\text{eff}} = \frac{g_5^2/\ell}{(x_1/\ell)^2} = \frac{g_5^2/\ell}{x_1^2/\ell^2} = \frac{g_5^2 \ell}{x_1^2}$$

### Final Form (Eq. 20.11)

$$\boxed{C_{\text{eff}} = \frac{g_5^2 \ell}{x_1^2}}$$

**Dimensional check**: $[g_5^2 \ell / x_1^2] = L \cdot L / 1 = L^2 = \text{GeV}^{-2}$ ✓

**Epistemic status**: [Dc] — combination of OPR-19 normalization + eigenvalue structure.

---

## 9. Scaling Estimates

### Order-of-Magnitude (Conditional on ℓ Identification)

**If** we identify $\ell \sim R_\xi = \hbar c / M_Z$ [BL anchor]:

$$m_{\text{med}} \sim \frac{\pi}{R_\xi} = \frac{\pi M_Z}{\hbar c} \cdot \frac{\hbar c}{1} = \pi \cdot M_Z \approx 286 \text{ GeV}$$

**Caution**: This is an order-of-magnitude estimate, not a derivation.

**If** $x_1 \neq \pi$ due to non-trivial potential or Robin BC:

$$m_{\text{med}} = \frac{x_1}{R_\xi} \cdot M_Z$$

For $x_1 \approx 2.5$: $m_{\text{med}} \approx (2.5/\pi) \cdot 286 \approx 228$ GeV.

**Epistemic status**: [I] identification + [BL] anchor.

---

## 10. Dimensional Analysis Summary

| Quantity | Dimension | Natural units |
|----------|-----------|---------------|
| $g_5$ | $L^{1/2}$ | $\text{GeV}^{-1/2}$ |
| $g_5^2$ | $L$ | $\text{GeV}^{-1}$ |
| $g_4$ | 1 | dimensionless |
| $\ell$ | $L$ | $\text{GeV}^{-1}$ |
| $m_n$ | $L^{-1}$ | GeV |
| $x_n$ | 1 | dimensionless |
| $V(\xi)$ | $L^{-2}$ | $\text{GeV}^2$ |
| $C_{\text{eff}}$ | $L^2$ | $\text{GeV}^{-2}$ |

**Unit conversion**: 1 fm = 5.0677 GeV⁻¹

**Consistency check for $C_{\text{eff}} = g_5^2 \ell / x_1^2$**:
$$[C_{\text{eff}}] = [g_5^2] \cdot [\ell] / [x_1^2] = L \cdot L / 1 = L^2 = \text{GeV}^{-2} \checkmark$$

This matches the required dimension for a 4-fermion contact strength.

**Note**: The full $G_F$ expression will include additional fermion overlap factors from OPR-22 (also of dimension $L^2$ or dimensionless, depending on formulation).

**Epistemic status**: [M] — dimensional analysis verified.

---

## 11. Failure Modes Documented

| # | Failure Mode | How to Avoid | Status |
|---|--------------|--------------|--------|
| 1 | Using $M_W$ to fix $\ell$ | $\ell$ must remain [P] or be derived | ✓ Checked |
| 2 | Tuning $V(\xi)$ to match $m_1 = M_W$ | V(ξ) must be postulated [P] a priori | ✓ Checked |
| 3 | Tuning BC parameter $\kappa$ | $\kappa$ from junction, not SM | ✓ Checked |
| 4 | Confusing $m_0$ with $m_1$ | Explicit mode labeling | ✓ Checked |
| 5 | Wrong warp weight in mass term | Verify: kinetic W=1, mass term has $e^{2A}$ | ✓ Checked |
| 6 | Missing factor of 2 in Robin BC | Consistent with OPR-21 | ✓ Checked |
| 7 | Assuming Dirichlet when Robin physical | State BC [P] explicitly | ✓ Checked |
| 8 | Dimensional mismatch | Verified: $[m_n] = L^{-1}$ | ✓ Checked |
| 9 | Identifying $\ell = R_\xi$ without tag | Scale Taxonomy (A2) required | ✓ Checked |
| 10 | Numerical agreement = derivation | [I] vs [Dc] distinguished | ✓ Checked |

---

## 12. Summary

### Main Results

**Eq. (20.3)**: Sturm-Liouville eigenvalue equation
$$-\frac{d^2 f_n}{d\xi^2} + V(\xi) f_n = m_n^2 f_n$$

**Eq. (20.7)**: Dimensionless eigenvalue definition
$$x_n := m_n \ell \quad \Leftrightarrow \quad m_n = \frac{x_n}{\ell}$$

**Critical**: $x_n = x_n(\kappa, V)$ depends on BVP parameters, NOT universal.

**Eq. (20.8)**: Mediator mass definition
$$m_{\text{med}} = m_1 = \frac{x_1}{\ell}$$

**Eq. (20.11)**: Effective contact strength (invariant + 5D form)
$$C_{\text{eff}} = \frac{g_{4,1}^2}{m_1^2} = \frac{g_5^2 \ell}{x_1^2}$$

### Epistemic Status

| Item | Status |
|------|--------|
| SL equation form | [Dc] |
| Mode expansion | [Dc] |
| Dimensionless eigenvalue definition | [M] |
| Eigenvalue value $x_n(\kappa, V)$ | [Dc] given BVP inputs |
| Connection to OPR-19 | [Dc] |
| Potential V(ξ) | [P] |
| BC parameters κ | [P] |
| Domain size ℓ | [P] |
| **Overall OPR-20** | **CONDITIONAL [Dc]** |

---

## 13. Cross-References

- **OPR-19**: Provides $g_5 \to g_4$ reduction (Eq. 19.8), warp cancellation
- **OPR-21**: Provides BVP framework, Robin BC form, V_eff structure
- **OPR-04**: Scale Taxonomy — $\ell$ distinct from $\Delta$, $\delta$, $R_\xi$
- **OPR-22**: Will use $m_{\text{med}}$ to compute $G_F$

---

*Evidence report completed 2026-01-25*
