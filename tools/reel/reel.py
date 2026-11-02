#!/usr/bin/env python3
"""Animated settings-card reel: 2024 Kawasaki KX250, 1080x1920, 30 fps.
Usage: kx250_reel.py frames <t1,t2,...> | render <out.mp4>"""
import math, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = "/home/claude/dialed-social/tools"
W, H, FPS = 1080, 1920, 30
CARBON = (11, 12, 16); PANEL = (21, 25, 32); BORDER = (38, 43, 54)
BLUE = (29, 155, 240); WHITE = (245, 247, 252); STEEL = (138, 147, 166); BODY = (201, 207, 218)
M = 84

_f = {}
def F(name, size):
    k = (name, size)
    if k not in _f:
        _f[k] = ImageFont.truetype(f"{ROOT}/fonts/{name}.ttf", size)
    return _f[k]
DISP, DISPI, BOLD, SEMI, MED = "BarlowCondensed-Black", "BarlowCondensed-BlackItalic", "Inter-Bold", "Inter-SemiBold", "Inter-Medium"

MARK = Image.open(f"{ROOT}/logo/mark_white.png").convert("RGBA")
def mark(h):
    w = round(MARK.width * h / MARK.height)
    return MARK.resize((w, h), Image.LANCZOS)

import json, os
CFG = json.load(open(os.environ["REEL_CFG"]))
ROWS = [tuple(r) for r in CFG["rows"]]

# timeline (seconds)
T_HOOK_END = 2.4
T_ROWS0 = 2.6        # first row lands
ROW_GAP = 0.95       # next row
FLIP_DELAY = 0.45    # stock -> dialed flip after a row lands
T_SAG = T_ROWS0 + ROW_GAP * len(ROWS) + 0.5   # ~7.85
T_CLOSE = T_SAG + 2.3                          # ~10.15
DUR = T_CLOSE + 3.2                            # ~13.35
FLIPS = [T_ROWS0 + i * ROW_GAP + FLIP_DELAY for i, r in enumerate(ROWS) if r[3]]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def mix(c1, c2, a): return tuple(round(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))

# static background with a soft blue glow, built once
def make_bg():
    bg = Image.new("RGB", (W, H), CARBON)
    glow = Image.new("RGB", (W, H), CARBON)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.15, -H * 0.12, W * 1.25, H * 0.42], fill=(18, 62, 104))
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    return Image.blend(bg, glow, 0.9)
BG = make_bg()

def tracked(d, x, y, text, font, fill, track=3, anchor_right=False):
    widths = [d.textlength(ch, font=font) + track for ch in text]
    total = sum(widths) - track
    if anchor_right: x -= total
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill)
        x += w
    return total

def fade_layer(base, layer, alpha):
    if alpha <= 0: return base
    if alpha >= 1: return layer
    return Image.blend(base, layer, alpha)

def header(img, d, a):
    # brand row
    m = mark(54)
    lay = img.copy()
    lay.paste(m, (M, 120), m)
    ld = ImageDraw.Draw(lay)
    ld.text((M + m.width + 18, 124), "DIALED", font=F(DISP, 50), fill=WHITE)
    ld.text((M + m.width + 18 + ld.textlength("DIALED ", font=F(DISP, 50)), 124), "OFFROAD", font=F(DISP, 50), fill=BLUE)
    return fade_layer(img, lay, a)

def scene_hook(t, img):
    d = ImageDraw.Draw(img)
    a1 = ease((t - 0.1) / 0.45)
    a2 = ease((t - 0.7) / 0.45)
    a3 = ease((t - 1.3) / 0.45)
    y = 640
    lay = img.copy(); ld = ImageDraw.Draw(lay)
    off = round((1 - a1) * 60)
    ld.text((M, y + off), "STOCK ISN'T", font=F(DISPI, 190), fill=WHITE)
    img = fade_layer(img, lay, a1)
    lay = img.copy(); ld = ImageDraw.Draw(lay)
    off = round((1 - a2) * 60)
    ld.text((M, y + 190 + off), "SET UP FOR YOU.", font=F(DISPI, 150), fill=BLUE)
    img = fade_layer(img, lay, a2)
    lay = img.copy(); ld = ImageDraw.Draw(lay)
    ld.text((M, y + 420), CFG["hook_sub"], font=F(SEMI, 46), fill=BODY)
    img = fade_layer(img, lay, a3)
    return img

def bike_title(img, a):
    lay = img.copy(); d = ImageDraw.Draw(lay)
    d.text((M, 250), CFG["title"], font=F(DISP, 112), fill=WHITE)
    tracked(d, M + 4, 385, CFG["sub"], F(SEMI, 30), STEEL, 2)
    # column heads
    tracked(d, 620, 478, "STOCK", F(SEMI, 26), STEEL, 3)
    tracked(d, 820, 478, "DIALED", F(SEMI, 26), BLUE, 3)
    return fade_layer(img, lay, a)

def row(img, i, t):
    label, stock, dialed, chip = ROWS[i][:4]
    note = ROWS[i][4] if len(ROWS[i]) > 4 else None
    big = lambda v: " " not in v
    t0 = T_ROWS0 + i * ROW_GAP
    a = ease((t - t0) / 0.35)
    if a <= 0: return img
    y = 530 + i * 196 + round((1 - a) * 40)
    lay = img.copy(); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([M, y, W - M, y + 172], radius=26, fill=PANEL, outline=BORDER, width=2)
    tracked(d, M + 32, y + 26, label, F(SEMI, 26), STEEL, 3)
    flip = ease((t - t0 - FLIP_DELAY) / 0.3) if chip else 0
    # stock value, dims once flipped
    sc = mix(WHITE, (90, 98, 115), flip)
    if " " in stock:
        d.text((620, y + 80), stock, font=F(DISP, 62), fill=sc)
    else:
        d.text((620, y + 58), stock, font=F(DISP, 96), fill=sc)
    if chip and flip > 0:
        sw = d.textlength(stock, font=F(DISP, 96 if big(stock) else 62))
        d.line([616, y + 112, 616 + (sw + 8) * flip, y + 112], fill=(90, 98, 115), width=6)
    # dialed value pops on flip
    if chip:
        if flip > 0:
            s = 1 + 0.25 * math.sin(math.pi * clamp((t - t0 - FLIP_DELAY) / 0.3))
            bs = 96 if big(dialed) else 62
            fnt = F(DISP, round(bs * s))
            d.text((820, (y + 58 if big(dialed) else y + 80) + round(bs * (1 - s) / 2)), dialed, font=fnt, fill=BLUE)
            ca = ease((t - t0 - FLIP_DELAY - 0.15) / 0.3)
            if ca > 0:
                cf = F(BOLD, 24)
                cw = d.textlength(chip, font=cf) + 36
                cl = img.copy() if False else None
                d.rounded_rectangle([M + 32, y + 104, M + 32 + cw, y + 148], radius=22, fill=mix(PANEL, BLUE, ca))
                d.text((M + 50, y + 113), chip, font=cf, fill=mix(PANEL, CARBON, ca))
    else:
        vf = F(DISP, 96 if " " not in dialed else 62)
        vy = y + 58 if " " not in dialed else y + 80
        d.text((820, vy), dialed, font=vf, fill=WHITE)
        d.text((M + 32, y + 112), note or ("stays stock" + ("  ·  turns" if " " in dialed else "")), font=F(MED, 26), fill=STEEL)
    return fade_layer(img, lay, a)

def sag(img, t):
    a = ease((t - T_SAG) / 0.4)
    if a <= 0: return img
    y = 530 + 5 * 196 + 10 + round((1 - a) * 40)
    lay = img.copy(); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([M, y, W - M, y + 230], radius=26, fill=BLUE)
    tracked(d, M + 36, y + 30, "RIDING SAG, SET THIS FIRST", F(BOLD, 26), CARBON, 3)
    d.text((M + 32, y + 64), CFG["sag"], font=F(DISP, 140), fill=WHITE)
    d.text((M + 470, y + 104), "Not a clicker.", font=F(SEMI, 34), fill=CARBON)
    d.text((M + 470, y + 146), "Measure yours first.", font=F(SEMI, 34), fill=CARBON)
    return fade_layer(img, lay, a)

def closer(img, t):
    a = ease((t - T_CLOSE) / 0.45)
    if a <= 0: return img
    lay = BG.copy(); d = ImageDraw.Draw(lay)
    d.text((M, 560), "STARTING", font=F(DISPI, 190), fill=WHITE)
    d.text((M, 750), "POINTS.", font=F(DISPI, 190), fill=BLUE)
    d.text((M, 1000), "Ride it. Log how it felt.", font=F(SEMI, 50), fill=BODY)
    d.text((M, 1070), "Move one thing at a time.", font=F(SEMI, 50), fill=BODY)
    b = ease((t - T_CLOSE - 0.8) / 0.45)
    m = mark(110)
    if b > 0:
        l2 = lay.copy(); d2 = ImageDraw.Draw(l2)
        l2.paste(m, (M, 1340), m)
        d2.text((M + m.width + 28, 1342), "DIALED OFFROAD", font=F(DISP, 80), fill=WHITE)
        d2.text((M + m.width + 28, 1430), "Your bike's baseline in the app", font=F(MED, 34), fill=STEEL)
        lay = fade_layer(lay, l2, b)
    return fade_layer(img, lay, a)

def frame(t):
    img = BG.copy()
    img = header(img, None, ease(t / 0.4))
    if t < T_HOOK_END + 0.35:
        hk = scene_hook(t, BG.copy())
        hk = header(hk, None, ease(t / 0.4))
        out_a = ease((t - T_HOOK_END) / 0.35)
        img = hk if out_a <= 0 else img
        if out_a > 0:
            card = header(BG.copy(), None, 1)
            card = bike_title(card, out_a)
            img = Image.blend(hk, card, out_a)
            return img
        return img
    img = bike_title(img, 1)
    for i in range(len(ROWS)):
        img = row(img, i, t)
    img = sag(img, t)
    img = closer(img, t)
    return img

def main():
    if sys.argv[1] == "frames":
        for s in sys.argv[2].split(","):
            frame(float(s)).save(f"{os.environ.get('REEL_OUT','.')}/f_{s}.jpg", quality=90)
        return
    out = sys.argv[2]
    n = round(DUR * FPS)
    tmp = out[:-4] + ".part.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
    for k in range(n):
        p.stdin.write(frame(k / FPS).tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, out)
    print("dur", DUR, "flips", [round(f + 0.0, 2) for f in FLIPS])

if __name__ == "__main__":
    main()
