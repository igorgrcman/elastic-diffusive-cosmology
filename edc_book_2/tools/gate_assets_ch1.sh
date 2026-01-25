#!/bin/bash
# gate_assets_ch1.sh — Asset gate check for CH1
# Runs the paranoid asset scanner and checks gate status
#
# Usage: ./gate_assets_ch1.sh
# Exit codes: 0 = PASS, 1 = FAIL

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=== CH1 Asset Gate Check ==="
echo "Book root: $BOOK_ROOT"
echo ""

# Run the asset scanner
python3 "$SCRIPT_DIR/ch1_asset_scan.py"

# Check gate report
GATE_REPORT="$BOOK_ROOT/audit/ch1/CH1_ASSET_GATE_REPORT.md"

if [[ ! -f "$GATE_REPORT" ]]; then
    echo "ERROR: Gate report not found: $GATE_REPORT"
    exit 1
fi

# Parse gate result
if grep -q "Result.*PASS" "$GATE_REPORT"; then
    echo ""
    echo "=== ASSET GATE: PASS ==="
    exit 0
else
    echo ""
    echo "=== ASSET GATE: FAIL ==="
    echo "Check $GATE_REPORT for details"
    exit 1
fi
