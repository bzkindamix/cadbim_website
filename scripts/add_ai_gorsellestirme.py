# -*- coding: utf-8 -*-
"""AI Destekli Gorsellestirme cozum sayfasini kurar ve siteye baglar.

Kaynak: chaos.com/ai-visualization (Veras, AI Material Generator, AI Image
Enhancer, AI Upscaler, AI Mood Match, Chaos Assistant, Glyph, Responsible AI),
lumion.com (Cloud AI Material Generator), Adobe Firefly. Metinler kopyalanmadi;
olgular alinip CADBIM kurumsal Turkcesiyle yeniden yazildi.

add_bim_icerik_sayfasi.py ile ayni adimlari izler; sira onemlidir (nav once).
"""
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'ai-gorsellestirme'
FILE = 'cadbim_ai_gorsellestirme.html'
TITLE = u'AI Destekli Görselleştirme'
NAVLBL = u'AI Destekli Görselleştirme'
ACCENT = '#c084fc'
# menude bu ogeden SONRA yer alir
AFTER = ('gorsellestirme', u'Görselleştirme & Render')

CARDS = [
    ('ti-wand', u'Konseptten Görsele: Veras',
     u'2B görsel, eskiz veya 3B modelden metin istemiyle gerçekçi görselleştirme. '
     u'Enscape, V-Ray ve Corona ile bütünleşir; SketchUp, Rhino ve Revit içinde çalışır.'),
    ('ti-texture', u'Fotoğraftan PBR Malzeme',
     u'AI Material Generator ile herhangi bir fotoğraf dikişsiz, render\'a hazır '
     u'malzemeye dönüşür. Chaos Cosmos kapsamında; Enscape, V-Ray ve Corona kullanıcılarına açık.'),
    ('ti-arrows-maximize', u'Çözünürlük Yükseltme (16K)',
     u'AI Upscaler ile render çıktısı tek tıkla 2x veya 4x büyütülür; yeniden render '
     u'almadan keskin sonuç, saatlerce render süresinden tasarruf.'),
    ('ti-sparkles', u'Detay ve Cila',
     u'AI Image Enhancer bitki, insan ve büyük yüzeylere (asfalt, tuğla, beton) '
     u'gerçekçilik katar; kir, yıpranma ve yaşlanma denetimli biçimde eklenir.'),
    ('ti-sun-moon', u'Referans Fotoğraftan Atmosfer',
     u'AI Mood Match referans görselin ışık koşullarını çözümleyip V-Ray Sun & Sky '
     u'veya görsel tabanlı aydınlatmayı buna göre kurar.'),
    ('ti-shield-check', u'Kurumsal Kullanım Politikası',
     u'Hangi işte hangi aracın kullanılacağı, çıktı sahipliği, müşteri gizliliği ve '
     u'lisans koşulları yazılı bir politikaya bağlanır — teslimde sürpriz olmaz.'),
]

PRODUCTS = [
    ('me-collection', 'me-collection.svg', u'M&E Collection',
     u'3ds Max, Maya ve Arnold ile üretim ölçeğinde görselleştirme ve animasyon altyapısı.'),
    ('autodesk-forma', 'forma.svg', u'Autodesk Forma',
     u'Erken aşama kütle, güneşlenme ve rüzgâr analizleriyle veri destekli tasarım kararı.'),
    ('fusion', 'fusion.svg', u'Autodesk Fusion',
     u'Jeneratif tasarım: yük ve kısıtlardan üretilebilir alternatiflerin otomatik türetilmesi.'),
    ('veras', None, u'Chaos Veras',
     u'Metin istemiyle AI görselleştirme; tasarım yazılımınızın içinden çalışır.'),
    ('cosmos', 'cosmos.svg', u'Chaos Cosmos',
     u'Varlık ve malzeme kütüphanesi; AI Material Generator bu kapsamda sunulur.'),
    ('chaos', None, u'Chaos V-Ray & Enscape',
     u'AI araçlarının bağlandığı fiziksel tabanlı render ve gerçek zamanlı görselleştirme.'),
    ('corona', 'corona.svg', u'Chaos Corona',
     u'AI Material Generator ve gelişmiş malzeme/atmosfer araçlarıyla mimari görselleştirme.'),
    ('lumion-cloud', 'lumion-cloud.png', u'Lumion Cloud',
     u'AI Material Generator ve görsel iş birliği ortamı; tüm Lumion planlarına dahil.'),
    ('firefly', 'firefly.svg', u'Adobe Firefly',
     u'Ticari kullanıma uygun üretken görsel araçları; sunum ve pazarlama görselleri.'),
    ('hp-z-workstation', None, u'HP Z Workstation',
     u'GPU belleği ve çekirdek sayısı AI ve render adımlarının süresini doğrudan belirler.'),
]

INDUSTRIES = [
    ('sektor-mimari', 'ti-building-arch', u'Mimarlık',
     u'Konsept keşfi, sunum görseli ve müşteri onay sürecinin hızlandırılması.'),
    ('sektor-icmimarlik', 'ti-armchair', u'İç Mimarlık & Tasarım',
     u'Malzeme ve atmosfer denemelerinin fotoğraftan üretilerek çoğaltılması.'),
    ('sektor-medya', 'ti-movie', u'Medya & Eğlence',
     u'Ön görselleştirme, kavramsal sanat ve son işlem adımlarında hız kazancı.'),
    ('sektor-otomotiv', 'ti-car', u'Otomotiv',
     u'Renk, kaplama ve ortam varyantlarının sunum öncesi hızla denenmesi.'),
]


# Konuyla ilgili gercek Cadbim YouTube videolari -- Autodesk once (marka sirasi kurali)
VIDEOS = [
    ('3tX5-SbxAoc', u'Autodesk Forma Board — Generate AI Image ile konsept görseller',
     u'Erken aşamada kütle modelinden yapay zekâ destekli konsept görsel üretimi.'),
    ('-3AgMlsmg1Y', u'Yapay zekâ destekli tasarım ve imalat iş ortağınız: Autodesk AI',
     u'Autodesk portföyünde yapay zekânın tasarım ve üretim akışına nereden girdiği.'),
    ('6Ru4ppNiQR4', u'Adobe Firefly — Yapı Referansı',
     u'Referans görselin yapısını koruyarak üretken görsel türetme.'),
    ('glOclQpjS-k', u'Creative Cloud + AI: yaratıcı süreçlerin yeni standardı',
     u'Üretken yapay zekânın Creative Cloud iş akışına gömülü hâli.'),
    ('8jJVF0tt5P8', u'Adobe — üretken yapay zekâ ile hızlı ve yenilikçi iş akışları',
     u'Varyant üretimi ve tekrar eden işlerin kısaltılması.'),
]


def video_section():
    items = []
    for vid, title, desc in VIDEOS:
        t = title.replace('"', '&quot;')
        items.append(u'''    <div class="cz-vid">
      <div class="cz-vid-thumb">
        <a class="yt-lite" href="https://www.youtube.com/watch?v=%s" target="_blank"
           rel="noopener" data-yt="%s" data-title="%s"
           aria-label="Videoyu oynat: %s"><img src="https://i.ytimg.com/vi/%s/hqdefault.jpg"
           alt="" width="480" height="360" loading="lazy" decoding="async"><span
           class="yt-lite-btn" aria-hidden="true"></span></a>
      </div>
      <div class="cz-vid-body">
        <h3>%s</h3>
        <p>%s</p>
      </div>
    </div>
''' % (vid, vid, t, t, vid, title, desc))
    return (u'''<!-- cz-video -->
<section class="section cz-sec" style="--cz:%s;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Video Eğitimler</div>
    <div class="stitle">Kendi Kanalımızdan Konu Anlatımları</div>
    <p class="ssub">Cadbim Teknik Destek kanalında yayınladığımız, tasarım ve
      görselleştirmede yapay zekâ kullanımına dair oturumlar.</p>
  </div>
  <div class="cz-vids">
%s  </div>
  <div class="cz-faq-cta" style="margin-top:22px;">
    <span>Tüm teknik destek videolarımız YouTube kanalımızda.</span>
    <a href="https://www.youtube.com/c/CadbimTeknikDestek" target="_blank" rel="noopener"
       class="btn-g">YouTube Kanalımız <i class="ti ti-brand-youtube"></i></a>
  </div>
</section>
<!-- /cz-video -->
''' % (ACCENT, "".join(items)))


def card(icon, title, desc):
    return (u'''    <div class="card">
      <div class="card-icon"><i class="ti %s"></i></div>
      <h3>%s</h3>
      <p>%s</p>
    </div>
''' % (icon, title, desc))


def product_card(href, logo, title, desc):
    if logo:
        ic = (u'<div class="card-icon" style="background:rgba(255,255,255,.07);">'
              u'<img width="965" height="1024" src="assets/logos/products/%s" alt="" '
              u'style="width:32px;height:32px;object-fit:contain;" loading="lazy" '
              u'decoding="async"></div>' % logo)
    else:
        ic = (u'<div class="card-icon" style="background:rgba(192,132,252,.14);">'
              u'<i class="ti ti-cube"></i></div>')
    return (u'''    <a href="%s" class="card">
      %s
      <h3>%s</h3>
      <p>%s</p>
    </a>
''' % (href, ic, title, desc))


def industry_card(href, icon, title, desc):
    return (u'''    <a href="%s" class="card">
      <div class="card-icon" style="background:rgba(0,200,240,.12);"><i class="ti %s"></i></div>
      <h3>%s</h3>
      <p>%s</p>
    </a>
''' % (href, icon, title, desc))


def build_page():
    src = io.open(os.path.join(ROOT, 'cadbim_gorsellestirme.html'), encoding='utf-8').read()
    head_end = src.index('</head>')
    nav_end = src.index('</nav>') + len('</nav>')
    blog_start = src.index('<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">')
    head = src[:head_end]
    nav = src[head_end:nav_end]
    tail = re.sub(r'data-topic="[^"]*"', u'data-topic="Görselleştirme"', src[blog_start:], count=1)

    desc = (u'AI destekli görselleştirme: Chaos Veras ile metin isteminden render, '
            u'fotoğraftan PBR malzeme, 16K çözünürlük yükseltme, AI Mood Match ve '
            u'kurumsal kullanım politikası. Cadbim — Autodesk Gold Partner.')
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="%s">' % desc, head, count=1)
    head = re.sub(r'<title>.*?</title>',
                  u'<title>%s — Veras, AI Malzeme & Upscale | Cadbim</title>' % TITLE,
                  head, count=1, flags=re.S)
    head = head.replace('https://www.cadbim.com.tr/gorsellestirme',
                        'https://www.cadbim.com.tr/' + SLUG)
    head = head.replace('assets/og/cadbim_gorsellestirme.png',
                        'assets/og/cadbim_ai_gorsellestirme.png')
    head = re.sub(r'"name": "[^"]*"', '"name": "%s"' % TITLE, head)
    head = re.sub(r'"description": "[^"]*"', '"description": "%s"' % desc, head)
    head = re.sub(r',\n  \{\n   "@type": "FAQPage".*?\n  \}(?=\n \])', '', head, flags=re.S)
    head = re.sub(r'(<meta (?:property="og:|name="twitter:)title" content=")[^"]*(")',
                  r'\g<1>%s — Cadbim\g<2>' % TITLE, head)

    nav = re.sub(r'<a class="active" href="([a-z0-9\-]+)">', r'<a href="\1">', nav)
    nav = re.sub(r'<a(?: class="active")? href="%s">[^<]*</a>\s*' % SLUG, '', nav)
    nav = nav.replace(
        '<a href="%s">%s</a>' % AFTER,
        '<a href="%s">%s</a>\n            <a class="active" href="%s">%s</a>'
        % (AFTER[0], AFTER[1], SLUG, NAVLBL), 1)

    body = u'''
<section class="hero">
  <div class="hero-bg" style="background:radial-gradient(ellipse 70%% 50%% at 20%% 0%%,rgba(192,132,252,0.1) 0%%,transparent 60%%);"></div>
  <div class="hero-grid"></div>
  <div style="position:relative;z-index:1;">
    <div class="crumb"><a href="/">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="cozumler">Çözümler</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">AI Destekli Görselleştirme</span></div>
    <div style="max-width:720px;">
      <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:%(accent)s;margin-bottom:12px;">AI Destekli Görselleştirme</div>
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
        <div style="width:52px;height:52px;border-radius:12px;background:rgba(192,132,252,0.12);display:flex;align-items:center;justify-content:center;border:.5px solid %(accent)s40;">
          <i class="ti ti-wand" style="font-size:24px;color:%(accent)s;"></i>
        </div>
        <h1 style="font-family:var(--fd);font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;line-height:1.1;color:var(--w);">Karar Sizde Kalsın, İşçiliği AI Yapsın</h1>
      </div>
      <p style="font-size:16px;color:var(--w50);line-height:1.75;margin-bottom:32px;max-width:600px;">AI destekli görselleştirme.</p>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="sh"><div class="slabel">Çözüm Kapsamı</div><div class="stitle">Neler Yapabiliriz?</div></div>
  <div class="grid g3">
%(cards)s  </div>
</section>
<section class="section" style="padding-top:56px;">
  <div class="sh">
    <div class="slabel">İlgili Ürünler</div>
    <div class="stitle">Bu Çözümde Kullanılan Cadbim Ürünleri</div>
    <p class="ssub">İlgili yazılım ve donanım sayfaları</p>
  </div>
  <div class="grid g3" style="margin-top:0;">
%(products)s  </div>
  <div class="sh" style="margin-top:40px;">
    <div class="slabel">Endüstriler</div>
    <div class="stitle">Bu Çözüm Hangi Endüstrilerde Kullanılıyor</div>
    <p class="ssub">İlgili endüstri sayfalarını inceleyin</p>
  </div>
  <div class="grid g3" style="margin-top:0;">
%(industries)s  </div>
</section>
%(videos)s''' % dict(accent=ACCENT,
           cards="".join(card(*c) for c in CARDS),
           products="".join(product_card(*p) for p in PRODUCTS),
           industries="".join(industry_card(*i) for i in INDUSTRIES),
           videos=video_section())

    out = head + nav + body + tail
    io.open(os.path.join(ROOT, FILE), 'w', encoding='utf-8', newline='').write(out)
    return len(out)


def add_nav_link():
    n = 0
    for f in glob.glob(os.path.join(ROOT, '*.html')) + glob.glob(os.path.join(ROOT, 'post', '*.html')):
        s = io.open(f, encoding='utf-8').read()
        if os.path.basename(f) == FILE or 'nav-mega' not in s:
            continue
        navpart = s[:s.index('</nav>')]
        if re.search(r'href="(?:\.\./)?%s"' % SLUG, navpart):
            continue
        pre = '../' if os.sep + 'post' + os.sep in f else ''
        old = '<a href="%s%s">%s</a>' % (pre, AFTER[0], AFTER[1])
        old_a = '<a class="active" href="%s%s">%s</a>' % (pre, AFTER[0], AFTER[1])
        target = old_a if old_a in navpart else old
        if target not in navpart:
            continue
        navpart = navpart.replace(
            target, target + '\n            <a href="%s%s">%s</a>' % (pre, SLUG, NAVLBL), 1)
        io.open(f, 'w', encoding='utf-8', newline='').write(navpart + s[s.index('</nav>'):])
        n += 1
    return n


def add_hub_card():
    p = os.path.join(ROOT, 'cadbim_cozumler.html')
    s = io.open(p, encoding='utf-8').read()
    if 'href="%s" class="sol-card"' % SLUG in s:
        return False
    html = u'''
    <a href="%s" class="sol-card">
      <div class="sol-icon" style="background:rgba(192,132,252,0.12);color:%s;"><i class="ti ti-wand"></i></div>
      <h3>AI Destekli Görselleştirme</h3>
      <p>Metin isteminden konsept görsel, fotoğraftan PBR malzeme, 16K çözünürlük yükseltme — yaratıcı karar sizde, işçilik yapay zekâda.</p>
      <div class="sol-meta">
        <span class="sol-tag">Veras</span><span class="sol-tag">AI Material</span><span class="sol-tag">AI Upscaler</span><span class="sol-tag">Firefly</span>
      </div>
      <div class="sol-arrow">Detaylı İncele <i class="ti ti-arrow-right"></i></div>
    </a>
''' % (SLUG, ACCENT)
    m = re.search(r'<a href="gorsellestirme" class="sol-card"[^>]*>.*?</a>\n', s, re.S)
    assert m, 'gorsellestirme karti bulunamadi'
    s = s[:m.end()] + html + s[m.end():]
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


def add_to_industry_map():
    p = os.path.join(ROOT, 'cadbim_endustriler.html')
    s = io.open(p, encoding='utf-8').read()
    block = (u'<a href="%s" class="ind-sol-block"><div class="ind-sol-icon" '
             u'style="background:rgba(192,132,252,0.12);color:%s;">'
             u'<i class="ti ti-wand"></i></div><h4>AI Destekli Görselleştirme</h4>'
             u'<div class="ind-sol-products"><span>Veras</span><span>AI Material</span>'
             u'<span>AI Upscaler</span></div></a>' % (SLUG, ACCENT))
    added = []
    for ind in ('mimari', 'icmimarlik', 'medya', 'otomotiv'):
        m = re.search(r'(<div class="ind-panel[^"]*" data-ind="%s">)(.*?)(\n  </div>)' % ind, s, re.S)
        if not m or 'href="%s"' % SLUG in m.group(2):
            continue
        a = re.search(r'<a href="gorsellestirme" class="ind-sol-block".*?</a>', m.group(2), re.S)
        pos = a.end() if a else 0
        body = m.group(2)[:pos] + '\n    ' + block + m.group(2)[pos:]
        s = s[:m.start(2)] + body + s[m.end(2):]
        added.append(ind)
    if added:
        io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return added


def add_url_map():
    p = os.path.join(ROOT, '404.html')
    s = io.open(p, encoding='utf-8').read()
    if '"%s"' % SLUG in s:
        return False
    old = '"gorsellestirme":"cadbim_gorsellestirme.html"'
    assert old in s
    s = s.replace(old, old + ',"%s":"%s"' % (SLUG, FILE), 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


def add_sitemap():
    p = os.path.join(ROOT, 'sitemap.xml')
    s = io.open(p, encoding='utf-8').read()
    url = 'https://www.cadbim.com.tr/' + SLUG
    if url + '<' in s:
        return False
    m = re.search(r'<url>\s*<loc>https://www\.cadbim\.com\.tr/gorsellestirme</loc>.*?</url>', s, re.S)
    assert m
    entry = m.group(0).replace('/gorsellestirme</loc>', '/' + SLUG + '</loc>')
    s = s[:m.end()] + '\n' + entry + s[m.end():]
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


if __name__ == '__main__':
    print('sayfa            : %d bayt' % build_page())
    print('nav baglantisi   : %d dosya' % add_nav_link())
    print('hub karti        : %s' % add_hub_card())
    print('endustri haritasi: %s' % add_to_industry_map())
    print('URL haritasi     : %s' % add_url_map())
    print('sitemap          : %s' % add_sitemap())
