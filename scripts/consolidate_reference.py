#!/usr/bin/env python3
"""
Consolidate the entire reference/ tree into a single file for external audit.

Walks reference/tree/**/*.yaml, parses each, and emits either:
  - Markdown (default) — human-readable, with TOC.
  - JSON (--format json) — machine-readable, preserves full schema.

Usage:
    python3 scripts/consolidate_reference.py                    # writes reference/_snapshot.md
    python3 scripts/consolidate_reference.py --format json      # writes reference/_snapshot.json
    python3 scripts/consolidate_reference.py --output -         # stdout
    python3 scripts/consolidate_reference.py --output FILE      # custom path

Dependencies:
    PyYAML  (pip install pyyaml)

Run from the repo root.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
TREE_DIR = REPO_ROOT / "reference" / "tree"
DOMAINS_FILE = REPO_ROOT / "reference" / "domains.yaml"
SOURCES_FILE = REPO_ROOT / "reference" / "sources.yaml"


def _require_yaml():
    try:
        import yaml  # noqa: F401
    except ImportError:
        sys.stderr.write(
            "Error: PyYAML is required.\n"
            "Install with:  pip install pyyaml\n"
        )
        sys.exit(1)
    import yaml
    return yaml


def load_yaml(path: pathlib.Path):
    yaml = _require_yaml()
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_areas() -> list[dict]:
    """Walk TREE_DIR for *.yaml files, return a list of area dicts sorted by path."""
    areas = []
    for yaml_path in sorted(TREE_DIR.rglob("*.yaml")):
        try:
            data = load_yaml(yaml_path)
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write(f"warn: {yaml_path}: failed to parse ({exc})\n")
            continue
        if not isinstance(data, dict) or "leaves" not in data:
            sys.stderr.write(f"warn: {yaml_path}: no 'leaves' key, skipping\n")
            continue
        rel = yaml_path.relative_to(REPO_ROOT).as_posix()
        area_meta = data.get("area") or {}
        leaves = data.get("leaves") or []
        areas.append({
            "file": rel,
            "part": area_meta.get("parent") or yaml_path.parts[-2],
            "area_slug": area_meta.get("slug") or yaml_path.stem,
            "area_title": area_meta.get("title") or yaml_path.stem,
            "source": area_meta.get("source"),
            "leaves": leaves,
        })
    return areas


def top_part(part_id: str) -> str:
    """First path segment — '07-technology/computing' → '07-technology'."""
    return part_id.split("/", 1)[0]


def build_summary(domains: dict | None, areas: list[dict]) -> dict:
    total_leaves = sum(len(a["leaves"]) for a in areas)
    by_part: dict[str, int] = {}
    for a in areas:
        by_part[a["part"]] = by_part.get(a["part"], 0) + len(a["leaves"])
    top_parts = {top_part(a["part"]) for a in areas}
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "repo_root": str(REPO_ROOT.name),
        "total_parts_defined": len((domains or {}).get("parts", [])),
        "total_parts_populated": len(top_parts),
        "total_areas": len(areas),
        "total_leaves": total_leaves,
        "leaves_by_part": dict(sorted(by_part.items())),
    }


def emit_markdown(out, domains: dict | None, sources: dict | None, areas: list[dict]) -> None:
    summary = build_summary(domains, areas)
    parts_by_id: dict[str, dict] = {p["slug"]: p for p in (domains or {}).get("parts", [])}

    w = out.write

    # --- Header ---
    w("# Reference tree snapshot\n\n")
    w(f"*Generated {summary['generated_at']}*  \n")
    w(f"*{summary['total_leaves']} leaves across "
      f"{summary['total_areas']} areas in {summary['total_parts_populated']}"
      f"/{summary['total_parts_defined']} Parts*\n\n")

    w("## Summary\n\n")
    w("| Part | Leaves |\n|------|-------:|\n")
    for part_id, n in summary["leaves_by_part"].items():
        title = parts_by_id.get(part_id, {}).get("title", part_id)
        w(f"| {title} | {n} |\n")
    w(f"| **Total** | **{summary['total_leaves']}** |\n\n")

    # --- Skeleton source ---
    if sources:
        skel = sources.get("skeleton", {})
        if skel:
            w("## Skeleton source\n\n")
            w(f"**{skel.get('title', '')}**  \n")
            if skel.get("editor"):
                w(f"Editor: {skel['editor']}  \n")
            if skel.get("publisher"):
                w(f"Publisher: {skel['publisher']}  \n")
            if skel.get("year"):
                w(f"Year: {skel['year']}  \n")
            if skel.get("url"):
                w(f"URL: {skel['url']}  \n")
            w("\n")

    # --- TOC ---
    w("## Contents\n\n")
    by_part: dict[str, list[dict]] = {}
    for a in areas:
        by_part.setdefault(a["part"], []).append(a)
    for part_id in sorted(by_part.keys()):
        title = parts_by_id.get(part_id, {}).get("title", part_id)
        slug = part_id.replace("/", "-")
        w(f"- **{title}**\n")
        for a in by_part[part_id]:
            area_anchor = f"{slug}--{a['area_slug']}"
            w(f"  - [{a['area_title']}](#{area_anchor}) "
              f"({len(a['leaves'])} leaves)\n")
    w("\n---\n\n")

    # --- Body ---
    for part_id in sorted(by_part.keys()):
        part_title = parts_by_id.get(part_id, {}).get("title", part_id)
        part_blurb = parts_by_id.get(part_id, {}).get("blurb", "")
        w(f"## {part_title}\n\n")
        if part_blurb:
            w(f"*{part_blurb}*\n\n")
        for a in by_part[part_id]:
            slug = part_id.replace("/", "-")
            area_anchor = f"{slug}--{a['area_slug']}"
            w(f"### {a['area_title']}<a id=\"{area_anchor}\"></a>\n\n")
            if a.get("source"):
                w(f"*Source: `{a['source']}` · File: `{a['file']}`*\n\n")
            else:
                w(f"*File: `{a['file']}`*\n\n")
            for leaf in a["leaves"]:
                emit_leaf_md(w, leaf)
        w("\n")


def emit_leaf_md(w, leaf: dict) -> None:
    title = leaf.get("title") or leaf.get("slug", "(untitled)")
    slug = leaf.get("slug", "")
    diff = leaf.get("difficulty")
    aliases = leaf.get("aliases") or []
    see_also = leaf.get("see_also") or []
    summary = leaf.get("summary", "")
    facts = leaf.get("facts") or []
    formulas = leaf.get("formulas") or []
    valid_regime = leaf.get("valid_regime")
    key_dates = leaf.get("key_dates") or []
    sources = leaf.get("sources") or {}

    header = f"#### {title} · `{slug}`"
    if diff is not None:
        header += f" · difficulty {diff}"
    w(header + "\n\n")

    if summary:
        w(f"{summary}\n\n")

    if aliases:
        w(f"*Aliases:* {', '.join(f'`{a}`' for a in aliases)}  \n")

    if facts:
        w("**Facts**\n\n")
        for f in facts:
            w(f"- {f}\n")
        w("\n")

    if formulas:
        w("**Formulas**\n\n")
        for f in formulas:
            w(f"- `{f}`\n")
        w("\n")

    if valid_regime:
        w(f"**Valid regime:** {valid_regime}\n\n")

    if key_dates:
        w("**Key dates**\n\n")
        for d in key_dates:
            w(f"- {d}\n")
        w("\n")

    if see_also:
        w(f"*See also:* {', '.join(f'`{s}`' for s in see_also)}\n\n")

    if sources:
        parts = []
        if "wikipedia" in sources:
            parts.append(f"[Wikipedia](https://en.wikipedia.org/wiki/{sources['wikipedia']})")
        if "wikidata" in sources:
            parts.append(f"[Wikidata](https://www.wikidata.org/wiki/{sources['wikidata']})")
        for k, v in sources.items():
            if k in ("wikipedia", "wikidata"):
                continue
            parts.append(f"{k}: {v}")
        if parts:
            w(f"*Sources:* {' · '.join(parts)}\n\n")

    w("---\n\n")


def emit_json(out, domains: dict | None, sources: dict | None, areas: list[dict]) -> None:
    payload = {
        "summary": build_summary(domains, areas),
        "domains": domains,
        "sources": sources,
        "areas": areas,
    }
    json.dump(payload, out, indent=2, ensure_ascii=False)
    out.write("\n")


def main() -> int:
    p = argparse.ArgumentParser(description="Consolidate reference/ into one file.")
    p.add_argument("--format", choices=["md", "json"], default="md",
                   help="Output format (default: md)")
    p.add_argument("--output", default=None,
                   help="Output path, or '-' for stdout. "
                        "Default: reference/_snapshot.md (or .json)")
    args = p.parse_args()

    domains = load_yaml(DOMAINS_FILE) if DOMAINS_FILE.exists() else None
    sources = load_yaml(SOURCES_FILE) if SOURCES_FILE.exists() else None
    areas = collect_areas()

    if args.output == "-":
        out = sys.stdout
        close_out = False
    else:
        default = f"reference/_snapshot.{args.format}"
        target = args.output or default
        out = open(REPO_ROOT / target, "w", encoding="utf-8")
        close_out = True
        print(f"Writing to {target} …", file=sys.stderr)

    try:
        if args.format == "md":
            emit_markdown(out, domains, sources, areas)
        else:
            emit_json(out, domains, sources, areas)
    finally:
        if close_out:
            out.close()

    summary = build_summary(domains, areas)
    print(
        f"done: {summary['total_leaves']} leaves, "
        f"{summary['total_areas']} areas, "
        f"{summary['total_parts_populated']}/{summary['total_parts_defined']} Parts.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
