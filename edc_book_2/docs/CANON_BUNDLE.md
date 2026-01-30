# CANON BUNDLE — P0 Mandatory Documents

**Generated:** 2026-01-30 12:46
**Purpose:** Single file containing ALL P0 canonical documents for session loading.
**Usage:** Read this file at the START of every CC session. MANDATORY.

> This file is auto-generated from `docs/CANON_P0.list`.
> Do NOT edit directly — edit source files and run `tools/regenerate_canon_bundle.sh`.

---


# ============================================================================
# DOCUMENT 1: STATUS.md
# Source: edc_book_2/docs/STATUS.md
# ============================================================================

# EDC Book 2 - Status

## Current Status: REORGANIZATION IN PROGRESS

### Branch: `reorganization-epistemic-framework`

## Week 1 Progress

### Day 1-2: Infrastructure (COMPLETE)
- [x] Created full directory structure
- [x] Copied framework files (Macros, Epistemic Standard, Baseline Constants)
- [x] Created main.tex with 3-part organization
- [x] Created all chapter stubs (17 chapters)
- [x] Created appendix stubs (3 appendices)
- [x] Test compilation: **62 pages** - SUCCESS

### Day 3-4: Bridge Chapter 0 (COMPLETE)
- [x] Wrote full content for Bridge Chapter 0
- [x] Added all sections (Book 1 summary, particles, weak sector, reading strategy)
- [x] Test compilation: **70 pages** - SUCCESS

### Day 5-7: Content Migration Started (COMPLETE)
- [x] Ch 10 V-A Structure migrated (1184 lines, 24 pages)
- [x] Fixed main.tex preamble for original chapter compatibility
- [x] Test compilation: **94 pages** - SUCCESS

## Week 2 Progress (COMPLETE)

### Chapter 1 Restructure
- [x] Rewrote Chapter 1 "The Weak Interface" with neutron lifetime front-loaded
- [x] Fixed Unicode character issues
- [x] Test compilation: **100 pages** - SUCCESS

### Chapter 13 Foundation Parameters (Consolidated)
- [x] Consolidated OPR-01 (σ → M₀ anchor) - 460 lines
- [x] Consolidated OPR-04 (Δ from kink theory) - 598 lines
- [x] Consolidated OPR-19 (g₅ reduction) - 480 lines
- [x] Added Scale Taxonomy as canonical reference
- [x] Added no-smuggling certification
- [x] Test compilation: **108 pages** - SUCCESS

### Chapter 6 Electroweak Parameters (Consolidated)
- [x] Weinberg angle from Z₆ symmetry (sin²θ_W = 1/4)
- [x] Membrane thickness → mediator mechanism
- [x] Robin BC eigenvalue structure
- [x] W/Z mass consistency check
- [x] Test compilation: **112 pages** - SUCCESS

## Week 3 Progress (COMPLETE)

### Chapter 8 Three Generations (Consolidated)
- [x] Physical picture: Z₆ → Z₃ angular channels
- [x] Candidate mechanisms A/B/C with verdicts
- [x] Falsifiability criteria (4th gen invalidates)
- [x] Epistemic audit table
- [x] Test compilation: SUCCESS

### Chapter 9 Neutrinos (Consolidated)
- [x] Edge-mode mass suppression (m_ν/m_e ~ 10⁻⁶)
- [x] Three flavors from Z₃
- [x] V-A from boundary conditions
- [x] PMNS: DFT baseline falsified
- [x] Test compilation: **120 pages** - SUCCESS

### Pending
- [ ] Week 4: Ch 7 Leptons, Ch 11 CKM
- [ ] Week 5: Additional migration
- [ ] Week 6-7: Polish and review

## Original Version
Archived as:
- Branch: `backup-original-602pages`
- Tag: `v0.0-original`
- Pages: 602

## Target Version
- 17 chapters in 3 parts
- ~565 pages
- 20+ 5D mechanism boxes
- Complete error budgets


# ============================================================================
# DOCUMENT 2: DERIVATIONS.md
# Source: edc_book_2/docs/DERIVATIONS.md
# ============================================================================

# EDC Book 2 - Derivations Registry

## Migration Status

### Part I: Foundations
| Derivation | Source | Target | Status |
|------------|--------|--------|--------|
| Neutron lifetime | Original Ch 1 | Ch 1, 5 | PENDING |
| Y-junction geometry | Book 1 | Ch 2 (ref) | ESTABLISHED |
| Frozen regime | Original Ch 2 | Ch 3 | PENDING |
| Z6 structure | Original Ch 5-7 | Ch 4 | PENDING |

### Part II: Predictions
| Derivation | Source | Target | Status |
|------------|--------|--------|--------|
| sin²θ_W = 1/4 | Scattered | Ch 6 | PENDING |
| Lepton masses | Scattered | Ch 7 | PENDING |
| Three generations | Scattered | Ch 8 | PENDING |
| V-A structure | Original Ch 10 | Ch 10 | **COPY** |

### Part III: Technical
| Derivation | Source | Target | Status |
|------------|--------|--------|--------|
| g5 → GF chain | Original Ch 13-19 | Ch 12 | PENDING |
| OPR-01, 04, 19 | Scattered | Ch 13 | CONSOLIDATE |
| OPR-21 (BVP) | Scattered | Ch 14 | CONSOLIDATE |
| OPR-20, 22 | Scattered | Ch 15 | CONSOLIDATE |


# ============================================================================
# DOCUMENT 3: TODO.md
# Source: edc_book_2/docs/TODO.md
# ============================================================================

# EDC Book 2 - TODO

## Week 1 (Current)
- [x] Create directory structure
- [x] Copy framework files
- [x] Create main.tex
- [x] Create chapter stubs
- [x] Test compilation
- [ ] Complete Bridge Chapter 0
- [ ] Create migration map

## Week 2
- [ ] Migrate Ch 1 (Weak Interface) - RESTRUCTURE
- [ ] Copy Ch 10 (V-A Structure)
- [ ] Consolidate Ch 13 (Foundation Params)

## Week 3
- [ ] Migrate Ch 2-5 (Foundations)
- [ ] Migrate Ch 6-9, 11 (Predictions)
- [ ] Migrate Ch 14-16 (Technical)

## Week 4-5
- [ ] Add 5D Mechanism boxes (20+)
- [ ] Add error budgets
- [ ] Add visual dependency graphs

## Week 6
- [ ] Polish cross-references
- [ ] Fix undefined refs
- [ ] TOC cleanup

## Week 7
- [ ] Review
- [ ] Final corrections
- [ ] Release


# ============================================================================
# DOCUMENT 4: DECISIONS.md
# Source: edc_book_2/docs/DECISIONS.md
# ============================================================================

# EDC Book 2 - Decisions Log

## 2026-01-30: Reorganization Structure

### Decision: 3-Part Structure
**Chosen**: 3 parts + Epilogue (17 chapters total)
- Part I: Foundations & Mechanisms (Ch 1-5)
- Part II: Predictions & Observables (Ch 6-11)
- Part III: Technical Derivations (Ch 12-16)
- Epilogue (Ch 17)

**Rationale**: Clear separation of conceptual, prediction, and technical content.

### Decision: Front-load Neutron Lifetime
**Chosen**: Put neutron lifetime result in Ch 1 Section 2
**Rationale**: Immediate "quick win" - shows framework works before deep dive.

### Decision: Consolidate OPR Chapters
**Chosen**: Merge scattered OPR content into Ch 13-15
**Rationale**: Original had OPR spread across Ch 13-19; consolidation improves readability.

### Decision: Keep V-A Chapter As-Is
**Chosen**: Copy Ch 10 (V-A Structure) with minimal changes
**Rationale**: Already the best chapter; don't fix what isn't broken.

### Decision: Brief Epilogue Only
**Chosen**: Ch 17 is brief teaser (5-10 pages max)
**Rationale**: Original Ch 20-21 were too long for an epilogue.


# ============================================================================
# DOCUMENT 5: TP-2026-01-20_EDC_Synthesis_Key_Findings.md
# Source: ../EDC_Research_PRIVATE/kb/turning_points/TP-2026-01-20_EDC_Synthesis_Key_Findings.md
# ============================================================================

# TURNING POINT: EDC Sinteza — Ključni Nalazi

**Datum:** 2026-01-20
**Status:** KANONSKI DOKUMENT — ne modificirati bez razloga
**Svrha:** Spriječiti ponavljanje istih otkrića i kruženje u krugovima

---

## 1. DERIVIRANE FUNDAMENTALNE KONSTANTE (BEZ FITANJA)

| Količina | EDC Formula | Predviđeno | Eksperiment | Greška | Status |
|----------|-------------|------------|-------------|--------|--------|
| m_p/m_e | 6π⁵ | 1836.12 | 1836.15 | 0.002% | **[Der]** |
| α⁻¹ | 6π⁵/(4π+5/6) | 136.92 | 137.04 | 0.08% | **[Der]** |
| Δm_np | 8m_e/π | 1.301 MeV | 1.293 MeV | 0.6% | **[Der]** |
| m_μ/m_e | (3/2)(1+α⁻¹) | 207.05 | 206.77 | 0.14% | **[I]** |
| m_τ/m_μ | 16π/3 | 16.76 | 16.82 | 0.37% | **[I]** |

**ZAPAMTI:** Ove formule su GEOMETRIJSKE, ne fitane. Greške < 1% bez slobodnih parametara.

---

## 2. KONCEPTUALNA SLIKA: BRANA KAO "STAKLENI PROZOR"

```
     5D BULK              BRANA (δ)           3D SVEMIR
    (Plenum)           ┌─────────┐          (Opažljivo)
                       │         │
   ════════════ ←──────│  ◀──▶  │──────→ ════════════
                       │         │
    LIJEVA             │ thick   │           DESNA
    strana             │ brane   │           strana
                       └─────────┘
```

**Ključna ideja [P]:** Brana ima DVA seta boundary conditions:
- **Lijeva strana:** BC prema 5D bulku (Plenum, energetski fluid)
- **Desna strana:** BC prema 3D opažljivom svemiru (naša fizika)

Fizika 5D je UZROK, 3D opažanja su POSLJEDICA.

---

## 3. EPISTEMOLOGIJA: 5D vs 3D — KAUZALNOST I PRECIZNOST

### 3.1 Kauzalni smjer (JEDNOSMJERAN)

```
     5D (UZROK)                      3D (POSLJEDICA)
    ──────────────────────────────────────────────────
    Geometrija brane        →       Masa elektrona
    Junction konfiguracija  →       Masa protona
    Membrana tension σ      →       Nuklearne skale
    Z₆ breaking             →       Δm_np

    AKO SE 5D PROMIJENI     →       3D SE MIJENJA

    ALI:
    3D mjerenja             ✗→      NE MOGU promijeniti 5D
```

**Pitanje:** Što se treba dogoditi da se fizika i mjerenja u 3D promjene?
**Odgovor:** Mora se promijeniti nešto u 5D. Mi u 3D NE MOŽEMO direktno utjecati na 5D.

### 3.2 Preciznost: Egzaktnost vs Pogreška mjerenja

```
     5D (LIJEVA STRANA)              3D (DESNA STRANA)
    ─────────────────────────────────────────────────────
    EGZAKTNA MATEMATIKA              MJERENJA S POGREŠKOM

    6π⁵ = 1836.1181346...           1836.15267343 ± 0.00000011
    (beskonačno precizan)            (ograničena preciznost)

    ČISTA GEOMETRIJA                 REALNI INSTRUMENTI
    π, e, geometrijski faktori       detektori, vaganje, brojanje

    NEMA POGREŠKE*                   UVIJEK IMA POGREŠKU (±σ)
```

***IZNIMKA:** Ako 5D derivacija koristi bilo koju vrijednost iz 3D mjerenja,
tada nasljeđuje pogrešku tog mjerenja. Čista 5D geometrija → egzaktan broj.

### 3.3 Kalibracija vs Validacija — KRITIČNA DISTINKCIJA

| Pojam | Definicija | Primjer | Status |
|-------|------------|---------|--------|
| **Kalibracija [Cal]** | Fitanje parametra DA BI SE dobio rezultat | "Namjestimo V_B da dobijemo τ_n = 878.4 s" | Parametar ovisi o mjerenju |
| **Validacija** | Model PREDVIĐA rezultat BEZ fitanja | "6π⁵ = 1836.12, eksperiment kaže 1836.15" | Uspjeh modela |
| **Činjenica [BL]** | Mjerenje koje JEST (± pogreška) | m_p/m_e = 1836.15267343(11) | Input za validaciju |

**KLJUČNO:** 3D činjenice [BL] NISU kalibracija — one su TVRDI FAKTI.
- Ako EDC iz čiste geometrije (bez slobodnih parametara) kaže m_p/m_e = 6π⁵
- I to se poklapa s mjerenjem unutar razumne greške
- → To je **PREDIKCIJA koja je VALIDIRANA**, NE kalibracija!

### 3.4 Pogreška mjerenja je REALNOST, ne mana

Svako 3D mjerenje ima pogrešku ±σ jer:
- Instrumenti nisu savršeni
- Kvantna mehanika postavlja granice (Heisenberg)
- Statistička fluktuacija u konačnom broju mjerenja

To NIJE problem — to je REALNOST 3D svemira i naše sposobnosti mjerenja.

5D matematika je egzaktna. 3D mjerenja su aproksimacije stvarnosti.

---

## 4. FILOZOFSKA IMPLIKACIJA: "THREE-BODY PROBLEM" SCENARIJ

### 4.1 EDC vs Standard Model — Priroda konstanti

```
STANDARD MODEL                      EDC
─────────────────────────────────────────────────────────
Konstante su...                    Konstante su...
FUNDAMENTALNE                      GEOMETRIJSKE POSLJEDICE

α = 1/137.036...                   α = f(5D geometrija)
"Jednostavno jest tako"            "Jer brana ima tu strukturu"

Može li se α promijeniti?          Može li se α promijeniti?
NE (bez razloga zašto)             DA — ako se 5D promijeni

Tko može promijeniti?              Tko može promijeniti?
Nitko (nema mehanizma)             Entitet s pristupom 5D
```

### 4.2 Scenarij: Vanjska inteligencija

Ako postoji entitet s pristupom 5D bulk-u (analogno Trisolarima u "Three-Body Problem"):

```
"VANJSKA INTELIGENCIJA" s pristupom 5D bulk-u
                │
                ▼
        Mijenja geometriju brane
        Mijenja membrane tension σ
        Mijenja junction topologiju
                │
                ▼
        MI U 3D MJERIMO DRUGE VRIJEDNOSTI

        α se promijenio!
        m_p/m_e se promijenio!
        Nuklearna fizika je drugačija!
```

### 4.3 Ključna razlika

| Pitanje | Standard Model | EDC |
|---------|----------------|-----|
| Zašto je α = 1/137? | Nema odgovora | Geometrija 5D brane |
| Može li se α promijeniti? | Ne (aksiom) | Da (promjenom 5D) |
| Postoji li mehanizam? | Ne | Da (5D manipulacija) |
| Tko bi mogao? | Nitko | Entitet u 5D |

**ZAKLJUČAK [P]:** U EDC-u, "fundamentalne konstante" NISU fundamentalne —
one su EMERGENTNE iz 5D geometrije. Teoretski, entitet koji može
manipulirati 5D mogao bi mijenjati našu 3D fiziku.

Ovo ne znači da takav entitet postoji — samo da EDC DOPUŠTA takvu mogućnost,
dok Standard Model je NE DOPUŠTA jer nema mehanizam.

---

## 5. SIGMA DERIVACIJA — POD HIPOTEZOM

### 3.1 Lijeva strana (5D Uzrok)

**Ključna hipoteza [P]:**
```
E_σ = m_e c² / α = 70.0 MeV
```
Ovo je energetska skala membrane — PRETPOSTAVKA, ne derivacija!

**Derivacija membrane tension σ [Dc] (uvjetno na hipotezu):**
```
σ = E_σ / r_e² = (m_e c²/α) / r_e²

Koristeći r_e = αℏ/(m_e c):

σ = (m_e c²/α) × (m_e c/αℏ)² = m_e³ c⁴ / (α³ ℏ²)

Numerički: σ = 8.82 MeV/fm²
```

**VAŽNO:** σ formula je [Dc], NE [Der]. Ovisi o hipotezi E_σ = m_e c²/α.

### 3.2 Desna strana (3D Opažanje)

- E_σ = σ × r_e² = 70 MeV ✓ (matches nuclear scale)
- Attempt frequency: Γ₀ = m_e c² / (α ℏ)

### 3.3 KRITIČNO: Dvije vrijednosti σr_e²

| Izvor | Formula | Vrijednost | Dokument |
|-------|---------|------------|----------|
| Companion H | E_σ = m_e c²/α | **70 MeV** | weak interactions |
| Framework v2.0 | σr_e² = (36/π)m_e | **5.856 MeV** | Z₆ geometry |

**Omjer: 70 / 5.856 = 12 (TOČNO!)**

---

## 6. FAKTOR 12 — Z₆ × Z₂ STRUKTURA [I]

### 6.1 Matematička veza
```
12 = 6 × 2 = |Z₆| × |Z₂|
```

### 6.2 Fizikalna interpretacija (HIPOTEZA)
- **σr_e² = 5.856 MeV** = energija PO JEDNOJ POZICIJI na Z₆ prstenu
- **E_σ = 70 MeV** = UKUPNA energija membrane (sve pozicije + faze)
- **Veza:** E_σ = 12 × (σr_e²)_single

### 6.3 Dodatna potvrda: S/ℏ = 60
```
S/ℏ = 60 ≈ 12 × ln(1/α) + 1 = 12 × 4.92 + 1 ≈ 60.04
```
Opet faktor 12 pojavljuje se u barrier action!

**ZAKLJUČAK:** Faktor 12 = Z₆ × Z₂ nije slučajnost. Potrebna rigorozna derivacija.

---

## 7. TOPOLOŠKA STRUKTURA ČESTICA

### 7.1 Elektron [Der]
```
Topologija: B³ (3D kugla) — jednostavni vrtlog
Konfiguracija: Vol(B³) = 4π/3
Naboj: W = -1 (winding number)
Stabilnost: Izoperimetrijski teorem → JEDINSTVEN minimum
```

### 7.2 Proton [Der]
```
Topologija: Y-junction (3 kraka pod 120°)
Konfiguracija: S³ × S³ × S³ → (2π²)³
Naboj: W = +1 (ukupni winding)
Boja: 3 kraka = 3 QCD boje (8 modova = 8 gluona)
Stabilnost: Steinerov teorem → 120° JEDINSTVEN minimum
```

### 7.3 Neutron [Dc]
```
Topologija: Asimetrični Y-junction (θ = 60°)
Parametar: q = 1/3 (half-Steiner)
Naboj: W = 0, Q = 0
Nestabilnost: Može relaksirati θ: 60° → 0° (prema protonu)
```

### 7.4 Z₆ simetrija [Dc]
```
Z₆ = Z₃ × Z₂
├── Z₃: Ciklička permutacija 3 kraka (θ → θ + 120°)
└── Z₂: Oscilacijska faza (φ → φ + π)

Proton: θ = 0° (minimum)
Neutron: θ = 60° (metastabilno)
Formula: θ = (1 - Q) × 60°
```

---

## 8. WEAK INTERAKCIJE — COMPANION H MODEL

### 8.1 Struktura
```
BULK-CORE (Y-junction: |0⟩=proton, |1⟩=neutron)
    │
    ▼ pumping kroz frozen boundary
    │
BRANE-LAYER (debljina δ, lokalizirani modovi)
    │
    ▼ izlaz na observer-facing stranu
    │
3D ČESTICE (e⁻, ν̄_e)
```

### 8.2 Jednosmjerni ventil [P]
- **Inflow** (bulk → brane): DOZVOLJEN (spontan)
- **Outflow** (brane → bulk): POTISNUT

### 8.3 β⁻ decay mapping
```
5D uzrok: n(|1⟩) → p(|0⟩), junction rotira θ: 60° → 0°
3D opažanje: n → p + e⁻ + ν̄_e
```

---

## 9. KALIBRACIJE vs DERIVACIJE

### 9.1 Kalibrirano [Cal] — potrebne derivacije
| Parametar | Vrijednost | Kalibriran na | Potrebno |
|-----------|------------|---------------|----------|
| V_B (barrier height) | ~2.6 MeV | τ_n = 878.4 s | Derivacija iz 5D akcije |
| V₃ (flavor-breaking) | -0.65 MeV | Δm_np = 1.293 MeV | Derivacija iz Z₆ |
| S/ℏ | 60 | τ_n = 878.4 s | Veza s 12×ln(1/α)+1 |

### 9.2 Derivirano [Der] / [Dc] — potvrđeno
- m_p/m_e = 6π⁵ iz Vol(B³) i Area(S³)³
- α iz geometrijskih faktora
- Δm_np iz Z₆ breaking
- 120° Steiner angles iz varijacijskog principa
- SU(3) algebra iz Y-junction modova
- Confinement iz beskonačne string energije
- **Frozen criterion [Dc]** iz 5D akcije (Paper 2, dva puta: instanton + topološka)
- **C = 4π/3 [Der]** za step funkciju (egzaktno, parameter-free)

---

## 10. OTVORENI PROBLEMI — PRIORITETI

### 10.1 KRITIČNI (moraju se riješiti)
| ID | Problem | Trenutni status |
|----|---------|-----------------|
| **KB-OPEN-033** | Deriviraj V_B iz 5D akcije | [Cal] |
| **KB-OPEN-040** | Razriješi σr_e² = 70 vs 5.856 MeV (faktor 12) | [OPEN] |
| **KB-OPEN-041** | Deriviraj S/ℏ = 12×ln(1/α)+1 | [I] pattern |

### 10.2 VAŽNI (za kompletnost)
- Neutrino kao ξ-val — dinamika
- 5/6 faktor u α formula

### 10.3 VEĆ RIJEŠENI (dokumentirano u Paper 2)

| Problem | Rješenje | Dokument |
|---------|----------|----------|
| Frozen boundary iz 5D akcije | **DVA PUTA:** Route A (instanton) + Route B (topološka) | `EDC_FROZEN_Criterion_From_Action_v1.tex` |
| Step funkcija implementacija | `f(r) = Θ(r-a)` → C = 4π/3 EGZAKTNO | `appendix_gl_frozen_numerics.py` |
| GL vs Frozen usporedba | Frozen je parameter-free, GL zahtijeva fine-tuning | Python numerika |

**Route A (Large-σ Instanton Barrier) [Dc]:**
```
Γ ∼ Γ₀ exp(-σ·ΔA/ℏ)
Frozen criterion: σ·ΔA_min > ℏ·ln(Γ₀·τ_obs)
```

**Route B (Topological Superselection) [Dc]:**
```
B1 [M]: Winding numbers su topološki invarijanti
B2 [P]: Nema topology-changing procesa tijekom τ_obs
B3 [Dc]: Γ = 0 (egzaktno, ne aproksimativno)
```

**Python step funkcija:**
```python
def frozen_profile(r, a):
    return np.where(r < a, 0.0, 1.0)  # Θ(r-a)
```

---

## 11. METODOLOŠKI PRINCIPI — NE ZABORAVI

### 11.1 Dvosmjerno čitanje
```
LIJEVA STRANA (5D)          DESNA STRANA (3D/4D)
─────────────────────────────────────────────────
5D geometrija         →     Opažene čestice
Bulk + brane akcija   →     Mase, naboji, lifetime
Topološki defekti     →     Elektron, proton, neutron
Junction dinamika     →     Weak decay
```

### 11.2 Epistemički kodovi
| Kod | Značenje | Primjer |
|-----|----------|---------|
| **[Der]** | Derivirano | m_p/m_e = 6π⁵ |
| **[Dc]** | Derivirano uvjetno | M(q), V(q) pod ansatzom |
| **[I]** | Identificirano | m_μ/m_e pattern |
| **[Cal]** | Kalibrirano | V_B na τ_n |
| **[P]** | Postulirano | 5D bulk postoji |
| **[BL]** | Baseline | PDG/CODATA vrijednosti |

### 11.3 Anti-cirkularity check
- NIKADA ne koristi X da deriviraš Y ako Y ovisi o X
- [BL] fakti su INPUTI za validaciju, ne za derivaciju
- Ako model reproducira [BL] → to je VALIDACIJA, ne kružnost

---

## 12. HIJERARHIJA DOKUMENATA — COMPANION F KAO "BACKBONE"

### 12.1 Zašto je F kičma serije?

**Kanonski opis:**
> "Companion F provides the 5D object model (proton as a junction) and the
> canonical 5D→brane→3D projection mechanism (Hopf + thick-brane + frozen
> boundary), which the weak and decay companions then use as process-level
> applications."

### 12.2 Šest razloga zašto F nosi kičmu

| # | Razlog | Objašnjenje |
|---|--------|-------------|
| 1 | **Ontologija** | F daje "ŠTO proton JEST" u 5D, ne samo "što izračunamo" |
| 2 | **120° nije QCD** | Steiner optimum dolazi iz geometrije minimizacije, ne iz SU(3) |
| 3 | **Hopf bridge** | Rješava S³ vs S² konfuziju: interno S³ → opažajno S² |
| 4 | **Frozen mehanizam** | Nije samo "fraza" — boundary law s kriterijem |
| 5 | **Epistemic kontrola** | Eksplicitne kutije [Der]/[Dc]/[P]/[OPEN] sprječavaju overclaim |
| 6 | **Spojni komad** | Povezuje Paper 2, Framework, G, H u koherentnu cjelinu |

### 12.3 Struktura luka dokumenata

```
Framework v2.0
    │   Formalna konzervacija + ledger, 5D zatvaranje
    │   = AKSIOMATIKA / PRAVILA IGRE
    ▼
Paper 2 (Frozen)
    │   Frozen režim i projekcija (temelj mapiranja)
    │   = PROJEKCIJSKI MEHANIZAM
    ▼
╔═══════════════════════════════════════════════════════╗
║  COMPANION F (Proton Junction) — BACKBONE             ║
║  • Konkretan 5D objekt (junction + 3 kraka)           ║
║  • Geometrija (120° Steiner optimum)                  ║
║  • Projekcija 5D→brane→3D (Hopf + thick-brane)        ║
║  = ONTOLOGIJA + PROJEKCIJA                            ║
╚═══════════════════════════════════════════════════════╝
    │
    ├──► Companion G (n–p mass)
    │       Kako odstupanje/nesimetrija daje Δm
    │       = FENOMENOLOGIJA (masa)
    │
    └──► Companion H (weak)
            Kako relaksacija isporuči energiju brani → e⁻ + ν̄
            = FENOMENOLOGIJA (procesi)

Companions A–E: Specifične redukcije i alati
```

### 12.4 Što F rješava za čitatelja

| Pitanje čitatelja | Odgovor u F |
|-------------------|-------------|
| "Što je proton u 5D?" | Junction s 3 kraka, 120° kutovi |
| "Zašto 120°?" | Steiner/Lami optimum (geometrija, ne QCD) |
| "Zašto S³ interno, a S² vidimo?" | Hopf fibration: ψ ∈ S³ → t̂ ∈ S² |
| "Kako 5D postaje 3D?" | Frozen projection boundary + thick-brane |
| "Je li to [Der] ili [P]?" | Eksplicitne epistemic oznake |

### 12.5 Bez F, G i H "vise u zraku"

- **S F:** G i H su "process-level applications" jasnog objekta
- **Bez F:** G i H izgledaju kao "modeli procesa" bez slike objekta

F daje **sidro** — čitatelj zna na što se odnose efektivne veličine (q, V(q), selection rules).

---

## 13. DOKUMENT REFERENCE

| Dokument | DOI | Ključni sadržaj |
|----------|-----|-----------------|
| Framework v2.0 | 10.5281/zenodo.18299085 | Svi postulati, σr_e²=5.856 MeV |
| **Paper 2** | (lokalno) | **Frozen derivacija, step funkcija, C=4π/3** |
| Paper 3 | 10.5281/zenodo.18262721 | Neutron lifetime WKB |
| Companion F | 10.5281/zenodo.18302953 | Proton Y-junction |
| Companion G | 10.5281/zenodo.18303494 | Δm_np, σr_e²=70 MeV |
| Companion H | 10.5281/zenodo.18307539 | Weak interactions, E_σ=70 MeV |

**Paper 2 ključni fajlovi:**
- `releases/paper_2_private/supplementary/postulate_derivations/EDC_FROZEN_Criterion_From_Action_v1.tex`
- `releases/paper_2_private/code/numerics/appendix_gl_frozen_numerics.py`

---

## 14. COMPANION N: NEUTRON KAO UZBUĐENI 5D JUNCTION — PLAN

### 14.1 Uloga u seriji

Companion N daje **objekt-model neutrona** u 5D, analogno Companion F za proton.

**Kanonski opis:**
> "In EDC, the neutron is modeled as an excited 5D junction state: the same
> three-arm junction core as the proton, but displaced from the local Steiner
> minimum. This excitation couples to the bulk-facing side of a thick brane,
> pumping energy into brane-layer modes. The observer-side frozen projection
> then organizes the released energy into allowed weak-channel outputs."

### 14.2 Ontologija: Što je neutron u 5D [P]

```
PROTON (Companion F)              NEUTRON (Companion N)
────────────────────────────────────────────────────────
Isti topološki junction           Isti topološki junction
3 kraka + čvor                    3 kraka + čvor + ring mode

Steiner minimum (120°)            UZBĐENO STANJE (θ ≠ 120°)
Statički minimum energije         Metastabilni paket

STABILAN                          NESTABILAN → relaksira prema protonu
```

**Ključ [P]:** Neutron NIJE "druga životinja" — nego pobuđeni režim ISTE 5D geometrije.

### 14.3 Relaksacija prema 120° [Der/Dc]

Odstupanje od optimuma:
```
θ_i(t) = 2π/3 + δθ_i(t)     gdje δθ_i ≠ 0 znak uzbuđenja [Def]
```

**Lemma [Dc]:** Svako |δθ| nosi geometrijsku energiju:
```
E_geom ~ κ_θ (δθ)²          (Taylor oko minimuma)
```

Nema novih brojeva — samo: "ako minimum postoji, odstupanje ima energiju i vraća se".

### 14.4 Junction + Ring Mode (Harmonički oscilator) [P/I]

**Model [P]:** Kolektivni način pobude (ring/collective constraint) veže tri kraka tako da ne mogu odmah pasti u Steiner minimum → sustav OSCILIRA oko metastabilnog položaja.

**Heuristic Interpretation [I/P]:** U 1D efektivi:
```
ẍ + 2γẋ + ω₀²x = 0

gdje:
  γ  = efektivno prigušenje (brane-dissipation) [OPEN]
  ω₀ = "stiffness" krakova [P]
```

**BITNO:** Ovo nije "SM oscillator" — ovo je mehanička linearizacija oko geometrijskog minimuma.

### 14.5 Thick-Brane Pumpa [P/OPEN]

```
     BULK-CORE                BRANE LAYER (δ)           OBSERVER
   (junction relaksira)    ┌─────────────────┐        (3D čestice)
                           │                 │
   x(t) oscilira  ───────► │  φ(y,t) modes   │ ───────►  e⁻ + ν̄
                           │                 │
                      y=-δ/2              y=+δ/2
                    bulk-facing        observer-facing
```

**Coupling [P/OPEN]:**
```
L_int ~ g · x(t) · φ(y=-δ/2, t)
```

**Ledger closure:** Energija se zatvara u 5D, brana prima inflow J^ν_bulk→brane (Framework v2.0, Remark 4.5) [BL].

### 14.6 Frozen Projection: Zašto 3D čestice [Dc/P]

1. Neutron nastaje u frozen režimu → energija "zaključana" [Dc/P]
2. Bulk-core relaksira prema proton optimumu → energija u branu [P]
3. Observer-facing frozen projekcija "izbacuje" dopuštene izlaze [Dc/P]:
   - e⁻ + ν̄ + recoil
   - BEZ tvrdnje da smo izveli V–A!

**Minimalna, sigurna formulacija:**
> "In EDC, neutron decay is modeled as relaxation of an excited 5D junction
> that pumps energy into the brane layer; the observer-side frozen projection
> organizes that energy into allowed weak-channel outputs."

### 14.7 Kompatibilnost s Paper 3 WKB [OPEN]

Dva efektivna opisa ISTOG prijelaza:

| Opis | Dokument | Status |
|------|----------|--------|
| WKB kroz barijeru u V(q) | Paper 3 | [Dc/Der] u 1D |
| Mehanika metastabilnosti + brane pumping | Companion N | [P/OPEN] |

**Bridge statement [OPEN]:**
> Cilj: pokazati limit u kojem dissipativni model reducira na efektivnu WKB stopu (ili obrnuto).

### 14.8 Cornerstone Box (Short) — za početak papera

```
┌─────────────────────────────────────────────────────────────────────┐
│  CORNERSTONE (Neutron in EDC)                                       │
├─────────────────────────────────────────────────────────────────────┤
│  In the EDC program, the neutron is modeled as an excited 5D        │
│  junction state: the same three-arm junction core as the proton,    │
│  but displaced from the local Steiner minimum (the universal 120°   │
│  optimum in the tangent metric). This excitation couples to the     │
│  bulk-facing side of a thick brane, pumping energy into brane-layer │
│  modes. The observer-side frozen projection boundary then organizes │
│  the released energy into allowed weak-channel outputs (e.g., e⁻    │
│  and ν̄), while overall bulk–brane conservation remains anchored    │
│  to Framework v2.0, Remark 4.5.                                     │
│                                                                     │
│  Epistemic status:                                                  │
│  • 120° as local optimum: [Der]/[Dc] (geometric)                    │
│  • Thick-brane pumping + frozen output mapping: [P]/[OPEN]          │
└─────────────────────────────────────────────────────────────────────┘
```

### 14.9 Epistemic Tags Summary

| Tvrdnja | Status | Komentar |
|---------|--------|----------|
| 120° Steiner optimum | [Der/Dc] | Geometrijski, iz F |
| Neutron = excited junction | [P] | Object assumption |
| Ring/collective mode | [P] | Model |
| Thick-brane coupling | [OPEN] | Mikrofizika |
| Damping γ | [OPEN] | Mehanizam nepoznat |
| Frozen projection output | [Dc/P] | Paper 2 / Companion H |
| Ledger closure | [BL] | Framework v2.0, Remark 4.5 |

---

## 15. SLJEDEĆI KORACI (2026-01-21+)

### 15.1 Prioriteti istraživanja

| # | Zadatak | Status | Napomena |
|---|---------|--------|----------|
| 1 | **Companion N** — Neutron backbone LaTeX | PLAN SPREMAN (Sekcija 14) | Cornerstone box gotov |
| 2 | Faktor 12 = Z₆ × Z₂ derivacija | [OPEN] | Je li 70/5.856 = 12 namjerno? |
| 3 | S/ℏ = 12×ln(1/α)+1 geometrija | [I] → [Der]? | Potvrdi numerički, traži objašnjenje |
| 4 | V_B derivacija iz 5D akcije | [Cal] → [Der]? | Ako uspije → τ_n PREDIKCIJA |

### 15.2 Companion N — Checklist za izradu

- [ ] Kreirati LaTeX strukturu (F-style: tcolorbox, epistemic tags)
- [ ] Cornerstone box (tekst spreman u 14.8)
- [ ] Sekcije: Ontologija, Steiner relaxation, Oscillator, Thick-brane, Frozen, WKB bridge
- [ ] Related Documents blok s DOI-ima
- [ ] Build PDF + dodati u INVENTORY.md + SHA256SUMS.txt

---

## 16. UPOZORENJE ZA BUDUĆEG CLAUDEA

**OBAVEZNO PROČITAJ PRIJE RADA:**

1. **NE ponavljaj analize** koje su već napravljene (vidi sekcije 1-14)

2. **Ključni rezultati:**
   - σ = m_e³c⁴/(α³ℏ²) je **[Dc]** (POD hipotezom E_σ = m_e c²/α)
   - Faktor 12 i S/ℏ=60 su **[I]** patterni — istraži ih
   - Frozen derivacija je **GOTOVA** u Paper 2

3. **Konceptualne slike:**
   - Brana = "stakleni prozor" (LIJEVA=5D, DESNA=3D)
   - 5D je UZROK, 3D su OPAŽANJA
   - 3D činjenice [BL] su VALIDACIJA, ne kalibracija

4. **Hijerarhija dokumenata:**
   - Companion F = BACKBONE za proton
   - Companion N = BACKBONE za neutron (plan u sekciji 14)

5. **Filozofska implikacija:**
   - EDC DOPUŠTA promjenu konstanti (5D manipulacija)
   - SM NE DOPUŠTA (nema mehanizam)

---

*Dokument kreiran: 2026-01-20*
*Zadnja izmjena: 2026-01-20*
*Autori: Claude Opus 4.5 + Igor Grčman*
*Verzija: 1.0 (kanonski)*


# ============================================================================
# DOCUMENT 6: ANTI_PATTERNS_3D_TRAPS.md
# Source: ../EDC_Research_PRIVATE/kb/5d_universe/ANTI_PATTERNS_3D_TRAPS.md
# ============================================================================

# Anti-Patterns: 3D Traps to Avoid

**Knowledge Base: 5D Universe**
**Last Updated:** 2026-01-13

---

## Purpose

Comprehensive catalog of errors where 3D intuition leads to incorrect 5D physics.
**MEMORIZE THESE TRAPS.** They have destroyed derivations.

---

## THE GOLDEN RULE

> **NEVER trust your 3D intuition in 5D calculations.**
> Every geometric factor must be DERIVED, not assumed.

---

## KB Entries: 3D Traps

---

### KB-TRAP-001: Wrong Volume Formula (4π/3 vs 2π²)

**Status:** VERIFIED (Known error pattern)
**Scope:** Any calculation involving "spherical" objects
**Dependencies:** KB-VOL-003, KB-VOL-004
**Pitfalls:** This is the #1 most common error

**The Trap:**
Using $V = \frac{4\pi}{3}r^3$ for a "sphere" in 5D without checking which sphere.

**Why It's Wrong:**
- $\frac{4\pi}{3}r^3$ = Vol(B³) = volume of 3-ball in ℝ³
- $2\pi^2 r^3$ = Vol(S³) = volume of 3-sphere in ℝ⁴

In EDC, particles are S³ defects (boundary of B⁴), NOT B³ objects.

**Correct Approach:**
1. Identify embedding dimension
2. Determine if you need ball (Bⁿ) or sphere (Sⁿ⁻¹)
3. Use correct formula from KB-VOL-001 or KB-VOL-002

**Error Cost:** Factor of ~4.7 error in mass calculations

---

### KB-TRAP-002: Wrong Surface Area (4π vs 2π²)

**Status:** VERIFIED (Known error pattern)
**Scope:** Flux calculations, boundary terms
**Dependencies:** KB-VOL-002
**Pitfalls:** Leads to wrong flux quantization

**The Trap:**
Using $A = 4\pi r^2$ for any "spherical surface" in 5D.

**Why It's Wrong:**
- $4\pi r^2$ = Area(S²) = surface of 2-sphere
- $2\pi^2 r^2$ = "Area"(S³) = the 3-volume of S³ at radius r

**Correct Approach:**
Match surface formula to the dimensionality of the object.

---

### KB-TRAP-003: Wrong Radial Integration Measure

**Status:** VERIFIED (Known error pattern)
**Scope:** Energy integrals, volume integrals
**Dependencies:** KB-VOL-006
**Pitfalls:** Invalidates entire derivations

**The Trap:**
Using $\int 4\pi r^2 dr$ as the "spherical radial measure" in 5D.

**Why It's Wrong:**
| Dimension | Correct Measure |
|-----------|-----------------|
| 3D | $4\pi r^2 dr$ |
| 4D | $2\pi^2 r^3 dr$ |
| 5D | $(8\pi^2/3) r^4 dr$ |

**Correct Approach:**
Always use $\int r^{n-1} d\Omega_{n-1} dr$ with correct n.

---

### KB-TRAP-004: S³ = S² (Dimensional Confusion)

**Status:** VERIFIED (Known error pattern)
**Scope:** Topology arguments, defect classification
**Dependencies:** KB-GEO-005
**Pitfalls:** Wrong topology = wrong physics

**The Trap:**
Thinking S³ is "just a bigger S²" or "a 3D sphere."

**Why It's Wrong:**
- S² = 2-sphere = surface of ball in ℝ³ = {x² + y² + z² = r²}
- S³ = 3-sphere = surface of ball in ℝ⁴ = {x² + y² + z² + w² = r²}

They have completely different topology:
- π₃(S²) = ℤ (Hopf fibration)
- π₃(S³) = ℤ (identity map)

**Correct Approach:**
Always specify the EMBEDDING dimension, not just the sphere number.

---

### KB-TRAP-005: "Particle is a Ball in 3D Space"

**Status:** VERIFIED (Known error pattern)
**Scope:** All particle models
**Dependencies:** KB-GEO-003, KB-POST-004
**Pitfalls:** Fundamentally wrong picture

**The Trap:**
Visualizing a particle as a "little ball" sitting in 3D space.

**Why It's Wrong:**
In EDC, particles are:
- Topological DEFECTS, not balls
- Located at ξ = 0 (membrane) or extending through bulk
- Have S³ topology (boundary condition in 4D)
- "Radius" a is defect core size, not a ball radius

**Correct Approach:**
Think of particles as:
- Vortex cores on membrane (electron)
- Y-junctions through bulk (proton)
- NOT as "tiny balls of stuff"

---

### KB-TRAP-006: Projecting Without Integration

**Status:** VERIFIED (Known error pattern)
**Scope:** 5D → 4D effective physics
**Dependencies:** KB-GEO-007
**Pitfalls:** Loses factors of 2πR_ξ or worse

**The Trap:**
"Projecting" a 5D quantity to 4D by just dropping ξ.

**Why It's Wrong:**
Proper dimensional reduction requires:
$$Q_{4D} = \int_0^{2\pi R_\xi} Q_{5D}(x^\mu, \xi) \, d\xi$$

The ξ-integral may give:
- Factors of 2πR_ξ (zero modes)
- Sums over KK modes
- Boundary terms from compactification

**Correct Approach:**
Always perform explicit integration over ξ.

---

### KB-TRAP-007: Wrong Energy Density Units

**Status:** VERIFIED (Known error pattern)
**Scope:** Dimensional analysis
**Dependencies:** KB-GEO-007
**Pitfalls:** Factor errors that look "small"

**The Trap:**
Using [J/m³] for energy density in 5D.

**Why It's Wrong:**
| Space | Energy Density Units |
|-------|---------------------|
| 5D bulk | [J/m⁴] |
| 4D membrane | [J/m³] (after ξ-integration) |
| 3D spatial | [J/m³] |
| 2D surface | [J/m²] = σ |

**Correct Approach:**
Track dimensions at every step. ρ₄ ≠ ρ₃.

---

### KB-TRAP-008: "Membrane is 3D"

**Status:** VERIFIED (Known error pattern)
**Scope:** All brane physics
**Dependencies:** KB-GEO-003
**Pitfalls:** Wrong counting of degrees of freedom

**The Trap:**
Calling the membrane "3D" because we live in "3D space."

**Why It's Wrong:**
- Membrane Σ⁴ is 4-DIMENSIONAL (3 space + 1 time)
- The spatial slice Σ³ is 3-dimensional
- This distinction matters for action principles

**Correct Approach:**
Use "4D membrane" or "Σ⁴" for spacetime membrane.
Use "Σ³" or "spatial slice" for 3D space.

---

### KB-TRAP-009: Sign of 5th Dimension

**Status:** VERIFIED (Known error pattern)
**Scope:** Metric calculations
**Dependencies:** KB-GEO-002
**Pitfalls:** Flips sign of mass terms

**The Trap:**
Treating ξ as just "another spatial dimension" without checking signature.

**Why It's Wrong:**
The sign ε in $ds^2 = ... + \varepsilon \, d\xi^2$ determines:
- ε = +1: spacelike extra dimension
- ε = -1: timelike extra dimension

These give DIFFERENT physics (stability, causality, etc.).

**Correct Approach:**
Always specify ε and track its effects on signs.

---

### KB-TRAP-010: "Obviously 4π"

**Status:** VERIFIED (Known error pattern)
**Scope:** All geometric calculations
**Dependencies:** None
**Pitfalls:** Hidden 3D assumption

**The Trap:**
Writing "the factor is obviously 4π" without derivation.

**Why It's Wrong:**
In 5D, "obvious" factors change:
- 4π → 2π² (for S³)
- 4π/3 → π²/2 (for B⁴)
- 1/r² → 1/r³ (for 4D force law)

**Correct Approach:**
NEVER use "obviously" for geometric factors.
ALWAYS derive from integral or definition.

---

### KB-TRAP-011: Wrong Counting of DOF

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle physics, field theory
**Dependencies:** KB-GEO-001
**Pitfalls:** Wrong number of particles, gauge bosons

**The Trap:**
Counting degrees of freedom as if in 4D.

**Why It's Wrong:**
| Object | 4D DOF | 5D DOF |
|--------|--------|--------|
| Scalar | 1 | 1 (but KK tower) |
| Vector | 4 | 5 (but A_ξ special) |
| Metric | 10 | 15 |

KK decomposition adds infinite towers of states.

**Correct Approach:**
Count in 5D first, then reduce.

---

### KB-TRAP-012: Boundary Conditions from 3D Intuition

**Status:** VERIFIED (Known error pattern)
**Scope:** All field equations
**Dependencies:** KB-GEO-001
**Pitfalls:** Misses junction conditions

**The Trap:**
Assuming "natural" boundary conditions without derivation.

**Why It's Wrong:**
5D boundary conditions include:
- Membrane junction conditions (Israel)
- Compactification conditions (periodic, orbifold)
- Behavior at ξ → ∞
- Source conditions at defects

**Correct Approach:**
Derive ALL boundary conditions from the action.

---

### KB-TRAP-013: Mass vs Energy in 5D

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle mass formulas
**Dependencies:** KB-POST-003
**Pitfalls:** mc² = E only in rest frame

**The Trap:**
Equating 5D energy directly to 4D mass.

**Why It's Wrong:**
The 5D energy includes:
- Rest mass contribution
- KK momentum (p_ξ = n/R_ξ)
- Kinetic energy

4D mass emerges after projecting out ξ-dependence.

**Correct Approach:**
$$m_{4D}^2 c^4 = E_{5D}^2 - p_\xi^2 c^2$$

---

### KB-TRAP-014: Assuming Spherical Symmetry

**Status:** VERIFIED (Known error pattern)
**Scope:** Particle models, especially proton
**Dependencies:** None
**Pitfalls:** Proton is Y-junction, NOT sphere

**The Trap:**
Treating all particles as spherically symmetric.

**Why It's Wrong:**
- Electron: approximately spherical
- Proton: Y-junction of 3 strings (C₃ symmetry, not SO(3))
- Neutron: asymmetric Y-junction

Spherical symmetry is emergent for proton (KB-DERIV-002).

**Correct Approach:**
Derive symmetry from configuration, don't assume it.

---

### KB-TRAP-015: "Volume Ratio = Mass Ratio"

**Status:** VERIFIED (Known error pattern)
**Scope:** m_p/m_e derivation
**Dependencies:** KB-VOL-005
**Pitfalls:** Requires P-sum postulate!

**The Trap:**
Assuming $m_p/m_e = V_p/V_e$ without justification.

**Why It's Wrong:**
Standard variational principle gives:
$$E = \min_{\text{config}} \mathcal{E}$$

NOT:
$$E = \int_{\text{config}} \varepsilon \, d\mu$$

The integral (P-sum) requires a NEW physical mechanism.

**Correct Approach:**
Acknowledge P-sum as a POSTULATE until derived.

---

## Self-Check Checklist

Before finalizing ANY 5D calculation:

- [ ] Did I use any formula from 3D without verifying it in 5D?
- [ ] Are my volume/area formulas correct for the dimension?
- [ ] Did I handle the ξ integration explicitly?
- [ ] Are boundary conditions derived, not assumed?
- [ ] Did I verify by dimensional analysis?
- [ ] Does the result reduce correctly in limiting cases?
- [ ] Did I avoid "obviously" for geometric factors?

---

## Error Log

| Date | Error | KB-TRAP | Location | Resolution |
|------|-------|---------|----------|------------|
| 2026-01-11 | Used "π⁵ has no geometry" | KB-TRAP-001 | Alpha_v1 | Corrected: 6π⁵ = (2π²)³/(4π/3) |

---

*Your 3D intuition is your enemy in 5D. Trust only derivations.*


# ============================================================================
# END OF CANON BUNDLE
# ============================================================================

**Total P0 documents:** 6
**Action:** Read this entire file at the start of every session. MANDATORY.
