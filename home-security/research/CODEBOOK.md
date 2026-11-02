# Codebook: home security buyer reviews and Reddit posts

One row per review or comment. Code only what the text says; use "unknown" rather than guess. Never infer gender or age from a name.

| Field | Values | Notes |
|---|---|---|
| source | trustpilot / bbb / consumeraffairs / bestcompany / reddit / other | |
| provider | ADT, SimpliSafe, Ring, Vivint, Brinks, Cove, Abode, Frontpoint, Arlo, Wyze, Deep Sentinel, Kangaroo, Xfinity, other, none | main one |
| stars | 1–5 or blank | |
| sentiment | pos / mixed / neg | |
| date | YYYY-MM if shown | |
| stage | first / switch / moving / after_incident / renew / unknown | first = first system; switch = names a previous provider; moving = new home; after_incident = break-in, package theft, scare; renew = contract ending |
| home | owner / renter / unknown | |
| install | diy / pro / unknown | |
| needs | PRICE_CLARITY / NO_CONTRACT / EASY_SETUP / RELIABLE / FAST_RESPONSE / HUMAN / APP / CAMERAS / NO_SUBSCRIPTION / PEACE_OF_MIND | several allowed |
| fears | TRAPPED_CONTRACT / CANCEL_HARD / HIDDEN_FEES / FALSE_ALARM / NO_RESPONSE / PUSHY_SALES / BAD_INSTALL / EQUIPMENT_FAILS / PRIVACY / PRICE_HIKE | several allowed |
| switch_reason | price / contract / support / reliability / moving / features | stage = switch only |
| quote | short verbatim line | |
| url | source URL | |
