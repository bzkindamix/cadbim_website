# -*- coding: utf-8 -*-
"""Yeni sektor sayfalari uretir: sektor_tesisat.html, sektor_icmimarlik.html.

sektor_mimari.html iskelet olarak kullanilir (head/CSS/nav/Calisma Modelimiz/
footer aynen alinir, aksan rengi degistirilir); sektore ozel butun bolumler
bu betikteki icerik sozluklerinden kurulur. Basari Oykuleri bolumu, gercek
musteri referansi olmadigi icin yeni sayfalara konmaz.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "sektor_mimari.html")

# mimari sayfasindaki aksan bicimleri
OLD_HEX = "818cf8"
OLD_RGB = "129,140,248"
OLD_RGB2 = "99,102,241"    # hero-bg / badge arka plani (indigo-600)


def rgb(hex6):
    return "%d,%d,%d" % (int(hex6[0:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16))


# ---------------------------------------------------------------- ikon kutulari
def ico_img(kind, size=40, pad=6):
    """pcard/brand-row logo kutusu HTML'i."""
    if kind == "autodesk":
        inner = ('<img width="997" height="563" src="assets/logos/autodesk-white.svg?v=2" '
                 'alt="Autodesk" style="max-width:100%;max-height:100%;object-fit:contain;" '
                 'loading="lazy" decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "sketchup":
        inner = ('<img width="1158" height="354" src="assets/logos/sketchup.svg" alt="SketchUp" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;'
                 'filter:brightness(0) invert(1);opacity:.92;" loading="lazy" decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "chaos":
        inner = ('<img width="1280" height="1280" src="assets/logos/chaos.webp" alt="Chaos" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" '
                 'decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "hp":
        inner = ('<img width="300" height="300" src="assets/logos/hp-blue.png" alt="HP" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" '
                 'decoding="async">')
        box = "background:#fff;"
    elif kind == "adobe":
        inner = ('<img width="65" height="35" src="assets/logos/adobe-logo.svg" alt="Adobe" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;'
                 'filter:brightness(0) invert(1);opacity:.92;" loading="lazy" decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "lumion":
        inner = ('<img width="800" height="153" src="assets/logos/lumion.png" alt="Lumion" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" '
                 'decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    else:
        raise ValueError(kind)
    return ('<div style="width:%dpx;height:%dpx;border-radius:8px;%sdisplay:flex;'
            'align-items:center;justify-content:center;flex-shrink:0;padding:%dpx;">%s</div>'
            % (size, size, box, pad, inner))


def emb_img(name):
    return ('<img width="64" height="64" src="assets/img/%s" alt="" '
            'style="width:40px;height:40px;border-radius:8px;flex-shrink:0;" '
            'loading="lazy" decoding="async">' % name)


def pcard(href, brand, title, desc, cat, icon_html):
    return ('      <a href="%s" class="pcard" data-cat="%s">%s'
            '<div><div class="pbrand">%s</div><h3>%s</h3><p>%s</p></div>'
            '<i class="ti ti-arrow-right parr"></i></a>' % (href, cat, icon_html, brand, title, desc))


def brand_row(kind, title, sub, size=28, pad=4):
    return ('<div class="brand-row">\n          %s\n          '
            '<div><div class="brand-name">%s</div>'
            '<div style="font-size:11px;color:var(--w30);">%s</div></div>\n        </div>'
            % (ico_img(kind, size, pad), title, sub))


def workflow_step(acc, num, icon, title, desc, last=False):
    arrow = ("" if last else
             '\n    <div style="position:absolute;right:-11px;top:50%%;transform:translateY(-50%%);'
             'width:20px;height:20px;border-radius:50%%;background:#0a1225;border:.5px solid '
             '#%s44;display:flex;align-items:center;justify-content:center;z-index:2;">'
             '<i class="ti ti-chevron-right" style="font-size:11px;color:#%s;"></i></div>' % (acc, acc))
    return ('  <div style="flex:1;min-width:190px;background:linear-gradient(160deg,#%s0f,'
            'transparent 55%%),#0d1830;border:.5px solid #%s33;border-radius:14px;'
            'padding:20px 18px;position:relative;">\n'
            '    <div style="position:absolute;top:14px;right:16px;font-family:\'Manrope\','
            'sans-serif;font-size:26px;font-weight:800;color:#%s22;">%s</div>\n'
            '    <i class="ti ti-%s" style="font-size:22px;color:#%s;display:block;'
            'margin-bottom:12px;"></i>\n'
            '    <h3 style="font-family:\'Manrope\',sans-serif;font-size:14px;font-weight:700;'
            'color:#fff;margin:0 0 6px;">%s</h3>\n'
            '    <p style="font-size:12px;color:rgba(255,255,255,.5);line-height:1.6;margin:0;">'
            '%s</p>%s\n  </div>'
            % (acc, acc, acc, num, icon, acc, title, desc, arrow))


def sol_card(href, icon, title, desc):
    return ('    <div class="card">\n'
            '      <div class="card-icon" style="background:rgba(0,200,240,.12);">'
            '<i class="ti ti-%s"></i></div>\n'
            '      <h3><a href="%s" style="color:inherit;text-decoration:none;">%s</a></h3>\n'
            '      <p>%s</p>\n    </div>' % (icon, href, title, desc))


def sol_pill(href, text):
    return ('    <a href="%s" class="sol-pill"><i class="ti ti-arrow-right"></i>%s</a>'
            % (href, text))


# ================================================================== ICERIK
SECTORS = {
    "tesisat": {
        "file": "sektor_tesisat.html",
        "slug": "sektor-tesisat",
        "acc": "2dd4bf",
        "name": "Mekanik Tesisat",
        "crumb": "Mekanik Tesisat",
        "badge": "MEP Engineering",
        "badge_icon": "air-conditioning",
        "title": "Mekanik Tesisat (MEP) Çözümleri — Cadbim",
        "desc": ("Cadbim Mekanik Tesisat (MEP) çözümleri — Revit MEP, Fabrication "
                 "CADmep/CAMduct, Autodesk CFD ve HP donanımıyla modelden imalata "
                 "uçtan uca tesisat teknolojisi."),
        "h1a": "Mekanik Tesisat için",
        "h1b": "Tam Çözüm Portföyü",
        "hero_p": ("Isıtma, soğutma, havalandırma ve sıhhi tesisat — modelden imalata, "
                   "hesaptan sahaya uçtan uca dijital akış."),
        "art_alt": "Mekanik tesisat iş akışı — klima santrali, kanal hattı ve borulama şeması",
        "svc_name": "Mekanik Tesisat (MEP) Çözümleri",
        "wf_title": "Modelden İmalata Koordineli Tesisat Süreci",
        "workflow": [
            ("pencil", "Tasarım & Modelleme",
             "Revit MEP ile mimari modelle koordineli kanal, boru ve elektrik tesisatı."),
            ("wind", "Hesap & Analiz",
             "Autodesk CFD ile akış, basınç ve ısıl konfor doğrulaması."),
            ("settings", "İmalat Detayı",
             "Fabrication CADmep ve CAMduct ile spool çizimleri ve sac kanal imalatı."),
            ("building", "Koordinasyon",
             "Navisworks ile disiplinler arası çakışma kontrolü (clash detection)."),
            ("helmet", "Saha & Devreye Alma",
             "BIM Collaborate Pro ile montaj paftaları, as-built ve teslim."),
        ],
        "sol_cards": [
            ("bim", "building", "BIM — Yapı Bilgi Modellemesi",
             "Mekanik, elektrik ve sıhhi tesisatı mimari ve strüktürle aynı koordineli modelde birleştirir."),
            ("simulasyon", "chart-dots-3", "Simülasyon & Analiz",
             "Autodesk CFD ile hava dağılımı, basınç kaybı ve ısıl konfor analizleri."),
            ("insaat-yonetimi", "crane", "İnşaat Proje Yönetimi",
             "Tesisat montajının saha planlaması ve pafta dağıtımı için bulut tabanlı süreç."),
        ],
        "sol_pills": [("dijital-ikiz", "Dijital İkiz"),
                      ("gerceklik-yakalama", "Gerçeklik Yakalama & Tarama")],
        "brands": [
            ("autodesk", "Autodesk", "Revit, Fabrication CADmep/CAMduct, Autodesk CFD, Navisworks"),
            ("hp", "HP", "HP Designjet T, HP Z Workstation, HP ZBook"),
        ],
        "chips": [("c0", "Tasarım"), ("c1", "İmalat & Detay"), ("c2", "Analiz"),
                  ("c3", "Koordinasyon & Saha"), ("c4", "Donanım")],
        "products": [
            ("revit", "Autodesk", "Revit", "Mekanik, elektrik ve sıhhi tesisat için BIM modelleme",
             "c0", emb_img("emb-7a5b9dd8eb.png")),
            ("autocad", "Autodesk", "AutoCAD", "2D tesisat şemaları ve detay çizimleri",
             "c0", emb_img("emb-d437006e38.png")),
            ("fabrication-cadmep", "Autodesk", "Fabrication CADmep",
             "İmalata yönelik kanal ve boru detaylandırma", "c1", ico_img("autodesk")),
            ("fabrication-camduct", "Autodesk", "Fabrication CAMduct",
             "Sac kanal imalatı ve kesim optimizasyonu", "c1", ico_img("autodesk")),
            ("fabrication-estmep", "Autodesk", "Fabrication ESTmep",
             "Tesisat maliyet tahmini ve metraj", "c1", ico_img("autodesk")),
            ("cfd", "Autodesk", "Autodesk CFD", "Akış ve ısıl analiz — HVAC doğrulama",
             "c2", ico_img("autodesk")),
            ("autodesk", "Autodesk", "Navisworks", "Clash detection ve model koordinasyonu",
             "c3", emb_img("emb-9ab064fc9a.png")),
            ("bim-collaborate-pro", "Autodesk", "Autodesk BIM Collaborate",
             "Bulut worksharing ve saha yönetimi", "c3", emb_img("emb-cc5dc22000.png")),
            ("designjet", "HP", "HP Designjet T", "Tesisat paftaları için geniş format baskı",
             "c4", ico_img("hp")),
            ("hp-z-workstation", "HP", "HP Z Workstation",
             "Revit ve CFD için sertifikalı iş istasyonu", "c4", ico_img("hp")),
        ],
        "blog_topic": "Revit",
        "cta_h2": "Tesisat projeniz için konuşalım",
    },
    "icmimarlik": {
        "file": "sektor_icmimarlik.html",
        "slug": "sektor-icmimarlik",
        "acc": "f472b6",
        "name": "İç Mimarlık & Tasarım",
        "crumb": "İç Mimarlık & Tasarım",
        "badge": "Interior Design",
        "badge_icon": "armchair",
        "title": "İç Mimarlık & Tasarım Çözümleri — Cadbim",
        "desc": ("Cadbim İç Mimarlık çözümleri — SketchUp, Chaos Corona, V-Ray, Lumion ve "
                 "Adobe ile konseptten fotogerçekçi sunuma iç mekân tasarım teknolojileri."),
        "h1a": "İç Mimarlık için",
        "h1b": "Tam Çözüm Portföyü",
        "hero_p": ("Konsept panosundan fotogerçekçi render'a ve uygulama paftasına — "
                   "iç mekân tasarımının tüm araçları."),
        "art_alt": "İç mimarlık iş akışı — izometrik oda, mobilya ve aydınlatma şeması",
        "svc_name": "İç Mimarlık & Tasarım Çözümleri",
        "wf_title": "Konseptten Uygulamaya İç Mekân Akışı",
        "workflow": [
            ("pencil", "Konsept & Mekân Kurgusu",
             "SketchUp ile hızlı hacim etüdü, yerleşim ve mobilya alternatifleri."),
            ("armchair", "Modelleme & Malzeme",
             "3ds Max ve SketchUp'ta doku, kumaş ve aydınlatma kurgusu."),
            ("sun-high", "Fotogerçekçi Render",
             "Chaos Corona ve V-Ray ile iç mekân görselleştirmede stüdyo kalitesi."),
            ("palette", "Sunum & Revizyon",
             "Lumion ve Enscape ile gerçek zamanlı gezinti; Photoshop ve InDesign ile sunum panosu."),
            ("file-text", "Uygulama & Teslim",
             "AutoCAD LT paftaları ve DesignJet baskılarıyla uygulamaya hazır teslim."),
        ],
        "sol_cards": [
            ("gorsellestirme", "sun-high", "Görselleştirme & Render",
             "Corona, V-Ray ve Lumion ile iç mekân görselleştirmede fotogerçekçi sonuçlar."),
            ("yaratici-icerik", "palette", "Yaratıcı İçerik & Tasarım",
             "Photoshop ve InDesign ile konsept panoları, sunum dosyaları ve içerik üretimi."),
            ("sanatsal-baski", "wand", "Sanatsal Baskı Atölyesi",
             "İç mekân projeleriniz için duvar sanatı ve fine art baskı — 12 renk pigment kalitesinde."),
        ],
        "sol_pills": [("gerceklik-yakalama", "Gerçeklik Yakalama & Tarama")],
        "brands": [
            ("sketchup", "Trimble", "SketchUp Pro, SketchUp Studio"),
            ("chaos", "Chaos", "Chaos Corona, Chaos V-Ray, Chaos Enscape"),
            ("autodesk", "Autodesk", "3ds Max, AutoCAD LT"),
            ("lumion", "Lumion", "Lumion Pro, Lumion View"),
            ("adobe", "Adobe", "Adobe Photoshop, Adobe InDesign"),
            ("hp", "HP", "HP Designjet Z, HP Z Workstation"),
        ],
        "chips": [("c0", "Konsept & Modelleme"), ("c1", "Görselleştirme"),
                  ("c2", "Sunum & İçerik"), ("c3", "Çıktı & Baskı"), ("c4", "Donanım")],
        "products": [
            ("sketchup-pro", "TRIMBLE", "SketchUp Pro",
             "İç mekân modelleme ve yerleşimin endüstri standardı", "c0", ico_img("sketchup")),
            ("3dsmax", "Autodesk", "3ds Max", "Detaylı modelleme, kumaş ve malzeme kurgusu",
             "c0", ico_img("autodesk")),
            ("autocad-lt", "Autodesk", "AutoCAD LT", "Uygulama paftaları ve 2D detaylar",
             "c0", ico_img("autodesk")),
            ("corona", "Chaos", "Chaos Corona",
             "İç mekân görselleştirmede fotogerçekçilik standardı", "c1", ico_img("chaos")),
            ("vray", "Chaos", "Chaos V-Ray", "Işık ve malzemede tam kontrol",
             "c1", ico_img("chaos")),
            ("enscape", "Chaos", "Chaos Enscape", "SketchUp ile gerçek zamanlı render",
             "c1", ico_img("chaos")),
            ("lumion", "Lumion", "Lumion", "Hızlı, atmosferik iç ve dış mekân animasyonu",
             "c1", ico_img("lumion")),
            ("photoshop", "Adobe", "Adobe Photoshop", "Post-prodüksiyon ve ambiyans dokunuşları",
             "c2", ico_img("adobe", pad=7)),
            ("indesign", "Adobe", "Adobe InDesign", "Konsept panoları ve sunum dosyaları",
             "c2", ico_img("adobe", pad=7)),
            ("designjet", "HP", "HP DesignJet Z", "Sunum panoları ve sanatsal baskı",
             "c3", ico_img("hp")),
            ("hp-z-workstation", "HP", "HP Z Workstation", "Render için GPU gücü",
             "c4", ico_img("hp")),
        ],
        "blog_topic": "V-Ray",
        "cta_h2": "İç mimarlık projeniz için konuşalım",
    },
}


# ================================================================ BOLUM KURUCULAR
def build_hero(c):
    acc = c["acc"]
    return """<section class="hero">
  <div class="hero-bg" style="background:radial-gradient(ellipse 80% 60% at 0% -10%,rgba(""" + rgb(acc) + """,0.15) 0%,transparent 60%);"></div>
  <div class="hero-grid"></div>
  <div class="crumb" style="position:relative;z-index:1;">
    <a href="/">Anasayfa</a>
    <i class="ti ti-chevron-right" style="font-size:11px;"></i>
    <a href="endustriler">Endüstriler</a>
    <i class="ti ti-chevron-right" style="font-size:11px;"></i>
    <span style="color:var(--w80);">""" + c["crumb"] + """</span>
  </div>
  <div class="hero-inner">
    <div>
      <div lang="en" class="hero-badge" style="background:rgba(""" + rgb(acc) + """,0.12);border-color:#""" + acc + """40;color:#""" + acc + """;">
        <i class="ti ti-""" + c["badge_icon"] + """" style="font-size:18px;color:#""" + acc + """;"></i>  """ + c["badge"] + """
      </div>
      <h1 class="sec-h1">""" + c["h1a"] + """<br><span style="color:#""" + acc + """;">""" + c["h1b"] + """</span></h1>
      <p class="sec-desc">""" + c["hero_p"] + """</p>
      <div class="btns">
        <a href="iletisim#form" class="btn-p">Uzmanla Konuş <i class="ti ti-arrow-right"></i></a>
        <a href="egitimler" class="btn-g">Eğitim Programları</a>
      </div>
    </div>
    <div class="hero-art">
      <img src="assets/img/sektor/""" + c["key"] + """.svg" alt=\"""" + c["art_alt"] + """\" width="640" height="420" decoding="async">
    </div>
  </div>
</section>
"""


def build_workflow(c):
    acc = c["acc"]
    steps = []
    for i, (icon, title, desc) in enumerate(c["workflow"]):
        steps.append(workflow_step(acc, "%02d" % (i + 1), icon, title, desc,
                                   last=(i == len(c["workflow"]) - 1)))
    return ('<section data-enrich style="padding:64px 3rem;background:#0a1225;">\n'
            '  <div style="max-width:1200px;margin:0 auto;">\n'
            '    <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;'
            'color:#00c8f0;margin-bottom:8px;">İş Akışı</div>\n'
            '    <div style="font-family:\'Manrope\',sans-serif;font-size:clamp(1.4rem,2.6vw,'
            '1.9rem);font-weight:800;color:#fff;margin-bottom:8px;">' + c["wf_title"] + '</div>\n'
            '    <p style="font-size:14px;color:rgba(255,255,255,.45);line-height:1.7;'
            'margin:0 0 28px;max-width:640px;">Bu sektörde kullandığımız araç zinciri, sürecin '
            'her halkasını bir öncekine bağlar — veri kopmadan akar.</p>\n'
            '    <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:8px;">\n'
            + "\n".join(steps) + '</div>\n  </div>\n</section>\n')


def build_solutions(c):
    cards = "\n".join(sol_card(*x[:1], *x[1:]) if False else sol_card(x[0], x[1], x[2], x[3])
                      for x in c["sol_cards"])
    pills = ""
    if c["sol_pills"]:
        pills = ('\n  <div class="sol-pills">\n'
                 + "\n".join(sol_pill(h, t) for h, t in c["sol_pills"]) + "\n  </div>")
    return ('<section class="section" style="padding-top:0;">\n'
            '  <div class="sh">\n    <div class="slabel">Çözümler</div>\n'
            '    <div class="stitle">Bu endüstride kullanılan Cadbim çözümleri</div>\n'
            '    <p class="ssub">İlgili çözüm sayfalarını inceleyin — her çözümde kullanılan '
            'ürünleri görün</p>\n  </div>\n'
            '  <div class="grid g3" style="margin-top:0;">\n' + cards + '\n  </div>' + pills
            + '\n</section>\n')


def build_brands(c):
    rows = "".join(brand_row(k, t, s) for k, t, s in c["brands"])
    return ('<section class="brands">\n'
            '  <div class="sh" style="margin-bottom:22px;">\n'
            '    <div class="slabel">Markalar</div>\n'
            '    <div class="stitle">Bu sektörde çalıştığımız markalar</div>\n'
            '    <p class="ssub">Cadbim; Autodesk Gold Partner ve Adobe Gold Reseller Partner, '
            'HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağıdır.</p>\n'
            '  </div>\n  <div class="brand-stack">' + rows + '</div>\n'
            '  <div class="partner-note"><i class="ti ti-shield-check" '
            'style="color:var(--cyan);margin-right:6px;"></i><strong style="color:var(--w80);">'
            'Cadbim Gold Partner</strong> — Autodesk, Adobe, HP ve UltiMaker için tek yetkili '
            'çözüm ortağı.</div>\n</section>\n')


def build_catalog(c):
    chips = "\n".join('    <button class="fchip" data-f="%s">%s</button>' % (k, t)
                      for k, t in c["chips"])
    cards = "\n".join(pcard(*p[:5], p[5]) if False else
                      pcard(p[0], p[1], p[2], p[3], p[4], p[5]) for p in c["products"])
    return ('<section class="solutions" id="urun-katalogu">\n'
            '  <div class="sol-header">\n'
            '    <div class="sol-label">Ürünler</div>\n'
            '    <div class="sol-title">' + c["name"].replace("&", "&amp;")
            + ' için kullandığımız ürünler</div>\n  </div>\n'
            '  <div class="pfilter" id="pfilter">\n'
            '    <button class="fchip active" data-f="all">Tümü</button>\n' + chips + '\n'
            '    <div class="psearch"><i class="ti ti-search"></i>'
            '<input id="psearch" type="text" placeholder="Ürün ara..." aria-label="Ürün ara">'
            '</div>\n  </div>\n'
            '  <div class="pgrid" id="pgrid" style="margin-top:22px;">\n' + cards + '\n  </div>\n'
            '  <p id="pempty" style="display:none;color:var(--w50);font-size:14px;'
            'margin-top:24px;">Aramanızla eşleşen ürün bulunamadı.</p>\n</section>\n'
            '<script>\n(function(){\n'
            "  var chips=document.querySelectorAll('#pfilter .fchip');\n"
            "  var cards=[].slice.call(document.querySelectorAll('#pgrid .pcard'));\n"
            "  var f='all', q='';\n"
            "  function apply(){\n    var n=0;\n    cards.forEach(function(c){\n"
            "      var ok=(f==='all'||c.getAttribute('data-cat')===f)&&(!q||c.textContent."
            "toLowerCase().indexOf(q)>-1);\n"
            "      c.style.display=ok?'':'none'; if(ok)n++;\n    });\n"
            "    document.getElementById('pempty').style.display=n?'none':'';\n  }\n"
            "  chips.forEach(function(ch){ch.addEventListener('click',function(){\n"
            "    chips.forEach(function(x){x.classList.remove('active');});\n"
            "    ch.classList.add('active'); f=ch.getAttribute('data-f'); apply();\n  });});\n"
            "  document.getElementById('psearch').addEventListener('input',function(e){\n"
            "    q=e.target.value.trim().toLowerCase(); apply();\n  });\n})();\n</script>\n")


# ================================================================== MONTAJ
def build_page(key):
    c = dict(SECTORS[key]); c["key"] = key
    acc = c["acc"]
    tpl = io.open(TPL, encoding="utf-8").read()

    head, _, rest = tpl.partition("</nav>\n")
    body, _, foot = rest.partition('<footer id="iletisim">')

    # head = dokuman basi + <body> + nav; meta degisimleri nav'a bulasmasin
    head_only = head.split("<body>")[0] + "<body>\n"
    nav = head.split("<body>")[1] + "</nav>\n"

    # --- head: meta/SEO degisimi ---
    rep = [
        ('content="Cadbim Mimarlık çözümleri — Konseptten teslimata — BIM, görselleştirme, '
         'koordinasyon ve baskı için tam portföy."', 'content="%s"' % c["desc"]),
        ("<title>Mimarlık Çözümleri — Cadbim</title>", "<title>%s</title>" % c["title"]),
        ('content="Mimarlık Çözümleri — Cadbim"', 'content="%s"' % c["title"]),
        ("sektor-mimari", c["slug"]),
        ("sektor_mimari.png", "%s.png" % c["file"].replace(".html", "").replace("sektor_", "sektor_")),
        ('"name": "Mimarlık Çözümleri"', '"name": "%s"' % c["svc_name"]),
        ('"name": "Mimarlık Çözümleri — Cadbim"', '"name": "%s"' % c["title"]),
        ('"description": "Cadbim Mimarlık çözümleri — Konseptten teslimata — BIM, görselleştirme, '
         'koordinasyon ve baskı için tam portföy."', '"description": "%s"' % c["desc"]),
    ]
    for old, new in rep:
        head_only = head_only.replace(old, new)
    head_only = re.sub(r'"name": "Mimarlık Çözümleri",\n     "item"',
                       '"name": "%s",\n     "item"' % c["svc_name"], head_only)
    # aksan rengi (hero-art glow)
    head_only = head_only.replace("rgba(%s,.16)" % OLD_RGB, "rgba(%s,.16)" % rgb(acc))
    head_only = head_only.replace("#" + OLD_HEX, "#" + acc)

    # --- govde bolumleri ---
    # Calisma Modelimiz blogu iskeletten alinir (aksan degistirilerek)
    m = re.search(r'<section data-enrich[^>]*>(?:(?!</section>).)*?Çalışma Modelimiz.*?\n</section>\n',
                  body, re.S)
    model = m.group(0).replace("#" + OLD_HEX, "#" + acc)
    # blog + cta
    m2 = re.search(r'<div class="cta-wrap">.*?\n</div>\n', body, re.S)
    ctawrap = m2.group(0)
    ctawrap = ctawrap.replace('data-topic="BIM"', 'data-topic="%s"' % c["blog_topic"])
    ctawrap = ctawrap.replace("<h2>Mimarlık projeniz için konuşalım</h2>",
                              "<h2>%s</h2>" % c["cta_h2"])
    ctawrap = ctawrap.replace('href="iletisim" class="btn-p"', 'href="iletisim#form" class="btn-p"')

    out = (head_only + nav + "\n"
           + build_hero(c) + "\n"
           + build_workflow(c) + "\n"
           + build_solutions(c) + "\n"
           + build_brands(c) + "\n"
           + build_catalog(c) + "\n"
           + model + "\n"
           + ctawrap
           + '<footer id="iletisim">' + foot)
    path = os.path.join(ROOT, c["file"])
    io.open(path, "w", encoding="utf-8", newline="\n").write(out)
    return path, len(out)


if __name__ == "__main__":
    for key in SECTORS:
        p, n = build_page(key)
        print("OK %-26s %d bayt" % (os.path.basename(p), n))
