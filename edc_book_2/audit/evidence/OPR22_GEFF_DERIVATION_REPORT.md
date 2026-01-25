# OPR-22 Evidence Report: G_eff from 5D Mediator Exchange

**Date**: 2026-01-25
**Sprint**: OPR-22 (First-principles G_eff)
**Branch**: book2-opr22-geff-derivation-v1

---

## Executive Summary

This report documents the derivation of the effective four-fermion contact strength G_eff from the 5D gauge-fermion action using Kaluza-Klein reduction. The key result is:

**Main Result**:
$$\boxed{G_{\text{eff}} = \frac{g_5^2 \, \ell}{2 x_1^2} \cdot |f_1(0)|^2}$$

where:
- $g_5$ = 5D gauge coupling [P]
- $\ell$ = domain size [P]
- $x_1$ = first eigenvalue from BVP [Dc]
- $f_1(0)$ = first mode at brane [Dc]

**Status**: CONDITIONAL [Dc] — structure derived; $g_5$, $\ell$, $V(\xi)$, $\kappa$ remain [P].

---

## 1. Starting Point: 5D Gauge-Fermion Action

### Definition (Eq. 22.1)

The 5D gauge field action in warped geometry:

$$S_{\text{gauge}} = -\frac{1}{4g_5^2} \int d^4x \, d\xi \, \sqrt{-G} \, G^{MA} G^{NB} F_{MN} F_{AB}$$

The gauge-fermion interaction:

$$S_{\text{int}} = \int d^4x \, d\xi \, \sqrt{-G} \, J^M A_M$$

**Epistemic status**: [M] — standard field theory definition.

---

## 2. Working Default: Brane-Localized Current

### Assumption (WD-22-1)

The fermion current relevant for weak interactions is localized at $\xi = 0$:

$$J^\mu(x,\xi) = j^\mu(x) \, \delta(\xi)$$

**Rationale**: Standard ansatz in Randall-Sundrum models. Provides clean derivation.

**Alternative** (OPEN-22-1): Bulk current $J^\mu = j^\mu \rho(\xi)$ requires overlap integrals.

**Epistemic status**: [P] — working hypothesis.

---

## 3. Normalization Conventions and Invariance

### 3.1 Convention Table

| Convention | Normalization | $[f_n]$ | $[\tilde{f}_n]$ | Conversion |
|------------|---------------|---------|-----------------|------------|
| Natural | $\int\|f_n\|^2 d\xi = \ell$ | 1 | — | — |
| Unit | $\int\|\tilde{f}_n\|^2 d\xi = 1$ | — | $L^{-1/2}$ | $\tilde{f}_n = f_n/\sqrt{\ell}$ |

### 3.2 Coupling Dimensions

| Quantity | Natural Norm | Unit Norm |
|----------|--------------|-----------|
| $g_5$ | $L^{1/2}$ | $L^{1/2}$ |
| $f_n(0)$ | 1 | $L^{-1/2}$ |
| $g_{\text{eff},n} = g_5 f_n(0)$ | $L^{1/2}$ | 1 |
| $g_{\text{eff},n}^2/m_n^2$ | $L^3$ | $L^2$ |

### 3.3 Normalization Invariance

**Lemma**: Under profile rescaling $f_n \to c \cdot f_n$:

- Normalization: $\int |f_n|^2 \to c^2 \int |f_n|^2$
- Brane evaluation: $f_n(0) \to c \cdot f_n(0)$
- Effective coupling: $g_{\text{eff},n} \to c \cdot g_{\text{eff},n}$

The physical $G_{\text{eff}}$ is **invariant** when conventions are consistently applied.

**Proof**: In natural normalization, $g_{\text{eff},n} = g_5 f_n(0)$ has dimension $L^{1/2}$. The product $g_{\text{eff},n}^2 / m_n^2$ has dimension $L^3$. But this must be multiplied by the normalization factor from the kinetic term, which restores the correct dimension $L^2$.

More directly: In unit normalization, $g_{\text{eff},n} = g_5 \tilde{f}_n(0)$ is dimensionless, so $g_{\text{eff},n}^2 / m_n^2$ has dimension $L^2$ directly.

The key is that the **same** physical observable results from either convention when applied consistently.

---

## 4. Derivation: KK Expansion

### Step 4.1: Mode Decomposition

$$A_\mu(x,\xi) = \sum_{n=0}^{\infty} a_\mu^{(n)}(x) \, f_n(\xi)$$

### Step 4.2: Substitute into Interaction

For brane-localized current:

$$S_{\text{int}} = \int d^4x \, j^\mu(x) \sum_n a_\mu^{(n)}(x) \int d\xi \, \delta(\xi) f_n(\xi)$$

$$= \sum_n \int d^4x \, j^\mu(x) \, a_\mu^{(n)}(x) \, f_n(0)$$

### Step 4.3: Effective 4D Coupling

With canonical normalization, the effective coupling to mode $n$:

$$g_{\text{eff},n} = g_5 \, f_n(0)$$

**Dimensional check** (unit normalization):
- $[g_5] = L^{1/2}$
- $[\tilde{f}_n(0)] = L^{-1/2}$
- $[g_{\text{eff},n}] = 1$ (dimensionless) ✓

---

## 5. Derivation: Integrate Out Mediator

### Step 5.1: Low-Energy Limit

At $E \ll m_1$, the mediator propagator becomes:

$$\frac{1}{p^2 - m_1^2} \xrightarrow{p^2 \ll m_1^2} -\frac{1}{m_1^2}$$

### Step 5.2: Four-Fermion Operator

The exchange diagram generates:

$$\mathcal{L}_{\text{eff}} = -\frac{g_{\text{eff},1}^2}{2 m_1^2} \, (j^\mu j_\mu)$$

The factor 1/2 is the standard Fermi convention.

### Step 5.3: Definition of G_eff

$$G_{\text{eff}} := \frac{g_{\text{eff},1}^2}{2 m_1^2} = \frac{g_5^2 \, f_1(0)^2}{2 m_1^2}$$

---

## 6. Dimensional Analysis

### 6.1 Complete Dimensional Check

**5D Action**:

$$S = -\frac{1}{4g_5^2} \int d^5x \, F^2$$

For $[S] = 1$, $[d^5x] = L^5$, $[F^2] = L^{-4}$:

$$[1/g_5^2] \cdot L^5 \cdot L^{-4} = 1 \implies [g_5^2] = L$$

**4D Lagrangian**:

$$\mathcal{L}_{\text{4D}} = G_{\text{eff}} \, j^\mu j_\mu$$

For $[\mathcal{L}] = L^{-4}$ and $[j^\mu] = L^{-3}$ (brane-localized 4D current):

$$[G_{\text{eff}}] \cdot L^{-6} = L^{-4} \implies [G_{\text{eff}}] = L^2 = \text{GeV}^{-2}$$ ✓

### 6.2 Formula Dimensional Check

**Unit normalization** ($[\tilde{f}_1(0)] = L^{-1/2}$):

$$G_{\text{eff}} = \frac{g_5^2 \, |\tilde{f}_1(0)|^2}{2 m_1^2}$$

$$[G_{\text{eff}}] = \frac{L \cdot L^{-1}}{L^{-2}} = \frac{1}{L^{-2}} = L^2$$ ✓

**Natural normalization** ($[f_1(0)] = 1$), using $m_1 = x_1/\ell$:

$$G_{\text{eff}} = \frac{g_5^2 \, \ell}{2 x_1^2} \cdot |f_1(0)|^2$$

$$[G_{\text{eff}}] = \frac{L \cdot L}{1} = L^2$$ ✓

---

## 7. Where OPR-21 Enters

### 7.1 Mode Profile Dependency

The formula $G_{\text{eff}} = \frac{g_5^2 \ell}{2 x_1^2} |f_1(0)|^2$ requires:

1. **Eigenvalue $x_1$**: From solving the Sturm-Liouville BVP with potential $V(\xi)$ and Robin BC parameters $\kappa_0$, $\kappa_\ell$. This is the OPR-21 eigenvalue problem.

2. **Mode value $f_1(0)$**: The first massive mode profile evaluated at $\xi = 0$. This comes directly from the OPR-21 BVP solution.

### 7.2 Toy Limit (V = 0, Neumann BC)

For the flat potential with Neumann BC:
- $x_1 = \pi$
- $f_1(\xi) = \sqrt{2} \cos(\pi \xi / \ell)$ (natural normalization)
- $f_1(0) = \sqrt{2}$
- $|f_1(0)|^2 = 2$

**Toy G_eff**:

$$G_{\text{eff}}^{\text{(toy)}} = \frac{g_5^2 \ell}{2 \pi^2} \cdot 2 = \frac{g_5^2 \ell}{\pi^2}$$

### 7.3 Physical Potential

For non-trivial $V(\xi)$ and Robin BC:
- $x_1 = x_1(\kappa, V)$ — depends on BVP
- $f_1(0)$ may be enhanced (peaked at brane) or suppressed (peaked in bulk)
- Both effects modify $G_{\text{eff}}$

**OPR-21 dependence**: The physical value of $G_{\text{eff}}$ cannot be computed until OPR-21 provides the mode solutions for physical $V(\xi)$ and BC parameters.

---

## 8. Connection to OPR-19 and OPR-20

### 8.1 From OPR-19

The 4D coupling normalization (OPR-19, Eq. 19.8):

$$g_{4,n}^2 = \frac{g_5^2}{\ell}$$

This holds for natural normalization with $\int |f_n|^2 d\xi = \ell$.

### 8.2 From OPR-20

The effective contact strength (OPR-20, Eq. 20.11):

$$C_{\text{eff}} = \frac{g_5^2 \, \ell}{x_1^2}$$

**Relation to G_eff**:

$$G_{\text{eff}} = \frac{1}{2} \, C_{\text{eff}} \cdot |f_1(0)|^2$$

**Physical interpretation**:
- $C_{\text{eff}}$ is the contact strength from OPR-20, before specifying current localization
- $|f_1(0)|^2$ is the brane-coupling factor from the Working Default
- Factor 1/2 is the Fermi convention

---

## 9. Dimensional Summary Table

| Quantity | Dimension | Natural units | Notes |
|----------|-----------|---------------|-------|
| $g_5$ | $L^{1/2}$ | $\text{GeV}^{-1/2}$ | 5D gauge coupling |
| $g_5^2$ | $L$ | $\text{GeV}^{-1}$ | |
| $\ell$ | $L$ | $\text{GeV}^{-1}$ | Domain size |
| $m_n$ | $L^{-1}$ | GeV | 4D mass |
| $x_n$ | 1 | dimensionless | $x_n := m_n \ell$ |
| $f_n(\xi)$ | 1 | dimensionless | Natural norm |
| $\tilde{f}_n(\xi)$ | $L^{-1/2}$ | $\text{GeV}^{1/2}$ | Unit norm |
| $C_{\text{eff}}$ | $L^2$ | $\text{GeV}^{-2}$ | OPR-20 contact |
| $G_{\text{eff}}$ | $L^2$ | $\text{GeV}^{-2}$ | This OPR |

**Unit conversion**: 1 fm = 5.0677 GeV⁻¹

---

## 10. Failure Modes Documented

| # | Failure Mode | How to Avoid | Status |
|---|--------------|--------------|--------|
| 1 | Using $G_F$ to fix $g_5$ or $\ell$ | All parameters [P]; no backsolving | ✓ Checked |
| 2 | Confusing unit vs natural normalization | Explicit conversion formulas | ✓ Checked |
| 3 | Missing factor of 2 in Fermi convention | Track from EFT definition | ✓ Checked |
| 4 | Wrong dimension for $g_5$ | State $[g_5] = L^{1/2}$ explicitly | ✓ Checked |
| 5 | Wrong dimension for $f_n$ | State convention (unit vs natural) | ✓ Checked |
| 6 | Ignoring $f_1(0)$ brane evaluation | Include in final formula | ✓ Checked |
| 7 | Assuming $f_1(0) = 1$ without justification | Note: depends on BC and $V(\xi)$ | ✓ Checked |
| 8 | Mixing $C_{\text{eff}}$ with $G_{\text{eff}}$ | Distinct symbols, factor 1/2 | ✓ Checked |
| 9 | Bulk vs brane current confusion | State WD assumption explicitly | ✓ Checked |
| 10 | Circular: using $G_F$ as validation criterion | Label as "external comparison only" | ✓ Checked |
| 11 | Forgetting warp factor | Cf. OPR-19 warp cancellation | ✓ Checked |
| 12 | Wrong eigenvalue indexing ($m_0$ vs $m_1$) | Mediator is $n=1$, not $n=0$ | ✓ Checked |

---

## 11. Summary

### Main Results

**Eq. (22.3)**: G_eff in natural normalization
$$G_{\text{eff}} = \frac{g_5^2 \, \ell}{2 x_1^2} \cdot |f_1(0)|^2$$

**Eq. (22.4)**: Connection to OPR-20
$$G_{\text{eff}} = \frac{1}{2} \, C_{\text{eff}} \cdot |f_1(0)|^2$$

**Eq. (22.5)**: Toy limit
$$G_{\text{eff}}^{\text{(toy)}} = \frac{g_5^2 \, \ell}{\pi^2}$$

### Epistemic Status

| Item | Status |
|------|--------|
| 5D action to 4D EFT | [Dc] |
| Brane-localized current | [P] (WD) |
| Normalization conventions | [Dc] |
| G_eff formula structure | [Dc] |
| Connection to OPR-19/20 | [Dc] |
| Dimensional verification | [M] |
| g₅ value | [P] |
| ℓ value | [P] |
| V(ξ) shape | [P] |
| BC parameters κ | [P] |
| **Overall OPR-22** | **CONDITIONAL [Dc]** |

---

## 12. Cross-References

- **OPR-19**: Provides $g_5 \to g_4$ reduction (Eq. 19.8), warp cancellation
- **OPR-20**: Provides $m_1 = x_1/\ell$ and $C_{\text{eff}} = g_5^2 \ell/x_1^2$
- **OPR-21**: Provides BVP framework, mode profiles, $f_1(0)$ value
- **OPR-01**: σ → M₀ anchor (upstream dependency)
- **OPR-04**: Scale Taxonomy (ℓ distinct from Δ, δ, R_ξ)

---

*Evidence report completed 2026-01-25*
