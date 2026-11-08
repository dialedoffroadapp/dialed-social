# Week of 2026-11-08 (posts Mon Nov 9 to Sat Nov 14). Bike card at 12:40 pm Boise every day (all carousels now),
# tip at 6:40 pm. Animated explainer reels Mon, Wed, Fri at 3:40 pm come from tools/anim (out/anim/2026-11-08).
# The approved YouTube-only shorts in social_posts (7:10, 10:40, 1:10, 4:40, 7:10) do not touch IG, FB or TikTok,
# so they do not block these slots (same as the week of Nov 1).
# Bike cards: stock from bike_model_specs on prod (oem_manual), Dialed from a real setup_versions baseline.
#   Mon 2025 KTM 300 EXC       Owner's Manual 2025 250/300 EXC, XC-W, part 3240047en (all, standard)
#   Tue 2024 Kawasaki KX450    Owner's Manual 2024 KX450 (KX450M), part 99803-0401 (us); no sag figure in the catalog
#   Wed 2024 Husqvarna FC 250  Husqvarna owner's manual 2024 FC 250, part 3402713e (us, standard)
#   Thu 2026 Yamaha YZ125      2026 Owner's Service Manual YZ125, part D68-2819U-11 (us, standard)
#   Fri 2022 Kawasaki KX250    Owner's Manual 2022 KX252C/D, part 99803-0214 (us); no sag figure in the catalog
#   Sat 2024 KTM 250 XC        Owner's Manual 2024 250/300 SX, 250/300 XC, part 3214833en (us, standard)
# Skipped: 2024 Beta RR 2T 300 (the one bike request) has no setup_versions row; 2023 Honda CRF250R and 2024 CRF450R
# (top tuned) have no stock clicker rows in the catalog.
import datetime as _dt
from zoneinfo import ZoneInfo as _Z

_B = _Z("America/Boise")


def _at(day, hour):
    return _dt.datetime(2026, 11, day, hour, 40, tzinfo=_B).astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


FOOT = "Dialed Offroad 3.0  ·  App Store  ·  Google Play"
CTA = "Drop your bike, year and weight below and I'll run yours."
BASE = {"post_to_ig": True, "post_to_fb": True, "fb_mode": "cover"}

WEEK = [
 # ------------------------------------------------------------------ Mon Nov 9
 dict(BASE, **{
  "slug": "2026-11-09-300exc-setup-sheet",
  "title": "Settings card: 2025 KTM 300 EXC / XC-W",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(9, 12),
  "caption": "2025 KTM 300 EXC and 300 XC-W. Same manual, same stock numbers, so this one is for both. About 160 lb, fast, hard enduro, stability and grip the goals. This is the baseline "
             "Dialed built, next to the standard settings from KTM's 2025 owner's manual for the 250 and 300 EXC and "
             "XC-W.\n\n"
             "Stock is 15 and 17 on the fork, 15 clicks and 2 turns on the shock, 15 on shock rebound, 110 mm of "
             "rider sag. Dialed went 3 clicks in on fork comp, 5 in on fork rebound, 5 in on low-speed, half a turn in "
             "on high-speed and 3 in on shock rebound. Sag stays at 110. Five clicks is a big move, so if it feels "
             "harsh in the rocks, come back toward stock two clicks at a time.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "What's your 300 running for the gnarly stuff?",
  "hashtags": "#ktm #300exc #300xcw #hardenduro #dialedoffroad",
  "story": "Poll on the sheet slide: \"Hard enduro: firmer or softer than stock?\" Firmer / Softer / Never changed it.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2025 KTM 300 EXC / XC-W",
    "sub": "about 160 lb  ·  fast  ·  hard enduro", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2025 KTM 300 EXC / XC-W  ·  about 160 lb  ·  fast  ·  hard enduro",
    "rows": [("Fork compression", "15", "12"), ("Fork rebound", "17", "12"), ("Shock low-speed comp", "15", "10"),
             ("Shock high-speed comp", "2 turns", "1 1/2 turns"), ("Shock rebound", "15", "12"),
             ("Rider sag", "110 mm", "110 mm"), ("Springs for 65 to 75 kg", "4.2 / 66 N/mm", "manual's row")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2025 KTM 250/300 EXC and XC-W owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 5 clicks in", "A slower return keeps the front calm off ledges."),
    ("Shock low-speed, 5 clicks in", "More hold for the rear on steep climbs."),
    ("Fork comp and shock rebound, 3 in", "More support up front, less kick out back."),
    ("Sag stays at 110 mm", "KTM's number. Set it before any click."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2025 KTM 300 EXC / XC-W",
  "sheet_sub": "about 160 lb  ·  fast  ·  hard enduro  ·  WP XPLOR fork",
  "tiles": [("FORK COMP", "12", "stock 15", "3 clicks in"),
            ("FORK REBOUND", "12", "stock 17", "5 clicks in"),
            ("SHOCK LOW-SPEED", "10", "stock 15", "5 clicks in"),
            ("SHOCK HIGH-SPEED", "1 1/2", "turns  ·  stock 2", "1/2 turn in"),
            ("SHOCK REBOUND", "12", "stock 15", "3 clicks in"),
            ("SPRINGS FOR 160 LB", "4.2 / 66", "N/mm  ·  manual, 65 to 75 kg", None)],
  "sag_value": "110 mm",
  "sag_note": "manual says 110 mm  ·  2025 KTM owner's manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-09-sag-by-manual",
  "title": "Carousel: riding sag by manual cheat sheet",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(9, 18),
  "paper_footer": "Riding sag: with you on the bike, in your gear.",
  "caption": "Riding sag is the first number every clicker setting assumes, and the manuals don't all agree. Here's "
             "what the 2025 and 2026 owner's manuals in our catalog say, brand by brand, plus how to measure it.\n\n"
             "Set sag first, then start on the clickers, one change at a time, counted out from fully closed.\n\n"
             "Save it for the next time you grab the tape. What's your bike's sag at right now?",
  "hashtags": "#sag #suspensionsetup #motocross #enduro #dialedoffroad",
  "story": "Quiz sticker on the Yamaha slide: \"Yamaha's sag window?\" 80 to 90 / 90 to 100 / 105 flat.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "RIDING SAG. WHAT EACH MANUAL SAYS.",
    "sub": "Save this before you grab the tape.", "footer": "From the 2025 and 2026 owner's manuals."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "KTM, HUSQVARNA, GASGAS MOTOCROSS",
    "fix": "105 mm",
    "why": "SX, SX-F, TC, FC and MC manuals. KTM's XC and XC-F cross-country bikes say 105 mm too."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "KTM, HUSQVARNA, GASGAS ENDURO",
    "fix": "110 mm",
    "why": "EXC, XC-W, TE, FE and EC manuals. The enduro bikes run 5 mm more than their motocross cousins."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "YAMAHA YZ, YZ-F, YZ-X, FX AND WR",
    "fix": "90 to 100 mm",
    "why": "Yamaha gives a window, not one number. Pick a spot in it, ride, and move from there."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "SHERCO SE AND SEF FACTORY",
    "fix": "95 to 100 mm",
    "why": "From the 2025 and 2026 Sherco owner's manuals for the two-strokes and four-strokes."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "85 CC BIKES",
    "fix": "100 mm",
    "why": "KTM 85 SX, Husqvarna TC 85 and GasGas MC 85. The 50s and 65s say 80 mm."},
   {"type": "symptom", "label": "BIKES", "label2": "MANUAL SAYS", "head": "HONDA AND KAWASAKI",
    "fix": "Check your manual",
    "why": "Our catalog has no riding sag figure from these manuals yet, so we won't guess one."},
   {"type": "symptom", "label": "HOW TO MEASURE", "label2": "MEASURE", "head": "RIDING SAG, STEP BY STEP",
    "fix": "Rear axle to a mark on the fender",
    "why": "Measure on a stand, then with you on the bike in your gear. The difference is your riding sag."},
   {"type": "closer", "head": "SAG FIRST. THEN CLICKERS.",
    "sub": "Dialed walks you through measuring it, then builds your starting point from there.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Tue Nov 10
 dict(BASE, **{
  "slug": "2026-11-10-kx450-split",
  "title": "Settings card: 2024 Kawasaki KX450",
  "design": "split", "kind": "carousel", "scheduled_at": _at(10, 12),
  "caption": "2024 Kawasaki KX450. About 205 lb, fast, hardpack moto, stability and jump support the goals. Left is "
             "stock from the 2024 KX450 owner's manual, right is the baseline Dialed built for that rider.\n\n"
             "Fork comp 12 to 11, fork rebound 12 to 10. Shock low-speed 11 to 9, high-speed 2 turns to 1 1/4, "
             "rebound 13 to 12. Sag set at 105 mm. A heavier, fast rider on the stock springs gets a little more hold "
             "everywhere, with the biggest move on high-speed for the landings.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Big KX owners: where does yours feel worst, landings or braking bumps?",
  "hashtags": "#kx450 #kawasaki #motocross #suspension #dialedoffroad",
  "story": "Poll on the split: \"Ever touched high-speed comp?\" Yes / No / That's the big nut?",
  "slides": [
   {"type": "hot", "head": "2024 KAWASAKI KX450. HARDPACK, ABOUT 205 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("High-speed, 3/4 turn in", "The biggest move: support on big landings."),
    ("Low-speed 2 in, fork rebound 2 in", "More hold and a calmer front off jump faces."),
    ("Fork comp and shock rebound, 1 in", "Small moves to match."),
    ("Springs stay stock", "5.0 fork, 54 shock, from the manual."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA},
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 12", "Fork reb 12", "Shock low 11", "High-speed 2", "Shock reb 13", "Sag: see manual"],
            "right": "DIALED",
            "right_lines": ["Fork comp 11", "Fork reb 10", "Shock low 9", "High-speed 1 1/4", "Shock reb 12", "Sag 105 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-10-clickers-work-together",
  "title": "Carousel: your clickers don't work alone",
  "design": "dials", "kind": "carousel", "scheduled_at": _at(10, 18),
  "caption": "A rider pointed out in the comments that shock rebound can change how low-speed compression feels. He's "
             "right, and it's not the only pair that talks to each other.\n\n"
             "Four ways one change shows up somewhere else, and why one change at a time, counted out from fully "
             "closed, is the only way to know what did what.\n\n"
             "Which change surprised you the most?",
  "hashtags": "#clickers #suspensiontuning #motocross #enduro #dialedoffroad",
  "story": "Share slide 02 with a question box: \"What's a change that fixed one thing and broke another?\"",
  "dials": ["FORK\nCOMP", "FORK\nREB", "SHOCK\nLSC", "SHOCK\nHSC", "SHOCK\nREB"],
  "slides": [
   {"type": "cover", "eyebrow": "SUSPENSION 101", "head": "YOUR CLICKERS DON'T WORK ALONE.", "footer": "Swipe"},
   {"type": "point", "tag": "SHOCK  ·  REBOUND", "head": "REBOUND CAN NUDGE LOW-SPEED.",
    "body": "On many shocks rebound and compression share oil and the main piston, so a big rebound move can change "
            "how low-speed feels."},
   {"type": "point", "tag": "SAG  ·  REBOUND", "head": "SAG CHANGES HOW REBOUND FEELS.",
    "body": "New sag puts the shock in a different part of its stroke. Recheck rebound after any sag change."},
   {"type": "point", "tag": "FORK  ·  SHOCK", "head": "CHANGE ONE END, FEEL BOTH.",
    "body": "Firm up the fork and the bike pitches differently, so the rear can feel different too. Ride a few laps "
            "before you chase the other end."},
   {"type": "point", "tag": "SHOCK  ·  HIGH AND LOW", "head": "TWO ADJUSTERS, ONE SPOT.",
    "body": "On most shocks the high-speed nut sits around the low-speed screw. Hold one still while you turn the "
            "other, then count both again."},
   {"type": "closer", "head": "ONE CHANGE. RIDE. THEN THE NEXT.",
    "sub": "Dialed logs every click, so you can see which change did what.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Wed Nov 11
 dict(BASE, **{
  "slug": "2026-11-11-fc250-setup-sheet",
  "title": "Settings card: 2024 Husqvarna FC 250",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(11, 12),
  "caption": "2024 Husqvarna FC 250. About 190 lb, fast, rutted clay moto, stock suspension, stability and jump "
             "support the goals. This is the baseline Dialed built, next to the standard settings from the 2024 "
             "Husqvarna FC 250 owner's manual.\n\n"
             "Stock is 12 and 18 on the fork, 15 clicks and 1 1/2 turns on the shock, 15 on shock rebound, 105 mm of "
             "riding sag. Dialed kept fork comp, went 7 clicks in on fork rebound, 5 in on low-speed, a quarter turn "
             "in on high-speed and 2 in on shock rebound. Seven clicks is a big move: if the front starts to pack in "
             "the ruts, come back toward stock two at a time. Fork air: set it from the manual for your weight.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "FC 250 riders: what's your fork rebound at?",
  "hashtags": "#husqvarna #fc250 #motocross #suspension #dialedoffroad",
  "story": "Quiz sticker: \"Stock fork rebound on a 2024 FC 250?\" 12 / 15 / 18.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2024 HUSQVARNA FC 250",
    "sub": "about 190 lb  ·  fast  ·  rutted clay moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2024 Husqvarna FC 250  ·  about 190 lb  ·  fast  ·  rutted clay",
    "rows": [("Fork compression", "12", "12"), ("Fork rebound", "18", "11"), ("Shock low-speed comp", "15", "10"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/4 turns"), ("Shock rebound", "15", "13"),
             ("Riding sag", "105 mm", "105 mm"), ("Shock spring, 187 to 209 lb", "45 N/mm", "manual's row")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2024 Husqvarna FC 250 owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 7 clicks in", "The big one: a slower front stays down in ruts."),
    ("Shock low-speed, 5 clicks in", "Holds a 190 lb rider up on the gas."),
    ("Shock rebound 2 in, high-speed 1/4 in", "Small moves to match the front."),
    ("Fork comp and sag stay put", "Set 105 mm of sag before any click."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2024 FC 250",
  "sheet_sub": "Husqvarna  ·  about 190 lb  ·  fast  ·  rutted clay  ·  WP XACT AER fork",
  "tiles": [("FORK COMP", "12", "stock 12", None),
            ("FORK REBOUND", "11", "stock 18", "7 clicks in"),
            ("SHOCK LOW-SPEED", "10", "stock 15", "5 clicks in"),
            ("SHOCK HIGH-SPEED", "1 1/4", "turns  ·  stock 1 1/2", "1/4 turn in"),
            ("SHOCK REBOUND", "13", "stock 15", "2 clicks in"),
            ("SHOCK SPRING", "45", "N/mm  ·  manual, 187 to 209 lb", None)],
  "sag_value": "105 mm",
  "sag_note": "manual says 105 mm  ·  2024 Husqvarna manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-11-clickers-cant-fix-it",
  "title": "Carousel: when clickers can't fix it",
  "design": "blue_list", "kind": "carousel", "scheduled_at": _at(11, 18),
  "caption": "Clickers tune a healthy fork and shock. They can't fix a tired one. Five signs it's time for a service "
             "or a spring, not another click.\n\n"
             "Rule these out, then go back to starting points and one change at a time, counted out from fully "
             "closed.\n\n"
             "Which one have you been chasing with clickers?",
  "hashtags": "#suspensionservice #dirtbikes #motocross #enduro #dialedoffroad",
  "story": "Poll: \"When did you last service your fork?\" This year / Last year / Never.",
  "slides": [
   {"type": "cover", "eyebrow": "SERVICE", "head": "5 THINGS NO CLICKER CAN FIX", "footer": "Swipe"},
   {"type": "point", "num": "01", "head": "OIL ON THE FORK TUBES.",
    "body": "A leaking seal lets oil out and dirt in. Clean under the dust seal first. If it keeps weeping, plan a "
            "service."},
   {"type": "point", "num": "02", "head": "IT FADES BY THE END OF A MOTO.",
    "body": "Fine for ten minutes, then harsh or vague. Worn, hot oil damps less. That's a service, not a click."},
   {"type": "point", "num": "03", "head": "THE CLICKER CHANGES NOTHING.",
    "body": "Four clicks and no feel at all? Count the full range gently. A short range or no stop needs a look."},
   {"type": "point", "num": "04", "head": "YOU CAN'T HIT THE MANUAL'S SAG.",
    "body": "If a sensible preload won't get you to the manual's sag, the spring rate is wrong for your weight."},
   {"type": "point", "num": "05", "head": "CLUNKS OR PLAY OUT BACK.",
    "body": "Lift the rear and feel for slop. Worn linkage bearings or bushings feel like bad damping."},
   {"type": "closer", "head": "CLICKERS TUNE IT. THEY DON'T FIX IT.",
    "sub": "Dialed keeps engine hours next to your setup, so service doesn't sneak up on you.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Thu Nov 12
 dict(BASE, **{
  "slug": "2026-11-12-yz125-split",
  "title": "Settings card: 2026 Yamaha YZ125",
  "design": "split", "kind": "carousel", "scheduled_at": _at(12, 12),
  "caption": "2026 Yamaha YZ125. About 155 lb, fast, hardpack moto, stability and jump support the goals. Left is "
             "stock from the 2026 YZ125 owner's service manual, right is the baseline Dialed built for that rider.\n\n"
             "Fork comp 10 to 12, fork rebound 11 to 12. Shock low-speed 12 to 10, high-speed 1 1/2 turns to 1, "
             "rebound 10 to 12. Sag 100 mm, the top of Yamaha's 90 to 100 window. A plusher front for the chatter, "
             "more hold out back for the jumps.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "125 riders: what did you change first?",
  "hashtags": "#yz125 #yamaha #twostroke #motocross #dialedoffroad",
  "story": "Poll: \"Best first bike to learn clickers on?\" 125 two-stroke / 250F.",
  "slides": [
   {"type": "hot", "head": "2026 YZ125. HARDPACK, ABOUT 155 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp 2 out, rebound 1 out", "A plusher front for hardpack chatter."),
    ("Low-speed 2 in, high-speed 1/2 in", "Holds the rear up on the gas and on landings."),
    ("Shock rebound, 2 clicks out", "A quicker return so the rear doesn't pack."),
    ("Sag at 100 mm", "The top of Yamaha's 90 to 100 window."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA},
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 10", "Fork reb 11", "Shock low 12", "High-speed 1 1/2", "Shock reb 10", "Sag 90 to 100"],
            "right": "DIALED",
            "right_lines": ["Fork comp 12", "Fork reb 12", "Shock low 10", "High-speed 1", "Shock reb 12", "Sag 100 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-12-saved-setups",
  "title": "App screens: a saved setup for every track",
  "design": "screens", "kind": "carousel", "scheduled_at": _at(12, 18),
  "big": "3.0", "sticker": "SAVED SETUPS", "footer": FOOT,
  "frames": [
   ("ONE BIKE.", "A SETUP PER TRACK.", "Hardpack, singletrack, your home track. Each one saved on the bike in your garage.", 5),
   ("RIDE IT.", "TAP WHAT IT DID.", "Front pushes, rear kicks, harsh on small bumps. One tap after the moto.", 2),
   ("ONE CHANGE.", "WHICH WAY.", "Which clicker, how many clicks and which way, counted out from fully closed.", 3),
   ("SAVED FOR", "NEXT TIME.", "Every change you turned is logged, so next weekend starts where this one ended.", 4),
  ],
  "caption": "One setup for every track is a compromise you picked by accident. Dialed keeps a saved setup per place "
             "you ride, on the same bike: hardpack, singletrack, your home track.\n\n"
             "Ride it, tap what the bike did, make one change, and it's saved for next time. Starting points you "
             "refine on the bike, counted out from fully closed.\n\n"
             "Link in bio. How many setups would your bike need?",
  "hashtags": "#motocross #enduro #suspensionsetup #dirtbikes #dialedoffroad",
  "story": "Share slide 02 with the link sticker: \"One bike, a setup for every track.\"",
  "slides": [],
 }),
 # ------------------------------------------------------------------ Fri Nov 13
 dict(BASE, **{
  "slug": "2026-11-13-kx250-setup-sheet",
  "title": "Settings card: 2022 Kawasaki KX250",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(13, 12),
  "caption": "2022 Kawasaki KX250. About 175 lb, comfortable pace, hardpack moto, stock suspension, stability and "
             "comfort the goals. This is the baseline Dialed built, next to the stock settings from the 2022 KX250 "
             "owner's manual.\n\n"
             "Stock is 12 and 11 on the fork, 10 clicks and 1 1/2 turns on the shock, 15 on shock rebound. Dialed "
             "went 2 clicks out on fork comp, 1 out on fork rebound, 2 out on low-speed and 1 in on shock rebound, and "
             "set sag at 103 mm. Comfort was the goal, so compression came out on both ends.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Comfort or support: which one does your KX250 need more?",
  "hashtags": "#kx250 #kawasaki #motocross #suspension #dialedoffroad",
  "story": "Poll on the sheet slide: \"Your bike feels...\" Too stiff / Too soft / Can't tell.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2022 KAWASAKI KX250",
    "sub": "about 175 lb  ·  comfortable pace  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2022 Kawasaki KX250  ·  about 175 lb  ·  hardpack moto",
    "rows": [("Fork compression", "12", "14"), ("Fork rebound", "11", "12"), ("Shock low-speed comp", "10", "12"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/2 turns"), ("Shock rebound", "15", "14"),
             ("Riding sag", "see manual", "103 mm"), ("Springs, fork / shock", "4.9 / 54 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2022 KX250 owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Compression out on both ends", "Fork 2 clicks, shock low-speed 2. Comfort first."),
    ("Fork rebound, 1 click out", "Keeps pace with the softer fork."),
    ("Shock rebound, 1 click in", "A touch slower so the rear stays calm."),
    ("High-speed and springs stay put", "Not every click has to move."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2022 KAWASAKI KX250",
  "sheet_sub": "about 175 lb  ·  comfortable pace  ·  hardpack moto",
  "tiles": [("FORK COMP", "14", "stock 12", "2 clicks out"),
            ("FORK REBOUND", "12", "stock 11", "1 click out"),
            ("SHOCK LOW-SPEED", "12", "stock 10", "2 clicks out"),
            ("SHOCK HIGH-SPEED", "1 1/2", "turns  ·  stock 1 1/2", None),
            ("SHOCK REBOUND", "14", "stock 15", "1 click in"),
            ("SPRINGS", "4.9 / 54", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "103 mm",
  "sag_note": "Dialed starting point  ·  measure yours first",
 }),
 dict(BASE, **{
  "slug": "2026-11-13-pre-ride-check",
  "title": "Carousel: the five minute suspension check",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(13, 18),
  "paper_footer": "Five minutes in the pits. Before every ride.",
  "caption": "Five minutes in the pits saves a day of chasing the wrong clicker. Six checks before the first moto, "
             "every time.\n\n"
             "Then ride it and change one thing at a time, counted out from fully closed, and write down what you "
             "did.\n\n"
             "Save it for the trailer. Which one do you always skip?",
  "hashtags": "#preride #dirtbikes #motocross #enduro #dialedoffroad",
  "story": "Share the cover with a poll: \"Do you check sag before every ride?\" Always / Sometimes / Never.",
  "slides": [
   {"type": "cover", "eyebrow": "CHECKLIST", "head": "THE 5 MINUTE SUSPENSION CHECK",
    "sub": "Save this for the pits.", "footer": "Before the first moto. Every time."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "CLICKERS WHERE YOU LEFT THEM",
    "fix": "Count in to closed, then back out",
    "why": "Bikes get bumped and borrowed. Turn in gently, never force the stop, and write the numbers down."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "TIRE PRESSURE",
    "fix": "A gauge, with the tires cold",
    "why": "A couple of psi changes how the bike feels before any clicker does."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "BLEED THE FORK",
    "fix": "Coil forks: wheel off the ground, open the bleed screws",
    "why": "Air builds up in the legs as you ride and stiffens the fork. Air forks: set pressure from the manual."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "WIPE THE FORK SEALS",
    "fix": "Clean the tubes and under the dust seals",
    "why": "Dirt on the tubes wears seals fast. Oil on them means a seal is leaking."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "RIDING SAG",
    "fix": "Measure it in your gear",
    "why": "Springs settle and gear changes. If sag moved since last ride, fix it before you touch a clicker."},
   {"type": "symptom", "label": "CHECK", "label2": "HOW", "head": "LINKAGE AND BEARINGS",
    "fix": "Lift the rear, feel for play",
    "why": "Clunks and slop out back feel like bad damping. Rule them out first."},
   {"type": "closer", "head": "CHECKED. NOW RIDE IT AND CHANGE ONE THING.",
    "sub": "Dialed logs your setup and every click you turn, so the next check starts from facts.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Sat Nov 14
 dict(BASE, **{
  "slug": "2026-11-14-250xc-split",
  "title": "Settings card: 2024 KTM 250 XC",
  "design": "split", "kind": "carousel", "scheduled_at": _at(14, 12),
  "caption": "2024 KTM 250 XC. About 155 lb, fast, singletrack, stability and grip the goals. Left is stock from "
             "KTM's 2024 owner's manual for the 250 and 300 SX and XC, right is the baseline Dialed built for that "
             "rider.\n\n"
             "Fork comp 12 to 15, fork rebound 18 to 14. Shock low-speed 15 to 13, high-speed 1 1/2 turns to 1 3/4, "
             "rebound 15 to 16. Sag stays at the manual's 105 mm. A softer front to follow the roots, slowed down so "
             "it stays calm.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Singletrack riders: softer front or stock?",
  "hashtags": "#ktm #250xc #singletrack #twostroke #dialedoffroad",
  "story": "Question box: \"Your favorite singletrack and the bike you ride it on.\" Share a few back.",
  "slides": [
   {"type": "hot", "head": "2024 KTM 250 XC. SINGLETRACK, ABOUT 155 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 3 clicks out", "A softer front follows roots and rocks."),
    ("Fork rebound, 4 clicks in", "A slower return keeps that softer front calm."),
    ("Low-speed 2 in, high-speed 1/4 out", "Holds the rear up, softens the sharp hits."),
    ("Shock rebound 1 out, sag stays 105", "A small move. Sag first, always."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA},
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 12", "Fork reb 18", "Shock low 15", "High-speed 1 1/2", "Shock reb 15", "Sag 105 mm"],
            "right": "DIALED",
            "right_lines": ["Fork comp 15", "Fork reb 14", "Shock low 13", "High-speed 1 3/4", "Shock reb 16", "Sag 105 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-14-no-clickers-answer",
  "title": "Comment answer: no clickers on an older bike",
  "design": "classic", "kind": "carousel", "scheduled_at": _at(14, 18),
  "caption": "Someone in the comments rides a 1984 XR200R and asked what the app can do for a bike with no clickers. "
             "Fair question, and the answer is: more than you'd think.\n\n"
             "Older bikes skip the clickers, not the tuning. Sag, fork oil level, oil weight, fork height and springs "
             "all still move. Same rules: one change at a time, write it down, ride it.\n\n"
             "What's the oldest bike you still ride?",
  "hashtags": "#vintagemx #xr200r #dirtbikes #suspension #dialedoffroad",
  "story": "Question box: \"Post your oldest running bike.\" Share the best ones back.",
  "slides": [
   {"type": "hot", "head": "NO CLICKERS? YOU CAN STILL TUNE IT.",
    "sub": "Someone asked about a 1984 XR200R. Older bikes skip the clickers, not the tuning. Swipe for what still "
           "moves."},
   {"type": "points", "title": "STILL ADJUSTABLE", "items": [
    ("Sag and preload", "Set rear sag with the spring collar first."),
    ("Fork oil level", "More oil adds support deep in the stroke."),
    ("Fork oil weight", "Heavier oil slows compression and rebound."),
    ("Fork height and springs", "Slide the tubes in the clamps. Match springs to you."),
   ]},
   {"type": "closer", "head": "ONE CHANGE AT A TIME. WRITE IT DOWN.",
    "sub": "Dialed's catalog starts at modern bikes with factory clicker settings. Older bikes aren't in it yet."},
  ],
 }),
]
