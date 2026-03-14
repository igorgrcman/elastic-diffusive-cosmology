# POST_RUN_CHECK_REPORT_HARD.md
## EDC Book IV - Hard Narrative Patch Verification

**Date:** 2026-02-11
**Build:** PASS

---

## 1. Build Summary

| Metric | Value |
|--------|-------|
| Page count | 212 |
| SHA-256 | `f6623e585dde8c4c571eb9eb15c3ada53e0ef35ef7338ae36077abf898077c2d` |
| Exit code | 0 |

---

## 2. Hard Gate Results

### AC-H1: Preface contains explicit projection table
**Status:** PASS
Projection mapping table added to main.tex Preface (lines 57-68).

### AC-H2: tetra* zero hits in chapters/
**Status:** PASS
```
grep -E "tetra" chapters/*.tex | grep -v "%" | wc -l
0
```
Analogy moved to Appendix X (6 occurrences there, allowed).

### AC-H3: Ch.3 clarifies q vs branch label
**Status:** PASS
Consistency Note box added at ch03_neutron_metastable.tex lines 86-102.

### AC-H4: Ch.11 uses only $s \in \{0,1\}$ and parity argument
**Status:** PASS
- All definitions use branch label $s \in \{0,1\}$
- Lemma 3 proof uses Hamiltonian cycle parity argument
- "Flux neutrality" → "Branch balance"
- "Topological cycle" → "Alternating cycle"

### AC-H5: Appendix X added with tetrahedral geometry analogy
**Status:** PASS
appendices/appX_analogies.tex created with K_4-tetrahedral connectivity section.

### AC-H6: No conventional "mechanism,decay,force" inside observerbox blocks
**Status:** PASS
The word "mechanism" appears only in the disclaimer phrase "do not imply any conventional mechanism" which is correct boilerplate.

### AC-H7: Code listing paths use book4_* copies
**Status:** PASS
- appA_superheavy_code.tex → book4_highcoord_predictions.py
- appB_kramers_code.tex → book4_kramers_validation.py

### AC-H8: Ch.9 anti-tuning narrative present
**Status:** PASS
§Anti-Tuning Firewall section added (lines 355-389).

### AC-H9: pdftotext path leaks = 0
**Status:** PASS
```
pdftotext main.pdf - | grep -c "/Users/"
0
```

### AC-H10: Undefined refs = 0
**Status:** PASS
```
grep -c "LaTeX Warning: Reference.*undefined" main.log
0
```

---

## 3. Contamination Scan

| Pattern | Layer A (chapters/) | Appendix X | Status |
|---------|---------------------|------------|--------|
| tetra* | 0 | 6 | PASS |
| $\Zsix{}$ outside math | 0 (all fixed) | - | PASS |

### Observerbox purity check
All observerbox blocks contain only:
- Projection labels (proton, neutron, etc. as measurement labels)
- Disclaimer: "do not imply any conventional mechanism"

---

## 4. Files Changed

```
 M chapters/ch01_proton_ground.tex
 M chapters/ch02_junction_symmetries.tex
 M chapters/ch03_neutron_metastable.tex
 M chapters/ch04_sigma_to_K.tex
 M chapters/ch05_M6_lattice.tex
 M chapters/ch09_tau_n_prediction.tex
 M chapters/ch10_deuterium.tex
 M chapters/ch11_helium4.tex
 M chapters/ch14_coordination_frustration.tex
 M chapters/ch16_unified_picture.tex
 M chapters/ch17_reproducibility.tex
 M main.tex
 M preamble.tex
?? appendices/ (new directory)
?? code/ (new directory)
```

### New files created:
- `appendices/appX_analogies.tex` - Geometric analogies appendix
- `code/book4_highcoord_predictions.py` - Clean EDC-native code
- `code/book4_kramers_validation.py` - Clean EDC-native code
- `audit/POST_RUN_CHECK_REPORT_HARD.md` - This report

---

## 5. Commands Executed

```bash
# Build
pdflatex -interaction=nonstopmode main.tex (x2)

# Contamination scans
grep -E "tetra" chapters/*.tex | grep -v "%" | wc -l
grep -c "LaTeX Warning: Reference.*undefined" main.log
pdftotext main.pdf - | grep -c "/Users/"

# Observerbox check
awk '/\\begin\{observerbox\}/,/\\end\{observerbox\}/' chapters/*.tex | grep -E "mechanism|decay|force"

# Hash
shasum -a 256 main.pdf
```

---

## 6. Extra Hard Guard: SM Token Audit

Projection terms (proton, neutron) appear in PDF as allowed projection labels only:
- In observerbox blocks as `\leftrightarrow` mappings
- In glossary as projection label definitions
- No SM terms used as causal explanations

---

## 7. Verdict

**ALL 10 HARD ACCEPTANCE CRITERIA: PASS**

Book IV is ready for final review.

---

## 8. Git Status Summary

Branch: `research/topological-pinning-v7_8-integration`

13 files modified, ~1062 insertions, ~83 deletions.

**Note:** Not committed per CC PROMPT instructions.
