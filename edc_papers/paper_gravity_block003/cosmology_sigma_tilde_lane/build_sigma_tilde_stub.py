#!/usr/bin/env python3
"""
build_sigma_tilde_stub.py

Generates a schema-compliant sigma_tilde_value.json with status="TBD" and null values.
No external packages required.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone


def get_git_commit():
    """Get current git commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def get_git_branch():
    """Get current git branch name."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def build_stub():
    """Build the sigma_tilde_value.json stub with TBD values.

    For DERIVED mode (not generated here), value would be:
    {
        "sigma_tilde": {
            "value": {
                "central": <number > 0>,
                "plus": <number >= 0>,
                "minus": <number >= 0>
            },
            "uncertainty": { ... },
            "status": "DERIVED"
        },
        "provenance": {
            "method": "cosmology_derivation",
            "derivation_ref": "path/to/derivation.md",
            "generated_by": "derive_sigma_tilde.py",
            "generated_at": "<ISO8601>",
            "sot_hash": "<actual_hash>",  # NOT "TBD"
            ...
        }
    }
    """

    stub = {
        "schema_version": "1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "sigma_tilde": {
            # TBD mode: value is null (v67 expects object only when DERIVED)
            "value": None,
            "uncertainty": {
                "type": "interval",
                "lo": None,
                "hi": None,
                "units": "dimensionless"
            },
            "status": "TBD"
        },
        "t_star": {
            "definition_ref": "TSTAR_DEFINITION.md",
            "derivation_ref": "TSTAR_DERIVATION_5D.md",
            "value": None,
            "units": None,
            "status": "TBD"
        },
        "sigma_dimensional": {
            "value": None,
            "units": None,
            "status": "TBD"
        },
        "provenance": {
            "method": "stub_generation",
            # derivation_ref is null in TBD mode; must be populated when DERIVED
            "derivation_ref": None,
            "generated_by": "build_sigma_tilde_stub.py",
            "generated_at": None,  # Optional, populated when DERIVED
            "epistemic_tags": ["placeholder", "awaiting_derivation"],
            "parent_hashes": {
                "v65": "c4e7f2a1b8d30965",
                "v67": "d8e9f0a1b2c34567"
            },
            # sot_hash = "TBD" in template mode; must be actual hash when DERIVED
            "sot_hash": "TBD",
            "git_commit": get_git_commit(),
            "git_branch": get_git_branch(),
            "notes": "Skeleton stub - no numeric values derived yet",
            "import_source": None  # Only used for IMPORTED status
        },
        "firewall": {
            "layer": "A",
            "forbidden_gate_pass": False,
            "notes": "no external anchors; placeholders only"
        }
    }

    return stub


def main():
    """Generate and write the stub file."""
    stub = build_stub()

    output_path = "sigma_tilde_value.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stub, f, indent=2)
        f.write("\n")  # Trailing newline

    print(f"Generated: {output_path}")
    print(f"  schema_version: {stub['schema_version']}")
    print(f"  created_utc: {stub['created_utc']}")
    print(f"  sigma_tilde.status: {stub['sigma_tilde']['status']}")
    print(f"  t_star.derivation_ref: {stub['t_star']['derivation_ref']}")
    print(f"  git_commit: {stub['provenance']['git_commit'][:12]}...")
    print(f"  git_branch: {stub['provenance']['git_branch']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
