# Mirror-sourced question banks

Question banks keyed to **mirror note slugs**, not reference leaves. Used by `../../quiz.html` to probe the subjective side of the system: "can I defend what this note claims I know?"

## Why separate from `reference/questions/`

- `reference/questions/<part>/<area>.yaml` — questions keyed to canonical leaves in `reference/tree/`. These test "what should be knowable."
- `mirror/questions/<area>.yaml` — questions keyed to slugs in `mirror/notes/`. These test "what *I* claim to know."

Both live side-by-side. Some slugs exist in both (canonical topics I've made a note on). Some are mirror-only (idiosyncratic content — `fl-property-tax-portability`, `duke-solar-net-metering`). A mirror quiz probes the full mirror; a reference quiz probes the canon. The comparison is the point of the diff.

## Schema

Same shape as `reference/questions/`. See `../../reference/questions/README.md` for:

- 4-tier ladder (recognition → comprehension/connection/analysis/regime-boundary → application → recall)
- `prompts: [...]` (array) for recognition; `prompt: "..."` (singular) for the other levels
- Rubric entries as grading keys, not hints
- Tiers-to-confidence mapping (0→1, 1→2, 2→3, 3→4, 4→5)

One difference: the `leaf:` slug under `questions:` must match a **mirror note filename** (`mirror/notes/<slug>.md`), not a reference tree slug.

```yaml
area:
  slug: fitness-and-nutrition
  title: Fitness & nutrition
  parent: mirror

questions:
  - leaf: hypertrophy-rir-and-volume    # matches mirror/notes/hypertrophy-rir-and-volume.md
    items:
      - id: hypertrophy-rir-and-volume.q0
        level: recognition
        prompts:
          - "When someone says 'ALMI' and 'RIR' in the same sentence, what field are they in?"
        rubric:
          - "Strength training / hypertrophy / resistance exercise."
      # ... q1 recall, q2 application, q3 analysis
```

## Registering in `quiz.html`

Add an entry to the `TOPICS` array near the top of the script block:

```js
{
  slug: 'fitness-and-nutrition',
  title: 'Fitness & nutrition (mirror)',
  part: 'mirror',
  source: 'mirror',
  path: 'mirror/questions/fitness.questions.yaml'
}
```

The `source: 'mirror'` field distinguishes these from reference-sourced banks. The quiz UI can use it to label or filter.

## Grading a mirror-sourced session

Same protocol as reference-sourced sessions (see `../../reference/questions/README.md`): a future Claude session reads unprocessed `mirror/sessions/*.json` files, matches each response's `question_id` to the rubric in this directory, and updates `mirror/notes/<slug>.md` with new `confidence_history` entries.

The slug match still works — because a mirror-sourced question ID already *is* the mirror slug.
