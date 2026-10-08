# HealthAccess Weight Loss — CRO Engagement

CRO consulting workspace for [healthaccess.com/weight-loss/compare](https://healthaccess.com/weight-loss/compare), a weight-loss (GLP-1 telehealth) comparison site.
Traffic today: Google Ads paid search, desktop. Mobile is coming soon.

## Structure

| Folder | What goes here |
|---|---|
| `research/` | Market research: search intent, competitors, voice of customer |
| `data/reviews/reddit/` | Raw Reddit threads/comments (drop CSV, JSON, TXT, or pasted text) |
| `data/reviews/trustpilot/` | Raw Trustpilot reviews, one file per provider is ideal |
| `data/campaigns/` | Google Ads exports: search terms report, keywords, ad copy, campaign/ad group stats |
| `data/analytics/` | GA4 / funnel / heatmap / click-out data |
| `site-audit/` | Screenshots + audit of the current compare page (desktop + mobile) |
| `plan/` | CRO plan, test backlog, roadmap |
| `dashboard/` | The client-facing presentation dashboard |

See `DATA_REQUEST.md` for the list of data to ask the client for.

## Hosting the dashboard on Vercel

`site/index.html` is a standalone copy of `dashboard/index.html`, built by `python3 scripts/build_site.py`. Re-run the script after any dashboard change. `vercel.json` serves the `site/` folder as-is, with no build step, and sends a `noindex` header so search engines skip the page.
