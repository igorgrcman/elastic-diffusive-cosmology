# SOURCES AND VERSIONS (V7.2)

**Created**: 2026-01-31
**Inherited from**: V7.1, V7

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

## Blacklist (NOT Allowed)

- Wikipedia
- Blogs / forums / Stack Exchange
- Undocumented "typical" values
- Random PDFs without DOI
- Textbook approximations without primary source

---

## Citation Format

Every BL value must include:
```
[BL:S#] (locator: nuclide + field)
```

Example:
```
Qα(²¹⁰Po) = 5407.45 keV [BL:S2] (locator: NuDat3 Po-210 adopted levels)
Jπ(²⁰⁸Pb) = 0⁺ [BL:S1] (locator: ENSDF A=208)
```

---

## V7.2 Specific Additions

### Daughter Jπ Sources

For hindrance classification, daughter Jπ values were fetched from:

| Daughter | Jπ | Source |
|----------|-----|--------|
| ²⁰⁵Pb | 5/2⁻ | [BL:S1] ENSDF A=205 |
| ²⁰⁶Pb | 0⁺ | [BL:S1] ENSDF A=206 |
| ²⁰⁷Pb | 1/2⁻ | [BL:S1] ENSDF A=207 |
| ²⁰⁸Pb | 0⁺ | [BL:S1] ENSDF A=208 |
| ²⁰⁷Bi | 9/2⁻ | [BL:S2] NuDat3 Bi-207 |
| ²¹³Bi | 9/2⁻ | [BL:S1] ENSDF A=213 |
| ²¹⁵At | 9/2⁻ | [BL:S1] ENSDF A=215 |
| ²¹⁷At | 9/2⁻ | [BL:S1] ENSDF A=217 |
| ²¹⁹Rn | 5/2⁺ | [BL:S2] NuDat3 Rn-219 |
| ²²²Rn | 0⁺ | [BL:S2] NuDat3 Rn-222 |
| ²²⁶Ra | 0⁺ | [BL:S2] NuDat3 Ra-226 |
| All even-even | 0⁺ | Standard nuclear physics |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| V7.0 | 2026-01-31 | Initial whitelist |
| V7.1 | 2026-01-31 | Inherited |
| V7.2 | 2026-01-31 | Added daughter Jπ sources |

