# Home security: what buyers say in reviews

Research date: 2026-11-02. Coded data: `home-security/data/reviews/reviews_coded.csv` (165 rows, one per quote). Codebook: `research/CODEBOOK.md`.

## Read this first: how the data was gathered and what it can't tell you

- **165 coded quotes across 13 brands.** That is above the 150 target, but it is a thin sample per brand. Abode, Arlo, Wyze, Cove and Xfinity have 6 to 11 quotes each. Deep Sentinel has 3 and Kangaroo has 2. Treat the brand-level shares as hints, not measurements.
- **No pages were read directly.** Trustpilot, Reddit, ConsumerAffairs and BBB are blocked on this network. sitejabber.com and pissedconsumer.com did not resolve, so no other review sites were fetched. Every quote came from web-search result snippets.
- **Quotes are verbatim fragments, not full reviews.** I kept only text that was clearly the reviewer's own words, such as first-person lines or lines with the reviewer's own typos. I dropped anything the search engine had paraphrased. Some quotes are short pieces of longer reviews.
- **URLs are sometimes approximate.** When one search result cited several pages, the URL in the row is the most likely page for that quote, not a confirmed one.
- **No Reddit data.** Reddit threads never appeared in search results. The "other" source (21 rows) covers Ring and Xfinity community forums, Home Depot, Best Buy, Google Play, the App Store, Yelp, Slickdeals and one tech blog.
- **Strong negative skew.** 68% of rows are negative (112), 29% positive (48) and 3% mixed (5). Three things push it that way. Complaint sites draw complaints: BBB is mostly complaints, and ConsumerAffairs and PissedConsumer lean negative. My search terms often named problems ("cancel", "false alarm", "price increase"). And search snippets favor dramatic lines. So the data shows **where things break**. It does not show how often they break for the typical buyer.
- **Much of each row is "unknown".** Most reviews don't say whether the writer owns or rents, how the system was installed, or what led them to buy. Only 2 rows say "owner", only 41 say DIY or pro install, and only 4 have a date. The stage mix below is mostly "unknown" for that reason.
- **Some ratings are second-hand.** Where a rating came from a review site quoting Trustpilot or BBB rather than from the page itself, the table says so. Country mirrors of the same Trustpilot page (uk., ca., au.) showed slightly different scores and counts because they were captured on different dates.

## Brand by brand

"Top complaint share" means the share of that brand's negative quotes that carry the fear code. One quote can carry more than one fear.

### ADT (18 quotes: 14 negative, 3 positive, 1 mixed)
| | |
|---|---|
| Ratings | **BBB:** 10,742 complaints in 3 years, 3,472 in the last 12 months (Boca Raton profile, Nov 2026). Central Florida profile: 1.07/5 from 2,811 reviews. **Trustpilot (US):** no score in snippets. About 4,400–5,200 reviews; Trustpilot's AI summary of 617 recent reviews says most were let down. (ADT UK shows 4.5 from ~36k reviews, but that is a different business.) **ConsumerAffairs:** ~21,000 reviews, score not shown. **BestCompany:** 4.1/167 (ADT), 593 reviews (ADT-Monitored), 3.2/144 (ADT Self Setup). |
| Where it breaks | **Cancelling: 43% of negatives (6 of 14).** Contract lock-in, price hikes and early-termination fees come next. "charged $6,662.38 for early termination fees and a balance for a five year contract" · "renews automatically every 30 days once the contract has expired" |
| What happy reviewers praise | The technician who explains the system, and peace of mind. "explained every step, ensuring I understood how to operate the system" · "ADT has given me peace of mind when I am home alone" |

### SimpliSafe (30 quotes: 18 negative, 10 positive, 2 mixed)
| | |
|---|---|
| Ratings | **Trustpilot:** 3.5 from ~16,800–16,944 reviews (country mirrors, Nov 2026). One snippet shows 3.3 for the US page. SafeWise cites 2.5 from 16,000+. **BBB:** 579 complaints in 3 years, 178 in 12 months. **BestCompany:** 3.5 from 200+ reviews (another page shows 3.3, with 30% one-star). **ConsumerAffairs:** score not shown. |
| Where it breaks | **Equipment failing: 39% of negatives (7 of 18). False alarms and police fines: 28% (5 of 18).** "A month later I received a $316 false alarm fine from the LAPD." · "the camera does NOT work with 5G network. Had to return camera." |
| What happy reviewers praise | Monitoring that calls back in seconds. "called my cell within 30 seconds" · "the police caught them because of the quick response on their monitoring" |

### Ring Alarm (17 quotes: 11 negative, 6 positive)
| | |
|---|---|
| Ratings | **Trustpilot (US):** 1.2–1.5 from ~3,100–4,600 reviews (mirrors and dates vary). **ConsumerAffairs:** 1.3 from 384–386 reviews (Oct 2026). **BBB:** no score in snippets. |
| Where it breaks | **Hidden fees or subscription surprises: 36% of negatives (4 of 11). The monitoring center not calling: 36% (4 of 11).** "a doubling of cost for the same service" · "Ring will call *any time* the alarm is triggered -- there is no caveat that the alarm must sound for over 1 minute." |
| What happy reviewers praise | Fast DIY setup and no required monthly fee. "incredibly easy to set up. You just take it out of the box, install the app, and follow directions." · "there is no monthly fee unless you want professional monitoring" |

### Vivint (25 quotes: 13 negative, 11 positive, 1 mixed)
| | |
|---|---|
| Ratings | **BBB:** B grade, accredited since Aug 2024. About 9,500 complaints in 3 years. About 2,500 reviews averaging ~1.06 (secondary summary, 2026). **ConsumerAffairs:** 4.4 from 39,274 reviews. **Trustpilot:** 3.8 from 49,000+ (SafeWise) or 3.8 from 67,823 (another secondary source). **BestCompany:** 8,453 reviews. |
| Where it breaks | **Equipment and app failing: 38% of negatives (5 of 13). Fees nobody mentioned: 31% (4 of 13).** Long contracts sold door to door and contracts that follow you after a move come next. "No one mentioned a 5-year contract or an early termination fee — not once during the sales process." · "Vivint did not let me out of my old contract so I payed for a home I no longer owned." |
| What happy reviewers praise | The app and the technician. Vivint has the most positive quotes of any brand. "the app is very, very easy to use" · "the technician was fast and knowledgeable" |

### Brinks Home (14 quotes: 10 negative, 4 positive)
| | |
|---|---|
| Ratings | **Trustpilot (US):** 3.2 from 7,703 reviews (other mirrors show 3.8–4.0 from ~7,660). **BBB:** grade given as A+ or A- depending on the source. Customer reviews average ~1/5 (Cybernews, 2026). **ConsumerAffairs:** 5,314 reviews (2023 page title). **BestCompany:** ~4,400 reviews. |
| Where it breaks | **Cancelling and contract lock-in: 40% of negatives each (4 of 10).** "every time you call for something they add another 2/3 years to the contract" · "could not cancel without a 1400 dollar buyout" |
| What happy reviewers praise | Individual reps and technicians who fix things fast. "in a matter of minutes everything was back working" |

### Frontpoint (12 quotes: 8 negative, 4 positive)
| | |
|---|---|
| Ratings | **Trustpilot (US):** 3.5 TrustScore (3.6 average) from ~13,000 reviews. **BBB:** A+ grade. **BestCompany:** 4.1 from 3,203 reviews (54% five-star, 8% one-star). **Yelp:** 2.7 from 1,259. **PissedConsumer:** 1.8 from 81. |
| Where it breaks | **Cancelling: 50% of negatives (4 of 8).** "$788.74 to cancel my service" · "an extra month is charged after signing terms, and they offer half price to stay" |
| What happy reviewers praise | Quick self-install guided by the app. "the app walked me through the whole thing" · "the installation took 30 minutes total" |

### Cove (11 quotes: 8 negative, 3 positive)
| | |
|---|---|
| Ratings | **Trustpilot:** 4.5–4.6 from ~8,600–9,000 reviews (country mirrors, 2026). **BBB:** B grade, but customer reviews average 1.14 from 70+ (Cybernews, 2026). **ConsumerAffairs:** 1.7 from 156. **BestCompany:** 4.5 from 345 (BestCompany takes referral fees). Cove's scores differ more from site to site than any other brand's. |
| Where it breaks | **Equipment failing: 50% of negatives (4 of 8).** False alarms and missed calls come next. "the control panel doesn't operate as intended... There are no options to update so it continues to malfunction." · "I didn't get any such call." |
| What happy reviewers praise | Low price compared with the big brands, and support reps. "the price is much less than ADT and Vivint." · "the Cove Customer Service reps are outstanding" |

### Abode (10 quotes: 5 negative, 4 positive, 1 mixed)
| | |
|---|---|
| Ratings | **Trustpilot:** 2.5 from 2,895 (another mirror shows 2.2). July 2026 roundups show 2.4–2.6. **ConsumerAffairs:** 4.3 from only 21 reviews. **BBB:** B or C grade, depending on the source. |
| Where it breaks | **Equipment failing: 60% of negatives (3 of 5).** "cameras go offline constantly and have to be reset in person" · "blared for 5 minutes straight, no call from Abode monitoring" |
| What happy reviewers praise | Smart-home links (HomeKit, Alexa) and flexible plans. "integrates nicely into Apple HomeKit" · "the ability to change my service level as I need to" |

### Arlo (6 quotes: 5 negative, 1 positive)
| | |
|---|---|
| Ratings | **Trustpilot (my.arlo.com, US):** 1/5 (count not shown). A secondary guide cites 2.6. The UK page has 437 reviews, mostly unhappy. **ConsumerAffairs and BBB:** no score found. |
| Where it breaks | **Features locked behind a subscription: 60% of negatives (3 of 5).** "bait (buy new cameras) and switch (not usable without subscription package)" |
| What happy reviewers praise | Easy camera setup. "Decent cameras and door bell, easy to mount and charge." |

### Wyze (10 quotes: 8 negative, 2 positive)
| | |
|---|---|
| Ratings | **Trustpilot (US):** no score in snippets. AI summary of 232 reviews says "somewhat happy". **ConsumerAffairs and BBB:** no score found. |
| Where it breaks | **Cameras going offline: 50% of negatives (4 of 8).** "failed to notify me of who was in my house because they constantly go offline" |
| What happy reviewers praise | Fast free replacements. "Wyze support assisted me and sent me a brand new replacement camera free of charge. I received the replacement within 2 days of the support ticket." |

### Xfinity Home (7 quotes: all negative)
| | |
|---|---|
| Ratings | **ConsumerAffairs:** about 1–1.3 (secondary summaries). Most Xfinity reviews online are about internet and TV, not Home. **BBB (Comcast):** grade reported as anything from C+ to A+. |
| Where it breaks | **Cancelling and surprise bills: 43% of negatives each (3 of 7).** "I was charged the balance for the equipment, even though it was returned at the local xfinity store, and I have the receipt to prove it." · "every little change you make to your account your home security contract starts over" |
| What happy reviewers praise | No positive Xfinity Home quotes were found. |

### Deep Sentinel (3 quotes) and Kangaroo (2 quotes): too thin to judge
- **Deep Sentinel:** Trustpilot ~2.6 from only 4 reviews (2022–Feb 2025). Yelp has 43 reviews (no score in snippet). All 3 quotes say guards did not act or video would not play: "guards ignore trespassers frequently". Independent testers (Security.org, SafeHome) did report guards answering in 20–30 seconds, but those are expert tests, not customer reviews, so they are not coded.
- **Kangaroo:** Trustpilot has 26–28 reviews: 57% one-star, 39% five-star. Kangaroo does not invite reviews. Both quotes are negative, about hardware life and support with no human: "does not employ a human that one can interact with".

## Pooled: what buyers need and what they fear

Base: all 165 quotes. One quote can carry several codes, so shares add up to more than 100%.

**Needs (% of all items)**
| Need | Items | % of all |
|---|---|---|
| HUMAN (a real, reachable person) | 35 | 21% |
| RELIABLE (it works, every time) | 31 | 19% |
| CAMERAS | 21 | 13% |
| PRICE_CLARITY | 19 | 12% |
| FAST_RESPONSE (someone calls fast) | 16 | 10% |
| APP | 16 | 10% |
| NO_CONTRACT | 12 | 7% |
| NO_SUBSCRIPTION | 11 | 7% |
| EASY_SETUP | 8 | 5% |
| PEACE_OF_MIND | 5 | 3% |

Among the 48 **positive** quotes, the top needs are HUMAN (18, 38%), APP (10, 21%) and EASY_SETUP (8, 17%).

**Fears**
| Fear | Items | % of all 165 | % of 112 negative |
|---|---|---|---|
| EQUIPMENT_FAILS | 39 | 24% | 34% |
| CANCEL_HARD | 26 | 16% | 23% |
| HIDDEN_FEES | 24 | 15% | 21% |
| TRAPPED_CONTRACT | 14 | 8% | 12% |
| NO_RESPONSE | 14 | 8% | 12% |
| FALSE_ALARM | 8 | 5% | 7% |
| PRICE_HIKE | 5 | 3% | 4% |
| BAD_INSTALL | 5 | 3% | 4% |
| PUSHY_SALES | 4 | 2% | 3% |
| PRIVACY | 1 | 1% | 1% |

**Fears grouped into three clusters (share of 112 negative items, each item counted once per cluster):**
- **Money and exit traps** (cancelling, hidden fees, contract, price hike): **53 items, 47%**
- **Hardware or app fails:** 38 items, 34%
- **Monitoring lets you down** (no call, or a false alarm): 20 items, 18%

The weight-loss study found a large privacy fear. Here, privacy barely shows up in reviews (1 item). It is in the news (Ring's police and Flock partnerships), but reviewers don't write about it.

## Stage mix

| Stage | Items | % |
|---|---|---|
| unknown | 144 | 87% |
| after_incident (break-in, scare) | 11 | 7% |
| switch (names a previous provider) | 5 | 3% |
| moving (new home) | 4 | 2% |
| renew (contract ending) | 1 | 1% |
| first (first system) | 0 | 0% |

Most reviews don't say why the person bought. Among the 21 that do, after-incident buyers are the largest group, and 7 of their 11 quotes are negative: the system failed or no one called. All 4 moving quotes are negative, and each one is about a contract or billing that followed the buyer to the new home. With these counts, read this table as a direction only.

## Seven findings for the comparison page

**1. The biggest fear is not getting out: 47% of negative items are about cancelling, hidden fees, contract lock-in or price hikes.**
On a mobile comparison page, put "contract length", "cancel online?" and "early-termination fee" in the first card, not in the fine print. Brands sold by door-to-door reps or on long contracts (ADT, Vivint, Brinks, Frontpoint, Xfinity) produce almost all of these quotes.
> "No one mentioned a 5-year contract or an early termination fee — not once during the sales process." (Vivint, Trustpilot)
> "$788.74 to cancel my service" (Frontpoint, Trustpilot)

**2. "Will it actually work?" is the largest single fear: EQUIPMENT_FAILS is in 34% of negatives.**
It shows up for every brand, and DIY camera brands (Wyze, Abode, Arlo, Cove) are hit hardest at 50–60% of their negatives. A comparison page can answer this with warranty length, battery and cellular backup, and replacement policy for each brand.
> "cameras go offline constantly and have to be reset in person" (Abode, Trustpilot)
> "Doorbell cameras themselves never once survived an entire year" (Kangaroo, Google Play)

**3. A reachable human is the top need: 21% of all items, and 38% of positive items.**
Happy reviewers praise a named tech or a rep who fixed things fast. Angry reviewers complain about bots, holds and transfers. Show phone support hours and whether there is live chat, and list "pro install available" as a feature, not a cost.
> "explained every step, ensuring I understood how to operate the system" (ADT, ConsumerAffairs)
> "does not employ a human that one can interact with" (Kangaroo, Best Buy)

**4. "No monthly fee" cuts both ways: 9 of the 11 NO_SUBSCRIPTION items are negative.**
Every one of the 11 is about a DIY brand (Ring, Wyze, Arlo, SimpliSafe). Buyers feel tricked when remote arming, video history or support turn out to need a plan. The page should show plainly what works with $0/month and what doesn't.
> "disabled without monthly subscription" (Ring, Home Depot)
> "there is no monthly fee unless you want professional monitoring" (Ring, Home Depot)

**5. Monitoring is judged in seconds: 18% of negatives are a missed call or a false alarm.**
Positive monitoring quotes name a time ("seconds", "30 seconds"). Negative ones are "no one called" or a police fine. Response time and how false alarms are handled (verification call, cancel from app) belong in the comparison.
> "called my cell within 30 seconds" (SimpliSafe, BestCompany)
> "A month later I received a $316 false alarm fine from the LAPD." (SimpliSafe, ConsumerAffairs)

**6. The price has to stay the price: 12% of items ask for price clarity, and price-hike quotes come with real numbers.**
Buyers remember exact figures: $40 to $70 at ADT, Ring "doubled". Show the all-in monthly cost (monitoring + cameras + equipment financing) and say whether the price is locked.
> "When I started, the service cost me about $40 a month, but now, two years later, it's jumped to over $70." (ADT, ConsumerAffairs)
> "rate still more than doubled at year 1 and is now at $29.99 per month" (Ring, Trustpilot)

**7. Star ratings conflict across sites, so a single "4.5 stars" badge can mislead.**
Cove has 4.5 on Trustpilot, 1.7 on ConsumerAffairs and 1.14 from BBB reviewers. Vivint has 4.4 on ConsumerAffairs and ~1.06 on BBB. ADT has 10,742 BBB complaints in 3 years. Buyers who check one more site will find a different number. Showing two sources per brand, with dates, builds more trust than one badge. Positive quotes like the one below show what the high ratings reward.
> "the price is much less than ADT and Vivint." (Cove, ConsumerAffairs)
> "the app is very, very easy to use" (Vivint, ConsumerAffairs)

## Sources

### Rating and count pages (as seen in search results, 2026-11-02)
- https://www.trustpilot.com/review/adt.com
- https://ie.trustpilot.com/review/www.adt.co.uk (ADT UK, for contrast)
- https://www.bbb.org/us/fl/boca-raton/profile/burglar-alarm-systems/adt-security-services-0633-30001337/complaints
- https://bbb.org/us/fl/orlando/profile/security-system-monitors/adt-security-services-inc-central-florida-0733-100365/customer-reviews
- https://www.consumeraffairs.com/homeowners/adt.htm
- https://bestcompany.com/home-security/adt/reviews
- https://bestcompany.com/home-security/blue-by-adt
- https://www.trustpilot.com/review/simplisafe.com
- https://www.bbb.org/us/ma/boston/profile/burglar-alarm-systems/simplisafe-inc-0021-129235/complaints
- https://bestcompany.com/home-security/simplisafe/reviews
- https://www.safewise.com/home-security-systems/adt/alternatives/ (cites SimpliSafe and Vivint Trustpilot figures)
- https://www.trustpilot.com/review/ring.com
- https://www.consumeraffairs.com/homeowners/ring.html
- https://www.consumeraffairs.com/homeowners/ring-vs-simplisafe.html
- https://www.bbb.org/us/ut/lehi/profile/security-systems/vivint-smart-home-1126-1000179796/customer-reviews
- https://www.consumeraffairs.com/homeowners/apx_alarm.html
- https://bestcompany.com/home-security/vivint/reviews
- https://www.trustpilot.com/review/brinkshome.com
- https://www.bbb.org/us/tx/dallas/profile/burglar-alarm-systems/brinks-home-0875-90346299
- https://cybernews.com/best-home-security-systems/brinks-review/
- https://bestcompany.com/home-security/brinks-home-security/reviews
- https://www.trustpilot.com/review/www.frontpointsecurity.com
- https://bestcompany.com/home-security/frontpoint/reviews
- https://www.yelp.com/brands/frontpoint-home-security
- https://frontpoint-security.pissedconsumer.com/review.html
- https://www.trustpilot.com/review/covesmart.com
- https://cybernews.com/best-home-security-systems/cove-review/
- https://www.consumeraffairs.com/homeowners/cove.html
- https://bestcompany.com/home-security/cove/reviews
- https://www.reviews.org/home-security/adt-vs-cove-home-security/
- https://www.trustpilot.com/review/goabode.com
- https://www.consumeraffairs.com/homeowners/abode.html
- https://www.topconsumerreviews.com/best-canadian-home-security/reviews/abode.php
- https://www.securitysystemsreview.com/consumer-reviews/abode/
- https://www.trustpilot.com/review/my.arlo.com
- https://uk.trustpilot.com/review/arlo.com/en_gb
- https://www.trustpilot.com/review/www.wyze.com
- https://www.consumeraffairs.com/homeowners/xfinity-home.html
- https://www.trustpilot.com/review/www.deepsentinel.com
- https://www.yelp.com/biz/deep-sentinel-pleasanton
- https://www.trustpilot.com/review/heykangaroo.com

### Pages quoted in the coded data
Each row's `url` column holds the page for that quote. The CSV contains 116 unique URLs, and the main ones are:
- ConsumerAffairs: adt.htm (pages 3, 5, 7, 10, 16, 73, 80, 97, 102), simplisafe.html (pages 3, 4, 5), apx_alarm.html (Vivint), monitronics.html (Brinks), cove.html, frontpoint-security.html, ring.html, abode.html, xfinity-home.html, wyze.html
- Trustpilot: adt.com, simplisafe.com, ring.com, vivint.security, brinkshome.com, frontpointsecurity.com, covesmart.com, goabode.com, my.arlo.com, wyze.com, xfinity.com (plus country mirrors)
- BBB: ADT (Boca Raton), SimpliSafe (Boston), Brinks Home (Dallas), Arlo (Orlando)
- BestCompany: ADT, ADT Pulse, SimpliSafe, Vivint, Cove, Frontpoint
- Other: community.ring.com (3 threads), forums.xfinity.com, homedepot.com (Ring Alarm kits), bestbuy.com (Kangaroo), play.google.com (Kangaroo), apps.apple.com (Deep Sentinel), yelp.com (Deep Sentinel), slickdeals.net (Wyze), terrywhite.com (Ring vs SimpliSafe)

### Not reachable from this network
trustpilot.com, reddit.com, consumeraffairs.com and bbb.org were blocked for direct fetch. sitejabber.com and pissedconsumer.com did not resolve. To read full reviews (with stars, dates and owner/renter details) and reduce the snippet bias, those hosts need to be allowed in the session's network settings.
