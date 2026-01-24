#!/bin/bash
# gate_build.sh - Verify build succeeds and produces expected output
# Exit 0 = PASS, Exit 1 = FAIL

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$SCRIPT_DIR/../src"
BUILD_DIR="$SCRIPT_DIR/../build"

echo "=== GATE: Build Verification ==="
ERRORS=0

# Expected baseline
BASELINE_PAGES=387

# Build the document
echo "Building document..."
cd "$SRC_DIR"

if ! latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null 2>&1; then
    echo "  ERROR: Build failed"
    ERRORS=$((ERRORS + 1))
else
    echo "  Build succeeded"
fi

# Check page count
if [ -f "main.pdf" ]; then
    PAGES=$(pdfinfo main.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}')
    echo "  Page count: $PAGES (baseline: $BASELINE_PAGES)"

    if [ "$PAGES" -ne "$BASELINE_PAGES" ]; then
        echo "  WARNING: Page count differs from baseline"
        # Not a hard failure, just informational
    fi

    # Move artifacts to build directory
    mv main.pdf "$BUILD_DIR/"
    mv main.log "$BUILD_DIR/"
    mv main.aux "$BUILD_DIR/"
    mv main.bbl "$BUILD_DIR/" 2>/dev/null || true
    mv main.bcf "$BUILD_DIR/" 2>/dev/null || true
    mv main.blg "$BUILD_DIR/" 2>/dev/null || true
    mv main.fdb_latexmk "$BUILD_DIR/" 2>/dev/null || true
    mv main.fls "$BUILD_DIR/" 2>/dev/null || true
    mv main.out "$BUILD_DIR/" 2>/dev/null || true
    mv main.run.xml "$BUILD_DIR/" 2>/dev/null || true
    mv main.toc "$BUILD_DIR/" 2>/dev/null || true
    mv main.xdv "$BUILD_DIR/" 2>/dev/null || true

    # Compute SHA256
    SHA=$(shasum -a 256 "$BUILD_DIR/main.pdf" | cut -d' ' -f1)
    echo "  Output SHA256: $SHA"
else
    echo "  ERROR: No PDF produced"
    ERRORS=$((ERRORS + 1))
fi

if [ "$ERRORS" -eq 0 ]; then
    echo "GATE RESULT: PASS"
    exit 0
else
    echo "GATE RESULT: FAIL ($ERRORS errors)"
    exit 1
fi
