"""Template "oneclick": a macro clicker, the needle and bleed gap, a damping graph, then "same number, different setting".

spec keys: hook [white line, blue line], hook_sub, intro {tag, body}, turn_in, turn_out (bodies), feel {tag, body},
bands [low-speed caption, high-speed caption], closer {tag, body, foot}, app {chip, part, from, to, how}, end {head, sub}.
"""
from lib import *
import app

DUR = 25.6
T_APP, T_END = 17.3, 21.9
STEP = 15  # degrees per click

# (time, clicks out)
EVENTS = [(2.4, 12), (3.8, 11), (7.3, 10), (8.75, 11), (9.25, 12), (10.9, 11), (11.8, 10), (12.7, 9)]
def n_at(t):
    """clicks out, as a float that animates over 0.14 s between detents"""
    n = 12.0
    prev = 12
    for te, v in EVENTS:
        if t >= te + 0.14: n = v; prev = v
        elif t >= te: n = prev + (v - prev) * ease((t - te) / 0.14); break
        else: break
    return n

def hook_angle(t):  # quick fidget turning during the hook
    return 20 * math.sin(t * 7) + 60 * ease(t / 1.2)

def dial(d, cx, cy, r, ang, a, label=None, sub=None, accent=BLUE):
    if a <= 0: return
    d.ellipse([cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10], fill=rgba((16, 18, 24), a))
    # knurled ring
    for k in range(48):
        th = math.radians(ang + k * 7.5)
        x0, y0 = cx + math.cos(th) * (r - 4), cy + math.sin(th) * (r - 4)
        x1, y1 = cx + math.cos(th) * (r * 0.8), cy + math.sin(th) * (r * 0.8)
        d.line([(x0, y0), (x1, y1)], fill=rgba((120, 128, 146), a), width=max(2, round(r / 40)))
    d.ellipse([cx - r * 0.78, cy - r * 0.78, cx + r * 0.78, cy + r * 0.78], fill=rgba((44, 50, 64), a), outline=rgba((160, 168, 186), a), width=4)
    # screwdriver slot
    th = math.radians(ang)
    dx, dy = math.cos(th) * r * 0.6, math.sin(th) * r * 0.6
    d.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], fill=rgba(CARBON, a), width=max(6, round(r / 7)))
    # index mark on the slot end
    d.ellipse([cx + dx * 1.15 - r * 0.06, cy + dy * 1.15 - r * 0.06, cx + dx * 1.15 + r * 0.06, cy + dy * 1.15 + r * 0.06], fill=rgba(accent, a))
    if label:
        text(d, (cx, cy + r + 40), label, F(DISP, max(40, r * 0.42)), WHITE, a, anchor="ma")
    if sub:
        text(d, (cx, cy + r + 40 + max(40, r * 0.42) + 6), sub, F(SEMI, 30), STEEL, a, anchor="ma")

def flow_diagram(d, t, n, a, cy=1180):
    if a <= 0: return
    cx = 540
    gap = 8 + 3.2 * n           # px between needle cone and seat edge
    # chambers
    d.rounded_rectangle([cx - 230, cy - 330, cx + 230, cy + 330], radius=40, fill=rgba((29, 155, 240), 0.12 * a), outline=rgba((120, 180, 240), a), width=3)
    # seat plate with orifice (hole 150 wide)
    hole = 75
    d.rectangle([cx - 230, cy - 12, cx - hole, cy + 18], fill=rgba((150, 160, 180), a))
    d.rectangle([cx + hole, cy - 12, cx + 230, cy + 18], fill=rgba((150, 160, 180), a))
    # needle from the top: deeper into the seat as you click in
    depth = clamp(150 - (n - 7) * 22, 10, 135)
    tip = cy + depth
    cone_top = tip - 140
    d.rectangle([cx - 70, cy - 330, cx + 70, cone_top], fill=rgba((205, 212, 225), a))
    d.polygon([(cx - 70, cone_top), (cx + 70, cone_top), (cx, tip)], fill=rgba((205, 212, 225), a))
    hw = 70 * clamp(depth / 140)
    g = hole - hw
    yy = cy + 40
    d.line([(cx + hw, yy), (cx + hole, yy)], fill=rgba(YELLOW, a), width=5)
    d.line([(cx + hw, yy - 14), (cx + hw, yy + 14)], fill=rgba(YELLOW, a), width=5)
    d.line([(cx + hole, yy - 14), (cx + hole, yy + 14)], fill=rgba(YELLOW, a), width=5)
    d.line([(cx + hole + 6, yy), (cx + 250, yy)], fill=rgba(YELLOW, a * 0.6), width=2)
    tracked(d, cx + 256, yy - 16, "BLEED GAP", F(BOLD, 28), YELLOW, a, 2)
    # oil particles: count scales with the open area, all squeeze through the gap
    rate = clamp((g - 8) / 50)
    count = round(6 + 26 * rate)
    for j in range(count):
        side = -1 if j % 2 else 1
        ph = ((j * 0.137 + t * 0.55) % 1.0)
        lane_off = ((j * 37) % 100) / 100
        # x converges from the chamber to the gap, then spreads again
        xg = cx + side * (hw + g * (0.25 + 0.5 * lane_off))
        xw = cx + side * (60 + 150 * lane_off)
        y = cy - 300 + ph * 600
        k = clamp(1 - abs(y - cy) / 260)
        x = lerp(xw, xg, k ** 0.7)
        r = 9 if abs(y - cy) < 60 else 6
        d.ellipse([x - r, y - r, x + r, y + r], fill=rgba(mix(BLUE, (140, 220, 255), k), a * 0.95))

def curve(n, v):
    ls = 0.10 + (12 - n) * 0.07
    return 0.75 * v ** 1.25 + ls * (1 - math.exp(-v / 0.09))

def graph(d, t, n, a, ghosts=(), bands=("", "")):
    if a <= 0: return
    x0, y0, x1, y1 = 170, 1560, 930, 980
    # bands
    split = x0 + (x1 - x0) * 0.3
    d.rectangle([x0, y1, split, y0], fill=rgba(BLUE, 0.10 * a))
    tracked(d, x0 + 14, y1 + 14, "LOW SPEED", F(BOLD, 26), BLUE, a, 2)
    tracked(d, split + 14, y1 + 14, "HIGH SPEED", F(BOLD, 26), STEEL, a, 2)
    d.line([(x0, y1), (x0, y0), (x1, y0)], fill=rgba(STEEL, a), width=4)
    text(d, (x1, y0 + 20), "SHAFT SPEED", F(BOLD, 24), STEEL, a, anchor="ra")
    text(d, (x0 - 24, y1), "DAMPING", F(BOLD, 24), STEEL, a, anchor="ra")
    def pts(nn):
        out = []
        for k in range(61):
            v = k / 60
            out.append((x0 + (x1 - x0) * v, y0 - (y0 - y1 - 40) * curve(nn, v) / 1.35))
        return out
    for gn in ghosts:
        d.line(pts(gn), fill=rgba(STEEL, a * 0.35), width=4)
    d.line(pts(n), fill=rgba(BLUE, a), width=8, joint="curve")
    # band captions under the axis
    text(d, (x0 + 4, y0 + 56), bands[0], F(SEMI, 28), BODY, a)
    text(d, (split + 30, y0 + 96), bands[1], F(SEMI, 28), STEEL, a)

def make(spec):
    def frame(t):
        img = bg("grid"); d = draw(img)
        n = n_at(t)
        ang = hook_angle(t) if t < 2.4 else (12 - n) * STEP + 60

        # ---- dial position by scene
        if t < 6.0:
            r = 250 if t >= 2.4 else 230
            cx, cy = 540, 1080
            if t > 5.4:
                k = ease((t - 5.4) / 0.6); r = lerp(250, 105, k); cx = lerp(540, 830, k); cy = lerp(1080, 690, k)
        elif t < 14.0:
            r, cx, cy = 105, 830, 690
        else:
            r, cx, cy = 105, 830, 690
        da = 1 - ease((t - 13.7) / 0.3)
        show_count = t >= 2.4
        lab = f"{round(n)} OUT" if show_count else None
        if t < 14.0:
            dial(d, cx, cy, r, ang, da, lab if r > 200 else None)
            if show_count and r <= 200:
                text(d, (cx, cy + r + 18), f"{round(n)} OUT", F(DISP, 60), WHITE, da, anchor="ma")
        # click flash: "1 CLICK IN"
        for te, v in EVENTS[1:]:
            fa = win(t, te, te + 0.9, 0.08, 0.3)
            if fa > 0 and t < 14:
                prev = [e for e in EVENTS if e[0] < te][-1][1]
                s = "1 CLICK IN" if v < prev else "1 CLICK OUT"
                col = BLUE if v < prev else ORANGE
                if r > 200:
                    chip(d, 540 - 115, 1505, s, col, fa)
                else:
                    chip(d, cx - 160, cy - r - 80, s, col, fa)

        # ---- hook
        if t < 2.5:
            a = 1 - ease((t - 2.2) / 0.3)
            pop = 1 + 0.08 * (1 - ease(t / 0.25))
            sz = 118
            while max(d.textlength(l, font=F(DISPI, sz)) for l in spec["hook"]) > W - 2 * M: sz -= 4
            text(d, (M, 230), spec["hook"][0], F(DISPI, sz * pop), WHITE, a)
            text(d, (M, 230 + sz * 0.97), spec["hook"][1], F(DISPI, sz * pop), BLUE, a)
            stack(d, M, 260 + sz * 2, [(spec["hook_sub"], F(SEMI, 44), BODY)], t, 0.5, a_out=a)
        caption(d, t, 2.45, 6.0, spec["intro"]["tag"], BLUE, spec["intro"]["body"])
        # ---- needle scene
        fda = win(t, 6.0, 10.4, 0.4, 0.35)
        flow_diagram(d, t, n, fda)
        caption(d, t, 6.0, 8.7, "TURN IN", BLUE, spec["turn_in"], width=640)
        caption(d, t, 8.7, 10.4, "TURN OUT", ORANGE, spec["turn_out"], width=640)
        # ---- graph scene
        ga = win(t, 10.3, 14.0, 0.4, 0.3)
        ghosts = [g for g in (12, 11, 10) if g > round(n)]
        graph(d, t, n, ga, ghosts, spec["bands"])
        caption(d, t, 10.4, 14.0, spec["feel"]["tag"], BLUE, spec["feel"]["body"], width=640)
        # ---- two bikes scene
        ta = win(t, 14.0, 17.4, 0.4, 0.3)
        if ta > 0:
            caption(d, t, 14.0, 17.4, spec["closer"]["tag"], YELLOW, spec["closer"]["body"])
            for k, (x, rng, lbl) in enumerate([(300, 18, "18 CLICK RANGE"), (780, 26, "26 CLICK RANGE")]):
                aa = ta * ease((t - 14.4 - k * 0.25) / 0.35)
                dial(d, x, 920, 140, (rng - 12) * 13, aa, "12 OUT", lbl, BLUE if k == 0 else ORANGE)
                # range bar
                pct = 12 / rng
                y = 1240
                d.rounded_rectangle([x - 170, y, x + 170, y + 26], radius=13, fill=rgba(PANEL, aa), outline=rgba(BORDER, aa), width=2)
                fill = ease((t - 14.8 - k * 0.25) / 0.6) * pct
                d.rounded_rectangle([x - 170, y, x - 170 + 340 * max(fill, 0.08), y + 26], radius=13, fill=rgba(BLUE if k == 0 else ORANGE, aa))
                text(d, (x, y + 50), f"{round(pct * 100)}% open", F(DISP, 64), WHITE, aa * ease((t - 15.2) / 0.3), anchor="ma")
            b = ease((t - 15.6) / 0.35) * ta
            text(d, (W / 2, 1480), spec["closer"]["foot"], F(SEMI, 44), BODY, b, anchor="ma")
        a_ = spec["app"]
        img = app.segment(img, t, T_APP, a_.get("chip"), (a_["part"], a_["from"], a_["to"], a_["how"]))
        return end_card(img, t, T_END, head=tuple(spec["end"]["head"]), sub=tuple(spec["end"]["sub"]))

    def track():
        tr = Track(DUR, 3)
        tr.pad((65.4, 98, 130.8), 0.12, 1.5)
        for k in range(6): tr.click(0.15 + k * 0.33, 0.35, 2600)
        for te, _ in EVENTS[1:]: tr.click(te, 0.9, 2200); tr.thump(te, 0.3, 0.15)
        tr.whoosh(2.4, 0.3); tr.whoosh(5.4, 0.3); tr.hum(6.0, 10.4, 82, 0.05)
        tr.whoosh(10.3, 0.3); tr.whoosh(14.0, 0.3); tr.ding(15.25, 740, 0.22); tr.ding(15.5, 990, 0.22)
        tr.whoosh(17.25, 0.35); tr.thump(17.4, 0.5); tr.click(18.4, 0.6, 2600); tr.ding(19.7, 990, 0.25)
        tr.whoosh(21.85, 0.35); tr.thump(22.0, 0.7); tr.thump(22.9, 0.5)
        return tr

    return frame, DUR, track, [0.05, 4.2, 7.6, 12.6, 15.9, T_APP + 1.4, T_APP + 3.4, T_END + 1.6]
