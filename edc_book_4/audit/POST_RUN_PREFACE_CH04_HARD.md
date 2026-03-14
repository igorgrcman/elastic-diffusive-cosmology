# POST_RUN_PREFACE_CH04_HARD.md
## EDC Book IV — Hard Narrative Patch (Preface + Ch04)

**Date:** 2026-02-11
**Status:** ALL ACCEPTANCE CRITERIA PASS

---

## 1. ACCEPTANCE CRITERIA RESULTS

| Criterion | Evidence | Status |
|-----------|----------|--------|
| AC-P1: Preface spacing | No macro-stuck words found | **PASS** |
| AC-4.12: Eq (4.12) renders correctly | Proper `\frac` and `\sqrt` in align block | **PASS** |
| AC-PROV: δ and L0 provenance | Notation box at lines 59-71 with [P] tags | **PASS** |
| AC-SCALE: κ_c treatment consistent | Removed; scaling bridge explains quadratic form | **PASS** |
| AC-AT: Anti-tuning language | "Consistency Check (Not a Fit)" subsection | **PASS** |
| AC-BUILD: Compiles clean | 216 pages, no errors | **PASS** |
| AC-SCAN: Contamination/path leak | Both = 0 | **PASS** |
| AC-AUDIT: This report created | ✓ | **PASS** |

---

## 2. FIXES APPLIED

### 2.1 Preface (main.tex)

**Status:** No changes needed. Inspection confirmed:
- "brane tension $\bsigma$" has proper spacing (line 45)
- "\emph{observerbox} that" has proper spacing (line 70)
- No macro-stuck words detected

---

### 2.2 Ch04: Notation Box for δ and L0 (lines 59-71)

**Added:**
```latex
\begin{tcolorbox}[colback=gray!5,colframe=gray!50!black,title=Notation: Length Scales $\delta$ and $L_0$]
This chapter uses two geometric parameters:
\begin{itemize}
    \item $\delta \approx 0.105\;\text{fm}$: brane thickness / flux tube radius.
          \textbf{Source:} Postulated as $\delta = \hbar/(2 m_p c)$ (Compton regularization);
          analyzed in Ch.~\ref{ch:L0delta}. \tagP
    \item $L_0 \approx 1.0\;\text{fm}$: characteristic junction scale.
          \textbf{Source:} Postulated via the ratio hypothesis $L_0/\delta = \pi^2$
          in Ch.~\ref{ch:L0delta}. \tagP
\end{itemize}
Both are \emph{imported} into this chapter; their derivation status is [P] (postulated).
The ratio $L_0/\delta \approx 9.87$ drives the instanton exponent in Ch.~\ref{ch:tau_n}.
\end{tcolorbox}
```

---

### 2.3 Ch04: Scaling Bridge for Quadratic Form (lines 139-176)

**Issue:** κ_c introduced but then dropped without explanation.

**Fix:** Replaced with explicit "Scaling Bridge" subsection:
- Explains symmetry constraint (even in Δq)
- Gives curvature estimate R_c ~ L0/|Δq| with [P] tag
- Shows curvature energy scaling ~(Δq)²
- States O(1) factors absorbed into Kpin definition

**κ_c removed entirely** — quadratic form now derived from scaling arguments.

---

### 2.4 Ch04: f-Factor Derivation (Eq 4.12) — lines 198-228

**BEFORE:**
```latex
f = \frac{w_{\text{eff}}}{r_{\text{contact}}} = \frac{\delta}{\sqrt{\delta L_0}} = \sqrt{\frac{\delta}{L_0}} \approx 0.32 \tagI
```

**AFTER:**
```latex
\begin{align}
    r_{\text{contact}} &:= \sqrt{\delta \cdot L_0}
        && \text{(from Eq.~\eqref{eq:contact_area})} \\[0.5em]
    w_{\text{eff}} &:= \delta
        && \text{(penetration depth $\sim$ brane thickness)} \\[0.5em]
    f &:= \frac{w_{\text{eff}}}{r_{\text{contact}}}
        = \frac{\delta}{\sqrt{\delta \cdot L_0}}
        = \sqrt{\frac{\delta}{L_0}}
        \approx 0.32
    \label{eq:f_factor}
\end{align}
\tagI{} (identified ansatz; derivation remains OPEN)
```

**Changes:**
- Proper align block with clear step-by-step
- Each intermediate quantity explicitly defined
- Explicit [I] tag with "derivation remains OPEN"

---

### 2.5 Ch04: Anti-Tuning Rewrite (lines 288-322)

**BEFORE:** "Phenomenological Check" with "excellent agreement"

**AFTER:** "Consistency Check (Not a Fit)" with:
- Yellow Anti-Tuning Declaration box
- Explicit statement: "not adjusted to match observation"
- Comparison table (Model vs Benchmark)
- Honest acknowledgment of 15-25% discrepancy
- List of possible sources of discrepancy
- Reference to OPEN Problem 4.1

---

## 3. VERIFICATION COMMANDS

```bash
# Build
pdflatex -interaction=nonstopmode main.tex  # ×2
# Output: 216 pages, 1181937 bytes

# Undefined refs
grep -c "LaTeX Warning: Reference.*undefined" main.log
# Output: 0

# Contamination scan
grep -E "tetrahed" chapters/*.tex | grep -v "%" | wc -l
# Output: 0

# Path leak scan
pdftotext main.pdf - | grep -c "/Users/"
# Output: 0

# Broken Eq (4.12) pattern
grep "δ√δL0" chapters/ch04_sigma_to_K.tex
# Output: (no match - fixed)

# Updated Eq (4.12) source
grep -A5 "eq:f_factor" chapters/ch04_sigma_to_K.tex
# Shows proper align block with \frac and \sqrt

# Anti-tuning language
grep "Anti-Tuning\|Not a Fit" chapters/ch04_sigma_to_K.tex
# Output: lines 288, 290

# δ/L0 provenance
grep "Notation.*Length\|Source:.*Ch" chapters/ch04_sigma_to_K.tex
# Output: lines 59, 64, 67
```

---

## 4. BUILD SUMMARY

| Metric | Value |
|--------|-------|
| Page count | 216 |
| SHA-256 | `952ca89a9a48a65081d2c437a7d71e58e5edfa6d7be5086c1743ca14c0bb36a3` |
| Exit code | 0 |
| Undefined refs | 0 |
| Contamination hits | 0 |
| Path leaks | 0 |

---

## 5. FILES MODIFIED

```
chapters/ch04_sigma_to_K.tex  (+62 lines net)
  - Notation box for δ, L0 (lines 59-71)
  - Scaling bridge subsection (lines 139-176)
  - f-factor align block (lines 198-228)
  - Anti-tuning rewrite (lines 288-322)
```

---

## 6. SUMMARY OF NARRATIVE IMPROVEMENTS

| Issue | Fix | Location |
|-------|-----|----------|
| δ, L0 provenance missing | Notation box with sources + [P] tags | §4.2 |
| κ_c introduced then dropped | Removed; scaling bridge explains quadratic | §4.3 |
| Eq (4.12) algebra unclear | Clean align block with definitions | §4.4 |
| "Phenomenological check" too strong | Anti-tuning language + discrepancy acknowledged | §4.6 |

**Reader trust breakers eliminated. Ch04 now reads as a strict derivation chain with honest epistemic markers.**

---

**ALL 8 ACCEPTANCE CRITERIA PASS.**
