/* Beiz FX — interactive layer. Safe to remove: the site works without it.
   1) Agent-network canvas in the hero (reacts to the mouse)
   2) Scroll reveal for sections
   3) Cursor glow on panels
   4) Scroll progress line */
(function(){
  if (document.documentElement.classList.contains('classic')) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CYAN = '46,242,226';

  /* 4. progress line */
  var bar = document.createElement('div'); bar.className = 'fx-bar'; document.body.appendChild(bar);
  function onScroll(){ var h = document.documentElement; var p = h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight); bar.style.transform = 'scaleX(' + p + ')'; }
  addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* 2. scroll reveal */
  var targets = document.querySelectorAll('.hz-sec h2, .hz-sec .lede, .hz-sec .sp-line, .hz-sec ul, .hz-sec .card, .hz-sec table, .hz-sec .cv-foot, .hz-sec .hz-ctas, .hz-sec figure, .hz-sec .am, .hz-sec .dl');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('fx-in'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -8% 0px'});
    targets.forEach(function(el, i){
      var r = el.getBoundingClientRect();
      if (r.top < innerHeight) return;
      el.classList.add('fx-r'); el.style.transitionDelay = (i % 3) * 70 + 'ms'; io.observe(el);
    });
  }

  /* 3. cursor glow */
  document.querySelectorAll('.card, .tier, .jd, .dl, .rp-lane, .gov-band, .env-win, .panel, .scene, .offer, .au-line, .hz-ws').forEach(function(el){
    el.classList.add('fx-host');
    var g = document.createElement('span'); g.className = 'fx-glow'; el.insertBefore(g, el.firstChild);
    el.addEventListener('pointermove', function(ev){ var r = el.getBoundingClientRect(); el.style.setProperty('--mx', (ev.clientX - r.left) + 'px'); el.style.setProperty('--my', (ev.clientY - r.top) + 'px'); });
  });

  /* 1. agent network */
  var hero = document.querySelector('.hz-hero');
  if (!hero || innerWidth < 760) return; /* no canvas on phones: battery and speed */
  var cv = document.createElement('canvas'); cv.className = 'fx-canvas'; cv.setAttribute('aria-hidden','true'); hero.insertBefore(cv, hero.firstChild);
  var ctx = cv.getContext('2d'), W, H, dpr, pts = [], agents = [], mouse = {x:-9999, y:-9999}, run = true, t = 0;
  function size(){
    dpr = Math.min(2, devicePixelRatio || 1); W = hero.clientWidth; H = hero.clientHeight;
    cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
    var n = Math.round(Math.min(90, W * H / 14000)); pts = [];
    for (var i = 0; i < n; i++) pts.push({x:Math.random()*W, y:Math.random()*H, vx:(Math.random()-.5)*.25, vy:(Math.random()-.5)*.25});
    agents = []; for (var k = 0; k < 6; k++) agents.push({a:k*Math.PI/3, r:Math.min(W,H)*.32});
  }
  size(); addEventListener('resize', size);
  hero.addEventListener('pointermove', function(e){ var r = hero.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
  hero.addEventListener('pointerleave', function(){ mouse.x = mouse.y = -9999; });
  if (!reduce) new IntersectionObserver(function(es){ run = es[0].isIntersecting; if (run) requestAnimationFrame(frame); }).observe(hero);

  function frame(){
    if (!run) return;
    t += .004; ctx.clearRect(0,0,W,H);
    var cx = W*.72, cy = H*.5, i, j, p, q, dx, dy, d;
    for (i = 0; i < pts.length; i++){
      p = pts[i]; p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > W) p.vx *= -1; if (p.y < 0 || p.y > H) p.vy *= -1;
      dx = p.x - mouse.x; dy = p.y - mouse.y; d = Math.sqrt(dx*dx + dy*dy);
      if (d < 140){ p.x += dx/d*.6; p.y += dy/d*.6; }
    }
    for (i = 0; i < pts.length; i++){
      p = pts[i];
      for (j = i+1; j < pts.length; j++){
        q = pts[j]; dx = p.x-q.x; dy = p.y-q.y; d = dx*dx+dy*dy;
        if (d < 15000){ ctx.strokeStyle = 'rgba(' + CYAN + ',' + (0.13*(1-d/15000)) + ')'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y); ctx.stroke(); }
      }
      dx = p.x-mouse.x; dy = p.y-mouse.y; d = dx*dx+dy*dy;
      if (d < 40000){ ctx.strokeStyle = 'rgba(' + CYAN + ',' + (0.35*(1-d/40000)) + ')'; ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(mouse.x,mouse.y); ctx.stroke(); }
      ctx.fillStyle = 'rgba(' + CYAN + ',.55)'; ctx.fillRect(p.x-1, p.y-1, 2, 2);
    }
    /* the hero map already shows the agents and the human check, so the canvas stays a quiet network */
    if (!reduce) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame); /* with motion turned off this draws one still frame */
})();
