"""Build a standalone copy of the dashboard for static hosting (Vercel).

dashboard/index.html is written for claude.ai artifacts, which add the
<!doctype>/<head>/<body> skeleton at publish time. This script adds that
skeleton itself and writes site/index.html.

Run after any dashboard change:  python3 scripts/build_site.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")

split = src.index('<header class="top wrap">')
head, body = src[:split], src[split:]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<style>body{{margin:0}} img{{max-width:100%}} [hidden]{{display:none!important}}</style>
{head}</head>
<body>
{body}
</body>
</html>
"""

out = ROOT / "site" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)} ({len(page):,} bytes)")
