# DATA GAPS (V7.4)

**Created**: 2026-01-31
**Purpose**: Document remaining BL gaps and future expansion candidates
**Status**: [Open]

---

## Excluded Nuclides (α-BR too low)

These nuclides were considered but excluded due to α-branching ratio below threshold.

| Nuclide | t₁/₂ | Qα (keV) | α-BR | Reason |
|---------|------|----------|------|--------|
| Fr-222 | 14.2 m | 5850 | 0.0006 | α-BR < 1% |
| Fr-223 | 21.8 m | 5430 | 0.00006 | α-BR < 1% |
| Ra-225 | 14.9 d | 5097 | 0.0001 | α-BR < 1% |
| Ra-227 | 42.2 m | 5042 | 0.0003 | α-BR < 1% |
| Pa-228 | 22 h | 6264 | 0.02 | α-BR < 5% |
| Pa-229 | 1.50 d | 5836 | 0.0048 | α-BR < 1% |
| Pa-230 | 17.4 d | 5439 | 0.0009 | α-BR < 1% |
| Po-207 | 5.80 h | 5216 | 0.00021 | α-BR < 1% |
| U-231 | 4.2 d | 5576 | 0.00004 | α-BR < 1% |
| Np-235 | 396.1 d | 5192 | 0.00003 | α-BR < 1% |
| Pu-237 | 45.64 d | 5748 | 0.000042 | α-BR < 1% |
| Pu-241 | 14.329 y | 5140 | 0.00002 | α-BR < 1% |
| Am-240 | 50.8 h | 5378 | 0.00019 | α-BR < 1% |
| Bk-248 | 23.7 h | 5793 | 0.00003 | α-BR < 1% |
| Bk-249 | 327 d | 5521 | 0.00001 | α-BR < 1% |
| Bi-210 | 5.012 d | 5036 | 0.000001 | α-BR < 1% |
| Bi-213 | 45.59 m | 5988 | 0.0214 | α-BR < 5% |
| Ac-227 | 21.772 y | 5042 | 0.0138 | α-BR < 5% |

**Total excluded**: 18 nuclides

---

## Missing Jπ Data

| Nuclide | Jπ(P) | Jπ(D) | Issue |
|---------|-------|-------|-------|
| Po-217 | (9/2+) | BL:NA | Daughter Jπ uncertain |
| Es-250 | (6+) | 2- | Parent Jπ tentative |
| Es-254 | (7-) | 2- | Parent Jπ tentative |

**Impact**: These nuclides are included but hindrance classification may be uncertain.

---

## Elements Not Included

| Element | Z | Reason |
|---------|---|--------|
| Pb | 82 | No ground-state α-decay |
| Md | 101 | Insufficient BL data in whitelist |
| No | 102 | Insufficient BL data in whitelist |
| Lr | 103 | Insufficient BL data in whitelist |
| Rf+ | 104+ | Beyond whitelist coverage |

---

## Potential Future Additions

### Mendelevium (Z=101) Candidates

| Nuclide | t₁/₂ | Qα (keV) | Status |
|---------|------|----------|--------|
| Md-255 | 27 m | 7910 | Needs BL verification |
| Md-256 | 78.1 m | 7742 | Needs BL verification |
| Md-257 | 5.52 h | 7558 | Needs BL verification |
| Md-258 | 51.5 d | 7271 | Needs BL verification |

**Issue**: Jπ assignments uncertain in current ENSDF evaluations.

### Nobelium (Z=102) Candidates

| Nuclide | t₁/₂ | Qα (keV) | Status |
|---------|------|----------|--------|
| No-255 | 3.1 m | 8424 | Needs BL verification |
| No-256 | 2.91 s | 8581 | Needs BL verification |
| No-257 | 25 s | 8477 | Needs BL verification |
| No-259 | 58 m | 7851 | Needs BL verification |

**Issue**: Half-life and Qα measurements have large uncertainties.

---

## Chain Intermediate Nuclides

These nuclides are in the canonical decay chains but not included:

### U-238 Chain

| Nuclide | Role | α-BR | Issue |
|---------|------|------|-------|
| Th-234 | β-emitter | 0 | No α |
| Pa-234m | β-emitter | 0 | No α |
| Bi-214 | Branchpoint | 0.021% | Below threshold |
| Tl-210 | β-emitter | 0 | No α |

### Th-232 Chain

| Nuclide | Role | α-BR | Issue |
|---------|------|------|-------|
| Ra-228 | β-emitter | 0 | No α |
| Ac-228 | β-emitter | 0 | No α |
| Tl-208 | β-emitter | 0 | No α |

### U-235 Chain

| Nuclide | Role | α-BR | Issue |
|---------|------|------|-------|
| Th-231 | β-emitter | 0 | No α |
| Ac-227 | Mixed | 1.38% | Below threshold |
| Tl-207 | β-emitter | 0 | No α |

---

## Relaxation Options (Not Recommended)

If future expansion requires more nuclides, these options could be considered:

| Option | Current | Relaxed | Risk |
|--------|---------|---------|------|
| α-BR threshold | 5% | 1% | Higher t₁/₂ uncertainty |
| Jπ requirement | Firm | (tentative) | Misclassification |
| t₁/₂ uncertainty | ≤10% | ≤20% | G-N fit degradation |

**Recommendation**: Do not relax criteria without clear justification.

---

## Future Work Priorities

### Priority 1: Verify Md/No data
If ENSDF updates provide firm Jπ assignments for Md-255 to Md-258 or No-255 to No-259, these would be valuable additions for extending Z coverage.

### Priority 2: Isomer decays
Isomeric α-decays (e.g., ²¹¹ᵐPo) could provide additional data points, but require careful handling of excitation energies.

### Priority 3: Neutron-deficient nuclides
Po-200 to Po-205, At-200 to At-206 may have measureable α-branches but data quality varies.

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| Nuclides included | 102 | ✓ |
| Excluded (α-BR low) | 18 | Documented |
| Missing Jπ(D) | 3 | Minor |
| Elements missing | 5 | Physics limitation |
| Future candidates | ~10 | Pending BL |

**Conclusion**: The α102 dataset is comprehensive for the current BL whitelist. Further expansion would require either relaxed criteria or updated source evaluations.

