# Plan: σ̃ Canonical Closure — Tasks 1, 2, 3

## Kontekst

OPR-30 identificirao četiri nekompatibilne definicije σ̃ (v28→v67).
DEF-D (σ̃ = σ/T_*) usvojena kao kanonska. Tri zadatka za zatvaranje:

---

## Task 1: Odrediti dimenzijsku konvenciju za σ jednom zasvagda

### Problem

Dva mjesta u repozitoriju daju različite [σ]:
- **EDC Book I Ch.7, ch15_opr01, TSTAR docs**: σ = 1.41 × 10¹⁸ J/m² → J/m² = M³
- **v48 linija 361**: "[σ] = 4 (mass⁴)" → M⁴

### Analiza

U 4+1D, brana je kodimenizije 1 (3-brana). Brane action:
```
S_brane = -σ ∫ d⁴x √{-g_ind}
```
Za S bezdimenzionalan: [σ]·[d⁴x] = [σ]·M⁻⁴ = M⁰ → [σ] = M⁴.

ALI EDC koristi σ u J/m² = energy/area. To je M³, ne M⁴.

**Ključno pitanje**: jesu li to ista veličina?
- σ_covariant (u brane action) ima [M⁴] = energy/3-volume
- σ_static (u Book I) ima [M³] = energy/2-area (statička napetost membrane)

U statičkom limitu za ravnu branu u 5D: σ_covariant = σ_static jer
d⁴x = d³x·dt, a √{-g_ind} apsorbira vremenski faktor, pa S = -σ·V₃·T.
Zapravo: [S] = [σ][V₃][T] = M⁴·M⁻³·M⁻¹ = M⁰. ✓

**Ali** u prirodnim jedinicama:
- 1 J/m² = 1 kg/s² (u SI) → konverzija u GeV:
  1 J = 6.242 × 10⁹ GeV
  1 m = 5.068 × 10¹⁵ GeV⁻¹
  1 J/m² = 6.242 × 10⁹ GeV / (5.068 × 10¹⁵)² GeV⁻²
         = 6.242 × 10⁹ / 2.568 × 10³¹ GeV³
         = 2.431 × 10⁻²² GeV³

Dakle J/m² = GeV³ u prirodnim jedinicama → **[σ] = M³**.

Ali brane action zahtijeva [σ] = M⁴. Kontradikcija?

**NE** — Israel junction condition razrješava:
- κ₅² σ mora imati dimenziju [K] = M¹ (extrinsic curvature)
- [κ₅²] = M⁻³ (jer κ₅² = 8π/M₅³)
- [κ₅² σ] = M⁻³ · [σ] = M¹ → **[σ] = M⁴**

Ali ako [σ] = M³ (od J/m²), tada [κ₅² σ] = M⁰, ne M¹. Problem!

**Rezolucija**: U 5D GR postoji ambiguitet u definiciji κ₅²:
- Konvencija A: S_EH = (1/2κ₅²)∫d⁵x√{-G}R → [κ₅²] = M⁻³
- Konvencija B: S_EH = (M₅³/2)∫d⁵x√{-G}R → κ₅² = 1/M₅³, [κ₅²] = M⁻³

I u brane action:
- [∫d⁴x√{-g}] ovisi o konvenciji za metričke koordinate
- Ako su x^μ bezdimenzionalne: [d⁴x] = 1, [g_μν] = M⁻², [√{-g}] = M⁻⁴
  → S = -σ·M⁻⁴ → [σ] = M⁴
- Ako x^μ imaju dimenziju duljine: [d⁴x] = M⁻⁴, [g_μν] = 1, [√{-g}] = 1
  → S = -σ·M⁻⁴ → [σ] = M⁴ (isti rezultat)

**Zaključak**: Neovisno o konvenciji, [σ] = M⁴ za 3-branu u 5D.

Ali J/m² = M³. Kako onda σ = 1.41 × 10¹⁸ J/m² može biti M⁴?

**ODGOVOR**: Ne može. Ili:
(a) Book I koristi drugu veličinu (surface tension, ne brane tension), ili
(b) Book I ima grešku u jedinicama, ili
(c) σ_BookI i σ_brane_action su povezani ali NISU ista stvar.

Najvjerojatnija opcija: **(c)** — σ_BookI je 3D spatial tension (J/m²),
a σ_brane je 4D covariant tension (J/m³ = GeV⁴). Veza:
σ_brane [GeV⁴] = σ_static [GeV³] × k [GeV]
gdje je k = 1/ℓ AdS curvature scale ili neki drugi UV cutoff.

### Deliverable

Kreirati `DIMENSION_CONVENTION_SIGMA.md` u block003/:

1. **Sekcija 1**: Prikaz dviju σ-veličina i njihove veze
   - σ_static = energy/area = M³ (Book I, σ ≈ 1.41 × 10¹⁸ J/m²)
   - σ_brane = covariant brane tension = M⁴ (brane action, v29)
   - Eksplicitna konverzija i veza

2. **Sekcija 2**: Deklaracija kanonske konvencije za BLOCK-003/004
   - **Za σ̃**: koristimo σ_brane [M⁴] jer T_* može imati [M⁴]
   - ILI: koristimo σ_static [M³] jer Israel junction daje [κ₅²σ] = M⁰
   - **Odluka se mora donijeti na temelju detaljne analize** brane action-a

3. **Sekcija 3**: Konverzija σ_BookI u prirodne jedinice
   - σ = 1.41 × 10¹⁸ J/m² = 1.41 × 10¹⁸ × 2.431 × 10⁻²² GeV³
   - σ = 3.43 × 10⁻⁴ GeV³ ≈ 343 MeV³

4. **Sekcija 4**: Update TSTAR_DEFINITION.md i TSTAR_DERIVATION_5D.md
   - [T_*] mora biti isti kao [σ] (inače σ̃ = σ/T_* nije bezdimenzionalan)
   - Ako [σ] = M³: T_* = C·M₅³ ✓ (jer [M₅³] = M³)
   - Ako [σ] = M⁴: T_* = C·M₅⁴ ili C·M₅³·k (treba dodati skalu)

5. **Sekcija 5**: Update OPR-30 Section 5.3

**Datoteke**:
- NOVO: `paper_gravity_block003/DIMENSION_CONVENTION_SIGMA.md`
- EDIT: `cosmology_sigma_tilde_lane/TSTAR_DEFINITION.md` (dim sekcija)
- EDIT: `cosmology_sigma_tilde_lane/TSTAR_DERIVATION_5D.md` (dim sekcija)
- EDIT: `OPR-30_SIGMA_TILDE_RESOLUTION.md` (Section 5.3)

---

## Task 2: Derivirati T_* numerički iz 5D geometrije

### Preduvjet
Task 1 mora fiksirati [σ] i [T_*] prije numeričkog računa.

### Već poznato
- Strukturni oblik: T_* = C · M₅³ (iz TSTAR_DERIVATION_5D.md, Route A+B)
- M₅ ≈ 2.41 × 10¹³ GeV (iz v18, [D] derived: M₅³ = M̄_Pl²/R_ξ)
- σ ≈ 1.41 × 10¹⁸ J/m² ≈ 343 MeV³ ≈ 3.43 × 10⁻⁴ GeV³ (iz Book I)
- σ̃ mora biti ~ 100 za α₃ ~ 0.01

### Račun (ako [σ] = M³, [T_*] = M³)

T_* = C · M₅³ = C · (2.41 × 10¹³)³ GeV³ = C · 1.40 × 10⁴⁰ GeV³

σ̃ = σ/T_* = 3.43 × 10⁻⁴ / (C · 1.40 × 10⁴⁰)
   = 2.45 × 10⁻⁴⁴ / C

Za σ̃ = 100: C = 2.45 × 10⁻⁴⁶

To je APSURDNO malo — C bi trebao biti O(1) geometrijski faktor!

### Problem
σ = 343 MeV³ i M₅ = 2.41 × 10¹³ GeV daju σ/M₅³ ~ 10⁻⁴⁴.
To znači da je σ (Book I) NEVJEROJATNO mala u usporedbi s M₅³.

**Moguća objašnjenja**:
1. σ_BookI NIJE isti σ koji se koristi u BLOCK-003
2. M₅ iz v18 je kriv
3. σ̃ = 100 ne slijedi iz ovih brojeva → moramo revidirati

### Plan za Task 2

1. **Eksplicitno konvertirati** σ_BookI u GeV³ (ili GeV⁴) s punim
   faktorima konverzije (ℏ, c, itd.)

2. **Provjeriti M₅ iz v18** — je li M₅³ = M̄_Pl²/R_ξ doista ispravno?
   - M̄_Pl = 2.435 × 10¹⁸ GeV
   - R_ξ = 2.165 × 10⁻¹⁸ m = 2.165 × 10⁻¹⁸ / (1.973 × 10⁻¹⁶) GeV⁻¹
     = 1.097 × 10⁻² GeV⁻¹
   - M₅³ = (2.435 × 10¹⁸)² / (1.097 × 10⁻²)
     = 5.929 × 10³⁶ / 1.097 × 10⁻² = 5.404 × 10³⁸ GeV³
   - M₅ = (5.404 × 10³⁸)^{1/3} = 8.14 × 10¹² GeV ≈ 8.1 TeV

   Hmm, v18 daje 2.41 × 10¹³, ali ovaj račun daje 8.1 × 10¹². Blizu ali ne isto.
   Razlika može biti faktor 8π ili sl.

3. **Izračunati σ̃ = σ/T_*** s ispravnim ulazima

4. **Ako σ̃ ≪ 100**: dokumentirati jaz, označiti kao [P]-pending
   (znači da σ̃ = 100 ne slijedi iz naivnog T_* = M₅³)

5. **Kreirati Python skriptu** `recompute_tstar.py`:
   - Input: σ_BookI, M₅, faktori konverzije
   - Output: T_*, σ̃, α₃, provjera konzistentnosti
   - Uključiti sensitivity analizu na C

### Deliverable
- EDIT: `TSTAR_DERIVATION_5D.md` — nova sekcija "Numeric Evaluation"
- NOVO: `cosmology_sigma_tilde_lane/recompute_tstar.py`
- UPDATE: `sigma_tilde_value.json` (ako se σ̃ može izračunati)

---

## Task 3: Kreirati kanonski v68 s ispravnim definicijama

### Preduvjeti
Task 1 (dimenzija σ) + Task 2 (T_* numerički) moraju biti gotovi.

### Svrha v68
Kanonska verzija koja zamjenjuje cijeli pokvareni lanac v48–v66.
Naslijeđuje v67-ovu import contract strukturu, ali s punim popravkama.

### Struktura

```
derivation_v68/
├── main.tex          # Kanonska derivacija (~800 linija)
├── recompute.py      # Numerička verifikacija
└── README.md         # Verzijske bilješke
```

### main.tex sekcije

1. **OPR-30 Compliance** (10 linija)
   - Hash chain: v67→v68
   - "This version replaces v48–v66 σ̃ definitions per OPR-30"

2. **Dimension Convention** (30 linija)
   - [σ] deklaracija (iz Task 1)
   - Dimensional verification table

3. **σ̃ Canonical Definition** (50 linija, boxed)
   - σ̃ ≡ σ/T_* (OPR-30-CAN)
   - T_* = C·M₅³ (ili M₅⁴, ovisno o Task 1)
   - Full dimensional check
   - Numeric value (iz Task 2)

4. **Reconciliation with β** (50 linija)
   - β = σL²/M̄_Pl² (v29 definition)
   - σ̃ vs β: show explicit relation
   - Under what conditions σ̃ ≈ β (or not)
   - Why β was NOT a good normalization

5. **Deprecation Log** (40 linija)
   - DEF-B (v48): deprecated, reason
   - DEF-C (v62): deprecated, reason
   - β = σ̃⁴ (v56): algebraic error, deleted

6. **Closure Map** (100 linija, inherited from v67)
   - σ̃ → α₃(μ*) = 1/σ̃
   - α₃ → M_X = C_X · μ* · σ̃^{1/2}
   - M_X → g_X = √(4π/σ̃)
   - g_X → τ_p ∝ σ̃⁴
   - All with dimensional verification

7. **Numeric Evaluation** (80 linija)
   - σ̃ = [value from Task 2]
   - α₃ = [value]
   - M_X = [value]
   - τ_p = [value]
   - Uncertainty propagation

8. **Import Contract** (inherited from v67, 40 linija)
   - A-APIσ1/2/3 specifications
   - JSON interface

9. **Guard Compliance** (30 linija)
   - G1–G7 verification

### Ključne razlike od v67
- v67 kaže "T_* is a characteristic EDC scale" — v68 specificira točno
- v67 koristi σ̃ ~ 100 kao benchmark — v68 derivira (ili dokumentira jaz)
- v68 uključuje OPR-30 deprecation log
- v68 uključuje eksplicitnu [σ] deklaraciju

### recompute.py
- Numerička provjera svih formula iz main.tex
- Input: σ, M₅, L, M̄_Pl
- Output: σ̃, α₃, M_X, g_X, τ_p s uncertainties
- Comparison table: v68 vs v67 vs v62 results

---

## Redoslijed izvršenja

```
Task 1 ──→ Task 2 ──→ Task 3 ──→ Commit + Push
  │                      │
  └── moguća iteracija ──┘
      (ako [σ] konvencija
       promijeni T_* račun)
```

**Procjena**: 3 commita, 4 nova fajla, 4 uređena fajla.

---

## Rizici

| Rizik | Mitigacija |
|-------|-----------|
| σ_BookI ≠ σ_brane_action (razne veličine) | Eksplicitno dokumentirati; koristiti σ_brane za BLOCK-003 |
| σ̃ ≠ 100 iz numerike | Dokumentirati jaz, označiti C kao [P]-pending |
| [σ] konvencija komplicira T_* | Razriješiti Task 1 prvo; ako dvojba, fiksirati s Israel jcn |
| v68 predugačak | Držati pod 800 linija; referencirati v67 za detalje |
