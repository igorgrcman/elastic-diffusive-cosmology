# Nalaz: M/mₑ = 1/α — Elastična Energija Vorteksa i Masa Elektrona

**Datum:** 11. siječnja 2026.
**Tip:** Teorijski nalaz
**Status:** I (Identified) — potrebno daljnje istraživanje
**Kontekst:** Proizašlo iz revizije Task B2

---

## 1. SAŽETAK NALAZA

Pri reviziji Task B2 s ispravnom formulom ℏ = σrₑ³/c, otkrivena je zanimljiva numerička podudarnost:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   M = σrₑ²/c² = 1.25×10⁻²⁸ kg                                  │
│                                                                 │
│   mₑ = 9.11×10⁻³¹ kg                                           │
│                                                                 │
│   M/mₑ = 136.9 ≈ 137 = 1/α                                     │
│                                                                 │
│   ELASTIČNA ENERGIJA VORTEKSA = (1/α) × MASA ELEKTRONA         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. DEFINICIJA VELIČINA

### 2.1 Što je M?

**M** je ekvivalentna masa elastične energije vorteksa na membrani:

```
M = E_elastic / c²
```

gdje je:
```
E_elastic = σ × rₑ²
```

**Fizikalno značenje:**
- Vortex (čestica) na membrani stvara elastičnu deformaciju
- Ta deformacija ima energiju proporcionalnu napetosti × površini
- E = σ × rₑ² je "cijena" postojanja vorteksa na membrani
- M = E/c² je ekvivalentna masa te energije (Einstein: E = Mc²)

### 2.2 Što je mₑ?

**mₑ** je eksperimentalno izmjerena masa elektrona:
```
mₑ = 9.109×10⁻³¹ kg = 0.511 MeV/c²
```

### 2.3 Što je α?

**α** je konstanta fine strukture:
```
α = e²/(4πε₀ℏc) = 1/137.036
```

Karakterizira snagu elektromagnetske interakcije.

---

## 3. NUMERIČKI RAČUN

### 3.1 Ulazne vrijednosti

| Parametar | Simbol | Vrijednost | Izvor |
|-----------|--------|------------|-------|
| Napetost membrane | σ | 1.41×10¹⁸ J/m² | EDC (kalibirano iz ℏ) |
| Klasični radijus elektrona | rₑ | 2.82×10⁻¹⁵ m | CODATA |
| Brzina svjetlosti | c | 2.998×10⁸ m/s | CODATA |
| Masa elektrona | mₑ | 9.11×10⁻³¹ kg | CODATA |
| Fine structure | α | 1/137.036 | CODATA |

### 3.2 Račun energije

```
E_elastic = σ × rₑ²
          = 1.41×10¹⁸ J/m² × (2.82×10⁻¹⁵ m)²
          = 1.41×10¹⁸ × 7.95×10⁻³⁰ m²
          = 1.12×10⁻¹¹ J
```

Pretvorba u MeV:
```
E_elastic = 1.12×10⁻¹¹ J / (1.6×10⁻¹³ J/MeV)
          = 70.1 MeV
```

### 3.3 Račun ekvivalentne mase

```
M = E_elastic / c²
  = 1.12×10⁻¹¹ J / (2.998×10⁸ m/s)²
  = 1.12×10⁻¹¹ / 8.99×10¹⁶
  = 1.25×10⁻²⁸ kg
```

### 3.4 Omjer M/mₑ

```
M/mₑ = 1.25×10⁻²⁸ kg / 9.11×10⁻³¹ kg
     = 136.9
     ≈ 137.0
     = 1/α ✓
```

### 3.5 Dimenzijska provjera

```
[M] = [σ × rₑ² / c²]
    = [J/m²] × [m²] / [m²/s²]
    = [J] / [m²/s²]
    = [J·s²/m²]
    = [kg·m²/s²] × [s²/m²]
    = [kg] ✓
```

---

## 4. FIZIKALNA INTERPRETACIJA

### 4.1 Problem

Ako je elektron vortex na membrani, očekivali bismo:
```
masa elektrona ≈ elastična energija vorteksa / c²
```

Ali dobivamo:
```
M = σrₑ²/c² = 137 × mₑ ≠ mₑ
```

**Elastična energija vorteksa je 137 puta VEĆA od mase elektrona!**

### 4.2 Energetska bilanca

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   UKUPNA ELASTIČNA ENERGIJA:     E_elastic = 70.1 MeV          │
│                                                                 │
│   MASA ELEKTRONA (energija):     mₑc² = 0.511 MeV              │
│                                                                 │
│   OMJER:                         70.1 / 0.511 = 137 = 1/α      │
│                                                                 │
│   SAMO 1/137 ELASTIČNE ENERGIJE POSTAJE INERCIJALNA MASA!      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Moguća objašnjenja

#### Hipoteza 1: Gola masa vs fizička masa

U kvantnoj elektrodinamici postoji koncept "gole mase" (bare mass) i "fizičke mase" (dressed mass):

```
m_bare = M = σrₑ²/c² = 70 MeV/c²    (gola masa)
m_physical = mₑ = 0.511 MeV/c²       (fizička masa)

Renormalizacija: m_physical = α × m_bare
```

**Interpretacija:** Interakcija s EM poljem "renormalizira" masu, reducirajući je faktorom α.

#### Hipoteza 2: Samo dio energije je inercijalan

Možda elastična energija membrane ima dvije komponente:

```
E_elastic = E_inertial + E_bound

E_inertial = α × E_elastic = mₑc²     (doprinosi inerciji)
E_bound = (1-α) × E_elastic           (vezana energija polja)
```

**Interpretacija:** Većina energije je "zaključana" u konfiguraciji polja i ne doprinosi inerciji čestice.

#### Hipoteza 3: Povezanost s definicijom rₑ

Klasični radijus elektrona je DEFINIRAN kao:
```
rₑ = e²/(4πε₀ mₑc²) = α × ℏ/(mₑc)
```

Ovo uključuje α u samoj definiciji! Možda podudarnost M/mₑ = 1/α proizlazi iz ove veze.

**Provjera:**
```
rₑ = α × λ_Compton
   = α × ℏ/(mₑc)

Tada:
σrₑ² = σ × α² × ℏ²/(mₑ²c²)

Ali ℏ = σrₑ³/c, dakle:
σ = ℏc/rₑ³

σrₑ² = (ℏc/rₑ³) × rₑ² = ℏc/rₑ

Zato:
M = σrₑ²/c² = ℏ/(c×rₑ) = ℏ/(c × α × ℏ/(mₑc)) = mₑ/α = mₑ × 137 ✓
```

**Ovo OBJAŠNJAVA zašto M/mₑ = 1/α!**

#### Hipoteza 4: Dublja fizikalna veza

α određuje snagu EM interakcije. Činjenica da se pojavljuje u omjeru energija možda ukazuje na:

- Elektron "troši" faktor α svoje elastične energije na masu
- Ostatak (1 - α ≈ 99.3%) je EM energija polja
- Masa i naboj su povezani kroz α

---

## 5. DERIVACIJA: ZAŠTO M/mₑ = 1/α

### 5.1 Polazne formule

Iz EDC (verificirano):
```
ℏ = σ × rₑ³ / c         ... (1)
```

Definicija klasičnog radijusa:
```
rₑ = α × ℏ / (mₑ × c)   ... (2)
```

### 5.2 Izvod

Iz (1):
```
σ = ℏ × c / rₑ³         ... (3)
```

Elastična energija:
```
E = σ × rₑ² = (ℏc/rₑ³) × rₑ² = ℏc/rₑ    ... (4)
```

Supstituiraj rₑ iz (2):
```
E = ℏc / (α × ℏ/(mₑc))
  = ℏc × mₑc / (α × ℏ)
  = mₑc² / α                            ... (5)
```

Ekvivalentna masa:
```
M = E/c² = mₑ/α = mₑ × 137              ... (6)
```

### 5.3 Zaključak derivacije

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   M/mₑ = 1/α  NIJE SLUČAJNOST!                                 │
│                                                                 │
│   Proizlazi iz:                                                 │
│   1. EDC formule ℏ = σrₑ³/c                                    │
│   2. Definicije rₑ = αℏ/(mₑc)                                  │
│                                                                 │
│   Ovo je KONZISTENTNOST, ne nova fizika.                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. FIZIKALNO ZNAČENJE

### 6.1 Što ovo znači

Relacija M/mₑ = 1/α je **matematička posljedica** kombinacije:
- EDC formule za ℏ
- Standardne definicije klasičnog radijusa elektrona

### 6.2 Zašto je to važno

1. **Konzistentnost EDC:** Formula ℏ = σrₑ³/c je konzistentna s poznatom fizikom
2. **Veza mase i α:** Elastična energija membrane i masa elektrona su povezane kroz α
3. **Interpretacija rₑ:** Klasični radijus elektrona ima fizikalno značenje u EDC kao veličina vorteksa

### 6.3 Alternativni pogled

Možemo reinterpretirati formulu za masu elektrona:
```
mₑ = α × σrₑ²/c²
   = α × (elastična energija vorteksa)/c²
```

**Masa elektrona je α-ti dio elastične energije vorteksa!**

---

## 7. IMPLIKACIJE ZA EDC

### 7.1 Struktura elektrona

```
ELEKTRON U EDC:

  Ukupna elastična energija membrane:  E_total = σrₑ² = 70 MeV
  
  Podjela energije:
  ├── Inercijalna masa:  mₑc² = α × E_total = 0.511 MeV
  └── EM energija polja: (1-α) × E_total = 69.5 MeV
```

### 7.2 Veza s "klasičnim" problemom

U klasičnoj elektrodinamici, "elektromagnetska masa" elektrona (self-energy) je:
```
m_EM = e²/(8πε₀rₑc²) = mₑ/2
```

Ovo je poznati rezultat koji vodi na problem: dio mase dolazi od EM polja.

EDC daje drukčiju sliku:
- Ukupna energija je σrₑ² (elastična deformacija membrane)
- Masa je α × σrₑ²/c² = mₑ

### 7.3 Otvorena pitanja

1. **Zašto baš α?** — Koja je fizikalna razlog da baš α određuje omjer?
2. **Gdje je ostatak energije?** — Ako je 99.3% energije nije masa, što je?
3. **Vrijedi li za druge čestice?** — Je li M/m = 1/α univerzalno?

---

## 8. EPISTEMIC STATUS

| Tvrdnja | Status | Obrazloženje |
|---------|--------|--------------|
| M = σrₑ²/c² | D (Derived) | Direktna definicija |
| M/mₑ = 136.9 | D (Derived) | Numerički račun |
| M/mₑ = 1/α | D (Derived) | Proizlazi iz ℏ = σrₑ³/c i rₑ = αℏ/(mₑc) |
| Interpretacija "gola masa" | P (Proposed) | Hipoteza, nije dokazano |
| Interpretacija "α dio energije" | P (Proposed) | Hipoteza, nije dokazano |
| Univerzalnost za druge čestice | ? (Unknown) | Potrebno istražiti |

---

## 9. REFERENCE

- task_b2_REVISED_v2.md — Izvor otkrića
- task_b4_F_bulk_derivation.md — Formula ℏ = σrₑ³/c
- CODATA 2018 — Vrijednosti konstanti
- Jackson, Classical Electrodynamics — Klasični radijus elektrona

---

## 10. ZAKLJUČAK

### 10.1 Glavni nalaz

Relacija M/mₑ = 1/α NIJE slučajnost, već matematička posljedica EDC formule ℏ = σrₑ³/c kombinirane s definicijom klasičnog radijusa elektrona.

### 10.2 Fizikalna interpretacija

Masa elektrona je α-ti dio elastične energije vorteksa na membrani:
```
mₑ = α × σrₑ²/c²
```

### 10.3 Značaj za EDC

- Potvrđuje konzistentnost EDC s poznatom fizikom
- Daje fizikalnu interpretaciju klasičnog radijusa elektrona
- Povezuje masu, naboj i elastičnost membrane kroz α

---

*"Masa elektrona je 1/137 elastične energije vorteksa — i to nije slučajnost."*

*"Bez grešaka i pretpostavki."*
