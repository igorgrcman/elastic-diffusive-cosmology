# V7.9 NARRATIVE MAP

**Created**: 2026-01-31
**Purpose**: Section-by-section outline of target document BEFORE and AFTER integration

---

## BEFORE: compile_topological_pinning.tex

### Current Structure (Wrapper Only)

```
Line 1-33:   Preamble (packages, setup)
Line 34-36: \maketitle
Line 38-40: Abstract (placeholder text mentioning key results)
Line 42-43: \tableofcontents
Line 46:    \input{BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex} ← FILE MISSING
Line 48:    \end{document}
```

**Issue**: The included file `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` does not exist.

### Abstract Claims (Line 39)

Current abstract mentions:
1. "neutron lifetime τ_n ≈ 880 s (<1% error)" — from M6 model
2. "He-4 binding energy 29 MeV (3% error)" — from M6 model
3. "Be-8 instability correctly predicted" — from M6 model
4. "allowed coordinations n = 2^a × 3^b with forbidden n = 43" — coordination law
5. "Frustration-Corrected Geiger-Nuttall Law for α-decay (R² = 0.9941, 44.7% improvement)" — from V7.x

**Note**: Abstract line 5 references V7.x results but the body content is missing.

---

## AFTER: Integrated Structure

### BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex (NEW FILE)

```
%========================================
% SECTION 1: INTRODUCTION AND M6 FOUNDATION
%========================================
1.1 What is M6? [from M6_TOPOLOGICAL_MODEL_EXPLORATION.md §1]
    - Three interpretations (graph, lattice, manifold)
    - Working definition: 6-coordinated graph in 5D
    - Why 6 neighbors (Z₆ symmetry)

1.2 The Toy Model Hamiltonian [from M6_TOPOLOGICAL_MODEL_EXPLORATION.md §2]
    - Variables: q_i deformation parameter
    - Single-cell potential V(q)
    - Pinning term H_pin

%========================================
% SECTION 2: FREE vs BOUND NEUTRON
%========================================
2.1 Free Neutron Analysis [from M6_TOPOLOGICAL_MODEL_EXPLORATION.md §3]
    - WKB tunneling rate
    - S_E/ℏ ≈ 60 → τ ≈ 880 s

2.2 Bound Neutron with 6 Neighbors [from M6_TOPOLOGICAL_MODEL_EXPLORATION.md §4]
    - Mean-field with correct pinning
    - Barrier enhancement → stability
    - K ≈ 1 MeV estimate

2.3 Summary Box [from M6_TOPOLOGICAL_MODEL_EXPLORATION.md §8]
    - Results table

%========================================
% SECTION 3: ALPHA-DECAY EMPIRICAL AUDIT (NEW)
%========================================
3.1 The Coordination Law Applied to Heavy Nuclei [NEW]
    - n(A) = 6.1 × A^(1/3) mapping
    - d(n) = distance to nearest allowed value
    - The forbidden zone [37, 47]

3.2 Regression Results [from V7.4, V7.8]
    - Model M2: g = -1.64 ± 0.14, p < 0.001 (V7.8)
    - Comparison with V7.4: g = -0.31 ± 0.11, p = 0.006
    - Note: Different d(n) scaling between versions

3.3 Sign Resolution: Prefactor not Barrier [from V7.6.1]
    - Sign paradox: higher d(n) → FASTER decay
    - Test T3: Additive model (prefactor) wins
    - Physical picture: frustration → S_α enhancement

3.4 Robustness Tests [from V7.5, V7.8]
    - Cross-validation (V7.5)
    - Permutation test (V7.5): p_perm < 0.001
    - Deformation proxy control (V7.8): absorbed by d(n)
    - S_α proxy control (V7.8): d(n) survives

3.5 Interpretation Box [NEW, sign-safe]
    - What we can claim [Der/I]
    - What remains hypothetical [P]
    - What we cannot claim

%========================================
% SECTION 4: FALSIFICATION FRAMEWORK
%========================================
4.1 Tests Already Passed [from V7.5, V7.8]
    - Robust regression
    - Permutation test
    - Cross-validation
    - Deformation control

4.2 Open Falsification Tests [from V7.7]
    - Independent S_α measurement
    - True β₂ deformation
    - Superheavy extension
    - Causal mechanism demonstration

%========================================
% SECTION 5: OPEN QUESTIONS
%========================================
5.1 Updated Kingpin Status [from V7.8]
    - Table: Kingpin | V7.8 Status | Priority

5.2 Path to [Der] Upgrade [from V7.8]
    - Checklist: 4/7 complete

%========================================
% APPENDIX: FORBIDDEN ALTERNATIVES MATRIX
%========================================
A.1 Mechanism × n Table [from V7.7]
    - M1 (domain), M2 (defect), M3 (cluster), M4 (metastable), M5 (quasi), M6 (core-mantle)
```

---

## Insertion Points Summary

| Section | Content Source | Epistemic Status |
|---------|----------------|------------------|
| 1.1-1.2 | M6_TOPOLOGICAL_MODEL_EXPLORATION.md §1-2 | [Der] for framework |
| 2.1-2.3 | M6_TOPOLOGICAL_MODEL_EXPLORATION.md §3-4, 8 | [Der] for calculation, [P] for K estimate |
| 3.1 | Coordination law definitions | [Der] |
| 3.2 | V7.4/V7.8 regression tables | [Der] |
| 3.3 | V7.6.1 sign resolution | [Der] |
| 3.4 | V7.5/V7.8 robustness | [Der] |
| 3.5 | Sign-safe interpretation | [I] with [P] mechanism |
| 4.1 | V7.5/V7.8 completed tests | [Der] |
| 4.2 | V7.7 falsification list | [P] |
| 5.1-5.2 | V7.8 kingpins | [Open] |
| A.1 | V7.7 forbidden matrix | [I]/[P] |

---

## Key Narrative Bridges

### Bridge A: M6 Theory → α-Decay Evidence

**Location**: End of Section 2, beginning of Section 3

**Narrative**:
> "The M6 model provides a framework for understanding how coordination number affects nuclear stability. In the preceding sections, we applied this to neutron lifetime in light nuclei. We now extend the analysis to α-decay in heavy nuclei (Z = 83–100), where the coordination distance d(n) can be tested against empirical half-life data."

### Bridge B: Evidence → Interpretation

**Location**: End of Section 3.4, beginning of Section 3.5

**Narrative**:
> "The statistical evidence establishes that d(n) correlates with α-decay rates beyond what Geiger-Nuttall predicts. The following interpretation box summarizes what we can and cannot conclude from this correlation."

### Bridge C: Interpretation → Falsification

**Location**: End of Section 3, beginning of Section 4

**Narrative**:
> "To upgrade the mechanistic interpretation from [P] to [Der], additional tests are required. The following falsification framework identifies which tests have passed and which remain open."

---

## Word Count Estimates

| Section | Estimated Words |
|---------|-----------------|
| 1. Introduction | 800 |
| 2. Free/Bound Neutron | 1200 |
| 3. α-Decay Audit | 1500 |
| 4. Falsification | 600 |
| 5. Open Questions | 400 |
| Appendix | 300 |
| **Total** | **~4800** |

---

## Sign-Safe Language Checklist

| Phrase | Safe? | Alternative if Unsafe |
|--------|-------|----------------------|
| "higher d(n) → faster decay" | ✓ | — |
| "frustration enhances preformation" | ✓ | — |
| "frustration impedes tunneling" | ✗ | "frustration correlates with shorter half-life" |
| "d(n) causes faster decay" | ✗ | "d(n) correlates with faster decay" |
| "proves topological mechanism" | ✗ | "consistent with topological mechanism" |
| "d(n) is not deformation" | ✓ | — |
| "S_α mediation confirmed" | ✗ | "consistent with S_α channel" |

