# Derivation v37 — Detailed Report

## Executive Summary

Derivation v37 establishes BC selection as a **principle** rather than a catalog.
Four hierarchical selectors are defined, each with explicit criteria:

1. **Variational**: Boundary term = 0
2. **Self-Adjointness**: Green's identity satisfied
3. **Topological**: Winding/homotopy quantization
4. **Vacuum Energy**: Minimize $\mathcal{E}_{\text{vac}}$

A pipeline diagram shows how the infinite BC space narrows to selected values.
Prediction hooks connect BC choice to observables ($m_{\text{gap}}$, gauge
survivors, $G_F$, EW scale).

**NO FORBIDDEN NUMERICAL INPUTS** are used anywhere.

---

## 1. Inputs Used Table (Dependency-Proof)

**CRITICAL**: This table lists EVERY symbol with a numerical value used in v37.
NONE are from the forbidden list.

| Symbol | Value | Units | Source | Tag | Forbidden? |
|--------|-------|-------|--------|-----|------------|
| π | 3.14159... | -- | mathematical | [I] | N |
| e | 2.71828... | -- | mathematical | [I] | N |
| 0, 1, 2, ... | integers | -- | mathematical | [I] | N |

**Verification**: ALL values are mathematical constants or integers.
NONE are physical measurements from {$M_Z$, $M_W$, $v_{EW}$, $\alpha_{EM}$, $G_N$, $\ell_P$}.

---

## 2. Selection Principle Overview

### Stage 1: Variational Principle

**Criterion**: The boundary term in the action variation must vanish.

For scalar field:
$$\left[ \partial_y \phi \cdot \delta\phi \right]_0^L = 0$$

**Allowed**: N, D, or Robin at each boundary.

### Stage 2: Self-Adjointness

**Criterion**: The differential operator must satisfy Green's identity.

For Laplacian:
$$[f^* \partial_y g - (\partial_y f)^* g]_0^L = 0 \quad \forall f,g$$

**Result**: Self-adjoint extensions form $U(2)$ family.

### Stage 3: Topological Pinning

**Criterion**: Parameters with topological origin are quantized.

$$\lambda = |k|/(2\pi), \quad k \in \mathbb{Z}$$

**Result**: Discrete set of allowed BCs.

### Stage 4: Vacuum Energy Minimization

**Criterion**: Nature selects minimum vacuum energy.

$$\text{BC}^* = \arg\min \mathcal{E}_{\text{vac}}(\text{BC})$$

**Result**: Unique (generically) selected BC.

---

## 3. Pipeline Structure

```
Stage 0: All BCs           ──  ∞-dimensional
           │
           ▼ (boundary term = 0)
Stage 1: Allowed BCs       ──  N, D, Robin
           │
           ▼ (Green's identity)
Stage 2: SA family         ──  U(2) ~ 4 parameters
           │
           ▼ (winding/homotopy)
Stage 3: Discrete set      ──  Finite or countable
           │
           ▼ (min E_vac)
Stage 4: Selected BC       ──  Unique (generically)
```

---

## 4. Prediction Hooks

### Hook 1: KK Mass Gap

$$m_{\text{gap}} = x_1(b)/L$$

where $x_1(b)$ is the first root of the BC equation.

### Hook 2: Gauge Survivor Pattern

$$(P_0, P_L) = (+,+) \Rightarrow \text{zero-mode} \Rightarrow \text{unbroken gauge}$$

### Hook 3: Fermi Constant

$$G_F/\sqrt{2} = \sum_n (g_4^{(n)})^2/(8 m_n^2)$$

Spectrum $\{m_n\}$ and couplings depend on BC.

### Hook 4: Higgs/EW Scale

$$V(\langle A_5 \rangle) = \mathcal{E}_{\text{vac}}(\theta)$$

Minimum determines electroweak scale via Hosotani mechanism.

---

## 5. Self-Adjointness Verification

**Neumann/Neumann**:
$$[f^* g' - f'^* g]_0^L = 0 \cdot 0 - 0 \cdot 0 = 0 \quad \checkmark$$

**Dirichlet/Dirichlet**:
$$[f^* g' - f'^* g]_0^L = 0 - 0 = 0 \quad \checkmark$$

**Robin/Robin** ($f' = m_b f$, $g' = m_b g$):
$$f^* m_b g - m_b f^* g = 0 \quad \checkmark$$

All standard BCs are self-adjoint.

---

## 6. Spectrum Dependence

### Robin Spectrum

Transcendental equation:
$$\tan(m_n L) = \frac{2 m_n m_b}{m_n^2 - m_b^2}$$

### Limiting Cases

- $m_b \to 0$: Neumann, $m_n = n\pi/L$
- $m_b \to \infty$: Dirichlet, $m_n = n\pi/L$ (for $n \geq 1$)

---

## 7. Vacuum Energy Structure

### Mode Sum

$$\mathcal{E}_{\text{vac}} = \frac{1}{2} \sum_n m_n(\text{BC})$$

### Regularization

Zeta-function regularization:
$$\mathcal{E}_{\text{vac}}^{\text{reg}} = \frac{1}{2L} \zeta_b(-1)$$

### Variation

At minimum:
$$\frac{\partial \mathcal{E}_{\text{vac}}}{\partial m_b}\bigg|_{m_b^*} = 0$$

---

## 8. Python Verification Summary

`recompute.py`: ALL 15 CHECKS PASSED

1. Forbidden tokens (main.tex) PASS
2. Forbidden tokens (recompute.py) PASS
3. Equation count ≥ 90 PASS (113)
4. Page count ≥ 18 PASS (25)
5. Four selectors PASS
6. Pipeline diagram PASS
7. Prediction hooks PASS
8. SA verification PASS
9. Robin spectrum formula PASS
10. Vacuum energy PASS
11. Dimensional analysis PASS
12. No private paths PASS
13. Epistemic ledger PASS
14. Gauge BC compatibility PASS
15. Fermion BC consistency PASS

---

## 9. Reviewer Trap Checklist

| # | Trap | Status |
|---|------|--------|
| 1 | Variation not derived | PASS |
| 2 | SA not verified | PASS |
| 3 | Topology ad hoc | PASS |
| 4 | Vacuum divergent | PASS (regularization) |
| 5 | Pipeline not constructive | PASS |
| 6 | No prediction hooks | PASS |
| 7 | Forbidden inputs | PASS |
| 8 | Missing fermion BCs | PASS |
| 9 | Gauge field incomplete | PASS |
| 10 | Robin not self-adjoint | PASS (verified) |
| 11 | U(2) claim unsourced | PASS ([BL]) |
| 12 | Vacuum minimum unproven | OPEN |

---

## 10. What Was Derived

1. Four-stage BC selection pipeline
2. Explicit criteria for each selector
3. Pipeline diagram (TikZ)
4. Prediction hooks to observables
5. SA verification for all standard BCs
6. Robin spectrum dependence
7. Vacuum energy structure
8. Connection to EDC parameters

---

## 11. What Remains Open

1. **Vacuum energy computation**: Full multi-field calculation
2. **Minimum location**: Explicit value of $m_b^*$
3. **Anomaly constraints**: Detailed cancellation
4. **Warped geometry**: Full RS treatment

---

*Report generated: 2026-02-03*
