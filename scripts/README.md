# scripts/

Utilities for maintaining the reference tree and quiz/mirror infrastructure.

## `consolidate_reference.py`

Walks `reference/tree/**/*.yaml` and produces a single consolidated file for external review or audit.

### Usage

Run from the repo root:

```bash
# Markdown (default) → reference/_snapshot.md
python3 scripts/consolidate_reference.py

# JSON → reference/_snapshot.json
python3 scripts/consolidate_reference.py --format json

# To stdout
python3 scripts/consolidate_reference.py --output -

# To a specific path
python3 scripts/consolidate_reference.py --output /tmp/snapshot.md
```

### Dependencies

`PyYAML`:

```bash
pip install pyyaml
```

### Output

- **Markdown**: human-readable, with a table-of-contents, per-part summary, and per-leaf content (summary, facts, formulas, key_dates, sources). Each leaf renders as a subsection with a direct anchor.
- **JSON**: preserves the full leaf schema verbatim for programmatic processing.

### When to use

- Sharing the full reference with an external reviewer who doesn't want to browse 20+ YAML files.
- Diffing reference content between releases (JSON format).
- Backing up the reference state at a point in time — commit `_snapshot.md` when you want a frozen audit trail.

Snapshots are not committed by default; add `reference/_snapshot.md` and `reference/_snapshot.json` to `.gitignore` if you want to keep them local.
