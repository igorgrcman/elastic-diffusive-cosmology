# Gap Register (145-str verzija)

**Generirano:** 2026-01-31
**Izvor:** prelet_scan_findings.json + keyword mapping na 461-str verziju
**Ukupno rupa:** 90 (C=22, B=56, A=12)

---

## Prioritetna shema

1. **Tip C** (narativ/mehanizam skok) — najopasnije za čitatelja
2. **Tip B** (fali derivacija/koraci) — srednji prioritet
3. **Tip A** (fali definicija/konvencija) — niži prioritet

Unutar svake kategorije: **SM-risk + dictionary_step** stavke idu na vrh.

---

## Tip C — narativ/mehanizam skok (N=22)

### C-1: Version 2.0 features (str. 4)
- **Target (145):** str. 4, section: Version 2.0 features, eq@L180
- **Source (461):** str. 1-3 (search: Version + features)
- **Minimalni backfill:** Narativ/mehanizam: ubaci dictionary box ili 2–3 rečenice koje eksplicitno vežu 'formalizam' → 'opažljiva veličina'; naglasi uvjete/ograničenja.
- **Ključni pojmovi:** Version, features, Epistemic
- **Loc:** main.tex:180
- **Flags:** `sm_risk`, `dictionary_step`

### C-2: Electron as B3 Vortex (str. 18) ⚠️ CRITICAL
- **Target (145):** str. 18, subsection: Electron as B3 Vortex, eq@L312
- **Source (461):** str. 37-39 (search: Vol(B3))
- **Minimalni backfill:** Narativ/mehanizam: ubaci dictionary box + SM-risk box / preformuliraj u EDC jezik; provjeri \tagDc vs \tagDer
- **Ključni pojmovi:** Electron, B3, Vol(B3)
- **Loc:** chapter_02_ontology.tex:312
- **Flags:** `sm_risk`, `dictionary_step`

### C-3: Stability (isoperimetric) (str. 19)
- **Target (145):** str. 19, subsection: Stability, eq@L344
- **Source (461):** str. 40-42 (search: isoperimetric)
- **Minimalni backfill:** Razdvojiti: (i) matematički teorem [M], (ii) fizička pretpostavka [P]/[I], (iii) topološka zabrana [P]/[Dc:Approx]
- **Ključni pojmovi:** Stability, isoperimetric, theorem
- **Loc:** chapter_02_ontology.tex:344
- **Flags:** `dictionary_step`

### C-4: Mass origin (str. 22)
- **Target (145):** str. 22, subsection: Mass origin, eq@L402
- **Source (461):** str. 44-46 (search: me + σ)
- **Minimalni backfill:** Dictionary box za m_e = σ·Vol(B³) identifikaciju
- **Ključni pojmovi:** Mass, origin, Vol(B3)
- **Loc:** chapter_02_ontology.tex:402
- **Flags:** `dictionary_step`

### C-5: Bosonic Modes (str. 33)
- **Target (145):** str. 33, subsection: Bosonic Modes, eq@L511
- **Source (461):** str. 78-80 (search: Bosonic + Modes)
- **Minimalni backfill:** SM-risk box / preformuliraj u EDC jezik; odvojiti "SM baseline" od "EDC mechanism"
- **Ključni pojmovi:** Bosonic, Modes, spectrum
- **Loc:** chapter_02_ontology.tex:511
- **Flags:** `sm_risk`

### C-6: Frozen-wall ansatz (str. 41)
- **Target (145):** str. 41, section: Frozen-wall ansatz, eq@L210
- **Source (461):** str. 95-97 (search: Frozen + ansatz)
- **Minimalni backfill:** Dictionary box za ansatz → fizička interpretacija
- **Ključni pojmovi:** Frozen, ansatz, step
- **Loc:** chapter_03_frozen.tex:210
- **Flags:** —

### C-7: Z₆ program overview (str. 54)
- **Target (145):** str. 54, section: Z₆ program overview, eq@L155
- **Source (461):** str. 122-124 (search: Z6 + program)
- **Minimalni backfill:** Dictionary box za Z₆ → generacije identifikaciju
- **Ključni pojmovi:** Z6, program, dictionary
- **Loc:** chapter_04_z6_program.tex:155
- **Flags:** `dictionary_step`

### C-8: sin²θ_W identification (str. 63) ⚠️ CRITICAL
- **Target (145):** str. 63, subsection: sin²θ_W identification, eq@L288
- **Source (461):** str. 150-152 (search: sin + θ_W)
- **Minimalni backfill:** Dictionary box + SM-risk box; razdvojiti [Der:Sym] (geometrijski omjer) od [Dc] (SM identifikacija)
- **Ključni pojmovi:** sin, θ_W, tree
- **Loc:** chapter_06_electroweak.tex:288
- **Flags:** `sm_risk`, `dictionary_step`

### C-9: Leptons selection rule (str. 72)
- **Target (145):** str. 72, section: Leptons selection rule, eq@L201
- **Source (461):** str. 175-177 (search: Lepton + selection)
- **Minimalni backfill:** Dictionary box za selekcijsko pravilo
- **Ključni pojmovi:** Leptons, selection, rule
- **Loc:** chapter_07_leptons.tex:201
- **Flags:** `dictionary_step`

### C-10: Three generations dictionary (str. 84)
- **Target (145):** str. 84, section: Three generations dictionary, eq@L244
- **Source (461):** str. 204-206 (search: generations + Z3)
- **Minimalni backfill:** Dictionary box: |Z₃| = 3 ↔ N_gen = 3
- **Ključni pojmovi:** generations, Z3, dictionary
- **Loc:** chapter_08_generations.tex:244
- **Flags:** `dictionary_step`

### C-11: PMNS interpretation (str. 93) ⚠️ CRITICAL
- **Target (145):** str. 93, subsection: PMNS interpretation, eq@L331
- **Source (461):** str. 228-230 (search: PMNS + neutrino)
- **Minimalni backfill:** Dictionary box + SM-risk box; razdvojiti EDC mixing od SM PMNS
- **Ključni pojmovi:** PMNS, neutrino, mixing
- **Loc:** chapter_09_neutrinos.tex:331
- **Flags:** `sm_risk`, `dictionary_step`

### C-12: V−A structural claim (str. 98) ⚠️ CRITICAL
- **Target (145):** str. 98, section: V−A structural claim, eq@L190
- **Source (461):** str. 243-245 (search: V-A + structure)
- **Minimalni backfill:** Dictionary box + SM-risk box; V−A iz EDC mehanizma vs SM fenomenologija
- **Ključni pojmovi:** V, structure, chirality
- **Loc:** chapter_10_va_structure.tex:190
- **Flags:** `sm_risk`, `dictionary_step`

### C-13: CKM hierarchy mechanism (str. 109) ⚠️ CRITICAL
- **Target (145):** str. 109, section: CKM hierarchy mechanism, eq@L265
- **Source (461):** str. 275-277 (search: CKM + hierarchy)
- **Minimalni backfill:** Dictionary box + SM-risk box; overlap integral → CKM elementi
- **Ključni pojmovi:** CKM, hierarchy, overlap
- **Loc:** chapter_11_ckm.tex:265
- **Flags:** `sm_risk`, `dictionary_step`

### C-14: g₅→G_F chain dictionary (str. 119)
- **Target (145):** str. 119, section: g₅→G_F chain dictionary, eq@L401
- **Source (461):** str. 305-307 (search: g_4 + g_5)
- **Minimalni backfill:** Dictionary box za g₄ = g₅/√ℓ → G_F lanac
- **Ključni pojmovi:** g_4, g_5, dilution
- **Loc:** chapter_12_gf_chain.tex:401
- **Flags:** `dictionary_step`

### C-15: Foundation parameters (kink/BPS) (str. 126)
- **Target (145):** str. 126, section: Foundation parameters (kink/BPS), eq@L287
- **Source (461):** str. 330-332 (search: kink + BPS)
- **Minimalni backfill:** Dictionary box za kink model → EDC membrane
- **Ključni pojmovi:** kink, BPS, Euler
- **Loc:** chapter_13_foundation_params.tex:287
- **Flags:** `dictionary_step`

### C-16: BVP physical role (str. 132)
- **Target (145):** str. 132, section: BVP physical role, eq@L210
- **Source (461):** str. 346-348 (search: Robin + boundary)
- **Minimalni backfill:** Dictionary box za Robin BC → fizički spektar
- **Ključni pojmovi:** Robin, boundary, spectrum
- **Loc:** chapter_14_bvp.tex:210
- **Flags:** `dictionary_step`

### C-17: M_W and G_F closure claim (str. 138) ⚠️ CRITICAL
- **Target (145):** str. 138, section: M_W and G_F closure claim, eq@L188
- **Source (461):** str. 360-362 (search: M_W + G_F)
- **Minimalni backfill:** Dictionary box + SM-risk box; δ → M_W zatvaranje
- **Ključni pojmovi:** M_W, G_F, δ
- **Loc:** chapter_15_mw_gf.tex:188
- **Flags:** `sm_risk`, `dictionary_step`

### C-18: Epistemic Summary table (str. 141)
- **Target (145):** str. 141, section: Epistemic Summary table, eq@L96
- **Source (461):** str. 372-374 (search: Epistemic + Summary)
- **Minimalni backfill:** Dictionary box za tablicu rezultata
- **Ključni pojmovi:** Epistemic, Summary, table
- **Loc:** chapter_16_epistemic_summary.tex:96
- **Flags:** `dictionary_step`

### C-19: Beyond (exploratory claims) (str. 144)
- **Target (145):** str. 144, section: Beyond (exploratory claims), eq@L170
- **Source (461):** str. 390-392 (search: exploratory + nuclear)
- **Minimalni backfill:** SM-risk box za nuklearne tvrdnje
- **Ključni pojmovi:** exploratory, nuclear, binding
- **Loc:** chapter_17_beyond.tex:170
- **Flags:** `sm_risk`

### C-20: Conclusions (str. 145)
- **Target (145):** str. 145, section: Conclusions, eq@L242
- **Source (461):** str. 402-404 (search: Conclusions + falsify)
- **Minimalni backfill:** Dictionary box za falsifikacijske kriterije
- **Ključni pojmovi:** Conclusions, falsify, hypothesis
- **Loc:** chapter_17_beyond.tex:242
- **Flags:** —

### C-21: Neutron vs muon selection (str. 27)
- **Target (145):** str. 27, section: Neutron vs muon selection, eq@L188
- **Source (461):** str. 62-64 (search: neutron + muon)
- **Minimalni backfill:** SM-risk box za neutron/muon razlikovanje
- **Ključni pojmovi:** neutron, muon, bulk
- **Loc:** chapter_01_weak_interface.tex:188
- **Flags:** `sm_risk`

### C-22: Cabibbo / calibration boundary (str. 116)
- **Target (145):** str. 116, section: Cabibbo / calibration boundary, eq@L119
- **Source (461):** str. 292-294 (search: Cabibbo)
- **Minimalni backfill:** Dictionary box za Cabibbo kalibraciju
- **Ključni pojmovi:** Cabibbo, calibrated, baseline
- **Loc:** chapter_11_ckm.tex:119
- **Flags:** `dictionary_step`

---

## Tip B — fali derivacija/koraci (N=56)

### B-1: Reader Contract (str. 6)
- **Target:** str. 6, section: Reader Contract, eq@L92
- **Source (461):** str. 7-9 (search: Reader + Contract)
- **Backfill:** Derivacija: 5–15 linija + 1–3 eq
- **Loc:** main.tex:92

### B-2: Barrier → WKB → dictionary (str. 10)
- **Target:** str. 10, section: Barrier → WKB → dictionary, eq@L210
- **Source (461):** str. 15-17 (search: WKB + barrier)
- **Backfill:** Derivacija + dictionary tag check
- **Loc:** chapter_01_weak_interface.tex:210
- **Flags:** `dictionary_step`

### B-3: Time mapping to seconds (str. 12)
- **Target:** str. 12, subsection: Time mapping to seconds, eq@L271
- **Source (461):** str. 20-22 (search: τ + seconds)
- **Backfill:** Derivacija + dictionary tag check
- **Loc:** chapter_01_weak_interface.tex:271
- **Flags:** `dictionary_step`

### B-4: WKB consistency condition (str. 14)
- **Target:** str. 14, eq@L330
- **Source (461):** str. 25-27 (search: WKB + consistency)
- **Loc:** chapter_01_weak_interface.tex:330

### B-5: G_F scaling step (str. 16)
- **Target:** str. 16, eq@L402
- **Source (461):** str. 31-33 (search: G_F + scaling)
- **Loc:** chapter_01_weak_interface.tex:402
- **Flags:** `dictionary_step`

### B-6: Vol(B3)=4π/3 integral (str. 21)
- **Target:** str. 21, eq@L360
- **Source (461):** str. 38-40 (search: Vol(B3) + integral)
- **Loc:** chapter_02_ontology.tex:360

### B-7: isoperimetric theorem → stability (str. 23)
- **Target:** str. 23, eq@L388
- **Source (461):** str. 41-43 (search: isoperimetric + theorem)
- **Loc:** chapter_02_ontology.tex:388

### B-8: "no topological unwind" argument (str. 24)
- **Target:** str. 24, eq@L395
- **Source (461):** str. 42-44 (search: topological + unwind)
- **Loc:** chapter_02_ontology.tex:395

### B-9: Bosonic modes spectrum derivation (str. 30)
- **Target:** str. 30, eq@L520
- **Source (461):** str. 79-81 (search: Bosonic + spectrum)
- **Loc:** chapter_02_ontology.tex:520
- **Flags:** `sm_risk`

### B-10 through B-56: [See prelet_scan_findings.json for complete list]

*(Remaining B-type gaps follow same format with tex location and source mapping)*

---

## Tip A — fali definicija/konvencija (N=12)

### A-1: Quick-ref σ, δ, V_B (str. 11)
- **Target:** str. 11, eq@L88
- **Source (461):** str. 17-19 (search: σ + δ)
- **Backfill:** 5–10 linija definicija + jedinice + ref na notation.tex
- **Loc:** chapter_01_weak_interface.tex:88

### A-2: κ defined at first mention (str. 92)
- **Target:** str. 92, eq@L120
- **Source (461):** str. 246-248 (search: κ + localization)
- **Loc:** chapter_09_neutrinos.tex:120

### A-3: κ_T disambiguation (str. 99)
- **Target:** str. 99, eq@L66
- **Source (461):** str. 248-250 (search: κ + coupling)
- **Loc:** chapter_10_va_structure.tex:66

### A-4: ℓ in Inputs box (str. 121)
- **Target:** str. 121, eq@L118
- **Source (461):** str. 304-306 (search: ℓ + compact)
- **Loc:** chapter_12_gf_chain.tex:118

### A-5: y (Yukawa) marked [Open] (str. 125)
- **Target:** str. 125, eq@L260
- **Source (461):** str. 335-337 (search: Yukawa)
- **Loc:** chapter_13_foundation_params.tex:260

### A-6: λ convention reminder (str. 133)
- **Target:** str. 133, eq@L90
- **Source (461):** str. 342-344 (search: λ + (mc/ℏ)²)
- **Loc:** chapter_14_bvp.tex:90

### A-7: R_ξ ↔ ℓ statement (str. 140)
- **Target:** str. 140, eq@L44
- **Source (461):** str. 309-311 (search: R_ξ + ℓ)
- **Loc:** notation.tex:44

### A-8: ξ domain vs δ vs ℓ reminder (str. 98)
- **Target:** str. 98, eq@L180
- **Source (461):** str. 340-342 (search: ξ + δ)
- **Loc:** notation.tex:180

### A-9: Acronyms/features list (str. 2)
- **Target:** str. 2, eq@None
- **Source (461):** str. 2-4 (search: Epistemic + tags)
- **Loc:** main.tex:40

### A-10, A-11, A-12: UNRESOLVED
- **Status:** Need tex→tex mapping from edc_book_2/src/

---

## Sažetak za backfill

| Tip | Broj | SM-risk | dictionary_step | UNRESOLVED |
|-----|------|---------|-----------------|------------|
| C   | 22   | 9       | 17              | 0          |
| B   | 56   | 7       | 12              | 1          |
| A   | 12   | 0       | 0               | 3          |
| **Ukupno** | **90** | **16** | **29** | **4** |

### Top 10 Critical (C + sm_risk + dictionary_step)

1. C-2: Electron as B3 Vortex (str. 18)
2. C-8: sin²θ_W identification (str. 63)
3. C-11: PMNS interpretation (str. 93)
4. C-12: V−A structural claim (str. 98)
5. C-13: CKM hierarchy mechanism (str. 109)
6. C-17: M_W and G_F closure claim (str. 138)
7. C-1: Version 2.0 features (str. 4)
8. C-5: Bosonic Modes (str. 33)
9. C-19: Beyond exploratory claims (str. 144)
10. C-21: Neutron vs muon selection (str. 27)

---

## Sljedeći koraci (TODO)

1. **Svaki Tip C s dictionary_step** → obavezni dictionary-box
2. **Svaki C/B s sm_risk** → SM-language guardrail ili preformulacija
3. **UNRESOLVED stavke** → zatvoriti tex→tex kada je dostupan edc_book_2/src/
4. **Top 10 Critical** → prioritet za prvi backfill pass

---

*Generirano: 2026-01-31 iz prelet_scan_findings.json*
