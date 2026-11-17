#!/usr/bin/env python3
"""og.png 1200x630 — Cocos Locos (2x supersample).
Poster share art: deep sea-teal field with dot grain, halved coconut right,
DIN Condensed caps masthead in coconut cream, coral eyebrow and rule.
Shop identity only — no builder markers, no photo claims."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

TEAL = (12, 42, 37); TEAL2 = (18, 63, 54); GRAIN = (24, 74, 63)
CREAM = (246, 239, 223); CORAL = (223, 83, 48); AMBER = (243, 197, 126)
SHELL = (74, 45, 25); SHELL2 = (93, 59, 34); MUTE = (157, 184, 172)

def font(paths, size):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

disp = lambda s: font(["DIN Condensed Bold.ttf", "Avenir Next Condensed Bold.ttf", "Avenir Next Condensed.ttc", "Futura.ttc"], s)
body = lambda s: font(["Avenir Next.ttc", "HelveticaNeue.ttc", "Helvetica.ttc"], s)

img = Image.new("RGB", (W * S, H * S), TEAL)
d = ImageDraw.Draw(img)
px = lambda x, y: (int(x * S), int(y * S))

# dot grain field
r = 2
step = 34
for yy in range(20, H - 10, step):
    off = (step // 2) if (yy // step) % 2 else 0
    for xx in range(10 + off, W - 10, step):
        d.ellipse([px(xx - r, yy - r), px(xx + r, yy + r)], fill=GRAIN)

# subtle vertical gradient of depth: lighter band low-left
for yy in range(H // 2, H, 6):
    a = (yy - H // 2) / (H // 2)
    d.rectangle([0, yy, W, yy + 6], fill=(
        int(TEAL[0] + (TEAL2[0] - TEAL[0]) * a * 0.5),
        int(TEAL[1] + (TEAL2[1] - TEAL[1]) * a * 0.5),
        int(TEAL[2] + (TEAL2[2] - TEAL[2]) * a * 0.5)))

def tracked(x, y, text, fnt, fill, sp):
    cx = x * S
    for ch in text:
        d.text((cx, y * S), ch, font=fnt, fill=fill)
        cx += d.textlength(ch, font=fnt) + sp * S

def left(x, y, text, fnt, fill):
    d.text((x * S, y * S), text, font=fnt, fill=fill)

# text block (left)
tracked(72, 118, "OPENING SOON · LAKELAND, FL", disp(27), CORAL, 3.2)
tracked(70, 158, "COCOS LOCOS", disp(112), CREAM, 2.0)
w_mast = sum(d.textlength(ch, font=disp(112)) for ch in "COCOS LOCOS") + 2.0 * S * (len("COCOS LOCOS") - 1)
left(72, 158 + 130, "MEXICAN KITCHEN · SEAFOOD & COCKTAILS", body(25), AMBER)
left(72, 158 + 168, "IN COCONUTS — PLATES AND CUPS", body(25), CREAM)
d.rectangle([72 * S, 428 * S, (72 + 430) * S, (428 + 4) * S], fill=CORAL)
left(72, 452, "1313 N Combee Rd · Lakeland, FL 33801", body(23), MUTE)
left(72, 486, "Cocktails until 3 on weekends · about 176 seats", body(23), MUTE)

# coconut (right)
cx, cy = 952, 315
d.ellipse([px(cx - 226, cy - 226), px(cx + 226, cy + 226)], fill=(16, 52, 45))          # halo
d.ellipse([px(cx - 180, cy - 180), px(cx + 180, cy + 180)], fill=SHELL)                  # shell
d.pieslice([px(cx - 180, cy - 180), px(cx + 180, cy + 180)], 180, 360, fill=SHELL2)      # top arc
d.ellipse([px(cx - 129, cy - 129), px(cx + 129, cy + 129)], fill=CREAM)                  # flesh
for hx, hy in [(-43, -62), (43, -62), (0, -27)]:                                          # sprout holes
    d.ellipse([px(cx + hx - 10, cy + hy - 10), px(cx + hx + 10, cy + hy + 10)], fill=SHELL)

# fine frame
d.rectangle([16, 16, (W - 16) * S, (H - 16) * S], outline=(30, 78, 68), width=2 * S)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, "PNG", optimize=True)
print("og.png", img.size, os.path.getsize(OUT), "bytes")
