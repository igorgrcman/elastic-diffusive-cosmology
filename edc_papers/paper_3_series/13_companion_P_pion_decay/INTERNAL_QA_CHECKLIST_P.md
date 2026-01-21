# Internal QA Checklist: Companion P (Pion)

**Date:** 2026-01-20
**Version:** v0.3 (internal QA hardened)
**Protocol:** EDC Internal Consistency Audit

---

## Core Guardrails

- [x] **Ontology tagged [P] only** — Pion ontology is explicitly postulated, not derived
- [x] **Helicity suppression treated as [BL]** — $m_\ell^2$ scaling accepted from SM/PDG
- [x] **No mass derivation** — $m_\pi = 140$ MeV flagged [OPEN], not claimed
- [x] **No lifetime derivation** — $\tau_\pi = 26$ ns flagged [OPEN], not claimed
- [x] **No BR derivation** — Branching ratios are [BL], not fitted

---

## Canon Compliance

- [x] **Absorption/Dissipation/Release vocabulary used** — Same triad as N/M/T
- [x] **No forbidden synonyms** — No "conversion", "creation from nothing", etc.
- [x] **Ledger conservation stated** — Energy bookkeeping table added
- [x] **Bulk leakage = "suppressed"** — Not "cannot escape"

---

## Epistemic Hygiene

- [x] **Epistemic Status table present** — Table 2 lists [BL], [P], [OPEN] claims
- [x] **All postulates tagged** — Postulate 1 (ontology), Postulate 2 (projection), Postulate 3 (metastability)
- [x] **All open problems flagged** — §9 lists 6 [OPEN] items
- [x] **Scope guardrail box present** — §1.2 declares consistency/ontology scope

---

## Physical Narration

- [x] **§2 Ontology** — 5D cause / Brane response / 3D output present
- [x] **§5 Helicity** — Physical narration for projection mechanism
- [x] **§6 Stability** — Physical narration for metastability

---

## Falsifiability

- [x] **6 falsifiability bullets** — §8 lists structural failure conditions
- [x] **Ontology falsifiable** — "If bulk-dominant, ontology fails"
- [x] **Pipeline falsifiable** — "If different mechanism needed, framework fails"
- [x] **Selection rules falsifiable** — "If forbidden channels dominate, rules fail"
- [x] **Helicity falsifiable** — "If P_chir predicts e > μ, mechanism fails"
- [x] **Ledger falsifiable** — "If energy doesn't close, conservation fails"
- [x] **Universality falsifiable** — "If different filter needed, hypothesis fails"
- [x] **"No immunity" guardrail box** — Explicit statement of falsifiability

---

## Anti-Overclaim List

The following are **explicitly NOT claimed** in Companion P:

1. Derivation of $m_\pi$ from first principles
2. Derivation of $\tau_\pi$ from first principles
3. Derivation of $m_\ell^2$ helicity suppression factor
4. Derivation of BR($\mu$)/BR($e$) ratio
5. Explanation of quark confinement in 5D
6. Junction-pair as proven (only candidate)
7. Photon ontology (deferred)
8. Any numerical fits or parameter tuning

---

## Build Verification

```bash
cd edc_papers/paper_3_series/13_companion_P_pion_decay/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Expected: No errors, no undefined references
```

---

## Verdict

**PASS** — Companion P v0.3 satisfies all internal QA audit requirements.

This document follows the EDC no-fit policy and has been internally audited for
dimensional consistency, epistemic tagging, and non-overclaim language.

---

*Generated: 2026-01-20 (internal QA pass)*
