# SOURCES AND VERSIONS (V7.1)

**Created**: 2026-01-31
**Inherited from**: V7 (audit/radioactivity_v7_bl/00_SOURCES_AND_VERSIONS.md)

---

## BL Source Whitelist

| ID | Source | Authority | URL | Status |
|----|--------|-----------|-----|--------|
| S1 | NNDC/ENSDF | Primary | nndc.bnl.gov/ensdf | Active |
| S2 | NuDat 3.0 | Derived from ENSDF | nndc.bnl.gov/nudat3 | Active |
| S3 | NUBASE2020 | Masses, t₁/₂ | DOI:10.1088/1674-1137/abddae | Active |
| S4 | AME2020 | Atomic masses, Q-values | DOI:10.1088/1674-1137/abddaf | Active |
| S5 | IAEA LiveChart | Cross-check | www-nds.iaea.org/livechart | Active |

---

## Blacklist (Not Allowed)

- Wikipedia
- Blogs / forums
- Undocumented "typical" values
- Random PDFs without DOI

---

## Citation Format

Every BL value must include:
```
[BL:S#] (locator: nuclide entry / page / table)
```

Example:
```
Qα(²¹⁰Po) = 5407.45 keV [BL:S2] (locator: NuDat3 Po-210 adopted levels)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V7.0 | 2026-01-31 | Initial whitelist |
| V7.1 | 2026-01-31 | Inherited; no changes |

