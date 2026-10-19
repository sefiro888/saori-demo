# -*- coding: utf-8 -*-
"""Regenera assets/lotus.png: loto + "Saori" completo (sin la palabra EXPERIENCIAS)."""
import os
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
src = os.path.join(ROOT, "Logotipo Saori EXPERIENCIAS en acuarela.png")
im = Image.open(src).convert("RGBA")
a = im.split()[3].point(lambda v: 255 if v > 40 else 0)
w, h = im.size
cols = [a.crop((x, 0, x + 1, h)).getbbox() is not None for x in range(w)]
# primer hueco vertical ancho (>=12 px) tras x=800: separa "Saori" de "EXPERIENCIAS"
cut = None
x = 800
while x < w - 12:
    if not any(cols[x:x + 12]):
        cut = x
        break
    x += 1
print("size", im.size, "cut", cut)
box = a.crop((0, 0, cut, h)).getbbox()
crop = im.crop((box[0], box[1], box[2], box[3]))
out = os.path.join(ROOT, "web", "assets", "lotus-saori.png")
crop.save(out)
print("saved", crop.size)
