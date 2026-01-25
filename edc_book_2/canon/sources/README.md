# Canon Sources

This directory references the canonical EDC source documents.

## Location

Canon PDFs are stored in the EDC_Research_PRIVATE repository at:
```
/Users/igor/ClaudeAI/EDC_Project/EDC_Research_PRIVATE/canon/sources/
```

## Structure

```
canon/sources/
├── book_part1/
│   └── EDC_Book_v17.49.pdf
├── paper2/
│   └── EDC_Paper2.pdf
└── paper3_bundle/
    ├── 00_Framework_v2_0__DOI_10.5281_zenodo.18299085.pdf
    ├── 01_Paper3_NJSR_Journal__DOI_10.5281_zenodo.18262721.pdf
    ├── 02_CompanionA_Effective_Lagrangian__DOI_10.5281_zenodo.18292841.pdf
    ├── 03_CompanionB_WKB_Prefactor__DOI_10.5281_zenodo.18299637.pdf
    ├── 04_CompanionC_5D_KK_Reduction__DOI_10.5281_zenodo.18299751.pdf
    ├── 05_CompanionD_Selection_Rules__DOI_10.5281_zenodo.18299855.pdf
    ├── 06_CompanionE_Symmetry_Operations__DOI_10.5281_zenodo.18300199.pdf
    ├── 07_CompanionF_Proton_Junction_Model__DOI_10.5281_zenodo.18302953.pdf
    ├── 08_CompanionG_Neutron_Proton_Mass__DOI_10.5281_zenodo.18303494.pdf
    └── 09_CompanionH_Weak_Interactions__DOI_10.5281_zenodo.18307539.pdf
```

## Checksums (SHA-256)

See `audit/notation/GLOBAL_SYMBOL_TABLE_RUN_MANIFEST.yml` for verified checksums.

## Usage

When running symbol extraction tools:
```bash
python3 tools/symbol_extract_canon.py \
  --sources /path/to/EDC_Research_PRIVATE/canon/sources \
  --output audit/notation/canon_symbol_dictionary.json
```

## Authority

- **CANON-PRIMARY**: Framework v2.0 (DOI: 10.5281/zenodo.18299085)
- **CANON**: All other published artifacts with DOIs
- **WORKING**: Book 2 content under development

---

*Last updated: 2026-01-24*
