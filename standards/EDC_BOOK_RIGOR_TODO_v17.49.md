# EDC Book v17.49 Rigor To‑Do (Epistemic Unification)

Scope: **no new physics**; only unification of epistemic labeling + removal of contradictory legends and misleading status marks.

## GS-001 Unify epistemic legend (single source of truth)
- Keep §3.5 as the **only canonical** definition of epistemic status.
- Insert/`\input{EDC_EPISTEMIC_STANDARD.tex}` and reuse `\EDCLegendText` verbatim.
- Ban redefinitions elsewhere; other chapters/appendices must *reference* §3.5.

## GS-002 Eliminate "C" collision
Problem: `C` is used as **Calibration** in §3.5 but **Conjecture** in Appendix C and in the Conjectures table.

Fix:
- Evidence Status stays: **DERIVED / IDENTIFIED / CALIBRATED / PROPOSED**
- Treat "Conjecture" as: **PROPOSED** with Role Tag **CONJECTURE**.
- Avoid single-letter `C` outside §3.5 tables; prefer `Cal` for calibrated and `P` for proposed.

## GS-003 Repair duplicated/alternative classification in §7.9
Location: §7.9 defines a separate scheme (adds “Consistency check”) and omits D/M.

Fix:
- Replace the §7.9 bullet list with: “We use the canonical epistemic scheme from §3.5.”
- Add Role Tag **CONSISTENCY CHECK** for outputs that are not independent predictions (i.e., computed using calibrated/identified inputs).

## GS-004 Normalize Appendix C to reference §3.5 (no new categories)
Location: Appendix C intro defines its own categories and adds **R**.

Fix:
- Replace Appendix C legend with a reference sentence pointing to §3.5.
- Convert **R = Recovered Result** to Role Tag on **DERIVED** items (e.g., `DERIVED (RECOVERED)`).
- Add **Prediction** category back only as `DERIVED (PREDICTION)` if applicable.

## GS-005 Unify Foundational Postulates list (P1…Pn)
Problem: §3.5 has **P1–P6** (includes σ); Appendix C has **P1–P5** and changes content (ρ_Plenuм ~ ρ_Planck, C3 bundle).

Fix options (choose one and apply globally):
- **Option A (recommended):** Promote missing assumptions to the canonical postulates list:
  - Keep §3.5 P1–P6 unchanged,
  - Add new items as **P7, P8...** (clearly marked PROPOSED if not derivable).
- **Option B:** Demote non-foundational items to **PROPOSED (CONJECTURE)** with IDs `K1, K2...`, and remove them from the postulates list.

## GS-006 Tighten §3.5.3 “Identifications and Calibrations” table
- `I4: ħ = ħ_geom` is currently tautological/overstated: rephrase as a claim and mark **PROPOSED** unless independently derived.
- `C2: ρ_Plenuм ~ ρ_Planck`: if assumed, mark **PROPOSED (POSTULATE/CONJECTURE)**; if fit, mark **CALIBRATED** and state what it is fit to.

## GS-007 Fix Appendix C.5 “Conjectures” table (IDs + Status)
- Rename IDs from `C1…` to `K1…` (or `Conj1…`) to avoid confusion with Calibration.
- Status column should be **PROPOSED** (and optionally Role Tag: CONJECTURE / TESTABLE).
- Remove any ✓ / “Exact” language unless the item is DERIVED with a pointer.

## GS-008 Add a global “rigor lint” checklist before release
Before tagging v17.49:
- Global search: `C = Conjecture`, `Recovered Result`, `Consistency check` (as a category), `✓`, `exact`, `verified`.
- Ensure every **DERIVED** item has: pointer + regime + no hidden inputs.
- Ensure every **PREDICTION** is not used as input/calibration anywhere.

---

### Known concrete conflict locations (PDF v17.48)
- §3.5 legend: `C = Calibration`, `Pr = Prediction`
- §7.9: alternative epistemic scheme includes “Consistency check”
- Appendix C: `C = Conjecture`, `R = Recovered Result`
- Appendix C.5: Conjectures table uses `C` both as ID prefix and status code
