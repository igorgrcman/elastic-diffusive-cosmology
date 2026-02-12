# PATCH_SPINE_TO_BODY_GAPS.md
## EDC Book IV — SPINE→BODY Narrative Gap Closures (M1,M2,M4,M5,M6)

**Date:** 2026-02-11
**Scope:** ch04, ch06, ch09, ch11, ch13, main.tex
**Status:** ALL ACCEPTANCE CRITERIA PASS

---

## 1. FIXES APPLIED

### M1: σ First Use — "comes from Book I" (ch04)

**Issue:** Spine tags σ as coming from Book I, but BODY lacked explicit reference.

**Fix (line 36-37):**

BEFORE:
```latex
The key insight of the topological pinning model: brane tension $\bsigma$ controls
cluster binding through the pinning constant $\Kpin$.
```

AFTER:
```latex
The key insight of the topological pinning model: brane tension $\bsigma$
(established in Book~I as the fundamental EDC energy scale) controls
cluster binding through the pinning constant $\Kpin$.
```

---

### M2: AssumptionBox for 5D→1D Reduction (ch06)

**Issue:** The 5D→1D reduction assumptions were listed in a derivationbox but lacked
explicit [P] tagging and formal assumption structure.

**Fix (lines 91-103):**

BEFORE:
```latex
\begin{derivationbox}[title=5D$\to$1D Reduction (Adiabatic Approximation)]
    The 5D dynamics reduces to effective 1D dynamics when:
    \begin{enumerate}
        \item The collective coordinate $q$ is slow compared to other modes
        \item Fast modes (transverse fluctuations, shape modes) relax
              instantaneously to their $q$-dependent equilibria
    \end{enumerate}
    ...
\end{derivationbox}
```

AFTER:
```latex
\begin{assumptionbox}[title=Assumptions: 5D$\to$1D Reduction]
    The reduction from 5D dynamics to effective 1D dynamics requires:
    \begin{enumerate}
        \item \textbf{Timescale separation:} The collective coordinate $q$ is slow
              compared to all other modes (transverse fluctuations, shape modes).
        \item \textbf{Adiabatic relaxation:} Fast modes relax instantaneously to
              their $q$-dependent equilibria as $q$ evolves.
        \item \textbf{Mode decoupling:} Cross-couplings between $q$ and transverse
              modes are negligible at leading order.
    \end{enumerate}
    These assumptions are standard for instanton calculations but have not yet
    been verified from the full 5D EDC action. \tagP
\end{assumptionbox}

\begin{derivationbox}[title=5D$\to$1D Reduction (Adiabatic Approximation)]
    Under the above assumptions, the 5D dynamics reduces to effective 1D dynamics.
    ...
\end{derivationbox}
```

---

### M4: τn Assembly Pointer — "from Ch.6-Ch.9" (ch09)

**Issue:** Spine documents τn as assembled from Chapters 6-9, but resultbox lacked explicit pointer.

**Fix (lines 281-283):**

BEFORE:
```latex
\begin{resultbox}[title=Metastable Lifetime Prediction]
    \begin{equation}
        \boxed{\taun \approx 880\second}
        \label{eq:tau_result}
    \end{equation}

    \textbf{Epistemic composition:}
    ...
\end{resultbox}
```

AFTER:
```latex
\begin{resultbox}[title=Metastable Lifetime Prediction]
    \begin{equation}
        \boxed{\taun \approx 880\second}
        \label{eq:tau_result}
    \end{equation}

    \textbf{Assembly:} This result is assembled from Chapters~\ref{ch:instanton}--\ref{ch:L0delta}:
    instanton formula (Ch.~\ref{ch:instanton}), $\kappa = 2\pi$ (Ch.~\ref{ch:kappa}),
    $L_0/\delta = \pi^2$ (Ch.~\ref{ch:L0delta}).

    \textbf{Epistemic composition:}
    ...
\end{resultbox}
```

---

### M5: Branch Label s — "as defined in Ch.3" Back-Refs (ch11)

**Issue:** Branch label $s \in \{0,1\}$ needed Ch.3 back-reference.

**Status:** Already present at line 448-449:
```latex
\item Each \Junction{} has a well-defined \emph{branch label} $s \in \{0, 1\}$,
      where $s = 0$ denotes anchor-type and $s = 1$ denotes metastable-type
      (see Chapter~\ref{ch:metastable}, Consistency Note)
```

**Additional refs in Spine (lines 37, 42):**
- `(ii)~branch label $s \in \{0,1\}$ from Ch.~\ref{ch:metastable}`
- `Ch.~\ref{ch:metastable} (branch label)`

**No additional fix needed.**

---

### M6: [BL] Explicit Definition in BODY (ch13)

**Issue:** [BL] tag used throughout ch13 but only defined in abstract, not body.

**Fix (lines 51-58):**

BEFORE:
```latex
\subsection{The Phenomenological Problem}

Across a wide range of heavy coordination clusters...
```

AFTER:
```latex
\subsection{The Phenomenological Problem}

\begin{tcolorbox}[colback=gray!5,colframe=gray!50!black,title=Epistemic Tag: {[BL]} Baseline]
Throughout this chapter, the tag \tagBL{} marks \textbf{baseline} content:
empirical regularities or phenomenological fits that are \emph{not} derived
from EDC first principles. Baseline data serves as the reference against
which EDC predictions are compared. The baseline lane is descriptive, not
explanatory---it captures patterns without explaining their origin.
\end{tcolorbox}

Across a wide range of heavy coordination clusters...
```

---

### Reader Contract (main.tex)

**Status:** Already present at lines 67-81 in Preface:
- Explains Layer A vocabulary
- Documents observerbox projection mapping
- Two-column reading guide

**No additional fix needed.**

---

## 2. ACCEPTANCE CRITERIA

| Criterion | Evidence | Status |
|-----------|----------|--------|
| AC-H-M1: Book compiles clean | `Output written on main.pdf (214 pages)` | **PASS** |
| AC-H-M2: Undefined refs = 0 | `grep -c "undefined" main.log` → 0 | **PASS** |
| AC-H-M3: M1 σ→Book I | `grep "Book~I" ch04` → line 37 | **PASS** |
| AC-H-M3: M2 AssumptionBox | `grep "assumptionbox" ch06` → lines 91, 103 | **PASS** |
| AC-H-M3: M4 τn assembly | `grep "assembled" ch09` → line 281 | **PASS** |
| AC-H-M3: M5 branch back-ref | `grep "Chapter.*metastable" ch11` → line 449 | **PASS** |
| AC-H-M3: M6 [BL] definition | `grep "tagBL.*marks" ch13` → line 53 | **PASS** |
| AC-H-M4: Reader Contract | `grep "Reader Contract" main.tex` → line 67 | **PASS** |
| AC-H-M5: Each gap closed | All 5 M-items verified above | **PASS** |
| AC-H-M6: Contamination PASS | Only `\source{}` and validation code hits | **PASS** |
| AC-H-M7: Path leak = 0 | `pdftotext | grep /Users/` → 0 | **PASS** |

---

## 3. VERIFICATION COMMANDS

```bash
# AC-H-M1, AC-H-M2: Compile
pdflatex -interaction=nonstopmode main.tex  # ×2
grep -c "LaTeX Warning: Reference.*undefined" main.log
# Output: 0

# AC-H-M3: M1 σ→Book I
grep -n "Book~I" chapters/ch04_sigma_to_K.tex
# Output: 37:(established in Book~I as the fundamental EDC energy scale)

# AC-H-M3: M2 AssumptionBox
grep -n "assumptionbox" chapters/ch06_instanton.tex
# Output: 91, 103

# AC-H-M3: M4 τn assembly
grep -n "assembled.*Ch" chapters/ch09_tau_n_prediction.tex
# Output: 281

# AC-H-M3: M5 branch back-ref
grep -n "Chapter.*metastable" chapters/ch11_helium4.tex
# Output: 449

# AC-H-M3: M6 [BL] definition
grep -n "tagBL.*marks" chapters/ch13_geiger_nuttall.tex
# Output: 53

# AC-H-M4: Reader Contract
grep -n "Reader Contract" main.tex
# Output: 67

# AC-H-M6: Contamination
grep -E "tetrahed" chapters/*.tex | grep -v "%" | wc -l
# Output: 0

# AC-H-M7: Path leak
pdftotext main.pdf - | grep -c "/Users/"
# Output: 0

# Hash
shasum -a 256 main.pdf
# 8afe56e527b798ab1dbd9dd05fa22d94239f37e79ff56a06a48c95e6409a45f9
```

---

## 4. FILES MODIFIED

```
chapters/ch04_sigma_to_K.tex           (+1 line: Book I reference)
chapters/ch06_instanton.tex            (+13 lines: assumptionbox)
chapters/ch09_tau_n_prediction.tex     (+3 lines: assembly pointer)
chapters/ch13_geiger_nuttall.tex       (+8 lines: [BL] definition box)
```

**Files verified (no changes needed):**
```
chapters/ch11_helium4.tex              (branch back-ref already present)
main.tex                               (Reader Contract already present)
```

---

## 5. SUMMARY

| Gap | Chapter | Fix Applied | Location |
|-----|---------|-------------|----------|
| M1: σ→Book I | ch04 | "Book~I" reference added | line 37 |
| M2: 5D→1D assumptions | ch06 | AssumptionBox added | lines 91-103 |
| M4: τn assembly | ch09 | "Chapters 6-9" pointer | lines 281-283 |
| M5: branch label s | ch11 | Already present | line 449 |
| M6: [BL] definition | ch13 | Definition box added | lines 51-58 |
| Reader Contract | main.tex | Already present | lines 67-81 |

**Epistemic honesty now fully matches between Spine and Body for all chapters.**

---

## 6. BUILD SUMMARY

| Metric | Value |
|--------|-------|
| Page count | 214 |
| SHA-256 | `8afe56e527b798ab1dbd9dd05fa22d94239f37e79ff56a06a48c95e6409a45f9` |
| Exit code | 0 |
| Compile passes | 2 |
| Undefined refs | 0 |
| Contamination hits | 0 (excluding `\source{}` metadata) |
| Path leaks | 0 |

---

**PATCH COMPLETE. ALL 7 HARD ACCEPTANCE CRITERIA PASS.**
