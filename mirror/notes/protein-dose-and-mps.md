---
title: Protein — dose, source kinetics, and MPS
created: 2026-04-19
updated: 2026-04-19
tags: [fitness, nutrition]
confidence: 3
confidence_history:
  - date: 2026-04-19
    session_id: "chatgpt-ingest-2026-04-19"
    confidence: 3
    tiers_passed: null
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversation 2026-01-01 'Protein absorption rates'. I framed the leucine-threshold argument and drew the correct inference that casein needs a larger gram dose to match whey on leucine. Some specific numeric thresholds were surfaced by the assistant, not recalled by me — hence 3."
gaps:
  - "The ~25 g MPS-maxing heuristic I stated was implicitly whey-anchored; actual dose-response studies used ~20 g of whole egg protein. The heuristic is broader than I thought."
  - "The pre-sleep dose ceiling above ~40 g casein is not cleanly established in the literature — there is no published 40 vs 60 vs 80 g head-to-head overnight MPS study, only indirect evidence."
  - "Leucine 'trigger' heuristic has mixed empirical support — faster/higher leucinemia does not always translate to higher MPS."
sources:
  - "ChatGPT conversation 2026-01-01 'Protein absorption rates'"
  - "Reference: reference/tree/03-life-on-earth/biology-fundamentals.yaml#protein (slug match is approximate — reference leaf is biology-general, not sports-nutrition specific)"
---

# Protein — dose, source kinetics, and MPS

## Summary

My working model: **whey is meaningfully faster than casein** (time-to-peak ~49 min vs ~96 min; whey peaks higher too), **chicken as whole food is intermediate and highly matrix-dependent**, and **casein needs ~35% more grams to match whey on leucine** (~11% leucine for whey vs ~8% for casein). For pre-sleep, ~30–40 g casein is the best-evidenced range — the rationale is **duration of overnight coverage**, not hitting a leucine threshold.

## Evidence

- I asked for a "X% faster than" heuristic across whey / casein / chicken, recognizing that absolute numbers vary with food matrix and meal composition — that's the right framing for a consumer-facing heuristic.
- I correctly reasoned from premise: "If the ~25 g protein / MPS-max heuristic is based on whey, casein needs a larger dose to hit the same signal" — the leucine-matching math that confirms this is what the literature uses.
- I asked specifically about going above 40 g casein pre-sleep being unhelpful — the correct skeptical framing because the dose-response ceiling there is more assumed than measured.
- I'm a 37 y/o, ~200 lb / ~91 kg male; gave the context to let the assistant translate the pre-sleep heuristic to a bodyweight-anchored dose (~0.4 g/kg ≈ 36 g, in the 30–40 g band).

## Gaps to close

1. **The ~25 g heuristic is for high-quality intact protein**, not whey specifically. Whole-egg tracer work established the original ~20 g ceiling in post-exercise dose-response.
2. **For post-exercise MPS**, going from 20 g → 40 g does NOT reliably further increase MPS in typical young-adult windows — extra amino acids get oxidized.
3. **For pre-sleep MPS in older adults**, 40 g outperformed 20 g, and adding leucine to 20 g didn't replicate the 40 g effect. Total substrate seems to matter more than leucine spikes overnight.
4. **Whole-food chicken** has no canonical Tmax — meal matrix (fat, fiber, chewing, cooking) dominates the kinetics. Can behave as "fast-digested" in low-fat/low-fiber contexts.

## Related

- [[hypertrophy-rir-and-volume]]
- `reference/tree/03-life-on-earth/biology-fundamentals.yaml#protein` (related but upstream — the reference leaf is biology of proteins, not sports-nutrition dose-response)
