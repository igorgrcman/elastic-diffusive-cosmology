# P-S2-Direction Ledger Update

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Test performed:** Prove-or-fail for P-S2-direction [P] → [Dc]
**Result:** FAIL — P-S2-direction remains [P]

---

## 1. Test Summary

| Item | Detail |
|------|--------|
| **Sub-claim tested** | P-S2-direction: "ε(n̂) does not depend on the S² spin direction n̂" |
| **Prior status** | [P] (sub-component of P-isotropy, identified in P-isotropy prove-or-fail) |
| **Target status** | [Dc] (derived conditional on bulk Plenum rotational isotropy) |
| **Derivation route** | Bulk Plenum rotational isotropy → no preferred S² direction |
| **Outcome** | **FAIL** |

---

## 2. Checkpoint Results

| # | Checkpoint | Result | Detail |
|---|-----------|--------|--------|
| 1 | Physical content of S² | **PASS** | S² is observed spin direction (genuine observable, not gauge) |
| 2 | Canonical bulk isotropy | **FAIL** | No independent bulk isotropy postulate in EDC; P-isotropy IS the assertion |
| 3 | Symmetry-breaking mechanisms | **MIXED** | Z₆ breaks membrane isotropy; other mechanisms compatible |

---

## 3. Failure Mode

**Circularity:** "Bulk Plenum rotational isotropy" is not an independent
canonical postulate. It IS P-isotropy — the postulate whose sub-component
(P-S2-direction) we are trying to derive. The formal postulate set P1–P6
does not contain SO(3) bulk symmetry. Using P-isotropy to derive a component
of itself is circular.

---

## 4. Completed P-Isotropy Decomposition

P-isotropy = P-U1-phase + P-S2-direction

| Component | Status | Source | Test |
|-----------|--------|--------|------|
| **P-U1-phase** | **[Dc]** | ξ gauge redundancy | Commit 58640bf — PASS |
| **P-S2-direction** | **[P]** | No independent derivation base | This test — FAIL |
| **P-isotropy (full)** | **[P]** | S² component blocks promotion | — |

**Interpretation:** P-isotropy's genuine physical content is P-S2-direction
alone. The U(1) phase component was always automatic from gauge structure.
The irreducible assertion is: "no physical mechanism selects a preferred
observed spin direction for a flux tube."

---

## 5. Final Postulate Count for 6π⁵

The 6π⁵ derivation chain retains **4 core postulates**:

| # | Postulate | Status | Change |
|---|-----------|--------|--------|
| 1 | P-σ | [P] | — |
| 2 | P-local-vertex | [P] | — |
| 3 | P-common-origin | [P] | — |
| 4 | P-isotropy | [P] | Decomposed: U(1) component [Dc], S² component [P] |

Postulate count: **4 [P]** (unchanged from pre-decomposition).

The decomposition did not reduce the count but clarified P-isotropy's
internal structure: its irreducible content is the S² direction invariance,
not the full S³ invariance.

---

## 6. What Would Be Needed

To close P-S2-direction, one would need one of:

| Route | Requirement | Available? |
|-------|-------------|------------|
| Independent SO(3) source | A postulate/derivation grounding 3D rotational symmetry of the Plenum, independent of P-isotropy | **No** |
| Dynamical isotropy | Show membrane action forces Plenum into isotropic config | **Not developed** |
| Statistical averaging | Show relevant energy scale averages over all S² directions | **Not developed** |

---

## 7. Z₆ Tension (Noted for Future Work)

The Z₆ lattice explicitly breaks membrane isotropy:
> "The 5D membrane is not isotropic — it has a preferred lattice structure."
> (Book II Ch. 4, line 46)

Any future derivation of P-S2-direction must address the relationship between
membrane spatial anisotropy (Z₆) and internal orientation isotropy
(P-S2-direction). These are logically independent constraints — Z₆ constrains
spatial positions while P-S2-direction concerns internal orientations — but
the tension should be explicitly resolved.

---

## 8. Bottom Line

P-S2-direction remains [P]. The P-isotropy decomposition program is now
complete:
- P-U1-phase: [Dc] (gauge-automatic, always derivable)
- P-S2-direction: [P] (genuine physical assumption, irreducible)
- P-isotropy: [P] (blocked by S² component)

The 6π⁵ derivation chain retains 4 core postulates. The decomposition did
not reduce the count but identified P-S2-direction as the irreducible
physical content of P-isotropy — a sharper characterization of what must
be postulated.
