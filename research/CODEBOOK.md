# Codebook: coding reviews and Reddit posts for the buyer profile

Use this for every new source (Reddit threads, more Trustpilot pages, quiz answers) so the buyer profile stays comparable across sources.

## Fields per item

| Field | Values | Notes |
|---|---|---|
| source | trustpilot / reddit / other | |
| provider | provider name, or "none" | Reddit posts often discuss several. Code the main one. |
| stars | 1–5, or blank | Reddit: blank |
| sentiment | pos / mixed / neg | Code from the text when there are no stars |
| collection | invited / verified / organic / unlabelled | Trustpilot only |
| **stage** | new / switch / long / restart / unknown | new = first GLP-1 or first time online; switch = names a previous provider, doctor or dose; long = 3+ months; restart = stopped and came back |
| medication | brand-inj / brand-oral / comp-inj / comp-oral / unknown | Wegovy, Zepbound, Foundayo, Wegovy pill vs compounded sema or tirz |
| payment | cash / insurance / medicare / unknown | |
| **needs** | HUMAN / EASY_START / HEARD / ON_TIME / MONEY_CONTROL / PRICE_CLARITY / WORKS / DOSE | Several allowed. These are the 8 needs in `10-buyer-profile.md`. |
| fears | OVERCHARGED / TRAPPED / RUN_OUT / SCAM / NO_HUMAN / JUDGED / SIDE_EFFECTS / REGAIN | Several allowed |
| switch_reason | price / membership / fulfilment / support / results / dose / insurance | Only when stage = switch |
| age_cue | explicit only, e.g. "72", "retiring" | Never infer from names or photos |
| quote | short verbatim line | For copy and the dashboard |

## Rules
- Code only what the text says. Leave "unknown" rather than guess.
- Never infer gender or age from a name.
- Keep the source URL and date when available.
- Store raw pasted text in `data/reviews/raw/` and coded rows in `data/reviews/<source>/`.
