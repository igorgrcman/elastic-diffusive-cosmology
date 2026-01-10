from __future__ import annotations

from edc.epistemic import Constant, EpistemicStatus

PROPOSED = {
    "EDC_MEMBRANE_TENSION": Constant(name="EDC_MEMBRANE_TENSION", value=1.0, status=EpistemicStatus.PROPOSED, units="arb", source="Internal default", note="Proposed model parameter; must be fitted or derived.", ref_book=None),
    "EDC_VISCOSITY": Constant(name="EDC_VISCOSITY", value=1.0, status=EpistemicStatus.PROPOSED, units="arb", source="Internal default", note="Proposed model parameter; must be fitted or derived.", ref_book=None),
    "EDC_NONLINEAR_TERM": Constant(name="EDC_NONLINEAR_TERM", value=0.0, status=EpistemicStatus.PROPOSED, units="arb", source="Internal default", note="Proposed correction term; if used, must be fitted or derived.", ref_book=None),
}
