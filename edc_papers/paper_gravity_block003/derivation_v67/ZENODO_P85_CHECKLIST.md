# Zenodo Upload Checklist — BLOCK-004 v67 REAL CLOSED

## Version: P85
## Date: 2026-02-09
## Tag: `BLOCK004_V67_REAL_CLOSED`

---

## 1. Files to Upload (Required)

| File | Location | Description |
|------|----------|-------------|
| Release PDF | `release/EDC_BLOCK004_DERIVATION_V67_REAL_CLOSED.pdf` | Main document |
| Release notes | `RELEASE_P83_REAL_CLOSURE.md` | Release documentation |
| Manifest | `release/manifest.sha256` | SHA256 checksums (7 files) |
| Audit doc | `AUDIT_P82_REAL_FIREWALL.md` | Firewall certification |
| Verifier | `VERIFY_P84.sh` | 60-second verification script |

---

## 2. Files to Upload (Optional)

| File | Location | Description |
|------|----------|-------------|
| Activation gate | `ACTIVATION_GATE.md` | Gate status documentation |
| Import contract | `IMPORT_CONTRACT.md` | σ̃ import interface |
| Smoke policy | `SMOKE_TEST_POLICY.md` | REAL vs SMOKE criteria |

---

## 3. Quarantine Files (Selective Upload)

**Upload these:**

| File | Description |
|------|-------------|
| `quarantine/sigma_tilde_value.json` | REAL provenance σ̃ import |
| `quarantine/sigma_tilde_value.sha256` | SHA256 seal |
| `quarantine/PROVENANCE_LINK.md` | Import provenance chain |

**Do NOT upload:**
- Any other quarantine files
- Temporary or intermediate files
- Build artifacts

---

## 4. What NOT to Upload

| Item | Reason |
|------|--------|
| `main.tex` | Source code (optional for reproducibility) |
| `main.aux`, `main.log`, etc. | Build artifacts |
| `recompute.py` | Internal verification (optional) |
| Full `release/` directory | May contain old PDFs |
| Cosmology lane files | Separate repository concern |

---

## 5. Citation Information

### Tag and Commits

```
Tag:     BLOCK004_V67_REAL_CLOSED
Commits: a110a08 (P83b index), e7f2235 (P83a release), 15a45fe (P82 audit)
```

### Layer A Statement

```
Layer A unchanged. SoT hash: d8e9f0a1b2c34567
Numerics contained in Layer B / quarantine only.
```

### REAL Provenance

```
derivation_ref: EDC-COSMO-TSTAR-5D-ROUTEAB
git_commit:     e41a228b226aebb10e406c93d57eca6e601b11a4
sot_hash:       edc_cosmo_tstar_5d_e41a228
sigma_tilde:    100.0 ± 10.0 (dimensionless)
```

### Suggested Citation

```
EDC BLOCK-004 v67: σ̃ Import Contract + Closure Map (REAL CLOSED)
Tag: BLOCK004_V67_REAL_CLOSED
Repository: elastic-diffusive-cosmology
Date: 2026-02-09
Layer A SoT: d8e9f0a1b2c34567
```

---

## 6. Zenodo Metadata

| Field | Value |
|-------|-------|
| Title | EDC BLOCK-004 v67: Proton Decay Closure (REAL) |
| Authors | [Your name(s)] |
| Publication date | 2026-02-09 |
| Version | v67-REAL-CLOSED |
| Keywords | EDC, proton decay, σ̃, REAL closure, GUT |
| License | [Specify license] |
| Related identifiers | Tag `BLOCK004_V67_REAL_CLOSED` |

---

## 7. Verification Steps

### Before Upload

```bash
cd derivation_v67

# Run verifier script
./VERIFY_P84.sh
# Expected: VERIFICATION PASSED

# Run full recompute
python3 recompute.py
# Expected: ALL CHECKS PASSED (197+)
```

### After Upload

1. Download the Zenodo archive
2. Extract and navigate to `derivation_v67/`
3. Run `./VERIFY_P84.sh`
4. Confirm all hashes match

---

## 8. Checklist

- [ ] Release PDF uploaded
- [ ] RELEASE_P83_REAL_CLOSURE.md uploaded
- [ ] release/manifest.sha256 uploaded
- [ ] AUDIT_P82_REAL_FIREWALL.md uploaded
- [ ] VERIFY_P84.sh uploaded
- [ ] quarantine/sigma_tilde_value.json uploaded
- [ ] quarantine/sigma_tilde_value.sha256 uploaded
- [ ] quarantine/PROVENANCE_LINK.md uploaded
- [ ] Zenodo metadata filled
- [ ] DOI reserved/minted
- [ ] ./VERIFY_P84.sh passes locally
- [ ] Download and re-verify after publish

---

## 9. Notes

- The tag `BLOCK004_V67_REAL_CLOSED` marks the frozen release point
- Layer A content is hash-locked and unchanged from prior versions
- All numeric values are contained in Layer B / quarantine
- The verifier script `VERIFY_P84.sh` provides 60-second validation

---

**Ready for archival. Run `./VERIFY_P84.sh` before uploading.**
