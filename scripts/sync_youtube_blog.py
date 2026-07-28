# -*- coding: utf-8 -*-
"""
Cadbim Teknik Destek YouTube kanalındaki yeni videoları tarar ve blog'a ekler.
- Video başlığı  -> blog başlığı (aynen)
- Video açıklaması -> blog açıklaması (aynen, ilk paragraf)
- Kategori/ürün etiketi başlıktaki anahtar kelimelerden basit eşleştirmeyle atanır (AI kullanılmaz)
"""
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

# ürün adı -> (kategori, ürün sayfası dosya adı)
PRODUCT_MAP = [
    ("HP Build Workspace", "CAD", "cadbim_hp_build_workspace.html"),
    ("Revit LT", "BIM", "cadbim_revit_lt.html"),
    ("Revit", "BIM", "cadbim_revit.html"),
    ("Navisworks", "BIM", "cadbim_navisworks.html"),
    ("BIM Collaborate Pro", "BIM", "cadbim_bim_collaborate_pro.html"),
    ("BIM 360", "BIM", "cadbim_bim.html"),
    ("Dynamo", "BIM", "cadbim_bim.html"),
    ("Civil 3D", "İnşaat", "cadbim_civil3d.html"),
    ("InfraWorks", "İnşaat", "cadbim_infraworks.html"),
    ("Advance Steel", "İnşaat", "cadbim_advance_steel.html"),
    ("Robot Structural", "İnşaat", "cadbim_robot_structural.html"),
    ("Forma", "BIM", "cadbim_forma.html"),
    ("Inventor", "CAD", "cadbim_inventor.html"),
    ("Fusion", "CAD", "cadbim_fusion.html"),
    ("AutoCAD LT", "CAD", "cadbim_autocad_lt.html"),
    ("AutoCAD", "CAD", "cadbim_autocad.html"),
    ("Vault", "CAD", "cadbim_vault_pdm.html"),
    ("PDM", "CAD", "cadbim_pdm.html"),
    ("PLM", "CAD", "cadbim_plm.html"),
    ("Nastran", "Simülasyon", "cadbim_simulasyon.html"),
    ("CFD", "Simülasyon", "cadbim_cfd.html"),
    ("Simulasyon", "Simülasyon", "cadbim_simulasyon.html"),
    ("Simülasyon", "Simülasyon", "cadbim_simulasyon.html"),
    ("Factory Design", "CAD", "cadbim_factory_design.html"),
    ("Fabrication", "CAD", "cadbim_fabrication_cadmep.html"),
    ("Generative Design", "CAD", "cadbim_tasarim_otomasyonu.html"),
    ("Alias", "Görselleştirme", "cadbim_alias.html"),
    ("Maya", "Görselleştirme", "cadbim_maya.html"),
    ("3ds Max", "Görselleştirme", "cadbim_3dsmax.html"),
    ("Recap Pro", "Görselleştirme", "cadbim_recap_pro.html"),
    ("Illustrator", "Görselleştirme", "cadbim_illustrator.html"),
    ("Photoshop", "Görselleştirme", "cadbim_photoshop.html"),
    ("Acrobat", "Genel", "cadbim_adobe.html"),
    ("Firefly", "Görselleştirme", "cadbim_firefly.html"),
    ("Adobe Express", "Görselleştirme", "cadbim_adobe_express.html"),
]

def tr_lower(s):
    s = s.replace("İ", "i").replace("I", "ı")
    return s.lower()

def slugify(title):
    s = title.strip()
    s = s.replace("İ", "i").replace("I", "i")
    repl = {"ş": "s", "ğ": "g", "ü": "u", "ö": "o", "ç": "c", "ı": "i"}
    for k, v in repl.items():
        s = s.replace(k, v)
    s = s.lower()
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
    return "cadbim_urunler.html"

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

POST_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
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
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3/dist/tabler-icons.min.css">
<style>
:root{{
  --navy:#060c1a;--navy2:#0a1225;--navy3:#0d1830;
  --cyan:#00c8f0;--cyan2:#0ea5e9;
  --cdim:rgba(0,200,240,0.12);--cbor:rgba(0,200,240,0.2);
  --w:#fff;--w80:rgba(255,255,255,0.8);--w50:rgba(255,255,255,0.5);
  --w30:rgba(255,255,255,0.3);--w10:rgba(255,255,255,0.1);--w06:rgba(255,255,255,0.06);
  --fd:'Manrope',sans-serif;--fb:'Manrope',sans-serif;
  --r:8px;--rm:12px;--rl:16px;--rxl:24px;
}}
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--navy);color:var(--w);font-family:var(--fb);font-size:16px;line-height:1.6;overflow-x:hidden;}}
.nav{{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:0 2.5rem;height:68px;background:rgba(6,12,26,0.92);backdrop-filter:blur(20px);border-bottom:.5px solid var(--w10);}}
.nav-logo{{display:flex;align-items:center;gap:11px;text-decoration:none;}}
.nav-logo img{{height:26px;width:auto;filter:brightness(0) invert(1);opacity:.92;}}
.nav-links{{display:flex;align-items:center;gap:1.75rem;list-style:none;}}
.nav-links a{{color:var(--w50);font-size:13px;text-decoration:none;transition:color .2s;}}
.nav-links a:hover,.nav-links a.active{{color:var(--cyan);}}
.nav-cta{{background:var(--cyan)!important;color:var(--navy)!important;padding:9px 20px;border-radius:var(--r);font-weight:700;font-size:13px;}}
.article-wrap{{max-width:760px;margin:0 auto;padding:120px 1.5rem 64px;}}
.crumb{{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--w30);margin-bottom:24px;flex-wrap:wrap;}}
.crumb a{{color:var(--w30);text-decoration:none;}}.crumb a:hover{{color:var(--cyan);}}
.article-tags{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px;}}
.atag{{font-size:11px;font-weight:600;letter-spacing:.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;}}
.atag.cat{{background:var(--cdim);border:.5px solid var(--cbor);color:var(--cyan);}}
.atag.prod{{background:rgba(255,255,255,0.04);border:.5px solid var(--w10);color:var(--w50);}}
h1.a-title{{font-family:var(--fd);font-size:clamp(1.5rem,3.2vw,2.2rem);font-weight:800;line-height:1.25;color:var(--w);margin-bottom:16px;}}
.a-meta{{font-size:13px;color:var(--w30);margin-bottom:28px;display:flex;align-items:center;gap:10px;}}
.a-video{{aspect-ratio:16/9;border-radius:var(--rl);overflow:hidden;margin-bottom:24px;background:#000;border:.5px solid var(--w10);}}
.a-video iframe{{width:100%;height:100%;border:0;}}
.a-body{{font-size:15px;color:var(--w80);line-height:1.85;}}
.a-body p{{margin-bottom:20px;}}
.a-cta{{margin-top:36px;background:var(--navy3);border:.5px solid var(--cbor);border-radius:var(--rl);padding:26px;}}
.a-cta h3{{font-family:var(--fd);font-size:15px;font-weight:700;color:var(--w);margin-bottom:8px;}}
.a-cta p{{font-size:13px;color:var(--w50);margin-bottom:16px;}}
.btn-p{{background:var(--cyan);color:var(--navy);padding:11px 22px;border-radius:var(--r);font-weight:700;font-size:13px;text-decoration:none;font-family:var(--fd);display:inline-flex;align-items:center;gap:8px;transition:opacity .2s;}}
.btn-p:hover{{opacity:.88;}}
.btn-g{{background:transparent;color:var(--w80);border:.5px solid var(--w30);padding:11px 22px;border-radius:var(--r);font-size:13px;text-decoration:none;display:inline-flex;align-items:center;gap:8px;margin-left:8px;transition:all .2s;}}
.btn-g:hover{{border-color:var(--cyan);color:var(--cyan);}}
footer{{background:#040810;border-top:.5px solid var(--w06);padding:36px 3rem 24px;}}
.fbot{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;max-width:1200px;margin:0 auto;}}
.fbot p{{font-size:12px;color:rgba(255,255,255,0.2);}}
.socials{{display:flex;gap:10px;}}
.socials a{{width:32px;height:32px;border-radius:var(--r);border:.5px solid var(--w10);display:flex;align-items:center;justify-content:center;color:var(--w30);text-decoration:none;font-size:15px;transition:all .2s;}}
.socials a:hover{{border-color:var(--cyan);color:var(--cyan);}}
@media(max-width:900px){{.nav-links{{display:none;}}}}
@media(max-width:600px){{.article-wrap{{padding:96px 1.25rem 48px;}}}}
</style>
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
    "https://www.instagram.com/cadbim_izmir/",
    "https://www.facebook.com/cadbimizmir"
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
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.svg">
<link rel="stylesheet" href="../assets/css/design-system.css?v=10">
</head>
<body><nav class="nav">
  <a href="../index.html" class="nav-logo"><img src="../assets/logos/cadbim-yatay.png" alt="Cadbim"></a>
      <ul class="nav-links">
    <li><a href="../cadbim_urunler.html">Ürünler</a></li>
    <li><a href="../cadbim_cozumler.html">Çözümler</a></li>
    <li><a href="../cadbim_endustriler.html">Endüstriler</a></li>
    <li><a href="../cadbim_egitimler.html">Eğitimler</a></li>
    <li><a href="../cadbim_hakkimizda.html">Hakkımızda</a></li>
    <li><a href="../cadbim_iletisim.html">İletişim</a></li>
    <li><a href="../cadbim_kvkk.html">KVKK</a></li>
    <li><a href="../cadbim_blog.html" class="active">Blog</a></li>
    <li><a href="../cadbim_iletisim.html" class="nav-cta">Teklif Al</a></li>
  </ul>
</nav>
<div class="article-wrap">
  <div class="crumb"><a href="../index.html">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="../cadbim_blog.html">Blog</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">{title}</span></div>
  <div class="article-tags">
    <span class="atag cat">{category}</span>
    {prod_spans}
  </div>
  <h1 class="a-title">{title}</h1>
  <div class="a-meta"><i class="ti ti-calendar" style="font-size:14px;"></i>{tr_date} &middot; <i class="ti ti-brand-youtube" style="font-size:14px;"></i>Video</div>
  <div class="a-video"><iframe src="https://www.youtube.com/embed/{video_id}" title="{title}" loading="lazy" allowfullscreen></iframe></div>
  <div class="a-body">
    <p>{desc}</p>
  </div>
  <div class="a-cta">
    <h3>Bu konu hakkında daha fazla bilgi alın</h3>
    <p>Videoda bahsedilen ürün ve çözümler hakkında Cadbim ile iletişime geçin.</p>
    <a href="../{cta_page}" class="btn-p">Ürün Sayfasına Git <i class="ti ti-arrow-right"></i></a>
    <a href="../cadbim_iletisim.html" class="btn-g">Teklif İste</a>
  </div>
</div>
<footer>
  <div class="fbot">
    <p>&copy; 2026 Cadbim &mdash; <a href="../index.html" style="color:rgba(255,255,255,0.3);text-decoration:none;">Anasayfaya Dön</a> &middot; <a href="../cadbim_kvkk.html" style="color:rgba(255,255,255,0.3);text-decoration:none;">KVKK</a></p>
    <div class="socials">
      <a href="https://www.linkedin.com/company/cadbim/" aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a>
      <a href="https://www.youtube.com/c/CadbimTeknikDestek" aria-label="YouTube"><i class="ti ti-brand-youtube"></i></a>
      <a href="https://www.instagram.com/cadbim_izmir/" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a>
    </div>
  </div>
</footer>
<script src="../mobilenav.js?v=9" defer></script>
<script src="../whatsapp-widget.js?v=1" defer></script>
<script src="../cookie-consent.js?v=1" defer></script>
</body>
</html>
"""

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def build_post_html(slug, title, desc, video_id, iso_date, category, products):
    prod_spans = "\n    ".join(f'<span class="atag prod">{esc(p)}</span>' for p in products)
    return POST_TEMPLATE.format(
        title=esc(title), desc=esc(desc), slug=slug, video_id=video_id,
        iso_date=iso_date, tr_date=tr_date(iso_date), category=esc(category),
        prod_spans=prod_spans, cta_page=cta_page_for(products),
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

        html = build_post_html(slug, title, desc, v["videoId"], v["publishedAt"], category, products)
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
