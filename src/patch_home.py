# -*- coding: utf-8 -*-
"""Una sola vez: inserta las tarjetas de redes realistas y la presentación (splash) en home.tpl.html."""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = os.path.join(ROOT, "src", "home.tpl.html")
h = open(p, encoding="utf-8").read()

if 'class="nets"' not in h:
    # ---------- redes ----------
    s = h.index('<div class="social">')
    e = h.index('</section>', s)
    nets = '''<div class="nets">

      <!-- INSTAGRAM -->
      <article class="net ig reveal">
        <header class="net-bar"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg><b>Instagram</b><a href="https://www.instagram.com/esteticasaori/" target="_blank" rel="noopener">Ver perfil</a></header>
        <div class="ig-head">
          <span class="ig-ring"><img src="assets/lotus.png" alt="Saori"></span>
          <div class="ig-stats"><div><b>213</b><span>publicaciones</span></div><div><b>1.361</b><span>seguidores</span></div><div><b>717</b><span>seguidos</span></div></div>
        </div>
        <div class="ig-bio"><b>Estética Avanzada Saori | Huelva</b><p>Estética avanzada en Huelva<br>Especialistas en diagnóstico facial 🥰<br>Tratamientos faciales personalizados<br>📍 C. Diego de Almagro, local 15, Huelva</p></div>
        <div class="ig-btns"><a class="b-blue" href="https://www.instagram.com/esteticasaori/" target="_blank" rel="noopener">Seguir</a><a class="b-grey" href="https://wa.me/34654767332" target="_blank" rel="noopener">Mensaje</a></div>
        <div class="ig-hl"><div><img src="assets/lotus.png" alt=""><span>Saori</span></div><div><img src="assets/kinesio.jpg" alt=""><span>Kinesiolifting</span></div><div><img src="assets/ipl.jpg" alt=""><span>Faciales</span></div><div><img src="assets/hifu.jpg" alt=""><span>Hifu 12D</span></div></div>
        <div class="ig-tabs"><i class="on"></i><i></i><i></i></div>
        <div class="ig-grid"><img src="assets/abdomen-despues.jpg" alt=""><img src="assets/dermapen.jpg" alt=""><img src="assets/rostro-despues.jpg" alt=""><img src="assets/limpieza-zensy.jpg" alt=""><img src="assets/poros-despues.jpg" alt=""><img src="assets/depilacion.jpg" alt=""></div>
      </article>

      <!-- TIKTOK -->
      <article class="net tt reveal">
        <header class="net-bar"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M16.6 3c.3 2.3 1.7 3.9 4 4.1v3.1c-1.5.1-2.9-.4-4-1.1v6.2c0 3.2-2.3 5.6-5.5 5.6-3 0-5.4-2.3-5.4-5.3 0-3.3 2.7-5.6 6-5.2v3.2c-1.5-.4-2.8.5-2.8 2 0 1.2.9 2.1 2.1 2.1 1.3 0 2.1-.9 2.1-2.3V3z"/></svg><b>TikTok</b><a href="https://www.tiktok.com/@esteticarocioguti" target="_blank" rel="noopener">Ver perfil</a></header>
        <div class="tt-head">
          <span class="tt-av"><img src="assets/lotus.png" alt="Saori"></span>
          <div><b>esteticarocioguti</b><span>Estetica avanzada Saori</span><a class="b-red" href="https://www.tiktok.com/@esteticarocioguti" target="_blank" rel="noopener">Seguir</a></div>
        </div>
        <div class="tt-stats"><div><b>172</b> Siguiendo</div><div><b>796</b> Seguidores</div><div><b>4122</b> Me gusta</div></div>
        <p class="tt-bio">💗 Tratamientos estéticos con resultados reales | Saori</p>
        <div class="tt-tabs"><span class="on">Vídeos</span><span>Favoritos</span><span>Me gusta</span></div>
        <div class="tt-grid">
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7620003087901674774" target="_blank" rel="noopener"><img src="assets/reels/tt-manchas.jpg" alt=""><em>▷ 7111</em></a>
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7601842837633748246" target="_blank" rel="noopener"><img src="assets/reels/tt-acne.jpg" alt=""><em>▷ 6828</em></a>
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7506831992978165014" target="_blank" rel="noopener"><img src="assets/reels/tt-hifu.jpg" alt=""><em>▷ 5570</em></a>
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7504277072064384278" target="_blank" rel="noopener"><img src="assets/reels/tt-kinesio.jpg" alt=""><em>▷ 4845</em></a>
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7592923026014948611" target="_blank" rel="noopener"><img src="assets/reels/tt-antesdespues.jpg" alt=""><em>▷ 2830</em></a>
          <a href="https://www.tiktok.com/@esteticarocioguti/video/7500606931984272662" target="_blank" rel="noopener"><img src="assets/reels/tt-limpieza.jpg" alt=""><em>▷ 2464</em></a>
        </div>
      </article>

      <!-- FACEBOOK -->
      <article class="net fb reveal">
        <header class="net-bar"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.9.3-1.5 1.5-1.5h1.6V4.3c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z"/></svg><b>Facebook</b><a href="https://www.facebook.com/esteticasaorihuelva" target="_blank" rel="noopener">Ver página</a></header>
        <div class="fb-cover"><img src="assets/emblema.jpg" alt=""></div>
        <div class="fb-id"><span class="fb-av"><img src="assets/lotus.png" alt="Saori"></span>
          <div><b>Estética Avanzada Saori</b><span>1.363 seguidores · 5 seguidos</span></div></div>
        <p class="fb-cat">Belleza, cosmética y cuidado personal · €€</p>
        <div class="fb-btns"><a class="b-fb" href="https://wa.me/34654767332" target="_blank" rel="noopener">WhatsApp</a><a class="b-fbg" href="https://www.facebook.com/esteticasaorihuelva" target="_blank" rel="noopener">Seguir</a></div>
        <ul class="fb-info"><li>📍 C/ Diego de Almagro 15, local, Huelva 21002</li><li>🟢 Abierto ahora (según horario)</li><li>⭐ 3 opiniones</li></ul>
        <div class="fb-post">
          <div class="fb-ph"><span class="fb-av s"><img src="assets/lotus.png" alt=""></span><div><b>Estética Avanzada Saori</b><small>Publicación reciente</small></div></div>
          <p><b>Edición Limitada: Protocolo Dermapen Total Face &amp; Lips.</b> Esta semana en Estética Avanzada Saori, elevamos tu cuidado facial. Hemos diseñado un protocolo exclusivo…</p>
          <img src="assets/dermapen.jpg" alt="">
          <div class="fb-act"><span>👍 Me gusta</span><span>💬 Comentar</span><span>↗ Compartir</span></div>
        </div>
      </article>
    </div>
  </div>
'''
    h = h[:s] + nets + h[e:]


if 'id="splash"' not in h:
    # ---------- splash ----------
    h = h.replace('</head>', '<script>try{if(!sessionStorage.getItem("saoriSplash")&&!matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("has-splash")}catch(e){}</script>\n</head>', 1)
    splash = '''<body class="home">
<!-- SPLASH -->
<div class="splash" id="splash" aria-hidden="true">
  <canvas id="splashCv"></canvas>
  <div class="sp-rays"></div>
  <div class="sp-center">
    <div class="sp-emblem">
      <svg class="sp-ring" viewBox="0 0 200 200"><circle cx="100" cy="100" r="96"/><circle cx="100" cy="100" r="88" class="thin"/></svg>
      <img src="assets/emblema.jpg" alt="">
    </div>
    <p class="sp-tag" id="spTag">Estética avanzada · Huelva</p>
    <div class="sp-bar"><i id="spBar"></i></div>
    <p class="sp-count"><span id="spNum">0</span>%</p>
    <button class="sp-enter" id="spEnter" type="button">Entrar</button>
  </div>
  <button class="sp-skip" id="spSkip" type="button">Saltar ›</button>
</div>
'''
    h = h.replace('<body class="home">', splash, 1)
open(p, "w", encoding="utf-8").write(h)
print("patched")
