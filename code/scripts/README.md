# Scripts — how to run and what to expect

All scripts are designed to be run from the `code/` folder **after** installing the package in editable mode:

```bash
cd code
source .venv/bin/activate
pip install -e .
```

Outputs (plots/images) go to: `scripts/artifacts/`

## Overview (current mainline scripts)

### `edc_constants.py`
Compares selected **EDC proposed relations** to **baseline reference values** (for comparison only).

Run:
```bash
python scripts/edc_constants.py
```

Expected:
- Console report with relative errors
- Plot saved into `scripts/artifacts/`

---

### `edc_double_slit.py` / `edc_double_slit2.py`
Double-slit visualization demos (pilot-wave style illustration).

Run:
```bash
python scripts/edc_double_slit.py
python scripts/edc_double_slit2.py
```

Expected:
- A wave-field visualization
- A detector histogram style plot

Notes:
- These are **illustrative demos**, not a quantitative fit to a specific experimental apparatus.

---

### `edc_entanglement.py`
Entanglement visualization demo (membrane projection vs bulk shortcut, illustrative).

Run:
```bash
python scripts/edc_entanglement.py
```

Expected:
- A visible illustration (static or simple animation), saved into `scripts/artifacts/`

---

### `edc_gravity_check.py`
Symbolic sanity-check that the Schwarzschild metric is a vacuum solution (Einstein tensor → 0).

Run:
```bash
python scripts/edc_gravity_check.py
```

Expected:
- Console output showing non-zero symbolic components for generic A(r), B(r)
- A PASS check for the Schwarzschild specialization

Epistemic note:
- This checks GR-consistency of the symbolic machinery; it does **not** derive gravity from EDC.

---

### `edc_lensing.py`
Lensing visualization demo.  
Two modes may exist depending on the branch/version:
- **demo** (exaggerated / illustrative)
- **physical** (weak-field scaling; may look subtle for small masses/FOVs)

Run:
```bash
python scripts/edc_lensing.py --help
python scripts/edc_lensing.py --mode demo
python scripts/edc_lensing.py --mode physical --mass 1.98847e30 --Dl 1 --Ds 2 --units Mpc --fov 2
```

Expected:
- `scripts/artifacts/edc_lensing_output.png`

Tip:
- If the physical mode looks “too small”, increase mass, distances, or adjust FOV/pixel scaling.

---

## About “versioned” scripts (e.g., `_v17.49.020.py`)

For public clarity, the repo should ideally keep **one canonical script name** per topic (e.g., `edc_mercury_precession.py`),
and move older point-in-time snapshots into an archive folder such as:

- `scripts/archive/v17.49/`

If you currently maintain many snapshots locally, you can add them under `scripts/archive/` with a short changelog.

## Adding your extra local scripts

If your local repo contains additional scripts not yet merged:

1. Place them under `scripts/experimental/` first.
2. Ensure English-only comments / output.
3. Add an epistemic header and list baseline sources (if any).
4. Add minimal tests under `tests/` for core calculations.
5. Once audited, promote the script into `scripts/` and document it here.

