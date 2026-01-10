# EDC Rigor Standard (Golden Standard)

This document defines the **single canonical epistemic standard** for Elastic Diffusive Cosmology (EDC).  
Goal: eliminate ambiguity and prevent overclaiming.

## 1) Two-layer labeling (MANDATORY)

Every non-trivial statement must carry:

### A) Evidence Status (one of four)
- **DERIVED** — obtained by explicit derivation from stated postulates + established mathematics, with regime/assumptions stated.
- **IDENTIFIED** — a motivated mapping between EDC parameters and observed quantities (not unique). Requires a note about non-uniqueness and what would make it falsifiable.
- **CALIBRATED** — a parameter fixed directly by observation/measurement (declared as input).
- **PROPOSED** — an unproven assumption, conjecture, interpretive claim, or placeholder awaiting derivation/test.

### B) Role Tag (optional but recommended)
- **POSTULATE** — foundational assumption (usually **PROPOSED**).
- **MATHEMATICS** — standard theorem/identity used (does not claim novelty).
- **RECOVERED** — a **DERIVED** result that matches known physics in a stated limit.
- **PREDICTION** — a **DERIVED** output that was not used as input/calibration.
- **CONJECTURE** — a **PROPOSED** claim with plausibility arguments but no derivation.
- **PLACEHOLDER** — explicitly incomplete content.

**Rule:** Evidence Status is primary. Role Tag is secondary.

---

## 2) Hard rules (NO EXCEPTIONS)

1. **No dual meanings for the same letter.**  
   If shorthand codes are used in tables, they must map uniquely to the four statuses.

2. **No checkmarks / “exact” / “verified” for non-DERIVED items.**  
   Numerical agreement without derivation is **PROPOSED (empirical target)**, not verified.

3. **No “derived” without a derivation pointer.**  
   A DERIVED statement must cite where it is derived (chapter/section/equation range) and under what regime.

4. **No hiding inputs.**  
   Any use of observed constants inside a “derivation” must be declared as IDENTIFIED or CALIBRATED.

5. **Every claim declares its regime.**  
   Examples: stiff-membrane limit, weak-field limit, low-energy limit, Rξ constant, etc.

---

## 3) Upgrade criteria (how claims move upward)

### PROPOSED → DERIVED
Requires:
- Explicit mathematical derivation steps,
- Clear assumptions and regime,
- Dimensional consistency,
- Reproducible numerical check (if numeric claim).

### PROPOSED → IDENTIFIED
Requires:
- Mapping rationale,
- Statement of non-uniqueness,
- A falsifiability path (what measurement/constraint would rule it out).

### PROPOSED → CALIBRATED
Requires:
- A declared dataset/measurement used as input,
- Uncertainty (if meaningful),
- Confirmation that the calibrated value is not later “predicted”.

### IDENTIFIED/CALIBRATED → PREDICTION
Requires:
- Output computed without using that output as an input,
- Sensitivity analysis (at least basic),
- Explicit note of what would falsify it.

---

## 4) Canonical location in the book

- The **only** canonical definition of the epistemic scheme should live in a single place (recommended: §3.5).
- Appendices and other chapters must **reference** that scheme, not redefine it.

---

## 5) Recommended table format (book + papers)

| ID | Statement | Evidence Status | Role | From / Pointer | Regime | Notes |
|---:|---|---|---|---|---|---|

Shorthand (allowed):
- **D** = DERIVED
- **I** = IDENTIFIED
- **Cal** = CALIBRATED
- **P** = PROPOSED

Avoid using **C** (too collision-prone).

---

## 6) Immediate known inconsistency to fix in v17.49

In v17.48:
- §3.5 defines **C = Calibration** and **Pr = Prediction**.
- Appendix C defines **C = Conjecture** and lacks Pr.

Fix:
- Make §3.5 the canonical legend.
- Update Appendix C to reference §3.5 and replace “C = Conjecture” with **PROPOSED** (Role: CONJECTURE).
