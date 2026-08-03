# -*- coding: utf-8 -*-
"""Endustri <-> cozum eslesmesini tek dogru kaynaga baglar.

Tek dogru kaynak: cadbim_endustriler.html icindeki "Detayli Inceleme —
Endustriye Gore Cozum & Urun Haritasi" bolumu (.ind-tab-btn sekmeleri ve
.ind-panel panelleri).

Bu betik o haritayi okuyup cadbim_cozumler.html'deki endustri filtresini
(sekmeler, sayaclar ve kartlardaki data-ind degerleri) yeniden uretir.
Boylece iki sayfa birbiriyle celisemez.

Ayrica cozum kartlarinin altindaki endustri listesi kaldirilip "Detayli
Incele" baglantisina cevrilir: ayni bilgi hem filtrede hem her kartin
altinda tekrarlaniyordu (Onur'un 2026-08-03 tarihli mukerrerlik notu).
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'cadbim_endustriler.html')
DST = os.path.join(ROOT, 'cadbim_cozumler.html')

TAB_RE = re.compile(
    r'<button class="ind-tab-btn[^"]*" data-ind="(?P<key>\w+)" '
    r'style="--ic:(?P<color>#[0-9a-f]{6});"><i class="ti (?P<icon>[a-z0-9-]+)">'
    r'</i>(?P<label>[^<]+)</button>')
PANEL_RE = re.compile(r'<div class="ind-panel[^"]*" data-ind="(\w+)">(.*?)\n  </div>', re.S)
BLOCK_RE = re.compile(r'<a href="([a-z0-9\-]+)" class="ind-sol-block"')

# Umbrella cozum: haritada ayri satiri yok, tum endustrilerde gecerli
UMBRELLA = 'dijital-donusum'


def read_map():
    s = io.open(SRC, encoding='utf-8').read()
    tabs = [m.groupdict() for m in TAB_RE.finditer(s)]
    per_ind = {}
    for ind, body in PANEL_RE.findall(s):
        per_ind[ind] = BLOCK_RE.findall(body)
    return tabs, per_ind


def invert(tabs, per_ind):
    inv = {}
    for t in tabs:
        for sol in per_ind.get(t['key'], []):
            inv.setdefault(sol, []).append(t['key'])
    inv[UMBRELLA] = [t['key'] for t in tabs]
    return inv


def build_filter(tabs, inv, slugs):
    total = len(slugs)
    btn = ('<button type="button" class="cz-fbtn is-on" data-f="all" aria-pressed="true">'
           '<i class="ti ti-layout-grid"></i>Tüm Çözümler<span>%d</span></button>' % total)
    for t in tabs:
        n = sum(1 for s in slugs if t['key'] in inv.get(s, []))
        if not n:
            continue
        btn += ('<button type="button" class="cz-fbtn" data-f="%s" style="--ic:%s;" '
                'aria-pressed="false"><i class="ti %s"></i>%s<span>%d</span></button>'
                % (t['key'], t['color'], t['icon'], t['label'], n))
    return u'''<!-- cz-filter -->
<div class="cz-filter">
  <div class="cz-filter-lbl">Endüstriye göre filtreleyin</div>
  <div class="cz-fbtns" role="group" aria-label="Endüstri filtresi">%s</div>
  <p class="cz-filter-out" role="status" aria-live="polite"></p>
</div>
<!-- /cz-filter -->
''' % btn


def build_js(tabs):
    names = ",".join("%s:'%s'" % (t['key'], t['label'].replace('&amp;', '&').replace("'", "\\'"))
                     for t in tabs)
    return u'''<!-- cz-filter-js -->
<script>
(function(){
  var bar=document.querySelector('.cz-filter'); if(!bar) return;
  var grid=document.getElementById('solGrid'); if(!grid) return;
  var cards=[].slice.call(grid.querySelectorAll('.sol-card'));
  var btns=[].slice.call(bar.querySelectorAll('.cz-fbtn'));
  var out=bar.querySelector('.cz-filter-out');
  var names={%s};
  function apply(f,push){
    var n=0;
    cards.forEach(function(c){
      var ok = f==='all' || (' '+(c.getAttribute('data-ind')||'')+' ').indexOf(' '+f+' ')>-1;
      c.hidden=!ok; if(ok) n++;
    });
    btns.forEach(function(b){
      var on=b.getAttribute('data-f')===f;
      b.classList.toggle('is-on',on); b.setAttribute('aria-pressed',on?'true':'false');
    });
    out.innerHTML = f==='all' ? '' :
      n+' çözüm · '+names[f]+' &nbsp;·&nbsp; <a href="endustriler#'+f+'">bu endüstrinin ürün haritası</a>';
    if(push){ try{ history.replaceState(null,'',f==='all'?location.pathname:location.pathname+'#'+f); }catch(e){} }
  }
  bar.addEventListener('click',function(e){
    var b=e.target.closest('.cz-fbtn'); if(!b) return;
    apply(b.getAttribute('data-f'),true);
  });
  var h=(location.hash||'').replace('#','');
  apply(names[h]?h:'all',false);
})();
</script>
<!-- /cz-filter-js -->
''' % names


def cut(s, open_m, close_m):
    if open_m in s:
        i = s.index(open_m)
        j = s.index(close_m) + len(close_m)
        while j < len(s) and s[j] == '\n':
            j += 1
        s = s[:i] + s[j:]
    return s


def main():
    tabs, per_ind = read_map()
    inv = invert(tabs, per_ind)

    s = io.open(DST, encoding='utf-8').read()
    slugs = re.findall(r'<a href="([a-z0-9\-]+)" class="sol-card"', s)

    missing = [x for x in slugs if x not in inv]
    if missing:
        print('UYARI: haritada yer almayan cozum ->', missing)

    # 1) kartlara data-ind + alt satiri "Detayli Incele"ye cevir
    def fix_card(m):
        slug = m.group('slug')
        head = re.sub(r'\s*data-ind="[^"]*"', '', m.group('head'))
        head = head[:-1] + ' data-ind="%s">' % " ".join(inv.get(slug, []))
        arrow = ('<div class="sol-arrow">Detaylı İncele '
                 '<i class="ti ti-arrow-right"></i></div>')
        return head + m.group('body') + arrow + '</a>'

    s, n = re.subn(
        r'(?P<head><a href="(?P<slug>[a-z0-9\-]+)" class="sol-card"[^>]*>)'
        r'(?P<body>.*?)<div class="sol-arrow">.*?</div>\s*</a>',
        fix_card, s, flags=re.S)
    print('guncellenen kart:', n)

    # 2) filtre seridi
    s = cut(s, '<!-- cz-filter -->', '<!-- /cz-filter -->')
    anchor = '<section class="section">\n  <div class="grid"'
    i = s.index(anchor)
    j = s.index('>', i + len(anchor)) + 1
    s = (s[:i] + '<section class="section">\n' + build_filter(tabs, inv, slugs)
         + '  <div class="grid" id="solGrid">' + s[j:])

    # 3) betik
    s = cut(s, '<!-- cz-filter-js -->', '<!-- /cz-filter-js -->')
    s = s.replace('</body>', build_js(tabs) + '</body>', 1)

    io.open(DST, 'w', encoding='utf-8', newline='').write(s)
    print('filtre %d endustri sekmesiyle yeniden uretildi' % len(tabs))
    for t in tabs:
        print('   %-11s %d cozum' % (t['key'],
                                     sum(1 for x in slugs if t['key'] in inv.get(x, []))))


if __name__ == '__main__':
    main()
