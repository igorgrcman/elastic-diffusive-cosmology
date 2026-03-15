#!/bin/sh
# VERIFY_P84.sh — 60-second verifier for BLOCK-004 v67 REAL CLOSED
# Usage: cd derivation_v67 && ./VERIFY_P84.sh
# Exit code: 0 = success, 1 = failure

set -e

TAG="BLOCK004_V67_REAL_CLOSED"
MANIFEST="release/manifest.sha256"
RELEASE_PDF="release/EDC_BLOCK004_DERIVATION_V67_REAL_CLOSED.pdf"
LAYER_A_SOT="d8e9f0a1b2c34567"

echo "========================================================================"
echo "BLOCK-004 v67 REAL CLOSED — Verification Script (P84)"
echo "========================================================================"
echo ""

FAILED=0

# Detect sha256sum command (Linux vs macOS)
if command -v sha256sum >/dev/null 2>&1; then
    SHA256CMD="sha256sum"
elif command -v shasum >/dev/null 2>&1; then
    SHA256CMD="shasum -a 256"
else
    echo "[FAIL] No sha256sum or shasum found"
    exit 1
fi

# Check 1: Tag exists (local)
echo "--- Check 1: Tag verification ---"
if git tag -l "$TAG" | grep -q "$TAG"; then
    echo "[PASS] Tag $TAG exists locally"
else
    echo "[WARN] Tag $TAG not found locally"
    echo "       Run: git fetch --tags"
    echo "       Then re-run this script"
    FAILED=1
fi
echo ""

# Check 2: Manifest exists
echo "--- Check 2: Manifest existence ---"
if [ -f "$MANIFEST" ]; then
    echo "[PASS] $MANIFEST exists"
else
    echo "[FAIL] $MANIFEST not found"
    FAILED=1
fi
echo ""

# Check 3: Hash verification (7 files)
echo "--- Check 3: SHA256 hash verification ---"
if [ -f "$MANIFEST" ]; then
    HASH_PASS=0
    HASH_TOTAL=0
    while IFS= read -r line; do
        if [ -n "$line" ]; then
            EXPECTED_HASH=$(echo "$line" | awk '{print $1}')
            FILEPATH=$(echo "$line" | awk '{print $2}')
            HASH_TOTAL=$((HASH_TOTAL + 1))
            if [ -f "$FILEPATH" ]; then
                ACTUAL_HASH=$($SHA256CMD "$FILEPATH" | awk '{print $1}')
                if [ "$EXPECTED_HASH" = "$ACTUAL_HASH" ]; then
                    echo "[PASS] $FILEPATH"
                    HASH_PASS=$((HASH_PASS + 1))
                else
                    echo "[FAIL] $FILEPATH (hash mismatch)"
                    FAILED=1
                fi
            else
                echo "[FAIL] $FILEPATH (file not found)"
                FAILED=1
            fi
        fi
    done < "$MANIFEST"
    echo ""
    echo "       Hash verification: $HASH_PASS/$HASH_TOTAL passed"
else
    echo "[SKIP] Cannot verify hashes without manifest"
    FAILED=1
fi
echo ""

# Check 4: Release PDF exists
echo "--- Check 4: Release PDF ---"
if [ -f "$RELEASE_PDF" ]; then
    echo "[PASS] $RELEASE_PDF exists"
else
    echo "[FAIL] $RELEASE_PDF not found"
    FAILED=1
fi
echo ""

# Summary
echo "========================================================================"
echo "SUMMARY"
echo "========================================================================"
echo ""
echo "MODE:        REAL"
echo "TAG:         $TAG"
echo "RELEASE PDF: $RELEASE_PDF"
echo "Layer A SoT: $LAYER_A_SOT"
echo "Commits:     a110a08 (P83b), e7f2235 (P83a)"
echo ""

if [ "$FAILED" -eq 0 ]; then
    echo "========================================================================"
    echo "VERIFICATION PASSED"
    echo "========================================================================"
    exit 0
else
    echo "========================================================================"
    echo "VERIFICATION FAILED — see errors above"
    echo "========================================================================"
    exit 1
fi
