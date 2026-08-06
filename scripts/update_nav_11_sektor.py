# -*- coding: utf-8 -*-
"""Siteyi 9 sektorden 11 sektore tasir (yapi_urunleri + tuketici).

- Kok VE post/ altindaki tum sayfalarda "Endustriler" nav dropdown'i ve footer
  "Endustriler" kolonu 11 linke cikarilir (post/ sayfalari "../" onekli href
  kullanir; her dosyada mevcut onek otomatik tespit edilip korunur)
- mobilenav.js menu ve arama listeleri guncellenir
- cadbim_endustriler.html: kartlar, tab/panel ve 9->11 metinleri
- index.html: sektor secici listesi ve istatistik sayaci
- sitemap.xml: 2 yeni <url> girdisi
"""
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEW = [
    ("yapiurunleri", "sektor-yapi-urunleri", "#f97316", "Yapı Ürünleri &amp; Fabrikasyon",
     "ti-building-warehouse"),
    ("tuketici", "sektor-tuketici-urunleri", "#3b82f6", "Tüketici Ürünleri", "ti-package"),
]


def plain(name):
    return name.replace("&amp;", "&")


# ------------------------------------------------------- A) nav dropdown + footer (sitewide)
ANCHOR_RE = re.compile(r'(<a href="((?:\.\./)?)sektor-havacilik">Savunma ve Havacılık</a>\n)')


def new_lines(prefix, indent):
    return "".join('%s<a href="%s%s">%s</a>\n' % (indent, prefix, u, plain(n))
                   for _k, u, _a, n, _i in NEW)


def update_dropdowns_and_footers():
    n = 0
    files = glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "post", "*.html"))
    for p in files:
        s = io.open(p, encoding="utf-8").read()

        def repl(m):
            full, prefix = m.group(0), m.group(2)
            # oncesindeki satirin girinti bosluklarini yakala
            line_start = s.rfind("\n", 0, m.start()) + 1
            indent = s[line_start:m.start()]
            indent = indent if indent.strip() == "" else "        "
            return full + new_lines(prefix, indent)

        s2 = ANCHOR_RE.sub(repl, s)
        if s2 != s:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
            n += 1
    return n


# ------------------------------------------------------- B) mobilenav.js
def update_mobilenav():
    p = os.path.join(ROOT, "mobilenav.js")
    s = io.open(p, encoding="utf-8").read()
    menu_old = '        ["Savunma ve Havacılık", "/sektor-havacilik"]\n      ]'
    menu_new = ('        ["Savunma ve Havacılık", "/sektor-havacilik"],\n'
                + "".join('        ["%s", "/%s"],\n' % (plain(n), u) for _k, u, _a, n, _i in NEW)
                ).rstrip(",\n") + "\n      ]"
    assert menu_old in s, "mobilenav menu blogu bulunamadi"
    s = s.replace(menu_old, menu_new, 1)

    search_old = ('["Savunma ve Havacılık", "/sektor-havacilik", "sektor havacilik savunma '
                  'defense aerospace", "Sektör"],')
    search_new = (search_old + "\n    "
                  + '["Yapı Ürünleri &amp; Fabrikasyon", "/sektor-yapi-urunleri", "sektor yapi '
                    'urunleri fabrikasyon building products cephe celik prefabrik nesting", '
                    '"Sektör"],\n    '
                  + '["Tüketici Ürünleri", "/sektor-tuketici-urunleri", "sektor tuketici '
                    'urunleri consumer products endustriyel tasarim", "Sektör"],')
    assert search_old in s, "mobilenav arama blogu bulunamadi"
    s = s.replace(search_old, search_new, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- C) index.html
def update_index():
    p = os.path.join(ROOT, "index.html")
    s = io.open(p, encoding="utf-8").read()
    m = re.search(
        r'      <a href="sektor-havacilik" data-obj="havacilik"[^\n]*\n', s)
    assert m, "index havacilik satiri bulunamadi"
    row = ('      <a href="%s" data-obj="%s" style="--sc:%s;--art:url(assets/img/sektor/%s.svg)">'
           '<span class="sec-ic" aria-hidden="true"><i class="ti %s"></i></span>'
           '<b>%s</b><span>%s</span><i class="ti ti-arrow-right"></i></a>\n')
    rows = (row % ("sektor-yapi-urunleri", "yapiurunleri", "#f97316", "yapiurunleri",
                   "ti-building-warehouse", "Yapı Ürünleri &amp; Fabrikasyon",
                   "Advance Steel, Nesting, CAM")
            + row % ("sektor-tuketici-urunleri", "tuketici", "#3b82f6", "tuketici",
                     "ti-package", "Tüketici Ürünleri", "Fusion, Alias, UltiMaker"))
    s = s[:m.end()] + rows + s[m.end():]
    s = s.replace('<span data-n="9">0</span></div><div class="stat-lbl">Sektör uzmanlığı</div>',
                  '<span data-n="11">0</span></div><div class="stat-lbl">Sektör uzmanlığı</div>')
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- D) endustriler hub
CARD_TPL = '''
    <a href="%s" class="sol-card" style="--sc:%s;--art:url(assets/img/sektor/%s.svg);">
      <div class="sol-icon" style="background:rgba(%s,0.12);color:%s;"><i class="ti %s"></i></div>
      <h3 aria-level="2">%s</h3>
      <p>%s</p>
      <div class="sol-meta">
        <span class="sol-tag">%s</span><span class="sol-tag">%s</span><span class="sol-tag">%s</span>
      </div>
      <div class="sol-arrow">Sektöre Git <i class="ti ti-arrow-right"></i></div>
    </a>
'''
TAB_TPL = '    <button class="ind-tab-btn" data-ind="%s" style="--ic:%s;"><i class="ti %s"></i>%s</button>\n'

BLOCK_TPL = ('<a href="%s" class="ind-sol-block"><div class="ind-sol-icon" '
             'style="background:rgba(%s,0.12);color:%s;"><i class="ti %s"></i></div>'
             '<h4 aria-level="3">%s</h4><div class="ind-sol-products">%s</div></a>')


def rgbstr(hex_color):
    h = hex_color.lstrip("#")
    return "%d,%d,%d" % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def update_hub():
    p = os.path.join(ROOT, "cadbim_endustriler.html")
    s = io.open(p, encoding="utf-8").read()
    s = s.replace(
        "Cadbim'in hizmet verdiği 9 endüstri: Mimarlık, İç Mimarlık, İnşaat & Altyapı, "
        "Mekanik Tesisat, Makine & Üretim, Otomotiv, Medya & Eğlence, Eğitim, "
        "Savunma ve Havacılık.",
        "Cadbim'in hizmet verdiği 11 endüstri: Mimarlık, İç Mimarlık, İnşaat & Altyapı, "
        "Mekanik Tesisat, Makine & Üretim, Otomotiv, Medya & Eğlence, Eğitim, Savunma ve "
        "Havacılık, Yapı Ürünleri & Fabrikasyon, Tüketici Ürünleri.")
    s = s.replace("<h1>9 Endüstride,", "<h1>11 Endüstride,")

    card_yapi = CARD_TPL % ("sektor-yapi-urunleri", "#f97316", "yapiurunleri", "249,115,22",
                            "#f97316", "ti-building-warehouse", "Yapı Ürünleri &amp; Fabrikasyon",
                            "Cephe, çelik konstrüksiyon ve prefabrik eleman üreticileri için "
                            "tasarımdan imalata tek veri seti.",
                            "Advance Steel", "Inventor", "Nesting")
    card_tuketici = CARD_TPL % ("sektor-tuketici-urunleri", "#3b82f6", "tuketici", "59,130,246",
                                "#3b82f6", "ti-package", "Tüketici Ürünleri",
                                "Endüstriyel tasarımdan seri üretime — mobilya, beyaz eşya, "
                                "ambalaj ve elektronik muhafazalar için tek platform.",
                                "Fusion", "Alias", "UltiMaker")
    m = re.search(r'    <a href="sektor-havacilik" class="sol-card"[^>]*>.*?</a>\n', s, re.S)
    assert m, "hub havacilik karti bulunamadi"
    s = s[:m.end()] + card_yapi + card_tuketici + s[m.end():]

    tab_yapi = TAB_TPL % ("yapiurunleri", "#f97316", "ti-building-warehouse",
                          "Yapı Ürünleri &amp; Fabrikasyon")
    tab_tuketici = TAB_TPL % ("tuketici", "#3b82f6", "ti-package", "Tüketici Ürünleri")
    m = re.search(r'    <button class="ind-tab-btn" data-ind="havacilik".*?</button>\n', s)
    assert m, "hub havacilik tab bulunamadi"
    s = s[:m.end()] + tab_yapi + tab_tuketici + s[m.end():]

    panel_yapi = (
        '\n  <div class="ind-panel" data-ind="yapiurunleri">\n    '
        + BLOCK_TPL % ("pdm", "129,140,248", "#818cf8", "ti-folders", "PDM",
                       "<span>Vault PDM</span><span>Fusion Manage</span>") + "\n    "
        + BLOCK_TPL % ("plm", "56,189,248", "#38bdf8", "ti-hierarchy-3", "PLM",
                       "<span>Fusion Manage</span><span>Vault PLM</span>") + "\n    "
        + BLOCK_TPL % ("nesting", "52,211,153", "#34d399", "ti-layout-grid", "Nesting — Yuvalama",
                       "<span>Inventor Nesting</span>") + "\n    "
        + BLOCK_TPL % ("cam", "248,113,113", "#f87171", "ti-settings-2", "CAM &amp; İmalat",
                       "<span>Fusion CAM</span><span>Inventor CAM</span>") + "\n    "
        + BLOCK_TPL % ("fabrika-tasarimi", "14,165,233", "#38bdf8", "ti-building-factory-2",
                       "Fabrika Tasarımı &amp; Dijital İkiz",
                       "<span>Factory Design Utilities</span><span>Autodesk Tandem</span>")
        + "\n    "
        + BLOCK_TPL % ("tasarim-otomasyonu", "251,191,36", "#fbbf24", "ti-robot",
                       "Tasarım Otomasyonu",
                       "<span>Fusion Extensions</span><span>Inventor iLogic</span>")
        + "\n    "
        + BLOCK_TPL % ("bim", "129,140,248", "#818cf8", "ti-building", "BIM",
                       "<span>Revit</span><span>Advance Steel</span>")
        + "\n  </div>\n"
    )
    panel_tuketici = (
        '\n  <div class="ind-panel" data-ind="tuketici">\n    '
        + BLOCK_TPL % ("plm", "56,189,248", "#38bdf8", "ti-hierarchy-3", "PLM",
                       "<span>Fusion Manage</span><span>Vault PLM</span>") + "\n    "
        + BLOCK_TPL % ("pdm", "52,211,153", "#34d399", "ti-folders", "PDM",
                       "<span>Vault Basic/Pro</span><span>Fusion Manage</span>") + "\n    "
        + BLOCK_TPL % ("simulasyon", "251,191,36", "#fbbf24", "ti-chart-dots-3",
                       "Simülasyon &amp; Analiz",
                       "<span>Fusion Simulation</span><span>Moldflow</span>") + "\n    "
        + BLOCK_TPL % ("eklemeli-imalat", "16,185,129", "#10b981", "ti-cube-3d-sphere",
                       "Eklemeli İmalat &amp; 3D Baskı",
                       "<span>UltiMaker</span><span>Cura</span>") + "\n    "
        + BLOCK_TPL % ("cam", "248,113,113", "#f87171", "ti-settings-2", "CAM &amp; İmalat",
                       "<span>Fusion CAM</span>") + "\n    "
        + BLOCK_TPL % ("gorsellestirme", "245,158,11", "#f59e0b", "ti-sun-high",
                       "Görselleştirme &amp; Render",
                       "<span>V-Ray</span><span>Chaos Corona</span>")
        + "\n  </div>\n"
    )
    m = re.search(r'  <div class="ind-panel" data-ind="havacilik">.*?\n  </div>\n', s, re.S)
    assert m, "hub havacilik panel bulunamadi"
    s = s[:m.end()] + panel_yapi + panel_tuketici + s[m.end():]

    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


# ------------------------------------------------------- E) sitemap.xml
def update_sitemap():
    p = os.path.join(ROOT, "sitemap.xml")
    s = io.open(p, encoding="utf-8").read()
    m = re.search(r'  <url><loc>https://www\.cadbim\.com\.tr/sektor-havacilik</loc>.*?</url>\n',
                  s)
    if not m:
        print("sitemap: sektor-havacilik girdisi bulunamadi, atlandi")
        return
    block = m.group(0)
    new_blocks = "".join(
        re.sub(r'sektor-havacilik', u, block) for _k, u, _a, _n, _i in NEW)
    s = s[:m.end()] + new_blocks + s[m.end():]
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


if __name__ == "__main__":
    print("nav+footer guncellenen sayfa:", update_dropdowns_and_footers())
    update_mobilenav(); print("mobilenav.js: OK")
    update_index(); print("index.html: OK")
    update_hub(); print("cadbim_endustriler.html: OK")
    update_sitemap()
