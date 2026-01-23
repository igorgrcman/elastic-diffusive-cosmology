#!/bin/bash
# ==============================================================================
# EDC Book Clean Build Script
# Builds Part II (and optionally Framework v2.0) from clean state
# ==============================================================================

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAPER_DIR="$(dirname "$SCRIPT_DIR")"
REPO_ROOT="$(cd "$PAPER_DIR/../../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}EDC Book Clean Build${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo "Paper directory: $PAPER_DIR"
echo "Repo root: $REPO_ROOT"
echo ""

# ==============================================================================
# Step 1: Clean auxiliary files
# ==============================================================================
echo -e "${YELLOW}[1/4] Cleaning auxiliary files...${NC}"

cd "$PAPER_DIR"

# Clean Part II
if [ -f "EDC_Part_II_Weak_Sector.tex" ]; then
    echo "  Cleaning Part II (EDC_Part_II_Weak_Sector)..."
    latexmk -C -f EDC_Part_II_Weak_Sector.tex 2>/dev/null || true
    rm -f EDC_Part_II_Weak_Sector.{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,toc,xdv,run.xml} 2>/dev/null || true
fi

# Clean other standalone documents
for doc in chapter_weak_interface Z6_PROGRAM_COMPLETE_DERIVATION Z6_PROGRAM_EXECUTIVE_SUMMARY; do
    if [ -f "${doc}.tex" ]; then
        echo "  Cleaning ${doc}..."
        latexmk -C -f "${doc}.tex" 2>/dev/null || true
        rm -f "${doc}."{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,toc,xdv,run.xml} 2>/dev/null || true
    fi
done

# Clean research_targets
if [ -d "research_targets" ]; then
    echo "  Cleaning research_targets/..."
    cd research_targets
    for tex in *.tex; do
        [ -f "$tex" ] && latexmk -C -f "$tex" 2>/dev/null || true
    done
    rm -f *.{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,toc,xdv,run.xml} 2>/dev/null || true
    cd "$PAPER_DIR"
fi

# ==============================================================================
# Step 2: Clean Framework v2.0 (Part I)
# ==============================================================================
FRAMEWORK_DIR="$REPO_ROOT/paper_3_series/00_framework_v2_0/paper"
if [ -d "$FRAMEWORK_DIR" ]; then
    echo -e "${YELLOW}[2/4] Cleaning Framework v2.0 (Part I)...${NC}"
    cd "$FRAMEWORK_DIR"
    if [ -f "main.tex" ]; then
        latexmk -C -f main.tex 2>/dev/null || true
        rm -f main.{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,toc,xdv,run.xml} 2>/dev/null || true
    fi
    cd "$PAPER_DIR"
else
    echo -e "${YELLOW}[2/4] Framework v2.0 not found, skipping...${NC}"
fi

# ==============================================================================
# Step 3: Build Framework v2.0 (Part I)
# ==============================================================================
BUILD_PART_I=${BUILD_PART_I:-false}
if [ "$BUILD_PART_I" = "true" ] && [ -d "$FRAMEWORK_DIR" ]; then
    echo -e "${YELLOW}[3/4] Building Framework v2.0 (Part I)...${NC}"
    cd "$FRAMEWORK_DIR"
    latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}  Framework v2.0 built successfully.${NC}"
    else
        echo -e "${RED}  Framework v2.0 build FAILED.${NC}"
        exit 1
    fi
    cd "$PAPER_DIR"
else
    echo -e "${YELLOW}[3/4] Skipping Part I build (set BUILD_PART_I=true to enable)${NC}"
fi

# ==============================================================================
# Step 4: Build Part II (Weak Sector)
# ==============================================================================
echo -e "${YELLOW}[4/4] Building Part II (Weak Sector)...${NC}"
cd "$PAPER_DIR"

if [ -f "EDC_Part_II_Weak_Sector.tex" ]; then
    latexmk -xelatex -interaction=nonstopmode -halt-on-error EDC_Part_II_Weak_Sector.tex
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}  Part II built successfully.${NC}"
        PAGES=$(pdfinfo EDC_Part_II_Weak_Sector.pdf 2>/dev/null | grep Pages | awk '{print $2}')
        echo -e "${GREEN}  Output: EDC_Part_II_Weak_Sector.pdf (${PAGES:-?} pages)${NC}"
    else
        echo -e "${RED}  Part II build FAILED.${NC}"
        exit 1
    fi
else
    echo -e "${RED}  ERROR: EDC_Part_II_Weak_Sector.tex not found!${NC}"
    exit 1
fi

# ==============================================================================
# Summary
# ==============================================================================
echo ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Build Complete${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo "Outputs:"
[ -f "$PAPER_DIR/EDC_Part_II_Weak_Sector.pdf" ] && echo "  - EDC_Part_II_Weak_Sector.pdf"
[ -f "$FRAMEWORK_DIR/main.pdf" ] && echo "  - Framework v2.0: main.pdf"
echo ""
echo "To build with Part I: BUILD_PART_I=true ./scripts/clean_build.sh"
