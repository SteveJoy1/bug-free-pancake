# Ingest — ChatGPT export → mirror notes

Drop zone for external conversation exports (ChatGPT, Claude.ai, whatever) and the canonical spec for processing them into `mirror/notes/`.

## Quick start for the next agent

You (the next Claude session) are being asked to:

1. **Find the export** in `mirror/ingest/`. The user typically drops one of:
   - `conversations.json` — ChatGPT's "Export data" zip contains this.
   - `chat.html` or similar — occasional alternate format.
   - Or the user will name the path in their prompt.

   If nothing is there, ask the user for the path.

2. **Parse it.** ChatGPT's `conversations.json` is an array of conversation objects. Each has a `mapping` graph of message nodes; each node has an `author.role` (`user` / `assistant` / `system`) and `content.parts` (the text). Walk the `current_node` chain or sort by `create_time` to get the linear transcript.

3. **Extract knowledge evidence** — NOT every topic mentioned. See §"What counts as evidence" below.

4. **Map to reference slugs** — every claim you write should use a slug that either already exists in `reference/tree/**/*.yaml` or is a reasonable new leaf. See §"Slug mapping" below.

5. **Write or update `mirror/notes/<slug>.md`** using the existing schema (frontmatter + body). See `mirror/README.md` and `mirror/notes/_template.md`.

6. **Commit in clusters**, not one giant commit. One commit per topic area (e.g., "ingest: classical-mechanics notes from ChatGPT 2026-03-13 conversation"). Makes review and revert cheap.

## The single most important rule

**This is measurement, not invention.** The mirror records what the user already knows — not what ChatGPT taught them, not what you (next agent) fill in from general knowledge.

If a conversation is the user asking "what is Kelvin?" and ChatGPT explaining it, that's evidence the user *didn't* know it — not evidence that they now do. The quiz (quiz.html) is the primary instrument for confidence calibration. Ingest from exports should lean conservative.

## What counts as evidence

Strong signal (can write a mirror note at confidence 3–5):
- User **explains** a concept correctly, in their own words.
- User **corrects** the assistant or notices a subtle error.
- User **applies** the concept to a new situation.
- User **builds on** an explanation with a deeper follow-up.
- User expresses explicit familiarity: *"I use X every day, but…"*, *"I learned Y in grad school."*

Weak / inverse signal (don't claim knowledge; consider adding to GAPS.md):
- User **asks** a basic question about a topic.
- User **accepts without follow-up** a long explanation from the assistant.
- User says *"I don't remember how X works"* or similar.

Ambiguous (note cautiously, mark confidence 2–3):
- Conversation was collaborative problem-solving — hard to attribute specific knowledge.
- User paraphrases what the assistant just said.

## Slug mapping

Every mirror note's filename is `<slug>.md`. The slug is the join key that lets future sessions diff `mirror/` against `reference/`. So:

1. **Prefer existing reference slugs.** Before creating a new one, search:
   ```bash
   grep -r "slug: " reference/tree/ | sort
   ```
   If the topic matches an existing reference leaf, use that slug verbatim.

2. **If no reference leaf exists**, decide:
   - Is this something that *should* exist in the canonical reference (broadly knowable)? If yes: first add a stub leaf to the appropriate `reference/tree/<part>/<area>.yaml`, then write the mirror note using that slug.
   - Is this idiosyncratic / personal (a specific person, pet project, inside joke)? Create a mirror-only note with a descriptive slug. These won't have a reference counterpart — that's fine; tag with `personal` or `idiosyncratic`.

3. **Slug conventions**: lowercase, kebab-case, topic-specific. Match the reference tree's style. Avoid names, dates, or context that would age poorly.

## Mirror note content

Follow the existing schema exactly — see `mirror/notes/_template.md` and any of the four existing notes for worked examples.

Frontmatter:

```yaml
---
title: <Human-readable title>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags: [<existing-tag>, <existing-tag>]   # every tag must be in mirror/TAGS.md
confidence: <1-5>                        # conservative initial reading
confidence_history:
  - date: <YYYY-MM-DD>
    session_id: "chatgpt-ingest-<date>"
    confidence: <same as above>
    tiers_passed: null                   # not applicable — not from the quiz
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversation <date> by ingest session."
gaps: []                                 # open questions the user actually had
sources:
  - "ChatGPT conversation YYYY-MM-DD"
  - "<any URLs/books the user cited in the conversation>"
---
```

Body:

```markdown
# <Title>

## Summary

One to three sentences in the user's voice, describing what they demonstrated knowing about this topic. Not a textbook definition.

## Evidence

What in the conversation shows this? Short quotes or paraphrases of user turns. Enough for a future session (or the user themselves) to verify your reading.

## Gaps to close

Open questions / uncertainties the user expressed. Optional; skip section if none.

## Related

- [[related-slug]]
- `reference/tree/<part>/<area>.yaml#<slug>` when a reference leaf exists.
```

## Tag hygiene

Before using a tag, confirm it exists in `mirror/TAGS.md`. If adding a new tag:

1. Add it to `TAGS.md` with a one-line description.
2. Then use it.

Never scatter unmanaged tags — the join doesn't work if tags aren't canonical.

## Gaps handling

`mirror/GAPS.md` is the human-facing index of known-unknowns. If ingestion surfaces:

- A cluster of related open questions → add a section to `GAPS.md`.
- A specific uncovered rubric point on a leaf that already has a note → append to that note's `gaps: []` frontmatter.

## Volume guidance

A ChatGPT export can contain thousands of messages. Do NOT try to write a mirror note for every topic mentioned. Target:

- ~1 note per **distinct demonstrated competence** (strong signal above).
- Skip topics that are pure Q&A with no user-side knowledge displayed.
- If the export is large, process in passes — breadth first (many shallow notes), then depth (update notes with more evidence on subsequent passes).

## Calibration note to leave for the user

When you're done ingesting, post a summary back to the user:

- How many notes created / updated.
- Breakdown by confidence level.
- Most ambiguous judgments you made (where evidence was borderline).
- Any topics where you added new tags or created reference stubs.
- Recommendation: run the quiz over the ingested leaves to validate confidence — your initial reading is a hypothesis, not a measurement.

## Privacy

ChatGPT exports routinely contain personal data (names, locations, work context, medical questions, etc). Before committing:

- Strip identifying details from quoted evidence — paraphrase instead.
- If a conversation is clearly private (health, finances, relationships) and the user hasn't asked for it in the mirror, skip it.
- Ask the user if any content seems questionable. The mirror will be public if `bug-free-pancake` is public — treat accordingly.

## Commit pattern

```
git add mirror/notes/<cluster>*.md mirror/TAGS.md mirror/GAPS.md
git commit -m "ingest: <topic cluster> notes from ChatGPT export <date>"
```

Repeat per cluster. After all clusters:

```
git add mirror/ingest/.processed   # append the export filename
git push -u origin main
```

## `.processed` marker

Same idea as `mirror/sessions/.processed` — append the export filename once you've finished processing it so future agents know not to reprocess:

```
mirror/ingest/.processed
```

One filename per line.

## Reference context you'll need

Read these before starting:

- `mirror/README.md` — mirror conventions and frontmatter spec.
- `mirror/TAGS.md` — current tag vocabulary.
- `mirror/GAPS.md` — current known-unknowns.
- `reference/README.md` — reference tree schema.
- `reference/tree/README.md` — what's populated and where.
- `mirror/notes/_template.md` — frontmatter template.
- An existing note like `mirror/notes/momentum.md` — worked example with confidence_history.
