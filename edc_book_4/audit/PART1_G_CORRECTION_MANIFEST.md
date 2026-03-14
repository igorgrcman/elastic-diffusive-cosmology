# Part I G-Formula Correction Manifest

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Scope:** Correction manifest only — no Part I text edited
**Status:** Complete; ready for future versioned action

---

## 1. Executive Verdict

Five locations in Part I were flagged during the G-formula tag spot-check after OPR-28.
**One is an immediate correction** (D11 claims table tag: `D` → `Dc`). **Four are
deferred enhancements** (rhetorical softening in titles, boxes, and summaries).

None involve false physics. The issues are labeling precision and rhetorical strength.
A future versioned correction pass is warranted — ideally as a minimal versioned patch
or an accompanying revision note.

---

## 2. Scope and Inputs

| Item | Detail |
|------|--------|
| **Basis** | `PART1_G_TAG_SPOTCHECK.md` (Part I G-formula tag spot-check) |
| **Published DOI** | `10.5281/zenodo.18176174` |
| **Purpose** | Future versioned correction planning only |
| **Constraint** | No Part I source files are modified by this manifest |
| **Epistemic baseline** | OPR-28 (`[I]` status for G exponent structure) |

This manifest is version-number agnostic. It does not prescribe whether the next
release is v17.50, v18.0, or an erratum. It provides the correction content; the
release vehicle is a separate editorial decision.

---

## 3. Governing Baseline

- Part I is **mostly internally honest** — Chapter 7 contains explicit caveats
  ("not rigorously derived," "consistency check only," "full derivation from 5D
  action is needed")
- The issues are **labeling precision and rhetorical strength**, not false physics
- The numerical result (`6.71 × 10⁻¹¹` vs `6.674 × 10⁻¹¹`) is correctly
  presented as a consistency check in Chapter 7
- Published text requires a **versioned or annotated correction path**, not silent
  source edits
- The OPR-28 exponent formula (`R_ξ¹²/(128π² σ r_e¹³)`) does not appear in Part I

---

## 4. Flagged Location Register

| ID | Location | File | Line(s) | Severity | Issue Type | Current Problem | Immediate or Deferred | Correction Style | Notes |
|----|----------|------|---------|----------|-----------|----------------|----------------------|-----------------|-------|
| F1 | Ch 0 claims table, D11 | `chapter_0_theory_core_V17.49.tex` | 1479 | **HIGH** | Formal tag | Status `D` for `G_N = c²/(4πσ)` — should be `Dc` (conditional on P6) | **IMMEDIATE** | Tag correction in claims table | KK reduction is derived; but the identification `G₅ = c²R_ξ/(2σ)` depends on postulate P6 |
| F2 | Ch 7 section title | `chapter_7_gravity.tex` | 220 | **MEDIUM** | Title wording | "Derivation of Newton's Constant" — body text disclaims being a derivation | **DEFERRED** | Title rewording | Body text caveats are honest; title is misleading relative to content |
| F3 | Ch 7 green main-result box | `chapter_7_gravity.tex` | 327–334 | **MEDIUM** | Box framing | Green "Main Result" box without formal `[I]` tag — visually signals positive derivation | **DEFERRED** | Add explicit status annotation or relabel box | Surrounding red and gray caveat boxes partially mitigate |
| F4 | Ch 6 roadmap box | `chapter_6_quantum_constants.tex` | 922 | **LOW** | Rhetorical wording | "is derived" — forward reference to Ch 7, which says it is NOT derived | **DEFERRED** | Wording change | Roadmap summary; secondary location |
| F5 | Epilogue | `epilogue.tex` | 29 | **LOW** | Rhetorical wording | "emerges from" — implies completed mechanism for a result framed as consistency check | **DEFERRED** | Wording softening | Summary chapter; tertiary location |

---

## 5. Immediate Corrections

### F1: Chapter 0 Claims Table D11 — Tag `D` → `Dc`

**Current text (line 1479):**
```
D11 & $G_N = c^2/(4\pi\sigma)$ (Newton's constant from tension) & D & P6, KK \\
```

**Recommended correction:**
```
D11 & $G_N = c^2/(4\pi\sigma)$ (Newton's constant from tension) & Dc & P6, KK \\
```

**Why immediate:**
- This is a **formal tag** in the claims registry — the most structurally load-bearing
  epistemic label in Part I for Newton's constant
- The tag `D` (Derived) implies unconditional derivation, but the formula depends on
  postulate P6 for the relationship between `G₅` and membrane tension `σ`
- The dependencies column already says "P6, KK" — the `Dc` tag makes this dependency
  explicit in the status column, which is currently inconsistent
- A reader consulting the claims table would conclude G is fully derived; this is
  stronger than the text warrants
- The correction is minimal (one character change: `D` → `Dc`) and creates no
  downstream ripple effects

**What `Dc` means here:** The KK reduction step `G₄ = G₅/(2πR_ξ)` is mathematically
derived. The subsequent identification `= c²/(4πσ)` requires `G₅ = c²R_ξ/(2σ)`,
which comes from postulate P6 (the 5D action with membrane tension). The full chain
is derived conditional on P6 — exactly what `Dc` means.

---

## 6. Deferred Enhancements

### F2: Chapter 7 Section Title

**Current:** "Derivation of Newton's Constant" (line 220)

**Problem:** The section itself contains a red caveat box explicitly stating the result
is "physically motivated through dimensional analysis and the Archimedean analogy,
not rigorously derived from a 5D hydrodynamic action." The title contradicts this.

**Candidate corrections:**
- "Newton's Constant from Membrane Parameters"
- "Towards Newton's Constant"
- "Newton's Constant: Dimensional Analysis and Consistency Check"

**Why deferred:** The body text caveats are strong enough that an attentive reader will
not be misled. The title is imprecise but not dangerous. This is a quality-of-labeling
issue suitable for a broader revision.

---

### F3: Chapter 7 Green Main-Result Box

**Current (lines 327–334):** Green `tcolorbox` titled "Main Result: Newton's Constant"
displaying `G = ℓ_P² c⁴/(σ r_e³)` without formal epistemic tag.

**Problem:** The green color + "Main Result" title visually signals a positive derivation
result. A reader scanning for key results would see this box and conclude G has been
derived. The surrounding red caveat box (lines 316–318) and gray consistency-check box
(lines 368–369) partially mitigate, but the green box itself lacks explicit status.

**Candidate corrections:**
- Add `[I]` tag inside the box title: "Main Result: Newton's Constant [I]"
- Relabel: "Consistency Check: Newton's Constant"
- Change box color from green to yellow/gray to signal non-derived status

**Why deferred:** The surrounding caveat boxes already provide honest framing. The
visual signal issue matters for scanning readers but is not a formal tag error.

---

### F4: Chapter 6 Roadmap Wording

**Current (line 922):** "Newton's constant is *not* fundamental. It is **derived** from
membrane tension at the topological scale"

**Problem:** "is derived" is too strong — Chapter 7 (which this refers to) explicitly
says it is not derived.

**Candidate correction:** "It is **expressed in terms of** membrane tension at the
topological scale" or "It is **proposed to arise from** membrane tension..."

**Why deferred:** This is a forward-looking roadmap box in Chapter 6. It is not where
a reader would go to assess the G formula's status. Low load-bearing weight.

---

### F5: Epilogue Wording

**Current (line 29):** "Newton's gravitational constant is not fundamental. It
**emerges from** the hierarchy between Planck and electromagnetic scales"

**Problem:** "emerges from" implies a completed mechanism. Chapter 7 frames the result
as a consistency check, not a completed emergence.

**Candidate correction:** "It is **proposed to emerge from** the hierarchy..." or
"It is **consistent with arising from** the hierarchy..."

**Why deferred:** Epilogue summary text. Low load-bearing weight. Suitable for
inclusion in a broader revision but not urgent.

---

## 7. Correction Types

| Type | Items | Description |
|------|-------|-------------|
| **Formal tag correction** | F1 | Claims-table status label change (`D` → `Dc`) |
| **Title-level wording correction** | F2 | Section title that contradicts body text |
| **Box/result framing correction** | F3 | Visual presentation of result box without epistemic tag |
| **Rhetorical consistency cleanup** | F4, F5 | Forward references and summaries using language stronger than source chapter |

---

## 8. Future Editorial Handling

The following handling modes are all acceptable for these corrections:

| Mode | Suitability | Notes |
|------|-------------|-------|
| **Minimal versioned patch** | GOOD | Suitable if only F1 is corrected; small diff, clean changelog |
| **Broader revision** | GOOD | Suitable if F1–F5 are all corrected together; coherent editorial pass |
| **Erratum note** | ACCEPTABLE | Could document F1 as a formal erratum on the Zenodo record |
| **Revision note** | ACCEPTABLE | Inline note in a future version explaining the tag correction |
| **Annotation layer** | ACCEPTABLE | Separate document listing corrections without modifying source |

**Recommended approach:** A **minimal versioned patch** correcting F1 (one-character
change in claims table) is the cleanest immediate action. F2–F5 can be bundled into
a broader revision whenever one is next planned.

**Not recommended:** Silent source edits without version increment. The published DOI
creates a contract with readers that the cited text matches what they access.

---

## 9. Not in Scope

This manifest explicitly does NOT:
- Change any Part I theory content
- Edit any Part I source files
- Perform any retroactive silent correction
- Force a specific release schedule or version number
- Introduce new physics claims or derivations
- Modify OPR-28 or any Book II content
- Address the standalone gravity manuscript (already assessed in PG-8.5)

---

## 10. Recommended Next Step

**Execute F1 as a minimal versioned Part I patch when next convenient.**

This means:
1. Change D11 status from `D` to `Dc` in the claims table
2. Increment version (number TBD by editorial decision)
3. Add a changelog entry documenting the tag correction
4. Upload to Zenodo as a new version of the existing record

F2–F5 can be deferred to a broader revision or addressed in the same patch if desired.
The editorial decision of "patch now" vs "wait for broader revision" is left to the
author.

---

## 11. Bottom Line

This manifest documents five flagged locations in Part I where G-formula tags or
rhetoric are stronger than warranted after OPR-28. One (D11 claims table tag) is an
immediate correction — a single-character change from `D` to `Dc`. Four are deferred
rhetorical enhancements. None involve false physics. The manifest is version-number
agnostic and ready for future editorial use whenever the next Part I revision is
undertaken.
