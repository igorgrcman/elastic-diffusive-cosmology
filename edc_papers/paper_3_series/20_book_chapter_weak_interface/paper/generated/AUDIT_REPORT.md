# EDC Numerical Forensic Audit Report

**Generated:** 2026-01-23T02:33:35.777809Z
**Git Hash:** c72256b

---

## Build Information

```bash
# Clean build command:
./scripts/clean_build.sh

# Full build with Part I:
BUILD_PART_I=true ./scripts/clean_build.sh
```

## Ledger Summary

Total entries: 175

### Entries by Epistemic Tag

| Tag | Count |
|-----|-------|
| [BL] | 12 |
| [BL→Dc] | 1 |
| [Dc] | 156 |
| [Dc]+[I] | 1 |
| [Dc]+[P] | 3 |
| [P] | 2 |

### Full Ledger Table

| Key | Value | Units | Tag | Source |
|-----|-------|-------|-----|--------|
| BASELINE_sigma | 5.67e+07 | N/m^2 | [BL] | baseline_constants |
| BASELINE_r_e | 2.818e-15 | m | [BL] | baseline_constants |
| BASELINE_R_xi | 2.16e-18 | m | [P] | baseline_constants |
| CONST_hbar | 1.055e-34 | J·s | [BL] | physical_constants |
| CONST_c | 299792458 | m/s | [BL] | physical_constants |
| CONST_e | 1.602e-19 | C | [BL] | physical_constants |
| CONST_alpha | 0.007297 | 1 | [BL] | physical_constants |
| CONST_m_e | 9.109e-31 | kg | [BL] | physical_constants |
| CONST_m_p | 1.673e-27 | kg | [BL] | physical_constants |
| CONST_G_F | 1.166e-05 | GeV^-2 | [BL] | physical_constants |
| CONST_M_W | 80.38 | GeV | [BL] | physical_constants |
| CONST_M_Z | 91.19 | GeV | [BL] | physical_constants |
| CONST_sin2_theta_W | 0.2312 | 1 | [BL] | physical_constants |
| GF_CHAIN_g2_sq | 0.373 | 1 | [Dc]+[P] | check_opr19_4pi_derivation.py |
| GF_CHAIN_x1_robin | 2.41 | 1 | [Dc] | solve_opr20_mediator_bvp.py |
| GF_CHAIN_x1_dirichlet | 3.142 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| GF_CHAIN_ell_over_Rxi | 8.886 | 1 | [Dc] | check_opr20_prefactor8_attemptE.py |
| GF_CHAIN_R_xi | 2.16e-18 | m | [P] | baseline_constants |
| MASS_phi_robin | 53.5 | GeV | [Dc]+[P] | check_opr20_alpha_2pi_prediction.py |
| MASS_phi_dirichlet | 70 | GeV | [Dc]+[P] | check_opr20_x1_bc_ledger.py |
| PMNS_sin2_theta23 | 0.564 | 1 | [Dc] | pmns_calculation |
| PMNS_sin2_theta13 | 0.025 | 1 | [BL→Dc] | pmns_calculation |
| CKM_delta | 60 | deg | [Dc]+[I] | check_z2_parity_sign_rule.py |
| check_gf_chain_status_v | 246 | GeV | [Dc] | check_gf_chain_status.py |
| check_gf_chain_status_alpha | 1 | /137 | [Dc] | check_gf_chain_status.py |
| check_g5_ell_dimensions_g^2 | 4 | *pi | [Dc] | check_g5_ell_dimensions.py |
| check_g5_ell_dimensions_g^2 | 4 | *pi | [Dc] | check_g5_ell_dimensions.py |
| check_g5_ell_dimensions_g_5^2 | 197.3 | ^2 | [Dc] | check_g5_ell_dimensions.py |
| check_g5_ell_dimensions_g^2 | 4 | *pi*sigma*r_e^3/hbar*c): | [Dc] | check_g5_ell_dimensions.py |
| check_dimensionless_fgeom_r_e^2 | 5.856 | MeV | [Dc] | check_dimensionless_fgeom.py |
| check_dimensionless_fgeom_r_e | 1 | fm | [Dc] | check_dimensionless_fgeom.py |
| check_dimensionless_fgeom_R_xi | 0.001 | fm | [Dc] | check_dimensionless_fgeom.py |
| check_dimensionless_fgeom_c | 197.3 | MeV*fm | [Dc] | check_dimensionless_fgeom.py |
| check_dimensionless_fgeom_g5^2 | 0.373 | [P] | [Dc] | check_dimensionless_fgeom.py |
| check_g1_coefficient_sensitivity_r_e² | 5.856 | MeV | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_r_e | 1 | fm | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_c | 197.3 | MeV·fm | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g₂² | 4 | πα/sin²θ_W | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_θ_W | 0.397 | 1 | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 4 | π | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 12 | × | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 8 | π/3 | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 2 | π | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 6 | × | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 4 | π/3 | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 4 | × | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 3 | × | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 8 | π | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 0.373 | (-6.0%) | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 0.3562 | (-10.3%) | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 0.323 | (-18.6%) | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 0.373 | (-6.0%) | [Dc] | check_g1_coefficient_sensitivity.py |
| check_g1_coefficient_sensitivity_g² | 0.373 | , | [Dc] | check_g1_coefficient_sensitivity.py |
| check_opr19_4pi_derivation_r_e² | 5.856 | MeV | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_r_e | 1 | fm | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_c | 197.3 | MeV·fm | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_dΩ | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g₂² | 0.4 | (comparison | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_v | 246 | GeV | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_r_e² | 5.856 | MeV | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_r_e | 1 | fm | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_c | 197.3 | MeV·fm | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_dφ | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_φ | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_π | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_π | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 0.373 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_dA | 1 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_r_e² | 1 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_r_e² | 12.57 | fm² | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_π | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 0.373 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_π | 12.57 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 0.373 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g₂² | 4 | πα/sin²θ_W | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_θ_W | 0.397 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 0.373 | 1 | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_C | 4 | π | [Dc] | check_opr19_4pi_derivation.py |
| check_opr19_4pi_derivation_g² | 0.373 | (6% | [Dc] | check_opr19_4pi_derivation.py |
| check_opr20_factor8_routes__eff | 2 | ℓ | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_factor8_routes_π | 4 | 1 | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_factor8_routes_π | 4 | 1 | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_factor8_routes_FACTOR | 8 | 1 | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_factor8_routes_m_φ | 99 | GeV | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_factor8_routes_φ | 99 | 1 | [Dc] | check_opr20_factor8_routes.py |
| check_opr20_overcounting_audit_π | 12.6 | 1 | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_norm | 2 | π | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_m_φ | 70 | GeV | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_φ | 70 | 1 | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_Israel | 4 | (double-counts | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_Z2 | 8 | (triple-counts | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_overcounting_audit_factor4 | 8 | (factor4 | [Dc] | check_opr20_overcounting_audit.py |
| check_opr20_prefactor8_attemptE_M_W | 80 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_G_F | 1.17 | × | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_v | 246 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_M_W | 80 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_R_ξ | 0.001 | fm | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_ξ | 0.001 | 1 | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_L | 2 | πR | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_M_W | 80 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_M_W | 80.4 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_κ | 0.11 | 1 | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_m_φ | 34.88 | GeV | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_prefactor8_attemptE_φ | 34.88 | 1 | [Dc] | check_opr20_prefactor8_attemptE.py |
| check_opr20_alpha_accounting_x₁ | 2.5 | , | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_x₁² | 2.56 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_α | 8 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_x₁ | 2.5 | , | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_x₁² | 3.84 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_α | 12 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_M_W | 80 | GeV | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_G_F | 1.17 | ×10⁻⁵ | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_v | 246 | GeV | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_α | 2 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_α | 2 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_f | 0 | from | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_αf | 0 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_f | 0 | from | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_accounting_αf | 0 | 1 | [Dc] | check_opr20_alpha_accounting.py |
| check_opr20_alpha_2pi_prediction_α | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_α | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_δ | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_M_W | 80.4 | GeV | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_R_ξ | 0.001 | fm | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_ξ | 0.001 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_R_ξ | 0.008886 | fm | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_ξ | 0.008886 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_α | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_π | 6.283 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_x₁ | 2.41 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_M_W | 80.4 | GeV | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_M_W | 0.6656 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_I₄ | 1.198 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_α | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_α | 2 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_π | 6.283 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_x₁ | 2.41 | │ | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_m_φ | 53.5 | GeV | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_alpha_2pi_prediction_φ | 53.5 | 1 | [Dc] | check_opr20_alpha_2pi_prediction.py |
| check_opr20_x1_bc_ledger_R_ξ | 8.886 | ×10⁻³ | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_ξ | 8.886 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_R_ξ | 1 | ×10⁻³ | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_ξ | 1 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_M_W | 80.4 | GeV | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_m_φ | 69.8 | GeV | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_φ | 69.8 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_m_φ | 34.9 | GeV | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_φ | 34.9 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_φ | 0 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_φ | 0 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_x₁ | 0 | ) | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_n | 1 | ,2,...). | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_n | 1 | ): | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_x₀ | 0 | (constant) | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_π | 3.142 | 1 | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_x₁ | 0 | (massless) | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_n | 1 | ) | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_M_W | 80 | GeV; | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_n | 0 | massless, | [Dc] | check_opr20_x1_bc_ledger.py |
| check_opr20_x1_bc_ledger_n | 1 | ): | [Dc] | check_opr20_x1_bc_ledger.py |
| check_z2_parity_sign_rule_δ | 60 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_δ | 120 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_δ | 60 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_δ | 60 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_δ | 60 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_δ | 60 | 1 | [Dc] | check_z2_parity_sign_rule.py |
| check_z2_parity_sign_rule_J | 2.9 | ×10⁻⁵ | [Dc] | check_z2_parity_sign_rule.py |
| check_lambda_provenance_λ | 0.225 | 1 | [Dc] | check_lambda_provenance.py |

---

## Script Results

- **check_gf_dimensions.py**: PASS
- **check_gf_chain_status.py**: PASS
- **check_g5_ell_dimensions.py**: PASS
- **check_dimensionless_fgeom.py**: PASS
- **check_g1_coefficient_sensitivity.py**: PASS
- **check_opr19_4pi_derivation.py**: PASS
- **check_opr20_factor8_routes.py**: PASS
- **check_opr20_overcounting_audit.py**: PASS
- **check_opr20_prefactor8_attemptE.py**: PASS
- **check_opr20_alpha_accounting.py**: PASS
- **check_opr20_alpha_2pi_prediction.py**: PASS
- **check_opr20_x1_bc_ledger.py**: PASS
- **check_opr20b_h2plus_delta_rxi_audit.py**: FAIL (code 1)
- **check_z2_parity_sign_rule.py**: PASS
- **check_lambda_provenance.py**: PASS

---

## Failures

### Script Errors
- **check_opr20b_h2plus_delta_rxi_audit.py**: Exit code 1

---

## Recommendations

1. **Replace hardcoded numbers** in LaTeX with `\input{generated/numbers.tex}` macros
2. **Run unit checker** to verify dimensional consistency
3. **Run circularity checker** to detect SM-smuggling
4. **Update epistemic tags** for any [Dc] claims that are actually [P] or [I]

---

*End of Audit Report*