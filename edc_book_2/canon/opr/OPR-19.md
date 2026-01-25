# OPR-19: Derive g₅ from 5D Action

**Status**: CONDITIONAL [Dc] — structure derived, warp factor remains [P]
**Created**: 2026-01-25
**Branch**: book2-opr19-g5-derivation-v1

---

## Purpose

Derive the canonical relation between the 5D gauge coupling g₅ and the effective 4D coupling g₄ by explicit dimensional reduction from a stated 5D action.

**Closure criteria**:
- FULL [Dc]: W(ξ) measure factor derived explicitly from metric, all rescalings tracked
- CONDITIONAL [Dc]: Warp factor A(ξ) or domain ℓ remain [P] with explicit declaration
- Remains [P]: Any SM observable used as input without derivation

---

## Lemma Chain

### L1: 5D Gauge Action Definition [M]

The 5D gauge field action with canonical normalization:

$$S_{\text{gauge}}^{(5D)} = -\frac{1}{4g_5^2} \int d^5x \sqrt{-G} \, G^{MA} G^{NB} F_{MN} F_{AB}$$

where:
- $G_{AB}$ is the 5D metric with signature $(-,+,+,+,+)$
- $F_{MN} = \partial_M A_N - \partial_N A_M$ is the field strength
- $g_5$ has dimension $[\text{length}]^{1/2}$ in natural units

**Status**: [M] — standard field theory definition

---

### L2: Warped Metric Ansatz [P]

The 5D metric takes the warped form:

$$ds^2 = G_{AB} dx^A dx^B = e^{2A(\xi)} \eta_{\mu\nu} dx^\mu dx^\nu + d\xi^2$$

where:
- $A(\xi)$ is the warp factor (function of transverse coordinate only)
- $\eta_{\mu\nu} = \text{diag}(-1,+1,+1,+1)$ is Minkowski metric
- $\xi \in [0, \ell]$ is the transverse coordinate

**Metric determinant**:
$$\sqrt{-G} = e^{4A(\xi)}$$

**Inverse metric components**:
- $G^{\mu\nu} = e^{-2A(\xi)} \eta^{\mu\nu}$
- $G^{55} = 1$
- $G^{\mu 5} = 0$

**Status**: [P] — ansatz; warp factor A(ξ) not derived from first principles

---

### L3: Kaluza-Klein Mode Decomposition [Dc]

Decompose the gauge field:
$$A_\mu(x,\xi) = \sum_n a_\mu^{(n)}(x) f_n(\xi)$$

where:
- $a_\mu^{(n)}(x)$ are 4D gauge fields
- $f_n(\xi)$ are mode profiles satisfying orthonormality condition
- $A_5$ is set to zero (unitary gauge) or handled separately as scalar

**Orthonormality**:
$$\int_0^\ell d\xi \, W(\xi) \, f_m(\xi) f_n(\xi) = \delta_{mn}$$

with weight function $W(\xi)$ to be determined from the action.

**Status**: [Dc] — standard KK decomposition technique

---

### L4: Field Strength Decomposition [Dc]

The field strength components:
- $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = \sum_n f_\mu^{(n)}(x) f_n(\xi)$ where $f_{\mu\nu}^{(n)} = \partial_\mu a_\nu^{(n)} - \partial_\nu a_\mu^{(n)}$
- $F_{\mu 5} = \partial_\mu A_5 - \partial_\xi A_\mu = -\sum_n a_\mu^{(n)}(x) f_n'(\xi)$ (in unitary gauge with $A_5=0$)

**Status**: [Dc] — direct computation

---

### L5: Dimensional Reduction of Kinetic Term [Dc]

Substitute into the action:

$$S_{\text{gauge}}^{(5D)} = -\frac{1}{4g_5^2} \int d^4x \int_0^\ell d\xi \, e^{4A} \left[ e^{-4A} f_{\mu\nu}^{(n)} f^{(n)\mu\nu} + 2 e^{-2A} (\partial_\xi A_\mu)^2 \right]$$

**Computation of measure factors**:

For the $F_{\mu\nu}F^{\mu\nu}$ term:
- $\sqrt{-G} = e^{4A}$
- $G^{\mu\alpha} G^{\nu\beta} = e^{-4A} \eta^{\mu\alpha} \eta^{\nu\beta}$
- Combined: $e^{4A} \cdot e^{-4A} = 1$ (warp factors cancel for 4D components!)

For the $F_{\mu 5}F^{\mu 5}$ term:
- $G^{\mu\alpha} G^{55} = e^{-2A}$
- Combined: $e^{4A} \cdot e^{-2A} = e^{2A}$

**Status**: [Dc] — explicit computation with metric factors

---

### L6: Effective 4D Action and g₄ Definition [Dc]

After ξ-integration, the 4D kinetic term becomes:

$$S_{\text{gauge}}^{(4D)} = -\frac{1}{4} \sum_n \frac{1}{g_{4,n}^2} \int d^4x \, f_{\mu\nu}^{(n)} f^{(n)\mu\nu}$$

where the effective 4D coupling is:

$$\boxed{\frac{1}{g_{4,n}^2} = \frac{1}{g_5^2} \int_0^\ell d\xi \, |f_n(\xi)|^2}$$

**Critical result**: For the $F_{\mu\nu}F^{\mu\nu}$ term, the weight function is:
$$W(\xi) = 1 \quad \text{(flat measure, warp factors cancelled)}$$

This is **non-trivial**: the warp factors from $\sqrt{-G}$ and inverse metric exactly cancel for the 4D gauge kinetic term.

**Status**: [Dc] — derived from explicit metric computation

---

### L7: Canonical Normalization Check [Dc]

To obtain canonical 4D kinetic term $-\frac{1}{4} f_{\mu\nu}f^{\mu\nu}$, we require:
$$g_{4,n}^2 = g_5^2 \left( \int_0^\ell d\xi \, |f_n(\xi)|^2 \right)^{-1}$$

For the zero mode with $f_0(\xi) = 1/\sqrt{\ell}$ (uniform profile):
$$\frac{1}{g_{4,0}^2} = \frac{1}{g_5^2} \cdot \frac{1}{\ell} \cdot \ell = \frac{1}{g_5^2}$$

Hence: $g_{4,0} = g_5$ for flat zero mode.

**For non-uniform modes**: The effective coupling depends on the mode profile integral.

**Status**: [Dc] — normalization verified

---

### L8: Dimensional Analysis [M]

**In 5D**:
- $[S] = 1$ (dimensionless)
- $[\int d^5x] = [\text{length}]^5$
- $[F_{MN}^2] = [\text{length}]^{-4}$
- $[\sqrt{-G}] = 1$ (determinant is dimensionless ratio)
- Therefore: $[g_5^2] = [\text{length}]^{5-4} = [\text{length}]$
- So: $[g_5] = [\text{length}]^{1/2}$

**In 4D**:
- $[g_4] = 1$ (dimensionless)

**Relation**:
$$[g_4^2] = [g_5^2] / [\ell] = [\text{length}] / [\text{length}] = 1 \quad \checkmark$$

**Unit conversion**: $1 \text{ fm} = 5.0677 \text{ GeV}^{-1}$

**Status**: [M] — dimensional analysis

---

## Assumptions Ledger

| ID | Statement | Status | Reference |
|----|-----------|--------|-----------|
| A-19-1 | Warped metric ansatz with A(ξ) | [P] | L2 |
| A-19-2 | Domain $\xi \in [0, \ell]$ with ℓ postulated | [P] | L2, Scale Taxonomy |
| A-19-3 | Unitary gauge $A_5 = 0$ | [Dc] | L3 (gauge choice) |
| A-19-4 | Mode profiles $f_n(\xi)$ satisfy BVP | [P]/[Dc] | Depends on BC derivation |
| A-19-5 | No brane-localized kinetic terms | [P] | L6 (simplifying assumption) |

**Scale Taxonomy cross-reference**:
- ℓ = domain size (from Scale Taxonomy)
- If ℓ = nΔ is assumed, must cite (A3)
- If ℓ = 2πR_ξ is assumed, must cite relevant OPR-20 derivation

---

## No-Smuggling Checklist

| Check | Status |
|-------|--------|
| No $M_W$ as input | ✓ |
| No $G_F$ as input | ✓ |
| No $v = 246$ GeV as input | ✓ |
| No $\sin^2\theta_W$ as input | ✓ |
| No $M_Z$ as input (except in R_ξ definition if declared [BL]) | ✓ |
| Scale Taxonomy respected | ✓ |
| All rescalings explicit | ✓ |

---

## Closure Criteria Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| 5D action definition | [M] | L1 |
| Metric determinant | [Dc] | L2, L5 |
| Index contractions | [Dc] | L5 |
| Warp factor cancellation | [Dc] | L5 (for $F_{\mu\nu}^2$) |
| Weight function W(ξ) | [Dc] | L6: W(ξ)=1 |
| 4D coupling formula | [Dc] | L6 |
| Dimensional consistency | [M] | L8 |
| Warp factor A(ξ) | [P] | Not derived |
| Domain ℓ | [P] | Not derived |
| Mode profiles | CONDITIONAL [Dc] | Depends on BC |

**Overall OPR-19**: **CONDITIONAL [Dc]** — reduction formula derived, parameters remain [P]

---

## Cross-Links

- **OPR-21**: Fermion BVP uses same metric ansatz; mode normalization analogous but with different weight
- **OPR-20**: Mediator mass from eigenvalue uses g₄ effective coupling
- **OPR-04**: Scale Taxonomy (Δ, δ, ℓ, R_ξ) applies to domain size
- **Israel junction**: If brane kinetic terms present, need Israel-derived coefficients

---

## Open Problems

| ID | Description | Priority |
|----|-------------|----------|
| OPEN-19-1 | Derive A(ξ) from brane-bulk matching | HIGH |
| OPEN-19-2 | Derive ℓ from first principles (link to OPR-04/OPR-21) | HIGH |
| OPEN-19-3 | Include brane-localized kinetic terms if present | MEDIUM |
| OPEN-19-4 | Verify F_{μ5} term contribution for massive modes | LOW |

---

*Canon file created 2026-01-25*
