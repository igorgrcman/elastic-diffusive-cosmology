# CONTAMINATION GUARD: Book IV Editorial Policy

**Date:** 2026-02-09
**Purpose:** Enforce NO 3D/SM policy in Book IV canonical text

---

## GUARDRAIL G1: Forbidden Vocabulary (Grep Gate)

### Banned Terms in Canonical Text

The following terms are **FORBIDDEN** in:
- `main.tex`
- `chapters/*.tex`
- `appendices/appA*.tex` through `appD*.tex`
- Glossary

```
# === HARD BAN (FAIL immediately) ===

# SM/particle words
Standard Model
SM (as abbreviation)
standardni model
fermion
boson
lepton
quark
hadron
baryon number
isospin
chirality
V-A
left-handed
right-handed
beta decay
β-decay
weak (as force)
electroweak
EW
CKM
PMNS
Yukawa
Higgs
gauge
coupling (as gauge coupling)
vertex
Feynman
matrix element
cross section
Weinberg
sin^2
theta_W
θ_W

# QCD/nuclear-model words
QCD
chromodynamics
gluon
color (as QCD color)
chrom
confinement (in SM sense)
shell model
shell (as nuclear shell)
magic number
spin-orbit
mean field
Fermi (as Fermi theory)
Hartree
Skyrme
Woods-Saxon
flux tube

# GUT/unification
SU(3)
SU(2)
U(1)
SO(10)
E6
E8
GUT
grand unif
Pati-Salam
Pati
Salam
Yang-Mills
Skyrmion

# === GUT/UNIFICATION ===
Pati-Salam
SO(10)
E6
E8
grand unif

# === ELECTROWEAK ===
electroweak
Weinberg
Salam (as in Glashow-Salam-Weinberg)
CKM
PMNS
Kobayashi
Maskawa
V-A
axial
W boson
Z boson
Higgs (as fundamental)
weak isospin
hypercharge

# === FERMION STRUCTURE ===
fermion generation
family (as in fermion family)
lepton
neutrino (as SM particle)

# === NUCLEAR PHYSICS (SM) ===
shell model
magic number
shell effect
shell closure
nuclear force (SM sense)
Coulomb barrier
strong force
strong interaction
PDG
Particle Data

# === QFT JARGON ===
beta function
running coupling
renormalization group
asymptotic freedom
confinement (QCD sense)
```

### Grep Command for Verification

```bash
#!/bin/bash
# Run from edc_book_4/

BANLIST="QCD|chromodynamics|gluon|Standard Model|SU\(3\)|SU\(2\)|U\(1\)|Yang-Mills|Skyrmion|Pati-Salam|SO\(10\)|electroweak|Weinberg|CKM|PMNS|V-A|axial|W boson|Z boson|Higgs|shell model|magic number|shell effect|Coulomb barrier|strong force|PDG|beta function|asymptotic freedom"

echo "=== Scanning canonical text for SM contamination ==="

# Scan chapters
grep -n -i -E "$BANLIST" chapters/*.tex

# Scan main
grep -n -i -E "$BANLIST" main.tex

# Scan appendices A-D only (Q and X are quarantine)
grep -n -i -E "$BANLIST" appendices/appA*.tex appendices/appB*.tex appendices/appC*.tex appendices/appD*.tex

echo "=== Expected: 0 hits ==="
```

Save as: `scripts/grep_contamination.sh`

---

## GUARDRAIL G2: Allowed Empirical Terms

### Permitted in Canonical Text

These terms ARE allowed (empirical/observational, not SM-theoretical):

| Term | Context | Constraint |
|------|---------|------------|
| proton | As observed particle | No SM structure |
| neutron | As observed particle | No SM structure |
| nucleus | As observed object | No SM force model |
| binding energy | Measured value | No SM derivation |
| half-life | Measured value | No SM derivation |
| decay | Observed process | No SM mechanism |
| α-particle | Observed entity | No SM interpretation |
| Geiger-Nuttall | Empirical formula | Label as [BL] baseline |
| τ_n = 880 s | Measured value | Label as [M] measurement |

### Required Framing

When using empirical data:
- Use "measured", "observed", "empirical"
- Do NOT use "predicted by SM", "QCD calculation", "shell model explains"
- Always tag with epistemic marker: [M], [BL], [Obs]

---

## GUARDRAIL G3: Quarantine Routing

### What Goes to Appendix Q

| Content Type | Example | Destination |
|--------------|---------|-------------|
| SM comparison | "In QCD, this corresponds to..." | Appendix Q |
| SM analogy | "Similar to flux tubes..." | Appendix Q |
| PDG citation | "PDG 2024 gives..." | Appendix Q |
| Fit to SM prediction | "Compared to shell model..." | Appendix Q |
| Nuclear force language | "Strong force binding..." | Appendix Q |

### What Goes to Appendix X

| Content Type | Example | Destination |
|--------------|---------|-------------|
| Non-binding analogy | "This is analogous to..." | Appendix X |
| Historical context | "Historically, this was called..." | Appendix X |
| Terminology mapping | "Z₆ ↔ baryon number" | Appendix X |

### Quarantine Box Template

```latex
\begin{quarantinebox}[title=Layer B: External Comparison]
    \textbf{Non-canonical:} [SM comparison here]

    This comparison is for orientation only and does not
    constitute a derivation or proof within EDC.
\end{quarantinebox}
```

---

## CHAPTER-SPECIFIC CLEANUP

### Chapter 1: Proton as Topological Ground State

**Source:** `04b_proton_anchor.tex`, `04c_routeB_z6_steiner.tex`

| Issue | Location | Action |
|-------|----------|--------|
| "QCD flux tubes" | If in source | → Appendix Q |
| "confinement (QCD)" | If in source | Rewrite as "topological confinement" |
| "quark" | If in source | → Appendix Q or omit |

### Chapter 2: Junction Symmetries

**Source:** `04c_routeB_z6_steiner.tex`, `M6_GEOMETRY_DERIVATION.md`

| Issue | Location | Action |
|-------|----------|--------|
| "3 generations" | §2.4-2.5 | → Book II |
| "CKM/PMNS" | §2.4-2.5 | → Book II |
| "V-A" | §2.4-2.5 | → Book II |
| "fermion family" | anywhere | → Book II |

### Chapter 5: M6 Lattice

| Issue | Location | Action |
|-------|----------|--------|
| "magic numbers" | §5.4 | Rewrite as "allowed coordinations" |
| "shell closure" | anywhere | Rewrite as "coordination boundary" |

### Chapter 7: κ = 2π

| Issue | Location | Action |
|-------|----------|--------|
| "Yang-Mills instanton" | §7.3 | → Appendix Q |
| "Skyrmion" | §7.3 | → Appendix Q |
| "BPST instanton" | anywhere | → Appendix Q |

### Chapter 13: Geiger-Nuttall

| Issue | Location | Action |
|-------|----------|--------|
| "Coulomb barrier" | anywhere | Rewrite as "empirical tunneling baseline" |
| "nuclear force" | anywhere | Omit or → Appendix Q |

---

## WORKFLOW FOR EACH CHAPTER

### Before Writing

1. Read source file(s)
2. Identify SM-contaminated sections
3. Plan routing: canonical vs Appendix Q vs Appendix X

### During Writing

1. Copy EDC-clean content to chapter
2. Rewrite SM-adjacent content in EDC terms
3. Route SM comparisons to quarantine boxes

### After Writing

1. Run `grep_contamination.sh`
2. Fix any hits
3. Verify epistemic tags present
4. Confirm source provenance noted

---

## QUALITY GATE CHECKLIST

Before marking chapter complete:

- [ ] `grep_contamination.sh` returns 0 hits
- [ ] All formulas have epistemic tag ([Der], [Dc], [P], [I], [BL], [M])
- [ ] Source file(s) cited in `\source{}` macro
- [ ] External comparisons in quarantine boxes only
- [ ] No "magic numbers" or "shell" language in canonical text
- [ ] No gauge group names (SU(n), SO(n)) in canonical text

---

**CONTAMINATION GUARD ACTIVE. Apply to all chapters.**

---

## DEFAULT BANLIST (applies to ALL chapters)

### TIER-1: Hard Ban (chapters must have 0 hits)

```bash
TIER1_REGEX="(standard model|\bSM\b|\bBSM\b|gauge|yang-?mills|\bYM\b|higgs|electroweak|weinberg|sin\^?2|ckm|pmns|neutrino|lepton|quark|gluon|fermion|boson|chirality|left-?handed|right-?handed|V-?A|yukawa|mass matrix|mixing angle|feynman|diagram|loop|tree-?level|propagator|vertex|beta function|running|renormaliz|counterterm|ward identity|SU\(|SO\(|U\(|E6|E_6|so\(10\)|so10|pati[- ]salam|\bPS\b|\bgut\b|grand unified|unification|hosotani|QCD|color|confinement|flux tube|bag model|skyrmion|chiral|pion|meson|shell model|magic number|mean field|hartree|fock|liquid drop|weizsacker|semi-?empirical|pairing|deformation|collective|nuclear force|strong force|weak force|electromagnetic force|coulomb barrier|as in standard physics|textbook|well-?known|it is known|as usual in nuclear physics)"

# Scan main text (must be 0 hits)
grep -RniE "$TIER1_REGEX" edc_book_4/chapters
```

### TIER-2: Soft Ban (allowed only in Appendix Q/X)

```bash
TIER2_REGEX="(textbook|well-?established|standard approach|as commonly done|as in the literature|Standard Model|QCD|electroweak|nuclear shell|magic number)"

# Scan main text (should route to Appendix Q/X if present)
grep -RniE "$TIER2_REGEX" edc_book_4/chapters
```

### ALLOWED LIST (EDC-core mathematics)

These terms are **ALLOWED** and should NOT be flagged:
- `Euclidean action`, `instanton`, `bounce`, `tunneling`, `WKB`, `Kramers`, `Langevin`, `double-well`
- `homotopy`, `pi_1`, `S^1`, `winding`, `topological charge`
- `Nambu-Goto`, `brane tension`, `Steiner`, `Plateau`, `minimal surface`, `Hessian`
- `Green's function`, `Laplacian`, `eigenvalue`, `boundary condition`
- `Kaluza-Klein` (only if used for pure geometry, not with gauge content)

### Per-Chapter Whitelist

| Chapter | Additional Allowed Terms |
|---------|-------------------------|
| Ch.1-17 | (none by default) |
| App.Q | TIER-1 terms allowed (quarantine) |
| App.X | TIER-2 terms allowed (analogies) |

### Quick Scan Commands

```bash
# Full TIER-1 scan (must return 0)
cd edc_book_4
grep -RniE "$TIER1_REGEX" chapters/ main.tex frontmatter/ | grep -v "^Binary"

# Per-chapter scan
grep -niE "$TIER1_REGEX" chapters/ch08*.tex

# Appendix policy check (Q/X may contain TIER-2)
grep -RniE "$TIER1_REGEX" appendices/ | grep -v "appQ\|appX"
```

---

---

## EDC-NATIVE VOCABULARY (Layer A)

**Principle:** In Book IV, "particles" are topological states of the brane (junction/loop excitations). SM and nuclear-model terms are forbidden in Layer A.

### Particle Translations

| SM Term (BANNED) | EDC Term (USE THIS) | Short Form |
|------------------|---------------------|------------|
| proton | Z₆ topological anchor junction | anchor junction |
| neutron | Z₃ metastable junction state | metastable junction |
| baryon | Y-junction defect | junction state |
| electron | S¹-loop excitation | loop state |
| positron | reverse-orientation loop | anti-loop |
| photon | transverse brane wave packet | brane wave |
| nucleus | pinned junction network (M₆) | pinning cluster |
| nucleon | junction constituent | constituent |

### Force/Interaction Translations

| SM Term (BANNED) | EDC Term (USE THIS) |
|------------------|---------------------|
| strong force | topological binding / pinning |
| weak force | junction transition / tunneling |
| nuclear force | pinning interaction |
| gauge boson | (avoid) → mode coupling |
| exchange particle | (avoid) → transition mechanism |

### Structure Translations

| SM Term (BANNED) | EDC Term (USE THIS) |
|------------------|---------------------|
| quark confinement | topological localization |
| nuclear shell | coordination boundary |
| magic number | stable coordination |
| binding energy | pinning energy |
| decay rate | tunneling rate |

---

## SCAN PROTOCOL

Before marking ANY chapter complete:

1. **Run TIER-1 scan** → must return 0 hits
2. **Run TIER-2 scan** → route any hits to Appendix Q/X
3. **Compile** → no LaTeX errors
4. **Verify epistemic tags** → all claims tagged

---

## LOCKED-IN POLICY (2026-02-09)

### PASS Criteria (MANDATORY)

```
PASS = 0 hits in Layer-A body (Ch1–Ch17)
     + 0 hits in titles/labels
     + 0 hits in appendices appA–appD
```

### ALLOWLIST (Permitted Zones Only)

| Zone | Permitted Content | Notes |
|------|-------------------|-------|
| Appendix Q | Quarantine/calibration content | Mark as [Cal] or [BL] |
| Appendix X | Non-binding SM analogies | Mark as non-canonical |
| Ch17 verbatim blocks | Scan command examples | Document as "scan tokens only" |

### CLEANUP PREFERRED (Non-Blocking but Target 0)

These are acceptable but should be eliminated when possible:

| Type | Example | Target |
|------|---------|--------|
| Comments with banned terms | `% SM comparison here` | Rewrite comments |
| Filename references | `NEUTRON_LIFETIME.md` | Accept (external) |
| EDC Book titles | "Book II pipeline" | Rephrase if possible |

### Canonical Banlist Regex

```bash
BAN_RE='(QCD|SU\(3\)|SU\(2\)|U\(1\)|gauge|boson|fermion|lepton|baryon|quark|gluon|hadron|isospin|CKM|PMNS|Standard Model|SM\b|nuclear|shell|magic number|Coulomb|Geiger|Nuttall|alpha decay|beta decay|weak|strong force|electromagnet|photon|electron|proton|neutron)'
```

### Verification Commands

```bash
# Full source scan (MUST be 0 Layer-A hits)
cd edc_book_4/
rg -c -i '\b(...BAN_RE...)\b' chapters/*.tex appendices/app[A-D]*.tex

# PDF scan (after compile)
pdftotext main.pdf - | rg -c -i '\b(...BAN_RE...)\b'

# Verify allowed-zone-only containment
rg -l -i '\b(proton|neutron|nuclear)\b' appendices/*.tex | grep -vE 'appX|appQ'
# Expected: 0 files
```

---

## TODO: Proof Obligations

### TODO-1: Closed-4 Minimality Proof

**Status:** OPEN

**Requirement:** Prove that the closed-4 (tetrahedral-like) connectivity is the minimal closed topology for junction networks, explaining:
- Why closed-4 is the smallest stable closed cluster
- Why it is the preferred emission unit in barrier-limited release
- Topological uniqueness argument

**Destination:** Chapter 11 (He-4) or dedicated appendix

### TODO-2: EDC-Native Ontology Standardization

**Status:** OPEN

**Requirement:** Create canonical vocabulary + preamble macros for all 5 books:
- Junction types: anchor, metastable, loop
- Cluster terminology: pinning network, coordination, frustration
- Process terminology: release, transition, tunneling
- Avoid all SM/nuclear-model vocabulary in Layer A

**Destination:** Shared preamble or Book 0 conventions

---

---

## OBSERVERBOX ALLOWANCE (Projection Labels Only)

### Purpose

The `observerbox` environment provides a controlled interface for mapping 5D EDC objects to 3D/4D observer measurement labels. This allows readers to connect EDC-native terminology to familiar labels WITHOUT introducing conventional mechanism explanations.

### Rules

1. **Exactly one observerbox per chapter** (ch01–ch17)
2. **Projection labels allowed ONLY inside observerbox:**
   - `proton`, `neutron`, `electron`, `positron`, `photon`
   - `observer`, `projection`, `shadow`, `measurement label`, `3D/4D`, `effective`, `recorded`, `measured`
3. **Forbidden EVERYWHERE (including observerbox):**
   - ALL mechanism/model words: QCD, gauge, weak, beta, decay, nuclear, nucleus, shell, magic, Coulomb, isospin, CKM, PMNS, fermion, boson, quark, gluon, neutrino, electroweak, strong force, half-life, etc.
   - The observerbox must NOT explain "why" using conventional theory
4. **Scan ignores observerbox content by design** (see scan wrapper below)

### Observerbox Template

```latex
\begin{observerbox}
Observer-side projection note: quoted terms are measurement labels for the
3D/4D projection of the 5D objects defined in this chapter; they do not
imply any conventional mechanism.

\begin{itemize}
    \item \AnchorJunction{} $\leftrightarrow$ ``proton'' (projection label)
    \item \MetastableJunction{} $\leftrightarrow$ ``neutron'' (projection label)
\end{itemize}

What the observer records: [description of measured quantity without forbidden words]
\end{observerbox}
```

### Scan Wrapper (Strips Observerbox Before Grep)

```bash
# Run from edc_book_4/
# Strips observerbox content, then runs contamination scan
perl -0777 -pe 's/\\begin\{observerbox\}.*?\\end\{observerbox\}//sg' \
    <(cat chapters/*.tex) | \
    grep -nEi '\b(proton|neutron|nuclear|electron|photon|weak|strong force|alpha decay|beta decay|quark|gluon|QCD|shell|magic number)\b' \
    || echo "PASS: 0 Layer-A violations (observerbox excluded)"
```

### Checklist Item

- [ ] Exactly one observerbox per chapter (verify: `grep -c 'begin{observerbox}' chapters/*.tex`)

---

## ONTOLOGY MACRO RULES (2026-02-10)

### Mandatory Macro Usage

In Layer A text (chapters + appendices A–D), authors MUST use EDC-native ontology macros instead of typing conventional particle names:

| Instead of typing... | Use this macro... |
|----------------------|-------------------|
| proton | `\AnchorJunction` |
| neutron | `\MetastableJunction` |
| electron | `\LoopState` |
| nucleus | `\ClusterState` |
| alpha particle | `\ClosedFour` |
| beta decay | `\JunctionTransition` |
| alpha decay | `\ClosedFourRelease` |
| nuclear | cluster, junction-network |

### Analogy Macros (Appendix X Only)

The `\AnalogProton`, `\AnalogNeutron`, etc. macros exist ONLY for use in Appendix X translation tables. They expand to the conventional name but signal intent.

**Do NOT use analogy macros in Layer A chapters.**

### Author Checklist

Before marking any chapter complete:

- [ ] Did you use `\AnchorJunction` / `\MetastableJunction` instead of typing "proton" / "neutron"?
- [ ] Did you use `\ClosedFour` instead of typing "alpha particle"?
- [ ] Did you use `\ClusterState` instead of typing "nucleus"?
- [ ] Did you route SM comparisons to Appendix Q?
- [ ] Did you route conventional name tables to Appendix X?
- [ ] Does the chapter pass the contamination grep scan?
- [ ] Are all empirical values tagged with `\tagBL` or `\tagM`?

### Canonical Reference

See `ontology/EDC_ONTOLOGY_CANON.md` for the complete dictionary and naming principles.

---

**POLICY LOCKED. Any relaxation requires explicit justification.**
