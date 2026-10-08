# 04 — Review analysis: Embody (Trustpilot, sample of 200)

**Source:** the user pasted 200 recent Embody (joinem.co) Trustpilot reviews, posted roughly Oct 4–7, 2026.
**Method:** each review was coded by hand for star rating, how the review was collected, and complaint/praise themes. Reviewer names were not stored.
**Files:**
- `data/reviews/trustpilot/embody_coded_2026-10-07.csv` — the coded data
- `scripts/review_stats.py` — the script that computes the numbers below

**Caveats:**
- This is one provider over about four days, so it is a snapshot, not a trend.
- The coding is a single analyst's judgment.
- One review had no visible star rating and was coded as 1★ from its text.

## Headline numbers

| How the review was collected | n | Avg ★ | 5★ | 1–2★ |
|---|---|---|---|---|
| **Invited by Embody** (sent after an appointment or call) | 87 | **4.93** | 94% | **0%** |
| Verified | 9 | 4.56 | 89% | 11% |
| **Written unprompted** | 104 | **2.66** | 38% | **58%** |
| All | 200 | 3.73 | 64% | 30% |

**The main finding:** Embody's Trustpilot score is propped up by invited reviews. Embody sends an invitation right after a good moment, usually the first consult or a call with a rep. Those reviews rate that one interaction. The unprompted reviews describe the actual service, and 58% of them are 1–2★.

One reviewer said it directly: *"That is what I'm rating the 5 stars on, not my overall Embody experience."*

## What drives 1–2★ reviews (n=61)

| Theme | Share of negative reviews | What it sounds like |
|---|---|---|
| **Refill not shipped / missed doses** | **72%** | "first month is good after that good luck" · "Day 19 and counting" · "18 days, no shots" · "I'll pay 12 months of subscription and get about 8 months of medication" |
| **Charged with no product / refund refused / cancel ignored** | 54% | "charged me again even after you told me you processed my cancellation" · "NO REFUNDS" · told to dispute with their bank |
| **Support makes promises but nothing happens** | 49% | "Five separate calls. Five assurances… Zero follow-through" · the same canned reply every time |
| Provider didn't show / appointment problems | 16% | consult calls went to voicemail; every booking slot "unavailable" |
| **Dose problems** (non-standard strengths, transferred dose not honoured) | 13% | "Embody is 6.3 when I should be on 7.5" · "will NOT honor… if you are already at a certain dose" |
| Doesn't work / "watered down" | 10% | "Did not curb my appetite at all" · "hungrier than on the previous supplier" |
| Switched in or wants to leave | 10% | switched from LillyDirect or another provider to save money; now "trapped" |
| Side effects or unsafe dosing | 8% | dose "tripled" on switching to tirzepatide; vomiting |
| Locked into a prepaid plan | 7% | paid $1,400 for 12 months upfront, then no consult and no refund |
| Checkout add-on traps | 7% | "10+ add-ons… no way to remove it from the cart" (NAD+, B12, glutathione) |
| Cold chain broken | 7% | "The ice was completely melted & the medication was warm" |

## What drives 4–5★ reviews (n=134)

| Theme | Share of positive reviews |
|---|---|
| **Felt heard by the clinician** ("listened", "felt seen, not judged") | 45% |
| **A named rep** (Jayvee, Miguel, Marie, Norman, Percy, Dane…) | 32% |
| Quick and easy appointment | 16% |
| Weight-loss results mentioned | 3% |
| Price mentioned | 1% |

Almost no positive review mentions getting the medication on time or seeing results. The praise is about how people felt in a conversation.

## What this means for HealthAccess

1. **Raw Trustpilot stars mislead in this vertical.** Embody shows about 3.7 overall (the competitor report found 3.6), but its unprompted score is 2.7. A comparison page that shows raw stars sends people to providers like this, and the result comes back as refunds, chargebacks and damage to our own brand. **Build a "real customer score"** that separates invited from unprompted reviews and weights recency. This is concrete evidence for the composite trust score in the roadmap.
2. **The thing that matters most is month 2, not month 1.** The top complaint is refill reliability. Every provider's first shipment arrives fast; the second one is where they fail. Nobody measures this. A "refill reliability" signal (share of recent reviews mentioning a late refill) is a column no competitor has.
3. **The cheapest providers go after the price-driven switcher, then let them down.** Embody's $79/$129 compounded price pulls people away from LillyDirect and other providers ("I was so excited to pay less… I guess you get what you pay for"). Several then went back to their old provider and paid more. This supports two things:
   - the "keep your dose" switching feature, with a check that the provider actually honours a transferred dose;
   - showing compounded, cheaper options next to the brand option they would be leaving.
4. **Partner risk.** If Embody is a HealthAccess partner, expect high refunds and chargebacks after month 1. Revenue should be judged on **retained or month-2 conversions**, not first sign-up. Ask for partner reversal and chargeback data.
5. **Copy cues from the positive side:** "feel heard", "a real person who knows your name", "not judged". Good material for trust copy, but only where the provider actually delivers it.
6. **Compliance flags to watch for in any compounded partner:**
   - non-standard strengths (6.3 mg, 17 mg)
   - large dose jumps on switching
   - add-on checkouts with no way to remove items
   - no refunds on prepaid plans

   These are FTC-type pricing and consumer-protection risks that could reach the comparison site's brand too.

## Seed quotes (verbatim from this paste)

- "They are very good at getting you your first dose after that their good at billing you for refills while it sits at the pharmacy."
- "I was so excited to pay less than what I have been paying with the other brand I use, but I guess you get what you pay for."
- "If the pharmacy is that backed up I should have been notified before I paid, not after I paid and then say you can't get a refund."
- "DON'T Switch from another company to them… This company will NOT Honor or consider if you are already at a certain dose."
- "I want to send you $300 a month and you send me medicine on time."
- "I felt seen. Not judged."
- "My experience today with the provider and RN were great. That is what I'm rating the 5 stars on not my overall Embody experience."
