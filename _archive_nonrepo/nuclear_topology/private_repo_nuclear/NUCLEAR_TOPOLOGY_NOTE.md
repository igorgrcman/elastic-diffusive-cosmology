# Nuklearna Topologija u 5D: Neutron kao Topološki Adapter

**Status:** Interna istraživačka bilješka / eksploracija hipoteza
**Verzija:** 1.0 (2026-01-15)
**Autor:** Igor Gričman

---

> **UPOZORENJE: Ova bilješka NIJE dio Paper 3.**
> Nije kompilirana u main.tex. Služi isključivo kao istraživački zapis
> za buduće formalizacije. Nijedna tvrdnja iz ove bilješke ne nadograđuje
> epistemički status claim-ova u Paper 3.

---

## 1. Svrha i Opseg

### 1.1 Cilj bilješke

Ova bilješka pokušava **formalizirati intuiciju** da neutroni u atomskim jezgrama
djeluju kao "topološki adapteri" ili "puferi" koji omogućuju stabilno pakiranje
protona unutar 5D membranske ontologije EDC-a.

**Ključna hipoteza [P]:** Neutroni nisu samo "dodatna masa" već topološki nužni
elementi koji smanjuju geometrijsku frustraciju u mreži Y-čvorišta na membrani.

### 1.2 Što ova bilješka NIJE

- **Nije derivacija.** Nijedna formula ovdje nije izvedena iz 5D akcije.
- **Nije dio Paper 3.** Ništa se ne kompilira niti referencira.
- **Nije numerička verifikacija.** Prikazani primjeri su kvalitativni.

### 1.3 Naprijed-program

Ova bilješka definira formalni okvir za buduće:
1. Enumeraciju grafova za male (Z,N)
2. Optimizaciju ulaganja X: V → M⁴
3. Usporedbu s poznatim trendovima nuklearne stabilnosti

---

## 2. Objekti i Definicije

### 2.1 Nuklearna Mreža kao Graf

**Definicija 2.1 [P]:** *Nuklearna mreža* je neusmjereni graf G = (V, E) gdje:

- **V** je skup vrhova (čvorova)
- **E** ⊆ V × V je skup bridova (veza)

**Definicija 2.2 [P]:** Vrhovi imaju tipove:

| Tip | Oznaka | Fizikalna interpretacija |
|-----|--------|--------------------------|
| p-vrh | vₚ | Proton-like čvor (naboj +1) |
| n-vrh | vₙ | Neutron-like čvor (naboj 0) |

**Napomena:** Ova identifikacija je **postulat [P]**, ne derivacija. Pretpostavljamo
da svaki nukleon odgovara jednom vrhu u grafu, ali veza s Y-junction geometrijom
iz Paper 3 ostaje **[OPEN]**.

### 2.2 Ulaganje u Membranu

**Definicija 2.3 [P]:** *Membranski embedding* je preslikavanje:

$$X: V \to \mathcal{M}^4$$

koje svakom vrhu pridružuje položaj na 4D membrani (brani).

**Definicija 2.4 [P]:** *Prošireno ulaganje* uključuje i bulk koordinatu:

$$\tilde{X}: V \to \mathcal{M}^4 \times \mathbb{R}_{\geq 0}$$
$$\tilde{X}(v) = (X(v), \xi_v)$$

gdje $\xi_v \geq 0$ označava lokalnu "dubinu" u bulk (5. dimenziju).

**Status:** Ovo je toy-model. Pravi 5D embedding zahtijeva tretman inducirane
metrike i Israel junction uvjeta — vidi Appendix J u Paper 3 za detalje.

### 2.3 Junction/Steiner Koncept

**Definicija 2.5 [P]:** Za vrh v ∈ V stupnja d(v) = k, definiramo *junction konfiguraciju*
kao skup k jediničnih vektora {ê₁, ..., êₖ} koji pokazuju prema susjedima.

**Postulat P-Steiner [P]:** Za minimizaciju napetosti stringova, optimalni kutovi
između bridova na čvoru stupnja 3 su **120°** (Steiner uvjet).

**Derivacijski sketch [Dc]:** Ako svi bridovi imaju jednaku napetost T, ravnoteža sila
na čvoru zahtijeva:

$$\sum_{i=1}^{k} T \cdot \hat{e}_i = 0$$

Za k = 3 u 2D, jedino rješenje s jednakim napetostima je 120° konfiguracija.

**Upozorenje:** Ovo vrijedi samo za:
- Jednake napetosti na svim bridovima
- Planarnu konfiguraciju
- Bez vanjskih sila

Za nuklearni slučaj, napetosti mogu varirati i konfiguracija može biti 3D.

### 2.4 Zatvorene Petlje

**Definicija 2.6 [P]:** *Ciklus* u grafu G je zatvorena staza bez ponavljanja vrhova.

**Definicija 2.7 [P]:** *Minimalna duljina ciklusa* (girth) grafa G je:

$$g(G) = \min\{|C| : C \text{ je ciklus u } G\}$$

**Hipoteza H-loop [P]:** Stabilne jezgre preferiraju grafove s $g(G) \geq 3$
(izbjegavanje "multiple edges" i self-loops).

---

## 3. Energetski Funkcional (Prijedlog Modela)

### 3.1 Opći Oblik

**Postulat P-energy [P]:** Predlažemo energetski funkcional:

$$\boxed{E[G, X] = E_{\text{tension}} + E_{\text{junction}} + E_{\text{bulk}} + E_{\text{bend}}}$$

### 3.2 Član Napetosti Bridova

$$E_{\text{tension}} = \sum_{(i,j) \in E} T_{ij} \cdot L_{ij}(X)$$

gdje je:
- $T_{ij}$ = napetost na bridu (i,j) **[P]**
- $L_{ij}(X) = |X(i) - X(j)|$ = duljina brida u embeddingu

**Status:** [P] — Pretpostavljamo da napetost stringova doprinosi energiji
proporcionalno duljini. Ovo je standardno u string-junction modelima.

### 3.3 Član Kutne Frustracije

$$E_{\text{junction}} = \sum_{v \in V} J_v \cdot F(\{\theta_k\}_v)$$

gdje je:
- $J_v$ = junction penalty koeficijent **[P]**
- $\{\theta_k\}_v$ = skup kutova između bridova na vrhu v
- $F(\cdot)$ = frustracija funkcija

**Prijedlog za F [P]:**

Za vrh stupnja 3:
$$F(\theta_1, \theta_2, \theta_3) = \sum_{k=1}^{3} (\theta_k - 120°)^2$$

Ovo je minimalno (= 0) za Steiner konfiguraciju.

**Status:** [P] — Kvadratni oblik je ansatz. Prava forma slijedi iz razvoja
5D akcije oko ravnotežne konfiguracije **[OPEN]**.

### 3.4 Bulk/Pressure Član

$$E_{\text{bulk}} = -P_{\text{bulk}} \cdot V_{\text{eff}}(G, X)$$

gdje je:
- $P_{\text{bulk}} > 0$ = tlak Plenuma **[P]** (KB-POST-005)
- $V_{\text{eff}}$ = efektivni volumen koji zauzima mreža

**Status:** [P]/[OPEN] — Forma ovog člana nije izvedena. Pretpostavljamo da
veći volumen daje energetsku prednost (smanjuje "crowding").

### 3.5 Član Savijanja (Opcionalno)

$$E_{\text{bend}} = \kappa \int (H)^2 \, dA$$

gdje je H = srednja zakrivljenost membrane.

**Diskretni surogat [P]:**
$$E_{\text{bend}}^{\text{disc}} = \kappa \sum_{v \in V} (\xi_v - \bar{\xi})^2$$

**Status:** [P] — Ovo kažnjava neuniformnost bulk-dubine.

---

## 4. Neutron kao Adapter: Matematička Formulacija

### 4.1 Glavna Hipoteza

> **Hipoteza H1 [P]:**
> Za Z > 1, minimizatori funkcionale E[G, X] preferiraju umetanje n-vrhova
> kako bi smanjili kutnu frustraciju i lokalnu "crowding" protona,
> čime se omogućuju stabilna ulaganja bez singularnih zakrivljenosti.

**Formalno:**

Neka je $G_0 = (V_0, E_0)$ graf samo s p-vrhovima (Z protona, 0 neutrona).
Neka je $G_n = (V_n, E_n)$ graf s Z protona i N neutrona.

**H1 tvrdi:** Postoji N* > 0 takav da:

$$\min_X E[G_{N^*}, X] < \min_X E[G_0, X]$$

uz uvjet da je $G_{N^*}$ povezan graf.

### 4.2 Toy Primjer: Z = 2 (Helij)

#### Slučaj A: Bez neutrona (N = 0)

Graf: Dva p-vrha povezana jednim bridom.

```
    p ——— p
```

**Problem:** Nema junction frustracije (stupanj = 1), ali:
- Sustav je linearan, nema zatvorenog volumena
- $V_{\text{eff}} \approx 0$ → $E_{\text{bulk}}$ član nije aktivan

**Energija [P]:**
$$E[G_0, X] = T \cdot L_{12}$$

Minimizacija → $L_{12} \to 0$ (protoni se približavaju).

**Fizikalni problem:** Coulombovo odbijanje nije uključeno! U realnosti,
$^2$He ne postoji kao stabilna jezgra.

#### Slučaj B: S 2 neutrona (N = 2) — $^4$He

Graf: 4 vrha (2p + 2n) formiraju tetraedar ili kvadrat.

```
    p ——— n
    |     |
    n ——— p
```

**Prednosti:**
- Stupanj svakog vrha = 2 ili 3 → junctions postoje
- Može se formirati zatvoreni volumen
- Neutroni "razdvajaju" protone → smanjuju Coulomb frustraciju

**Energija [P] (kvalitativno):**
$$E[G_2, X] = 4T \cdot \bar{L} + \sum_v J_v F_v - P \cdot V_{\text{tetra}}$$

Ako je $V_{\text{tetra}} > 0$, bulk član može kompenzirati tension.

**Zaključak [P]:** Model sugerira da N = 2 stabilizira Z = 2 kroz:
1. Geometrijsko razdvajanje protona
2. Aktivaciju bulk/volume člana
3. Distribuciju junction frustracije

### 4.3 Generički Mehanizam

**Teza [P]:** Neutroni djeluju kao "topološki adapteri" na tri načina:

1. **Geometrijski spacer:** Povećavaju prosječnu udaljenost p-p parova
2. **Junction distributor:** Dijele junction frustraciju na više čvorova
3. **Volume enabler:** Omogućuju formiranje zatvorenog volumena

---

## 5. Prvih 10 Elemenata — Diskusija

> **UPOZORENJE:**
> Ova tablica NIJE derivacija. To je mapiranje konvencionalne nuklearne
> kompozicije na predloženu mrežnu sliku. Sve interpretacije su **[P]**.

| Z | Element | Stabilan (Z,N) | Topološka interpretacija [P] |
|---|---------|----------------|------------------------------|
| 1 | H | (1,0) | Trivijalan: 1 p-vrh, nema mreže. Stabilan jer je najjednostavniji. |
| 1 | D | (1,1) | 1p + 1n: Najjednostavnija "veza". N sugerira stabilizaciju dipolne konfiguracije. |
| 2 | He | (2,2) | Tetraedar/kvadrat mogućnost. Prva "zatvorena" topologija? α-čestica stabilnost [P]. |
| 3 | Li | (3,3), (3,4) | Li-6, Li-7: Dodavanje n sugerira rast frustracije s Z=3 (trokut protona). |
| 4 | Be | (4,5) | Be-9: Asimetrija (N>Z) sugerira visoku frustraciju za Z=4 bez dodatnih n. |
| 5 | B | (5,5), (5,6) | B-10, B-11: Pentagon protona? Kutna frustracija (108° vs 120°) [P]. |
| 6 | C | (6,6) | **C-12: Heksagon hipoteza** — prvi "jednostavan zatvoreni ciklus" s 120° [P]. |
| 7 | N | (7,7) | N-14: Heptagon ili heksagon+1? Frustracija raste [P]. |
| 8 | O | (8,8) | O-16: Dvostruki magic number. Moguća simetrična 3D struktura [P]. |
| 9 | F | (9,10) | F-19: Asimetrija (N>Z) opet sugerira frustraciju kompenzaciju. |
| 10 | Ne | (10,10) | Ne-20: Dekagon ili nested struktura? [P]. |

**Napomene:**

1. **Magic numbers (2, 8, 20, ...):** U ovom modelu, magic numbers bi mogli
   odgovarati grafovima s minimalnom ukupnom frustracijom [P].

2. **N ≥ Z trend:** Za Z > 20, N > Z postaje norma. Model sugerira da
   veći Z zahtijeva više n-adaptera za stabilnost [P].

3. **Izotopi:** Postojanje više stabilnih izotopa za isti Z sugerira
   više lokalnih minimuma E[G, X] za različite N [P].

---

## 6. Carbon-12: Heksagon/Steiner Konjektura

### 6.1 Formulacija Konjekture

> **Konjektura C12 [P]:**
> Nisko-frustracijsko ulaganje za Z = 6 (Carbon-12) je 6-ciklus
> s približno uniformnim junction kutovima blizu 120°, čineći ga
> prvim "jednostavnim zatvorenim loop" kandidatom u ovom modelu.

**Grafička reprezentacija:**

```
        p₁
       /  \
     n₆    n₁
     |      |
     p₆    p₂
     |      |
     n₅    n₂
       \  /
        p₃
       /  \
     n₄    n₃
     |      |
     p₅    p₄
       \  /
        p₃  ← [GREŠKA: ovo nije 6-ciklus nego veći graf]
```

**Ispravna verzija — jednostavan 6-ciklus alternansa:**

```
      p — n — p
     /         \
    n           n
     \         /
      p — n — p
```

Ovdje p i n alterniraju duž ciklusa duljine 12 (6p + 6n).

### 6.2 Zašto Heksagon?

1. **120° kutovi:** U pravilnom heksagonu, unutarnji kutovi su 120° —
   točno Steiner optimum za stupanj 3.

2. **Zatvoreni loop:** Prvi element gdje je moguć potpuno zatvoren
   ciklus bez "loose ends".

3. **α-cluster:** C-12 je poznat kao 3α jezgra. Heksagon može biti
   viđen kao 3 spojena tetraedra (He-4 jedinice).

### 6.3 Što bi Činilo Dokaz?

**Nužni uvjeti za potvrdu [I]:**

1. **Enumeracija:** Minimizacija E[G, X] preko svih grafova za (Z=6, N=6)
   pokazuje basin oko 6-ciklusa ili srodne strukture.

2. **Robusnost:** Rezultat stabilan pod moderatnim varijacijama parametara
   (T, J, P, κ).

3. **Usporedba:** E[6-ciklus] < E[alternativni grafovi] za razumne parametre.

**Trenutni status:** **[P]** — Konjektura nije verificirana.

### 6.4 Eksplicitno Odbacivanje "QED" Jezika

> **UPOZORENJE:**
> Fraza "QED" (Quod Erat Demonstrandum) je ZABRANJENA u ovom kontekstu.
> Nijedna tvrdnja o C-12 nije **dokazana**. Sve ostaje na razini hipoteze [P].

---

## 7. Plan Testiranja / Sljedeći Koraci

### 7.1 Računalni Eksperimenti [I]

**Korak A: Enumeracija Grafova**
- Za (Z, N) ∈ {(1,0), (1,1), (2,2), (3,3), (3,4), ..., (6,6)}
- Generiraj sve povezane grafove s Z p-vrhova i N n-vrhova
- Status: [I] — implementacijski plan

**Korak B: Optimizacija Embeddinga**
- Za svaki graf G, optimiziraj X: V → ℝ² ili ℝ³
- Metoda: gradient descent na E[G, X]
- Constraints: minimalne udaljenosti, granični uvjeti
- Status: [I] — implementacijski plan

**Korak C: Rangiranje po Energiji**
- Rangiraj sve (G, X*) parove po E[G, X*]
- Usporedi s poznatim stabilnostima:
  - Stabilan izotop → trebao bi biti nisko rangiran
  - Nestabilan → trebao bi biti visoko rangiran
- Status: [I] — implementacijski plan

**Korak D: Validacija Neutron-Adapter Hipoteze**
- Za fiksni Z, variraj N
- Mjeri: ΔE(N) = E[G_N, X*_N] - E[G_0, X*_0]
- Pitanje: Postoji li N* gdje ΔE < 0?
- Status: [I] — implementacijski plan

### 7.2 Analitički Koraci [I]

**Korak E: Derivacija F(θ) iz 5D akcije**
- Razvij 5D brane akciju oko Y-junction konfiguracije
- Izvedi frustracija funkciju F kao drugučlan u ekspanziji
- Status: [I]/[OPEN] — zahtijeva rad iz Appendix J

**Korak F: Veza s Nuclear Shell Model**
- Usporedi predviđene "magic" konfiguracije s empirijskim magic numbers
- Pitanje: Mogu li se (2, 8, 20, 28, 50, 82, 126) reproducirati?
- Status: [I] — dugoročni cilj

### 7.3 Prioriteti

| Prioritet | Korak | Razlog |
|-----------|-------|--------|
| 1 | A + B | Proof-of-concept za male grafove |
| 2 | C | Validacija protiv poznatih podataka |
| 3 | D | Test ključne hipoteze H1 |
| 4 | E | Povećanje epistemičkog statusa [P] → [Dc] |
| 5 | F | Veza s etabliranom nuklearnom fizikom |

---

## 8. Zaključak

### 8.1 Što je Postignuto

1. **Formalni okvir [P]:** Definirani su objekti (graf, embedding, junction, ciklus).
2. **Energetski funkcional [P]:** Predložen E[G, X] s četiri člana.
3. **Hipoteza H1 [P]:** Formulirana teza o neutronima kao adapterima.
4. **Plan testiranja [I]:** Konkretan program za računalnu verifikaciju.

### 8.2 Što NIJE Postignuto

1. **Derivacija iz 5D akcije:** Svi članovi su [P], ne [Dc] ili [D].
2. **Numerička verifikacija:** Nema optimizacija, nema podataka.
3. **Veza s Paper 3:** Ova bilješka je izolirana.

### 8.3 Epistemički Status

| Tvrdnja | Status | KB-ID (proposed) |
|---------|--------|------------------|
| Nuklearna mreža kao graf | [P] | KB-POST-050 |
| Steiner 120° za d=3 | [Dc] | KB-DERIV-050 |
| Energetski funkcional E[G,X] | [P] | KB-POST-051 |
| H1: Neutroni kao adapteri | [P] | KB-POST-052 |
| C12 heksagon konjektura | [P] | KB-CONJ-010 |
| Test plan koraci A-F | [I] | KB-IMPL-010 |

---

## Appendix A: Notacija

| Simbol | Značenje |
|--------|----------|
| G = (V, E) | Graf s vrhovima V i bridovima E |
| p-vrh, n-vrh | Proton-like i neutron-like čvor |
| X: V → M⁴ | Embedding mape |
| ξ | Bulk koordinata (5. dimenzija) |
| T | Napetost stringa |
| J | Junction penalty koeficijent |
| P_bulk | Plenum tlak |
| κ | Bending rigidity |
| E[G, X] | Ukupni energetski funkcional |
| θ | Kut između bridova na junctionu |
| d(v) | Stupanj vrha v |
| g(G) | Girth (minimalna duljina ciklusa) |

---

## Appendix B: Epistemičke Oznake

| Oznaka | Značenje |
|--------|----------|
| [P] | Postulate — hipoteza, ansatz |
| [Dc] | Derived conditional — izvedeno uz pretpostavke |
| [D] | Derived — strogo izvedeno |
| [I] | Implementation — plan, ne tvrdnja |
| [OPEN] | Otvoreni problem |
| [BL] | Baseline — vanjska referenca (PDG, etc.) |
| [M] | Mathematics — matematički teorem |

---

*Kraj bilješke.*

---

**Changelog:**
- 2026-01-15: Inicijalna verzija (v1.0)
