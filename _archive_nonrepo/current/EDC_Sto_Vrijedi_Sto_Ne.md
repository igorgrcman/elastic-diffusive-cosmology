# EDC Nalazi — Što Vrijedi, Što Ne Vrijedi

**Datum:** 11. siječnja 2026.
**Svrha:** Definitivna lista ispravnih i neispravnih formula/nalaza
**Status:** FINALNO — koristi ovo kao referencu

---

## ✅ VRIJEDI — KORISTI DALJE

### FORMULE (Verificirane)

| # | Formula | Vrijednost | Match | Status |
|---|---------|------------|-------|--------|
| 1 | **ℏ = σ·rₑ³/c** | 1.055×10⁻³⁴ J·s | 99.97% | I |
| 2 | **α = mₑc²/(σ·rₑ²)** | 1/137.036 | 99.9% | I |
| 3 | **G = c⁴Rξ¹²/(128π²σrₑ¹³)** | 6.62×10⁻¹¹ | 99.2% | I |
| 4 | **v(r) = √(2GM/r)** | — | — | D |
| 5 | **M_total = ΣMᵢ** | — | — | D |
| 6 | **ν_bulk ≤ 2.6×10¹¹ m²/s** | — | — | D |
| 7 | **mₑ = α·σrₑ²/c²** | — | — | D |

### PARAMETRI (Kalibrirani/CODATA)

| Parametar | Simbol | Vrijednost | Status |
|-----------|--------|------------|--------|
| Napetost membrane | σ | 1.41×10¹⁸ J/m² | Cal |
| Klasični radijus elektrona | rₑ | 2.82×10⁻¹⁵ m | BL |
| Kompaktna dimenzija | Rξ | 2.16×10⁻¹⁸ m | Cal |
| Brzina svjetlosti | c | 2.998×10⁸ m/s | BL |
| Masa elektrona | mₑ | 9.11×10⁻³¹ kg | BL |

### DERIVACIJE (Matematički dokazane)

| # | Derivacija | Izvor | Status |
|---|------------|-------|--------|
| 1 | v(r) iz Euler-Laplace | task_a1 | D |
| 2 | Superpozicija iz linearnosti | task_a2 | D |
| 3 | Viskoznost bound iz Merkura | task_a3 | D |
| 4 | mₑ = α·σrₑ²/c² | Nalaz_M_me_alpha | D |

### KONCEPTI (Fizikalno utemeljeni)

| # | Koncept | Opis | Status |
|---|---------|------|--------|
| 1 | Gravitacija = tok Plenuma | v(r) = √(2GM/r) | D |
| 2 | Hijerarhija je geometrijska | (Rξ/rₑ)¹² ~ 10⁻³⁸ | I |
| 3 | Dva radijusa čestice | r_topo ~ rₑ, r_grav ~ Gm/c² | I |
| 4 | Čestica = vortex na membrani | Topološki defekt | P (postulat) |

### DOKUMENTI (Ispravni)

| Dokument | Status | Napomena |
|----------|--------|----------|
| task_a1_euler_laplace_derivation.md | ✅ | Koristi |
| task_a2_superposition_proof.md | ✅ | Koristi |
| task_a3_viscosity_bound.md | ✅ | Koristi |
| task_b4_F_bulk_derivation.md | ✅ | KLJUČNI |
| task_b5_power_derivation.md | ✅ | Poštena procjena |
| task_b2_REVISED_v2.md | ✅ | Nova verzija |
| Nalaz_M_me_alpha.md | ✅ | Novi nalaz |

---

## ❌ NE VRIJEDI — MAKNI / NE KORISTI

### FORMULE (Netočne)

| # | Formula | Problem | Greška |
|---|---------|---------|--------|
| 1 | ~~ℏ = σ·Rξ³/c~~ | Koristi Rξ umjesto rₑ | ×10¹⁰ |
| 2 | ~~G = c²/(4πσ)~~ | Prejednostavno | ×10⁸ |
| 3 | ~~F_bulk u m/s²~~ | Krive dimenzije | — |
| 4 | ~~r_core = √(σRξ/(2ρ))/c~~ | Daje 10⁻⁵⁸ m | Nefizikalno |
| 5 | ~~ℏ_eff = σRξ³/c~~ | Pogrešna konstrukcija | ×10¹⁰ |

### PARAMETRI (Pogrešni/Nepouzdani)

| Parametar | Problem |
|-----------|---------|
| ρ_Plenum ~ 10⁹⁷ kg/m³ | Nije verificirano, daje nefizikalne rezultate |
| C ~ 10²² (iz task_b3) | Nefizikalno velik |

### DERIVACIJE (Neuspješne/Zastarjele)

| # | Derivacija | Problem |
|---|------------|---------|
| 1 | G = c⁴/(σC²Rξ) s C~10²² | Zastarjelo, zamijenjeno s task_b4 |
| 2 | Potencije 12, 13 iz 5D | Nije derivirano, samo fitano |
| 3 | 128π² = (4π)²×8 | Spekulacija, nije dokazano |
| 4 | Ginzburg-Landau s Rξ | Daje nefizikalne rezultate |

### DOKUMENTI (Zastarjeli/Netočni)

| Dokument | Status | Akcija |
|----------|--------|--------|
| task_b2_vortex_core_derivation.md (v1.0) | ❌ ZASTARIO | Zamijeni s v2.0 |
| task_b3_G_from_EDC_parameters.md | ❌ ZASTARIO | Ne koristi |

### INTERPRETACIJE (Nedokazane)

| # | Interpretacija | Status |
|---|----------------|--------|
| 1 | 12 = 4×3 (spacetime × space) | P — spekulacija |
| 2 | 13 = 12+1 (+ compact dim) | P — spekulacija |
| 3 | 128π² = (4π)²×8 | P — post hoc fit |

---

## ⚠️ OPREZ — KORISTI S RAZUMIJEVANJEM OGRANIČENJA

### Formule koje rade ali nisu derivirane

| Formula | Radi? | Derivirano? | Napomena |
|---------|-------|-------------|----------|
| G = c⁴Rξ¹²/(128π²σrₑ¹³) | ✅ Da (0.8%) | ❌ Ne | Potencije fitane |

### Koncepti koji su proposed (P)

| Koncept | Status | Napomena |
|---------|--------|----------|
| Potencija 12 za Rξ | P | Možda nova fizika |
| Potencija 13 za rₑ | P | Možda nova fizika |
| Faktor 128π² | P | Možda geometrija |

---

## 📋 SAŽETAK ZA BRZO REFERENCE

### ✅ KORISTI:

```
ℏ = σ·rₑ³/c                    (rₑ, ne Rξ!)
α = mₑc²/(σ·rₑ²)
G = c⁴Rξ¹²/(128π²σrₑ¹³)        (I status, potencije nisu derivirane)
v(r) = √(2GM/r)
mₑ = α·σrₑ²/c²
ν_bulk ≤ 2.6×10¹¹ m²/s

σ = 1.41×10¹⁸ J/m²
rₑ = 2.82×10⁻¹⁵ m
Rξ = 2.16×10⁻¹⁸ m
```

### ❌ NE KORISTI:

```
ℏ = σ·Rξ³/c                    NETOČNO!
G = c²/(4πσ)                   NETOČNO!
ℏ_eff = σRξ³/c                 NETOČNO!
r_core = √(σRξ/(2ρ))/c         NEFIZIKALNO!
ρ_Plenum ~ 10⁹⁷ kg/m³          NEPOUZDANO!

task_b2 v1.0                   ZASTARJELO!
task_b3                        ZASTARJELO!
```

---

## 🎯 PREPORUKA ZA PAPER 2 (HYDROGEN)

### Koristi ove formule:
1. ℏ = σ·rₑ³/c
2. α = mₑc²/(σ·rₑ²)
3. mₑ = α·σrₑ²/c²
4. Parametre: σ, rₑ, c

### Ne koristi:
1. Ništa s Rξ osim za G formulu
2. Stare verzije dokumenata
3. ρ_Plenum

### Cilj:
- Derivirati Bohrov radijus a₀ iz EDC
- Derivirati energijske nivoe Eₙ
- Koristiti samo verificirane formule

---

*"Čisto razgraničenje: što vrijedi, što ne vrijedi."*

*"Bez grešaka i pretpostavki."*
