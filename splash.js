(() => {
  const $ = s => document.querySelector(s);
  const splash = $('#splash');
  const on = document.documentElement.classList.contains('has-splash');
  if (!splash || !on) { document.body.classList.add('entered'); return; }

  const num = $('#spNum'), bar = $('#spBar'), enter = $('#spEnter'), tag = $('#spTag');

  // frase letra a letra
  const txt = tag.textContent; tag.textContent = '';
  [...txt].forEach((c, i) => {
    const s = document.createElement('span');
    s.textContent = c === ' ' ? ' ' : c;
    s.style.cssText = `opacity:0;display:inline-block;transform:translateY(8px);animation:spUp .5s ${1.8 + i * .035}s forwards`;
    tag.appendChild(s);
  });

  // partículas doradas
  const cv = $('#splashCv'), cx = cv.getContext('2d');
  let W, H; const P = [];
  const rs = () => { W = cv.width = innerWidth; H = cv.height = innerHeight; };
  rs(); addEventListener('resize', rs);
  const mk = burst => {
    const a = Math.random() * 6.283, sp = burst ? Math.random() * 3 + .6 : 0;
    return { x: burst ? W / 2 : Math.random() * W, y: burst ? H / 2 : H + 10, vx: burst ? Math.cos(a) * sp : (Math.random() - .5) * .3, vy: burst ? Math.sin(a) * sp : -(Math.random() * .8 + .3), r: Math.random() * 2.2 + .5, life: 1, d: Math.random() * .006 + .003 };
  };
  for (let i = 0; i < 60; i++) P.push(mk(false));
  let alive = true, burstDone = false; const t0 = performance.now();
  (function loop(t) {
    if (!alive) return;
    cx.clearRect(0, 0, W, H);
    if (!burstDone && t - t0 > 1500) { burstDone = true; for (let i = 0; i < 90; i++) P.push(mk(true)); }
    P.forEach((p, i) => {
      p.x += p.vx; p.y += p.vy; p.vx *= .995; p.life -= p.d;
      if (p.life <= 0 || p.y < -10) { P[i] = mk(false); return; }
      cx.beginPath(); cx.fillStyle = `rgba(233,196,106,${Math.max(p.life, 0) * .85})`;
      cx.shadowBlur = 12; cx.shadowColor = 'rgba(233,196,106,.9)'; cx.arc(p.x, p.y, p.r, 0, 7); cx.fill();
    });
    requestAnimationFrame(loop);
  })(t0);

  // progreso y cierre
  let closed = false;
  function close() {
    if (closed) return; closed = true;
    try { sessionStorage.setItem('saoriSplash', '1'); } catch (e) {}
    splash.classList.add('out');
    setTimeout(() => document.body.classList.add('entered'), 500);
    setTimeout(() => { alive = false; document.documentElement.classList.remove('has-splash'); splash.remove(); }, 1400);
  }
  const DUR = 3800, s0 = performance.now();
  (function prog(t) {
    const p = Math.min((t - s0) / DUR, 1), e = 1 - Math.pow(1 - p, 2);
    num.textContent = Math.round(e * 100); bar.style.width = e * 100 + '%';
    if (p < 1) requestAnimationFrame(prog);
    else { splash.classList.add('ready'); enter.classList.add('show'); setTimeout(close, 2600); }
  })(s0);
  enter.addEventListener('click', close);
  $('#spSkip').addEventListener('click', close);
  addEventListener('keydown', e => { if (e.key === 'Escape' || e.key === 'Enter') close(); });
})();
