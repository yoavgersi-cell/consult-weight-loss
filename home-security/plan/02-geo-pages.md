# Geo landing pages for paid search

Paid-only traffic, so geo pages are about ad-to-page match, not SEO.

## Build
- One template, many geo versions: H1 "Best Home Security Systems in {State|City} 2026".
- Fill the location from the campaign, not the visitor's IP:
  - Google Ads: ValueTrack {loc_physical_ms} / {loc_interest_ms} → map criteria ID to city/state; or a fixed ?state=CA per geo campaign/ad group.
  - Bing: {Location} / location IDs, same mapping.
  - IP lookup only as a last fallback. US only; otherwise "Best Home Security Systems of 2026".
- Same URL for every geo, so it's one page to maintain.

## Make it more than one word (per state, small)
- "Pro install available in {City} · often next day" on ADT / Vivint / Brinks.
- Phone number per state if partners give local or tracked numbers.
- Order or offers per state where payouts or coverage differ.
- One line of local facts later (state cancel rules e.g. California auto-renewal law, city false-alarm fines).

## Test
- Generic H1 vs geo H1 on geo-targeted campaigns. Measure partner-paid revenue per visitor.
- Bring ad copy in line: "Best Home Security in {State}" headlines (location insertion) so ad → page match is exact.
