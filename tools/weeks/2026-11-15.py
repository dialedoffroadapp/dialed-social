# Week of 2026-11-15 (posts Mon Nov 16 to Sat Nov 21). Bike card carousel at 12:40 pm Boise every day (sheet / split
# alternating, sheet Monday), tip at 6:40 pm. Animated explainer reels Mon, Wed, Fri at 3:40 pm come from tools/anim
# (out/anim/2026-11-15). Nothing was queued in social_posts for these slots.
# Bike cards: stock from bike_model_specs on prod (oem_manual), Dialed from a real setup_versions baseline.
#   Mon 2024 KTM 250 SX-F       Owner's Manual 2024 250 SX-F, 250 XC-F, 250 SX-F Factory Edition, part 3214834en (us, standard)
#   Tue 2025 Kawasaki KX450     Owner's Manual 2025 KX450M/N (KX450, KX450X), part 99814-0003 (us); no sag figure in the catalog
#   Wed 2026 Yamaha YZ250F      2026 Owner's Service Manual YZ250F, part DR8-2819U-10 (us, standard)
#   Thu 2024 KTM 125 XC         Owner's Manual 2024 125 XC, US edition (us, standard)
#   Fri 2022 Honda CRF250R      Competition Handbook CRF250R/RX, Honda Motor Europe, April 2021, part 62K95X10 (eu, standard)
#   Sat 2027 Yamaha YZ250FX     2027 Owner's Service Manual YZ250FX, part DP3-2819U-11 (us, standard)
# Skipped: 2024 Beta RR 2T 300 (the one open bike request) still has no setup_versions row; 2023 and 2024 Honda
# CRF250R, 2024 CRF450R and 2021 KX250 (top tuned) have no stock clicker rows in the catalog; 2025 Husqvarna TE 300
# ran Oct 31.
import datetime as _dt
from zoneinfo import ZoneInfo as _Z

_B = _Z("America/Boise")


def _at(day, hour):
    return _dt.datetime(2026, 11, day, hour, 40, tzinfo=_B).astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


FOOT = "Dialed Offroad 3.0  ·  App Store  ·  Google Play"
CTA = "Drop your bike, year and weight below and I'll run yours."
BASE = {"post_to_ig": True, "post_to_fb": True, "fb_mode": "cover"}
CLOSE = {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
         "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT}
CLOSE_SPLIT = {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
               "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA}

WEEK = [
 # ------------------------------------------------------------------ Mon Nov 16
 dict(BASE, **{
  "slug": "2026-11-16-250sxf-setup-sheet",
  "title": "Settings card: 2024 KTM 250 SX-F",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(16, 12),
  "caption": "2024 KTM 250 SX-F. About 195 lb, fast, hardpack moto, stock suspension, stability and jump support the "
             "goals. This is the baseline Dialed built, next to the standard settings from KTM's 2024 owner's manual "
             "for the 250 SX-F and 250 XC-F.\n\n"
             "Stock is 12 and 18 on the fork, 15 clicks and 1 1/2 turns on the shock, 15 on shock rebound, 105 mm of "
             "riding sag. Dialed went 1 click in on fork comp, 8 in on fork rebound, 5 in on low-speed, a quarter turn "
             "in on high-speed and 3 in on shock rebound. Sag stays at 105. Eight clicks is a big move: if the front "
             "starts to feel slow or packs in braking bumps, come back toward stock two at a time. Fork air: set it "
             "from the manual for your weight.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "250 SX-F riders: where's your fork rebound sitting?",
  "hashtags": "#ktm #250sxf #motocross #suspension #dialedoffroad",
  "story": "Quiz sticker on the tiles: \"Stock fork rebound on a 2024 250 SX-F?\" 12 / 15 / 18.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2024 KTM 250 SX-F",
    "sub": "about 195 lb  ·  fast  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2024 KTM 250 SX-F  ·  about 195 lb  ·  fast  ·  hardpack moto",
    "rows": [("Fork compression", "12", "11"), ("Fork rebound", "18", "10"), ("Shock low-speed comp", "15", "10"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/4 turns"), ("Shock rebound", "15", "12"),
             ("Riding sag", "105 mm", "105 mm"), ("Shock spring, 187 to 209 lb", "45 N/mm", "manual's row")],
    "note": "Clicks counted out from fully closed. Stock figures from KTM's 2024 250 SX-F owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 8 clicks in", "The big one: a calmer front off jump faces."),
    ("Shock low-speed, 5 clicks in", "Holds a 195 lb rider up on the gas."),
    ("Shock rebound 3 in, high-speed 1/4 in", "More support for the landings."),
    ("Fork comp 1 in, sag stays 105 mm", "Set sag before any click."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2024 KTM 250 SX-F",
  "sheet_sub": "about 195 lb  ·  fast  ·  hardpack moto  ·  WP XACT AER fork",
  "tiles": [("FORK COMP", "11", "stock 12", "1 click in"),
            ("FORK REBOUND", "10", "stock 18", "8 clicks in"),
            ("SHOCK LOW-SPEED", "10", "stock 15", "5 clicks in"),
            ("SHOCK HIGH-SPEED", "1 1/4", "turns  ·  stock 1 1/2", "1/4 turn in"),
            ("SHOCK REBOUND", "12", "stock 15", "3 clicks in"),
            ("SHOCK SPRING", "45", "N/mm  ·  manual, 187 to 209 lb", None)],
  "sag_value": "105 mm",
  "sag_note": "manual says 105 mm  ·  2024 KTM 250 SX-F manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-16-setup-log",
  "title": "Carousel: the setup log cheat sheet",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(16, 18),
  "paper_footer": "Write it down before you load the bike.",
  "caption": "The best tuners aren't the ones with the best memory. They write it down. Here's what goes in a setup "
             "log, and why each line matters the next time you ride.\n\n"
             "Clicks counted out from fully closed, one change at a time, so every line tells you what that change "
             "did.\n\n"
             "Save it for the trailer. Which line do you never write down?",
  "hashtags": "#setuplog #suspensionsetup #motocross #enduro #dialedoffroad",
  "story": "Poll on the cover: \"Do you keep a setup log?\" Notebook / Phone / In my head.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "THE SETUP LOG. WHAT TO WRITE DOWN.",
    "sub": "Save this for the trailer.", "footer": "Six lines. Every ride."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "WHERE AND WHAT DIRT",
    "fix": "Home track, hardpack, dry",
    "why": "The same clickers feel different in sand and on hardpack. The dirt is part of the setup."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "ALL FIVE CLICKERS",
    "fix": "F 12 / 18  ·  S 15 / 1 1/2 / 15",
    "why": "Counted out from fully closed, fork then shock. Bikes get bumped, so count before you ride."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "SAG AND TIRE PRESSURE",
    "fix": "Sag 105 mm  ·  13 / 13 psi",
    "why": "Both change how the bike feels before any clicker does. Check them on the day, cold."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "WHAT THE BIKE DID",
    "fix": "Rear kicks in braking bumps",
    "why": "Describe the bike, not the fix. Where on the track, and how bad."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "THE ONE CHANGE YOU MADE",
    "fix": "Shock rebound 15 to 14, 1 in",
    "why": "One clicker, how many clicks, which way. If you changed two things, you can't tell which one worked."},
   {"type": "symptom", "label": "WRITE DOWN", "label2": "LOOKS LIKE", "head": "BETTER, SAME OR WORSE",
    "fix": "Better. Kicks less, still a bit busy",
    "why": "Worse is useful too. Go back to the last good number and try the other way."},
   {"type": "closer", "head": "WRITE IT DOWN. THEN CHANGE ONE THING.",
    "sub": "Dialed logs every moto, every click and how it felt, so the log writes itself.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Tue Nov 17
 dict(BASE, **{
  "slug": "2026-11-17-kx450-split",
  "title": "Settings card: 2025 Kawasaki KX450",
  "design": "split", "kind": "carousel", "scheduled_at": _at(17, 12),
  "caption": "2025 Kawasaki KX450. About 125 lb, fast, rutted clay moto, stock suspension, stability and jump support "
             "the goals. Left is stock from the 2025 KX450 owner's manual, right is the baseline Dialed built for "
             "that rider.\n\n"
             "Fork comp 12 to 14, fork rebound 12 to 13. Shock low-speed 11 to 12, high-speed 2 turns to 1 1/2, "
             "rebound 13 to 15. Sag set at 105 mm. A light rider on a big bike gets less compression and a quicker "
             "return on most clickers, with half a turn of high-speed in for the landings.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Lighter riders on a 450: what did you change first?",
  "hashtags": "#kx450 #kawasaki #motocross #suspension #dialedoffroad",
  "story": "Poll on the split: \"Light rider on a 450?\" Love it / Too much bike / Never tried.",
  "slides": [
   {"type": "hot", "head": "2025 KAWASAKI KX450. RUTTED CLAY, ABOUT 125 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 2 clicks out", "A softer front for a light rider in ruts."),
    ("Shock rebound, 2 clicks out", "A quicker return so the rear doesn't pack."),
    ("Fork rebound and low-speed, 1 out", "Small moves to match."),
    ("High-speed, 1/2 turn in", "Support for the jump landings."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 12", "Fork reb 12", "Shock low 11", "High-speed 2", "Shock reb 13", "Sag: see manual"],
            "right": "DIALED",
            "right_lines": ["Fork comp 14", "Fork reb 13", "Shock low 12", "High-speed 1 1/2", "Shock reb 15", "Sag 105 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-17-clickers-dont-hold-it-up",
  "title": "Carousel: clickers, preload and springs",
  "design": "dials", "kind": "carousel", "scheduled_at": _at(17, 18),
  "caption": "Riders turn clickers in to fix a bike that sits too low, and crank preload to make it stiffer. Neither "
             "does what they hoped. Clickers, preload and springs each do one job.\n\n"
             "Get the spring and sag right first, then work the clickers one change at a time, counted out from fully "
             "closed.\n\n"
             "Which one did you have mixed up?",
  "hashtags": "#springrate #sag #suspensiontuning #motocross #dialedoffroad",
  "story": "Quiz sticker on slide 03: \"More preload makes the spring...\" Stiffer / Sit higher / Both.",
  "dials": ["FORK\nCOMP", "FORK\nREB", "SHOCK\nLSC", "SHOCK\nHSC", "SHOCK\nREB"],
  "slides": [
   {"type": "cover", "eyebrow": "SUSPENSION 101", "head": "CLICKERS DON'T HOLD THE BIKE UP.", "footer": "Swipe"},
   {"type": "point", "tag": "CLICKERS  ·  DAMPING", "head": "CLICKERS SET HOW FAST IT MOVES.",
    "body": "Damping only works while the fork or shock is moving. It slows the stroke, it doesn't hold the bike "
            "higher at rest."},
   {"type": "point", "tag": "NOT A CLICKER", "head": "PRELOAD SETS RIDE HEIGHT.",
    "body": "Winding the shock collar sets your sag. It doesn't make the spring any stiffer."},
   {"type": "point", "tag": "SPRING  ·  RATE", "head": "THE SPRING CARRIES YOUR WEIGHT.",
    "body": "Spring rate is how hard it gets per inch of travel. Too soft for you and no clicker or collar fixes it."},
   {"type": "point", "tag": "ORDER  ·  OF WORK", "head": "SPRING, THEN SAG, THEN CLICKERS.",
    "body": "Right spring for your weight, then sag from the manual, then clickers one change at a time."},
   {"type": "closer", "head": "EACH ONE HAS ONE JOB.",
    "sub": "Dialed walks you through sag, then builds your clicker starting point from there.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Wed Nov 18
 dict(BASE, **{
  "slug": "2026-11-18-yz250f-setup-sheet",
  "title": "Settings card: 2026 Yamaha YZ250F",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(18, 12),
  "caption": "2026 Yamaha YZ250F. About 175 lb, learning, hardpack moto, stability and comfort the goals. This is the "
             "baseline Dialed built, next to the standard settings from the 2026 YZ250F owner's service manual.\n\n"
             "Stock is 13 and 12 on the fork, 12 clicks and 1 1/2 turns on the shock, 12 on shock rebound, and "
             "Yamaha's 90 to 100 mm sag window. Dialed went 1 click out on fork comp and 2 out on shock rebound, left "
             "the other three alone and set sag at 100. For a newer rider on hardpack, stock is already close, and "
             "not every click has to move.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Newer riders: have you touched your clickers yet?",
  "hashtags": "#yz250f #yamaha #motocross #suspension #dialedoffroad",
  "story": "Poll on the tiles: \"How many clickers have you moved?\" None / One or two / All five.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2026 YAMAHA YZ250F",
    "sub": "about 175 lb  ·  learning  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2026 Yamaha YZ250F  ·  about 175 lb  ·  learning  ·  hardpack",
    "rows": [("Fork compression", "13", "14"), ("Fork rebound", "12", "12"), ("Shock low-speed comp", "12", "12"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/2 turns"), ("Shock rebound", "12", "14"),
             ("Riding sag", "90 to 100 mm", "100 mm"), ("Springs, fork / shock", "4.7 / 54 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2026 YZ250F owner's service manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 1 click out", "A touch softer up front for hardpack chatter."),
    ("Shock rebound, 2 clicks out", "A quicker return so the rear stays settled."),
    ("Three clickers stay stock", "Not every click has to move."),
    ("Sag at 100 mm", "The top of Yamaha's 90 to 100 window."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2026 YAMAHA YZ250F",
  "sheet_sub": "about 175 lb  ·  learning  ·  hardpack moto",
  "tiles": [("FORK COMP", "14", "stock 13", "1 click out"),
            ("FORK REBOUND", "12", "stock 12", None),
            ("SHOCK LOW-SPEED", "12", "stock 12", None),
            ("SHOCK HIGH-SPEED", "1 1/2", "turns  ·  stock 1 1/2", None),
            ("SHOCK REBOUND", "14", "stock 12", "2 clicks out"),
            ("SPRINGS", "4.7 / 54", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "100 mm",
  "sag_note": "manual says 90 to 100 mm  ·  2026 YZ250F manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-18-winter-truths",
  "title": "Carousel: 5 winter suspension truths",
  "design": "blue_list", "kind": "carousel", "scheduled_at": _at(18, 18),
  "caption": "Cold days change how the bike feels before you touch a clicker. Five things to know before you chase a "
             "setup in winter.\n\n"
             "Let it warm up, check the basics, then change one thing at a time, counted out from fully closed.\n\n"
             "Are you riding through the winter or parking it?",
  "hashtags": "#winterriding #dirtbikes #suspension #enduro #dialedoffroad",
  "story": "Poll: \"Riding this winter?\" Every weekend / When it's dry / Bike's parked.",
  "slides": [
   {"type": "cover", "eyebrow": "WINTER", "head": "5 WINTER SUSPENSION TRUTHS", "footer": "Swipe"},
   {"type": "point", "num": "01", "head": "COLD OIL DAMPS MORE.",
    "body": "Thick oil makes the fork and shock feel stiff for the first laps. Judge a change once it's warm."},
   {"type": "point", "num": "02", "head": "TIRE PRESSURE DROPS IN THE COLD.",
    "body": "Set in a warm garage, it reads lower at a cold track. Check it where you ride."},
   {"type": "point", "num": "03", "head": "AIR FORKS DROP TOO.",
    "body": "Same air, same rule. Check air fork pressure at the temperature you ride in, using the manual's number."},
   {"type": "point", "num": "04", "head": "WINTER GEAR ADDS POUNDS.",
    "body": "Layers and a pack add weight on the bike. Measure sag in what you actually ride in."},
   {"type": "point", "num": "05", "head": "THE OFF SEASON IS SERVICE TIME.",
    "body": "Fork and shock oil wear out. Service now and spring starts on fresh oil."},
   {"type": "closer", "head": "WARM IT UP. THEN CHANGE ONE THING.",
    "sub": "Dialed tracks engine hours next to your setup, so service doesn't sneak up on you.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Thu Nov 19
 dict(BASE, **{
  "slug": "2026-11-19-125xc-split",
  "title": "Settings card: 2024 KTM 125 XC",
  "design": "split", "kind": "carousel", "scheduled_at": _at(19, 12),
  "caption": "2024 KTM 125 XC. About 285 lb, fast, singletrack, stock suspension, stability and grip the goals. Left "
             "is stock from KTM's 2024 125 XC owner's manual, right is the baseline Dialed built for that rider.\n\n"
             "Fork comp 12 to 11, fork rebound 18 to 11. Shock low-speed 15 to 10, high-speed stays at 1 1/2 turns, "
             "rebound stays at 15. Sag stays at the manual's 105 mm. A big rider gets more hold everywhere, with the "
             "biggest move on fork rebound. The manual's spring chart stops at 209 lb, so springs are worth a look "
             "before any clicker.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Bigger riders: what's your 125 XC running?",
  "hashtags": "#ktm #125xc #twostroke #singletrack #dialedoffroad",
  "story": "Question box: \"Big rider, small bike. What's your setup?\" Share a few back.",
  "slides": [
   {"type": "hot", "head": "2024 KTM 125 XC. SINGLETRACK, ABOUT 285 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 7 clicks in", "The big one: a calmer front for a heavy rider."),
    ("Shock low-speed, 5 clicks in", "Holds the rear up on the gas."),
    ("Fork comp, 1 click in", "A little more support up front."),
    ("Springs first", "The manual's chart stops at 209 lb."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 12", "Fork reb 18", "Shock low 15", "High-speed 1 1/2", "Shock reb 15", "Sag 105 mm"],
            "right": "DIALED",
            "right_lines": ["Fork comp 11", "Fork reb 11", "Shock low 10", "High-speed 1 1/2", "Shock reb 15", "Sag 105 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-19-spring-check",
  "title": "Carousel: is your shock spring right for you?",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(19, 18),
  "paper_footer": "Riding sag first. Then static sag tells you about the spring.",
  "caption": "Two sag numbers tell you if the shock spring suits your weight. Set riding sag first, then read the "
             "static sag. Here's how to read it.\n\n"
             "Get the spring right before you work the clickers, one change at a time, counted out from fully "
             "closed.\n\n"
             "Save it for the next time you grab the tape. Have you ever checked static sag?",
  "hashtags": "#springrate #sag #shocksetup #dirtbikes #dialedoffroad",
  "story": "Quiz sticker on slide 03: \"Static sag too small means the spring is...\" Too soft / Too stiff.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "IS YOUR SHOCK SPRING RIGHT FOR YOU?",
    "sub": "Two sag numbers tell you.", "footer": "Save this before you grab the tape."},
   {"type": "symptom", "label": "STEP 1", "label2": "TARGET", "head": "SET RIDING SAG",
    "fix": "Your manual's number",
    "why": "You on the bike in your gear. KTM's 2024 250 SX-F and 125 XC say 105 mm. Yamaha says 90 to 100."},
   {"type": "symptom", "label": "STEP 2", "label2": "TARGET", "head": "THEN MEASURE STATIC SAG",
    "fix": "35 mm on those KTMs",
    "why": "The bike on its own weight, no rider. Leave the preload where riding sag put it."},
   {"type": "symptom", "label": "READING", "label2": "MEANS", "head": "STATIC SAG TOO SMALL",
    "fix": "Spring too soft for you",
    "why": "It took a lot of preload to reach riding sag, so the bike tops out with you off it."},
   {"type": "symptom", "label": "READING", "label2": "MEANS", "head": "STATIC SAG TOO BIG",
    "fix": "Spring too stiff for you",
    "why": "Barely any preload reached riding sag, so the bike sits down under its own weight."},
   {"type": "symptom", "label": "CHECK", "label2": "2024 KTM 250 SX-F", "head": "THE MANUAL'S SPRING CHART",
    "fix": "39, 42 or 45 N/mm",
    "why": "For 143 to 165 lb, 165 to 187 lb and 187 to 209 lb riders. Most manuals print a chart like it."},
   {"type": "closer", "head": "RIGHT SPRING. THEN SAG. THEN CLICKERS.",
    "sub": "Dialed walks you through riding sag before it builds your starting point.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Fri Nov 20
 dict(BASE, **{
  "slug": "2026-11-20-crf250r-setup-sheet",
  "title": "Settings card: 2022 Honda CRF250R",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(20, 12),
  "caption": "2022 Honda CRF250R. About 195 lb, fast, hardpack moto, stock suspension, stability and jump support the "
             "goals. This is the baseline Dialed built, next to the standard settings from Honda's CRF250R "
             "competition handbook (Honda Motor Europe edition).\n\n"
             "Stock is 12 and 13 on the fork, 6 clicks and 2 1/6 turns on the shock, 11 on shock rebound, 105 mm of "
             "riding sag. Dialed went 1 click in on fork comp, 3 in on fork rebound, 4 out on low-speed, 5/6 of a "
             "turn in on high-speed and 1 out on shock rebound. Sag stays at 105. Low-speed went softer while "
             "high-speed went firmer: more grip on the gas, more hold on the big hits.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "CRF250R riders: is your shock low-speed still at 6?",
  "hashtags": "#crf250r #honda #motocross #suspension #dialedoffroad",
  "story": "Quiz sticker: \"Honda's stock shock high-speed on the 2022 CRF250R?\" 1 1/2 / 2 / 2 1/6 turns.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2022 HONDA CRF250R",
    "sub": "about 195 lb  ·  fast  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2022 Honda CRF250R  ·  about 195 lb  ·  fast  ·  hardpack moto",
    "rows": [("Fork compression", "12", "11"), ("Fork rebound", "13", "10"), ("Shock low-speed comp", "6", "10"),
             ("Shock high-speed comp", "2 1/6 turns", "1 1/3 turns"), ("Shock rebound", "11", "12"),
             ("Riding sag", "105 mm", "105 mm"), ("Springs, fork / shock", "4.8 / 50 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from Honda's CRF250R competition handbook (Europe)."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Shock low-speed, 4 clicks out", "More grip and squat on the gas."),
    ("High-speed, 5/6 turn in", "More hold on landings and square edges."),
    ("Fork rebound, 3 clicks in", "A calmer front off jump faces."),
    ("Fork comp 1 in, shock rebound 1 out", "Small moves. Sag stays 105 mm."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2022 HONDA CRF250R",
  "sheet_sub": "about 195 lb  ·  fast  ·  hardpack moto  ·  Showa coil fork",
  "tiles": [("FORK COMP", "11", "stock 12", "1 click in"),
            ("FORK REBOUND", "10", "stock 13", "3 clicks in"),
            ("SHOCK LOW-SPEED", "10", "stock 6", "4 clicks out"),
            ("SHOCK HIGH-SPEED", "1 1/3", "turns  ·  stock 2 1/6", "5/6 turn in"),
            ("SHOCK REBOUND", "12", "stock 11", "1 click out"),
            ("SPRINGS", "4.8 / 50", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "105 mm",
  "sag_note": "manual says 105 mm  ·  Honda handbook",
 }),
 dict(BASE, **{
  "slug": "2026-11-20-ride-mode",
  "title": "App screens: ride mode, one moto at a time",
  "design": "screens", "kind": "carousel", "scheduled_at": _at(20, 18),
  "big": "3.0", "sticker": "RIDE MODE", "footer": FOOT,
  "frames": [
   ("RIDE IT.", "THEN TUNE IT.", "Start a moto, ride, log it when you're off the bike. Your settings are right there.", 1),
   ("TELL IT WHAT", "THE BIKE DID.", "Better, same or worse, then tap what you felt. Front pushes, rear kicks, harsh on small bumps.", 2),
   ("ONE CHANGE.", "WHICH WAY.", "Which clicker, how many clicks and which way, counted out from fully closed.", 3),
   ("DAY WRAPPED.", "SAVED.", "Motos logged, changes turned and engine hours, saved with the setup for next time.", 4),
  ],
  "caption": "Ride mode is the part of Dialed you use with your helmet on the seat. Start a moto, ride it, then tap "
             "what the bike did. It gives you one change, which clicker and which way, and logs the day when you "
             "wrap it.\n\n"
             "Starting points you refine on the bike, one change at a time, counted out from fully closed.\n\n"
             "Link in bio. How many motos does it usually take you to find a setup?",
  "hashtags": "#motocross #enduro #suspensionsetup #rideday #dialedoffroad",
  "story": "Share slide 02 with the link sticker: \"Tell it what the bike did.\"",
  "slides": [],
 }),
 # ------------------------------------------------------------------ Sat Nov 21
 dict(BASE, **{
  "slug": "2026-11-21-yz250fx-split",
  "title": "Settings card: 2027 Yamaha YZ250FX",
  "design": "split", "kind": "carousel", "scheduled_at": _at(21, 12),
  "caption": "2027 Yamaha YZ250FX. About 255 lb, learning, singletrack, stock suspension, stability and comfort the "
             "goals. Left is stock from the 2027 YZ250FX owner's service manual, right is the baseline Dialed built "
             "for that rider.\n\n"
             "Fork comp 7 to 13, fork rebound 7 to 12. Shock low-speed 10 to 12, high-speed 1 5/8 turns to 1 3/8, "
             "rebound 10 to 13. Sag 100 mm, the top of Yamaha's 90 to 100 window. Comfort and a newer rider drove it: "
             "compression and rebound came out, with a quarter turn of high-speed in for the big hits. Six clicks is "
             "a big move, so if it starts to bottom, come back toward stock two at a time.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "FX riders: does yours feel stiff in the tight stuff?",
  "hashtags": "#yz250fx #yamaha #singletrack #enduro #dialedoffroad",
  "story": "Poll on the split: \"Stock FX in the woods?\" Too stiff / Just right / Too soft.",
  "slides": [
   {"type": "hot", "head": "2027 YAMAHA YZ250FX. SINGLETRACK, ABOUT 255 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp 6 out, rebound 5 out", "A softer, quicker front for roots and rocks."),
    ("Shock rebound, 3 clicks out", "The rear comes back in time for the next hit."),
    ("Low-speed 2 out, high-speed 1/4 in", "Grip on the gas, hold on big hits."),
    ("Sag at 100 mm", "The top of Yamaha's 90 to 100 window."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 7", "Fork reb 7", "Shock low 10", "High-speed 1 5/8", "Shock reb 10", "Sag 90 to 100"],
            "right": "DIALED",
            "right_lines": ["Fork comp 13", "Fork reb 12", "Shock low 12", "High-speed 1 3/8", "Shock reb 13", "Sag 100 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-21-cost-answer",
  "title": "Comment answer: is Dialed free?",
  "design": "classic", "kind": "carousel", "scheduled_at": _at(21, 18),
  "caption": "Someone asked in the comments if Dialed is free or a subscription. Straight answer: you get 7 days with "
             "everything unlocked. After that, Pro is $7.99 a month or $59.99 a year, and you can cancel any time "
             "in the store.\n\n"
             "Build your first starting point, ride it, and refine it on the bike one change at a time, counted out "
             "from fully closed. Then decide.\n\n"
             "Link in bio. What would you want a setup app to do that none of them do yet?",
  "hashtags": "#dirtbikes #motocross #enduro #suspension #dialedoffroad",
  "story": "Question box: \"What should Dialed do next?\" Share the best answers back.",
  "slides": [
   {"type": "hot", "head": "IS DIALED FREE?",
    "sub": "Someone asked in the comments. 7 days with everything unlocked. Then Pro is $7.99 a month or $59.99 a "
           "year."},
   {"type": "points", "title": "IN THE 7 DAYS", "items": [
    ("A starting point for your bike", "Your weight, your track, the manual's stock."),
    ("Ride mode and the refine loop", "Tap what the bike did, get one change."),
    ("Setups saved per track", "Every click logged on the bike."),
    ("Cancel any time", "In the App Store or Google Play."),
   ]},
   {"type": "closer", "head": "BUILD YOURS. RIDE IT. THEN DECIDE.",
    "sub": "Starting points you refine on the bike, one change at a time.", "footer": FOOT},
  ],
 }),
]
