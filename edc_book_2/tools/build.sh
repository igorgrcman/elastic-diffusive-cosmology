#!/bin/bash
# ==============================================================================
# BUILD.SH — Deterministic Build for Book 2
# ==============================================================================
# Single-command build that produces build/main.pdf
# Exit codes: 0 = success, 1 = failure
#
# Usage: bash tools/build.sh [--verify]
#   --verify: Also check page count and record hash
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$REPO_ROOT/src"
BUILD_DIR="$REPO_ROOT/build"
OUTPUT_PDF="$BUILD_DIR/main.pdf"
BASELINE_FILE="$REPO_ROOT/audit/BASELINE_BUILD.md"

# Expected values
EXPECTED_PAGES=387
MAIN_TEX="main.tex"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=============================================="
echo "Book 2 Build Script"
echo "=============================================="
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Repo: $REPO_ROOT"
echo ""

# Check dependencies
check_deps() {
    local missing=0

    if ! command -v xelatex &> /dev/null; then
        echo -e "${RED}ERROR: xelatex not found${NC}"
        missing=1
    fi

    if ! command -v latexmk &> /dev/null; then
        echo -e "${RED}ERROR: latexmk not found${NC}"
        missing=1
    fi

    if [ $missing -eq 1 ]; then
        echo ""
        echo "Required dependencies:"
        echo "  - xelatex (TeX Live or MacTeX)"
        echo "  - latexmk"
        echo ""
        echo "See audit/evidence/BUILD_DEPS.md for installation instructions."
        exit 1
    fi

    echo -e "${GREEN}Dependencies OK${NC}"
}

# Build PDF
build_pdf() {
    echo ""
    echo "Building PDF..."

    mkdir -p "$BUILD_DIR"
    cd "$SRC_DIR"

    # Run latexmk with xelatex
    latexmk -xelatex \
        -interaction=nonstopmode \
        -halt-on-error \
        -output-directory="$BUILD_DIR" \
        "$MAIN_TEX"

    if [ ! -f "$OUTPUT_PDF" ]; then
        echo -e "${RED}ERROR: Build failed - no PDF produced${NC}"
        exit 1
    fi

    echo -e "${GREEN}Build successful: $OUTPUT_PDF${NC}"
}

# Verify output
verify_output() {
    echo ""
    echo "Verifying output..."

    # Check if pdfinfo is available
    if command -v pdfinfo &> /dev/null; then
        PAGES=$(pdfinfo "$OUTPUT_PDF" 2>/dev/null | grep "Pages:" | awk '{print $2}')

        if [ "$PAGES" != "$EXPECTED_PAGES" ]; then
            echo -e "${RED}ERROR: Page count mismatch${NC}"
            echo "  Expected: $EXPECTED_PAGES"
            echo "  Got: $PAGES"
            exit 1
        fi

        echo -e "${GREEN}Page count OK: $PAGES${NC}"
    else
        echo -e "${YELLOW}WARNING: pdfinfo not available, skipping page count check${NC}"
    fi

    # Compute SHA256
    if command -v shasum &> /dev/null; then
        HASH=$(shasum -a 256 "$OUTPUT_PDF" | cut -d' ' -f1)
    elif command -v sha256sum &> /dev/null; then
        HASH=$(sha256sum "$OUTPUT_PDF" | cut -d' ' -f1)
    else
        HASH="UNKNOWN"
    fi

    echo "SHA256: $HASH"

    # Record to baseline if requested
    if [ "$1" == "--record" ]; then
        echo ""
        echo "Recording to baseline..."
        echo "" >> "$BASELINE_FILE"
        echo "| $(date -u +%Y-%m-%d) | Build | $PAGES | $HASH | ✅ |" >> "$BASELINE_FILE"
        echo -e "${GREEN}Recorded to $BASELINE_FILE${NC}"
    fi
}

# Main
check_deps

if [ "$1" == "--verify" ]; then
    build_pdf
    verify_output
else
    build_pdf
fi

echo ""
echo "=============================================="
echo -e "${GREEN}BUILD COMPLETE${NC}"
echo "=============================================="
