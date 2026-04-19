---
title: Dehumidifier vs AC — latent/sensible load and energy penalty
created: 2026-04-19
updated: 2026-04-19
tags: [hvac, physics]
confidence: 3
confidence_history:
  - date: 2026-04-19
    session_id: "chatgpt-ingest-2026-04-19"
    confidence: 3
    tiers_passed: null
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversation 2026-04-10 'PLA Filament Moisture Control'. I pushed back twice on the assistant's framing (80% overestimate → 60% → correct ~25% net whole-house penalty when the AC no longer has to remove the same latent load). Clean HVAC-physics reasoning but the cleanest synthesis came via interactive pushback, not from memory."
gaps:
  - "The whole-house penalty for running a portable dehumidifier instead of letting the AC handle latent load is roughly ~1/COP of the dehumidifier's electricity usage (~25% at COP 4), because the latent duty is shifted to sensible duty, not added on top."
  - "Window-unit AC as a latent-removal tool: only competitive when the room already needs cooling (rejects heat outdoors rather than back into the room). Typical window-unit moisture removal is ~1.4–3.6 pints/kWh vs ~4.6 pints/kWh for a good dedicated dehumidifier."
  - "Glycogen/water and heat-transfer math feel adjacent — both use phase-change enthalpy as the critical term. Water's heat of vaporization (~2.38 MJ/kg at room conditions) is what makes the dehumidifier's in-room heat penalty non-trivial."
sources:
  - "ChatGPT conversation 2026-04-10 'PLA Filament Moisture Control'"
---

# Dehumidifier vs AC — latent/sensible load and energy penalty

## Summary

My working model: a portable dehumidifier running inside a conditioned room is **not** a pure-win over letting the central AC dehumidify. It condenses water and releases both the motor's electrical input **plus** the water's latent heat of vaporization back into the room as sensible heat. But the **cleanest framing** is not "the AC has to remove that extra heat on top of everything." It's: **the dehumidifier shifts what would have been AC latent load into AC sensible load**. Net whole-house penalty of running the dehumidifier is ~1/COP of its own electricity (~25% at COP 4), not ~60–80%.

## Evidence

- I initially flagged the assistant's claim that the AC penalty was "close to 80%" as inconsistent with my intuition that modern HVAC operates near COP 4 (four units heat moved per unit electricity) — implying ~25% penalty. The assistant walked it down to ~60% and offered phase-change latent-heat accounting as the correction (2.38 MJ/kg vaporization + motor input adds ~2.45 kWh of room heat per 1 kWh of dehumidifier electricity → 0.61 kWh of extra AC electricity at COP 4).
- I then pushed the cleaner framing: "doesn't that reduce the amount of latent heat removal the HVAC removes? Like, aside from efficiency loss, HVAC still has same total to take care of because latent heat dropped when sensible heat rose." The assistant conceded this was the right framing and the correct net penalty under apples-to-apples comparison is ~1/COP, i.e., **~25% at COP 4**.
- I asked about conductive envelope heat flow: "decreased heat coming in from outside of the room is materially warmer from the dehumidifier" — asked whether the effect is negligible below ~5°F delta-T differential. The assistant confirmed heat-gain is roughly proportional to delta-T; a 2°F uplift in the room (e.g., 75 → 77) drops conductive gain by ~13%.
- I reframed the window-AC vs dehumidifier question as a first-order efficiency comparison: "comparing the efficiency of the central vs window unit AC to see net energy penalty and then compare that to like penalty of 125% energy of dehumidifier." The assistant confirmed this is the correct structure: `Q_shift × (1/EER_window − 1/EER_central_effective)`. Use EER, not SEER2/CEER, for running-watt comparisons.
- I noted that for my specific upstairs-that-runs-warm use case, the "room needs cooling anyway" condition is met — so the window-unit path has a real chance of beating a dehumidifier on whole-house kWh.

## Gaps to close

1. **Enthalpy of vaporization**: ~2.38 MJ/kg at room conditions → 1 kWh into a good dehumidifier (~2.2 L/kWh) removes ~2.2 kg water, releases ~1.45 kWh of latent heat back into the room → total ~2.45 kWh of heat from 1 kWh of electricity.
2. **Same comparison framed as load shifting**: the room's moisture is the same either way; the dehumidifier converts what would have been AC latent duty into AC sensible duty. Net penalty is mostly the dehumidifier's own kWh, plus a modest AC cleanup term (~25% at COP 4).
3. **Window AC efficiency metric**: use EER (Btu/Wh running), not SEER2 (seasonal) or CEER (includes standby). Central duct losses in unconditioned space can be 25–40%+, which can make a nominally-less-efficient window unit competitive.
4. **Oversized AC doesn't dehumidify well**: short-cycling hits temp setpoint before moisture removal. Lower coil airflow increases moisture removal per pass because coil runs colder relative to air stream.
5. **Filament dry-box feed** is the higher-leverage fix for 3D printing: solves the exposed-spool problem without conditioning a whole room.

## Related

- [[glycogen-water-in-endurance]] — phase-change enthalpy intuition shows up here too
- `reference/tree/01-matter-and-energy/classical-mechanics.yaml#heat-transfer` (related)
