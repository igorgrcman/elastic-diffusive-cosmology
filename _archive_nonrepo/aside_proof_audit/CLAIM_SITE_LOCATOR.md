# CLAIM SITE LOCATOR

Quick reference for finding proof fragments in source files.

---

## PRIMARY SOURCES (edc_book_2/src/)

### Z6_content_full.tex

| Lines | Content | Status |
|-------|---------|--------|
| 1-43 | Prologue: Igor's original question | Context |
| 44-79 | Question decomposition | Context |
| 82-137 | **Step 1: Classical Steiner** | [M] |
| 94-121 | Theorem: Steiner 1834 | [M] PROVEN |
| 123-137 | Gap: Equal weights assumption | [OPEN] |
| 140-207 | **Step 2: Z6 Symmetry** | [P]→[Dc] |
| 155-166 | **POSTULATE: Z6-Invariant BC** | [P] |
| 168-187 | Lemma: Equal tensions from Z6 | [Dc] |
| 189-200 | Corollary: Steiner angles from Z6 | [Dc] |
| 202-207 | Gap: Origin of Z6 | [OPEN] |
| 210-355 | **Step 3: Hexagonal Packing** | [P]+[M]→[Dc] |
| 225-237 | Theorem: Kepler-Hales | [M] |
| 239-253 | **POSTULATE: Flux Tube Interactions** | [P] |
| 255-310 | Physical justification box | Motivation |
| 312-332 | Theorem: Hexagonal ground state | [Dc] from [P] |
| 334-341 | Corollary: Z6 emergence | [Dc] |
| 343-355 | Resolution: Z6 not ad-hoc | Summary |
| 358-542 | **Step 4: Proton Stability** | [Dc] |
| 371-429 | Bridge: Lattice to Y-junction | Explanation |
| 431-435 | **DEFINITION: Y-Junction (GEOMETRIC)** | [Dc] |
| 437-446 | Definition: Z6 potential | [Dc] |
| 448-461 | Proposition: Proton as Z3 fixed point | [Dc] |
| 463-488 | **THEOREM: Proton Stability (+Hessian)** | [Dc] |
| 490-527 | Figure: Proton as perfect lattice | Visual |
| 528-542 | Answer box: Q1 answered | Summary |
| 584-826 | **Step 5: Neutron as Dislocation** | [P]+[Dc]+[I] |
| 642-651 | **POSTULATE: Neutron = Dislocation** | [P] |
| 739-764 | Theorem: Dislocation energy | [Dc] |
| 750-764 | Proposition: Mass difference | [I] (calibration) |
| 827-843 | Theorem: Beta decay mechanism | [Dc] |
| 914-1013 | Theorem: Neutron lifetime from WKB | [Dc] |

### 02_frozen_regime_foundations.tex

| Lines | Content | Status |
|-------|---------|--------|
| 11-69 | Reader map, chapter overview | Context |
| 75-141 | EDC framework recap | [P] postulates |
| 86-108 | **POSTULATES: 5D bulk, membrane** | [P] |
| 143-214 | Ice wall analogy | Pedagogy |
| 220-293 | **Frozen vs GL comparison** | [Dc] |
| 245-253 | Frozen profile definition | [Dc] |
| 267-284 | Table: GL fails, frozen succeeds | [Dc] |
| 298-385 | Physical justification for frozen | [Dc] |
| 329-359 | Kinetic vs topological freezing | [Dc] |
| 390-546 | **Electron as frozen defect** | [Dc] |
| 422-447 | **THEOREM: Isoperimetric** | [M] |
| 449-486 | **THEOREM: Vol(B³) = 4π/3** | [Dc] |
| 488-520 | Proposition: Electron stability | [Dc] |
| 548-714 | **Proton as Y-junction** | [Dc] |
| 556-559 | 5D cause → 3D shadow | Framework |
| 592-628 | Theorem: 8 gluons from geometry | [M] |
| 636-663 | **THEOREM: Steiner equilibrium** | [M] |
| 670-692 | **THEOREM: Area(S³) = 2π²** | [M] |
| 694-713 | Theorem: Factorization (2π²)³ | [Dc] |
| 718-802 | **Mass ratio derivation** | [Dc] |
| 731-749 | Theorem: 6π⁵ identity | [M] |
| 751-775 | **THEOREM: m_p/m_e = 6π⁵** | [Dc] |
| 778-802 | Comparison with CODATA | [BL] check |
| 808-905 | **Fine-structure constant** | [Dc] |
| 846-866 | **THEOREM: α = (4π + 5/6)/6π⁵** | [Dc] |
| 869-892 | Comparison with CODATA | [BL] check |
| 910-937 | Numerical verification summary | [Cal] |

### 04b_proton_anchor.tex

| Lines | Content | Status |
|-------|---------|--------|
| 1-15 | Section header | Context |
| 10-15 | **POSTULATE: Proton-Anchor Stability** | [P] |
| 17-21 | Proposition: Consequence of stability | [Dc] |
| 30-37 | Energy functional definition | [P] |
| 39-51 | Core claim box (forward reference) | [Dc] |
| 53-69 | Forward reference to Z6 | Context |
| 85-106 | Status table of claims | Summary |
| 108-121 | Falsifiability hooks | Science |

---

## GREP PATTERNS FOR KEY CLAIMS

```bash
# Find Steiner theorem
rg -n "Steiner" --type tex

# Find Z6 postulate
rg -n "Z.*6.*Invariant|Z_6.*BC" --type tex

# Find proton stability theorem
rg -n "Proton.*Stability|proton.*minimum" --type tex

# Find Y-junction definition
rg -n "Y-junction|Y-Junction" --type tex

# Find homotopy mentions
rg -n "homotopy|\\pi_2" --type tex

# Find positive Hessian
rg -n "Hessian|second.*variation" --type tex

# Find topological minimum
rg -n "topolog.*minimum" --type tex
```

---

## CROSS-REFERENCES

| From | To | Type |
|------|-----|------|
| 04b_proton_anchor.tex:48 | Z6_content_full.tex Ch2 | Forward ref |
| 02_frozen_regime.tex:984 | Z6_content_full.tex | Forward ref |
| Z6_content_full.tex:48 | 02_frozen_regime.tex | Depends on |
| Z6_content_full.tex:636 | T1 (Steiner 1834) | Uses [M] |
| Z6_content_full.tex:463 | L3, L4, L5 | Depends on |

---

## FIGURE LOCATIONS

| Figure | File | Purpose |
|--------|------|---------|
| Proton as perfect lattice | Z6:490-527 | Visual proof element |
| Neutron as dislocation | Z6:652-737 | Comparison visual |
| Beta decay steps | Z6:846-905 | Mechanism diagram |
| Burgers vectors | Z6:617-640 | Hexagonal symmetry |
| Ice wall analogy | FR:164-194 | Pedagogical |

---

## EPISTEMIC TAG LOCATIONS

To find all epistemic tags:

```bash
# Find all [M] tags
rg -n "\\\\tagM|\\[M\\]" --type tex

# Find all [P] tags
rg -n "\\\\tagP|\\[P\\]" --type tex

# Find all [Dc] tags
rg -n "\\\\tagDc|\\[Dc\\]" --type tex

# Find all [I] tags
rg -n "\\\\tagI|\\[I\\]" --type tex

# Find all [BL] tags
rg -n "\\\\tagBL|\\[BL\\]" --type tex

# Find all [OPEN] or gaps
rg -n "\\\\tagOPEN|\\(open\\)|gapbox" --type tex
```
