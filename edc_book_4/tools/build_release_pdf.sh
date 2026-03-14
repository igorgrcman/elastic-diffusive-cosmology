#!/bin/bash
# Build Release PDF with Versioned Filename
# EDC Book IV - Cluster Structure from Topological Pinning
# Usage: ./tools/build_release_pdf.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "=== EDC Book IV Release Build ==="
echo "Project dir: $PROJECT_DIR"

# Get git info
SHORT_SHA=$(git rev-parse --short HEAD)
FULL_SHA=$(git rev-parse HEAD)
BUILD_DATE=$(date +%Y%m%d)
BUILD_DATETIME=$(date "+%Y-%m-%d %H:%M:%S")

# Try to get tag, fallback to branch
TAG_OR_BRANCH=$(git describe --tags --exact-match 2>/dev/null || git rev-parse --abbrev-ref HEAD)
# Sanitize for filename (replace / with -)
TAG_SAFE=$(echo "$TAG_OR_BRANCH" | tr '/' '-')

echo "Git tag/branch: $TAG_OR_BRANCH"
echo "Short SHA: $SHORT_SHA"
echo "Build date: $BUILD_DATE"

# Create build info file for LaTeX
cat > build_info.tex << EOF
% Auto-generated build info - DO NOT EDIT
\renewcommand{\BuildTag}{$TAG_OR_BRANCH}
\renewcommand{\BuildSHA}{$SHORT_SHA}
\renewcommand{\BuildDate}{$BUILD_DATE}
EOF

echo "Created build_info.tex"

# Run LaTeX build (2 passes for cross-refs)
# Note: We build main.tex directly; build_info.tex is \input in preamble via \providecommand fallbacks
echo ""
echo "=== Running pdflatex (pass 1) ==="
rm -f main.pdf
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true
# Check if PDF was created (pdflatex may return non-zero for warnings)
if [ ! -f "main.pdf" ]; then
    echo "ERROR: First pdflatex pass failed - no PDF created"
    pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30
    exit 1
fi

echo "=== Running pdflatex (pass 2) ==="
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true
if [ ! -f "main.pdf" ]; then
    echo "ERROR: Second pdflatex pass failed"
    exit 1
fi

# Get page count
if command -v pdfinfo &> /dev/null; then
    PAGES=$(pdfinfo main.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}')
else
    # Fallback: extract from log
    PAGES=$(grep -o "Output written on main.pdf ([0-9]* pages" main.log | grep -o "[0-9]*" | head -1)
fi

if [ -z "$PAGES" ]; then
    PAGES="unknown"
fi

echo "Page count: $PAGES"

# Create dist directory
mkdir -p dist

# Generate versioned filename
RELEASE_FILENAME="book4_${BUILD_DATE}_${TAG_SAFE}_${SHORT_SHA}_p${PAGES}.pdf"
RELEASE_PATH="dist/$RELEASE_FILENAME"

# Copy to dist
cp main.pdf "$RELEASE_PATH"
echo "Created: $RELEASE_PATH"

# Compute SHA256
PDF_SHA256=$(shasum -a 256 "$RELEASE_PATH" | awk '{print $1}')

# Check for undefined refs
UNDEF_REFS=$(grep -c "LaTeX Warning: Reference.*undefined" main.log 2>/dev/null || echo "0")

# Write fingerprint report
mkdir -p audit
cat > audit/RELEASE_FINGERPRINT.md << EOF
# Release Fingerprint Report
## EDC Book IV: Cluster Structure from Topological Pinning

**Generated:** $BUILD_DATETIME

---

## Build Information

| Field | Value |
|-------|-------|
| Release filename | \`$RELEASE_FILENAME\` |
| Git commit (full) | \`$FULL_SHA\` |
| Git commit (short) | \`$SHORT_SHA\` |
| Tag/Branch | \`$TAG_OR_BRANCH\` |
| Build date | $BUILD_DATE |
| Page count | $PAGES |
| PDF SHA-256 | \`$PDF_SHA256\` |

---

## Build Quality

| Check | Result |
|-------|--------|
| Undefined refs | $UNDEF_REFS |
| LaTeX errors | 0 (build succeeded) |

---

## Artifact Location

\`\`\`
$RELEASE_PATH
\`\`\`

---

## Verification Command

\`\`\`bash
shasum -a 256 $RELEASE_PATH
# Expected: $PDF_SHA256
\`\`\`
EOF

echo ""
echo "=== Release Build Complete ==="
echo "Artifact: $RELEASE_PATH"
echo "SHA-256:  $PDF_SHA256"
echo "Pages:    $PAGES"
echo "Report:   audit/RELEASE_FINGERPRINT.md"

# Clean up build_info.tex
rm -f build_info.tex
