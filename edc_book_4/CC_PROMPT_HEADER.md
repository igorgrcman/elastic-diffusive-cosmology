# CC PROMPT HEADER — Book IV Chapter Template

**Copy-paste this header at the start of every CC prompt for new chapters.**

---

## MANDATORY CONSTRAINTS (apply to ALL chapters)

### AC-C: Contamination Guard

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| AC-C1 | Compiles | `pdflatex main.tex` exits 0, no errors |
| AC-C2 | Clean scan | `grep -niE "$BANLIST" chapters/chXX*.tex` returns 0 hits |
| AC-C3 | Routing | Any SM/nuclear term → Appendix X (analogy) or Appendix Q (data) |

### Mini-Banlist (TIER-1 Hard Ban — Global)

```
BANLIST="(standard model|\bSM\b|QCD|quark|gluon|color|confinement|gauge|SU\(|SO\(|U\(|electroweak|higgs|yukawa|ckm|pmns|generations|fermion|lepton|boson|baryon number|isospin|shell model|magic number|mean field|woods.saxon|liquid drop|pairing|nuclear force|strong force|weak force|coulomb barrier|force carrier|exchange particle|point particle)"
```

### Mini-Banlist (Chapter-Local)

Each chapter prompt **MUST** define 5–15 additional terms specific to that chapter's topic.
This supplements the global banlist above.

**Example for Chapter 11 (He-4):**
```
LOCALBAN="(alpha particle|alpha decay|alpha cluster|shell closure|double magic|saturation|asymmetry energy|Coulomb|Weizsacker|semi-empirical|nucleon-nucleon|NN force|tensor force|spin-orbit)"
```

Run both scans:
```bash
grep -niE "$BANLIST" chapters/chXX*.tex; echo "---"; grep -niE "$LOCALBAN" chapters/chXX*.tex
```

### Acceptance Criteria Update

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| AC-C2a | Global scan | `grep -niE "$BANLIST"` returns exit code 1 (0 hits) |
| AC-C2b | Local scan | `grep -niE "$LOCALBAN"` returns exit code 1 (0 hits) |

### Routing Rules

| If you need... | Route to... |
|----------------|-------------|
| SM comparison / analogy | Appendix X (non-binding) |
| Fit coefficients / data | Appendix Q (quarantine) |
| PDG values, nuclear data | Appendix Q |
| Historical terminology | Appendix X |

---

## EDC-NATIVE VOCABULARY

Use these terms instead of SM/nuclear language:

### Particles → Topological States

| SM Term | EDC Term (Layer A) | Short Form |
|---------|-------------------|------------|
| proton | Z₆ topological anchor junction | anchor junction |
| neutron | Z₃ metastable junction state | metastable junction |
| baryon | Y-junction defect / junction state | junction |
| electron | S¹-loop excitation | loop state |
| positron | reverse-orientation loop | anti-loop |
| photon | transverse brane wave packet | brane wave |
| nucleus | pinned junction network (M₆ cluster) | pinning cluster |
| nucleon | junction constituent | constituent |

### Forces → Couplings

| SM Term | EDC Term |
|---------|----------|
| strong force | topological binding / pinning |
| weak force | junction transition / tunneling |
| electromagnetic | brane-mediated coupling |
| gauge boson | mode coupling / brane mode |
| exchange particle | (avoid — use "transition" or "coupling") |

### Structures → Geometry

| SM Term | EDC Term |
|---------|----------|
| quark confinement | topological localization |
| nuclear shell | coordination boundary |
| magic number | stable coordination |
| binding energy | pinning energy |
| decay rate | tunneling rate / transition rate |

---

## REQUIRED ELEMENTS IN EACH CHAPTER

1. **Abstract** — 3-5 sentences stating the chapter's goal
2. **Epistemic Tags** — Every claim tagged: [Der], [Dc], [P], [I], [BL], [OPEN], [Cal], [M]
3. **Forward/Backward refs** — Connect to adjacent chapters
4. **Epistemic Status Table** — At chapter end
5. **Falsifiability Hooks** — At least 3 concrete conditions
6. **Open Problems** — Explicit [OPEN] box if anything unresolved

---

## CHAPTER PREAMBLE (insert at line ~10 of each .tex file)

```latex
% Contamination guard: SM/nuclear-model terminology routed to Appendix X/Q.
% Layer A text uses EDC-native vocabulary only.
```

---

## QUALITY GATE CHECKLIST

Before marking chapter complete:

- [ ] AC-C1: Compiles without errors
- [ ] AC-C2: Contamination scan = 0 hits
- [ ] AC-C3: No SM terms in main text (routed if needed)
- [ ] All equations have epistemic tags
- [ ] Abstract present
- [ ] Forward references to next chapter(s)
- [ ] Epistemic Status Table present
- [ ] Falsifiability section present
- [ ] No internal file paths in PDF output

---

## EXAMPLE CC PROMPT STRUCTURE

```
CC PROMPT — Chapter N: [Title]

[Paste this header]

Goal: Fill edc_book_4/chapters/chN_*.tex with [description].

Source of Truth: [list .md or .tex files to pull from]

Required Sections:
- N.1 [Section name]
- N.2 [Section name]
- ...

Acceptance Criteria:
- AC-1: [specific to chapter]
- AC-2: [specific to chapter]
- AC-C1/C2/C3: (from header — always apply)

Output:
1. Filled .tex file
2. Compile log (success)
3. Contamination grep log (0 hits)
4. What changed (bullet list)
```

---

**END OF HEADER — Paste above into every new chapter prompt.**
