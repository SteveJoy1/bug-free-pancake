# Reference

A curated "shape of human knowledge" — the canonical outline that `../mirror/` is measured against.

Where `mirror/` answers *"what do I know?"*, `reference/` answers *"what exists to be known?"*.

## Source

The top-level structure is **Propaedia** — Mortimer Adler's *Outline of Knowledge*, *Encyclopædia Britannica* 15th edition (1974). It divides the world into **10 Parts → 42 Divisions → 189 Sections**. We use the 10 Parts as the skeleton.

Where Propaedia is weak (post-1974 fields: computing, genomics, climate, ML) or non-machine-readable, we graft in:

- **Wikidata** for stable, machine-readable leaf identifiers.
- **Domain canons** where one exists:
  - **PhySH** (physics), **MSC** (math), **MeSH** (medicine), **ACM CCS** (computing), **JEL** (economics).
- **Curricula** (Khan Academy, AP, IB) for pedagogical ordering where it matters.

See `sources.yaml` for the provenance of every subtree. A branch without a source does not belong here.

## Schema

Each leaf is a YAML entry:

```yaml
- slug: newtons-laws-of-motion
  title: Newton's Laws of Motion
  summary: Three foundational laws relating force, mass, and motion.
  difficulty: 1          # 1 (foundational) to 5 (specialist)
  wikidata: Q14627       # verify before trusting
  aliases: [newtons-laws]
  see_also: [force, mass, acceleration]
  source: physh:classical-mechanics
```

Required: `slug`, `title`, `summary`.
Optional: `difficulty`, `wikidata`, `aliases`, `see_also`, `source`.

**`slug` is the join key** — it must match `../mirror/notes/<slug>.md` for diffing to work. Pick canonical forms and stick to them.

## Diffing against mirror/

Conceptually:

- **Gaps** = `{reference slugs} \ {mirror slugs}` — topics in the canon you have no note on.
- **Covered** = intersection — topics you've taken notes on.
- **Outside the canon** = `{mirror slugs} \ {reference slugs}` — personal notes (people, tools, books) or things to promote into the reference.

An AI can trivially generate a coverage report and sample uncovered leaves for quiz questions.

## Why a separate folder from mirror/

- `mirror/` = subjective, revisable, messy, confidence-scored.
- `reference/` = bounded, provenanced, stable.
- Mixing them destroys the comparison, which is the whole point.

## Relationship to the eventual `Mirror` repo split

Both `mirror/` and `reference/` are part of the same knowledge system and should move together when this is split out with `git subtree split --prefix=<folder>`. Either split both into one target repo, or into two (e.g., `Mirror` and `Mirror-Reference`) depending on whether you want to share the canon publicly.
