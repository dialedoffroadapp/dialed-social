#!/usr/bin/env python3
"""Render animated explainer reels and write the Sunday Review page documents for them.

    python3 tools/anim/build.py <week> <date>=<spec id> [<date>=<spec id> ...] [--sheet] [--slot 15:40]

<week> is the Sunday the week is reviewed on (YYYY-MM-DD). Each <date> is the post day; the reel goes out at the slot
(default 3:40 pm Boise, between the 12:40 pm and 6:40 pm posts). A spec id comes from catalog.py, or from a JSON file
passed as <date>=path/to/spec.json for a new theme.

Writes, for each reel: reels/<date>-anim-<id>.mp4 and reels/<date>-anim-<id>-cover.jpg (repo root), and
out/anim/<week>/reels.json (one page document per reel, status "drafting", waiting for River's approval).
--sheet only draws contact sheets to out/anim/<week>/<slug>_sheet.jpg for checking, no video.
"""
import json, os, re, subprocess, sys
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import lib, catalog, xray, oneclick, pov

TEMPLATES = {"xray": xray, "oneclick": oneclick, "pov": pov}
RAW = "https://raw.githubusercontent.com/dialedoffroadapp/dialed-social/main/reels/"
BANNED = [r"\bAI\b", r"\bexact\b", r"\bexactly\b", r"\bperfect\b", r"free trial", "—"]

def all_text(o):
    if isinstance(o, str): return [o]
    if isinstance(o, dict): return [x for v in o.values() for x in all_text(v)]
    if isinstance(o, (list, tuple)): return [x for v in o for x in all_text(v)]
    return []

def check(spec):
    errs = []
    for s in all_text(spec):
        for b in BANNED:
            if re.search(b, s, flags=0 if b == r"\bAI\b" else re.I): errs.append(f"banned {b!r} in: {s[:60]}")
    tags = spec["hashtags"].split()
    if not (3 <= len(tags) <= 5) or tags[-1] != "#dialedoffroad": errs.append("hashtags: 3 to 5, #dialedoffroad last")
    if not spec["caption"].rstrip().endswith("?") or spec["caption"].count("?") != 1: errs.append("caption must end with one question")
    if "Link in bio." not in spec["caption"]: errs.append('caption needs "Link in bio." (Facebook swaps it for the store link)')
    if len(spec["caption"]) + len(spec["hashtags"]) + 2 > 2200: errs.append("caption over 2200 characters")
    return errs

def load(ref):
    if ref.endswith(".json"): return json.load(open(ref))
    return catalog.BY_ID[ref]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sheet_only = "--sheet" in sys.argv
    slot = "15:40"
    if "--slot" in sys.argv: slot = sys.argv[sys.argv.index("--slot") + 1]; args.remove(slot)
    week, pairs = args[0], [a.split("=", 1) for a in args[1:]]
    out_dir = os.path.join(REPO, "out", "anim", week); os.makedirs(out_dir, exist_ok=True)
    os.makedirs(os.path.join(REPO, "reels"), exist_ok=True)
    docs, failed = [], False
    for date, ref in pairs:
        spec = load(ref)
        errs = check(spec)
        if errs:
            failed = True; print(f"{ref}: " + "; ".join(errs)); continue
        slug = f"{date}-anim-{spec['id']}"
        frame, dur, track, sheet_times = TEMPLATES[spec["template"]].make(spec)
        if sheet_only:
            lib.stills(frame, sheet_times, os.path.join(out_dir, f"{slug}_sheet.jpg")); print("sheet", slug); continue
        mp4 = os.path.join(REPO, "reels", slug + ".mp4")
        v = os.path.join(out_dir, slug + "_v.mp4"); wav = os.path.join(out_dir, slug + ".wav")
        lib.render(frame, dur, v); track().save(wav); lib.mux(v, wav, mp4); os.remove(v); os.remove(wav)
        cover = os.path.join(REPO, "reels", slug + "-cover.jpg")
        frame(spec.get("cover_s", 2.0)).convert("RGB").save(cover, quality=88)
        hh, mm = map(int, slot.split(":"))
        when = datetime(*map(int, date.split("-")), hh, mm, tzinfo=ZoneInfo("America/Boise")).astimezone(ZoneInfo("UTC"))
        docs.append({
            "slug": slug, "title": spec["title"], "caption": spec["caption"], "hashtags": spec["hashtags"],
            "tt_title": spec["tt_title"], "yt_title": "", "note": f"Animated explainer ({spec['template']}: {spec['id']}), made by Claude",
            "scheduled_at": when.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "status": "drafting", "queue_status": None, "applied_at": None,
            "video_url": RAW + slug + ".mp4", "parts": [], "pieces_deleted": True, "source": None, "source_name": slug + ".mp4",
            "source_type": "video/mp4", "mime": "video/mp4", "width": 1080, "height": 1920, "duration_s": round(dur, 2),
            "cover_ms": round(spec.get("cover_s", 2.0) * 1000), "size_bytes": os.path.getsize(mp4),
            "post_to_ig": True, "post_to_fb": True, "post_to_tt": True, "post_to_yt": False,
            "tt": {"brand_content": False, "brand_organic": False, "comment": True, "disclose": False, "duet": False,
                   "privacy": "PUBLIC_TO_EVERYONE", "stitch": False},
            "poster_id": None, "preview_id": None, "error": None, "ai": None,
            "_local_cover": os.path.relpath(cover, REPO), "_local_mp4": os.path.relpath(mp4, REPO),
        })
        print("rendered", slug, round(dur, 1), "s")
    if docs:
        path = os.path.join(out_dir, "reels.json")
        old = json.load(open(path)) if os.path.exists(path) else []
        keep = {d["slug"]: d for d in old}; keep.update({d["slug"]: d for d in docs})
        json.dump(sorted(keep.values(), key=lambda d: d["scheduled_at"]), open(path, "w"), indent=2)
        print("wrote", os.path.relpath(path, REPO))
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
