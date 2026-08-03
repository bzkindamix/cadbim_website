# -*- coding: utf-8 -*-
"""BIM Icerik / Obje Uretimi cozum sayfasini kurar ve siteye baglar.

Yapilanlar:
  1. cadbim_bim.html kabugundan cadbim_bim_icerik_uretimi.html uretir
     (SEO, hero, yetenek kartlari, urunler, endustriler, kurulmus video bolumu)
  2. Cozumler merkezine kart ekler
  3. Ust menudeki Cozumler mega menusune baglanti ekler -- TUM sayfalarda
  4. cadbim_endustriler.html endustri haritasina ekler
  5. 404.html URL haritasina ve sitemap.xml'e ekler

Betik yeniden calistirilabilir; var olan kayitlari tekrar eklemez.
Ardindan scripts/enrich_cozum_pages.py ve scripts/sync_endustri_haritasi.py
calistirilmalidir (tanitim / marka / SSS / Cadbim Farki bloklari ve filtre).
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'bim-icerik-uretimi'
FILE = 'cadbim_bim_icerik_uretimi.html'
TITLE = u'BIM İçerik & Obje Üretimi'
NAVLBL = u'BIM İçerik & Obje Üretimi'
ACCENT = '#818cf8'

# Onur'un belirttigi, konuyla ilgili gercek Cadbim YouTube videolari
VIDEOS = [
    ('8LJRgGyiv94', u'Üretim Sektörü için BIM (BIM Objects)',
     u'Yapı ürünü üreticilerinin BIM ekosistemine nasıl dahil olduğunu anlatan oturum.'),
    ('YpCkINbyHG8', u'Revit ile sıfırdan Family yaratmak ve mevcut Family dosyalarını düzenlemek',
     u'Aile oluşturmanın temelleri ve var olan ailelerin düzenlenmesi.'),
    ('j93XtQCeppY', u'Revit: Yeni başlayanlar için Family oluşturma',
     u'İlk ailenizi kurarken izlenecek adımlar.'),
    ('_Ud17NbY2Nk', u'Revit projesini Family olarak kaydetme (.rvt → .rfa)',
     u'Proje olarak modellenmiş bir ürünü yeniden kullanılabilir aileye çevirme.'),
    ('bDl7kFVq70A', u'InfraWorks: Parametrik içerik oluşturma',
     u'Inventor bileşenleriyle altyapı kitaplıklarını genişletme.'),
]

CARDS = [
    ('ti-box-multiple', u'Revit Aile (Family) Üretimi',
     u'Doğru kategoride, parametrik ve tip kataloglu aileler; ana hatlar, referans '
     u'düzlemleri ve kısıtlar en baştan sağlam kurulur.'),
    ('ti-transform', u'CAD → BIM Dönüşümü',
     u'Inventor, SolidWorks veya STEP verisinin sadeleştirilmesi; üretim detayı '
     u'atılırken tasarım için gereken geometri korunur.'),
    ('ti-table-options', u'Parametre & Veri Zenginleştirme',
     u'Paylaşılan parametreler, üretici kodu, performans değerleri ve malzeme '
     u'bilgisi; metraj ve şartname doğrudan modelden alınır.'),
    ('ti-plug-connected', u'MEP Bağlantı Noktaları',
     u'Boru, kanal ve elektrik bağlantı noktaları tanımlanır; obje sistem '
     u'içinde doğru davranır, bağlantı analizine girer.'),
    ('ti-library', u'Kütüphane & Şablon Yönetimi',
     u'Ofis şablonu, adlandırma standardı ve onaylı aile kütüphanesinin tek '
     u'kaynaktan yönetimi; sürüm ve güncelleme düzeni.'),
    ('ti-file-export', u'Yayınlama: .rfa ve IFC',
     u'Revit ailesinin yanında IFC çıktısı; Revit kullanmayan paydaşlar da '
     u'ürününüzü kendi ortamında kullanır.'),
]

PRODUCTS = [
    ('aec-collection', 'aec-collection.svg', u'AEC Collection',
     u'Revit, AutoCAD, Navisworks ve Forma araçlarını bir arada sunan yapı sektörü koleksiyonu.'),
    ('pdm-collection', 'pdm-collection.svg', u'PD&M Collection',
     u'Inventor ve Vault ile üretim tarafındaki CAD verisinin kaynağı; CAD→BIM akışının başlangıcı.'),
    ('revit', 'revit.svg', u'Autodesk Revit',
     u'BIM ailelerinin üretildiği ve kullanıldığı ana ortam; aile düzenleyici ve tip kataloğu.'),
    ('inventor', 'inventor.svg', u'Autodesk Inventor',
     u'Üretim CAD modelinin kaynağı; sadeleştirme ve Revit ile karşılıklı çalışma.'),
    ('vault-pdm', 'vault-pdm.svg', u'Vault PDM',
     u'Aile kütüphanesinin sürüm ve revizyon kontrolüyle merkezî yönetimi.'),
    ('autodesk-docs', 'autodesk-docs.svg', u'Autodesk Docs',
     u'Onaylı kütüphanenin proje ekipleri ve dış paydaşlarla paylaşımı.'),
    ('navisworks', 'navisworks.svg', u'Navisworks',
     u'Üretilen objelerin proje bağlamında çakışma ve koordinasyon denetimi.'),
    ('yazilim-gelistirme', None, u'Yazılım Geliştirme',
     u'Toplu aile üretimi, parametre aktarımı ve katalog otomasyonu için özel araçlar.'),
]

INDUSTRIES = [
    ('sektor-mimari', 'ti-building-arch', u'Mimarlık',
     u'Ofis kütüphanesinin standarda oturtulması ve üretici içeriğinin denetimi.'),
    ('sektor-insaat', 'ti-crane', u'İnşaat & Altyapı',
     u'Şartnameye giren ürün verisinin model üzerinden doğrulanması.'),
    ('sektor-makine', 'ti-settings', u'Makine & Üretim',
     u'Yapı ürünü üreticileri için ürün gamının BIM objesine dönüştürülmesi.'),
]


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
        ic = (u'<div class="card-icon" style="background:rgba(0,200,240,.12);">'
              u'<i class="ti ti-code"></i></div>')
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
    <div class="stitle">Kendi kanalımızdan konu anlatımları</div>
    <p class="ssub">Cadbim Teknik Destek kanalında yayınladığımız, BIM içerik ve
      aile üretimiyle ilgili oturumlar.</p>
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


# --------------------------------------------------------------------------
def build_page():
    src = io.open(os.path.join(ROOT, 'cadbim_bim.html'), encoding='utf-8').read()

    # --- kabuk: head + nav + footer korunur, govde yeniden yazilir
    head_end = src.index('</head>')
    nav_end = src.index('</nav>') + len('</nav>')
    foot_start = src.index('<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">')
    head = src[:head_end]
    nav = src[head_end:nav_end]
    tail = re.sub(r'data-topic="[^"]*"', 'data-topic="Revit"', src[foot_start:], count=1)

    # SEO / meta / JSON-LD
    desc = (u'BIM içerik ve obje üretimi: Revit aile (family) üretimi, CAD verisinin '
            u'BIM objesine dönüştürülmesi, parametre ve veri standardı, .rfa ve IFC '
            u'yayınlama, kütüphane yönetimi. Cadbim — Autodesk Gold Partner.')
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="%s">' % desc, head, count=1)
    head = re.sub(r'<title>.*?</title>',
                  u'<title>%s — Revit Family & BIM Objesi | Cadbim</title>' % TITLE,
                  head, count=1, flags=re.S)
    head = head.replace('https://www.cadbim.com.tr/bim', 'https://www.cadbim.com.tr/' + SLUG)
    head = head.replace('assets/og/cadbim_bim.png', 'assets/og/cadbim_bim_icerik_uretimi.png')
    for a, b in ((u'BIM — Yapı Bilgi Modellemesi', TITLE),
                 (u'BIM — Cadbim', TITLE + u' — Cadbim')):
        head = head.replace(a, b)
    head = re.sub(r'"name": "BIM"', '"name": "%s"' % TITLE, head)
    # onceki sayfadan gelen FAQPage / aciklama metinleri temizlenir; enrich yeniden yazar
    head = re.sub(r',\n  \{\n   "@type": "FAQPage".*?\n  \}(?=\n \])', '', head, flags=re.S)
    head = re.sub(r'"description": "[^"]*BIM[^"]*"', '"description": "%s"' % desc, head)

    # nav: BIM pasif, bu sayfa aktif
    nav = nav.replace('<a class="active" href="bim">BIM</a>', '<a href="bim">BIM</a>')
    nav = re.sub(r'<a(?: class="active")? href="%s">[^<]*</a>\s*' % SLUG, '', nav)
    nav = nav.replace(
        '<a href="bim">BIM</a>',
        '<a href="bim">BIM</a>\n            '
        '<a class="active" href="%s">%s</a>' % (SLUG, NAVLBL), 1)

    cfg = dict(slug=SLUG, title=TITLE, accent=ACCENT)
    body = u'''
<section class="hero">
  <div class="hero-bg" style="background:radial-gradient(ellipse 70%% 50%% at 20%% 0%%,rgba(129,140,248,0.1) 0%%,transparent 60%%);"></div>
  <div class="hero-grid"></div>
  <div style="position:relative;z-index:1;">
    <div class="crumb"><a href="/">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="cozumler">Çözümler</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">BIM İçerik & Obje Üretimi</span></div>
    <div style="max-width:720px;">
      <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:%(accent)s;margin-bottom:12px;">BIM İçerik & Obje Üretimi</div>
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
        <div style="width:52px;height:52px;border-radius:12px;background:rgba(129,140,248,0.12);display:flex;align-items:center;justify-content:center;border:.5px solid %(accent)s40;">
          <i class="ti ti-box-multiple" style="font-size:24px;color:%(accent)s;"></i>
        </div>
        <h1 style="font-family:var(--fd);font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;line-height:1.1;color:var(--w);">Ürününüzü Mimarın Modeline Sokun</h1>
      </div>
      <p style="font-size:16px;color:var(--w50);line-height:1.75;margin-bottom:32px;max-width:600px;">BIM içerik ve obje üretimi.</p>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="sh"><div class="slabel">Çözüm Kapsamı</div><div class="stitle">Neler Yapabiliriz?</div></div>
  <div class="grid g3">
%(cards)s  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="sh">
    <div class="slabel">İlgili Ürünler</div>
    <div class="stitle">Bu çözümde kullanılan Cadbim ürünleri</div>
    <p class="ssub">İlgili yazılım ve donanım sayfaları</p>
  </div>
  <div class="grid g3" style="margin-top:0;">
%(products)s  </div>
  <div class="sh" style="margin-top:40px;">
    <div class="slabel">Endüstriler</div>
    <div class="stitle">Bu çözüm hangi endüstrilerde kullanılıyor</div>
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

    out = head + '</head>' + nav[nav.index('>') + 1:] if False else (head + nav + body + tail)
    io.open(os.path.join(ROOT, FILE), 'w', encoding='utf-8', newline='').write(out)
    return len(out)


# --------------------------------------------------------------------------
def add_nav_link():
    """Tum sayfalardaki Cozumler mega menusune baglanti ekler."""
    old = u'<a href="bim">BIM</a>'
    new = old + u'\n            <a href="%s">%s</a>' % (SLUG, NAVLBL)
    old_active = u'<a class="active" href="bim">BIM</a>'
    new_active = old_active + u'\n            <a href="%s">%s</a>' % (SLUG, NAVLBL)
    n = 0
    import glob
    for f in glob.glob(os.path.join(ROOT, '*.html')) + glob.glob(os.path.join(ROOT, 'post', '*.html')):
        s = io.open(f, encoding='utf-8').read()
        # sayfanin kendisinde baglanti build_page tarafindan zaten aktif eklenir.
        # Kontrol SADECE nav bolumunde yapilir; govdedeki kart/harita gecisleri
        # nav'in atlanmasina yol acmasin.
        if os.path.basename(f) == FILE or 'nav-mega' not in s:
            continue
        navpart = s[:s.index('</nav>')]
        if re.search(r'href="(?:\.\./)?%s"' % SLUG, navpart):
            continue
        o = s
        if old_active in s:
            s = s.replace(old_active, new_active, 1)
        elif old in s:
            s = s.replace(old, new, 1)
        if s != o:
            io.open(f, 'w', encoding='utf-8', newline='').write(s)
            n += 1
    return n


def add_hub_card():
    p = os.path.join(ROOT, 'cadbim_cozumler.html')
    s = io.open(p, encoding='utf-8').read()
    if 'href="%s" class="sol-card"' % SLUG in s:
        return False
    cardhtml = u'''
    <a href="%s" class="sol-card">
      <div class="sol-icon" style="background:rgba(129,140,248,0.12);color:%s;"><i class="ti ti-box-multiple"></i></div>
      <h3>BIM İçerik & Obje Üretimi</h3>
      <p>Ürününüzün üretim CAD modelini, mimarın Revit projesine yerleşen, veri taşıyan ve doğru davranan bir BIM objesine dönüştürüyoruz.</p>
      <div class="sol-meta">
        <span class="sol-tag">Revit Family</span><span class="sol-tag">IFC</span><span class="sol-tag">Inventor</span><span class="sol-tag">Vault</span>
      </div>
      <div class="sol-arrow">Detaylı İncele <i class="ti ti-arrow-right"></i></div>
    </a>
''' % (SLUG, ACCENT)
    # BIM kartinin hemen ardina koy
    m = re.search(r'<a href="bim" class="sol-card"[^>]*>.*?</a>\n', s, re.S)
    assert m, 'BIM karti bulunamadi'
    s = s[:m.end()] + cardhtml + s[m.end():]
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


def add_to_industry_map():
    """Endustri haritasindaki mimari / insaat / makine panellerine ekler."""
    p = os.path.join(ROOT, 'cadbim_endustriler.html')
    s = io.open(p, encoding='utf-8').read()
    block = (u'<a href="%s" class="ind-sol-block"><div class="ind-sol-icon" '
             u'style="background:rgba(129,140,248,0.12);color:%s;">'
             u'<i class="ti ti-box-multiple"></i></div><h4>BIM İçerik & Obje Üretimi</h4>'
             u'<div class="ind-sol-products"><span>Revit</span><span>Inventor</span>'
             u'<span>IFC</span></div></a>' % (SLUG, ACCENT))
    added = []
    for ind in ('mimari', 'insaat', 'makine'):
        m = re.search(r'(<div class="ind-panel[^"]*" data-ind="%s">)(.*?)(\n  </div>)' % ind, s, re.S)
        if not m or 'href="%s"' % SLUG in m.group(2):
            continue
        a = re.search(r'<a href="bim" class="ind-sol-block".*?</a>', m.group(2), re.S)
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
    s = s.replace('"bim": "cadbim_bim.html"',
                  '"bim": "cadbim_bim.html",\n  "%s": "%s"' % (SLUG, FILE), 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


def add_sitemap():
    p = os.path.join(ROOT, 'sitemap.xml')
    s = io.open(p, encoding='utf-8').read()
    url = 'https://www.cadbim.com.tr/' + SLUG
    if url + '<' in s:
        return False
    m = re.search(r'<url>\s*<loc>https://www\.cadbim\.com\.tr/bim</loc>.*?</url>', s, re.S)
    assert m, 'sitemap bim kaydi bulunamadi'
    entry = m.group(0).replace('https://www.cadbim.com.tr/bim</loc>', url + '</loc>')
    s = s[:m.end()] + '\n' + entry + s[m.end():]
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True


if __name__ == '__main__':
    # SIRA ONEMLI: nav baglantisi, slug'i sayfa govdesine yazan adimlardan
    # (hub karti / endustri haritasi) ONCE eklenmeli. Aksi halde add_nav_link'in
    # "zaten var" korumasi govdedeki gecise takilip nav'i atlar.
    print('sayfa           : %d bayt' % build_page())
    print('nav baglantisi  : %d dosya' % add_nav_link())
    print('hub karti       : %s' % add_hub_card())
    print('endustri haritasi: %s' % add_to_industry_map())
    print('URL haritasi    : %s' % add_url_map())
    print('sitemap         : %s' % add_sitemap())
