# Week of 2026-11-22 (posts Mon Nov 23 to Sat Nov 28). Bike card carousel at 12:40 pm Boise every day (sheet / split
# alternating, sheet Monday), tip at 6:40 pm. Animated explainer reels Mon, Wed, Fri at 3:40 pm come from tools/anim
# (out/anim/2026-11-22). Nothing was queued in social_posts for these slots.
# Bike cards: stock from bike_model_specs on prod (oem_manual), Dialed from a real setup_versions baseline.
#   Mon 2024 Yamaha YZ250       2024 Owner's Service Manual YZ250, part BCR-2819U-12 (us, standard)
#   Tue 2026 Kawasaki KX250     Owner's Manual 2026 KX252E/F, part 99814-0119 (us); no sag figure in the catalog
#   Wed 2020 KTM 300 XC         Owner's Manual 2020 250 XC TPI, 300 XC TPI, US edition (us, standard)
#   Thu 2025 Yamaha YZ450F      2025 Owner's Service Manual YZ450F, part D02-2819U-10 (us, standard)
#   Fri 2024 KTM 250 SX         Owner's Manual 2024 250 SX, 300 SX, 250 XC, 300 XC, part 3214833en (all, standard)
#   Sat 2022 Yamaha YZ250F      2022 Owner's Service Manual YZ250F, part B7B-2819U-13 (us, standard)
# Skipped: 2024 Beta RR 2T 300 (open bike request) still has no setup_versions row; 2023 Honda CRF250R, 2024 and 2025
# CRF450R, 2021 KX250 (top tuned) have no stock clicker rows; 2017 KTM 250 SX and 2014 YZ250F are older than 2019.
# Tips: no app-screens post this week (the last two got 0 saves and the lowest reach of the fortnight).
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
 # ------------------------------------------------------------------ Mon Nov 23
 dict(BASE, **{
  "slug": "2026-11-23-yz250-setup-sheet",
  "title": "Settings card: 2024 Yamaha YZ250",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(23, 12),
  "caption": "2024 Yamaha YZ250. About 170 lb, comfortable pace, hardpack moto, stock suspension, stability and comfort "
             "the goals. This is the baseline Dialed built, next to the standard settings from the 2024 YZ250 owner's "
             "service manual.\n\n"
             "Stock is 9 and 14 on the fork, 9 clicks and 1 1/8 turns on the shock, 8 on shock rebound, and Yamaha's "
             "90 to 100 mm sag window. Dialed moved one thing: shock high-speed a quarter turn out, to 1 3/8. Sag at "
             "100. For this rider on hardpack, stock is already close, so the first move is a small one.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "YZ250 riders: what was the first clicker you moved?",
  "hashtags": "#yz250 #yamaha #twostroke #motocross #dialedoffroad",
  "story": "Quiz sticker on the tiles: \"Stock shock high-speed on a 2024 YZ250?\" 1 / 1 1/8 / 1 1/2 turns.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2024 YAMAHA YZ250",
    "sub": "about 170 lb  ·  comfortable pace  ·  hardpack moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2024 Yamaha YZ250  ·  about 170 lb  ·  hardpack moto",
    "rows": [("Fork compression", "9", "9"), ("Fork rebound", "14", "14"), ("Shock low-speed comp", "9", "9"),
             ("Shock high-speed comp", "1 1/8 turns", "1 3/8 turns"), ("Shock rebound", "8", "8"),
             ("Riding sag", "90 to 100 mm", "100 mm"), ("Springs, fork / shock", "4.4 / 50 N/mm", "stock")],
    "note": "Clicks counted out from fully closed. Stock figures from the 2024 YZ250 owner's service manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Shock high-speed, 1/4 turn out", "A little more give on hardpack edges."),
    ("Four clickers stay stock", "Stock is already close for this rider."),
    ("Sag at 100 mm", "The top of Yamaha's 90 to 100 window."),
    ("Ride it before you turn more", "Then change one thing at a time."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2024 YAMAHA YZ250",
  "sheet_sub": "about 170 lb  ·  comfortable pace  ·  hardpack moto",
  "tiles": [("FORK COMP", "9", "stock 9", None),
            ("FORK REBOUND", "14", "stock 14", None),
            ("SHOCK LOW-SPEED", "9", "stock 9", None),
            ("SHOCK HIGH-SPEED", "1 3/8", "turns  ·  stock 1 1/8", "1/4 turn out"),
            ("SHOCK REBOUND", "8", "stock 8", None),
            ("SPRINGS", "4.4 / 50", "N/mm fork / shock  ·  stock", None)],
  "sag_value": "100 mm",
  "sag_note": "manual says 90 to 100 mm  ·  2024 YZ250 manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-23-trailer-kit",
  "title": "Carousel: the trailer kit cheat sheet",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(23, 18),
  "paper_footer": "Pack it once. Leave it in the trailer.",
  "caption": "You can't tune at the track without the right few things in the trailer. Here's the kit, and what each "
             "piece is for.\n\n"
             "Check sag and pressure first, then work the clickers one change at a time, counted out from fully "
             "closed.\n\n"
             "Save it for packing day. What's the one tool you always forget?",
  "hashtags": "#trackday #suspensionsetup #motocross #enduro #dialedoffroad",
  "story": "Poll on the cover: \"Do you tune at the track?\" Every ride / Sometimes / Never.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "THE TRAILER KIT. TUNE AT THE TRACK.",
    "sub": "Save this for packing day.", "footer": "Six things. Every ride."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "A SAG TAPE OR RULER",
    "fix": "Riding sag, every new day",
    "why": "Check sag before you touch a clicker. Two people and a tape take two minutes."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "A FLAT BLADE SCREWDRIVER",
    "fix": "Most fork and shock clickers",
    "why": "Many clickers take a flat blade, some turn by hand. Count from fully closed before you change one."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "A WRENCH FOR HIGH-SPEED",
    "fix": "The shock's high-speed nut",
    "why": "On many shocks high-speed is a bigger nut, set in turns. Check the size in your manual."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "A TIRE GAUGE",
    "fix": "Pressure, cold, every ride",
    "why": "A couple of psi changes how the bike feels over bumps. Check it at the track, not the garage."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "AN AIR FORK PUMP",
    "fix": "Air forks only",
    "why": "Set pressure from the manual's chart for your weight, cold, before the first moto."},
   {"type": "symptom", "label": "PACK", "label2": "FOR", "head": "A NOTEBOOK OR YOUR PHONE",
    "fix": "One line per change",
    "why": "Which clicker, how many, which way, and how it felt. Or the next ride starts from a guess."},
   {"type": "closer", "head": "PACK IT. THEN CHANGE ONE THING.",
    "sub": "Dialed keeps the log for you: every click and how it felt, saved with the setup.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Tue Nov 24
 dict(BASE, **{
  "slug": "2026-11-24-kx250-split",
  "title": "Settings card: 2026 Kawasaki KX250",
  "design": "split", "kind": "carousel", "scheduled_at": _at(24, 12),
  "caption": "2026 Kawasaki KX250. About 135 lb, fast, supercross style track, stock suspension, stability and jump "
             "support the goals. Left is stock from the 2026 KX250 owner's manual, right is the baseline Dialed built "
             "for that rider.\n\n"
             "Fork comp 8 to 7, fork rebound 7 to 8. Shock low-speed stays at 11, high-speed stays at 2 1/2 turns, "
             "rebound 10 to 11. Sag set at 103 mm; check your manual for Kawasaki's figure. Small moves: one click in "
             "on fork comp for jump faces, and a quicker return front and rear for a light rider.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Lighter riders on a KX250: how close to stock do you run?",
  "hashtags": "#kx250 #kawasaki #supercross #motocross #dialedoffroad",
  "story": "Poll on the split: \"Light rider, stock clickers?\" Run stock / Changed a few / Changed them all.",
  "slides": [
   {"type": "hot", "head": "2026 KAWASAKI KX250. SUPERCROSS, ABOUT 135 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 1 click in", "A bit more hold on jump faces."),
    ("Fork rebound, 1 click out", "A quicker return for a light rider."),
    ("Shock rebound, 1 click out", "The rear comes back in time."),
    ("Low-speed and high-speed stay stock", "Not every click has to move."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 8", "Fork reb 7", "Shock low 11", "High-speed 2 1/2", "Shock reb 10", "Sag: see manual"],
            "right": "DIALED",
            "right_lines": ["Fork comp 7", "Fork reb 8", "Shock low 11", "High-speed 2 1/2", "Shock reb 11", "Sag 103 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-24-rebound-explained",
  "title": "Carousel: rebound, the clicker riders forget",
  "design": "dials", "kind": "carousel", "scheduled_at": _at(24, 18),
  "caption": "Riders spend weeks on compression and never touch rebound. Rebound doesn't change how hard the fork or "
             "shock hits. It changes how fast it comes back after.\n\n"
             "Too fast and the bike feels light and kicks. Too slow and it packs down. One click at a time, counted "
             "out from fully closed.\n\n"
             "When did you last move a rebound clicker?",
  "hashtags": "#rebound #clickers #suspensiontuning #motocross #dialedoffroad",
  "story": "Quiz sticker on slide 02: \"Rebound 1 click in makes the fork come back...\" Slower / Quicker.",
  "dials": ["FORK\nCOMP", "FORK\nREB", "SHOCK\nLSC", "SHOCK\nHSC", "SHOCK\nREB"],
  "slides": [
   {"type": "cover", "eyebrow": "SUSPENSION 101", "head": "REBOUND. THE CLICKER RIDERS FORGET.", "footer": "Swipe"},
   {"type": "point", "tag": "FORK  ·  REBOUND", "head": "IT SETS HOW FAST THE FORK COMES BACK.",
    "body": "Not how hard it hits. How fast it returns after the hit. In is slower, out is quicker."},
   {"type": "point", "tag": "SHOCK  ·  REBOUND", "head": "SAME JOB OUT BACK.",
    "body": "Usually the clicker at the bottom of the shock. In is slower, out is quicker, counted out from fully "
            "closed."},
   {"type": "point", "tag": "REBOUND  ·  TOO FAST", "head": "THE BIKE FEELS LIGHT AND KICKS.",
    "body": "The front deflects and the rear kicks off braking bumps and jump faces. Try 1 click in."},
   {"type": "point", "tag": "REBOUND  ·  TOO SLOW", "head": "IT PACKS DOWN AND GETS HARSH.",
    "body": "It can't come back between bumps, so each hit starts lower in the stroke. Try 1 click out."},
   {"type": "closer", "head": "ONE REBOUND CLICK. THEN RIDE.",
    "sub": "Tell Dialed what the bike did and it tells you which rebound clicker and which way.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Wed Nov 25
 dict(BASE, **{
  "slug": "2026-11-25-300xc-setup-sheet",
  "title": "Settings card: 2020 KTM 300 XC",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(25, 12),
  "caption": "2020 KTM 300 XC. About 175 lb, intermediate, roots and hardpack, short motos, stability and comfort the "
             "goals. This is the baseline Dialed built, next to the standard settings from KTM's 2020 owner's manual "
             "for the 250 and 300 XC TPI (US edition).\n\n"
             "Stock is 12 and 12 on the fork, 15 clicks and 2 turns on the shock, 15 on shock rebound, 105 mm of riding "
             "sag. Dialed went 2 clicks out on fork comp, 3 in on low-speed, a full turn in on high-speed and 1 in on "
             "shock rebound. Fork rebound and sag stay stock. A softer front for the roots, more hold out back for the "
             "ledges and hardpack hits.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "300 XC riders: is your shock high-speed still at 2 turns?",
  "hashtags": "#ktm #300xc #twostroke #enduro #dialedoffroad",
  "story": "Poll on the tiles: \"Roots or rocks?\" Roots / Rocks / Both, every ride.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2020 KTM 300 XC",
    "sub": "about 175 lb  ·  intermediate  ·  roots and hardpack", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2020 KTM 300 XC  ·  about 175 lb  ·  roots and hardpack",
    "rows": [("Fork compression", "12", "14"), ("Fork rebound", "12", "12"), ("Shock low-speed comp", "15", "12"),
             ("Shock high-speed comp", "2 turns", "1 turn"), ("Shock rebound", "15", "14"),
             ("Riding sag", "105 mm", "105 mm"), ("Shock spring, 165 to 187 lb", "42 N/mm", "manual's row")],
    "note": "Clicks counted out from fully closed. Stock figures from KTM's 2020 250/300 XC TPI owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork comp, 2 clicks out", "A softer front over roots."),
    ("Shock high-speed, 1 turn in", "More hold on ledges and hard hits."),
    ("Low-speed 3 in, rebound 1 in", "A calmer rear on the gas."),
    ("Fork rebound and sag stay stock", "Sag first, 105 mm."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2020 KTM 300 XC",
  "sheet_sub": "about 175 lb  ·  intermediate  ·  roots and hardpack",
  "tiles": [("FORK COMP", "14", "stock 12", "2 clicks out"),
            ("FORK REBOUND", "12", "stock 12", None),
            ("SHOCK LOW-SPEED", "12", "stock 15", "3 clicks in"),
            ("SHOCK HIGH-SPEED", "1", "turn  ·  stock 2", "1 turn in"),
            ("SHOCK REBOUND", "14", "stock 15", "1 click in"),
            ("SHOCK SPRING", "42", "N/mm  ·  manual, 165 to 187 lb", None)],
  "sag_value": "105 mm",
  "sag_note": "manual says 105 mm  ·  2020 KTM 300 XC TPI manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-25-track-changes",
  "title": "Carousel: the track changes, morning to afternoon",
  "design": "classic", "kind": "carousel", "scheduled_at": _at(25, 18),
  "caption": "The setup that felt great in the first moto can feel wrong by the last. The bike didn't change. The "
             "track did. Here's what usually shows up as the day goes on, and where to start.\n\n"
             "One change per session, counted out from fully closed, so you know what each click did.\n\n"
             "Save it for race day. Does your bike feel worse in the afternoon motos?",
  "hashtags": "#raceday #motocross #suspensionsetup #brakingbumps #dialedoffroad",
  "story": "Poll: \"Do you change clickers between motos?\" Every moto / Sometimes / Never.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "THE TRACK CHANGES. SO DOES THE BIKE.",
    "sub": "Morning to afternoon, where to start.", "footer": "Swipe"},
   {"type": "symptom", "head": "FRONT GETS HARSHER AS BUMPS BUILD",
    "fix": "Fork rebound: 1 click out",
    "why": "Afternoon braking bumps come closer together. If the fork can't come back between them, it packs down."},
   {"type": "symptom", "head": "FRONT WON'T SETTLE INTO DEEP RUTS",
    "fix": "Fork compression: 1 click out",
    "why": "A fork that rides high in the stroke won't sit into a rut. Small moves, then another lap."},
   {"type": "symptom", "head": "REAR STARTS KICKING ON EDGES",
    "fix": "Shock rebound: 1 click in",
    "why": "Square edges grow through the day. A slower return stops the rear bucking off them."},
   {"type": "symptom", "head": "IT DRIED OUT AND LOST GRIP",
    "fix": "Check tire pressure first",
    "why": "Hard, dry dirt changes grip before any clicker does. Check pressure, then ride it before you click."},
   {"type": "closer", "head": "ONE CHANGE PER SESSION.",
    "sub": "Dialed saves a setup per track and logs every change, so next time you start closer.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Thu Nov 26
 dict(BASE, **{
  "slug": "2026-11-26-yz450f-split",
  "title": "Settings card: 2025 Yamaha YZ450F",
  "design": "split", "kind": "carousel", "scheduled_at": _at(26, 12),
  "caption": "2025 Yamaha YZ450F. About 185 lb, fast, hardpack moto, stock suspension, stability and jump support the "
             "goals. Left is stock from the 2025 YZ450F owner's service manual, right is the baseline Dialed built for "
             "that rider.\n\n"
             "Fork comp stays at 12, fork rebound 10 to 11. Shock low-speed 9 to 10, high-speed 1 turn to 1 3/8, "
             "rebound 12 to 13. Sag 97 mm, inside Yamaha's 90 to 100 window. Small moves out across the board: a touch "
             "more give on hardpack without giving up the jump support.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "YZ450F riders: where's your sag sitting in that 90 to 100 window?",
  "hashtags": "#yz450f #yamaha #motocross #hardpack #dialedoffroad",
  "story": "Quiz sticker on the split: \"Yamaha's sag window on the 2025 YZ450F?\" 90 to 100 / 100 to 110 / 105.",
  "slides": [
   {"type": "hot", "head": "2025 YAMAHA YZ450F. ABOUT 185 LB, HARDPACK.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("High-speed, 3/8 turn out", "More give on hardpack hits."),
    ("Fork and shock rebound, 1 out", "A quicker return on the hard stuff."),
    ("Shock low-speed, 1 click out", "A bit more grip on the gas."),
    ("Fork comp stays 12, sag 97 mm", "Inside Yamaha's 90 to 100 window."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 12", "Fork reb 10", "Shock low 9", "High-speed 1", "Shock reb 12", "Sag 90 to 100"],
            "right": "DIALED",
            "right_lines": ["Fork comp 12", "Fork reb 11", "Shock low 10", "High-speed 1 3/8", "Shock reb 13", "Sag 97 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-26-landing-cheat-sheet",
  "title": "Carousel: the jump landing cheat sheet",
  "design": "paper_list", "kind": "carousel", "scheduled_at": _at(26, 18),
  "paper_footer": "Sag and springs first. Then one clicker at a time.",
  "caption": "Landings tell you a lot about your setup. Bottoming, harshness and a rear that kicks after the landing "
             "each point to a different place to start.\n\n"
             "Check sag and springs first, then one change at a time, counted out from fully closed.\n\n"
             "Save it for the next jump day. What does your bike do on a big landing?",
  "hashtags": "#jumps #motocross #shocksetup #forksetup #dialedoffroad",
  "story": "Poll on slide 02: \"Your bike on big landings?\" Bottoms / Harsh / Kicks / Feels great.",
  "slides": [
   {"type": "cover", "eyebrow": "CHEAT SHEET", "head": "WHAT YOUR LANDINGS ARE TELLING YOU.",
    "sub": "Save this for jump day.", "footer": "Five landings. Five places to start."},
   {"type": "symptom", "head": "REAR BOTTOMS HARD",
    "fix": "Shock high-speed: 1/4 turn in",
    "why": "If it bottoms on every landing, check sag and the spring before you keep turning."},
   {"type": "symptom", "head": "FRONT BOTTOMS ON LANDINGS",
    "fix": "Fork comp: 1 to 2 clicks in",
    "why": "Air fork? Check pressure against the manual first. Coil fork? The spring may be soft for you."},
   {"type": "symptom", "head": "HARSH BUT NEVER BOTTOMS",
    "fix": "Shock high-speed: 1/4 turn out",
    "why": "You're not using the travel. Give some back and let it soak up the hit."},
   {"type": "symptom", "head": "REAR KICKS AFTER THE LANDING",
    "fix": "Shock rebound: 1 click in",
    "why": "The shock comes back too quick and throws the rear up. A slower return settles it."},
   {"type": "symptom", "head": "SITS LOWER JUMP AFTER JUMP",
    "fix": "Rebound: 1 click out",
    "why": "It's not coming back up between landings. A quicker return lets it recover for the next one."},
   {"type": "closer", "head": "ONE LANDING. ONE CHANGE.",
    "sub": "Tell Dialed what the bike did on the landing and it gives you one change to try.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Fri Nov 27
 dict(BASE, **{
  "slug": "2026-11-27-250sx-setup-sheet",
  "title": "Settings card: 2024 KTM 250 SX",
  "design": "sheet", "kind": "carousel", "scheduled_at": _at(27, 12),
  "caption": "2024 KTM 250 SX. About 165 lb, pro pace, sand moto, stability and jump support the goals. This is the "
             "baseline Dialed built, next to the standard settings from KTM's 2024 owner's manual for the 250 SX, "
             "300 SX, 250 XC and 300 XC.\n\n"
             "Stock is 12 and 18 on the fork, 15 clicks and 1 1/2 turns on the shock, 15 on shock rebound, 105 mm of "
             "riding sag. Dialed went 1 click out on fork comp, 7 in on fork rebound, 5 in on low-speed and 1 in on "
             "shock rebound. High-speed and sag stay stock. Seven clicks is a big move: if the front starts to feel "
             "slow or packs in the whoops, come back toward stock two at a time. Fork air: set it from the manual for "
             "your weight.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "250 SX riders: where's your fork rebound sitting?",
  "hashtags": "#ktm #250sx #twostroke #sand #dialedoffroad",
  "story": "Quiz sticker on the tiles: \"Stock fork rebound on a 2024 KTM 250 SX?\" 12 / 15 / 18.",
  "slides": [
   {"type": "cover", "eyebrow": "DIALED BASELINE", "head": "2024 KTM 250 SX",
    "sub": "about 165 lb  ·  pro pace  ·  sand moto", "footer": "Swipe for the numbers"},
   {"type": "table", "title": "STOCK VS DIALED", "sub": "2024 KTM 250 SX  ·  about 165 lb  ·  pro pace  ·  sand moto",
    "rows": [("Fork compression", "12", "13"), ("Fork rebound", "18", "11"), ("Shock low-speed comp", "15", "10"),
             ("Shock high-speed comp", "1 1/2 turns", "1 1/2 turns"), ("Shock rebound", "15", "14"),
             ("Riding sag", "105 mm", "105 mm"), ("Static sag", "35 mm", "manual's figure")],
    "note": "Clicks counted out from fully closed. Stock figures from KTM's 2024 250 SX owner's manual."},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 7 clicks in", "The big one: a calmer front in sand."),
    ("Shock low-speed, 5 clicks in", "Holds the rear up in deep sand."),
    ("Fork comp 1 out, shock rebound 1 in", "Small moves to match."),
    ("High-speed and sag stay stock", "Sag first, 105 mm."),
   ]},
   CLOSE,
  ],
  "sheet_title": "2024 KTM 250 SX",
  "sheet_sub": "about 165 lb  ·  pro pace  ·  sand moto  ·  WP AER fork",
  "tiles": [("FORK COMP", "13", "stock 12", "1 click out"),
            ("FORK REBOUND", "11", "stock 18", "7 clicks in"),
            ("SHOCK LOW-SPEED", "10", "stock 15", "5 clicks in"),
            ("SHOCK HIGH-SPEED", "1 1/2", "turns  ·  stock 1 1/2", None),
            ("SHOCK REBOUND", "14", "stock 15", "1 click in"),
            ("STATIC SAG", "35", "mm  ·  manual", None)],
  "sag_value": "105 mm",
  "sag_note": "manual says 105 mm  ·  2024 KTM 250 SX manual",
 }),
 dict(BASE, **{
  "slug": "2026-11-27-air-fork-truths",
  "title": "Carousel: 5 air fork truths",
  "design": "blue_list", "kind": "carousel", "scheduled_at": _at(27, 18),
  "caption": "An air fork works like any fork, except the air is the spring. Five things to know before you reach for "
             "the pump.\n\n"
             "Start from the manual's pressure for your weight, then refine on the bike one change at a time, clickers "
             "counted out from fully closed.\n\n"
             "Air fork or coil fork, which do you run?",
  "hashtags": "#airfork #forksetup #motocross #suspension #dialedoffroad",
  "story": "Poll: \"Air fork or coil?\" Air / Coil / Swapped to coil.",
  "slides": [
   {"type": "cover", "eyebrow": "AIR FORKS", "head": "5 AIR FORK TRUTHS", "footer": "Swipe"},
   {"type": "point", "num": "01", "head": "THE AIR IS YOUR SPRING.",
    "body": "Pressure does the spring's job. Clickers slow the oil. The air carries your weight."},
   {"type": "point", "num": "02", "head": "START FROM THE MANUAL'S CHART.",
    "body": "Air fork manuals list a starting pressure by rider weight. Start there, then refine on the bike."},
   {"type": "point", "num": "03", "head": "SET IT COLD.",
    "body": "Air warms up as you ride and pressure climbs. Set it cold, before the first moto, every time."},
   {"type": "point", "num": "04", "head": "SMALL CHANGES MATTER.",
    "body": "Use a fork pump with a fine gauge. A tire pump can't read the small steps you'll feel."},
   {"type": "point", "num": "05", "head": "AIR OR CLICKER. NOT BOTH.",
    "body": "Change one at a time. If you move both, you can't tell which one helped."},
   {"type": "closer", "head": "SET THE AIR. THEN CHANGE ONE THING.",
    "sub": "Dialed starts air fork bikes from the manual's pressure for your weight.", "footer": FOOT},
  ],
 }),
 # ------------------------------------------------------------------ Sat Nov 28
 dict(BASE, **{
  "slug": "2026-11-28-yz250f-split",
  "title": "Settings card: 2022 Yamaha YZ250F",
  "design": "split", "kind": "carousel", "scheduled_at": _at(28, 12),
  "caption": "2022 Yamaha YZ250F. About 175 lb, learning, muddy moto, stock suspension, stability and comfort the "
             "goals. Left is stock from the 2022 YZ250F owner's service manual, right is the baseline Dialed built for "
             "that rider.\n\n"
             "Fork comp 10 to 14, fork rebound 7 to 12. Shock low-speed 8 to 12, high-speed 7/8 turn to 1 3/8, "
             "rebound 10 to 14. Sag 100 mm, the top of Yamaha's 90 to 100 window. Comfort and a newer rider drove it: "
             "everything came out. Five clicks is a big move, so if it starts to bottom, come back toward stock two at "
             "a time.\n\n"
             "All counted out from fully closed. Starting points riders refine on the bike, one change at a time.\n\n"
             "Newer riders: does your stock YZ250F feel stiff?",
  "hashtags": "#yz250f #yamaha #motocross #suspension #dialedoffroad",
  "story": "Poll on the split: \"Stock YZ250F for a newer rider?\" Too stiff / Just right / Too soft.",
  "slides": [
   {"type": "hot", "head": "2022 YAMAHA YZ250F. MUD, ABOUT 175 LB.", "sub": ""},
   {"type": "points", "title": "WHAT MOVED", "items": [
    ("Fork rebound, 5 clicks out", "A quicker front for a newer rider."),
    ("Fork comp and low-speed, 4 out", "Softer, so it moves on slow stuff."),
    ("Shock rebound 4 out, high-speed 1/2 out", "The rear stays with the ground."),
    ("Sag at 100 mm", "The top of Yamaha's 90 to 100 window."),
   ]},
   CLOSE_SPLIT,
  ],
  "split": {"left": "STOCK",
            "left_lines": ["Fork comp 10", "Fork reb 7", "Shock low 8", "High-speed 7/8", "Shock reb 10", "Sag 90 to 100"],
            "right": "DIALED",
            "right_lines": ["Fork comp 14", "Fork reb 12", "Shock low 12", "High-speed 1 3/8", "Shock reb 14", "Sag 100 mm"]},
 }),
 dict(BASE, **{
  "slug": "2026-11-28-soft-lows-firm-highs",
  "title": "Comment answer: soft lows, firm highs",
  "design": "classic", "kind": "carousel", "scheduled_at": _at(28, 18),
  "caption": "A comment on our CRF250R card picked up on it: the low-speed went softer while the high-speed went "
             "firmer. That isn't a contradiction. The two adjusters on the shock do different jobs.\n\n"
             "Low-speed handles the slow stuff, like squat on the gas. High-speed handles the fast hits, like landings "
             "and square edges. Starting points, refined on the bike one change at a time, counted out from fully "
             "closed.\n\n"
             "Link in bio. Have you ever moved your low-speed and high-speed opposite ways?",
  "hashtags": "#shocksetup #highspeed #lowspeed #motocross #dialedoffroad",
  "story": "Question box: \"Low-speed or high-speed, which one confuses you?\" Share the best ones back.",
  "slides": [
   {"type": "hot", "head": "SOFT LOWS, FIRM HIGHS?",
    "sub": "A comment on our CRF250R card picked up on it. The shock's two adjusters do different jobs, so they can "
           "move opposite ways."},
   {"type": "points", "title": "TWO ADJUSTERS, TWO JOBS", "items": [
    ("Low-speed: the slow stuff", "Squat on the gas, body weight, rollers."),
    ("High-speed: the fast hits", "Landings, square edges, holes."),
    ("Softer lows, firmer highs", "More grip on the gas, more hold on hits."),
    ("Clicks and turns", "Low-speed in clicks, high-speed usually turns."),
   ]},
   {"type": "closer", "head": "TWO JOBS. ONE CHANGE AT A TIME.",
    "sub": "Tell Dialed what the rear did and it tells you which adjuster to move.", "footer": FOOT},
  ],
 }),
]
