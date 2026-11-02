# Phone CTA on mobile (ADT, Vivint, Brinks)

Status: client confirmed tracked phone numbers exist for the top 3 (Nov 2 2026).

## What to build (mobile)
- Cards #1–3: two buttons side by side. Phone = filled primary ("Call 855-xxx-xxxx"), Visit Site = outline secondary.
- Above the number, small line: "Talk to an ADT expert · free quote". Green dot + "Open now" only while the call center is open.
- Outside call hours: hide the phone button; Visit Site goes back to full-width primary.
- Sticky bottom bar (mobile): #1 brand + Call button + Visit Site.
- Repeat block after the list: "Our most popular" #1 card with the phone button.
- DIY brands (SimpliSafe, Cove, ADT Blu): Visit Site only.

## Tracking
- Use each partner's tracked number (or dynamic number insertion per campaign) so calls attribute to page and keyword.
- Fire a "call_click" event on tap; import qualified calls (partner's minimum duration, e.g. 90–120s) into Google Ads and Bing as conversions.
- Get from partners: call center hours by timezone, qualified-call definition, payout per call vs per click.

## Test
- A: current (Visit Site only) vs B: phone primary + Visit Site secondary on cards #1–3.
- Primary metric: partner-paid revenue per visitor (paid calls + click-out sales). Secondary: call taps, qualified-call rate, click-outs.
- Watch that calls don't just cannibalise click-outs that paid more.
