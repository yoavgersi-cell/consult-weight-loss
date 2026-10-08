# 07 — Review analysis: Mochi Health (Trustpilot, 84 reviews + profile data)

**Source:** the user pasted pages 1–4 of Mochi's Trustpilot listing on Oct 7, 2026. That gives 80 reviews, plus 4 from the "reviews shaping this summary" box.
**Limitation:** star ratings for individual reviews were not in the paste. Each review is coded **pos / mixed / neg from its text**, and star figures below come from Mochi's profile.
**Files:**
- `data/reviews/trustpilot/mochi_coded_2026-10-07.csv` — the coded data

## Profile facts (Trustpilot, Oct 7, 2026)

- 19,180 reviews in total, rated 4.5. **6,007 in the last 12 months.**
- Star mix: 5★ 81%, 4★ 5%, 3★ 3%, 2★ 2%, **1★ 9%**. Ratings cluster at the top and bottom with little in between.
- Profile labels: "Asks customers to review", "Paid Trustpilot subscription", "Replied to 99% of negative reviews", "May use AI-assist with replies".
- The company's own "About" text includes: "If you're already a Mochi Health member, leave us a review!"

## What the sample shows

| | |
|---|---|
| Share of reviews labelled Verified (invited) | **95%** (80 of 84) |
| Share describing a **provider visit** (consult or coach call) | **76%** |
| Share mentioning delivery, refills or results at all | 10% (8 of 84) |
| Sentiment | 69 positive · 5 mixed · 10 negative |

**The main finding:** Mochi sends a review invitation right after each clinician visit. Its Trustpilot score therefore mostly rates **the video consult**, which Mochi does well. It barely covers the rest of the journey: pharmacy, refills and billing. One reviewer in this sample was already worried about that part: *"I'm just praying that my delivery from the pharmacy is as smooth as I have read some horror stories."* A TrimRx reviewer had also switched away from Mochi after an order "sat there with no medication showing up."

## Negative and mixed themes (n=15)

| Theme | Count | Example |
|---|---|---|
| **Appointment problems** (no-show, late, no meeting link) | 5 | "the doctor didn't show up… I've spent money for the membership… and gotten nothing in return" · "Nutritionist did not show up" |
| **Membership vs medication billing** | 4 | "I thought i was paying 6 months of GLP's… spending 275.00 for dr services" · "I thought the first month was free?" |
| Unhelpful consult | 3 | "The dr seems very indifferent" · "didn't talk to me about my choices" |
| Auto-renewal after a policy change | 1 | "sent only an email and then automatically took the subscription and medication out of my bank account… I had to come off the medication" |
| Provider changed without notice / history repeated | 1 | |
| Cold chain | 1 | "NOT delivered in refrigerated packs" |

**Mochi's own replies confirm the billing structure:**
- "Our platform separates the health membership… from the medication subscription, which is billed separately."
- "Our billing process includes automatic renewal unless a cancellation is submitted for each component."

That means **two subscriptions, each of which must be cancelled separately.**

## What positive reviews praise

- A clinician who listens and doesn't judge. One reviewer: *"She did not make me feel ashamed of my very slow progress."* Another: *"My goals weren't safe for my weight and age and she helped me pivot."*
- Named clinicians and coaches: Mahala, Trisha, Dr. Lewis, Jane and others.
- Price: "the cheapest around"; "The prices went down, which is a huge benefit."
- A few long-term members mention reliability: "Billing and shipping are consistent" and "two years now".

## What this means for HealthAccess

1. **The membership surprise comes from the business model, not from Ro alone.** Ro and Mochi both bill a membership plus a separate medication subscription, and both get the same complaint. The all-in price column and a "Membership: Yes / No + cost" field apply to every membership provider.
2. **Show cancellation steps.** Mochi requires two separate cancellations. Add a "How to cancel" field to each provider: one click, two subscriptions, or phone only.
3. **When a review is collected tells you what it measures.** Mochi collects after the consult, Ro at checkout, Embody after calls, TrimRx after the order. None of them collect at month 3. A real customer score must weight reviews by **how far into treatment** the reviewer is, and the methodology page should say so.
4. **Mochi's real strength is clinical care.** For "nervous first-timer" and "midlife / menopause" buyers, Mochi's clinician experience is a fair "Best for clinician support" label. Pair it with an honest note on billing structure and cancellation.
5. **Gaps to fill:** the profile's 9% 1★ share likely hides fulfilment complaints that these pages didn't capture. To see them, paste Mochi's reviews filtered to 1★ and 2★, or the unprompted ones.

## The four providers compared

| | Ro | Mochi | Embody | TrimRx |
|---|---|---|---|---|
| Model | Brand + membership | Membership + compounded or brand subscription | Compounded, cheap monthly | Compounded, flat, prepay bundles |
| When reviews are collected | At checkout | Right after the consult | After calls | After the order |
| Share invited | n/a | **95%** | 48% | 87% |
| Where it breaks | Checkout: membership surprise | Appointments + the membership/medication billing split | Month-2 refill | Mid-way through a prepaid plan |
| Field the page needs | All-in cost | All-in cost + how to cancel | Refill reliability | Prepay terms + refund policy |
