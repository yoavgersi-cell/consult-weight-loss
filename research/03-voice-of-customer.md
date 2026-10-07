# 03 — Voice of Customer: Online GLP-1 Buyer (Seed Version)

*Prepared 2026-10-07 for CRO work on a US weight-loss comparison site that sends paid-search traffic to telehealth GLP-1 providers. This is a baseline persona model built from public sources. It is meant to be replaced or validated with the client's raw Reddit and Trustpilot exports.*

---

## 0. Method, source limits, and confidence

- **Sources used:** WebSearch (standard and extended) over public polls (KFF, Gallup, Axios-Ipsos), industry surveys (Rock Health/Evidation, Veru, Tebra), news coverage (NPR, KFF Health News, CNBC, Fierce, Axios), regulatory coverage (FDA warning letters, 503B proposal), Trustpilot/BBB/ConsumerAffairs summaries, and third-party review aggregators that quote Reddit and Trustpilot.
- **Access limits:** reddit.com, trustpilot.com (all country mirrors), kff.org, goodrx.com and the Reddit archive APIs were **blocked** by the egress proxy and by the search provider (reddit.com cannot be used as a search domain). WebFetch failed on every target tried. All findings therefore come from **search-result snippets and secondary coverage**. Verbatim quotes below are reproduced as the search engine returned them from the cited page. Treat them as *seed quotes*: check each one against the client's raw export before using it in ad copy.
- **Trust caveat on Trustpilot:** several GLP-1 telehealth pages carry very high scores (4.5–4.8) next to F/B BBB ratings, and Trustpilot has put fraud or suspicious-review banners on at least one (Henry Meds) ([consumer summaries via search, ca.trustpilot.com/review/henrymeds.com](https://ca.trustpilot.com/review/henrymeds.com); [formblends](https://formblends.com/articles/glp1-hub/how-to-spot-a-fake-glp1-provider-red-flags)). Shoppers know this. For this audience, Trustpilot stars count for less than BBB, Reddit and LegitScript signals.
- **Market context that shapes VoC as of Oct 2026** (it changed sharply in the last 12 months):
  - Compounded tirzepatide lost its shortage pathway in 2025. The FDA sent 100+ warning letters in 2025 and 30 more on 2026-02-20 over "same as brand" claims ([BenefitsPRO](https://www.benefitspro.com/amp/2026/03/05/fda-issues-warning-letters-to-30-telehealth-firms-over-glp-1-marketing/); [Patient Care](https://www.patientcareonline.com/view/fda-issues-warning-letters-30-telehealth-companies-over-misleading-compounded-glp-1-ra-marketing)). On 2026-04-30 it proposed excluding semaglutide/tirzepatide/liraglutide from the 503B bulks list ([Orrick](https://www.orrick.com/en/Insights/2026/05/FDA-Moves-to-Shut-the-Door-on-Large-Scale-Compounding-of-GLP1-Drugs); [Medscape](https://www.medscape.com/viewarticle/fda-proposes-end-mass-glp-1-compounding-2026a1000e06)). It issued a warning letter to Empower Pharmacy on 2026-09-18 ([Frier Levitt](https://www.frierlevitt.com/articles/fda-warning-letter-compounded-glp-1-products/)). 503A compounding continues under more scrutiny.
  - Hims & Hers pulled its $49 compounded oral sema pill in Feb 2026. In March 2026 it settled with Novo, began offering branded Wegovy/Ozempic pens and pills, and stopped advertising compounded GLP-1s ([WTOP/AP](https://wtop.com/national/2026/03/hims-hers-health-and-novo-nordisk-end-lawsuit-over-weight-loss-medications-enter-collaboration/); [HLTH](https://hlth.com/insights/news/hims-and-hers-makes-deal-with-novo-nordisk-as-it-shifts-obesity-strategy-2026-03-10)).
  - Brand cash prices have fallen. Wegovy pill: $149 (low doses) and $299 (high doses) ([NBC](https://www.nbcmiami.com/news/health/weight-loss-drugs-changes-2026/3742592/)). Foundayo (orforglipron), launched 2026-04-06 on LillyDirect: from $149 ([GLP1 Guide](https://glp1guide.substack.com/p/foundayo-orforglipron-is-approved)). Wegovy injection self-pay: $349 at all doses, $199 intro for the first two fills ([NovoCare](https://www.novocare.com/obesity/products/wegovy.html); [Fierce Pharma](https://www.fiercepharma.com/marketing/novo-unveils-newly-reduced-self-pay-prices-wegovy-ozempic-after-white-house-deal)). Zepbound vials: $299 / $399 / $449 by dose ([Fierce Healthcare](https://www.fiercehealthcare.com/marketing/lilly-joins-novo-glp-1-self-pay-price-cuts-lowering-costs-single-dose-zepbound-vials)). TrumpRx.gov links shoppers to manufacturer cash prices ([NBC](https://www.nbcmiami.com/news/health/weight-loss-drugs-changes-2026/3742592/)).
  - **Implication:** "brand vs compounded" is no longer a choice between $1,000+ and $199. The gap is now about $149–$449 brand against $149–$399 compounded plus membership fees. For many shoppers the price argument for compounded has mostly gone, and the safety and legitimacy argument against it has grown.

---

## 1. Demographics & context of the online GLP-1 buyer

| Dimension | What the data says | Source |
|---|---|---|
| **Penetration** | 12% of US adults currently take a GLP-1 (for weight loss, diabetes or another condition); 18% have ever taken one (Nov 2025). Gallup: 12.4% take one *specifically for weight loss* (2025), up from 5.8% in Feb 2024. | [KFF Nov 2025](https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/); [Gallup](https://news.gallup.com/poll/696599/obesity-rate-declining.aspx) |
| **Gender** | Women outpace men: 15% vs 9% currently using (KFF); 15.2% vs 9.7% (Gallup). The online and telehealth channel skews more female. In one telehealth GLP-1 program cohort, 91% of patients were female. Compounded-only users are more likely to be female and far less likely to have T2D (13.8% vs 50.5% of brand-only users). | KFF; Gallup; [Drug Topics (ADA 2025)](https://www.drugtopics.com/view/telemedicine-with-glp-1-behavior-program-shows-significant-declines-in-weight-blood-pressure-ada-2025); [medRxiv primary-care EHR study](https://www.medrxiv.org/content/10.1101/2025.05.12.25327436.full.pdf) |
| **Age** | Use is highest at ages 50–64 (22% current, KFF). Gallup shows use at 16.2% for ages 40–49 and 17.0% for ages 50–64. Mean age in the telehealth cohort above was 44. **Core online buyer: woman aged 35–64, with the heaviest use at 40–64 (peri- and post-menopause).** | KFF; Gallup; Drug Topics |
| **Income / education** | Telehealth cohorts skew affluent: in one study 72.8% had household income of $100k+ and 73.9% held a bachelor's degree or higher. Affordability is still strained: 56% of users say the drugs were difficult to afford, including 55% of those with insurance. | [Drug Topics](https://www.drugtopics.com/view/telemedicine-with-glp-1-behavior-program-shows-significant-declines-in-weight-blood-pressure-ada-2025) (via search summary); KFF Nov 2025 |
| **Channel** | 76% got the drug from their own doctor, 17% from an online provider or website, and about 9% from a med spa (KFF Nov 2025). An earlier survey put telehealth startups plus aesthetic services at 23% of users. | [KFF via search](https://www.kff.org/public-opinion/kff-health-tracking-poll-prescription-drug-costs-views-on-trump-administration-actions-and-glp-1-use/); [medRxiv](https://www.medrxiv.org/content/10.1101/2025.05.12.25327436.full.pdf) |
| **Insurance status** | Among *insured* users, 27% paid the full cost themselves, 57% shared the cost, and 24% had full coverage (KFF Nov 2025; the categories overlap as reported). 62.4% of pharmacy claims for weight-loss GLP-1s were rejected between Jan 2021 and Oct 2024. 90%+ of commercial plans require prior authorization, and 40–60% of appeals succeed. Compounded GLP-1s are never covered by insurance. | KFF; [RX Index denial stats](https://therxindex.com/guides/glp-1-insurance-denial-statistics/); [glpplaybook](https://glpplaybook.com/glp-1-cost-comparison/) |
| **Prior diet history** | Almost every buyer has a long dieting history. Among 150k Evidation members, 88% had used exercise and 84% diet to lose weight, and 66% lost less than they wanted on their last attempt. 14% of GLP-1 users said their insurer required another method first, and 25% heard the same from their clinician. | [Rock Health Weight Care survey](https://rockhealth.com/insights/weighing-in-consumer-perspectives-on-weight-care/) |
| **Persistence** | Only 32% are still on therapy at one year, about 15% at two years, and 8% at three years (Prime Therapeutics, insured population). Cost and side effects are the top reasons for stopping. | [Becker's / Prime](https://www.beckerspayer.com/payer/most-patients-stop-taking-weight-loss-drugs-after-1-year-report.html); [KFF May 2024](https://www.kff.org/health-costs/kff-health-tracking-poll-may-2024-the-publics-use-and-views-of-glp-1-drugs/) |
| **Non-buyer barriers** | Among the uninterested, 51% prefer diet and exercise, 38% worry about side effects, and only 16% cite cost (Axios-Ipsos, Mar 2026). Of non-users, 21% are interested in a pill and 15% in an injection. | [Axios-Ipsos](https://www.axios.com/2026/03/19/glp-1-use-cost-hurdles-axios-ipsos-poll) |

**Persona baseline:** a woman aged 38–62 with a household income of roughly $75–150k and either commercial insurance that excludes weight-loss GLP-1s or a denied prior authorization. She has tried WW/Noom/keto/calorie counting several times. She has done her homework on Reddit and TikTok and expects to pay cash at $150–$450 a month. She is price-sensitive *month over month*, not just at signup.

---

## 2. Jobs-to-be-done, motivations, triggers

**Core functional job:** *"Get a legitimate prescription for a GLP-1 I can actually afford every month, delivered to my door, without a fight with my insurer or doctor."*

**Emotional jobs**
- Quiet the "food noise" and stop the daily willpower battle. Typical quote: *"I didn't realize how much of my day revolved around food until that noise was gone."* (Reddit user u/QuietHeadspace, quoted by [Medino](https://www.medino.com/article/real-stories-about-mounjaro-and-food-noise))
- Finally win after years of diets that didn't work (Rock Health: 66% lost less than they wanted on the last attempt).
- Avoid judgment. Online means no awkward conversation with a PCP who may say "just eat less."
- Take back midlife health (menopause belly weight, prediabetes, blood pressure, joint pain).

**Social job:** a discreet and fast route. 69% of eligible adults say they would prefer a daily pill to a weekly shot *because it's more discreet* ([survey via search, People's Pharmacy / Sunlight](https://www.goskagit.com/sunlight-com-survey-4-in-10-overweight-americans-say-theyll-try-a-glp-1-pill/article_a544c2fe-74a5-5ff4-a723-66a65191fa4d.html)).

**Triggers (why now)**
1. **Price drop or news event:** brand cash-price cuts, the Wegovy pill at $149, Foundayo at $149, TrumpRx coverage. Search spikes follow news.
2. **Insurance denial or lost coverage:** a PA denial, an employer dropping coverage on Jan 1, or a job change.
3. **Provider disruption:** a compounded supplier shut down, Hims switching patients to brand, a price increase at the current provider, or an FDA headline. These produce "switcher" searches such as "best Hims alternative" and "cheapest tirzepatide."
4. **Health scare or milestone:** an A1c or BP reading, a doctor saying "prediabetic," a 40th or 50th birthday, an upcoming wedding or reunion, a photo.
5. **Social proof:** a friend or coworker's visible loss, or before/after posts on TikTok, Instagram and Reddit.
6. **Menopause onset:** sudden weight gain despite unchanged habits.
7. **Plateau or regain after stopping:** the restart search. Restarting is common (Michigan Public, Apr 2026: "Quit a GLP-1, plan to start again — plenty of people do it" [link](https://www.michiganpublic.org/2026-04-15/quit-a-glp-1-plan-to-start-again-its-not-recommended-but-plenty-of-people-do-it)).

---

## 3. Top anxieties & objections (ranked)

Ranking weighs how often each appears in complaint and review summaries and surveys, and how close it sits to the click and checkout decision.

| # | Anxiety / objection | Evidence | What it sounds like |
|---|---|---|---|
| 1 | **True monthly cost / hidden fees / membership** | Mochi advertises $199 tirz, but a mandatory $79 membership makes the real cost $278 ([giftfromwithin](https://www.giftfromwithin.org/weight-loss/mochi-review/)). Noom bills compounded sema every 12 weeks ($852.27) with no mid-cycle refunds ([PlexusDx](https://plexusdx.com/blogs/learn/noom-med-reviews-trustpilot-reddit-user-reports-plexusdx)). On r/TirzepatideRX, "hidden membership fees" for compounded tirz are described as "getting out of control" ([GummySearch](https://gummysearch.com/r/TirzepatideRX/)). | "What's the *all-in* price?" "Is the $X just the first month?" |
| 2 | **Price jumps at higher doses** | 2.5 mg is a 4-week starter. "Starter-dose pricing is misleading… real monthly costs increase at month two or three" ([Trimi blog](https://trytrimi.com/blog/shed-tirzepatide-hidden-costs)). Henry Meds costs "can increase by $100/month as dosages are adjusted upward" ([allglp1](https://allglp1.com/providers/henry-meds)). Brand Zepbound vials run $299 → $449. | "Same price at every dose?" "What do I pay at 10 mg?" |
| 3 | **Subscription traps / cancellation / refunds** | Hims: "unauthorized subscription renewals, no advance notice… zero refund policies," with a 48-hour cancel window ([Hims review summaries](https://weightrxguide.com/reviews/hims-and-hers-glp-1-review)). MEDVi: charges after a pause, a customer told they had to "reactivate their subscription to get a refund" ([Trustpilot via search](https://www.trustpilot.com/review/medvi.org?page=6)). SkinnyRx: "Cancellation requires contacting support" ([RX Index](https://therxindex.com/guides/skinny-rx-reviews/)). Henry Meds: BBB F with 228 complaints ([allglp1](https://allglp1.com/providers/henry-meds)). | "Can I cancel online, anytime?" "Will they keep charging me?" |
| 4 | **"Is this a scam / legit?"** | Reviews like "STAY AWAY- Medication is a SCAM. They refused to ship me the medications that I've already paid for" (bmiMD, [Trustpilot via search](https://nl.trustpilot.com/review/bmimd.com)). Users know about fake-review bursts and the Trustpilot banners ([formblends red flags](https://formblends.com/articles/glp1-hub/how-to-spot-a-fake-glp1-provider-red-flags)). On r/CompoundedSemaglutide, the dominant post types are "pain & anger" and advice requests ([GummySearch](https://gummysearch.com/r/CompoundedSemaglutide/)). | "Has anyone actually used X?" "Real doctor? Real pharmacy?" |
| 5 | **Compounded safety, legality & continuity** | API sourced overseas, FDA does not review it ([KFF Health News](https://kffhealthnews.org/health-industry/glp1-weight-loss-drugs-telehealth-oversight-regulation-compounded-semaglutide/)). The FDA crackdown means users fear losing access: "If approved we will lose access!" ([GummySearch r/CompoundedSemaglutide](https://gummysearch.com/r/CompoundedSemaglutide/)). Users report efficacy varying between pharmacies; one compounded ODT buyer got "zero results after 26 days… no reduction in food noise" ([Henry Meds Trustpilot via search](https://ca.trustpilot.com/review/henrymeds.com)). | "Is compounded still legal?" "Which pharmacy (503A/503B)?" "Is it the real stuff?" |
| 6 | **Side effects (nausea, vomiting, dosing errors)** | Side effects are the #2 reason for stopping (KFF), and 38% of non-interested adults cite them (Axios-Ipsos). In one dosing error, a telehealth patient was prescribed 2.21 mg sema for a first dose, roughly 9x the normal start, and was hospitalized ([KFF Health News](https://kffhealthnews.org/health-industry/glp1-weight-loss-drugs-telehealth-oversight-regulation-compounded-semaglutide/)). The FDA warns that confusion between mL, mg and "units" in vials leads to errors ([FDA](https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-concerns-unapproved-glp-1-drugs-used-weight-loss)). | "Do they give anti-nausea meds?" "Who do I message if I'm sick?" |
| 7 | **Insurance denial / PA hassle** | 62% claim rejection rate ([RX Index](https://therxindex.com/guides/glp-1-insurance-denial-statistics/)). Ro's insurance concierge is the reason users pick Ro, but "multiple reviewers reported difficulty navigating the PA process" ([RX Index Ro](https://therxindex.com/guides/ro-glp1-reviews/)). Found: a member "paid for a full year of membership fees upfront, never receiving any medication" ([Found Trustpilot via search](https://ca.trustpilot.com/review/joinfound.com)). | "Will they handle the PA?" "Do I pay the membership if denied?" |
| 8 | **Customer support responsiveness** | Common across Hims, Ro, Mochi, MEDVi and Henry: "several days for email replies," BBB pattern of "long phone wait times… messages that went unanswered" (Mochi, [giftfromwithin](https://www.giftfromwithin.org/weight-loss/mochi-review/)). Embody: "I was 'guaranteed' a call back by a supervisor same day and was never called" ([healthymealsincentives](https://healthymealsincentives.org/reviews/)). | "Can I reach a human?" "How fast do refills get approved?" |
| 9 | **Shipping / cold chain / refill gaps** | "receiving spoiled medication due to improper packaging, being provided with old shipment tracking numbers" ([telehealth.org summary](https://telehealth.org/news/online-glp-1-scams-telehealth-consumer-safety/)). "2nd month wasn't shipped but I was charged" (Embody). Hims refill problems have been documented ([Trimi](https://trytrimi.com/blog/hims-tirzepatide-refill-problems)). | "Will I miss a dose between refills?" "Is it shipped with ice packs?" |
| 10 | **Weight regain on stopping** | Trial data show about two-thirds of lost weight returns within a year of stopping ([Prime/Undark](https://undark.org/2025/09/01/weight-loss-drugs-holistic/)). In a survey, 66% regained some weight after stopping ([xtalks](https://xtalks.com/survey-finds-most-glp-1-users-discontinue-drug-before-reaching-goal-weight-3959/)). | "Am I on this forever?" "What's the maintenance plan?" |
| 11 | **Muscle loss** | 36% of 1,000 GLP-1 users rate their muscle-loss risk as moderate to very high. 15% report actually experiencing muscle loss, rising to 32% among those aged 60+ ([Veru survey / Fierce Pharma](https://www.fiercepharma.com/marketing/veru-survey-highlights-muscle-loss-concerns-among-glp-1-users-lean-mass-preserving-med)). | "Ozempic face," "skinny fat," "protein goals" |
| 12 | **Needles** | Needle aversion is a primary barrier for about 19% of interested people. 87% of current users are interested in switching to a pill ([survey summary](https://www.goskagit.com/sunlight-com-survey-4-in-10-overweight-americans-say-theyll-try-a-glp-1-pill/article_a544c2fe-74a5-5ff4-a723-66a65191fa4d.html)). | "Is there a pill?" "Does the shot hurt?" |

---

## 4. Decision criteria — what they compare providers on

Listed in the order buyers seem to weigh them. Each criterion pairs **their words** with what it means for comparison-site UX.

1. **All-in monthly price at *my* dose, including membership.** Phrases: "same price any dose," "no membership fee," "flat rate," "price lock." Lumi was cited at "$309 for any dose with a coupon," and Mochi "a flat monthly fee regardless of dosage" ([GummySearch tirzepatide](https://gummysearch.com/tools/best-products/tirzepatide/)). *UX:* show the price at starter, mid and max doses, plus membership, plus the 12-month total.
2. **Brand vs compounded (and pill vs injection), and whether the brand is available through this provider.** After March 2026 many users ask "does X offer real Wegovy/Zepbound?" *UX:* a filter for "FDA-approved brand only" vs "compounded."
3. **Legitimacy signals:** LegitScript, a named US pharmacy (503A/503B), a licensed clinician, BBB grade, years in business, Reddit reputation. Mochi was noted as the "only provider tested that lets you pick your pharmacy" ([giftfromwithin](https://www.giftfromwithin.org/weight-loss/mochi-review/)). *UX:* a trust row on every card.
4. **Speed to medication:** approval time and days to delivery. "received their medication within a week" (Mochi Trustpilot summary); "free 2-day shipping" is a headline claim ([CoreAge PR](https://www.barchart.com/story/news/37303616/coreage-rx-earns-top-ranking-for-including-free-2-day-shipping-on-all-prescriptions)).
5. **Insurance help:** whether the provider handles the PA, what happens if it's denied, and whether insurance plus cash fallback are both offered (Ro's differentiator; [RX Index Ro](https://therxindex.com/guides/ro-glp1-reviews/)). A Ro user paid "$25/month" for Zepbound after concierge approval ([search summary](https://www.glp1clinics.org/blog/ro-body-review-glp1-weight-loss)).
6. **Cancel and refund terms:** cancel online, no long prepay required, refund when denied.
7. **Clinician access and support responsiveness:** a "real doctor" who "really took her time" ([Mochi Trustpilot via search](https://www.trustpilot.com/review/joinmochi.com)), and "the most responsive" of three GLP-1 providers tried ([Remedy Meds Trustpilot via search](https://uk.trustpilot.com/review/remedymeds.com?page=3)).
8. **Dosing flexibility:** microdosing, staying at a lower dose, choosing a titration pace, vials with extra "units."
9. **Extras that matter:** anti-nausea meds (ondansetron), syringes and alcohol pads included, a dosing calculator or video, coaching, and protein/muscle guidance.
10. **Switching ease:** carrying over their current dose rather than restarting at 2.5 mg. One reviewer said a staff member "made the conversion from a previous provider to SkinnyRX as easy as it could have been" ([SkinnyRx Trustpilot via search](https://ca.trustpilot.com/review/skinnyrx.com?page=2)).

### Seed quote bank (verbatim from search results; verify before reuse)

| Theme | Quote | Source |
|---|---|---|
| Food noise | "I didn't realize how much of my day revolved around food until that noise was gone." (u/QuietHeadspace) | [Medino](https://www.medino.com/article/real-stories-about-mounjaro-and-food-noise) |
| Food noise | "Two weeks into Mounjaro, it was like someone flipped a switch. I could walk past a bakery and feel nothing." (u/CraveNoMore) | [Medino](https://www.medino.com/article/real-stories-about-mounjaro-and-food-noise) |
| Ambivalence | "I'm healthier, but life tastes a little greyer" | [Medino](https://www.medino.com/article/real-stories-about-mounjaro-and-food-noise) |
| Value / praise | Semaglutide+ was "instrumental in my weight loss journey"; pricing "fair in today's market" | [Hims Trustpilot via RX Index](https://therxindex.com/guides/hims-weight-loss-reviews/) |
| Support pain | Reaching support described as "extremely frustrating" | [Hims Trustpilot via RX Index](https://therxindex.com/guides/hims-weight-loss-reviews/) |
| Scam fear | "STAY AWAY- Medication is a SCAM. They refused to ship me the medications that I've already paid for." | [bmiMD Trustpilot](https://nl.trustpilot.com/review/bmimd.com) |
| Billing | "2nd month wasn't shipped but I was charged." | [Embody via healthymealsincentives](https://healthymealsincentives.org/reviews/) |
| Fees | "hidden membership fees" for compounded tirz are "getting out of control" | [GummySearch r/TirzepatideRX](https://gummysearch.com/r/TirzepatideRX/) |
| Access fear | "If approved we will lose access!" | [GummySearch r/CompoundedSemaglutide](https://gummysearch.com/r/CompoundedSemaglutide/) |
| Switching praise | "night & day better" than the previous provider; the doctor "really took her time, getting to know my medical background & my personal goals" | [Mochi Trustpilot](https://www.trustpilot.com/review/joinmochi.com) |
| Responsiveness | Third GLP-1 provider tried; "so far, they are the most responsive" | [Remedy Meds Trustpilot](https://uk.trustpilot.com/review/remedymeds.com?page=3) |
| Midlife | "She prescribed me a GLP-1 for weight loss and HRT. I've lost 20 pounds. I feel so much better now that I'm getting the right support." (Laura M., *brand testimonial*) | [Midi Health](https://start.joinmidi.com/weight-loss-made-for-midlife) |
| Overdose harm | "still dealing with the residual side effects" | [KFF Health News](https://kffhealthnews.org/health-industry/glp1-weight-loss-drugs-telehealth-oversight-regulation-compounded-semaglutide/) |

---

## 5. Language & vocabulary (for ads and landing copy)

**Drug names & shorthand:** sema, semi, tirz, tirzep, "Zep," "Mounj," "Wegovy pill," "the pill," orforglipron / Foundayo ("orfor"), GLP-1, "GLP," "compounded," "compound," "comp tirz," "brand," "name-brand," "the real stuff," "off-brand," "knock-off" (critics), "gray" / "grey market," "research peptides" / "RUO," "reta" (retatrutide, gray market; [NPR](https://www.npr.org/2025/10/07/nx-s1-5528695/patients-turn-to-gray-market-for-cheaper-obesity-drugs-but-its-risky)).

**Format & dosing:** vials vs pens, "single-dose vials" (Zepbound), "multi-dose vial," "units" (on an insulin syringe), "mg," "BAC water," "reconstitute," "draw up," "pinning" or "pin day," "shot day," "titrate," "dose up," "step up," "starter dose," "2.5," "maintenance dose," "microdosing," "split dose," "stay on the lowest dose," ODT / sublingual / drops (compounded orals), "with B12" or "with glycine" (compounded add-ons; [eMarketer on Lilly's B12 concerns](https://www.emarketer.com/content/compounded-glp-1s-with-b12-pose-safety-risks--lilly-says)).

**Effects & experience:** "food noise," "quiet the food noise," "appetite suppression," "the switch flipped," "sulfur burps," "Ozempic face," "Ozempic butt," "nausea," "constipation," "fatigue," "plateau," "stall," "whoosh," "NSV" (non-scale victory), "SW/CW/GW" (start, current, goal weight), "down 40 lbs," "the scale finally moved."

**Commerce & provider language:** "telehealth," "provider," "clinic," "same price every dose," "flat price," "price lock," "membership fee," "no hidden fees," "self-pay," "cash pay," "LillyDirect," "NovoCare," "TrumpRx," "PA" (prior auth), "denied," "appeal," "coverage checker," "HSA/FSA eligible," "LegitScript," "503A/503B," "US-licensed pharmacy," "refill," "auto-ship," "cancel anytime."

**Copy guidance:** buyers trust specificity. Lead with dose-specific prices ("$X at every dose, including membership") rather than "from $99." Use their words: *food noise, flat price, real doctors, cancel anytime, FDA-approved brand or 503A-compounded*. Avoid "same as Ozempic" or "generic Wegovy" claims, which the FDA flagged in its 2026 warning letters ([Venable](https://www.venable.com/insights/publications/2026/03/fdas-latest-glp-1-crackdown-what-compounders)). These claims also carry ad-policy and legal risk for the client.

---

## 6. Personas / segments

### P1. "The Price-Driven Switcher" (post-shortage / post-crackdown refugee)
- **Who:** has used compounded tirz or sema for 6–24 months. Their provider raised prices, cut the product, moved them to brand (Hims after March 2026), or their pharmacy got a warning letter. Highly informed, Reddit-native.
- **Goals:** keep their current dose without restarting at a starter dose, and keep monthly cost about the same or lower.
- **Fears:** losing access mid-journey; a new pharmacy's product "not working the same"; restarting titration; a new subscription trap.
- **Needs to see to click:** "transfer your current dose," a named pharmacy, dose-specific all-in price, no long prepay, and an honest legal-status note. Compare the brand cash price ($349 Wegovy; $449 Zepbound 7.5 mg+) side by side with compounded.
- **Search terms:** "Hims alternative," "cheapest tirzepatide 2026," "compounded tirzepatide still available," "switch provider keep dose."

### P2. "The Nervous First-Timer" (needle-averse, scam-wary)
- **Who:** has never used a GLP-1. A friend's results or a price-drop headline triggered the search. Often female, 35–55, and anxious about needles, side effects and "is this legit."
- **Goals:** a simple, safe start, ideally a pill.
- **Fears:** needles (19% say needle aversion is a primary barrier), nausea, scams, an online doctor who doesn't care, and doing it wrong (dosing errors).
- **Needs to see to click:** "pill options" (Wegovy pill or Foundayo from $149), a "real US-licensed clinician" with photos, a step-by-step "how it works," auto-injector pens rather than vials, nausea support included, and BBB and LegitScript badges. Explain "brand vs compounded" in plain English.
- **Search terms:** "weight loss pill prescription online," "is [brand] legit," "GLP-1 for beginners," "does the shot hurt."

### P3. "Insured-but-Denied"
- **Who:** has commercial insurance and got a PA denial or a "plan excludes weight-loss drugs" notice, or lost coverage at plan renewal.
- **Goals:** maximize the chance of coverage while having a cash fallback ready.
- **Fears:** paying membership fees while waiting weeks for a PA that gets denied anyway (Found and Ro complaints), and being bounced between insurer and provider.
- **Needs to see to click:** "we handle PA and appeals," a "coverage checker," "no membership charge if denied" or a clear refund, and an instant cash path (LillyDirect / NovoCare pricing). Copy hook: "Denied? Here's your cheapest path today."
- **Search terms:** "Zepbound denied what now," "Wegovy not covered alternatives," "GLP-1 prior authorization help."

### P4. "The Brand-Only Skeptic"
- **Who:** often older (50–64), higher income, sometimes with T2D or cardiac history. Distrusts compounded drugs because of FDA headlines and overseas API reports.
- **Goals:** an FDA-approved drug at the lowest cash price, with convenience.
- **Fears:** counterfeit or "knock-off" product, contamination, being upsold into compounded drugs.
- **Needs to see to click:** "FDA-approved Wegovy / Zepbound / Wegovy pill / Foundayo only," manufacturer pharmacy fulfillment (LillyDirect / NovoCare), and a transparent total of drug plus visit fee. A filter to hide compounded providers.
- **Search terms:** "real Zepbound online," "Wegovy pill prescription online," "buy Wegovy without insurance."

### P5. "The Midlife / Menopause Woman"
- **Who:** 45–60, peri- or post-menopausal, gaining weight "doing everything the same." The highest-use age band (KFF 22% at 50–64; Gallup 17%). May want HRT as well.
- **Goals:** lose the "menopause belly," improve sleep and energy, protect bones and muscle.
- **Fears:** being dismissed by doctors, muscle loss and frailty, "Ozempic face," side effects layered on menopause symptoms.
- **Needs to see to click:** menopause-trained clinicians, HRT + GLP-1 in one plan (Midi, Alloy-type positioning), protein and strength guidance, and microdosing or low-dose options.
- **Search terms:** "GLP-1 for menopause weight gain," "HRT and semaglutide," "perimenopause weight loss medication."

### P6. "Maintenance / Microdoser"
- **Who:** reached their goal or is near it, or wants a "metabolic" low dose. 36% of GLP-1 users report microdosing, for tolerability, cost and maintenance ([Tebra via eMarketer](https://www.emarketer.com/content/telehealths-bet-on-microdoses-broaden-glp-1-weight-loss-health-appeal)). Microdosers are more likely to source from telehealth (about 24%) ([ISPOR 2026](https://www.ispor.org/heor-resources/presentations-database/presentation-cti/ispor-2026/poster-session-4-3/emerging-patterns-of-glp-1-microdosing-in-a-large-real-world-population)). Found launched a microdosing program in Oct 2025 ([BusinessWire](https://www.businesswire.com/news/home/20251028348303/en/Found-Health-Launches-GLP-1-Microdosing-Program-for-Early-Metabolic-Dysfunction)).
- **Goals:** avoid regain cheaply, with a lower monthly cost and flexible dosing.
- **Fears:** regain ("two-thirds comes back"), having to pay full price for a low dose, a provider forcing them to titrate up.
- **Needs to see to click:** "maintenance plans," low-dose pricing, flexible dosing (vials or pill), long-term cost per year.
- **Search terms:** "GLP-1 maintenance dose," "microdosing tirzepatide," "stop GLP-1 without regaining."

### P7 (emerging). "The Restarter"
- Stopped because of cost or side effects (two-thirds stop within a year) and regained weight. Comes back with guilt and price sensitivity. Needs "no judgment," "restart at a tolerable dose," and the price.

### P8 (watch, do not target). "Gray-Market Bargain Hunter"
- Buys "research peptides" or raw API from overseas ([NPR](https://www.npr.org/2025/10/07/nx-s1-5528695/patients-turn-to-gray-market-for-cheaper-obesity-drugs-but-its-risky)). Not a compliant target. The client can intercept this searcher with education ("cheapest *legal* options: $149 pills").

---

## 7. Positive praise patterns (what makes a 5-star review)

Synthesized from Trustpilot and Reddit summaries for SkinnyRx (4.8, 91% five-star), Remedy Meds (4.5, 13k reviews), Mochi, Henry, Hims and Ro ([RX Index SkinnyRx](https://therxindex.com/guides/skinny-rx-reviews/); [Remedy Meds Trustpilot](https://uk.trustpilot.com/review/remedymeds.com?page=3); [Mochi Trustpilot](https://www.trustpilot.com/review/joinmochi.com)):

1. **A named, human support person**, e.g. "customer service getting praised by name repeatedly" (SkinnyRx). Five-star reviews name the agent.
2. **Fast responses and refill approvals**, e.g. "most responsive" of three providers (Remedy).
3. **Fast shipping that arrives intact and complete**: "arriving quickly and intact with all necessary equipment and support medications" (Henry Meds Trustpilot summary).
4. **A clinician who listens**: "really took her time, getting to know my medical background & my personal goals" (Mochi).
5. **Visible results plus food-noise relief**, reported in pounds and timeframe ("down 30 lbs in 4 months"). Reddit users call appetite suppression "the game-changer" ([RX Index Hims](https://therxindex.com/guides/hims-weight-loss-reviews/)).
6. **Price honesty**, i.e. the bill matched the quote. "Fair in today's market" (Hims). Flat pricing across doses is praised.
7. **An easy switch from another provider**, which is a strong comparative cue ("night & day better," "made the conversion… as easy as it could have been").
8. **Side-effect support**: anti-nausea medication included, and dose adjustments when sick.
9. **Insurance win**: "Ro got my Zepbound covered — $25/month."

**What turns stars into 1-stars:** a surprise charge after cancelling or pausing, a refill gap, no human reply for days, and a price increase after dosing up. These are the inverse of the praise list, and they are operational problems, not clinical ones.

---

## 8. Implications for the comparison site (CRO hypotheses to test)

1. Make **"Real monthly cost at your dose (incl. membership)"** the primary sort and column, not the "from $" price.
2. Add trust chips to every provider card: **Brand / Compounded / Pill**, LegitScript, named pharmacy, BBB grade, cancel-online yes/no, refund-if-denied yes/no.
3. Build segment landing pages for paid search clusters: *switchers* ("keep your dose"), *denied* ("insurance said no?"), *pill/needle-free*, *menopause*, *maintenance/microdose*, *brand-only*.
4. Put a short, neutral "Is compounded still legal in 2026?" explainer high on the page. It addresses the #4–5 anxieties without making prohibited equivalence claims.
5. Ad copy should use customer vocabulary: "quiet the food noise," "same price every dose," "real US doctors," "cancel anytime," "FDA-approved pill from $149."

---

*Next step: replace or augment the quote bank with the client's raw Reddit and Trustpilot exports, code every review against the anxiety taxonomy in section 3, and re-rank by frequency.*
