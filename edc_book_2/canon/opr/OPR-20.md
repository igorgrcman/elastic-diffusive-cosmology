# OPR-20: Mediator Mass from ξ-Geometry

**Status**: CONDITIONAL [Dc] — eigenvalue structure derived, parameters [P]
**Created**: 2026-01-25
**Branch**: book2-opr20-mediator-mass-v1

---

## Purpose

Derive the mediator mass scale m_med from the ξ-geometry Sturm–Liouville eigenvalue problem, using only EDC primitives and already-derived infrastructure (OPR-21 BVP structure, OPR-19 coupling reduction).

**Closure criteria**:
- FULL [Dc]: m_med computed from derived potential V(ξ) and derived BC parameters
- CONDITIONAL [Dc]: Eigenvalue structure derived, but V(ξ) or BC parameter remains [P]
- Remains [P]: Any SM observable used as input without derivation

---

## Lemma Chain

### L1: 5D Gauge Field Action [M]

Starting from the canonical 5D gauge action (cf. OPR-19, Eq. 19.1):

$$S_{\text{gauge}}^{(5D)} = -\frac{1}{4g_5^2} \int d^5x \sqrt{-G} \, G^{MA} G^{NB} F_{MN} F_{AB}$$

**Status**: [M] — standard field theory definition

---

### L2: Mode Expansion and Separation of Variables [Dc]

Decompose the gauge field:
$$A_\mu(x,\xi) = \sum_n a_\mu^{(n)}(x) f_n(\xi)$$

Under the warped metric (cf. OPR-19, Eq. 19.2):
$$ds^2 = e^{2A(\xi)} \eta_{\mu\nu} dx^\mu dx^\nu + d\xi^2$$

The 4D field equations become:
$$(\eta^{\mu\nu}\partial_\mu\partial_\nu + m_n^2) a_\alpha^{(n)}(x) = 0$$

where $m_n$ are eigenvalues of the ξ-operator acting on $f_n(\xi)$.

**Status**: [Dc] — standard KK separation

---

### L3: Sturm–Liouville Eigenvalue Problem [Dc]

**Lemma L3.1** (Gauge Mode Equation)

The extra-dimensional profile $f_n(\xi)$ satisfies:

$$\boxed{-\frac{d^2 f_n}{d\xi^2} + V(\xi) f_n(\xi) = m_n^2 f_n(\xi)}$$

where the effective potential V(ξ) arises from:
1. Bulk mass term (if present)
2. Warp factor derivatives: $V_{\text{warp}} = 2A'' + 2(A')^2$
3. Brane-localized contributions

**Domain**: $\xi \in [0, \ell]$ (finite thick-brane interval)

**Status**: [Dc] — derived from 5D action mode expansion

---

### L4: Robin Boundary Conditions [P]/[Dc]

At the domain boundaries, apply Robin BC consistent with Israel junction conditions (cf. OPR-21, L3):

$$f'(0) + \kappa_0 f(0) = 0, \quad f'(\ell) - \kappa_\ell f(\ell) = 0$$

where $\kappa_0, \kappa_\ell$ are BC parameters.

**Limiting cases**:
- $\kappa \to 0$: Neumann BC (bulk insulated)
- $\kappa \to \infty$: Dirichlet BC (brane-localized)

**Status**: Structure [Dc] from variational principle; parameter values [P]

---

### L5: Dimensionless Formulation [Dc]

Define dimensionless coordinate $\tilde{\xi} := \xi/\ell \in [0,1]$ and:

$$\lambda_n := \ell^2 m_n^2, \quad x_n := \sqrt{\lambda_n}, \quad \tilde{V}(\tilde{\xi}) := \ell^2 V(\ell\tilde{\xi})$$

The eigenvalue equation becomes:

$$\left[ -\frac{d^2}{d\tilde{\xi}^2} + \tilde{V}(\tilde{\xi}) \right] \tilde{f}_n(\tilde{\xi}) = \lambda_n \tilde{f}_n(\tilde{\xi})$$

**Physical mass recovery**:
$$\boxed{m_n = \frac{x_n}{\ell}}$$

**Status**: [Dc] — coordinate rescaling (pure mathematics)

---

### L6: Zero Mode Analysis [Dc]

For the zero mode ($m_0 = 0$, $\lambda_0 = 0$):

With flat potential ($\tilde{V} = 0$) and Neumann BC ($\kappa = 0$):
$$f_0'' = 0 \Rightarrow f_0 = \text{const}$$

This is the **massless zero mode** (photon-like for U(1), or W/Z longitudinal partner).

**Status**: [Dc] — direct solution

---

### L7: First Massive Mode (Mediator) [Dc]

**Definition L7.1** (Mediator Mass)

The mediator mass is identified with the first nonzero eigenvalue:

$$\boxed{m_{\text{med}} := m_1 = \frac{x_1}{\ell}}$$

**Flat-potential limit** ($\tilde{V} = 0$):

| BC Type | Eigenvalue $x_1$ | $m_1$ |
|---------|-----------------|-------|
| Neumann-Neumann | $\pi$ | $\pi/\ell$ |
| Dirichlet-Dirichlet | $\pi$ | $\pi/\ell$ |
| Neumann-Dirichlet | $\pi/2$ | $\pi/(2\ell)$ |
| Robin (general $\kappa$) | root of transcendental eq. | $x_1(\kappa)/\ell$ |

**Status**: [Dc] — eigenvalue problem solution structure

---

### L8: Connection to 4D Effective Coupling [Dc]

Combining with OPR-19 (Eq. 19.8), the effective 4D gauge coupling for mode n:

$$\frac{1}{g_{4,n}^2} = \frac{1}{g_5^2} \int_0^\ell d\xi \, |f_n(\xi)|^2$$

The 4D effective contact interaction strength (before overlap factors):

$$C_{\text{eff}} \sim \frac{g_{4,1}^2}{m_1^2} = \frac{g_5^2 \ell^2}{x_1^2 \int_0^\ell d\xi \, |f_1(\xi)|^2}$$

For normalized modes ($\int |f_1|^2 d\xi = 1$):

$$\boxed{C_{\text{eff}} = \frac{g_5^2 \ell^2}{x_1^2}}$$

**Status**: [Dc] — combination of OPR-19 and L7

---

### L9: Scaling Relations [Dc]

**Key scaling** (conditional on parameter values):

$$m_{\text{med}} = \frac{x_1}{\ell} \propto \frac{1}{\ell}$$

For $x_1 \sim \mathcal{O}(\pi)$ and $\ell \sim \mathcal{O}(R_\xi)$:

$$m_{\text{med}} \sim \frac{\pi}{R_\xi} \sim \frac{\pi M_Z}{\hbar c} \sim \text{few} \times M_Z$$

**Caution**: This estimate uses $R_\xi = \hbar c / M_Z$ [BL], which is a baseline anchor, not a derivation.

**Status**: [Dc] structure, [BL] numerical anchor

---

## Assumptions Ledger

| ID | Statement | Status | Reference |
|----|-----------|--------|-----------|
| A-20-1 | Warped metric ansatz with A(ξ) | [P] | L2, OPR-19 |
| A-20-2 | Domain $\xi \in [0, \ell]$ with ℓ postulated | [P] | L3 |
| A-20-3 | Effective potential V(ξ) shape | [P] | L3 |
| A-20-4 | Robin BC parameters $\kappa_0, \kappa_\ell$ | [P] | L4, OPR-21 |
| A-20-5 | Mediator = first massive mode | [P] | L7 (physics identification) |
| A-20-6 | Mode normalization convention | [Dc] | L8, OPR-19 |

---

## No-Smuggling Checklist

| Check | Status |
|-------|--------|
| No $M_W$ as input | ✓ |
| No $M_Z$ as input (except in $R_\xi$ if declared [BL]) | ✓ |
| No $G_F$ as input | ✓ |
| No $v = 246$ GeV as input | ✓ |
| No $\sin^2\theta_W$ as input | ✓ |
| Scale Taxonomy respected | ✓ |
| All rescalings explicit | ✓ |

---

## Failure Modes

| # | Failure Mode | How to Avoid | Status |
|---|--------------|--------------|--------|
| 1 | Using $M_W$ to fix $\ell$ | $\ell$ must remain [P] or be derived from geometry | ✓ Checked |
| 2 | Tuning $V(\xi)$ to match eigenvalue to $M_W$ | Potential must be postulated [P] a priori, not fitted | ✓ Checked |
| 3 | Tuning BC parameter $\kappa$ to match $x_1$ | $\kappa$ must come from junction/action, not SM observables | ✓ Checked |
| 4 | Confusing $m_0$ (zero mode) with $m_1$ (mediator) | Explicit mode labeling | ✓ Checked |
| 5 | Wrong warp factor weight in mass term | Verify against OPR-19: kinetic term has W(ξ)=1 | ✓ Checked |
| 6 | Missing factor of 2 in Robin BC | Consistent with OPR-21 convention | ✓ Checked |
| 7 | Assuming Dirichlet when Robin is physical | State BC assumption explicitly | ✓ Checked |
| 8 | Dimensional mismatch: $[m_n] \neq [1/L]$ | Verify: $[x_n] = 1$, $[\ell] = L$, $[m_n] = 1/L$ | ✓ Checked |
| 9 | Identifying $\ell = R_\xi$ without tag | Must cite Scale Taxonomy assumption (A2) | ✓ Checked |
| 10 | Claiming numerical agreement with $M_W$ as "derivation" | Numerical proximity is [I], not [Dc] | ✓ Checked |

---

## Closure Criteria Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| 5D action to SL form | [Dc] | L1–L3 |
| Dimensionless formulation | [Dc] | L5 |
| Zero mode analysis | [Dc] | L6 |
| First massive mode definition | [Dc] | L7 |
| Scaling relation $m_1 = x_1/\ell$ | [Dc] | L7 |
| Connection to $g_4$ | [Dc] | L8 (via OPR-19) |
| Effective potential V(ξ) | [P] | Not derived |
| BC parameters $\kappa$ | [P] | Structural form from OPR-21, value [P] |
| Domain size $\ell$ | [P] | Not derived |
| **Overall OPR-20** | **CONDITIONAL [Dc]** | |

---

## Cross-Links

- **OPR-19**: g₅ → g₄ dimensional reduction (provides coupling normalization)
- **OPR-21**: BVP mode profiles (provides BC structure and V_eff framework)
- **OPR-04**: Scale Taxonomy ($\ell$ distinct from $\Delta$, $\delta$, $R_\xi$)
- **OPR-22**: First-principles G_F (uses $m_{\text{med}}$ from this OPR)

---

## Open Problems

| ID | Description | Priority |
|----|-------------|----------|
| OPEN-20-1 | Derive V(ξ) from 5D action (complete gauge analog of OPR-21 L2) | HIGH |
| OPEN-20-2 | Derive BC parameter $\kappa$ from Israel junction for gauge field | HIGH |
| OPEN-20-3 | Derive $\ell$ from first principles | HIGH (shared with OPR-19) |
| OPEN-20-4 | Numerical eigenvalue for realistic V(ξ) | MEDIUM |
| OPEN-20-5 | Zero mode interpretation (is it massless photon or eaten?) | MEDIUM |
| OPEN-20-6 | Connection to Higgs mechanism / W mass generation | LOW (depends on gauge embedding) |

---

*Canon file created 2026-01-25*
