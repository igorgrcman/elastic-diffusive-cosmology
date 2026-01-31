# Donor Hunt Pass 2 — Systematic Repo-Wide Search

**Date:** 2026-01-31
**Branch:** audit/gap-register-full-v1
**Mode:** Critique/Report Only (no patches)

---

## Executive Summary

| Status | Count | Percentage |
|--------|-------|------------|
| FOUND (HIGH confidence) | 9 | 53% |
| FOUND (MED confidence) | 3 | 18% |
| PARTIAL (LOW confidence) | 3 | 18% |
| NO_MATCH | 2 | 12% |
| **Total** | **17** | 100% |

### Top 5 HIGH-Confidence Donors (Ready for Backfill)

1. **GAP-10** → `src/sections/11_gf_derivation.tex:162-331` (G_F chain)
2. **GAP-12** → `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex:136-405` (M_W derivation)
3. **GAP-1** → `src/sections/09_va_structure.tex:365-1030` (V−A emergence)
4. **GAP-8** → `src/sections/07_ckm_cp.tex:52-99` (CKM overlap)
5. **GAP-7** → `src/sections/05_three_generations.tex:40-100` (Z₃ generations)

---

## CRITICAL GAPS (4)

### GAP-10 — G_F Reduction Chain Steps 2-3
**Target (145):** `part3/chapter_12_gf_chain.tex:40`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/11_gf_derivation.tex:162-331`

**Patterns used:**
- "G_F" near "chain" OR "reduction"
- "g_5" and "g_4"
- "Fermi" formula

**Matches:**
- [HIGH] `11_gf_derivation.tex:162-176` — Fermi constant baseline with $G_F = 1.166 \times 10^{-5}$ GeV$^{-2}$
- [HIGH] `11_gf_derivation.tex:185-220` — Mediator integration and tree-level coupling
- [HIGH] `11_gf_derivation.tex:250-265` — Effective coupling formula $G_{EDC} \sim g_{eff}^2/m_\phi^2$
- [HIGH] `11_gf_derivation.tex:275-331` — Derivation chain with self-consistency caveat

**Snippet:**
```latex
% Lines 250-265 (approx)
\textbf{Effective contact strength:}
\begin{equation}
G_{EDC} = \frac{g_{eff}^2}{m_\phi^2} \sim \frac{g_4^2}{M_W^2}
\end{equation}
where $g_{eff}$ emerges from 5D → 4D reduction...
```

**SM-language risk:** YES (Fermi coupling terminology)
**Dictionary box needed:** YES

---

### GAP-12 — M_W Derivation from 5D
**Target (145):** `part3/chapter_15_mw_gf.tex:1`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex:136-405`

**Patterns used:**
- "M_W" near "brane" OR "thickness"
- "eigenvalue" near "gauge"
- "Robin" OR "BVP"

**Matches:**
- [HIGH] `ch18_opr20_mediator_mass_from_eigenvalue.tex:136-163` — Sturm-Liouville operator, Schrödinger form
- [HIGH] `ch18_opr20_mediator_mass_from_eigenvalue.tex:246-266` — Dimensionless eigenvalue $x_n := m_n \ell$
- [HIGH] `ch18_opr20_mediator_mass_from_eigenvalue.tex:295-305` — Mediator mass $m_{med} := m_1 = x_1/\ell$
- [HIGH] `ch18_opr20_mediator_mass_from_eigenvalue.tex:379-405` — Effective contact strength $C_{eff} = g_5^2 \ell / x_1^2$

**Snippet:**
```latex
% Lines 295-305
\textbf{Mediator mass definition:}
\begin{equation}
m_{\text{med}} := m_1 = \frac{x_1}{\ell}
\end{equation}
This is the first massive mode above the zero mode...
```

**SM-language risk:** NO
**Dictionary box needed:** YES

---

### GAP-7 — Z₃ → Three Generations
**Target (145):** `part2/chapter_08_generations.tex:29`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/05_three_generations.tex:40-100`

**Patterns used:**
- "three generations" OR "generation truncation"
- "Z_3" near "mode"
- "n = 0, 1, 2"

**Matches:**
- [HIGH] `05_three_generations.tex:1-27` — Epistemic status (HIGH RISK; [I] identification)
- [HIGH] `05_three_generations.tex:40-47` — Z₆ = Z₂ × Z₃ factorization
- [HIGH] `05_three_generations.tex:55-97` — Physical process: hexagonal flux lattice, three channels
- [MED] `05_three_generations.tex:96` — "Why only three? That's the open question" (OPR-12)

**Snippet:**
```latex
% Lines 55-70 (approx)
\textbf{Physical picture:}
The hexagonal flux lattice admits $\mathbb{Z}_6 = \mathbb{Z}_2 \times \mathbb{Z}_3$
symmetry. The $\mathbb{Z}_3$ factor partitions angular space into three sectors...
```

**SM-language risk:** NO
**Dictionary box needed:** YES (Z₃ → generation count is [I])

---

### GAP-16 — SU(3) Ontological Derivation
**Target (145):** `part1/chapter_02_ontology.tex:148`
**Status:** PARTIAL
**Confidence:** MED

**Best donor:** Requires Part I material (not in Part II src)

**Patterns used:**
- "SU(3)" near "junction"
- "Y-junction" OR "three-armed"
- "Lie algebra" near "color"

**Matches:**
- [MED] `src/Z6_content_full.tex` — Z₆ group structure found, but not explicit SU(3) derivation
- [LOW] `src/aside_m5_to_z6_proof/M5_TO_Z6_PROOF.md` — Related symmetry proof

**Next search suggestions:**
1. Check `edc_papers/paper_*` directories for Part I content
2. Search for "Y-junction" in entire repo
3. Look for "S^3 × S^3 × S^3" topology discussion

**SM-language risk:** YES (SU(3) color)
**Dictionary box needed:** YES

---

## HIGH PRIORITY GAPS (4)

### GAP-1 — V−A Structure Emergence
**Target (145):** `part2/chapter_10_va_structure.tex:20`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/09_va_structure.tex:365-1030`

**Patterns used:**
- "Jackiw" OR "Rebbi" OR "domain wall"
- "V-A" OR "chiral selection"
- "(1 - γ^5)"

**Matches:**
- [HIGH] `09_va_structure.tex:365-366` — Jackiw-Rebbi-Kaplan mechanism citation
- [HIGH] `09_va_structure.tex:374-375` — "Sign of mass profile determines chirality"
- [HIGH] `09_va_structure.tex:963-1030` — Full V−A structure derivation

**Snippet:**
```latex
% Lines 365-375
The Jackiw–Rebbi–Kaplan mechanism: localization of chiral fermions
at domain walls is a mathematical consequence of the 5D Dirac equation
with a sign-changing mass term.
\textbf{The sign of the mass profile determines chirality selection.}
```

**SM-language risk:** YES (chirality terminology)
**Dictionary box needed:** YES

---

### GAP-3 — Barrier Parameter μ Origin
**Target (145):** `part2/chapter_10_va_structure.tex:668`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/09_va_structure.tex:516-521` + `11_gf_derivation.tex`

**Patterns used:**
- "barrier" near "μ"
- "exponential suppression" near "localization"

**Matches:**
- [HIGH] `09_va_structure.tex:518-519` — $m_0 \sim 200$ MeV, suppression factor $e^{-m_0\lambda} \sim 0.37$
- [HIGH] Implicit: $(0.37)^4 \approx 0.02$ (50-fold suppression for $|f|^4$ overlap)

**SM-language risk:** YES
**Dictionary box needed:** YES (μ may be [Cal])

---

### GAP-5 — Plenum Definition
**Target (145):** `part2/chapter_10_va_structure.tex:15`
**Status:** FOUND
**Confidence:** MED

**Best donor:** `src/sections/09_va_structure.tex:37,55` + `src/Z6_content_full.tex:278,293`

**Patterns used:**
- "Plenum" (case insensitive)
- "diffuse field" OR "background scalar"
- "inflow"

**Matches:**
- [MED] `09_va_structure.tex:37` — "Plenum inflow creates directional mass gradient"
- [MED] `09_va_structure.tex:55` — "sign-changing mass term—induced by Plenum inflow—acts as chirality filter"
- [MED] `Z6_content_full.tex:278` — "In EDC, the bulk (5D) contains Plenum energy"
- [MED] `Z6_content_full.tex:293` — "Plenum inflow creates pressure..."

**SM-language risk:** NO (neologism)
**Dictionary box needed:** YES

---

### GAP-8 — CKM Overlap Derivation
**Target (145):** `part2/chapter_11_ckm.tex:261`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/07_ckm_cp.tex:52-99`

**Patterns used:**
- "CKM" near "overlap"
- "Δξ" OR "Wolfenstein"
- "V_{us}" OR "V_{cb}"

**Matches:**
- [HIGH] `07_ckm_cp.tex:52-79` — Physical process: generation separation, overlap integrals
- [HIGH] `07_ckm_cp.tex:63` — $V_{ij} \propto \int f_i^{(u)}(\xi) f_j^{(d)}(\xi) d\xi$
- [HIGH] `07_ckm_cp.tex:67-68` — $|V_{ij}| \sim e^{-|\xi_i - \xi_j|/2\kappa}$

**Snippet:**
```latex
% Lines 63-68
\begin{equation}
V_{ij} \propto \int f_i^{(u)}(\xi) f_j^{(d)}(\xi) d\xi
\end{equation}
Off-diagonal overlaps are exponentially suppressed:
$|V_{ij}| \sim e^{-|\xi_i - \xi_j|/2\kappa}$
```

**SM-language risk:** NO
**Dictionary box needed:** NO (existing [Cal] disclosure)

---

## MEDIUM PRIORITY GAPS (9)

### GAP-2 — Zero-Mode Selection
**Target (145):** `part2/chapter_10_va_structure.tex:321`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex:273-323`

**Snippet:**
```latex
% Lines 284-290
This is the massless zero mode ($m_0 = 0$, $\lambda_0 = 0$).
Physical interpretation: photon remains massless...
```

---

### GAP-6 — BC Normalizability
**Target (145):** `part2/chapter_10_va_structure.tex:938`
**Status:** FOUND
**Confidence:** MED

**Best donor:** `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex:169-241`

**Note:** Implicit in Sturm-Liouville formulation via L² inner product.

---

### GAP-9 — Neutrino Counting (LEP)
**Target (145):** `part2/chapter_09_neutrinos.tex:152`
**Status:** PARTIAL
**Confidence:** LOW

**Best donor:** Needs secondary search in `sections/10_case_neutrino.tex`

**Next search suggestions:**
1. Search `sections/10_case_neutrino.tex` explicitly
2. Grep for "2.984" or "invisible width"

---

### GAP-13 — RG Running Context
**Target (145):** `part3/chapter_15_mw_gf.tex:134`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/11_gf_derivation.tex:116,280-320`

**Snippet:**
```latex
% Line 116
Standard physics step [BL]: RG running from lattice scale to M_Z
using known beta functions
% Lines 319-320
After RG running, this gives sin²θ_W(M_Z) = 0.2314...
```

---

### GAP-14 — Kink Model Definition
**Target (145):** `part3/chapter_13_foundation_params.tex:162`
**Status:** NO_MATCH
**Confidence:** LOW

**Note:** No explicit kink/soliton/tanh derivation found in expected donor `CH3_electroweak_parameters.tex`. Profile shape is [P], not derived.

**Next search suggestions:**
1. Check `derivations/` subdirectory
2. Search for "tanh" in entire repo
3. May require original writing

---

### GAP-15 — Frozen Regime Superselection
**Target (145):** `part1/chapter_03_frozen.tex:113`
**Status:** PARTIAL
**Confidence:** MED

**Best donor:** `src/sections/02_frozen_regime_foundations.tex:27-68`

**Snippet:**
```latex
% Lines 53-61
Topological argument: Step functions are topologically protected
from continuous deformation...
```

**Note:** Covers stability/topological protection but not explicit "superselection" or "Γ → 0" mechanism.

---

### GAP-17 — CKM Calibration Procedure
**Target (145):** `part2/chapter_11_ckm.tex:264`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/07_ckm_cp.tex:52-78`

---

### GAP-19 — Normalization Propagation
**Target (145):** `part3/chapter_13_foundation_params.tex:292`
**Status:** FOUND
**Confidence:** HIGH

**Best donor:** `src/sections/ch17_opr19_g5_from_action.tex:20-80`

---

### GAP-20 — Part I→II Transition
**Target (145):** `bridge/chapter_0_bridge.tex:42`
**Status:** PARTIAL
**Confidence:** LOW

**Best donor:** `src/sections/02_frozen_regime_foundations.tex:27-70`

**Note:** Some dependency statements exist but no systematic Part I→II transition. Likely needs structural addition.

---

## Primary Donor Files Summary

| File | Gaps Covered | Lines |
|------|-------------|-------|
| `src/sections/11_gf_derivation.tex` | GAP-10, GAP-3, GAP-13 | 650 |
| `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex` | GAP-12, GAP-2, GAP-6 | 545 |
| `src/sections/09_va_structure.tex` | GAP-1, GAP-3, GAP-5 | 1183 |
| `src/sections/07_ckm_cp.tex` | GAP-8, GAP-17 | 1100 |
| `src/sections/05_three_generations.tex` | GAP-7 | 596 |
| `src/sections/ch17_opr19_g5_from_action.tex` | GAP-19 | 400+ |
| `src/Z6_content_full.tex` | GAP-5 (partial) | 2000+ |
| `src/sections/02_frozen_regime_foundations.tex` | GAP-15, GAP-20 (partial) | 200+ |

---

## Gaps Requiring Secondary Search

| GAP-ID | Reason | Suggested Action |
|--------|--------|------------------|
| GAP-9 | LEP neutrino counting not found | Search `10_case_neutrino.tex` |
| GAP-14 | Kink/soliton profile not found | Check `derivations/` or write original |
| GAP-16 | SU(3) ontology needs Part I | Search `edc_papers/` for Part I |
| GAP-20 | Structural content needed | May need original writing |

---

*Generated: 2026-01-31 | Branch: audit/gap-register-full-v1 | Mode: Critique only*
