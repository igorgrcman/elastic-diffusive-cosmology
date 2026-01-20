# Neutron Lifetime from 5D Membrane Cosmology

**Paper 3 (NJSR Journal Format)**

DOI: [10.5281/zenodo.18262721](https://doi.org/10.5281/zenodo.18262721)

---

## Description

Main research paper deriving the neutron lifetime from 5D membrane cosmology. Uses WKB tunneling through a barrier in the collective coordinate connecting neutron and proton brane configurations.

Key results:
- tau_n derived within 1% of experimental value (878.4 s)
- No Standard Model G_F as input
- Single calibrated parameter (barrier height V_B)

---

## Build

```bash
cd paper/
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

---

## Dependencies

- `body_shared/main_body.tex` — shared content file

---

## Related Documents

- Framework v2.0 (DOI: 10.5281/zenodo.18299085)
- Companions A-H (supplementary derivations)

---

## Author

Igor Grcman
