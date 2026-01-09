# EDC Python Code (Reproducibility)

This folder contains small, self-contained scripts used to reproduce/illustrate EDC checks and figures.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python edc_double_slit.py
```

## Scripts
- `edc_constants.py` — constants/utility calculations (NumPy/Matplotlib)
- `edc_double_slit.py`, `edc_double_slit2.py` — double-slit interference simulations
- `edc_entanglement.py` — illustrative entanglement visualization
- `edc_galaxy_rotation.py` — rotation curve check
- `edc_gravity_check.py` — symbolic consistency checks (SymPy)
- `edc_lensing.py` — lensing check
- `edc_mercury_precession_simulator.py` — Mercury precession simulator (SciPy)

## Outputs
By default scripts may display plots or write files to the working directory.
Recommended: run from this folder and save generated figures under `code/output/` (gitignored).
