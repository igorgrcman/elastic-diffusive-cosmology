# BVP Reports — Upute za korištenje

## Struktura direktorija

```
bvp_reports/
├── README.md                      ← Ova datoteka
├── ROBUSTNESS_ATLAS_REPORT.md     ← Glavni report template
├── run_manifest_template.yml      ← Template za run metadata
├── FIGURES/                       ← Generirane slike (drop zone)
│   └── [*.png, *.pdf]
└── TABLES/                        ← Generirane tablice (drop zone)
    └── [*.csv, *.tex]
```

## Workflow

### 1. Prije pokretanja numerike

1. Kopiraj `run_manifest_template.yml` u novi file s datumom:
   ```bash
   cp run_manifest_template.yml run_manifest_2026-01-24.yml
   ```

2. Popuni metadata (git commit, machine, python version, itd.)

### 2. Pokretanje solvera

```bash
# V0 benchmarks
python3 ../code/bvp_verification_suite.py --level V0 --output bvp_reports/

# V1 cross-method
python3 ../code/bvp_verification_suite.py --level V1 --output bvp_reports/

# Phase atlas
python3 ../code/bvp_phase_atlas.py --all-candidates --output bvp_reports/
```

### 3. Popunjavanje reporta

1. Otvori `ROBUSTNESS_ATLAS_REPORT.md`
2. Zamijeni sve `[Popuniti]` placeholdere s rezultatima
3. Označi PASS/FAIL checkboxe
4. Umetni figure/table reference

### 4. Kvalitativna provjera

Prije finalizacije, provjeri:

- [ ] Svi V0 benchmarks PASS?
- [ ] V1 cross-method agreement < 10⁻⁴?
- [ ] V2 stability checks PASS?
- [ ] N_bound = 3 postoji za barem jedan V(z)?
- [ ] Blob criterion zadovoljen (nije fine-tuning)?
- [ ] Gap margins > 5%?
- [ ] PDG nije korišten kao input (guardrails)?

## Naming Conventions

### Figures

```
FIGURES/
├── v0_infinite_well_convergence.png
├── v0_harmonic_convergence.png
├── v0_poschl_teller_convergence.png
├── v1_cross_method_comparison.png
├── v2_grid_convergence.png
├── phase_diagram_poschl_teller.png
├── phase_diagram_volcano.png
├── phase_diagram_box.png
├── phase_diagram_double_well.png
├── phase_diagram_exponential.png
├── mode_profiles.png
├── I4_convergence.png
└── robustness_blob_slice.png
```

### Tables

```
TABLES/
├── v0_benchmark_results.csv
├── v1_cross_method_results.csv
├── phase_table_poschl_teller.csv
├── phase_table_volcano.csv
├── phase_table_box.csv
├── phase_table_double_well.csv
├── phase_table_exponential.csv
├── eigenvalues_all.csv
├── phase_transitions.csv
└── gap_margins.csv
```

## No-Smuggling Checklist

Prije publishanja, eksplicitno potvrdi:

1. **G1:** PDG mase nisu korištene za fit → [ ]
2. **G2:** M_W, G_F, v nisu input → [ ]
3. **G3:** Parametri nisu tunirani za N=3 → [ ]
4. **G4:** Verification Ladder prošao → [ ]
5. **G5:** Threshold intrinsično definiran → [ ]

## Verzioniranje

- Report se verzionira s git commitom
- Svaki run ima svoj `run_manifest_*.yml`
- Finalni report uključuje git hash za reproducibilnost

---

*Template version: 1.0*
*Last updated: 2026-01-24*
