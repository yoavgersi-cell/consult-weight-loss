# 08 — Review analysis: WellMedr (Trustpilot, 80 reviews)

**Source:** the user pasted WellMedr Trustpilot reviews, posted roughly Oct 1–7, 2026. One reviewer says the company appears to have renamed itself "Welldoc". That is unverified, but worth checking before listing the company.
**Method:** hand-coded for star rating and themes. This paste carries no "Verified" or "Invited" labels.
**Files:**
- `data/reviews/trustpilot/wellmedr_coded_2026-10-07.csv` — the coded data
- `scripts/review_stats.py` — the script that computes the numbers below

## Headline numbers

- Average **3.80★** across 80 reviews. 57% are 5★ and 28% are 1–2★.
- **1–2★ reviews (n=22):**
  - first order or refill not shipped: **73%**
  - no response from support: 64%
  - billing errors (double charges, charged after cancelling, promo price not applied): 55%
- **4–5★ reviews (n=57):**
  - **67% praise a named rep** (Rob, Autumn, Tobias, Victoria, Ryan Harlow…)
  - **42% describe a problem that a rep then fixed**
  - **8 were raised after the reviewer was contacted**, usually from 1★ to 4–5★

## Where WellMedr breaks: a promotion it couldn't fulfil

Several reviewers relay what the company told them: *"the recent fall sale increased buyer engagement and sales volume considerably… personnel staffing didn't increase as fast"* and *"Apparently their volume has increased massively, shutting down their system for several days."* As a result:
- Orders sit in "processing" or "pending provider review" for 1–3 weeks.
- People are double-charged, or the promised discount wasn't applied. One reviewer was charged $646.99 when the promotion said "$150 off… automatically applied."
- They can't reach a human: "Communication is by a bot."

**Billing patterns to flag:**
- **"Monthly" plans billed every 21 days.** "While their pricing is advertised as monthly it's actually every three weeks while shipment of product is monthly." Another reviewer said the same.
- **The headline price applies only to prepaid plans:** "the advertised pricing was only for an extended 6+ month purchase." This is the same prepay-as-headline pattern as TrimRx and Embody.
- **Cancelling requires a phone call:** "They make it hard to cancel as you must call them to do so."
- **Aggressive sales calls after intake:** "they have called me 10 times… He then read my weight from the intake form." This is also a sensitive-data and tone problem.

**Review-handling flag (an allegation, not verified):** one reviewer says *"a wellmedr employee assured me that my medication would be expedited to me if I took down the review."* If true, this would fall under the FTC's 2024 rule on consumer reviews, which bans suppressing reviews. Note it, don't repeat it publicly, and raise it in partner due diligence.

## What's distinctive: recovering bad reviews

A senior contact ("Rob in operations") phones people who leave 1★ reviews, explains the growth problems, issues refunds, and many reviewers then raise their rating. That's good service recovery. But it means WellMedr's star rating reflects **how well it handles complaints after they're posted**, not how often orders arrive on time. The same is true of the many 5★ reviews that open with "I was frustrated… then [rep] fixed it."

## What this means for HealthAccess

1. **Add a "billing cycle" field.** Every 21 days vs every 28–30 days changes the true yearly cost by about 45%. A $99 "monthly" charge billed every 21 days comes to about $1,720 a year, not $1,188. The true-cost calculator should take billing frequency as an input.
2. **This is the third provider where the headline price is a prepay price** (TrimRx, Embody, WellMedr). Show prices on a pay-monthly basis by default, with prepay as an option.
3. **Watch partners during their promotions.** When a partner runs a big sale, sending them more traffic can push them past what they can fulfil, and those buyers then fail. Ask partners to warn ahead of promotions, and watch reviews for complaints of late shipping during them.
4. **Score providers on fulfilment and billing problems, not complaint handling.** WellMedr shows a provider can raise its rating by recovering complaints after they're posted. The real customer score should count *how often problems happen* (e.g. the share of reviews mentioning late shipping or billing errors), not just the final star rating.
5. **Partner due diligence:** check the rebrand, the review-suppression allegation, and the 21-day billing before listing or continuing to list.

## The five providers compared

| | Ro | Mochi | Embody | TrimRx | WellMedr |
|---|---|---|---|---|---|
| Where it breaks | Checkout: membership surprise | Appointments + billing split | Month-2 refill | Mid-way through a prepaid plan | First order after a promotion surge; 21-day billing |
| Top 1–2★ theme | Membership 66% | Appointments 5/15 | Refill 72% | Support silent 62% | Not shipped 73% |
| What 4–5★ praise | Quick sign-up | The consult | Felt heard, named rep | Quick sign-up | **Named rep who fixed a problem** (42%) |
| Field the page needs | All-in cost | How to cancel | Refill reliability | Prepay terms | **Billing cycle** + how to cancel |
