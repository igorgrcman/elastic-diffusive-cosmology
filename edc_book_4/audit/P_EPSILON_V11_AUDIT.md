# P-ε v11 Audit

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Read-only inspection and classification of FAILURE_CERTIFICATE_v11.md
**Status:** Complete

---

## 1. Executive Verdict

**P-ε** is the core-density postulate `ρ₀ = σ/a` (with coefficient `C_ε = 1`)
used in the analytic derivation chain for `m_p/m_e = 6π⁵`.

**v11 closes** the last of 8 internal gaps in that derivation chain, promoting P-ε
from `[P]` (postulated) to `[Dc]` (derived conditional) via an energy-matching
dimensional argument.

**Closure type: Type 1 — Local closure within one derivation lane.**

The claimed closure is real within the ledger system (all 8 gaps that existed in v4
are now `[Dc]` or closed), but:
- The P-ε "derivation" is essentially a dimensional/definitional argument, not a
  deep physical derivation
- The specific derivation chain (4 postulates → 8 derived items → 6π⁵) has never
  been integrated into canonical Part I or Book II text
- The underlying result (`m_p/m_e = 6π⁵`) is already canonical and independently
  treated in both Part I Ch. 4 and Book II Ch. 2, with appropriate epistemic tags
- The ARCHIVE_REDISCOVERY_TRACKER already classified this analytic lane as
  "Preserved structural dead-end / constraint" (AR-01)

The v11 closure is historically/forensically valuable but does not change the
canonical epistemic status of any EDC result.

---

## 2. Scope and Inputs

### Files Inspected Directly

| File | Location | Purpose |
|------|----------|---------|
| `FAILURE_CERTIFICATE_v11.md` | `EDC_Research_PRIVATE/derivations/analytic/` | Primary target — v11 closure claim |
| `FAILURE_CERTIFICATE_v10.md` | same directory | Context — previous version (1 gap remaining) |
| `FAILURE_CERTIFICATE_v12.md` | same directory | Post-v11 continuation (neutron instability, separate topic) |
| `DERIVATION_LEDGER_v11.md` | same directory | Full ledger with dependency graph |

### Canonical Files Checked for Integration

| File | Location | What was checked |
|------|----------|-----------------|
| `chapter_4_leptons.tex` | `edc_book/chapters/` | Part I treatment of 6π⁵ and mass ratio |
| `chapter_02_ontology.tex` | `edc_book_2/reorganized/part1/` | Book II canonical treatment of E_p/E_e = 6π⁵ |
| `opr_register.tex` | `edc_book_2/reorganized/appendices/` | OPR entries — checked for P-ε or mass ratio OPR |
| `ARCHIVE_REDISCOVERY_TRACKER.md` | `edc_book_4/audit/` | Existing classification of analytic lane |
| `BASELINE_CONSTANTS_TABLE.tex` | `edc_book_2/reorganized/bridge/` | Baseline m_p/m_e value |

---

## 3. What Is P-ε?

### Definition

P-ε is one of several named postulates in the analytic derivation chain for
`m_p/m_e = 6π⁵`. It states:

$$
\rho_0 = \frac{\sigma}{a} \quad \text{with } C_\varepsilon = 1
$$

where:
- `ρ₀` is the core energy density of the electron defect
- `σ` is the membrane tension
- `a` is the characteristic core size
- `C_ε` is a dimensionless coefficient (claimed = 1)

### Role in the Derivation

P-ε determines the electron energy `E_e = (4π/3)σa²` by fixing the volume
energy density. Combined with the proton energy `E_p = ε₀ × Vol(Q)` from the
L-frozen mechanism, it feeds into the mass ratio:

$$
\frac{m_p}{m_e} = \frac{(2\pi^2)^3}{\frac{4\pi}{3}} \times \frac{\varepsilon_0}{\sigma a^2}
= 6\pi^5 \times \frac{\tau L}{\sigma a^2}
$$

With the scale-matching postulate `τL = σa²`, this gives `m_p/m_e = 6π⁵`.

### Canonical Status

- **P-ε as a named postulate** does NOT appear in any canonical text (Part I, Book II,
  or Book IV)
- The underlying physics (core density, membrane tension, electron energy) IS
  canonical — Part I Ch. 4 and Book II Ch. 2 both discuss the electron energy
- Part I Ch. 4 uses a different formulation: geometric scaling with α and κ₃q,
  not the L-frozen mechanism with explicit P-ε
- Book II Ch. 2 presents `E_p/E_e = 6π⁵` with `\tagDerSym{}` (model result derived)
  and identifies `m_p/m_e ≡ E_p/E_e` with `\tagDc{}`
- The ARCHIVE_REDISCOVERY_TRACKER (AR-01) classifies the analytic failure certificate
  program including P-ε as "Preserved structural dead-end / constraint" and
  "Not actionable for current Book IV V(q) program"

---

## 4. v11 Claim Reconstruction

### What v11 Claims

`FAILURE_CERTIFICATE_v11.md` claims:

1. **P-ε promoted from `[P]` to `[Dc]`** via two successful derivation routes:
   - Route 1 (Energy Matching): Surface energy density = volume density × depth → C_ε = 1
   - Route 2 (Thin-Shell): Shell physics ρ = σ/δ with δ = a → C_ε = 1
   - Route 3 (Virial): PARTIAL — scaling only, not coefficient
   - Route 4 (BPS): FAIL — EDC not BPS-like

2. **"ALL GAPS CLOSED"** — this is the last of 8 gaps tracked since v4:

| Gap | Description | Closed In |
|-----|-------------|-----------|
| Gap 1 | Frozen criterion | v5 |
| Gap 2 | S³ independence | v6 |
| P-junction | No θ at vertex | v7 |
| Gap 6 (P-scale) | τL = σa² | v8 |
| Gap D1 (ΔΩ) | State-cell | v8 |
| Gap 3 (P-SU2-sym) | SU(2)³ symmetry | v9 |
| Gap 4 (P-loc) | Electron localization | v10 |
| **Gap 5 (P-ε)** | **Core density** | **v11** |

3. **Final derivation status**: `m_p/m_e = 6π⁵` is `[Dc]` conditional on 4 core
   postulates: P-σ, P-local-vertex, P-common-origin, P-isotropy.

### What "ALL GAPS CLOSED" Refers To

"All gaps" means all 8 items that were tagged `[P]` (postulated without derivation)
in the v4 baseline have been promoted to `[Dc]` (derived conditionally). This is
an internal accounting closure within the ledger system — it means the derivation
chain from 4 core postulates to the 6π⁵ result has no remaining intermediate
assumptions that are merely asserted.

### What Was Missing Before v11

Before v11 (in v10), Gap 5 (P-ε) was the sole remaining `[P]`-tagged item. P-ε
stated `ρ₀ = σ/a` with coefficient `C_ε = 1` without justification. The v10
certificate explicitly noted this as "the last remaining gap" and rated it HIGH
difficulty.

### Critical Assessment of the P-ε "Derivation"

The v11 derivation of C_ε = 1 deserves scrutiny:

1. **Route 1 (Energy Matching):** Introduces "D23: Energy Matching: σ = ρ₀ · a"
   as a definition/axiom `[D]`, then immediately obtains `ρ₀ = σ/a`. This is
   essentially circular — the "derivation" assumes the very relation it claims
   to derive, repackaged as an energy matching principle.

2. **Route 2 (Thin-Shell):** States `ρ = σ/δ` (thin-shell physics) and sets
   `δ = a` (core thickness = core size). This is also definitional — it assumes
   the shell thickness equals the core size without independent justification.

3. **Both routes give C_ε = 1** because they both encode the same dimensional
   relationship `[σ/a] = [E/L³] = [ρ]`. The coefficient is 1 by construction
   of the matching condition, not by derivation from deeper principles.

4. **The claim that C_ε = 1 is "not fine-tuned"** (Section "Why C_ε = 1 is Not
   Fine-Tuned") is misleading. Dimensional analysis determines the functional
   form `ρ ∝ σ/a` but does NOT determine the numerical coefficient. The
   coefficient could be `4π/3`, `1/(2π)`, or any other O(1) number without
   violating dimensional analysis. The energy matching principle D23 is what
   fixes C_ε = 1, and D23 is introduced as an axiom.

**Conclusion:** The P-ε "derivation" is a dimensional/definitional argument
that repackages an assumption as a matching condition. It is internally
consistent but does not constitute a deep physical derivation. The "closure"
of Gap 5 is ledger-level closure, not physics-level closure.

---

## 5. Context in the Analytic Derivation Program

### What Derivation Lane This Belongs To

The v4–v11 certificate series documents the **5D analytic / action-from-principle
derivation program** for the proton-to-electron mass ratio. This program attempts
to derive `m_p/m_e = 6π⁵` from a minimal set of physical postulates using:

- The L-frozen mechanism (proton as frozen topological defect)
- Q = (S³)³ configuration space for 3-quark junction
- Energy additivity over Q with uniform density (L-frozen theorem)
- Electron as δ-localized membrane excitation with core density ρ₀

### How Central or Peripheral

**The underlying result (6π⁵) is central to EDC.** It is one of the flagship
predictions — the proton-to-electron mass ratio explained geometrically.

**The specific derivation chain in v11 is peripheral.** The canonical texts
(Part I Ch. 4, Book II Ch. 2) present the result via different routes:
- Part I Ch. 4: geometric scaling ansatz with α, connecting to Lenz's formula
- Book II Ch. 2: volume ratio `(2π²)³/(4π/3)` with `\tagDerSym{}`

The v11 chain adds intermediate physical justification (frozen criterion,
Q factorization, localization, core density) but this justification has never
been reviewed for canonical adoption.

### Character of the Result

The result is **mixed mathematical/physical/bookkeeping**:
- The geometric identity `(2π²)³/(4π/3) = 6π⁵` is pure mathematics `[M]`
- The physical assumptions (membrane tension, core density, localization) are physics
- The gap-closing ledger is bookkeeping
- The P-ε derivation specifically is closer to bookkeeping (dimensional definition
  repackaged as derivation) than to deep physics

---

## 6. Broader Repo Presence

### OPR Infrastructure

**P-ε does not appear in any OPR entry.** The OPR register has no entry for the
mass ratio derivation chain, the L-frozen mechanism, or the core density postulate.

OPR-28 (G Formula Exponent Derivation) is the closest OPR entry by topic area
(gravity sector), but it addresses Newton's constant, not the mass ratio.

### Canonical Books

| Location | How 6π⁵ Appears | How P-ε Appears |
|----------|-----------------|-----------------|
| Part I Ch. 4 | Extensively — Lenz connection, geometric scaling, α derivation | Not mentioned |
| Part I Ch. 10 (Summary) | Mass ratio table | Not mentioned |
| Book II Ch. 2 | `E_p/E_e = 6π⁵` with `\tagDerSym{}` | Not mentioned |
| Book II Ch. 1 | References 6π⁵ with `\tagDerSym{}` / `\tagDc{}` | Not mentioned |
| Book IV | Not directly | Not mentioned |

**6π⁵ is well-integrated canonically. P-ε is completely absent from canonical text.**

### Audit/Tracking Files

| File | How It References This |
|------|----------------------|
| `ARCHIVE_REDISCOVERY_TRACKER.md` (AR-01) | "5D analytic failure certificate (missing lemmas: P-sum, P-scale, P-epsilon_0)" — classified as "Preserved structural dead-end / constraint", "Not actionable" |
| `PRIVATE_REPO_PHASEB3_ANALYTIC_PRESERVATION_REPORT.md` | Lists failure certificates as preserved, notes v11 title |

### Companion Papers

No companion paper references P-ε or the specific v11 derivation chain.

### Other Derivation Notes

The analytic derivation cluster itself (85 files) contains the full v4–v12
certificate/ledger series. This is entirely internal to `derivations/analytic/`
in the private repo. v12 moves on to a separate topic (neutron instability
hardening) and does not revisit P-ε.

---

## 7. Closure-Type Classification

### Classification: Type 1 — Local closure within one derivation lane

### Justification

**Why Type 1 (not Type 2 or Type 3):**

1. **The closure is real within the ledger system.** All 8 gaps tracked since v4
   have been promoted from `[P]` to `[Dc]`. The internal accounting is complete.
   This rules out Type 3 (purely terminological) — actual mathematical/physical
   arguments were made at each step.

2. **The closure is local to the analytic derivation lane.** The specific
   derivation chain (4 postulates → 8 intermediate derivations → 6π⁵) has
   never been integrated into canonical text, has never been peer-reviewed
   outside the AI-assisted derivation sessions, and uses constructs (D23
   Energy Matching Principle, P-common-origin, P-local-vertex) that are not
   established canonical EDC postulates. This rules out Type 2.

3. **The P-ε derivation specifically is weak.** The "energy matching" argument
   is essentially dimensional analysis repackaged as a derivation. The coefficient
   C_ε = 1 is assumed via the matching condition D23, not derived from deeper
   physics. This is the kind of argument that closes an internal gap but does
   not constitute a publishable physical result.

4. **The underlying result is already canonical at the right epistemic level.**
   Book II Ch. 2 tags `E_p/E_e = 6π⁵` as `\tagDerSym{}` — meaning the *model*
   derives it (the volume ratio is mathematical), but the physical identification
   with the mass ratio is `\tagDc{}` (conditional). This is already the appropriate
   epistemic level. The v11 closure does not strengthen or change this canonical
   tag.

5. **The ARCHIVE_REDISCOVERY_TRACKER already classified this lane as non-actionable.**
   AR-01 explicitly says "Not actionable for current Book IV V(q) program" and
   "Only [review] if broader 5D analytic closure program is revived."

**Why not Type 2:**

Type 2 requires "clear evidence of canonical compatibility and broader relevance."
While the *result* (6π⁵) is canonically relevant, the specific *derivation chain*
that achieved "all gaps closed" introduces non-canonical constructs (D23, the
named postulate system P-σ/P-local-vertex/P-common-origin/P-isotropy), and the
P-ε step itself is dimensionally circular. There is no evidence that the v11
derivation chain adds canonical value beyond what Book II Ch. 2 already states.

**Why not Type 3:**

Type 3 would mean "ALL GAPS CLOSED" is purely terminological. It's not — each gap
closure involved specific mathematical or physical arguments (instanton barriers,
thin-brane limits, junction geometry). The closure is substantive within its own
framework, even though that framework is local.

---

## 8. Canonical Relevance Assessment

**Historically/forensically useful only.**

The v11 certificate is valuable as:

1. **A record of the derivation exploration.** The v4→v11 progression documents
   a systematic attempt to reduce the postulate count for 6π⁵ — this is genuine
   theoretical exploration, even if the final P-ε step is weak.

2. **A constraint on future work.** The failure of Route 4 (BPS) and the partial
   success of Route 3 (Virial) provide useful information for anyone attempting
   a deeper derivation of the core density.

3. **A provenance marker.** The analytic derivation program pre-dates the current
   Book IV work. If the Book IV program ever revisits the mass ratio derivation
   from the 5D action perspective, v11 documents what was previously attempted.

**It is NOT canonically relevant because:**

- The underlying result (6π⁵) is already canonical with appropriate tags
- The P-ε derivation does not strengthen the canonical epistemic status
- The derivation chain uses non-canonical constructs
- The ARCHIVE_REDISCOVERY_TRACKER already deferred this lane

---

## 9. Recommended Handling

**Primary recommendation: Tracker note only.**

Specifically:
- The existing AR-01 entry in `ARCHIVE_REDISCOVERY_TRACKER.md` already covers this
  material at the right level of detail
- No new OPR entry is warranted — the mass ratio is already well-tracked canonically,
  and P-ε is not a canonical open problem
- No canonical integration candidate review is needed — the canonical treatment in
  Book II Ch. 2 is already at the appropriate epistemic level
- No deeper derivation audit is needed now — the v11 closure is sufficiently
  understood from this inspection

If a future derivation program revisits the 5D action → mass ratio path, the v11
chain (and its weakness at the P-ε step) should be consulted as prior art.

---

## 10. Bottom Line

P-ε is the core-density postulate `ρ₀ = σ/a` in the analytic derivation chain for
`m_p/m_e = 6π⁵`. The v11 certificate closes the last internal gap by promoting P-ε
from `[P]` to `[Dc]` via an energy-matching dimensional argument. This is a **Type 1
local closure** — real within its own ledger system, but the P-ε derivation is
essentially definitional (dimensional analysis repackaged as a matching condition),
the derivation chain uses non-canonical constructs, and the underlying result is
already canonical in Book II at the appropriate epistemic level. The closure is
historically and forensically valuable but does not warrant canonical integration,
OPR action, or epistemic status changes. The existing AR-01 tracker entry already
covers this material at the right level.
