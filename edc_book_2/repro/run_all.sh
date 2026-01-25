#!/bin/bash
#===============================================================================
# REPRO Pack — Run All Scripts
#===============================================================================
# Executes all REPRO scripts and generates checksum file.
#
# Usage:
#   cd edc_book_2/repro
#   bash run_all.sh
#
# Output:
#   output/*.json         — Script results
#   output/checksums.sha256 — SHA256 hashes for verification
#===============================================================================

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/output"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"

echo "========================================"
echo "REPRO Pack — Running All Scripts"
echo "========================================"
echo ""

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Track overall status
ALL_PASS=true

# Run each REPRO script
echo "[1/2] Running repro_sin2_z6_verify.py..."
if python "$SCRIPTS_DIR/repro_sin2_z6_verify.py"; then
    echo "  → PASS"
else
    echo "  → FAIL"
    ALL_PASS=false
fi
echo ""

echo "[2/2] Running repro_sin2_rg_running.py..."
if python "$SCRIPTS_DIR/repro_sin2_rg_running.py"; then
    echo "  → PASS"
else
    echo "  → FAIL"
    ALL_PASS=false
fi
echo ""

# Generate checksums
echo "Generating checksums..."
cd "$OUTPUT_DIR"
CHECKSUM_FILE="checksums.sha256"

# Create checksum file with header
cat > "$CHECKSUM_FILE" <<EOF
# REPRO Pack Checksums — Book 2
# Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
# Note: Timestamps in JSON files vary; checksums verify structure only.
#
# To verify: sha256sum -c checksums.sha256
#
EOF

# Add checksums for all JSON files
for json_file in *.json; do
    if [ -f "$json_file" ]; then
        shasum -a 256 "$json_file" >> "$CHECKSUM_FILE"
    fi
done

echo "  → Written: $CHECKSUM_FILE"
echo ""

# Summary
echo "========================================"
if $ALL_PASS; then
    echo "RESULT: ALL REPRO SCRIPTS PASSED"
    echo "========================================"
    echo ""
    echo "Outputs:"
    ls -la "$OUTPUT_DIR"/*.json
    echo ""
    echo "Checksums:"
    cat "$OUTPUT_DIR/$CHECKSUM_FILE"
    exit 0
else
    echo "RESULT: SOME REPRO SCRIPTS FAILED"
    echo "========================================"
    exit 1
fi
