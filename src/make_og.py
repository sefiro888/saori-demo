# -*- coding: utf-8 -*-
"""Imagen para compartir (WhatsApp, redes): 1200x630 con el logo de Saori sobre fondo ciruela."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
W, H = 1200, 630

# fondo: degradado ciruela con brillo dorado
bg = Image.new("RGB", (W, H), (16, 6, 20))
px = bg.load()
for y in range(H):
    for x in range(W):
        dx, dy = (x - 380) / 700, (y - 300) / 520
        d = min(1, (dx * dx + dy * dy) ** .5)
        r = int(58 - 42 * d); g = int(20 - 14 * d); b = int(74 - 54 * d)
        px[x, y] = (max(r, 12), max(g, 5), max(b, 16))
glow = Image.new("RGB", (W, H), (0, 0, 0))
ImageDraw.Draw(glow).ellipse((60, 40, 700, 600), fill=(120, 80, 20))
glow = glow.filter(ImageFilter.GaussianBlur(110))
from PIL import ImageChops
bg = ImageChops.add(bg, glow.point(lambda v: int(v * .55)))

# logo (loto + Saori)
logo = Image.open(os.path.join(ROOT, "assets", "lotus-saori.png")).convert("RGBA")
lh = 470
logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
bg = bg.convert("RGBA")
bg.alpha_composite(logo, (70, (H - lh) // 2 - 6))

# marco fino dorado
d = ImageDraw.Draw(bg)
d.rectangle((22, 22, W - 22, H - 22), outline=(233, 196, 106, 90), width=1)

def font(names, size):
    for n in names:
        for base in ("C:/Windows/Fonts/",):
            p = base + n
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

serif = font(["georgia.ttf", "times.ttf"], 54)
serif_i = font(["georgiai.ttf", "timesi.ttf"], 32)
sans = font(["segoeui.ttf", "arial.ttf"], 24)
sansb = font(["segoeuib.ttf", "arialbd.ttf"], 24)

x0 = 720
d.text((x0, 190), "Centro de Estética", font=serif, fill=(255, 255, 255, 255))
d.text((x0, 252), "Avanzada Saori", font=serif, fill=(233, 196, 106, 255))
d.line((x0, 340, x0 + 120, 340), fill=(233, 196, 106, 255), width=2)
d.text((x0, 362), "Diagnóstico facial a medida", font=serif_i, fill=(246, 232, 200, 255))
d.text((x0, 410), "Tratamientos faciales y corporales,", font=sans, fill=(220, 205, 230, 255))
d.text((x0, 444), "depilación IPL · Huelva", font=sans, fill=(220, 205, 230, 255))
d.text((x0, 520), "5,0 en Google · 75 opiniones", font=sansb, fill=(233, 196, 106, 255))

out = os.path.join(ROOT, "assets", "og-saori.jpg")
bg.convert("RGB").save(out, quality=86, optimize=True)
print("ok", os.path.getsize(out) // 1024, "KB")
