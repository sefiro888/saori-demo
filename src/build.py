# -*- coding: utf-8 -*-
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from data import SERVICES, BY_SLUG, MENU_GROUPS, WA
import voice
voice.apply(SERVICES)
import reels as R

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
E = html.escape

def wa(msg):
    from urllib.parse import quote
    return WA + quote(msg)

DIAG = wa("Hola, quiero pedir mi diagnóstico facial")

def ticker_items():
    items = ["✦ Pide tu diagnóstico facial sin ningún compromiso", "★ 5,0 en Google · 75 opiniones",
             "✦ Edición limitada: Protocolo Dermapen Total Face &amp; Lips", "✦ Depilación IPL desde 10 €",
             "✦ C/ Diego de Almagro 15, local · Huelva", "✦ HIFU 12D · Diatermia · Radiofrecuencia fraccionada", "☎ 654 76 73 32"]
    return "".join(f"<span>{i}</span>" for i in items * 2)

def header(prefix="", dark=False):
    # menú de escritorio (mega menú)
    cols = ""
    n = 0
    for title, slugs in MENU_GROUPS:
        links = ""
        for s in slugs:
            sv = BY_SLUG[s]
            n += 1
            links += (f'<a class="mlink" style="--d:{n}" href="{prefix}{s}.html"><img src="{prefix}assets/{sv["img"]}" alt="" loading="lazy">'
                      f'<span><b>{E(sv["name"])}</b><small>{E(sv["accent"])}</small></span></a>')
        cols += f'<div class="mcol"><h4>{E(title)}</h4>{links}</div>'
    mega = f'''<div class="mega" role="menu"><div class="mega-in">
      <div class="mcols">{cols}</div>
      <a class="mfeat" href="{DIAG}" target="_blank" rel="noopener">
        <img src="{prefix}assets/emblema.jpg" alt="">
        <div><em>Todo empieza aquí</em><b>Diagnóstico facial</b><span>Sin ningún compromiso. Te aconsejamos el plan exacto para tu piel.</span><i>Reservar ahora →</i></div>
      </a></div></div>'''
    # menú móvil
    m_acc = ""
    for title, slugs in MENU_GROUPS:
        m_acc += f'<p class="m-sub">{E(title)}</p>' + "".join(f'<a href="{prefix}{s}.html">{E(BY_SLUG[s]["name"])}</a>' for s in slugs)
    return f'''<div class="progress" id="progress"></div>
<div class="site-top{' is-dark' if dark else ''}" id="siteTop">
  <div class="topbar" aria-label="Información destacada"><div class="ticker"><div class="ticker-track">{ticker_items()}</div></div></div>
  <header class="hdr" id="hdr"><div class="hdr-in">
    <a href="{prefix}index.html" class="brand" aria-label="Inicio"><img class="lg-light" src="{prefix}assets/logo.png" alt="Saori Experiencias"><img class="lg-dark" src="{prefix}assets/logo-light.png" alt=""></a>
    <nav class="dnav" aria-label="Principal">
      <a href="{prefix}index.html#diagnostico">Diagnóstico</a>
      <div class="has-mega" id="hasMega">
        <button class="mega-btn" aria-expanded="false" aria-haspopup="true">Tratamientos <svg width="11" height="11" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
        {mega}
      </div>
      <a href="{prefix}index.html#reels">Reels</a>
      <a href="{prefix}index.html#resultados">Resultados</a>
      <a href="{prefix}depilacion-ipl.html">Depilación</a>
      <a href="{prefix}index.html#opiniones">Opiniones</a>
      <a href="{prefix}index.html#visitanos">Contacto</a>
    </nav>
    <a class="btn btn-gold hdr-cta" href="{DIAG}" target="_blank" rel="noopener"><span>Pedir cita</span></a>
    <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
  </div></header>
</div>
<div class="mnav" id="mnav" aria-hidden="true">
  <div class="mnav-in">
    <a href="{prefix}index.html#diagnostico" style="--i:1">Diagnóstico</a>
    <button class="m-acc" id="mAcc" style="--i:2" aria-expanded="false">Tratamientos <i>+</i></button>
    <div class="m-panel" id="mPanel"><div>{m_acc}</div></div>
    <a href="{prefix}index.html#reels" style="--i:3">Reels</a>
    <a href="{prefix}index.html#resultados" style="--i:3">Resultados</a>
    <a href="{prefix}depilacion-ipl.html" style="--i:4">Depilación</a>
    <a href="{prefix}index.html#opiniones" style="--i:5">Opiniones</a>
    <a href="{prefix}index.html#visitanos" style="--i:6">Contacto</a>
    <a class="btn btn-gold m-cta" href="{DIAG}" target="_blank" rel="noopener" style="--i:7">Pedir mi diagnóstico</a>
    <p class="m-contact" style="--i:8">☎ 654 76 73 32 · C/ Diego de Almagro 15, Huelva</p>
  </div>
</div>'''

def footer(prefix=""):
    cols = ""
    for title, slugs in MENU_GROUPS:
        cols += f'<div><h4>{E(title)}</h4>' + "".join(f'<a href="{prefix}{s}.html">{E(BY_SLUG[s]["name"])}</a>' for s in slugs) + '</div>'
    return f'''<footer class="footer">
  <div class="foot-in">
    <div class="foot-brand"><img src="{prefix}assets/logo-light.png" alt="Saori Experiencias">
      <p>En Centro de Estética Avanzada Saori te ayudamos a cuidar tu piel. Lo último en tratamientos faciales con las últimas tecnologías.</p>
      <div class="foot-soc"><a href="https://www.instagram.com/esteticasaori/" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@esteticarocioguti" target="_blank" rel="noopener">TikTok</a><a href="https://www.facebook.com/esteticasaorihuelva" target="_blank" rel="noopener">Facebook</a></div></div>
    {cols}
    <div><h4>Visítanos</h4><p>C/ Diego de Almagro, 15 · local<br>21002 Huelva</p><p><a href="tel:+34654767332">654 76 73 32</a></p>
      <p class="foot-h">Lun y Mié 9–14 · 16–19<br>Mar, Jue y Vie 9–14:30<br>Sáb y Dom cerrado</p></div>
  </div>
  <small>© <span id="yr"></span> Estética Avanzada Saori · Huelva · Demo de diseño</small>
</footer>
<a class="wa-float" href="{DIAG}" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 3a13 13 0 0 0-11 19.8L3 29l6.4-2A13 13 0 1 0 16 3zm0 2.4a10.6 10.6 0 1 1-5.6 19.6l-.4-.2-3.8 1.2 1.2-3.7-.3-.4A10.6 10.6 0 0 1 16 5.4zm-3.7 5.2c-.3 0-.7.1-1 .5-.4.4-1.4 1.4-1.4 3.3s1.4 3.8 1.6 4.1c.2.3 2.8 4.4 6.9 6 3.4 1.3 4.1 1 4.8.9.8-.1 2.4-1 2.7-2 .3-.9.3-1.7.2-1.9-.1-.2-.4-.3-.8-.5l-2.5-1.2c-.3-.1-.6-.2-.8.2-.3.4-1 1.2-1.2 1.4-.2.2-.4.3-.8.1-.4-.2-1.6-.6-3-1.9-1.1-1-1.9-2.3-2.1-2.7-.2-.4 0-.6.2-.8l.6-.7c.2-.2.2-.4.4-.6.1-.2.1-.5 0-.7l-1.1-2.7c-.3-.7-.6-.6-.8-.6z"/></svg>
</a>
<script src="{prefix}app.js"></script>
<script src="{prefix}premium.js"></script>
<script src="{prefix}viewer.js"></script>'''

def head(title, desc, prefix=""):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="{prefix}assets/lotus-saori.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Great+Vibes&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css">
<link rel="stylesheet" href="{prefix}site.css">
<link rel="stylesheet" href="{prefix}extra.css">
<link rel="stylesheet" href="{prefix}premium.css">
<link rel="stylesheet" href="{prefix}viewer.css">
<link rel="stylesheet" href="{prefix}reelstyle.css">
</head>'''


def reel_card(key, tilt=""):
    r = R.REELS[key]
    net = "Instagram" if r["net"] == "ig" else "TikTok"
    handle = "@esteticasaori" if r["net"] == "ig" else "@esteticarocioguti"
    uid = "rc" + key.replace("-", "")
    ring = (f'<span class="reel-ring" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="{uid}" d="M60,60 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>'
            f'<text><textPath href="#{uid}">PLAY REEL · PLAY REEL · PLAY REEL · </textPath></text></svg>'
            f'<i><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></i></span>')
    return f'''<figure class="reel {tilt}" data-net="{r["net"]}" data-open="{R.embed(r)}" data-link="{R.url(r)}" data-title="{E(r["title"])}">
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
</figure>'''

def tilted(keys):
    return "".join(reel_card(k, "tilt-l" if i % 2 == 0 else "tilt-r") for i, k in enumerate(keys))

def reels_home():
    cards = tilted(R.HOME)
    return f'''<section class="sec reels-sec" id="reels">
  <span class="reel-bg-text" aria-hidden="true">REELS</span>
  <div class="wrap">
    <div class="head reveal"><p class="eyebrow">Mírala en acción</p><h2>Nuestros reels <span class="script">más queridos</span></h2>
      <p class="muted">Tratamientos, consejos y mucho cariño por la piel, en vídeo. Desliza y dale al play.</p></div>
  </div>
  <div class="rail-wrap"><button class="rail-btn prev" aria-label="Anterior">‹</button><div class="rail reel-row" id="rail">{cards}</div><button class="rail-btn next" aria-label="Siguiente">›</button></div>
  <div class="wrap reels-foot reveal"><a class="btn btn-ghost" href="https://www.instagram.com/esteticasaori/" target="_blank" rel="noopener">Más en Instagram</a><a class="btn btn-ghost" href="https://www.tiktok.com/@esteticarocioguti" target="_blank" rel="noopener">Más en TikTok</a></div>
</section>'''

def reels_service(slug, name):
    keys = R.BY_SERVICE.get(slug)
    if not keys:
        return ""
    cards = tilted(keys)
    return f'''<section class="sec reels-sec" id="reels"><span class="reel-bg-text" aria-hidden="true">REELS</span><div class="wrap">
  <div class="head reveal"><p class="eyebrow">Mírala en acción</p><h2>{E(name)} <span class="script">en vídeo</span></h2></div>
  <div class="reels-grid reel-row n{len(keys)}">{cards}</div></div></section>'''

def service_page(sv):
    s = sv["slug"]
    msg = wa(f"Hola, me interesa {sv['name']}. ¿Me podéis dar información y cita?")
    chips = "".join(f"<span>{E(c)}</span>" for c in sv["chips"])
    facts = "".join(f'<div class="fact"><small>{E(k)}</small><b>{E(v)}</b></div>' for k, v in sv["facts"])
    intro = "".join(f"<p>{E(p)}</p>" for p in sv["intro"])
    bens = "".join(f'<div class="ben reveal"><span class="ben-n">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(sv["benefits"]))
    steps = "".join(f'<li class="reveal"><span>{i+1}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div></li>' for i, (t, d) in enumerate(sv["steps"]))
    ideal = "".join(f"<li>{E(x)}</li>" for x in sv["ideal"])
    before = "".join(f"<li>{E(x)}</li>" for x in sv["before"])
    after = "".join(f"<li>{E(x)}</li>" for x in sv["after"])
    faqs = "".join(f'<div class="faq reveal"><button class="faq-q" aria-expanded="false"><span>{E(q)}</span><i>+</i></button><div class="faq-a"><div><p>{E(a)}</p></div></div></div>' for q, a in sv["faqs"])
    rel = ""
    for r in sv["related"]:
        o = BY_SLUG[r]
        rel += (f'<a class="card tilt" href="{r}.html"><img src="assets/{o["img"]}" alt="{E(o["name"])}" loading="lazy"><div class="card-b">'
                f'<span class="tag">{E(o["cat"])}</span><h3>{E(o["name"])}</h3><p>{E(o["tagline"][:120].rsplit(" ",1)[0])}…</p><span class="more">Ver tratamiento →</span></div></a>')
    points = ""
    if sv["body_points"]:
        points = '<ul class="checks">' + "".join(f"<li>{E(p)}</li>" for p in sv["body_points"]) + "</ul>"
    calc = ""
    if sv.get("calculator"):
        calc = '''<div class="calc"><div class="zones" id="zones"></div>
        <div class="calc-side"><div class="total"><span>Total por sesión</span><b id="total">0 €</b><small id="count">0 zonas</small></div>
        <a class="btn btn-gold" id="wa-dep" href="https://wa.me/34654767332" target="_blank" rel="noopener">Pedir cita con mis zonas</a></div></div>'''
    body = f'''<section class="sec alt" id="especial"><div class="wrap two">
      <div class="reveal"><p class="eyebrow">Lo que debes saber</p><h2>{E(sv["body_title"])}</h2><p class="lead2">{E(sv["body_text"])}</p>{points}</div>
      <div class="reveal photo-card"><img src="assets/{sv["img"]}" alt="{E(sv["name"])}"><span class="photo-tag">{E(sv["name"])}</span></div>
    </div>{('<div class="wrap">'+calc+'</div>') if calc else ''}</section>'''
    return f'''{head(f"{sv['name']} en Huelva · Estética Avanzada Saori", sv["tagline"])}
<body class="page-service">
{header(dark=True)}
<main>
<section class="shero">
  <div class="shero-bg" style="background-image:url(assets/{sv["img"]})"></div>
  <div class="shero-ov"></div>
  <canvas id="sparkles" aria-hidden="true"></canvas>
  <div class="shero-in">
    <div class="shero-text">
      <nav class="crumbs" aria-label="Migas"><a href="index.html">Inicio</a><i>/</i><a href="index.html#tratamientos">Tratamientos</a><i>/</i><span>{E(sv["name"])}</span></nav>
      <span class="pill">{E(sv["cat"])}</span>
      <p class="eyebrow gold">{E(sv["eyebrow"])}</p>
      <h1>{E(sv["name"])}<span class="script">{E(sv["accent"])}</span></h1>
      <p class="lead">{E(sv["tagline"])}</p>
      <div class="schips">{chips}</div>
      <div class="hero-actions"><a class="btn btn-gold" href="{msg}" target="_blank" rel="noopener">Pedir cita</a><a class="btn btn-light" href="#que-es">Saber más ↓</a></div>
    </div>
    <div class="shero-photo"><div class="arch"><img src="assets/{sv["img"]}" alt="{E(sv["name"])}"></div>
      <span class="float f1">★ 5,0 · 75 opiniones</span><span class="float f2">Diagnóstico sin compromiso</span></div>
  </div>
</section>
<div class="factbar"><div class="wrap facts">{facts}</div></div>
<nav class="subnav" id="subnav" aria-label="En esta página"><div class="wrap">
  <a href="#que-es">Qué es</a><a href="#beneficios">Beneficios</a><a href="#especial">Detalle</a><a href="#proceso">Proceso</a><a href="#ideal">Ideal para</a><a href="#cuidados">Cuidados</a>{('<a href="#reels">Vídeos</a>' if R.BY_SERVICE.get(s) else '')}<a href="#faq">Preguntas</a>
</div></nav>

<section class="sec" id="que-es"><div class="wrap two">
  <div class="reveal"><p class="eyebrow">Conócelo</p><h2>¿Qué es <span class="script">{E(sv["name"])}?</span></h2>{intro}
    <a class="btn btn-gold" href="{msg}" target="_blank" rel="noopener">Quiero información</a></div>
  <div class="reveal photo-card tall"><img src="assets/{sv["img"]}" alt="{E(sv["name"])}"><span class="photo-tag">{E(sv["cat"])}</span></div>
</div></section>

<section class="sec tint" id="beneficios"><div class="wrap">
  <div class="head reveal"><p class="eyebrow">Por qué elegirlo</p><h2>Beneficios <span class="script">visibles</span></h2></div>
  <div class="bens">{bens}</div>
</div></section>

{body}

<section class="sec" id="proceso"><div class="wrap two">
  <div class="reveal"><p class="eyebrow">Tu momento Saori</p><h2>Cómo es <span class="script">tu sesión</span></h2>
    <p>Todo empieza con tu diagnóstico facial: sin prisas y sin compromiso. Después, cada sesión es un momento para ti, siempre adaptado a tu piel.</p></div>
  <ol class="steps">{steps}</ol>
</div></section>

<section class="sec dark" id="ideal"><div class="wrap two">
  <div class="reveal"><p class="eyebrow gold">Para ti si…</p><h2>Ideal <span class="script">para</span></h2><ul class="ideal">{ideal}</ul></div>
  <div class="reveal ideal-img"><img src="assets/lotus-saori.png" alt=""><p>“Cada piel necesita un plan a medida.”</p></div>
</div></section>

<section class="sec" id="cuidados"><div class="wrap">
  <div class="head reveal"><p class="eyebrow">Para un mejor resultado</p><h2>Cuidados <span class="script">y precauciones</span></h2></div>
  <div class="care3">
    <div class="care reveal"><h3>Antes</h3><ul>{before}</ul></div>
    <div class="care reveal"><h3>Después</h3><ul>{after}</ul></div>
    <div class="care warn reveal"><h3>Importante</h3><p>{E(sv["caution"])}</p></div>
  </div>
</div></section>

{reels_service(s, sv["name"])}

<section class="sec tint" id="faq"><div class="wrap narrow">
  <div class="head reveal"><p class="eyebrow">Resolvemos tus dudas</p><h2>Preguntas <span class="script">frecuentes</span></h2></div>
  <div class="faqs">{faqs}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="head reveal"><p class="eyebrow">Combínalo con</p><h2>Otros tratamientos <span class="script">que te pueden gustar</span></h2></div>
  <div class="grid">{rel}</div>
</div></section>

<section class="cta"><div class="wrap cta-in reveal">
  <img src="assets/lotus-saori.png" alt="">
  <div><h2>¿Lista para <span class="script">redescubrir tu piel?</span></h2><p>Pide tu diagnóstico facial y te aconsejamos sin ningún compromiso. Aquí te ayudamos a cuidar tu piel.</p></div>
  <div class="hero-actions"><a class="btn btn-gold" href="{msg}" target="_blank" rel="noopener">Pedir cita por WhatsApp</a><a class="btn btn-light" href="tel:+34654767332">654 76 73 32</a></div>
</div></section>
</main>
{footer()}
</body></html>'''

def build():
    for sv in SERVICES:
        with open(os.path.join(ROOT, sv["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(service_page(sv))
    # home
    tpl = open(os.path.join(ROOT, "src", "home.tpl.html"), encoding="utf-8").read()
    tpl = tpl.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="site.css"><link rel="stylesheet" href="extra.css"><link rel="stylesheet" href="premium.css"><link rel="stylesheet" href="viewer.css"><link rel="stylesheet" href="reelstyle.css">').replace("{{REELS}}", reels_home()).replace("{{HISTORIA}}", reel_card("ig-historia")).replace("{{HEADER}}", header(dark=True)).replace("{{FOOTER}}", footer() + '\n<script src="splash.js"></script>')
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("ok", len(SERVICES) + 1, "páginas")

if __name__ == "__main__":
    build()
