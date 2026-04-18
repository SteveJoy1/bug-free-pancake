# Quiz sessions

Raw session JSON files committed from `../../quiz.html` via the GitHub API. Each file is the output of one quiz session — questions served, user's free-text answers, self-rated confidence.

## Filename convention

```
<ISO-timestamp>--<area-slug>.json
```

The timestamp has colons replaced with dashes (for filesystem safety). Examples:

```
2026-04-18T14-30-00-000Z--classical-mechanics.json
2026-04-19T09-12-00-000Z--classical-mechanics.json
```

Sort-by-filename = sort-by-time.

## Lifecycle

1. **Created** by `quiz.html` when the user taps *Commit to repo* at the end of a session. The commit is made directly to `main` via the GitHub Contents API using the user's stored fine-scoped PAT.
2. **Pending** until graded — a Claude session reads unprocessed files, grades each response against the rubric in `../../reference/questions/`, and updates `../notes/<slug>.md` accordingly.
3. **Marked processed** by appending the filename to `.processed`. This is the durable "already graded" log — no file moves or renames, so commit history stays clean.

## `.processed` marker

One filename per line, oldest first. Example:

```
2026-04-18T14-30-00-000Z--classical-mechanics.json
2026-04-19T09-12-00-000Z--classical-mechanics.json
```

A file is **unprocessed** if it's in this directory but NOT in `.processed`. That's the grading queue.

## Grading protocol (for Claude sessions)

When the user says "grade my quiz sessions" or similar:

1. List `mirror/sessions/*.json`.
2. Read `mirror/sessions/.processed` (may not exist yet — treat as empty).
3. For each file not in `.processed`, oldest first:
   - Load its responses.
   - Load matching rubrics from `reference/questions/**/*.questions.yaml`.
   - For each non-skipped response:
     - Compare `answer` to `rubric[]`. Identify covered points, missed points, and any extra content.
     - Weight against `self_rating` — note calibration (over/under-confident).
   - For each distinct `slug` touched:
     - Create or update `mirror/notes/<slug>.md`:
       - Frontmatter: `confidence` (1–5, derived from graded coverage + self-rating; update existing), `gaps` (append uncovered rubric points), `updated` (today).
       - Body: user's answer content, lightly cleaned, in their voice. Not rewritten.
   - Append the session filename to `.processed`.
4. Commit: one commit per session file processed, or a batch commit listing all processed files.

## Why session files, not direct-to-notes

- **Preserves the raw input.** The user's exact answers are auditable.
- **Idempotent grading.** A grading rule change can be re-run over old sessions.
- **Append-only.** No risk of the UI silently overwriting a note the user was curating by hand.

## File schema

See `../../reference/questions/README.md` §"Session export schema".
