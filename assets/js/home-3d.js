/* index.html'den çıkarıldı (O11, DK-2026-08-03-18) — kalıcı 3D sahne (hero + tüm sayfa).
   Aynı konumda senkron <script src> ile yüklenir; davranış birebir aynı. */
/* ================= KALICI 3D SAHNE (hero + tüm sayfa) ================= */
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var svg = document.getElementById('isoSvg');
  if(!svg) return;
  var NS = 'http://www.w3.org/2000/svg';
  var CY = '#00c8f0';
  var cos30 = Math.cos(Math.PI/6), sin30 = Math.sin(Math.PI/6);
  var S = 34, OX = 258, OY = 201, C = 2.9;
  var theta = 0.15, jibPhi = 0, faceO = 0, dimBoost = 0;
  var segs = [], faces = [], texts = [];

  function proj(pt){
    var dx = pt[0]-C, dy = pt[1]-C, ct = Math.cos(theta), st = Math.sin(theta);
    var xr = C + dx*ct - dy*st, yr = C + dx*st + dy*ct;
    return [ OX + (xr - yr)*cos30*S, OY + (xr + yr)*sin30*S - pt[2]*S ];
  }
  function rotJib(pt){
    var mx = 4.6, my = 1.2;
    var dx = pt[0]-mx, dy = pt[1]-my, c = Math.cos(jibPhi), s2 = Math.sin(jibPhi);
    return [ mx + dx*c - dy*s2, my + dx*s2 + dy*c, pt[2] ];
  }
  var gFaces = document.createElementNS(NS,'g');
  var gLines = document.createElementNS(NS,'g');
  svg.appendChild(gFaces); svg.appendChild(gLines);

  function seg(a,b,g,o){
    o = o || {};
    var el = document.createElementNS(NS,'line');
    el.setAttribute('stroke', CY);
    el.setAttribute('stroke-width', o.w || 1.2);
    el.setAttribute('stroke-linecap','round');
    el.setAttribute('opacity', o.o != null ? o.o : .85);
    gLines.appendChild(el);
    segs.push({a:a, b:b, g:g, el:el, o:(o.o != null ? o.o : .85), d:(o.d || 0)});
  }
  function face(pts,fo){
    var el = document.createElementNS(NS,'polygon');
    el.setAttribute('fill', CY);
    el.setAttribute('opacity','0');
    gFaces.appendChild(el);
    faces.push({pts:pts, el:el, fo:fo});
  }

  var g;
  for (g = -1; g <= 6; g++){
    seg([g,-1,0],[g,6,0],'grid',{o:.13, w:1, d:.05 + (g+1)*.03});
    seg([-1,g,0],[6,g,0],'grid',{o:.13, w:1, d:.05 + (g+1)*.03});
  }
  function box(x,y,w,d,h,t,step,grp){
    [[x,y],[x+w,y],[x,y+d],[x+w,y+d]].forEach(function(c2,i){
      seg([c2[0],c2[1],0],[c2[0],c2[1],h],grp,{d:t + i*step, o:.9, w:1.3});
    });
    seg([x,y,h],[x+w,y,h],grp,{d:t+4*step, o:.9, w:1.3});
    seg([x,y,h],[x,y+d,h],grp,{d:t+4*step, o:.9, w:1.3});
    seg([x+w,y,h],[x+w,y+d,h],grp,{d:t+5*step, o:.9, w:1.3});
    seg([x,y+d,h],[x+w,y+d,h],grp,{d:t+5*step, o:.9, w:1.3});
  }
  box(0.6,2.8, 2,2, 4.6, .35, .12, 'bld');
  box(3.1,3.2, 2.4,1.6, 1.5, .8, .1, 'bld');
  var f;
  for (f = 1; f <= 4; f++){
    seg([0.6,4.8,f],[2.6,4.8,f],'bld',{o:.3, w:1, d:1.1 + f*.09});
    seg([2.6,4.8,f],[2.6,2.8,f],'bld',{o:.3, w:1, d:1.15 + f*.09});
  }
  face([[0.6,2.8,4.6],[2.6,2.8,4.6],[2.6,4.8,4.6],[0.6,4.8,4.6]], .10);
  face([[0.6,2.8,0],[2.6,2.8,0],[2.6,2.8,4.6],[0.6,2.8,4.6]], .05);
  face([[2.6,2.8,0],[2.6,4.8,0],[2.6,4.8,4.6],[2.6,2.8,4.6]], .05);
  face([[2.6,4.8,0],[0.6,4.8,0],[0.6,4.8,4.6],[2.6,4.8,4.6]], .07);
  face([[0.6,4.8,0],[0.6,2.8,0],[0.6,2.8,4.6],[0.6,4.8,4.6]], .07);
  face([[3.1,3.2,1.5],[5.5,3.2,1.5],[5.5,4.8,1.5],[3.1,4.8,1.5]], .08);
  seg([4.6,1.2,0],[4.6,1.2,5.4],'crane',{d:1.5, w:1.4, o:.95});
  seg([4.6,1.2,5.4],[1.4,1.2,5.4],'jib',{d:1.75, w:1.4, o:.95});
  seg([4.6,1.2,5.4],[5.6,1.2,5.4],'jib',{d:1.75, w:1.2, o:.7});
  seg([4.6,1.2,4.6],[3.4,1.2,5.4],'jib',{d:1.9, w:1, o:.5});
  seg([2.0,1.2,5.4],[2.0,1.2,3.6],'jib',{d:2.05, w:1, o:.6});
  seg([1.85,1.2,3.6],[2.15,1.2,3.6],'jib',{d:2.2, w:1.6, o:.9});
  seg([3.1,4.8,0],[3.1,5.35,0],'dim',{o:.5, w:1, d:2.3});
  seg([5.5,4.8,0],[5.5,5.35,0],'dim',{o:.5, w:1, d:2.3});
  seg([3.1,5.2,0],[5.5,5.2,0],'dim',{o:.6, w:1, d:2.4});
  (function(){
    var el = document.createElementNS(NS,'text');
    el.setAttribute('fill', CY); el.setAttribute('opacity','.75');
    el.setAttribute('font-size','11'); el.setAttribute('text-anchor','middle');
    el.setAttribute('font-family','Space Grotesk, sans-serif'); el.setAttribute('letter-spacing','2');
    el.textContent = '24.40 m';
    if(!reduce){ el.classList.add('iso-txt'); el.style.setProperty('--d','2.7s'); }
    gLines.appendChild(el);
    texts.push({p3:[4.3,5.75,0], el:el});
  })();
  [[30,30],[490,30],[30,410],[490,410]].forEach(function(c2){
    ['h','v'].forEach(function(dir){
      var el = document.createElementNS(NS,'line');
      var d = 7;
      el.setAttribute('x1', dir==='h' ? c2[0]-d : c2[0]);
      el.setAttribute('x2', dir==='h' ? c2[0]+d : c2[0]);
      el.setAttribute('y1', dir==='v' ? c2[1]-d : c2[1]);
      el.setAttribute('y2', dir==='v' ? c2[1]+d : c2[1]);
      el.setAttribute('stroke', CY); el.setAttribute('stroke-width','1'); el.setAttribute('opacity','.35');
      if(!reduce){ el.classList.add('iso-line'); el.style.setProperty('--len','14'); el.style.setProperty('--d','.1s'); }
      gLines.appendChild(el);
    });
  });

  /* yapısal düğüm noktaları — sektör görselleriyle aynı nabız animasyonu */
  var nodes = [];
  [[0.6,2.8,4.6],[2.6,2.8,4.6],[2.6,4.8,4.6],[0.6,4.8,4.6],
   [3.1,3.2,1.5],[5.5,4.8,1.5],[4.6,1.2,5.4],
   [2.0,1.2,3.6,'jib']].forEach(function(p, i){
    var el = document.createElementNS(NS,'circle');
    el.setAttribute('r','2.4'); el.setAttribute('fill', CY);
    /* çizim animasyonu bitene kadar gizli; free() içinde nabza geçiyor */
    el.setAttribute('opacity', reduce ? '.85' : '0');
    el.style.animationDelay = (i*0.38).toFixed(2) + 's';
    gLines.appendChild(el);
    nodes.push({p:[p[0],p[1],p[2]], g:p[3] || '', el:el});
  });

  function render(){
    var i, s2, A, B, p1, p2;
    for (i = 0; i < nodes.length; i++){
      var np = nodes[i].g === 'jib' ? rotJib(nodes[i].p) : nodes[i].p;
      var nq = proj(np);
      nodes[i].el.setAttribute('cx', nq[0].toFixed(1));
      nodes[i].el.setAttribute('cy', nq[1].toFixed(1));
    }
    for (i = 0; i < segs.length; i++){
      s2 = segs[i]; A = s2.a; B = s2.b;
      if (s2.g === 'jib'){ A = rotJib(A); B = rotJib(B); }
      p1 = proj(A); p2 = proj(B);
      s2.el.setAttribute('x1', p1[0].toFixed(1)); s2.el.setAttribute('y1', p1[1].toFixed(1));
      s2.el.setAttribute('x2', p2[0].toFixed(1)); s2.el.setAttribute('y2', p2[1].toFixed(1));
      if (s2.g === 'dim'){ s2.el.setAttribute('opacity', Math.min(1, s2.o + .45*dimBoost).toFixed(2)); }
    }
    for (i = 0; i < faces.length; i++){
      var fc = faces[i];
      fc.el.setAttribute('points', fc.pts.map(function(pt){ var q = proj(pt); return q[0].toFixed(1)+','+q[1].toFixed(1); }).join(' '));
      fc.el.setAttribute('opacity', (fc.fo * faceO).toFixed(3));
    }
    for (i = 0; i < texts.length; i++){
      var tp = proj(texts[i].p3);
      texts[i].el.setAttribute('x', tp[0].toFixed(1)); texts[i].el.setAttribute('y', tp[1].toFixed(1));
    }
  }
  render();

  if(!reduce){
    segs.forEach(function(s2){
      var len = Math.hypot(
        parseFloat(s2.el.getAttribute('x2')) - parseFloat(s2.el.getAttribute('x1')),
        parseFloat(s2.el.getAttribute('y2')) - parseFloat(s2.el.getAttribute('y1'))
      );
      s2.el.classList.add('iso-line');
      s2.el.style.setProperty('--len', len.toFixed(1));
      s2.el.style.setProperty('--d', s2.d.toFixed(2) + 's');
    });
  }
  var freed = false;
  function free(){
    if (freed) return; freed = true;
    segs.forEach(function(s2){
      s2.el.classList.remove('iso-line');
      s2.el.style.strokeDasharray = 'none';
      s2.el.style.strokeDashoffset = '0';
      s2.el.style.transition = 'none';
    });
    if (!reduce) nodes.forEach(function(n){ n.el.removeAttribute('opacity'); n.el.classList.add('vnode'); });
  }
  if (reduce) free(); else setTimeout(free, 3600);

  /* scroll: tüm sayfa ilerlemesi sahneyi döndürür; hero'dan çıkarken katman
     merkeze kayıp büyür ve düşük opaklıkta arka plana geçer */
  var layer = document.getElementById('heroDraw');
  var coord = document.getElementById('heroCoord');
  function smooth(a,b,x){ var t = Math.min(1, Math.max(0, (x-a)/(b-a))); return t*t*(3-2*t); }
  function applyProgress(p){
    p = Math.min(1, Math.max(0, p));
    theta = 0.15 + p * 1.55;
    jibPhi = p * 1.3;
    faceO = smooth(.10, .30, p);
    dimBoost = smooth(.35, .60, p);
    render();
    if (coord){
      var deg = ('00' + Math.round((theta*180/Math.PI) % 360)).slice(-3);
      coord.textContent = 'ORBIT ' + deg + '° · 38.42°N · 27.14°E';
    }
  }
  function applyLayer(q){
    if (!layer) return;
    var e = smooth(0, 1, q);
    layer.style.transform = 'translateX(' + (-24*e).toFixed(2) + 'vw) scale(' + (1 + .38*e).toFixed(3) + ')';
    layer.style.opacity = (1 - .87*e).toFixed(3);
  }
  window.CADBIM_hero = { set: function(p){ free(); applyProgress(p); }, setLayer: applyLayer };

  var wide = matchMedia('(min-width:900px)').matches;
  if (wide && !reduce){
    var ticking = false;
    var onScroll = function(){
      if (!freed && scrollY > 4) free();
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function(){
        ticking = false;
        var doc = document.documentElement;
        var range = doc.scrollHeight - innerHeight;
        applyProgress(range > 0 ? scrollY / range : 0);
        applyLayer(Math.min(1, scrollY / (innerHeight * 0.85)));
      });
    };
    addEventListener('scroll', onScroll, {passive:true});
    addEventListener('resize', onScroll, {passive:true});
  }

  /* sayaçlar */
  function runCounters(root){
    root.querySelectorAll('[data-n]').forEach(function(el){
      var target = parseInt(el.getAttribute('data-n'),10);
      if (reduce){ el.textContent = target.toLocaleString('tr-TR'); return; }
      var t0 = null, dur = 1400;
      function step(ts){
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0)/dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1-p,3))).toLocaleString('tr-TR');
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }
  var hero = document.querySelector('.hero');
  var stats = document.getElementById('statsBand');
  if (reduce || !('IntersectionObserver' in window)){
    if (hero) hero.classList.add('iso-on');
    if (stats) runCounters(stats);
  } else {
    var done = {};
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        if (e.target === hero && !done.h){ done.h = 1; hero.classList.add('iso-on'); io.unobserve(hero); }
        if (e.target === stats && !done.s){ done.s = 1; runCounters(stats); io.unobserve(stats); }
      });
    }, {threshold:.2});
    if (hero) io.observe(hero);
    if (stats) io.observe(stats);
  }
})();

/* ================= 3D SEKTÖR SEÇİCİ ================= */
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';
  var CY = '#00c8f0';
  var cos30 = Math.cos(Math.PI/6), sin30 = Math.sin(Math.PI/6);

  function bx(o,x,y,w,d,h,z0,op){
    z0 = z0 || 0; op = op || .9;
    [[x,y],[x+w,y],[x,y+d],[x+w,y+d]].forEach(function(c2){ o.push([[c2[0],c2[1],z0],[c2[0],c2[1],z0+h],op]); });
    o.push([[x,y,z0+h],[x+w,y,z0+h],op]); o.push([[x,y,z0+h],[x,y+d,z0+h],op]);
    o.push([[x+w,y,z0+h],[x+w,y+d,z0+h],op]); o.push([[x,y+d,z0+h],[x+w,y+d,z0+h],op]);
    o.push([[x,y,z0],[x+w,y,z0],op*.5]); o.push([[x,y,z0],[x,y+d,z0],op*.5]);
    o.push([[x+w,y,z0],[x+w,y+d,z0],op*.5]); o.push([[x,y+d,z0],[x+w,y+d,z0],op*.5]);
  }
  function ringZ(o,cx,cy,z,r,n,op){
    var i, pts = [];
    for (i = 0; i <= n; i++){ var a = i/n*2*Math.PI; pts.push([cx + r*Math.cos(a), cy + r*Math.sin(a), z]); }
    for (i = 0; i < n; i++){ o.push([pts[i], pts[i+1], op || .8]); }
  }
  function wheelY(o,cx,y,cz,r,n,op){
    var i, pts = [];
    for (i = 0; i <= n; i++){ var a = i/n*2*Math.PI; pts.push([cx + r*Math.cos(a), y, cz + r*Math.sin(a)]); }
    for (i = 0; i < n; i++){ o.push([pts[i], pts[i+1], op || .85]); }
  }
  var objects = {
    icmimarlik: function(){
      var o = [], i;
      /* oda: zemin cercevesi + iki duvar */
      o.push([[0.4,0.4,0],[4.2,0.4,0],.35]); o.push([[4.2,0.4,0],[4.2,3.4,0],.35]);
      o.push([[4.2,3.4,0],[0.4,3.4,0],.35]); o.push([[0.4,3.4,0],[0.4,0.4,0],.35]);
      for (i=1;i<5;i++){ o.push([[0.4+i*0.76,0.4,0.01],[0.4+i*0.76,3.4,0.01],.14]); }
      o.push([[0.4,0.4,0],[0.4,0.4,2.2],.8]); o.push([[4.2,0.4,0],[4.2,0.4,2.2],.8]);
      o.push([[0.4,3.4,0],[0.4,3.4,2.2],.8]);
      o.push([[0.4,0.4,2.2],[4.2,0.4,2.2],.7]); o.push([[0.4,0.4,2.2],[0.4,3.4,2.2],.7]);
      /* pencere (arka duvar) */
      o.push([[1.6,0.4,0.7],[3.1,0.4,0.7],.55]); o.push([[1.6,0.4,1.8],[3.1,0.4,1.8],.55]);
      o.push([[1.6,0.4,0.7],[1.6,0.4,1.8],.55]); o.push([[3.1,0.4,0.7],[3.1,0.4,1.8],.55]);
      o.push([[2.35,0.4,0.7],[2.35,0.4,1.8],.3]);
      /* kanepe */
      bx(o, 0.8,2.2, 1.6,0.7, 0.4, 0, .85);
      bx(o, 0.8,2.75, 1.6,0.18, 0.5, 0.35, .6);
      bx(o, 0.64,2.2, 0.16,0.9, 0.55, 0, .5);
      bx(o, 2.4,2.2, 0.16,0.9, 0.55, 0, .5);
      /* sehpa + sarkit */
      bx(o, 2.9,1.5, 0.7,0.7, 0.35, 0, .6);
      o.push([[3.25,1.85,2.2],[3.25,1.85,1.35],.6]);
      o.push([[3.05,1.35,1.35],[3.45,1.35,1.35],0]);
      o.push([[3.25,1.85,1.35],[3.05,1.85,1.15],.8]); o.push([[3.25,1.85,1.35],[3.45,1.85,1.15],.8]);
      o.push([[3.05,1.85,1.15],[3.45,1.85,1.15],.8]);
      /* tablo (sol duvar) */
      o.push([[0.4,1.0,1.0],[0.4,1.8,1.0],.55]); o.push([[0.4,1.8,1.0],[0.4,1.8,1.6],.55]);
      o.push([[0.4,1.8,1.6],[0.4,1.0,1.6],.55]); o.push([[0.4,1.0,1.6],[0.4,1.0,1.0],.55]);
      return o;
    },
    tesisat: function(){
      var o = [], i;
      /* klima santrali */
      bx(o, 0.4,0.6, 1.2,1.0, 1.3, 0, .85);
      o.push([[1.0,0.6,0.3],[1.0,0.6,1.0],.4]);
      /* ana kanal (yuksek kot) */
      bx(o, 1.6,0.9, 2.7,0.4, 0.4, 1.7, .8);
      for (i=1;i<4;i++){
        o.push([[1.6+i*0.68,0.9,1.7],[1.6+i*0.68,1.3,1.7],.3]);
        o.push([[1.6+i*0.68,0.9,2.1],[1.6+i*0.68,1.3,2.1],.3]);
      }
      /* dikey bransman + difuzor */
      bx(o, 2.5,1.0, 0.34,0.2, 0.75, 0.95, .6);
      bx(o, 2.38,0.92, 0.58,0.36, 0.06, 0.86, .8);
      bx(o, 3.5,1.0, 0.34,0.2, 0.75, 0.95, .6);
      bx(o, 3.38,0.92, 0.58,0.36, 0.06, 0.86, .8);
      /* borulama (dusuk kot, gidis-donus) + vana */
      o.push([[1.6,2.6,0.35],[4.4,2.6,0.35],.7]);
      o.push([[1.6,2.85,0.22],[4.4,2.85,0.22],.45]);
      o.push([[2.9,2.6,0.35],[3.06,2.52,0.27],.8]); o.push([[2.9,2.6,0.35],[3.06,2.68,0.43],.8]);
      o.push([[3.22,2.6,0.35],[3.06,2.52,0.27],.8]); o.push([[3.22,2.6,0.35],[3.06,2.68,0.43],.8]);
      return o;
    },
    mimari: function(){
      var o = [], i;
      bx(o, 0.4,0.5, 3.2,2.0, 1.0, 0, .55);
      bx(o, 1.15,0.95, 1.7,1.1, 3.6, 1.0, .9);
      var tx0=1.15, tx1=2.85, tz0=1.0, tz1=4.6;
      for (i=1;i<5;i++){ var x=tx0+(tx1-tx0)*i/5; o.push([[x,0.95,tz0],[x,0.95,tz1],.35]); }
      for (i=1;i<7;i++){ var z=tz0+(tz1-tz0)*i/7; o.push([[tx0,0.95,z],[tx1,0.95,z],.35]); }
      for (i=1;i<4;i++){ var z2=tz0+(tz1-tz0)*i/4; o.push([[tx1,0.95,z2],[tx1,2.05,z2],.22]); }
      o.push([[3.6,0.5,1.0],[4.3,0.5,1.0],.85]); o.push([[4.3,0.5,1.0],[4.3,2.5,1.0],.85]);
      o.push([[4.3,2.5,1.0],[3.6,2.5,1.0],.85]); o.push([[3.6,2.5,1.0],[3.6,0.5,1.0],.5]);
      o.push([[4.1,0.7,1.0],[4.1,0.7,0],.6]); o.push([[4.1,2.3,1.0],[4.1,2.3,0],.6]);
      o.push([[0.0,0.1,0],[4.8,0.1,0],.18]); o.push([[4.8,0.1,0],[4.8,3.0,0],.18]);
      o.push([[4.8,3.0,0],[0.0,3.0,0],.18]); o.push([[0.0,3.0,0],[0.0,0.1,0],.18]);
      return o;
    },
    insaat: function(){
      var o = [];
      o.push([[0.4,0.4,0.05],[3.8,0.4,0.05],.5]); o.push([[3.8,0.4,0.05],[3.8,3.2,0.05],.5]);
      o.push([[3.8,3.2,0.05],[0.4,3.2,0.05],.5]); o.push([[0.4,3.2,0.05],[0.4,0.4,0.05],.5]);
      bx(o, 0.8,0.8, 1.2,1.9, 0.8);
      bx(o, 2.3,0.8, 1.1,1.2, 0.5);
      o.push([[3.1,2.6,0],[3.1,2.6,3.3],.95]);
      o.push([[3.1,2.6,3.3],[0.9,2.6,3.3],.95]); o.push([[3.1,2.6,3.3],[3.8,2.6,3.3],.7]);
      o.push([[3.1,2.6,2.7],[2.1,2.6,3.3],.5]);
      o.push([[1.4,2.6,3.3],[1.4,2.6,1.6],.6]); o.push([[1.28,2.6,1.6],[1.52,2.6,1.6],.9]);
      return o;
    },
    makine: function(){
      var o = [], i;
      ringZ(o, 2.1,2.1, 0.55, 1.35, 28, .85);
      ringZ(o, 2.1,2.1, 1.25, 1.35, 28, .85);
      var nT = 14, tw = 0.10;
      for (i = 0; i < nT; i++){
        var a = i/nT*2*Math.PI, a0 = a-tw, a1 = a+tw;
        [0.55,1.25].forEach(function(z){
          var p0=[2.1+1.35*Math.cos(a0), 2.1+1.35*Math.sin(a0), z];
          var p1=[2.1+1.6*Math.cos(a0), 2.1+1.6*Math.sin(a0), z];
          var p2=[2.1+1.6*Math.cos(a1), 2.1+1.6*Math.sin(a1), z];
          var p3=[2.1+1.35*Math.cos(a1), 2.1+1.35*Math.sin(a1), z];
          o.push([p0,p1,.85]); o.push([p1,p2,.85]); o.push([p2,p3,.85]);
        });
        var pa=[2.1+1.6*Math.cos(a0), 2.1+1.6*Math.sin(a0)], pb=[2.1+1.6*Math.cos(a1), 2.1+1.6*Math.sin(a1)];
        o.push([[pa[0],pa[1],0.55],[pa[0],pa[1],1.25],.55]);
        o.push([[pb[0],pb[1],0.55],[pb[0],pb[1],1.25],.55]);
      }
      for (i = 0; i < 8; i++){
        var aa = i/8*2*Math.PI, ca = Math.cos(aa), sa = Math.sin(aa);
        o.push([[2.1+0.4*ca,2.1+0.4*sa,0.55],[2.1+1.35*ca,2.1+1.35*sa,0.55],.35]);
        o.push([[2.1+0.4*ca,2.1+0.4*sa,1.25],[2.1+1.35*ca,2.1+1.35*sa,1.25],.35]);
      }
      ringZ(o, 2.1,2.1, 0.55, 0.4, 12, .6);
      ringZ(o, 2.1,2.1, 1.25, 0.4, 12, .6);
      o.push([[2.1,2.1,0],[2.1,2.1,1.9],.9]);
      return o;
    },
    otomotiv: function(){
      var o = [], i;
      var railY1=1.3, railY2=2.9, lx0=0, lx1=5.6;
      o.push([[lx0,railY1,0],[lx1,railY1,0],.5]);
      o.push([[lx0,railY2,0],[lx1,railY2,0],.5]);
      for (i=0;i<=14;i++){ var x=lx0+i*(lx1-lx0)/14; o.push([[x,railY1,0],[x,railY2,0],.16]); }
      var yf=1.65, yb=2.55, z0=0.1;
      var profile=[[1.9,z0+0.28],[2.15,z0+0.42],[2.65,z0+0.42],[2.85,z0+0.68],[3.35,z0+0.68],[3.55,z0+0.42],[3.85,z0+0.42],[4.05,z0+0.28]];
      for (i=0;i<profile.length-1;i++){
        var a=profile[i], b=profile[i+1];
        o.push([[a[0],yf,a[1]],[b[0],yf,b[1]],.85]);
        o.push([[a[0],yb,a[1]],[b[0],yb,b[1]],.85]);
      }
      profile.forEach(function(p){ o.push([[p[0],yf,p[1]],[p[0],yb,p[1]],.4]); });
      wheelY(o, 2.15,yf, z0+0.22, 0.22, 10, .5);
      wheelY(o, 2.15,yb, z0+0.22, 0.22, 10, .35);
      wheelY(o, 3.75,yf, z0+0.22, 0.22, 10, .5);
      wheelY(o, 3.75,yb, z0+0.22, 0.22, 10, .35);
      o.push([[0.2,0.7,0],[0.2,0.7,2.0],.8]);
      o.push([[0.2,0.7,2.0],[2.6,0.7,2.0],.85]);
      o.push([[2.6,0.7,2.0],[2.6,1.55,1.3],.9]);
      o.push([[2.6,1.55,1.3],[2.9,1.55,0.9],.95]);
      o.push([[2.6,1.55,1.3],[2.3,1.55,0.9],.95]);
      o.push([[2.9,1.55,0.9],[2.3,1.55,0.9],.5]);
      o.push([[4.8,3.5,0],[4.8,3.5,2.0],.8]);
      o.push([[4.8,3.5,2.0],[2.4,3.5,2.0],.85]);
      o.push([[2.4,3.5,2.0],[2.4,2.65,1.3],.9]);
      o.push([[2.4,2.65,1.3],[2.1,2.65,0.9],.95]);
      o.push([[2.4,2.65,1.3],[2.7,2.65,0.9],.95]);
      o.push([[2.1,2.65,0.9],[2.7,2.65,0.9],.5]);
      return o;
    },
    medya: function(){
      var o = [], i;
      bx(o, 1.2,1.45, 1.5,1.1, 1.05, 1.5);
      for (i = 0; i < 12; i++){
        var a1 = i/12*2*Math.PI, a2 = (i+1)/12*2*Math.PI;
        o.push([[2.7, 1.35+0.35*Math.cos(a1), 2.02+0.35*Math.sin(a1)],[2.7, 1.35+0.35*Math.cos(a2), 2.02+0.35*Math.sin(a2)],.85]);
        o.push([[3.15, 1.35+0.42*Math.cos(a1), 2.02+0.42*Math.sin(a1)],[3.15, 1.35+0.42*Math.cos(a2), 2.02+0.42*Math.sin(a2)],.85]);
      }
      for (i = 0; i < 4; i++){
        var a3 = i/4*2*Math.PI + .4;
        o.push([[2.7, 1.35+0.35*Math.cos(a3), 2.02+0.35*Math.sin(a3)],[3.15, 1.35+0.42*Math.cos(a3), 2.02+0.42*Math.sin(a3)],.6]);
      }
      o.push([[1.95,2.0,1.5],[1.0,1.0,0],.75]); o.push([[1.95,2.0,1.5],[3.0,0.9,0],.75]); o.push([[1.95,2.0,1.5],[2.1,3.2,0],.75]);
      bx(o, 1.45,1.7, 0.5,0.5, 0.3, 2.55, .6);
      return o;
    },
    egitim: function(){
      var o = [], i, j;
      o.push([[0,0,0],[4.4,0,0],.18]); o.push([[4.4,0,0],[4.4,3.4,0],.18]);
      o.push([[4.4,3.4,0],[0,3.4,0],.18]); o.push([[0,3.4,0],[0,0,0],.18]);
      var sx0=0.5, sx1=2.9, sz0=0.9, sz1=2.3, sy=0.25;
      o.push([[sx0,sy,sz0],[sx1,sy,sz0],.9]); o.push([[sx1,sy,sz0],[sx1,sy,sz1],.9]);
      o.push([[sx1,sy,sz1],[sx0,sy,sz1],.9]); o.push([[sx0,sy,sz1],[sx0,sy,sz0],.9]);
      [1.3,1.6,1.9].forEach(function(z){ o.push([[sx0+0.25,sy,z],[sx1-0.25,sy,z],.4]); });
      o.push([[(sx0+sx1)/2,sy,sz0],[(sx0+sx1)/2,sy,0],.5]);
      o.push([[(sx0+sx1)/2-0.3,sy,0],[(sx0+sx1)/2+0.3,sy,0],.5]);
      bx(o, 3.3,0.35, 0.45,0.4, 0.85, 0, .6);
      for (i=0;i<2;i++){
        for (j=0;j<3;j++){
          var dx=0.5+j*1.15, dy=1.4+i*1.0;
          bx(o, dx,dy, 0.75,0.55, 0.45, 0, .55);
        }
      }
      return o;
    },
    havacilik: function(){
      var o = [];
      o.push([[0.5,1.9,1],[3.5,1.9,1],.9]); o.push([[0.5,2.3,1],[3.5,2.3,1],.9]);
      o.push([[3.5,1.9,1],[4.1,2.1,1],.9]); o.push([[3.5,2.3,1],[4.1,2.1,1],.9]);
      o.push([[0.5,1.9,1],[0.5,2.3,1],.7]);
      o.push([[0.5,1.9,1.35],[3.5,1.9,1.35],.35]); o.push([[0.5,2.3,1.35],[3.5,2.3,1.35],.35]);
      o.push([[2.55,1.9,1],[1.45,0.25,1.1],.85]); o.push([[1.95,1.9,1],[1.15,0.25,1.1],.85]);
      o.push([[1.45,0.25,1.1],[1.15,0.25,1.1],.85]);
      o.push([[2.55,2.3,1],[1.45,3.95,1.1],.85]); o.push([[1.95,2.3,1],[1.15,3.95,1.1],.85]);
      o.push([[1.45,3.95,1.1],[1.15,3.95,1.1],.85]);
      o.push([[0.6,2.1,1],[0.35,2.1,1.85],.85]); o.push([[1.15,2.1,1],[0.7,2.1,1.85],.85]);
      o.push([[0.35,2.1,1.85],[0.7,2.1,1.85],.85]);
      o.push([[0.8,1.95,1.05],[0.45,1.35,1.15],.6]); o.push([[0.8,2.25,1.05],[0.45,2.85,1.15],.6]);
      return o;
    }
  };

  /* Sektör sayfalarındaki teknik çizim diliyle aynı aksan renkleri */
  var ACCENT = {
    mimari:'#818cf8', icmimarlik:'#f472b6', tesisat:'#2dd4bf', insaat:'#22c55e', makine:'#f59e0b', otomotiv:'#ef4444',
    medya:'#c084fc', egitim:'#38bdf8', havacilik:'#a5b4fc',
    bim:'#818cf8', gorsellestirme:'#f59e0b', yaratici_icerik:'#e25922',
    gerceklik_yakalama:'#fbbf24', dijital_donusum:'#38bdf8', insaat_yonetimi:'#22c55e',
    dijital_ikiz:'#38bdf8', cam:'#f87171', simulasyon:'#fbbf24',
    tolerans_analizi:'#c084fc', tasarim_otomasyonu:'#fbbf24', fabrika_tasarimi:'#38bdf8',
    plm:'#38bdf8', pdm:'#34d399', nesting:'#34d399', eklemeli_imalat:'#a5b4fc',
    egitimler:'#38bdf8', sanatsal_baski:'#e879f9'
  };
  function hexRgba(hex, a){
    var h = hex.replace('#','');
    return 'rgba(' + parseInt(h.slice(0,2),16) + ',' + parseInt(h.slice(2,4),16)
         + ',' + parseInt(h.slice(4,6),16) + ',' + a + ')';
  }

  function createViewer(svg, objMap){
    var S = 40, OX = 210, OY = 225, C = 2.1, theta = 0.15;
    var accent = CY;
    function proj(pt){
      var dx = pt[0]-C, dy = pt[1]-C, ct = Math.cos(theta), st = Math.sin(theta);
      var xr = C + dx*ct - dy*st, yr = C + dx*st + dy*ct;
      return [ OX + (xr - yr)*cos30*S, OY + (xr + yr)*sin30*S - pt[2]*S ];
    }
    /* Mavi kopya ızgarası ve aksan parıltısı panelin tamamını kaplasın diye
       SVG içinde değil, kapsayıcıda (.sectorsel-view) CSS ile çiziliyor. */
    var panel = svg.parentNode;
    if (panel && panel.querySelector && !panel.querySelector('.vcorner')){
      ['tl','tr','bl','br'].forEach(function(c){
        var d = document.createElement('div');
        d.className = 'vcorner ' + c;
        panel.appendChild(d);
      });
    }
    var gPlane = document.createElementNS(NS,'g');   // izometrik zemin düzlemi
    var gAll   = document.createElementNS(NS,'g');   // model
    var gNode  = document.createElementNS(NS,'g');   // düğüm noktaları
    var gUi    = document.createElementNS(NS,'g');   // eksen üçlüsü + okuma
    svg.appendChild(gPlane); svg.appendChild(gAll); svg.appendChild(gNode); svg.appendChild(gUi);

    /* tarama çizgisi — sektör görselleriyle aynı hareket */
    var scan = document.createElementNS(NS,'line');
    scan.setAttribute('x1','14'); scan.setAttribute('x2','406');
    scan.setAttribute('y1','0');  scan.setAttribute('y2','0');
    scan.setAttribute('stroke', CY); scan.setAttribute('stroke-opacity','.45');
    scan.setAttribute('stroke-width','1');
    if (!reduce) scan.setAttribute('class','vscan');
    svg.appendChild(scan);

    /* eksen üçlüsü (X/Y/Z) — modelle birlikte döner */
    var AX = 46, AY = 296, AL = 24;
    var axis = [];
    ['X','Y','Z'].forEach(function(nm){
      var ln = document.createElementNS(NS,'line');
      ln.setAttribute('stroke-width','1.1'); ln.setAttribute('stroke-linecap','round');
      ln.setAttribute('stroke-opacity','.6');
      var tx = document.createElementNS(NS,'text');
      tx.setAttribute('font-size','8'); tx.setAttribute('font-family','ui-monospace,monospace');
      tx.setAttribute('fill-opacity','.7'); tx.textContent = nm;
      gUi.appendChild(ln); gUi.appendChild(tx);
      axis.push({ln:ln, tx:tx});
    });
    var readout = document.createElementNS(NS,'text');
    readout.setAttribute('x','406'); readout.setAttribute('y','302');
    readout.setAttribute('text-anchor','end');
    readout.setAttribute('font-size','9'); readout.setAttribute('letter-spacing','1.6');
    readout.setAttribute('font-family','ui-monospace,monospace');
    readout.setAttribute('fill','rgba(255,255,255,.4)');
    gUi.appendChild(readout);

    var lines = [], plane = [], nodes = [], pending = null, offX = 0, offY = 0;
    function place(el, p1, p2){
      el.setAttribute('x1', (p1[0]+offX).toFixed(1)); el.setAttribute('y1', (p1[1]+offY).toFixed(1));
      el.setAttribute('x2', (p2[0]+offX).toFixed(1)); el.setAttribute('y2', (p2[1]+offY).toFixed(1));
    }
    function renderObj(){
      var i, q1, q2, cache = [];
      /* Model dönerken izdüşüm kutusu kayar; her karede yeniden merkezle ki
         sahne yörünge boyunca kadrajın ortasında kalsın. */
      var mnX=Infinity, mxX=-Infinity, mnY=Infinity, mxY=-Infinity;
      for (i = 0; i < lines.length; i++){
        q1 = proj(lines[i].a); q2 = proj(lines[i].b);
        cache.push(q1, q2);
        if(q1[0]<mnX)mnX=q1[0]; if(q1[0]>mxX)mxX=q1[0];
        if(q2[0]<mnX)mnX=q2[0]; if(q2[0]>mxX)mxX=q2[0];
        if(q1[1]<mnY)mnY=q1[1]; if(q1[1]>mxY)mxY=q1[1];
        if(q2[1]<mnY)mnY=q2[1]; if(q2[1]>mxY)mxY=q2[1];
      }
      if (lines.length){
        offX = 210 - (mnX+mxX)/2;
        offY = 170 - (mnY+mxY)/2;
      }
      for (i = 0; i < lines.length; i++) place(lines[i].el, cache[i*2], cache[i*2+1]);
      for (i = 0; i < plane.length; i++) place(plane[i].el, proj(plane[i].a), proj(plane[i].b));
      for (i = 0; i < nodes.length; i++){
        var q = proj(nodes[i].p);
        nodes[i].el.setAttribute('cx', (q[0]+offX).toFixed(1));
        nodes[i].el.setAttribute('cy', (q[1]+offY).toFixed(1));
      }
      /* eksen üçlüsü: birim vektörlerin ekran izdüşümü */
      var o0 = proj([0,0,0]);
      [[1,0,0],[0,1,0],[0,0,1]].forEach(function(v, k){
        var q = proj(v), dx = q[0]-o0[0], dy = q[1]-o0[1];
        var m = Math.hypot(dx,dy) || 1;
        var ex = AX + dx/m*AL, ey = AY + dy/m*AL;
        axis[k].ln.setAttribute('x1',AX); axis[k].ln.setAttribute('y1',AY);
        axis[k].ln.setAttribute('x2',ex.toFixed(1)); axis[k].ln.setAttribute('y2',ey.toFixed(1));
        axis[k].tx.setAttribute('x', (AX + dx/m*(AL+7)).toFixed(1));
        axis[k].tx.setAttribute('y', (AY + dy/m*(AL+7) + 3).toFixed(1));
      });
      var deg = Math.round((theta * 180 / Math.PI) % 360); if (deg < 0) deg += 360;
      readout.textContent = 'ISO · ORBIT ' + ('00' + deg).slice(-3) + '°';
    }
    function show(key){
      var build = objMap[key];
      if (!build) return;
      accent = ACCENT[key] || CY;
      if (panel && panel.style){
        panel.style.setProperty('--acc', accent);
        panel.style.setProperty('--accGlow', hexRgba(accent, .16));
      }
      scan.setAttribute('stroke', accent);
      axis.forEach(function(a){ a.ln.setAttribute('stroke', accent); a.tx.setAttribute('fill', accent); });
      while (gAll.firstChild) gAll.removeChild(gAll.firstChild);
      while (gPlane.firstChild) gPlane.removeChild(gPlane.firstChild);
      while (gNode.firstChild) gNode.removeChild(gNode.firstChild);
      lines = []; plane = []; nodes = [];
      var data = build();
      var minX=Infinity,maxX=-Infinity,minY=Infinity,maxY=-Infinity;
      var mnx=Infinity,mxx=-Infinity,mny=Infinity,mxy=-Infinity,mxz=-Infinity;
      data.forEach(function(sd){
        [sd[0],sd[1]].forEach(function(p){
          var q = proj(p);
          if(q[0]<minX)minX=q[0]; if(q[0]>maxX)maxX=q[0];
          if(q[1]<minY)minY=q[1]; if(q[1]>maxY)maxY=q[1];
          if(p[0]<mnx)mnx=p[0]; if(p[0]>mxx)mxx=p[0];
          if(p[1]<mny)mny=p[1]; if(p[1]>mxy)mxy=p[1];
          if(p[2]>mxz)mxz=p[2];
        });
      });
      offX = 210 - (minX+maxX)/2;
      offY = 170 - (minY+maxY)/2;

      /* zemin düzlemi — modelin ayak izini biraz taşan izometrik ızgara */
      var pad = 0.6, step = 0.7;
      var x0 = Math.floor((mnx-pad)/step)*step, x1 = Math.ceil((mxx+pad)/step)*step;
      var y0 = Math.floor((mny-pad)/step)*step, y1 = Math.ceil((mxy+pad)/step)*step;
      function planeSeg(a,b,op){
        var el = document.createElementNS(NS,'line');
        el.setAttribute('stroke', accent); el.setAttribute('stroke-width','1');
        el.setAttribute('opacity', op);
        gPlane.appendChild(el); plane.push({a:a,b:b,el:el});
      }
      var t;
      for (t = x0; t <= x1 + 1e-6; t += step) planeSeg([t,y0,0],[t,y1,0], .11);
      for (t = y0; t <= y1 + 1e-6; t += step) planeSeg([x0,t,0],[x1,t,0], .11);
      planeSeg([x0,y0,0],[x1,y0,0], .26); planeSeg([x0,y0,0],[x0,y1,0], .26);

      data.forEach(function(sd){
        var el = document.createElementNS(NS,'line');
        el.setAttribute('stroke', accent);
        el.setAttribute('stroke-width', 1.25);
        el.setAttribute('stroke-linecap','round');
        el.setAttribute('opacity', sd[2] != null ? sd[2] : .85);
        gAll.appendChild(el);
        lines.push({a:sd[0], b:sd[1], el:el});
      });

      /* düğüm noktaları — en tepedeki birkaç köşe (kalabalık yapmadan) */
      var seen = {}, cand = [];
      data.forEach(function(sd){
        [sd[0],sd[1]].forEach(function(p){
          var k = p[0].toFixed(2)+'|'+p[1].toFixed(2)+'|'+p[2].toFixed(2);
          if (!seen[k]){ seen[k] = 1; cand.push(p); }
        });
      });
      cand.sort(function(a,b){ return b[2] - a[2]; });
      cand.filter(function(p){ return p[2] > mxz * 0.55; }).slice(0, 7).forEach(function(p, i){
        var el = document.createElementNS(NS,'circle');
        el.setAttribute('r','2.6'); el.setAttribute('fill', accent);
        if (!reduce){ el.setAttribute('class','vnode'); el.style.animationDelay = (i*0.42).toFixed(2)+'s'; }
        gNode.appendChild(el); nodes.push({p:p, el:el});
      });
      renderObj();
      if (!reduce){
        lines.forEach(function(l, i){
          var len = Math.hypot(
            parseFloat(l.el.getAttribute('x2')) - parseFloat(l.el.getAttribute('x1')),
            parseFloat(l.el.getAttribute('y2')) - parseFloat(l.el.getAttribute('y1'))
          );
          l.el.classList.add('iso-line','iso-fast');
          l.el.style.setProperty('--len', len.toFixed(1));
          l.el.style.setProperty('--d', (i * 0.012).toFixed(3) + 's');
        });
        svg.classList.remove('iso-on');
        requestAnimationFrame(function(){ requestAnimationFrame(function(){ svg.classList.add('iso-on'); }); });
        if (pending) clearTimeout(pending);
        spinning = false;
        spinStart = 0;
        pending = setTimeout(function(){
          lines.forEach(function(l){
            l.el.classList.remove('iso-line','iso-fast');
            l.el.style.strokeDasharray = 'none';
            l.el.style.strokeDashoffset = '0';
            l.el.style.transition = 'none';
          });
          spinning = true;
        }, 900);
      }
    }
    var visible = false, spinning = false, rafOn = false, spinStart = 0;
    function loop(ts){
      if (!visible || reduce){ rafOn = false; return; }
      if (spinning){
        if (!spinStart) spinStart = ts;
        if (ts - spinStart > 16000){ spinning = false; rafOn = false; return; }
        theta += 0.0035; renderObj();
      }
      requestAnimationFrame(loop);
    }
    function ensureLoop(){ if (!rafOn && !reduce){ rafOn = true; requestAnimationFrame(loop); } }
    if ('IntersectionObserver' in window){
      new IntersectionObserver(function(es){
        es.forEach(function(e){ visible = e.isIntersecting; if (visible) ensureLoop(); });
      }, {threshold:.15}).observe(svg);
    } else { visible = true; ensureLoop(); }
    return { show: show };
  }

  var solutions = {
    bim: function(){
      var o = [], i;
      bx(o, 0.8,0.8, 2.2,1.8, 3.2, 0, .85);
      for (i=1;i<4;i++){ var z=i*0.8;
        o.push([[0.8,0.8,z],[3.0,0.8,z],.4]); o.push([[3.0,0.8,z],[3.0,2.6,z],.4]);
        o.push([[3.0,2.6,z],[0.8,2.6,z],.25]); o.push([[0.8,2.6,z],[0.8,0.8,z],.25]);
      }
      o.push([[3.7,1.0,0.6],[3.7,2.4,0.6],.8]); o.push([[3.7,2.4,0.6],[3.7,2.4,2.6],.8]);
      o.push([[3.7,2.4,2.6],[3.7,1.0,2.6],.8]); o.push([[3.7,1.0,2.6],[3.7,1.0,0.6],.8]);
      [1.0,1.5,2.0].forEach(function(z){ o.push([[3.7,1.15,z],[3.7,2.25,z],.4]); });
      o.push([[3.0,1.7,1.6],[3.7,1.7,1.6],.45]);
      return o;
    },
    gorsellestirme: function(){
      var o = [];
      ringZ(o, 3.2,2.1, 1.4, 0.9, 20, .8);
      ringZ(o, 3.2,2.1, 1.85, 0.72, 16, .6);
      ringZ(o, 3.2,2.1, 0.95, 0.72, 16, .6);
      ringZ(o, 3.2,2.1, 2.15, 0.4, 12, .45);
      ringZ(o, 3.2,2.1, 0.65, 0.4, 12, .45);
      bx(o, 0.3,1.75, 0.7,0.7, 0.55, 1.1, .9);
      var cx=1.0, cy=2.1, cz=1.4;
      o.push([[cx,cy,cz],[2.3,1.35,0.6],.55]); o.push([[cx,cy,cz],[2.3,2.85,0.6],.55]);
      o.push([[cx,cy,cz],[2.3,1.35,2.2],.55]); o.push([[cx,cy,cz],[2.3,2.85,2.2],.55]);
      o.push([[2.3,1.35,0.6],[2.3,2.85,0.6],.4]); o.push([[2.3,2.85,0.6],[2.3,2.85,2.2],.4]);
      o.push([[2.3,2.85,2.2],[2.3,1.35,2.2],.4]); o.push([[2.3,1.35,2.2],[2.3,1.35,0.6],.4]);
      return o;
    },
    yaratici_icerik: function(){
      var o = [], i;
      o.push([[0.3,0.3,0],[4.5,0.3,0],.35]); o.push([[4.5,0.3,0],[4.5,3.5,0],.35]);
      o.push([[4.5,3.5,0],[0.3,3.5,0],.35]); o.push([[0.3,3.5,0],[0.3,0.3,0],.35]);
      var pts = [];
      for (i=0;i<=24;i++){
        var t=i/24;
        var x = Math.pow(1-t,3)*0.7 + 3*Math.pow(1-t,2)*t*1.6 + 3*(1-t)*t*t*3.2 + Math.pow(t,3)*4.1;
        var y = Math.pow(1-t,3)*3.0 + 3*Math.pow(1-t,2)*t*0.6 + 3*(1-t)*t*t*3.6 + Math.pow(t,3)*0.9;
        pts.push([x,y,0.04]);
      }
      for (i=0;i<pts.length-1;i++) o.push([pts[i],pts[i+1],.9]);
      o.push([[0.7,3.0,0.04],[1.6,0.6,0.04],.3]); o.push([[4.1,0.9,0.04],[3.2,3.6,0.04],.3]);
      [[0.7,3.0],[1.6,0.6],[3.2,3.6],[4.1,0.9]].forEach(function(p){ o.push([[p[0],p[1],0],[p[0],p[1],0.35],.6]); });
      return o;
    },
    gerceklik_yakalama: function(){
      var o = [], i;
      var hx=1.0, hy=2.6, hz=1.7;
      o.push([[hx,hy,hz],[0.5,2.0,0],.85]); o.push([[hx,hy,hz],[1.6,2.2,0],.85]); o.push([[hx,hy,hz],[0.9,3.4,0],.85]);
      bx(o, hx-0.18, hy-0.18, 0.36,0.36, 0.3, hz, .9);
      bx(o, 2.9,1.1, 1.4,1.1, 1.7, 0, .8);
      bx(o, 3.15,1.35, 0.9,0.6, 0.5, 1.7, .6);
      for (i=0;i<5;i++){
        o.push([[hx+0.2,hy,hz+0.1],[2.9,1.4+i*0.2, 0.2+i*0.45],.28]);
      }
      return o;
    },
    dijital_donusum: function(){
      var o = [], i;
      var cx=2.1, cy=2.1, r=1.7, z=0.9, n=24;
      for (i=0;i<n;i++){
        if (i%8===7) continue;
        var a1=i/n*2*Math.PI, a2=(i+1)/n*2*Math.PI;
        o.push([[cx+r*Math.cos(a1),cy+r*Math.sin(a1),z],[cx+r*Math.cos(a2),cy+r*Math.sin(a2),z],.8]);
      }
      [7,15,23].forEach(function(k){
        var a=(k+1)/n*2*Math.PI;
        var px=cx+r*Math.cos(a), py=cy+r*Math.sin(a);
        var ta=a+Math.PI/2;
        o.push([[px,py,z],[px-0.32*Math.cos(ta)+0.22*Math.cos(a), py-0.32*Math.sin(ta)+0.22*Math.sin(a), z],.9]);
        o.push([[px,py,z],[px-0.32*Math.cos(ta)-0.22*Math.cos(a), py-0.32*Math.sin(ta)-0.22*Math.sin(a), z],.9]);
      });
      bx(o, 1.5,1.5, 1.2,1.2, 0.5, 0, .3);
      bx(o, 1.7,1.7, 0.8,0.8, 1.5, 0.5, .9);
      return o;
    },
    insaat_yonetimi: function(){
      var o = [];
      [[0.4,0.5,2.4],[0.4,1.1,1.6],[0.4,1.7,3.0]].forEach(function(b){
        var y=b[1];
        o.push([[b[0],y,0.02],[b[0]+b[2],y,0.02],.7]);
        o.push([[b[0],y+0.28,0.02],[b[0]+b[2],y+0.28,0.02],.7]);
        o.push([[b[0],y,0.02],[b[0],y+0.28,0.02],.7]); o.push([[b[0]+b[2],y,0.02],[b[0]+b[2],y+0.28,0.02],.7]);
      });
      o.push([[3.6,2.9,0],[3.6,2.9,3.0],.95]);
      o.push([[3.6,2.9,3.0],[1.6,2.9,3.0],.95]); o.push([[3.6,2.9,3.0],[4.3,2.9,3.0],.7]);
      o.push([[3.6,2.9,2.5],[2.6,2.9,3.0],.5]);
      o.push([[2.0,2.9,3.0],[2.0,2.9,1.4],.6]); o.push([[1.88,2.9,1.4],[2.12,2.9,1.4],.9]);
      bx(o, 1.4,2.4, 1.2,1.0, 1.2, 0, .6);
      return o;
    },
    dijital_ikiz: function(){
      var o = [];
      bx(o, 0.5,1.2, 1.5,1.5, 2.0, 0, .9);
      bx(o, 3.0,1.2, 1.5,1.5, 2.0, 0, .4);
      [0.5,1.1,1.7].forEach(function(z){ o.push([[2.0,1.95,z],[3.0,1.95,z],.35]); });
      o.push([[2.5,1.95,0.35],[2.5,1.95,1.85],.2]);
      return o;
    },
    cam: function(){
      var o = [];
      bx(o, 0.6,0.9, 3.2,2.4, 0.35, 0, .55);
      bx(o, 1.5,1.5, 1.4,1.2, 0.7, 0.35, .85);
      o.push([[2.2,0.9,0.35],[2.2,0.9,2.3],.9]); o.push([[2.2,3.3,0.35],[2.2,3.3,2.3],.9]);
      o.push([[2.2,0.9,2.3],[2.2,3.3,2.3],.9]);
      o.push([[2.2,2.1,2.3],[2.2,2.1,1.05],.95]);
      o.push([[2.1,2.1,1.05],[2.3,2.1,1.05],.9]);
      var z=1.06;
      o.push([[1.6,1.6,z],[2.8,1.6,z],.4]); o.push([[2.8,1.6,z],[1.6,1.95,z],.4]);
      o.push([[1.6,1.95,z],[2.8,1.95,z],.4]); o.push([[2.8,1.95,z],[1.6,2.3,z],.4]);
      o.push([[1.6,2.3,z],[2.8,2.3,z],.4]);
      return o;
    },
    simulasyon: function(){
      var o = [], i, j, n=8;
      function zz(i,j){ return 0.55 + 0.5*Math.sin(i/n*Math.PI*1.6) * Math.sin(j/n*Math.PI*1.4); }
      for (i=0;i<=n;i++){
        for (j=0;j<n;j++){
          o.push([[0.4+i*0.45,0.4+j*0.45,zz(i,j)],[0.4+i*0.45,0.4+(j+1)*0.45,zz(i,j+1)],.55]);
        }
      }
      for (j=0;j<=n;j++){
        for (i=0;i<n;i++){
          o.push([[0.4+i*0.45,0.4+j*0.45,zz(i,j)],[0.4+(i+1)*0.45,0.4+j*0.45,zz(i+1,j)],.55]);
        }
      }
      return o;
    },
    tolerans_analizi: function(){
      var o = [];
      bx(o, 1.2,1.4, 2.0,1.4, 1.1, 0, .85);
      o.push([[1.2,1.4,1.5],[1.2,1.4,1.95],.5]); o.push([[3.2,1.4,1.5],[3.2,1.4,1.95],.5]);
      o.push([[1.2,1.4,1.85],[3.2,1.4,1.85],.85]);
      o.push([[1.2,1.4,1.85],[1.42,1.4,1.95],.85]); o.push([[1.2,1.4,1.85],[1.42,1.4,1.75],.85]);
      o.push([[3.2,1.4,1.85],[2.98,1.4,1.95],.85]); o.push([[3.2,1.4,1.85],[2.98,1.4,1.75],.85]);
      o.push([[3.55,1.4,0],[3.9,1.4,0],.5]); o.push([[3.55,2.8,0],[3.9,2.8,0],.5]);
      o.push([[3.8,1.4,0],[3.8,2.8,0],.85]);
      o.push([[3.8,1.4,0],[3.7,1.62,0],.85]); o.push([[3.8,1.4,0],[3.9,1.62,0],.85]);
      o.push([[3.8,2.8,0],[3.7,2.58,0],.85]); o.push([[3.8,2.8,0],[3.9,2.58,0],.85]);
      return o;
    },
    tasarim_otomasyonu: function(){
      var o = [];
      bx(o, 2.7,1.3, 1.5,1.3, 1.0, 0, .85);
      bx(o, 3.0,1.6, 0.9,0.7, 0.5, 1.0, .55);
      [[0.4,1.2,0.7],[0.4,1.9,0.35],[0.4,2.6,0.95]].forEach(function(s){
        var y=s[1];
        o.push([[s[0],y,0.02],[s[0]+1.6,y,0.02],.4]);
        var kx=s[0]+1.6*s[2];
        o.push([[kx,y,0],[kx,y,0.3],.95]);
        o.push([[kx-0.08,y,0.3],[kx+0.08,y,0.3],.95]);
      });
      o.push([[2.1,1.9,0.15],[2.7,1.9,0.5],.35]);
      return o;
    },
    fabrika_tasarimi: function(){
      var o = [], i;
      o.push([[0.2,0.3,0],[4.6,0.3,0],.3]); o.push([[4.6,0.3,0],[4.6,3.6,0],.3]);
      o.push([[4.6,3.6,0],[0.2,3.6,0],.3]); o.push([[0.2,3.6,0],[0.2,0.3,0],.3]);
      bx(o, 0.6,0.7, 0.9,0.7, 0.6, 0, .7);
      bx(o, 2.0,0.7, 0.9,0.7, 0.6, 0, .7);
      bx(o, 3.4,0.7, 0.9,0.7, 0.6, 0, .7);
      bx(o, 0.6,2.4, 0.9,0.7, 0.6, 0, .7);
      bx(o, 2.0,2.4, 0.9,0.7, 0.6, 0, .7);
      bx(o, 3.4,2.4, 1.0,0.9, 0.9, 0, .85);
      var path=[[1.05,1.55],[2.45,1.55],[2.45,2.2],[3.9,2.2]];
      for (i=0;i<path.length-1;i++) o.push([[path[i][0],path[i][1],0.05],[path[i+1][0],path[i+1][1],0.05],.6]);
      o.push([[3.9,2.2,0.05],[3.7,2.05,0.05],.6]); o.push([[3.9,2.2,0.05],[3.68,2.32,0.05],.6]);
      return o;
    },
    plm: function(){
      var o = [], i, n=28, cx=2.1, cy=2.1, r=1.6, z=0.5;
      for (i=0;i<n;i++){
        var a1=i/n*2*Math.PI, a2=(i+1)/n*2*Math.PI;
        o.push([[cx+r*Math.cos(a1),cy+r*Math.sin(a1),z],[cx+r*Math.cos(a2),cy+r*Math.sin(a2),z],.5]);
      }
      for (i=0;i<4;i++){
        var a=i/4*2*Math.PI + Math.PI/4;
        var px=cx+r*Math.cos(a), py=cy+r*Math.sin(a);
        bx(o, px-0.28, py-0.28, 0.56,0.56, 0.56, 0.22, .9);
      }
      bx(o, 1.72,1.72, 0.76,0.76, 0.76, 0.12, .6);
      return o;
    },
    pdm: function(){
      var o = [], i;
      ringZ(o, 1.6,2.1, 0.2, 1.0, 20, .8);
      ringZ(o, 1.6,2.1, 0.95, 1.0, 20, .6);
      ringZ(o, 1.6,2.1, 1.7, 1.0, 20, .8);
      for (i=0;i<8;i++){ var a=i/8*2*Math.PI; o.push([[1.6+Math.cos(a),2.1+Math.sin(a),0.2],[1.6+Math.cos(a),2.1+Math.sin(a),1.7],.3]); }
      o.push([[3.3,1.6,0.5],[4.3,1.6,0.5],.85]); o.push([[4.3,1.6,0.5],[4.3,1.6,1.9],.85]);
      o.push([[4.3,1.6,1.9],[3.3,1.6,1.9],.85]); o.push([[3.3,1.6,1.9],[3.3,1.6,0.5],.85]);
      [0.85,1.15,1.45].forEach(function(z){ o.push([[3.45,1.6,z],[4.15,1.6,z],.4]); });
      o.push([[2.6,1.9,1.0],[3.3,1.7,1.0],.4]);
      return o;
    },
    nesting: function(){
      var o = [];
      o.push([[0.5,0.5,0.05],[4.3,0.5,0.05],.8]); o.push([[4.3,0.5,0.05],[4.3,3.3,0.05],.8]);
      o.push([[4.3,3.3,0.05],[0.5,3.3,0.05],.8]); o.push([[0.5,3.3,0.05],[0.5,0.5,0.05],.8]);
      function rect(x,y,w,d){ o.push([[x,y,0.07],[x+w,y,0.07],.6]); o.push([[x+w,y,0.07],[x+w,y+d,0.07],.6]); o.push([[x+w,y+d,0.07],[x,y+d,0.07],.6]); o.push([[x,y+d,0.07],[x,y,0.07],.6]); }
      rect(0.7,0.7,1.3,1.0); rect(2.2,0.7,0.9,1.5); rect(3.3,0.7,0.8,0.8);
      rect(0.7,1.9,0.9,1.2); rect(1.8,2.4,1.5,0.7);
      o.push([[3.4,1.7,0.07],[4.1,1.7,0.07],.6]); o.push([[4.1,1.7,0.07],[3.4,2.5,0.07],.6]); o.push([[3.4,2.5,0.07],[3.4,1.7,0.07],.6]);
      o.push([[3.5,2.7,0.07],[4.15,3.15,0.07],.6]); o.push([[4.15,3.15,0.07],[3.5,3.15,0.07],.6]); o.push([[3.5,3.15,0.07],[3.5,2.7,0.07],.6]);
      return o;
    },
    eklemeli_imalat: function(){
      var o = [], i;
      var f=[[0.8,0.8],[3.4,0.8],[3.4,3.4],[0.8,3.4]];
      for (i=0;i<4;i++){ o.push([[f[i][0],f[i][1],0],[f[i][0],f[i][1],2.6],.7]); }
      for (i=0;i<4;i++){ var g=f[(i+1)%4]; o.push([[f[i][0],f[i][1],2.6],[g[0],g[1],2.6],.7]); o.push([[f[i][0],f[i][1],0],[g[0],g[1],0],.4]); }
      bx(o, 1.4,1.4, 1.4,1.4, 0.35, 0, .85);
      bx(o, 1.65,1.65, 0.9,0.9, 0.35, 0.35, .85);
      bx(o, 1.9,1.9, 0.4,0.4, 0.35, 0.7, .85);
      o.push([[0.8,2.1,2.2],[3.4,2.1,2.2],.6]);
      o.push([[2.1,2.1,2.2],[2.1,2.1,1.05],.9]);
      o.push([[2.0,2.1,1.05],[2.2,2.1,1.05],.9]);
      return o;
    },
    egitimler: function(){
      var o = [];
      bx(o, 1.3,1.4, 1.6,1.6, 0.16, 0.3, .5);
      bx(o, 1.42,1.52, 1.36,1.36, 0.16, 0.46, .6);
      bx(o, 1.5,1.6, 1.2,1.2, 0.16, 0.62, .65);
      var c2 = 2.1, d = 1.75, z0 = 0.92, z1 = 1.08;
      [z0,z1].forEach(function(z){
        o.push([[c2-d,c2,z],[c2,c2+d,z],.9]); o.push([[c2,c2+d,z],[c2+d,c2,z],.9]);
        o.push([[c2+d,c2,z],[c2,c2-d,z],.9]); o.push([[c2,c2-d,z],[c2-d,c2,z],.9]);
      });
      o.push([[c2-d,c2,z0],[c2-d,c2,z1],.7]); o.push([[c2+d,c2,z0],[c2+d,c2,z1],.7]);
      o.push([[c2,c2-d,z0],[c2,c2-d,z1],.7]); o.push([[c2,c2+d,z0],[c2,c2+d,z1],.7]);
      o.push([[c2,c2,z1],[c2+d*.92,c2,z1-0.02],.6]);
      o.push([[c2+d*.92,c2,z1-0.02],[c2+d*.92,c2,z1-0.82],.6]);
      o.push([[c2+d*.85,c2,z1-0.82],[c2+d*.99,c2,z1-0.82],.9]);
      return o;
    },
    sanatsal_baski: function(){
      var o = [];
      var x0=1.0, x1=3.6, w=x1-x0, y0=1.5, d=0.16, z0=1.1, h=2.0, z1=z0+h;
      bx(o, x0, y0, w, d, h, z0, .9);
      var fy = y0, mx0=x0+0.3, mx1=x1-0.3, mz0=z0+0.35, mz1=z1-0.3;
      o.push([[mx0,fy,mz0],[mx1,fy,mz0],.55]);
      o.push([[mx0+0.15,fy,mz0],[mx0+0.85,fy,mz0+0.85],.65]);
      o.push([[mx0+0.85,fy,mz0+0.85],[mx0+1.5,fy,mz0],.65]);
      wheelY(o, mx1-0.35, fy, mz1-0.3, 0.28, 14, .7);
      var midx=(x0+x1)/2;
      o.push([[midx-1.2, y0-0.05, 0],[midx-0.18, y0, z0+0.1],.5]);
      o.push([[midx+1.2, y0-0.05, 0],[midx+0.18, y0, z0+0.1],.5]);
      o.push([[midx, y0+1.3, 0],[midx, y0+0.15, z0+0.1],.4]);
      o.push([[midx-1.2, y0-0.05, z0*0.45],[midx+1.2, y0-0.05, z0*0.45],.35]);
      return o;
    }
  };

  /* Endüstriler paneli: sektör sayfalarındaki teknik illüstrasyonları gösterir */
  var sectorArt = document.getElementById('sectorArt');
  var sectorView = document.getElementById('sectorView');
  var list = document.getElementById('sectorList');
  var cap = document.getElementById('sectorCap');
  if (sectorArt && list){
    var links = list.querySelectorAll('a[data-obj]');
    var fadeT = null;
    /* görselleri önden ısıt — ilk hover'da beklenmesin */
    links.forEach(function(a){
      var im = new Image();
      im.src = 'assets/img/sektor/' + a.getAttribute('data-obj') + '.svg';
    });
    function apply(key){
      var acc = ACCENT[key] || '#00c8f0';
      if (sectorView){
        sectorView.style.setProperty('--acc', acc);
        sectorView.style.setProperty('--accGlow', hexRgba(acc, .16));
      }
      sectorArt.src = 'assets/img/sektor/' + key + '.svg';
    }
    function select(a){
      links.forEach(function(x){ x.classList.toggle('on', x === a); });
      if (cap) cap.textContent = a.querySelector('b').textContent.toLocaleUpperCase('tr-TR');
      var key = a.getAttribute('data-obj');
      if (reduce){ apply(key); return; }
      sectorArt.classList.add('swap');
      if (fadeT) clearTimeout(fadeT);
      fadeT = setTimeout(function(){
        apply(key);
        sectorArt.classList.remove('swap');
      }, 160);
    }
    links.forEach(function(a){
      a.addEventListener('mouseenter', function(){ select(a); });
      a.addEventListener('focus', function(){ select(a); });
    });
    apply('mimari');
  }

  var cozumSvg = document.getElementById('cozumSvg');
  var cozumCap = document.getElementById('cozumCap');
  if (cozumSvg){
    var cozumViewer = createViewer(cozumSvg, solutions);
    function solKey(a){
      var href = (a.getAttribute('href')||'').replace(/^.*\//,'').replace(/\.html$/,'').replace(/-/g,'_');
      return href || null;
    }
    function showSol(chip){
      var k = solKey(chip);
      if (!k || !solutions[k]) return;
      cozumViewer.show(k);
      if (cozumCap) cozumCap.textContent = chip.querySelector('b').textContent.toLocaleUpperCase('tr-TR');
    }
    document.querySelectorAll('.soltab-panel .solchip').forEach(function(c){
      c.addEventListener('mouseenter', function(){ showSol(c); });
      c.addEventListener('focus', function(){ showSol(c); });
    });
    document.querySelectorAll('.soltab-btn').forEach(function(b){
      b.addEventListener('click', function(){
        var p = document.querySelector('.soltab-panel[data-panel="'+b.getAttribute('data-tab')+'"]');
        var f = p && p.querySelector('.solchip');
        if (f) showSol(f);
      });
    });
    var first = document.querySelector('.soltab-panel.on .solchip');
    if (first) showSol(first);
  }
})();

/* ================= ÇÖZÜM SEKMELERİ ================= */
(function(){
  var btns = document.querySelectorAll('.soltab-btn');
  if (!btns.length) return;
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      var key = b.getAttribute('data-tab');
      btns.forEach(function(x){
        var on = x === b;
        x.classList.toggle('on', on);
        x.setAttribute('aria-selected', on ? 'true' : 'false');
      });
      document.querySelectorAll('.soltab-panel').forEach(function(p){
        p.classList.toggle('on', p.getAttribute('data-panel') === key);
      });
    });
  });
})();
