# Elastic Diffusive Cosmology — Code & Verification Toolkit

This folder contains the **EDC verification / demonstration toolkit** that accompanies the book (**v17.49**).
The code follows the project's epistemic standard: every computation must clearly label which inputs are:

- **BASELINE** (external reference values; e.g., CODATA / PDG / NIST),
- **PROPOSED** (EDC postulates / conjectured relations),
- **DERIVED** (mathematical consequences of stated assumptions),
- **IDENTIFIED** (a mapping/bridge between EDC objects and standard observables).

> Important: many scripts are **bridge-layer** checks (EDC mapping → known GR/QM expressions).  
> Passing such a check demonstrates **consistency**, not an independent prediction, unless the mapping and inputs are derived from EDC alone.

## Quick start (recommended)

From this `code/` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e .
```

Now you can run scripts:

```bash
python scripts/edc_constants.py
python scripts/edc_double_slit.py
python scripts/edc_entanglement.py
python scripts/edc_gravity_check.py
python scripts/edc_lensing.py
```

### Why `pip install -e .`?

The scripts import the local package `edc` from `src/`.  
If you run scripts without the virtual environment / editable install, you may get `ModuleNotFoundError: edc`.

## Where outputs go

- Plots and generated images are written to: `scripts/artifacts/`
- Some scripts also write intermediate files to: `output/` (if enabled)

## Scripts index

See **`scripts/README.md`** for per-script purpose, expected output, and example commands.

## Tests

Run unit tests from `code/`:

```bash
python -m unittest -v
```

## Contributing / adding scripts

If you add new scripts:

1. Put them under `scripts/` (or `scripts/experimental/` until audited).
2. Ensure **all comments and CLI text are in English**.
3. Add an epistemic header block (STATUS, inputs, and references).
4. Add at least one **unit test** for any non-trivial numerical function.
5. Update `scripts/README.md` with a short description and example command.

## Licensing / citations

- Keep baseline values and reference sources in `SOURCES.md`.
- When publishing results, cite the book and the baseline sources used by the specific script.
