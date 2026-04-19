---
title: Duke Florida solar net metering and EV charging interaction
created: 2026-04-19
updated: 2026-04-19
tags: [personal]
confidence: 3
confidence_history:
  - date: 2026-04-19
    session_id: "chatgpt-ingest-2026-04-19"
    confidence: 3
    tiers_passed: null
    tiers_available: null
    schema_version: ingest-1
    notes: "Derived from ChatGPT conversations 2025-12-14 'Duke solar credit delay' and 2025-12-24 'End of Year Solar Payout' and 2025-12-14 'Duke Florida electricity rates'. I caught an inconsistency in the assistant's framing of billing-cycle delay and correctly reasoned about year-end true-up mechanics, but a lot of the detail (minimum-bill tariff specifics, COG-1 rate) I was learning from the assistant."
gaps:
  - "Year-end true-up: any unused kWh credits at the Dec cutoff are paid out at wholesale COG-1 rate — typically much lower than retail. Nearly everyone in my area will have some credits cashed out at year-end because AC drives most usage and Dec is cooler."
  - "$30 minimum bill is computed *excluding* the EV charging credit. So EV credit cannot help me avoid the minimum — it applies as a separate line after the minimum-bill test."
  - "Duke TOU schedule is not especially compelling for me: off-peak is close to standard low tier rates, on-peak is above standard high tier. No strong net win for me."
sources:
  - "ChatGPT conversation 2025-12-14 'Duke solar credit delay'"
  - "ChatGPT conversation 2025-12-24 'End of Year Solar Payout'"
  - "ChatGPT conversation 2025-12-14 'Duke Florida electricity rates'"
---

# Duke Florida solar net metering and EV charging interaction

## Summary

My working knowledge of my Duke Florida solar setup: **net metering is a monthly billing-cycle settlement, not a real-time running balance**. Over a billing cycle, net kWh = imports − exports. Net import → charged; net export → kWh credit rolls forward up to 12 months. Credits cash out at wholesale COG-1 at year-end (much less than retail). I still owe the customer charge (~$14.27/month residential RS-1) and the **$30 minimum bill** even in net-export months. The minimum-bill test is computed **excluding** the off-peak EV charging credit — so the EV credit cannot be used to avoid triggering the minimum. Billing cycle is 21st–20th; PTO was 10th.

## Evidence

- I correctly framed the billing mechanics as a *monthly netting* process, not a minute-by-minute wallet, and asked the right diagnostic questions about why "1–2 billing cycle" delay appears after PTO.
- I asked an optimization question — "time EV charging to minimize the number of months I get the minimum. Ideal state would be net minimum months also are very high net export" — which showed I was already holding multiple dimensions (minimum bill, export crediting, EV credit exclusion) in mind.
- I caught an inconsistency when the assistant conflated the billing-cycle-delay storyline with the rule mechanics: "I thought you talked about the 1-2 billing cycle delay changing how credits actually get applied?" The clarification that the delay is an activation artifact, not a permanent rule change, was what I needed.
- I stress-tested a specific numeric scenario: "Month 1: 1,000 kWh use, 1,000 kWh created, 500 covered by solar" — correctly identified that if 500 is self-consumed and 500 is both imported and exported, net kWh = 0 and nothing rolls over. My follow-up Month 2 framing was correct assuming Month 1 had actually been net-export 500.
- I reasoned about end-of-year settlement: "almost everyone in my area will end up getting some amount sold out at wholesale at year end since AC cost is such a large portion of electricity and since December is so pleasant" — correctly identified the structural reason most FL homes with solar will have leftover credits cashed at COG-1.
- I correctly concluded that Duke's TOU rider isn't compelling for me: off-peak is close to standard low-tier, on-peak is above standard high-tier.

## Gaps to close

1. **Net kWh = Imports − Exports**, metered bidirectionally. Self-consumed solar never touches the meter.
2. **Customer charge + minimum bill apply regardless** of net export. RS-1 customer charge is ~$14.27/month; $30 minimum bill kicks in when everything-except-EV-credit would be under $30.
3. **Year-end true-up** pays excess credits at COG-1 (wholesale) rate. Strategic EV charging in sunny months self-consumes rather than banks credits that would cash at wholesale.
4. **Billing cycle mismatch at year-end**: statement ends ~20th of month, not Dec 31. Any Dec 21–Dec 31 net export gets credited then straddle-measured at year-end true-up — worth checking whether it's prorated or a hard cutoff.
5. **EV charging program**: $7.50/month credit with off-peak windows Mon–Fri 10am–6pm and 11pm–5am, weekends all hours. 10am–6pm overlaps with solar production — can stack self-consumption with off-peak credit eligibility.

## Related

- [[estimated-tax-safe-harbor]] — solar credit reduces 1040 line 22, reducing next year's safe-harbor target
