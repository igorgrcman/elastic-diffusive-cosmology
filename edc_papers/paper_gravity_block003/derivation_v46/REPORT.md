# P47 / Derivation v46: No-Escape Track Selector — Final Report

## Objective

Create a deterministic "No-Escape Track Selector" that consumes v45 SoT (ONLY)
and produces:
1. A single selected track OR explicit UNRESOLVED
2. Fully reproducible scoring vector + lexicographic decision rule
3. Prediction hook map for selected track

## Decision Pipeline Implementation

### Stage 0: Hard Gates

All tracks pass:
- G0: No forbidden inputs used
- G1: All anomalies = 0
- G2: v45 hash verified (a80b3886903152d3)

### Stage 1: Admissibility

| Track | Status | Reason |
|-------|--------|--------|
| SU(5) | CONDITIONAL | BRANE_MASS_TUNING |
| SO(10) | PASS | ALL_CRITERIA_MET |
| Pati-Salam | PASS | ALL_CRITERIA_MET |
| E6 | CONDITIONAL | HOSOTANI_REQUIRED |

AC-P47-17 applied: SU(5) and E6 excluded (CONDITIONAL while PASS exists)

Candidates: {SO(10), Pati-Salam}

### Stage 2: Vacuum Energy Ranking

| Track | S_vac | Rank |
|-------|-------|------|
| Pati-Salam | 25 | 1 (best) |
| SO(10) | 49 | 2 |

**Winner at Stage 2: Pati-Salam**

### Stages 3-4: Not Reached

Decision made at Stage 2 (vacuum energy).

### Tie-Breakers: Not Needed

Clear winner at Stage 2.

## Selection Result

```
SELECTED TRACK: Pati-Salam
STATUS: SELECTED
DECISION POINT: Stage 2 (ΔE_vac^finite)
WINNING CRITERION: S_vac(PS) = 25 < S_vac(SO10) = 49
```

## Verification Results

```
Total: 55/55 CHECKS PASSED
Check count requirement (>=45): PASS
ALL CHECKS PASSED

v45 SoT hash: a80b3886903152d3
v46 tables hash: 2742edea37e863ac
```

## Metrics Achieved

| Metric | Required | Achieved | Status |
|--------|----------|----------|--------|
| Pages | ≥26 | 26 | ✓ |
| Equations | ≥160 | 228 | ✓ |
| Labels | ≥240 | 350 | ✓ |
| Checks | ≥45 | 55 | ✓ |
| Reviewer traps | ≥18 | 18 | ✓ |

## Inputs Used

| Symbol | Source | Tag | Forbidden? |
|--------|--------|-----|------------|
| SoT_TRACKS | v45 recompute.py | [BL] | No |
| BC counts | SoT gauge/matter | [D] | No |
| Hypercharges | Exact fractions | [D] | No |
| Hash reference | v45 output | [D] | No |

**No forbidden inputs used.**

## Files Produced

- `main.tex` — Main document (1500+ lines)
- `main.pdf` — Compiled PDF (26 pages)
- `recompute.py` — Decision engine + 55 checks
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V46_NO_ESCAPE_TRACK_SELECTOR.pdf` — Export
- `README.md`, `REPORT.md`, `ACCEPTANCE.md` — Documentation

## Conclusion

The No-Escape Track Selector deterministically selects **Pati-Salam** as
the preferred GUT track for the EDC program based on:

1. PASS admissibility status (no exotic gating issues)
2. Lowest vacuum energy score among PASS tracks (25 vs 49)
3. Smallest group dimension among candidates (dim = 21)

The selection is robust with a margin of 24 points on the vacuum energy
score, and the decision is fully reproducible from the hash-locked SoT.
