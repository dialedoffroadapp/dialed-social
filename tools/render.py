import os, sys, math
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")
OUT = os.path.join(BASE, "out")

W, H = 1080, 1350
M = 84                      # side margin
CARBON = (11, 12, 16)
PANEL = (21, 25, 32)
BORDER = (38, 43, 54)
BLUE = (29, 155, 240)
WHITE = (245, 247, 252)
STEEL = (138, 147, 166)
BODY = (201, 207, 218)

_cache = {}
def F(name, size):
    key = (name, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(os.path.join(FONTS, name + ".ttf"), size)
    return _cache[key]

DISPLAY = "BarlowCondensed-BlackItalic"
DISPLAY_UP = "BarlowCondensed-ExtraBold"
BODY_F = "Inter-Regular"
MED = "Inter-Medium"
SEMI = "Inter-SemiBold"
BOLD = "Inter-Bold"


def wrap(text, font, maxw):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            t = (cur + " " + w).strip()
            if font.getlength(t) <= maxw or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fit(text, fname, maxw, maxh, start, floor, lh):
    """Largest size from start down to floor whose wrapped block fits maxw x maxh."""
    for size in range(start, floor - 1, -4):
        font = F(fname, size)
        lines = wrap(text, font, maxw)
        if any(font.getlength(l) > maxw for l in lines):
            continue
        height = len(lines) * size * lh
        if height <= maxh:
            return font, lines, size
    font = F(fname, floor)
    return font, wrap(text, font, maxw), floor


def draw_block(d, x, y, lines, font, size, lh, fill):
    for l in lines:
        d.text((x, y), l, font=font, fill=fill, anchor="la")
        y += int(size * lh)
    return y


def tracked(d, x, y, text, font, fill, spacing):
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill, anchor="la")
        x += font.getlength(ch) + spacing
    return x


def chevrons(d, x, y, n=2, size=18, fill=BLUE, width=5):
    for i in range(n):
        ox = x + i * (size + 8)
        d.line([(ox, y - size), (ox + size, y), (ox, y + size)], fill=fill, width=width, joint="curve")


LOGO_DIR = os.path.join(BASE, "logo")
_marks = {}


def mark(theme="dark", height=56):
    """The real Dialed Offroad mark. theme: dark (white D, blue bars), white (all white), light (ink D, blue bars)."""
    key = (theme, height)
    if key not in _marks:
        im = Image.open(os.path.join(LOGO_DIR, f"mark_{theme}.png")).convert("RGBA")
        w = int(im.width * height / im.height)
        _marks[key] = im.resize((w, height), Image.LANCZOS)
    return _marks[key]


def wordmark(d, x, y, size, first, second):
    """DIALED in `first` color, OFFROAD in `second` color, on one line."""
    f = F(DISPLAY, size)
    d.text((x, y), "DIALED", font=f, fill=first, anchor="la")
    x2 = x + f.getlength("DIALED ") + size * 0.08
    d.text((x2, y), "OFFROAD", font=f, fill=second, anchor="la")
    return x2 + f.getlength("OFFROAD")


def brand_row(d, img=None, theme="dark"):
    if img is None:
        img = d._image
    m = mark("dark" if theme == "dark" else ("white" if theme == "blue" else "light"), 56)
    img.paste(m, (M, 70), m)
    if theme == "dark":
        wordmark(d, M + m.width + 22, 76, 40, WHITE, BLUE)
    elif theme == "blue":
        wordmark(d, M + m.width + 22, 76, 40, WHITE, CARBON)
    else:
        wordmark(d, M + m.width + 22, 76, 40, INK, BLUE)


INK = (11, 12, 16)


def footer(d, left_text=None, counter=None, swipe=False, key=None):
    y = H - 92
    fs = F(MED, 26)
    if swipe:
        txt = (left_text or "Swipe").upper()
        x = tracked(d, M, y - 14, txt, F(SEMI, 26), BLUE, 3)
        chevrons(d, x + 10, y, n=2, size=12, width=4)
    elif left_text:
        d.text((M, y - 14), left_text, font=fs, fill=STEEL, anchor="la")
    else:
        d.text((M, y - 14), "@dialed_offroad", font=fs, fill=STEEL, anchor="la")
    if counter:
        d.text((W - M, y - 14), counter, font=F(SEMI, 26), fill=STEEL, anchor="ra")


def new_canvas():
    img = Image.new("RGB", (W, H), CARBON)
    d = ImageDraw.Draw(img)
    # faint diagonal accent at the bottom right for texture
    d.polygon([(W, H - 420), (W, H), (W - 300, H)], fill=(14, 16, 22))
    brand_row(d, img)
    return img, d


# ---------------- slide types ----------------

def slide_hot(s, counter):
    img, d = new_canvas()
    maxw = W - 2 * M - 36
    font, lines, size = fit(s["head"], DISPLAY, maxw, 640, 156, 96, 0.98)
    hh = len(lines) * size * 0.98
    sub_font = F(MED, 40)
    sub_lines = wrap(s["sub"], sub_font, W - 2 * M - 36)
    sh = len(sub_lines) * 40 * 1.4
    total = hh + 56 + sh
    y = int((H - total) / 2) - 20
    # accent bar
    d.rectangle([M, y + 10, M + 12, y + hh - 10], fill=BLUE)
    draw_block(d, M + 36, y, lines, font, size, 0.98, WHITE)
    y2 = y + hh + 56
    draw_block(d, M + 36, y2, sub_lines, sub_font, 40, 1.4, BODY)
    footer(d)
    return img


def slide_cover(s, counter):
    img, d = new_canvas()
    y = 300
    if s.get("eyebrow"):
        tracked(d, M, y, s["eyebrow"], F(SEMI, 30), BLUE, 5)
        y += 70
    maxw = W - 2 * M
    font, lines, size = fit(s["head"], DISPLAY, maxw, 700, 172, 110, 0.96)
    y = draw_block(d, M, y, lines, font, size, 0.96, WHITE)
    if s.get("sub"):
        y += 30
        d.rectangle([M, y, M + 120, y + 6], fill=BLUE)
        y += 40
        f = F(MED, 42)
        draw_block(d, M, y, wrap(s["sub"], f, maxw), f, 42, 1.4, BODY)
    footer(d, left_text=s.get("footer"), counter=counter, swipe=(s.get("footer", "").lower().startswith("swipe")))
    return img


def slide_point(s, counter):
    img, d = new_canvas()
    y = 230
    if s.get("num"):
        d.text((M - 6, y), s["num"], font=F(DISPLAY, 200), fill=BLUE, anchor="la")
        y += 230
    elif s.get("tag"):
        tracked(d, M, y + 40, s["tag"], F(SEMI, 30), BLUE, 5)
        y += 130
    maxw = W - 2 * M
    font, lines, size = fit(s["head"], DISPLAY, maxw, 420, 112, 80, 0.96)
    y = draw_block(d, M, y, lines, font, size, 0.96, WHITE)
    y += 40
    d.rectangle([M, y, M + 120, y + 6], fill=BLUE)
    y += 44
    f = F(BODY_F, 40)
    draw_block(d, M, y, wrap(s["body"], f, maxw), f, 40, 1.42, BODY)
    footer(d, counter=counter)
    return img


def slide_symptom(s, counter):
    img, d = new_canvas()
    y = 210
    tracked(d, M, y, "SYMPTOM", F(SEMI, 30), STEEL, 5)
    y += 70
    maxw = W - 2 * M
    font, lines, size = fit(s["head"], DISPLAY, maxw, 330, 116, 84, 0.96)
    y = draw_block(d, M, y, lines, font, size, 0.96, WHITE)
    y += 48
    # panel
    pf = F(DISPLAY_UP, 60)
    fix_lines = wrap(s["fix"], pf, maxw - 2 * 48)
    ph = 48 + 40 + 16 + len(fix_lines) * 60 * 1.1 + 40
    d.rounded_rectangle([M, y, W - M, y + ph], radius=24, fill=PANEL, outline=BORDER, width=2)
    tracked(d, M + 48, y + 44, "START HERE", F(SEMI, 28), BLUE, 5)
    draw_block(d, M + 48, y + 104, fix_lines, pf, 60, 1.1, WHITE)
    y += ph + 44
    f = F(BODY_F, 36)
    draw_block(d, M, y, wrap(s["why"], f, maxw), f, 36, 1.42, BODY)
    footer(d, left_text="In = more damping.  Out = less.  One change at a time.", counter=counter)
    return img


def slide_table(s, counter):
    img, d = new_canvas()
    y = 176
    d.text((M, y), s["title"], font=F(DISPLAY, 100), fill=WHITE, anchor="la")
    y += 108
    if s.get("sub"):
        d.text((M, y), s["sub"], font=F(MED, 30), fill=STEEL, anchor="la")
        y += 58
    col_label_x = M + 28
    col_stock_x = W - M - 372
    col_dialed_x = W - M - 28
    hf = F(SEMI, 26)
    tracked(d, col_stock_x - 70, y, "STOCK", hf, STEEL, 4)
    tracked(d, col_dialed_x - 96, y, "DIALED", hf, BLUE, 4)
    y += 54
    row_h = 100
    lf = F(MED, 34)
    vf = F(DISPLAY_UP, 54)
    for i, (label, stock, dialed) in enumerate(s["rows"]):
        top = y + i * row_h
        if i % 2 == 0:
            d.rounded_rectangle([M, top, W - M, top + row_h - 8], radius=16, fill=PANEL, outline=BORDER, width=1)
        cy = top + (row_h - 8) // 2
        d.text((col_label_x, cy), label, font=lf, fill=BODY, anchor="lm")
        changed = stock.strip() != dialed.strip() and stock != "see manual"
        sf = vf if stock != "see manual" else F(MED, 28)
        d.text((col_stock_x, cy), stock, font=sf, fill=STEEL, anchor="mm")
        d.text((col_dialed_x, cy), dialed, font=vf, fill=(BLUE if changed else WHITE), anchor="rm")
        if changed:
            # small marker
            d.ellipse([col_dialed_x - vf.getlength(dialed) - 34, cy - 7, col_dialed_x - vf.getlength(dialed) - 20, cy + 7], fill=BLUE)
    y += len(s["rows"]) * row_h + 24
    if s.get("note"):
        f = F(BODY_F, 28)
        draw_block(d, M, y, wrap(s["note"], f, W - 2 * M), f, 28, 1.4, STEEL)
    footer(d, counter=counter)
    return img


def slide_points(s, counter):
    img, d = new_canvas()
    y = 196
    d.text((M, y), s["title"], font=F(DISPLAY, 104), fill=WHITE, anchor="la")
    y += 150
    hf = F(DISPLAY_UP, 50)
    bf = F(BODY_F, 34)
    maxw = W - 2 * M - 48
    for head, body in s["items"]:
        d.rectangle([M, y + 8, M + 10, y + 46], fill=BLUE)
        y = draw_block(d, M + 36, y, wrap(head, hf, maxw), hf, 50, 1.05, WHITE)
        y += 8
        y = draw_block(d, M + 36, y, wrap(body, bf, maxw), bf, 34, 1.4, BODY)
        y += 46
    footer(d, counter=counter)
    return img


def slide_closer(s, counter):
    img, d = new_canvas()
    maxw = W - 2 * M
    font, lines, size = fit(s["head"], DISPLAY, maxw, 520, 150, 96, 0.96)
    hh = len(lines) * size * 0.96
    sf = F(MED, 40)
    sub_lines = wrap(s.get("sub", ""), sf, maxw)
    sh = len(sub_lines) * 40 * 1.4 if s.get("sub") else 0
    cf = F(SEMI, 36)
    cta_lines = wrap(s["cta"], cf, maxw - 96) if s.get("cta") else []
    ch = (len(cta_lines) * 36 * 1.35 + 72) if cta_lines else 0
    total = hh + (46 + sh if sh else 0) + (56 + ch if ch else 0)
    y = int((H - total) / 2) - 30
    y = draw_block(d, M, y, lines, font, size, 0.96, WHITE)
    if sh:
        y += 46
        y = draw_block(d, M, y, sub_lines, sf, 40, 1.4, BODY)
    if ch:
        y += 56
        d.rounded_rectangle([M, y, W - M, y + ch], radius=22, fill=BLUE)
        draw_block(d, M + 48, y + 36, cta_lines, cf, 36, 1.35, WHITE)
    else:
        # pill button
        y += 64
        pf = F(DISPLAY_UP, 40)
        label = s.get("button", "GET THE APP  ·  LINK IN BIO")
        pw = int(pf.getlength(label)) + 96
        d.rounded_rectangle([M, y, M + pw, y + 92], radius=46, fill=BLUE)
        d.text((M + 48, y + 46), label, font=pf, fill=WHITE, anchor="lm")
    footer(d, left_text=s.get("footer"), counter=counter)
    return img


RENDER = {"hot": slide_hot, "cover": slide_cover, "point": slide_point,
          "symptom": slide_symptom, "table": slide_table, "points": slide_points, "closer": slide_closer}


def main():
    """Render a week module with the classic design only: python render.py weeks/<date>.py out/"""
    import importlib.util
    week_path = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else OUT
    spec = importlib.util.spec_from_file_location("week", week_path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    os.makedirs(out, exist_ok=True)
    total = 0
    for post in mod.WEEK:
        folder = os.path.join(out, post.get("slug") or post["folder"]); os.makedirs(folder, exist_ok=True)
        n = len(post["slides"])
        for i, s in enumerate(post["slides"], 1):
            img = RENDER[s["type"]](s, f"{i:02d} / {n:02d}" if n > 1 else None)
            img.save(os.path.join(folder, f"slide_{i:02d}.png"), optimize=True); total += 1
    print(total, "slides rendered")


if __name__ == "__main__":
    main()
