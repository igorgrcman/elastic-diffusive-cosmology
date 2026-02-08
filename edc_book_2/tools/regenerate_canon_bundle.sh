#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
# regenerate_canon_bundle.sh — Deterministically regenerate CANON_BUNDLE.md
# ============================================================================
# Run from git repo root: bash edc_book_2/tools/regenerate_canon_bundle.sh
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK2_DIR="$(dirname "$SCRIPT_DIR")"
REPO_ROOT="$(dirname "$BOOK2_DIR")"

LIST="${BOOK2_DIR}/docs/CANON_P0.list"
OUT="${BOOK2_DIR}/docs/CANON_BUNDLE.md"

if [[ ! -f "$LIST" ]]; then
  echo "ERROR: Missing CANON_P0.list at $LIST" >&2
  exit 1
fi

# Start fresh
: > "$OUT"

cat >> "$OUT" << 'HEADER'
# CANON BUNDLE — P0 Mandatory Documents

**Generated:** TIMESTAMP
**Purpose:** Single file containing ALL P0 canonical documents for session loading.
**Usage:** Read this file at the START of every CC session. MANDATORY.

> This file is auto-generated from `docs/CANON_P0.list`.
> Do NOT edit directly — edit source files and run `tools/regenerate_canon_bundle.sh`.

---

HEADER

# Replace TIMESTAMP with actual date
if [[ "$OSTYPE" == "darwin"* ]]; then
  sed -i '' "s/TIMESTAMP/$(date '+%Y-%m-%d %H:%M')/" "$OUT"
else
  sed -i "s/TIMESTAMP/$(date '+%Y-%m-%d %H:%M')/" "$OUT"
fi

file_count=0
missing_count=0

while IFS= read -r line || [[ -n "$line" ]]; do
  # Skip empty lines and comments
  [[ -z "$line" ]] && continue
  [[ "$line" =~ ^[[:space:]]*# ]] && continue

  # Trim whitespace
  f=$(echo "$line" | xargs)

  # Resolve path relative to repo root
  full_path="${REPO_ROOT}/${f}"

  if [[ ! -f "$full_path" ]]; then
    echo "WARNING: Missing file listed in CANON_P0.list: $f" >&2
    echo "         Expected at: $full_path" >&2
    missing_count=$((missing_count + 1))
    continue
  fi

  file_count=$((file_count + 1))

  # Extract just filename for header
  basename_f=$(basename "$f")

  cat >> "$OUT" << SEPARATOR

# ============================================================================
# DOCUMENT ${file_count}: ${basename_f}
# Source: ${f}
# ============================================================================

SEPARATOR

  cat "$full_path" >> "$OUT"
  echo "" >> "$OUT"

done < "$LIST"

cat >> "$OUT" << FOOTER

# ============================================================================
# END OF CANON BUNDLE
# ============================================================================

**Total P0 documents:** ${file_count}
**Action:** Read this entire file at the start of every session. MANDATORY.
FOOTER

echo "OK: Regenerated $OUT"
echo "    Files included: $file_count"
if [[ $missing_count -gt 0 ]]; then
  echo "    WARNING: $missing_count files were missing!"
  exit 1
fi
