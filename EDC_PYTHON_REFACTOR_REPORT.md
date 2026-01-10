# Python refactor report (EDC epistemic separation)

Date: 2026-01-09

Repository URL: https://github.com/igorgrcman/elastic-diffusive-cosmology

## What changed
- Introduced a small Python package under `code/src/edc/` with:
  - `edc/epistemic.py` — canonical epistemic labels (`DERIVED/IDENTIFIED/CALIBRATED/PROPOSED/BASELINE`)
  - `edc/constants/` — split constant stores:
    - `codata_baseline.py` (BASELINE)
    - `edc_validated.py` (empty placeholder; add only when truly derived)
    - `proposed.py` (PROPOSED model parameters, explicit)
  - `edc/constants/registry.py` — **strict** accessor: every constant fetch requires `allow={...}`.

- Moved runnable scripts to `code/scripts/` and refactored them to fetch constants only via `get_constant(...)`.
- Removed `scipy.constants` imports to prevent silent baseline injection.
- Enforced English-only comments by removing any comment lines containing Croatian diacritics.

## Guardrail policy
If a script needs a CODATA/IAU number, it must call:
`get_constant("c", allow={"BASELINE"}).value`
so the usage is explicit and reviewable.

## Notes / Warnings
- edc_double_slit.py: WARNING: Croatian diacritics still present somewhere; please review manually.
- edc_double_slit2.py: WARNING: Croatian diacritics still present somewhere; please review manually.
- edc_galaxy_rotation.py: WARNING: Croatian diacritics still present somewhere; please review manually.
- edc_lensing.py: WARNING: Croatian diacritics still present somewhere; please review manually.
- edc_mercury_precession_simulator.py: WARNING: Croatian diacritics still present somewhere; please review manually.
