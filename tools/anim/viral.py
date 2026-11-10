"""Two hook-first reels: arm pump, and the manual's rider weight. Flat carbon, no glow.

    python3 tools/anim/viral.py sheet|render <outdir>
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib
from lib import *

def flat(kind="glow"): return Image.new("RGB", (W, H), CARBON)
lib.bg = flat
import app
app.bg = flat
bg = flat

def fit(d, lines, font, size, width=W - 2 * M):
    while max(d.textlength(l, font=F(font, size)) for l in lines) > width and size > 60: size -= 4
    return size

def title(d, t, t0, t1, white, blue, size=150, y=230):
    """white lines then blue lines, big italic, in at t0 and out at t1."""
    a = win(t, t0, t1, 0.25, 0.25) if t0 > 0 else 1 - ease((t - (t1 - 0.25)) / 0.25)
    if a <= 0: return y
    sz = fit(d, list(white) + list(blue), DISPI, size)
    lines = [(s, F(DISPI, sz), WHITE) for s in white] + [(s, F(DISPI, sz), BLUE) for s in blue]
    return stack(d, M, y, lines, t, t0 if t0 > 0 else -1, stagger=0.07, a_out=a, lh=sz * 0.95)

def centered(d, t, t0, t1, s, y, size=62, col=WHITE, font=XB):
    a = win(t, t0, t1, 0.25, 0.2)
    text(d, (W / 2, y), s, F(font, size), col, a, anchor="ma", dy=round((1 - ease((t - t0) / 0.25)) * 24))

# ================================================================= 1. ARM PUMP
A_DUR, A_S2, A_S3, A_APP, A_END = 21.0, 2.5, 7.0, 13.4, 18.2

def bump(x):
    """braking-bump profile, px of height at ground x"""
    return 30 * abs(math.sin(x / 78.0)) ** 1.6 + 9 * abs(math.sin(x / 31.0 + 1.3))

def grip_scene(d, t, a):
    if a <= 0: return
    amp = lerp(3, 15, ease(t / 1.8))
    dy = round(math.sin(t * 58) * amp); dx = round(math.cos(t * 41) * amp * 0.4)
    y = 955 + dy
    d.rounded_rectangle([120 + dx, y - 20, 960 + dx, y + 20], radius=20, fill=rgba((150, 158, 176), a))
    d.rounded_rectangle([520 + dx, y - 46, 950 + dx, y + 46], radius=30, fill=rgba((34, 38, 48), a), outline=rgba((70, 78, 94), a), width=3)
    for k in range(13):
        x = 556 + dx + k * 29
        d.line([(x, y - 34), (x, y + 34)], fill=rgba((62, 68, 82), a), width=6)
    d.rounded_rectangle([944 + dx, y - 54, 972 + dx, y + 54], radius=10, fill=rgba((52, 58, 72), a))
    # vibration marks
    for k, off in enumerate((-96, 96)):
        va = a * clamp(amp / 15) * (0.5 + 0.5 * math.sin(t * 30 + k))
        for j in range(3):
            xx = 600 + j * 130 + dx
            d.arc([xx - 40, y + off - 22, xx + 40, y + off + 22], 200 if off < 0 else 20, 340 if off < 0 else 160, fill=rgba(RED, va), width=6)
    # grip meter
    fill = lerp(0.25, 1.0, ease(t / 1.9))
    col = mix(GREEN, RED, (fill - 0.4) / 0.5)
    tracked(d, M, 1126, "GRIP FORCE", F(BOLD, 30), STEEL, a, 4)
    d.rounded_rectangle([M, 1180, W - M, 1230], radius=25, fill=rgba(PANEL, a), outline=rgba(BORDER, a), width=2)
    d.rounded_rectangle([M, 1180, M + (W - 2 * M) * fill, 1230], radius=25, fill=rgba(col, a))
    if fill > 0.93:
        pa = a * (0.65 + 0.35 * math.sin(t * 16))
        tracked(d, W - M, 1122, "PUMPED", F(DISP, 44), RED, pa, 3, anchor="r")

def front_end(d, t, a, k_harsh):
    """side view: wheel on braking bumps, fork, bar. k_harsh = how much of each bump reaches the bar."""
    if a <= 0: return
    G = 1330
    scroll = t * 560
    pts = [(x, G - bump(x + scroll)) for x in range(0, W + 12, 12)]
    d.polygon(pts + [(W, 1400), (0, 1400)], fill=rgba((24, 28, 36), a))
    d.line(pts, fill=rgba((96, 104, 122), a), width=5)
    wx, r = 690, 172
    h = max(bump(wx + scroll + o) for o in (-40, -20, 0, 20, 40))
    wy = G - h - r
    wy0 = G - 16 - r
    # tyre, rim, spokes
    d.ellipse([wx - r, wy - r, wx + r, wy + r], outline=rgba((30, 33, 42), a), width=40, fill=rgba(CARBON, a))
    d.ellipse([wx - r, wy - r, wx + r, wy + r], outline=rgba((64, 70, 86), a), width=4)
    ri = r - 42
    d.ellipse([wx - ri, wy - ri, wx + ri, wy + ri], outline=rgba((170, 178, 196), a), width=7)
    rot = scroll / r
    for j in range(12):
        th = rot + j * math.pi / 6
        d.line([(wx, wy), (wx + math.cos(th) * ri, wy + math.sin(th) * ri)], fill=rgba((90, 98, 116), a), width=3)
    d.ellipse([wx - 26, wy - 26, wx + 26, wy + 26], fill=rgba((150, 158, 176), a))
    # fork: axle up and back to the clamp
    ux, uy = -0.42, -0.9075
    top_y = (wy0 - 0.9075 * 560) + k_harsh * (wy - wy0) * 1.0
    tx = wx + ux * 560; ty = top_y
    d.line([(wx, wy), (tx, ty)], fill=rgba((196, 204, 220), a), width=22)                    # chrome inner tube
    ox, oy = tx - ux * 300, ty - uy * 300
    d.line([(ox, oy), (tx, ty)], fill=rgba((70, 78, 96), a), width=40)                       # outer tube
    d.line([(wx, wy), (wx + ux * 70, wy + uy * 70)], fill=rgba((70, 78, 96), a), width=44)   # axle lug
    # bar and grip
    bx, by = tx - 20, ty - 46
    d.line([(tx, ty), (bx, by)], fill=rgba((110, 118, 136), a), width=18)
    d.ellipse([bx - 40, by - 40, bx + 40, by + 40], fill=rgba((34, 38, 48), a), outline=rgba(RED if k_harsh > 0.6 else GREEN, a), width=7)
    jit = abs(wy - wy0) * k_harsh / 30
    for j in range(3):
        rr = 62 + j * 26
        d.arc([bx - rr, by - rr, bx + rr, by + rr], 150, 250, fill=rgba(RED, a * clamp(jit) * (1 - j * 0.28)), width=6)
    return by

def hands_panel(d, t, a, kfn):
    if a <= 0: return
    x0, y0, x1, y1 = 600, 600, W - M, 830
    d.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=rgba(PANEL, a), outline=rgba(BORDER, a), width=2)
    tracked(d, x0 + 26, y0 + 22, "WHAT YOUR HANDS FEEL", F(BOLD, 22), STEEL, a, 2)
    mid = y0 + 140
    pts = []
    for i in range(0, 61):
        tt = t - (60 - i) * 0.02
        k = kfn(tt)
        hgt = bump(690 + tt * 560) - 16
        pts.append((x0 + 26 + i * (x1 - x0 - 52) / 60, mid - hgt * k * 1.9))
    col = mix(GREEN, RED, (kfn(t) - 0.3) / 0.4)
    d.line(pts, fill=rgba(col, a), width=6, joint="curve")

CHECKS = [("1", "BLEED YOUR FORKS", "Let the built-up air out before you ride."),
          ("2", "COUNT YOUR CLICKS", "Fork compression, out from fully closed."),
          ("3", "GO 2 CLICKS SOFTER", "Same section. See if your hands last.")]

def checks(d, t, a):
    if a <= 0: return
    for i, (n, head, sub) in enumerate(CHECKS):
        t0 = A_S3 + 0.5 + i * 1.75
        ca = ease((t - t0) / 0.35) * a
        if ca <= 0: continue
        active = t < t0 + 1.75 or i == 2
        y = 590 + i * 250 + round((1 - ease((t - t0) / 0.35)) * 50)
        d.rounded_rectangle([M - 20, y, W - M + 20, y + 218], radius=30, fill=rgba(PANEL, ca),
                            outline=rgba(BLUE if active else BORDER, ca), width=4 if active else 2)
        text(d, (M + 26, y + 22), n, F(DISPI, 170), BLUE, ca)
        text(d, (M + 150, y + 36), head, F(XB, 72), WHITE, ca)
        text(d, (M + 150, y + 132), sub, F(MED, 35), BODY, ca)

def arm_frame(t):
    img = bg(); d = draw(img)
    # ---- hook, on screen from frame 1
    if t < A_S2 + 0.1:
        a = 1 - ease((t - (A_S2 - 0.25)) / 0.25)
        pop = 1 + 0.07 * (1 - ease(t / 0.22))
        s1 = fit(d, ["ARM PUMP"], DISPI, 300)
        s2 = fit(d, ["ISN'T ALWAYS", "YOUR ARMS."], DISPI, 170)
        text(d, (M, 215), "ARM PUMP", F(DISPI, s1 * pop), WHITE, a)
        text(d, (M, 215 + s1 * 0.93), "ISN'T ALWAYS", F(DISPI, s2), WHITE, a)
        text(d, (M, 215 + s1 * 0.93 + s2 * 0.95), "YOUR ARMS.", F(DISPI, s2), BLUE, a)
        grip_scene(d, t, a)
    # ---- the fork
    a2 = win(t, A_S2, A_S3, 0.3, 0.25)
    if a2 > 0:
        title(d, t, A_S2, A_S3, ["SOMETIMES"], ["IT'S YOUR FORK."], 170)
        kfn = lambda tt: 0.92
        front_end(d, t, a2, 0.92)
        hands_panel(d, t, a2, kfn)
        chip(d, M, 620, "HARSH FORK", RED, a2 * ease((t - A_S2 - 0.3) / 0.3), fg=WHITE)
        centered(d, t, A_S2 + 0.9, A_S2 + 2.7, "Every small bump goes into your hands.", 1452, 58)
        centered(d, t, A_S2 + 2.7, A_S3, "You squeeze harder. That's the pump.", 1452, 60)
    # ---- three checks
    a3 = win(t, A_S3, A_APP + 0.1, 0.3, 0.25)
    if a3 > 0:
        title(d, t, A_S3, A_APP + 0.1, ["3 CHECKS BEFORE"], ["YOUR NEXT MOTO."], 150)
        checks(d, t, a3)
        centered(d, t, A_S3 + 4.9, A_APP + 0.1, "One change at a time.", 1372, 46, BODY, SEMI)
    img = app.segment(img, t, A_APP, "Arm pump", None,
                      lines=(("TELL DIALED OFFROAD", "WHAT THE BIKE DID."), ("IT TELLS YOU WHICH CLICKER,", "WHICH WAY, HOW MANY.")))
    return end_card(img, t, A_END, head=("GET YOUR", "STARTING POINT."),
                    sub=("Your bike. Your weight. Your track.", "Then fine tune it on the bike."))

def arm_track():
    tr = Track(A_DUR, 5)
    tr.pad((55, 82.4, 110), 0.13, 2.0)
    tr.slam(0.05, 0.8); tr.thump(0.75, 0.5); tr.thump(1.45, 0.5)
    tr.hum(0.2, 2.3, 96, 0.07)
    tr.whoosh(A_S2 - 0.1, 0.3); tr.thump(A_S2, 0.6)
    x = A_S2 + 0.3
    while x < A_S3 - 0.2: tr.thump(x, 0.33, 0.12); x += 0.437
    tr.whoosh(A_S3 - 0.1, 0.3); tr.thump(A_S3, 0.6)
    for i in range(3):
        at = A_S3 + 0.5 + i * 1.75
        tr.thump(at, 0.5, 0.2); tr.ding(at + 0.1, 660 + i * 110, 0.2)
    tr.click(A_S3 + 4.4, 0.8, 2200); tr.click(A_S3 + 4.65, 0.8, 2200)
    tr.whoosh(A_APP - 0.05, 0.35); tr.thump(A_APP + 0.1, 0.5); tr.click(A_APP + 1.1, 0.7, 2600); tr.ding(A_APP + 2.4, 990, 0.25)
    tr.whoosh(A_END - 0.05, 0.35); tr.thump(A_END + 0.1, 0.7); tr.thump(A_END + 1.0, 0.5)
    return tr

# ================================================================= 2. RIDER WEIGHT
B_DUR, B_S2, B_S3, B_APP, B_END = 18.2, 2.8, 7.0, 10.5, 15.3
PAPER = (238, 234, 224); INK = (26, 28, 34); INK2 = (112, 114, 122)
LO, HI = 165, 187   # 2026 KTM 250 SX-F owner's manual: set up for a rider of 75 to 85 kg

def manual_card(img, d, t, a):
    if a <= 0: return
    x0, y0, x1, y1 = M - 10, 820, W - M + 10, 1420
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=PAPER + (255,))
    tracked(ld, x0 + 46, y0 + 40, "OWNER'S MANUAL", F(BOLD, 26), INK2, 1, 4)
    tracked(ld, x1 - 46, y0 + 40, "2026 KTM 250 SX-F", F(BOLD, 26), INK2, 1, 3, anchor="r")
    ld.line([(x0 + 46, y0 + 92), (x1 - 46, y0 + 92)], fill=(200, 196, 186, 255), width=3)
    for k, wd in enumerate((0.92, 0.7)):
        ld.rounded_rectangle([x0 + 46, y0 + 124 + k * 34, x0 + 46 + (x1 - x0 - 92) * wd, y0 + 138 + k * 34], radius=7, fill=(212, 208, 198, 255))
    ld.text((x0 + 46, y0 + 214), "Standard rider weight", font=F(SEMI, 44), fill=INK + (255,))
    f = F(DISP, 170); s = f"{LO} to {HI} lb"
    tw = ld.textlength(s, font=f)
    hw = ease((t - 0.45) / 0.55)
    if hw > 0:
        ld.rounded_rectangle([x0 + 34, y0 + 300, x0 + 34 + (tw + 30) * hw, y0 + 456], radius=10, fill=(255, 214, 0, 255))
    ld.text((x0 + 46, y0 + 276), s, font=f, fill=INK + (255,))
    ld.text((x0 + 46, y0 + 478), "75 to 85 kg", font=F(SEMI, 40), fill=INK2 + (255,))
    for k, wd in enumerate((0.55,)):
        ld.rounded_rectangle([x0 + 46, y0 + 552, x0 + 46 + (x1 - x0 - 92) * wd, y0 + 566], radius=7, fill=(212, 208, 198, 255))
    if a < 1: lay.putalpha(lay.getchannel("A").point(lambda v: round(v * a)))
    img.paste(lay, (0, round((1 - a) * -30)), lay)

def scale_scene(d, t, a):
    if a <= 0: return
    w = keys(t, [(B_S2, 176), (B_S2 + 0.9, 176), (B_S2 + 1.5, 148), (B_S2 + 2.5, 148), (B_S2 + 3.1, 216), (B_S3, 216)])
    x0, x1, y = M, W - M, 1110
    def X(v): return x0 + (x1 - x0) * (v - 120) / (250 - 120)
    inside = LO <= w <= HI
    col = GREEN if inside else (ORANGE if w < LO else RED)
    text(d, (W / 2, 610), f"{round(w)}", F(DISP, 280), WHITE, a, anchor="ma")
    tracked(d, W / 2, 965, "LB, IN YOUR GEAR", F(BOLD, 30), STEEL, a, 4, anchor="m")
    d.rounded_rectangle([x0, y, x1, y + 36], radius=18, fill=rgba(PANEL, a), outline=rgba(BORDER, a), width=2)
    d.rounded_rectangle([X(LO), y, X(HI), y + 36], radius=6, fill=rgba(GREEN, a))
    tracked(d, (X(LO) + X(HI)) / 2, y + 58, "BUILT FOR", F(BOLD, 24), GREEN, a, 3, anchor="m")
    for v in (120, 250):
        text(d, (X(v), y + 56), str(v), F(MED, 26), DIM, a, anchor="ma")
    mx = X(w)
    d.polygon([(mx, y - 10), (mx - 26, y - 54), (mx + 26, y - 54)], fill=rgba(WHITE, a))
    d.line([(mx, y - 10), (mx, y + 46)], fill=rgba(WHITE, a), width=6)
    msg = "IN THE WINDOW" if inside else ("LIGHTER: STOCK IS STIFF FOR YOU" if w < LO else "HEAVIER: STOCK IS SOFT FOR YOU")
    f = F(BOLD, 38); tw = d.textlength(msg, font=f) + 38 * 1.3 + len(msg) * 2
    chip(d, W / 2 - tw / 2, 1290, msg, col, a, fg=CARBON if col != RED else WHITE, size=38)

STOCK = [("FORK COMPRESSION", "12"), ("FORK REBOUND", "18"), ("SHOCK COMPRESSION", "15"), ("SHOCK REBOUND", "15")]

def stock_sheet(d, t, a):
    if a <= 0: return
    x0, y0, x1 = M - 10, 640, W - M + 10
    d.rounded_rectangle([x0, y0, x1, y0 + 690], radius=30, fill=rgba(PANEL, a), outline=rgba(BORDER, a), width=2)
    tracked(d, x0 + 44, y0 + 40, "STOCK CLICKERS, FROM THE MANUAL", F(BOLD, 26), STEEL, a, 3)
    for i, (name, val) in enumerate(STOCK):
        ra = a * ease((t - B_S3 - 0.35 - i * 0.22) / 0.3)
        y = y0 + 110 + i * 142
        d.line([(x0 + 44, y), (x1 - 44, y)], fill=rgba(BORDER, ra), width=2)
        text(d, (x0 + 44, y + 44), name, F(XB, 56), WHITE, ra)
        text(d, (x1 - 150, y + 14), val, F(DISP, 116), WHITE, ra, anchor="ra")
        qa = ra * ease((t - B_S3 - 1.7 - i * 0.12) / 0.25)
        text(d, (x1 - 44, y + 14), "?", F(DISPI, 116), ORANGE, qa, anchor="ra")
        if qa <= 0: text(d, (x1 - 44, y + 70), "out", F(MED, 30), STEEL, ra, anchor="ra")
    centered(d, t, B_S3 + 2.0, B_APP + 0.1, "Right for that rider. Maybe not for you.", 1372, 50, BODY, SEMI)

def weight_frame(t):
    img = bg(); d = draw(img)
    if t < B_S2 + 0.1:
        a = 1 - ease((t - (B_S2 - 0.25)) / 0.25)
        pop = 1 + 0.06 * (1 - ease(t / 0.22))
        sz = fit(d, ["YOUR BIKE WAS", "SET UP FOR", "THIS RIDER."], DISPI, 190)
        for i, (s, c) in enumerate((("YOUR BIKE WAS", WHITE), ("SET UP FOR", WHITE), ("THIS RIDER.", BLUE))):
            text(d, (M, 215 + i * sz * 0.94), s, F(DISPI, sz * pop), c, a)
        manual_card(img, d, t, a); d = draw(img)
    a2 = win(t, B_S2, B_S3, 0.3, 0.25)
    if a2 > 0:
        title(d, t, B_S2, B_S3, ["IS THAT YOU"], ["IN FULL GEAR?"], 180)
        scale_scene(d, t, a2)
    a3 = win(t, B_S3, B_APP + 0.1, 0.3, 0.25)
    if a3 > 0:
        title(d, t, B_S3, B_APP + 0.1, ["IF NOT, STOCK IS"], ["ONLY A GUESS."], 170)
        stock_sheet(d, t, a3)
    img = app.segment(img, t, B_APP, None, None, screens=(6, 5),
                      lines=(("TELL DIALED OFFROAD YOUR", "BIKE, WEIGHT AND TRACK."), ("GET A STARTING POINT", "BUILT AROUND YOU.")))
    return end_card(img, t, B_END, head=("START FROM", "YOUR NUMBERS."), sub=("Then ride it and refine it.",))

def weight_track():
    tr = Track(B_DUR, 9)
    tr.pad((61.7, 92.5, 123.5), 0.13, 1.5)
    tr.slam(0.05, 0.8); tr.whoosh(0.45, 0.4, 0.55); tr.thump(1.1, 0.4)
    tr.whoosh(B_S2 - 0.1, 0.3); tr.thump(B_S2, 0.6)
    for k in range(6): tr.tick(B_S2 + 0.95 + k * 0.09, 0.3)
    tr.thump(B_S2 + 1.5, 0.45, 0.2)
    for k in range(8): tr.tick(B_S2 + 2.5 + k * 0.075, 0.3)
    tr.thump(B_S2 + 3.1, 0.45, 0.2)
    tr.whoosh(B_S3 - 0.1, 0.3); tr.thump(B_S3, 0.6)
    for i in range(4): tr.click(B_S3 + 0.35 + i * 0.22, 0.6, 2200)
    for i in range(4): tr.tick(B_S3 + 1.7 + i * 0.12, 0.4)
    tr.whoosh(B_APP - 0.05, 0.35); tr.thump(B_APP + 0.1, 0.5); tr.whoosh(B_APP + 2.4, 0.25); tr.ding(B_APP + 2.6, 990, 0.25)
    tr.whoosh(B_END - 0.05, 0.35); tr.thump(B_END + 0.1, 0.7); tr.thump(B_END + 1.0, 0.5)
    return tr

VIDEOS = {
    "arm-pump": (arm_frame, A_DUR, arm_track, [0.0, 1.9, 4.0, 6.2, 9.6, 12.8, A_APP + 1.5, A_APP + 3.6, A_END + 1.8]),
    "rider-weight": (weight_frame, B_DUR, weight_track, [0.0, 1.6, 3.4, 5.0, 6.6, 8.2, 9.9, B_APP + 1.5, B_APP + 3.6, B_END + 1.8]),
}

if __name__ == "__main__":
    mode, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for name, (frame, dur, track, times) in VIDEOS.items():
        if len(sys.argv) > 3 and name not in sys.argv[3:]: continue
        if mode == "sheet":
            lib.stills(frame, times, f"{out}/{name}_sheet.jpg")
        elif mode == "full":
            for tt in times[:int(os.environ.get("N", 3))]: frame(tt).save(f"{out}/{name}_{tt:05.2f}.jpg", quality=88)
        else:
            v, wav = f"{out}/{name}_v.mp4", f"{out}/{name}.wav"
            lib.render(frame, dur, v); track().save(wav); lib.mux(v, wav, f"{out}/dialed-{name}.mp4")
            os.remove(v); os.remove(wav)
            frame(times[0] + 0.6).save(f"{out}/dialed-{name}-cover.jpg", quality=90)
        print("done", mode, name)
