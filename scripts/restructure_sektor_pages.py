# -*- coding: utf-8 -*-
"""Sektor sayfalarini tek ve mantikli bir akisa gore yeniden kurar.

Yapilanlar
----------
1. Ince "tab" seridi yerine buyuk ikonlu, hover'da sektor gorseli animasyonla
   acilan sektor gecis seridi (.secnav) — 7 sayfada da ayni.
2. Hero'daki marka listesi kaldirilir; yerine sektore ozel teknik illustrasyon
   gelir. Markalar sayfanin ortasinda ayri bir seride toplanir.
3. "Diger Sektorler" blogu silinir (ust seritle mukerrer).
4. Bolum sirasi: Hero -> Is Akisi -> Cozumler -> Markalar -> Urunler ->
   Basari Oykuleri -> Calisma Modelimiz -> Blog -> CTA.
5. Cozum kartlari ile cozum "pill"lerinin olusturdugu iki ayri bolum tek
   bolumde birlestirilir; yanlis bolum etiketleri duzeltilir.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# key, dosya, aksan rengi, gorunen ad, ikon, url
SECTORS = [
    ("mimari",    "sektor_mimari.html",    "#818cf8", "Mimarlık",            "ti-building", "sektor-mimari"),
    ("insaat",    "sektor_insaat.html",    "#22c55e", "İnşaat &amp; Altyapı", "ti-crane",    "sektor-insaat"),
    ("makine",    "sektor_makine.html",    "#f59e0b", "Makine &amp; Üretim",  "ti-settings", "sektor-makine"),
    ("otomotiv",  "sektor_otomotiv.html",  "#ef4444", "Otomotiv",            "ti-car",      "sektor-otomotiv"),
    ("medya",     "sektor_medya.html",     "#c084fc", "Medya &amp; Eğlence",  "ti-movie",    "sektor-medya"),
    ("egitim",    "sektor_egitim.html",    "#38bdf8", "Eğitim",              "ti-school",   "sektor-egitim"),
    ("havacilik", "sektor_havacilik.html", "#a5b4fc", "Havacılık &amp; Savunma", "ti-plane", "sektor-havacilik"),
]

ART_ALT = {
    "mimari": "Mimarlık BIM iş akışı — izometrik yapı modeli şeması",
    "insaat": "İnşaat ve altyapı iş akışı — köprü ve saha şeması",
    "makine": "Makine ve üretim iş akışı — dişli ve CAM takım yolu şeması",
    "otomotiv": "Otomotiv iş akışı — araç yüzey ağı şeması",
    "medya": "Medya ve eğlence iş akışı — 3B model ve film şeridi şeması",
    "egitim": "Eğitim iş akışı — sınıf, ekran ve 3B baskı şeması",
    "havacilik": "Havacılık ve savunma iş akışı — uçak sonlu eleman ağı şeması",
}


# Sablon B sayfalarinda hero'da marka listesi yok; sayfadaki urunlerden turetilir.
LOGO = {
    "autodesk": ('assets/logos/autodesk-white.svg', 997, 563, "dark", ""),
    "trimble": ('assets/logos/sketchup.svg', 1158, 354, "dark", "filter:brightness(0) invert(1);opacity:.92;"),
    "chaos": ('assets/logos/chaos.webp', 1280, 1280, "dark", ""),
    "hp": ('assets/logos/hp-blue.png', 300, 300, "light", ""),
    "adobe": ('assets/logos/adobe-logo.svg', 65, 35, "dark", "filter:brightness(0) invert(1);opacity:.92;"),
    "ultimaker": ('assets/logos/ultimaker.svg', 150, 22, "dark", "filter:brightness(0) invert(1);opacity:.92;"),
}

BRANDS_B = {
    "egitim": [
        ("autodesk", "Autodesk", "Autodesk Eğitim Portföyü, Tinkercad"),
        ("ultimaker", "UltiMaker", "UltiMaker S Serisi, MakerBot Sketch Sprint"),
        ("adobe", "Adobe", "Adobe Express"),
        ("trimble", "Trimble", "SketchUp"),
        ("hp", "HP", "HP Z Workstation"),
        ("chaos", "Chaos", "Chaos V-Ray"),
    ],
    "havacilik": [
        ("autodesk", "Autodesk", "Inventor, Fusion, Vault PDM, Moldflow"),
        ("ultimaker", "UltiMaker", "UltiMaker Factor 4"),
        ("hp", "HP", "HP Z Workstation"),
    ],
}


def brand_rows(key):
    rows = []
    for slug, title, sub in BRANDS_B.get(key, []):
        src, w, h, tone, extra = LOGO[slug]
        box = ("background:#fff;" if tone == "light"
               else "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);")
        rows.append(
            '<div class="brand-row">\n'
            '          <div style="width:28px;height:28px;border-radius:6px;%s'
            'display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:4px;">'
            '<img width="%d" height="%d" src="%s" alt="%s" '
            'style="max-width:100%%;max-height:100%%;object-fit:contain;%s" loading="lazy"></div>\n'
            '          <div><div class="brand-name">%s</div>'
            '<div style="font-size:11px;color:var(--w30);">%s</div></div>\n'
            '        </div>' % (box, w, h, src, title, extra, title, sub))
    if not rows:
        return None
    return '<div class="brand-stack">' + "".join(rows) + "</div>"


def rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "rgba(%d,%d,%d,%s)" % (r, g, b, alpha)


# --------------------------------------------------------------------- CSS
def build_css(accent):
    return """
<style>
/* === SEKTOR GECIS SERIDI ============================================== */
.secnav{position:sticky;top:68px;z-index:100;margin-top:68px;background:rgba(10,18,37,.94);backdrop-filter:blur(20px);border-bottom:.5px solid var(--w10);}
.secnav-inner{position:relative;max-width:1180px;margin:0 auto;}
.secnav-inner::after{content:'';position:absolute;top:0;right:0;bottom:0;width:52px;background:linear-gradient(90deg,transparent,rgba(10,18,37,.96));pointer-events:none;opacity:0;transition:opacity .25s;}
.secnav-inner.has-more::after{opacity:1;}
.secnav-track{display:flex;gap:9px;overflow-x:auto;padding:13px 0;scrollbar-width:none;-ms-overflow-style:none;scroll-snap-type:x proximity;}
.secnav-track::-webkit-scrollbar{display:none;}
.sec-card{position:relative;overflow:hidden;isolation:isolate;flex:0 0 auto;scroll-snap-align:start;display:flex;align-items:center;gap:11px;padding:9px 20px 9px 10px;border-radius:14px;border:.5px solid var(--w10);background:var(--navy3);text-decoration:none;transition:border-color .25s,transform .25s,background .25s,box-shadow .25s;}
.sec-card::after{content:'';position:absolute;inset:0;z-index:-1;background-image:var(--art);background-size:auto 205%;background-position:right -14px center;background-repeat:no-repeat;opacity:0;transform:scale(1.2) translateX(10px);transition:opacity .4s ease,transform .9s cubic-bezier(.16,.8,.3,1);}
.sec-card:hover{border-color:var(--sc);transform:translateY(-3px);background:#101d3a;box-shadow:0 10px 26px rgba(0,0,0,.35);}
.sec-card:hover::after{opacity:.72;transform:scale(1) translateX(0);}
.sec-ico{position:relative;width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:21px;color:var(--sc);background:var(--scbg);flex-shrink:0;transition:transform .35s cubic-bezier(.16,.8,.3,1),box-shadow .25s;}
.sec-card:hover .sec-ico{transform:scale(1.09) rotate(-4deg);box-shadow:0 0 0 1px var(--sc) inset;}
.sec-name{position:relative;font-size:13.5px;font-weight:600;color:var(--w80);white-space:nowrap;transition:color .2s;}
.sec-card:hover .sec-name{color:var(--w);}
.sec-card.active{border-color:var(--sc);background:linear-gradient(180deg,rgba(255,255,255,.05),transparent),var(--navy3);}
.sec-card.active .sec-ico{box-shadow:0 0 0 1px var(--sc) inset;}
.sec-card.active .sec-name{color:var(--w);}
.sec-bar{position:absolute;left:10px;right:10px;bottom:0;height:2px;border-radius:2px 2px 0 0;background:var(--sc);}
@media(prefers-reduced-motion:reduce){.sec-card,.sec-card::after,.sec-ico{transition:none;}}

/* === HERO GORSELI ===================================================== */
.hero{padding:40px 3rem 56px;}
.hero-inner{display:grid;grid-template-columns:1.05fr .95fr;gap:3.5rem;align-items:center;position:relative;z-index:1;}
.hero-art{position:relative;border-radius:var(--rxl);border:.5px solid var(--w10);background:linear-gradient(165deg,rgba(255,255,255,.045),transparent 55%),var(--navy2);overflow:hidden;}
.hero-art::after{content:'';position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse 65% 55% at 72% 18%,__GLOW__,transparent 72%);}
.hero-art img{display:block;width:100%;height:auto;}

/* === MARKA SERIDI ===================================================== */
.brands{padding:56px 3rem;background:var(--navy2);border-top:.5px solid var(--w06);border-bottom:.5px solid var(--w06);}
.brand-stack{display:grid;grid-template-columns:repeat(auto-fit,minmax(238px,1fr));gap:12px;}
.brand-row{display:flex;align-items:center;gap:12px;padding:14px 16px;background:rgba(255,255,255,0.03);border:.5px solid rgba(255,255,255,0.08);border-radius:var(--rm);font-size:12px;color:var(--w50);transition:border-color .2s;}
.brand-row:hover{border-color:var(--cbor);}
.brand-name{font-weight:600;color:var(--w80);font-size:13px;}
.partner-note{margin-top:16px;padding:13px 16px;background:rgba(0,200,240,0.04);border:.5px solid var(--cbor);border-radius:var(--rm);font-size:12.5px;color:var(--w50);line-height:1.6;}

/* === COZUM PILL SATIRI ================================================ */
.sol-pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;}
.sol-pill{display:inline-flex;align-items:center;gap:8px;padding:9px 15px;border-radius:12px;background:var(--navy3);border:.5px solid var(--w10);font-size:13px;color:var(--w50);text-decoration:none;transition:border-color .2s,color .2s,transform .2s;}
.sol-pill:hover{border-color:var(--cbor);color:var(--w);transform:translateY(-2px);}
.sol-pill i{font-size:13px;color:var(--cyan);}

/* === ORTAK YERLESIM =================================================== */
.section{padding:56px 3rem;}
.hero-inner,.hero>.crumb,.brands>*,.solutions>*{max-width:1180px;margin-left:auto;margin-right:auto;}
.secnav{padding:0 3rem;}

@media(max-width:960px){
  .hero{padding:32px 1.5rem 44px;}
  .hero-inner{grid-template-columns:1fr;gap:2rem;}
  .secnav{padding:0 1.5rem;}
  .brands{padding:44px 1.5rem;}
  .section{padding:44px 1.5rem;}
}
</style>
""".replace("__GLOW__", rgba(accent, ".16"))


# ------------------------------------------------------------------ SECNAV
def build_secnav(active_key):
    rows = []
    for key, _f, accent, name, icon, url in SECTORS:
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


# ------------------------------------------------------------------ HELPERS
def cut(text, pattern, flags=re.S, required=True, label=""):
    m = re.search(pattern, text, flags)
    if not m:
        if required:
            raise RuntimeError("Blok bulunamadi: %s" % (label or pattern[:60]))
        return None, text
    return m.group(0), text[:m.start()] + text[m.end():]


def cut_all(text, pattern, flags=re.S):
    blocks = re.findall(pattern, text, flags)
    for b in blocks:
        text = text.replace(b, "", 1)
    return blocks, text


def section(label, title, sub, body, alt=False, pad="56px 3rem"):
    bg = "background:var(--navy2);" if alt else ""
    subhtml = ('\n    <p class="ssub">%s</p>' % sub) if sub else ""
    return ('<section style="padding:%s;%s">\n'
            '  <div class="sh" style="margin-bottom:24px;">\n'
            '    <div class="slabel">%s</div>\n'
            '    <div class="stitle">%s</div>%s\n'
            '  </div>\n%s\n</section>\n' % (pad, bg, label, title, subhtml, body))


def split_sections(block):
    """Ayni <section> icine sikismis birden fazla .sh basligini ayirir."""
    m = re.match(r'(<section[^>]*>)(.*)(\n</section>\n)$', block, re.S)
    if not m:
        return [block]
    open_tag, inner, close = m.groups()
    idxs = [mm.start() for mm in re.finditer(r'\n\s*<div class="sh"', inner)]
    if len(idxs) < 2:
        return [block]
    parts = []
    for i, s in enumerate(idxs):
        e = idxs[i + 1] if i + 1 < len(idxs) else len(inner)
        parts.append(open_tag + inner[s:e].rstrip() + close)
    return parts


def pills_html(pairs):
    out = ['<div class="sol-pills">']
    for href, text in pairs:
        out.append('    <a href="%s" class="sol-pill"><i class="ti ti-arrow-right"></i>%s</a>' % (href, text))
    out.append("  </div>")
    return "\n  ".join(out)


# --------------------------------------------------------------------- MAIN
def rebuild(path, key, accent, name):
    with io.open(path, encoding="utf-8") as fh:
        html = fh.read()

    head, sep, rest = html.partition("</nav>\n")
    if not sep:
        raise RuntimeError("%s: </nav> bulunamadi" % path)
    body, fsep, foot = rest.partition("<footer id=\"iletisim\">")
    if not fsep:
        raise RuntimeError("%s: footer bulunamadi" % path)

    # --- eski tab seridi ve "Diger Sektorler" ---
    _tabs, body = cut(body, r'<div class="tabs-nav">.*?\n</div>\n', required=False)
    _others, body = cut(body, r'<div class="others">.*?\n</div>\n', required=False)

    # --- hero ---
    hero, body = cut(body, r'<section class="hero">.*?\n</section>\n', label="hero")

    # --- urun katalogu ---
    catalog, body = cut(
        body, r'<section class="solutions" id="urun-katalogu">.*?</section>\n<script>.*?</script>\n',
        required=False)
    if catalog is None:  # sablon B: .cross icinde
        catalog, body = cut(
            body, r'<section class="section" style="padding-top:0;">\s*<div class="cross">.*?\n</section>\n',
            label="urun katalogu")
        catalog = catalog.replace("<h3>Bu sektörde kullanılan ürünler</h3>",
                                  "<h3>%s için kullandığımız ürünler</h3>" % name)
    else:               # sablon A: "Cozum Alanlari" etiketi artik Cozumler bolumunde
        catalog = re.sub(r'<div class="sol-label">.*?</div>',
                         '<div class="sol-label">Ürünler</div>', catalog, count=1)
        catalog = re.sub(r'<div class="sol-title">.*?</div>',
                         '<div class="sol-title">%s için kullandığımız ürünler</div>' % name,
                         catalog, count=1)

    # --- is akisi / calisma modeli ---
    enrich, body = cut_all(body, r'<section data-enrich.*?\n</section>\n')
    workflow = next((b for b in enrich if "İş Akışı" in b), None)
    model = next((b for b in enrich if "Çalışma Modelimiz" in b), None)
    leftover_enrich = [b for b in enrich if b not in (workflow, model)]

    # --- cozum kartlari / basari oykuleri / yetenek kartlari ---
    raw_plain, body = cut_all(body, r'<section class="section[^"]*"[^>]*>.*?\n</section>\n')
    plain = [p for blk in raw_plain for p in split_sections(blk)]
    success = next((b for b in plain if "Başarı Öyküleri" in b), None)
    caps = next((b for b in plain if "Neler Sunuyoruz" in b), None)
    sol_cards = [b for b in plain if b not in (success, caps)]

    # --- cozum pill bolumleri (bazi sayfalarda basari oykuleri de bu bicimde) ---
    newsol_raw, body = cut_all(body, r'<section data-newsol.*?\n</section>\n')
    newsol = []
    for blk in newsol_raw:
        if "Başarı Öyküleri" in blk and success is None:
            success = blk
        else:
            newsol.append(blk)

    # --- blog + cta ---
    ctawrap, body = cut(body, r'<div class="cta-wrap">.*?\n</div>\n', required=False)
    if ctawrap is None:
        blog, body = cut(body, r'<section[^>]*id="blog-related-section">.*?</script>\n',
                         required=False)
        cta, body = cut(body, r'<div class="cta-strip">.*?\n</div>\n', label="cta")
        ctawrap = (blog or "") + cta

    # hicbir icerik gozden kacmamali
    if body.strip():
        raise RuntimeError("%s: siniflandirilmamis icerik kaldi:\n%s"
                           % (os.path.basename(path), body.strip()[:400]))

    # ---------------------------------------------------------------- HERO
    # sablon A hero'sunun sag sutunu: marka listesi + Gold Partner notu
    RIGHTCOL = r'    <div>\n      <div style="font-size:10px;letter-spacing:2px.*?\n    </div>\n'
    rc = re.search(RIGHTCOL, hero, re.S)
    brand_html = partner_text = None
    if rc:
        rc_text = rc.group(0)
        start = rc_text.index('<div class="brand-stack">')
        m_note = re.search(r'\n      <div style="margin-top:14px;', rc_text)
        end = m_note.start() if m_note else rc_text.rindex('\n    </div>\n')
        brand_html = rc_text[start:end].rstrip()
        m_txt = re.search(r'<strong[^>]*>Cadbim Gold Partner</strong>(.*?)\n      </div>',
                          rc_text, re.S)
        partner_text = m_txt.group(1).strip() if m_txt else None

    art = ('    <div class="hero-art">\n'
           '      <img src="assets/img/sektor/%s.svg" alt="%s" width="640" height="420" decoding="async">\n'
           '    </div>\n' % (key, ART_ALT[key]))

    if brand_html:  # sablon A — sag sutunu gorselle degistir
        hero = hero[:rc.start()] + art + hero[rc.end():]
    else:           # sablon B — tek sutunlu hero'yu iki sutuna cevir
        inner = re.search(r'<div style="position:relative;z-index:1;">\n(.*?)\n  </div>\n</section>',
                          hero, re.S)
        if not inner:
            raise RuntimeError("%s: sablon B hero govdesi cozulemedi" % path)
        crumb = re.search(r'<div class="crumb">.*?</div>', inner.group(1), re.S).group(0)
        col = re.search(r'<div style="max-width:720px;">\n(.*?)\n    </div>', inner.group(1), re.S).group(1)
        col = col.replace('max-width:600px;', '')
        hero = re.sub(
            r'<div style="position:relative;z-index:1;">\n.*?\n  </div>\n</section>',
            '  %s\n  <div class="hero-inner">\n    <div>\n%s\n    </div>\n%s  </div>\n</section>'
            % (crumb, col, art), hero, flags=re.S)

    # ------------------------------------------------------------ COZUMLER
    known = set()
    for blk in sol_cards:
        known.update(re.findall(r'<h3><a href="([^"]+)"', blk))
    extra = []
    for blk in newsol:
        for href, text in re.findall(r'<a href="([^"]+)"[^>]*>(?:<i[^>]*></i>)?\s*([^<]+)</a>', blk):
            if href not in known:
                known.add(href)
                extra.append((href, text.strip()))

    solutions_html = ""
    if sol_cards:
        blk = sol_cards[0]
        blk = blk.replace('<div class="slabel">İlgili Ürünler</div>',
                          '<div class="slabel">Çözümler</div>')
        blk = blk.replace('<div class="slabel">İlgili Çözümler</div>',
                          '<div class="slabel">Çözümler</div>')
        if extra:
            blk = blk.replace("\n</section>\n", "\n  %s\n</section>\n" % pills_html(extra))
        solutions_html = blk
        for other in sol_cards[1:]:
            solutions_html += other
    elif extra:
        solutions_html = section(
            "Çözümler", "Bu sektöre hizmet eden Cadbim çözümleri",
            "Her çözüm sayfasında, o alanda kullandığımız ürünleri bulabilirsiniz.",
            "  " + pills_html(extra))

    # ------------------------------------------------------------- MARKALAR
    brands_html = ""
    if brand_html is None:
        brand_html = brand_rows(key)
    if brand_html:
        note = ('  <div class="partner-note"><i class="ti ti-shield-check" '
                'style="color:var(--cyan);margin-right:6px;"></i><strong '
                'style="color:var(--w80);">Cadbim Gold Partner</strong> %s</div>\n'
                % (partner_text or
                   "— Autodesk, Adobe, HP ve UltiMaker için tek yetkili çözüm ortağı."))
        brands_html = ('<section class="brands">\n'
                       '  <div class="sh" style="margin-bottom:22px;">\n'
                       '    <div class="slabel">Markalar</div>\n'
                       '    <div class="stitle">Bu sektörde çalıştığımız markalar</div>\n'
                       '    <p class="ssub">Cadbim; Autodesk Gold Partner ve Adobe Gold Reseller '
                       'Partner, HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağıdır.</p>\n'
                       '  </div>\n  %s\n%s</section>\n' % (brand_html.strip(), note))

    # ------------------------------------------------------- BASARI OYKULERI
    if success:
        success = success.replace('<div class="slabel">İlgili Ürünler</div>',
                                  '<div class="slabel">Referanslar</div>')

    # ------------------------------------------------------------- MONTAJ
    parts = [build_secnav(key), hero]
    for blk in (caps, workflow, solutions_html, brands_html, catalog, success, model):
        if blk:
            parts.append(blk if blk.endswith("\n") else blk + "\n")
    parts.extend(leftover_enrich)
    parts.append(ctawrap)
    new_body = "\n" + "\n".join(p.strip("\n") + "\n" for p in parts if p) + "\n"

    # ------------------------------------------------------------- CSS
    # artik kullanilmayan eski bilesenlerin kurallarini temizle
    head = re.sub(r'^/\* TABS \*/\n', "", head, flags=re.M)
    head = re.sub(r'^/\* DIĞER SEKTÖRLER \*/\n', "", head, flags=re.M)
    head = re.sub(r'^\.(tabs-nav|tab-btn|others|others-title|others-grid|other-link|other-name)'
                  r'[^\n]*\n', "", head, flags=re.M)
    head = re.sub(r'^  \.others\{[^\n]*\n', "", head, flags=re.M)
    head = head.replace("</head>", build_css(accent).strip() + "\n</head>", 1)

    out = head + "</nav>\n" + new_body + "<footer id=\"iletisim\">" + foot
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    return len(out)


if __name__ == "__main__":
    for key, fname, accent, name, _icon, _url in SECTORS:
        p = os.path.join(ROOT, fname)
        try:
            size = rebuild(p, key, accent, name)
            print("OK   %-24s %7d bytes" % (fname, size))
        except Exception as exc:  # noqa: BLE001
            print("HATA %-24s %s" % (fname, exc))
            sys.exit(1)
