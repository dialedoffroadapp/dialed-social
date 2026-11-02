"""Template "pov": a POV hook, a setup sheet, comparison bars, a sag gauge, three red stamps, a punchline.

spec keys: hook [white, blue], stamp_word (green stamp over the sheet in the hook), sheet {title, rows [[label, value]], tag, body},
bars {tag, body, items [[label, number, unit, color]], max, big}, gauge {tag, body, value, lo, hi, target [lo, hi], label, unit, note},
feel_head, stamps [[line1, line2] x 3], punch [line1, line2, line3 (blue)], app {chip+part.. or screens+lines}, end {head, sub}.
"""
from lib import *
import app

DUR = 25.6
COLORS = {"blue": BLUE, "red": RED, "orange": ORANGE, "green": GREEN, "steel": STEEL, "yellow": YELLOW}
T_APP, T_END = 17.6, 22.2

def sheet(d, x, y, a, title, col, rows, hi=-1):
    w = W - 2 * x
    d.rounded_rectangle([x, y, x + w, y + 140 + 92 * len(rows)], radius=30, fill=rgba(PANEL, a), outline=rgba(col, a), width=3)
    tracked(d, x + 40, y + 40, title, F(BOLD, 30), col, a, 3)
    for i, (k, v) in enumerate(rows):
        yy = y + 110 + i * 92
        if i == hi: d.rounded_rectangle([x + 20, yy - 14, x + w - 20, yy + 64], radius=14, fill=rgba(YELLOW, a * 0.18))
        d.line([(x + 40, yy + 74), (x + w - 40, yy + 74)], fill=rgba(BORDER, a), width=2)
        text(d, (x + 40, yy + 4), k, F(SEMI, 36), STEEL, a)
        text(d, (x + w - 40, yy - 8), v, F(DISP, 62), WHITE, a, anchor="ra")

def gauge(d, cx, cy, r, val, a, lo=70, hi=125, tgt=(100, 110)):
    if a <= 0: return
    def ang(v): return 180 + 180 * (v - lo) / (hi - lo)
    d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=rgba(BORDER, a), width=34)
    d.arc([cx - r, cy - r, cx + r, cy + r], ang(tgt[0]), ang(tgt[1]), fill=rgba(GREEN, a), width=34)
    for v in range(lo, hi + 1, 5):
        th = math.radians(ang(v))
        r0 = r - 30 if v % 10 == 0 else r - 22
        d.line([(cx + math.cos(th) * (r + 22), cy + math.sin(th) * (r + 22)), (cx + math.cos(th) * (r + 22 + (18 if v % 10 == 0 else 9)), cy + math.sin(th) * (r + 22 + (18 if v % 10 == 0 else 9)))], fill=rgba(STEEL, a), width=3)
    th = math.radians(ang(val))
    d.line([(cx, cy), (cx + math.cos(th) * (r - 10), cy + math.sin(th) * (r - 10))], fill=rgba(WHITE, a), width=10)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=rgba(WHITE, a))
    th = math.radians(ang((tgt[0] + tgt[1]) / 2))
    text(d, (cx + math.cos(th) * (r + 70), cy + math.sin(th) * (r + 70)), "TARGET", F(BOLD, 26), GREEN, a, anchor="mm")

def make(spec):
    def frame(t):
        STAMPS = [(12.2 + 1.1 * k, l1, l2) for k, (l1, l2) in enumerate(spec["stamps"])]
        sh, ba, gg = spec["sheet"], spec["bars"], spec["gauge"]
        img = bg("glow")
        sx, sy = 0, 0
        for st, *_ in STAMPS:
            a_, b_ = shake(t, st, 0.3, 16); sx += a_; sy += b_
        d = draw(img)

        # ---- hook + setup sheet
        if t < 5.3:
            a = 1 - ease((t - 5.0) / 0.3)
            z = 1 + 0.04 * t
            if t < 2.5:
                pa = 1 - ease((t - 2.2) / 0.3)
                chip(d, M, 230, "POV", YELLOW, pa, size=34)
                pop = 1 + 0.08 * (1 - ease(t / 0.25))
                sz = 130
                while max(d.textlength(l, font=F(DISPI, sz)) for l in spec["hook"]) > W - 2 * M: sz -= 4
                text(d, (M, 310), spec["hook"][0], F(DISPI, sz * pop), WHITE, pa)
                text(d, (M, 310 + sz * 0.97), spec["hook"][1], F(DISPI, sz * pop), BLUE, pa)
            else:
                caption(d, t, 2.45, 5.3, sh["tag"], YELLOW, sh["body"])
            sy0 = 640 if t < 2.5 else 600
            sheet(d, M, sy0, a, sh["title"], YELLOW, [tuple(r) for r in sh["rows"]], hi=int((t - 2.6) / 0.4) if 2.6 <= t < 5.0 else -1)
            # COPIED stamp
            ca = win(t, 1.3, 2.4, 0.12, 0.25)
            if ca > 0:
                s = 1 + 0.4 * (1 - ease((t - 1.3) / 0.2))
                d.rounded_rectangle([W / 2 - 230 * s, 1060 - 70 * s, W / 2 + 230 * s, 1060 + 70 * s], radius=20, outline=rgba(GREEN, ca), width=8, fill=rgba(CARBON, 0.7 * ca))
                text(d, (W / 2, 1060), spec["stamp_word"], F(DISPI, 120 * s), GREEN, ca, anchor="mm")

        # ---- weight bars
        wa = win(t, 5.2, 8.7, 0.35, 0.3)
        if wa > 0:
            caption(d, t, 5.2, 8.7, ba["tag"], RED, ba["body"])
            for k, (lbl, lb, unit, cname) in enumerate(ba["items"]):
                col = COLORS[cname]
                y = 760 + k * 330
                g = ease((t - 5.5 - k * 0.35) / 0.8)
                text(d, (M, y), lbl, F(DISP, 70), col, wa)
                full = W - 2 * M
                d.rounded_rectangle([M, y + 90, M + full, y + 170], radius=40, fill=rgba(PANEL, wa))
                d.rounded_rectangle([M, y + 90, M + max(80, full * (lb / ba["max"]) * g), y + 170], radius=40, fill=rgba(col, wa))
                text(d, (M + full, y - 4), f"{round(lb * g)} {unit}", F(DISP, 80), WHITE, wa, anchor="ra")
            b = ease((t - 6.8) / 0.3) * wa
            text(d, (W / 2, 1520), ba["big"], F(DISPI, 170), RED, b, anchor="mm")

        # ---- sag gauge
        ga = win(t, 8.6, 12.2, 0.35, 0.3)
        if ga > 0:
            caption(d, t, 8.6, 12.2, gg["tag"], ORANGE, gg["body"])
            val = gg["lo"] + (gg["value"] - gg["lo"]) * ease((t - 9.0) / 0.9) + 2 * math.sin(t * 9) * (1 - ease((t - 9.9) / 0.6))
            gauge(d, W / 2, 1140, 330, val, ga, gg["lo"], gg["hi"], tuple(gg["target"]))
            text(d, (W / 2, 1210), f"{round(val)} {gg['unit']}", F(DISP, 130), WHITE, ga, anchor="ma")
            text(d, (W / 2, 1350), gg["label"], F(BOLD, 30), STEEL, ga, anchor="ma")
            b = ease((t - 10.3) / 0.3) * ga
            text(d, (W / 2, 1440), gg["note"], F(SEMI, 38), BODY, b, anchor="ma")

        # ---- stamps
        sa = win(t, 12.1, 15.6, 0.15, 0.3)
        if sa > 0:
            text(d, (M, 250), spec.get("feel_head", "WHAT YOU FEEL:"), F(DISPI, 110), WHITE, sa)
            for i, (st, l1, l2) in enumerate(STAMPS):
                a = ease((t - st) / 0.12) * sa
                if a <= 0: continue
                s = 1 + 0.35 * (1 - ease((t - st) / 0.18))
                y = 620 + i * 330
                rot_off = (-1) ** i * 12
                d.rounded_rectangle([M + sx - 10, y + sy - 20, W - M + sx + 10, y + 270 + sy], radius=26, fill=rgba(RED, a * 0.12), outline=rgba(RED, a), width=6)
                text(d, (W / 2 + sx + rot_off, y + 70 + sy), l1, F(DISPI, 96 * s), WHITE, a, anchor="mm")
                text(d, (W / 2 + sx - rot_off, y + 180 + sy), l2, F(DISPI, 96 * s), RED, a, anchor="mm")

        # ---- the line
        la = win(t, 15.5, 17.7, 0.25, 0.3)
        if la > 0:
            pop = 1 + 0.06 * (1 - ease((t - 15.5) / 0.25))
            p1, p2, p3 = spec["punch"]
            psz = 140
            while max(d.textlength(l, font=F(DISPI, psz)) for l in (p1, p2, p3)) > W - 2 * M: psz -= 4
            text(d, (W / 2, 820), p1, F(DISPI, psz * pop), WHITE, la, anchor="mm")
            text(d, (W / 2, 960), p2, F(DISPI, psz * pop), WHITE, la, anchor="mm")
            b = ease((t - 16.3) / 0.25) * la
            s = 1 + 0.15 * (1 - ease((t - 16.3) / 0.2))
            text(d, (W / 2, 1160), p3, F(DISPI, psz * 1.07 * s), BLUE, b, anchor="mm")
        a_ = spec["app"]
        img = app.segment(img, t, T_APP, a_.get("chip"), (a_["part"], a_["from"], a_["to"], a_["how"]) if a_.get("part") else None,
                          tuple(a_["screens"]) if a_.get("screens") else (2,), tuple(tuple(x) for x in a_["lines"]) if a_.get("lines") else None)
        return end_card(img, t, T_END, head=tuple(spec["end"]["head"]), sub=tuple(spec["end"]["sub"]))

    def track():
        tr = Track(DUR, 5)
        tr.pad((51.9, 77.8, 103.8), 0.12, 1.8)
        tr.beat(110, 2.4, 15.4, 0.12)
        tr.thump(0.0, 0.6); tr.slam(1.3, 0.7)
        for k in range(6): tr.tick(2.6 + k * 0.4, 0.35)
        tr.whoosh(5.2, 0.3); tr.thump(5.9, 0.4); tr.thump(6.25, 0.4); tr.slam(6.8, 0.6)
        tr.whoosh(8.6, 0.3); tr.hum(9.0, 10.0, 110, 0.06)
        for k in range(len(spec["stamps"])): tr.slam(12.2 + 1.1 * k, 0.9)
        tr.whoosh(15.45, 0.3); tr.thump(15.5, 0.6); tr.slam(16.3, 0.8)
        tr.whoosh(17.55, 0.35); tr.thump(17.7, 0.5)
        if spec["app"].get("chip"): tr.click(T_APP + 1.1, 0.6, 2600)
        tr.ding(20.1, 990, 0.25)
        tr.whoosh(22.15, 0.35); tr.thump(22.3, 0.7); tr.thump(23.2, 0.5)
        return tr

    return frame, DUR, track, [0.05, 1.6, 3.5, 7.4, 10.8, 13.6, 16.6, T_APP + 1.4, T_APP + 3.4, T_END + 1.6]
