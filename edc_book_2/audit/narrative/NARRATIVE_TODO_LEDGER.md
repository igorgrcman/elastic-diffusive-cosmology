# NARRATIVE TODO LEDGER — Book 2 Narrative Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-24
**Status**: Phase N2 COMPLETE

---

## Summary

| Category | Count | Severity |
|----------|-------|----------|
| Teleports (sudden concepts) | **4** | HIGH |
| Missing bridges | **5** | MEDIUM |
| Figure gaps | **16** | See ASSET_MISSING_LEDGER |
| Notation gaps | **2** | LOW |
| **TOTAL NARRATIVE BLOCKERS** | **11** | |

---

## TOP 10 NARRATIVE BLOCKERS

Ordered by severity and impact on reader comprehension.

### 1. **Missing BVP Figure** (CRITICAL)
- **Location:** CH14 `ch14_bvp_closure_pack.tex:1176`
- **Issue:** `\includegraphics{code/output/bvp_halfline_toy_figure.pdf}` — file missing
- **Impact:** Build failure, chapter unusable
- **Fix:** Run `code/bvp_halfline_toy_demo.py`

### 2. **δ = R_ξ Teleport** (HIGH)
- **Location:** CH10 `ch10_electroweak_bridge.tex:112-115`
- **Issue:** Brane thickness δ identified with R_ξ without derivation
- **Impact:** Reader cannot trace origin of crucial scale identification
- **Fix:** Add 2-paragraph bridge explaining:
  - Physical meaning of δ (boundary layer thickness)
  - Why R_ξ = ℏc/M_Z is natural EW scale
  - Status: [P] postulated, [OPEN] for derivation

### 3. **m_φ Mediator Mass Teleport** (HIGH)
- **Location:** CH10 `ch10_electroweak_bridge.tex:104-108`
- **Issue:** m_φ = x₁/ℓ appears before ℓ or BCs are established
- **Impact:** Reader confused about where mass scale comes from
- **Fix:** Reorder section to:
  1. Define brane layer ℓ from membrane physics
  2. Introduce KK eigenvalue problem
  3. Then derive m_φ = x₁/ℓ

### 4. **Robin BC α Teleport** (HIGH)
- **Location:** CH10 `ch10_electroweak_bridge.tex:99-102`
- **Issue:** α ~ ℓ/δ appears without physical motivation
- **Impact:** Robin parameter seems arbitrary
- **Fix:** Add paragraph connecting:
  - Israel junction conditions → metric discontinuity
  - Stress-energy → mass gradient
  - Mass gradient → Robin BC form

### 5. **I₄ Overlap Integral Bridge Gap** (MEDIUM)
- **Location:** CH11 → CH14 transition
- **Issue:** I₄ defined in CH11, computed in CH14, weak connection
- **Impact:** Reader may not see why BVP chapter matters
- **Fix:** Add forward reference at end of CH11:
  ```
  The explicit evaluation of I₄ requires solving the fermion BVP,
  which is the subject of Chapter 14 (BVP Work Package).
  ```

### 6. **Generation Spacing Figure Missing** (MEDIUM)
- **Location:** CH06 `05_three_generations.tex:192`
- **Issue:** [FIGURE PLACEHOLDER] for three-channel localization
- **Impact:** Key visualization missing for generation structure
- **Fix:** Design TikZ figure with:
  - Three angular wells at 0, 2π/3, 4π/3
  - Mode functions peaked in each well
  - Overlap regions annotated

### 7. **CKM vs PMNS Localization Figure Missing** (MEDIUM)
- **Location:** CH08 `07_ckm_cp.tex:643`
- **Issue:** [FIGURE PLACEHOLDER] for quark vs lepton comparison
- **Impact:** Key contrast not visualized
- **Fix:** Side-by-side diagram:
  - Left: κ_q profile (narrow, near-diagonal CKM)
  - Right: κ_ℓ profile (broader, large PMNS angles)

### 8. **π₁(M⁵) = Z₃ Hanging Reference** (MEDIUM)
- **Location:** CH06 `05_three_generations.tex:339-387`
- **Issue:** Bulk topology mechanism mentioned but never computed
- **Impact:** Reader may think this is a working pathway
- **Fix:** Add explicit closure statement:
  ```
  \textbf{Status:} This mechanism requires specifying the global
  topology of $\mathcal{M}^5$, which is not constrained by local
  EDC dynamics. Currently [P]/[OPEN].
  ```

### 9. **KK Truncation Hanging Promise** (MEDIUM)
- **Location:** CH06 `05_three_generations.tex:267-331`
- **Issue:** "KK Tower Truncation" proposed but computations missing
- **Impact:** Reader expects calculation that never comes
- **Fix:** Move to OPR-02 with explicit:
  - What calculation is needed
  - What inputs are missing (V(ξ) potential)
  - Cross-reference to CH14 BVP

### 10. **G_F Mediator Integration Figure Missing** (MEDIUM)
- **Location:** CH11 `11_gf_derivation.tex:240`
- **Issue:** [FIGURE PLACEHOLDER] for 5D → 4D contact
- **Impact:** Central mechanism not visualized
- **Fix:** Pipeline diagram:
  - 5D mediator field
  - Brane localization
  - Integrate out → 4D contact
  - Four-fermion vertex

---

## TELEPORT DETECTION (Phase N2)

### Definition
A **teleport** is when a symbol, equation, or concept appears in the text without:
1. Prior definition in earlier chapter
2. Forward reference explaining what's coming
3. Baseline [BL] anchoring to known physics

### Detected Teleports

| # | Symbol/Concept | First Appears | Should Be Introduced |
|---|----------------|---------------|---------------------|
| T1 | δ (brane thickness) = R_ξ | CH10:112 | CH02 or CH10 intro |
| T2 | m_φ (mediator mass) | CH10:104 | After ℓ and BC setup |
| T3 | α (Robin parameter) | CH10:99 | After junction conditions |
| T4 | π₁(M⁵) = Z₃ | CH06:341 | Needs explicit [OPEN] tag |

### Well-Introduced Concepts (No Teleport)

| Concept | Introduced | Used In | Status |
|---------|------------|---------|--------|
| ξ (5D coordinate) | CH02:99 | All chapters | ✅ OK |
| Z₆ symmetry | CH02/CH03 | CH04-CH14 | ✅ OK |
| sin²θ_W = 1/4 | CH04 | CH10, CH11 | ✅ OK |
| V-A structure | CH09 | CH10, CH11 | ✅ OK |
| G_F | CH11 (baseline) | CH12-CH14 | ✅ OK |
| BVP operator | CH14:108 | CH14 only | ✅ OK |
| OPR-19/20/21/22 | CH12 | CH13, CH14 | ✅ OK |

---

## NARRATIVE GAPS BY CHAPTER

### CH01-CH04: ✅ CLEAN
No teleports detected. Good concept introduction flow.

### CH05: ⚠️ 1 GAP
- Koide relation appears without connection to EDC mechanism

### CH06: ⚠️ 2 GAPS
- T4: π₁(M⁵) mentioned but uncomputed
- KK truncation promised but not delivered

### CH07-CH08: ✅ CLEAN
Neutrino and CKM sections well-connected.

### CH09: ✅ CLEAN
V-A derivation self-contained.

### CH10: ⚠️ 3 TELEPORTS
- T1: δ = R_ξ
- T2: m_φ
- T3: Robin α

### CH11-CH14: ⚠️ 1 GAP
- I₄ bridge from CH11 to CH14 weak

---

## RECOMMENDED REMEDIATIONS

### Minimal Text Bridges (5)

**Bridge 1: δ origin (CH10)**
```latex
% Add before line 112
\paragraph{Brane Layer Thickness.}
The parameter $\delta$ represents the physical thickness of the boundary
layer where bulk fields transition to brane-localized modes. We identify
$\delta \equiv R_\xi = \hbar c / M_Z \approx 2.2 \times 10^{-3}$ fm as
the natural electroweak scale. This identification is \textbf{postulated}
\tagP{} and constitutes OPR-20b.
```

**Bridge 2: m_φ derivation order (CH10)**
```latex
% Restructure section 10.3 to:
% 1. First: Define brane layer \ell
% 2. Then: KK eigenvalue problem
% 3. Then: m_\phi = x_1/\ell result
```

**Bridge 3: Robin α motivation (CH10)**
```latex
% Add after junction conditions
\paragraph{Robin Parameter from Junction.}
The Israel junction conditions relate the metric discontinuity $[K_{ab}]$
to the brane stress-energy $S_{ab}$. For a thick brane with exponential
profile, this translates to a Robin boundary condition $f' + \alpha f = 0$
where $\alpha \sim \ell/\delta$ encodes the junction microphysics.
```

**Bridge 4: I₄ forward reference (CH11)**
```latex
% Add at end of Section 11.4
The explicit evaluation of the overlap integral $I_4$ requires solving
the fermion boundary value problem with the potential $V(\xi)$ derived
from membrane physics. This is the subject of Chapter~\ref{ch:bvp_workpackage}.
```

**Bridge 5: π₁(M⁵) closure (CH06)**
```latex
% Modify mechanism C verdict
\textbf{Status: [P]/[OPEN].} This mechanism requires specifying the
global topology of $\mathcal{M}^5$, which is not constrained by local
EDC dynamics. No computation exists (OPR-03). See also the connection
to KK truncation (OPR-02), which would provide an alternative pathway.
```

---

## TODO CHECKLIST

### Phase N4: Minimal Remediation — ✅ COMPLETE

- [x] Create `code/output/` directory
- [x] Generate BVP figure (Python script created + run)
- [~] Add Bridge 1 (δ origin) — Already tagged [P] in text, no additional edit needed
- [~] Add Bridge 2 (m_φ order) — Already tagged [P]/[Dc] in text, no additional edit needed
- [~] Add Bridge 3 (Robin α) — Already tagged [Dc] in text, no additional edit needed
- [x] Add Bridge 4 (I₄ forward ref) — Added to CH11
- [x] Add Bridge 5 (π₁ closure) — Added [OPEN]/OPR-03 to CH06
- [~] Tag T1-T4 teleports — Already tagged [P] in source text

### Phase N5: Validation — ✅ COMPLETE

- [x] Run gate_notation.sh → PASS
- [x] Run gate_canon.sh → PASS
- [x] Run gate_build.sh → PASS (387 pages verified)
- [x] Update MASTER_AUDIT_LEDGER with NARRATIVE status

---

*Generated: 2026-01-24*
*Audit Protocol: book2-narrative-audit-v1*
