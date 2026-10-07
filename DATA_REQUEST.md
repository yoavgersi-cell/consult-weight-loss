# Data Request — what to get from the client

Ordered by how much it unlocks. Drop files into the matching `data/` folder.

## 1. Google Ads (→ `data/campaigns/`)
- **Search terms report**, last 90 days, with impressions, clicks, cost, conversions. This is the single most important file: it shows what users are actually looking for.
- Keyword list with match types, QS (and its 3 components), CPC, conv. rate
- Campaign / ad group structure and the landing page URL for each ad group
- Ad copy (RSAs) and asset performance labels
- Device, hour-of-day, and geo segments
- What counts as a "conversion": click-out? partner lead? partner sale? Which one is imported into Ads?

## 2. Partner / revenue data (→ `data/campaigns/`)
- Partners listed, payout model (CPA / CPL / rev-share) and payout per partner
- Click-out → partner conversion rate per partner (EPC = earnings per click-out)
- Any partner caps, geo limits, or required compliance copy

## 3. On-site analytics (→ `data/analytics/`)
- GA4 (or other) access: landing → scroll → click-out funnel, broken down by device and by position in the list
- Click-out share by rank position and by CTA type (button vs logo vs "read review")
- Heatmaps / session recordings (Hotjar, Clarity) if they exist
- Page speed (CWV) for the landing pages
- History of past A/B tests and their results

## 4. Site (→ `site-audit/`)
- Full-page screenshots, desktop + mobile, of each landing page variant
- List of all LP variants and which ad groups point to which one

## 5. Voice of customer (→ `data/reviews/`)
- Reddit threads and Trustpilot reviews (raw text is fine; keep the source URL, date, and star rating if you have them)
- Any on-site survey, quiz answers, or support/chat logs
