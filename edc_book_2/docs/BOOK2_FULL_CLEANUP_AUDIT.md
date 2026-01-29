# Book 2 Full Cleanup Audit Report

**Generated:** 2026-01-29 18:36
**Files scanned:** 112
**Total issues:** 155

## Issues by Category

| Category | Count | Autofixable |
|----------|-------|-------------|
| 3_DELTA_USAGE | 2 | 0 |
| 4_TAG_HYGIENE | 152 | 0 |
| 8_TYPOGRAPHY | 1 | 0 |

## 3_DELTA_USAGE

**Note:** The delta_from_5d_action files are dedicated derivations for the brane thickness scale.
Using bare δ (without subscript) is appropriate in this context since there's no ambiguity with
CP phase δ. No changes needed.

| File | Line | Subcategory | Snippet | Severity | Autofix |
|------|------|-------------|---------|----------|---------|
| delta_from_5d_action_proton_scale.tex | 0 | delta_derivation_file | `File uses bare δ without δ_nucl subscript` | LOW | NO |
| delta_from_5d_action_proton_scale.include.tex | 0 | delta_derivation_file | `File uses bare δ without δ_nucl subscript` | LOW | NO |

**Manual Review Result:** Acceptable - dedicated derivation file, no δ ambiguity.

## 4_TAG_HYGIENE

| File | Line | Subcategory | Snippet | Severity | Autofix |
|------|------|-------------|---------|----------|---------|
| ch11_gf_full_closure_plan.tex | 292 | literal_Dc_tag | `OPR-22: \textbf{YELLOW} [Dc]+[OPEN] --- Closure sp` | LOW | NO |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 37 | literal_Dc_tag | `\textbf{Status:} OPR-20 remains \textbf{RED-C [Dc]` | LOW | NO |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 520 | literal_Dc_tag | `\textbf{Final status:} OPR-20 remains \textbf{RED-` | LOW | NO |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 522 | literal_Dc_tag | `\item \textbf{[Dc]:} BC route negative closure con` | LOW | NO |
| ch11_opr20_attemptD_interpretation_robin_overcount.tex | 565 | literal_Dc_tag | `RED-C [Dc]+[OPEN].` | LOW | NO |
| ch7_z2_parity_origin.tex | 171 | literal_Dc_tag | `\textbf{Established [Dc]:}` | LOW | NO |
| ch7_z2_parity_origin.tex | 179 | literal_P_tag | `\textbf{Proposed [P]:}` | LOW | NO |
| ch7_z2_parity_origin.tex | 189 | literal_Dc_tag | `\textbf{OPR-11} $(\bar\rho, \bar\eta)$ derivation:` | LOW | NO |
| ch11_g5_ell_value_closure_attempt.tex | 80 | literal_Dc_tag | `\textbf{Would be [Dc] if:} We could derive $M_W$ f` | LOW | NO |
| ch11_g5_ell_value_closure_attempt.tex | 130 | literal_Dc_tag | `\textbf{Would be [Dc] if:} $f_{\text{geom}}$ were ` | LOW | NO |
| ch11_g5_ell_value_closure_attempt.tex | 194 | literal_Dc_tag | `\textbf{Would be [Dc] if:} The $4\pi$ factor were ` | LOW | NO |
| ch11_g5_ell_suppression_attempt2.tex | 132 | literal_Dc_tag | `\textbf{What would upgrade to [Dc]:}` | LOW | NO |
| ch11_g5_ell_suppression_attempt2.tex | 217 | literal_Dc_tag | `\textbf{What would upgrade to [Dc]:}` | LOW | NO |
| ch10_electroweak_bridge.tex | 260 | literal_Dc_tag | `\item Arrow $\alpha \to x_1$: ``[Dc] Sturm--Liouvi` | LOW | NO |
| ch10_electroweak_bridge.tex | 261 | literal_P_tag | `\item Box around $\delta = R_\xi$: ``Identificatio` | LOW | NO |
| ch10_electroweak_bridge.tex | 311 | literal_Dc_tag | `\textbf{Status:} \textcolor{YellowOrange}{\textbf{` | LOW | NO |
| ch10_electroweak_bridge.tex | 311 | literal_P_tag | `\textbf{Status:} \textcolor{YellowOrange}{\textbf{` | LOW | NO |
| ch10_electroweak_bridge.tex | 363 | literal_Dc_tag | `\item This would upgrade OPR-20b from [P] to [Dc].` | LOW | NO |
| ch10_electroweak_bridge.tex | 363 | literal_P_tag | `\item This would upgrade OPR-20b from [P] to [Dc].` | LOW | NO |
| ch10_electroweak_bridge.tex | 366 | literal_Dc_tag | `\textbf{Status:} \textcolor{BrickRed}{\textbf{RED-` | LOW | NO |
| ch10_electroweak_bridge.tex | 366 | literal_P_tag | `\textbf{Status:} \textcolor{BrickRed}{\textbf{RED-` | LOW | NO |
| ch10_electroweak_bridge.tex | 402 | literal_Dc_tag | `Steps 2--4 are derivable [Dc] once $\delta$ is kno` | LOW | NO |
| ch10_electroweak_bridge.tex | 410 | literal_P_tag | `\item Marking: ``OPR-20b [P]+[OPEN]''` | LOW | NO |
| ch10_electroweak_bridge.tex | 446 | literal_P_tag | `$\delta$, but this is a postulate [P]. Deriving $\` | LOW | NO |
| ch10_electroweak_bridge.tex | 481 | literal_Dc_tag | `\item OPR-20 closure: Path to upgrade [P] $\to$ [D` | LOW | NO |
| ch10_electroweak_bridge.tex | 481 | literal_P_tag | `\item OPR-20 closure: Path to upgrade [P] $\to$ [D` | LOW | NO |
| ch10_electroweak_bridge.tex | 492 | literal_Dc_tag | `\item OPR-20a: \textcolor{YellowOrange}{\textbf{YE` | LOW | NO |
| ch10_electroweak_bridge.tex | 492 | literal_P_tag | `\item OPR-20a: \textcolor{YellowOrange}{\textbf{YE` | LOW | NO |
| ch10_electroweak_bridge.tex | 493 | literal_Dc_tag | `\item OPR-20b: \textcolor{BrickRed}{\textbf{RED-C}` | LOW | NO |
| ch10_electroweak_bridge.tex | 493 | literal_P_tag | `\item OPR-20b: \textcolor{BrickRed}{\textbf{RED-C}` | LOW | NO |
| main.tex | 475 | literal_P_tag | `\textit{Provisional candidate formulas for charged` | LOW | NO |
| 05b_neutron_dual_route.tex | 93 | literal_P_tag | `$\Delta m_{np} c^2 \approx 1.3\,\mathrm{MeV}$ [P].` | LOW | NO |
| 05b_neutron_dual_route.tex | 94 | literal_P_tag | `This is a physical argument [P] based on scale sep` | LOW | NO |
| 05b_neutron_dual_route.tex | 98 | literal_Der_tag | `\begin{edcLemmaBox}{Energy Functional in Thin-Stri` | LOW | NO |
| 05b_neutron_dual_route.tex | 108 | literal_Der_tag | `\textbf{Derived [Der]:} The dominant contribution ` | LOW | NO |
| 05b_neutron_dual_route.tex | 111 | literal_P_tag | `\textbf{Assumed [P]:} The specific shape of $V(q)$` | LOW | NO |
| 05b_neutron_dual_route.tex | 116 | literal_Dc_tag | `\begin{edcPropositionBox}{Neutron as Metastable Lo` | LOW | NO |
| 05b_neutron_dual_route.tex | 127 | literal_Dc_tag | `\textbf{Status:} [Dc] conditional on the existence` | LOW | NO |
| 05b_neutron_dual_route.tex | 128 | literal_P_tag | `is currently [P] (postulated based on physical rea` | LOW | NO |
| 05b_neutron_dual_route.tex | 156 | literal_Dc_tag | `A0 & Proton is local minimum at $q=0$ & [Dc] & Cor` | LOW | NO |
| 05b_neutron_dual_route.tex | 157 | literal_P_tag | `A1 & Topological sector preserved & [M]+[P] & Lemm` | LOW | NO |
| 05b_neutron_dual_route.tex | 158 | literal_Der_tag | `A2 & $E[q] = E_0 + V(q)$ structure & [Der]+[P] & L` | LOW | NO |
| 05b_neutron_dual_route.tex | 158 | literal_P_tag | `A2 & $E[q] = E_0 + V(q)$ structure & [Der]+[P] & L` | LOW | NO |
| 05b_neutron_dual_route.tex | 159 | literal_Dc_tag | `A3 & Neutron is metastable at $q_n > 0$ & [Dc]+[P]` | LOW | NO |
| 05b_neutron_dual_route.tex | 159 | literal_P_tag | `A3 & Neutron is metastable at $q_n > 0$ & [Dc]+[P]` | LOW | NO |
| 05b_neutron_dual_route.tex | 161 | literal_P_tag | `--- & Specific $V(q)$ shape & [P] & Not derived \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 162 | literal_P_tag | `--- & Barrier height $V_B$ & [P]/[Cal] & \S\ref{su` | LOW | NO |
| 05b_neutron_dual_route.tex | 162 | literal_Cal_tag | `--- & Barrier height $V_B$ & [P]/[Cal] & \S\ref{su` | LOW | NO |
| 05b_neutron_dual_route.tex | 163 | literal_Der_tag | `--- & BC do not create barrier & [Der] & aside\_fr` | LOW | NO |
| 05b_neutron_dual_route.tex | 183 | literal_Cal_tag | `Current numbers are calibrated [Cal] to reproduce ` | LOW | NO |
| 05b_neutron_dual_route.tex | 184 | literal_Der_tag | `not derived [Der] from first principles.` | LOW | NO |
| 05b_neutron_dual_route.tex | 197 | literal_P_tag | `\begin{edcLemmaBox}{Effective Action Ansatz}{[P]+[` | LOW | NO |
| 05b_neutron_dual_route.tex | 207 | literal_P_tag | `\item $M(q)$ is an effective mass (currently [P]--` | LOW | NO |
| 05b_neutron_dual_route.tex | 211 | literal_Dc_tag | `\textbf{Physical motivation [Dc]:} This form follo` | LOW | NO |
| 05b_neutron_dual_route.tex | 214 | literal_P_tag | `\textbf{Not derived [P]:} The specific functions $` | LOW | NO |
| 05b_neutron_dual_route.tex | 259 | literal_Der_tag | `\item \textbf{Derive $V_B$ from first principles:}` | LOW | NO |
| 05b_neutron_dual_route.tex | 259 | literal_Cal_tag | `\item \textbf{Derive $V_B$ from first principles:}` | LOW | NO |
| 05b_neutron_dual_route.tex | 289 | literal_Dc_tag | `B1 & Effective action form & [P]+[Dc] & Lemma~\ref` | LOW | NO |
| 05b_neutron_dual_route.tex | 289 | literal_P_tag | `B1 & Effective action form & [P]+[Dc] & Lemma~\ref` | LOW | NO |
| 05b_neutron_dual_route.tex | 291 | literal_Cal_tag | `B3 & $V_B \approx 2.6$ MeV reproduces $\tau_n$ & [` | LOW | NO |
| 05b_neutron_dual_route.tex | 333 | literal_P_tag | `Key assumption & Barrier exists [P] & $V_B$, $M(q)` | LOW | NO |
| 05b_neutron_dual_route.tex | 333 | literal_Cal_tag | `Key assumption & Barrier exists [P] & $V_B$, $M(q)` | LOW | NO |
| 05b_neutron_dual_route.tex | 335 | literal_Dc_tag | `5D-derived? & Partially [Dc] & Not yet (OPEN) \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 347 | literal_Dc_tag | `\item Neutron is a metastable Y-junction configura` | LOW | NO |
| 05b_neutron_dual_route.tex | 347 | literal_P_tag | `\item Neutron is a metastable Y-junction configura` | LOW | NO |
| 05b_neutron_dual_route.tex | 348 | literal_Dc_tag | `\item Decay is relaxation toward proton anchor ($q` | LOW | NO |
| 05b_neutron_dual_route.tex | 349 | literal_Cal_tag | `\item Effective 1D WKB model reproduces $\tau_n \a` | LOW | NO |
| 05b_neutron_dual_route.tex | 363 | literal_Der_tag | `\textbf{Path forward:} Derive $S_{\mathrm{eff}}[q]` | LOW | NO |
| 05b_neutron_dual_route.tex | 363 | literal_Cal_tag | `\textbf{Path forward:} Derive $S_{\mathrm{eff}}[q]` | LOW | NO |
| 05b_neutron_dual_route.tex | 374 | literal_P_tag | `Neutron in same topo sector as proton & [M]+[P] & ` | LOW | NO |
| 05b_neutron_dual_route.tex | 375 | literal_Dc_tag | `Neutron has $E > E_{\mathrm{proton}}$ & [Dc] & A \` | LOW | NO |
| 05b_neutron_dual_route.tex | 376 | literal_Dc_tag | `Metastable local minimum exists & [Dc]+[P] & A \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 376 | literal_P_tag | `Metastable local minimum exists & [Dc]+[P] & A \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 377 | literal_Dc_tag | `Decay via barrier penetration & [Dc] & A+B \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 378 | literal_Cal_tag | `$\tau_n \approx 879$ s reproduced & [Cal] & B \\` | LOW | NO |
| 05b_neutron_dual_route.tex | 380 | literal_Der_tag | `BC do not generate attraction & [Der] & A (audit) ` | LOW | NO |
| Z6_content_full.tex | 1854 | literal_Dc_tag | `\node[box, fill=purple!20] (hex) at (2.5,-3) {[Dc]` | LOW | NO |
| Z6_content_full.tex | 1857 | literal_Dc_tag | `\node[box, fill=purple!20] (z6) at (2.5,-4.5) {[Dc` | LOW | NO |
| Z6_content_full.tex | 1860 | literal_Dc_tag | `\node[box, fill=purple!20] (equal) at (0,-6) {[Dc]` | LOW | NO |
| Z6_content_full.tex | 1861 | literal_Dc_tag | `\node[box, fill=purple!20] (z3) at (5,-6) {[Dc] $\` | LOW | NO |
| Z6_content_full.tex | 1864 | literal_Dc_tag | `\node[box, fill=purple!20] (steiner) at (0,-7.5) {` | LOW | NO |
| Z6_content_full.tex | 1865 | literal_Dc_tag | `\node[box, fill=purple!20] (vortex) at (5,-7.5) {[` | LOW | NO |
| Z6_content_full.tex | 1868 | literal_Dc_tag | `\node[box, fill=green!20] (proton) at (-2,-9) {[Dc` | LOW | NO |
| Z6_content_full.tex | 1869 | literal_Dc_tag | `\node[box, fill=red!20] (neutron) at (2,-9) {[Dc] ` | LOW | NO |
| Z6_content_full.tex | 1870 | literal_Dc_tag | `\node[box, fill=blue!20] (confine) at (6,-9) {[Dc]` | LOW | NO |
| Z6_content_full.tex | 1915 | literal_P_tag | `Hexagonal crystallization on brane & \tagDc{} & Fr` | LOW | NO |
| Z6_content_full.tex | 2022 | literal_Dc_tag | `Proton stability & $\mathbb{Z}_3$ fixed point [Dc]` | LOW | NO |
| Z6_content_full.tex | 2022 | literal_P_tag | `Proton stability & $\mathbb{Z}_3$ fixed point [Dc]` | LOW | NO |
| Z6_content_full.tex | 2023 | literal_Dc_tag | `Neutron decay & Dislocation annihilation [Dc] & Pi` | LOW | NO |
| Z6_content_full.tex | 2023 | literal_P_tag | `Neutron decay & Dislocation annihilation [Dc] & Pi` | LOW | NO |
| Z6_content_full.tex | 2024 | literal_Dc_tag | `Color confinement & $\mathbb{Z}_3$ topology [Dc] &` | LOW | NO |
| Z6_content_full.tex | 2025 | literal_P_tag | `Muon/tau decay & --- & $\mathcal{P}_{\mathrm{froze` | LOW | NO |
| Z6_content_full.tex | 2026 | literal_P_tag | `Pion decay & --- & Helicity suppression [P] (open)` | LOW | NO |
| Z6_content_full.tex | 2027 | literal_P_tag | `V$-$A structure & $\mathbb{Z}_2 \subset \mathbb{Z}` | LOW | NO |
| Z6_content_full.tex | 2045 | literal_P_tag | `Postulates [P] & 5 \\` | LOW | NO |
| Z6_content_full.tex | 2046 | literal_Dc_tag | `Derived consequences [Dc] & 15 \\` | LOW | NO |
| Z6_content_full.tex | 2047 | literal_I_tag | `Identifications/calibrations [I] & 5 \\` | LOW | NO |
| ch11_opr20_attemptE_prefactor8_derivation.tex | 51 | literal_Dc_tag | `\item \textbf{Standard BC route [Dc] (negative):} ` | LOW | NO |
| ch11_opr20_attemptE_prefactor8_derivation.tex | 55 | literal_Dc_tag | `\item \textbf{Overcounting audit [Dc]:} The Z$_2$ ` | LOW | NO |
| ch11_opr20_attemptE_prefactor8_derivation.tex | 59 | literal_Dc_tag | `\item \textbf{Robin BC parameters [Dc]+[P]:} The R` | LOW | NO |

*... and 52 more*

## 8_TYPOGRAPHY

| File | Line | Subcategory | Snippet | Severity | Autofix |
|------|------|-------------|---------|----------|---------|
| zn_toy_functional_from_5d_action.include.tex | 298 | double_space_in_prose | `u(θ) = u_0 + a_1 cos(Nθ),  a_1 ∝ 1/N` | LOW | NO |