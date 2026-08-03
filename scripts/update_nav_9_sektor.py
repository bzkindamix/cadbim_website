# -*- coding: utf-8 -*-
"""Siteyi 7 sektorden 9 sektore tasir (tesisat + icmimarlik).

- Tum kok sayfalarda "Endustriler" nav dropdown'i 9 linke cikarilir
- 9 sektor sayfasinda sektor gecis seridi (secnav) yeniden kurulur
- mobilenav.js menu ve arama listeleri guncellenir
- cadbim_endustriler.html: kartlar, tab/panel ve 7->9 metinleri
- index.html: sektor listesi, soltab, istatistik, ACCENT ve 3B modeller
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# key, url, aksan, gorunen ad (&amp;'li), ikon
SECTORS9 = [
    ("mimari",     "sektor-mimari",     "#818cf8", "Mimarlık",                "ti-building"),
    ("icmimarlik", "sektor-icmimarlik", "#f472b6", "İç Mimarlık &amp; Tasarım", "ti-armchair"),
    ("insaat",     "sektor-insaat",     "#22c55e", "İnşaat &amp; Altyapı",     "ti-crane"),
    ("tesisat",    "sektor-tesisat",    "#2dd4bf", "Mekanik Tesisat",         "ti-air-conditioning"),
    ("makine",     "sektor-makine",     "#f59e0b", "Makine &amp; Üretim",      "ti-settings"),
    ("otomotiv",   "sektor-otomotiv",   "#ef4444", "Otomotiv",                "ti-car"),
    ("medya",      "sektor-medya",      "#c084fc", "Medya &amp; Eğlence",      "ti-movie"),
    ("egitim",     "sektor-egitim",     "#38bdf8", "Eğitim",                  "ti-school"),
    ("havacilik",  "sektor-havacilik",  "#a5b4fc", "Havacılık &amp; Savunma",  "ti-plane"),
]
FILES9 = {k: "sektor_%s.html" % k for k, _u, _a, _n, _i in SECTORS9}


def rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    return "rgba(%d,%d,%d,%s)" % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), alpha)


def plain(name):
    return name.replace("&amp;", "&")


# ------------------------------------------------------- A) nav dropdown
DROP_OLD = re.compile(
    r'        <a href="sektor-mimari">Mimarlık</a>\n'
    r'        <a href="sektor-insaat">İnşaat & Altyapı</a>\n'
    r'        <a href="sektor-makine">Makine & Üretim</a>\n'
    r'        <a href="sektor-otomotiv">Otomotiv</a>\n'
    r'        <a href="sektor-medya">Medya & Eğlence</a>\n'
    r'        <a href="sektor-egitim">Eğitim</a>\n'
    r'        <a href="sektor-havacilik">Havacılık & Savunma</a>')
DROP_NEW = "\n".join('        <a href="%s">%s</a>' % (u, plain(n))
                     for _k, u, _a, n, _i in SECTORS9)


def update_dropdowns():
    import glob
    n = 0
    for p in glob.glob(os.path.join(ROOT, "*.html")):
        s = io.open(p, encoding="utf-8").read()
        s2 = DROP_OLD.sub(DROP_NEW, s)
        if s2 != s:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
            n += 1
    return n


# ------------------------------------------------------- B) secnav
SECNAV_RE = re.compile(
    r'<nav class="secnav".*?</nav>\n<script>\n\(function\(\)\{var t=document\.getElementById\("secnavTrack"\).*?</script>\n',
    re.S)


def build_secnav(active_key):
    rows = []
    for key, url, accent, name, icon in SECTORS9:
        cls = "sec-card active" if key == active_key else "sec-card"
        bar = '<span class="sec-bar"></span>' if key == active_key else ""
        aria = ' aria-current="page"' if key == active_key else ""
        rows.append(
            '    <a href="%s" class="%s"%s style="--sc:%s;--scbg:%s;--art:url(assets/img/sektor/%s.svg);">'
            '<span class="sec-ico"><i class="ti %s"></i></span>'
            '<span class="sec-name">%s</span>%s</a>'
            % (url, cls, aria, accent, rgba(accent, ".13"), key, icon, name, bar))
    return ('<nav class="secnav" aria-label="Endüstriler">\n  <div class="secnav-inner">\n'
            '  <div class="secnav-track" id="secnavTrack">\n'
            + "\n".join(rows) + "\n  </div>\n  </div>\n</nav>\n"
            '<script>\n'
            '(function(){var t=document.getElementById("secnavTrack");if(!t)return;\n'
            '  var a=t.querySelector(".sec-card.active");\n'
            '  if(a&&t.scrollWidth>t.clientWidth){\n'
            '    t.scrollLeft=Math.max(0,a.offsetLeft-(t.clientWidth-a.offsetWidth)/2);}\n'
            '  function upd(){t.parentNode.classList.toggle("has-more",\n'
            '    t.scrollLeft+t.clientWidth<t.scrollWidth-2);}\n'
            '  t.addEventListener("scroll",upd,{passive:true});\n'
            '  window.addEventListener("resize",upd);upd();})();\n'
            '</script>\n')


def update_secnavs():
    done = []
    for key, fname in FILES9.items():
        p = os.path.join(ROOT, fname)
        s = io.open(p, encoding="utf-8").read()
        new_nav = build_secnav(key)
        if SECNAV_RE.search(s):
            s = SECNAV_RE.sub(lambda _m: new_nav, s, count=1)
        else:
            i = s.index("</nav>\n") + len("</nav>\n")
            s = s[:i] + "\n" + new_nav + s[i:]
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        done.append(fname)
    return done


# ------------------------------------------------------- C) mobilenav.js
def update_mobilenav():
    p = os.path.join(ROOT, "mobilenav.js")
    s = io.open(p, encoding="utf-8").read()
    menu_old = '''        ["Mimarlık", "/sektor-mimari"],
        ["İnşaat & Altyapı", "/sektor-insaat"],'''
    menu_new = '''        ["Mimarlık", "/sektor-mimari"],
        ["İç Mimarlık & Tasarım", "/sektor-icmimarlik"],
        ["İnşaat & Altyapı", "/sektor-insaat"],
        ["Mekanik Tesisat", "/sektor-tesisat"],'''
    assert menu_old in s, "mobilenav menu blogu bulunamadi"
    s = s.replace(menu_old, menu_new, 1)

    search_old = '''    ["Mimarlık", "/sektor-mimari", "sektor mimari", "Sektör"],
    ["İnşaat & Altyapı", "/sektor-insaat", "sektor insaat altyapi", "Sektör"],'''
    search_new = '''    ["Mimarlık", "/sektor-mimari", "sektor mimari", "Sektör"],
    ["İç Mimarlık & Tasarım", "/sektor-icmimarlik", "sektor ic mimarlik dekorasyon mobilya interior", "Sektör"],
    ["İnşaat & Altyapı", "/sektor-insaat", "sektor insaat altyapi", "Sektör"],
    ["Mekanik Tesisat", "/sektor-tesisat", "sektor mekanik tesisat mep hvac havalandirma kanal boru", "Sektör"],'''
    assert search_old in s, "mobilenav arama blogu bulunamadi"
    s = s.replace(search_old, search_new, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- D) endustriler hub
CARD_ICM = '''
    <a href="sektor-icmimarlik" class="sol-card" style="--sc:#f472b6;--art:url(assets/img/sektor/icmimarlik.svg);">
      <div class="sol-icon" style="background:rgba(244,114,182,0.12);color:#f472b6;"><i class="ti ti-armchair"></i></div>
      <h3>İç Mimarlık &amp; Tasarım</h3>
      <p>Konseptten fotogerçekçi sunuma — iç mekân modelleme, render ve baskı çözümleri.</p>
      <div class="sol-meta">
        <span class="sol-tag">SketchUp</span><span class="sol-tag">Chaos Corona</span><span class="sol-tag">Lumion</span>
      </div>
      <div class="sol-arrow">Sektöre Git <i class="ti ti-arrow-right"></i></div>
    </a>
'''
CARD_TES = '''
    <a href="sektor-tesisat" class="sol-card" style="--sc:#2dd4bf;--art:url(assets/img/sektor/tesisat.svg);">
      <div class="sol-icon" style="background:rgba(45,212,191,0.12);color:#2dd4bf;"><i class="ti ti-air-conditioning"></i></div>
      <h3>Mekanik Tesisat</h3>
      <p>Modelden imalata — HVAC, borulama ve elektrik tesisatında koordineli BIM akışı.</p>
      <div class="sol-meta">
        <span class="sol-tag">Revit MEP</span><span class="sol-tag">Fabrication</span><span class="sol-tag">Autodesk CFD</span>
      </div>
      <div class="sol-arrow">Sektöre Git <i class="ti ti-arrow-right"></i></div>
    </a>
'''
TAB_ICM = '    <button class="ind-tab-btn" data-ind="icmimarlik" style="--ic:#f472b6;"><i class="ti ti-armchair"></i>İç Mimarlık &amp; Tasarım</button>\n'
TAB_TES = '    <button class="ind-tab-btn" data-ind="tesisat" style="--ic:#2dd4bf;"><i class="ti ti-air-conditioning"></i>Mekanik Tesisat</button>\n'

PANEL_ICM = '''
  <div class="ind-panel" data-ind="icmimarlik">
    <a href="gorsellestirme" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(245,158,11,0.12);color:#f59e0b;"><i class="ti ti-sun-high"></i></div><h4>Görselleştirme &amp; Render</h4><div class="ind-sol-products"><span>Chaos Corona</span><span>V-Ray</span><span>Lumion</span><span>Enscape</span></div></a>
    <a href="yaratici-icerik" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(226,89,34,0.12);color:#e25922;"><i class="ti ti-palette"></i></div><h4>Yaratıcı İçerik &amp; Tasarım</h4><div class="ind-sol-products"><span>Photoshop</span><span>InDesign</span></div></a>
    <a href="sanatsal-baski" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(232,121,249,0.12);color:#e879f9;"><i class="ti ti-wand"></i></div><h4>Sanatsal Baskı Atölyesi</h4><div class="ind-sol-products"><span>HP DesignJet Z9+</span><span>12 renk pigment</span></div></a>
    <a href="gerceklik-yakalama" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(251,191,36,0.12);color:#fbbf24;"><i class="ti ti-scan"></i></div><h4>Gerçeklik Yakalama &amp; Tarama</h4><div class="ind-sol-products"><span>ReCap Pro</span><span>Scan Essentials</span></div></a>
  </div>
'''
PANEL_TES = '''
  <div class="ind-panel" data-ind="tesisat">
    <a href="bim" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(129,140,248,0.12);color:#818cf8;"><i class="ti ti-building"></i></div><h4>BIM</h4><div class="ind-sol-products"><span>Revit</span><span>Fabrication CADmep</span><span>Navisworks</span></div></a>
    <a href="simulasyon" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(251,191,36,0.12);color:#fbbf24;"><i class="ti ti-chart-dots-3"></i></div><h4>Simülasyon &amp; Analiz</h4><div class="ind-sol-products"><span>Autodesk CFD</span></div></a>
    <a href="insaat-yonetimi" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(34,197,94,0.12);color:#22c55e;"><i class="ti ti-crane"></i></div><h4>İnşaat Proje Yönetimi</h4><div class="ind-sol-products"><span>BIM Collaborate Pro</span><span>Autodesk Docs</span></div></a>
    <a href="dijital-ikiz" class="ind-sol-block"><div class="ind-sol-icon" style="background:rgba(56,189,248,0.12);color:#38bdf8;"><i class="ti ti-building-factory-2"></i></div><h4>Dijital İkiz</h4><div class="ind-sol-products"><span>Autodesk Tandem</span></div></a>
  </div>
'''


def update_hub():
    p = os.path.join(ROOT, "cadbim_endustriler.html")
    s = io.open(p, encoding="utf-8").read()
    # 7 -> 9 metinleri
    s = s.replace("Cadbim'in hizmet verdiği 7 endüstri: Mimarlık, İnşaat & Altyapı, Makine & "
                  "Üretim, Otomotiv, Medya & Eğlence, Eğitim, Havacılık & Savunma.",
                  "Cadbim'in hizmet verdiği 9 endüstri: Mimarlık, İç Mimarlık, İnşaat & Altyapı, "
                  "Mekanik Tesisat, Makine & Üretim, Otomotiv, Medya & Eğlence, Eğitim, "
                  "Havacılık & Savunma.")
    s = s.replace("<h1>7 Endüstride,", "<h1>9 Endüstride,")
    s = s.replace("mimarlıktan havacılığa uzanan 7 farklı endüstriye",
                  "mimarlıktan havacılığa uzanan 9 farklı endüstriye")
    # kartlar
    m = re.search(r'    <a href="sektor-mimari" class="sol-card"[^>]*>.*?</a>\n', s, re.S)
    assert m, "hub mimari karti bulunamadi"
    s = s[:m.end()] + CARD_ICM + s[m.end():]
    m = re.search(r'    <a href="sektor-insaat" class="sol-card"[^>]*>.*?</a>\n', s, re.S)
    assert m, "hub insaat karti bulunamadi"
    s = s[:m.end()] + CARD_TES + s[m.end():]
    # tab butonlari
    m = re.search(r'    <button class="ind-tab-btn active" data-ind="mimari".*?</button>\n', s)
    assert m, "hub mimari tab bulunamadi"
    s = s[:m.end()] + TAB_ICM + s[m.end():]
    m = re.search(r'    <button class="ind-tab-btn" data-ind="insaat".*?</button>\n', s)
    s = s[:m.end()] + TAB_TES + s[m.end():]
    # paneller
    m = re.search(r'  <div class="ind-panel active" data-ind="mimari">.*?\n  </div>\n', s, re.S)
    assert m, "hub mimari panel bulunamadi"
    s = s[:m.end()] + PANEL_ICM + s[m.end():]
    m = re.search(r'  <div class="ind-panel" data-ind="insaat">.*?\n  </div>\n', s, re.S)
    assert m, "hub insaat panel bulunamadi"
    s = s[:m.end()] + PANEL_TES + s[m.end():]
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- E) index.html
IDX_ROW_ICM = '      <a href="sektor-icmimarlik" data-obj="icmimarlik"><b>İç Mimarlık &amp; Tasarım</b><span>SketchUp, Corona, Lumion</span><i class="ti ti-arrow-right"></i></a>\n'
IDX_ROW_TES = '      <a href="sektor-tesisat" data-obj="tesisat"><b>Mekanik Tesisat</b><span>Revit MEP, Fabrication, CFD</span><i class="ti ti-arrow-right"></i></a>\n'

IDX_TAB_ICM = '      <button class="soltab-btn" role="tab" aria-selected="false" data-tab="icmimarlik">İç Mimarlık &amp; Tasarım</button>\n'
IDX_TAB_TES = '      <button class="soltab-btn" role="tab" aria-selected="false" data-tab="tesisat">Mekanik Tesisat</button>\n'

IDX_PANEL_ICM = '''    <div class="soltab-panel" data-panel="icmimarlik" role="tabpanel">
      <a class="solchip feat" href="gorsellestirme"><b>Görselleştirme &amp; Render</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="yaratici-icerik"><b>Yaratıcı İçerik &amp; Tasarım</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="sanatsal-baski"><b>Sanatsal Baskı</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="gerceklik-yakalama"><b>Gerçeklik Yakalama</b><i class="ti ti-arrow-right"></i></a>
    </div>
'''
IDX_PANEL_TES = '''    <div class="soltab-panel" data-panel="tesisat" role="tabpanel">
      <a class="solchip feat" href="bim"><b>BIM</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="simulasyon"><b>Simülasyon &amp; Analiz</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="insaat-yonetimi"><b>İnşaat Proje Yönetimi</b><i class="ti ti-arrow-right"></i></a>
      <a class="solchip" href="dijital-ikiz"><b>Dijital İkiz</b><i class="ti ti-arrow-right"></i></a>
    </div>
'''

IDX_MODELS = '''    icmimarlik: function(){
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
'''


def update_index():
    p = os.path.join(ROOT, "index.html")
    s = io.open(p, encoding="utf-8").read()
    # sektor listesi
    m = re.search(r'      <a href="sektor-mimari" data-obj="mimari"[^\n]*\n', s)
    assert m, "index mimari satiri bulunamadi"
    s = s[:m.end()] + IDX_ROW_ICM + s[m.end():]
    m = re.search(r'      <a href="sektor-insaat" data-obj="insaat"[^\n]*\n', s)
    s = s[:m.end()] + IDX_ROW_TES + s[m.end():]
    # soltab butonlari + paneller
    m = re.search(r'      <button class="soltab-btn on"[^\n]*data-tab="mimari"[^\n]*\n', s)
    assert m, "index soltab mimari bulunamadi"
    s = s[:m.end()] + IDX_TAB_ICM + s[m.end():]
    m = re.search(r'      <button class="soltab-btn"[^\n]*data-tab="insaat"[^\n]*\n', s)
    s = s[:m.end()] + IDX_TAB_TES + s[m.end():]
    m = re.search(r'    <div class="soltab-panel on" data-panel="mimari"[^>]*>.*?\n    </div>\n', s, re.S)
    assert m, "index mimari panel bulunamadi"
    s = s[:m.end()] + IDX_PANEL_ICM + s[m.end():]
    m = re.search(r'    <div class="soltab-panel" data-panel="insaat"[^>]*>.*?\n    </div>\n', s, re.S)
    s = s[:m.end()] + IDX_PANEL_TES + s[m.end():]
    # istatistik
    s = s.replace('<span data-n="7">0</span></div><div class="stat-lbl">Sektör uzmanlığı</div>',
                  '<span data-n="9">0</span></div><div class="stat-lbl">Sektör uzmanlığı</div>')
    # ACCENT haritasi
    s = s.replace("mimari:'#818cf8', insaat:'#22c55e',",
                  "mimari:'#818cf8', icmimarlik:'#f472b6', tesisat:'#2dd4bf', insaat:'#22c55e',")
    # 3B modeller
    anchor = "  var objects = {\n"
    assert anchor in s, "index objects haritasi bulunamadi"
    s = s.replace(anchor, anchor + IDX_MODELS, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


if __name__ == "__main__":
    n = update_dropdowns()
    print("nav dropdown guncellenen sayfa:", n)
    print("secnav yeniden kurulan:", len(update_secnavs()))
    update_mobilenav(); print("mobilenav.js: OK")
    update_hub(); print("endustriler hub: OK")
    update_index(); print("index: OK")
