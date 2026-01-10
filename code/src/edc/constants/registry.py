from __future__ import annotations

from typing import Iterable, Optional, Set, Dict, List

from edc.epistemic import Constant, EpistemicStatus
from edc.constants.codata_baseline import BASELINE
from edc.constants.pdg_baseline import PDG_BASELINE
from edc.constants.edc_validated import VALIDATED
from edc.constants.proposed import PROPOSED


_DB: Dict[str, Constant] = {}
_DB.update(BASELINE)
_DB.update(PDG_BASELINE)
_DB.update(VALIDATED)
_DB.update(PROPOSED)


def list_constants() -> List[str]:
    """Return all known constant keys."""
    return sorted(_DB.keys())


def get_constant(name: str, *, allow: Optional[Iterable[str]] = None) -> Constant:
    """Fetch a constant by name with explicit epistemic permission.

    Parameters
    ----------
    name:
        Constant key (e.g., 'c', 'G', 'hbar', 'AU', 'EDC_MEMBRANE_TENSION').
    allow:
        Iterable of allowed status strings, e.g. {'BASELINE'} or {'PROPOSED'}.
        If omitted, this function raises (strict mode).

    Returns
    -------
    Constant
        A Constant record including value and epistemic status.

    Notes
    -----
    This guardrail exists to prevent accidental use of BASELINE constants
    inside code that is later described as an EDC prediction.
    """
    if name not in _DB:
        raise KeyError(f"Unknown constant: {name!r}. Known: {', '.join(list_constants()[:20])} ...")

    c = _DB[name]
    if allow is None:
        raise PermissionError(
            f"Missing allow=... when requesting {name!r} (status={c.status}). "
            "Call get_constant(name, allow={...}) explicitly."
        )

    allow_set: Set[str] = {str(a) for a in allow}
    if c.status.value not in allow_set:
        raise PermissionError(
            f"Constant {name!r} has status {c.status.value}, not in allowed set {sorted(allow_set)}."
        )
    return c
