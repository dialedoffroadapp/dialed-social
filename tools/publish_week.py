#!/usr/bin/env python3
"""Turn a week module into everything the pipeline needs.

    python3 tools/publish_week.py tools/weeks/2026-11-01.py

Writes, relative to the repo root:
  posts/<slug>/NN.jpg          full slides, 1080 x 1350 JPEG (what Instagram and Facebook fetch)
  posts/<slug>/tNN.jpg         540 x 675 thumbnails (what the Sunday Review page shows)
  posts/manifest-<week>.json   slug -> list of full-slide URLs
  out/<week>/seed.json         the page's `posts` documents (ArtifactData set, collection "posts", doc_id = slug)
  out/<week>/enqueue.sql       one social_enqueue(...) per post, run on prod after the images are pushed
  out/<week>/review.md         the week at a glance, for the handoff message
  out/<week>/preview_*.png     contact sheets, one per post

Nothing here talks to GitHub, Supabase or the page: push the repo, run the SQL, write the seed, in that order,
because the queue and the page both point at raw.githubusercontent.com and the images must be there first.
"""
import os, re, sys, json, datetime as dt
from zoneinfo import ZoneInfo

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
RAW = "https://raw.githubusercontent.com/dialedoffroadapp/dialed-social/main/posts"
BOISE = ZoneInfo("America/Boise")
FORBIDDEN = [(r"\bAI\b", '"AI"'), (r"\bexact(ly)?\b", '"exact"'), (r"\bfree trial\b", '"free trial"'), (r"—", "an em dash"), (r"\bperfect\b", '"perfect"')]

sys.path.insert(0, BASE)
import designs  # noqa: E402


def die(msg):
    print("ERROR:", msg); sys.exit(1)


def check(week, week_id):
    seen = set()
    for p in week:
        slug = p.get("slug") or die("a post has no slug")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+", slug): die(f"{slug}: slug must be YYYY-MM-DD-topic, lower case")
        if slug in seen: die(f"{slug}: duplicate slug"); seen.add(slug)
        if p.get("design", "classic") not in designs.DESIGNS: die(f"{slug}: unknown design {p.get('design')}")
        n = len(p.get("slides") or [])
        kind = p.get("kind")
        if kind == "image" and n != 1 and p.get("design") not in ("screens", "sheet"): die(f"{slug}: kind image needs exactly one slide")
        if kind == "carousel" and not (2 <= n <= 10) and p.get("design") not in ("screens", "sheet"): die(f"{slug}: a carousel is 2 to 10 slides, got {n}")
        if kind not in ("image", "carousel"): die(f"{slug}: kind must be image or carousel")
        try:
            t = dt.datetime.fromisoformat(p["scheduled_at"].replace("Z", "+00:00"))
        except Exception:
            die(f"{slug}: scheduled_at must be ISO 8601 UTC like 2026-11-03T01:40:00Z")
        local = t.astimezone(BOISE)
        if not (17 <= local.hour <= 20): print(f"note: {slug} posts at {local.strftime('%a %b %d %-I:%M %p')} Boise, outside the usual 6:40 pm window")
        text = " ".join(str(v) for v in [p.get("caption", ""), p.get("hashtags", "")] + [str(s) for s in p.get("slides", [])])
        for pat, name in FORBIDDEN:
            if re.search(pat, text): die(f"{slug}: copy contains {name}; the copy rules forbid it")
        if len((p.get("caption", "") + "\n\n" + p.get("hashtags", ""))) > 2200: die(f"{slug}: caption over 2200 characters")
        if len(re.findall(r"#\w+", p.get("hashtags", ""))) > 30: die(f"{slug}: more than 30 hashtags")
        if not p.get("title"): die(f"{slug}: needs a title")
    print(f"checked {len(week)} posts for week {week_id}")


def sql_lit(s):
    tag = "$q$"
    while tag in s: tag = tag[:-1] + "x$"
    return f"{tag}{s}{tag}"


def main():
    if len(sys.argv) < 2: die(__doc__)
    week_path = os.path.abspath(sys.argv[1])
    week_id = os.path.splitext(os.path.basename(week_path))[0]
    week = designs.load_week(week_path)
    week.sort(key=lambda p: p["scheduled_at"])
    check(week, week_id)
    out_dir = os.path.join(ROOT, "out", week_id); os.makedirs(out_dir, exist_ok=True)
    manifest, seed, sql, review = {}, [], [], [f"# Week {week_id}: {len(week)} posts\n"]
    for p in week:
        slug = p["slug"]
        imgs = designs.render_post(p)
        folder = os.path.join(ROOT, "posts", slug); os.makedirs(folder, exist_ok=True)
        media = []
        for i, im in enumerate(imgs, 1):
            im = im.convert("RGB")
            im.save(os.path.join(folder, f"{i:02d}.jpg"), quality=92, optimize=True, progressive=True)
            im.resize((540, 675)).save(os.path.join(folder, f"t{i:02d}.jpg"), quality=80, optimize=True)
            media.append({"src": f"{RAW}/{slug}/{i:02d}.jpg", "thumb": f"{RAW}/{slug}/t{i:02d}.jpg"})
        designs.preview(imgs, os.path.join(out_dir, f"preview_{slug}.png"))
        manifest[slug] = [m["src"] for m in media]
        caption = p["caption"].strip()
        ig_caption = caption + ("\n\n" + p["hashtags"].strip() if p.get("hashtags") else "")
        fb_message = caption.replace("Link in bio.", "Get it here: dialedoffroad.app/get").replace("Link in bio", "Get it here: dialedoffroad.app/get")
        kind = p["kind"] if p["kind"] in ("image", "carousel") else ("carousel" if len(imgs) > 1 else "image")
        if len(imgs) > 1 and kind == "image": kind = "carousel"
        seed.append({"slug": slug, "title": p["title"], "week": week_id, "kind": kind, "scheduled_at": p["scheduled_at"],
                     "ig_caption": ig_caption, "fb_message": fb_message, "media": media, "fb_mode": p.get("fb_mode", "cover"),
                     "post_to_ig": p.get("post_to_ig", True), "post_to_fb": p.get("post_to_fb", True), "queue_status": "draft",
                     "story": p.get("story", ""), "design": p.get("design", "classic")})
        sql.append("select slug, status, scheduled_at at time zone 'America/Boise' as boise from public.social_enqueue("
                   f"{sql_lit(slug)}, {sql_lit(kind)}, {sql_lit(ig_caption)}, {sql_lit(fb_message)}, "
                   f"{sql_lit(json.dumps([{'url': m['src']} for m in media]))}::jsonb, {sql_lit(p['scheduled_at'])}::timestamptz, "
                   f"{sql_lit(p.get('fb_mode', 'cover'))}, {str(p.get('post_to_ig', True)).lower()}, {str(p.get('post_to_fb', True)).lower()});")
        local = dt.datetime.fromisoformat(p["scheduled_at"].replace("Z", "+00:00")).astimezone(BOISE)
        review.append(f"- **{local.strftime('%a %b %-d, %-I:%M %p')}** · {p['title']} · {kind}, {len(imgs)} slide{'s' if len(imgs) != 1 else ''} · design `{p.get('design', 'classic')}` · `{slug}`\n  Story: {p.get('story', '')}")
        print(slug, len(imgs), "slides")
    json.dump(manifest, open(os.path.join(ROOT, "posts", f"manifest-{week_id}.json"), "w"), indent=1)
    json.dump(seed, open(os.path.join(out_dir, "seed.json"), "w"), indent=1)
    open(os.path.join(out_dir, "enqueue.sql"), "w").write("\n".join(sql) + "\n")
    open(os.path.join(out_dir, "review.md"), "w").write("\n".join(review) + "\n")
    print(f"\nwrote posts/manifest-{week_id}.json, out/{week_id}/seed.json, enqueue.sql, review.md")
    print("next: git add posts && git commit && git push; then run enqueue.sql on prod; then set each seed document on the page.")


if __name__ == "__main__":
    main()
