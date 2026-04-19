---
title: Momentum
created: 2026-04-19
updated: 2026-04-19
tags: [classical-mechanics, physics]
confidence: 2
gaps:
  - "Key confusion: applied kinetic-energy conservation to an inelastic collision, where only momentum is conserved."
  - "Inelastic-collision formula: v_final = (m1·v1 + m2·v2) / (m1 + m2), linear in velocities."
  - "F = dp/dt form of Newton's second law and why it is more general than F = m·a (variable mass, relativistic limit)."
  - "Self-rated 4 (solid) on a wrong answer — calibration to watch."
sources:
  - "quiz session 2026-04-19T01:01:35Z (momentum.q2 wrong, momentum.q3 skipped)"
---

# Momentum

## Summary

Some engagement with the canonical inelastic-collision problem, but with a fundamental mix-up: answered `sqrt(400 · 1500 / 2500) ≈ 15.5 m/s` on momentum.q2, which is the **kinetic-energy** answer — KE is *not* conserved in inelastic collisions. Momentum is. The correct answer: (1500)(20) = 2500·v → **v = 12 m/s**. Also skipped the F = dp/dt generality question.

## Gaps to close

1. **Momentum is conserved in all collisions; kinetic energy is only conserved in elastic ones.** Inelastic = some KE → heat, sound, deformation.
2. **Inelastic collision formula** (stick together): `v_final = (m1·v1 + m2·v2) / (m1 + m2)`. It's linear in v — no square root.
3. **F = dp/dt** is more general than F = m·a because:
   - It handles variable-mass systems (e.g., a rocket expelling fuel — mass changes with time).
   - It carries over to relativistic mechanics, where F = m·a breaks down.
4. **Self-calibration**: rating a wrong answer 4/5 suggests over-confidence on collision problems. Worth flagging for re-quiz.

## Related

- [[conservation-of-momentum]]
- [[kinetic-energy]]
- [[newtons-laws-of-motion]]
- `reference/tree/01-matter-and-energy/classical-mechanics.yaml#momentum`
