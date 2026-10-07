"""Summarise a coded review CSV: rating mix by source and theme frequency by sentiment."""
import csv, sys
from collections import Counter

rows = list(csv.DictReader(open(sys.argv[1])))
n = len(rows)
print(f"reviews: {n}")
for src in ("invited", "verified", "organic"):
    r = [int(x["stars"]) for x in rows if x["source"] == src]
    if r:
        print(f"{src:9} n={len(r):3}  avg={sum(r)/len(r):.2f}  5*={sum(s==5 for s in r)/len(r):.0%}  1-2*={sum(s<=2 for s in r)/len(r):.0%}")
allr = [int(x["stars"]) for x in rows]
print(f"all       n={n}  avg={sum(allr)/n:.2f}  5*={sum(s==5 for s in allr)/n:.0%}  1-2*={sum(s<=2 for s in allr)/n:.0%}")
neg = [x for x in rows if int(x["stars"]) <= 2]
pos = [x for x in rows if int(x["stars"]) >= 4]
for label, group in (("NEGATIVE (1-2*)", neg), ("POSITIVE (4-5*)", pos)):
    c = Counter(t for x in group for t in x["themes"].split("|") if t)
    print(f"\n{label} n={len(group)}")
    for t, k in c.most_common():
        print(f"  {t:8} {k:3}  {k/len(group):.0%}")
