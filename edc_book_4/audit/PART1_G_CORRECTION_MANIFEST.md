# Part I G-Formula Correction Manifest

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Published DOI:** `10.5281/zenodo.18176174`
**Scope:** Correction manifest only — no Part I text edited
**Status:** Amended 2026-03-14 — circularity finding added from EDC_Trijaza_v1

---

## 1. Executive Verdict

Five locations in Part I were flagged during the G-formula tag spot-check after OPR-28.

**Amendment (2026-03-14):** `EDC_Trijaza_v1.md` (private repo, Phase B.4) formally
classified the Chapter 7 formula `G = ℓ_P² c⁴/(σ r_e³)` as **circular** — because
`ℓ_P = √(ℏG/c³)` contains `G`, making the formula `G` expressed as a function of `G`.
This upgrades F2 and F3 from DEFERRED/MEDIUM to **IMMEDIATE/HIGH**.

**Current priority:**
- **Three immediate corrections** (F1: D11 tag; F2: Ch 7 section title; F3: Ch 7
  result box — the latter two upgraded due to circularity)
- **Two deferred enhancements** (F4: roadmap wording; F5: epilogue wording)

The Chapter 7 issues are no longer merely rhetorical imprecision — the formula
itself is circular and must not be presented as a derivation in any future version.

---

## 2. Scope and Inputs

| Item | Detail |
|------|--------|
| **Basis** | `PART1_G_TAG_SPOTCHECK.md` (Part I G-formula tag spot-check) |
| **Circularity source** | `EDC_Trijaza_v1.md` (`EDC_Research_PRIVATE`, branch `restructure/paper3-companion-doi-split`, committed Phase B.4 `06f874d`, dated 2026-01-11) — formal classification of Ch 7 G formula as circular/rejected |
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
- **However**, the Chapter 7 formula `G = ℓ_P² c⁴/(σ r_e³)` is **circular** —
  `ℓ_P = √(ℏG/c³)` contains `G`, so the formula is `G` as a function of `G`.
  This was formally classified in `EDC_Trijaza_v1.md` (§4.6, January 11, 2026).
  The issues are therefore **both structural (circularity) and rhetorical**
- The numerical result (`6.71 × 10⁻¹¹` vs `6.674 × 10⁻¹¹`) is correctly
  presented as a consistency check in Chapter 7
- Published text requires a **versioned or annotated correction path**, not silent
  source edits
- The OPR-28 exponent formula (`R_ξ¹²/(128π² σ r_e¹³)`) does not appear in Part I
- **Note:** `EDC_Trijaza_v1.md` is a private research classification document,
  not a published result. The circularity finding is mathematically
  straightforward and verifiable independently

---

## 4. Flagged Location Register

| ID | Location | File | Line(s) | Severity | Issue Type | Current Problem | Immediate or Deferred | Correction Style | Notes |
|----|----------|------|---------|----------|-----------|----------------|----------------------|-----------------|-------|
| F1 | Ch 0 claims table, D11 | `chapter_0_theory_core_V17.49.tex` | 1479 | **HIGH** | Formal tag | Status `D` for `G_N = c²/(4πσ)` — should be `Dc` (conditional on P6) | **IMMEDIATE** | Tag correction in claims table | KK reduction is derived; but the identification `G₅ = c²R_ξ/(2σ)` depends on postulate P6 |
| F2 | Ch 7 section title | `chapter_7_gravity.tex` | 220 | **HIGH** ↑ | Title wording + circularity | "Derivation of Newton's Constant" — the formula presented is circular (`ℓ_P` contains `G`), not merely weakly derived | **IMMEDIATE** ↑ | Title rewording + circularity note | Upgraded from MEDIUM/DEFERRED: Trijaza circularity finding |
| F3 | Ch 7 green main-result box | `chapter_7_gravity.tex` | 327–334 | **HIGH** ↑ | Box framing + circularity | Green "Main Result" box displaying circular formula `G = ℓ_P² c⁴/(σ r_e³)` without tag or circularity warning | **IMMEDIATE** ↑ | Add circularity note, relabel box, add `[I]` tag | Upgraded from MEDIUM/DEFERRED: formula is circular, not just untagged |
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

## 6. Immediate Corrections — Chapter 7 Circularity (Upgraded)

### F2: Chapter 7 Section Title — UPGRADED from DEFERRED to IMMEDIATE

**Current:** "Derivation of Newton's Constant" (line 220)

**Original problem (pre-amendment):** The section title says "Derivation" while the
body text disclaims being a derivation.

**Upgraded problem (post-Trijaza):** The formula presented in this section,
`G = ℓ_P² c⁴/(σ r_e³)`, is **circular**. The Planck length `ℓ_P = √(ℏG/c³)`
contains `G` itself, so the formula is `G` expressed as a function of `G`. This is
not a weak derivation, a scaling argument, or a consistency check — it is a circular
identity. A section titled "Derivation" that presents a circular formula is
structurally misleading regardless of body-text caveats.

**Circularity chain:**
```
G = ℓ_P² c⁴ / (σ r_e³)
    │
    └── ℓ_P = √(ℏG/c³)
                │
                └── G  ← CIRCULAR
```

**Source:** `EDC_Trijaza_v1.md`, §4.6 (private repo, 2026-01-11)

**Candidate corrections:**
- "Newton's Constant: Dimensional Consistency Check" (preferred — accurate)
- "Newton's Constant from Membrane Parameters" (acceptable — avoids "derivation")
- Add an explicit circularity note at the start of the section

**Why now IMMEDIATE:** The issue is not merely rhetorical imprecision — the formula
is mathematically circular. No future Part I version should present this as a
derivation. The title must be corrected regardless of whether F4/F5 are addressed.

---

### F3: Chapter 7 Green Main-Result Box — UPGRADED from DEFERRED to IMMEDIATE

**Current (lines 327–334):** Green `tcolorbox` titled "Main Result: Newton's Constant"
displaying `G = ℓ_P² c⁴/(σ r_e³)` without formal epistemic tag.

**Original problem (pre-amendment):** Green color + "Main Result" title visually
signals a positive derivation result without an epistemic tag.

**Upgraded problem (post-Trijaza):** The formula displayed in the box is circular.
Presenting a circular identity in a green "Main Result" box — regardless of
surrounding caveats — is structurally misleading. The issue is not just a missing
tag; the formula itself cannot be a "result" in the derivation sense.

**Candidate corrections (in order of preference):**
1. **Relabel + recolor + add circularity note:**
   - Change title to "Consistency Check: Newton's Constant"
   - Change box color from green to yellow or gray
   - Add explicit note: "This formula is a dimensional identity, not a derivation:
     `ℓ_P` itself contains `G`"
   - Add `[I]` tag
2. **Minimal:** Add `[I]` tag + circularity footnote
3. **Conservative:** Add red caveat text inside the box noting circularity

**Why now IMMEDIATE:** A green "Main Result" box displaying a circular formula is
the single most misleading visual element in Chapter 7. Combined with the F2 title
issue, these two items represent the highest-impact corrections for any future
Part I revision.

---

### Deferred Enhancements

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
| **Circularity correction** | F2, F3 | Section title and result box present a circular formula as a derivation (upgraded from rhetorical to structural) |
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

**Recommended approach:** A **versioned patch** correcting F1, F2, and F3 together.
F1 is a one-character tag fix. F2 and F3 require title/box changes to remove
derivation framing from a circular formula. These three corrections are
co-equal immediate priorities. F4–F5 can be bundled or deferred.

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

**Execute F1 + F2 + F3 as a versioned Part I patch when next convenient.**

This means:
1. Change D11 status from `D` to `Dc` in the claims table (F1)
2. Rename Chapter 7 section from "Derivation of Newton's Constant" to
   "Newton's Constant: Dimensional Consistency Check" or similar (F2)
3. Relabel green "Main Result" box, add circularity note and `[I]` tag (F3)
4. Increment version (number TBD by editorial decision)
5. Add changelog entries documenting the tag correction and circularity fix
6. Upload to Zenodo as a new version of the existing record

F4–F5 can be deferred to a broader revision or addressed in the same patch if
desired. The editorial decision of "patch now" vs "wait for broader revision" is
left to the author.

---

## 11. Bottom Line

This manifest documents five flagged locations in Part I where G-formula tags or
rhetoric are stronger than warranted. **Three are now immediate corrections:**
F1 (D11 claims table tag: `D` → `Dc`), F2 (Chapter 7 section title presents
circular formula as "Derivation"), and F3 (green "Main Result" box displays
circular formula without warning). F2 and F3 were upgraded from DEFERRED/MEDIUM
to IMMEDIATE/HIGH after `EDC_Trijaza_v1.md` formally classified `G = ℓ_P² c⁴/(σ r_e³)`
as circular (`ℓ_P` contains `G`). Two items (F4, F5) remain deferred rhetorical
enhancements. The manifest is version-number agnostic and ready for future editorial
use whenever the next Part I revision is undertaken.
