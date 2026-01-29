#!/usr/bin/env python3
"""
book2_manifest.py — Generate Book2 include manifest and dependency graph

Recursively parses LaTeX files starting from entry point, following:
  \input{...}, \include{...}, \subfile{...}, \import{path}{file}

Outputs:
  - BOOK2_CHAPTER_LIST.md: High-level chapter structure
  - BOOK2_MANIFEST.md: Full include tree with depths
  - BOOK2_INCLUDE_GRAPH.json: Machine-readable dependency graph
  - BOOK2_INCLUDE_GRAPH.md: Mermaid visualization
  - BOOK2_ORPHANS_REPORT.md: Derivations/boxes not included

Author: Claude Code session 2026-01-29
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional

# === Configuration ===
REPO_ROOT = Path(__file__).parent.parent.parent  # edc_book_2/tools -> repo root
BOOK2_ROOT = REPO_ROOT / "edc_book_2"
SHARED_ROOT = REPO_ROOT / "edc_papers" / "_shared"
ENTRY_POINT = BOOK2_ROOT / "src" / "main.tex"
OUTPUT_DIR = BOOK2_ROOT / "docs"

# Regex patterns for include statements
INCLUDE_PATTERNS = [
    (r'\\input\{([^}]+)\}', 'input'),
    (r'\\include\{([^}]+)\}', 'include'),
    (r'\\subfile\{([^}]+)\}', 'subfile'),
    (r'\\import\{([^}]+)\}\{([^}]+)\}', 'import'),
]

# Known chapter patterns (for chapter list extraction)
# Book2 uses: 01_xxx, ch10_xxx, CH3_xxx, etc.
CHAPTER_PATTERNS = [
    r'^(\d{2})_',           # 01_how_we_got_here, 05_case_neutron
    r'^ch(\d+)_',           # ch10_electroweak_bridge, ch11_xxx
    r'^CH(\d+)_',           # CH3_electroweak_parameters, CH4_xxx
]


class IncludeNode:
    """Represents a node in the include tree."""
    def __init__(self, path: Path, include_type: str, depth: int):
        self.path = path
        self.include_type = include_type
        self.depth = depth
        self.children: List['IncludeNode'] = []
        self.exists = path.exists()
        self.line_count = self._count_lines() if self.exists else 0

    def _count_lines(self) -> int:
        try:
            return len(self.path.read_text(encoding='utf-8', errors='ignore').splitlines())
        except:
            return 0


def normalize_path(include_path: str, current_file: Path, include_type: str) -> Path:
    """
    Normalize an include path to absolute path.

    Rules:
    - Add .tex extension if missing
    - Resolve relative to current file's directory
    - Handle _shared/ references
    """
    # Remove any quotes
    include_path = include_path.strip('"\'')

    # Add .tex if no extension
    if not include_path.endswith('.tex'):
        include_path += '.tex'

    # Handle _shared/ paths (relative to edc_papers/)
    if include_path.startswith('_shared/'):
        return REPO_ROOT / "edc_papers" / include_path

    # Handle paths starting with ../
    if include_path.startswith('../'):
        return (current_file.parent / include_path).resolve()

    # Default: relative to current file's directory
    candidate = current_file.parent / include_path
    if candidate.exists():
        return candidate.resolve()

    # Try relative to src/ directory
    candidate = BOOK2_ROOT / "src" / include_path
    if candidate.exists():
        return candidate.resolve()

    # Return best guess
    return (current_file.parent / include_path).resolve()


def parse_includes(file_path: Path, visited: Set[Path], depth: int = 0) -> Optional[IncludeNode]:
    """
    Recursively parse a LaTeX file for includes.

    Returns IncludeNode tree, or None if file doesn't exist or was visited.
    """
    file_path = file_path.resolve()

    # Skip if already visited (prevent cycles)
    if file_path in visited:
        return None

    visited.add(file_path)

    node = IncludeNode(file_path, 'root' if depth == 0 else 'input', depth)

    if not file_path.exists():
        return node

    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return node

    # Remove comments (lines starting with %)
    lines = content.splitlines()
    active_lines = []
    for line in lines:
        # Find first % not preceded by \
        idx = 0
        while idx < len(line):
            if line[idx] == '%' and (idx == 0 or line[idx-1] != '\\'):
                line = line[:idx]
                break
            idx += 1
        active_lines.append(line)
    content = '\n'.join(active_lines)

    # Find all includes
    for pattern, include_type in INCLUDE_PATTERNS:
        for match in re.finditer(pattern, content):
            if include_type == 'import':
                # \import{path}{file} -> combine path + file
                import_path = match.group(1) + match.group(2)
            else:
                import_path = match.group(1)

            child_path = normalize_path(import_path, file_path, include_type)
            child_node = parse_includes(child_path, visited, depth + 1)
            if child_node:
                child_node.include_type = include_type
                node.children.append(child_node)

    return node


def extract_chapters(root: IncludeNode) -> List[Tuple[str, Path, int, int]]:
    """
    Extract chapter-level files from include tree.

    Returns list of (chapter_name, path, line_count, chapter_number).
    """
    chapters = []

    def get_chapter_num(filename: str) -> Optional[int]:
        """Extract chapter number from filename."""
        for pattern in CHAPTER_PATTERNS:
            match = re.match(pattern, filename, re.IGNORECASE)
            if match:
                return int(match.group(1))
        return None

    def walk(node: IncludeNode):
        filename = node.path.stem
        ch_num = get_chapter_num(filename)
        if ch_num is not None:
            chapters.append((filename, node.path, node.line_count, ch_num))
        for child in node.children:
            walk(child)

    walk(root)
    # Sort by chapter number
    chapters.sort(key=lambda x: x[3])
    return chapters


def flatten_tree(root: IncludeNode) -> List[IncludeNode]:
    """Flatten include tree to list in DFS order."""
    result = []

    def walk(node: IncludeNode):
        result.append(node)
        for child in node.children:
            walk(child)

    walk(root)
    return result


def find_orphans(root: IncludeNode) -> Dict[str, List[Path]]:
    """
    Find derivations and boxes that are NOT included in Book2.

    Returns dict with keys: 'derivations', 'boxes', 'lemmas'
    """
    # Collect all included paths
    included = set()
    for node in flatten_tree(root):
        included.add(node.path.resolve())

    orphans = {
        'derivations': [],
        'boxes': [],
        'lemmas': [],
    }

    # Check _shared directories
    for category in orphans.keys():
        category_dir = SHARED_ROOT / category
        if category_dir.exists():
            for tex_file in category_dir.glob('*.tex'):
                if tex_file.resolve() not in included:
                    orphans[category].append(tex_file)

    return orphans


def build_graph_json(root: IncludeNode) -> Dict:
    """Build JSON representation of include graph."""
    nodes = []
    edges = []
    node_ids = {}

    def get_id(path: Path) -> str:
        path_str = str(path)
        if path_str not in node_ids:
            node_ids[path_str] = f"n{len(node_ids)}"
        return node_ids[path_str]

    def walk(node: IncludeNode):
        node_id = get_id(node.path)
        rel_path = str(node.path.relative_to(REPO_ROOT)) if node.path.is_relative_to(REPO_ROOT) else str(node.path)

        nodes.append({
            'id': node_id,
            'path': rel_path,
            'exists': node.exists,
            'lines': node.line_count,
            'depth': node.depth,
        })

        for child in node.children:
            child_id = get_id(child.path)
            edges.append({
                'from': node_id,
                'to': child_id,
                'type': child.include_type,
            })
            walk(child)

    walk(root)

    return {
        'nodes': nodes,
        'edges': edges,
        'stats': {
            'total_files': len(nodes),
            'total_edges': len(edges),
            'max_depth': max(n['depth'] for n in nodes) if nodes else 0,
            'total_lines': sum(n['lines'] for n in nodes),
        }
    }


def generate_mermaid(root: IncludeNode, max_depth: int = 3) -> str:
    """Generate Mermaid diagram of include graph (limited depth for readability)."""
    lines = ["```mermaid", "graph TD"]
    seen = set()

    def short_name(path: Path) -> str:
        return path.stem[:30]

    def node_id(path: Path) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '_', path.stem)[:20]

    def walk(node: IncludeNode):
        if node.depth > max_depth:
            return

        nid = node_id(node.path)
        if nid in seen:
            return
        seen.add(nid)

        label = short_name(node.path)
        if not node.exists:
            lines.append(f'    {nid}["{label} (MISSING)"]')
        else:
            lines.append(f'    {nid}["{label}"]')

        for child in node.children:
            if child.depth <= max_depth:
                cid = node_id(child.path)
                lines.append(f'    {nid} --> {cid}')
                walk(child)

    walk(root)
    lines.append("```")

    return '\n'.join(lines)


def write_chapter_list(chapters: List[Tuple[str, Path, int, int]], output_path: Path):
    """Write BOOK2_CHAPTER_LIST.md."""
    lines = [
        "# Book 2 Chapter List",
        "",
        "**Generated:** " + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Chapters",
        "",
        "| Ch# | Title | Lines | Path |",
        "|-----|-------|-------|------|",
    ]

    for name, path, line_count, ch_num in chapters:
        rel_path = str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)
        # Extract chapter title from filename (remove prefix like 01_, ch10_, CH3_)
        title = re.sub(r'^(\d{2}|ch\d+|CH\d+)_', '', name, flags=re.IGNORECASE)
        title = title.replace('_', ' ').title()
        lines.append(f"| {ch_num} | {title} | {line_count} | `{rel_path}` |")

    lines.extend([
        "",
        f"**Total chapters:** {len(chapters)}",
        f"**Total chapter lines:** {sum(c[2] for c in chapters)}",
        "",
        "---",
        "*Auto-generated by book2_manifest.py*",
    ])

    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote: {output_path}")


def write_manifest(root: IncludeNode, output_path: Path):
    """Write BOOK2_MANIFEST.md with full include tree."""
    nodes = flatten_tree(root)

    lines = [
        "# Book 2 Include Manifest",
        "",
        "**Generated:** " + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Statistics",
        "",
        f"- **Total files:** {len(nodes)}",
        f"- **Total lines:** {sum(n.line_count for n in nodes)}",
        f"- **Max depth:** {max(n.depth for n in nodes)}",
        f"- **Missing files:** {sum(1 for n in nodes if not n.exists)}",
        "",
        "## Include Tree",
        "",
        "```",
    ]

    for node in nodes:
        indent = "  " * node.depth
        rel_path = str(node.path.relative_to(REPO_ROOT)) if node.path.is_relative_to(REPO_ROOT) else str(node.path)
        status = "" if node.exists else " [MISSING]"
        lines.append(f"{indent}{node.path.name} ({node.line_count} lines){status}")

    lines.extend([
        "```",
        "",
        "## Full Path Listing",
        "",
        "| Depth | Type | Lines | Path |",
        "|-------|------|-------|------|",
    ])

    for node in nodes:
        rel_path = str(node.path.relative_to(REPO_ROOT)) if node.path.is_relative_to(REPO_ROOT) else str(node.path)
        status = "MISSING" if not node.exists else node.include_type
        lines.append(f"| {node.depth} | {status} | {node.line_count} | `{rel_path}` |")

    lines.extend([
        "",
        "---",
        "*Auto-generated by book2_manifest.py*",
    ])

    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote: {output_path}")


def write_graph(graph_data: Dict, json_path: Path, md_path: Path, root: IncludeNode):
    """Write include graph as JSON and Mermaid markdown."""
    # JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=2)
    print(f"Wrote: {json_path}")

    # Mermaid
    lines = [
        "# Book 2 Include Graph",
        "",
        "**Generated:** " + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "## Visualization (depth ≤ 3)",
        "",
        generate_mermaid(root, max_depth=3),
        "",
        "## Statistics",
        "",
        f"- Nodes: {graph_data['stats']['total_files']}",
        f"- Edges: {graph_data['stats']['total_edges']}",
        f"- Max depth: {graph_data['stats']['max_depth']}",
        f"- Total lines: {graph_data['stats']['total_lines']}",
        "",
        "## JSON Data",
        "",
        f"Full graph data available in: `{json_path.name}`",
        "",
        "---",
        "*Auto-generated by book2_manifest.py*",
    ]

    md_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote: {md_path}")


def write_orphans_report(orphans: Dict[str, List[Path]], output_path: Path):
    """Write BOOK2_ORPHANS_REPORT.md."""
    total = sum(len(v) for v in orphans.values())

    lines = [
        "# Book 2 Orphans Report",
        "",
        "**Generated:** " + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M"),
        "",
        "Files in `edc_papers/_shared/` that are NOT included in Book 2.",
        "",
        f"## Summary: {total} orphan files",
        "",
    ]

    for category, files in orphans.items():
        lines.extend([
            f"### {category.title()} ({len(files)} orphans)",
            "",
        ])

        if files:
            for f in sorted(files):
                rel_path = str(f.relative_to(REPO_ROOT)) if f.is_relative_to(REPO_ROOT) else str(f)
                lines.append(f"- `{rel_path}`")
        else:
            lines.append("*All files included.*")

        lines.append("")

    lines.extend([
        "## Integration Candidates",
        "",
        "Orphan derivations that may need integration:",
        "",
    ])

    # Flag high-priority integration candidates
    priority_keywords = ['gf_', 'weak_', 'fermi', 'neutr', 'z6_', 'zn_']
    candidates = []
    for f in orphans.get('derivations', []):
        name = f.stem.lower()
        if any(kw in name for kw in priority_keywords):
            candidates.append(f)

    if candidates:
        for f in candidates:
            lines.append(f"- **HIGH PRIORITY:** `{f.stem}`")
    else:
        lines.append("*No high-priority candidates identified.*")

    lines.extend([
        "",
        "---",
        "*Auto-generated by book2_manifest.py*",
    ])

    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote: {output_path}")


def main():
    """Main entry point."""
    print(f"Book2 Manifest Generator")
    print(f"========================")
    print(f"Entry point: {ENTRY_POINT}")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Parse include tree
    print("Parsing include tree...")
    visited = set()
    root = parse_includes(ENTRY_POINT, visited)

    if not root:
        print("ERROR: Could not parse entry point")
        return 1

    # Extract chapters
    chapters = extract_chapters(root)
    print(f"Found {len(chapters)} chapters")

    # Build graph
    graph_data = build_graph_json(root)
    print(f"Graph: {graph_data['stats']['total_files']} nodes, {graph_data['stats']['total_edges']} edges")

    # Find orphans
    orphans = find_orphans(root)
    print(f"Orphans: {sum(len(v) for v in orphans.values())} files")

    # Write outputs
    print()
    print("Writing outputs...")

    write_chapter_list(chapters, OUTPUT_DIR / "BOOK2_CHAPTER_LIST.md")
    write_manifest(root, OUTPUT_DIR / "BOOK2_MANIFEST.md")
    write_graph(graph_data, OUTPUT_DIR / "BOOK2_INCLUDE_GRAPH.json", OUTPUT_DIR / "BOOK2_INCLUDE_GRAPH.md", root)
    write_orphans_report(orphans, OUTPUT_DIR / "BOOK2_ORPHANS_REPORT.md")

    print()
    print("Done!")
    return 0


if __name__ == "__main__":
    exit(main())
