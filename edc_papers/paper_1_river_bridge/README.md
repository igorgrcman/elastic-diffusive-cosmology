# EDC Mercury Precession Validation (v17.51)

Numerical verification engine for the **Elastic-Diffusive Cosmology (EDC) "River Bridge"** model.

## DOI
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18211854.svg)](https://doi.org/10.5281/zenodo.18211854)

## Overview
This repository reproduces the numerical validation of Mercury's anomalous perihelion precession using a 2nd-order symplectic Verlet-Binet integrator. It employs a "difference-of-runs" methodology to isolate the relativistic signal from discretization artifacts.

## Contents
- `src/edc_validation_v17.51.py`: Core simulation script.
- `src/generate_plots.py`: Visualization script.
- `data/raw_output_v17.51.log`: Terminal output for the 5-step refinement ladder.

## Installation & Usage
1. Install requirements: `pip install numpy scipy matplotlib`
2. Run validation: `python src/edc_validation_v17.51.py`
3. Results will match Table 1 in the technical report. Execution time depends on CPU performance.

## License
MIT License - see LICENSE file for details.
