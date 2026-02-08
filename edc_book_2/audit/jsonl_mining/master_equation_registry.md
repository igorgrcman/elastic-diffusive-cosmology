# Master Equation Registry

**Generated:** 2026-01-31
**Sources:** 22826edd, 73d92ff5, 98cc5184, 5251e090, ce8dadbd sessions

---

## Summary Statistics

| Source | Equations | Focus Area |
|--------|-----------|------------|
| 22826edd | 519 | PRIMARY BOOK 2 (weak sector, BVP, G_F) |
| 73d92ff5 | 37,256 | Theory maturity, gap analysis |
| 98cc5184 | ~100 | Paper 3 Framework (neutron lifetime) |
| 5251e090 | 0 | F_bulk derivation (narrative focus) |
| ce8dadbd | 0 | Gravity derivation (narrative focus) |

---

## Core Physics Equations (Deduplicated)

### Mixing Angle / Weak Sector

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-001 | mixing_angle | Weinberg angle from Z6 | `\sin^2\theta_W = 1/4` | 22826edd | 1553 |
| EQ-CORE-002 | mixing_angle | Coupling ratio | `g'^2/g^2 = \|\mathbb{Z}_2\|/\|\mathbb{Z}_6\| = 1/3` | 22826edd | 1623 |
| EQ-CORE-003 | mixing_angle | Full sin2thetaW derivation | `\sin^2\theta_W = g'^2/(g^2+g'^2) = 1/4` | 22826edd | 1623 |
| EQ-CORE-004 | mixing_angle | Boxed result | `\boxed{\sin^2\theta_W = \frac{1}{4}}` from Z6=Z2xZ3 | 22826edd | 13866 |
| EQ-CORE-005 | mixing_angle | Experimental value | `\sin^2\theta_W(M_Z) = 0.2314` | 22826edd | 22571 |

### Scale Parameters

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-010 | scale | Weak-sector length scale | `R_\xi = \hbar c / M_Z \approx 2.2 \times 10^{-3}` fm | 22826edd | 1770 |
| EQ-CORE-011 | scale | delta identification | `\delta = R_\xi` | 22826edd | 1968 |
| EQ-CORE-012 | scale | Kink width | `\Delta = 2/(v\sqrt{\lambda})` | 22826edd | 15944 |
| EQ-CORE-013 | scale | Dimensionless parameter | `\mu := M_0\,\ell` | 22826edd | 14674 |
| EQ-CORE-014 | scale | n-ratio | `n \equiv \ell/\Delta` | 22826edd | 15944 |

### BVP / Generation Counting

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-020 | bvp | Generation definition | `N_{gen} := N_{bound}(V, BC, threshold)` | 22826edd | 3439 |
| EQ-CORE-021 | bvp | Target | `N_{\text{bound}} = 3` | 22826edd | 3509 |
| EQ-CORE-022 | bvp | Closure chain | `\text{derive } V(z) \& \text{BCs} \Rightarrow \text{solve BVP} \Rightarrow N_{\text{bound}} \stackrel{?}{=} 3` | 22826edd | 3850 |
| EQ-CORE-023 | bvp | mu-window | `\mu \in [25,35)` for N_bound=3 | 22826edd | 15944 |
| EQ-CORE-024 | bvp | V-A suppression | `R_{\mathrm{LR}} \sim \exp(-C\,\mu)` | 22826edd | 4122 |
| EQ-CORE-025 | bvp | mu bound | `\mu > \frac{1}{C}\ln(10^3)` with C=O(1) | 22826edd | 4401 |

### Mode Profiles / Localization

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-030 | mass | Zero mode profile | `\psi_L \propto \exp\left(-\int_0^\xi m(\xi')\,d\xi'\right)` | 22826edd | 7658 |
| EQ-CORE-031 | bvp | Schrodinger form | `[-\partial_\xi^2 + V(\xi)]f = m^2 f` | 22826edd | 6501 |
| EQ-CORE-032 | bvp | Potential forms | `V_L = (M+2A')^2 - (M+2A')'` | 22826edd | 14674 |
| EQ-CORE-033 | bvp | Robin BC | `f'(0) + \kappa f(0)=0` with `\kappa=m_b/2` | 22826edd | 14674 |
| EQ-CORE-034 | bvp | Chirality gap | `V_R(\xi)-V_L(\xi) = 2(M(\xi)+2A'(\xi))'` | 22826edd | 14674 |

### Fermi Constant / Coupling

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-040 | fermi | Overlap integral | `I_4 = \int_0^\ell d\xi \, \|f_L(\xi)\|^4` | 22826edd | 6501 |
| EQ-CORE-041 | fermi | G_F standard | `G_F = g^2/(4\sqrt{2}M_W^2) = 1/(\sqrt{2}v^2)` | 22826edd | 14063 |
| EQ-CORE-042 | coupling | Effective coupling | `C_{\text{eff}} = g_5^2 \ell / x_1^2` | 22826edd | 16959 |
| EQ-CORE-043 | coupling | 4D from 5D | `1/g_4^2 = (1/g_5^2)\int d\xi\,W(\xi)\,\|f(\xi)\|^2` | 22826edd | 16508 |
| EQ-CORE-044 | coupling | G_eff definition | `G_{\mathrm{eff}} := g_{4,1}^2/(2m_1^2)` | 22826edd | 18212 |
| EQ-CORE-045 | coupling | G_eff formula | `G_{\text{eff}} = g_5^2 \ell \|f_1(0)\|^2/(2x_1^2)` | 22826edd | 17417 |

### Mass Parameters

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-050 | mass | M0 definition | `M_0^2 = \frac{3y^2}{4}\,\sigma\Delta` | 22826edd | 15944 |
| EQ-CORE-051 | mass | x_n definition | `x_n := m_n \cdot \ell` (dimensionless eigenvalue) | 22826edd | 16948 |
| EQ-CORE-052 | mass_hierarchy | Kink profile | `\phi = v\tanh(\xi/\Delta)` | 22826edd | 16235 |
| EQ-CORE-053 | mass | Neutrino suppression | `m_\nu/m_e \sim e^{-\Delta z/\kappa^{-1}}` | 22826edd | 1430 |

### Neutron Lifetime (WKB/Tunneling)

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-060 | lifetime | Effective Lagrangian | `L_{\rm eff}(q, \dot{q}) = \frac{1}{2}M(q)\dot{q}^2 - V(q)` | 98cc5184 | - |
| EQ-CORE-061 | lifetime | Bounce action | `B = 2 \int_{q_{tp}^{(p)}}^{q_{tp}^{(n)}} dq \sqrt{2 M(q) [V(q) - E_n]}` | 98cc5184 | - |
| EQ-CORE-062 | lifetime | Quartic barrier | `V(q) = 16V_B q^2(1-q)^2 + Q \cdot q` | 98cc5184 | - |
| EQ-CORE-063 | lifetime | V_B calibration | `V_B \approx 2.6` MeV [Cal from tau_n] | 22826edd | 14182 |
| EQ-CORE-064 | lifetime | tau_n result | `\tau_n \approx 879` s | 22826edd | 26109 |
| EQ-CORE-065 | lifetime | Prefactor | `A_0 = \frac{\omega_{\rm well}}{2\pi} \cdot R_{\rm det} \cdot C_{\rm zero}` | 98cc5184 | - |
| EQ-CORE-066 | lifetime | Well frequency | `\omega_{\rm well} = \sqrt{V''(q_n) / M(q_n)}` | 98cc5184 | - |

### 5D Action / Brane

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-070 | 5D | Bulk action | `S_{\rm bulk} = \frac{1}{2\kappa_5^2} \int d^5X \sqrt{-g^{(5)}} (R^{(5)} - 2\Lambda_5)` | 73d92ff5 | - |
| EQ-CORE-071 | 5D | GHY term | `S_{\rm GHY} = \frac{1}{\kappa_5^2} \int d^4x \sqrt{-h}\, K` | 73d92ff5 | - |
| EQ-CORE-072 | 5D | Brane action | `S_{\rm brane} = -\sigma \int d^4x \sqrt{-h}` | 73d92ff5 | - |
| EQ-CORE-073 | 5D | Warped metric | `ds^2 = e^{2A(\xi)}\eta_{\mu\nu}dx^\mu dx^\nu + d\xi^2` | 22826edd | 14674 |
| EQ-CORE-074 | 5D | Mode decomposition | `\phi(x^\mu, \xi) = \sum_n \phi_n(x^\mu) f_n(\xi)` | 22826edd | 6765 |

### Gravity (F_bulk derivation)

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-080 | gravity | Newtonian flow | `v(r) = \sqrt{2GM/r}` | 5251e090 | 42 |
| EQ-CORE-081 | gravity | Core radius | `r_{core} = GM/c^2 = r_s/2` | 5251e090 | 46 |
| EQ-CORE-082 | gravity | G formula (I) | `G = c^4 R_\xi^{12} / (128\pi^2 \sigma r_e^{13})` | ce8dadbd | 72 |
| EQ-CORE-083 | gravity | F_bulk formula | `F_{bulk} = c^4 R_\xi^{12} / (32\pi r_e^{13})` | ce8dadbd | 26 |
| EQ-CORE-084 | gravity | Hierarchy ratio | `(R_\xi/r_e)^{12} \approx 4.1 \times 10^{-38}` | ce8dadbd | 72 |

### Topological / String Sector

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-CORE-090 | topological | String energy | `E_i = \tau L_i + \text{subleading}` | 22826edd | 25533 |
| EQ-CORE-091 | topological | Steiner junction | `\hat{t}_1+\hat{t}_2+\hat{t}_3=0` at 120 degrees | 22826edd | 25533 |
| EQ-CORE-092 | symmetry | Z6 decomposition | `\mathbb{Z}_6 = \mathbb{Z}_2 \times \mathbb{Z}_3` | 22826edd | 1268 |
| EQ-CORE-093 | topological | q_n fraction | `q_n \approx 1/3` from Z6 symmetry [I] | 22826edd | 14182 |

### Mathematical Identities

| eq_id | topic | short meaning | LaTeX | source | line |
|-------|-------|---------------|-------|--------|------|
| EQ-MATH-001 | identity | Golden ratio | `\varphi = (1+\sqrt{5})/2 \approx 1.618` | 98cc5184 | - |
| EQ-MATH-002 | identity | Homotopy groups | `\pi_1(S^1) = \mathbb{Z}`, `\pi_2(S^2) = \mathbb{Z}` | 73d92ff5 | - |
| EQ-MATH-003 | identity | Gaussian integrals | `\int_0^\infty r^2 e^{-r^2/w^2} dr = \frac{\sqrt{\pi}}{4}w^3` | 73d92ff5 | - |
| EQ-MATH-004 | identity | Mass ratio | `6\pi^5 = 1836.12... \approx m_p/m_e` | 73d92ff5 | 7611 |
| EQ-MATH-005 | identity | Fine structure candidate | `\alpha = (4\pi + 5/6)/(6\pi^5) = 1/137.027` | 22826edd | 22571 |

---

## Epistemic Status Legend

| Tag | Meaning | Color |
|-----|---------|-------|
| [M] | Mathematical identity | Purple |
| [BL] | Baseline (empirical input) | Blue |
| [Der] | Derived step-by-step | Green |
| [Dc] | Derived conditional on ansatz | Teal |
| [I] | Identified pattern (not derived) | Orange |
| [P] | Postulated | Red |
| [Cal] | Calibrated to data | Yellow |
| [OPEN] | Not yet derived | Red |

---

## Notes

1. **Deduplication**: Equations appearing in multiple sessions are consolidated under a single CORE ID
2. **Line numbers**: Refer to extracted report lines, not original source files
3. **73d92ff5 session**: Contains 37,256 equations but most are duplicates across iterations
4. **5251e090 and ce8dadbd**: These sessions focus on gravity derivation with narrative, few formal equations extracted

---

*Total unique core equations: ~95*
*Total raw equations across all sources: ~38,000 (mostly duplicates)*
