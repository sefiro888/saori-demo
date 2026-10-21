# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://sefiro888.github.io/saori-demo/"
IMG = BASE + "assets/og-saori.jpg"
HOME_T = "Centro de Estética Avanzada Saori · Huelva"
HOME_D = "Diagnóstico facial personalizado y tratamientos faciales y corporales con la última tecnología: HIFU 12D, dermapen, radiofrecuencia, depilación IPL y más. ★ 5,0 en Google. Pide tu cita."

# imagen: línea más corta
m = os.path.join(ROOT, "src", "make_og.py")
t = open(m, encoding="utf-8").read().replace("Valoración 5,0 en Google · 75 opiniones", "5,0 en Google · 75 opiniones")
open(m, "w", encoding="utf-8").write(t)

# ---- build.py: metadatos en las páginas de servicio ----
p = os.path.join(ROOT, "src", "build.py")
b = open(p, encoding="utf-8").read()
if "og:image" not in b:
    og = '''<meta name="theme-color" content="#1b0b22">
<link rel="canonical" href="https://sefiro888.github.io/saori-demo/{{slug}}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Estética Avanzada Saori · Huelva">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="https://sefiro888.github.io/saori-demo/{{slug}}">
<meta property="og:image" content="%s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Logo de Estética Avanzada Saori, Huelva">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="%s">
<link rel="apple-touch-icon" href="{prefix}assets/lotus-saori.png">
''' % (IMG, IMG)
    # head(title, desc, prefix) recibe el nombre de archivo mediante un parámetro opcional
    b = b.replace("def head(title, desc, prefix=\"\"):", "def head(title, desc, prefix=\"\", slug=\"\"):")
    b = b.replace('<link rel="icon" href="{prefix}assets/lotus-saori.png">', '<link rel="icon" href="{prefix}assets/lotus-saori.png">\n' + og.replace("{{slug}}", "{slug}"))
    b = b.replace("{head(f\"{sv['name']} en Huelva · Estética Avanzada Saori\", sv[\"tagline\"])}", "{head(f\"{sv['name']} en Huelva · Estética Avanzada Saori\", sv[\"tagline\"], slug=s + '.html')}")
    open(p, "w", encoding="utf-8").write(b)

# ---- home.tpl.html ----
h = os.path.join(ROOT, "src", "home.tpl.html")
t = open(h, encoding="utf-8").read()
if "og:image" not in t:
    meta = '''<link rel="canonical" href="%s">
<meta name="theme-color" content="#1b0b22">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Estética Avanzada Saori · Huelva">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Logo de Estética Avanzada Saori, Huelva">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s">
<link rel="apple-touch-icon" href="assets/lotus-saori.png">
''' % (BASE, HOME_T, HOME_D, BASE, IMG, HOME_T, HOME_D, IMG)
    t = t.replace('<link rel="icon" href="assets/lotus-saori.png">', '<link rel="icon" href="assets/lotus-saori.png">\n' + meta, 1)
    t = t.replace("<title>Estética Avanzada Saori · Huelva</title>", "<title>%s</title>" % HOME_T, 1)
    open(h, "w", encoding="utf-8").write(t)
print("ok")
