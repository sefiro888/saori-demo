# -*- coding: utf-8 -*-
"""Pósters de Instagram + nuevo diseño de reels (móviles inclinados, anillo PLAY REEL, ecualizador)."""
import os
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
T = "C:/Users/sefir/.claude/projects/C--Users-sefir-Desktop-demostraciones-Centro-Est-tica-Avanzada-Saori/360ff432-5df9-494f-8a16-5a6a53979d64/tool-results/mcp-claude-in-chrome-blob-"
M = {"ig-coctel": "1792570310271-wk3d6q", "ig-hidrafacial": "1792570317745-eo3vir", "ig-diapasones": "1792570324789-ei3w45",
     "ig-diamante": "1792570335051-0kt96s", "ig-historia": "1792570344188-85iket", "ig-rf": "1792570353120-p7d5xy"}
for k, v in M.items():
    p = os.path.join(ROOT, "assets", "reels", k + ".jpg")
    if os.path.exists(p):
        continue
    im = Image.open(T + v + ".png").convert("RGB")
    im = im.crop((0, 0, im.width, im.height - 50))
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    im.save(p, quality=88)
    print("poster", k, im.size)

# ---- build.py: nueva tarjeta ----
bp = os.path.join(ROOT, "src", "build.py")
b = open(bp, encoding="utf-8").read()
if "reel-ring" not in b:
    s = b.index("def reel_card(key):")
    e = b.index("def reels_home():")
    new = '''def reel_card(key, tilt=""):
    r = R.REELS[key]
    net = "Instagram" if r["net"] == "ig" else "TikTok"
    handle = "@esteticasaori" if r["net"] == "ig" else "@esteticarocioguti"
    uid = "rc" + key.replace("-", "")
    ring = (f'<span class="reel-ring" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="{uid}" d="M60,60 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>'
            f'<text><textPath href="#{uid}">PLAY REEL · PLAY REEL · PLAY REEL · </textPath></text></svg>'
            f'<i><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></i></span>')
    return f\'\'\'<figure class="reel {tilt}" data-net="{r["net"]}" data-open="{R.embed(r)}" data-link="{R.url(r)}" data-title="{E(r["title"])}">
  <div class="phone">
    <span class="phone-notch" aria-hidden="true"></span>
    <span class="reel-credit"><b>Saori</b><i>{handle}</i></span>
    <button type="button" class="reel-play" aria-label="Reproducir el reel: {E(r["title"])}">
      <img src="assets/reels/{key}.jpg" alt="" loading="lazy">
      {ring}
      <span class="reel-eq" aria-hidden="true"><b></b><b></b><b></b><b></b></span>
      <span class="reel-meta"><em><i class="rec"></i> Reel · {net}</em><strong>{E(r["title"])}</strong><small>▶ {r["views"]} visualizaciones</small></span>
    </button>
  </div>
  <figcaption><strong class="reel-by">Reel de <a href="{R.url(r)}" target="_blank" rel="noopener">Saori</a></strong><span>{E(r["desc"])}</span>
    <a class="link-arrow" href="{R.url(r)}" target="_blank" rel="noopener">Ver en {net}</a></figcaption>
</figure>\'\'\'

def tilted(keys):
    return "".join(reel_card(k, "tilt-l" if i % 2 == 0 else "tilt-r") for i, k in enumerate(keys))

'''
    b = b[:s] + new + b[e:]
    b = b.replace('cards = "".join(reel_card(k) for k in R.HOME)', 'cards = tilted(R.HOME)')
    b = b.replace('cards = "".join(reel_card(k) for k in keys)', 'cards = tilted(keys)')
    b = b.replace('<section class="sec reels-sec" id="reels">\n  <div class="wrap">', '<section class="sec reels-sec" id="reels">\n  <span class="reel-bg-text" aria-hidden="true">REELS</span>\n  <div class="wrap">')
    b = b.replace('<div class="rail" id="rail">', '<div class="rail reel-row" id="rail">')
    b = b.replace('<div class="reels-grid n{len(keys)}">', '<div class="reels-grid reel-row n{len(keys)}">')
    b = b.replace('<section class="sec reels-sec" id="reels"><div class="wrap">\n  <div class="head reveal"><p class="eyebrow">Mírala en acción</p><h2>{E(name)}', '<section class="sec reels-sec" id="reels"><span class="reel-bg-text" aria-hidden="true">REELS</span><div class="wrap">\n  <div class="head reveal"><p class="eyebrow">Mírala en acción</p><h2>{E(name)}')
    open(bp, "w", encoding="utf-8").write(b)

# ---- reels.py: 8 en portada ----
rp = os.path.join(ROOT, "src", "reels.py")
r = open(rp, encoding="utf-8").read()
import re
r = re.sub(r'HOME = \[.*?\]', 'HOME = ["ig-diamante", "tt-acne", "ig-rf", "tt-manchas", "ig-diapasones", "tt-hifu", "ig-coctel", "tt-kinesio"]', r, count=1)
open(rp, "w", encoding="utf-8").write(r)

# ---- viewer.js: engancha el botón .reel-play ----
vp = os.path.join(ROOT, "viewer.js")
v = open(vp, encoding="utf-8").read()
v = v.replace("const shield = $('.reel-shield', c), poster = $('.reel-poster', c);\n    if (shield) shield.addEventListener('click', e => { e.preventDefault(); open(c); });\n    if (poster) poster.addEventListener('click', e => { if (e.metaKey || e.ctrlKey) return; e.preventDefault(); open(c); });",
              "const btn = $('.reel-play', c);\n    if (btn) btn.addEventListener('click', e => { e.preventDefault(); open(c); });")
v = v.replace("const im = $('img', c); ttImg.src", "const im = $('.reel-play img', c); ttImg.src")
open(vp, "w", encoding="utf-8").write(v)
print("ok", "reel-play" in v)
