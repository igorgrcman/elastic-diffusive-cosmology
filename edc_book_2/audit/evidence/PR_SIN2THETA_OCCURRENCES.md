# PR-SIN2THETA: sin²θ_W Derivation Audit

**Date:** 2026-01-25
**Branch:** book2-peerreview-verification-remediation-v1
**Triggered by:** Peer review claim of arithmetic error "2/6 = 1/3 = 0.25"

---

## Executive Summary

**VERDICT: NO ARITHMETIC ERROR FOUND**

The peer reviewer misread the derivation chain. The document correctly states:
- `g'²/g² = |Z₂|/|Z₆| = 2/6 = 1/3` (coupling ratio, [P] postulate)
- `sin²θ_W = g'²/(g² + g'²) = 1/4` (derived via standard EW relation, [Dc])

These are TWO DIFFERENT quantities. The math is:
```
g'²/g² = 1/3  →  let g² = 3k, g'² = k
sin²θ_W = g'²/(g² + g'²) = k/(3k + k) = k/4k = 1/4  ✓
```

---

## Evidence Table: All Occurrences

### Pattern: "2/6" (coupling ratio)

| File | Line | Content | Status |
|------|------|---------|--------|
| `meta_part2/01_claim_ledger.tex` | 16 | `$\sin^2\theta_W = 1/4$ (bare) from $\|Z_2\|/\|Z_6\| = 2/6$` | Condensed but correct |
| `CH3_electroweak_parameters.tex` | 56 | `We \emph{adopt} the map: $g'^2/g^2 = 2/6 = 1/3$ \tagP{}` | ✓ CORRECT |
| `CH3_electroweak_parameters.tex` | 265 | `The ratio of ``symmetry volumes'' is $2/6 = 1/3$` | ✓ CORRECT |
| `CH3_electroweak_parameters.tex` | 387 | `Ratio $2/6 = 1/3$ giving $g'^2/g^2$` | ✓ CORRECT |

### Pattern: sin²θ_W = 1/4 derivation

| File | Line | Content | Status |
|------|------|---------|--------|
| `CH3_electroweak_parameters.tex` | 62-63 | `sin²θ_W = g'²/(g² + g'²) = 1/4 \tagDc{}` | ✓ CORRECT |
| `CH3_electroweak_parameters.tex` | 71 | `The value $\sin^2\theta_W = 1/4$ applies at the lattice scale` | ✓ CORRECT |
| `CH3_electroweak_parameters.tex` | 102 | `$\sin^2\theta_W = 1/4$` (boxed key result) | ✓ CORRECT |

### Pattern: Claimed error "= 1/3 = 0.25" or "2/6 = 0.25"

```bash
grep -rn "= 1/3 = 0\.25\|2/6 = 0\.25\|1/3.*=.*0\.25" --include="*.tex" .
```
**Result: NO MATCHES FOUND**

---

## Detailed Analysis

### CH3_electroweak_parameters.tex (Lines 56-63)

```latex
We \emph{adopt} the map: $g'^2/g^2 = 2/6 = 1/3$ \tagP{}. This is an identification,
not derived from a 5D action.

\textbf{Step 4: The Weinberg angle follows (conditional).}
The photon $\gamma$ and $Z$ boson are \emph{orthogonal combinations} of the
``natural'' $SU(2)_L \times U(1)_Y$ basis. \emph{Given} the coupling ratio from Step~3,
the rotation angle $\theta_W$ satisfies $\sin^2\theta_W = g'^2/(g^2 + g'^2) = 1/4$
\tagDc{} (derived-conditional: IF Step~3 accepted THEN this follows).
```

**Analysis:**
1. Line 56: `g'²/g² = 2/6 = 1/3` — Mathematically correct (2/6 = 1/3 ✓)
2. Line 56: Tagged `[P]` (postulate) — Epistemically correct
3. Line 62: `sin²θ_W = g'²/(g² + g'²) = 1/4` — Mathematically correct
4. Line 63: Tagged `[Dc]` (derived-conditional) — Epistemically correct

### meta_part2/01_claim_ledger.tex (Line 16)

```latex
$\sin^2\theta_W = 1/4$ (bare) from $|Z_2|/|Z_6| = 2/6$
```

**Analysis:**
- This is a compressed summary
- Does NOT claim "2/6 = 1/4" (that would be wrong)
- Claims sin²θ_W = 1/4 COMES FROM the ratio 2/6
- The intermediate step (standard EW relation) is implicit
- **Suggestion:** Could add clarifying text for completeness, but NOT an error

---

## Epistemic Status Verification

| Claim | Current Tag | Correct? | Notes |
|-------|-------------|----------|-------|
| g'²/g² = 2/6 = 1/3 | [P] | ✓ | Postulate/identification |
| sin²θ_W = 1/4 (bare) | [Dc] | ✓ | Follows from [P] via EW relation |
| sin²θ_W(M_Z) = 0.2314 | [Dc] | ✓ | RG running from 1/4 |

---

## Conclusion

**No patch required for arithmetic.**

The peer reviewer's claim of "2/6 = 1/3 = 0.25" error does not exist in the codebase. The confusion arose from:
1. Misreading "2/6 = 1/3" (coupling ratio) as claiming equality with sin²θ_W
2. Not recognizing that sin²θ_W = 1/4 follows via the standard relation g'²/(g² + g'²)

**Optional improvement:** The claim ledger entry (line 16) could be expanded for clarity, but this is stylistic, not a correction.
