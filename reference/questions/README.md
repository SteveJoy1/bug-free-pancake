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

### Level vocabulary and ladder order

Questions are asked in the ladder below. **Start at step 0 (recognition) and drill down only on success.** Failure or low confidence stops the ladder and moves to the next leaf.

| level | step | What it tests |
|-------|-----:|---------------|
| `recognition` | **0 (ask first)** | *"Does this topic ring a bell? What field does it belong to?"* The gate. |
| `comprehension` / `connection` / `analysis` / `regime-boundary` | 1 | conceptual understanding — explain, relate, or place the concept |
| `application` | 2 | use the concept on a new example or problem |
| `recall` | 3 (ask last) | state the formula/definition cold |

Recognition is deliberately cheap: a failed recognition question means we learned "user doesn't know this" in one question rather than wasting three. The overall design prioritizes **mapping breadth** (how many leaves do I know something about) over **depth-at-all-costs** (how perfectly do I know each).

Target mix: **four questions per leaf** — one at each step. Order within the YAML file doesn't matter; the quiz engine sorts by `step` at load time.

### Confidence derivation

With four tiers, confidence maps cleanly to tiers passed:

| Tiers passed | Confidence | Means |
|-:|-:|-|
| 0 | 1 | Don't recognize it |
| 1 | 2 | Recognize but can't engage |
| 2 | 3 | Conceptual grasp |
| 3 | 4 | Can apply it |
| 4 | 5 | Full mastery (recall included) |

### Rubric guidelines

- Rubric entries are the **grading key**, not the answer shown to the user.
- Each entry is one key point. A good answer should hit most of them; grading weighs coverage.
- Be specific. "Understands the concept" is useless; "States F = m·a, identifies units as N = kg·m/s²" is gradable.

## Quiz flow

1. User opens `quiz.html`, picks a topic and session length.
2. Questions are served from this bank. User types a free-text answer and self-rates confidence 1–5.
3. Responses are held in `localStorage` so refresh/close/reopen resumes mid-session.
4. At the end:
   - **Preferred**: *Commit to repo* — opens GitHub's new-file editor in a new tab with the session JSON pre-filled at `../../mirror/sessions/<timestamp>--<area>.json`. User taps *Commit directly to the main branch* on GitHub. No credentials stored in the browser.
   - **Fallback**: *Download JSON* — for when the session is too large for a URL or popups are blocked.
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
      - Frontmatter:
        - `confidence`: latest reading (derived from tiers passed).
        - `confidence_history`: **append** a new entry with `date`, `session_id`, `confidence`, `tiers_passed`, `tiers_available`, and `notes` (any detected calibration issues, hints used, etc). Never delete prior entries — the trajectory itself is valuable.
        - `gaps`: merge — keep unresolved gaps from prior sessions, add new ones, remove any that the current session confirmed resolved.
        - `updated`: today.
      - Body: user's own words from their answers, lightly cleaned. Keep in their voice; don't rewrite into your own phrasing.
   e. Append the session filename to `mirror/sessions/.processed`.
3. Commit — one per session or a batch, as appropriate.

See `../../mirror/sessions/README.md` for the full lifecycle model.

## Adding new question banks

1. Create `<part>/<area>.questions.yaml` mirroring the corresponding `tree/` file.
2. Aim for ~3 questions per leaf; don't sacrifice quality for volume.
3. Add the topic to the `TOPICS` registry at the top of `quiz.html` so it's pickable.
