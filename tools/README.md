# Dialed Offroad weekly static posts: how a week gets made

One week module in `tools/weeks/<week>.py` produces everything the pipeline needs. `<week>` is the Sunday River reviews it; the posts run Monday to Saturday after that Sunday, two a day, at 12:40 pm and 6:40 pm Boise. Sunday has no post.

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
    "scheduled_at": "2026-11-04T01:40:00Z",     # the slot in UTC. Boise is MST from Nov 1: 12:40 pm = 19:40Z same day, 6:40 pm = 01:40Z next day (MDT: 18:40Z and 00:40Z)
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
| `split` | `hot` (head), then optional `points`, `closer` (from the week of Nov 8, bike cards run it as a 3-slide carousel) | diagonal STOCK / YOU split; `post["split"] = {left, left_lines, right, right_lines}`; slides after the first render in the plain dark design |
| `paper_list` | `cover`, `symptom` x N (num, head, why, fix, optional `label`/`label2` to rename the SYMPTOM / START HERE boxes), `closer` | light paper, flow boxes symptom → why → fix; the save-this cheat sheet. `post["paper_footer"]` overrides the footer line |
| `dials` | `cover`, `point` x N (tag, head, body; a point tagged `NOT A CLICKER` gets the sag treatment), `closer` | carbon with drawn clicker dials; `post["dials"]` names the five dials on the cover |
| `screens` | none needed; `post["frames"]` = list of (line1, line2, sub, shot_index 1..6), `big`, `sticker`, `footer` | app screenshots in phone frames from `tools/shots/` |
| `classic` | any mix of `hot`, `cover`, `point`, `symptom`, `table`, `points`, `closer` | the plain dark design from `render.py`; the fallback |

Every design draws the real mark from `tools/logo/` and sets type in Barlow Condensed and Inter from `tools/fonts/`. 1080 x 1350, 84 px margins.

## Copy rules (checked by `publish_week.py`, the run fails on a hit)

- Never "AI", "exact", "exactly", "perfect", "free trial". Never an em dash anywhere.
- Numbers are starting points riders refine on the bike, counted out from fully closed, one change at a time. Never "do what the app says".
- Stock figures come from the catalog (`bike_model_specs` on prod: field, value, unit, counted_from, the manual it came from and its quote). A Dialed column comes from a real baseline the app produced (a `setup_versions` row on prod for a bike of that model and year, with the rider's weight band, skill and terrain), never invented. A bike without both halves gets no card; pick another bike.
- No rider names, no account details. Weight is a band ("about 180 lb"), never someone's exact entry.
- Captions end with one question. Hashtags: 3 to 5, specific to the post, the last one `#dialedoffroad` (Instagram counts only the first five since December 2025; more just dilutes the signal).
- Under 2200 characters including hashtags.

## A week's mix

Twelve posts, Monday to Saturday, two a day (from the week of November 2, 2026).

The midday post (12:40 pm) is a **bike card, every day**: one make, model and year, the owner's manual stock clickers and sag next to one real Dialed baseline for a rider band, framed as a starting point. Alternate the `sheet` and `split` designs day by day (sheet Monday, split Tuesday, and so on) so neither runs more than three times. Pick the bike in this order: a bike people asked about (`social_bike_requests`), then the models riders tune most in the app (`setup_versions` joined to `bikes`, last 60 days), then rotate brands and classes (250F, 450F, two-stroke, off-road) across years 2019 and newer. Never the same model-year twice in 26 weeks, never two bikes of the same brand on neighbouring days. A bike qualifies only when both halves exist: a sourced stock row set in `bike_model_specs` (fork_comp, fork_reb, shock_reb at least, `source_kind` oem_manual or oem_spec, prefer market us then all then eu, preset standard then null) and at least one `setup_versions` row for a bike of that model and year. About 180 model-years qualify today and the list grows as riders tune.

The evening post (6:40 pm) is a **tip**: a hot take (`glow`), a numbered list of truths (`blue_list`), a cheat sheet or symptom-to-fix sheet (`paper_list`), a clicker explainer (`dials`), an app-screens post when there is a feature worth showing, or a one-slide answer to the week's most common comment. No tip design more than twice in a week, and no two neighbouring posts with the same design. Repeat a tip theme only after four weeks; `posts/manifest-*.json` and `tools/weeks/` are the record of what already ran.

TikTok gets the same slides: the Sunday Review page ticks TikTok on every static post by default and the pipeline posts them as photo carousels there once TikTok is connected. Nothing about the week module changes for that.

## Animated explainer reels (from the week of November 8, 2026)

One animated reel a day, Monday to Saturday, at **3:40 pm Boise** (between the 12:40 pm and 6:40 pm posts; 22:40Z in MST, 21:40Z in MDT). They live in `tools/anim/`:

| file | what |
|---|---|
| `xray.py` | X-ray fork cutaway: oil through the piston, spring, travel meter. Beats use motions from `MOTIONS` (land_slow, slam, harsh, rebound, rebound_fast, pack, dive, dialed, chop_dialed) |
| `oneclick.py` | macro clicker, needle and bleed gap, damping graph, "same number, different setting" |
| `pov.py` | POV hook, setup sheet, comparison bars, sag gauge, three red stamps, punchline |
| `app.py` | the app moment every reel ends on: the real "How was it?" screen (`tools/shots/02`) with a tap on the matching chip, then the change card (part, from, to, which way), or two real screens (`screens`, `lines`) |
| `catalog.py` | reviewed specs, one per theme (`id`). Add new themes here, in the same shape |
| `build.py` | renders and writes the page documents |

```
python3 tools/anim/build.py <week> <date>=<spec id> ... [--sheet]
```

`--sheet` draws contact sheets to `out/anim/<week>/` for checking; without it each reel renders to `reels/<date>-anim-<id>.mp4` with a cover `reels/<date>-anim-<id>-cover.jpg`, and `out/anim/<week>/reels.json` gets one Sunday Review `reels` document per reel (status `drafting`, `video_url` on raw.githubusercontent.com, `parts` empty). build.py fails on the copy rules above.

Then: push the repo; for each document upload the cover and the mp4 to the page's asset store (Artifact publish, `asset: true`) and set `poster_id` and `preview_id` to the returned ids (the id is the hex part of `/_blob/<id>`), drop the two `_local_*` keys, and `ArtifactData set` collection `reels`, doc_id = slug. They show under This week with an Approve button. Approving makes them `ready`; the hourly sync queues them (it skips the upload step because `video_url` is set and `parts` is empty).

Week mix: rotate the templates xray, oneclick, pov, xray, oneclick, pov (Monday to Saturday), never the same template on neighbouring days. A theme (`id`) repeats only after four weeks (check `out/anim/*/reels.json`). When the catalog runs short, write new specs into `catalog.py`: a new symptom, clicker or POV situation, the app chip that matches it from `app.CHIPS`, and a change card that points the right way (in = clockwise = more damping; rebound in = slower). Suspension claims must be ones a suspension tech would sign off on; numbers on screen are illustrative and framed as starting points. No bike animations.

## What is not here

Posting, comments, ads, and the page itself live in the app repo (`supabase/functions/social-*`) and on the Sunday Review page. This repo is only the images and the week modules, public because Instagram has to fetch the images from somewhere.
