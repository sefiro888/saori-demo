# -*- coding: utf-8 -*-
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
j = os.path.join(ROOT, "viewer.js")
t = open(j, encoding="utf-8").read()
if "rv-tt" not in t:
    t = t.replace("""'<div class="rv-stage"><div class="rv-load"><i></i><span>Cargando vídeo…</span></div><iframe""",
                  """'<div class="rv-stage"><div class="rv-load"><i></i><span>Cargando vídeo…</span></div><div class="rv-tt"><img alt=""><span class="rv-shade"></span><button type="button" class="rv-play" aria-label="Reproducir"></button><a class="rv-out" target="_blank" rel="noopener">Abrir en TikTok</a></div><iframe""")
    t = t.replace("const frame = $('iframe', rv),", "const tt = $('.rv-tt', rv), ttImg = $('img', tt), ttOut = $('.rv-out', tt), frame = $('iframe', rv),")
    old = t[t.index("  const show = i => {"):t.index("  const open = c => {")]
    new = """  const play = c => {
    load.classList.remove('off');
    frame.classList.remove('on');
    frame.onload = () => { frame.classList.add('on'); load.classList.add('off'); };
    frame.src = c.dataset.open;
    setTimeout(() => load.classList.add('off'), 6000);
  };
  const show = i => {
    cur = (i + list.length) % list.length;
    const c = list[cur];
    cap.textContent = c.dataset.title;
    alt.href = c.dataset.link;
    rv.dataset.net = c.dataset.net;
    frame.classList.remove('on'); frame.src = 'about:blank';
    if (c.dataset.net === 'tt') {
      // TikTok: portada a pantalla completa y, al pulsar play, se carga el reproductor dentro de la web
      load.classList.add('off');
      tt.classList.add('show');
      const im = $('img', c); ttImg.src = im ? im.src : '';
      ttOut.href = c.dataset.link;
      tt.querySelector('.rv-play').onclick = () => { tt.classList.remove('show'); play(c); };
    } else {
      tt.classList.remove('show');
      play(c);
    }
  };
"""
    t = t.replace(old, new)
    open(j, "w", encoding="utf-8").write(t)
css = os.path.join(ROOT, "viewer.css")
c = open(css, encoding="utf-8").read()
if ".rv-tt" not in c:
    c += """
/* TikTok en el visor: portada + play */
.rv-tt{position:absolute;inset:0;display:none;z-index:3;background:#000}
.rv-tt.show{display:block}
.rv-tt img{width:100%;height:100%;object-fit:cover}
.rv-shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,2,10,.35),transparent 30%,rgba(7,2,10,.85))}
.rv-play{position:absolute;left:50%;top:46%;width:92px;height:92px;margin:-46px 0 0 -46px;border-radius:50%;border:0;background:rgba(255,255,255,.94);cursor:pointer;animation:ping2 2.4s infinite}
.rv-play::after{content:"";position:absolute;left:36px;top:27px;border-left:30px solid var(--violet);border-top:19px solid transparent;border-bottom:19px solid transparent}
.rv-out{position:absolute;left:50%;bottom:120px;transform:translateX(-50%);padding:11px 22px;border-radius:999px;border:1px solid rgba(255,255,255,.6);background:rgba(20,6,26,.6);color:#fff;font:700 .72rem 'Montserrat';letter-spacing:.1em;text-transform:uppercase;backdrop-filter:blur(8px);white-space:nowrap}
.rv-stage iframe{background:#fff}
.rv[data-net="tt"] .rv-stage iframe{background:#fff}
"""
    open(css, "w", encoding="utf-8").write(c)
print("ok")
