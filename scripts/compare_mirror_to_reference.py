#!/usr/bin/env python3
"""Compare mirror/ coverage against the reference/ canon.

Prints three sets:
  - Covered    = mirror slugs ∩ reference slugs
                 (topics in the canon you have a note on)
  - Mirror-only = mirror slugs \\ reference slugs
                  (idiosyncratic notes — personal assets, state-specific,
                  hobby projects — that don't map to canonical leaves)
  - Reference-only = reference slugs \\ mirror slugs
                     (canonical leaves with no mirror coverage yet —
                      primary sampling targets for future quiz sessions)

Usage:
    scripts/compare_mirror_to_reference.py [--json]

With --json: emits a machine-readable summary to stdout.
Without:     emits a human-readable report.

Run from the repo root. Requires PyYAML.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "PyYAML is required. Install with `pip3 install --user pyyaml`.\n"
    )
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
MIRROR_NOTES = REPO_ROOT / "mirror" / "notes"
REFERENCE_TREE = REPO_ROOT / "reference" / "tree"


def collect_mirror_slugs() -> set[str]:
    """Every .md file in mirror/notes/ except the template and the meta note.

    Uses filename as slug, since that's the convention.
    """
    exclude = {"_template", "about-this-mirror"}
    slugs = set()
    for md in MIRROR_NOTES.glob("*.md"):
        slug = md.stem
        if slug in exclude:
            continue
        slugs.add(slug)
    return slugs


def collect_reference_slugs() -> set[str]:
    """Every leaf slug in reference/tree/**/*.yaml.

    The schema uses `- slug: <name>` entries at various depths. We parse
    the YAML and walk for dict nodes containing a `slug` key — this catches
    both top-level area slugs and the leaf-level slugs under them.
    """
    slugs = set()
    for yml in REFERENCE_TREE.rglob("*.yaml"):
        try:
            doc = yaml.safe_load(yml.read_text())
        except yaml.YAMLError:
            continue
        if doc is None:
            continue
        _walk_for_slugs(doc, slugs)
    return slugs


def _walk_for_slugs(node, acc: set[str]) -> None:
    """Recursively collect every value of a key named 'slug'."""
    if isinstance(node, dict):
        s = node.get("slug")
        if isinstance(s, str):
            acc.add(s)
        for v in node.values():
            _walk_for_slugs(v, acc)
    elif isinstance(node, list):
        for v in node:
            _walk_for_slugs(v, acc)


def render_human(mirror: set[str], reference: set[str]) -> str:
    covered = sorted(mirror & reference)
    mirror_only = sorted(mirror - reference)
    reference_only = sorted(reference - mirror)

    lines = []
    lines.append(f"Mirror slugs: {len(mirror)}")
    lines.append(f"Reference slugs: {len(reference)}")
    lines.append("")
    lines.append(f"Covered (mirror ∩ reference): {len(covered)}")
    for s in covered:
        lines.append(f"  {s}")
    lines.append("")
    lines.append(f"Mirror-only (idiosyncratic / outside canon): {len(mirror_only)}")
    for s in mirror_only:
        lines.append(f"  {s}")
    lines.append("")
    lines.append(
        f"Reference-only (canonical gaps — quiz-sampling targets): "
        f"{len(reference_only)}"
    )
    # Don't dump the full 300+ list by default; show first 30 and a total.
    for s in reference_only[:30]:
        lines.append(f"  {s}")
    if len(reference_only) > 30:
        lines.append(f"  ... and {len(reference_only) - 30} more")
    return "\n".join(lines)


def render_json(mirror: set[str], reference: set[str]) -> str:
    return json.dumps(
        {
            "mirror_count": len(mirror),
            "reference_count": len(reference),
            "covered": sorted(mirror & reference),
            "mirror_only": sorted(mirror - reference),
            "reference_only": sorted(reference - mirror),
        },
        indent=2,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit a machine-readable JSON report instead of the human-readable one.",
    )
    args = parser.parse_args()

    mirror = collect_mirror_slugs()
    reference = collect_reference_slugs()

    if args.json:
        print(render_json(mirror, reference))
    else:
        print(render_human(mirror, reference))
    return 0


if __name__ == "__main__":
    sys.exit(main())
