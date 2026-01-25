# BASELINE LOCK — Evidence Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E (Evidence)

---

## Build Baseline

| Metric | Value |
|--------|-------|
| PDF File | `EDC_Part_II_Weak_Sector_rebuild.pdf` |
| Page Count | **387** |
| SHA256 | `8427d09baf270c0f369ac3fda02530779c61b3b24e5e2a26fc7f9b3d53ed638f` |
| Build Command | `latexmk -xelatex -interaction=nonstopmode EDC_Part_II_Weak_Sector_rebuild.tex` |
| Timestamp | 2026-01-25T00:00:00Z |

---

## Gate Status at Baseline

| Gate | Status |
|------|--------|
| gate_notation.sh | PASS |
| gate_canon.sh | PASS |
| gate_build.sh | PASS (387 pages) |

---

## Evidence Audit Scope

This audit will verify:
1. All [Der] claims have complete derivation chains
2. All [Dc] claims have explicit conditions documented
3. All numeric results have reproducible scripts with hashes
4. No "trust me" steps for Tier-1 claims

---

## Constraints

- Page count must remain 387
- No physics content changes
- All new code labeled DEMO or REPRO
- DEMO artifacts cannot support physics claims

---

*Baseline locked: 2026-01-25*
