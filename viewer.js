/* Visor de vídeos a pantalla completa: se reproducen dentro de la web, sin salir a la red social. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cards = $$('.reel[data-open]');
  if (!cards.length) return;

  const rv = document.createElement('div');
  rv.className = 'rv'; rv.hidden = true; rv.setAttribute('role', 'dialog'); rv.setAttribute('aria-modal', 'true');
  rv.innerHTML =
    '<div class="rv-bg"></div>' +
    '<div class="rv-stage"><div class="rv-load"><i></i><span>Cargando vídeo…</span></div><div class="rv-tt"><img alt=""><span class="rv-shade"></span><button type="button" class="rv-play" aria-label="Reproducir"></button><a class="rv-out" target="_blank" rel="noopener">Abrir en TikTok</a></div><iframe title="Vídeo" allow="autoplay; encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe></div>' +
    '<button class="rv-x" type="button" aria-label="Cerrar">✕</button>' +
    '<button class="rv-nav rv-prev" type="button" aria-label="Anterior">‹</button>' +
    '<button class="rv-nav rv-next" type="button" aria-label="Siguiente">›</button>' +
    '<div class="rv-cap"><b></b><a target="_blank" rel="noopener">¿No se reproduce? Ábrelo en la red →</a></div>';
  document.body.appendChild(rv);

  const tt = $('.rv-tt', rv), ttImg = $('img', tt), ttOut = $('.rv-out', tt), frame = $('iframe', rv), cap = $('.rv-cap b', rv), alt = $('.rv-cap a', rv), load = $('.rv-load', rv);
  let cur = 0, list = cards;

  const play = c => {
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
  const open = c => {
    // el visor recorre las tarjetas de su misma sección
    const rail = c.closest('.rail, .reels-grid, .story-reel');
    list = rail ? $$('.reel[data-open]', rail) : [c];
    rv.hidden = false; document.body.classList.add('noscroll'); requestAnimationFrame(() => rv.classList.add('open'));
    show(list.indexOf(c));
  };
  const close = () => {
    rv.classList.remove('open'); document.body.classList.remove('noscroll');
    setTimeout(() => { rv.hidden = true; frame.src = 'about:blank'; }, 350);
  };

  cards.forEach(c => {
    const shield = $('.reel-shield', c), poster = $('.reel-poster', c);
    if (shield) shield.addEventListener('click', e => { e.preventDefault(); open(c); });
    if (poster) poster.addEventListener('click', e => { if (e.metaKey || e.ctrlKey) return; e.preventDefault(); open(c); });
  });

  $('.rv-x', rv).onclick = close;
  $('.rv-bg', rv).onclick = close;
  $('.rv-prev', rv).onclick = () => show(cur - 1);
  $('.rv-next', rv).onclick = () => show(cur + 1);
  addEventListener('keydown', e => {
    if (rv.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
  });
  // deslizar hacia abajo para cerrar, a los lados para cambiar (sobre los bordes del visor)
  let sx = 0, sy = 0;
  rv.addEventListener('touchstart', e => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  rv.addEventListener('touchend', e => {
    if (e.target.closest('iframe')) return;
    const dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    if (dy > 90 && Math.abs(dy) > Math.abs(dx)) close();
    else if (Math.abs(dx) > 70 && Math.abs(dx) > Math.abs(dy)) show(cur + (dx < 0 ? 1 : -1));
  }, { passive: true });
})();
