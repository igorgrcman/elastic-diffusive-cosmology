#!/bin/bash
# Paper 3 Series — Run All Reproducibility Scripts
# =================================================
# This script runs all Python verification scripts in sequence.
#
# Usage:
#   ./run_all.sh
#
# Prerequisites:
#   - Python 3.9+ with numpy, scipy, matplotlib
#   - Recommended: run in virtual environment
#
# Author: Igor Grcman

set -e  # Exit on first error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=============================================="
echo "Paper 3 Series — Reproducibility Run"
echo "=============================================="
echo "Date: $(date)"
echo "Python: $(python3 --version)"
echo ""

# Check dependencies
echo "Checking dependencies..."
python3 -c "import numpy; import scipy; print(f'numpy={numpy.__version__}, scipy={scipy.__version__}')"
echo ""

# --- Common modules ---
echo "=== common/full5d_reduction.py ==="
python3 common/full5d_reduction.py 2>&1 | head -100
echo ""

echo "=== common/solve_electron_soliton_bvp_v5.py ==="
python3 common/solve_electron_soliton_bvp_v5.py 2>&1 | head -100
echo ""

# --- Companion B WKB ---
echo "=== companion_B_wkb/gaussian_step9.py ==="
cd companion_B_wkb
python3 gaussian_step9.py 2>&1 | head -100
cd ..
echo ""

echo "=== companion_B_wkb/compute_Rdet_v2.py ==="
cd companion_B_wkb
python3 compute_Rdet_v2.py 2>&1 | head -100
cd ..
echo ""

# --- Paper 3 lifetime ---
echo "=== paper3_lifetime/neutron_wkb_sensitivity.py ==="
cd paper3_lifetime
# This script may import from common/, so add to path
PYTHONPATH="../common:$PYTHONPATH" python3 neutron_wkb_sensitivity.py 2>&1 | head -100
cd ..
echo ""

echo "=============================================="
echo "All scripts completed."
echo "=============================================="
