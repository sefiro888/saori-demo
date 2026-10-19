(() => {
  const $ = s => document.querySelector(s);
  const splash = $('#splash');
  const on = document.documentElement.classList.contains('has-splash');
  if (!splash || !on) { document.body.classList.add('entered'); return; }

  const tag = $('#spTag');

  // frase letra a letra (tras el destello inicial)
  const txt = tag.textContent; tag.textContent = '';
  [...txt].forEach((c, i) => {
    const s = document.createElement('span');
    s.textContent = c === ' ' ? ' ' : c;
    s.style.cssText = `opacity:0;display:inline-block;transform:translateY(8px);animation:spUp .6s ${2 + i * .04}s forwards`;
    tag.appendChild(s);
  });

  // polvo dorado muy sutil
  const cv = $('#splashCv'), cx = cv.getContext('2d');
  let W, H; const P = [];
  const rs = () => { W = cv.width = innerWidth; H = cv.height = innerHeight; };
  rs(); addEventListener('resize', rs);
  const mk = () => ({ x: Math.random() * W, y: H + 10, vy: -(Math.random() * .35 + .12), vx: (Math.random() - .5) * .15, r: Math.random() * 1.5 + .4, a: Math.random() * 6.283, s: Math.random() * .02 + .008 });
  for (let i = 0; i < 38; i++) { const p = mk(); p.y = Math.random() * H; P.push(p); }
  let alive = true;
  (function loop() {
    if (!alive) return;
    cx.clearRect(0, 0, W, H);
    P.forEach((p, i) => {
      p.y += p.vy; p.x += p.vx + Math.sin(p.a += p.s) * .2;
      if (p.y < -10) { P[i] = mk(); return; }
      const o = .25 + .5 * Math.abs(Math.sin(p.a * 1.6));
      cx.beginPath(); cx.fillStyle = `rgba(233,196,106,${o})`; cx.shadowBlur = 10; cx.shadowColor = 'rgba(233,196,106,.8)';
      cx.arc(p.x, p.y, p.r, 0, 7); cx.fill();
    });
    requestAnimationFrame(loop);
  })();

  // cierre: las cortinas se abren
  let closed = false;
  function close() {
    if (closed) return; closed = true;
    try { sessionStorage.setItem('saoriSplash', '1'); } catch (e) {}
    splash.classList.add('out');
    setTimeout(() => document.body.classList.add('entered'), 700);
    setTimeout(() => { alive = false; document.documentElement.classList.remove('has-splash'); splash.remove(); }, 1700);
  }
  setTimeout(close, 4600);
  $('#spSkip').addEventListener('click', close);
  addEventListener('keydown', e => { if (e.key === 'Escape' || e.key === 'Enter') close(); });
  splash.addEventListener('click', e => { if (e.target === splash || e.target.closest('.sp-center')) close(); });
})();
