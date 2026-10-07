# 01 — Search Intent, Market Context, Ad Policy & Device Behavior
**Client:** healthaccess.com/weight-loss/compare (US GLP-1 telehealth comparison / affiliate site, Google Ads paid search; desktop now, mobile next)
**Prepared:** 2026-10-07
**Method & caveats:** Web research via search engine results. Direct page fetches (WebFetch) were blocked by the network proxy for nearly every domain (fda.gov, support.google.com, biopharmadive, searchengineland, techtarget, etc.), so facts below come from search-result extracts of the cited pages, not full-page reads. Every claim carries its source URL; confidence flags:
- **[V]** = corroborated by 2+ independent sources or a primary source (company / regulator / SEC filing)
- **[S]** = single secondary source; plausible but re-check before using in ad copy
- **[U]** = could not verify / from niche tracker sites or from analyst memory — treat as hypothesis

No keyword-volume or CPC data from Google Keyword Planner was available to this research. The keyword universe below is built from market logic plus observed SERP/competitor patterns; volumes must be pulled from the client's own Google Ads account (Search Terms report + Keyword Planner) — see DATA_REQUEST.md.

---

## 0. The 60-second version

1. **The market flipped from "cheap compounded" to "cheap branded" between Dec 2025 and Apr 2026.** Brand-name GLP-1s now sell cash-pay at $149–$449/month (Wegovy pill from $149, Foundayo from $149, Zepbound vial/KwikPen $299–$449, Wegovy pen $349, Wegovy HD $399). Compounded sema/tirz still exists ($99–$399) but is legally and reputationally squeezed. Searchers' "price" and "safety" questions have changed accordingly.
2. **Pills are the new demand driver.** Oral Wegovy (launched 5 Jan 2026) and Lilly's Foundayo/orforglipron (approved 1 Apr 2026) created a new query family ("weight loss pill", "wegovy pill price", "foundayo vs wegovy pill").
3. **Google policy is the binding constraint for an affiliate:** since 29 Oct 2025 you can *mention* Rx drug names in ads/landing pages in the US without certification, but you **must be certified to keyword-target** Rx drug terms (semaglutide, Wegovy, Zepbound, tirzepatide, Foundayo…). LegitScript does certify "price comparison websites" — whether a telehealth-comparison affiliate qualifies needs a direct LegitScript/Google conversation. This decides which half of the keyword universe the site can even buy.
4. **Desktop converts better per visit; mobile has the volume.** Health & wellness: mobile ≈7x traffic, desktop converts ~22% better (Unbounce). Mobile launch needs a mobile-native comparison UI, not a shrunk table.

---

## 1. Keyword universe by intent cluster

### How to read this section
- **Funnel stage**: TOFU (problem-aware) → MOFU (solution-aware, evaluating) → BOFU (provider/product-aware, ready to act).
- **Policy flag**: 🔒 = contains Rx drug terms → keyword-targeting requires Google healthcare certification (see §3). ✅ = no Rx drug term in keyword (still subject to healthcare policy on landing page).
- "Above the fold" = what must be visible in the first viewport (desktop ~ 1366×768; mobile ~ 390×700) for message-match.

### Cluster A — Provider brand (navigational / evaluative)
| Example queries | Policy |
|---|---|
| hims weight loss, hims glp-1, hims weight loss reviews, hims weight loss cost | ✅ (brand) |
| ro body program, ro body program reviews, ro weight loss price, ro wegovy | ✅ / 🔒 if drug name |
| weightwatchers med+ / ww clinic, noom med / noom glp-1, found weight loss, calibrate, henry meds, mochi health, sesame weight loss, lifemd weight loss, goodrx wegovy, amazon one medical weight loss, lillydirect, novocare pharmacy, trumprx | ✅ / 🔒 (LillyDirect/NovoCare pages are drug-specific) |
| "is [brand] legit", "[brand] cancel subscription", "[brand] side effects", "[brand] vs [brand]" | ✅ |

- **What the searcher wants:** confirmation the brand is trustworthy, the *real total monthly cost* (membership + medication), what medications it offers now (branded vs compounded — this changed for Hims in 2026), insurance acceptance, how fast they can start, and how to cancel.
- **Funnel stage:** BOFU (already chose a shortlist). Highest CVR, but searcher may click the brand's own ad first; your value-add is neutral verification + alternatives.
- **Above the fold must show:** the brand's name and logo in the H1 ("Hims Weight Loss Review (Oct 2026): Cost, Medications, Pros & Cons"); a verdict box with all-in monthly price, medications offered (branded/compounded/pill), insurance Y/N, star rating with methodology link; a primary CTA to that brand **and** a "compare with 2 alternatives" row. "Last updated" date visible (prices changed ~monthly in 2026).
- **Notes:** Many affiliate programs **prohibit bidding on their brand term** — check each partner's terms before buying brand keywords. Google's trademark policy may also restrict use of the brand in ad text if the owner filed a complaint. Hims's March 2026 Novo deal and May 2026 pivot to branded GLP-1s ([WTOP/AP, Mar 2026](https://wtop.com/national/2026/03/hims-hers-health-and-novo-nordisk-end-lawsuit-over-weight-loss-medications-enter-collaboration/); [Hims Q2 2026 coverage, Aug 2026](https://www.thestar.com.my/business/business-news/2026/08/12/hims-shift-to-obesity-drugs-drives-wider-quarterly-loss)) means "hims weight loss" searchers in late 2026 are often asking "does Hims still sell compounded / how much is Wegovy at Hims?" — review pages must reflect the current offering. **[V]**

### Cluster B — Comparison / "best" (evaluative)
| Example queries | Policy |
|---|---|
| best online weight loss program, best weight loss telehealth, best glp-1 telehealth, best online weight loss doctor | ✅ |
| hims vs ro, ro vs found, noom med vs ww, hims vs henry meds | ✅ |
| best place to get semaglutide online, best tirzepatide provider, best place to get wegovy pill, cheapest place to get zepbound | 🔒 |
| weight loss programs compared, online weight loss clinic reviews, top rated weight loss programs 2026 | ✅ |

- **What the searcher wants:** a short, credible ranked list; *how* it was ranked; price side-by-side; which ones take insurance; which offer pills vs injections vs compounded; speed of start.
- **Funnel stage:** MOFU → BOFU. This is the comparison site's core money cluster and the one where it has most right-to-win vs the providers themselves.
- **Above the fold must show:** H1 echoing the query ("Best Online Weight Loss Programs — Compared Oct 2026"); a compact top-3 (desktop: table row; mobile: stacked cards) with *all-in* monthly price, medication types, insurance, rating, CTA; a one-line methodology / "how we rank" link and advertising disclosure ("We may earn a commission…") adjacent — the FTC NextMed case (below) shows hidden fees and fake reviews are enforcement targets. Filter chips (Pill / Injection / Uses insurance / Under $200) are high-value above the fold.
- **"X vs Y" queries** need a dedicated head-to-head layout (two columns, winner by category), not the generic top-10 page.

### Cluster C — Price / cost (transactional research)
| Example queries | Policy |
|---|---|
| cheapest weight loss medication online, affordable weight loss program, glp-1 cost without insurance, weight loss shot cost | ✅ ("glp-1" is a drug class — **treat as ambiguous**; verify in account whether it's flagged) |
| cheapest semaglutide online, compounded tirzepatide cost, semaglutide price per month, tirzepatide cost without insurance | 🔒 |
| zepbound vial price, zepbound kwikpen price, wegovy cost without insurance, wegovy pill price, wegovy pill $149, foundayo price, trumprx wegovy, lillydirect zepbound price | 🔒 |
| $99 semaglutide, $149 weight loss pill | 🔒 |

- **What the searcher wants:** a single, trustworthy *all-in* monthly number (medication + membership + labs), the price by dose (since prices step up with titration), the lowest legitimate option, and whether the low intro price "sticks".
- **Funnel stage:** BOFU-adjacent; very high commercial intent but highly price-anchored — expect them to bounce if the first number shown is higher than the number in the ad.
- **Above the fold must show:** a price table ranked by price with columns *Starting price → Maintenance price → Membership fee → Total*; clearly labelled "Brand-name (FDA-approved)" vs "Compounded (not FDA-approved)"; the manufacturer-direct anchors (LillyDirect, NovoCare, TrumpRx) because savvy searchers already know them; "Prices verified [date]". Do **not** headline a starter price without showing the maintenance price — the FTC alleged exactly this kind of deceptive pricing against NextMed ([Kelley Drye summary, 2025](https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/the-ftc-takes-a-shot-at-telehealth-program-for-allegedly-deceptive-pricing-consumer-reviews-and-weight-loss-claims.md); [Foley, Aug 2025](https://www.foley.com/insights/publications/2025/08/health-care-marketing-enforcement-ftc-targets-telehealth-company-for-deceptive-w/)). **[V]**
- **Price reference points (late 2026)** — see §2 table. Key intent shift: "cheapest" no longer automatically means compounded; Wegovy pill and Foundayo at $149 starting doses compete head-on with $99–$199 compounded offers.

### Cluster D — Medication-specific (product research / acquisition)
| Example queries | Policy |
|---|---|
| semaglutide online prescription, get semaglutide online, tirzepatide online, compounded semaglutide online | 🔒 |
| wegovy online, how to get wegovy prescription, zepbound online prescription, zepbound vial, zepbound kwikpen | 🔒 |
| wegovy pill, oral wegovy, foundayo, orforglipron, weight loss pill prescription, new weight loss pill 2026 | 🔒 ("weight loss pill" alone ✅) |
| wegovy hd / wegovy 7.2 mg, ozempic for weight loss, mounjaro for weight loss (off-label intent) | 🔒 |
| semaglutide vs tirzepatide, wegovy pill vs foundayo, zepbound vs wegovy, pill vs injection weight loss | 🔒 |
| weight loss injections online, glp-1 prescription online | ✅/ambiguous |

- **What the searcher wants:** "Where can I legitimately get *this specific drug*, prescribed online, today, and what will it cost me?" For drug-vs-drug queries: efficacy (% weight loss), side effects, pill vs shot, price.
- **Funnel stage:** BOFU for "[drug] online/prescription"; MOFU for "[drug] vs [drug]".
- **Above the fold must show:** the drug name in H1; a list filtered to providers that actually prescribe *that* drug (critical — sending a "zepbound vial" searcher to a compounded-only provider kills CVR and trust); per-provider price for that drug; insurance/cash; FDA-approval status label. For vs-queries: a 4–6 row comparison (avg weight loss in trials, form, dosing frequency, cash price, common side effects) with source links. Must include fair-balance / safety info link (FDA's 2025–26 crackdown targets omitted risk info).
- **Clinical anchors worth surfacing (cite source on page):** oral Wegovy 16.6% mean loss at 64 weeks ([HLTH, Jan 2026](https://hlth.com/insights/news/the-149-disruptor-goodrx-weightwatchers-lifemd-scale-wegovy-access-2026-01-06)) **[S]**; Wegovy HD 7.2 mg 20.7% at 72 weeks ([HCPLive, 19 Mar 2026](https://hcplive.com/view/fda-approves-higher-dose-semaglutide-wegovy-hd-injection-7-2-mg-for-obesity)) **[V]**. Foundayo does not require fasting, unlike oral Wegovy ([GLP1 Guide](https://glp1guide.substack.com/p/foundayo-orforglipron-is-approved)) **[S]** — a real differentiator for "pill" searchers.
- **Head-to-head comparative claims are legally live:** Novo sued Lilly on 21 Jul 2026 (Lanham Act) over ads comparing Zepbound high doses vs Wegovy low doses while omitting Wegovy 7.2 mg ([UPI, 21 Jul 2026](https://www.upi.com/Top_News/World-News/2026/07/21/novo-nordisk-lawsuit-eli-lilly-wegovy-glp-1/1551784642135/); [eMarketer](https://www.emarketer.com/content/novo-nordisk-sues-eli-lilly-over--misleading--drug-ads-glp-1-marketing-rivalry-escalates)) **[V]**. Comparison tables must compare like-for-like doses and cite trials.

### Cluster E — Insurance / coverage
| Example queries | Policy |
|---|---|
| does insurance cover wegovy, is zepbound covered by insurance, does medicare cover wegovy, wegovy $50 medicare | 🔒 |
| weight loss program that takes insurance, online weight loss doctor accepts insurance, does insurance cover weight loss medication, glp-1 coverage 2026 | ✅/ambiguous |
| bcbs / aetna / cigna / united weight loss medication coverage, prior authorization wegovy | 🔒/✅ |

- **What the searcher wants:** a yes/no for *their* plan, the copay if covered ($25 copay card pricing is common), what to do if denied (cash-pay path), and Medicare specifics.
- **Funnel stage:** MOFU. Often a qualifier: insured searchers convert to providers with insurance concierge; denied/uninsured searchers convert to cash-pay.
- **Above the fold must show:** a 2-path selector — "I have insurance (commercial / Medicare / Medicaid)" vs "Paying cash"; a one-line current-state answer ("Coverage varies; many employers restrict it. Medicare: $50/month via the GLP-1 Bridge since July 2026"); providers that offer insurance navigation surfaced first in the insured path.
- **2026 drivers of this intent:** Medicare GLP-1 Bridge pilot, 1 Jul 2026 – 31 Dec 2027, flat $50 copay for Wegovy (pill & pen), Zepbound KwikPen and Foundayo ([WUNC/NPR, 6 May 2026](https://www.wunc.org/2026-05-06/a-new-medicare-option-for-weight-loss-drugs-is-coming-heres-what-to-know)) **[V]**; employer pullback — Cigna dropped GLP-1 weight-loss coverage for its own employees from 1 Jul 2026, ~10% of covering employers (Business Group on Health) and 5% of large employers (Mercer) plan to drop in 2027 ([InsuranceNewsNet](https://insurancenewsnet.com/oarticle/cigna-drops-coverage-of-glp-1-obesity-drugs-for-its-own-employees); [MarketScreener/Reuters](https://www.marketscreener.com/news/some-us-employers-to-drop-coverage-of-glp-1-obesity-drugs-in-2027-as-use-increases-ce7f5cd8d989fe21)) **[V]**. Net effect: more "denied → cash" searchers and more 65+ Medicare searchers (older skew = more desktop, see §4).
- **Policy note:** Medicare-targeted messaging is sensitive; avoid implying government affiliation. "TrumpRx" and "Medicare" in ad copy should be factual only.

### Cluster F — Eligibility / qualification
| Example queries | Policy |
|---|---|
| bmi for semaglutide, bmi for wegovy, zepbound bmi requirement, do i qualify for glp-1, can i get wegovy with bmi 27 | 🔒/ambiguous |
| bmi calculator weight loss medication, weight loss medication if bmi 25, glp-1 for 20 lbs | ✅ |
| weight loss medication for pcos / menopause / sleep apnea / prediabetes | 🔒/✅ |

- **What the searcher wants:** "Will I be approved?" Labels: BMI ≥30, or ≥27 with a weight-related condition (hypertension, type 2 diabetes, dyslipidemia, OSA, etc.) for Wegovy/Zepbound/Foundayo **[U — label facts from analyst knowledge; confirm against current prescribing information before publishing]**. Zepbound also has an OSA indication and Wegovy a CV-risk-reduction indication **[U]**.
- **Funnel stage:** MOFU, but very high-quality when the answer is "yes" — this is the best place for an **interactive qualifier** (height, weight → BMI → eligible providers).
- **Above the fold must show:** an inline BMI calculator / 3-question quiz as the hero, with the result routing to eligible providers; plain statement that a licensed clinician makes the final decision. Avoid "Guaranteed approval" (Google + FTC risk; also untrue).

### Cluster G — Problem / symptom (TOFU)
| Example queries | Policy |
|---|---|
| how to lose weight fast, can't lose weight, weight loss plateau, lose belly fat, weight loss after 40/50, menopause weight gain | ✅ |
| medical weight loss, doctor prescribed weight loss, weight loss shots, weight loss injections near me, online weight loss doctor | ✅ |
| ozempic face, glp-1 side effects, hair loss on semaglutide | 🔒 (safety-adjacent) |

- **What the searcher wants:** education and hope; not yet shopping. Medical weight loss / "weight loss shots" are the bridge terms from problem to solution.
- **Funnel stage:** TOFU. Low CVR on paid; use only bridge terms ("medical weight loss online", "weight loss shots", "prescription weight loss") and exact/phrase match, with tight negatives.
- **Above the fold must show:** a short "Is prescription medication right for you?" explainer + the qualifier quiz; no body-shaming language (Google personalized-ads/sensitive-content policy and general ad-quality), no before/after images (Google restricts weight-loss before/after) ([OuterBox](https://www.outerboxdesign.com/articles/digital-marketing/health-and-wellness-advertising-restrictions-on-google-ads-keeping-your-campaigns-compliant/)) **[S]**.
- **Signal:** Google search interest in lifestyle interventions has stayed steady despite GLP-1 growth ([Healio, 20 Jul 2026](https://www.healio.com/news/endocrinology/20260720/google-search-volume-for-lifestyle-interventions-remains-steady-despite-rise-of-glp1s)) **[S]** — some TOFU searchers want non-drug options; a "with or without medication" angle (e.g., WW, Noom) can capture them.

### Cluster H — Safety / legitimacy / trust
| Example queries | Policy |
|---|---|
| is compounded semaglutide safe, is compounded tirzepatide legal 2026, compounded vs brand semaglutide, is compounded semaglutide still available | 🔒 |
| is hims legit, is ro legit, is [provider] a scam, [provider] reviews bbb, [provider] fda warning letter | ✅ |
| legitscript certified weight loss, safe place to buy semaglutide online, fake ozempic | ✅/🔒 |

- **What the searcher wants:** permission to proceed — "is this legal, is it safe, will I get the real thing, has this company been in trouble?"
- **Funnel stage:** BOFU friction removal (they are close to buying but anxious).
- **Above the fold must show:** a direct, sourced answer in the first two lines (e.g., "Compounded GLP-1s are not FDA-approved; FDA does not review their safety, effectiveness or quality. Since Feb 2025 shortages have ended and mass compounding is no longer permitted." + source links); a "trust checklist" (licensed US clinicians, LegitScript-certified, state-licensed pharmacy, FDA-approved option available, clear cancellation); providers that pass the checklist with badges; a link to methodology.
- **Copy rules that follow from FDA enforcement** (see §2.1): never say a compounded product is "the same as", "generic", or "same active ingredient as" Wegovy/Ozempic/Zepbound; disclose that compounded drugs are not FDA-approved; identify the dispensing pharmacy where known.

### Cross-cluster negatives & match-type guidance
- Negatives to test: "ozempic lawsuit", "free", "coupon" (if no coupon offer), "near me" (unless local partners), "for dogs/cats", "peptide"/"research chemical"/"retatrutide buy" (gray-market intent — also a policy hazard), "jobs", "stock", "nurse", "dosage chart" (informational, low CVR — test), "reddit" (test; Reddit-intent users are skeptical but often convert on neutral comparison pages).
- Gray-market: queries for "retatrutide" spiked (+196% YoY per one Trends-based analysis, [Athletech News](https://athletechnews.com/top-glp-1-cities-usa)) **[S]**; retatrutide is *not* FDA-approved (Lilly BLA filing expected ~Q1 2027 **[U]**). Don't bid — Google "unapproved substances" policy and reputational risk.

---

## 2. Market state late 2025 → Oct 2026 (what shapes intent)

### 2.1 Compounding: shortage ended, legal path closed, enforcement escalating
| Date | Event | Source | Conf. |
|---|---|---|---|
| 19 Dec 2024 | FDA resolves tirzepatide shortage | [NCPA](https://ncpa.org/newsroom/qam/2025/03/13/fda-ends-compounding-discretion-tirzepatide-maintains-discretion) | V |
| 18 Feb / 19 Mar 2025 | Tirzepatide enforcement discretion ends for 503A / 503B | [NCPA](https://ncpa.org/newsroom/qam/2025/03/13/fda-ends-compounding-discretion-tirzepatide-maintains-discretion) | V |
| 21 Feb 2025 | FDA declares semaglutide shortage over; discretion ends 22 Apr (503A) / 22 May 2025 (503B) | [Buchanan Ingersoll](https://www.bipc.com/fdas-removal-of-semaglutide-and-the-evolving-tirzepatide-decisions-what-compounders-need-to-know) | V |
| 2025 | FDA import alert + "green list" of vetted foreign GLP-1 API makers | [Pharma Manufacturing](https://pharmamanufacturing.com/industry-news/news/55314887/fda-launches-import-alert-to-block-illegal-glp-1-drug-ingredients-from-entering-us) | V |
| 9 Sep 2025 | HHS/FDA DTC advertising crackdown: thousands of letters to pharma, ~100 cease-and-desist; telehealth compounded GLP-1 ads targeted; flagged claims incl. "same active ingredient as Ozempic and Wegovy" and "clinically proven ingredients" | [King & Spalding](https://www.kslaw.com/insights/articles/hhs-and-fda-declare-crackdown-on-drug-advertising-and-promotion); [Holland & Knight, 29 Sep 2025](https://www.hklaw.com/en/insights/publications/2025/09/fda-hhs-taking-action-against-telehealths-compounded-drug-advertising) | V |
| 6 Feb 2026 | FDA announces intent to restrict GLP-1 APIs for non-approved compounded drugs and combat misleading DTC marketing | [McDermott+](https://www.mcdermottplus.com/insights/fdas-makary-declares-upcoming-crackdown-on-glp-1-claims-importation/); [Polsinelli](https://www.polsinelli.com/food-drug-device/publications/fda-threats-escalating-enforcement-glp-1-compounding) | V |
| 5–7 Feb 2026 | Hims launches $49 compounded semaglutide pill, withdraws it ~48h later; HHS refers Hims to DOJ | [Axios, 9 Feb 2026](https://www.axios.com/2026/02/09/hims-retreats-compounded-wegovy-pill); [Hims 10-Q](https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000076/hims-20260331.htm) | V |
| 9 Feb 2026 | Novo sues Hims (patent '343) | [Hims 10-Q](https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000076/hims-20260331.htm) | V |
| ~20 Feb–3 Mar 2026 | FDA warning letters to 30 telehealth firms: "sameness" claims and branding that implies the telehealth firm is the compounder | [FDA press release](https://www.fda.gov/news-events/press-announcements/fda-warns-30-telehealth-companies-against-illegal-marketing-compounded-glp-1s); [Pharmaceutical Commerce, 4 Mar 2026](https://www.pharmaceuticalcommerce.com/view/fda-issues-30-warning-letters-to-telehealth-firms-over-misleading-compounded-glp-1-marketing) | V |
| 13 Mar 2026 | Novo drops suit; Hims to sell Wegovy (pen + pill) and Ozempic, stop advertising compounded GLP-1s (limited compounded continues) | [American Med Spa Assoc.](https://americanmedspa.org/news/novo-nordisk-ends-lawsuit-forms-distribution-deal-with-hims-hers); [WTOP/AP](https://wtop.com/national/2026/03/hims-hers-health-and-novo-nordisk-end-lawsuit-over-weight-loss-medications-enter-collaboration/) | V |
| 2026 (after 30 Mar argument) | Fifth Circuit affirms FDA in both shortage-delisting cases (sema & tirz) | [Clark Hill](https://www.clarkhill.com/news-events/news/fifth-circuit-upholds-fda-glp1-shortage-decisions); [Mealey's](https://www.mealeys.com/mealeys/articles/2520341) | V (exact decision date not captured) |
| Aug 2026 | Hims Q2: pivot to branded drugs cuts gross margin 76%→64%; ~$33M restructuring; subscribers ~2.9M | [The Star/Reuters, 12 Aug 2026](https://www.thestar.com.my/business/business-news/2026/08/12/hims-shift-to-obesity-drugs-drives-wider-quarterly-loss) | V |
| Sep 2026 | Compounded sema still sold via 503A patient-specific Rx: ~$99–$348/mo; compounded tirz ~$125–$399 | [Cora, 2026](https://www.trycora.io/blog/best-online-glp1-programs-2026/); [WBOC/Ozari PR](https://www.wboc.com/online_features/press_releases/ozari-health-offers-compounded-semaglutide-from-86-per-month-and-tirzepatide-from-125-per-month/article_de6ed535-bf4f-530a-a04e-8d02a982561a.html) | S |

**Intent implications**
- "Is compounded semaglutide still legal/available/safe" is a live, anxious query family — answer it honestly; it's a trust-builder.
- Searchers who previously defaulted to compounded for price now have a $149 branded pill option; the comparison page should present "brand-name from $149" alongside compounded, not bury it.
- Provider landscape churn (Hims pivot, smaller compounders exiting) means stale review content is a CVR and compliance risk. Put "Last verified" dates on every price.

### 2.2 Manufacturer direct-to-consumer cash prices (current reference points)
| Product | Cash price | Channel | Date / source | Conf. |
|---|---|---|---|---|
| Zepbound single-dose vials | $299 (2.5 mg) / $399 (5 mg) / $449 (7.5–15 mg) | LillyDirect (Self Pay Journey; higher doses require refill within 45 days) | 1 Dec 2025 — [Lilly IR](https://lilly.gcs-web.com/news-releases/news-release-details/lilly-lowers-price-zepboundr-tirzepatide-single-dose-vials); [Fierce Healthcare](https://www.fiercehealthcare.com/marketing/lilly-joins-novo-glp-1-self-pay-price-cuts-lowering-costs-single-dose-zepbound-vials) | V |
| Zepbound KwikPen (multi-dose, 1 month/pen) | from $299 (2.5 mg); Ro lists $299/$399/$449 | LillyDirect + major retail pharmacies | FDA label exp. 23 Feb 2026; self-pay at retail 16 Mar 2026 — [Lilly IR](https://investor.lilly.com/node/53996); [therxindex Ro pricing](https://therxindex.com/guides/ro-vs-hims-weight-loss/) | V |
| Wegovy pen | $349 all doses; intro $199 for first 2 fills of 0.25/0.5 mg (through 31 Mar 2026) | NovoCare Pharmacy, telehealth partners | [NovoCare](https://www.novocare.com/obesity/products/wegovy.html); [KVIA/CNN, 5 Jan 2026](https://kvia.com/health/cnn-health/2026/01/05/starter-dose-of-wegovy-now-available-as-a-daily-pill-instead-of-weekly-injection/) | V |
| Wegovy HD 7.2 mg | $399 | NovoCare / partners | Approved 19 Mar 2026; price — [Bloomberg, 7 Apr 2026](https://www.bloomberg.com/news/articles/2026-04-07/novo-undercuts-lilly-with-high-dose-wegovy-at-399-a-month) | V |
| Wegovy pill (oral semaglutide) | $149 (1.5 mg); 4 mg $149 → $199 after 15 Apr 2026; $299 (9 & 25 mg) | NovoCare, GoodRx, retail, LifeMD, WW, Ro, Hims, Amazon | FDA 22 Dec 2025; launched 5 Jan 2026 — [PharmExec](https://www.pharmexec.com/view/novo-nordisk-wegovy-pill-becomes-first-oral-glp-available-us); [GlobeNewswire/LifeMD](https://www.globenewswire.com/news-release/2026/01/05/3212749/6480/en/LifeMD-Expands-Collaboration-with-Novo-Nordisk-as-Recognized-Telehealth-Partner-Offering-Newly-Approved-Wegovy-Pill.html) | V |
| Foundayo (orforglipron) pill | $149 (0.8 mg) / $199 (2.5 mg) / $299 (5.5 & 9 mg) / $349 (14.5 & 17.2 mg); $25 w/ commercial coverage; $50 Medicare | LillyDirect from 6 Apr 2026; retail & telehealth (Ro, WW Med+, Amazon) from 9 Apr 2026 | FDA 1 Apr 2026 — [HLTH, 13 Apr 2026](https://hlth.com/insights/news/eli-lilly-launches-oral-glp-1-drug-across-us-through-lilly-direct-telehealth-providers-2026-04-13); [PharmaShots](https://pharmashots.com/32720/eli-lilly-launches-foundayo-orforglipron-for-weight-loss-in-the-us/); [Reuters factbox via AOL](https://www.aol.com/articles/factbox-pricing-availability-novo-lillys-190720512.html) | V |
| Amazon One Medical GLP-1 program | oral from $149 cash / $25 insured; injectables (Wegovy, Zepbound) from $299 cash; $50 Medicare | Amazon Pharmacy; expanded to 48 states + DC with video care 15 Sep 2026 | [Quartz, Apr 2026](https://qz.com/amazon-one-medical-glp1-weight-loss-program-042126); [Cora](https://www.trycora.io/blog/best-online-glp1-programs-2026/) | S/V |

**Telehealth membership on top:** e.g., Ro Body $39 first month then $149/mo (or ~$74/mo annual), medication billed separately ([therxindex, Jun–Jul 2026](https://therxindex.com/guides/does-ro-have-a-membership-fee/)) **[S]**. The "all-in" number (membership + drug) is what searchers actually need and what most provider ads obscure — this is the comparison site's strongest value proposition.

### 2.3 TrumpRx / Most-Favored-Nation deals
- Nov 2025 deal with Lilly and Novo: Wegovy injectable avg $350 (from $1,349), Zepbound avg $346 / as low as $299 (from $1,088), starting doses of pills $149 if approved; target trending to ~$250 within two years; Medicare copay $50 ([NBC News](https://www.nbcnews.com/health/health-news/trump-weight-loss-drugs-cost-wegovy-zepbound-novo-nordisk-eli-lilly-rcna242309); [MobiHealthNews](https://www.mobihealthnews.com/news/white-house-partners-lilly-novo-nordisk-trumprx)) **[V]**. Exact deal date (early Nov 2025) not captured in extracts.
- TrumpRx.gov launched 5 Feb 2026 with 40+ drugs from AstraZeneca, Lilly, EMD Serono, Novo, Pfizer; Ozempic avg $350 / as low as $199 ([HIT Consultant, 5 Feb 2026](https://hitconsultant.net/2026/02/05/health-policy-trumprx-gov-launch-ozempic-wegovy-price-cuts-mfn/); [Pharmaceutical Technology](https://www.pharmaceutical-technology.com/news/trumprx-launches-to-slash-drug-prices-for-cash-paying-us-patients/)) **[V]**.
- "TrumpRx" is now a navigational/brand query in its own right. Note TrumpRx is a price/referral portal; patients still need a prescription — a natural hand-off for a comparison site ("TrumpRx price + where to get prescribed").

### 2.4 Oral GLP-1s & pipeline
- Wegovy pill: first oral GLP-1 for chronic weight management (and CV risk reduction), 16.6% mean loss at 64 weeks ([HLTH](https://hlth.com/insights/news/the-149-disruptor-goodrx-weightwatchers-lifemd-scale-wegovy-access-2026-01-06)) **[S]**.
- Foundayo (orforglipron): once-daily, no fasting requirement **[S]**.
- Wegovy HD (7.2 mg): 20.7% at 72 wks; dysesthesia 22% vs 6% at 2.4 mg ([HCPLive](https://hcplive.com/view/fda-approves-higher-dose-semaglutide-wegovy-hd-injection-7-2-mg-for-obesity)) **[V]**.
- CagriSema PDUFA expected Oct 2026 ([findhonestcare tracker](https://www.findhonestcare.com/metabolic-innovations/cagrisema/fda-timeline/); [therxindex](https://therxindex.com/guides/cagrisema-fda-approval-status/)) **[U — tracker sites only; watch for news this month; a launch would create a new branded query cluster]**.
- Retatrutide: TRIUMPH-1 ~28% loss presented ADA Jun 2026; filing expected late 2026/Q1 2027 ([midgardfinance calendar](https://www.midgardfinance.com/obesity/calendar/)) **[U]**. Not approved — do not bid.

### 2.5 Demand signals
- 11% of US adults currently using a GLP-1 for weight loss in 2026 vs 3% in 2024 (cited in [Becker's "5 GLP-1 updates"](https://beckershospitalreview.com/glp-1s/5-glp-1-updates-to-know)) **[S]**.
- Search interest: Ozempic searches −26% YoY while tirzepatide +138%, Zepbound +109%, retatrutide +196% ([Athletech News](https://athletechnews.com/top-glp-1-cities-usa)) **[S]**. Obesity-drug search interest up 25x over a decade (ICO 2026, [The Limbic](https://thelimbic.com/?p=20730053)) **[S]**. Implication: brand-name and tirzepatide queries are growing; generic "Ozempic" intent is decaying.
- Geographic hot spots for GLP-1 interest: Orlando, Miami, Atlanta; fastest growth Cape Coral, Riverside, Anaheim ([Athletech News](https://athletechnews.com/top-glp-1-cities-usa)) **[S]** — candidate geo bid modifiers to test.

---

## 3. Google Ads policy constraints

### 3.1 The rules that matter (US)
1. **Prescription drug terms — Oct 2025 update.** From 29 Oct 2025 Google's Healthcare & Medicines policy changed: for campaigns targeting the US, Canada and NZ, Rx drug terms may be used promotionally in **ads and landing pages** per local law, and **you do not need certification to use them in ad text/landing pages — but you must be certified to keyword-target them**. Certification is also required by business type (online pharmacies, telemedicine providers, pharma manufacturers). Enforcement ramped over 4–6 weeks with ≥7-day warnings before suspension ([Search Engine Roundtable](https://www.seroundtable.com/google-ads-prescription-drug-terms-policy-40272.html); [Search Engine Land](https://searchengineland.com/google-certification-prescription-drug-advertising-463409); [Google: Restricted drug terms](https://support.google.com/adspolicy/answer/15595717?hl=en); [Google: Update Oct 2025](https://support.google.com/adspolicy/answer/16551459?hl=en)) **[V — via search extracts; read the Google pages directly before acting]**.
2. **Online pharmacy / telemedicine / prescription drug services** require certification; accepted certifiers: LegitScript Healthcare Merchant Certification, NABP VIPPS, NABP .pharmacy ([Google: Prescription drug services](https://support.google.com/adspolicy/answer/15598647?hl=en)) **[V]**. Google applies the policy cautiously to landing pages that "link or refer to content that in any way appears to be or to facilitate the online prescription, dispensation or sale of medicines" ([stubgroup summary](https://stubgroup.com/glossary/healthcare-and-medicines-policy/)) **[S]** — i.e., an affiliate page whose CTAs go to telehealth prescribers is in scope.
3. **LegitScript categories include "price comparison websites/apps"** (Category A tier; one-time ~$535 + ~$1,070/yr per older fee schedule; telemedicine tier ~$1,050 + $2,150/yr per site) ([LegitScript fact sheet](https://www.legitscript.com/healthcare-certification-factsheet); [LegitScript telemedicine fact sheet 2024](https://www.legitscript.com/wp-content/uploads/2024/10/Healthcare-Certification-FactSheet-Telemedicine_-CHM-PC004-FSE-22.pdf)) **[S — fees may have changed]**. LegitScript also requires a certified merchant's affiliates/partners to comply with its standards.
   - **Open question (critical, unverified):** whether a *telehealth-provider* comparison/affiliate site (vs. a drug-price comparison site like GoodRx) is eligible for LegitScript + Google certification that unlocks Rx keyword targeting. **Action:** client to confirm (a) current certification status, (b) which Google certification type is on the account, (c) LegitScript's view of the site's model. If uncertified, cluster D, most of C, E and H keywords (🔒) are unbuyable; the account must live on ✅ keywords (brand-of-provider, "best online weight loss program", "medical weight loss online", "weight loss pill", "weight loss program that takes insurance") and let broad/AI Max matching be *policy-checked*, not assumed.
4. **Unapproved substances / compounded drugs.** Google requires LegitScript certification for any compounded Rx advertiser in the US; uncertified compounded GLP-1 ads are disapproved ([Visionary Marketing case study](https://visionary-marketing.co.uk/case-studies/biopreventative-glp-1-google-ads-legitscript-compliance)) **[S]**. Don't bid on peptides/research-chemical/retatrutide terms.
5. **Weight-loss content restrictions.** No before/after images for weight loss; no unsubstantiated health claims; heightened enforcement for compounded meds, weight-loss drugs, telehealth prescribing; enforcement tightened Aug 2025 (retired "Restricted Medical Content" label) ([OuterBox](https://www.outerboxdesign.com/articles/digital-marketing/health-and-wellness-advertising-restrictions-on-google-ads-keeping-your-campaigns-compliant/); [Google Healthcare & medicines](https://support.google.com/adspolicy/answer/176031?hl=en)) **[S]**.
6. **Personalized advertising (remarketing, Customer Match, custom segments)** cannot target physical health conditions/treatments, and ads must not body-shame or imply knowledge of the user's condition ([Accelerated Digital Media 2026 guide](https://www.accelerateddigitalmedia.com/insights/health-policies-and-restrictions-guide-for-google-ads-microsoft-ads-2026/)) **[S]**. Practical consequence: the classic "browse on mobile → retarget → convert on desktop" loop is largely unavailable; the first session must do the work (or capture an email with clear consent — handled under HIPAA/FTC Health Breach Notification considerations, outside this doc).
7. **Destination requirements / "insufficient original content".** Bridge pages that exist only to pass clicks to another site are flagged; pages must provide unique, useful content and not immediately redirect ([Google: Insufficient original content](https://support.google.com/adspolicy/answer/16427718); [Google: Destination requirements](https://support.google.com/adspolicy/answer/6368661)) **[V]**. This is good news for a genuinely editorial comparison page and a warning against thin "pre-lander" variants in CRO tests.
8. **Trademarks.** Bidding on competitor/partner brand keywords is generally allowed by Google, but trademark owners can restrict their mark in ad text; affiliate agreements frequently forbid brand bidding and direct-linking. **[U — general industry knowledge; check each partner's IO]**.

### 3.2 Regulatory overlay beyond Google (affects landing-page copy)
- **FDA (via the provider ecosystem):** "sameness" claims ("same active ingredient as Wegovy", "generic semaglutide"), "clinically proven" for compounded products, and branding that hides the compounder are the specific failures cited in 2025–26 warning letters ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/09/fda-hhs-taking-action-against-telehealths-compounded-drug-advertising); [Pharmaceutical Commerce](https://www.pharmaceuticalcommerce.com/view/fda-issues-30-warning-letters-to-telehealth-firms-over-misleading-compounded-glp-1-marketing)). FDA's jurisdiction over a third-party comparison site is indirect, but repeating a provider's non-compliant claims puts the site's Google account and partner relationships at risk.
- **FTC:** NextMed (Jul 2025) — deceptive "$79 first month" pricing that omitted drug/lab/membership costs, fake before/after photos, non-customer testimonials, incentivized/suppressed reviews, unsubstantiated "average 53 lb" claims, cancellation obstruction ([Foley](https://www.foley.com/insights/publications/2025/08/health-care-marketing-enforcement-ftc-targets-telehealth-company-for-deceptive-w/); [Frier Levitt](https://www.frierlevitt.com/articles/ftcs-nextmed-settlement-signals-enforcement-against-telemedicine-companies-making-false-or-misleading-drug-claims/)) **[V]**. The FTC Endorsement Guides and Consumer Reviews rule apply to affiliate rankings and star ratings. The National Consumers League petitioned the FTC on compounded GLP-1 advertising in Sep 2025 ([NCL PDF](https://nclnet.org/wp-content/uploads/2025/09/NCL-Petition-to-the-FTC-on-Deceptive-FTC-Adverising-of-Compounded-GLP-1-Drugs-09.22.2025.pdf)) **[S]**.

### 3.3 Landing-page copy implications (do / don't)
| Do | Don't |
|---|---|
| Label each option "FDA-approved brand" or "Compounded — not FDA-approved" | "Same as Wegovy", "generic Ozempic", "same active ingredient", "clinically proven" for compounded |
| Show all-in monthly price (drug + membership + labs) and the maintenance-dose price | Headline only an intro/starter price |
| "A licensed clinician will determine if treatment is appropriate" | "Guaranteed approval", "no doctor visit needed", "get Ozempic today" |
| Cite trial results with dose and duration, like-for-like comparisons | Cross-dose comparisons (the Novo v. Lilly issue); unsourced "lose 50 lbs" |
| Visible affiliate disclosure + ranking methodology + review sources | Fake/unsourced testimonials, before/after photos, body-shaming |
| Link to safety info / boxed warning (thyroid C-cell tumor risk for GLP-1s) | Burying risk info |
| Name the dispensing pharmacy type (503A/503B/manufacturer) where known | Implying the telehealth brand manufactures the drug |
| Keep provider facts dated ("Verified Oct 2026") | Static review copy from 2025 (Hims, others have changed offerings) |

---

## 4. Desktop vs mobile behavior (health comparison)

### Evidence
- **Health & wellness landing pages:** mobile brings ~7x more traffic than desktop, but desktop converts ~22% better (Unbounce Conversion Benchmark Report 2024, 57M conversions) ([Unbounce](https://unbounce.com/conversion-benchmark-report/healthcare-wellness-conversion-rate); [Hartzer summary](https://www.hartzer.com/blog/unbounce-2024-conversion-benchmark-report/)) **[V]**. Unbounce attributes the gap to desktop-first design and to higher-consideration purchases shifting to larger screens.
- **Telemedicine sites:** ~72% of traffic from mobile; medical practice sites 68.5% mobile / 29.2% desktop; health insurance 61.4% mobile with desktop still converting for enrollment ([CUFinder telemedicine](https://cufinder.io/blog/benchmarks/telemedicine/); [CUFinder health insurance](https://cufinder.io/blog/benchmarks/health-insurance/)) **[S — aggregator, methodology unclear]**.
- **Google paid search:** mobile has held the majority of Google paid clicks since 2016–17 (Merkle: 62% mobile incl. tablet) ([MarketingCharts](https://www.marketingcharts.com/online/smartphones-reportedly-accounted-for-a-majority-of-google-search-ad-clicks-in-q4-74118/)) **[V but dated; current share likely higher — verify in client account]**.
- **Comparison UX:** Baymard — remove identical attributes, group attributes, persist column headings, horizontal row styling; on mobile, horizontal scrolling of comparison matrices is unnatural; keep titles/price/CTA fixed and collapse detail behind "show more" ([Baymard](https://baymard.com/blog/user-friendly-comparison-tools); [Foolproof](https://foolproof.co.uk/journal/making-product-comparison-work-on-mobile)) **[V]**.

### Behavioral model for this vertical (analysis — test, don't assume)
| Dimension | Desktop | Mobile |
|---|---|---|
| Typical query | Longer, research-y ("ro vs hims cost per month with insurance", "does medicare cover zepbound") | Shorter, brand/price ("wegovy pill price", "hims weight loss") |
| Session context | Work/home, multi-tab comparison, reads tables and fine print | Fragmented, often after a social video/ad or TV exposure; skims to price + CTA |
| Demographic skew | Older (Medicare-eligible cluster E skews desktop) | Younger, more cash-pay/pill-curious |
| Trust needs | Methodology, sources, disclosures read more | Need *compressed* trust: rating, "LegitScript certified", "FDA-approved" badge, # reviews |
| Conversion path | Click-out to provider and completes intake in-session more often | Click-out, then provider's long medical intake on a phone (often 10–20 questions + ID + payment) → higher abandonment downstream; retargeting is restricted by Google personalized-ads policy |
| Page pattern | Side-by-side table (3–5 columns), sticky header with price+CTA | Stacked cards ranked; one primary CTA per card; sticky bottom CTA; filter chips; tap-to-expand details; no horizontal-scroll table |
| Measurement | Click-out CTR ≈ OK proxy | Click-out CTR overstates; need partner postbacks (approved/started) by device |

### Implications for the mobile launch
1. Build a mobile-native layout (cards + sticky CTA + 3-question qualifier), not the desktop table shrunk. Keep price and the FDA-approved/compounded label visible on each card without expansion.
2. Expect lower lead-to-approval on mobile because the provider's intake is the friction point; set device-level bid adjustments from *partner-confirmed conversions*, not click-outs.
3. Since remarketing on health conditions isn't allowed, consider a consented "email me this comparison" or "text me the price table" save-for-later — subject to legal review (FTC Health Breach Notification Rule, state health-privacy laws such as Washington's My Health My Data Act **[U — flag for counsel]**).
4. Prioritize mobile on clusters that are naturally mobile and short (brand, "wegovy pill price", "weight loss pill") and keep insurance/Medicare and "vs" research clusters desktop-weighted initially.
5. Page speed matters more on mobile; comparison pages with heavy JS tables and partner logos/scripts are common LCP offenders — measure CWV by template.

---

## 5. Open items / what we could not verify
- Google policy pages and FDA press releases were not readable directly (proxy-blocked); content is from search-result extracts. Re-read: Google answers 15595717, 16551459, 15598647, 176031, 16427718.
- Whether the client is (or can be) LegitScript/Google-certified as a comparison site for telehealth — **highest-priority question**.
- Exact current NovoCare Wegovy pen price after Mar 2026 intro offer ended (likely $349; verify) and whether Wegovy pill 4 mg moved to $199 as scheduled (reported, verify).
- CagriSema approval (PDUFA ~Oct 2026) and any Q4 2026 price moves — re-check before finalizing ad copy.
- Prescribing-label eligibility criteria (BMI thresholds, indications) stated from analyst knowledge — confirm against current PI.
- Keyword volumes/CPCs — need Keyword Planner + client Search Terms data.
- Device split and CVR for *this* site — need GA4/Ads segment exports (see DATA_REQUEST.md).
