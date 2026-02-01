# V7.9 — TOPOLOGICAL PINNING ↔ α-DECAY INTEGRATION

**Created**: 2026-01-31
**Branch**: research/topological-pinning-v7_8-integration
**Purpose**: Integrate V7.4–V7.8 α-decay findings into the topological pinning derivation document
**Status**: COMPLETE

---

## Executive Summary

This integration creates `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex`, the content file that the existing `compile_topological_pinning.tex` wrapper references (via `\input{}`). The document combines:

1. **M6 theoretical framework** (from `M6_TOPOLOGICAL_MODEL_EXPLORATION.md`)
2. **α-decay empirical audit** (from V7.4–V7.8 audit packages)

**Key achievement**: A clean "bridge" from theory to evidence, with sign-safe language and full source traceability.

---

## What Changed

### New File Created

| File | Location | Lines | Pages |
|------|----------|-------|-------|
| `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` | `src/derivations/` | ~350 | 10 |

### Sections Added

| Section | Content | Source | Tag |
|---------|---------|--------|-----|
| 1. Introduction | M6 definition, Hamiltonian | M6 exploration | [Der]/[P] |
| 2. Free/Bound Neutron | Tunneling, pinning, stability | M6 exploration | [Der]/[P] |
| **3. α-Decay Audit** | **NEW** — coordination law, regression, sign resolution | V7.4–V7.8 | [Der]/[I] |
| 4. Falsification | Passed/open tests | V7.7/V7.8 | [Der]/[Open] |
| 5. Open Questions | Kingpins, upgrade path | V7.8 | [Open] |
| Appendix | Forbidden alternatives matrix | V7.7 | [P] |

---

## Key Numerics (Traced)

| Claim | Value | Source | Lines |
|-------|-------|--------|-------|
| V7.8 M2 coefficient | g = -1.64 ± 0.14 | V7.8/07_FIT_RESULTS_V7_8.md | 68 |
| V7.8 M2 significance | p < 0.001 | V7.8/07_FIT_RESULTS_V7_8.md | 68 |
| V7.8 M2 R² | 0.9805 | V7.8/07_FIT_RESULTS_V7_8.md | 70 |
| Deformation proxy p (M5) | 0.67 | V7.8/07_FIT_RESULTS_V7_8.md | 127 |
| Model A vs B ΔAIC | 3.4 | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 148 |
| Free neutron τ | 880 s | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 338 |
| Pinning constant K | ~1 MeV | M6_TOPOLOGICAL_MODEL_EXPLORATION.md | 308 |

---

## Sign-Safe Language

### Used Throughout

- "correlates with" (not "causes")
- "consistent with prefactor/S_α channel" (not "confirms")
- "higher d(n) → shorter t₁/₂" (correct sign)
- "frustration enhances preformation" (not "impedes tunneling")
- "d(n) captures variance beyond" (neutral)

### Avoided

- "proves topological mechanism"
- "S_α mechanism confirmed"
- "deformation irrelevant"
- "predicts half-life"

---

## Compilation

```bash
cd src/derivations
pdflatex compile_topological_pinning.tex
pdflatex compile_topological_pinning.tex  # Second pass for ToC
```

**Output**: `compile_topological_pinning.pdf` (10 pages, ~365 KB)

---

## Files in This Package

| # | File | Description |
|---|------|-------------|
| 1 | 00_README.md | This summary |
| 2 | 01_SESSION_LOG.md | Chronological log |
| 3 | 02_FILE_INVENTORY.md | Source file scan |
| 4 | 03_NARRATIVE_MAP.md | Before/after section outline |
| 5 | 04_CLAIM_LEDGER.md | **42 claims** with file:line sources |
| 6 | 05_INTEGRATION_PLAN.md | Step-by-step plan |
| 7 | 06_PATCH.diff | Summary diff |
| 8 | 07_BUILD_NOTES.md | Compilation guide |
| 9 | 08_OPEN_QUESTIONS_AND_TODOS.md | Kingpin sync |

---

## Guardrail Compliance

| Guardrail | Status | Notes |
|-----------|--------|-------|
| G0: No Book2 .tex edits | ✓ | Only derivations/ touched |
| G1: Branch created | ✓ | research/topological-pinning-v7_8-integration |
| G2: No webfetch | ✓ | All sources repo-local |
| G3: No hallucinated numerics | ✓ | 42 claims traced in ledger |
| G4: Epistemic tags | ✓ | [Der]/[I]/[P]/[Open] used |
| G5: Derivation voice | ✓ | Not paper style |
| G6: Reproducible log | ✓ | SESSION_LOG.md |
| G7: Minimal edits | ✓ | One new file created |

---

## Story Arc (AC6)

The document establishes this narrative chain:

```
M-topology (Z₆ symmetry)
    ↓
Coordination law: n = 2^a × 3^b
    ↓
Forbidden zone [37,47] for heavy nuclei
    ↓
Coordination distance d(n)
    ↓
Statistical correlation: g = -1.64, p < 0.001
    ↓
Sign resolution: prefactor (S_α) not barrier
    ↓
Physical interpretation: frustration → preformation enhancement
    ↓
Observed: faster α-decay for high d(n) nuclei
```

---

## Path to [Der] Upgrade

Current status: **4/7 complete** → **Strong [P], approaching [I]**

| Test | Status |
|------|--------|
| Robust regression | ✓ |
| Permutation test | ✓ |
| Cross-validation | ✓ |
| Deformation control | ✓ |
| Independent S_α | ⬜ |
| Causation mechanism | ⬜ |
| Superheavy validation | ⬜ |

---

## Commit Message

```
integrate(v7.8): tie topological pinning to α-decay prefactor evidence

- Create BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex with M6 framework
- Add Section 3: α-decay empirical audit (V7.4-V7.8)
- Sign-safe interpretation: frustration → S_α enhancement [I]
- 42 claims traced in audit/topological_pinning_v7_9_integration/
- Compiles to 10-page derivation document

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## One-Sentence Summary

**The topological pinning derivation now includes a complete audit-linked Section 3 demonstrating that coordination distance d(n) robustly correlates with α-decay rates via the prefactor channel, with sign-safe interpretation and explicit epistemic tagging.**

