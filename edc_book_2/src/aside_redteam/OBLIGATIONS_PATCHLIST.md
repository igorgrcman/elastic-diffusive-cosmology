# OBLIGATIONS PATCHLIST: Red Team Demands

**IMPORTANT:** This is NOT to be implemented in the main book.
This is a patchlist as DEMANDS from Red Team.

---

## CRITICAL PATCHES (Must-Have for Publication)

### PATCH-001: Coupling Map Derivation

**Target:** CH3_electroweak_parameters.tex, after line 213

**What Must Be Added:**
```latex
\begin{proofobligationbox}{Coupling Map Derivation Required}
\label{oblg:coupling_map}
The identification $g'^2/g^2 = |\mathbb{Z}_2|/|\mathbb{Z}_6|$ is currently \tagP{}.

\textbf{Required proof:}
\begin{enumerate}
    \item Start from 5D EDC action with Z6-symmetric boundary conditions
    \item Derive gauge kinetic terms via Kaluza-Klein reduction
    \item Show that coupling constants emerge as overlap integrals
    \item Prove the ratio equals $|Z_2|/|Z_6| = 1/3$
\end{enumerate}

\textbf{Without this proof:} $\sin^2\theta_W = 1/4$ is an IDENTIFICATION [I], not a derivation [Dc].
\end{proofobligationbox}
```

**Expected Tag:** [Dc] after resolution, [OPEN] currently

**Acceptance Test:** Passes if derivation uses only 5D action + BC, with no coupling ratio as input.

---

### PATCH-002: σ→∞ Convergence Theorem

**Target:** sections/02_frozen_regime_foundations.tex, after line 253

**What Must Be Added:**
```latex
\begin{theorem}[Frozen Limit Convergence]
\label{thm:frozen_convergence}
\tagOPEN{}

Let $f_\sigma(r)$ be the profile minimizing the 5D energy functional at tension $\sigma$.
Then:
\begin{equation}
\lim_{\sigma \to \infty} f_\sigma(r) = \Theta(r - a) \quad \text{in } \mathcal{D}'(\mathbb{R}^3)
\end{equation}
where convergence is in the sense of distributions.

\textbf{Required proof:}
\begin{enumerate}
    \item Write Euler-Lagrange equation for energy functional
    \item Solve for $f_\sigma(r)$ at finite $\sigma$
    \item Take $\sigma \to \infty$ limit and show distributional convergence
    \item Verify energy convergence: $E[f_\sigma] \to E[\Theta]$
\end{enumerate}
\end{theorem}
```

**Expected Tag:** [Dc] after resolution

**Acceptance Test:** Passes if limit is proven in distributional sense with explicit error bound.

---

### PATCH-003: Y-Junction Topological Definition

**Target:** Z6_content_full.tex, after line 435

**What Must Be Added:**
```latex
\begin{definition}[Y-Junction as Topological Class]
\label{def:y_junction_topological}
\tagOPEN{}

A Y-junction is a map $\Phi: S^2 \to \mathcal{M}$ where $\mathcal{M}$ is the order parameter manifold,
such that:
\begin{enumerate}
    \item $\Phi$ has winding number $(n_1, n_2, n_3)$ around three asymptotic directions
    \item The total winding satisfies $n_1 + n_2 + n_3 = 0$ (color neutrality)
    \item The configuration is classified by $\pi_2(\mathcal{M}/G)$ where $G$ is the gauge group
\end{enumerate}

\textbf{Required proof:} Compute $\pi_2$ explicitly and show Y-junction is non-trivial element.
\end{definition}
```

**Expected Tag:** [M] for group theory, [Dc] for physical identification

**Acceptance Test:** Passes if homotopy group is computed and Y-junction assigned explicit element.

---

### PATCH-004: Projection Operator Definition

**Target:** sections/03_unified_pipeline.tex, after line 121

**What Must Be Added:**
```latex
\begin{definition}[Frozen Projection Operator - Rigorous]
\label{def:pfrozen_rigorous}
\tagOPEN{}

Let $\mathcal{H}_{\text{brane}}$ be the Hilbert space of brane mode configurations.
The frozen projection operator is:
\begin{equation}
\mathcal{P}_{\text{frozen}}: \mathcal{H}_{\text{brane}} \to \mathcal{H}_{\text{3D}}
\end{equation}
defined as the composition:
\begin{equation}
\mathcal{P}_{\text{frozen}} = P_{\text{energy}} \circ P_{\text{mode}} \circ P_{\text{chir}}
\end{equation}
where each component is a bounded operator with:
\begin{itemize}
    \item $P_{\text{energy}}$: projection onto $E < Q$ subspace (spectral projector)
    \item $P_{\text{mode}}$: projection onto frozen modes (discrete spectrum)
    \item $P_{\text{chir}}$: projection onto left-handed chirality
\end{itemize}

\textbf{Required proof:}
\begin{enumerate}
    \item Define $\mathcal{H}_{\text{brane}}$ explicitly
    \item Show each component is bounded (or closable)
    \item Prove composition is well-defined
    \item Compute spectrum of $\mathcal{P}_{\text{frozen}}$
\end{enumerate}
\end{definition}
```

**Expected Tag:** [M] for operator theory, [Dc] for physical application

**Acceptance Test:** Passes if inner products and norms are defined, spectrum computed.

---

## HIGH PRIORITY PATCHES

### PATCH-005: RG Running Calculation

**Target:** CH3_electroweak_parameters.tex, after line 239

**What Must Be Added:**
```latex
\begin{gapbox}{RG Running: Quantitative Check Required}
\label{gap:rg_running}

The 8\% discrepancy between $\sin^2\theta_W = 0.25$ (EDC) and $\sin^2\theta_W = 0.231$ (experiment at $M_Z$)
is attributed to RG running. This must be verified quantitatively.

\textbf{Required calculation:}
\begin{enumerate}
    \item Identify lattice scale $\mu_{\text{lattice}}$ (where is Z6 realized?)
    \item Compute SM RG flow: $\sin^2\theta_W(\mu)$ from $\mu_{\text{lattice}}$ to $M_Z$
    \item Verify that $0.25 \xrightarrow{\text{RG}} 0.231 \pm \epsilon$
\end{enumerate}

\textbf{Problem:} In SM, $\sin^2\theta_W$ \emph{increases} with energy scale.
At $M_Z$: 0.231; at GUT scale: $\sim 0.375$.
So 0.25 corresponds to an intermediate scale $\sim 10^3$ GeV.

\textbf{Question:} Is the EDC lattice scale $\sim 10^3$ GeV? If so, why?
\end{gapbox}
```

**Expected Tag:** [Cal] after computation

**Acceptance Test:** Passes if running is computed and scale identified.

---

### PATCH-006: Baseline Value Tagging

**Target:** ALL FILES with SM values

**What Must Be Added:**

Every occurrence of:
- 0.511 MeV (m_e)
- 105.7 MeV (m_μ)
- 938.3 MeV (m_p)
- 137.036 (1/α)
- 0.231 (sin²θ_W at M_Z)
- etc.

MUST carry explicit tag:
```latex
$m_e = 0.511~\text{MeV}$ \tagBL{}
```

**Expected Tag:** [BL] everywhere

**Acceptance Test:** Passes if `no_smuggling_scan.py` reports 0 SUSPICIOUS instances.

---

### PATCH-007: Explicit Falsifiers

**Target:** New section in Chapter 12 or Summary

**What Must Be Added:**
```latex
\section{Falsification Criteria}
\label{sec:falsifiers}

For EDC Part II to be considered scientific, it must be falsifiable.
The following observations would REFUTE the framework:

\begin{enumerate}
    \item \textbf{Proton decay:} If $\tau_p < 10^{34}$ years, frozen stability fails.
    \item \textbf{Fourth generation:} If $N_g > 3$ discovered, Z6/Z2 counting fails.
    \item \textbf{Weinberg angle:} If high-precision measurement at lattice scale
          gives $\sin^2\theta_W \neq 0.25 \pm 0.01$, Z6 partition fails.
    \item \textbf{Neutron lifetime:} If $\tau_n$ deviates from prediction by $> 10\%$,
          frozen projection selection rules fail.
    \item \textbf{New light charged lepton:} If m < m_e exists, ground mode identification fails.
\end{enumerate}

\textbf{Tolerance:} Each prediction has stated tolerance. Agreement within tolerance
supports the framework; disagreement refutes it.
\end{enumerate}
```

**Expected Tag:** [Framework requirement]

**Acceptance Test:** Passes if 5+ explicit falsifiers stated with tolerances.

---

## MEDIUM PRIORITY PATCHES

### PATCH-008: Z6 Uniqueness Proof

**Target:** Z6_content_full.tex, after line 354

**What Must Be Added:**
```latex
\begin{lemma}[Z6 is Unique Minimal Discrete Symmetry]
\label{lem:z6_unique}
\tagOPEN{}

Among all discrete rotational symmetries $\mathbb{Z}_n$ compatible with:
\begin{enumerate}
    \item 2D energy minimization (Kepler packing)
    \item Non-trivial quotient structure ($n$ composite)
    \item Three-way junction stability
\end{enumerate}
$\mathbb{Z}_6$ is the unique solution.

\textbf{Required proof:}
\begin{enumerate}
    \item $\mathbb{Z}_4$: Square lattice, but 90° junctions unstable (not Steiner)
    \item $\mathbb{Z}_8$: Octagonal tiling not space-filling
    \item $\mathbb{Z}_{12}$: Leads to $\mathbb{Z}_4 \times \mathbb{Z}_3$, not $\mathbb{Z}_2 \times \mathbb{Z}_3$
    \item $\mathbb{Z}_6 = \mathbb{Z}_2 \times \mathbb{Z}_3$: Hexagonal, space-filling, Steiner-stable
\end{enumerate}
\end{lemma}
```

**Expected Tag:** [M] + [Dc]

**Acceptance Test:** Passes if alternative Z_n are explicitly ruled out.

---

### PATCH-009: Neutron Excitation Spectrum

**Target:** sections/05_case_neutron.tex, after line 30

**What Must Be Added:**
```latex
\begin{gapbox}{Excitation Spectrum Required}
\label{gap:neutron_spectrum}

The neutron is claimed to be an "excited state" of the proton Y-junction.
For this to be rigorous:

\textbf{Required derivation:}
\begin{enumerate}
    \item Define configuration space $\mathcal{C}$ of Y-junction displacements
    \item Compute effective potential $V(\delta)$ where $\delta$ = displacement
    \item Quantize: find energy levels $E_n$
    \item Show: $E_0 = m_p$, $E_1 = m_n$, with $E_1 - E_0 = 1.293$ MeV
    \item Show: no other states between $E_0$ and $E_1$
\end{enumerate}

\textbf{Without this:} "Excited state" is metaphor, not prediction.
\end{gapbox}
```

**Expected Tag:** [OPEN] → [Dc] after resolution

**Acceptance Test:** Passes if n-p mass difference is computed from potential, not fit.

---

### PATCH-010: Step Function Regularization

**Target:** sections/02_frozen_regime_foundations.tex, after line 280

**What Must Be Added:**
```latex
\begin{remark}[Step Function Regularization]
\label{rem:step_regularization}

The step function $\Theta(r-a)$ has infinite derivative at $r=a$.
For well-defined energy integrals, we regularize:
\begin{equation}
\Theta_\epsilon(r-a) = \frac{1}{2}\left(1 + \tanh\frac{r-a}{\epsilon}\right)
\end{equation}
and take $\epsilon \to 0$ after integration.

\textbf{Check:} Energy integrals converge as $\epsilon \to 0$.

\textbf{Note:} This is the physical σ→∞ limit: large σ forces small ε.
The frozen profile is the $\epsilon \to 0$ limit of smooth profiles.
\end{remark}
```

**Expected Tag:** [M] for regularization procedure

**Acceptance Test:** Passes if convergence is verified for key integrals.

---

## PATCH IMPLEMENTATION RULES

1. **DO NOT implement in src/** — patches are demands, not implementations
2. **Author must decide** — Red Team identifies gaps, author fills them
3. **Tag changes cascade** — if [P] becomes [Dc], update all dependents
4. **Falsifiers are non-negotiable** — scientific status requires falsifiability

---

## ACCEPTANCE CRITERIA SUMMARY

| Patch | Status | Acceptance Test |
|-------|--------|-----------------|
| PATCH-001 | CRITICAL | Coupling map derived from action |
| PATCH-002 | CRITICAL | σ→∞ limit proven convergent |
| PATCH-003 | CRITICAL | Y-junction in homotopy class |
| PATCH-004 | CRITICAL | P_frozen has Hilbert space |
| PATCH-005 | HIGH | RG running computed |
| PATCH-006 | HIGH | 0 SUSPICIOUS in smuggling scan |
| PATCH-007 | HIGH | 5+ falsifiers with tolerances |
| PATCH-008 | MEDIUM | Z6 uniqueness proven |
| PATCH-009 | MEDIUM | n-p mass from spectrum |
| PATCH-010 | MEDIUM | Regularization verified |

---

*Patch obligations from Red Team forensic audit. Resolution elevates claims from [P]/[I]/[OPEN] to [Dc].*
