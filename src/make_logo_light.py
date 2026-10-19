# -*- coding: utf-8 -*-
"""Versión clara del logo para fondos oscuros: "EXPERIENCIAS" en crema, loto y Saori intactos."""
import os
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
im = Image.open(os.path.join(ROOT, "Logotipo Saori EXPERIENCIAS en acuarela.png")).convert("RGBA")
w, h = im.size
px = im.load()
CUT = 1109
for y in range(h):
    for x in range(CUT, w):
        r, g, b, a = px[x, y]
        if a:
            px[x, y] = (246, 232, 200, a)
im = im.crop(im.split()[3].point(lambda v: 255 if v > 40 else 0).getbbox())
im.save(os.path.join(ROOT, "web", "assets", "logo-light.png"))
print("ok", im.size)
