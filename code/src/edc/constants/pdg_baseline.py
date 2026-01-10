from __future__ import annotations

from edc.epistemic import Constant, EpistemicStatus

# Baseline values sourced from PDG Physical Constants (2020 review; Revised 2019).
# Use these strictly as reference numbers for comparison/validation, not as EDC-derived results.

PDG_BASELINE = {
    # Mass ratio mp/me is listed directly in PDG constants table.
    "mp_over_me": Constant(
        name="mp_over_me",
        value=1836.15267343,
        status=EpistemicStatus.BASELINE,
        source="PDG 2020 Physical constants (mp/me)",
        note="Proton-to-electron mass ratio (dimensionless).",
        ref_book=None,
    ),
    # Electroweak: MS-bar definition at the Z mass (PDG table entry).
    "sin2_thetaW_hat_mZ_MSbar": Constant(
        name="sin2_thetaW_hat_mZ_MSbar",
        value=0.23121,
        status=EpistemicStatus.BASELINE,
        source="PDG 2020 Physical constants: sin^2(theta_hat)(MZ) (MS-bar)",
        note="Weak mixing angle in the MS-bar scheme at mu=MZ.",
        ref_book=None,
    ),
    # Electroweak: PDG footnote for effective angle (Z-pole effective leptonic angle).
    "sin2_thetaW_eff": Constant(
        name="sin2_thetaW_eff",
        value=0.23153,
        status=EpistemicStatus.BASELINE,
        source="PDG 2020 Physical constants footnote for effective angle",
        note="Effective weak mixing angle (Z-pole, definition-dependent).",
        ref_book=None,
    ),
    # W and Z masses (PDG table entries) used for on-shell definition cross-check.
    "mW_GeV": Constant(
        name="mW_GeV",
        value=80.379,
        status=EpistemicStatus.BASELINE,
        source="PDG 2020 Physical constants: mW",
        note="W boson mass in GeV (pole mass in PDG table).",
        ref_book=None,
    ),
    "mZ_GeV": Constant(
        name="mZ_GeV",
        value=91.1876,
        status=EpistemicStatus.BASELINE,
        source="PDG 2020 Physical constants: mZ",
        note="Z boson mass in GeV.",
        ref_book=None,
    ),
    # NIST 'weak mixing angle' value (often aligned with on-shell definition).
    "sin2_thetaW_NIST": Constant(
        name="sin2_thetaW_NIST",
        value=0.22305,
        status=EpistemicStatus.BASELINE,
        source="NIST Fundamental Physical Constants: sin^2(theta_W)",
        note="NIST weak mixing angle value (definition-dependent; often aligned with on-shell).",
        ref_book=None,
    ),
}
