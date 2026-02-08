# N48 SECOND ISLAND MODULE (V6)

**Created**: 2026-01-31
**Purpose**: Model n=48 as LOCAL effective coordination, not global
**Focus**: "Second island of stability" via topology, not magic numbers

---

## Key Distinction (V6 Scope)

| Term | Meaning in this module |
|------|------------------------|
| n | Coordination number (topological) |
| N | Neutron number (NOT primary focus) |
| n=48 | Allowed value: 48 = 2⁴ × 3 |
| n≈43 | Saturation optimum (forbidden, prime) |

**Critical**: n=48 refers to coordination n, NOT neutron number N, unless donor explicitly defines otherwise.

---

## Grounding (from V4/V5)

The allowed coordination set is:
```
S = {n : n = 2^a × 3^b, a,b ≥ 0} = {1,2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,...}
```

Practical nuclear range: {4, 6, 8, 12, 24, 36, 48, 72}

**Source**: DN-001..005, 22826edd:2440-2540, 12444

---

## V6 Focus Areas

1. **Local effective n≈48**: How can a nucleus with A~200-500 achieve effective n≈48 locally?
2. **Mechanism taxonomy**: M1-M6 routes to n=48 stability
3. **Toy pipeline**: Symbolic n(A) mapping with explicit [P] tags
4. **Branching rule**: H-N48-01 hypothesis for decay channel selection

---

## File Inventory

| # | File | Purpose |
|---|------|---------|
| 00 | 00_README_N48.md | This file |
| 01 | 01_SESSION_LOG_N48.md | Activity tracking |
| 02 | 02_DECISIONS_N48.md | Methodology |
| 03 | 03_DONOR_TRACEBACK_N48.md | Citations for N48 module |
| 04 | 04_N48_ALLOWED_SET_AND_GEOMETRY.md | Geometry + local vs global |
| 05 | 05_SECOND_ISLAND_MODEL.md | Toy pipeline + A-table |
| 06 | 06_DECAY_CHAIN_RE-ANNOTATION_N48.md | Chains with N48 view |
| 07 | 07_BRANCHING_RULE_H-N48-01.md | Hypothesis + tests |
| 08 | 08_BULK_CRYSTAL_ANALOGY_N48.md | Defects/domains → n=48 |
| 09 | 09_LAWS_INVARIANTS_N48.md | N48-specific rules |
| 11 | 11_ASSUMPTION_LEDGER.md | All [P] assumptions |
| 12 | 12_MECHANISM_TAXONOMY_AND_TESTS.md | M1-M6+ tests |

---

## Guardrails (V6 additions)

| Guard | Rule |
|-------|------|
| G8 | No re-mining jsonl; use extracted files only |
| G9 | No long paraphrases; excerpt + cite + map |
| G10 | Every equation labeled [Der]/[I]/[P]/[Open] |
| G11 | Assumption ledger for all [P] |
| G12 | Supernova/gravity origin is [P] without donor |

---

## Acceptance Criteria (V6)

| AC | Criterion | Status |
|----|-----------|--------|
| AC-V6-1 | Files 11 + 12 exist | ✓ |
| AC-V6-2 | ≥12 assumptions in ledger | ✓ |
| AC-V6-3 | ≥6 mechanisms, ≥8 tests | ✓ |
| AC-V6-4 | A-table for {208,238,294,350,400,488} | ✓ |
| AC-V6-5 | No invented donors | ✓ |
| AC-V6-6 | No .tex, no webfetch | ✓ |
