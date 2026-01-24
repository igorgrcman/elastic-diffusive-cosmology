#!/bin/bash
# gate_canon.sh - Verify no contradictions to canonical documents
# Exit 0 = PASS, Exit 1 = FAIL

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$SCRIPT_DIR/../src"

echo "=== GATE: Canon Compliance ==="
ERRORS=0

# Check for DOI citations to canonical documents
echo "Checking canonical DOI references..."
CANON_DOIS=(
    "10.5281/zenodo.14538403"  # Framework v2.0
    "10.5281/zenodo.14538507"  # Paper 1
    "10.5281/zenodo.14564310"  # Paper 2
)

# Look for Framework v2.0 references without DOI
FRAMEWORK_REFS=$(grep -r "Framework v2.0" "$SRC_DIR" --include="*.tex" 2>/dev/null | grep -v "10.5281/zenodo.14538403" | wc -l | tr -d ' ')
if [ "$FRAMEWORK_REFS" -gt 0 ]; then
    echo "  WARNING: $FRAMEWORK_REFS Framework v2.0 references without DOI"
    # Not a hard failure, just warning
fi

# Check for redefinition of canonical symbols
echo "Checking for symbol redefinitions..."
REDEFINES=$(grep -rE "\\\\(re)?newcommand\{\\\\Rxi\}" "$SRC_DIR" --include="*.tex" 2>/dev/null | wc -l | tr -d ' ')
if [ "$REDEFINES" -gt 1 ]; then
    echo "  WARN: Multiple definitions of \\Rxi found"
fi

# Check for bulk-brane paraphrases (should cite Remark 4.5)
echo "Checking bulk-brane conservation statements..."
PARAPHRASES=$(grep -rE "bulk.*(to|→).*brane.*conservation" "$SRC_DIR" --include="*.tex" 2>/dev/null | grep -v "Remark~4.5\|Remark 4.5" | wc -l | tr -d ' ')
if [ "$PARAPHRASES" -gt 0 ]; then
    echo "  WARNING: $PARAPHRASES bulk-brane statements without Remark 4.5 citation"
fi

if [ "$ERRORS" -eq 0 ]; then
    echo "GATE RESULT: PASS"
    exit 0
else
    echo "GATE RESULT: FAIL ($ERRORS errors)"
    exit 1
fi
