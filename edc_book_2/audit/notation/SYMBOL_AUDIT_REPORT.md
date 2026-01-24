# Symbol Audit Report

Generated: 2026-01-24 19:49

## Summary

| Metric | Count |
|--------|-------|
| Files scanned | 55 |
| Total findings | 81 |
| VIOLATIONS | 61 |
| NEEDS_REVIEW | 20 |
| OK | 0 |

## Violations (z as 5D depth, bad manifold notation)

| File | Line | Token | Classification | Context |
|------|------|-------|----------------|----------|
| 02_frozen_regime_foundations.tex | 133 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\item Paper 2 uses $\Bulk = \mathcal{M}^5$; Book uses ``5D b` |
| 05_three_generations.tex | 334 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\subsection{\texorpdfstring{Candidate Mechanism C: Bulk Topo` |
| 05_three_generations.tex | 339 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `If the 5D bulk manifold $M_5$ has nontrivial fundamental gro` |
| 05_three_generations.tex | 341 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\pi_1(M_5) = \mathbb{Z}_3` |
| 05_three_generations.tex | 369 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `$M_5$ topology specified & No & \textcolor{red!80!black}{\te` |
| 05_three_generations.tex | 370 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `$\pi_1(M_5)$ computed & No & \textcolor{red!80!black}{\textb` |
| 05_three_generations.tex | 378 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `This mechanism requires knowing the global topology of $M_5$` |
| 05_three_generations.tex | 385 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `but EDC currently provides \textbf{no constraint or calculat` |
| 05_three_generations.tex | 402 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `C: $\pi_1(M_5) = \mathbb{Z}_3$ & No \tagP{} & No & \textcolo` |
| 05_three_generations.tex | 501 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\item \textbf{Bulk topology:} Constrain $\pi_1(M_5)$ from ED` |
| 05_three_generations.tex | 605 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `$\pi_1(M_5) = \mathbb{Z}_3$ & \tagP{} & Not computed \\` |
| 06_neutrinos_edge_modes.tex | 70 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `it is $\sim e^{-\Delta z/\kappa^{-1}}$ where $\Delta z$ is t` |
| 06_neutrinos_edge_modes.tex | 71 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `is the penetration depth. With $\Delta z/\kappa^{-1} \approx` |
| 06_neutrinos_edge_modes.tex | 93 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\item Large neutrino mass ($m_\nu > 1$ eV): would require $\` |
| 06_neutrinos_edge_modes.tex | 437 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `where $\Delta z$ is the separation between the neutrino inte` |
| 06_neutrinos_edge_modes.tex | 457 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\frac{m_\nu}{m_e} \approx e^{-2\kappa z_H} = e^{-\Delta z/\k` |
| 06_neutrinos_edge_modes.tex | 458 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\quad \text{with } \Delta z \equiv 2\kappa z_H` |
| 06_neutrinos_edge_modes.tex | 465 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `e^{-\Delta z / \kappa^{-1}} \sim 10^{-6}` |
| 06_neutrinos_edge_modes.tex | 467 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\frac{\Delta z}{\kappa^{-1}} \approx 14` |
| 06_neutrinos_edge_modes.tex | 485 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `$m_\nu/m_e \sim 10^{-6}$ & YELLOW & \tagI{} & Requires $\Del` |
| 06_neutrinos_edge_modes.tex | 530 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `m_{\nu_i} \propto f(n_i) \cdot e^{-\Delta z_i/\kappa^{-1}}` |
| 06_neutrinos_edge_modes.tex | 536 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `and the dependence of $\Delta z$ on mode number are not deri` |
| 06_neutrinos_edge_modes.tex | 701 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `If $\Delta z / \kappa^{-1} \ll 14$, the mass ratio $m_\nu/m_` |
| 06_neutrinos_edge_modes.tex | 757 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Absolute neutrino mass scale & Derive $\kappa^{-1}$ and $\De` |
| 07_ckm_cp.tex | 66 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `If generations are well-separated (distance $\Delta z \gg$ p` |
| 07_ckm_cp.tex | 97 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Single parameter $\Delta z/\kappa \approx 1.5$ produces Wolf` |
| 07_ckm_cp.tex | 102 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Two parameters: $\Delta z_{12}/(2\kappa) = 1.49$, $\Delta z_` |
| 07_ckm_cp.tex | 446 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `$\Delta z$, the CKM matrix is nearly diagonal with small off` |
| 07_ckm_cp.tex | 460 | `z)` | CLASS_VIOLATION_Z_AS_5D | `f_i^{(u)}(z) &= N_u \exp\!\bigl(-\|z - z_i^{(u)}\|/\kappa_u\bi` |
| 07_ckm_cp.tex | 505 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Arrows indicate $\Delta z_{12}$ and $\Delta z_{23}$ separati` |
| 07_ckm_cp.tex | 511 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `($\Delta z \gg \kappa$) produce exponential suppression of o` |
| 07_ckm_cp.tex | 521 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Define the \textbf{inter-generation separation} $\Delta z$ (` |
| 07_ckm_cp.tex | 526 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\|V_{i,i\pm 1}\| &\sim \exp(-\Delta z/2\kappa) \equiv \lambda` |
| 07_ckm_cp.tex | 528 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\|V_{i,i\pm 2}\| &\sim \exp(-2\Delta z/2\kappa) = \lambda^2` |
| 07_ckm_cp.tex | 541 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\frac{\Delta z}{2\kappa} = -\ln\lambda \approx 1.49` |
| 07_ckm_cp.tex | 572 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\item Non-uniform generation spacing: $\Delta z_{12} < \Delt` |
| 07_ckm_cp.tex | 693 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `The uniform-spacing model (Attempt~2) uses a single paramete` |
| 07_ckm_cp.tex | 697 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `$\Delta z_{12} \neq \Delta z_{23}$.` |
| 07_ckm_cp.tex | 705 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\|V_{us}\| &= \exp\bigl(-\Delta z_{12}/(2\kappa)\bigr)` |
| 07_ckm_cp.tex | 706 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\quad\Rightarrow\quad \Delta z_{12}/(2\kappa) = -\ln\|V_{us}\|` |
| 07_ckm_cp.tex | 708 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\|V_{cb}\| &= \exp\bigl(-\Delta z_{23}/(2\kappa)\bigr)` |
| 07_ckm_cp.tex | 709 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\quad\Rightarrow\quad \Delta z_{23}/(2\kappa) = -\ln\|V_{cb}\|` |
| 07_ckm_cp.tex | 724 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\|V_{ub}\|_{\text{pred}} = \exp\Bigl(-\frac{\Delta z_{12} + \D` |
| 07_ckm_cp.tex | 803 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\Delta z/(2\kappa_q) \approx 1.5 \\` |
| 07_ckm_cp.tex | 805 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `\Delta z/(2\kappa_\ell) \approx 0.6` |
| 07_ckm_cp.tex | 808 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `If the inter-generation spacing $\Delta z$ is \emph{universa` |
| 07_ckm_cp.tex | 1012 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Single parameter $\Delta z/\kappa$ produces Wolfenstein hier` |
| 07_ckm_cp.tex | 1015 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Two parameters ($\Delta z_{12}$, $\Delta z_{23}$) calibrated` |
| 07_ckm_cp.tex | 1047 | `\Delta z` | CLASS_VIOLATION_Z_AS_5D | `Wolfenstein hierarchy from $\Delta z/\kappa$ & \textcolor{Ol` |
| 09_va_structure.tex | 275 | `x^\mu, z)` | CLASS_VIOLATION_Z_AS_5D | `\textbf{The setup.} Consider a fermion field $\Psi(x^\mu, z)` |
| 09_va_structure.tex | 276 | `x^\mu, z)` | CLASS_VIOLATION_Z_AS_5D | `The coordinates are $x^M = (x^\mu, z)$ where $\mu = 0,1,2,3$` |
| 11_gf_derivation.tex | 404 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `Combining $G_5 \sim g_5^2/M_5^2$ with $I_4$ \tagP{}:` |
| 11_gf_derivation.tex | 406 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `G_F \sim \frac{g_5^2}{M_5^2} \times I_4` |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 248 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `then $\kappa \sim \sigma/M_5^3$ where $M_5$ is the 5D Planck` |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 259 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `$M_5 \sim 10^{16}$ GeV. This gives:` |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 261 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\kappa \sim \frac{\sigma}{M_5^3} \sim \frac{10^{14}}{10^{48}` |
| ch11_opr20_attemptF_mediator_bvp_junction.tex | 23 | `x^\mu, z)` | CLASS_VIOLATION_Z_AS_5D | `Consider a scalar or gauge mediator $\phi(x^\mu, z)$ propaga` |
| ch14_bvp_closure_pack.tex | 276 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `\frac{M_5^3}{2} R_5 + \mathcal{L}_{\text{bulk matter}}` |
| ch14_bvp_closure_pack.tex | 280 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `where $M_5$ is the 5D Planck mass and $R_5$ is the 5D Ricci ` |
| ch14_bvp_closure_pack.tex | 297 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `[K_{ab}] - g_{ab}[K] = -\frac{1}{M_5^3} S_{ab}` |
| ch14_bvp_closure_pack.tex | 305 | `M5/M_5` | CLASS_VIOLATION_MANIFOLD | `S_{\text{GHY}} = M_5^3 \int_{\partial\mathcal{M}} d^4x \sqrt` |

## Needs Manual Review

| File | Line | Token | Context |
|------|------|-------|----------|
| 06_neutrinos_edge_modes.tex | 434 | `\Delta z` | `\frac{m_\nu}{m_e} \sim \exp\left(-\frac{\Delta z}{\kappa^{-1` |
| 06_neutrinos_edge_modes.tex | 442 | `z)` | `For the electron (interior mode) with profile $f_e(z)$ peake` |
| 07_ckm_cp.tex | 462 | `z)` | `f_j^{(d)}(z) &= N_d \exp\!\bigl(-\|z - z_j^{(d)}\|/\kappa_d\bi` |
| 07_ckm_cp.tex | 471 | `z)` | `of the 5D Dirac boundary value problem. The full derivation ` |
| 07_ckm_cp.tex | 683 | `z)` | `\item Derivation of $f_i(z)$ from 5D Dirac BVP` |
| 09_va_structure.tex | 250 | `z)` | `\item \textbf{Bridge:} The same fermion profiles $f_{L/R}(z)` |
| 09_va_structure.tex | 309 | `,z)` | `\Psi(x,z) = \Psi_L(x,z) + \Psi_R(x,z), \qquad \Psi_{L/R} = P` |
| 09_va_structure.tex | 396 | `z)` | `m(\xi) \sim \kappa \left( T^{zz}(z) - T^{zz}(0) \right)` |
| 09_va_structure.tex | 409 | `z)` | `T^{zz}(z) > T^{zz}(0) \quad \text{for } \xi > 0` |
| 09_va_structure.tex | 520 | `z)` | `f_L^{\text{(toy)}}(z) = \frac{1}{(\pi w_L^2)^{1/4}} \exp\lef` |
| 09_va_structure.tex | 527 | `z)` | `f_R^{\text{(toy)}}(z) = \frac{1}{(\pi w_R^2)^{1/4}} \exp\lef` |
| 09_va_structure.tex | 1079 | `z)` | `\item $[f_{L/R}(z)] = [\text{mass}]^{1/2}$ (profile function` |
| ch11_g5_ell_suppression_attempt2.tex | 270 | `z)` | `\item \textbf{Output:} KK spectrum $\{m_n\}$ and mode profil` |
| ch11_g5_value_closure_attempt2_coefficient.tex | 257 | `z)` | `$S_{\text{brane}} = \int d^4x\, \delta(z) (-\frac{1}{4g_b^2}` |
| ch11_opr20_attemptF_mediator_bvp_junction.tex | 24 | `,z)` | `background. Separating variables $\phi(x,z) = \varphi(x) f(\` |
| ch12_bvp_workpackage.tex | 222 | `z)` | `f_n(z) = \sqrt{\frac{2}{\ell}} \sin\left(\frac{n\pi z}{\ell}` |
| ch14_bvp_closure_pack.tex | 331 | `z)` | `V(\xi) = V_{\text{warp}}(z) + V_{\text{mass}}(z) + V_{\text{` |
| ch14_bvp_closure_pack.tex | 441 | `z)` | `\emph{Status: \tagP{} (toy ansatz).}` |
| ch14_bvp_closure_pack.tex | 529 | `z)` | `\emph{Status: \tagP{} (toy ansatz).}` |
| ch14_bvp_closure_pack.tex | 956 | `z)` | `\item Mode localization profiles $f_{L/R}(z)$` |

## Gate Status

**FAIL**: 61 violations found
