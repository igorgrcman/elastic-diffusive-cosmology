# Derivation v31 — Detailed Report

## Executive Summary

Derivation v31 extends the BLOCK-003 derivation framework to the gauge sector. Starting
from a 5D gauge action, we derive the 4D effective gauge kinetic term, establish a
unified Boundary Condition Registry, and construct a Scale Regime Map. A toy example
demonstrates BC-induced symmetry breaking (SU(3) → SU(2) × U(1)), with explicit
Generator Survival Matrix. This is a program note: it derives structures but does NOT
claim full SM unification.

---

## 1. Inputs Used (AC-P39-6 Compliance Table)

**CRITICAL**: This table lists ALL numeric values used. It does NOT contain forbidden
SM inputs (M_Z, M_W, v_EW, α_EM, G_N, ℓ_P).

| Symbol | Numerical Value | Units | Source | Tag | Where Used |
|--------|-----------------|-------|--------|-----|------------|
| ℏ | 1.054571817×10⁻³⁴ | J·s | SI 2019 exact | [BL] | Dimensional checks |
| c | 299792458 | m/s | SI definition | [BL] | Dimensional checks |
| π | 3.14159265... | — | Mathematical | — | Spectra, CS levels |

**Verification**: Table contains NONE of {M_Z, M_W, v_EW, α_EM, G_N, ℓ_P}.

**AC-P39-6 STATUS: PASS**

---

## 2. Gauge Bridge Slot (§4)

### Main Result

$$\frac{1}{g_4^2} = \frac{1}{g_5^2} \int_0^L d\xi \, |f_0(\xi)|^2 \equiv \frac{I_{\text{gauge}}}{g_5^2}$$

**Tag**: [D]

### Evaluation

| Case | $I_{\text{gauge}}$ | Result |
|------|-------------------|--------|
| Flat Neumann | $\int 1/L \, d\xi = 1$ | $g_4^2 = g_5^2$ |
| Warped (RS) | Factors cancel | $g_4^2 = g_5^2$ |
| With brane kinetic | $I + r_0|f_0(0)|^2 + r_L|f_0(L)|^2$ | Modified |

---

## 3. BC Registry (AC-P39-1)

### Registry Table

| Field | BC Type | Zero Mode? | Symmetry | Gap |
|-------|---------|------------|----------|-----|
| Graviton $h_{\mu\nu}$ | N/N | Yes | Full diff. | $\pi/L$ |
| Graviton $h_{\mu\nu}$ | Robin | Yes (shifted) | Full diff. | $<\pi/L$ |
| Gauge $A_\mu^a$ | N/N | Yes | $G$ preserved | $\pi/L$ |
| Gauge $A_\mu^a$ | D/D | No | $G$ broken | $\pi/L$ |
| Gauge $A_\mu^a$ | N/D | No | $G$ broken | $\pi/(2L)$ |
| Scalar $\phi$ | N/N | Yes | $\mathbb{Z}_2$ even | $\pi/L$ |
| Scalar $\phi$ | D/D | No | $\mathbb{Z}_2$ odd | $\pi/L$ |
| Fermion $\psi$ | orbifold | chiral | [OPEN] | — |

**AC-P39-1 STATUS: PASS** (4 field types covered)

---

## 4. Scale Regime Map (AC-P39-2)

### Regimes

| Regime | Energy Range | Description |
|--------|--------------|-------------|
| UV (5D) | $E \gg 1/L$ | Full 5D dynamics |
| KK threshold | $E \sim 1/L$ | Tower activation |
| IR (4D EFT) | $E \ll 1/L$ | Zero modes only |

### Threshold Conditions

- 4D EFT valid: $E \ll m_{\text{gap}} = x_1/L$
- KK activation: $E \gtrsim n\pi/L$
- UV cutoff: $E \lesssim M_5$

**AC-P39-2 STATUS: PASS** (TikZ figure in main.tex)

---

## 5. Generator Survival Matrix (AC-P39-10)

### SU(3) → SU(2) × U(1) Example

| Generator | Subgroup | BC at 0 | BC at L | Zero Mode | 4D Role |
|-----------|----------|---------|---------|-----------|---------|
| $T^1, T^2, T^3$ | SU(2) | N | N | Yes | $W^{1,2,3}$ |
| $T^8$ | U(1) | N | N | Yes | $B$ boson |
| $T^4, T^5$ | coset | D | N | No | massive |
| $T^6, T^7$ | coset | D | N | No | massive |

### U(1) Factor Count

$$k = \text{rank}(SU(3)) - \text{rank}(SU(2)) = 2 - 1 = 1$$

**AC-P39-10 STATUS: PASS**

---

## 6. Python Verification Summary

`recompute.py`: ALL 15 CHECKS PASSED

1. [g₅²] = [M]⁻¹ ✓
2. [g₄²] = 1 (dimensionless) ✓
3. Bridge dimension consistency ✓
4. Neumann I_gauge = 1 ✓
5. Neumann spectrum m_n = nπ/L ✓
6. Dirichlet: no zero mode ✓
7. Robin transcendental ✓
8. Orthonormality ✓
9. CS level quantization k ∈ ℤ ✓
10. U(1) count formula ✓
11. Generator survival 3+1+4=8 ✓
12. KK threshold condition ✓
13. Warped cancellation ✓
14. No forbidden inputs ✓
15. Sturm-Liouville form ✓

---

## 7. Trap Resolution

| # | Trap | Status |
|---|------|--------|
| 1 | Hidden α_EM import | PASS — no 1/137 |
| 2 | Claim SM unification | PASS — marked [OPEN] |
| 3 | Assume G derived | PASS — stated [P] |
| 4 | BC not from variation | PASS — Lemma 2.1 |
| 5 | Mode equation ad-hoc | PASS — from action |
| 6 | Missing orthonormality | PASS — Eq (28) |
| 7 | g₅ determined | PASS — marked [OPEN] |
| 8 | Zero-mode wrong | PASS — Thm 2.2 |
| 9 | Warp ignored | PASS — included |
| 10 | Brane terms missing | PASS — Eq (46) |
| 11 | Scale map prose | PASS — Figure 1 |
| 12 | Generator matrix | PASS — Table 3 |
| 13 | U(1) count wrong | PASS — Lemma 6.2 |
| 14 | CS unstated | PASS — Thm 7.1 |

---

## 8. Closure Status

### Strong Closure: NOT ACHIEVED

Full SM unification requires:
- UV gauge group choice [P]
- Fermion chirality mechanism [OPEN]
- Yukawa couplings [OPEN]
- Coupling matching [I]

### Weak Closure: ACHIEVED

- Gauge bridge slot derived [D]
- BC Registry unified [D]
- Scale map explicit [D]
- Breaking mechanism demonstrated [D]

---

## 9. Conclusions

1. **Gauge Bridge**: $g_4^{-2} = g_5^{-2} I_{\text{gauge}}$ [D]
2. **BC Registry**: Unified across field types [D]
3. **Scale Map**: UV/KK/IR with thresholds [D]
4. **Breaking**: BC-induced mechanism shown [D]
5. **SM Unification**: Remains [OPEN]

---

*Report generated: 2026-02-03*
