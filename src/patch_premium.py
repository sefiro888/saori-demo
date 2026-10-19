# -*- coding: utf-8 -*-
import os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def rd(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
def wr(p, t): open(os.path.join(ROOT, p), "w", encoding="utf-8").write(t)

# ---------- build.py ----------
b = rd("src/build.py")
if "lg-dark" not in b:
    b = b.replace('<a href="{prefix}index.html" class="brand" aria-label="Inicio"><img src="{prefix}assets/logo.png" alt="Saori Experiencias"></a>',
                  '<a href="{prefix}index.html" class="brand" aria-label="Inicio"><img class="lg-light" src="{prefix}assets/logo.png" alt="Saori Experiencias"><img class="lg-dark" src="{prefix}assets/logo-light.png" alt=""></a>')
    b = b.replace('<div class="foot-brand"><img src="{prefix}assets/logo.png" alt="Saori Experiencias">',
                  '<div class="foot-brand"><img src="{prefix}assets/logo-light.png" alt="Saori Experiencias">')
    b = b.replace('<link rel="stylesheet" href="{prefix}extra.css">', '<link rel="stylesheet" href="{prefix}extra.css">\n<link rel="stylesheet" href="{prefix}premium.css">')
    b = b.replace('<link rel="stylesheet" href="extra.css">', '<link rel="stylesheet" href="extra.css"><link rel="stylesheet" href="premium.css">')
    # escudo táctil en los embeds de Instagram
    b = b.replace('''<iframe title="{E(r["title"])}" loading="lazy" allowfullscreen allow="autoplay; encrypted-media; fullscreen; picture-in-picture"></iframe>')''',
                  '''<iframe title="{E(r["title"])}" loading="lazy" allowfullscreen allow="autoplay; encrypted-media; fullscreen; picture-in-picture"></iframe>'
                  f'<button class="reel-shield" type="button" aria-label="Reproducir: {E(r["title"])}"><span>Toca para reproducir</span></button>')''')
    wr("src/build.py", b)

# ---------- home.tpl.html : nueva presentación ----------
h = rd("src/home.tpl.html")
s = h.index("<!-- SPLASH -->")
e = h.index("<!-- /SPLASH -->") + len("<!-- /SPLASH -->") if "<!-- /SPLASH -->" in h else h.index("</div>\n", h.index('id="spSkip"')) + len("</div>\n")
new = '''<!-- SPLASH -->
<div class="splash" id="splash" aria-hidden="true">
  <div class="sp-panel sp-top"></div><div class="sp-panel sp-bot"></div>
  <canvas id="splashCv"></canvas>
  <div class="sp-frame"></div>
  <div class="sp-center">
    <div class="sp-logo"><img src="assets/lotus-saori.png" alt=""><i class="sp-shine"></i></div>
    <div class="sp-line"></div>
    <p class="sp-tag" id="spTag">Estética avanzada · Huelva</p>
  </div>
  <button class="sp-skip" id="spSkip" type="button">Entrar</button>
</div>
<!-- /SPLASH -->
'''
h = h[:s] + new + h[e:]
wr("src/home.tpl.html", h)
print("ok")
