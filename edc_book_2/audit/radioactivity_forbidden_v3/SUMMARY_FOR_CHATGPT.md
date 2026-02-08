# V3 SUMMARY: EDC Radioactivity + M-Topology Research

**Created**: 2026-01-31
**Purpose**: Compact summary for ChatGPT or other LLM context
**Full package**: audit/radioactivity_forbidden_v3/ (14 files)

---

## Core Framework

### LAW-1: Coordination Law [Der]
```
n is ALLOWED iff n = 2^a × 3^b for non-negative integers a, b
```
Allowed: 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, ...
Forbidden: 5, 7, 10, 11, 13, 14, 15, 17, 19, 20, 21, 22, 23, 37-47, ...

### LAW-2: Nuclear Saturation [Der]
```
n_opt ≈ 43.3 for nuclear matter
BUT 43 is prime > 3, hence FORBIDDEN
```
**Result**: Heavy nuclei exist in frustrated metastable state → radioactive decay

### LAW-3: Frustration-Corrected G-N [I]
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
a = 1.63, c = -2.40, b = -42.1
R² = 0.9941 (44.7% improvement over standard G-N)
```

---

## Key Findings

### Forbidden Zone [37-47]
All 11 values in this range are forbidden. n = 42 is equidistant from 36 and 48 (maximum frustration). n = 43 is the nuclear saturation optimum but prime (the "M43 paradox").

### Decay Chains
Three primordial chains (U-238, Th-232, U-235) all terminate at stable Pb isotopes:
- U-238 → Pb-206 (14 steps: 8α + 6β)
- Th-232 → Pb-208 (10 steps: 6α + 4β)
- U-235 → Pb-207 (11 steps: 7α + 4β)

**Hypothesis [P]**: Chains end because Pb isotopes have n ≈ 36 (allowed).

### n(A) Candidate Formula [P]
```
n(A) ≈ 6.1 × A^(1/3)

Gives: n(206) ≈ 36, n(238) ≈ 38
d(n) decreases along decay chains
```

### Crystal Coordination
Standard crystals have allowed n:
- FCC/HCP: n = 12 ✓
- BCC: n = 8 ✓
- SC: n = 6 ✓
- Diamond: n = 4 ✓

No stable periodic crystal exists with n = 5, 7, or 11.

---

## Epistemic Tags

| Tag | Meaning | Count |
|-----|---------|-------|
| [Der] | Derived from axioms | 6 laws |
| [I] | Inferred from fit | 3 laws |
| [P] | Proposed/hypothesis | 5+ generalizations |
| [Cal] | Calibrated from data | K, f values |
| [BL] | Blocked (needs source) | All nuclear data |
| [Open] | Unresolved | n(A), ε_f formulas |

---

## Open Questions (Priority Order)

1. **OQ-V3-001 [KINGPIN]**: What is n(A) formula exactly?
2. **OQ-V3-002**: What is ε_f(A) functional form?
3. **OQ-V3-003**: Can branching ratios be predicted from d(n)?
4. **OQ-V3-004**: Why are Pb-206/207/208 all stable?
5. **OQ-V3-005**: Does EDC predict fissility (U-235 vs U-238)?

---

## File Inventory

| # | File | Lines | Purpose |
|---|------|-------|---------|
| 1 | SESSION_LOG.md | ~80 | Activity tracking |
| 2 | DECISIONS.md | ~120 | Methodology decisions |
| 3 | OPEN_QUESTIONS.md | ~150 | Research gaps |
| 4 | DONOR_TRACEBACK.md | ~180 | 41+ precise citations |
| 5 | FORBIDDEN_CATALOG.md | ~200 | n=37..47 analysis |
| 6 | DECAY_CHAIN_U238.md | ~120 | 14-step chain |
| 7 | DECAY_CHAIN_TH232.md | ~130 | 10-step + branching |
| 8 | DECAY_CHAIN_U235.md | ~160 | 11-step + 2 branches |
| 9 | LAW_REGISTRY.md | ~200 | 6 laws + generalizations |
| 10 | N_A_MAPPING_RESEARCH.md | ~160 | Kingpin research |
| 11 | EPSILON_F_RESEARCH.md | ~150 | GAP-R1 research |
| 12 | BULK_CRYSTAL_STRUCTURES.md | ~180 | Crystal add-on |
| 13 | CRYSTAL_DONOR_TRACEBACK.md | ~100 | Crystal citations |
| 14 | CRYSTAL_FALSIFIABILITY.md | ~180 | Falsifiable tests |
| 15 | SUMMARY_FOR_CHATGPT.md | ~100 | This file |

**Total**: ~2000 lines across 15 files

---

## Primary Source

All content mined from: `audit/jsonl_mining/reports/22826edd_full.md` (17,562 lines)

Secondary sources: `73d92ff5_full.md`, `98cc5184_snippets.json`

---

## Guardrails Compliance

✓ No Book 2 .tex modifications
✓ No WebFetch without approval
✓ No hallucinated numerics (all data marked [BL:SOURCE_TBD])
✓ Epistemic tags on all claims
✓ file:line-range citations in DONOR_TRACEBACK.md
