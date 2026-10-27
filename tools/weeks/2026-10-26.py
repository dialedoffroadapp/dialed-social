# Week of 2026-10-26 (posts Tue Oct 27 to Mon Nov 2). The first week, kept as the worked example.
# Each post: slug (YYYY-MM-DD-topic, the folder under posts/), title, design (see tools/designs.py DESIGNS),
# kind (image | carousel), scheduled_at (UTC ISO; 6:40 pm Boise), caption, hashtags (first comment on IG,
# appended to the caption by publish_week.py), story (a Story idea for the same day), slides (per design).
WEEK = [{'slug': '2026-10-27-3-0-launch',
  'title': 'Carousel: 3.0 launch',
  'design': 'screens',
  'kind': 'carousel',
  'scheduled_at': '2026-10-28T00:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': 'Dialed Offroad 3.0 is live on the App Store and Google Play.\n'
             '\n'
             'What changed: your bikes live in the Garage, riding and refining happen on ride days, sag is measured or '
             "entered instead of guessed, every tune comes with the reasoning, and it's built for off-road conditions, "
             'not just the track.\n'
             '\n'
             'Build your first tune free. Link in bio.',
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #suspension #dialedoffroad #newrelease',
  'story': 'Share the cover with the link sticker. Then a second story: "What should the 3.1 settings card be?" '
           'question box.',
  'slides': [{'type': 'cover',
              'eyebrow': 'NEW',
              'head': 'DIALED OFFROAD 3.0 IS OUT.',
              'sub': 'iOS and Android.',
              'footer': 'Swipe'},
             {'type': 'point',
              'num': '01',
              'head': 'YOUR BIKES LIVE IN THE GARAGE.',
              'body': 'Every bike you added came with you, with its setup, tires, sag and service log in one place.'},
             {'type': 'point',
              'num': '02',
              'head': 'RIDE DAYS.',
              'body': 'Log the ride, the conditions and how the bike felt. The next refinement starts from what '
                      'actually happened, not what you remember.'},
             {'type': 'point',
              'num': '03',
              'head': 'SAG, KNOWN NOT GUESSED.',
              'body': 'Measure it in the app step by step, or enter the number if you already know it. Every tune '
                      'builds on it.'},
             {'type': 'point',
              'num': '04',
              'head': 'THE WHY, NOT JUST THE NUMBERS.',
              'body': 'Every tune comes with the reasoning in plain words, so you learn your bike instead of copying '
                      'numbers.'},
             {'type': 'point',
              'num': '05',
              'head': 'BUILT FOR OFF-ROAD TOO.',
              'body': 'Hardpack, loam, sand, mud, rocks, roots, ruts, whoops. Tell it the conditions and the tune '
                      'starts there.'},
             {'type': 'closer',
              'head': 'FREE TO START.',
              'sub': 'Build your first tune free. Pro unlocks the full refine loop, setup history and more bikes.',
              'footer': 'Link in bio  ·  App Store  ·  Google Play'}]},
 {'slug': '2026-10-28-250sxf-setup-sheet',
  'title': 'Settings card: 2026 KTM 250 SX-F',
  'design': 'sheet',
  'kind': 'carousel',
  'scheduled_at': '2026-10-29T00:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': '2026 KTM 250 SX-F. 165 lb, fast, hardpack moto. This is the baseline Dialed built, next to the stock '
             "settings from the 2026 owner's manual.\n"
             '\n'
             "The numbers aren't a law. They're where to start so your first ride is spent refining instead of "
             'guessing. Ride it, log how it felt, move one thing.\n'
             '\n'
             "Drop your bike, year and weight below and I'll run yours.",
  'hashtags': '#ktm #250sxf #dirtbikes #moto #mx #motocross #suspension #clickers #dialedoffroad',
  'story': 'Question box: "Drop your bike, year and weight." Every answer is a future settings-card post.',
  'slides': [{'type': 'cover',
              'eyebrow': 'DIALED BASELINE',
              'head': '2026 KTM 250 SX-F',
              'sub': '165 lb  ·  fast  ·  hardpack moto',
              'footer': 'Swipe for the numbers'},
             {'type': 'table',
              'title': 'STOCK VS DIALED',
              'sub': '2026 KTM 250 SX-F  ·  165 lb  ·  fast  ·  hardpack moto',
              'rows': [('Fork compression', '12', '12'),
                       ('Fork rebound', '18', '10'),
                       ('Fork air', 'see manual', '10.2 bar'),
                       ('Shock low-speed comp', '15', '10'),
                       ('Shock high-speed comp', '1.5 turns', '1.5 turns'),
                       ('Shock rebound', '15', '12'),
                       ('Riding sag', '105 mm', '105 mm')],
              'note': "Clicks counted out from fully closed. Stock figures from the 2026 KTM owner's manual."},
             {'type': 'points',
              'title': 'WHAT MOVED',
              'items': [('Fork rebound, 8 clicks slower',
                         'Keeps the front planted on hardpack instead of springing back at you.'),
                        ('Shock low-speed comp, 5 clicks in',
                         "Holds the rear up under throttle so it doesn't squat and push wide."),
                        ('Shock rebound, 3 clicks slower', 'Less kick off the braking bumps.'),
                        ('Fork comp, high-speed and sag stay put', 'Not every click has to move.')]},
             {'type': 'closer',
              'head': "STOCK ISN'T WRONG. IT'S FOR SOMEONE ELSE.",
              'sub': 'This is a starting point, not a law. Ride it, log how it felt, refine from there.',
              'cta': "Drop your bike, year and weight below and I'll run yours.",
              'footer': 'Dialed Offroad 3.0  ·  App Store  ·  Google Play'}],
  'sheet_title': '2026 KTM 250 SX-F',
  'sheet_sub': '165 lb  ·  fast  ·  hardpack moto  ·  WP XACT air fork',
  'sag_note': "stock 105 mm  ·  from the 2026 owner's manual"},
 {'slug': '2026-10-29-clicker-cheat-sheet',
  'title': 'Carousel: symptom to clicker cheat sheet',
  'design': 'paper_list',
  'kind': 'carousel',
  'scheduled_at': '2026-10-30T00:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': 'Eight symptoms, eight places to start. Not laws, starting points. One change at a time, two clicks max, '
             'and write down what you did and how it felt.\n'
             '\n'
             'Save it for the track. Send it to the guy who runs stock and complains.\n'
             '\n'
             "What's the one symptom you can't get rid of?",
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #suspension #suspensionsetup #clickers #dialedoffroad',
  'story': 'Share the cover to your story with "Save this for the track" and the link sticker.',
  'slides': [{'type': 'cover',
              'eyebrow': 'CHEAT SHEET',
              'head': 'YOUR BIKE IS TELLING YOU WHICH CLICKER TO TURN',
              'sub': 'Save this for the track.',
              'footer': 'In = more damping. Out = less. One change at a time.'},
             {'type': 'symptom',
              'head': 'FRONT END DIVES UNDER BRAKING',
              'fix': 'Fork compression: 1 to 2 clicks in.',
              'why': 'Check sag first. A rear end that sits too high throws weight onto the fork.'},
             {'type': 'symptom',
              'head': 'FORK FEELS HARSH ON SQUARE EDGES',
              'fix': 'Fork compression: 1 to 2 clicks out.',
              'why': "If it gets harsher as the bumps get closer together, it's packing. That's rebound, not "
                     'compression.'},
             {'type': 'symptom',
              'head': 'FORK PACKS DOWN THROUGH BRAKING BUMPS',
              'fix': 'Fork rebound: 1 to 2 clicks out (faster).',
              'why': "The fork isn't recovering between hits, so each one starts lower and harsher than the last."},
             {'type': 'symptom',
              'head': 'FRONT FEELS LOOSE, DEFLECTS, HEADSHAKES ON EXIT',
              'fix': 'Fork rebound: 1 to 2 clicks in (slower).',
              'why': "Rebound that's too fast springs the front back at you. A rear end that's too high makes it "
                     'worse, so check sag.'},
             {'type': 'symptom',
              'head': 'REAR KICKS ON BRAKING BUMPS',
              'fix': 'Shock rebound: 1 to 2 clicks in (slower).',
              'why': "If the rear feels dead and harsh instead of kicking, it's packing. Go the other way."},
             {'type': 'symptom',
              'head': 'REAR SQUATS AND WALLOWS OUT OF CORNERS',
              'fix': 'Shock low-speed compression: 1 to 2 clicks in.',
              'why': 'Low-speed handles rider-driven movement: squat, wallow, G-outs. Check sag first.'},
             {'type': 'symptom',
              'head': 'BOTTOMING ON JUMP LANDINGS',
              'fix': 'Shock high-speed: 1/4 turn in. Fork compression: 1 to 2 clicks in.',
              'why': "If it bottoms on every landing, that's springs or air pressure, not clickers."},
             {'type': 'symptom',
              'head': 'FRONT PUSHES IN FLAT CORNERS',
              'fix': 'Riding sag: try 2 to 3 mm less.',
              'why': 'A slightly higher rear puts more weight on the front tire. Fork height in the clamps is the next '
                     'lever.'},
             {'type': 'closer',
              'head': 'ONE CHANGE AT A TIME. TWO CLICKS MAX. WRITE IT DOWN.',
              'sub': 'Dialed gives you the starting point and logs every click you change, so you always know what you '
                     'did.',
              'footer': 'Dialed Offroad 3.0  ·  App Store  ·  Google Play'}]},
 {'slug': '2026-10-30-arm-pump',
  'title': 'Hot take: arm pump',
  'design': 'glow',
  'kind': 'image',
  'scheduled_at': '2026-10-31T00:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': "Arm pump gets treated like a fitness problem. A lot of the time it's a harsh front end: the fork isn't "
             'absorbing the chatter, so you squeeze the bars to survive it, and your forearms are full by lap three.\n'
             '\n'
             'Before the gym fixes it, try the free stuff. A click or two out on fork compression. Check your sag. '
             "Make sure rebound isn't packing the fork down through the braking bumps.\n"
             '\n'
             "What's your front comp at right now?",
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #armpump #suspension #dialedoffroad',
  'story': 'Poll: "Where\'s your fork compression right now?" 10 / 12 / 14 / no idea. Reply to the "no idea" voters '
           'with the app link.',
  'slides': [{'type': 'hot',
              'head': 'ARM PUMP IS NOT A FITNESS PROBLEM.',
              'sub': "Most of the time it's a harsh front end and a death grip to survive it. Fix the fork before you "
                     'buy another grip trainer.'}]},
 {'slug': '2026-10-31-dealer-wont-tell-you',
  'title': "Carousel: what the dealer won't tell you",
  'design': 'blue_list',
  'kind': 'carousel',
  'scheduled_at': '2026-11-01T00:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': 'Six things about your suspension that nobody at the dealership is going to walk you through. Save this '
             'one for the next guy who tells you stock is fine.\n'
             '\n'
             'Which one did you learn the hard way?',
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #suspension #suspensiontuning #dialedoffroad',
  'story': 'Share slide 02 (sag comes first) to your story with the link sticker to the app.',
  'slides': [{'type': 'cover',
              'eyebrow': 'SUSPENSION',
              'head': "WHAT THE DEALER WON'T TELL YOU ABOUT YOUR SUSPENSION",
              'footer': 'Swipe'},
             {'type': 'point',
              'num': '01',
              'head': 'THE STOCK CLICKERS WERE SET FOR SOMEONE ELSE.',
              'body': "The factory baseline is one rider, one weight, one track. If that isn't you, the bike is set up "
                      'wrong on day one, and nobody at the dealership is going to mention it.'},
             {'type': 'point',
              'num': '02',
              'head': 'SAG COMES FIRST. EVERY TIME.',
              'body': 'Every clicker number in the manual assumes sag is right. Set it before you touch a single '
                      'click. The 2026 250 SX-F manual calls for 105 mm of riding sag.'},
             {'type': 'point',
              'num': '03',
              'head': 'COMFORT, STANDARD AND SPORT ARE REFERENCE POINTS, NOT LIMITS.',
              'body': "The manual's three settings are examples, not a fence. Your right number can live between them "
                      'or past them.'},
             {'type': 'point',
              'num': '04',
              'head': 'THE FREE ADJUSTMENTS COME BEFORE THE EXPENSIVE ONES.',
              'body': 'A revalve is a real fix and sometimes the right one. But most riders have never used the '
                      'adjustments they already paid for. Those come first.'},
             {'type': 'point',
              'num': '05',
              'head': 'THE TRACK CHANGES BY NOON. SO SHOULD YOUR CLICKERS.',
              'body': 'Hardpack in the morning, ruts and square edges by lunch. One setting for the whole day is a '
                      'compromise you chose by accident.'},
             {'type': 'point',
              'num': '06',
              'head': 'COUNT OUT FROM FULLY CLOSED. WRITE IT DOWN.',
              'body': "Turn the clicker in until it stops, then count out. Log every change and how it felt, or you'll "
                      'be guessing again next weekend.'},
             {'type': 'closer',
              'head': 'DIALED BUILDS YOUR STARTING POINT.',
              'sub': 'From your bike, your weight and how you ride. Then you refine it on ride days.',
              'footer': 'Dialed Offroad 3.0  ·  App Store  ·  Google Play'}]},
 {'slug': '2026-11-01-five-clickers',
  'title': 'Carousel: what each clicker does',
  'design': 'dials',
  'kind': 'carousel',
  'scheduled_at': '2026-11-02T01:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': "Five clickers, millions of combinations, and most riders can't tell you what two of them do. Here's the "
             "whole set in plain words, plus the one thing that isn't a clicker and has to come first.\n"
             '\n'
             'Save it. Tag the guy who "just leaves it stock".\n'
             '\n'
             'Which one do you actually understand?',
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #suspension #suspension101 #dialedoffroad',
  'story': 'Quiz sticker: "Which clicker controls squat out of corners?" Fork comp / Shock low-speed / Shock rebound.',
  'slides': [{'type': 'cover',
              'eyebrow': 'SUSPENSION 101',
              'head': "5 CLICKERS. HERE'S WHAT EACH ONE ACTUALLY DOES.",
              'footer': 'Swipe'},
             {'type': 'point',
              'tag': 'FORK  ·  COMPRESSION',
              'head': 'HOW FAST THE FORK CAN COMPRESS ON A HIT.',
              'body': 'In holds the front up under braking and on jump faces. Out is plusher over chatter but dives '
                      'more.'},
             {'type': 'point',
              'tag': 'FORK  ·  REBOUND',
              'head': 'HOW FAST THE FORK EXTENDS AFTER A HIT.',
              'body': "Too fast: loose, deflecting, nervous front. Too slow: it packs down and turns harsh. It's the "
                      'clicker most riders never touch.'},
             {'type': 'point',
              'tag': 'SHOCK  ·  LOW-SPEED COMPRESSION',
              'head': 'RIDER-DRIVEN MOVEMENT.',
              'body': 'Squat under throttle, wallow in corners, G-outs, braking. In holds the rear up. Out gives more '
                      'squat and more grip.'},
             {'type': 'point',
              'tag': 'SHOCK  ·  HIGH-SPEED COMPRESSION',
              'head': 'BIG, SUDDEN HITS.',
              'body': "Jump landings, square edges, the stuff that hits hard and fast. It's set in turns, not clicks, "
                      'and a quarter turn is a big change.'},
             {'type': 'point',
              'tag': 'SHOCK  ·  REBOUND',
              'head': 'HOW FAST THE REAR EXTENDS.',
              'body': 'Too fast: the rear kicks on braking bumps. Too slow: it packs and feels dead. Sag changes this '
                      'one, so set sag first.'},
             {'type': 'point',
              'tag': 'NOT A CLICKER',
              'head': 'SAG. SET IT FIRST.',
              'body': 'Every clicker in the manual assumes sag is right. On a 2026 250 SX-F the manual calls for 105 '
                      "mm of riding sag. Measure it, don't guess it."},
             {'type': 'closer',
              'head': 'DIALED SETS THE STARTING POINT FOR YOUR BIKE AND WEIGHT.',
              'sub': 'Then it logs every click you change on ride days.',
              'footer': 'Dialed Offroad 3.0  ·  App Store  ·  Google Play'}]},
 {'slug': '2026-11-02-stock-vs-you',
  'title': 'Hot take: stock is a starting point',
  'design': 'split',
  'kind': 'image',
  'scheduled_at': '2026-11-03T01:40:00Z',
  'post_to_ig': True,
  'post_to_fb': True,
  'fb_mode': 'cover',
  'caption': "Every bike leaves the factory set up for a rider who isn't you. Stock isn't wrong. It just fits somebody "
             'else.\n'
             '\n'
             "Sag, then clickers, then ride it and refine. That's the whole game.\n"
             '\n'
             'Still on stock? Be honest.',
  'hashtags': '#dirtbikes #moto #mx #motocross #enduro #suspension #dialedoffroad',
  'story': 'Poll: "Still running stock clickers?" Yes / No / What\'s a clicker.',
  'slides': [{'type': 'hot',
              'head': "STOCK ISN'T A SETTING. IT'S A STARTING POINT.",
              'sub': "The factory set it for one rider, one weight, one track. That rider isn't you."}]}]
