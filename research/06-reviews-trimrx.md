# 06 — Review analysis: TrimRx (Trustpilot, 119 reviews)

**Source:** the user pasted TrimRx Trustpilot reviews, posted roughly Oct 2–7, 2026.
**Method:** hand-coded the same way as Embody and Ro. On Trustpilot, the "Verified" label means TrimRx sent the review invitation through its own order system, so it is treated here as an invited review.
**Files:**
- `data/reviews/trustpilot/trimrx_coded_2026-10-07.csv` — the coded data
- `scripts/review_stats.py` — the script that computes the numbers below

## Headline numbers

| How the review was collected | n | Avg ★ | 5★ | 1–2★ |
|---|---|---|---|---|
| **Verified** (invited by TrimRx) | 103 | **4.83** | 93% | 4% |
| **Written unprompted** | 16 | **2.12** | 25% | **75%** |
| All | 119 | 4.47 | 84% | 13% |

87% of all reviews are invited. That share, not the service, is what produces the 4.5★ headline. The unprompted sample is small (16), so treat its average as a direction, not a precise number.

## Where TrimRx breaks: partway through a prepaid plan

**5 of the 12 unprompted 1–2★ reviews describe the same failure.** The customer prepaid for 6 or 12 months and received the first half. Then the second shipment never arrived and support stopped answering.

- "I paid for a 6-month plan… getting close to the end of my initial 3-month supply… Their lovely AI chatbot… I have yet to receive any response."
- "I prepaid for a year… received two of four shipments… the third shipment was due around September 15 and they still have not shipped it."
- "I was charged $1519 on June 16… When it came time for the second part of my subscription… no response."
- "They took my $1519 and did not send the product… they will not refund you."

**Other negative themes:**
- Support goes silent or is only a chatbot: 62% of 1–2★ reviews.
- Refund promised but not paid: 31%.
- Underfilled vials or "placebo"-like effect: 19%.
- Side effects: 19%.

## What 4–5★ reviews say (n=102)

| Theme | Share |
|---|---|
| Quick, easy sign-up | 39% |
| Responsive support | 29% |
| Fast shipping | 23% |
| Price is good / no membership | 22% |
| Results | 13% |
| "Too early to tell" | 10% |

**Pattern worth watching (not verifiable):**
- The positive reviews are unusually uniform. Almost all come from accounts with a single review, and they are written in polished, complete sentences.
- 9 of them repeat TrimRx's price message almost word for word: "one amount", "no second subscription", "the amount at checkout matched what was advertised", "no separate membership fee". That is the exact attack line against membership providers like Ro.
- These could be genuine, or the invitation flow could be prompting them. Either way, do not take the star score at face value.

## Competitive notes from switchers

- "I switched after an order I placed with **Mochi** on April 3 sat there with no medication showing up." This adds a fulfilment complaint about Mochi.
- "My last provider charged about twice as much and **added a separate doctor fee every month**." Annoyance with membership fees drives switching.
- "I had already been taking this medication for years, so **starting on a different dose** was frustrating." TrimRx also doesn't fully honour a transferred dose, the same as Embody.

## What this means for HealthAccess

1. **Prepay and commitment terms must be in the comparison table.** Two of the three providers reviewed so far fail around a long prepaid plan (TrimRx: $1,519 for 6 months; Embody: $1,428 for 12 months). If the provider fails partway through, the buyer loses that money. Show "Pay monthly" vs "Prepay N months", and do not feature prepay bundles as the headline price.
2. **The gap between invited and unprompted reviews is now confirmed across providers.** Embody: 4.93 vs 2.66. TrimRx: 4.83 vs 2.12. In this vertical, the star score mostly reflects how many reviews the provider invited. The real customer score should use unprompted reviews and reviews from customers at least 30 days in.
3. **Flat pricing with no membership is a real draw**, and it is the main reason people switch. Show it as a filter ("No membership fee"). Pair it with the reliability signals, because low-price providers are where fulfilment fails.
4. **Partner economics:** if TrimRx is a partner, prepaid bundles inflate first-order revenue. Chargebacks arrive months later, after the payout window. Ask partners for reversal rates by plan length.

## The three providers side by side

| | Ro | Embody | TrimRx |
|---|---|---|---|
| Model | Brand drugs + membership | Compounded, low monthly price | Compounded, flat price, prepay bundles |
| Where it breaks | **Checkout** (month 0): membership surprise | **First refill** (month 2): not shipped | **Halfway through a prepaid plan** (months 3–7): second half not shipped |
| Top 1–2★ theme | Membership surprise, 66% | Refill not shipped, 72% | Support silent, 62%; prepaid plan not delivered, 42% of unprompted negatives |
| Invited vs unprompted ★ | n/a (no labels in paste) | 4.93 vs 2.66 | 4.83 vs 2.12 |
| What the comparison page should show | All-in monthly cost | Refill reliability | Commitment and prepay terms, and refund policy |
