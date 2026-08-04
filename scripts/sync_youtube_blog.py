# -*- coding: utf-8 -*-
"""
Cadbim Teknik Destek YouTube kanalındaki yeni videoları tarar ve blog'a ekler.
- Video başlığı  -> blog başlığı (aynen)
- Video açıklaması -> blog açıklaması (aynen, ilk paragraf)
- Kategori/ürün etiketi başlıktaki anahtar kelimelerden basit eşleştirmeyle atanır (AI kullanılmaz)
"""
import datetime
import json
import os
import re
import sys
import urllib.request
import urllib.parse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_JSON = os.path.join(BASE, "assets", "data", "blog-posts.json")
POST_DIR = os.path.join(BASE, "post")

API_KEY = os.environ.get("YOUTUBE_API_KEY")
CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID", "UCGLIaycdAkSFM3Q54d3zVQg")
MAX_RESULTS = int(os.environ.get("YOUTUBE_MAX_RESULTS", "15"))

# ürün adı -> (kategori, ürün sayfası temiz URL slug'ı)
PRODUCT_MAP = [
    ("HP Build Workspace", "CAD", "hp-build-workspace"),
    ("Revit LT", "BIM", "revit-lt"),
    ("Revit", "BIM", "revit"),
    ("Navisworks", "BIM", "navisworks"),
    ("BIM Collaborate Pro", "BIM", "bim-collaborate-pro"),
    ("BIM 360", "BIM", "bim"),
    ("Dynamo", "BIM", "bim"),
    ("Civil 3D", "İnşaat", "civil3d"),
    ("InfraWorks", "İnşaat", "infraworks"),
    ("Advance Steel", "İnşaat", "advance-steel"),
    ("Robot Structural", "İnşaat", "robot-structural"),
    ("Forma", "BIM", "forma"),
    ("Inventor", "CAD", "inventor"),
    ("Fusion", "CAD", "fusion"),
    ("AutoCAD LT", "CAD", "autocad-lt"),
    ("AutoCAD", "CAD", "autocad"),
    ("Vault", "CAD", "vault-pdm"),
    ("PDM", "CAD", "pdm"),
    ("PLM", "CAD", "plm"),
    ("Nastran", "Simülasyon", "simulasyon"),
    ("CFD", "Simülasyon", "cfd"),
    ("Simulasyon", "Simülasyon", "simulasyon"),
    ("Simülasyon", "Simülasyon", "simulasyon"),
    ("Factory Design", "CAD", "factory-design"),
    ("Fabrication", "CAD", "fabrication-cadmep"),
    ("Generative Design", "CAD", "tasarim-otomasyonu"),
    ("Alias", "Görselleştirme", "alias"),
    ("Maya", "Görselleştirme", "maya"),
    ("3ds Max", "Görselleştirme", "3dsmax"),
    ("Recap Pro", "Görselleştirme", "recap-pro"),
    ("Illustrator", "Görselleştirme", "illustrator"),
    ("Photoshop", "Görselleştirme", "photoshop"),
    ("Acrobat", "Genel", "adobe"),
    ("Firefly", "Görselleştirme", "firefly"),
    ("Adobe Express", "Görselleştirme", "adobe-express"),
]

def tr_lower(s):
    s = s.replace("İ", "i").replace("I", "ı")
    return s.lower()

def slugify(title):
    s = title.strip()
    s = s.replace("İ", "i").replace("I", "i")
    s = s.lower()
    repl = {"ş": "s", "ğ": "g", "ü": "u", "ö": "o", "ç": "c", "ı": "i"}
    for k, v in repl.items():
        s = s.replace(k, v)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def detect_products_and_category(title):
    tl = tr_lower(title)
    products = []
    category = None
    for name, cat, page in PRODUCT_MAP:
        if tr_lower(name) in tl:
            if name not in products:
                products.append(name)
            if category is None:
                category = cat
    return products, category

def cta_page_for(products):
    for name, cat, page in PRODUCT_MAP:
        if name in products:
            return page
    return "urunler"

def api_get(url, params):
    qs = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{qs}", timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def fetch_recent_videos():
    data = api_get("https://www.googleapis.com/youtube/v3/search", {
        "key": API_KEY,
        "channelId": CHANNEL_ID,
        "part": "snippet",
        "order": "date",
        "maxResults": MAX_RESULTS,
        "type": "video",
    })
    videos = []
    for item in data.get("items", []):
        vid = item["id"]["videoId"]
        sn = item["snippet"]
        videos.append({
            "videoId": vid,
            "title": sn["title"],
            "description": (sn.get("description") or "").strip().split("\n")[0][:300],
            "publishedAt": sn["publishedAt"][:10],  # YYYY-MM-DD
        })
    return videos

TR_MONTHS = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

def tr_date(iso_date):
    y, m, d = iso_date.split("-")
    return f"{int(d)} {TR_MONTHS[int(m)-1]} {y}"

# Sablon post/ dizinindeki guncel blog sayfalariyla birebir ayni tutulur.
# Referans sayfa: post/3d-gorunum.html -- head/nav/footer degisirse buradaki
# sablon da ayni anda guncellenmeli (yoksa yeni post sayfalari geride kalir).
POST_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https://i.ytimg.com https://img.youtube.com https://images.autodesk.com https://damassets.autodesk.net https://www.googletagmanager.com https://*.google-analytics.com; frame-src https://www.youtube-nocookie.com https://www.youtube.com https://maps.google.com https://www.google.com https://fast.wistia.net; connect-src 'self' https://*.powerplatform.com https://*.google-analytics.com https://analytics.google.com https://www.googletagmanager.com; media-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self' https://*.powerplatform.com">
  <meta name="referrer" content="strict-origin-when-cross-origin"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<title>{title} | Cadbim Blog</title>
  <meta property="og:title" content="{title} | Cadbim Blog">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="video.other">
  <meta property="og:url" content="https://www.cadbim.com.tr/post/{slug}">
  <meta property="og:image" content="https://img.youtube.com/vi/{video_id}/hqdefault.jpg">
  <meta property="og:site_name" content="Cadbim">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | Cadbim Blog">
  <meta name="twitter:description" content="{desc}">
  <link rel="canonical" href="https://www.cadbim.com.tr/post/{slug}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/tabler-icons-subset.css?v=4">
<link rel="stylesheet" href="../assets/css/blog-post.css?v=4">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#060c1a">
<meta property="og:locale" content="tr_TR">
<script type="application/ld+json">
{{
 "@context": "https://schema.org",
 "@graph": [
  {{
   "@type": "Organization",
   "@id": "https://www.cadbim.com.tr/#organization",
   "name": "Cadbim",
   "url": "https://www.cadbim.com.tr/",
   "logo": "https://www.cadbim.com.tr/og-image.png",
   "foundingDate": "1993",
   "email": "cadbim@cadbim.com.tr",
   "telephone": "+902324643490",
   "sameAs": [
    "https://www.linkedin.com/company/cadbim/",
    "https://www.youtube.com/c/CadbimTeknikDestek",
    "https://www.instagram.com/cadbim_izmir/"
   ]
  }},
  {{
   "@type": "VideoObject",
   "name": "{title}",
   "description": "{desc}",
   "uploadDate": "{iso_date}",
   "thumbnailUrl": "https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
   "embedUrl": "https://www.youtube.com/embed/{video_id}",
   "publisher": {{"@id": "https://www.cadbim.com.tr/#organization"}}
  }},
  {{
   "@type": "BreadcrumbList",
   "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "https://www.cadbim.com.tr/"}},
    {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.cadbim.com.tr/blog"}},
    {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "https://www.cadbim.com.tr/post/{slug}"}}
   ]
  }}
 ]
}}
</script>
  <link rel="icon" type="image/svg+xml" href="../favicon.svg">
  <link rel="apple-touch-icon" href="../assets/apple-touch-icon-180.png">
  <link rel="manifest" href="../site.webmanifest">
<link rel="stylesheet" href="../assets/css/design-system.css?v=29">
  <link rel="alternate" type="application/rss+xml" title="Cadbim Blog" href="/feed.xml">
<link rel="stylesheet" href="../assets/css/mobile-guardrails.css?v=3">
<link rel="stylesheet" href="../assets/css/wide-screen.css?v=1">
</head>
<body>
<a class="skip-link" href="#icerik">İçeriğe geç</a><header><nav class="nav">
  <a href="../" class="nav-logo"><img width="260" height="62" src="../assets/logos/cadbim-yatay.webp" alt="Cadbim"></a>
    <ul class="nav-links">
    <li class="nav-dropdown">
      <a href="../urunler">Ürünler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu">
        <a href="../autodesk">Autodesk</a>
        <a href="../adobe">Adobe</a>
        <a href="../designjet">HP DesignJet</a>
        <a href="../hp-z-workstation">HP Workstations</a>
        <a href="../hp-build-workspace">HP Build Workspace</a>
        <a href="../chaos">Chaos</a>
        <a href="../ultimaker">UltiMaker</a>
        <a href="../sketchup">SketchUp</a>
        <a href="../lumion">Lumion</a>
        <a href="../microsoft">Microsoft</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="../cozumler">Çözümler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu nav-mega">
        <a href="../dijital-donusum" class="nav-dd-feat"><i class="ti ti-sparkles" style="font-size:12px;"></i>Dijital Dönüşüm</a>
        <div class="nav-mega-cols">
          <div class="nav-mega-col">
            <div class="nav-dd-label">Yapı & Altyapı</div>
            <a href="../bim">BIM</a>
            <a href="../bim-icerik-uretimi">BIM İçerik & Obje Üretimi</a>
            <a href="../insaat-yonetimi">İnşaat Proje Yönetimi</a>
            <a href="../gerceklik-yakalama">Gerçeklik Yakalama</a>
            <a href="../dijital-ikiz">Dijital İkiz</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Ürün Tasarımı & Mühendislik</div>
            <a href="../simulasyon">Simülasyon & Analiz</a>
            <a href="../tolerans-analizi">Tolerans Analizi</a>
            <a href="../tasarim-otomasyonu">Tasarım Otomasyonu</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Üretim & İmalat</div>
            <a href="../cam">CAM & İmalat</a>
            <a href="../eklemeli-imalat">Eklemeli İmalat & 3D Baskı</a>
            <a href="../nesting">Nesting</a>
            <a href="../fabrika-tasarimi">Fabrika Tasarımı</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Veri & Süreç Yönetimi</div>
            <a href="../plm">PLM</a>
            <a href="../pdm">PDM</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Görselleştirme & İçerik</div>
            <a href="../gorsellestirme">Görselleştirme & Render</a>
            <a href="../ai-gorsellestirme">AI Destekli Görselleştirme</a>
            <a href="../yaratici-icerik">Yaratıcı İçerik & Tasarım</a>
          </div>
        </div>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="../endustriler">Endüstriler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu">
        <a href="../sektor-mimari">Mimarlık</a>
        <a href="../sektor-icmimarlik">İç Mimarlık</a>
        <a href="../sektor-insaat">İnşaat & Altyapı</a>
        <a href="../sektor-tesisat">Mekanik Tesisat</a>
        <a href="../sektor-makine">Makine & Üretim</a>
        <a href="../sektor-otomotiv">Otomotiv</a>
        <a href="../sektor-medya">Medya & Eğlence</a>
        <a href="../sektor-egitim">Eğitim</a>
        <a href="../sektor-havacilik">Savunma ve Havacılık</a>
      </div>
    </li>
    <li class="nav-dropdown"><a href="../danismanlik">Hizmetler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a><div class="nav-dropdown-menu"><a href="../sanatsal-baski"><span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span></a><a href="../danismanlik">Danışmanlık</a><a href="../designjet-teknik-servis">HP Plotter Teknik Servis</a><a href="../yazilim-gelistirme">Yazılım Geliştirme</a></div></li><li><a href="../egitimler">Eğitimler</a></li>
    <li><a href="../hakkimizda">Hakkımızda</a></li>
    <li><a href="../iletisim">İletişim</a></li>
    <li><a href="../kvkk">KVKK</a></li>
    <li><a href="../blog" class="active">Blog</a></li>
    <li><a href="../teklif-iste" class="nav-cta">Teklif Al</a></li>
  </ul>
</nav></header>
<main id="icerik">
<div class="article-wrap">
  <div class="crumb"><a href="../">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="../blog">Blog</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">{title}</span></div>
  <div class="article-tags">
    <span class="atag cat">{category}</span>
    {prod_spans}
  </div>
  <h1 class="a-title">{title}</h1>
  <div class="a-meta"><i class="ti ti-calendar" style="font-size:14px;"></i>{tr_date} &middot; <i class="ti ti-brand-youtube" style="font-size:14px;"></i>Video</div>
  <div class="a-video"><a class="yt-lite" href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener" data-yt="{video_id}" data-title="{title}" aria-label="Videoyu oynat: {title}"><img src="https://i.ytimg.com/vi/{video_id}/hqdefault.jpg" alt="" width="480" height="360" loading="lazy" decoding="async"><span class="yt-lite-btn" aria-hidden="true"></span></a></div>
  <div class="a-body">
    <p>{desc}</p>
  </div>
  <div class="a-cta">
    <h2>Bu konu hakkında daha fazla bilgi alın</h2>
    <p>Videoda bahsedilen ürün ve çözümler hakkında Cadbim ile iletişime geçin.</p>
    <a href="../{cta_page}" class="btn-p">Ürün Sayfasına Git <i class="ti ti-arrow-right"></i></a>
    <a href="../iletisim" class="btn-g">Teklif İste</a>
  </div>
{related}
</div>
</main>
<footer>
  <div class="footer-grid">
    <div class="f-brand">
      <a href="../"><img width="220" height="203" src="../assets/logos/cadbim-logo.webp" alt="Cadbim" loading="lazy" decoding="async"></a>
      <p>Tasarım, Mühendislik ve Simülasyon için yazılım & donanım çözümleri. Autodesk Gold Partner ve Adobe Gold Reseller Partner; HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağı.</p>
      <div class="f-offices">
        <span><i class="ti ti-map-pin" style="font-size:12px;margin-right:4px;"></i>İzmir Merkez Ofis</span>
        <span><i class="ti ti-map-pin" style="font-size:12px;margin-right:4px;"></i>Ankara Temsilcilik</span>
      </div>
    </div>
    <div class="footer-col">
      <h2>Ürünler</h2>
      <a href="../autodesk">Autodesk</a>
      <a href="../adobe">Adobe</a>
      <a href="../designjet">HP DesignJet</a>
      <a href="../hp-z-workstation">HP Workstations</a>
      <a href="../chaos">Chaos / V-Ray</a>
      <a href="../ultimaker">UltiMaker 3D</a>
    </div>
    <div class="footer-col">
      <h2>Hizmetler</h2>
      <a href="../egitimler">Eğitimler & Sertifikasyon</a>
      <a href="../bim">BIM Danışmanlığı</a>
      <a href="../iletisim">Teknik Destek</a>
      <a href="../hp">HP Yetkili Servis</a>
      <a href="../yazilim-gelistirme">Yazılım Geliştirme</a>
    </div>
    <div class="footer-col">
      <h2>İletişim</h2>
      <a href="mailto:cadbim@cadbim.com.tr">cadbim@cadbim.com.tr</a>
      <a href="tel:+902324643490">0232 464 34 90</a>
      <a href="https://wa.me/905532426737" target="_blank" rel="noopener">WhatsApp: 0553 242 67 37</a>
      <a href="../teklif-iste">Teklif İste</a>
      <a href="../egitimler">Eğitim Kayıt</a>
    </div>
  </div>
  <div class="footer-bot">
    <p>© 2026 Cadbim. Tüm hakları saklıdır. · <a href="../kvkk">KVKK</a> · <a href="javascript:void(0)" onclick="window.openCookiePrefs&amp;&amp;window.openCookiePrefs()">Çerez Ayarları</a></p>
    <div class="socials">
      <a href="https://www.linkedin.com/company/cadbim/" aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a>
      <a href="https://www.youtube.com/c/CadbimTeknikDestek" aria-label="YouTube"><i class="ti ti-brand-youtube"></i></a>
      <a href="https://www.instagram.com/cadbim_izmir/" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a>
      <a href="https://www.facebook.com/cadbimizmir" aria-label="Facebook"><i class="ti ti-brand-facebook"></i></a>
    </div>
  </div>
</footer>
<script src="../mobilenav.js?v=19" defer></script>
<script src="../whatsapp-widget.js?v=1" defer></script>
<script src="../cookie-consent.js?v=2" defer></script>
<script src="../yt-facade.js?v=1" defer></script>
</body>
</html>
"""

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

RELATED_COUNT = 4

def _days(iso_date):
    y, m, d = (int(x) for x in iso_date.split("-"))
    return datetime.date(y, m, d).toordinal()

def related_html(existing, category, iso_date):
    """post/ sayfalarındaki "İlgili Yazılar" bloğunu üretir.

    Seçim: aynı kategoriden, tarihi en yakın RELATED_COUNT yazı; kategori
    yetmezse en yeni yazılarla tamamlanır. Blok işaretlemesi mevcut post
    sayfalarıyla aynıdır, yalnızca seçim ölçütü bu betiğe özgüdür.
    """
    same_cat = sorted(
        (p for p in existing if p.get("cat") == category),
        key=lambda p: (abs((_days(p["date"]) - _days(iso_date))), p["date"]),
    )
    picked = same_cat[:RELATED_COUNT]
    if len(picked) < RELATED_COUNT:
        chosen = {p["slug"] for p in picked}
        filler = sorted(existing, key=lambda p: p["date"], reverse=True)
        picked += [p for p in filler if p["slug"] not in chosen][:RELATED_COUNT - len(picked)]
    if not picked:
        return ""
    cards = "\n    ".join(
        f'<a href="{p["slug"]}" class="a-related-card">'
        f'<span class="a-related-cat">{esc(p.get("cat") or "Genel")}</span>'
        f'<span class="a-related-title">{esc(p["title"])}</span>'
        f'<span class="a-related-date">{esc(p.get("trdate") or tr_date(p["date"]))}</span></a>'
        for p in picked
    )
    return (
        '  <div class="a-related">\n'
        "    <h2>İlgili Yazılar</h2>\n"
        '    <div class="a-related-grid">\n'
        f"    {cards}\n"
        "    </div>\n"
        "  </div>"
    )

def build_post_html(slug, title, desc, video_id, iso_date, category, products, existing=()):
    prod_spans = "\n    ".join(f'<span class="atag prod">{esc(p)}</span>' for p in products)
    return POST_TEMPLATE.format(
        title=esc(title), desc=esc(desc), slug=slug, video_id=video_id,
        iso_date=iso_date, tr_date=tr_date(iso_date), category=esc(category),
        prod_spans=prod_spans, cta_page=cta_page_for(products),
        related=related_html(existing, category, iso_date),
    )

def main():
    if not API_KEY:
        print("YOUTUBE_API_KEY tanımlı değil, çıkılıyor.")
        sys.exit(0)

    with open(POSTS_JSON, encoding="utf-8") as f:
        data = json.load(f)

    existing_video_ids = {p.get("videoId") for p in data if p.get("videoId")}
    existing_slugs = {p["slug"] for p in data}

    videos = fetch_recent_videos()
    new_count = 0
    new_items = []

    for v in videos:
        if v["videoId"] in existing_video_ids:
            continue

        title = v["title"]
        desc = v["description"] or title
        products, category = detect_products_and_category(title)
        category = category or "Genel"

        slug = slugify(title)
        base_slug = slug
        i = 2
        while slug in existing_slugs:
            slug = f"{base_slug}-{i}"
            i += 1
        existing_slugs.add(slug)

        html = build_post_html(slug, title, desc, v["videoId"], v["publishedAt"], category, products, data)
        with open(os.path.join(POST_DIR, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(html)

        data.append({
            "slug": slug, "title": title, "cat": category, "desc": desc,
            "date": v["publishedAt"], "trdate": tr_date(v["publishedAt"]),
            "products": products, "type": "video", "videoId": v["videoId"],
        })
        new_count += 1
        new_items.append(f"- {title}\n  https://www.cadbim.com.tr/post/{slug}\n  Kategori: {category} · Ürün: {', '.join(products) or '-'}")
        print("eklendi:", slug)

    if new_count:
        data.sort(key=lambda p: p["date"], reverse=True)
        with open(POSTS_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    notify_path = os.path.join(BASE, "new_videos_notify.txt")
    if new_items:
        header = (
            f"Bu e-posta bir yapay zeka otomasyonu (GitHub Actions) tarafından, "
            f"insan müdahalesi olmadan otomatik olarak gönderilmiştir.\n\n"
            f"Cadbim Teknik Destek YouTube kanalı otomatik olarak tarandı ve "
            f"{new_count} yeni video tespit edildi. Aşağıdaki içerikler için "
            f"blog.cadbim.com.tr üzerinde otomatik olarak birer sayfa oluşturuldu "
            f"ve siteye eklendi (video başlığı ve açıklaması olduğu gibi kullanıldı, "
            f"kategori/ürün etiketi başlıktaki anahtar kelimelerden otomatik atandı):\n"
        )
        with open(notify_path, "w", encoding="utf-8") as f:
            f.write(header + "\n" + "\n\n".join(new_items))
    elif os.path.exists(notify_path):
        os.remove(notify_path)

    print(f"toplam yeni video: {new_count}")

if __name__ == "__main__":
    main()
