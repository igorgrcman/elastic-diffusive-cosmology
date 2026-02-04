# Derivation v33 — Detailed Report

## Executive Summary

Derivation v33 establishes the dual-track program for BLOCK-003:
- **Track M**: Matter sector with chirality emergence, Higgs-from-$A_5$ mechanism, and Yukawa overlap integrals.
- **Track R**: RG framework with KK threshold matching and piecewise running.

**NO FORBIDDEN INPUTS** are used anywhere in this derivation.

---

## 1. Inputs Used Table (AC-P40-8 Dependency-Proof)

**CRITICAL**: This table lists EVERY symbol with a numerical value used in v33.
NONE are from the forbidden list.

| Symbol | Value | Units | Source File:Line | Tag |
|--------|-------|-------|------------------|-----|
| pi | 3.14159265... | -- | recompute.py:17 | mathematical |
| L_TEST | 1.0 | arbitrary | recompute.py:20 | [TEST] |
| k_TEST | 1.0 | arbitrary | recompute.py:21 | [TEST] |
| alpha_TEST | 1.0 | dimensionless | recompute.py:22 | [TEST] |
| c_Y | 5/3 | dimensionless | main.tex:eq(cy-value) | [Dc] |
| dim(SU(5)) | 24 | count | main.tex, recompute.py | [D] |
| dim(SO(10)) | 45 | count | main.tex, recompute.py | [D] |
| dim(E_6) | 78 | count | main.tex, recompute.py | [D] |
| dim(PS) | 21 | count | main.tex, recompute.py | [D] |
| dim(SM) | 12 | count | main.tex, recompute.py | [D] |
| N_g | 3 | count | main.tex:eq(sm-betas) | [Dc] |
| N_H | 1 | count | main.tex:eq(sm-betas) | [Dc] |
| b_1 | 41/10 | dimensionless | main.tex:eq(sm-beta-values) | [Dc] |
| b_2 | -19/6 | dimensionless | main.tex:eq(sm-beta-values) | [Dc] |
| b_3 | -7 | dimensionless | main.tex:eq(sm-beta-values) | [Dc] |

**Verification**: NONE of these are {M_Z, M_W, v_EW, l_P, G_N, alpha_EM}.

**AC-P40-8 STATUS: PASS**

---

## 2. Track M: Matter Sector Summary

### M1) Fermion BCs from Variation

The 5D Dirac action variation produces boundary term:
$$\delta S_{\text{boundary}} = -\int d^4x \left[\delta\bar{\Psi}\gamma^5\Psi\right]_0^L$$

**Chiral BC Theorem**: Boundary term vanishes iff $\Psi_L|_{\text{bdry}} = 0$ or $\Psi_R|_{\text{bdry}} = 0$. [D]

### M2) Zero Mode Profiles

For flat background:
$$f_R^{(0)}(\xi) = N_R e^{m_5\xi}, \quad f_L^{(0)}(\xi) = N_L e^{-m_5\xi}$$

Normalization: $N_R = \sqrt{\frac{2m_5}{e^{2m_5 L} - 1}}$ [D]

### M3) Anomaly Risk Matrix

| Type | SU(5) | SO(10) | PS | E_6 | Status |
|------|-------|--------|-----|-----|--------|
| [SU(3)]³ | Safe | Safe | Safe | Safe | [I] |
| [SU(2)]³ | Safe | Safe | Safe | Safe | [I] |
| [U(1)_Y]³ | Depends | Depends | Depends | Depends | [OPEN] |
| Complete | [OPEN] | [OPEN] | [OPEN] | [OPEN] | Requires spectrum |

### M4) Gauge-Higgs Unification

$A_5$ transforms as scalar under Lorentz, with Hosotani mechanism generating effective potential:
$$V_{\text{eff}}(\langle A_5 \rangle) = -\frac{1}{2}\sum_n \text{Tr}\log(p^2 + m_n^2(\langle A_5 \rangle))$$

**Status**: [D] for mechanism, [OPEN] for specific potential shape.

### M5) Yukawa Overlap

$$y_4 = y_5 \cdot I_{\text{overlap}}, \quad I_{\text{overlap}} = \int_0^L d\xi\, f_1(\xi) h(\xi) f_2(\xi)$$

Dimensional check: $[y_4] = M^{-1/2} \cdot M^{1/2} = M^0$ ✓ [D]

### M6) BC Registry v33

| Field Type | Component | BC Type | Zero Mode? |
|------------|-----------|---------|------------|
| Graviton | $h_{\mu\nu}$ | N/N | Yes |
| Gauge (kept) | $A_\mu^a$ | N/N | Yes |
| Gauge (broken) | $A_\mu^{\hat{a}}$ | D/D | No |
| Scalar $A_5$ (kept) | $A_5^{\hat{a}}$ | N/N | Yes (Higgs) |
| Fermion LH (+) | $\Psi_L$ | D/D | No |
| Fermion RH (+) | $\Psi_R$ | N/N | Yes (chiral) |
| Fermion LH (-) | $\Psi_L$ | N/N | Yes (chiral) |
| Fermion RH (-) | $\Psi_R$ | D/D | No |
| Bulk scalar (even) | $\Phi$ | N/N | Yes |
| Bulk scalar (odd) | $\Phi$ | D/D | No |

**AC-P40-6 STATUS: PASS** (10 field entries, ≥6 required)

---

## 3. Track R: RG Framework Summary

### R1) Gauge Matching Formula

$$\frac{1}{g_4^2} = \frac{1}{g_5^2} I_{\text{gauge}} + \Delta_{\text{brane}}$$

where $I_{\text{gauge}} = \int_0^L d\xi\, e^{-2A(\xi)} |f_0(\xi)|^2$. [D]

Flat limit: $g_4^2 = g_5^2/L$ [D]

### R2) KK Scale Definition

$$\mu_{\text{KK}} \equiv m_1 = \frac{\pi}{L}$$

for Neumann/Neumann BCs. [D]

### R3) Piecewise Running

$$\alpha_i^{-1}(\mu) = \begin{cases}
\alpha_i^{-1}(\mu_0) - \frac{b_i}{2\pi}\ln\frac{\mu}{\mu_0} & \mu < \mu_{\text{KK}} \\
\alpha_i^{-1}(\mu_{\text{KK}}) - \frac{b_i + \Delta b_i^{\text{KK}}}{2\pi}\ln\frac{\mu}{\mu_{\text{KK}}} & \mu > \mu_{\text{KK}}
\end{cases}$$

with matching condition at $\mu_{\text{KK}}$. [D]

### R4) Track-to-RG Dictionary

| Property | SU(5) | SO(10) | PS | E_6 |
|----------|-------|--------|-----|-----|
| dim(G_5) | 24 | 45 | 21 | 78 |
| Surviving | 12 | 12 | 12 | 12 |
| c_Y | 5/3 | 5/3 | 5/3 | 5/3 |
| Y formula | Canonical | Canonical | $T_{3R}+(B-L)/2$ | Canonical |

### R5) Reviewer Trap Checklist

| # | Trap | Status |
|---|------|--------|
| 1 | Double counting KK tower | PASS |
| 2 | Scheme dependence | [OPEN] |
| 3 | Hypercharge normalization | PASS |
| 4 | Brane kinetic terms | PASS |
| 5 | Orbifold factor | PASS |
| 6 | Reduced vs unreduced Planck | [OPEN] |
| 7 | Gauge fixing | [OPEN] |
| 8 | Warp exponent | PASS |
| 9 | Threshold order | PASS |
| 10 | KK gap BC dependence | PASS |
| 11 | $A_5$ scalar mass | [OPEN] |
| 12 | Proton decay operators | [OPEN] |
| 13 | Anomaly inflow | [OPEN] |
| 14 | Wilson line periodicity | PASS |
| 15 | Zero mode localization | PASS |
| 16 | Running above μ_UV | [OPEN] |

---

## 4. Python Verification Summary

`recompute.py`: ALL 18 CHECKS PASSED

1. Forbidden token grep gate PASS
2. Fermion BC consistency PASS
3. Flat normalization PASS
4. Exponential normalization PASS
5. Neumann spectrum zero mode PASS
6. Dirichlet no zero mode PASS
7. Wilson line periodicity PASS
8. Gauge matching dimensions PASS
9. Yukawa matching dimensions PASS
10. Hypercharge c_Y = 5/3 PASS
11. Generator counts PASS
12. Beta coefficients PASS
13. KK scale definition PASS
14. Warped localization PASS
15. No private paths PASS
16. SM anomaly cancellation PASS
17. Equation count ≥140 PASS
18. Labeled equations ≥80 PASS

---

## 5. Closure Status

### Structural Closure: ACHIEVED

- Fermion BCs from variation [D]
- Chiral zero modes [D]
- Gauge-Higgs mechanism [D] + [P]
- Yukawa overlap [D]
- Gauge matching [D]
- Piecewise running [D]
- Hypercharge normalization [Dc]

### Open Items: LISTED

- Anomaly cancellation [OPEN]
- Hosotani potential shape [OPEN]
- Unification scale [OPEN]
- Proton decay rates [OPEN]
- 5D strong coupling [OPEN]

---

## 6. Conclusions

1. **Track M**: Chirality emerges from orbifold BCs; $A_5$ provides Higgs mechanism skeleton.
2. **Track R**: RG framework with KK thresholds and piecewise running established.
3. **Dependency-Proof**: No forbidden inputs used anywhere.
4. **Verification**: 18/18 checks pass.

---

*Report generated: 2026-02-03*
