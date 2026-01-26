# PHYSICAL_PATH_LOCK Audit Report

**Status**: COMPLETE
**Date**: 2026-01-25
**Sprint**: PHYSICAL PATH LOCK (Canonical Reader Path)

---

## Executive Summary

The canonical physical reader path is now locked throughout Book 2:
- **Physical (WD)**: Domain wall V_L = M² − M', μ-window [13, 17] [Dc]
- **Toy benchmark**: Pöschl–Teller V = −V₀ sech², μ-window [15, 18] [M]

No silent path switching remains. All μ-window references specify potential family.

---

## Grep Patterns and Counts

### Pattern Search Commands

```bash
# [25,35) occurrences
rg -c "\[25.*35\)|\[25,.*35\]" --type tex src/sections/

# [13,17] occurrences
rg -c "\[13.*17\]" --type tex src/sections/

# [15,18] occurrences
rg -c "\[15.*18\]" --type tex src/sections/

# Untagged three-generation requirements
rg -n "three.generation.*require|require.*μ.*window" --type tex src/sections/ | \
  grep -v "shape.dependent\|physical\|toy\|domain.wall"
```

### Results

| Pattern | Count | Status |
|---------|-------|--------|
| [25, 35) in tex sections | 3 files | All tagged as "toy benchmark" or "deprecated" |
| [13, 17] in tex sections | 4 files | Physical path properly labelled |
| [15, 18] in tex sections | 4 files | Toy benchmark properly labelled |
| Untagged "require μ" statements | 0 | ✓ PASS |

---

## Files Modified

| File | Change | Purpose |
|------|--------|---------|
| ch14_opr21_closure_derivation.tex | +35 lines | Added Box 14.1: Canonical Physical Path (WD) |
| ch16_opr04_delta_derivation.tex | +8 lines | Added reminder box |
| ch19_opr22_geff_from_exchange.tex | +9 lines | Added reminder box |
| OPR_REGISTRY.md | +30 lines | Added WD path section + DONE entry |

---

## Canonical Box Locations

| Chapter | Box | Label | Purpose |
|---------|-----|-------|---------|
| CH14 | Box 14.1 | `box:ch14_canonical_physical_path` | Main reader route map |
| CH16 | Reminder | (inline) | Cross-ref to CH14 |
| CH19 | Reminder | (inline) | Cross-ref to CH14 |

---

## [25, 35) Reference Audit

All remaining [25, 35) occurrences are properly qualified:

| File | Line | Context | Status |
|------|------|---------|--------|
| ch14_opr21_closure_derivation.tex | 511 | `(TOY BENCHMARK)` label | ✓ OK |
| ch14_opr21_closure_derivation.tex | 520 | "toy benchmark, not universal" | ✓ OK |
| ch14_opr21_closure_derivation.tex | varies | Deprecated note context | ✓ OK |
| ch15_opr01_sigma_anchor_derivation.tex | 299 | "deprecated toy benchmark" | ✓ OK |
| ch19_opr22_geff_from_exchange.tex | 683 | "not at [25,35] as estimated for PT" | ✓ OK (contrast) |

---

## Gate Results

| Gate | Status | Evidence |
|------|--------|----------|
| BUILD | ✓ PASS | 443 pages, XeLaTeX |
| NOTATION | ✓ PASS | μ = M₀ℓ consistent throughout |
| NO-SMUGGLING | ✓ PASS | No SM observables introduced |
| NO SILENT SWITCHING | ✓ PASS | All μ-windows specify potential family |
| DEPRECATED WINDOW | ✓ PASS | No unqualified [25,35) remains |

---

## What a Reader Can No Longer Misread

After PHYSICAL_PATH_LOCK:

1. **No ambiguity about which V(ξ)**: Physical path is domain wall, explicitly highlighted
2. **No "universal" μ-window claims**: Shape-dependence stated in canonical box
3. **No silent toy/physical switching**: Each chapter reminds reader of the path
4. **Toy path clearly demoted**: Labelled as "benchmark / sanity check / intuition only"
5. **Clear navigation**: "If you read only one path, follow the green-highlighted row"

---

## Checklist

- [x] WD path uniquely identified (domain wall V = M² − M')
- [x] Toy explicitly marked as benchmark only
- [x] No silent path switching in reader path
- [x] All [25,35) properly qualified or removed
- [x] Reminder boxes in CH16 and CH19
- [x] OPR_REGISTRY updated with WD path section
- [x] Build PASS (443 pages)

---

*Generated: 2026-01-25*
*Sprint: PHYSICAL PATH LOCK*
*Status: COMPLETE*
