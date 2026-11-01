# Week of 2026-11-01 (posts Mon Nov 2 to Sat Nov 7). Bike card at 12:40 pm Boise every day, tip at 6:40 pm.
# Mon 6:40 pm is skipped: 2026-11-02-stock-vs-you (week of Oct 26) is already queued there.
# Bike cards: stock from bike_model_specs on prod (oem_manual), Dialed from a real setup_versions baseline.
#   Mon 2024 Kawasaki KX250    Owner's Manual 2024 KX252C/D, part 99803-0400 (us)
#   Tue 2025 KTM 500 EXC-F     Owner's Manual 2025 450/500 EXC-F, part 3240051en (all, standard)
#   Wed 2025 Yamaha YZ250F     2025 Owner's Service Manual YZ250F, part D01-2819U-10 (us, standard)
#   Thu 2026 KTM 150 XC-W      Owner's Manual 2026 150 XC-W US (us, standard)
#   Fri 2023 Kawasaki KX450    Owner's Manual 2023 KX450J/K, part 99803-0308 (us); no shock high-speed or sag figure in the catalog
#   Sat 2026 Yamaha YZ250X     2026 Owner's Service Manual YZ250X, part DF4-2819U-11 (us, standard)
import datetime as _dt
from zoneinfo import ZoneInfo as _Z

_B = _Z("America/Boise")


def _at(day, hour):
    return _dt.datetime(2026, 11, day, hour, 40, tzinfo=_B).astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


FOOT = "Dialed Offroad 3.0  ·  App Store  ·  Google Play"
CTA = "Drop your bike, year and weight below and I'll run yours."
BASE = {"post_to_ig": True, "post_to_fb": True, "fb_mode": "cover"}

WEEK = [
 # ------------------------------------------------------------------ Mon Nov 2
 dict(BASE, **{
  "slug": "2026-11-02-kx250-setup-sheet",
  "title": "Settings card: 2024 Kawasaki KX250",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(2, 12),
  "caption": "2024 Kawasaki KX250. About 185 lb, fast, hardpack moto, stability and jump support the goals. This is the "
             "baseline Dialed built, next to the stock settings from the 2024 KX250 owner's manual.\n\n"
             "Stock is 11 on fork comp and 12 on fork rebound, 12 clicks and 1 1/2 turns on the shock, 13 on shock "
             "rebound. Dialed opened fork comp one click, slowed fork rebound one, went two clicks in on low-speed and "
             "set sag at 103 mm. Everything counted out from fully closed.\n\n"
             "These are starting points riders refine on the bike, one change at a time. Ride it, log how it felt, "
             "move one thing.\n\n"
             "What's your KX250 running on low-speed right now?",
  "hashtags": "#kx250 #kawasaki #motocross #suspension #dialedoffroad",
  "story": "Poll on the sheet slide: \"Ever changed low-speed on your shock?\" Yes / No / Which one is that.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2024 KAWASAKI KX250",
    "sub": "about 185 lb  ·  fast  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2024 Kawasaki KX250  ·  about 185 lb  ·  fast  ·  hardpack moto",
    "rows": [("Fork compression", "11", "12"), ("Fork rebound", "12", "11"), ("Shock low-speed comp", "12", "10"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/2 turns"), ("Shock rebound", "13", "13"),
             ("Riding sag", "see manual", "103 mm"), ("Springs, fork / shock", "4.9 / 54 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2024 KX250 owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 1 click out", "A touch plusher on hardpack chatter."),
    ("Fork rebound, 1 click in", "A slower return keeps the front calm off jump faces."),
    ("Shock low-speed, 2 clicks in", "More hold for a 185 lb rider on the stock spring."),
    ("High-speed, rebound, springs stay put", "Not every click has to move."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2024 KAWASAKI KX250",
  "sheet_sub": "about 185 lb  ·  fast  ·  hardpack moto  ·  48 mm coil fork",
  "tiles": [("FORK COMP", "12", "stock 11", "1 click out"),
            ("FORK REBOUND", "11", "stock 12", "1 click in"),
            ("SHOCK LOW-SPEED", "10", "stock 12", "2 clicks in"),
            ("SHOCK HIGH-SPEED", "1 1/2", "turns  ·  stock 1 1/2", None),
            ("SHOCK REBOUND", "13", "stock 13", None),
            ("SPRINGS", "4.9 / 54", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "103 mm",
  "sag_note": "Dialed starting point  ·  measure yours first",
 }),
 # ------------------------------------------------------------------ Tue Nov 3
 dict(BASE, **{
  "slug": "2026-11-03-500excf-split",
  "title": "Settings card: 2025 KTM 500 EXC-F",
  "design": "split", "kind": "image", "scheduled_at": _at(3, 12),
  "caption": "2025 KTM 500 EXC-F. About 205 lb, fast, rocks and roots, stability and grip the goals. Left is stock "
             "from the 2025 KTM owner's manual for the 450 and 500 EXC-F, right is the baseline Dialed built for that "
             "rider.\n\n"
             "Fork comp 15 to 12, fork rebound 17 to 12. Shock low-speed 15 to 10, high-speed 2 turns to 1 1/2, "
             "rebound 15 to 12. Sag stays at the manual's 110 mm. A heavier, faster rider gets more support and "
             "slower rebound on both ends to keep the big four-stroke settled over the rocks.\n\n"
             "All clicks counted out from fully closed. Starting points riders refine on the bike, one change at a "
             "time.\n\n"
             "Which trail section tells you first that your setup is off?",
  "hashtags": "#ktm #500excf #enduro #suspension #dialedoffroad",
  "story": "Question box: \"Name the trail section that beats up your bike.\" Share the best answers back.",
  "slides": [{"type": "hot", "head": "2025 KTM 500 EXC-F. ROCKS AND ROOTS, ABOUT 205 LB.", "sub": ""}],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 15", "Fork reb 17", "Shock low 15", "High-speed 2", "Shock reb 15", "Sag 110 mm"],
            "right": "DIALED",
            "right_lines": ["Fork comp 12", "Fork reb 12", "Shock low 10", "High-speed 1 1/2", "Shock reb 12", "Sag 110 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-03-terrain-cheat-sheet",
  "title": "Carousel: terrain to clicker cheat sheet",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(3, 18),
  "caption": "Same bike, different dirt, different starting point. Six kinds of ground and where to begin on each.\n\n"
             "Not laws, starting points. One change at a time, two clicks max, counted out from fully closed, and "
             "write down what you did and how it felt.\n\n"
             "Save it for your next trip somewhere new. Which ground gives your bike the most trouble?",
  "hashtags": "#dirtbikes #enduro #motocross #suspensionsetup #dialedoffroad",
  "story": "Poll on the cover: \"What do you ride most?\" Hardpack / Sand / Rocks and roots / Mud.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "THE DIRT CHANGED. WHERE TO START.",
    "sub": "Save this for the next new track.", "footer": "In = more damping. Out = less. One change at a time."},
   {"type": "symptom", "head": "HARDPACK AND CHATTER",
    "fix": "Fork compression: 1 to 2 clicks out.",
    "why": "Hard ground rarely pushes the fork deep. A softer start takes the sting out of the small stuff."},
   {"type": "symptom", "head": "SAND AND WHOOPS",
    "fix": "Shock low-speed and fork compression: 1 to 2 clicks in.",
    "why": "Sand loads the bike all lap. More support keeps the rear from squatting and the front from diving."},
   {"type": "symptom", "head": "ROCKS AND ROOTS",
    "fix": "Compression on both ends: 1 to 2 clicks out.",
    "why": "Grip comes from the wheel following the ground. Let it move, then check rebound is not kicking."},
   {"type": "symptom", "head": "DEEP RUTS",
    "fix": "Shock low-speed: 1 click out.",
    "why": "A rear that settles into the rut tracks better than one that skates over the top of it."},
   {"type": "symptom", "head": "MUD",
    "fix": "Leave the clickers. Clean the bike between motos.",
    "why": "Packed mud adds real weight and changes how the bike sits. Fix the weight before the damping."},
   {"type": "symptom", "head": "COLD MORNING",
    "fix": "Ride a lap or two before you change anything.",
    "why": "Cold oil feels stiffer. Judge the setting once the fork and shock are warm."},
   {"type": "closer", "head": "THE GROUND DECIDES. YOU ADJUST ONE CLICK AT A TIME.",
    "sub": "Dialed builds the starting point for your bike, weight and terrain, then logs every click you change.",
    "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Wed Nov 4
 dict(BASE, **{
  "slug": "2026-11-04-yz250f-setup-sheet",
  "title": "Settings card: 2025 Yamaha YZ250F",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(4, 12),
  "caption": "2025 Yamaha YZ250F. About 175 lb, fast, loamy moto, stability and jump support the goals. This is the "
             "baseline Dialed built, next to the stock settings from the 2025 YZ250F owner's service manual.\n\n"
             "Stock is 13 and 12 on the fork, 12 clicks and 1 1/2 turns on the shock, 12 on shock rebound, sag 90 to "
             "100 mm. Dialed went one click in on fork comp, two in on low-speed, half a turn in on high-speed, and set "
             "sag at 100 mm. Rebound stays stock on both ends. All counted out from fully closed.\n\n"
             "Starting points riders refine on the bike, one change at a time, two clicks max.\n\n"
             "Loam or hardpack: which one makes your YZ250F feel worse?",
  "hashtags": "#yz250f #yamaha #motocross #suspension #dialedoffroad",
  "story": "Quiz sticker: \"Yamaha's sag window on the 2025 YZ250F?\" 80 to 90 / 90 to 100 / 100 to 110.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2025 YAMAHA YZ250F",
    "sub": "about 175 lb  ·  fast  ·  loamy moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2025 Yamaha YZ250F  ·  about 175 lb  ·  fast  ·  loamy moto",
    "rows": [("Fork compression", "13", "12"), ("Fork rebound", "12", "12"), ("Shock low-speed comp", "12", "10"),
             ("Shock high-speed comp", "1 1/2 turns", "1 turn"), ("Shock rebound", "12", "12"),
             ("Riding sag", "90 to 100 mm", "100 mm"), ("Springs, fork / shock", "4.7 / 54 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2025 YZ250F owner's service manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 1 click in", "A bit more hold on soft jump faces."),
    ("Shock low-speed, 2 clicks in", "Keeps the rear up when the loam lets it squat."),
    ("High-speed, 1/2 turn in", "More support on the big landings."),
    ("Sag at 100 mm, set first", "The top of Yamaha's 90 to 100 window."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2025 YAMAHA YZ250F",
  "sheet_sub": "about 175 lb  ·  fast  ·  loamy moto  ·  KYB coil fork",
  "tiles": [("FORK COMP", "12", "stock 13", "1 click in"),
            ("FORK REBOUND", "12", "stock 12", None),
            ("SHOCK LOW-SPEED", "10", "stock 12", "2 clicks in"),
            ("SHOCK HIGH-SPEED", "1", "turn  ·  stock 1 1/2", "1/2 turn in"),
            ("SHOCK REBOUND", "12", "stock 12", None),
            ("SPRINGS", "4.7 / 54", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "100 mm",
  "sag_note": "manual says 90 to 100 mm  ·  2025 owner's service manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-04-location-answer",
  "title": "Comment answer: why the app asks where you ride",
  "design": "glow", "kind": "image", "scheduled_at": _at(4, 18),
  "caption": "Someone asked in the comments why the app wants to know their location. Fair question.\n\n"
             "It's optional, and your clicker settings don't use it. It fills in your state and riding region and "
             "suggests which track you're at when you log a ride day. Skip it and your starting point comes out the "
             "same: built from your bike, weight, skill and terrain, then refined on the bike one change at a time.\n\n"
             "What else do you want to know about how the numbers get built?",
  "hashtags": "#dirtbikes #motocross #suspension #dialedoffroad",
  "story": "Question box: \"Ask me anything about how Dialed builds a setup.\" Answer the best ones on stories.",
  "slides": [{"type": "hot", "head": "WHY THE APP ASKS WHERE YOU RIDE.",
              "sub": "It's optional, and your clicker settings don't use it. It fills in your riding region and "
                     "suggests the track when you log a ride day. Skip it and your numbers come out the same."}],
 }),
 # ------------------------------------------------------------------ Thu Nov 5
 dict(BASE, **{
  "slug": "2026-11-05-150xcw-split",
  "title": "Settings card: 2026 KTM 150 XC-W",
  "design": "split", "kind": "image", "scheduled_at": _at(5, 12),
  "caption": "2026 KTM 150 XC-W. About 135 lb, intermediate, mixed woods with sand, roots, rocks, mud and a few "
             "jumps. Left is stock from the 2026 KTM 150 XC-W owner's manual, right is the baseline Dialed built for "
             "that rider.\n\n"
             "Fork comp 15 to 12, fork rebound 17 to 12. Shock low-speed 15 to 10, high-speed 2 turns to 1, rebound "
             "15 to 12. Sag 105 mm against the manual's 110.\n\n"
             "All clicks counted out from fully closed. Starting points riders refine on the bike: ride it, log how it "
             "felt, move one thing at a time.\n\n"
             "Light riders on small two-strokes: what's the first thing you changed?",
  "hashtags": "#ktm #150xcw #twostroke #enduro #dialedoffroad",
  "story": "Poll: \"Best woods bike under 200cc?\" 150 XC-W / 125 / Something else.",
  "slides": [{"type": "hot", "head": "2026 KTM 150 XC-W. MIXED WOODS, ABOUT 135 LB.", "sub": ""}],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 15", "Fork reb 17", "Shock low 15", "High-speed 2", "Shock reb 15", "Sag 110 mm"],
            "right": "DIALED",
            "right_lines": ["Fork comp 12", "Fork reb 12", "Shock low 10", "High-speed 1", "Shock reb 12", "Sag 105 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-05-test-day-rules",
  "title": "Carousel: how to run a test day",
  "design": "blue_list", "kind": "carousel", "scheduled_at": _at(5, 18),
  "caption": "Most riders change a clicker, ride a different line, and decide it feels better. That's not a test, "
             "that's a mood.\n\n"
             "Five rules for a test day that tells you something: one section, one change, two clicks, two laps, and "
             "go back when it gets worse. Counted out from fully closed, written down every time.\n\n"
             "Which rule do you break the most?",
  "hashtags": "#dirtbikes #motocross #enduro #suspensiontuning #dialedoffroad",
  "story": "Share slide 03 to your story: \"Two clicks, then two laps.\"",
  "slides": [
   {"type": "cover", "eyebrow": "TEST DAY", "head": "HOW TO TEST A CLICKER CHANGE AND LEARN SOMETHING",
    "footer": "Swipe"},
   {"type": "point", "num": "01", "head": "PICK ONE SECTION AND STICK TO IT.",
    "body": "Same braking bumps, same jump, same corner, every lap. If the ground changes, you can't tell what the "
            "click did."},
   {"type": "point", "num": "02", "head": "ONE CHANGE AT A TIME.",
    "body": "Move two clickers and you will never know which one helped. Change one, then ride."},
   {"type": "point", "num": "03", "head": "TWO CLICKS, THEN TWO LAPS.",
    "body": "Small steps are easier to feel. One lap to forget the old setting, one lap to judge the new one."},
   {"type": "point", "num": "04", "head": "IF IT GOT WORSE, GO BACK.",
    "body": "Going back to the last good setting is a result too. Now you know which way that clicker goes on your "
            "bike."},
   {"type": "point", "num": "05", "head": "TEST WHILE YOU CAN STILL FEEL IT.",
    "body": "Tired arms make every setting feel harsh. Do your testing early, before the third moto."},
   {"type": "closer", "head": "DIALED LOGS EVERY CLICK.",
    "sub": "Start from a baseline for your bike and weight, then refine it on ride days, one change at a time.",
    "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Fri Nov 6
 dict(BASE, **{
  "slug": "2026-11-06-kx450-setup-sheet",
  "title": "Settings card: 2023 Kawasaki KX450",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(6, 12),
  "caption": "2023 Kawasaki KX450. About 200 lb, intermediate, hardpack, sand and dunes, stability and comfort at "
             "speed the goals. This is the baseline Dialed built, next to the stock settings from the 2023 KX450 "
             "owner's manual.\n\n"
             "Stock is 14 and 12 on the fork, 18 on shock low-speed, 12 on shock rebound. Dialed went two clicks in "
             "on fork comp, two out on fork rebound, eight in on low-speed and set sag at 105 mm. Eight clicks is a "
             "big move, so if it feels harsh, come back toward stock two at a time.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Dunes or hardpack: where does your KX450 feel worst?",
  "hashtags": "#kx450 #kawasaki #dunes #suspension #dialedoffroad",
  "story": "Poll: \"Ever ridden the dunes on stock clickers?\" Yes / No / Never again.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2023 KAWASAKI KX450",
    "sub": "about 200 lb  ·  intermediate  ·  sand and hardpack", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED",
    "sub": "2023 Kawasaki KX450  ·  about 200 lb  ·  intermediate  ·  sand and hardpack",
    "rows": [("Fork compression", "14", "12"), ("Fork rebound", "12", "14"), ("Shock low-speed comp", "18", "10"),
             ("Shock high-speed comp", "see manual", "1 turn"), ("Shock rebound", "12", "12"),
             ("Riding sag", "see manual", "105 mm"), ("Springs, fork / shock", "5.0 / 54 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2023 KX450 owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Shock low-speed, 8 clicks in", "The big one: holds a 200 lb rider up in sand."),
    ("Fork comp, 2 clicks in", "Less dive when the sand grabs the front."),
    ("Fork rebound, 2 clicks out", "Recovers quicker between whoops."),
    ("Shock rebound and springs stay put", "Not every click has to move."),
   ]},
   {"type": "closer", "head": "A STARTING POINT. YOU FINISH IT ON THE BIKE.",
    "sub": "Ride it, log how it felt, change one thing at a time.", "cta": CTA, "footer": FOOT},
  ],
  "sheet_title": "2023 KAWASAKI KX450",
  "sheet_sub": "about 200 lb  ·  intermediate  ·  sand, dunes, hardpack",
  "tiles": [("FORK COMP", "12", "stock 14", "2 clicks in"),
            ("FORK REBOUND", "14", "stock 12", "2 clicks out"),
            ("SHOCK LOW-SPEED", "10", "stock 18", "8 clicks in"),
            ("SHOCK HIGH-SPEED", "1", "turn  ·  stock: see manual", None),
            ("SHOCK REBOUND", "12", "stock 12", None),
            ("SPRINGS", "5.0 / 54", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "105 mm",
  "sag_note": "Dialed starting point  ·  measure yours first",
 }),
 dict(BASE, **{
  "slug": "2026-11-06-counting-clicks",
  "title": "Carousel: how to count clicks",
  "design": "dials", "kind": "carousel", "scheduled_at": _at(6, 18),
  "caption": "\"Run 12 on the fork\" means nothing until you know where zero is. Here's how to find it, count from "
             "it, and not wreck a clicker doing it.\n\n"
             "Every number on a Dialed card is counted out from fully closed, and so are most manuals. Check yours.\n\n"
             "Save it, send it to the friend who counts from the wrong end. Do you count from closed or open?",
  "hashtags": "#dirtbikes #motocross #suspension101 #clickers #dialedoffroad",
  "story": "Quiz sticker: \"12 clicks out from fully closed is...\" Softer than 10 / Firmer than 10.",
  "dials": ["FORK\nCOMP", "FORK\nREB", "SHOCK\nLSC", "SHOCK\nHSC", "SHOCK\nREB"],
  "slides": [
   {"type": "cover", "eyebrow": "SUSPENSION 101", "head": "HOW TO COUNT CLICKS WITHOUT GUESSING", "footer": "Swipe"},
   {"type": "point", "tag": "STEP 1  ·  FIND ZERO", "head": "TURN IN GENTLY UNTIL IT STOPS.",
    "body": "Light fingers, no wrench muscle. Forcing it past the stop can damage the adjuster. That soft stop is "
            "zero."},
   {"type": "point", "tag": "STEP 2  ·  COUNT OUT", "head": "COUNT EVERY CLICK BACK OUT.",
    "body": "12 out on your bike means 12 clicks out from that stop. Higher number, less damping."},
   {"type": "point", "tag": "HIGH-SPEED  ·  TURNS", "head": "HIGH-SPEED IS OFTEN SET IN TURNS.",
    "body": "Many shocks set high-speed comp in turns out, not clicks. A quarter turn is a real change, so move it in "
            "quarters."},
   {"type": "point", "tag": "CHECK  ·  YOUR MANUAL", "head": "NOT EVERY MANUAL COUNTS FROM CLOSED.",
    "body": "Beta's 2024 RR two-stroke sheet counts shock high-speed from fully open. Read the line before you copy a "
            "number."},
   {"type": "point", "tag": "LAST  ·  WRITE IT DOWN", "head": "LOG THE NUMBER BEFORE YOU RIDE.",
    "body": "Clicker, number, track, how it felt. The next ride starts from a fact instead of a memory."},
   {"type": "closer", "head": "EVERY NUMBER IN DIALED IS COUNTED FROM FULLY CLOSED.",
    "sub": "So the starting point on your phone matches the clicker in your hand.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Sat Nov 7
 dict(BASE, **{
  "slug": "2026-11-07-yz250x-split",
  "title": "Settings card: 2026 Yamaha YZ250X",
  "design": "split", "kind": "image", "scheduled_at": _at(7, 12),
  "caption": "2026 Yamaha YZ250X. About 200 lb, intermediate, tight woods with rocks, sand, roots and some whoops, "
             "corner control and flow the goals. Left is stock from the 2026 YZ250X owner's service manual, right is "
             "the baseline Dialed built for that rider.\n\n"
             "Fork comp 10 to 9, fork rebound 9 to 12. Shock low-speed stays at 8, high-speed 1 turn to 1 1/4, "
             "rebound 9 to 12. Sag 103 mm, a little past Yamaha's 90 to 100 window. If it wallows, come back toward "
             "100.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "What's your YZ250X running for the tight stuff?",
  "hashtags": "#yz250x #yamaha #woodsriding #twostroke #dialedoffroad",
  "story": "Poll: \"Tight woods: two-stroke or four-stroke?\" Two / Four.",
  "slides": [{"type": "hot", "head": "2026 YAMAHA YZ250X. TIGHT WOODS, ABOUT 200 LB.", "sub": ""}],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 10", "Fork reb 9", "Shock low 8", "High-speed 1", "Shock reb 9", "Sag 90 to 100"],
            "right": "DIALED",
            "right_lines": ["Fork comp 9", "Fork reb 12", "Shock low 8", "High-speed 1 1/4", "Shock reb 12", "Sag 103 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-07-tire-pressure",
  "title": "Hot take: tire pressure is suspension",
  "design": "glow", "kind": "image", "scheduled_at": _at(7, 18),
  "caption": "Before you chase a harsh front end with clickers, check the gauge. The tire is the first spring the "
             "bump hits, and a couple of psi changes how the bike feels over rocks, roots and chatter.\n\n"
             "Set pressure, set sag, then start on the clickers, one change at a time, counted out from fully "
             "closed.\n\n"
             "What pressure are you running front and rear?",
  "hashtags": "#dirtbikes #enduro #motocross #tirepressure #dialedoffroad",
  "story": "Question box: \"Front and rear psi, and where you ride.\" Share a few answers back.",
  "slides": [{"type": "hot", "head": "TIRE PRESSURE IS PART OF YOUR SUSPENSION.",
              "sub": "The tire is the first spring every bump hits. Check the gauge before you touch a clicker, "
                     "then change one thing at a time."}],
 }),
]
