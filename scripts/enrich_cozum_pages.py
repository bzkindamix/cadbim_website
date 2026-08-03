# -*- coding: utf-8 -*-
"""Cozum sayfalarini zenginlestirir.

Yapilanlar (her cozum sayfasi icin):
  1. Hero altina olcut seridi (stat strip)
  2. Hero'nun hemen ardina "Ne ise yarar" bolumu: uc paragraf + dort madde +
     o cozume ait teknik illustrasyon (assets/img/cozum/*.svg)
  3. Urun bolumunun oncesine marka seridi  -- Autodesk her zaman ilk
  4. Urun kartlarinin siralanmasi          -- Koleksiyonlar her zaman ilk
  5. Blog bolumunun oncesine SSS bolumu + FAQPage yapisal verisi

Betik yeniden calistirilabilir: daha once eklenmis bloklari isaretlerinden
tanir ve tekrar eklemez (once siler, sonra guncel halini yazar).
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cozum_icerik import BRANDS, COZUM  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

M_STATS = ("cz-stats", "<!-- /cz-stats -->")
M_INTRO = ("cz-intro", "<!-- /cz-intro -->")
M_BRANDS = ("cz-brands", "<!-- /cz-brands -->")
M_FAQ = ("cz-faq", "<!-- /cz-faq -->")
M_FARK = ("cz-fark", "<!-- /cz-fark -->")


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


def strip_block(html, marker):
    """Daha once eklenmis <!-- marker --> ... <!-- /marker --> blogunu siler."""
    name, close = marker
    start = '<!-- %s -->' % name
    while start in html:
        i = html.index(start)
        j = html.index(close, i) + len(close)
        # blogun onundeki bos satirlari da topla
        while j < len(html) and html[j] == '\n':
            j += 1
        html = html[:i] + html[j:]
    return html


# --------------------------------------------------------------------------
# blok ureticiler
# --------------------------------------------------------------------------
def build_stats(cfg):
    items = "".join(
        '<div class="cz-stat"><b>%s</b><span>%s</span></div>' % (esc(v), esc(l))
        for v, l in cfg["stats"])
    return ('<!-- cz-stats -->\n      <div class="cz-stats" style="--cz:%s;">%s</div>\n'
            '      <!-- /cz-stats -->' % (cfg["accent"], items))


def build_intro(cfg):
    """Tanitim bolumu: baslik solda, anlatim sagda, maddeler tam genislikte.

    Illustrasyon bu bolumde degil, hero'nun sag sutununda durur
    (bkz. build_hero_art) -- Onur'un 2026-08-03 tarihli yerlesim notu.
    """
    ps = "".join('<p class="cz-p">%s</p>\n        ' % p for p in cfg["intro"])
    buls = "".join(
        '<div class="cz-bul"><i class="ti ti-circle-check"></i>'
        '<div><h3>%s</h3><p>%s</p></div></div>' % (esc(t), esc(d))
        for t, d in cfg["bullets"])
    return u'''<!-- cz-intro -->
<section class="section cz-sec" style="--cz:%(accent)s;">
  <div class="cz-intro">
    <div class="cz-intro-h">
      <div class="slabel" style="color:var(--cz);">Bu Çözüm Nedir?</div>
      <div class="stitle">%(title)s</div>
    </div>
    <div class="cz-intro-b">
        %(ps)s
    </div>
  </div>
  <div class="cz-buls">%(buls)s</div>
</section>
<!-- /cz-intro -->
''' % dict(accent=cfg["accent"], title=esc(cfg["intro_title"]), ps=ps.strip(),
           buls=buls)


def build_hero_art(cfg):
    return ('<div class="cz-art cz-art-hero">'
            '<img src="assets/img/cozum/%s.svg" width="640" height="420" alt="%s" '
            'decoding="async"></div>'
            % (cfg["visual"],
               esc(cfg["intro_title"]) + u" — Cadbim teknik şeması"))


FARK_CARDS = [
    ("ti-license", u"Esnek Abonelik ve Lisans Modelleri",
     u"Tek ve çok kullanıcılı abonelikler, 1 ve 3 yıllık dönemler, koleksiyon "
     u"avantajı — kullanım profilinize uygun planı birlikte belirliyoruz."),
    ("ti-school", u"Yetkili Eğitim Merkezi (ATC)",
     u"Autodesk Yetkili Eğitim Merkezi olarak sertifikalı eğitimler; İzmir merkez "
     u"ofisimizde sınıf ve çevrim içi programlar."),
    ("ti-headset", u"Türkçe Teknik Destek",
     u"Kurulum, lisans yönetimi ve teknik sorularınızda Türkiye'den, Türkçe, "
     u"aynı gün yanıt."),
]

FARK_STEPS = [
    ("ti-message", u"1. Teklif & İhtiyaç Analizi",
     u"Kullanım profilinizi dinleyip doğru ürün ve adet planını çıkarıyoruz."),
    ("ti-file-check", u"2. Lisanslama / Tedarik",
     u"Resmî kanaldan, doğru fiyatla ve kayıtlı sözleşmeyle temin."),
    ("ti-settings", u"3. Kurulum & Eğitim",
     u"Dağıtım, yapılandırma ve rol bazlı kullanıcı eğitimi."),
    ("ti-headset", u"4. Sürekli Destek",
     u"Türkçe teknik destek ve yenileme dönemi hatırlatmaları."),
]


def build_fark(cfg):
    """Cadbim Farki seridi -- SSS'ten sonra gelir, 16 sayfada da ayni."""
    cards = "".join(
        '<div class="cz-fark-c"><span><i class="ti %s"></i></span>'
        '<h3>%s</h3><p>%s</p></div>' % (ic, esc(t), esc(d))
        for ic, t, d in FARK_CARDS)
    steps = "".join(
        '<div class="cz-step"><span><i class="ti %s"></i></span>'
        '<div><b>%s</b><em>%s</em></div></div>' % (ic, esc(t), esc(d))
        for ic, t, d in FARK_STEPS)
    return u'''<!-- cz-fark -->
<section class="section cz-sec" style="--cz:%(accent)s;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Cadbim Farkı</div>
    <div class="stitle">Yazılımı satıp bırakmıyoruz</div>
    <p class="ssub">Lisans satışı işin başlangıcı — kurulumdan eğitime, destekten
      yenilemeye kadar tüm yaşam döngüsü tek muhatapta kalır.</p>
  </div>
  <div class="cz-fark">%(cards)s</div>
  <div class="cz-steps">%(steps)s</div>
</section>
<!-- /cz-fark -->
''' % dict(accent=cfg["accent"], cards=cards, steps=steps)


def build_brands(cfg):
    rows = []
    for key in cfg["brands"]:
        name, href, logo, note = BRANDS[key]
        rows.append(
            '<a href="%s" class="cz-brand"><span class="cz-brand-logo">'
            '<img src="%s" alt="%s" loading="lazy" decoding="async"></span>'
            '<span class="cz-brand-txt"><b>%s</b><em>%s</em></span></a>'
            % (href, logo, esc(name), esc(name), esc(note)))
    return u'''<!-- cz-brands -->
<section class="section section-alt cz-sec" style="--cz:%(accent)s;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Markalar</div>
    <div class="stitle">Bu çözümde çalıştığımız markalar</div>
    <p class="ssub">Cadbim; Autodesk Gold Partner ve Adobe Gold Reseller Partner,
      HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağıdır.</p>
  </div>
  <div class="cz-brands">%(rows)s</div>
</section>
<!-- /cz-brands -->
''' % dict(accent=cfg["accent"], rows="".join(rows))


def build_faq(cfg):
    items = "".join(
        '<details class="cz-faq-i"><summary>%s<i class="ti ti-plus"></i></summary>'
        '<div class="cz-faq-a">%s</div></details>' % (esc(q), esc(a))
        for q, a in cfg["faq"])
    return u'''<!-- cz-faq -->
<section class="section section-alt cz-sec" style="--cz:%(accent)s;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Sıkça Sorulanlar</div>
    <div class="stitle">Bu çözüm hakkında merak edilenler</div>
    <p class="ssub">Aradığınız yanıt burada yoksa uzmanımıza doğrudan sorabilirsiniz.</p>
  </div>
  <div class="cz-faq">%(items)s</div>
  <div class="cz-faq-cta">
    <span>Sorunuz listede yok mu?</span>
    <a href="iletisim#form" class="btn-p">Uzmanımıza Sorun <i class="ti ti-arrow-right"></i></a>
  </div>
</section>
<!-- /cz-faq -->
''' % dict(accent=cfg["accent"], items=items)


def build_faq_jsonld(cfg):
    import json
    data = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in cfg["faq"]
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------
# donusumler
# --------------------------------------------------------------------------
HERO_P = re.compile(
    r'(<p style="font-size:16px;color:var\(--w50\);line-height:1\.75;'
    r'margin-bottom:32px;max-width:600px;">)(.*?)(</p>)', re.S)

PRODUCTS_HEAD = u'Bu çözümde kullanılan Cadbim ürünleri'
ALT_HEAD = u'Bu Ürünle İlgili'
CARD_RE = re.compile(r'<a href="(?P<href>[^"]+)" class="card"[^>]*>.*?</a>', re.S)
GRID_RE = re.compile(r'<div class="grid g3"[^>]*>')

# Autodesk portfoyu -- urun siralamasinda koleksiyonlardan hemen sonra gelir
AUTODESK = set("""
autodesk aec-collection pdm-collection me-collection
autocad autocad-lt autocad-web revit revit-lt inventor fusion fusion-manage
navisworks civil3d infraworks advance-steel robot-structural vehicle-tracking
autodesk-forma forma autodesk-docs autodesk-drive bim-collaborate-pro
construction-cloud tandem recap-pro vault-pdm netfabb moldflow cfd
featurecam powermill powershape factory-design alias vred 3dsmax maya
maya-creative arnold motionbuilder mudbox flow-studio flow-production-tracking
flame golaem meshmixer tinkercad dwg-trueview design-review desktop-connector
fabrication-cadmep fabrication-camduct fabrication-estmep
""".split())


def apply_hero(html, cfg):
    """Hero paragrafini zenginlestirir ve altina olcut seridi koyar."""
    html = strip_block(html, M_STATS)
    m = HERO_P.search(html)
    if m:
        html = (html[:m.start()] + m.group(1) + cfg["lead"] + m.group(3)
                + "\n      " + build_stats(cfg) + html[m.end():])
        return html, True
    # dijital-donusum gibi kendi hero duzeni olan sayfalar: mevcut serit korunur
    return html, False


def _close_div(html, start):
    depth = 0
    for m in re.finditer(r'</?div\b', html[start:]):
        if m.group(0).startswith('</'):
            depth -= 1
            if depth == 0:
                return start + m.start()
        else:
            depth += 1
    return -1


def _rank(href):
    if href.endswith('-collection'):
        return 0
    if href in AUTODESK:
        return 1
    return 2


def reorder_products(html):
    """Urun izgaralarinda koleksiyonlari, ardindan Autodesk urunlerini basa alir.

    Sadece urun izgaralarina dokunur; yalnizca endustri (sektor-*) karti
    iceren izgaralar oldugu gibi birakilir.
    """
    moved = 0
    pos = 0
    out = []
    for gm in GRID_RE.finditer(html):
        if gm.start() < pos:
            continue
        gs, ge = gm.end(), _close_div(html, gm.start())
        if ge < 0:
            continue
        block = html[gs:ge]
        cards = CARD_RE.findall(block)
        hrefs = [m.group('href') for m in CARD_RE.finditer(block)]
        if len(hrefs) < 2 or all(h.startswith('sektor-') for h in hrefs):
            continue
        full = [m.group(0) for m in CARD_RE.finditer(block)]
        order = sorted(range(len(full)), key=lambda i: (_rank(hrefs[i]), i))
        if order == list(range(len(full))):
            continue
        new_cards = [full[i] for i in order]
        parts, k, p = [], 0, 0
        for m in CARD_RE.finditer(block):
            parts.append(block[p:m.start()])
            parts.append(new_cards[k])
            k += 1
            p = m.end()
        parts.append(block[p:])
        out.append(html[pos:gs])
        out.append("".join(parts))
        pos = ge
        moved += 1
    out.append(html[pos:])
    return "".join(out), moved


def insert_before(html, needle, block):
    i = html.find(needle)
    if i < 0:
        return html, False
    return html[:i] + block + "\n" + html[i:], True


HERO_TEXT_DIV = re.compile(r'<div style="max-width:(?:720|680)px;">')


def apply_hero_art(html, cfg):
    """Hero'yu iki sutuna cevirip sag sutuna illustrasyonu koyar."""
    hs = html.find('<section class="hero"')
    he = html.find('</section>', hs)
    hero = html[hs:he]
    if 'cz-hero-grid' in hero:                       # zaten sarilmis: sadece gorseli tazele
        new_hero = re.sub(r'<div class="cz-art cz-art-hero">.*?</div>',
                          build_hero_art(cfg), hero, flags=re.S)
        return html[:hs] + new_hero + html[he:], 'hero-art(guncel)'
    m = HERO_TEXT_DIV.search(hero)
    if not m:
        return html, 'hero-art(atlandi)'
    close = _close_div(hero, m.start())
    if close < 0:
        return html, 'hero-art(atlandi)'
    inner = hero[m.end():close]
    new_hero = (hero[:m.start()]
                + '<div class="cz-hero-grid">\n      <div class="cz-hero-text">'
                + inner + '</div>\n      ' + build_hero_art(cfg) + '\n    </div>'
                + hero[close + len('</div>'):])
    return html[:hs] + new_hero + html[he:], 'hero-art'


# --------------------------------------------------------------------------
# bolum siralamasi
# --------------------------------------------------------------------------
SECTION_SPLIT = re.compile(r'(?m)^(?:<!-- cz-\w+ -->\n)?<section')

# Onur'un 2026-08-03 notu: Ilgili Urunler "Neler Yapabiliriz"den hemen sonra,
# Cadbim Farki seridi SSS'ten sonra gelir.
ORDER = ['hero', 'intro', 'yetenek', 'kitle', 'urun', 'endustri', 'other',
         'marka', 'enrich', 'sss', 'fark', 'blog']


def classify(chunk):
    if '<section class="hero"' in chunk:
        return 'hero'
    if '<!-- cz-intro -->' in chunk:
        return 'intro'
    if '<!-- cz-brands -->' in chunk:
        return 'marka'
    if '<!-- cz-faq -->' in chunk:
        return 'sss'
    if '<!-- cz-fark -->' in chunk or 'data-enrich-brand' in chunk:
        return 'fark'
    if '<!-- cz-kitle -->' in chunk:
        return 'kitle'
    if 'id="blog-related-section"' in chunk:
        return 'blog'
    if u'Neler Yapabiliriz' in chunk:
        return 'yetenek'
    if PRODUCTS_HEAD in chunk or ALT_HEAD in chunk:
        return 'urun'
    if u'hangi endüstrilerde kullanılıyor' in chunk:
        return 'endustri'
    if 'data-enrich' in chunk:
        return 'enrich'
    return 'other'


def reorder_sections(html):
    """Govdeyi bolumlere ayirip ORDER dizisine gore yeniden dizer."""
    bs = html.index('</nav>') + len('</nav>')
    be = html.index('<footer')
    body = html[bs:be]
    starts = [m.start() for m in SECTION_SPLIT.finditer(body)]
    if not starts:
        return html, False
    lead = body[:starts[0]]
    chunks = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(body)
        chunks.append(body[s:e])
    buckets = {k: [] for k in ORDER}
    for c in chunks:
        buckets[classify(c)].append(c)
    new_body = lead + "".join("".join(buckets[k]) for k in ORDER)
    if new_body == body:
        return html, False
    return html[:bs] + new_body + html[be:], True


def add_faq_jsonld(html, cfg):
    """FAQPage nesnesini mevcut @graph dizisine ekler."""
    if '"@type": "FAQPage"' in html:
        html = re.sub(r',\n  \{\n   "@type": "FAQPage".*?\n  \}(?=\n \])',
                      '', html, flags=re.S)
    marker = '\n ]\n}\n</script>'
    i = html.find(marker)
    if i < 0:
        return html, False
    body = build_faq_jsonld(cfg)
    body = "\n".join("  " + ln for ln in body.split("\n"))
    return html[:i] + ",\n" + body + html[i:], True


# --------------------------------------------------------------------------
def process(key, cfg):
    path = os.path.join(ROOT, 'cadbim_%s.html' % key)
    html = io.open(path, encoding='utf-8').read()
    orig = html
    log = []

    html, ok = apply_hero(html, cfg)
    log.append('hero' if ok else 'hero(atlandi)')

    # 2. tanitim bolumu -- hero'dan hemen sonra
    html = strip_block(html, M_INTRO)
    hero_end = html.find('</section>', html.find('<section class="hero"')) + len('</section>')
    html = html[:hero_end] + "\n" + build_intro(cfg) + html[hero_end:]
    log.append('intro')

    # 3. marka seridi -- urun bolumunun oncesine
    html = strip_block(html, M_BRANDS)
    pi = html.find(PRODUCTS_HEAD)
    if pi < 0:
        pi = html.find(ALT_HEAD)
    if pi > 0:
        si = html.rfind('<section', 0, pi)
        # marka seridi (koyu bant) hemen ustune geldigi icin urun bolumunun
        # padding-top:0 degeri basligi banda yapistiriyordu
        se = html.index('>', si) + 1
        head = html[si:se].replace('padding-top:0;', 'padding-top:56px;')
        html = html[:si] + build_brands(cfg) + "\n" + head + html[se:]
        log.append('markalar')
    else:
        # urun bolumu yoksa blog oncesine koy
        html, ok = insert_before(html, '<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">',
                                 build_brands(cfg))
        log.append('markalar' if ok else 'markalar(atlandi)')

    # 4. koleksiyonlari basa al
    html, n = reorder_products(html)
    log.append('koleksiyon-ilk(%d)' % n)

    # 5. SSS -- blog bolumunun oncesine
    html = strip_block(html, M_FAQ)
    html, ok = insert_before(
        html, '<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">',
        build_faq(cfg))
    log.append('sss' if ok else 'sss(atlandi)')

    # 6. Cadbim Farki seridi -- eskisi (varsa) atilir, 16 sayfada ayni surum kurulur
    html = strip_block(html, M_FARK)
    html = re.sub(r'<section data-enrich-brand.*?</section>\n*', '', html, flags=re.S)
    html, ok = insert_before(
        html, '<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">',
        build_fark(cfg))
    log.append('cadbim-farki' if ok else 'cadbim-farki(atlandi)')

    # 7. gorsel hero'ya tasinir
    html, msg = apply_hero_art(html, cfg)
    log.append(msg)

    # 8. bolum sirasi
    html, ok = reorder_sections(html)
    log.append('sira' if ok else 'sira(degismedi)')

    html, ok = add_faq_jsonld(html, cfg)
    log.append('faq-jsonld' if ok else 'faq-jsonld(atlandi)')

    if html != orig:
        io.open(path, 'w', encoding='utf-8', newline='').write(html)
    return log


if __name__ == '__main__':
    for key in COZUM:
        print('%-22s %s' % (key, ' · '.join(process(key, COZUM[key]))))
