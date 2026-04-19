# Mirror

A personal knowledge base — organized, searchable, expandable. Notes about things I've learned or want to remember, plus explicit tracking of where the gaps are.

## How to add a note

1. Copy `notes/_template.md` to `notes/<slug>.md` (kebab-case).
2. Fill in the frontmatter.
3. Write the note. Short and skimmable beats long and exhaustive.
4. If you use a new tag, add it to `TAGS.md` first.

## Frontmatter fields

- `title` — human-readable title.
- `created` / `updated` — ISO dates (YYYY-MM-DD).
- `tags` — list; each tag must appear in `TAGS.md`.
- `confidence` — 1 (just encountered) to 5 (could teach it). Always the **latest** reading.
- `confidence_history` — append-only list of prior readings, each with `date`, `confidence`, `tiers_passed`/`tiers_available`, `session_id`, and optionally `needed_hint`. Never deleted; this is the durable trajectory.
- `status` — optional; `opted_out` if the user chose "Don't need this" on the leaf. Excludes from future sampling.
- `gaps` — list of open questions or things not yet understood.
- `sources` — where this came from (URL, book, person, conversation).

### Why `confidence_history` is append-only

A single session gives a noisy reading. Over N sessions the median of `confidence_history` is a better estimate of actual knowledge than any single value. The array also captures whether a leaf is *improving* (went from 1 → 4) vs. *stable* (always 2) vs. *regressing* (4 → 2, probably needs review). Don't delete entries, even if they seem outdated.

## Finding things

- Full-text: `grep -r "keyword" notes/`
- Filter by tag: `grep -l "- tag-name" notes/*.md`
- Find the learning edge: `grep -l "^confidence: [12]$" notes/*.md`

## Conventions

- **Flat folder, tags over subfolders.** Every note lives in `notes/`. Categorization is via `tags`, not directory depth — avoids "which folder?" paralysis.
- **Link with `[[wiki-links]]`.** Reference other notes by slug: `[[other-note]]`. Works in Obsidian, Foam, and VS Code markdown extensions.
- **Short notes over long ones.** If a note grows past ~1 page, split and link.
- **Bump `updated` when you revise.**

## Roadmap

- Layer a static site generator (MkDocs Material or Quartz) once the collection is big enough to need full-text search and a graph view.
- Auto-generate `GAPS.md` from frontmatter instead of maintaining by hand.
- Eventually move this folder to its own repo (`Mirror`) via `git subtree split`.
