#!/usr/bin/env python3
"""Build the small GitHub Pages site for media.dialedoffroad.app from site/*.txt.

    python3 site/build.py

Writes index.html, privacy.html and terms.html at the repo root (GitHub Pages serves the root, which is
also where posts/ and reels/ live, so TikTok can fetch the slides from the same verified domain).
"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

CSS = """
:root { color-scheme: light dark; --bg: #0b0c10; --fg: #f5f7fc; --mute: #8a93a6; --blue: #1d9bf0; --panel: #151920; --line: #262b36; }
@media (prefers-color-scheme: light) { :root { --bg: #f3f5fa; --fg: #0b0c10; --mute: #5b6475; --blue: #1a8fe0; --panel: #ffffff; --line: #d7dce6; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.6 Inter, system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 760px; margin: 0 auto; padding: 32px 20px 64px; }
header { display: flex; align-items: center; gap: 12px; margin-bottom: 28px; }
header img { width: 40px; height: 40px; border-radius: 10px; }
header a { color: var(--fg); text-decoration: none; font-weight: 700; letter-spacing: .02em; }
nav a { color: var(--mute); text-decoration: none; margin-right: 14px; font-size: 14px; }
nav a:hover { color: var(--blue); }
h1 { font-size: 30px; line-height: 1.15; margin: 0 0 6px; }
h2 { font-size: 20px; margin: 28px 0 8px; }
p { margin: 0 0 12px; }
ul { margin: 0 0 12px; padding-left: 22px; }
li { margin: 4px 0; }
.date { color: var(--mute); margin-bottom: 22px; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 18px 20px; margin: 16px 0; }
.btn { display: inline-block; background: var(--blue); color: #fff; padding: 10px 16px; border-radius: 999px; text-decoration: none; font-weight: 600; margin: 6px 8px 6px 0; }
footer { margin-top: 40px; color: var(--mute); font-size: 13px; }
footer a { color: var(--mute); }
"""

def page(title, body, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="/tools/logo/icon.png">
<style>{CSS}</style>
</head>
<body>
<main>
<header><img src="/tools/logo/icon.png" alt=""><a href="/">Dialed Offroad</a><nav><a href="/">Home</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></nav></header>
{body}
<footer>Atlas Systems LLC, Boise, Idaho. <a href="mailto:dialedoffroadapp@gmail.com">dialedoffroadapp@gmail.com</a></footer>
</main>
</body>
</html>
"""

def legal(path):
    lines = [l.rstrip("\n") for l in open(path, encoding="utf-8")]
    title, date = lines[0], lines[1]
    out = [f"<h1>{html.escape(title)}</h1>", f'<p class="date">{html.escape(date)}</p>']
    ul = []
    def flush():
        nonlocal ul
        if ul:
            out.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in ul) + "</ul>"); ul = []
    for l in lines[2:]:
        if not l.strip(): continue
        if l.startswith("## "): flush(); out.append(f"<h2>{html.escape(l[3:])}</h2>")
        elif l.startswith("• "): ul.append(l[2:])
        else: flush(); out.append(f"<p>{html.escape(l)}</p>")
    flush()
    return title, "\n".join(out)

def main():
    t, body = legal(os.path.join(SITE, "privacy.txt"))
    open(os.path.join(ROOT, "privacy.html"), "w", encoding="utf-8").write(page(f"{t} | Dialed Offroad", body, "How the Dialed Offroad app handles your data."))
    t, body = legal(os.path.join(SITE, "terms.txt"))
    open(os.path.join(ROOT, "terms.html"), "w", encoding="utf-8").write(page(f"{t} | Dialed Offroad", body, "The terms for using the Dialed Offroad app."))
    home = """
<h1>Dialed Offroad</h1>
<p class="date">Dirt bike suspension setup, built by a rider in Boise, Idaho.</p>
<div class="card">
<p>Dialed gives you a starting point for your clickers, sag and tire pressure from your bike, your weight and where you ride, then helps you refine it one change at a time from how the bike felt. The numbers are a starting point you refine on the bike, never a law.</p>
<a class="btn" href="https://apps.apple.com/app/id6754007586">App Store</a>
<a class="btn" href="https://play.google.com/store/apps/details?id=com.dialedoffroad.app">Google Play</a>
</div>
<div class="card">
<h2 style="margin-top:0">Dialed Offroad Social</h2>
<p>This site also serves the slides and clips that Dialed Offroad posts to its own Instagram, Facebook, YouTube and TikTok accounts. The posting tool is a private review page used by one person, the owner of those accounts; nothing here collects anything from visitors.</p>
<p>Follow along: <a href="https://www.instagram.com/dialed_offroad/">Instagram</a>, <a href="https://www.tiktok.com/@dialed.offroad">TikTok</a>.</p>
</div>
<p><a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms of Service</a> for the app.</p>
"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page("Dialed Offroad", home, "Dirt bike suspension setup app. Starting points you refine on the bike."))
    open(os.path.join(ROOT, "CNAME"), "w").write("media.dialedoffroad.app\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("wrote index.html, privacy.html, terms.html, CNAME, .nojekyll")

if __name__ == "__main__":
    main()
