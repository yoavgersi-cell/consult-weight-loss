# 00 — Review synthesis across providers (Trustpilot, Oct 2026)

**Data:** 701 reviews, hand-coded. Details for each provider are in files 04–09, and the coded data in `data/reviews/trustpilot/`.

| Provider | n | Avg ★ (sample) | Invited/Verified share | Invited ★ vs unlabelled ★ | Where it breaks | What 4–5★ reviews mostly rate |
|---|---|---|---|---|---|---|
| Ro | 138 | 3.87 | no labels | — | **Checkout:** membership on top of the medication (66% of 1–2★) | Quick sign-up (81%) |
| Mochi | 84 | (stars not in paste) | 95% | — | Appointments + membership/medication billing split | The consult (76%) |
| WellMedr | 80 | 3.80 | no labels | — | **First order** after a promotion surge (73%); billed every 21 days | A rep who fixed a problem (42%) |
| Embody | 200 | 3.73 | 48% | **4.93 vs 2.66** | **Month-2 refill** (72%) | Felt heard (45%), named rep (32%) |
| TrimRx | 119 | 4.47 | 87% | **4.83 vs 2.12** | **Mid-way through a prepaid plan** | Quick sign-up, support |
| SkinnyRx | 80 | 4.59 | 50% | 4.97 vs 4.20 | **No effect** (esp. oral compounded) + prepaid bundles with no refund | A named phone rep (97%) |

## Seven findings

1. **The star rating depends on when the review is collected.** Each provider asks at its best moment: checkout (Ro), right after the consult (Mochi), after a rep call (Embody, SkinnyRx), after the order (TrimRx), after a fix (WellMedr). None ask at month 3, when most problems happen. Where labels exist, **invited reviews score 2–2.7★ higher than the rest** (Embody, TrimRx).
2. **Reps are actively asking for reviews that name them.** SkinnyRx: a rep's script, "Please be sure to mention my name." WellMedr: a manager calls 1★ reviewers, and one reviewer alleges the company asked them to remove a review. Raw star ratings can't be used as the trust signal on a comparison page.
3. **Each provider breaks at a different stage**, and each stage maps to one field the comparison page should show:
   - all-in monthly cost (membership + medication)
   - billing cycle (every 21 days vs monthly)
   - how to cancel (online / phone only / two subscriptions)
   - refill reliability (share of recent reviews describing late refills)
   - prepay terms and refund policy
4. **Prepaid bundles are the biggest money risk for buyers.** Four of the six providers advertise their lowest price on 3–12-month prepaid plans (TrimRx $1,519, Embody $1,428, SkinnyRx up to $3,588, WellMedr "6+ months"). When a provider fails mid-plan, refunds are refused. **Pay-monthly pricing should be the default.**
5. **The membership surprise comes from the business model.** Ro and Mochi bill a membership and the medication separately, and both get "I thought it was included" complaints.
6. **"Doesn't work" complaints cluster around compounded products**, especially oral or dissolving tablets (SkinnyRx), underfilled vials (TrimRx) and "watered down" (Embody). Compounded oral GLP-1s need their own clear label, separate from the FDA-approved Wegovy pill and Foundayo.
7. **Buyers move between providers, and they say why:**
   - Membership fees push them to flat-price providers.
   - Failed fulfilment pushes them back to brand-name or bigger providers ("going back to Ivim"; "Ro"; "LillyDirect").
   - Transferred doses are often not honoured (Embody, TrimRx, WellMedr).

   This is the "switcher" persona, and it is real and frequent.

## What this changes in the CRO plan

- **Comparison table fields:** add billing cycle, how to cancel, refill reliability, prepay terms with refund policy, and an "FDA-approved / compounded injectable / compounded oral" label.
- **Default price shown:** pay-monthly, all-in, at the dose people stay on.
- **Trust score:** a "real customer score" that weights unprompted reviews and reviews from customers at least 30 days in, ignores rep shout-outs, and counts how often problems happen. Publish the method.
- **Partner management:** ask partners for refund and chargeback rates by plan length, warnings before promotions, and data on customers still active in month 2. Judge partners on retained revenue, not first sign-ups.
- **Compliance due diligence before listing:** review-suppression allegations (WellMedr), checkout defaulting to bigger bundles (SkinnyRx), 21-day billing (WellMedr), FDA warning letters (see `02-competitors.md`).
