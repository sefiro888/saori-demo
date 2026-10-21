/* Reproductor integrado: el vídeo se reproduce DENTRO del móvil de la tarjeta, sin salir de la web. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const cards = $$('.reel[data-open]');
  if (!cards.length) return;

  // medidas del embed de Instagram (cabecera 54 px; el vídeo ocupa ~1.2 × el ancho y se ve con barras)
  const S = 1.47, HEAD = 54;

  function stop(c) {
    const live = $('.reel-live', c);
    if (live) live.remove();
    c.classList.remove('playing');
  }

  function play(c) {
    cards.forEach(o => { if (o !== c) stop(o); });
    if (c.classList.contains('playing')) return;
    const phone = $('.phone', c);
    const live = document.createElement('div');
    live.className = 'reel-live';
    live.innerHTML = '<div class="rl-load"><i></i></div><iframe title="' + (c.dataset.title || 'Vídeo') + '" allow="autoplay; encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>' +
      '<button type="button" class="rl-x" aria-label="Cerrar vídeo">✕</button>' +
      '<a class="rl-out" target="_blank" rel="noopener">Abrir en ' + (c.dataset.net === 'ig' ? 'Instagram' : 'TikTok') + '</a>';
    phone.appendChild(live);
    c.classList.add('playing');
    const f = $('iframe', live), load = $('.rl-load', live);
    $('.rl-out', live).href = c.dataset.link;
    $('.rl-x', live).onclick = () => stop(c);
    f.onload = () => { f.classList.add('on'); load.classList.add('off'); };
    setTimeout(() => load.classList.add('off'), 7000);

    const W = live.clientWidth, H = live.clientHeight;
    if (c.dataset.net === 'ig') {
      // recorta la cabecera y el pie del embed y amplía el vídeo para que llene el móvil
      f.style.cssText = 'position:absolute;left:0;width:' + W + 'px;height:' + (W * 1.95) + 'px;top:' + Math.max(0, (H - W * 1.764) / 2) + 'px;transform-origin:50% 0;transform:translateY(' + (-HEAD * S) + 'px) scale(' + S + ')';
    } else {
      f.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%';
    }
    f.src = c.dataset.open;
  }

  cards.forEach(c => {
    const btn = $('.reel-play', c);
    if (btn) btn.addEventListener('click', e => { e.preventDefault(); play(c); });
  });

  // al salir de pantalla, el vídeo se detiene
  const io = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) stop(e.target); }), { threshold: .15 });
  cards.forEach(c => io.observe(c));
  addEventListener('keydown', e => { if (e.key === 'Escape') cards.forEach(stop); });
})();
