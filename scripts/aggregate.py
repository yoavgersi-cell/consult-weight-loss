"""Aggregate every coded review/Reddit file into one JSON blob and inject it into the dashboard.

Run after adding any new coded data:
    python3 scripts/aggregate.py
"""
import csv
import glob
import json
import os
import re
import statistics as st
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TP_DIR = os.path.join(ROOT, 'data/reviews/trustpilot')
RD_DIR = os.path.join(ROOT, 'data/reviews/reddit')
DASH = os.path.join(ROOT, 'dashboard/index.html')

NEEDS = ['HUMAN', 'EASY_START', 'HEARD', 'ON_TIME', 'MONEY_CONTROL', 'PRICE_CLARITY', 'WORKS', 'DOSE']
NEED_LABEL = {
    'HUMAN': 'A human who answers', 'EASY_START': 'Easy, fast start', 'HEARD': 'Being heard, not judged',
    'ON_TIME': 'Medication on time', 'MONEY_CONTROL': 'Control over money', 'PRICE_CLARITY': 'A price they understand',
    'WORKS': 'That it works / is safe', 'DOSE': 'Dose continuity, med type',
}
# Trustpilot provider-theme codes -> buyer needs (same map used in research/10-buyer-profile.md)
TP_NEED = {
    'PRICE_CLARITY': ['MEMB', 'DOSEPRICE', 'PRICE', 'ONMSG', 'PRICEPOS', 'AFFORD', 'CADENCE', 'PROMO'],
    'ON_TIME': ['SHIP', 'SHIPFAST', 'RELIABLE', 'COLD', 'PREPAY'],
    'HUMAN': ['CS', 'CSPOS', 'NAMED', 'REP', 'FIX', 'PORTAL', 'NOTIF'],
    'HEARD': ['HEARD', 'CONSULT', 'APPT'],
    'EASY_START': ['QUICK', 'TOOSOON', 'PRESALE', 'PLAN'],
    'MONEY_CONTROL': ['BILL', 'UPSELL', 'BUNDLE', 'AUTOSUB', 'CANCELEASY', 'SUPPRESS', 'SALESCALLS'],
    'WORKS': ['EFF', 'RESULTS', 'SE'],
    'DOSE': ['DOSE', 'SWITCH', 'ORAL', 'INS', 'LILLY', 'FDA'],
}
TP_NEED_INV = {t: k for k, v in TP_NEED.items() for t in v}

FEARS = ['OVERCHARGED', 'TRAPPED', 'RUN_OUT', 'NO_HUMAN', 'SCAM', 'SIDE_EFFECTS', 'JUDGED', 'REGAIN']
FEAR_LABEL = {
    'OVERCHARGED': 'Being overcharged', 'TRAPPED': 'Being trapped (prepay, cancel, refunds)', 'RUN_OUT': 'Running out of medication',
    'NO_HUMAN': 'Nobody to call', 'SCAM': 'Scam / doesn\'t work', 'SIDE_EFFECTS': 'Side effects', 'JUDGED': 'Being judged',
    'REGAIN': 'Regaining weight',
}
# Trustpilot complaint themes (only counted on 1-2★ / negative items) -> fears
TP_FEAR = {
    'OVERCHARGED': ['MEMB', 'DOSEPRICE', 'CADENCE', 'PROMO', 'UPSELL', 'BUNDLE'],
    'TRAPPED': ['BILL', 'PREPAY', 'AUTOSUB'],
    'RUN_OUT': ['SHIP', 'COLD'],
    'NO_HUMAN': ['CS', 'PORTAL', 'APPT', 'NOTIF'],
    'SCAM': ['EFF', 'ORAL', 'SUPPRESS'],
    'SIDE_EFFECTS': ['SE'],
    'JUDGED': ['SALESCALLS'],
}
TP_FEAR_INV = {t: k for k, v in TP_FEAR.items() for t in v}


def read(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def tp_sentiment(row):
    s = (row.get('stars') or '').strip()
    if s:
        n = int(s)
        return 'pos' if n >= 4 else 'neg' if n <= 2 else 'mixed'
    return row.get('sentiment') or 'mixed'


def share(counter, n, keys):
    return {k: round(counter.get(k, 0) / n * 100, 1) if n else 0 for k in keys}


def main():
    out = {'sources': {}, 'providers': [], 'stage': {}, 'needs': {}, 'fears': {}, 'reddit': {}, 'prices': {}}

    # ---------- Trustpilot ----------
    tp_rows = []
    for f in sorted(glob.glob(os.path.join(TP_DIR, '*_coded_*.csv'))):
        prov = os.path.basename(f).split('_')[0]
        rows = read(f)
        for r in rows:
            r['_prov'] = prov
        tp_rows += rows
        stars = [int(r['stars']) for r in rows if (r.get('stars') or '').strip()]
        inv = [int(r['stars']) for r in rows if r['source'] in ('invited', 'verified') and (r.get('stars') or '').strip()]
        org = [int(r['stars']) for r in rows if r['source'] == 'organic' and (r.get('stars') or '').strip()]
        sent = Counter(tp_sentiment(r) for r in rows)
        neg = [r for r in rows if tp_sentiment(r) == 'neg']
        top_neg = Counter(t for r in neg for t in r['themes'].split('|') if t).most_common(1)
        out['providers'].append({
            'provider': prov, 'n': len(rows),
            'avg': round(st.mean(stars), 2) if stars else None,
            'invited_share': round(sum(r['source'] in ('invited', 'verified') for r in rows) / len(rows) * 100),
            'labelled': any(r['source'] in ('invited', 'verified', 'organic') for r in rows),
            'invited_avg': round(st.mean(inv), 2) if inv else None,
            'organic_avg': round(st.mean(org), 2) if org else None,
            'pos': sent['pos'], 'neg': sent['neg'], 'mixed': sent['mixed'],
            'top_neg_theme': top_neg[0][0] if top_neg else None,
            'top_neg_share': round(top_neg[0][1] / len(neg) * 100) if top_neg and neg else None,
        })
    n_tp = len(tp_rows)

    tp_need_any, tp_need_pos, tp_need_neg = Counter(), Counter(), Counter()
    tp_fear = Counter()
    for r in tp_rows:
        themes = [t for t in r['themes'].split('|') if t]
        needs = {TP_NEED_INV[t] for t in themes if t in TP_NEED_INV}
        s = tp_sentiment(r)
        for k in needs:
            tp_need_any[k] += 1
            if s == 'pos':
                tp_need_pos[k] += 1
            elif s == 'neg':
                tp_need_neg[k] += 1
        if s == 'neg':
            for k in {TP_FEAR_INV[t] for t in themes if t in TP_FEAR_INV}:
                tp_fear[k] += 1
    n_tp_neg = sum(tp_sentiment(r) == 'neg' for r in tp_rows)

    stage_rows = read(os.path.join(TP_DIR, 'user_stage_signals_2026-10-07.csv'))
    tp_stage = Counter(r['stage'] for r in stage_rows)

    # ---------- Reddit ----------
    rd = read(os.path.join(RD_DIR, 'reddit_coded_2026-10-07.csv'))
    n_rd = len(rd)
    rd_stage = Counter(r['stage'] for r in rd if r['stage'] != 'unknown')
    rd_need = Counter(t for r in rd for t in r['needs'].split('|') if t)
    rd_fear = Counter(t for r in rd for t in r['fears'].split('|') if t)
    rd_med = Counter(r['medication'] for r in rd)
    rd_pay = Counter(r['payment'] for r in rd if r['payment'] != 'unknown')
    rd_switch = Counter(r['switch_reason'] for r in rd if r['switch_reason'])
    rd_threads = Counter(r['thread'] for r in rd)

    # ---------- price census ----------
    pc = read(os.path.join(RD_DIR, 'price_census_2026-10-07.csv'))
    prices = defaultdict(list)
    for r in pc:
        prices[r['channel']].append(float(r['usd_per_month']))
    for ch, v in prices.items():
        v.sort()
        q = st.quantiles(v, n=4) if len(v) >= 4 else [v[0], st.median(v), v[-1]]
        out['prices'][ch] = {'values': v, 'n': len(v), 'median': round(st.median(v)), 'q1': round(q[0]), 'q3': round(q[2])}

    # ---------- drug preference ----------
    dp_path = os.path.join(RD_DIR, 'drug_preference_2026-10-07.csv')
    dp = Counter(r['choice'] for r in read(dp_path)) if os.path.exists(dp_path) else Counter()

    # ---------- explicit demographics ----------
    dm_path = os.path.join(ROOT, 'data/reviews/demographics_explicit_2026-10-07.csv')
    dm = read(dm_path) if os.path.exists(dm_path) else []
    ages = sorted(int(r['age']) for r in dm if r['age'])
    bands = Counter()
    for a in ages:
        bands['<40' if a < 40 else '40-49' if a < 50 else '50-64' if a < 65 else '65+'] += 1
    for r in dm:
        if not r['age'] and (r.get('age_band') or '').strip():
            bands[r['age_band'].strip()] += 1
    losses = [round((float(r['start_lbs']) - float(r['current_lbs'])) / float(r['start_lbs']) * 100, 1) for r in dm if r['start_lbs'] and r['current_lbs']]
    out['demographics'] = {'n_age': sum(bands.values()), 'ages': ages, 'bands': {k: bands.get(k, 0) for k in ['<40', '40-49', '50-64', '65+']},
                           'sex': dict(Counter(r['sex'] for r in dm if r['sex'])), 'loss_pct': losses,
                           'median_age': st.median(ages) if ages else None}

    # ---------- community comparison list (competitor benchmark) ----------
    cl_path = os.path.join(ROOT, 'data/competitors/community_where_to_buy_2026-10-05.csv')
    if os.path.exists(cl_path):
        cl = read(cl_path)
        monthly = sorted(round(float(r['total_3mo']) / 3) for r in cl)
        known28 = [r for r in cl if r['compliant_28day']]
        out['community_list'] = {
            'plans': len(cl), 'providers': len({r['provider'] for r in cl}),
            'monthly': monthly, 'median_monthly': st.median(monthly), 'min_monthly': monthly[0], 'max_monthly': monthly[-1],
            'share_503b': round(sum(r['pharmacy_type'] == '503B' for r in cl) / len(cl) * 100),
            'share_28day': round(sum(r['compliant_28day'] == 'yes' for r in known28) / len(known28) * 100) if known28 else None,
            'share_auto_refill': round(sum(r['refill'] == 'auto' for r in cl) / len(cl) * 100),
            'share_all_states': round(sum(r['ships_all_states'] == 'yes' for r in cl) / len(cl) * 100),
            'share_additive_free': round(sum(r['additive'].startswith('none') for r in cl) / len(cl) * 100),
            'pharmacies': dict(Counter(r['pharmacy'].split(' (')[0] for r in cl)),
            'tiers': read(os.path.join(ROOT, 'data/competitors/community_where_to_buy_tiers_2026-10-05.csv')),
        }

    # ---------- assemble ----------
    out['sources'] = {
        'trustpilot_reviews': n_tp, 'trustpilot_providers': len(out['providers']), 'trustpilot_negative': n_tp_neg,
        'reddit_items': n_rd, 'reddit_threads': len(rd_threads), 'price_reports': len(pc),
        'stage_revealing_tp': sum(tp_stage.values()), 'stage_revealing_rd': sum(rd_stage.values()),
    }
    stage_keys = ['new', 'switch', 'long', 'restart']
    out['stage'] = {
        'trustpilot': share(tp_stage, sum(tp_stage.values()), stage_keys),
        'reddit': share(rd_stage, sum(rd_stage.values()), stage_keys),
    }
    out['needs'] = {
        'labels': NEED_LABEL, 'order': NEEDS,
        'trustpilot_share': share(tp_need_any, n_tp, NEEDS),
        'reddit_share': share(rd_need, n_rd, NEEDS),
        'trustpilot_pos': dict(tp_need_pos), 'trustpilot_neg': dict(tp_need_neg),
    }
    out['fears'] = {
        'labels': FEAR_LABEL, 'order': FEARS,
        'trustpilot_share_of_negative': share(tp_fear, n_tp_neg, FEARS),
        'reddit_share': share(rd_fear, n_rd, FEARS),
    }
    # ---------- pooled: one database, no source split ----------
    all_stage = tp_stage + rd_stage
    n_rd_worry = sum(1 for r in rd if r['fears'].strip())
    out['stage']['all'] = share(all_stage, sum(all_stage[k] for k in stage_keys), stage_keys)
    out['needs']['all_share'] = share(tp_need_any + rd_need, n_tp + n_rd, NEEDS)
    # complaints/worries pool = Trustpilot 1-2 star reviews + Reddit comments that voice a fear
    out['fears']['all_share'] = share(tp_fear + rd_fear, n_tp_neg + n_rd_worry, FEARS)
    out['sources']['all_items'] = n_tp + n_rd
    out['sources']['stage_revealing_all'] = sum(all_stage[k] for k in stage_keys)
    out['sources']['complaint_pool'] = n_tp_neg + n_rd_worry
    out['reddit'] = {
        'medication': dict(rd_med), 'payment': dict(rd_pay), 'switch_reason': dict(rd_switch),
        'threads': dict(rd_threads),
        'drug_preference': dict(dp),
    }

    blob = json.dumps(out, separators=(',', ':'))
    with open(os.path.join(ROOT, 'data/aggregate.json'), 'w') as f:
        json.dump(out, f, indent=1)
    html = open(DASH).read()
    tag = f'<script id="agg-data">window.AGG={blob};</script>'
    if '<script id="agg-data">' in html:
        html = re.sub(r'<script id="agg-data">.*?</script>', lambda m: tag, html, count=1, flags=re.S)
    else:
        html = html.replace('<script>\n(function () {', tag + '\n<script>\n(function () {', 1)
    open(DASH, 'w').write(html)
    print(json.dumps(out['sources']), '\nstage', out['stage'], '\nneeds tp', out['needs']['trustpilot_share'],
          '\nneeds rd', out['needs']['reddit_share'], '\nfears tp', out['fears']['trustpilot_share_of_negative'],
          '\nfears rd', out['fears']['reddit_share'], '\nPOOLED stage', out['stage']['all'], '\nneeds', out['needs']['all_share'], '\nfears', out['fears']['all_share'], out['sources'])


if __name__ == '__main__':
    main()
