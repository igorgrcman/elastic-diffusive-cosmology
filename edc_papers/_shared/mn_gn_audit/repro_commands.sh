#!/bin/bash
#
# repro_commands.sh — Reproduce the 44.7% improvement claim
#
# Usage:
#   cd elastic-diffusive-cosmology_repo
#   bash edc_papers/_shared/mn_gn_audit/repro_commands.sh
#
# Expected output:
#   Improvement: 44.7%
#
# Author: EDC Audit
# Date: 2026-01-29

set -e

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo ".")
cd "$REPO_ROOT"

echo "=============================================================="
echo "REPRODUCTION SCRIPT: Frustration-Corrected Geiger-Nuttall"
echo "=============================================================="
echo ""
echo "Git hash: $(git rev-parse HEAD)"
echo "Python version: $(python3 --version)"
echo "Date: $(date -Iseconds)"
echo ""

# Create logs directory if needed
mkdir -p edc_papers/_shared/mn_gn_audit/logs

# Run the original producer script
echo "--- Running original producer script ---"
python3 edc_book_2/src/derivations/frustration_geiger_nuttall.py | tee edc_papers/_shared/mn_gn_audit/logs/producer_output.log
echo ""

# Run the comparison harness
echo "--- Running comparison harness ---"
python3 edc_papers/_shared/mn_gn_audit/compare_models.py | tee edc_papers/_shared/mn_gn_audit/logs/comparison_output.log
echo ""

# Extract the key line
echo "=============================================================="
echo "KEY RESULT:"
grep -E "Improvement.*%" edc_papers/_shared/mn_gn_audit/logs/producer_output.log
echo "=============================================================="
