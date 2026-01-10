from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class EpistemicStatus(str, Enum):
    """Canonical epistemic labels used across the EDC codebase."""

    DERIVED = "DERIVED"
    IDENTIFIED = "IDENTIFIED"
    CALIBRATED = "CALIBRATED"
    PROPOSED = "PROPOSED"
    BASELINE = "BASELINE"  # Standard-theory / external reference constants


@dataclass(frozen=True)
class Constant:
    name: str
    value: float
    status: EpistemicStatus
    units: str = ""
    source: str = ""
    note: str = ""
    ref_book: Optional[str] = None
