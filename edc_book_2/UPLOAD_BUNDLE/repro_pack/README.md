# V7.8 Topological Pinning Model - Reproducibility Package

## Overview

This package contains all scripts, data, and outputs needed to reproduce the quantitative results in the **Topological Pinning Monograph** (TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex).

## Directory Structure

```
repro_pack/
├── README.md              # This file
├── requirements.txt       # Python dependencies (minimal)
├── run_all.sh            # Master runner script
├── scripts/              # All Python analysis scripts
│   ├── v78_canonical_pipeline.py    # Master entrypoint
│   ├── m_coordination_full_test.py  # Coordination law fitting
│   ├── m6_extended_test.py          # Light nuclei (He-4, Li-6, Be-8)
│   ├── m6_sensitivity_test.py       # Sensitivity analysis
│   ├── prefactor_refit_cv.py        # 5-fold CV prefactor refit
│   ├── prefactor_sensitivity_full.py # Prefactor sensitivity
│   ├── superheavy_oos_test.py       # OOS superheavy validation
│   ├── superheavy_predictions.py    # Og-294 prediction
│   └── kramers_double_well_v2.py    # WKB/instanton tunneling
├── data/                 # Input datasets
│   └── alpha100_nndc_2025.csv       # NNDC α-emitter data (ALPHA100)
├── outputs/              # Generated output files
│   ├── v78_oos_table.csv            # OOS validation results
│   ├── cv_fold_results.csv          # Cross-validation results
│   └── ...
└── logs/                 # Script execution logs
```

## Quick Start

### Prerequisites
- Python 3.9 or higher
- No external packages required (pure Python standard library)

### Run All Scripts

```bash
cd edc_book_2/repro_pack
./run_all.sh
```

Or run the master pipeline directly:

```bash
python scripts/v78_canonical_pipeline.py --export-all
```

### Run Individual Scripts

```bash
# Coordination law fitting
python scripts/m_coordination_full_test.py

# 5-fold cross-validation
python scripts/prefactor_refit_cv.py

# Superheavy OOS validation
python scripts/superheavy_oos_test.py
```

## Key Results Reproduced

| Result | Script | Output |
|--------|--------|--------|
| n(A) = 6.1 × A^{1/3} | m_coordination_full_test.py | stdout |
| CV R² = 0.971 | prefactor_refit_cv.py | cv_fold_results.csv |
| OOS 6/6 pass | superheavy_oos_test.py | v78_oos_table.csv |
| Og-294: 0.5 ms | superheavy_predictions.py | stdout |
| K = 4.7 MeV | m6_extended_test.py | stdout |

## Data Provenance

### ALPHA100 Dataset
- **Source**: NNDC Nuclear Data (Brookhaven)
- **Snapshot date**: 2025-06-15
- **File**: `data/alpha100_nndc_2025.csv`
- **Records**: 100+ α-emitting nuclei with A ≤ 252
- **Columns**: nuclide, Z, A, t12_seconds, Qalpha_keV, hindrance_class, ...

### Superheavy Data
- **Source**: Published experimental papers (JINR, GSI, LBNL)
- **Nuclei**: Fl-289, Mc-290, Lv-293, Ts-294, Og-294, Og-295
- **Embedded in**: superheavy_oos_test.py

## Known Limitations

1. **No external data dependencies**: All data is self-contained in the package.

2. **Pure Python implementation**: Scripts use only Python standard library for maximum portability. Some advanced statistical features may be simplified.

3. **Computation time**: Most scripts complete in <1 minute. `prefactor_sensitivity_full.py` may take 5-10 minutes.

4. **Missing microscopic K derivation**: The bond energy K = 4.7 MeV is calibrated from He-4 anchor, not derived from first principles (marked as [OPEN] blocker).

## Verification

After running `./run_all.sh`, verify:

```bash
# Check OOS results
cat outputs/v78_oos_table.csv

# Check CV results
cat outputs/cv_fold_results.csv

# Check logs for errors
grep -l "FAIL\|Error" logs/*.log
```

## Citation

If using this reproducibility package, cite:

```
EDC Research (2026). Topological Pinning Model for Nuclear Structure.
DOI: 10.5281/zenodo.18299636
```

## Contact

Report issues: https://github.com/edc-research/elastic-diffusive-cosmology
