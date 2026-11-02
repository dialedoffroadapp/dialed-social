"""Template "xray": an X-ray fork cutaway. Oil through the piston, spring, travel meter, one idea per beat.

spec keys: hook (2 or 3 lines, last one blue), beats (list of {tag, color, body, motion, dur?, labels?, stamp?}),
app ({chip, part, from, to, how}), end ({head: [2 lines], sub: [lines]}).
motion is one of MOTIONS below. color is a name in COLORS.
"""
from lib import *
import app

COLORS = {"blue": BLUE, "red": RED, "orange": ORANGE, "green": GREEN, "cyan": (120, 220, 255), "yellow": YELLOW}
HOOK_DUR = 2.4
# keyframes (seconds from the beat start, normalized travel 0..1[, "lin"]), optional shake times and stamp time
MOTIONS = {
    "hook_land": dict(keys=[(0.0, 0.40), (0.30, 0.86), (1.2, 0.30), (2.4, 0.28)], dur=2.4, thump=[0.0]),
    "land_slow": dict(keys=[(0.0, 0.28), (0.4, 0.05), (2.0, 0.75), (2.8, 0.70), (3.6, 0.30)], dur=3.6, thump=[1.9]),
    "slam": dict(keys=[(0.0, 0.30), (0.5, 0.05), (0.85, 1.0, "lin"), (1.6, 1.0), (2.6, 0.25), (3.0, 0.22)], dur=3.0, slam=0.85),
    "harsh": dict(keys=[(0.0, 0.22), (0.3, 0.05), (0.45, 0.27, "lin"), (0.6, 0.08), (0.8, 0.29, "lin"), (0.95, 0.08), (1.15, 0.26, "lin"),
                        (1.3, 0.07), (1.55, 0.28, "lin"), (1.7, 0.09), (1.95, 0.25, "lin"), (2.1, 0.1), (3.0, 0.3)],
                  dur=3.0, shake=[0.45, 0.8, 1.15, 1.55, 1.95]),
    "rebound": dict(keys=[(0.0, 0.3), (0.5, 0.8), (0.8, 0.8), (2.6, 0.12), (3.0, 0.15)], dur=3.0),
    "rebound_fast": dict(keys=[(0.0, 0.3), (0.4, 0.8), (0.6, 0.8), (0.85, 0.0, "lin"), (1.0, 0.12), (1.15, 0.0), (1.6, 0.25), (2.0, 0.8),
                                (2.2, 0.8), (2.45, 0.0, "lin"), (2.6, 0.1), (3.0, 0.15)], dur=3.0, shake=[0.85, 2.45]),
    "pack": dict(keys=[(0.0, 0.3), (0.3, 0.55), (0.6, 0.46), (0.9, 0.7), (1.2, 0.63), (1.5, 0.83), (1.8, 0.77), (2.1, 0.93),
                       (2.6, 0.9), (3.0, 0.6)], dur=3.0, shake=[0.3, 0.9, 1.5, 2.1]),
    "dive": dict(keys=[(0.0, 0.25), (0.3, 0.2), (1.6, 0.9), (2.4, 0.88), (3.0, 0.4)], dur=3.0, thump=[1.5]),
    "dialed": dict(keys=[(0.0, 0.15), (0.15, 0.05), (0.75, 0.72), (1.6, 0.42), (2.4, 0.32), (3.4, 0.32)], dur=3.4, ding=0.9),
    "chop_dialed": dict(keys=[(0.0, 0.3)] + [(0.2 + k * 0.28, 0.3 + (0.12 if k % 2 == 0 else -0.02)) for k in range(11)] + [(3.4, 0.3)],
                        dur=3.4, ding=0.9),
}

TRAVEL_PX, CX, FY = 300, 540, 40
CROP = (330, 560 + FY, 750, 1800 + FY)

def make(spec):
    beats = [dict(b) for b in spec["beats"]]
    t = HOOK_DUR
    keys = list(MOTIONS["hook_land"]["keys"])
    shakes, slams, thumps, dings, starts = [], [], [0.0], [], []
    for b in beats:
        mo = MOTIONS[b["motion"]]
        b["t0"] = t; b["dur"] = b.get("dur", mo["dur"]); starts.append(t)
        for k in mo["keys"]:
            if k[0] <= b["dur"]:
                keys.append((t + k[0], k[1]) + tuple(k[2:]))
        shakes += [t + s for s in mo.get("shake", [])]
        if "slam" in mo: slams.append(t + mo["slam"])
        thumps += [t + s for s in mo.get("thump", [])]
        if "ding" in mo: dings.append(t + mo["ding"])
        t += b["dur"]
    keys.sort(key=lambda k: k[0])
    t_app = t
    t_end = t_app + app.APP_LEN - 0.2
    dur = t_end + 3.4
    a = spec["app"]; e = spec["end"]

    def comp(tt): return keys_at(tt, keys)
    def speed(tt): return (comp(tt + 0.02) - comp(tt - 0.02)) / 0.04

    def fork_layer(tt, flash_red):
        c = comp(tt); v = speed(tt); cp = c * TRAVEL_PX
        ox, oy = CROP[0], CROP[1]
        L = Image.new("RGBA", (CROP[2] - CROP[0], CROP[3] - CROP[1]), (0, 0, 0, 0))
        d = ImageDraw.Draw(L, "RGBA")
        def R(x0, y0, x1, y1, **k): d.rounded_rectangle([x0 - ox, y0 - oy, x1 - ox, y1 - oy], **k)
        Y = lambda y: y + FY
        lt, lb = Y(1080) - cp, Y(1700) - cp
        R(455, lt, 625, lb, radius=18, fill=(70, 55, 20, 120), outline=(214, 170, 80, 255), width=4)
        R(430, lb - 60, 650, lb + 50, radius=22, fill=(40, 44, 55, 230), outline=(160, 168, 186, 255), width=4)
        d.ellipse([CX - 34 - ox, lb - 38 - oy, CX + 34 - ox, lb + 30 - oy], outline=(160, 168, 186, 255), width=5)
        R(418, Y(640), 662, Y(1250), radius=20, fill=(30, 36, 48, 120), outline=(150, 160, 180, 255), width=5)
        R(436, Y(606), 644, Y(650), radius=10, fill=(110, 118, 136, 255))
        top, bot = Y(1300), lb - 70
        pts = [((488 if i % 2 else 592) - ox, top + (bot - top) * i / 18 - oy) for i in range(19)]
        d.line(pts, fill=mix((150, 160, 180), RED, flash_red) + (255,), width=7, joint="curve")
        R(503, Y(690), 577, Y(1300), radius=10, fill=(29, 155, 240, 70), outline=(120, 180, 240, 255), width=3)
        py = Y(1240) - cp
        R(533, py, 547, lb - 64, radius=6, fill=(205, 212, 225, 255))
        heat = clamp(abs(v) / 4.0)
        flow_col = mix(BLUE, ORANGE, heat) if v >= 0 else mix(BLUE, (120, 220, 255), 0.5)
        flex = clamp(abs(v) / 3.0) * 9 * (1 if v >= 0 else -1)
        for k in range(4):
            sy = py - 18 - k * 6 if v >= 0 else py + 18 + k * 6
            w = 30 - k * 5
            d.line([(CX - w - ox, sy + flex - oy), (CX - ox, sy - oy), (CX + w - ox, sy + flex - oy)], fill=(230, 235, 245, 255), width=3)
        R(507, py - 13, 573, py + 13, radius=6, fill=(245, 247, 252, 255))
        if abs(v) > 0.05:
            al = clamp(abs(v) / 1.2); phase = -c * 900
            for col_x in (520, 560):
                for j in range(14):
                    rel = ((j * 31 + phase + (0 if col_x == 520 else 15)) % 260) - 130
                    y = py + rel
                    if Y(700) < y < Y(1295):
                        r = 9 if abs(rel) < 24 else 6
                        d.ellipse([col_x - r - ox, y - r - oy, col_x + r - ox, y + r - oy], fill=flow_col + (round(255 * al),))
        for j in range(10):
            y = Y(700) + ((j * 59 + tt * 18) % 590); x = 512 + (j * 23) % 54
            d.ellipse([x - 2 - ox, y - 2 - oy, x + 2 - ox, y + 2 - oy], fill=(180, 220, 255, 90))
        return L, c

    def frame(tt):
        img = bg("grid")
        flash = 0.0
        for s in slams:
            if s <= tt < s + 0.85: flash = max(flash, 1 - ease((tt - s) / 0.85))
        if tt < t_app + 0.6:
            L, c = fork_layer(tt, flash)
            sx, sy = 0, 0
            for s in slams: a_, b_ = shake(tt, s, 0.45, 22); sx += a_; sy += b_
            for s in shakes: a_, b_ = shake(tt, s, 0.22, 10); sx += a_; sy += b_
            glow = L.filter(ImageFilter.GaussianBlur(14))
            img.paste(glow, (CROP[0] + sx, CROP[1] + sy), glow)
            img.paste(L, (CROP[0] + sx, CROP[1] + sy), L)
            d = draw(img)
            if flash > 0: d.rectangle([0, 0, W, H], fill=rgba(RED, 0.18 * flash))
            ma = ease(tt / 0.3) * (1 - ease((tt - t_app) / 0.3))
            x0, y0, y1 = 130, 820 + FY, 1520 + FY
            tracked(d, x0 - 26, y0 - 70, "TRAVEL", F(BOLD, 24), STEEL, ma, 3)
            d.rounded_rectangle([x0, y0, x0 + 34, y1], radius=17, outline=rgba(BORDER, ma), width=3, fill=rgba(PANEL, ma))
            fh = (y1 - y0) * c
            col = RED if c > 0.95 else (ORANGE if c > 0.82 else BLUE)
            if fh > 4: d.rounded_rectangle([x0 + 5, y1 - 5 - max(24, fh - 10), x0 + 29, y1 - 5], radius=12, fill=rgba(col, ma))
            text(d, (x0 + 17, y1 + 24), f"{round(c * 310)}", F(DISP, 62), col if c > 0.82 else WHITE, ma, anchor="ma")
            text(d, (x0 + 17, y1 + 88), "MM", F(BOLD, 22), STEEL, ma, anchor="ma")
            # captions
            if tt < HOOK_DUR + 0.1:
                ha = 1 - ease((tt - 2.2) / 0.3)
                pop = 1 + 0.08 * (1 - ease(tt / 0.25))
                lines = spec["hook"]
                sz = 122
                while max(d.textlength(l, font=F(DISPI, sz)) for l in lines) > W - 2 * M: sz -= 4
                for i, l in enumerate(lines):
                    text(d, (M, 250 + i * sz * 0.97), l, F(DISPI, sz * pop), BLUE if i == len(lines) - 1 else WHITE, ha)
            for b in beats:
                caption(d, tt, b["t0"] + 0.05, b["t0"] + b["dur"], b["tag"], COLORS[b["color"]], b["body"])
                if b.get("labels"):
                    la = win(tt, b["t0"] + 0.5, b["t0"] + b["dur"] - 0.1, 0.35, 0.3)
                    if la > 0:
                        cp = c * TRAVEL_PX
                        for i, (lbl, ty) in enumerate([("OIL", 820 + FY), ("PISTON + SHIMS", 1240 + FY - cp), ("SPRING", 1440 + FY - cp * 0.5)]):
                            aa = la * ease((tt - b["t0"] - 0.5 - i * 0.18) / 0.3)
                            d.line([(600, ty), (700, ty)], fill=rgba(STEEL, aa), width=3)
                            d.ellipse([594, ty - 6, 606, ty + 6], fill=rgba(WHITE, aa))
                            tracked(d, 712, ty - 16, lbl, F(BOLD, 28), WHITE, aa, 2)
                if b.get("stamp"):
                    st = b["t0"] + MOTIONS[b["motion"]].get("slam", 0.9)
                    ba = win(tt, st, b["t0"] + b["dur"] - 0.2, 0.12, 0.3)
                    if ba > 0:
                        s = 1 + 0.3 * (1 - ease((tt - st) / 0.25))
                        ssz = 140
                        while d.textlength(b["stamp"], font=F(DISPI, ssz)) > 700: ssz -= 4
                        text(d, (600, 1500 + FY), b["stamp"], F(DISPI, ssz * s), COLORS[b["color"]], ba, anchor="mm")
        img = app.segment(img, tt, t_app, a.get("chip"), (a["part"], a["from"], a["to"], a["how"]) if a.get("part") else None,
                          tuple(a["screens"]) if a.get("screens") else (2,), tuple(tuple(x) for x in a["lines"]) if a.get("lines") else None)
        return end_card(img, tt, t_end, head=tuple(e["head"]), sub=tuple(e["sub"]))

    def track():
        tr = Track(dur, 1)
        tr.pad((55, 82.4, 110, 164.8), 0.14, 1.0)
        tr.slam(0.0, 0.8)
        for s in starts: tr.whoosh(s - 0.05, 0.3)
        for s in thumps[1:]: tr.thump(s, 0.6)
        for s in slams: tr.slam(s, 1.0)
        for s in shakes: tr.click(s, 0.5, 1500)
        for s in dings: tr.ding(s, 880, 0.3)
        tr.whoosh(t_app - 0.05, 0.35); tr.thump(t_app + 0.1, 0.5)
        if a.get("chip"): tr.click(t_app + 1.1, 0.6, 2600)
        tr.ding(t_app + 2.4, 990, 0.25)
        tr.whoosh(t_end - 0.05, 0.35); tr.thump(t_end + 0.1, 0.7); tr.thump(t_end + 1.0, 0.5)
        return tr

    sheet = [0.05] + [b["t0"] + min(1.2, b["dur"] / 2) for b in beats] + [t_app + 1.4, t_app + 3.4, t_end + 1.6]
    return frame, dur, track, sheet

def keys_at(t, ks): return keys(t, ks)
