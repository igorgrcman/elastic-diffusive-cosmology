# Book 2 Baseline Build Record

Generated: 2026-01-24
Purpose: Anchor point for symbol table and context-aware audit

## Build Verification

| Metric | Value |
|--------|-------|
| PDF path | `edc_book_2/src/main.pdf` |
| Page count | 387 |
| SHA256 | `1827705110b355474ef9f57e5c9922efe5a17747ab9b3597c06c87b826a9b0e0` |
| Git commit | `7efd642fb466ef9d5cd876f952cedd30996e8701` |
| Branch | `book2-ch1-asset-inventory-v1` |
| Build command | `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex` |
| Build status | PASS |

## Canon Sources Verified

All canon PDFs verified against `EDC_Research_PRIVATE/canon/checksums.sha256`:

| Artifact | DOI | SHA256 (first 16) |
|----------|-----|-------------------|
| EDC_Book_v17.49 (Part I) | - | `035e97497c0086d9` |
| EDC_Paper2 | - | `7250b74cdec8f38b` |
| Framework_v2.0 | 10.5281/zenodo.18299085 | `34d235c318fd401b` |
| Paper3_NJSR_Journal | 10.5281/zenodo.18262721 | `aa2dba0fbde18386` |
| CompanionA_Effective_Lagrangian | 10.5281/zenodo.18292841 | `3204d7f36aa9339c` |
| CompanionB_WKB_Prefactor | 10.5281/zenodo.18299637 | `b7914331d5a9cb46` |
| CompanionC_5D_KK_Reduction | 10.5281/zenodo.18299751 | `105c4cede1a38933` |
| CompanionD_Selection_Rules | 10.5281/zenodo.18299855 | `75ddb9b512f61775` |
| CompanionE_Symmetry_Operations | 10.5281/zenodo.18300199 | `83a28a6dfeaeee09` |
| CompanionF_Proton_Junction_Model | 10.5281/zenodo.18302953 | `3bde2d69315329e8` |
| CompanionG_Neutron_Proton_Mass | 10.5281/zenodo.18303494 | `7fa70b29fd4b153a` |
| CompanionH_Weak_Interactions | 10.5281/zenodo.18307539 | `8bdf960877158b57` |

## Notes

This baseline is the anchor for the canonical symbol table audit.
Any changes to Book 2 during this audit must maintain build PASS status.
