# Notation Audit Directory

Generated: 2026-01-24
Purpose: Context-aware symbol audit infrastructure for Book 2

## Directory Contents

| File | Purpose | Status |
|------|---------|--------|
| `SYMBOL_AUDIT_REPORT.md` | Generated audit report (violations, needs review) | Auto-generated |
| `SYMBOL_AUDIT_REPORT.csv` | Machine-readable audit data | Auto-generated |
| `SYMBOL_USAGE_BOOK2.md` | Per-symbol usage summary across Book 2 | Manual curation |
| `CHAPTER_VARIABLE_CONTEXT_LEDGER.md` | Per-chapter variable classification | Manual curation |
| `COLLISION_AND_AMBIGUITY_TODO.md` | Tracked symbol collisions and ambiguities | Work in progress |
| `REPLACEMENT_RISK_LEDGER.md` | Change tracking (BEFORE any replacement) | Append-only log |

## Workflow

### Running the Symbol Audit

```bash
cd edc_book_2
python3 tools/symbol_audit.py
```

Outputs:
- `audit/notation/SYMBOL_AUDIT_REPORT.md`
- `audit/notation/SYMBOL_AUDIT_REPORT.csv`

### Before Changing Any Symbol

1. Read `CHAPTER_VARIABLE_CONTEXT_LEDGER.md` for context classification
2. Add entry to `REPLACEMENT_RISK_LEDGER.md` with:
   - Old symbol → New symbol
   - Classification
   - Canon anchor
   - One-sentence reason
3. Make the change
4. Verify build passes
5. Re-run audit to confirm violation count decreased

### Gate Pass Criteria

The symbol audit gate PASSES when:
- Zero M5/M_5 violations
- Zero z-as-5D violations
- All NEEDS_REVIEW items classified
- REPLACEMENT_RISK_LEDGER.md complete for all changes
- Build gate PASS (387 pages)

## Canon Reference

Authority: Framework v2.0 (DOI: 10.5281/zenodo.18299085)

See `canon/SYMBOL_TABLE.md` for complete canonical symbol dictionary.

## Current Status

| Metric | Count |
|--------|-------|
| M5/M_5 violations | 22 |
| z-as-5D violations | 39 |
| NEEDS_REVIEW | 20 |
| **Total violations** | **61** |

Gate status: **FAIL**

---

Last updated: 2026-01-24
