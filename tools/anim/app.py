"""App moment: real Dialed Offroad screens in a phone, a tap on the matching symptom, then the app's change card."""
from lib import *

SHOTS = os.path.join(ASSETS, "shots")
APP_LEN = 4.8
PHONE_BOX = (224, 499, 856, 1920)     # phone area inside the 1080x1920 store screenshot
PHONE_Y = 600                          # where the phone's top lands on screen

# chip boxes on screen 2 (screenshot coords)
CHIPS = {   # every chip on the real "How was it?" screen (tools/shots/02)
    "Front pushes": (270, 996, 532, 1070), "Wallows / dives": (547, 996, 810, 1070),
    "Headshake": (270, 1086, 532, 1160), "Deflects in chop": (547, 1086, 810, 1160),
    "Arm pump": (270, 1176, 532, 1250), "Chatters": (547, 1176, 810, 1250),
    "Rear kicks": (270, 1313, 532, 1387), "Packs in chop": (547, 1313, 810, 1387),
    "Rear swaps": (270, 1403, 532, 1477), "Rear squats on the gas": (547, 1403, 810, 1508),
    "Harsh on small bumps": (270, 1571, 532, 1677), "Bottoms on landings": (547, 1571, 810, 1677),
    "Too stiff all over": (270, 1692, 532, 1766), "Too soft all over": (547, 1692, 810, 1766),
}

_phones = {}
def phone(i):
    if i not in _phones:
        im = Image.open(f"{SHOTS}/0{i}_dialed_play_1080x1920.png").convert("RGB")
        _phones[i] = im.crop(PHONE_BOX)
    return _phones[i]

def change_card(d, img, x, y, a, part, frm, to, how):
    """The app's 'change' block: part name, old -> new clicks, direction. Drawn in the app's style."""
    if a <= 0: return
    w, h = W - 2 * x, 440
    d.rounded_rectangle([x, y, x + w, y + h], radius=36, fill=rgba((12, 13, 17), a), outline=rgba(BLUE, a), width=4)
    tracked(d, x + 46, y + 40, "DIALED OFFROAD SAYS", F(BOLD, 24), BLUE, a, 3)
    tracked(d, W / 2, y + 100, part, F(XB, 38), STEEL, a, 3, anchor="m")
    fo, fb = F(DISP, 120), F(DISP, 190)
    wa = d.textlength(frm, font=fo); wb = d.textlength(to, font=fb); gap = 90
    x0 = W / 2 - (wa + gap + wb) / 2
    text(d, (x0, y + 150), frm, fo, (120, 128, 146), a)
    ax, ay = x0 + wa + gap / 2, y + 232
    d.line([(ax - 26, ay), (ax + 18, ay)], fill=rgba(STEEL, a), width=7)
    d.polygon([(ax + 30, ay), (ax + 10, ay - 18), (ax + 10, ay + 18)], fill=rgba(STEEL, a))
    text(d, (x0 + wa + gap, y + 120), to, fb, WHITE, a)
    text(d, (W / 2, y + 362), how, F(SEMI, 42), BLUE, a, anchor="mm")

def segment(img, t, t0, chip=None, change=None, screens=(2,), lines=None):
    """Draws the app moment for t in [t0, t0 + APP_LEN]. Returns img."""
    if t < t0 or t > t0 + APP_LEN + 0.5: return img
    a = ease((t - t0) / 0.35)
    base = bg("glow")
    d = draw(base)
    # phone slides up
    u = ease((t - t0 - 0.05) / 0.55)
    py = round(lerp(H + 40, PHONE_Y, u))
    swap = t0 + 2.5 if len(screens) > 1 else None
    scr = screens[0] if swap is None or t < swap else screens[1]
    ph = phone(scr)
    base.paste(ph, (PHONE_BOX[0], py))
    if swap is not None and swap - 0.2 < t < swap + 0.2:
        # quick crossfade between the two screens
        k = clamp((t - (swap - 0.2)) / 0.4)
        other = phone(screens[0] if t >= swap else screens[1])
        blend = Image.blend(other, ph, k if t >= swap else 1 - k)
        base.paste(blend, (PHONE_BOX[0], py))
    d = draw(base)
    dy = py - PHONE_BOX[1]
    # tap on the symptom chip
    if chip:
        cx0, cy0, cx1, cy1 = CHIPS[chip]
        ta = ease((t - t0 - 1.1) / 0.15)
        if ta > 0:
            d.rounded_rectangle([cx0, cy0 + dy, cx1, cy1 + dy], radius=14, fill=rgba(BLUE, 0.35 * ta), outline=rgba(BLUE, ta), width=5)
            k = clamp((t - t0 - 1.1) / 0.5)
            if k < 1:
                cx, cy = (cx0 + cx1) / 2, (cy0 + cy1) / 2 + dy
                rr = 30 + 90 * k
                d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=rgba(WHITE, 0.8 * (1 - k)), width=6)
                d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=rgba(WHITE, 0.55 * (1 - k)))
    # captions
    l1, l2 = lines or (("TELL DIALED OFFROAD", "WHAT THE BIKE DID."), ("IT TELLS YOU WHICH CLICKER,", "WHICH WAY, HOW MANY."))
    c1 = win(t, t0 + 0.1, t0 + 2.3, 0.3, 0.25)
    c2 = ease((t - t0 - 2.3) / 0.3)
    for (s1, s2), ca, t_in in ((l1, c1, t0 + 0.1), (l2, c2, t0 + 2.3)):
        if ca <= 0: continue
        sz = 96
        while max(d.textlength(s1, font=F(DISPI, sz)), d.textlength(s2, font=F(DISPI, sz))) > W - 2 * M: sz -= 4
        stack(d, M, 250, [(s1, F(DISPI, sz), WHITE), (s2, F(DISPI, sz), BLUE)], t, t_in, a_out=ca)
    # the change card slides over the phone
    if change:
        ka = ease((t - t0 - 2.35) / 0.35)
        if ka > 0:
            d.rectangle([0, 470, W, H], fill=rgba(CARBON, 0.82 * ka))
            change_card(d, base, M - 20, 980 + round((1 - ka) * 120), ka, *change)
            na = ease((t - t0 - 3.1) / 0.3)
            text(d, (W / 2, 1490 + round((1 - ka) * 120)), "A starting point. Ride it, log it, adjust.", F(SEMI, 38), BODY, na, anchor="mm")
    return Image.blend(img, base, a) if a < 1 else base
