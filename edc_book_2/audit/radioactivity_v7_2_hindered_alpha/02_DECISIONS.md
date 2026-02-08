# DECISIONS LOG (V7.2)

**Created**: 2026-01-31
**Purpose**: Document methodological choices and their rationale

---

## D-001: Hindrance Classification Scheme

**Decision**: Use three-class system (H0, H1, H2) based on ΔJ and parity change.

**Rationale**:
- Continuous hindrance factors require spectroscopic data not available for all nuclides
- Three classes capture the main physical distinctions
- Consistent with nuclear physics literature conventions

**Definition**:
| Class | ΔJ | Parity Change | Physical Interpretation |
|-------|-----|---------------|------------------------|
| H0 | 0-2 | No | Favored (L=0 allowed for α) |
| H1 | 0-2 | Yes | First-forbidden equivalent |
| H2 | >2 | Any | Highly hindered |

**Registered**: 2026-01-31

---

## D-002: Include Sub-100% α-Branch Nuclides

**Decision**: Include At-211 (α=41.8%) and Cf-252 (α=96.9%) in dataset.

**Rationale**:
- These provide hindrance diversity (At-211 has EC competition)
- Use partial half-life: t₁/₂(α) = t₁/₂(total) / BR(α)
- Document this correction explicitly in dataset

**Impact**: Allows broader hindrance coverage at cost of slight model complexity.

**Registered**: 2026-01-31

---

## D-003: d(n) Mapping Model

**Decision**: Use n(A) = 6.1 × A^(1/3) with d(n) = |n(A) - n*|, n* = nearest in S.

**Rationale**:
- Consistent with V7/V7.1
- Calibrated to n(208) ≈ 36
- Alternative models (M-B, M-C) tested in sensitivity analysis

**Status**: [P] — This is a model assumption, not derived from BL.

**Registered**: 2026-01-31

---

## D-004: Regression Model Hierarchy

**Decision**: Test models in order: G-N → +Hindrance → +d(n) → +d(n)².

**Rationale**:
- Hierarchical approach allows isolating d(n) effect after structure control
- If d(n) is significant only without hindrance, it may be confounded
- Quadratic term tests for non-linear frustration effects

**Pre-registered analysis**:
1. Model 0: log₁₀(t₁/₂) = a(Z/√Qα) + b
2. Model 1: residual₀ ~ H1 + H2 (dummy coding, H0 = reference)
3. Model 2: residual₀ ~ H1 + H2 + d(n)
4. Model 3: residual₀ ~ H1 + H2 + d(n) + d(n)²

**Registered**: 2026-01-31

---

## D-005: Significance Threshold

**Decision**: Use α = 0.05 for primary inference; report p-values for all tests.

**Rationale**:
- Standard threshold in nuclear physics literature
- Sample size (N=32) provides moderate power
- Exploratory analysis allows p < 0.10 as "suggestive"

**Registered**: 2026-01-31

---

## D-006: Daughter Jπ Source Priority

**Decision**: For daughter Jπ, use ground state values from ENSDF adopted levels.

**Rationale**:
- Most α-decays populate ground state or low-lying excited states
- Ground-state-to-ground-state transition defines minimum ΔJ
- Decays to excited states would increase effective hindrance

**Limitation**: This is a lower bound on hindrance; actual may be higher.

**Registered**: 2026-01-31

---

## D-007: Target Switching Threshold

**Decision**: Define target switching at n(A) = (n₁ + n₂)/2 equidistant point.

**Rationale**:
- 36 ↔ 48: n = 42, A = 326
- 48 ↔ 54: n = 51, A = 587
- No nuclides in α32 are above A = 252, so all lock to n* = 36

**Registered**: 2026-01-31

---

## D-008: Handling Missing Daughter Jπ

**Decision**: If daughter Jπ is unknown, mark hindrance as [H?] and exclude from Model 1–3.

**Nuclides affected**: None in final dataset (all have BL Jπ).

**Registered**: 2026-01-31

---

## D-009: Partial Half-Life Correction

**Decision**: For nuclides with α-branch < 100%, compute t₁/₂(α) = t₁/₂(total) / BR(α).

**Applied to**:
| Nuclide | t₁/₂(total) | BR(α) | t₁/₂(α) |
|---------|-------------|-------|---------|
| At-211 | 7.214 h | 0.418 | 17.26 h |
| Cf-252 | 2.647 y | 0.969 | 2.73 y |
| Cm-248 | 3.48×10⁵ y | 0.916 | 3.80×10⁵ y |

**Rationale**: The G-N law applies to the α-decay channel specifically, not total decay.

**Registered**: 2026-01-31

---

## Hypothesis Registry

### H-V7.2-01: Hindrance-Corrected d(n) Effect [P]

**Statement**: After controlling for spin-parity hindrance class, d(n) shows a negative correlation with G-N residuals (more frustrated nuclei decay faster).

**Formulation**: In Model 2, coefficient g for d(n) is negative and significant.

**Falsification Test**: If g > 0 or p > 0.05, hypothesis is not supported.

**Status**: INCONCLUSIVE — g = -0.58, p = 0.11

---

### H-V7.2-02: Hindrance Dominates Over d(n) [I]

**Statement**: Hindrance class explains more variance in G-N residuals than d(n).

**Formulation**: ΔR² for Model 1 (adding hindrance) > ΔR² for adding d(n) to G-N alone.

**Falsification Test**: If d(n) alone has larger ΔR² than hindrance, hypothesis fails.

**Status**: SUPPORTED — Hindrance ΔR² ≈ 0.04, d(n) alone ΔR² ≈ 0.02

---

### H-V7.2-03: Non-linear d(n) Effect [P]

**Statement**: The d(n) effect is non-linear; quadratic term is significant.

**Formulation**: In Model 3, coefficient for d(n)² is significant.

**Falsification Test**: If p(d(n)²) > 0.05, no evidence for non-linearity.

**Status**: REJECTED — d(n)² coefficient not significant (p > 0.3)

