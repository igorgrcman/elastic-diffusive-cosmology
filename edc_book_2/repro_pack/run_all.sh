#!/bin/bash
#
# V7.8 TOPOLOGICAL PINNING MODEL - REPRODUCIBILITY RUNNER
# ========================================================
# This script runs all analysis scripts and generates outputs.
#
# Usage:
#   cd edc_book_2/repro_pack
#   ./run_all.sh           # Fast mode (default) - skips slow scripts
#   ./run_all.sh --fast    # Same as default
#   ./run_all.sh --full    # Full mode - runs everything including slow scripts
#
# Prerequisites:
#   - Python 3.9+
#   - No external packages required (pure Python)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Parse arguments
MODE="fast"
if [ "$1" == "--full" ]; then
    MODE="full"
fi

echo "========================================"
echo "V7.8 Topological Pinning - Repro Runner"
echo "========================================"
echo "Date: $(date)"
echo "Mode: $MODE"
echo "Directory: $SCRIPT_DIR"
echo ""

# Create output directories
mkdir -p outputs logs

# Check Python
PYTHON=${PYTHON:-python3}
echo "Python: $($PYTHON --version)"
echo ""

# Expected artifacts
echo "Expected artifacts:"
echo "  outputs/v78_oos_table.csv      - Superheavy OOS results"
echo "  outputs/cv_fold_results.csv    - 5-fold CV results"
echo "  outputs/alpha100_fitted.csv    - Full dataset with predictions"
echo ""

# Function to run script with logging
run_script() {
    local script=$1
    local desc=$2
    local slow=$3
    local logfile="logs/$(basename $script .py).log"

    echo "----------------------------------------"
    echo "Running: $desc"
    echo "Script: scripts/$script"
    echo "Log: $logfile"

    if [ "$slow" == "slow" ] && [ "$MODE" == "fast" ]; then
        echo "Status: SKIP (slow script, use --full to run)"
        echo "Expected runtime: 5-10 minutes"
        echo "Expected output: bootstrap_params.csv"
        return 0
    fi

    if [ -f "scripts/$script" ]; then
        START=$(date +%s)
        $PYTHON "scripts/$script" > "$logfile" 2>&1 && {
            END=$(date +%s)
            echo "Status: PASS ($(($END - $START))s)"
            tail -5 "$logfile"
        } || {
            echo "Status: FAIL (see $logfile)"
            tail -10 "$logfile"
            return 1
        }
    else
        echo "Status: SKIP (script not found)"
    fi
    echo ""
}

# Track results
PASSED=0
FAILED=0
SKIPPED=0

echo ""
echo "========================================"
echo "STEP 1: Coordination Law Analysis"
echo "========================================"
run_script "m_coordination_full_test.py" "Coordination law fitting" && ((PASSED++)) || ((FAILED++))

echo "========================================"
echo "STEP 2: Light Nuclei Tests"
echo "========================================"
run_script "m6_extended_test.py" "He-4, Li-6, Be-8 analysis" && ((PASSED++)) || ((FAILED++))
run_script "m6_sensitivity_test.py" "Sensitivity analysis" && ((PASSED++)) || ((FAILED++))

echo "========================================"
echo "STEP 3: V7.8 Prefactor Analysis"
echo "========================================"
run_script "prefactor_refit_cv.py" "5-fold cross-validation" && ((PASSED++)) || ((FAILED++))
run_script "prefactor_sensitivity_full.py" "Prefactor sensitivity (slow)" "slow" && {
    if [ "$MODE" == "full" ]; then ((PASSED++)); else ((SKIPPED++)); fi
} || ((FAILED++))

echo "========================================"
echo "STEP 4: Superheavy Validation"
echo "========================================"
run_script "superheavy_oos_test.py" "Out-of-sample superheavy test" && ((PASSED++)) || ((FAILED++))
run_script "superheavy_predictions.py" "Superheavy predictions" && ((PASSED++)) || ((FAILED++))

echo "========================================"
echo "STEP 5: WKB/Instanton Verification"
echo "========================================"
run_script "kramers_double_well_v2.py" "Kramers tunneling rate" && ((PASSED++)) || ((FAILED++))

echo "========================================"
echo "STEP 6: Master Pipeline (export CSVs)"
echo "========================================"
$PYTHON scripts/v78_canonical_pipeline.py --export-all --skip-slow > logs/v78_canonical_pipeline.log 2>&1 && {
    echo "Status: PASS"
    ((PASSED++))
} || {
    echo "Status: FAIL"
    ((FAILED++))
}

echo ""
echo "========================================"
echo "SUMMARY"
echo "========================================"
echo "Mode: $MODE"
echo "Passed: $PASSED"
echo "Failed: $FAILED"
echo "Skipped: $SKIPPED"
echo ""
echo "Outputs:"
ls -la outputs/ 2>/dev/null || echo "(no outputs)"
echo ""

if [ "$MODE" == "fast" ]; then
    echo "NOTE: Running in --fast mode. Skipped scripts:"
    echo "  - prefactor_sensitivity_full.py (5-10 min, produces bootstrap_params.csv)"
    echo ""
    echo "To run all scripts including slow ones:"
    echo "  ./run_all.sh --full"
fi

echo ""
echo "Done: $(date)"

# Exit with error if any failed
[ $FAILED -eq 0 ] && exit 0 || exit 1
