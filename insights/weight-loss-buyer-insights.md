# Weight-loss (GLP-1) buyer insights: portable brief

**Purpose:** a self-contained summary of what we learned about the online weight-loss medication buyer. Any GLP-1 comparison or treatment hub can use it.

**Built from:**
- 864 buyer reviews and comments:
  - 701 Trustpilot reviews across 6 providers;
  - 163 Reddit comments from 19 threads.
- 88 price reports.
- 32 people who stated their age.
- The r/tirzepatidecompound "Where to Buy" community list.
- Desk research on prices, regulation and competitors.

**Date:** October 2026. Prices and rules change monthly, so re-check before publishing anything.

**Machine-readable numbers:** `data/aggregate.json` in this repo. Rebuild it with `python3 scripts/aggregate.py`.

**Scope:** this file is about the market and the buyer. It contains no client-specific material: no HealthAccess site audit, screenshots or partner card copy.

---

## 1. Bottom lines

1. **The buyer pays out of pocket.** 95% of buyers who say how they pay get no insurance help. The monthly price they see is the price they pay, so it has to be the main number on every card.
2. **Most buyers use the cheaper copy.** 67% of buyers who name a drug are on compounded medication, 24% on brand-name. Typical spend is $138 a month for compounded and $335 for brand-name. Stated budgets stop at $100–$200.
3. **Tirzepatide is the favourite.** 74% pick it when asked to choose one drug.
4. **The top need is a human who answers** (35% of everything buyers wrote). Online clinics rarely put a person in front of the buyer, so proof of a reachable human is a differentiator.
5. **Complaints come after month 1, not at sign-up.** The top complaints are nobody to call (35%), running out of medication / late refills (31%), feeling trapped by prepay, cancelling or refunds (30%), and being overcharged (28%).
6. **Star ratings mislead.** Invited reviews score up to 2.7★ higher than unprompted ones. Experienced buyers don't trust Trustpilot; they trust community lists and surveys.
7. **The audience is mixed by stage:** 31% first-timers, 21% switching providers, 46% already 3+ months in. Each group needs a different first screen.
8. **The intro price is the enemy.** "$39 first month" headlines create the "overcharged" complaint. Show the price at the dose people stay on.
9. **Buyers judge legitimacy by the pharmacy.** Experienced buyers compare the named pharmacy (503A/503B), the 28-day rule and refill type, as the community list does.
10. **Older buyers are real.** The median stated age is 48, and 25% are 65+. Medicare has paid $50 a month for originals since July 2026.

---

## 2. The average buyer

| | |
|---|---|
| **One line** | Most often a woman around 48, paying out of pocket, on compounded tirzepatide at about $138 a month. Wants one honest price and a human who answers. |
| **Sex (where stated)** | 78% women |
| **Age (where stated)** | median 48 · <40: 22% · 40–49: 34% · 50–64: 19% · 65+: 25% |
| **Weight lost so far (where stated)** | median about 24% of starting weight |
| **Pays** | 95% out of pocket |
| **Medication** | 67% compounded, 24% brand-name, 8% gray market |
| **Prefers** | tirzepatide, 74% |
| **Why they switch** | losing or being denied insurance, then price, then poor results, then membership fees |

### Where they are in the journey (all sources combined)

| Stage | Share | What they need first |
|---|---|---|
| First-timer | 31% | reassurance, how it works, cost in month 1 vs month 4, a real clinician, no judgment, pill options |
| Switching | 21% | keep my dose, a lower all-in price, someone who answers, a fast first shipment |
| 3+ months in | 46% | price at the maintenance dose, 3-month plans, a named pharmacy, reliable refills, no lock-in |
| Restarting | 1% | low starting dose, no judgment, a price they can keep paying |

### What they want, as a share of all reviews and comments

| Need | Share |
|---|---|
| A human who answers | 35% |
| A price they understand | 20% |
| An easy, fast start | 19% |
| Medication on time | 18% |
| Being heard, not judged | 16% |
| That it works and is safe | 15% |
| Control over money (cancel, refunds) | 11% |
| Keeping their dose / drug type | 6% |

### What they fear, as a share of complaints and worries

| Fear | Share |
|---|---|
| Nobody to call | 35% |
| Running out of medication | 31% |
| Being trapped (prepay, cancel, refunds) | 30% |
| Being overcharged | 28% |
| Scam / doesn't work | 24% |
| Side effects | 9% |
| Being judged | 2% |
| Regaining weight | 2% |

---

## 3. Prices people actually pay (monthly)

| Channel | Median | Middle half |
|---|---|---|
| Compounded via an online clinic | $138 | $109–$169 |
| Brand-name, out of pocket | $335 | $299–$450 |
| Gray-market "research peptides" | $18 | $8–$31 |
| Community "Where to Buy" list (3-month plans) | $166 | $100–$200 range |

Stated budgets cluster at $100–$200 a month.

**Community list benchmark (how experienced buyers compare):**
- price per 3 months;
- the named pharmacy, 503A or 503B (50% are 503B);
- whether the plan follows the 28-day rule (95% do);
- additives;
- beyond-use date;
- states served (only 25% ship everywhere);
- auto or manual refill (71% auto).

---

## 4. Industry primer, in plain words

- **The medicine:** GLP-1 drugs reduce hunger. Most are a weekly injection; two are daily pills.
- **Originals (brand-name):** made by the inventors, **Novo Nordisk** and **Eli Lilly**. They're FDA-approved, trial-tested and identical in every pack.
  - Semaglutide: **Wegovy**, Wegovy pill (Ozempic is the diabetes name).
  - Tirzepatide: **Zepbound** (Mounjaro is the diabetes name).
  - Orforglipron: **Foundayo**, a pill since April 2026.
  - Prices without insurance: pills from $149; injections $299–$449.
- **Copies (compounded):** a compounding pharmacy mixes its own version from the same main ingredient.
  - It's not FDA-approved and has no trials of its own.
  - Quality varies by pharmacy. Some add B12, or sell it as drops, pills or "gum".
  - It costs about $100–$300.
  - It isn't a "generic": no approved generic of Wegovy or Zepbound exists yet.
  - It was allowed during the 2022–2024 shortages. Those ended in late 2024 (tirzepatide) and early 2025 (semaglutide), so it's now a legal gray zone, and the FDA sent warning letters to 55+ firms in 2026.
- **Gray market:** "research peptides" such as retatrutide, sold "not for human use" with no prescription, for $10–$35. Unsafe. Never list them; answer them with "cheapest legal options".
- **Who does what:** drug company (makes it) → pharmacy (fills and ships it; a compounding pharmacy also makes copies) → online clinic (prescribes and sells) → comparison site (helps the buyer choose and is paid per sign-up or lead) → buyer.
- **What an online clinic is:** a website and app, contracted clinicians (often from a doctor network, rarely met), and a partner pharmacy. Approval is usually a form with no call, often the same day. Some states require a video or phone visit.
- **Four routes to the drug:**
  1. online clinic;
  2. own doctor and a local pharmacy (the insurance route, with prior authorization);
  3. straight from the maker: LillyDirect or NovoCare, which still need a prescription;
  4. the gray market, with no doctor.
- **Who pays:**
  - Compounded: insurance never pays.
  - Brand-name for weight loss: sometimes, with prior authorization. Many requests are denied; about 62% of claims were rejected in 2021–24.
  - Diabetes uses: usually covered.
  - Medicare: $50 a month (GLP-1 Bridge, Jul 2026 – Dec 2027).
  - With a maker's savings card and coverage: $25–$50 a month.
- **Provider types:**
  - brand-name telehealth: Ro, Hims & Hers, WW Med+, Amazon One Medical;
  - compounded telehealth: Embody, TrimRx, WellMedr, MEDVi, SkinnyRx, Trimi, Refills;
  - mixed: Found, Noom, Mochi;
  - maker-direct: LillyDirect, NovoCare, TrumpRx;
  - gray market.
- **Pricing models and what trips buyers up:**

  | Model | Example | What trips buyers up |
  |---|---|---|
  | Membership + drug | Ro: $149 + drug | Reading "$39 first month" as the price |
  | All-in flat price | Embody: $129 at any dose | Late refills |
  | Intro price, then higher | MEDVi: $179, then $299 | The month-2 jump |
  | Prepaid bundle | TrimRx: $1,519 for 6 months | No refund if the provider fails |

- **Trends 2025–26:**
  - brand prices fell;
  - pills launched;
  - compounded crackdown;
  - Medicare at $50;
  - tirzepatide preference;
  - microdosing and maintenance;
  - buyers shopping with ChatGPT and Reddit;
  - gray-market temptation.

---

## 5. What a comparison page must show (the blueprint)

**Six rules**
1. Sell the real price, not the starting price.
2. Show what happens after month 1: refills, cancelling, refunds.
3. Prove there's a human.
4. Answer "is this safe and legit?": FDA-approved vs compounded, and the named pharmacy.
5. Route by stage, not one list for everyone.
6. Be more transparent than the community list, and don't lean on raw stars.

**Page order**
1. Trust bar: prices verified [date], how we rank, disclosure.
2. Hero: "Compare by what you'll really pay", plus 3 bullets that answer overcharged, trapped and scam.
3. Stage question: "Have you taken a GLP-1 before?" (first time / switching / 3+ months / stopped).
4. Filters: FDA-approved / compounded / both; budget $100 / $150 / $200 / $300+; no membership; insurance / Medicare.
5. Provider cards, sorted by all-in price at the maintenance dose.
6. True-cost widget: month 1 vs month 4 vs year one.
7. Safety checklist: licensed in your state, named pharmacy, real clinician names, cancel online, refund terms.
8. Stage guides.
9. Method, verification and FAQ.

**Provider card, in priority order**
1. All-in monthly price at the maintenance dose (paying monthly and 3-month), with "starts at" underneath.
2. Drug and type label: FDA-approved / compounded injection / compounded oral.
3. Named pharmacy and type.
4. Itemised fees: membership, consult, shipping, dose-change price.
5. Cancel and refund terms.
6. Support style and reply time.
7. Dose transfer and refill type.
8. States not served.
9. A "Best for…" label, and a survey or unprompted score instead of raw stars.

**If the card layout is fixed** (offer line + ✓ bullets + one highlighted bullet), fill the slots like this:
- offer line: the regular monthly price first, then the promo;
- ✓ what it is, labelled FDA-approved or compounded;
- ✓ what's included;
- ✓ billing and cancelling;
- ★ the one real differentiator.

---

## 6. Copy rules

- **Use the buyers' words:**
  - real person
  - one price
  - no hidden fees
  - same price every dose
  - cancel anytime
  - ships in 2–3 days
  - no judgment
  - keep my dose
  - FDA-approved
  - food noise
- **Avoid:**
  - "from $X" as the headline
  - "#1 rated"
  - "generic Wegovy" or "same as Ozempic"
  - "guaranteed approval"
  - before/after photos
  - urgency tricks
  - "results backed by clinical trials" for compounded products
- **Compliance:**
  - Label every option FDA-approved or compounded.
  - Show the maintenance price, not only a starter price.
  - Say "a licensed clinician decides".
  - Compare like-for-like doses.
  - Date-stamp prices.
  - Drug-name keyword bidding on Google needs healthcare certification; LegitScript certifies price-comparison sites.

---

## 7. Articles to write (each backed by the data)

**Write first**
1. What will I really pay? Month 1 vs month 4 vs year one *(price clarity, 20%)*
2. Compounded vs brand-name vs pills: what's FDA-approved *(works and safe, 15%)*
3. Is this GLP-1 provider legit? A 5-point checklist *(scam fear, 24% of complaints)*
4. Before you prepay: 5 questions about refunds and cancelling *(trapped, 30%)*
5. New to GLP-1s? The first 4 weeks *(first-timers, 31%)*

**Next**
6. Switching providers without restarting your dose *(switching, 21%)*
7. Cheapest legal GLP-1 options, and why research peptides are risky *(gray-market median $18)*
8. What $100–$200 a month gets you
9. Why refills arrive late, and how to pick a provider that ships on time *(running out, 31%)*
10. How to cancel [provider], step by step
11. Lost coverage for Zepbound or Wegovy? Your next options *(the #1 switch reason)*
12. Tirzepatide vs semaglutide: which people pick *(74% tirzepatide)*

**Later**
13. GLP-1s after 65: Medicare's $50 option *(25% of stated ages are 65+)*
14. 503A vs 503B and the 28-day rule
15. How we rate providers, and why stars mislead *(2.7★ invited vs unprompted gap)*
16. Microdosing explained
17. Stopping GLP-1s: will the weight come back?

---

## 8. Provider signals (public Trustpilot, coded)

| Provider | Average ★ | Invited ★ | Unprompted ★ | Top complaint (share of 1–2★) | When it breaks |
|---|---|---|---|---|---|
| Embody | 3.7 | 4.9 | 2.7 | refills not shipped (72%) | month 2 |
| TrimRx | 4.5 | 4.8 | 2.1 | support silent (62%); prepaid plan not delivered | months 3–7 |
| SkinnyRx | 4.6 | 5.0 | 4.2 | "doesn't work" (71%) | checkout upsell / over months |
| Ro | 3.9 | – | – | membership fee surprise (66%) | checkout |
| WellMedr | 3.8 | – | – | orders/refills not shipped (73%) | months 0–1 |
| Mochi | – | – | – | appointment no-shows (40%) | months 0–1 |

---

## 9. Caveats

- **Sample bias:**
  - Trustpilot leans toward new sign-ups (invited reviews at checkout).
  - Reddit leans toward experienced buyers of compounded drugs.
  - Shares are pooled counts across both, not averages of percentages.
- **Small samples:** demographics are based on 32 stated ages and 23 stated sexes. Treat them as directional.
- **Payment bias:** the 95% out-of-pocket figure leans toward buyers of compounded drugs. Search traffic likely includes more insured people. Ask a quiz question ("How will you pay?") to get the real split for your own site.
- **Freshness:** prices are snapshots from Mar–Oct 2026, and regulation is moving. Re-verify before publishing.
