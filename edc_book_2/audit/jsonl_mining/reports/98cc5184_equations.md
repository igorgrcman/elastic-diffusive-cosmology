# Paper 3 Framework Session - Equation Catalog

**Source:** `98cc5184-b172-4833-9b17-b923ac34b0c1.jsonl`
**Extraction Date:** 2026-01-31

---

## 1. Effective Lagrangian Mechanics

### 1.1 Core Effective Lagrangian
```latex
L_{\rm eff}(q, \dot{q}) = \frac{1}{2}M(q)\dot{q}^2 - V(q)
```
**Status:** [Dc] - Derived from 5D action via Israel junction conditions

### 1.2 Supermetric (Configuration Space Metric)
```latex
M(q) = \sigma \int d^3\sigma \, a^2(f) \sqrt{1 + a^{-2}|\nabla f|^2} \left( \frac{\partial f}{\partial q} \right)^2
```
**Status:** [Der] - Direct derivation from brane kinetic term

### 1.3 Explicit Supermetric Form
```latex
M(q) = M_0 (1-2q)^2
```
**Status:** [Dc] - From Gaussian profile ansatz

### 1.4 Quartic Barrier Potential
```latex
V(q) = V_B \cdot q^2(1-q)^2
```
**Status:** [Dc] - From Euler-Lagrange minimization (not postulated)

### 1.5 Full Potential with Q-value
```latex
V(q) = 16V_B q^2(1-q)^2 + Q \cdot q
```
Where $Q = 0.782$ MeV [BL]

---

## 2. WKB Tunneling Formulas

### 2.1 Decay Rate
```latex
\Gamma = A_0 \exp(-B/\hbar)
```

### 2.2 Euclidean Bounce Action
```latex
B = 2 \int_{q_{\rm tp}^{(p)}}^{q_{\rm tp}^{(n)}} dq \sqrt{2 M(q) [V(q) - E_n]}
```
**Status:** [Der] - Standard WKB formula

### 2.3 Prefactor Decomposition
```latex
A_0 = \frac{\omega_{\rm well}}{2\pi} \cdot R_{\rm det} \cdot C_{\rm zero}
```

### 2.4 Well Frequency
```latex
\omega_{\rm well} = \sqrt{V''(q_n) / M(q_n)}
```

### 2.5 Zero-Mode Factor
```latex
C_{\rm zero} = \sqrt{B/(2\pi\hbar)}
```

### 2.6 Golden Ratio from Asymptotic ODE
```latex
\varphi = \frac{1+\sqrt{5}}{2} \approx 1.618
```
**Status:** [Dc] - Geometric consequence of 5D localization

---

## 3. 5D Geometry

### 3.1 Bulk Metric Ansatz
```latex
ds^2_5 = e^{-2|y|/\ell}\eta_{\mu\nu}dx^\mu dx^\nu + dy^2
```
**Status:** [P] - Postulated (AdS_5-like)

### 3.2 Brane Embedding
```latex
X^A(\sigma; q) = (\sigma^\mu, f(r;q))
```
**Status:** [P]

### 3.3 Gaussian Profile Ansatz
```latex
f(r;q) = A(q) e^{-r^2/2w^2}
```
With $A(q) = A_{\rm max} q(1-q)$ [P]

### 3.4 Dimensional Reduction Chain
```latex
S_{\rm 5D} \xrightarrow{\text{embedding}} S[\phi(x;q)] \xrightarrow{\text{collective coord}} S_{\rm eff}[q]
```

---

## 4. Energy Conservation

### 4.1 5D Closure
```latex
\nabla_A T^{AB}_{(5)} = 0
```

### 4.2 Brane Open Subsystem
```latex
\nabla_\mu T^{\mu\nu}_{\mathrm{brane}} = -J^\nu_{\mathrm{bulk}\to\mathrm{brane}}
```

### 4.3 Sign Convention
$J^\nu > 0$ means inflow (bulk to brane)

---

## 5. Conservation Laws (Selection Rules)

### 5.1 Charge Conservation
```latex
Q_n = Q_p + Q_e + Q_{\text{neutral}}
0 = +1 + (-1) + 0
```

### 5.2 Winding Conservation
```latex
W_n = W_p + \sum W_i
+1 = +1 + 0
```

### 5.3 Fifth Momentum Budget
```latex
p^\xi_n = p^\xi_p + \sum p^\xi_i + \Delta p^\xi_{\text{Plenum}}
```

### 5.4 Winding-Charge Correspondence
```latex
Q = W = \frac{1}{2\pi}\oint A_\phi d\phi
```

---

## 6. Symmetry Structure

### 6.1 Layered Symmetry
```latex
\text{Symmetry} = \text{Diff}(\mathcal{M}^4) \oplus \text{Isom}(S^1_\xi)
```

### 6.2 Mode Raising Operator
```latex
\mathcal{E}_n: n_0 \to n_0 + n
```

### 6.3 Sector Shift Operator
```latex
\mathcal{R}: s \to s+1 \pmod 6
```

---

## 7. PMNS Matrix Construction

### 7.1 Rotation Matrices
```latex
U_{\rm PMNS} = R_{23}(\theta_{23}^0) \cdot R_{13}(\epsilon) \cdot R_{12}(\theta_{12}^0)
```

### 7.2 Atmospheric Angle (Z_6 geometry)
```latex
\sin^2\theta_{23} = 0.564
```
**Status:** [Dc]

### 7.3 Reactor Perturbation
```latex
\epsilon = \lambda/\sqrt{2} \approx 0.159 \text{ rad}
```
**Status:** [BL->Dc] (uses $\lambda$ [BL])

### 7.4 Solar Angle (Geometric)
```latex
\theta_{12} = \arctan(1/\sqrt{2}) = 35.26^\circ
```
**Status:** [Dc]

---

## 8. CKM Matrix

### 8.1 Phase Cancellation Theorem
Pure Z_3 gives $J = 0$ identically
**Status:** [Dc]

### 8.2 Sign-Flip Rule
Odd number of flips gives $\delta = 60^\circ$
**Status:** [Dc]

### 8.3 Jarlskog Invariant
```latex
J = 2.9 \times 10^{-5}
```
(PDG: $3.08 \times 10^{-5}$, 6% error)

---

## 9. Fermi Constant Chain

### 9.1 G_F Formula
```latex
G_F = \frac{g_5^2 \ell^2 I_4}{x_1^2}
```
**Status:** [Dc] (spine established)

### 9.2 4D Coupling from Membrane
```latex
g^2 = \frac{4\pi \sigma r_e^3}{\hbar c} \approx 0.37
```
**Status:** [Dc]+[P] (6% from SM)

### 9.3 Suppression Factor
```latex
f_{\text{geom}} = \frac{R_\xi}{r_e} \sim 10^{-3}
```
**Status:** [P]

### 9.4 Combined Geometric Factor
```latex
2\pi\sqrt{2} \approx 8.89
```
Gives $m_\phi \approx 70$ GeV
**Status:** [Dc]+[P]

---

## 10. Dislocation Model

### 10.1 Total Energy
```latex
E_{\text{total}} = E_{\text{disl}} + E_{\text{pinning}}(r)
```

### 10.2 Mass Difference Scaling
```latex
\Delta m(n-p) \propto Gb^2L
```
**Status:** [OPEN]

### 10.3 Decay Energy
```latex
E_{\text{disl}} = 1.293 \text{ MeV} = E(e^-) + E(\bar{\nu}_e) + E_{\text{recoil}}
```

---

## 11. Thick-Brane Interaction

### 11.1 Interaction Lagrangian
```latex
\mathcal{L}_{\mathrm{int}} = g\,q(t)\,\phi(-\delta/2,t)
```
**Status:** [P]

### 11.2 Switch Criterion (Working Hypothesis)
```latex
|\phi(+\delta/2, t)| > \phi_{\mathrm{crit}}
```
**Status:** [P]/[OPEN]

---

## 12. Numerical Constants

| Constant | Value | Status |
|----------|-------|--------|
| $\hat{B}$ | $0.720 \pm 0.001$ | [Dc] |
| $R_{\rm det}$ | $0.63 \pm 0.10$ | [Dc] |
| $\varphi$ | $1.618...$ | [M] |
| $\tau_n$ | $878.4 \pm 0.5$ s | [BL] |
| $Q$ (n-p) | 0.782 MeV | [BL] |
| $g^2$ | 0.37 | [Dc]+[P] |

---

## 13. Status Legend

| Tag | Meaning | Can upgrade to |
|-----|---------|----------------|
| [M] | Mathematical identity | - |
| [BL] | Baseline (empirical) | - |
| [Der] | Derived step-by-step | - |
| [Dc] | Derived conditional | [Der] with ansatz derivation |
| [I] | Identified pattern | [Dc] with mechanism |
| [P] | Postulated | [Dc] with derivation |
| [Cal] | Calibrated | [Dc] with first-principles |
| [OPEN] | Not yet derived | any |

---

*Equation catalog from Paper 3 Framework session*
