# Dialed Offroad weekly static posts: how a week gets made

One week module in `tools/weeks/<week>.py` produces everything the pipeline needs. `<week>` is the Sunday River reviews it; the posts run Monday to Saturday after that Sunday, one a day at 6:40 pm Boise. Sunday has no post.

```
python3 tools/publish_week.py tools/weeks/2026-11-01.py
```

renders every slide (`posts/<slug>/NN.jpg` plus `tNN.jpg` thumbnails), writes `posts/manifest-<week>.json`, and under `out/<week>/`: `seed.json` (the Sunday Review page's `posts` documents), `enqueue.sql` (one `social_enqueue` per post for prod), `review.md` (the week at a glance). Then, in this order: push the repo (the queue and the page fetch images from raw.githubusercontent.com), run `enqueue.sql` on prod, set each `seed.json` document on the page (`ArtifactData set`, collection `posts`, doc_id = slug). Every post lands as a draft. Nothing publishes until River approves it on the page.

## The week module

```python
WEEK = [
  {
    "slug": "2026-11-03-yz250f-setup-sheet",   # YYYY-MM-DD of the post day, then the topic; the folder under posts/
    "title": "Settings card: 2024 Yamaha YZ250F",
    "design": "sheet",                          # one of the designs below; vary them across the week
    "kind": "carousel",                         # image (one slide) or carousel (2 to 10)
    "scheduled_at": "2026-11-04T01:40:00Z",     # 6:40 pm Boise in UTC (MST from Nov 1: 01:40Z next day; MDT: 00:40Z)
    "caption": "...",                           # the Instagram caption without hashtags; Facebook gets it with "Link in bio." swapped for the store link
    "hashtags": "#dirtbikes #moto ... #dialedoffroad",
    "story": "...",                             # a Story idea for the same day, shown on the page, never posted automatically
    "slides": [ {...}, ... ],                   # slide dicts, see the design's slide types
  },
]
```

`tools/weeks/2026-10-26.py` is the first week, kept as the worked example of every design.

## Designs (`tools/designs.py`, `DESIGNS`)

| design | slides | look |
|---|---|---|
| `glow` | one `hot` slide: `head`, `sub` | carbon, blue glow, the take in big type, a body paragraph |
| `sheet` | `cover` (head, sub), `table` (rows of (label, stock, dialed)), `points` (items), `closer` | setup sheet: blue header with the bike, six value tiles (`post["tiles"]`: (label, value, sub, chip)), then the stock vs Dialed table, then the points and the closer. Post keys: `sheet_title`, `sheet_sub`, `tiles`, `sag_note` |
| `blue_list` | `cover` (eyebrow, head, sub), `point` x N (num, head, body), `closer` (head, sub, footer) | all blue with black stickers; numbered truths |
| `split` | one `hot` slide (head) | diagonal STOCK / YOU split; `post["split"] = {left, left_lines, right, right_lines}` |
| `paper_list` | `cover`, `symptom` x N (num, head, why, fix), `closer` | light paper, flow boxes symptom → why → fix; the save-this cheat sheet |
| `dials` | `cover`, `point` x N (tag, head, body; a point tagged `NOT A CLICKER` gets the sag treatment), `closer` | carbon with drawn clicker dials; `post["dials"]` names the five dials on the cover |
| `screens` | none needed; `post["frames"]` = list of (line1, line2, sub, shot_index 1..6), `big`, `sticker`, `footer` | app screenshots in phone frames from `tools/shots/` |
| `classic` | any mix of `hot`, `cover`, `point`, `symptom`, `table`, `points`, `closer` | the plain dark design from `render.py`; the fallback |

Every design draws the real mark from `tools/logo/` and sets type in Barlow Condensed and Inter from `tools/fonts/`. 1080 x 1350, 84 px margins.

## Copy rules (checked by `publish_week.py`, the run fails on a hit)

- Never "AI", "exact", "exactly", "perfect", "free trial". Never an em dash anywhere.
- Numbers are starting points riders refine on the bike, counted out from fully closed, one change at a time. Never "do what the app says".
- Stock figures come from the catalog row (the owner's manual values in `bike_models` and its generations). A Dialed column comes from a real baseline the app produced (a `setup_versions` row on prod for that bike, weight band, skill and terrain), never invented. If no clean row exists for the bike that week, no settings card that week.
- No rider names, no account details. Weight is a band ("about 180 lb"), never someone's exact entry.
- Captions end with one question. Hashtags: 3 to 5, specific to the post, the last one `#dialedoffroad` (Instagram counts only the first five since December 2025; more just dilutes the signal).
- Under 2200 characters including hashtags.

## A week's mix

Six posts, Monday to Saturday, no two neighbours with the same design: one settings card for a bike people asked about (the `social_bike_requests` view on prod lists them), one save-worthy carousel (cheat sheet, clicker explainer, pre-ride checklist, sag how-to), one hot take, one myth or "nobody tells you" list, one app-screens post when there is a feature worth showing, one that answers last week's most common comment. Repeat a theme only after four weeks; `posts/manifest-*.json` and `tools/weeks/` are the record of what already ran.

## What is not here

Posting, comments, ads, and the page itself live in the app repo (`supabase/functions/social-*`) and on the Sunday Review page. This repo is only the images and the week modules, public because Instagram has to fetch the images from somewhere.
