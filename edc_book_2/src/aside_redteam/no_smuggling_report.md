# No-Smuggling Scan Report

**Adversarial Premise:** Any untagged SM/PDG value is potential smuggling.

- Files scanned: 88
- Total risky tokens: 361
- Properly tagged: 115
- **SUSPICIOUS (untagged): 246**

## SUSPICIOUS INSTANCES

These require immediate review:

### CH3_electroweak_parameters.tex

- **Line 106**: `Z boson mass`
  - Pattern: `91\.2|91\.19`
  - Context: `Combined with standard RG running to $M_Z = 91.2$ GeV~\cite{PDG2024}, this yield...`

- **Line 106**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Combined with standard RG running to $M_Z = 91.2$ GeV~\cite{PDG2024}, this yield...`

- **Line 108**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\item Weinberg angle $\sin^2\theta_W(M_Z) = 0.2314$ (\textbf{0.08\%} from experi...`

- **Line 109**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item Weak coupling $g^2(M_Z) = 0.4246$ (\textbf{1.1\%} from experiment)...`

- **Line 111**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `\item Fermi constant $G_F = 1.166 \times 10^{-5}$ GeV$^{-2}$ (\textbf{exact})...`

- **Line 132**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W$ (Weinberg) & 0.231 & (open) \\...`

- **Line 181**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `g^2 = \frac{4\pi}{127.9 \times 0.2314} = \frac{12.566}{29.59} = 0.4246...`

- **Line 181**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `g^2 = \frac{4\pi}{127.9 \times 0.2314} = \frac{12.566}{29.59} = 0.4246...`

- **Line 239**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\textbf{Comparison:} Experimental value at $M_Z$: $\sin^2\theta_W = 0.231$ (8\% ...`

- **Line 392**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\item Final output: $\sin^2\theta_W(M_Z) = 0.2314$...`

- **Line 429**: `Z boson mass`
  - Pattern: `91\.2|91\.19`
  - Context: `Therefore at $M_Z = 91.2$ GeV:...`

- **Line 431**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\boxed{\sin^2\theta_W(M_Z) = 0.250 - 0.0186 = 0.2314}...`

- **Line 576**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\boxed{M_W = \frac{0.6516 \times 246.2}{2} = 80.2 \text{ GeV}}...`

- **Line 583**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `G_F = \frac{g^2}{4\sqrt{2} M_W^2} = \frac{0.4246}{4\sqrt{2} \times (80.2)^2} = 1...`

- **Line 583**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `G_F = \frac{g^2}{4\sqrt{2} M_W^2} = \frac{0.4246}{4\sqrt{2} \times (80.2)^2} = 1...`

- **Line 911**: `Z boson mass`
  - Pattern: `91\.2|91\.19`
  - Context: `not at the experimental scale $M_Z = 91.2$ GeV....`

- **Line 989**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\sin^2\theta_W(M_Z) &= 0.2314 \quad \text{(EDC + RG)} \\...`

- **Line 990**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\sin^2\theta_W^{\text{exp}} &= 0.2312 \quad \text{(experiment)}...`

- **Line 1033**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W$ & $\frac{1}{4}$ + RG & 0.2314 & 0.2312 & \textbf{0.08\%} & \che...`

- **Line 1081**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W(M_Z)$ & 0.2314 & 0.2312 & Consistency (RG) \\...`

- **Line 1082**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$g^2(M_Z)$ & 0.4246 & 0.42 & Follows from $\alpha$, $\sin^2\theta_W$ \\...`

- **Line 1083**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `$M_W$ & 80.2 GeV & 80.4 GeV & Follows from $g$, $v$ \\...`

- **Line 1084**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `$G_F$ & $1.166 \times 10^{-5}$ & $1.166 \times 10^{-5}$ & Self-consistent (exact...`

- **Line 1160**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\emph{Current status:} $m_\gamma < 10^{-18}$ eV (PDG limit)....`

### CH4_lepton_mass_candidates.tex

- **Line 44**: `fine structure constant`
  - Pattern: `137\.03|137\.036`
  - Context: `m_e^{(\mathrm{EDC})} = \pi \times \sqrt{\frac{1}{137.036} \times 5.86 \times 3.1...`

- **Line 90**: `fine structure constant`
  - Pattern: `137\.03|137\.036`
  - Context: `= \frac{3}{2} \times 137.036 = 205.55...`

- **Line 191**: `electron mass`
  - Pattern: `0\.511`
  - Context: `$m_e$ & $\pi\sqrt{\alpha\sigma\Delta\hbar c}$ & 0.508 MeV & 0.511 MeV & [P] \\...`

- **Line 194**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `$m_\tau$ & Koide($m_e, m_\mu$) & 1763 MeV & 1776.9 MeV & [P], not indep. \\...`

### EDC_Part_II_Weak_Sector_rebuild.tex

- **Line 689**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W(M_Z)$ & 0.2312 (input) & 0.2314 (predicted, 0.08\% error) \\...`

- **Line 754**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W$ (Weinberg angle) & 0.2314 & 0.2312 & \textbf{0.08\%} \\...`

- **Line 755**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$g^2$ (weak coupling) & 0.4246 & 0.42 & \textbf{1.1\%} \\...`

- **Line 756**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `$M_W$ (W boson mass) & 80.2 GeV & 80.4 GeV & \textbf{0.2\%} \\...`

- **Line 757**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `$G_F$ (Fermi constant) & $1.166 \times 10^{-5}$ & $1.166 \times 10^{-5}$ & \text...`

### Z6_content_full.tex

- **Line 938**: `proton mass`
  - Pattern: `938\.3|938\.27`
  - Context: `M_{\text{eff}} = m_p = 938.3 \text{ MeV}/c^2...`

- **Line 1337**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\textbf{Comparison:} Experimental value $\sin^2\theta_W = 0.231$ at $M_Z$ scale,...`

- **Line 1647**: `electron mass`
  - Pattern: `0\.511`
  - Context: `1 & Electron ($e$) & 0.511 & 1 \\...`

- **Line 1648**: `muon mass`
  - Pattern: `105\.7`
  - Context: `2 & Muon ($\mu$) & 105.7 & 207 \\...`

- **Line 1649**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `3 & Tau ($\tau$) & 1777 & 3477 \\...`

- **Line 1735**: `electron mass`
  - Pattern: `0\.511`
  - Context: `= \frac{0.511 + 105.7 + 1777}{(0.715 + 10.28 + 42.16)^2} = \frac{1883.2}{2827.0}...`

- **Line 1735**: `muon mass`
  - Pattern: `105\.7`
  - Context: `= \frac{0.511 + 105.7 + 1777}{(0.715 + 10.28 + 42.16)^2} = \frac{1883.2}{2827.0}...`

- **Line 1735**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `= \frac{0.511 + 105.7 + 1777}{(0.715 + 10.28 + 42.16)^2} = \frac{1883.2}{2827.0}...`

- **Line 1978**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `within 8\% of experimental value 0.231...`

### figures/fig_master_weak_pipeline.tex

- **Line 82**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `Neutron: $Q = 0.78$ MeV $\Rightarrow$ $e$ only\\...`

### main.tex

- **Line 689**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W(M_Z)$ & 0.2312 (input) & 0.2314 (predicted, 0.08\% error) \\...`

- **Line 754**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W$ (Weinberg angle) & 0.2314 & 0.2312 & \textbf{0.08\%} \\...`

- **Line 755**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$g^2$ (weak coupling) & 0.4246 & 0.42 & \textbf{1.1\%} \\...`

- **Line 756**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `$M_W$ (W boson mass) & 80.2 GeV & 80.4 GeV & \textbf{0.2\%} \\...`

- **Line 757**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `$G_F$ (Fermi constant) & $1.166 \times 10^{-5}$ & $1.166 \times 10^{-5}$ & \text...`

### meta_part2/01_claim_ledger.tex

- **Line 20**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `$\sin^2\theta_W(M_Z) = 0.2314$ after RG running (0.08\% from PDG)%...`

- **Line 20**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\sin^2\theta_W(M_Z) = 0.2314$ after RG running (0.08\% from PDG)%...`

- **Line 24**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$g^2 = 4\pi\alpha/\sin^2\theta_W = 0.4246$ (1.1\% from PDG)%...`

- **Line 24**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$g^2 = 4\pi\alpha/\sin^2\theta_W = 0.4246$ (1.1\% from PDG)%...`

### meta_part2/04_evidence_map.tex

- **Line 68**: `PDG reference`
  - Pattern: `PDG`
  - Context: `PDG 2024 & CKM matrix values, $\sin^2\theta_W(M_Z)$, $G_F$, $M_W$ \\...`

- **Line 69**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `CODATA 2018 & $\alpha$, $\hbar$, $c$ \\...`

### sections/02_frozen_regime_foundations.tex

- **Line 42**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `\item \textbf{Mass ratio:} $m_p/m_e = 6\pi^5 = 1836.118...$ with 0.0018\% error ...`

- **Line 42**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `\item \textbf{Mass ratio:} $m_p/m_e = 6\pi^5 = 1836.118...$ with 0.0018\% error ...`

- **Line 726**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `\textbf{3D shadow:} Mass ratio $m_p/m_e = 6\pi^5 = 1836.118...$...`

- **Line 757**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `\frac{m_p}{m_e} = \frac{E_p}{E_e} = \frac{\text{Area}(S^3)^3}{\text{Vol}(B^3)} =...`

- **Line 793**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `$\text{Area}(S^3)^3 / \text{Vol}(B^3)$ & $1836.1181087117$ & --- \\...`

- **Line 794**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `$6\pi^5$ & $1836.1181087117$ & $2.3 \times 10^{-13}$ (numerical) \\...`

- **Line 795**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `CODATA $m_p/m_e$ & $1836.15267343$ & $\pm 0.00000011$ \\...`

- **Line 795**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `CODATA $m_p/m_e$ & $1836.15267343$ & $\pm 0.00000011$ \\...`

- **Line 797**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `\textbf{EDC vs CODATA} & & \textbf{0.0018\%} \\...`

- **Line 840**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `\text{M8} = 6\pi^5 = 1836.118109......`

- **Line 860**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `&= \frac{12.566370... + 0.833333...}{1836.118109...} \\...`

- **Line 861**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `&= \frac{13.399704...}{1836.118109...} \\...`

- **Line 885**: `fine structure constant`
  - Pattern: `137\.03|137\.036`
  - Context: `CODATA 2022 & $\alpha = 0.00729735...$ & $137.036$ \\...`

- **Line 885**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `CODATA 2022 & $\alpha = 0.00729735...$ & $137.036$ \\...`

- **Line 922**: `fine structure constant`
  - Pattern: `137\.03|137\.036`
  - Context: `$\alpha$ prediction & --- & 0.0067\% error & $1/137.036$ & Frozen \\...`

### sections/04a_unified_master_figure.tex

- **Line 26**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `$m_\mu \approx 106$ MeV $\gg Q_n \approx 0.78$ MeV).}...`

- **Line 58**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `Neutron $n \to p + \cdots$ & $Q_n \approx 0.782$ MeV &...`

- **Line 62**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `Tau $\tau \to \cdots$ & $m_\tau c^2 \approx 1777$ MeV &...`

- **Line 75**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `Q_n = (m_n - m_p - m_e)c^2 \approx 0.782~\text{MeV},...`

- **Line 80**: `muon mass`
  - Pattern: `105\.7`
  - Context: `Because $m_\mu c^2 \approx 105.7$ MeV $\gg Q_n$, a neutron \emph{cannot} produce...`

### sections/05_case_neutron.tex

- **Line 523**: `electron mass`
  - Pattern: `0\.511`
  - Context: `Q_\beta(e) \approx 1.293 - 0.511 = 0.782~\text{MeV} > 0....`

- **Line 523**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `Q_\beta(e) \approx 1.293 - 0.511 = 0.782~\text{MeV} > 0....`

- **Line 531**: `muon mass`
  - Pattern: `105\.7`
  - Context: `Q_\beta(\mu) \approx 1.293 - 105.7 \approx -104.4~\text{MeV} < 0,...`

- **Line 556**: `muon mass`
  - Pattern: `105\.7`
  - Context: `$m_p + m_\mu + m_\nu \approx 938.3 + 105.7 + 0 = 1044$ MeV....`

- **Line 556**: `proton mass`
  - Pattern: `938\.3|938\.27`
  - Context: `$m_p + m_\mu + m_\nu \approx 938.3 + 105.7 + 0 = 1044$ MeV....`

- **Line 557**: `neutron mass`
  - Pattern: `939\.6|939\.57`
  - Context: `\item \textbf{Comparison}: But $m_n c^2 \approx 939.6$ MeV $<$ 1044 MeV....`

### sections/06_case_muon.tex

- **Line 22**: `muon mass`
  - Pattern: `105\.7`
  - Context: `Energy: $m_\mu c^2 = 105.7$ MeV available\\...`

### sections/06_neutrinos_edge_modes.tex

- **Line 217**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Observable} & \textbf{Value (PDG 2024)} & \textbf{Puzzle} \\...`

### sections/07_case_tau.tex

- **Line 15**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `Energy: $m_\tau c^2 = 1777$ MeV (heaviest lepton)...`

### sections/07_ckm_cp.tex

- **Line 78**: `PDG reference`
  - Pattern: `PDG`
  - Context: `(5° from PDG 65°) \tagDc{}....`

- **Line 103**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Predicts $|V_{ub}| \approx 0.0094$ (vs.\ PDG $0.0037$): factor 2.5 overshoot....`

- **Line 116**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Resolution: $\mathbb{Z}_2$ sign selection produces $\delta = 60°$ (5° from PDG 6...`

- **Line 195**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\label{eq:ch7_ckm_pdg}...`

- **Line 216**: `PDG reference`
  - Pattern: `PDG`
  - Context: `then compare to PDG data to quantify the required breaking....`

- **Line 304**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\subsection{Comparison with PDG Data}...`

- **Line 550**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Overlap type} & \textbf{Predicted scaling} & \textbf{Numerical} & \textb...`

- **Line 562**: `PDG reference`
  - Pattern: `PDG`
  - Context: `PDG shows $|V_{cb}| \approx 0.04 \sim \lambda^2$. This indicates that the...`

- **Line 712**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\paragraph{Comparison with PDG:}...`

- **Line 714**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\frac{|V_{ub}|_{\text{pred}}}{|V_{ub}|_{\text{PDG}}}...`

- **Line 726**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item PDG shows $|V_{ub}| \approx 0.0037$, which is $\approx 0.4 \times$ the pro...`

- **Line 830**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$|V_{ub}| \approx 0.0094$, while PDG gives $0.0037$. This section analyzes...`

- **Line 862**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$|V_{ub}|$ (PDG) & $0.0094$ & $0.0037$ & $\times 2.5$ \\...`

- **Line 976**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[\ding{51}] $\mathbb{Z}_2$ sign selection produces $\delta = 60°$ (5° from ...`

- **Line 999**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Predicts $|V_{ub}| \approx 0.0094$, overshoots PDG by factor 2.5....`

- **Line 1005**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Jarlskog $J = 2.9 \times 10^{-5}$ predicted (PDG: $3.1 \times 10^{-5}$), 6\% agr...`

### sections/09_case_electron.tex

- **Line 200**: `electron mass`
  - Pattern: `0\.511`
  - Context: `\item $e^-$ channel: $m_e = 0.511$ MeV $< Q_\beta$ \checkmark\ (allowed)...`

- **Line 201**: `muon mass`
  - Pattern: `105\.7`
  - Context: `\item $\mu^-$ channel: $m_\mu = 105.7$ MeV $\gg Q_\beta$ \texttimes\...`

- **Line 203**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `\item $\tau^-$ channel: $m_\tau = 1777$ MeV $\gg Q_\beta$ \texttimes\...`

- **Line 223**: `electron mass`
  - Pattern: `0\.511`
  - Context: `$e^-$ & 0.511 MeV & $+0.782$ MeV & Allowed \\...`

- **Line 223**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `$e^-$ & 0.511 MeV & $+0.782$ MeV & Allowed \\...`

- **Line 224**: `muon mass`
  - Pattern: `105\.7`
  - Context: `$\mu^-$ & 105.7 MeV & $-104.4$ MeV & Kinematically forbidden \\...`

- **Line 225**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `$\tau^-$ & 1777 MeV & $-1776$ MeV & Kinematically forbidden \\...`

- **Line 460**: `neutron mass`
  - Pattern: `939\.6|939\.57`
  - Context: `$n$ (input) & $939.57$ MeV & 0 & 0 & 0 & \\...`

- **Line 462**: `proton mass`
  - Pattern: `938\.3|938\.27`
  - Context: `$p$ (output) & $938.27$ MeV & $p_p$ & $+1$ & 0 & \\...`

- **Line 507**: `electron mass`
  - Pattern: `0\.511`
  - Context: `Origin of $m_e = 0.511$ MeV & Mode spectrum derivation from brane geometry...`

### sections/09_va_structure.tex

- **Line 639**: `PDG reference`
  - Pattern: `PDG`
  - Context: `bounded~\cite{PDG2024}:...`

### sections/11_gf_derivation.tex

- **Line 123**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `The Higgs VEV $v = (\sqrt{2}G_F)^{-1/2} = 246.2$ GeV is experimentally...`

- **Line 177**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `where $g \approx 0.65$ is the $SU(2)_L$ gauge coupling and $M_W \approx 80.4$ Ge...`

- **Line 181**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `That requires the Higgs mechanism with a VEV $v \approx 246$ GeV. The hierarchy...`

- **Line 282**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\sin^2\theta_W(M_Z) &= 0.2314 \quad \text{(0.08\% from PDG)} \\...`

- **Line 282**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\sin^2\theta_W(M_Z) &= 0.2314 \quad \text{(0.08\% from PDG)} \\...`

- **Line 283**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `g^2 &= \frac{4\pi\alpha}{\sin^2\theta_W} = 0.4246 \\...`

- **Line 284**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `M_W &= \frac{gv}{2} = \frac{0.6516 \times 246.2}{2} = 80.2 \text{ GeV}...`

- **Line 290**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `G_F = \frac{g^2}{4\sqrt{2}M_W^2} = \frac{0.4246}{4\sqrt{2}(80.2)^2}...`

- **Line 291**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `= 1.166 \times 10^{-5} \text{ GeV}^{-2}...`

- **Line 319**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `After RG running, this gives $\sin^2\theta_W(M_Z) = 0.2314$, which agrees with...`

- **Line 320**: `PDG reference`
  - Pattern: `PDG`
  - Context: `PDG at 0.08\%. \textbf{This} is the non-trivial, falsifiable prediction....`

- **Line 550**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `\item[\ding{51}] $\sin^2\theta_W(M_Z) = 0.2314$ (0.08\% from PDG) \tagDer{}...`

- **Line 550**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[\ding{51}] $\sin^2\theta_W(M_Z) = 0.2314$ (0.08\% from PDG) \tagDer{}...`

- **Line 620**: `sin^2(theta_W) at M_Z`
  - Pattern: `0\.231|0\.2312`
  - Context: `After standard RG running, this gives $\sin^2\theta_W(M_Z) = 0.2314$, agreeing...`

- **Line 621**: `PDG reference`
  - Pattern: `PDG`
  - Context: `with PDG at \textbf{0.08\%}. This is a non-trivial, falsifiable prediction....`

- **Line 626**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `\item $G_F = 1.166 \times 10^{-5}$ GeV$^{-2}$ from electroweak relations,...`

### sections/12_epistemic_map.tex

- **Line 42**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Z$_2$ selection yields $\delta\simeq60^\circ$ \textbf{YELLOW [Dc]+[I]} (5° from ...`

- **Line 67**: `neutron-proton mass diff (MeV)`
  - Pattern: `0\.782|0\.78`
  - Context: `$+0.782$ MeV & $\mathcal{P}_{\text{energy}}$ & OPEN \\...`

- **Line 77**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `$+1776/1671$ MeV & $\mathcal{P}_{\text{energy}}$ & OPEN \\...`

- **Line 112**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `Tau & $1776.9$ & $0.290$ ps & Brane-dominant &...`

- **Line 116**: `electron mass`
  - Pattern: `0\.511`
  - Context: `Electron & $0.511$ & $> 10^{28}$ yr & Brane defect (ground) &...`

- **Line 180**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Neutron mass & $m_n = 939.565$ MeV & PDG \\...`

- **Line 181**: `proton mass`
  - Pattern: `938\.3|938\.27`
  - Context: `Proton mass & $m_p = 938.272$ MeV & PDG \\...`

- **Line 181**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Proton mass & $m_p = 938.272$ MeV & PDG \\...`

- **Line 182**: `electron mass`
  - Pattern: `0\.511`
  - Context: `Electron mass & $m_e = 0.511$ MeV & PDG \\...`

- **Line 182**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Electron mass & $m_e = 0.511$ MeV & PDG \\...`

- **Line 183**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Muon mass & $m_\mu = 105.66$ MeV & PDG \\...`

- **Line 184**: `tau mass`
  - Pattern: `1776|1777`
  - Context: `Tau mass & $m_\tau = 1776.9$ MeV & PDG \\...`

- **Line 184**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Tau mass & $m_\tau = 1776.9$ MeV & PDG \\...`

- **Line 185**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Pion mass & $m_{\pi^\pm} = 139.57$ MeV & PDG \\...`

- **Line 197**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Neutron & $\tau_n \approx 880$ s & PDG \\...`

- **Line 198**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Muon & $\tau_\mu \approx 2.2 \times 10^{-6}$ s & PDG \\...`

- **Line 199**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Tau & $\tau_\tau \approx 2.9 \times 10^{-13}$ s & PDG \\...`

- **Line 200**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Pion & $\tau_\pi \approx 2.6 \times 10^{-8}$ s & PDG \\...`

- **Line 201**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Electron & $> 10^{28}$ years & PDG (limit) \\...`

- **Line 231**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `Fermi constant & $G_F = 1.166 \times 10^{-5}~\text{GeV}^{-2}$ & PDG \\...`

- **Line 231**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Fermi constant & $G_F = 1.166 \times 10^{-5}~\text{GeV}^{-2}$ & PDG \\...`

- **Line 232**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `$W$ boson mass & $M_W = 80.4$ GeV & PDG \\...`

- **Line 232**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$W$ boson mass & $M_W = 80.4$ GeV & PDG \\...`

- **Line 233**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `Fine structure const. & $\alpha \approx 1/137$ & CODATA \\...`

- **Line 424**: `PDG reference`
  - Pattern: `PDG`
  - Context: `OPR-05b & PMNS $\theta_{13}$/$\varepsilon$ & \textcolor{YellowOrange}{\textbf{YE...`

- **Line 427**: `PDG reference`
  - Pattern: `PDG`
  - Context: `OPR-12 & CP phase $\delta$ & \textcolor{YellowOrange}{\textbf{YELLOW}} [Dc]+[I] ...`

- **Line 440**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item \textcolor{YellowOrange}{\textbf{Partial:}} $\delta = 60°$ (5° from PDG) v...`

- **Line 486**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item \emph{Status:} Attempt~4 + Z$_2$ parity origin completed; $\delta = 60°$ (...`

- **Line 494**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item \emph{Status:} Attempts~2--4.2 completed; all three angles now have geomet...`

- **Line 498**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item \emph{Result (Attempt~4.1):} $\varepsilon = \lambda/\sqrt{2}$ predicts $\s...`

- **Line 499**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item \emph{Result (Attempt~4.2):} $\theta_{12} = \arctan(1/\sqrt{2}) = 35.26°$ ...`

- **Line 504**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{PMNS closure:} OPR-05a GREEN ($\theta_{23}$ from $\mathbb{Z}_6$, 3\%), O...`

### sections/ch11_g5_ell_suppression_attempt2.tex

- **Line 64**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item $v = 246$ GeV (defined via $G_F$)...`

### sections/ch11_g5_ell_value_closure_attempt.tex

- **Line 25**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item Use $M_W$, $G_F$, or $v = 246$ GeV to fix parameters (forbidden)...`

### sections/ch11_g5_value_closure_attempt2_coefficient.tex

- **Line 65**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item[\ding{55}] Importing $M_W$, $G_F$, or $v = 246$ GeV...`

### sections/ch11_gf_full_closure_plan.tex

- **Line 135**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item \textbf{Using $v = 246$ GeV:} The Higgs VEV is defined via $G_F$:...`

- **Line 151**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Comparison to PDG values \emph{after} prediction (evaluation, not fitting)...`

- **Line 190**: `PDG reference`
  - Pattern: `PDG`
  - Context: `RG-run value matches PDG at 0.08\%. Falsifiable. &...`

- **Line 236**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `G_F^{\text{PDG}} = 1.1664 \times 10^{-5} \text{ GeV}^{-2}...`

- **Line 236**: `PDG reference`
  - Pattern: `PDG`
  - Context: `G_F^{\text{PDG}} = 1.1664 \times 10^{-5} \text{ GeV}^{-2}...`

- **Line 330**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\square$ & Compare to PDG & — & Check $G_F$ prediction \\...`

### sections/ch11_gf_sanity_skeleton.tex

- **Line 103**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item \textbf{$v = 246$ GeV input:} The Higgs VEV is experimentally determined...`

### sections/ch11_opr20_attemptD_interpretation_robin_overcount.tex

- **Line 50**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[\ding{55}] PDG mixing angles ($\theta_{13}$, $\theta_W$, etc.)...`

- **Line 51**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[\ding{55}] Fitting $\ell$ to match PDG values...`

### sections/ch11_opr20_attemptE_prefactor8_derivation.tex

- **Line 87**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item[\ding{55}] $M_W = 80$ GeV, $G_F$, $g_2$, $v = 246$ GeV...`

- **Line 88**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[\ding{55}] Any PDG weak-scale numbers to define $\ell$, $x_1$, or $R_\xi$...`

### sections/ch11_opr20_attemptG_derive_alpha_from_action.tex

- **Line 213**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item[$\times$] $v = 246$ GeV (Higgs VEV)...`

- **Line 215**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item[$\times$] PDG mixing angles...`

### sections/ch11_opr20_attemptH2plus_delta_Rxi_stricter_audit.tex

- **Line 70**: `Z boson mass`
  - Pattern: `91\.2|91\.19`
  - Context: `(specifically $M_Z = 91.2$ GeV). Deriving $R_\xi$ from the EDC action is listed...`

### sections/ch11_opr20_attemptH_delta_equals_Rxi.tex

- **Line 323**: `W boson mass`
  - Pattern: `80\.4|80\.38`
  - Context: `The predicted $m_\phi \approx 54$ GeV is 33\% below $M_W = 80.4$ GeV. This...`

### sections/ch14_bvp_closure_pack.tex

- **Line 29**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Calibration to PDG values (forbidden by design)...`

- **Line 93**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item The spectrum is computed without calibrating to PDG masses...`

- **Line 390**: `PDG reference`
  - Pattern: `PDG`
  - Context: `The derivation must \emph{not} use 3D observables (PDG masses, $M_W$, $G_F$) to...`

- **Line 425**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item No calibration to PDG values...`

- **Line 566**: `PDG reference`
  - Pattern: `PDG`
  - Context: `match $N_{\text{bound}} = 3$ or any PDG value...`

- **Line 921**: `PDG reference`
  - Pattern: `PDG`
  - Context: `If $V(\xi)$ or BCs are tuned to reproduce PDG masses $\to$ no predictive power....`

- **Line 922**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\emph{Next step:} Derive parameters from membrane physics only; compare to PDG \...`

- **Line 1218**: `PDG reference`
  - Pattern: `PDG`
  - Context: `All parameters are chosen \emph{a priori}. No fitting to PDG, $M_W$, $G_F$, or...`

- **Line 1219**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$v = 246$~GeV. The toy potential does NOT close OPR-21 or OPR-02....`

- **Line 1249**: `PDG reference`
  - Pattern: `PDG`
  - Context: `nor does it use PDG inputs to define thresholds or counts. It is included to ill...`

### sections/ch15_opr01_sigma_anchor_derivation.tex

- **Line 33**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item[$\times$] $v = 246$ GeV (Higgs VEV)...`

- **Line 38**: `CODATA reference`
  - Pattern: `CODATA`
  - Context: `\item[$\times$] Any CODATA-fitted constants...`

### sections/ch16_opr04_delta_derivation.tex

- **Line 441**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `\item[$\times$] No $M_W$, $G_F$, $v_{\rm EW} = 246$ GeV, $\sin^2\theta_W$ used...`

### sections/ch18_opr20_mediator_mass_from_eigenvalue.tex

- **Line 55**: `Higgs vev`
  - Pattern: `246|v\s*=\s*246`
  - Context: `$M_W = g v / 2$, where $v = 246$~GeV is the vacuum expectation value. In EDC, we...`

### sections/ch19_opr22_geff_from_exchange.tex

- **Line 45**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Any numerical comparison to PDG values is labeled ``external comparison on...`

- **Line 751**: `PDG reference`
  - Pattern: `PDG`
  - Context: `The measured Fermi constant is (PDG 2024):...`

- **Line 753**: `Fermi constant`
  - Pattern: `1\.166|1\.1664`
  - Context: `G_F = 1.1663788(6) \times 10^{-5} \, \text{GeV}^{-2}...`

### sections/ch4_attempt3B_em_options.tex

- **Line 22**: `proton/electron mass ratio`
  - Pattern: `1836|1837`
  - Context: `\item $m_p/m_e = 6\pi^5 = 1836.12$ \tagDer{}...`

### sections/ch6_pmns_attempt1.tex

- **Line 85**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\subsubsection{Comparison with PDG Data}...`

### sections/ch6_pmns_attempt3_z6_refinement.tex

- **Line 19**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\sin^2\theta_{13}^{\text{A3}} &= 0.0075 \quad \text{vs.} \quad 0.022 \text{ (PDG...`

- **Line 100**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Angle & Model & PDG & Status \\...`

### sections/ch6_pmns_attempt4_1_derive_epsilon.tex

- **Line 21**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item We compare predicted $\theta_{13}$ to PDG \emph{after} the prediction...`

- **Line 59**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{PDG} & \textbf{Error} & \textbf{Status} \\...`

- **Line 73**: `PDG reference`
  - Pattern: `PDG`
  - Context: `(excluding the PDG-exact value $33.7°$):...`

- **Line 86**: `PDG reference`
  - Pattern: `PDG`
  - Context: `PDG targets & $0.307$ & $0.546$ & $0.022$ & --- \\...`

- **Line 91**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Key finding:} With $\theta_{12}^0 = 35°$ (a discrete candidate, not PDG-...`

- **Line 102**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\times 2.7$ smaller than PDG. For C2 to work, the $\kappa$ ratio would need to ...`

### sections/ch6_pmns_attempt4_2_theta12_origin.tex

- **Line 21**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item PDG sin$^2\theta_{12} = 0.307$ is used ONLY for \emph{evaluation} AFTER pr...`

- **Line 22**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item The PDG-exact value $\theta_{12} = 33.7°$ is \textbf{not} a candidate...`

- **Line 55**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\caption{Attempt 4.2: $\theta_{12}$ candidates and comparison to PDG}...`

- **Line 60**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{PDG} & \textbf{Error} & \textbf{Status} \\...`

- **Line 72**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\paragraph{Key observation: PDG sits between T1 and T2.}...`

- **Line 74**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item T1 (35.26°) \emph{overshoots} PDG (33.65°) by $1.6°$...`

- **Line 75**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item T2 (32.00°) \emph{undershoots} PDG by $1.7°$...`

- **Line 94**: `PDG reference`
  - Pattern: `PDG`
  - Context: `PDG targets & $0.307$ & $0.546$ & $0.022$ & --- \\...`

- **Line 123**: `PDG reference`
  - Pattern: `PDG`
  - Context: `T2 has marginally better numerical fit. Both bracket the PDG value....`

- **Line 142**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Both T1 and T2 achieve GREEN ($<10\%$ error) without PDG-smuggling.}...`

- **Line 148**: `PDG reference`
  - Pattern: `PDG`
  - Context: `both $\sim 8.5\%$ from PDG, neither calibrated...`

- **Line 157**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Neither candidate exactly hits PDG ($\pm 1.6°$ bracketing)...`

- **Line 165**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Complete PMNS picture (no PDG-smuggling):}...`

- **Line 168**: `PDG reference`
  - Pattern: `PDG`
  - Context: `geometry (3\% from PDG)...`

- **Line 170**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\sin^2\theta_{13} = 0.025$ (15\% from PDG)...`

- **Line 172**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\sin^2\theta_{12} = 0.333$ (8.6\% from PDG)...`

- **Line 178**: `PDG reference`
  - Pattern: `PDG`
  - Context: `provides geometric origin for solar angle ($<10\%$ from PDG, no fit);...`

- **Line 185**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\theta_{12}$: $\arctan(1/\sqrt{2})$)---none calibrated to PDG.}...`

### sections/ch6_pmns_attempt4_menu.tex

- **Line 61**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{PDG 2024} & $[$BL$]$ & 0.307 & 0.546 & 0.022 & — & — \\...`

- **Line 92**: `PDG reference`
  - Pattern: `PDG`
  - Context: `achieves all three angles within 3\% of PDG values:...`

- **Line 96**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Angle & Model & PDG & Status \\...`

- **Line 111**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item $\theta_{12}^0 = 33.7°$: \textbf{Identified [I]} — matches PDG exactly, bu...`

### sections/ch7_attempt3_cp_phase.tex

- **Line 30**: `PDG reference`
  - Pattern: `PDG`
  - Context: `sign selection mechanism, yielding $\delta = 60°$ (5° from PDG)....`

- **Line 55**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\label{eq:ch7_J_pdg} \\...`

- **Line 57**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\label{eq:ch7_delta_pdg} \\...`

- **Line 59**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\label{eq:ch7_rhoeta_pdg}...`

- **Line 77**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Allow exactly one new parameter calibrated to one PDG input ($\delta$,...`

- **Line 158**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\textbf{Comparison:} $J_{\text{PDG}} = 3.08 \times 10^{-5}$ --- agreement within...`

- **Line 195**: `PDG reference`
  - Pattern: `PDG`
  - Context: `This predicts $\delta = \phi/2 \approx 67°$, compared to PDG $\delta \approx 65°...`

- **Line 206**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Track A (O4): predicts $\delta = 120°$, PDG gives $\delta \approx 65°$...`

- **Line 285**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Z3 gives $120°$, PDG gives $65°$. Need mechanism to reduce...`

- **Line 289**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Currently uses PDG magnitudes for $|V_{ub}|$. Need to derive the...`

- **Line 294**: `PDG reference`
  - Pattern: `PDG`
  - Context: `Z3 gives $\arg(\omega) = 120°$, but PDG $\arctan(\bar\eta/\bar\rho) \approx 65°$...`

- **Line 318**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\item Attempt~4 predicts $\delta = 60°$ (5° from PDG 65°) with...`

- **Line 319**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$J \simeq 2.9 \times 10^{-5}$ (5\% from PDG)....`

### sections/ch7_attempt4_cp_refinement.tex

- **Line 11**: `PDG reference`
  - Pattern: `PDG`
  - Context: `structure can refine $\delta$ toward the PDG value of $65°$ while preserving the...`

- **Line 103**: `PDG reference`
  - Pattern: `PDG`
  - Context: `This achieves $\delta = 60°$ (within 5° of PDG) while preserving $J \simeq 2.9 \...`

- **Line 135**: `PDG reference`
  - Pattern: `PDG`
  - Context: `\delta_{\text{pred}} &= 67° \quad \text{(PDG: 65°, error 2°)} \notag \\...`

- **Line 136**: `PDG reference`
  - Pattern: `PDG`
  - Context: `J_{\text{pred}} &= 3.05 \times 10^{-5} \quad \text{(PDG: 3.08×10$^{-5}$, error 1...`

- **Line 156**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\delta = 60°$ (5° from PDG), $J$ within 5\% of PDG \tagDc{} + \tagI{}....`

- **Line 182**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\delta$ prediction & YELLOW & \textbf{YELLOW (60°)} & Improved: 5° from PDG \\...`

- **Line 230**: `PDG reference`
  - Pattern: `PDG`
  - Context: `compared to PDG values $\delta = 65°$, $J = 3.08 \times 10^{-5}$....`

### sections/ch7_z2_parity_origin.tex

- **Line 155**: `PDG reference`
  - Pattern: `PDG`
  - Context: `$\delta_{\text{PDG}} = 65°$. May require:...`


## PROPERLY TAGGED INSTANCES

These have [BL] tags nearby (sample):

- main.tex:289 - PDG reference
- main.tex:289 - CODATA reference
- main.tex:316 - PDG reference
- main.tex:316 - CODATA reference
- main.tex:846 - PDG reference
- main.tex:846 - CODATA reference
- CH3_electroweak_parameters.tex:22 - PDG reference
- CH3_electroweak_parameters.tex:73 - sin^2(theta_W) at M_Z
- CH3_electroweak_parameters.tex:154 - sin^2(theta_W) at M_Z
- CH3_electroweak_parameters.tex:156 - sin^2(theta_W) at M_Z
- CH3_electroweak_parameters.tex:156 - Higgs vev
- CH3_electroweak_parameters.tex:176 - sin^2(theta_W) at M_Z
- CH3_electroweak_parameters.tex:434 - sin^2(theta_W) at M_Z
- CH3_electroweak_parameters.tex:434 - PDG reference
- CH3_electroweak_parameters.tex:474 - proton mass
- CH3_electroweak_parameters.tex:572 - Higgs vev
- CH3_electroweak_parameters.tex:574 - Higgs vev
- CH3_electroweak_parameters.tex:579 - W boson mass
- CH3_electroweak_parameters.tex:579 - PDG reference
- CH3_electroweak_parameters.tex:586 - Fermi constant
