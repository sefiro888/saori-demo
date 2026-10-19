(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- cabecera: progreso, scroll, mega menú, menú móvil ---------- */
  const top = $('#siteTop'), prog = $('#progress');
  const onScroll = () => {
    const y = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    if (prog) prog.style.transform = `scaleX(${h > 0 ? y / h : 0})`;
    if (top) top.classList.toggle('scrolled', y > 30);
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  const hm = $('#hasMega');
  if (hm) {
    const btn = $('.mega-btn', hm); let t;
    const set = v => { hm.classList.toggle('open', v); btn.setAttribute('aria-expanded', v); };
    hm.addEventListener('mouseenter', () => { clearTimeout(t); t = setTimeout(() => set(true), 60); });
    hm.addEventListener('mouseleave', () => { clearTimeout(t); t = setTimeout(() => set(false), 200); });
    btn.addEventListener('click', () => set(!hm.classList.contains('open')));
    addEventListener('keydown', e => { if (e.key === 'Escape') { set(false); closeMenu(); } });
    document.addEventListener('click', e => { if (!hm.contains(e.target)) set(false); });
    $$('.mega a', hm).forEach(a => a.addEventListener('click', () => set(false)));
  }

  const burger = $('#burger'), mnav = $('#mnav');
  function closeMenu() { if (!mnav) return; burger.classList.remove('open'); mnav.classList.remove('open'); top.classList.remove('menu-open'); document.body.classList.remove('noscroll'); burger.setAttribute('aria-expanded', false); }
  if (burger && mnav) {
    burger.addEventListener('click', () => {
      const o = !mnav.classList.contains('open');
      burger.classList.toggle('open', o); mnav.classList.toggle('open', o); top.classList.toggle('menu-open', o);
      document.body.classList.toggle('noscroll', o); burger.setAttribute('aria-expanded', o);
    });
    $$('a', mnav).forEach(a => a.addEventListener('click', closeMenu));
    const acc = $('#mAcc'), pan = $('#mPanel');
    acc.addEventListener('click', () => { const o = !pan.classList.contains('open'); pan.classList.toggle('open', o); acc.setAttribute('aria-expanded', o); });
  }

  /* ---------- reveal ---------- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
  $$('.reveal').forEach((el, i) => { el.style.transitionDelay = (i % 3) * 90 + 'ms'; io.observe(el); });

  /* ---------- contadores ---------- */
  const co = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, to = +el.dataset.count, dec = +(el.dataset.dec || 0), t0 = performance.now();
    const step = t => { const p = Math.min((t - t0) / 1400, 1), v = to * (1 - Math.pow(1 - p, 3)); el.textContent = v.toFixed(dec).replace('.', ','); if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step); co.unobserve(el);
  }), { threshold: .6 });
  $$('[data-count]').forEach(el => co.observe(el));


  /* ---------- reels: carga diferida de los embeds + carrusel ---------- */
  const reelsEls = $$('.reel[data-embed]');
  if (reelsEls.length) {
    const lo = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      const r = e.target, f = $('iframe', r); lo.unobserve(r);
      f.addEventListener('load', () => { f.classList.add('on'); const s = $('.reel-skel', r); if (s) setTimeout(() => s.remove(), 700); });
      f.src = r.dataset.embed;
    }), { rootMargin: '0px 400px 300px 400px' });
    reelsEls.forEach(r => lo.observe(r));
  }
  const rail = $('#rail');
  if (rail) {
    const step = () => Math.min(340, rail.clientWidth * .8);
    $('.rail-btn.next').onclick = () => rail.scrollBy({ left: step(), behavior: 'smooth' });
    $('.rail-btn.prev').onclick = () => rail.scrollBy({ left: -step(), behavior: 'smooth' });
    let down = false, sx = 0, sl = 0, moved = false;
    rail.addEventListener('mousedown', e => { if (e.target.closest('iframe,a')) return; down = true; moved = false; sx = e.pageX; sl = rail.scrollLeft; });
    addEventListener('mouseup', () => { down = false; rail.classList.remove('drag'); });
    rail.addEventListener('mousemove', e => { if (!down) return; const dx = e.pageX - sx; if (Math.abs(dx) > 5) { moved = true; rail.classList.add('drag'); } rail.scrollLeft = sl - dx; });
  }

  /* ---------- FAQ ---------- */
  $$('.faq-q').forEach(b => b.addEventListener('click', () => {
    const f = b.parentElement, o = !f.classList.contains('open');
    f.classList.toggle('open', o); b.setAttribute('aria-expanded', o);
  }));

  /* ---------- tilt 3D en tarjetas ---------- */
  if (!reduce && matchMedia('(hover:hover)').matches) {
    $$('.tilt').forEach(c => {
      c.addEventListener('mousemove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        c.style.transform = `perspective(900px) rotateX(${-y * 7}deg) rotateY(${x * 9}deg) translateY(-6px)`;
      });
      c.addEventListener('mouseleave', () => { c.style.transform = ''; });
    });
  }

  /* ---------- scroll-spy del subnav ---------- */
  const sub = $('#subnav');
  if (sub) {
    const links = $$('a', sub), map = new Map(links.map(a => [a.getAttribute('href').slice(1), a]));
    const so = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { links.forEach(l => l.classList.remove('on')); const a = map.get(e.target.id); if (a) { a.classList.add('on'); a.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' }); } }
    }), { rootMargin: '-40% 0px -55% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) so.observe(s); });
  }

  /* ---------- filtros de tratamientos (home) ---------- */
  const tabs = $('#tabs');
  if (tabs) tabs.addEventListener('click', e => {
    const b = e.target.closest('.tab'); if (!b) return;
    $$('.tab').forEach(t => t.classList.toggle('on', t === b));
    const f = b.dataset.f;
    $$('#grid .card').forEach(c => c.classList.toggle('hide', f !== 'all' && !c.dataset.cat.split(' ').includes(f)));
  });

  /* ---------- palabras rotativas (home) ---------- */
  const rot = $('#rot');
  if (rot) {
    const W = ['diagnóstico facial', 'tratamientos faciales personalizados', 'depilación IPL', 'tecnologías avanzadas', 'el cuidado de tu piel']; let i = 0;
    setInterval(() => { rot.style.opacity = 0; setTimeout(() => { i = (i + 1) % W.length; rot.textContent = W[i]; rot.style.opacity = 1; }, 400); }, 2800);
  }

  /* ---------- antes / después (home) ---------- */
  const ba = $('#ba');
  if (ba) {
    const range = $('#baRange'), wrap = $('#baBeforeWrap'), handle = $('#baHandle'), bimg = $('#baBefore');
    const setBA = v => { wrap.style.width = v + '%'; handle.style.left = v + '%'; bimg.style.setProperty('--w', (10000 / Math.max(v, 1)) + '%'); };
    const CASES = [
      ['abdomen', 'Reafirmación abdominal sin cirugía: piel más firme y tensa, contorno redefinido.'],
      ['abdomen2', 'Abdomen: contorno más definido y piel más uniforme.'],
      ['abdomen3', 'Abdomen: mejora visible de la laxitud y la textura.'],
      ['rostro', 'Rostro: piel más luminosa, uniforme y revitalizada.'],
      ['cuello', 'Cuello y perfil: efecto lifting y firmeza.'],
      ['poros', 'Textura de la piel: poros más refinados y piel más lisa.']
    ];
    let cur = 0, anim = 0, touched = false;
    const lbl1 = $('#lbl1'), lbl2 = $('#lbl2'), count = $('#baCount');
    const paint = v => { setBA(v); lbl1.style.opacity = v < 18 ? 0 : 1; lbl2.style.opacity = v > 82 ? 0 : 1; };
    const goTo = (v, ms = 600) => {
      cancelAnimationFrame(anim);
      const from = +range.value, t0 = performance.now();
      const run = t => { const p = Math.min((t - t0) / ms, 1), e = 1 - Math.pow(1 - p, 3); range.value = from + (v - from) * e; paint(+range.value); if (p < 1) anim = requestAnimationFrame(run); };
      anim = requestAnimationFrame(run);
    };
    CASES.forEach(([k]) => { ['antes', 'despues'].forEach(t => { new Image().src = `assets/${k}-${t}.jpg?v=3`; }); });
    const loadCase = i => {
      cur = (i + CASES.length) % CASES.length;
      const [k, note] = CASES[cur], probe = new Image();
      ba.classList.add('swap');
      probe.onload = () => {
        const r = probe.naturalWidth / probe.naturalHeight;
        ba.style.aspectRatio = Math.min(Math.max(r, 1.2), 1.6); $('#baBg').style.backgroundImage = `url(assets/${k}-despues.jpg?v=3)`;
        $('#baAfter').src = `assets/${k}-despues.jpg?v=3`; bimg.src = `assets/${k}-antes.jpg?v=3`;
        cancelAnimationFrame(anim); range.value = 50; paint(50);
        ba.classList.remove('swap');
        if (touched) return;
        goTo(15, 500); setTimeout(() => { if (!touched) goTo(50, 700); }, 650);
      };
      probe.src = `assets/${k}-antes.jpg?v=3`;
      $('#caseNote').textContent = note; count.textContent = `${cur + 1} / ${CASES.length}`;
      $$('.case').forEach(c => { const on = +c.dataset.i === cur; c.classList.toggle('on', on); c.setAttribute('aria-selected', on); });
    };
    $('#cases').addEventListener('click', e => { const c = e.target.closest('.case'); if (c) loadCase(+c.dataset.i); });
    $('#baPrev').addEventListener('click', () => loadCase(cur - 1));
    $('#baNext').addEventListener('click', () => loadCase(cur + 1));
    $$('.ba-snap').forEach(b => b.addEventListener('click', () => { touched = true; goTo(+b.dataset.v); }));
    const stop = () => { touched = true; cancelAnimationFrame(anim); };
    range.addEventListener('pointerdown', stop);
    range.addEventListener('input', () => { stop(); paint(+range.value); });
    $('#caseNote').textContent = CASES[0][1];
    paint(50);
    new IntersectionObserver((es, ob) => es.forEach(e => {
      if (!e.isIntersecting) return; ob.disconnect();
      if (touched) return;
      range.value = 50; goTo(12, 900); setTimeout(() => { if (!touched) goTo(88, 1400); }, 1000); setTimeout(() => { if (!touched) goTo(50, 900); }, 2500);
    }), { threshold: .5 }).observe(ba);
  }

  /* ---------- calculadora depilación IPL ---------- */
  const zones = $('#zones');
  if (zones) {
    const Z = [['Labio superior', 15], ['Patillas', 15], ['Mejillas', 10], ['Mentón', 15], ['Axilas', 25], ['Brazos', 30], ['Pecho', 49], ['Espalda', 49], ['Línea alba', 15],
      ['Ingles normales', 24], ['Ingles brasileñas', 26], ['Ingles completas', 30], ['Glúteos', 29], ['Perianal', 10], ['Empeine y dedos', 15], ['Medias piernas', 29], ['Piernas completas', 49]];
    const sel = new Set();
    const upd = () => {
      const tot = [...sel].reduce((a, i) => a + Z[i][1], 0);
      $('#total').textContent = tot + ' €'; $('#count').textContent = sel.size + (sel.size === 1 ? ' zona' : ' zonas');
      const txt = sel.size ? `Hola, quiero cita para depilación IPL: ${[...sel].map(i => Z[i][0]).join(', ')} (${tot} €/sesión)` : 'Hola, quiero información sobre depilación IPL';
      $('#wa-dep').href = 'https://wa.me/34654767332?text=' + encodeURIComponent(txt);
    };
    Z.forEach(([n, p], i) => {
      const b = document.createElement('button'); b.className = 'zone'; b.innerHTML = `<span>${n}</span><b>${p} €</b>`;
      b.onclick = () => { sel.has(i) ? sel.delete(i) : sel.add(i); b.classList.toggle('on'); upd(); };
      zones.appendChild(b);
    });
  }

  /* ---------- horario en vivo (home) ---------- */
  const hours = $('#hours');
  if (hours) {
    const H = { 1: [[9, 0, 14, 0], [16, 0, 19, 0]], 2: [[9, 0, 14, 30]], 3: [[9, 0, 14, 0], [16, 0, 19, 0]], 4: [[9, 0, 14, 30]], 5: [[9, 0, 14, 30]], 6: [], 0: [] };
    const now = new Date(), d = now.getDay(), m = now.getHours() * 60 + now.getMinutes();
    $(`tr[data-d="${d}"]`, hours).classList.add('today');
    const open = H[d].some(([a, b, c, e]) => m >= a * 60 + b && m < c * 60 + e);
    const st = $('#status'); st.classList.add(open ? 'open' : 'closed');
    $('#statusTxt').textContent = open ? 'Abierto ahora' : 'Cerrado ahora';
  }

  /* ---------- destellos dorados ---------- */
  const cv = $('#sparkles');
  if (cv && !reduce) {
    const cx = cv.getContext('2d'); let W, Hh, P = [];
    const mk = () => ({ x: Math.random() * W, y: Math.random() * Hh, r: Math.random() * 2.4 + .6, v: Math.random() * .4 + .15, a: Math.random() * Math.PI * 2, s: Math.random() * .02 + .01 });
    const rs = () => { W = cv.width = cv.offsetWidth; Hh = cv.height = cv.offsetHeight; P = Array.from({ length: Math.min(70, W / 16) }, mk); };
    addEventListener('resize', rs); rs();
    (function loop() {
      cx.clearRect(0, 0, W, Hh);
      P.forEach(p => {
        p.y -= p.v; p.x += Math.sin(p.a += p.s) * .4; if (p.y < -10) { p.y = Hh + 10; p.x = Math.random() * W; }
        const o = .35 + .45 * Math.abs(Math.sin(p.a * 2));
        cx.beginPath(); cx.fillStyle = `rgba(233,196,106,${o})`; cx.shadowBlur = 10; cx.shadowColor = 'rgba(233,196,106,.9)';
        cx.arc(p.x, p.y, p.r, 0, 7); cx.fill();
      });
      requestAnimationFrame(loop);
    })();
  }
})();
