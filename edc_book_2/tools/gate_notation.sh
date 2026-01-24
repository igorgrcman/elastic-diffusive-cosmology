#!/bin/bash
# gate_notation.sh - Verify notation compliance with canonical standards
# Exit 0 = PASS, Exit 1 = FAIL

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$SCRIPT_DIR/../src"

echo "=== GATE: Notation Compliance ==="
ERRORS=0

# Forbidden patterns
echo "Checking forbidden patterns..."

# Check for 'z' used as 5D coordinate
# Pattern: R_z, R_{z} (explicit 5D radius with z)
Z_COORD=$(grep -rE "R_z|R_\{z\}" "$SRC_DIR" --include="*.tex" 2>/dev/null | wc -l | tr -d ' ')
if [ "$Z_COORD" -gt 0 ]; then
    echo "  ERROR: Found $Z_COORD instances of R_z (use R_ξ or \\Rxi)"
    grep -rE "R_z|R_\{z\}" "$SRC_DIR" --include="*.tex" 2>/dev/null | head -3
    ERRORS=$((ERRORS + 1))
else
    echo "  No R_z found (good - using canonical R_ξ)"
fi

# Check ξ usage (should exist in 5D context)
XI_USES=$(grep -rE "\\\\xi|ξ" "$SRC_DIR" --include="*.tex" 2>/dev/null | wc -l | tr -d ' ')
echo "  Found $XI_USES uses of ξ (canonical 5D coordinate)"

# Check Rxi macro usage
RXI_USES=$(grep -r "\\\\Rxi" "$SRC_DIR" --include="*.tex" 2>/dev/null | wc -l | tr -d ' ')
echo "  Found $RXI_USES uses of \\Rxi macro"

# Check epistemic tags
echo "Checking epistemic tag usage..."
for TAG in "\\\\tagBL" "\\\\tagDer" "\\\\tagDc" "\\\\tagI" "\\\\tagP" "\\\\tagCal"; do
    COUNT=$(grep -r "$TAG" "$SRC_DIR" --include="*.tex" 2>/dev/null | wc -l | tr -d ' ')
    TAG_NAME=$(echo "$TAG" | sed 's/\\\\tag//')
    echo "  [$TAG_NAME]: $COUNT occurrences"
done

# Check for claims without tags (heuristic: lines with "=" in math mode without tags)
# This is just informational, not a hard check
UNTAGGED=$(grep -rE "\\$.*=.*\\$" "$SRC_DIR/sections" --include="*.tex" 2>/dev/null | grep -v "tag" | wc -l | tr -d ' ')
echo "  Potential untagged equations: ~$UNTAGGED (informational)"

if [ "$ERRORS" -eq 0 ]; then
    echo "GATE RESULT: PASS"
    exit 0
else
    echo "GATE RESULT: FAIL ($ERRORS errors)"
    exit 1
fi
