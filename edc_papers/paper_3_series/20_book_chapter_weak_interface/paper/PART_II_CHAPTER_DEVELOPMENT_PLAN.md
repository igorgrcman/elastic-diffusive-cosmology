# PART II — CHAPTER DEVELOPMENT PLAN
## EDC Book II: The Weak Sector — Extension Roadmap

Created: 2026-01-22
Author: Claude Opus 4.5 (AI assistant)
Status: PROPOSAL — awaiting Igor's review

---

## EXECUTIVE SUMMARY

Part II currently covers ~25-30% of SM Weak physics. This document proposes
6 additional chapters to achieve ~80% coverage, organized by dependencies
and building on established EDC findings.

**Key insight:** All proposed chapters derive from the SAME geometric
foundation: Z₆ = Z₂ × Z₃ hexagonal symmetry and thick-brane mode spectrum.

---

## DEPENDENCY GRAPH

```
                    ┌─────────────────────────────────────────────┐
                    │  EXISTING FOUNDATION (Part II, Ch 1-3)      │
                    │  • Z₆ symmetry → sin²θW = 1/4               │
                    │  • Thick-brane: bulk-core / brane / edge    │
                    │  • Mode indices: n = 0,1,2 for e,μ,τ        │
                    │  • σr_e² = 5.86 MeV (lattice cell energy)   │
                    └─────────────────┬───────────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
    │  CHAPTER 4      │    │  CHAPTER 9      │    │  CHAPTER 8      │
    │  Leptonske mase │    │  V-A struktura  │    │  Higgs sektor   │
    │  ★★★★★          │    │  ★★★★           │    │  ★★★★           │
    │                 │    │                 │    │                 │
    │ INPUT: mode     │    │ INPUT: boundary │    │ INPUT: σ, r_e   │
    │ spectrum, σ     │    │ conditions      │    │ brane tension   │
    │                 │    │                 │    │                 │
    │ OUTPUT: m_e,    │    │ OUTPUT: P_L,    │    │ OUTPUT: v,      │
    │ m_μ, m_τ        │    │ V-A current     │    │ m_H derivation  │
    └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
             │                      │                      │
             │                      │                      │
             ▼                      │                      │
    ┌─────────────────┐             │                      │
    │  CHAPTER 5      │             │                      │
    │  3 generacije   │◄────────────┘                      │
    │  ★★★★★          │                                    │
    │                 │                                    │
    │ INPUT: Ch4      │                                    │
    │ mass spectrum   │                                    │
    │                 │                                    │
    │ OUTPUT: why 3   │                                    │
    │ families        │                                    │
    └────────┬────────┘                                    │
             │                                             │
             ▼                                             │
    ┌─────────────────┐                                    │
    │  CHAPTER 6      │◄───────────────────────────────────┘
    │  Neutrini       │
    │  ★★★★★          │
    │                 │
    │ INPUT: edge     │
    │ mode + Ch5      │
    │                 │
    │ OUTPUT: m_ν,    │
    │ PMNS matrix     │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  CHAPTER 7      │
    │  CKM & CP       │
    │  ★★★★           │
    │                 │
    │ INPUT: Ch5,Ch6  │
    │ mixing patterns │
    │                 │
    │ OUTPUT: CKM,    │
    │ CP phase        │
    └─────────────────┘
```

**Dependency chains:**
1. **Lepton masses → Generations → Neutrinos → CKM/CP**
2. **V-A (parallel)** — can proceed independently
3. **Higgs (parallel)** — can proceed independently

---

## CHAPTER 4: LEPTONSKE MASE IZ THICK-BRANE SPEKTRA

### Priority: ★★★★★ (CRITICAL)

### Cilj
Derivirati m_e = 0.511 MeV, m_μ = 105.66 MeV, m_τ = 1776.9 MeV
iz geometrije thick-brane i Z₆ simetrije.

### Postojeći EDC temelji
1. **Mode indices** već uspostavljeni: n_e = 0, n_μ = 1, n_τ = 2 (Ch1, §1.7)
2. **Lattice cell energy:** σr_e² = 5.86 MeV (Ch2, Ch3)
3. **Electron = ground mode** brane defekta (§1.7.3)
4. **Muon/Tau = excited states** istog sektora (§1.7.1)

### Predloženi pristup

#### A) Thick-Brane Mode Equation
Riješiti eigenvalue problem za spinor polje u thick-brane potencijalu:

```
[-∂²/∂y² + V(y)] ψ_n(y) = E_n² ψ_n(y)
```

gdje je V(y) potencijal koji lokalizira modove na brani.

**Ansatz za V(y):**
- Asimetrični profil iz Plenum inflowa (već definiran u Ch3):
  ```
  m(y) = m₀(1 - e^{-y/λ})
  ```
- λ ~ Δ (brane thickness)
- m₀ ~ σ/r_e (bulk mass scale from membrane tension)

#### B) Mass Formula Derivation

**Hipoteza [P]:**
```
m_n = m₀ · f(n, Z₆)
```
gdje f(n, Z₆) uključuje:
- Mode index n
- Hexagonal degeneracy factors

**Konkretni ansatz za ispitivanje:**

1. **Harmonic oscillator analogy:**
   ```
   E_n = ℏω(n + 1/2)
   m_n ∝ √(n + 1/2)
   ```
   Problem: m_μ/m_e ≈ 207 ≠ √3 ≈ 1.73

2. **Exponential mode spacing:**
   ```
   m_n = m₀ · α^n
   ```
   Za m_μ/m_e = 207 i m_τ/m_μ = 16.8:
   α_1 ≈ 207, α_2 ≈ 17 — NIJE konstanta!

3. **Power-law with Z₆ factor:**
   ```
   m_n = m₀ · n! · (6^n / Z₆_degeneracy)
   ```

4. **Koide-inspired approach:**
   Koide formula: (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

   **EDC interpretacija:** Ova relacija može slijediti iz
   constraint-a na overlap integrale tri moda:
   ```
   ∫ ψ_0 ψ_1 ψ_2 dy = geometrijski faktor
   ```

#### C) Konkretna strategija

**Korak 1:** Riješiti thick-brane mode equation numerički
za različite V(y) profile.

**Korak 2:** Identificirati koji profil V(y) daje:
- m₀ ~ 0.5 MeV (ground state = electron)
- m₁/m₀ ~ 200 (first excited = muon)
- m₂/m₁ ~ 17 (second excited = tau)

**Korak 3:** Povezati V(y) parametre s poznatim EDC
veličinama (σ, r_e, Δ).

**Korak 4:** Provjeriti je li rezultat konzistentan s Koide.

### Očekivani output
- Explicit formula: m_n = f(σ, r_e, n)
- Numerical verification: errors < 5% for all three leptons
- Koide formula kao CONSEQUENCE, ne input

### Rizici
- Možda ne postoji jednostavna formula
- Možda treba više parametara nego što EDC ima

### Status promjena
- [BL] → [Dc]: Leptonske mase postaju derivirane
- Koide: [BL] → [Der]

---

## CHAPTER 5: TRI GENERACIJE — TOPOLOŠKI IZVOR

### Priority: ★★★★★ (FUNDAMENTAL)

### Cilj
Odgovoriti na pitanje: **ZAŠTO POSTOJE TOČNO 3 GENERACIJE?**

### Postojeći EDC temelji
1. **Z₆ = Z₂ × Z₃** simetrija
2. **Z₃ → color (3 boje)**
3. **Tri mode indeksa** za leptone (n = 0,1,2)

### Predloženi pristup

#### A) Topological Argument

**Hipoteza [P]:** Broj generacija = broj nezavisnih
topoloških sektora thick-brane mode spektra.

**Mehanizam:**
1. Z₆ ima 3 nezavisna Z₂ podgrupa
2. Svaka Z₂ definira jedan "flavor sektor"
3. Rezultat: 3 familije

**Problem:** Z₆ ima samo JEDAN Z₂ podgrupu,
ne 3! Dakle ovaj argument ne radi direktno.

#### B) Mode Spectrum Truncation

**Hipoteza [P]:** Samo 3 moda su stabilna
(viši modovi raspadaju se prebrzo).

**Argument:**
```
Lifetime(n) ∝ exp(-n · barrier)
```

Za n ≥ 3, lifetime < Planck time → ne observable.

**Problem:** Zašto baš 3? Treba derivirati cutoff.

#### C) Z₆ × Something = Generation Structure

**Nova hipoteza [P]:**
Generacije dolaze iz DRUGOG faktora simetrije,
ne iz Z₆ direktno.

**Kandidati:**
1. **Bulk topology:** π₁(M₅) = Z₃?
2. **Brane winding:** Winding numbers u 5D
3. **KK tower truncation:** First 3 KK modes

**Najobećavniji pristup:**
```
Full symmetry = Z₆ × Z₃_generation
```
gdje Z₃_generation dolazi iz topologije M₅.

#### D) Konkretna strategija

**Korak 1:** Analizirati M₅ topologiju — ima li prirodni Z₃?

**Korak 2:** Provjeriti KK redukciju — koliko modova preživljava?

**Korak 3:** Povezati s leptonskim masama iz Ch4.

**Korak 4:** Proširiti na kvark sektor.

### Očekivani output
- Derivacija: N_gen = 3 iz geometrije
- Prediction: Nema 4. generacije
- Falsifiable: Ako se nađe 4. generacija → model fails

### Povezanost s Ch4
- Ch4 daje mass spectrum za n = 0,1,2
- Ch5 objašnjava ZAŠTO samo n = 0,1,2

---

## CHAPTER 6: NEUTRINI KAO RUBNI MODOVI

### Priority: ★★★★★ (EXPERIMENTALLY ACTIVE)

### Cilj
1. Derivirati m_ν < 1 eV iz edge-mode energije
2. Derivirati PMNS matricu iz geometrijskog miješanja
3. Adresirati Dirac vs Majorana pitanje

### Postojeći EDC temelji (iz §1.9)
1. **Neutrino = edge mode** na bulk-brane interfaceu
2. **Suppressed coupling** iz malog overlap integrala
3. **Chirality filter** P_chir selektira L-handed ν
4. **Three flavors** (ν_e, ν_μ, ν_τ) — match charged leptons

### Predloženi pristup

#### A) Edge-Mode Energy Calculation

**Setup:**
Edge mode zadovoljava boundary condition na y = -δ/2:
```
[BC] ψ_ν|_{y=-δ/2} = 0 ili ∂_y ψ_ν|_{y=-δ/2} = 0
```

**Energija edge moda:**
```
E_edge ~ exp(-separation/λ) × bulk_scale
```

Za separation ~ 10-100 × λ:
```
m_ν ~ 10^{-11} × m_bulk ~ 0.1 eV
```
konzistentno s opažanjima!

#### B) PMNS Matrix from Geometric Mixing

**Hipoteza [P]:**
Flavor mixing dolazi iz overlap integrala:
```
U_αi = ∫ ψ_α(y) × ψ_i(y) dy
```
gdje:
- α = e, μ, τ (flavor eigenstates)
- i = 1, 2, 3 (mass eigenstates)

**Konkretna strategija:**
1. Riješiti edge mode equation za 3 masa
2. Izračunati overlap integrale
3. Usporediti s PMNS vrijednostima

#### C) Dirac vs Majorana

**EDC perspektiva:**
- **Dirac:** ν i ν̄ su različiti edge modovi
- **Majorana:** Isti mod, različite faze

**Testable prediction:**
Ako je neutrino Majorana → neutrinoless double beta decay.

**EDC hypothesis [P]:**
Edge mode structure može preferirati Dirac
(separate left/right boundaries).

#### D) Mass Hierarchy

**Normal vs Inverted:**
Ovisi o relative positions edge modova.

**Prediction možda moguća** iz geometrije.

### Očekivani output
- m_ν derivacija: m_ν ~ exp(-L/λ) × m_0
- PMNS elements: θ₁₂, θ₂₃, θ₁₃ iz overlapsa
- Dirac/Majorana: prediction based on BC structure

### Rizici
- Puno parametara u BC
- Možda model underdetermined

---

## CHAPTER 7: CKM MATRICA I CP VIOLACIJA

### Priority: ★★★★

### Cilj
1. Derivirati CKM matricu iz kvark mode overlapa
2. Identificirati geometrijski izvor CP faze
3. Povezati s bariogenezom

### Preduvjeti
- Ch5 (generacijska struktura)
- Ch6 (mixing formalism iz PMNS)

### Predloženi pristup

#### A) Quark Sector Extension

**Kvarkovi u EDC:**
- u, c, t = "up-type" brane modovi (Q = +2/3)
- d, s, b = "down-type" brane modovi (Q = -1/3)

**Mode indices (analogija s leptonima):**
```
up-type:   n_u = 0, n_c = 1, n_t = 2
down-type: n_d = 0, n_s = 1, n_b = 2
```

#### B) CKM from Overlap Mismatch

**Ključna ideja:**
CKM = overlap mismatch između up i down sektora.

```
V_CKM = U_up† × U_down
```

gdje U_up i U_down su rotation matriceiz
bulk-to-brane projections za svaki sektor.

**Fizička slika:**
Up i down modovi imaju RAZLIČITE profile ψ(y)
jer imaju različite mase → overlap nije dijagonalan.

#### C) CP Phase from Geometry

**Standard Model:** CP faza δ je "just a parameter."

**EDC hipoteza [P]:**
CP faza dolazi iz COMPLEX boundary conditions:
```
ψ|_boundary = e^{iδ} × ψ'|_boundary
```

Ova faza je geometrijska — dolazi iz
relative orientation between sectors.

#### D) Connection to Baryogenesis

**Sakharov conditions:**
1. Baryon number violation ✓ (može iz topology)
2. C and CP violation ✓ (ako deriviramo δ)
3. Out of equilibrium ✓ (cosmological expansion)

**EDC može potencijalno objasniti matter-antimatter asymmetry
ako CP faza ima geometrijski izvor.**

### Očekivani output
- CKM elements: |V_us|, |V_cb|, |V_ub| iz overlapa
- CP phase: δ iz boundary geometry
- Jarlskog invariant: J = Im(V_us V_cb V_ub* V_cs*)

### Rizici
- Kvark sektor kompliciraniji od leptonskog
- Možda treba QCD efekte

---

## CHAPTER 8: HIGGSOV SEKTOR U 5D

### Priority: ★★★★

### Cilj
1. Derivirati Higgs VEV v = 246.2 GeV
2. Derivirati Higgs mass m_H = 125 GeV
3. Objasniti electroweak symmetry breaking geometrijski

### Trenutni status
- v = 246.2 GeV koristi se kao [BL] input
- m_H nije uopće adresirano

### Predloženi pristup

#### A) Higgs as 5D Scalar Fluctuation

**Hipoteza [P]:**
Higgs polje = fluktuacija brane položaja u 5D.

```
h(x) = δy(x) × (tension parameter)
```

Ovo je poznato kao "brane bending mode."

#### B) VEV from Brane Tension

**Dimensional analysis:**
```
v² ~ σ × r_e / (coupling factor)
```

Poznato: σr_e² = 5.86 MeV, r_e ~ 1 fm

**Problem:** v = 246 GeV je puno veće od 5.86 MeV!
Treba veliki enhancement factor.

**Možda rješenje:**
```
v ~ σ × r_e × N_effective
```
gdje N_effective ~ 10^4 dolazi iz collective modes.

#### C) Higgs Mass from Curvature

**Hipoteza [P]:**
```
m_H² ~ ∂²V/∂h² |_{h=v}
```
gdje V(h) je effective potential za brane bending.

**Konkretni ansatz:**
```
V(h) = λ(h² - v²)² + curvature terms
```

Curvature terms dolaze iz 5D Ricci scalar.

#### D) Electroweak Symmetry Breaking

**Standard picture:** SU(2)_L × U(1)_Y → U(1)_EM

**EDC reinterpretation:**
- Z₆ → Z₃ (color preserved)
- Remaining Z₂ → electroweak breaking

**Geometrijska slika:**
Brane "freezes" u određenoj Z₂ orijentaciji,
breaking the full Z₆ to residual Z₃.

### Očekivani output
- v derivacija: v = f(σ, r_e, geometry)
- m_H derivacija: m_H = g(v, curvature)
- EWSB: geometrijska interpretacija

### Rizici
- Ovo je najspekulativnije poglavlje
- Možda Higgs sektor zahtijeva separate physics

---

## CHAPTER 9: V−A STRUKTURA — KVANTITATIVNA DERIVACIJA

### Priority: ★★★★

### Cilj
1. Derivirati P_chir operator iz boundary conditions
2. Pokazati da V−A slijedi automatski
3. Izračunati beta decay asymmetry coefficients

### Postojeći EDC temelji
1. **P_chir postuliran** ali ne deriviran (§1.7, §1.9)
2. **MIT bag BC sketch** dan (§1.7.1)
3. **V−A stated as output** ali ne proven

### Predloženi pristup

#### A) Explicit Boundary Condition Derivation

**Start:** 5D Dirac equation u thick-brane background:
```
[iΓ^A ∂_A - M(y)] Ψ = 0
```
gdje M(y) je y-dependent mass profile.

**Boundary conditions na y = +δ/2:**
```
(1 - iΓ^5 n_μ Γ^μ) Ψ|_{boundary} = 0
```

Ovo je generalized MIT bag condition.

#### B) Chirality Projection from BC

**Pokazati:**
Gornja BC automatski projicira:
- Left-handed za ℓ⁻
- Right-handed za ν̄

**Matematika:**
```
Γ^5 Ψ_L = -Ψ_L
Γ^5 Ψ_R = +Ψ_R
```

BC preferira one kombinacije koje zadovoljavaju
boundary matching.

#### C) V−A Current Derivation

**Cilj:** Pokazati da 4D effective current ima oblik:
```
J^μ = ψ̄_L γ^μ ψ_L = ψ̄ γ^μ (1-γ^5)/2 ψ
```

**Pristup:**
1. Integrate out 5th dimension
2. Keep only boundary-compatible modes
3. Result: purely left-handed current

#### D) Beta Decay Asymmetries

**Observable quantities:**
- A (beta asymmetry)
- a (beta-neutrino correlation)
- b (Fierz interference)
- B (neutrino asymmetry)

**Standard Model predictions:**
A = -0.1184, a = -0.103, etc.

**EDC should reproduce these** if V−A derivation correct.

### Očekivani output
- P_chir explicit form: (1 - iΓ^5 n·Γ)/2
- V−A proof: J^μ ∝ ψ̄γ^μ(1-γ^5)ψ
- Asymmetry predictions: A, a, b, B values

### Status promjena
- V−A: [P] → [Der]
- P_chir: [P] → [Dc]

---

## IMPLEMENTATION PRIORITY ORDER

### Phase 1 (Parallel tracks)
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ CHAPTER 4   │  │ CHAPTER 9   │  │ CHAPTER 8   │
│ Lepton mass │  │ V-A struct. │  │ Higgs       │
│ [highest]   │  │ [high]      │  │ [medium]    │
└──────┬──────┘  └─────────────┘  └─────────────┘
       │
       ▼
┌─────────────┐
│ CHAPTER 5   │
│ 3 gens      │
│ [highest]   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CHAPTER 6   │
│ Neutrinos   │
│ [high]      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CHAPTER 7   │
│ CKM/CP      │
│ [medium]    │
└─────────────┘
```

### Phase 2 (After Phase 1 completed)
- Integration across chapters
- Cross-referencing
- Numerical consistency checks

### Phase 3 (Final)
- Experimental predictions compilation
- Falsifiability matrix
- Open problems update

---

## RISK ASSESSMENT

| Chapter | Risk Level | Main Risk | Mitigation |
|---------|------------|-----------|------------|
| 4 | MEDIUM | No simple formula exists | Try multiple ansätze |
| 5 | HIGH | Can't derive 3 uniquely | Accept as [P] if needed |
| 6 | MEDIUM | Too many BC parameters | Constrain from Ch5 |
| 7 | HIGH | QCD complications | Focus on CKM angles only |
| 8 | VERY HIGH | Higgs may need separate physics | Mark as [P]/[OPEN] |
| 9 | LOW | V-A is well-defined math | Should succeed |

---

## SUCCESS CRITERIA

### Chapter 4
- [ ] m_e, m_μ, m_τ derived with <5% error each
- [ ] Koide relation emerges naturally
- [ ] Formula uses only σ, r_e, n (no extra parameters)

### Chapter 5
- [ ] N_gen = 3 derived (not assumed)
- [ ] Prediction: no 4th generation
- [ ] Consistent with Ch4 mass spectrum

### Chapter 6
- [ ] m_ν ~ 0.1 eV derived from geometry
- [ ] At least 2 PMNS angles approximately correct
- [ ] Dirac/Majorana preference stated

### Chapter 7
- [ ] |V_us| ~ 0.22 from overlap
- [ ] CP phase δ has geometric origin
- [ ] Connection to baryogenesis sketched

### Chapter 8
- [ ] v derived from σ, r_e (order of magnitude)
- [ ] m_H = 125 GeV consistent with derived v
- [ ] EWSB has geometric interpretation

### Chapter 9
- [ ] P_chir derived from 5D BC
- [ ] V−A current proven
- [ ] Beta asymmetry A predicted correctly

---

## APPENDIX: KEY EDC PARAMETERS

| Parameter | Value | Source | Status |
|-----------|-------|--------|--------|
| σr_e² | 5.86 MeV | Lattice cell energy | [Cal] |
| r_e | ~1 fm | Lattice spacing | [Cal] |
| sin²θ_W | 1/4 (bare) | Z₆ symmetry | [Der] |
| Z₆ | Z₂ × Z₃ | Hexagonal BC | [P] |
| Δ | Brane thickness | ~r_e | [P] |
| n_e, n_μ, n_τ | 0, 1, 2 | Mode indices | [P]/[I] |

---

## CONCLUSION

The proposed 6 chapters would extend Part II from ~25% to ~80% coverage
of SM Weak physics. The key insight is that ALL new results should derive
from the SAME geometric foundation (Z₆ + thick-brane), maintaining
theoretical coherence.

**Most critical:** Chapter 4 (lepton masses) is the decisive test.
If EDC can derive m_e, m_μ, m_τ from geometry, the framework gains
significant credibility. If not, the theory remains structural/interpretive
rather than predictive.

---

*Document generated by Claude Opus 4.5 for EDC Project*
*Status: PROPOSAL — awaiting Igor's review and approval*
