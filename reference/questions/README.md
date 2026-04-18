# Question banks

Per-area question banks used by `../../quiz.html` to probe knowledge against the reference tree. Questions are hand-written here (no LLM at runtime); grading happens later in a Claude session using the exported session JSON.

## Directory layout

Mirrors `../tree/`:

```
reference/questions/
  01-matter-and-energy/
    classical-mechanics.questions.yaml
  07-technology/
    ...
```

One `.questions.yaml` per area file in `../tree/`.

## File schema

```yaml
area:
  slug: <matches the area slug in ../tree/<part>/<area>.yaml>
  title: Human-readable title
  parent: <part slug>

questions:
  - leaf: <leaf-slug>         # must match a slug in the corresponding tree/ area
    items:
      - id: <leaf-slug>.q1    # stable, unique question id
        level: recall | comprehension | application | analysis | regime-boundary | connection
        prompt: "The question text shown to the user."
        rubric:
          - "Key point a good answer must include."
          - "Another key point."
```

### Level vocabulary

Loose Bloom-taxonomy mapping:

| level | Bloom | What it tests |
|-------|-------|---------------|
| `recall` | 1 | remember the definition, formula, or basic fact |
| `comprehension` | 2 | explain in your own words |
| `application` | 3 | use the concept on a new example or problem |
| `analysis` | 4 | compare, contrast, decompose |
| `regime-boundary` | 4 | where does the concept stop applying? |
| `connection` | 5 | link to another concept or deeper principle |

Target mix: 1 question at recall/comprehension, 1 at application, 1 at analysis / regime-boundary / connection. That's the canonical three-question probe per leaf — enough coverage to tell memorization from understanding.

### Rubric guidelines

- Rubric entries are the **grading key**, not the answer shown to the user.
- Each entry is one key point. A good answer should hit most of them; grading weighs coverage.
- Be specific. "Understands the concept" is useless; "States F = m·a, identifies units as N = kg·m/s²" is gradable.

## Quiz flow

1. User opens `quiz.html`, picks a topic and session length.
2. Questions are served from this bank. User types a free-text answer and self-rates confidence 1–5.
3. Responses are held in `localStorage` so refresh/close/reopen resumes mid-session.
4. At the end:
   - **Preferred**: *Commit to repo* — writes a session JSON directly to `../../mirror/sessions/` on `main` via the GitHub Contents API using a fine-scoped PAT stored in the browser.
   - **Fallback**: *Download JSON* — for when no token is set, or the API call fails.
5. A later Claude session reads unprocessed session files, grades answers against the rubric, and creates or updates `../../mirror/notes/<slug>.md`.

## Session export schema

```json
{
  "session_id": "2026-04-18T14:30:00.000Z",
  "area": "classical-mechanics",
  "area_title": "Classical Mechanics",
  "part": "01-matter-and-energy",
  "started_at": "2026-04-18T14:30:00.000Z",
  "completed_at": "2026-04-18T14:52:17.000Z",
  "response_count": 10,
  "responses": [
    {
      "question_id": "newtons-laws-of-motion.q1",
      "slug": "newtons-laws-of-motion",
      "level": "recall",
      "prompt": "State Newton's three laws of motion in your own words.",
      "answer": "First law is about inertia...",
      "self_rating": 4,
      "skipped": false,
      "timestamp": "2026-04-18T14:31:02.000Z"
    }
  ]
}
```

The exported JSON is self-contained — it includes the prompt text, so a grading session doesn't need the question bank loaded to proceed. (It does still need the rubric, which lives in this directory.)

## Grading protocol (for future Claude sessions)

Trigger: user says something like "grade my quiz sessions."

1. List `mirror/sessions/*.json` and read `mirror/sessions/.processed` (the already-graded log; may be empty).
2. For each file NOT in `.processed`, oldest first:
   a. Load rubrics from `reference/questions/**/*.questions.yaml`.
   b. Load any existing mirror notes: `mirror/notes/<slug>.md`.
   c. For each non-skipped response:
      - Match `question_id` to its rubric.
      - Grade user's `answer` against rubric. Note what was covered, what was missed.
      - Compare against user's `self_rating` — overconfidence and underconfidence are both signals.
   d. For each `slug` touched:
      - Create or update `mirror/notes/<slug>.md`.
      - Frontmatter: `confidence` (weighted from graded answers + self-rating), `gaps` (uncovered rubric points), `updated` (today).
      - Body: user's own words from their answers, lightly cleaned. Keep in their voice; don't rewrite into your own phrasing.
   e. Append the session filename to `mirror/sessions/.processed`.
3. Commit — one per session or a batch, as appropriate.

See `../../mirror/sessions/README.md` for the full lifecycle model.

## Adding new question banks

1. Create `<part>/<area>.questions.yaml` mirroring the corresponding `tree/` file.
2. Aim for ~3 questions per leaf; don't sacrifice quality for volume.
3. Add the topic to the `TOPICS` registry at the top of `quiz.html` so it's pickable.
