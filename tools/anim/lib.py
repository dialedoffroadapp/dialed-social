"""Shared helpers for the Dialed Offroad animated reels. 1080x1920, 30 fps."""
import math, os, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ASSETS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # tools/
W, H, FPS = 1080, 1920, 30
M = 84  # side margin

CARBON = (11, 12, 16); PANEL = (21, 25, 32); BORDER = (38, 43, 54)
BLUE = (29, 155, 240); WHITE = (245, 247, 252); STEEL = (138, 147, 166)
BODY = (201, 207, 218); DIM = (90, 98, 115)
RED = (255, 77, 77); ORANGE = (255, 150, 40); GREEN = (52, 211, 120); YELLOW = (255, 204, 0)

DISP, DISPI, XB = "BarlowCondensed-Black", "BarlowCondensed-BlackItalic", "BarlowCondensed-ExtraBold"
BOLD, SEMI, MED, REG = "Inter-Bold", "Inter-SemiBold", "Inter-Medium", "Inter-Regular"

_f = {}
def F(name, size):
    k = (name, int(size))
    if k not in _f:
        _f[k] = ImageFont.truetype(f"{ASSETS}/fonts/{name}.ttf", int(size))
    return _f[k]

_marks = {}
def mark(h, kind="white"):
    k = (h, kind)
    if k not in _marks:
        m = Image.open(f"{ASSETS}/logo/mark_{kind}.png").convert("RGBA")
        _marks[k] = m.resize((round(m.width * h / m.height), h), Image.LANCZOS)
    return _marks[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_io(x): x = clamp(x); return x * x * (3 - 2 * x)
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, a): return tuple(round(c1[i] + (c2[i] - c1[i]) * clamp(a)) for i in range(3))
def rgba(c, a): return (c[0], c[1], c[2], max(0, min(255, round(255 * a))))
def win(t, t0, t1, fin=0.3, fout=0.3):
    """alpha that fades in at t0 and out at t1"""
    return min(ease((t - t0) / fin), 1 - ease((t - (t1 - fout)) / fout)) if t1 else ease((t - t0) / fin)

_bgs = {}
def bg(kind="glow"):
    if kind not in _bgs:
        base = Image.new("RGB", (W, H), CARBON)
        if kind == "glow":
            g = Image.new("RGB", (W, H), CARBON); gd = ImageDraw.Draw(g)
            gd.ellipse([W * 0.1, -H * 0.15, W * 1.3, H * 0.4], fill=(18, 62, 104))
            base = Image.blend(base, g.filter(ImageFilter.GaussianBlur(220)), 0.9)
        elif kind == "grid":
            g = Image.new("RGB", (W, H), CARBON); gd = ImageDraw.Draw(g)
            gd.ellipse([W * -0.2, H * 0.25, W * 1.2, H * 0.85], fill=(14, 40, 70))
            base = Image.blend(base, g.filter(ImageFilter.GaussianBlur(260)), 0.85)
            d = ImageDraw.Draw(base, "RGBA")
            for x in range(0, W, 60): d.line([x, 0, x, H], fill=(60, 120, 200, 14), width=1)
            for y in range(0, H, 60): d.line([0, y, W, y], fill=(60, 120, 200, 14), width=1)
        _bgs[kind] = base
    return _bgs[kind].copy()

def draw(img): return ImageDraw.Draw(img, "RGBA")

def text(d, xy, s, font, color, a=1.0, anchor="la", dy=0):
    if a <= 0: return
    d.text((xy[0], xy[1] + dy), s, font=font, fill=rgba(color, a), anchor=anchor)

def tracked(d, x, y, s, font, color, a=1.0, track=3, anchor="l"):
    if a <= 0: return 0
    ws = [d.textlength(ch, font=font) + track for ch in s]
    total = sum(ws) - track
    if anchor == "r": x -= total
    elif anchor == "m": x -= total / 2
    for ch, w in zip(s, ws):
        d.text((x, y), ch, font=font, fill=rgba(color, a)); x += w
    return total

def wrap(d, s, font, width):
    out, line = [], ""
    for w in s.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=font) <= width: line = t
        else: out.append(line); line = w
    if line: out.append(line)
    return out

def stack(d, x, y, lines, t, t0, stagger=0.12, rise=50, fade=0.35, a_out=1.0, anchor="la", lh=None):
    """lines: [(text, font, color)] each slides up in turn. returns bottom y."""
    for i, (s, fnt, col) in enumerate(lines):
        a = ease((t - t0 - i * stagger) / fade) * a_out
        h = lh or fnt.size * 0.98
        text(d, (x, y), s, fnt, col, a, anchor=anchor, dy=round((1 - ease((t - t0 - i * stagger) / fade)) * rise))
        y += h
    return y

def brand_row(img, a=1.0, y=118):
    if a <= 0: return
    m = mark(50)
    if a < 1:
        m = m.copy(); m.putalpha(m.getchannel("A").point(lambda v: round(v * a)))
    img.paste(m, (M, y), m)
    d = draw(img)
    text(d, (M + m.width + 16, y + 2), "DIALED", F(DISP, 46), WHITE, a)
    text(d, (M + m.width + 16 + d.textlength("DIALED ", font=F(DISP, 46)), y + 2), "OFFROAD", F(DISP, 46), BLUE, a)

def end_card(img, t, t0, head=("GET YOUR", "STARTING POINT."), sub=("Your bike. Your weight. Your track.",), cta="On iPhone and Android. Link in bio."):
    """Fades a full closing card over img starting at t0."""
    a = ease((t - t0) / 0.4)
    if a <= 0: return img
    card = bg("glow"); d = draw(card)
    y = 560
    sz = 170
    while max(d.textlength(h, font=F(DISPI, sz)) for h in head) > W - 2 * M and sz > 80: sz -= 4
    y = stack(d, M, y, [(head[0], F(DISPI, sz), WHITE), (head[1], F(DISPI, sz), BLUE)], t, t0 + 0.1, rise=60)
    y += 40
    stack(d, M, y, [(s, F(SEMI, 46), BODY) for s in sub], t, t0 + 0.45, lh=64)
    b = ease((t - t0 - 0.9) / 0.4)
    if b > 0:
        m = mark(104); mm = m.copy(); mm.putalpha(m.getchannel("A").point(lambda v: round(v * b)))
        card.paste(mm, (M, 1250), mm)
        text(d, (M + m.width + 26, 1250), "DIALED OFFROAD", F(DISP, 78), WHITE, b)
        text(d, (M + m.width + 26, 1338), cta, F(MED, 32), STEEL, b)
    return Image.blend(img, card, a) if a < 1 else card

def keys(t, ks):
    """ks: [(time, value[, 'lin'])] interpolated with smoothstep (or linear when the target key says 'lin')."""
    if t <= ks[0][0]: return ks[0][1]
    for a, b in zip(ks, ks[1:]):
        if t <= b[0]:
            u = (t - a[0]) / (b[0] - a[0])
            return lerp(a[1], b[1], u if len(b) > 2 and b[2] == "lin" else ease_io(u))
    return ks[-1][1]

def chip(d, x, y, s, color, a=1.0, fg=CARBON, size=30):
    if a <= 0: return 0
    f = F(BOLD, size); w = d.textlength(s, font=f) + size * 1.3 + len(s) * 2
    d.rounded_rectangle([x, y, x + w, y + size * 1.75], radius=size, fill=rgba(color, a))
    tracked(d, x + size * 0.65, y + size * 0.36, s, f, fg, a, track=2)
    return w

def caption(d, t, t0, t1, tag, tag_col, body, y=250, size=78, col=WHITE, width=None):
    """chip + wrapped headline that slides in at t0 and fades by t1."""
    a = win(t, t0, t1, 0.3, 0.25)
    if a <= 0: return
    chip(d, M, y + round((1 - ease((t - t0) / 0.3)) * 30), tag, tag_col, a)
    lines = wrap(d, body, F(XB, size), width or W - 2 * M)
    stack(d, M, y + 80, [(l, F(XB, size), col) for l in lines], t, t0 + 0.12, stagger=0.08, a_out=a, lh=size * 1.02)

def shake(t, t0, dur=0.35, amp=14, freq=38):
    k = (t - t0) / dur
    if k < 0 or k > 1: return 0, 0
    e = (1 - k) ** 2 * amp
    return round(math.sin(t * freq) * e), round(math.cos(t * freq * 1.3) * e * 0.6)

def render(frame_fn, dur, out):
    """frame_fn(t) -> RGB PIL image. Encodes to out (temp name, rename on success)."""
    n = round(dur * FPS)
    tmp = out[:-4] + ".part.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                          "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
    for k in range(n):
        p.stdin.write(frame_fn(k / FPS).tobytes())
    p.stdin.close()
    if p.wait() != 0: raise SystemExit("ffmpeg failed")
    os.replace(tmp, out)

def stills(frame_fn, times, out_png):
    ims = [frame_fn(t).resize((432, 768)) for t in times]
    sheet = Image.new("RGB", (432 * len(ims), 768))
    for i, im in enumerate(ims): sheet.paste(im, (i * 432, 0))
    sheet.save(out_png)

# ---------- sound ----------
SR = 44100
class Track:
    def __init__(self, dur, seed=1):
        self.n = int(SR * dur); self.a = np.zeros(self.n); self.dur = dur
        self.t = np.arange(self.n) / SR; self.rng = np.random.default_rng(seed)
    def _add(self, at, sig):
        i = int(at * SR); j = min(self.n, i + len(sig))
        if i < self.n: self.a[i:j] += sig[: j - i]
    def pad(self, notes=(55, 82.4, 110), amp=0.16, pulse=2.0, fade_in=1.2):
        t = self.t; s = sum(np.sin(2 * np.pi * f * t) * w for f, w in zip(notes, (0.5, 0.3, 0.15, 0.1)))
        env = np.clip(t / fade_in, 0, 1) * np.clip((self.dur - t) / 1.0, 0, 1) * (0.75 + 0.25 * np.sin(2 * np.pi * t * pulse))
        self.a += s * env * amp
    def beat(self, bpm=120, start=0.0, end=None, amp=0.18):
        end = end or self.dur - 1.0; step = 60 / bpm; x = start
        while x < end: self.thump(x, amp, 0.18); x += step
    def thump(self, at, amp=0.6, length=0.25):
        k = np.arange(int(length * SR)) / SR
        self._add(at, amp * np.sin(2 * np.pi * (55 + 90 * np.exp(-k * 30)) * k) * np.exp(-k * 14))
    def click(self, at, amp=0.5, f=2400):
        k = np.arange(int(0.03 * SR)) / SR
        self._add(at, amp * np.sin(2 * np.pi * f * k) * np.exp(-k * 180) + amp * 0.5 * self.rng.uniform(-1, 1, len(k)) * np.exp(-k * 300))
    def tick(self, at, amp=0.25): self.click(at, amp, 4200)
    def whoosh(self, at, amp=0.35, length=0.45, up=True):
        L = int(length * SR); k = np.arange(L) / SR; noise = self.rng.uniform(-1, 1, L)
        # crude band shaping: moving average of noise
        # soft air: heavy smoothing (dull, low hiss) and much quieter than the other effects
        for win_ in (40, 40):
            noise = np.convolve(noise, np.ones(win_) / win_, mode="same")
        noise /= (np.max(np.abs(noise)) + 1e-9)
        env = np.sin(np.pi * np.clip(k / length, 0, 1)) ** 2
        self._add(at, amp * 0.22 * noise * env)
    def slam(self, at, amp=0.9):
        self.thump(at, amp, 0.4)
        L = int(0.25 * SR); k = np.arange(L) / SR
        self._add(at, amp * 0.25 * self.rng.uniform(-1, 1, L) * np.exp(-k * 40))
    def ding(self, at, f=880, amp=0.25):
        k = np.arange(int(0.6 * SR)) / SR
        self._add(at, amp * (np.sin(2 * np.pi * f * k) + 0.4 * np.sin(2 * np.pi * f * 2 * k)) * np.exp(-k * 6))
    def hum(self, t0, t1, f=70, amp=0.12):
        L = int((t1 - t0) * SR); k = np.arange(L) / SR
        env = np.clip(k / 0.2, 0, 1) * np.clip(((t1 - t0) - k) / 0.2, 0, 1)
        sig = (np.sin(2 * np.pi * f * k) + 0.5 * np.sign(np.sin(2 * np.pi * f * 2 * k)) * 0.3) * env * amp
        self._add(t0, sig)
    def save(self, path):
        a = self.a / (np.max(np.abs(self.a)) + 1e-9) * 0.85
        w = wave.open(path, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((a * 32767).astype(np.int16).tobytes()); w.close()

def mux(video, wav, out):
    tmp = out[:-4] + ".part.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", tmp], check=True)
    os.replace(tmp, out)
