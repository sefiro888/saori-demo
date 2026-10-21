# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "data-open" not in b:
    b = b.replace('<span>Toca para reproducir</span>', '<span>Ver a pantalla completa</span>')
    b = b.replace('<span class="rp-cta">Ver en TikTok</span>', '<span class="rp-cta">Ver a pantalla completa</span>')
    b = b.replace('''return f\'\'\'<article class="reel"{attr} data-net="{r["net"]}">''',
                  '''return f\'\'\'<article class="reel"{attr} data-net="{r["net"]}" data-open="{R.embed(r)}" data-link="{R.url(r)}" data-title="{E(r["title"])}">''')
    open(p, "w", encoding="utf-8").write(b)
print("ok" if "data-open" in b else "FALLO")
