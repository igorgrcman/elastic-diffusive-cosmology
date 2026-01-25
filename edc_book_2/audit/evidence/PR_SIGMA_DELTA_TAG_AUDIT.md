# PR-SIGMA-DELTA: Epistemic Tag Audit

**Date:** 2026-01-25
**Branch:** book2-peerreview-verification-remediation-v1
**Triggered by:** Peer review claim that σ and Δ are tagged [Dc] while depending on OPEN OPRs

---

## Executive Summary

**VERDICT: VALID CRITICISM — PATCH APPLIED**

The peer reviewer correctly identified an epistemic inconsistency:
- σ and Δ were tagged `\tagDc{}` (derived-conditional)
- But their comments explicitly state "[depends on OPR-01/OPR-04]"
- OPR-01 and OPR-04 are **OPEN** in the registry

This violates epistemic rigor: `[Dc]` implies "derived from accepted premises" but OPEN OPRs are not yet resolved derivations.

---

## Evidence

### Before (CH4_lepton_mass_candidates.tex, lines 35-36)

```latex
\item $\sigma = 5.86$ MeV/fm$^2$ — membrane tension \tagDc{} [depends on OPR-01]
\item $\Delta = 3.121 \times 10^{-3}$ fm — brane thickness \tagDc{} [depends on OPR-04]
```

### OPR Registry Status

| OPR | Title | Status |
|-----|-------|--------|
| OPR-01 | σ anchor derivation | **OPEN** |
| OPR-04 | δ ≡ R_ξ identification | **OPEN** |

### Issue Analysis

The tag `[Dc]` (derived-conditional) means:
> "IF the preceding postulates are accepted, THEN this follows by derivation"

However, OPR-01 and OPR-04 are labeled **OPEN**, meaning the derivation chains are not yet complete. Using `[Dc]` for values that depend on unresolved derivations is epistemically incorrect.

**Correct tagging options:**
1. `[P]` (Postulate) — if treating as adopted value pending derivation
2. `[Cal]` (Calibrated) — if fitted to data
3. `[OPEN]` — if explicitly marking as unresolved

Given that:
- The values are "adopted" for calculation purposes
- The derivation is explicitly marked as pending (OPR reference)
- The chapter header already marks entire section as `[P]` status

The appropriate tag is `[P]` (Postulate/Provisional).

---

## Patch Applied

### After (CH4_lepton_mass_candidates.tex, lines 35-36)

```latex
\item $\sigma = 5.86$ MeV/fm$^2$ — membrane tension \tagP{} (OPR-01, OPEN)
\item $\Delta = 3.121 \times 10^{-3}$ fm — brane thickness \tagP{} (OPR-04, OPEN)
```

### Changes Made

| Item | Before | After | Rationale |
|------|--------|-------|-----------|
| σ tag | `\tagDc{}` | `\tagP{}` | Cannot be [Dc] while derivation OPEN |
| σ comment | `[depends on OPR-01]` | `(OPR-01, OPEN)` | Clearer status indication |
| Δ tag | `\tagDc{}` | `\tagP{}` | Cannot be [Dc] while derivation OPEN |
| Δ comment | `[depends on OPR-04]` | `(OPR-04, OPEN)` | Clearer status indication |

---

## Conclusion

The peer reviewer's criticism was **valid**. The inconsistency has been corrected by downgrading tags from `[Dc]` to `[P]` to reflect that these values are provisional pending resolution of OPR-01 and OPR-04.
