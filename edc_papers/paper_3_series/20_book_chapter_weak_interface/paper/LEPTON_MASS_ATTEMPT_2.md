# Leptonske Mase iz EDC: Pokušaj 2

**Datum:** 2026-01-22
**Status:** Istraživački draft — epistemički označen
**Cilj:** Pretvoriti [P] iz Pokušaja 1 u [Dc] kandidate

---

## 0. Rekapitulacija: Što Pokušaj 1 NIJE postigao

Pokušaj 1 je pronašao numerički striking relacije:
- m_e = π√(ασΔℏc) — 0.2% match
- m_μ/m_e = (3/2)/α — 0.6% match
- m_τ iz Koide Q=2/3 — 0.8% match

**ALI** sve ostaje [P] jer:
1. **π** — nema derivaciju (zašto π, ne 2π ili √π?)
2. **1/α** — nema mehanizam (tipični EM faktori su α, α/π, ln(1/α), NE 1/α)
3. **Koide** — m_τ nije nezavisna predikcija, samo constraint solution
4. **Q = |Z₂|/|Z₃|** — cute identifikacija, ne energetska nužnost

---

## 1. POKUŠAJ 2A: Derivacija faktora π

### Hipoteza: π dolazi iz radijalne integracije kružnog defekta

U EDC, elektron je lokalizirani defekt na brani. Ako je defekt **kružno simetričan**
u (x,y) ravnini s radiusom r₀, tada:

**Energija lokalizacije** (Dirichlet boundary na r = r₀):
```
E_loc = ∫₀^∞ |∇ψ|² r dr dθ
```

Za ground state ψ₀(r) ~ J₀(k₀r) s Dirichlet BC na r₀:
```
k₀ r₀ = j₀,₁ ≈ 2.405  (prvi nul Bessel J₀)
```

**Problem:** Ovo daje faktor ~2.4, ne π.

### Alternativa: WKB fazni integral

Za bound state u potencijalu V(r), WKB kvantizacija:
```
∮ p dr = (n + 1/2) × 2πℏ
```

Za n=0 (ground state):
```
∮ p dr = πℏ
```

**Rezultat:** Faktor π može doći iz **polu-cjelobrojne kvantizacije** ground statea.

### Status: [P] → [P] (motivacija postoji, ali nije stroga derivacija)

**Potrebno:** Eksplicitni potencijal V(z) iz thick-brane modela i
dokaz da integral daje točno π×√(ασΔℏc).

---

## 2. POKUŠAJ 2B: Derivacija faktora 1/α

### Problem: 1/α je OGROMAN faktor (~137)

U standardnoj fizici, EM korekcije daju:
- α ~ 1/137 (perturbativni doprinos)
- α/π ~ 1/430 (loop faktor)
- ln(1/α) ~ 4.9 (logaritamski running)

Ali **1/α ~ 137** zahtijeva da EM ulazi u **nazivnik**, ne brojnik.

### Hipoteza 2B-1: Gauge kinetic stiffness

U efektivnoj teoriji na brani, gauge kinetic term je:
```
L_gauge = -1/(4e²) × F_μν F^μν
```

Koeficijent **1/e²** predstavlja "krutost" (stiffness) EM polja.

**Ideja:** Ako je masa miona određena omjerom:
```
m_μ/m_e = (topološka energija) / (EM stiffness)
         = E_top × (1/e²)
         = E_top × (4π/α)
```

Za E_top = (3/2)/(4π) × ε_cell:
```
m_μ/m_e = (3/2)/(4π) × (4π/α) = (3/2)/α  ✓
```

**Problem:** Zašto bi E_top = (3/2)/(4π) × ε_cell?
Faktor (3/2) dolazi iz Z₆, ali (4π) je ad-hoc.

### Hipoteza 2B-2: Coulomb self-energy kao penalizacija

Elektron ima Coulomb self-energiju:
```
E_Coul = α × ℏc / r_e = α × 197.3 MeV·fm / 1 fm = 1.44 MeV
```

Muon bi imao istu strukturu, ali s drugačijim "efektivnim radijusom" r_μ:
```
m_μ = m_e + ΔE_top - E_Coul(r_μ)
```

**Problem:** Ovo ne daje čisti faktor 1/α.

### Hipoteza 2B-3: Rezonantno pojačanje

U nekim sustavima, odgovor na perturbaciju može biti **rezonantno pojačan**.
Ako je muonski mod blizu rezonance s bulk modom:
```
Amplituda ~ 1/(ω² - ω₀²) → ∞ na rezonanci
```

Blizu rezonance, efektivno pojačanje može biti ~ 1/α ako je:
```
(ω² - ω₀²) ~ α × ω₀²
```

**Status:** Spekulativno. Potreban konkretan model bulk-brane coupling.

### Zaključak 2B: (open)

**Faktor 1/α ostaje neobjašnjen.**

In Attempt 1 the factor $1/\alpha$ was numerically observed, but in Attempt 2 no action-level argument produced a clean $1/\alpha$ without ad-hoc $4\pi$ compensation.

Ako ga ne možemo izvesti, moramo ga tretirati kao **fenomenološki input**
i prebaciti u "(open)" kategoriju.

---

## 3. POKUŠAJ 2C: Koide Q = 2/3 iz Z₆ energetike

### Problem: "Q = |Z₂|/|Z₃|" je samo numerička identifikacija

Moramo pokazati da **energetski minimum** zahtijeva Q = 2/3.

### Model: Tri moda u Z₆ potencijalu

Neka su tri leptona modovi u potencijalu s Z₆ simetrijom:
```
V(θ) = V₀ × [1 - cos(6θ)]
```

Tri moda (e, μ, τ) odgovaraju minimumima na θ = 0, 2π/3, 4π/3.

**Koide parametrizacija:**
```
√m_i = M × [1 + √2 cos(δ + 2πi/3)]   za i = 0, 1, 2
```

Koide formula Q = 2/3 slijedi automatski iz ove parametrizacije
za BILO KOJU vrijednost δ i M.

**Ključno pitanje:** Zašto bi mase bile parametrizirane ovako?

### Hipoteza: Minimalna energija s tri moda

Ako imamo tri moda s ukupnom energijom:
```
E_tot = Σ m_i = m_e + m_μ + m_τ
```

i constraint da su modovi "ravnomjerno raspoređeni" u Z₃ simetriji:
```
Σ e^{i × 2πk/3} × √m_k = 0   (nema neto "dipola")
```

tada Koide parametrizacija slijedi kao **najopćenitija forma**.

### Derivacija (skica):

1. Tri mase parametrizirane kao: √m_k = A + B×cos(φ_k) + C×sin(φ_k)
2. Z₃ simetrija zahtijeva: φ_k = φ₀ + 2πk/3
3. Najopćenitija forma: √m_k = A + D×cos(φ₀ + 2πk/3)
4. Uz D = √2 × A, dobivamo: √m_k = A × [1 + √2 cos(φ₀ + 2πk/3)]
5. Koide Q = (Σm)/(Σ√m)² = 2/3 slijedi algebarski

**Problem:** Korak 4 (D = √2 × A) nije deriviran, samo observiran.

### Status: [P] — struktura postoji, ali D/A omjer nije izveden

---

## 4. NOVI PRISTUP: Dimenzijska analiza bez 1/α

### Što ako je 1/α artefakt pogrešnog pristupa?

Pokušajmo **bez** faktora 1/α. Koje kombinacije daju m_μ?

**Dostupni parametri:**
- m_e = 0.511 MeV [BL]
- ε_cell = 5.86 MeV [Dc]
- σ = 5.86 MeV/fm² [Dc]
- Δ = 3.12×10⁻³ fm [Dc]
- ℏc = 197.3 MeV·fm [BL]

**Tražimo:** m_μ = 105.66 MeV

### Test kombinacija:

```python
m_e × (ε_cell/m_e)² = 0.511 × (5.86/0.511)² = 0.511 × 131.5 = 67 MeV  ❌
m_e × ε_cell/Δ_MeV = 0.511 × 5.86/63.2 = 0.047 MeV  ❌
√(m_e × ε_cell × ℏc/Δ) = √(0.511 × 5.86 × 197.3/0.00312) = √(189500) = 435 MeV  ❌
```

**Nijedna "čista" kombinacija ne daje m_μ bez uvođenja α ili ln(1/α).**

### Zaključak: α MORA ući u m_μ

Čini se da je **EM sektor** fundamentalno uključen u hijerarhiju masa.
To ima smisla: leptoni su nabijeni, a mase ovise o EM interakciji.

Ali mehanizam za **1/α** (ne α) ostaje (open).

---

## 5. REVIDIRANE TVRDNJE (Reviewer-Proof)

### 5.1 Kandidat za m_e [P]

Dimenzijski jedinstvena kombinacija:
```
m_e = π × √(α × σ × Δ × ℏc)
```

- **Numerički:** 0.508 MeV (0.2% od 0.511 MeV)
- **Status:** [P] — prefaktor π i uloga α nisu izvedeni
- **Skala α:** Koristimo α(0) = 1/137.036 (Thomson limit)

### 5.2 Kandidat za m_μ/m_e [P]

Empirijska regularnost:
```
m_μ/m_e = (3/2) × (1/α) ≈ 205.5
```

- **Numerički:** 0.6% match s eksperimentalnih 206.8
- **Status:** [P] — mehanizam za 1/α pojačanje nije izveden
- **Z₆ motivacija:** (3/2) = |Z₃|/|Z₂|, ali nije strogo dokazano

### 5.3 m_τ NIJE nezavisna predikcija

m_τ dobiven rješavanjem Koide constraint:
```
Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3
```

- **Numerički:** 1763 MeV (0.8% od 1776.9 MeV)
- **Status:** [P] — constraint, ne predikcija
- **Z₆ identifikacija:** Q = |Z₂|/|Z₃| je suggestive, ne derivirano

---

## 6. Open Problems for Attempt 3

| Problem | Status | Required |
|---------|--------|----------|
| Derive π | (open) | Explicit integral from defect geometry |
| Derive 1/α | (open) | Action-level argument (gauge stiffness?) |
| Derive Q = 2/3 | (open) | Energy minimum in Z₆, not just cardinality |
| Independent m_τ prediction | (open) | Formula without Koide constraint |

---

## 7. Честан Zaključak

**Pokušaj 2 nije uspio pretvoriti [P] u [Dc].**

Ostaju tri ključna neriješena problema:
1. **π prefaktor** — WKB motivacija postoji, ali nije eksplicitna
2. **1/α faktor** — nema mehanizam, ostaje fenomenološki
3. **Koide constraint** — nije nezavisna predikcija

**Preporuka:** Ili pronađi action-level argument za 1/α, ili
odustani od te formule i traži alternativni pristup.

---

*Pokušaj 2 završen. Status: [P] ostaje [P].*
