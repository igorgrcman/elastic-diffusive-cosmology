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


def build_stub():
    """Build the sigma_tilde_value.json stub with TBD values."""

    stub = {
        "schema_version": "1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "sigma_tilde": {
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
            "epistemic_tags": ["placeholder", "awaiting_derivation"],
            "parent_hashes": {
                "v65": "c4e7f2a1b8d30965",
                "v67": "d8e9f0a1b2c34567"
            },
            "sot_hash": "TBD",
            "repo_commit": get_git_commit(),
            "notes": "Skeleton stub - no numeric values derived yet"
        },
        "firewall": {
            "layer": "A",
            "forbidden_gate_pass": False
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
    print(f"  repo_commit: {stub['provenance']['repo_commit'][:12]}...")

    return 0


if __name__ == "__main__":
    sys.exit(main())
