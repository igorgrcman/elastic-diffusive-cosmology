# Book II OPR G-Exponent Audit

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Audit Book II OPR registry for G-exponent problem; create or amend entry
**Status:** New entry created (OPR-28)

---

## 1. Executive Verdict

No OPR entry for the G-exponent problem existed in the formal Book II OPR register.
**OPR-28 has been created** in `edc_book_2/reorganized/appendices/opr_register.tex`
with status `[I]`, capturing the negative KK result, the non-uniqueness finding, and
the explicit upgrade condition.

The monograph (`TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex`) already contained BLOCK-003
and CLAIM-G-001, both correctly tagged `[I]`. These were consistent but informal —
the formal OPR register lacked the entry. That gap is now closed.

The reorganized Book II canonical chapters contain **no G-formula references** (Book II
is the weak sector). No tag corrections are needed in the reorganized chapters.

---

## 2. Scope and Inputs

**Inspected:**

| Source | Purpose |
|--------|---------|
| `edc_book_2/reorganized/appendices/opr_register.tex` | Formal OPR registry (12 entries: OPR-01, 04, 17, 19–27) |
| `edc_book_2/canon/opr/OPR_REGISTRY.md` | Markdown OPR registry (47 KB) |
| `edc_book_2/canon/opr/OPR-19.md` | Individual OPR file for g₅ |
| `edc_book_2/src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex` | Monograph with BLOCK-003 and CLAIM-G-001 |
| `edc_book_2/reorganized/part3/chapter_16_epistemic_summary.tex` | Epistemic summary chapter |
| `edc_book_2/reorganized/` (all `.tex` files) | Canonical chapters — searched for G formula |
| `book2-opr-registry-v1` branch | Checked for divergent registry state |

**Negative-result source basis:**

| Source | Location |
|--------|----------|
| `task_b5_power_derivation.md` | Private repo, branch `research/neutron-proton-mass-difference-5D` |
| `08_gravity_topological_ops.tex` | Private repo, `derivations/mass_difference/paper/framework/sections/` (now committed) |

---

## 3. Negative-Result Basis

The following key findings from `task_b5_power_derivation.md` govern this audit:

1. **Standard KK gives power −1, not +12.** The Kaluza-Klein dimensional reduction
   $G_4 = G_5/(2\pi R_\xi)$ yields $G \propto R_\xi^{-1}$, not $R_\xi^{+12}$.
   No known physical mechanism within the current 5D framework generates the
   required power 12.

2. **Exponent combinations are non-unique.** Multiple pairs $(n, m)$ satisfying
   the dimensional constraint $n + m = -1$ can fit $G_\mathrm{CODATA}$ by adjusting
   the geometric prefactor. The pair $(12, -13)$ is one such fit, not a unique
   determination.

3. **Derivation not achieved.** The document's own verdict: "INVESTIGATION COMPLETE —
   DERIVATION NOT ACHIEVED. Powers remain IDENTIFIED (I), not DERIVED (D)."

4. **Safe current status is `[I]`.** The exponent structure is an identified candidate
   form with numerical fit (~0.81% match), but it is neither derived from first
   principles nor uniquely constrained by EDC postulates.

---

## 4. OPR Registry Audit

### 4.1 Formal OPR Register (`opr_register.tex`)

**Did a G-exponent entry exist?** NO.

The register contained 12 entries (OPR-01, 04, 17, 19–27), organized into:
- Critical Problems: OPR-01 (σ), OPR-04 (δ), OPR-19 (g₅), OPR-21 (BVP)
- Electroweak Sector: OPR-20 (M_W), OPR-22 (G_F)
- Decay Processes: OPR-23 (V_B), OPR-24 (Z₃), OPR-25 (hadronic), OPR-26 (CP)
- Generation Structure: OPR-17, OPR-27

No "Gravity Sector Problems" section existed. The G formula, its exponents, and
the derivation problem were absent from the formal register.

### 4.2 Monograph BLOCK-003 and CLAIM-G-001

The `TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex` contains two correctly-tagged references:

| Identifier | Location | Content | Tag |
|-----------|----------|---------|-----|
| BLOCK-003 | Lines 690–696 | "G Formula Power Derivation — [I] — Identified by numerical fitting (0.8% match with CODATA), but NOT derived from 5D action" | `[I]` ✓ |
| CLAIM-G-001 | Line 2161 | "$G = c^4 R_\xi^{12}/(128\pi^2 \sigma r_e^{13})$ — Powers 12, 13 identified by fitting" | `\tagI{}` ✓ |
| BLOCK-003 (appendix) | Lines 2988–3002 | "Current status: [I] — Identified by fitting (0.8% match), not derived. Closure requirement: Rigorous 5D→4D reduction producing these powers." | `\tagI{}` ✓ |

These are correctly tagged `[I]` and contain honest assessments. However, they were
not linked to the formal OPR numbering system.

### 4.3 Markdown OPR Registry (`OPR_REGISTRY.md`)

Searched for Newton/gravitational/G/128/exponent references. Found only a passing
mention of "gravitational" in the context of σ derivation routes — no dedicated
G-exponent entry.

### 4.4 Problem Identified

The formal OPR register was **complete for the weak sector** (Book II's domain) but
had a **structural gap**: no gravity-sector entry. Since Book II explicitly references
the G formula in BLOCK-003 and CLAIM-G-001, and since the G-exponent problem is a
cross-sector open problem that appears in the monograph's blockers appendix, the OPR
register should include it.

---

## 5. OPR Action Taken

**Action: Created new entry OPR-28.**

**Location:** `edc_book_2/reorganized/appendices/opr_register.tex`

**What was added:**

1. A new section header "Gravity Sector Problems" (before "Electroweak Sector Problems")
2. OPR-28 entry with:
   - Status: `\tagI{}` (Identified by fitting; derivation not achieved)
   - Location: Part I gravity sector (cross-sector reference)
   - Dependencies: 5D action, dimensional reduction framework
   - Blocks: First-principles gravity-sector closure
   - Current formula: $G = c^4 R_\xi^{12}/(128\pi^2 \sigma r_e^{13})$, ~0.81% error
   - Problem statement: derive exponents and prefactor from 5D action / EDC primitives
   - Negative result: KK gives power −1, not +12
   - Non-uniqueness: multiple exponent pairs fit G_CODATA
   - Epistemic status rationale: why `[Dc]` and `[Cal]` are too strong, why `[I]` is safe
   - Upgrade condition: first-principles derivation or uniqueness proof
   - Source reference: `task_b5_power_derivation.md`
3. OPR-28 row in the summary table (status: `\tagI`, priority: Critical)
4. OPR-28 in the recommended priority order (after normalizations, before refinements)

---

## 6. Canonical Epistemic Lock

### Why `[Dc]` is too strong

`[Dc]` (Derived — Conditional) requires a closed derivation path, even if conditional
on upstream assumptions. No derivation path exists for the G exponents. The standard
KK route gives power −1, not +12. No alternative route has been identified. There is
no conditional derivation to point to.

### Why `[Cal]` is too strong for the exponent form

`[Cal]` (Calibrated) implies a unique functional form whose free parameters have been
fitted to data. But the exponent pair (12, −13) is NOT the unique form satisfying the
dimensional constraint $n + m = -1$. Multiple pairs can fit $G_\mathrm{CODATA}$ by
adjusting the geometric prefactor. Calibration presupposes a unique functional form to
calibrate — that uniqueness is absent here.

Note: `[Cal]` would be appropriate for the **numerical value** of G given the exponent
form (i.e., "if you accept powers 12, 13, then the formula matches G to 0.81%"). But
it is NOT appropriate for the exponent **structure** itself, which is the subject of
OPR-28.

### Why `[I]` is the safe current status

`[I]` (Identified) correctly describes the situation: a candidate formula has been
identified that numerically matches observation to ~0.81%. The formula's functional
form (including its exponents) was found by numerical fitting, not derived. It is not
known to be unique. This is exactly what `[I]` means in the EDC epistemic system.

---

## 7. Spot-Check of Book II Canonical Sections

### 7.1 Reorganized Book II Chapters

| Location | G Formula Present? | Current Tag | Consistent? | Notes |
|----------|-------------------|-------------|-------------|-------|
| `reorganized/part1/chapter_01_weak_interface.tex` | No | — | — | Weak sector; no G formula |
| `reorganized/part1/chapter_03_frozen.tex` | No | — | — | Frozen regime; no G formula |
| `reorganized/part1/chapter_04_z6_program.tex` | No | — | — | Z₆ program; no G formula |
| `reorganized/part2/chapter_09_neutrinos.tex` | No | — | — | Neutrino section; no G formula |
| `reorganized/part2/chapter_10_va_structure.tex` | No | — | — | V−A structure; no G formula |
| `reorganized/part2/chapter_11_ckm.tex` | No | — | — | CKM matrix; no G formula |
| `reorganized/part3/chapter_12_gf_chain.tex` | No (g₅ only) | — | — | Coupling chain; G_F not G |
| `reorganized/part3/chapter_14_bvp.tex` | No | — | — | BVP chapter; no G formula |
| `reorganized/part3/chapter_15_mw_gf.tex` | No (G_F only) | — | — | M_W and G_F; not Newton's G |
| `reorganized/part3/chapter_16_epistemic_summary.tex` | No | — | — | Epistemic summary; no G |
| `reorganized/appendices/opr_register.tex` | **YES** (OPR-28, just created) | `\tagI{}` | **YES** ✓ | Newly created; correctly tagged |
| `reorganized/appendices/notation.tex` | No G formula | — | — | Notation reference |
| `reorganized/appendices/numerical_standards.tex` | No G formula | — | — | Numerical standards |

**Result: No tag inconsistencies in reorganized Book II chapters.** The G formula does
not appear in the canonical weak-sector chapters (as expected — Book II covers the weak
sector, not gravity).

### 7.2 Monograph (`src/derivations/TOPOLOGICAL_PINNING_MONOGRAPH_v1.tex`)

| Location | Content | Current Tag | Consistent? | Notes |
|----------|---------|-------------|-------------|-------|
| Lines 690–696 (BLOCK-003) | G formula power derivation blocker | `[I]` | **YES** ✓ | Correctly states "Identified by numerical fitting, but NOT derived from 5D action" |
| Line 2161 (CLAIM-G-001) | G formula in claims registry | `\tagI{}` | **YES** ✓ | "Powers 12, 13 identified by fitting" |
| Lines 2988–3002 (BLOCK-003 appendix) | Detailed blocker entry | `\tagI{}` | **YES** ✓ | "Closure requirement: Rigorous 5D→4D reduction producing these powers" |

**Result: All monograph G-formula tags are already `[I]` and consistent.**

### 7.3 Other `src/` Files with G Formula References

| Location | Content | Current Tag | Consistent? | Notes |
|----------|---------|-------------|-------------|-------|
| `src/CH3_electroweak_parameters.tex` | May reference G | Not inspected in detail | UNKNOWN | Spot-check scope — would need deeper read |
| `src/sections/11_gf_derivation.tex` | G_F derivation (not Newton's G) | — | — | Not relevant |
| `src/sections/ch11_g5_ell_value_closure_attempt.tex` | g₅ value closure | — | — | About g₅, not G exponents |

---

## 8. Resulting OPR Entry Summary

**OPR-28: G Formula Exponent Derivation**

| Field | Content |
|-------|---------|
| **Status** | `[I]` — Identified by fitting; derivation not achieved |
| **Formula** | $G = c^4 R_\xi^{12}/(128\pi^2 \sigma r_e^{13})$, ~0.81% error |
| **Negative result** | Standard KK yields power −1 (not +12); no known mechanism produces power 12 |
| **Non-uniqueness** | Multiple exponent pairs $(n,m)$ with $n+m=-1$ fit $G_\mathrm{CODATA}$ |
| **Current epistemic status** | `[I]` (not `[Dc]`, not `[Cal]` for the exponent form) |
| **Upgrade condition** | First-principles derivation from 5D action uniquely producing powers 12, 13 and factor $128\pi^2$ |
| **Source** | `task_b5_power_derivation.md` (private repo) |
| **Priority** | Critical |
| **Blocks** | First-principles gravity-sector closure |

---

## 9. Remaining Tag-Correction Targets

**None identified in the reorganized Book II chapters.**

The G formula does not appear in the canonical weak-sector chapters. All existing
G-formula references in the monograph are already correctly tagged `[I]`.

**Potential future attention areas (not urgent):**

| Location | Issue | Priority |
|----------|-------|----------|
| `src/CH3_electroweak_parameters.tex` | Not deeply inspected — may mention G or gravity constants | LOW |
| Part I canonical text (outside Book II) | The G formula's primary home; not in scope for this audit | SEPARATE TASK |
| Standalone gravity manuscript (archived) | Already assessed in PG-8.5 — correctly uses `[I]` | NONE |

---

## 10. Recommended Next Step

**Spot-check Part I canonical text for G-formula tag consistency.**

OPR-28 is now locked in the Book II registry. The next logical step is to verify that
Part I's canonical presentation of the G formula (its primary home) also uses `[I]`
for the exponent structure, and to flag any locations that use `[Dc]` or `[Cal]` for
the exponents themselves.

---

## 11. Bottom Line

The Book II OPR register had no G-exponent entry despite the monograph correctly
identifying this as BLOCK-003 with `[I]` status. OPR-28 has been created with full
negative-result documentation, non-uniqueness finding, epistemic status rationale,
and upgrade condition. All existing G-formula tags in Book II are already consistent
(`[I]`). No tag corrections are needed in the canonical chapters. The G-exponent
problem is now epistemically locked at registry level with the correct status.
