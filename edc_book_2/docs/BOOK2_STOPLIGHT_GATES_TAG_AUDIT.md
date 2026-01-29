# Book 2 Stoplight, Gates & Epistemic Tag Audit

**Generated:** 2026-01-29
**Purpose:** KORAK 2-3 output - detailed audit of defensive framework

## A) Summary: Top 10 Issues

1. **Case chapters missing Stoplight Verdicts** (6 files)
   - `05_case_neutron.tex`, `06_case_muon.tex`, `07_case_tau.tex`
   - `08_case_pion.tex`, `09_case_electron.tex`, `10_case_neutrino.tex`

2. **Core chapters missing Stoplight** (4 files)
   - `02_frozen_regime_foundations.tex` - foundational chapter
   - `ch10_electroweak_bridge.tex` - bridge chapter
   - `13_summary.tex` - should summarize verdicts
   - `ch20_epistemic_summary_closure_status.tex` - should have overall verdict

3. **OPR chapters missing final Verdicts** (6 files)
   - ch14-ch19 OPR derivation chapters need closure statements

4. **Gate Registry fragmentation**
   - Gates mentioned in multiple places without central registry
   - GF gates in `11_gf_derivation.tex`
   - BVP gates in `ch14_bvp_closure_pack.tex`
   - Q-gates in `05_case_neutron.tex`
   - No consolidated "gate registry" table

5. **k-channel guardrail OK**
   - Box `kchannel_spinchain_crossval_box.tex` included in §12
   - Box `zn_kchannel_robustness_box.tex` in Derivation Library
   - Explicit "Do NOT use for cardinality ratios" present

6. **[Der] tag usage - mostly OK**
   - `sin²θ_W = 1/4` tagged [Der] - CORRECT (Z6 counting derivation exists)
   - `m_p/m_e = 6π⁵` tagged [Der] - CORRECT (Book 1 derivation)
   - No obvious overclaiming found

7. **Stoplight legend defined but not always referenced**
   - `edc_stoplight_legend.tex` exists with proper definitions
   - Not all chapters reference the legend

8. **"Reader Contract" exists but is short**
   - Located in `00_reader_contract.tex` (33 lines) and main.tex front matter
   - Could use explicit "How to read this book" flowchart

9. **Duplication: GF constraint window explained multiple places**
   - `11_gf_derivation.tex`
   - Multiple ch11 attempt files
   - `ch12_bvp_workpackage.tex`

10. **Missing "projection principle" explicit connection**
    - δ = L₀ - rₚ derivation exists in derivations/ but not prominently linked

## B) Chapter-by-Chapter Findings

### Chapter 1: The Weak Interface

| File | Issue | Line | Severity |
|------|-------|------|----------|
| 00_reader_contract.tex | OK - meta section | - | - |
| 01_how_we_got_here.tex | No stoplight (intro OK) | - | LOW |
| 02_geometry_interface.tex | No stoplight | - | MEDIUM |
| 03_unified_pipeline.tex | No stoplight | - | MEDIUM |
| 04_ontology.tex | No stoplight | - | MEDIUM |
| 05_case_neutron.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 06_case_muon.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 07_case_tau.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 08_case_pion.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 09_case_electron.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 10_case_neutrino.tex | **Missing Stoplight Verdict** | - | **HIGH** |
| 13_summary.tex | **Missing overall verdict** | - | **HIGH** |

### Chapter 2: Frozen Regime Foundations

| File | Issue | Line | Severity |
|------|-------|------|----------|
| 02_frozen_regime_foundations.tex | **Missing Stoplight Verdict** | - | **HIGH** |

### Chapters 3-7: Core Weak Sector

| File | Status | Notes |
|------|--------|-------|
| Z6_content_full.tex | Has internal verdicts | OK |
| CH3_electroweak_parameters.tex | Has verdicts | OK |
| CH4_lepton_mass_candidates.tex | Has verdicts | OK |
| 05_three_generations.tex | Has Stoplight | OK |
| 06_neutrinos_edge_modes.tex | Has Stoplight | OK |
| 07_ckm_cp.tex | Has Stoplight | OK |

### Chapters 8-11: GF and V-A

| File | Status | Notes |
|------|--------|-------|
| 11_gf_derivation.tex | Has Stoplight | OK |
| 09_va_structure.tex | Has Stoplight | OK |
| ch10_electroweak_bridge.tex | **Missing Stoplight** | HIGH |
| 12_epistemic_map.tex | Has Stoplight | OK |

### Chapter 12: GF Closure Attempts

| File | Status | Notes |
|------|--------|-------|
| ch11_g5_* files | Have Verdicts | OK |
| ch11_opr20_* files | Have Verdicts | OK |
| ch11_gf_sanity_skeleton.tex | Has Verdict | OK |

### Chapters 14-20: OPR Derivations

| File | Issue | Severity |
|------|-------|----------|
| ch14_bvp_closure_pack.tex | Has PASS/FAIL gates, **no summary verdict** | MEDIUM |
| ch14_opr21_closure_derivation.tex | Has PASS/FAIL gates, **no summary verdict** | MEDIUM |
| ch15_opr01_sigma_anchor_derivation.tex | **No verdict** | MEDIUM |
| ch16_opr04_delta_derivation.tex | Has verdict box | OK |
| ch17_opr19_g5_from_action.tex | **No verdict** | MEDIUM |
| ch18_opr20_mediator_mass_from_eigenvalue.tex | **No verdict** | MEDIUM |
| ch19_opr22_geff_from_exchange.tex | **No verdict** | MEDIUM |
| ch20_epistemic_summary_closure_status.tex | **Should have OVERALL verdict** | **HIGH** |

## C) Proposed Minimal Patches

### HIGH PRIORITY - Case Chapter Stoplight Stubs

For each case chapter (`05_case_neutron.tex`, `06_case_muon.tex`, etc.), add at the end:

```latex
% ========================================
% STOPLIGHT VERDICT
% ========================================
\subsubsection{Stoplight Verdict}

\begin{tcolorbox}[colback=yellow!10!white, colframe=orange!50!black,
    title=\textbf{Case [X] Verdict}]
\begin{center}
\begin{tabular}{lll}
\toprule
\textbf{Claim} & \textbf{Status} & \textbf{Tag} \\
\midrule
[Main claim 1] & [G/Y/R] & [Tag] \\
[Main claim 2] & [G/Y/R] & [Tag] \\
\bottomrule
\end{tabular}
\end{center}

\textbf{Overall:} [YELLOW] --- [brief justification]

See \S\ref{ch:epistemic_map} for full epistemic landscape.
\end{tcolorbox}
```

### MEDIUM PRIORITY - OPR Chapter Verdicts

For OPR chapters without verdicts, add:

```latex
\subsection{OPR-XX Verdict}
\begin{tcolorbox}[colback=green!5!white, colframe=green!50!black,
    title=\textbf{OPR-XX Closure Status}]
\textbf{Status:} [GREEN-A / GREEN-B / YELLOW / RED]

\textbf{Gates passed:} [list]

\textbf{Open items:} [list or "None"]
\end{tcolorbox}
```

### LOW PRIORITY - Gate Registry

Add to `12_epistemic_map.tex` or create new section:

```latex
\subsection{Consolidated Gate Registry}
\begin{center}
\begin{tabular}{llll}
\toprule
\textbf{Gate ID} & \textbf{Description} & \textbf{Location} & \textbf{Status} \\
\midrule
GF-1 & $\sin^2\theta_W$ closure & \S11.2 & PASS \\
GF-2 & $g^2$ closure & \S11.3 & PASS \\
GF-3 & Mode overlap & \S11.4 & OPEN \\
BVP-1 & $N_{\text{bound}} = 3$ & \S14 & PASS \\
BVP-2 & BC independence & \S14 & PASS \\
Q-Gate & Kinematic selection & \S1.5 & PASS \\
\bottomrule
\end{tabular}
\end{center}
```

## D) k-channel Guardrail Status: OK

**Location:** `edc_book_2/src/sections/12_epistemic_map.tex` line 71

**Includes:**
- `kchannel_spinchain_crossval_box.tex` - cross-validation summary
- `zn_kchannel_robustness_box.tex` - applicability rules (in Derivation Library)

**Explicit guardrail text present:**
> "Do NOT use for cardinality/subgroup ratios (sin²θ_W = |Z_2|/|Z_6|, N_g = |Z_3|, CP phases, Koide Q)"

**Status:** No patches needed for k-channel.

## E) Epistemic Tag Audit: OK

**[Der] usage verified:**
- `sin²θ_W = 1/4` [Der] - Z6 counting derivation in CH3/Z6_content
- `m_p/m_e = 6π⁵` [Der] - Book 1 derivation
- No overclaiming found

**Common pattern observed:**
- Most derivations properly tagged [Dc] (conditional)
- Clear distinction between [Der] (from postulates) and [Dc] (conditional on assumptions)

## F) Recommendations

1. **Immediate (minimal patches):**
   - Add stoplight stubs to 6 case chapters
   - Add overall verdict to ch20_epistemic_summary_closure_status.tex
   - Add verdict to 13_summary.tex

2. **Near-term (consolidation):**
   - Create Gate Registry table in §12
   - Add "How to read this book" flowchart
   - De-duplicate GF constraint explanations

3. **Deferred (human judgment):**
   - Decide exact GREEN/YELLOW/RED for each case chapter
   - Review OPR chapters for final closure status

---
*Generated by Book 2 Stoplight/Gates/Tag Audit (KORAK 2-3)*
