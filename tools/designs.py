import os, sys, math, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import F, wrap, fit, draw_block, tracked, chevrons, DISPLAY, DISPLAY_UP, BODY_F, MED, SEMI, BOLD, mark, wordmark

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "out")
SHOTS = os.path.join(BASE, "shots")

W, H = 1080, 1350
M = 84
CARBON = (11, 12, 16)
PANEL = (21, 25, 32)
BORDER = (38, 43, 54)
BLUE = (29, 155, 240)
BLUE_DEEP = (16, 110, 176)
WHITE = (245, 247, 252)
STEEL = (138, 147, 166)
BODY = (201, 207, 218)
LIGHT = (245, 247, 252)
LIGHT_LINE = (215, 220, 230)
LIGHT_TILE = (255, 255, 255)
INK = (11, 12, 16)
INK_SOFT = (74, 80, 94)
SLATE = (42, 48, 60)


def canvas(bg):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def brand(d, theme="dark", x=M, y=70):
    img = d._image
    if theme == "dark":
        m, first, second = mark("dark", 56), WHITE, BLUE
    elif theme == "blue":
        m, first, second = mark("white", 56), WHITE, CARBON
    else:
        m, first, second = mark("light", 56), INK, BLUE
    img.paste(m, (x, y), m)
    wordmark(d, x + m.width + 22, y + 6, 40, first, second)


def counter(d, text, fill):
    if text:
        d.text((W - M, H - 106), text, font=F(SEMI, 26), fill=fill, anchor="ra")


def sticker(img, text, cx, cy, angle, fill, color, size=40, pad=28):
    """Rotated label pasted onto img, centered at cx, cy."""
    f = F(DISPLAY_UP, size)
    tw = int(f.getlength(text)) + 2 * pad
    th = size + 2 * pad - 10
    lab = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lab)
    ld.rectangle([0, 0, tw - 1, th - 1], fill=fill)
    ld.text((tw // 2, th // 2), text, font=f, fill=color, anchor="mm")
    lab = lab.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(lab, (cx - lab.width // 2, cy - lab.height // 2), lab)


# ------------------------------------------------------------------ 1. Threads-style screenshot
def post1(post):
    s = post["slides"][0]
    img, d = canvas(CARBON)
    # glow
    glow = Image.new("RGB", (W, H), CARBON)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([120, 260, 960, 1060], fill=(18, 60, 96))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    img.paste(glow)
    d = ImageDraw.Draw(img)
    body = s["head"].capitalize() + "\n\n" + s.get("sub", "")
    bf = F(BODY_F, 46)
    lines = []
    for para in body.split("\n"):
        lines += wrap(para, bf, W - 2 * M - 2 * 56) if para else [""]
    body_h = sum((46 * 1.4) if l else 28 for l in lines)
    ph = 56 + 84 + 36 + body_h + 44 + 48 + 56
    py = int((H - ph) / 2)
    d.rounded_rectangle([M, py, W - M, py + ph], radius=32, fill=PANEL, outline=BORDER, width=2)
    x = M + 56
    y = py + 56
    # round avatar from the real app icon
    icon = Image.open(os.path.join(BASE, "logo", "icon.png")).convert("RGBA").resize((84, 84), Image.LANCZOS)
    maskc = Image.new("L", (84, 84), 0)
    ImageDraw.Draw(maskc).ellipse([0, 0, 83, 83], fill=255)
    img.paste(icon, (x, y), maskc)
    d = ImageDraw.Draw(img)
    d.text((x + 108, y + 6), "dialed_offroad", font=F(BOLD, 36), fill=WHITE, anchor="la")
    # verified-style dot
    d.text((x + 108, y + 50), "Dialed Off-road", font=F(MED, 28), fill=STEEL, anchor="la")
    d.text((W - M - 56, y + 10), "2h", font=F(MED, 30), fill=STEEL, anchor="ra")
    y += 84 + 36
    for l in lines:
        if l:
            d.text((x, y), l, font=bf, fill=WHITE, anchor="la")
            y += int(46 * 1.4)
        else:
            y += 28
    y += 44
    # icon row
    ix = x
    c = STEEL
    # heart
    d.ellipse([ix, y, ix + 20, y + 20], outline=c, width=4)
    d.ellipse([ix + 16, y, ix + 36, y + 20], outline=c, width=4)
    d.polygon([(ix + 2, y + 14), (ix + 34, y + 14), (ix + 18, y + 36)], fill=PANEL)
    d.line([(ix + 2, y + 14), (ix + 18, y + 34), (ix + 34, y + 14)], fill=c, width=4)
    ix += 90
    # comment
    d.rounded_rectangle([ix, y, ix + 38, y + 30], radius=10, outline=c, width=4)
    d.polygon([(ix + 8, y + 28), (ix + 18, y + 28), (ix + 8, y + 38)], fill=c)
    ix += 90
    # repost
    d.line([(ix, y + 10), (ix + 28, y + 10)], fill=c, width=4)
    d.polygon([(ix + 28, y + 2), (ix + 38, y + 10), (ix + 28, y + 18)], fill=c)
    d.line([(ix + 38, y + 28), (ix + 10, y + 28)], fill=c, width=4)
    d.polygon([(ix + 10, y + 20), (ix, y + 28), (ix + 10, y + 36)], fill=c)
    ix += 90
    # share
    d.line([(ix + 18, y + 30), (ix + 18, y + 2)], fill=c, width=4)
    d.polygon([(ix + 6, y + 12), (ix + 18, y), (ix + 30, y + 12)], fill=c)
    d.line([(ix, y + 36), (ix + 36, y + 36)], fill=c, width=4)
    d.text((M, H - 106), "@dialed_offroad", font=F(MED, 26), fill=STEEL, anchor="la")
    return [img]


# ------------------------------------------------------------------ 2. Light setup sheet
def post2(post):
    imgs = []
    tbl = post["slides"][1]
    # slide 1: sheet
    img, d = canvas(LIGHT)
    d.rectangle([0, 0, W, 250], fill=BLUE)
    tracked(d, M, 70, "SETUP SHEET", F(SEMI, 28), WHITE, 5)
    d.text((M, 110), post.get("sheet_title", post["slides"][0]["head"]), font=F(DISPLAY, 104), fill=WHITE, anchor="la")
    mw = mark("white", 72)
    img.paste(mw, (W - M - mw.width, 62), mw)
    d = ImageDraw.Draw(img)
    d.text((M, 284), post.get("sheet_sub", post["slides"][0].get("sub", "")), font=F(MED, 32), fill=INK_SOFT, anchor="la")
    tiles = post.get("tiles") or [
        ("FORK COMP", "12", "stock 12", None),
        ("FORK REBOUND", "10", "stock 18", "8 clicks in"),
        ("FORK AIR", "10.2", "bar", None),
        ("SHOCK LOW-SPEED", "10", "stock 15", "5 clicks in"),
        ("SHOCK HIGH-SPEED", "1.5", "turns  ·  stock 1.5", None),
        ("SHOCK REBOUND", "12", "stock 15", "3 clicks in"),
    ]
    gx, gy = M, 350
    tw_, th_ = (W - 2 * M - 28) // 2, 220
    for i, (lab, val, sub, chip) in enumerate(tiles):
        r, c = divmod(i, 2)
        x0 = gx + c * (tw_ + 28)
        y0 = gy + r * (th_ + 20)
        d.rounded_rectangle([x0, y0, x0 + tw_, y0 + th_], radius=22, fill=LIGHT_TILE, outline=LIGHT_LINE, width=2)
        tracked(d, x0 + 32, y0 + 28, lab, F(SEMI, 22), INK_SOFT, 2)
        d.text((x0 + 28, y0 + 62), val, font=F(DISPLAY, 100), fill=(BLUE if chip else INK), anchor="la")
        d.text((x0 + 32, y0 + th_ - 44), sub, font=F(MED, 24), fill=INK_SOFT, anchor="la")
        if chip:
            cf = F(SEMI, 22)
            cw = int(cf.getlength(chip)) + 32
            d.rounded_rectangle([x0 + tw_ - 28 - cw, y0 + th_ - 66, x0 + tw_ - 28, y0 + th_ - 24], radius=21, fill=BLUE)
            d.text((x0 + tw_ - 28 - cw // 2, y0 + th_ - 45), chip, font=cf, fill=WHITE, anchor="mm")
    y = gy + 3 * (th_ + 20) + 4
    d.rounded_rectangle([M, y, W - M, y + 112], radius=22, fill=INK)
    tracked(d, M + 32, y + 24, "RIDING SAG", F(SEMI, 22), BLUE, 2)
    d.text((M + 32, y + 50), "105 mm", font=F(DISPLAY, 56), fill=WHITE, anchor="la")
    d.text((W - M - 32, y + 56), post.get("sag_note", ""), font=F(MED, 24), fill=STEEL, anchor="rm")
    d.text((M, H - 106), "Clicks counted out from fully closed. A starting point, not a law.", font=F(MED, 26), fill=INK_SOFT, anchor="la")
    counter(d, "01 / 03", INK_SOFT)
    imgs.append(img)

    # slide 2: what moved (light)
    pts = post["slides"][2]
    img, d = canvas(LIGHT)
    brand(d, "light")
    d.text((M, 200), "WHAT MOVED", font=F(DISPLAY, 110), fill=INK, anchor="la")
    y = 360
    hf, bf = F(DISPLAY_UP, 50), F(BODY_F, 34)
    for head, body in pts["items"]:
        d.rounded_rectangle([M, y + 6, M + 22, y + 48], radius=4, fill=BLUE)
        y = draw_block(d, M + 48, y, wrap(head, hf, W - 2 * M - 48), hf, 50, 1.05, INK)
        y += 6
        y = draw_block(d, M + 48, y, wrap(body, bf, W - 2 * M - 48), bf, 34, 1.4, INK_SOFT)
        y += 52
    counter(d, "02 / 03", INK_SOFT)
    d.text((M, H - 106), "@dialed_offroad", font=F(MED, 26), fill=INK_SOFT, anchor="la")
    imgs.append(img)

    # slide 3: closer (light)
    cl = post["slides"][3]
    img, d = canvas(LIGHT)
    brand(d, "light")
    font, lines, size = fit(cl["head"], DISPLAY, W - 2 * M, 460, 140, 96, 0.96)
    y = 300
    y = draw_block(d, M, y, lines, font, size, 0.96, INK)
    y += 40
    sf = F(MED, 40)
    y = draw_block(d, M, y, wrap(cl["sub"], sf, W - 2 * M), sf, 40, 1.4, INK_SOFT)
    y += 60
    cf = F(SEMI, 34)
    cta = cl["cta"]
    cl_lines = wrap(cta, cf, W - 2 * M - 96)
    ch = len(cl_lines) * 46 + 64
    d.rounded_rectangle([M, y, W - M, y + ch], radius=24, fill=BLUE)
    draw_block(d, M + 48, y + 32, cl_lines, cf, 34, 1.35, WHITE)
    d.text((M, H - 106), cl["footer"], font=F(MED, 26), fill=INK_SOFT, anchor="la")
    counter(d, "03 / 03", INK_SOFT)
    imgs.append(img)
    return imgs


# ------------------------------------------------------------------ 3. All blue, giant numerals
def post3(post):
    imgs = []
    n = len(post["slides"])
    for i, s in enumerate(post["slides"], 1):
        img, d = canvas(BLUE)
        brand(d, "blue")
        if s["type"] == "cover":
            sticker(img, s["eyebrow"], 300, 330, 6, CARBON, WHITE, size=44)
            d = ImageDraw.Draw(img)
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 640, 160, 110, 0.95)
            draw_block(d, M, 420, lines, font, size, 0.95, WHITE)
            x = tracked(d, M, H - 120, "SWIPE", F(SEMI, 26), WHITE, 3)
            chevrons(d, x + 10, H - 106, n=2, size=12, fill=WHITE, width=4)
        elif s["type"] == "point":
            d.text((M - 10, 200), s["num"], font=F(DISPLAY, 300), fill=CARBON, anchor="la")
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 360, 110, 80, 0.96)
            y = draw_block(d, M, 540, lines, font, size, 0.96, WHITE)
            y += 36
            d.rectangle([M, y, M + 120, y + 6], fill=CARBON)
            y += 40
            bf = F(MED, 38)
            draw_block(d, M, y, wrap(s["body"], bf, W - 2 * M), bf, 38, 1.42, (236, 246, 254))
            d.text((M, H - 106), "@dialed_offroad", font=F(MED, 26), fill=(190, 225, 250), anchor="la")
        else:
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 460, 150, 96, 0.96)
            y = draw_block(d, M, 340, lines, font, size, 0.96, WHITE)
            y += 40
            sf = F(MED, 40)
            y = draw_block(d, M, y, wrap(s["sub"], sf, W - 2 * M), sf, 40, 1.4, (236, 246, 254))
            y += 64
            pf = F(DISPLAY_UP, 40)
            label = "GET THE APP  ·  LINK IN BIO"
            pw = int(pf.getlength(label)) + 96
            d.rounded_rectangle([M, y, M + pw, y + 92], radius=46, fill=CARBON)
            d.text((M + 48, y + 46), label, font=pf, fill=WHITE, anchor="lm")
            d.text((M, H - 106), s["footer"], font=F(MED, 26), fill=(190, 225, 250), anchor="la")
        counter(d, f"{i:02d} / {n:02d}", (190, 225, 250))
        imgs.append(img)
    return imgs


# ------------------------------------------------------------------ 4. Split screen
def post4(post):
    s = post["slides"][0]
    img, d = canvas(CARBON)
    brand(d, "dark")
    font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 330, 120, 84, 0.95)
    draw_block(d, M, 190, lines, font, size, 0.95, WHITE)
    top = 560
    # left slate, right blue, diagonal split
    d.polygon([(0, top), (610, top), (470, H), (0, H)], fill=SLATE)
    d.polygon([(610, top), (W, top), (W, H), (470, H)], fill=BLUE)
    sp = post.get("split") or {"left": "STOCK", "left_lines": ["One rider.", "One weight.", "One track.", "Not you."], "right": "YOU", "right_lines": ["Your weight.", "Your speed.", "Your track.", "Your bike."]}
    d.text((M, top + 90), sp["left"], font=F(DISPLAY, 120), fill=WHITE, anchor="la")
    d.rectangle([M, top + 230, M + 90, top + 236], fill=STEEL)
    lf = F(MED, 40)
    y = top + 280
    for l in sp["left_lines"]:
        d.text((M, y), l, font=lf, fill=BODY, anchor="la")
        y += 60
    rx = 650
    d.text((rx, top + 90), sp["right"], font=F(DISPLAY, 120), fill=WHITE, anchor="la")
    d.rectangle([rx, top + 230, rx + 90, top + 236], fill=CARBON)
    y = top + 280
    for l in sp["right_lines"]:
        d.text((rx, y), l, font=lf, fill=WHITE, anchor="la")
        y += 60
    d.text((M, H - 80), "@dialed_offroad", font=F(MED, 24), fill=(190, 198, 212), anchor="la")
    return [img]


# ------------------------------------------------------------------ 5. Light cheat sheet with flow boxes
def post5(post):
    imgs = []
    n = len(post["slides"])
    for i, s in enumerate(post["slides"], 1):
        img, d = canvas(LIGHT)
        brand(d, "light")
        if s["type"] == "cover":
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 600, 150, 100, 0.95)
            y = draw_block(d, M, 300, lines, font, size, 0.95, INK)
            sticker(img, "SAVE THIS", W - 300, 250, -8, BLUE, WHITE, size=44)
            d = ImageDraw.Draw(img)
            y += 40
            d.text((M, y), s["sub"], font=F(MED, 40), fill=INK_SOFT, anchor="la")
            d.text((M, H - 106), s["footer"], font=F(MED, 26), fill=INK_SOFT, anchor="la")
        elif s["type"] == "symptom":
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M - 96, 300, 100, 64, 0.96)
            bh = 48 + 34 + 24 + len(lines) * size * 0.96 + 52
            pf = F(DISPLAY_UP, 64)
            fl = wrap(s["fix"], pf, W - 2 * M - 96)
            ph = 48 + 32 + 24 + len(fl) * 64 * 1.1 + 52
            wf = F(BODY_F, 38)
            wl = wrap(s["why"], wf, W - 2 * M)
            wh = len(wl) * 38 * 1.42
            total = bh + 110 + ph + 48 + wh
            y = max(190, int((H - 150 - total) / 2) + 60)
            d.rounded_rectangle([M, y, W - M, y + bh], radius=26, fill=INK)
            tracked(d, M + 48, y + 44, "SYMPTOM", F(SEMI, 26), STEEL, 5)
            draw_block(d, M + 48, y + 106, lines, font, size, 0.96, WHITE)
            y += bh + 24
            cx = W // 2
            d.line([(cx, y), (cx, y + 44)], fill=BLUE, width=8)
            d.polygon([(cx - 22, y + 36), (cx + 22, y + 36), (cx, y + 64)], fill=BLUE)
            y += 86
            d.rounded_rectangle([M, y, W - M, y + ph], radius=26, fill=BLUE)
            tracked(d, M + 48, y + 44, "START HERE", F(SEMI, 26), (200, 230, 252), 5)
            draw_block(d, M + 48, y + 104, fl, pf, 64, 1.1, WHITE)
            y += ph + 48
            draw_block(d, M, y, wl, wf, 38, 1.42, INK_SOFT)
            d.text((M, H - 106), "In = more damping.  Out = less.  One change at a time.", font=F(MED, 24), fill=INK_SOFT, anchor="la")
        else:
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 520, 140, 96, 0.96)
            y = draw_block(d, M, 300, lines, font, size, 0.96, INK)
            y += 40
            sf = F(MED, 40)
            y = draw_block(d, M, y, wrap(s["sub"], sf, W - 2 * M), sf, 40, 1.4, INK_SOFT)
            y += 64
            pf = F(DISPLAY_UP, 40)
            label = "GET THE APP  ·  LINK IN BIO"
            pw = int(pf.getlength(label)) + 96
            d.rounded_rectangle([M, y, M + pw, y + 92], radius=46, fill=BLUE)
            d.text((M + 48, y + 46), label, font=pf, fill=WHITE, anchor="lm")
            d.text((M, H - 106), s["footer"], font=F(MED, 26), fill=INK_SOFT, anchor="la")
        counter(d, f"{i:02d} / {n:02d}", INK_SOFT)
        imgs.append(img)
    return imgs


# ------------------------------------------------------------------ 6. Dial diagrams
def dial(d, cx, cy, r, pointer_deg=None, label=None, ticks=24, ring=STEEL, sub=None):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ring, width=6)
    for t in range(ticks):
        a = math.radians(-90 + t * 360 / ticks)
        big = t % 6 == 0
        r0 = r - (34 if big else 20)
        d.line([(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + (r - 8) * math.cos(a), cy + (r - 8) * math.sin(a))],
               fill=(ring if big else BORDER), width=(6 if big else 4))
    inner = r * 0.62
    d.ellipse([cx - inner, cy - inner, cx + inner, cy + inner], fill=PANEL, outline=BORDER, width=3)
    if pointer_deg is not None:
        a = math.radians(-90 + pointer_deg)
        if label:
            d.line([(cx + (inner + 6) * math.cos(a), cy + (inner + 6) * math.sin(a)),
                    (cx + (r - 44) * math.cos(a), cy + (r - 44) * math.sin(a))], fill=BLUE, width=14)
        else:
            d.line([(cx, cy), (cx + (r - 48) * math.cos(a), cy + (r - 48) * math.sin(a))], fill=BLUE, width=12)
            d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=BLUE)
    if label:
        d.text((cx, cy - (30 if sub else 0)), label, font=F(DISPLAY_UP, int(r * 0.26)), fill=WHITE, anchor="mm")
    if sub:
        sf = F(MED, int(r * 0.11))
        words = sub.split()
        if sf.getlength(sub) > inner * 1.7 and len(words) > 1:
            mid = len(words) // 2
            d.text((cx, cy + 24), " ".join(words[:mid]), font=sf, fill=STEEL, anchor="mm")
            d.text((cx, cy + 24 + int(r * 0.13)), " ".join(words[mid:]), font=sf, fill=STEEL, anchor="mm")
        else:
            d.text((cx, cy + 30), sub, font=sf, fill=STEEL, anchor="mm")


def arc_arrow(d, cx, cy, r, start, end, color=BLUE, width=8):
    d.arc([cx - r, cy - r, cx + r, cy + r], start=start, end=end, fill=color, width=width)
    a = math.radians(end)
    tip = (cx + r * math.cos(a), cy + r * math.sin(a))
    # arrow head tangent
    tx, ty = -math.sin(a), math.cos(a)
    nx, ny = math.cos(a), math.sin(a)
    p1 = (tip[0] - tx * 26 + nx * 16, tip[1] - ty * 26 + ny * 16)
    p2 = (tip[0] - tx * 26 - nx * 16, tip[1] - ty * 26 - ny * 16)
    d.polygon([tip, p1, p2], fill=color)


def post6(post):
    imgs = []
    n = len(post["slides"])
    names = post.get("dials") or ["FORK\nCOMP", "FORK\nREB", "SHOCK\nLSC", "SHOCK\nHSC", "SHOCK\nREB"]
    for i, s in enumerate(post["slides"], 1):
        img, d = canvas(CARBON)
        brand(d, "dark")
        if s["type"] == "cover":
            # row of five small dials
            for k in range(5):
                cx = 150 + k * 195
                dial(d, cx, 330, 76, pointer_deg=[40, 120, 200, 300, 250][k], ticks=12)
                d.text((cx, 440), names[k].replace("\n", " "), font=F(SEMI, 22), fill=STEEL, anchor="mm")
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 520, 140, 100, 0.95)
            draw_block(d, M, 540, lines, font, size, 0.95, WHITE)
            x = tracked(d, M, H - 120, "SWIPE", F(SEMI, 26), BLUE, 3)
            chevrons(d, x + 10, H - 106, n=2, size=12, width=4)
        elif s["type"] == "point" and s.get("tag") != "NOT A CLICKER":
            tag = s["tag"]
            lab = tag.replace("  ·  ", "\n")
            cx, cy, r = W // 2, 400, 215
            dial(d, cx, cy, r, pointer_deg=[0, 60, 250, 310, 200, 150][i % 6], label=lab.split("\n")[0], sub=lab.split("\n")[1].title())
            arc_arrow(d, cx, cy, r + 46, -80, -10)
            d.text((cx + r + 10, cy - r - 30), "IN", font=F(DISPLAY_UP, 34), fill=BLUE, anchor="la")
            arc_arrow(d, cx, cy, r + 46, -100, -170, color=STEEL)
            d.text((cx - r - 10, cy - r - 30), "OUT", font=F(DISPLAY_UP, 34), fill=STEEL, anchor="ra")
            y = cy + r + 90
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 220, 84, 60, 0.96)
            y = draw_block(d, M, y, lines, font, size, 0.96, WHITE)
            y += 26
            bf = F(BODY_F, 34)
            draw_block(d, M, y, wrap(s["body"], bf, W - 2 * M), bf, 34, 1.42, BODY)
            d.text((M, H - 106), "In = clockwise = more damping", font=F(MED, 26), fill=STEEL, anchor="la")
        elif s["type"] == "point":
            # sag ruler
            rx, top, bot = 200, 220, 780
            d.rectangle([rx, top, rx + 14, bot], fill=STEEL)
            for k in range(0, 561, 20):
                big = k % 100 == 0
                d.line([(rx + 14, top + k), (rx + 14 + (48 if big else 24), top + k)], fill=(WHITE if big else BORDER), width=(4 if big else 3))
            # bracket showing 105 mm
            by0, by1 = top + 40, top + 40 + 420
            d.line([(rx + 110, by0), (rx + 110, by1)], fill=BLUE, width=8)
            d.line([(rx + 90, by0), (rx + 130, by0)], fill=BLUE, width=8)
            d.line([(rx + 90, by1), (rx + 130, by1)], fill=BLUE, width=8)
            d.text((rx + 170, (by0 + by1) // 2 - 40), "105", font=F(DISPLAY, 190), fill=WHITE, anchor="lm")
            d.text((rx + 170 + F(DISPLAY, 190).getlength("105") + 16, (by0 + by1) // 2 + 20), "mm", font=F(DISPLAY_UP, 60), fill=BLUE, anchor="lm")
            d.text((rx + 170, (by0 + by1) // 2 + 100), "riding sag, 2026 250 SX-F manual", font=F(MED, 28), fill=STEEL, anchor="lm")
            tracked(d, M, 860, "NOT A CLICKER", F(SEMI, 28), BLUE, 5)
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 130, 90, 70, 0.96)
            y = draw_block(d, M, 910, lines, font, size, 0.96, WHITE)
            y += 20
            bf = F(BODY_F, 32)
            draw_block(d, M, y, wrap(s["body"], bf, W - 2 * M), bf, 32, 1.42, BODY)
        else:
            dial(d, W - 200, 300, 150, pointer_deg=35, ticks=12)
            font, lines, size = fit(s["head"], DISPLAY, W - 2 * M, 380, 110, 80, 0.96)
            y = draw_block(d, M, 470, lines, font, size, 0.96, WHITE)
            y += 40
            sf = F(MED, 40)
            y = draw_block(d, M, y, wrap(s["sub"], sf, W - 2 * M), sf, 40, 1.4, BODY)
            y += 64
            pf = F(DISPLAY_UP, 40)
            label = "GET THE APP  ·  LINK IN BIO"
            pw = int(pf.getlength(label)) + 96
            d.rounded_rectangle([M, y, M + pw, y + 92], radius=46, fill=BLUE)
            d.text((M + 48, y + 46), label, font=pf, fill=WHITE, anchor="lm")
            d.text((M, H - 106), s["footer"], font=F(MED, 26), fill=STEEL, anchor="la")
        counter(d, f"{i:02d} / {n:02d}", STEEL)
        imgs.append(img)
    return imgs


# ------------------------------------------------------------------ 7. Real app screenshots
FRAMES = [
    ("RIDE IT.", "THEN TUNE IT.", "Run a moto. Log how it felt. Make one change.", 1),
    ("TELL IT WHAT", "THE BIKE DID.", "Front pushes, rear kicks, harsh on small bumps. Just tap it.", 2),
    ("BETTER", "CLICK BY CLICK.", "Which clicker, how many clicks and which way to turn it.", 3),
    ("CLOSER", "EVERY MOTO.", "Every change you turned, tracked until your bike is dialed.", 4),
    ("MULTIPLE SETUPS.", "ONE BIKE.", "Hardpack, singletrack, home track. Each one saved.", 5),
    ("EVERY BIKE", "IN YOUR GARAGE.", "Each bike keeps its own setups and its own progress.", 6),
]


def phone(idx):
    im = Image.open(os.path.join(SHOTS, f"{idx:02d}_dialed_play_1080x1920.png")).convert("RGB")
    return im.crop((225, 500, 925, 1920))


def post7(post):
    imgs = []
    frames = post.get("frames") or FRAMES
    n = len(frames) + 2
    # cover
    img, d = canvas(CARBON)
    brand(d, "dark")
    ph = phone(6).resize((470, int(470 * 1420 / 700)))
    img.paste(ph, (W - 470 - 40, 540))
    big = mark("dark", 230)
    img.paste(big, (M - 10, 180), big)
    d = ImageDraw.Draw(img)
    d.text((M, 420), "DIALED", font=F(DISPLAY, 120), fill=WHITE, anchor="la")
    d.text((M, 530), "OFFROAD", font=F(DISPLAY, 120), fill=BLUE, anchor="la")
    d.text((M, 640), post.get("big", "3.0"), font=F(DISPLAY, 260), fill=WHITE, anchor="la")
    sticker(img, post.get("sticker", "OUT NOW"), 210, 960, 5, BLUE, WHITE, size=40)
    sticker(img, "iOS AND ANDROID", 290, 1055, 5, WHITE, CARBON, size=34)
    d = ImageDraw.Draw(img)
    x = tracked(d, M, H - 120, "SWIPE", F(SEMI, 26), BLUE, 3)
    chevrons(d, x + 10, H - 106, n=2, size=12, width=4)
    counter(d, f"01 / {n:02d}", STEEL)
    imgs.append(img)
    for k, (l1, l2, sub, idx) in enumerate(frames, 2):
        img, d = canvas(CARBON)
        brand(d, "dark")
        d.text((M, 190), l1, font=F(DISPLAY, 112), fill=WHITE, anchor="la")
        d.text((M, 300), l2, font=F(DISPLAY, 112), fill=BLUE, anchor="la")
        sf = F(MED, 34)
        draw_block(d, M, 440, wrap(sub, sf, W - 2 * M), sf, 34, 1.4, BODY)
        ph = phone(idx).resize((700, 1420))
        img.paste(ph, ((W - 700) // 2, 560))
        d = ImageDraw.Draw(img)
        # fade the bottom edge into the footer band
        d.rectangle([0, H - 150, W, H], fill=CARBON)
        d.text((M, H - 106), "@dialed_offroad", font=F(MED, 26), fill=STEEL, anchor="la")
        counter(d, f"{k:02d} / {n:02d}", STEEL)
        imgs.append(img)
    # closer
    img, d = canvas(CARBON)
    brand(d, "dark")
    d.text((M, 300), "FREE TO START.", font=F(DISPLAY, 150), fill=WHITE, anchor="la")
    sf = F(MED, 40)
    y = draw_block(d, M, 470, wrap("Build your first tune free. Pro unlocks the full refine loop, setup history and more bikes.", sf, W - 2 * M), sf, 40, 1.4, BODY)
    y += 70
    pf = F(DISPLAY_UP, 40)
    x = M
    for label in ["APP STORE", "GOOGLE PLAY"]:
        pw = int(pf.getlength(label)) + 96
        d.rounded_rectangle([x, y, x + pw, y + 92], radius=46, fill=BLUE)
        d.text((x + pw // 2, y + 46), label, font=pf, fill=WHITE, anchor="mm")
        x += pw + 24
    d.text((M, y + 130), "Link in bio.", font=F(MED, 34), fill=STEEL, anchor="la")
    d.text((M, H - 106), post.get("footer", "Dialed Offroad 3.0"), font=F(MED, 26), fill=STEEL, anchor="la")
    counter(d, f"{n:02d} / {n:02d}", STEEL)
    imgs.append(img)
    return imgs


RENDERERS = [post1, post2, post3, post4, post5, post6, post7]

import render as _classic
def classic(post):
    """The generic dark design from render.py: any mix of hot, cover, point, symptom, table, points, closer slides."""
    fns = {"hot": _classic.slide_hot, "cover": _classic.slide_cover, "point": _classic.slide_point, "symptom": _classic.slide_symptom,
           "table": _classic.slide_table, "points": _classic.slide_points, "closer": _classic.slide_closer}
    n = len(post["slides"])
    return [fns[s["type"]](s, f"{i}/{n}" if n > 1 else "") for i, s in enumerate(post["slides"], 1)]

# design name -> renderer. Each week's posts name their design; the look should vary across the week.
DESIGNS = {
    "glow": post1,        # one slide: carbon with a blue glow, a hot take in big type (slide types: hot)
    "sheet": post2,       # setup sheet: blue header, six value tiles, then the stock vs Dialed table, points, closer (cover, table, points, closer)
    "blue_list": post3,   # all-blue carousel with stickers, numbered points (cover, point..., closer)
    "split": post4,       # one slide: diagonal STOCK / YOU split (hot) with post["split"] labels
    "paper_list": post5,  # light paper carousel with flow boxes, symptom -> fix (cover, symptom..., closer)
    "dials": post6,       # carbon carousel with drawn clicker dials (cover, point with tag..., closer)
    "screens": post7,     # app screens carousel from tools/shots (post["frames"], big, sticker, footer)
    "classic": classic,   # the generic dark design, any slide types
}


def preview(imgs, path, per_row=4):
    tw, th = 405, 506
    rows = (len(imgs) + per_row - 1) // per_row
    cols = min(per_row, len(imgs))
    sheet = Image.new("RGB", (cols * (tw + 16) + 16, rows * (th + 16) + 16), (34, 36, 42))
    for i, im in enumerate(imgs):
        r, c = divmod(i, per_row)
        sheet.paste(im.resize((tw, th)), (16 + c * (tw + 16), 16 + r * (th + 16)))
    sheet.save(path)


def load_week(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("week", path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod.WEEK


def render_post(post):
    fn = DESIGNS[post.get("design", "classic")]
    return fn(post)


def main():
    week_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "weeks", "2026-10-26.py")
    out = sys.argv[2] if len(sys.argv) > 2 else OUT
    os.makedirs(out, exist_ok=True)
    total = 0
    for post in load_week(week_path):
        fn = DESIGNS[post.get("design", "classic")]
        folder = os.path.join(out, post.get("slug") or post["folder"])
        os.makedirs(folder, exist_ok=True)
        imgs = fn(post)
        for i, im in enumerate(imgs, 1):
            im.save(os.path.join(folder, f"slide_{i:02d}.png"), optimize=True)
        preview(imgs, os.path.join(out, f"preview_{post.get('slug') or post['folder']}.png"))
        total += len(imgs)
        print(post.get("slug") or post["folder"], len(imgs))
    print(total, "slides")


if __name__ == "__main__":
    main()
