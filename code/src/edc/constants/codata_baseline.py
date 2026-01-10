from __future__ import annotations

from edc.epistemic import Constant, EpistemicStatus

BASELINE = {
    "alpha": Constant(name="alpha", value=7.2973525693e-3, status=EpistemicStatus.BASELINE,
                     source="PDG 2020 Physical constants (alpha; 1/137.035999084)",
                     note="Baseline fine-structure constant at Q^2=0 (dimensionless).", ref_book=None),

    "c": Constant(name="c", value=299792458.0, status=EpistemicStatus.BASELINE, units="m/s", source="CODATA (exact)", note="Baseline reference constant.", ref_book=None),
    "G": Constant(name="G", value=6.6743e-11, status=EpistemicStatus.BASELINE, units="m^3 kg^-1 s^-2", source="CODATA (G)", note="Baseline reference constant; do not treat as EDC-derived unless derived in-book.", ref_book=None),
    "hbar": Constant(name="hbar", value=1.054571817e-34, status=EpistemicStatus.BASELINE, units="J s", source="CODATA (ħ)", note="Baseline reference constant.", ref_book=None),
    "k_B": Constant(name="k_B", value=1.380649e-23, status=EpistemicStatus.BASELINE, units="J/K", source="CODATA (exact)", note="Baseline reference constant.", ref_book=None),
    "AU": Constant(name="AU", value=149597870700.0, status=EpistemicStatus.BASELINE, units="m", source="IAU 2012 (exact)", note="Baseline reference constant.", ref_book=None),
    "M_sun": Constant(name="M_sun", value=1.98847e+30, status=EpistemicStatus.BASELINE, units="kg", source="IAU nominal / common", note="Baseline reference mass (demo).", ref_book=None),
    "R_sun": Constant(name="R_sun", value=6.957e8, status=EpistemicStatus.BASELINE, units="m", source="IAU nominal solar radius", note="Baseline reference radius (used for solar-limb light deflection benchmark).", ref_book=None),
}
