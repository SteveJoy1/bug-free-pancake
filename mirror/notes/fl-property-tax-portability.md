---
title: FL property tax — Save Our Homes portability (Pinellas)
created: 2026-04-19
updated: 2026-04-19
tags: [personal-tax, personal]
confidence: 3
confidence_history:
  - date: 2026-04-19
    session_id: "chatgpt-ingest-2026-04-19"
    confidence: 3
    tiers_passed: null
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversation 2026-02-09 'Pinellas Portability Application'. I applied corporate-side assessment-dispute intuition to residential and caught an internal inconsistency in the assistant's response about whether 2026 Just/Assessed exists yet. Moderate-strong signal, but a lot of this was also Q&A learning."
gaps:
  - "County's 'Just/Market' is the Jan 1 snapshot value, not my closing price. I initially expected sale-price-to-assessment would track proportionally year over year — in practice, ratio can shift based on market movement, comp-set, and sale-specific terms."
  - "Portability reduces the **Assessed Value**, not Just/Market. The Assessed Value gets the Save Our Homes cap differential from the prior homestead transferred to it."
  - "Informal pre-TRIM engagement on residential is evidence-driven (record errors, condition as of Jan 1, pre-Jan-1 comps) — not the 'soft negotiation' that exists in corporate assessment contexts."
sources:
  - "ChatGPT conversation 2026-02-09 'Pinellas Portability Application'"
---

# FL property tax — Save Our Homes portability (Pinellas)

## Summary

My working knowledge of FL residential property tax: three distinct values — **Just/Market** (Jan 1 market estimate), **Assessed** (Just reduced by Save Our Homes cap or portability transfer), and **Taxable** (Assessed minus exemptions). Portability transfers the SOH *assessment difference* from my prior homestead to my new one, reducing Assessed Value — not Just/Market. Pinellas handles this through PCPAO's Exemptions Department (DR-501T for paper filings); March 1 is the annual deadline.

## Evidence

- I noticed that on a prior home my closing price ($276k, 12/14/14) and the following year's Just/Market ($229k as of 1/1/15) did not track proportionally — only 2 weeks between transactions. On my current home the gap is ~2% instead of ~17%. I asked whether a similar "year-after discount" should be expected, showing I'd assumed the relationship was consistent enough to model. The assistant's correction — Just/Market is a Jan 1 mass-appraisal snapshot, not a post-sale discount — is now part of my mental model.
- I applied **corporate tax intuition** to residential: "I've seen on corporate side that it's sometimes easier to nudge for assessment lower before rather than disputing later (not as adversarial). Not a Thing on residential?" Right question — corporate assessment work often has a relationship-driven pre-filing phase that's much weaker in residential.
- I caught an internal inconsistency in the assistant's timeline reasoning about 2026: "Wait, haven't we just said 2026 Just + Assessed doesn't exist yet?" The assistant conceded it had conflated "exists internally" with "exists as a published value."
- I anticipated the right distinction: HOA/private-roads/shared-infrastructure arguments don't directly reduce Just/Market unless I can produce **comp sales** showing homes with my HOA sell for less than comparable homes without. Mass appraisal already accounts for neighborhood factors indirectly.

## Gaps to close

1. **Pinellas timeline for the 2026 roll**: Jan 1 = "as-of" date; by July 1 preliminary values certified to FL DOR; mid-August TRIM notices; 25 days after TRIM = VAB petition window.
2. **Three lanes for a lower assessment** (residential): (1) record errors (SF, quality, features coded wrong); (2) property condition as of Jan 1 (damage, deferred maintenance, documented); (3) pre-Jan-1 comp sales supporting lower Just/Market.
3. **Save Our Homes vs portability vs purchase reset**: assessed value resets to market on the next Jan 1 after change of ownership, then portability/exemptions are applied. SOH cap (currently 3% or CPI-U, whichever lower) kicks in the following year.
4. **DR-501T is the state form** for paper portability filing; online route is through PCPAO's exemption portal.

## Related

- [[estimated-tax-safe-harbor]]
