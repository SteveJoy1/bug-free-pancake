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

Each leaf is a YAML entry with three layers of content:

- **Layer 1 — index**: `slug`, `title`, `summary`. The taxonomy — what exists and what to call it.
- **Layer 2 — fact card**: `facts`, `formulas`, `key_dates`, `valid_regime`. The offline-queryable core of a concept, enough for an AI to generate and grade questions without fetching external content.
- **Layer 3 — deep content**: delegated to external sources via `sources.wikipedia`, `sources.wikidata`, etc. Do not duplicate encyclopedic prose here.

```yaml
- slug: newtons-laws-of-motion
  title: Newton's Laws of Motion
  summary: Three foundational laws relating force, mass, and motion.
  difficulty: 1          # 1 (foundational) to 5 (specialist)
  aliases: [newtons-laws]
  see_also: [force, mass, acceleration]

  # Layer 2 — fact card
  facts:
    - "First (inertia): an object at rest stays at rest, an object in motion stays in motion, unless acted upon by a net external force."
    - "Second: the net force on an object equals the rate of change of its momentum; for constant mass, F = m·a."
    - "Third: for every action, there is an equal and opposite reaction."
  formulas:
    - "F = m·a (constant mass)"
    - "F = dp/dt (general)"
  valid_regime: "Non-relativistic (v ≪ c), classical scales."
  key_dates:
    - "1687: Principia Mathematica published."

  # Layer 3 — external pointers (verify before trusting)
  sources:
    wikipedia: "Newton%27s_laws_of_motion"
    wikidata: Q14627     # placeholder; verify
```

**Required**: `slug`, `title`, `summary`.
**Optional**: everything else. Omit fields that don't apply — not every concept has formulas or key dates.

**`slug` is the join key** — it must match `../mirror/notes/<slug>.md` for diffing to work. Pick canonical forms and stick to them.

### Fact card guidelines

- **Facts**: short propositional statements. Each should be independently quotable as a quiz question or answer. Aim for 2–6 per leaf.
- **Formulas**: only where a concept has canonical mathematical form. Include units and variable definitions where not obvious.
- **Valid regime**: when, where, and at what scale the concept applies. Essential for physics and algorithms (complexity regime).
- **Key dates**: only when a date is part of the canon (1687 for Principia, 1977 for RSA). Don't clutter with trivia.
- **Sources**: prefer Wikipedia (canonical article slug) and Wikidata (QID). Add `khan_academy`, `mdn`, etc. when a pedagogical link is materially better than Wikipedia.

### When to promote a leaf to Layer 3

Add a sibling `<slug>.md` only if: (a) external sources are absent or bad, (b) offline access to deep prose is required, or (c) the synthesis is the value (your framing, not just restating Wikipedia). Default to not doing this.

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
