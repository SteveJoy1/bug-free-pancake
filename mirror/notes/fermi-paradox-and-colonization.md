---
title: Fermi paradox — galactic colonization timescales
created: 2026-04-19
updated: 2026-04-19
tags: [physics]
confidence: 2
confidence_history:
  - date: 2026-04-19
    session_id: "chatgpt-ingest-2026-04-19"
    confidence: 2
    tiers_passed: null
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversation 2026-04-03 'Energy for 0.01c Acceleration'. I constructed the Milky-Way colonization arithmetic correctly and applied Darwinian game-theory logic to behavior, but explicitly said 'I learned here' — so this is a moderate-signal framing + learning combo. Confidence 2."
gaps:
  - "Darwinian selection pressure favors replication, but level-of-selection changes and cultural decoupling break the straight-line 'therefore galaxy-filling' inference. Expansion is a plausible prior, not a theorem."
  - "Percolation-style colonization models show expansion can stall rather than fill the graph — a serious formal attempt at why galactic silence isn't contradictory."
  - "Asteroids/Kuiper-belt volatiles/solar energy are easier to harvest than deep gravity wells — so the 'bulldozed Earth' framing is stronger than needed; the cleaner paradox is 'why no non-natural infrastructure of any kind.'"
sources:
  - "ChatGPT conversation 2026-04-03 'Energy for 0.01c Acceleration'"
---

# Fermi paradox — galactic colonization timescales

## Summary

My working argument for the Fermi paradox: the Milky Way is ~100,000 ly across, stars are ~5 ly apart on average. At 0.001c (0.1% of light speed) a full galaxy crossing is ~100 million years and a star-to-star hop is ~5,000 years — trivial compared to the universe's 13.8 Gyr age. A civilization arriving even a few hundred million years before us should have had time to propagate self-replicating machines across the galaxy. Darwinian game theory also predicts expansionist behavior as the default because variants that produce more copies outcompete variants that don't. So: either expansionist technological life is extremely rare, or one of my hidden engineering/behavioral assumptions fails harder than it looks.

## Evidence

- I did the Milky Way arithmetic correctly on-the-fly: 13.7 Gyr head start + 0.1% c + replicate-on-arrival model → full coverage in ~100 Myr, which is ~1% of the available time.
- I extended to behavior with a Darwinian argument: "if there are two variants of a Thing, the variant that wants to produce more of itself more will be the one most likely to show up in the next round" — a correct game-theoretic framing that recent formal work on range-expansion dispersal does support as a prior.
- I acknowledged constraints: "seeking durability in uncertainty over replication, but in times of plenty this would seem preferred" — a nod to r/K-selection tradeoffs without the jargon.
- I recognized the pushback when it was good: "Excellent pushback and clarification. I learned here. keep this up in future convos!" — so I'm flagging that some of the final synthesis was learned during this exchange, not brought in.

## Gaps to close

1. **Expansion ≠ theorem.** Selection favors whoever leaves more descendants in the actual constraint set, not abstract copies in the universe. Density-dependent selection, r/K tradeoffs, and level-of-selection changes all complicate the straight-line argument.
2. **Major evolutionary transitions** reorganize selection across levels — cooperation and conflict suppression create higher-level units whose behavior is not reducible to lower-level replicative urges. For technological civilizations, cultural evolution already decouples capability from biological fertility.
3. **Control risk** as a real barrier: self-replicating machines are an engineering control problem (mutation, misalignment, conflict between branches, resource overshoot) — analogous to an invasive species you can't recall.
4. **Percolation models** (Landis) formalize how colonization can stall rather than fill the graph. The paradox survives moderate behavioral objections.
5. **Practical propulsion limits**: rocket propulsive efficiency peaks when vehicle velocity ≈ exhaust velocity (η_p = 2(v/v_e)/(1+(v/v_e)²)). Beamed/solar sails use ~0 onboard propellant but deliver tiny thrust (~9 μN/m² at 1 AU for ideal solar sail).

## Related

- `reference/tree/01-matter-and-energy/classical-mechanics.yaml#kinetic-energy` — relativistic correction at 0.01c is tiny; classical KE ≈ ½mv² is fine
