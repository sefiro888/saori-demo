(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- reels: el escudo táctil deja deslizar el carrusel; un toque activa el vídeo ---------- */
  $$('.reel-shield').forEach(b => b.addEventListener('click', () => b.closest('.reel').classList.add('live')));

  /* ---------- reels: botones, contador y puntos para el móvil ---------- */
  const rail = $('#rail');
  if (rail) {
    const cards = $$('.reel', rail);
    const nav = document.createElement('div'); nav.className = 'rail-nav';
    nav.innerHTML = '<button type="button" aria-label="Anterior">‹</button><span class="rail-count">1 / ' + cards.length + '</span><button type="button" aria-label="Siguiente">›</button>';
    const dots = document.createElement('div'); dots.className = 'rail-dots';
    dots.innerHTML = cards.map(() => '<i></i>').join('');
    rail.parentElement.after(nav); nav.after(dots);
    const [prev, , next] = [...nav.children];
    const count = $('.rail-count', nav), dotEls = $$('i', dots);
    const idx = () => {
      const c = rail.scrollLeft + rail.clientWidth / 2; let best = 0, bd = 1e9;
      cards.forEach((el, i) => { const d = Math.abs(el.offsetLeft + el.offsetWidth / 2 - c); if (d < bd) { bd = d; best = i; } });
      return best;
    };
    const upd = () => { const i = idx(); count.textContent = (i + 1) + ' / ' + cards.length; dotEls.forEach((d, k) => d.classList.toggle('on', k === i)); };
    const go = i => { const el = cards[Math.max(0, Math.min(cards.length - 1, i))]; rail.scrollTo({ left: el.offsetLeft - (rail.clientWidth - el.offsetWidth) / 2, behavior: 'smooth' }); };
    prev.onclick = () => go(idx() - 1); next.onclick = () => go(idx() + 1);
    rail.addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true });
    upd();
    // pausa los demás vídeos al cambiar de tarjeta
    rail.addEventListener('scroll', () => { const i = idx(); cards.forEach((c, k) => { if (k !== i && c.classList.contains('live')) { c.classList.remove('live'); const f = $('iframe', c); if (f) { const s = f.src; f.src = s; } } }); }, { passive: true });
  }
})();
