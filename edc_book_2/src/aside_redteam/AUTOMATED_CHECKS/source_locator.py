#!/usr/bin/env python3
"""
source_locator.py — Red Team Forensic Tool
Locates all occurrences of key terms in the source tree.
Outputs CSV with file/line/context for forensic analysis.
"""

import subprocess
import csv
import os
import sys
from pathlib import Path

# Key terms for each pillar
PILLAR_TERMS = {
    "P1_proton": [
        r"Y-junction|Y junction|Yjunction",
        r"M5.*topolog|M5.*brane",
        r"proton.*5D|5D.*proton",
        r"Steiner",
        r"topolog.*proton|proton.*topolog",
        r"flux.*tube",
    ],
    "P2_Z6": [
        r"\\mathbb\{Z\}_6|Z_6|Z6",
        r"\\mathbb\{Z\}_2.*\\mathbb\{Z\}_3|Z_2.*Z_3|Z2.*Z3",
        r"hexagon.*lattice|lattice.*hexagon",
        r"Weinberg.*angle|sin.*theta_W",
        r"generation.*3|three.*generation",
        r"subgroup.*counting|counting.*subgroup",
    ],
    "P3_frozen": [
        r"frozen.*regime|regime.*frozen",
        r"\\sigma.*\\to.*\\infty|sigma.*infty",
        r"step.*function|Theta.*r.*a",
        r"projection.*operator|\\mathcal\{P\}",
        r"GL.*fail|Ginzburg.*Landau",
        r"boundary.*condition|BC.*sharp",
    ],
    "smuggling": [
        r"PDG|CODATA",
        r"M_Z|M_W|G_F",
        r"v.*=.*246|vev.*246",
        r"alpha.*M_Z|\\alpha\(M",
        r"baseline|\\tagBL",
        r"137\.03|0\.511|938|939",  # Known SM values
    ],
}

def run_ripgrep(pattern, src_dir, context_lines=3):
    """Run ripgrep and return results."""
    try:
        cmd = [
            "rg", "-n", "-i",
            f"-C{context_lines}",
            "--type", "tex",
            pattern,
            str(src_dir)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout
    except Exception as e:
        return f"ERROR: {e}"

def parse_rg_output(output, pattern, pillar):
    """Parse ripgrep output into structured records."""
    records = []
    if not output or output.startswith("ERROR"):
        return records

    current_file = None
    for line in output.split('\n'):
        if not line.strip():
            continue
        if ':' in line:
            parts = line.split(':', 2)
            if len(parts) >= 3:
                try:
                    filepath = parts[0]
                    lineno = int(parts[1].replace('-', ''))
                    content = parts[2][:200]  # Truncate
                    records.append({
                        'pillar': pillar,
                        'pattern': pattern[:50],
                        'file': filepath,
                        'line': lineno,
                        'context': content.strip()
                    })
                except ValueError:
                    continue
    return records

def main():
    src_dir = Path(__file__).parent.parent.parent
    output_dir = Path(__file__).parent.parent

    all_records = []

    print("=" * 60)
    print("RED TEAM SOURCE LOCATOR")
    print("=" * 60)

    for pillar, patterns in PILLAR_TERMS.items():
        print(f"\n[{pillar}] Scanning...")
        for pattern in patterns:
            output = run_ripgrep(pattern, src_dir)
            records = parse_rg_output(output, pattern, pillar)
            all_records.extend(records)
            print(f"  {pattern[:40]}: {len(records)} hits")

    # Write CSV
    csv_path = output_dir / "source_locator_results.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['pillar', 'pattern', 'file', 'line', 'context'])
        writer.writeheader()
        writer.writerows(all_records)

    print(f"\n[DONE] Total records: {len(all_records)}")
    print(f"[DONE] Output: {csv_path}")

    # Summary by pillar
    print("\n" + "=" * 60)
    print("SUMMARY BY PILLAR")
    print("=" * 60)
    for pillar in PILLAR_TERMS:
        count = sum(1 for r in all_records if r['pillar'] == pillar)
        print(f"  {pillar}: {count} occurrences")

if __name__ == "__main__":
    main()
