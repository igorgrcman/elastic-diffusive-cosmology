#!/bin/bash
# Verify No Ambiguous PDF - Ensures proper release artifacts exist
# EDC Book IV
# Usage: ./tools/verify_no_ambiguous_pdf.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "=== PDF Artifact Verification ==="

ERRORS=0

# Check if dist/ exists
if [ ! -d "dist" ]; then
    echo "ERROR: dist/ directory does not exist"
    ERRORS=$((ERRORS + 1))
fi

# Count versioned PDFs in dist/
VERSIONED_COUNT=$(ls dist/book4_*.pdf 2>/dev/null | wc -l | tr -d ' ')

if [ "$VERSIONED_COUNT" -eq 0 ]; then
    echo "ERROR: No versioned PDFs found in dist/"
    echo "       Expected: dist/book4_<date>_<tag>_<sha>_p<pages>.pdf"
    ERRORS=$((ERRORS + 1))
else
    echo "OK: Found $VERSIONED_COUNT versioned PDF(s) in dist/"
fi

# Check if main.pdf is the ONLY artifact (bad)
if [ -f "main.pdf" ] && [ "$VERSIONED_COUNT" -eq 0 ]; then
    echo "ERROR: Only main.pdf exists with no dist/ artifact"
    echo "       Run 'make release-pdf' or './tools/build_release_pdf.sh'"
    ERRORS=$((ERRORS + 1))
fi

# Find and display newest dist artifact
if [ "$VERSIONED_COUNT" -gt 0 ]; then
    NEWEST=$(ls -t dist/book4_*.pdf 2>/dev/null | head -1)
    NEWEST_SHA=$(shasum -a 256 "$NEWEST" | awk '{print $1}')
    NEWEST_SIZE=$(ls -lh "$NEWEST" | awk '{print $5}')

    echo ""
    echo "=== Newest Release Artifact ==="
    echo "File:    $NEWEST"
    echo "Size:    $NEWEST_SIZE"
    echo "SHA-256: $NEWEST_SHA"
fi

# Summary
echo ""
if [ "$ERRORS" -eq 0 ]; then
    echo "=== VERIFICATION PASSED ==="
    exit 0
else
    echo "=== VERIFICATION FAILED ($ERRORS errors) ==="
    exit 1
fi
