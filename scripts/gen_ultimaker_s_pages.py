#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates cadbim_ultimaker_s{8,7,5,3}.html from a shared template + per-model data.
One-off content-generation script; not part of the site runtime."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Sablon kok dizindeki guncel sayfalarla birebir ayni tutulur.
# Referans sayfa: cadbim_ultimaker_s3.html -- head/nav/footer degisirse
# buradaki sablon da ayni anda guncellenmeli.
TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https://i.ytimg.com https://img.youtube.com https://images.autodesk.com https://damassets.autodesk.net https://www.googletagmanager.com https://*.google-analytics.com; frame-src https://www.youtube-nocookie.com https://www.youtube.com https://maps.google.com https://www.google.com https://fast.wistia.net; connect-src 'self' https://*.powerplatform.com https://*.google-analytics.com https://analytics.google.com https://www.googletagmanager.com; media-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self' https://*.powerplatform.com">
  <meta name="referrer" content="strict-origin-when-cross-origin"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{meta_desc}">
<title>{title}</title>
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.cadbim.com.tr/{slug}">
  <meta property="og:image" content="https://www.cadbim.com.tr/assets/og/cadbim_ultimaker.png">
  <meta property="og:site_name" content="Cadbim">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{meta_desc}">
  <link rel="canonical" href="https://www.cadbim.com.tr/{slug}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tabler-icons-subset.css?v=4">
<link rel="stylesheet" href="assets/css/tpl-ultimaker.css?v=1">

<!-- Google Analytics -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
</script>

<!-- SEO -->
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
   "url": "https://www.cadbim.com.tr/"
  }},
  {{
   "@type": "WebPage",
   "@id": "https://www.cadbim.com.tr/{slug}#webpage",
   "url": "https://www.cadbim.com.tr/{slug}",
   "name": "{title}",
   "description": "{meta_desc}",
   "inLanguage": "tr-TR",
   "publisher": {{
    "@id": "https://www.cadbim.com.tr/#organization"
   }}
  }},
  {{
   "@type": "BreadcrumbList",
   "itemListElement": [
    {{
     "@type": "ListItem",
     "position": 1,
     "name": "Ana Sayfa",
     "item": "https://www.cadbim.com.tr/"
    }},
    {{
     "@type": "ListItem",
     "position": 2,
     "name": "UltiMaker",
     "item": "https://www.cadbim.com.tr/ultimaker"
    }},
    {{
     "@type": "ListItem",
     "position": 3,
     "name": "{name}",
     "item": "https://www.cadbim.com.tr/{slug}"
    }}
   ]
  }},
  {{
   "@type": "Product",
   "name": "{name}",
   "description": "{meta_desc}",
   "url": "https://www.cadbim.com.tr/{slug}",
   "image": "https://www.cadbim.com.tr/assets/og/cadbim_ultimaker.png",
   "brand": {{
    "@type": "Brand",
    "name": "UltiMaker"
   }},
   "offers": {{
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceCurrency": "TRY",
    "seller": {{
     "@id": "https://www.cadbim.com.tr/#organization"
    }},
    "url": "https://www.cadbim.com.tr/{slug}"
   }}
  }}
 ]
}}
</script>
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon-180.png">
  <link rel="manifest" href="site.webmanifest">
<link rel="stylesheet" href="assets/css/design-system.css?v=31">
<link rel="stylesheet" href="assets/css/mobile-guardrails.css?v=3">
<link rel="stylesheet" href="assets/css/wide-screen.css?v=2">
</head>
<body>
<a class="skip-link" href="#icerik">İçeriğe geç</a>
<header><nav class="nav">
  <a href="/" class="nav-logo"><img width="260" height="62" src="assets/logos/cadbim-yatay.webp" alt="Cadbim"></a>
      <ul class="nav-links">
    <li class="nav-dropdown">
      <a href="urunler" class="active">Ürünler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu">
        <a href="autodesk">Autodesk</a>
        <a href="adobe">Adobe</a>
        <a href="designjet">HP DesignJet</a>
        <a href="hp-z-workstation">HP Workstations</a>
        <a href="hp-build-workspace">HP Build Workspace</a>
        <a href="chaos">Chaos</a>
        <a href="ultimaker">UltiMaker</a>
        <a href="sketchup">SketchUp</a>
        <a href="lumion">Lumion</a>
        <a href="microsoft">Microsoft</a>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="cozumler">Çözümler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu nav-mega">
        <a href="dijital-donusum" class="nav-dd-feat"><i class="ti ti-sparkles" style="font-size:12px;"></i>Dijital Dönüşüm</a>
        <div class="nav-mega-cols">
          <div class="nav-mega-col">
            <div class="nav-dd-label">Yapı & Altyapı</div>
            <a href="bim">BIM</a>
            <a href="bim-icerik-uretimi">BIM İçerik & Obje Üretimi</a>
            <a href="insaat-yonetimi">İnşaat Proje Yönetimi</a>
            <a href="gerceklik-yakalama">Gerçeklik Yakalama</a>
            <a href="dijital-ikiz">Dijital İkiz</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Ürün Tasarımı & Mühendislik</div>
            <a href="simulasyon">Simülasyon & Analiz</a>
            <a href="tolerans-analizi">Tolerans Analizi</a>
            <a href="tasarim-otomasyonu">Tasarım Otomasyonu</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Üretim & İmalat</div>
            <a href="cam">CAM & İmalat</a>
            <a href="eklemeli-imalat">Eklemeli İmalat & 3D Baskı</a>
            <a href="nesting">Nesting</a>
            <a href="fabrika-tasarimi">Fabrika Tasarımı</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Veri & Süreç Yönetimi</div>
            <a href="plm">PLM</a>
            <a href="pdm">PDM</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Görselleştirme & İçerik</div>
            <a href="gorsellestirme">Görselleştirme & Render</a>
            <a href="ai-gorsellestirme">AI Destekli Görselleştirme</a>
            <a href="yaratici-icerik">Yaratıcı İçerik & Tasarım</a>
          </div>
        </div>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="endustriler">Endüstriler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu">
        <a href="sektor-mimari">Mimarlık</a>
        <a href="sektor-makine">Makine & Üretim</a>
        <a href="sektor-medya">Medya & Eğlence</a>
        <a href="sektor-icmimarlik">İç Mimarlık</a>
        <a href="sektor-insaat">İnşaat & Altyapı</a>
        <a href="sektor-tesisat">Mekanik Tesisat</a>
        <a href="sektor-otomotiv">Otomotiv</a>
        <a href="sektor-egitim">Eğitim</a>
        <a href="sektor-havacilik">Savunma ve Havacılık</a>
      </div>
    </li>
    <li class="nav-dropdown"><a href="danismanlik">Hizmetler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a><div class="nav-dropdown-menu"><a href="sanatsal-baski"><span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span></a><a href="danismanlik">Danışmanlık</a><a href="designjet-teknik-servis">HP Plotter Teknik Servis</a><a href="yazilim-gelistirme">Yazılım Geliştirme</a></div></li><li><a href="egitimler">Eğitimler</a></li>
    <li><a href="hakkimizda">Hakkımızda</a></li>
    <li><a href="iletisim#form">İletişim</a></li>
    <li><a href="kvkk">KVKK</a></li>
    <li><a href="blog">Blog</a></li>
    <li><a href="teklif-iste#form" class="nav-cta">Teklif Al</a></li>
  </ul>
</nav></header>
<main id="icerik">

<section class="hero">
  <div class="hero-bg" style="background:radial-gradient(ellipse 70% 50% at 20% 0%,rgba(16,185,129,0.12) 0%,transparent 60%);"></div>
  <div class="hero-grid"></div>
  <div style="position:relative;z-index:1;">
    <div class="crumb"><a href="/">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="ultimaker">UltiMaker</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">{name}</span></div>
    <div style="max-width:760px;">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:18px;">
        <div style="width:56px;height:56px;border-radius:12px;background:#10b9811f;border:.5px solid #10b98140;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><img width="192" height="192" src="assets/logos/products/ultimaker-icon.webp" alt="{name}" style="width:30px;height:30px;object-fit:contain;" loading="lazy" decoding="async"></div>
        <div>
          <div style="font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--w30);">ULTIMAKER</div>
          <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">{name}</div>
          <div style="font-size:11px;color:var(--w30);margin-top:2px;">{kicker}</div>
        </div>
      </div>
      <h1 style="font-family:var(--fd);font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;line-height:1.12;color:var(--w);margin-bottom:16px;">{h1}</h1>
      <p style="font-size:16px;color:var(--w50);line-height:1.75;margin-bottom:32px;max-width:620px;">{hero_p}</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div style="border-radius:20px;overflow:hidden;border:.5px solid var(--w10);aspect-ratio:16/9;background:#000;">
    <iframe style="width:100%;height:100%;border:0;" src="{video_src}" title="{name} Tanıtım Videosu" loading="lazy" allowfullscreen allow="autoplay; fullscreen"></iframe>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div style="border-radius:20px;overflow:hidden;border:.5px solid var(--w10);display:flex;justify-content:center;"><img width="1484" height="1850" src="{hero_img}" alt="{name} 3D yazıcı" style="max-width:100%;width:auto;height:auto;max-height:460px;display:block;" loading="lazy" decoding="async"></div>
</section>

<section class="section section-alt">
  <div class="sh"><div class="slabel">Öne Çıkan Özellikler</div><div class="stitle" role="heading" aria-level="2">{name} ile Neler Yapabilirsiniz?</div></div>
  <div class="grid g3">{features}</div>
</section>
<section class="section">
  <div class="sh"><div class="slabel">Kullanım Senaryoları</div><div class="stitle" role="heading" aria-level="2">Kimler İçin?</div></div>
  <div class="grid g3">{usecases}</div>
</section>

<section data-enrich-brand style="padding:60px 3rem;background:#0a1225;">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:#00c8f0;margin-bottom:8px;">Cadbim Farkı</div>
    <div style="font-family:'Manrope',sans-serif;font-size:clamp(1.3rem,2.4vw,1.7rem);font-weight:800;color:#fff;margin-bottom:8px;">UltiMaker Tedarikinde Doğru Yapılandırma</div>
    <p style="font-size:14px;color:rgba(255,255,255,.45);line-height:1.7;margin:0 0 26px;max-width:640px;">Doğru model ve malzeme seçimi, kesintisiz sarf tedariki — satın alma ve yenileme sürecinde tek muhatap.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-bottom:30px;">
   <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
     <div style="width:36px;height:36px;border-radius:10px;background:#10b9811a;color:#10b981;display:flex;align-items:center;justify-content:center;margin-bottom:12px;"><i class="ti ti-flask" style="font-size:18px;"></i></div>
     <h3 style="font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:#fff;margin:0 0 6px;">Malzeme Danışmanlığı</h3>
     <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">300+ malzeme arasından parça gereksiniminize uygun seçim ve doğrulanmış profiller.</p>
   </div>
   <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
     <div style="width:36px;height:36px;border-radius:10px;background:#10b9811a;color:#10b981;display:flex;align-items:center;justify-content:center;margin-bottom:12px;"><i class="ti ti-truck-delivery" style="font-size:18px;"></i></div>
     <h3 style="font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:#fff;margin:0 0 6px;">Düzenli Sarf Tedariki</h3>
     <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">Filament, print core ve destek malzemesi stok planlamasıyla üretiminiz hiç durmaz.</p>
   </div></div>
    <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:24px;display:flex;flex-wrap:wrap;gap:22px;">
   <div style="flex:1;min-width:170px;display:flex;gap:10px;align-items:flex-start;">
     <div style="width:30px;height:30px;border-radius:50%;background:#10b9811a;border:1px solid #10b98155;color:#10b981;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti ti-message" style="font-size:14px;"></i></div>
     <div>
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">1. Teklif & İhtiyaç Analizi</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Kullanım profilinizi dinleyip doğru ürün ve adet planını çıkarıyoruz.</div>
     </div>
   </div>
   <div style="flex:1;min-width:170px;display:flex;gap:10px;align-items:flex-start;">
     <div style="width:30px;height:30px;border-radius:50%;background:#10b9811a;border:1px solid #10b98155;color:#10b981;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti ti-file-check" style="font-size:14px;"></i></div>
     <div>
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">2. Lisanslama / Tedarik</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Resmi kanaldan, doğru fiyatla ve kayıtlı sözleşmeyle temin.</div>
     </div>
   </div>
   <div style="flex:1;min-width:170px;display:flex;gap:10px;align-items:flex-start;">
     <div style="width:30px;height:30px;border-radius:50%;background:#10b9811a;border:1px solid #10b98155;color:#10b981;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti ti-settings" style="font-size:14px;"></i></div>
     <div>
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">3. Sarf & Malzeme Planı</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Doğru filament ve print core kombinasyonuyla ilk üretim planı.</div>
     </div>
   </div>
   <div style="flex:1;min-width:170px;display:flex;gap:10px;align-items:flex-start;">
     <div style="width:30px;height:30px;border-radius:50%;background:#10b9811a;border:1px solid #10b98155;color:#10b981;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti ti-headset" style="font-size:14px;"></i></div>
     <div>
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">4. Sürekli İletişim</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Ürün ve sarf sorularınızda Türkçe tek muhatap, yenileme hatırlatmaları.</div>
     </div>
   </div></div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="sh">
    <div class="slabel">İlgili Ürünler</div>
    <div class="stitle" role="heading" aria-level="2">İlgili ürünler ve çözümler</div>
    <p class="ssub">Birlikte değerlendirin</p>
  </div>
  <div class="grid g3" style="margin-top:0;">
{cross_cards}
  </div>
</section>
<div class="cta-strip">
  <h2>{name} teklifi alın</h2>
  <p>İhtiyacınıza uygun konfigürasyonu birlikte belirleyelim.</p>
  <div class="cta-btns">
    <a href="teklif-iste#form" class="btn-p">Teklif İste <i class="ti ti-arrow-right"></i></a>
  </div>
</div>
</main>
<footer id="iletisim">
  <div class="footer-grid">
    <div class="f-brand">
      <a href="/"><img width="220" height="203" src="assets/logos/cadbim-logo.webp" alt="Cadbim" loading="lazy" decoding="async"></a>
      <p>Tasarım, Mühendislik ve Simülasyon için yazılım &amp; donanım çözümleri. Autodesk Gold Partner, Adobe Gold Reseller Partner ve HP Amplify Synergy Partner; Microsoft, Chaos ve UltiMaker yetkili iş ortağı.</p>
      <div class="f-offices">
        <span><i class="ti ti-map-pin" style="font-size:12px;margin-right:4px;"></i>İzmir Merkez Ofis</span>
        <span><i class="ti ti-map-pin" style="font-size:12px;margin-right:4px;"></i>Ankara Temsilcilik</span>
      </div>
    </div>
    <div class="footer-col">
      <h2>Ürünler</h2>
      <a href="autodesk">Autodesk</a>
      <a href="adobe">Adobe</a>
      <a href="designjet">HP DesignJet</a>
      <a href="hp-z-workstation">HP Workstations</a>
      <a href="chaos">Chaos / V-Ray</a>
      <a href="ultimaker">UltiMaker 3D</a>
      <a href="microsoft">Microsoft</a>
      <a href="urunler">Tüm ürünler</a>
    </div>
    <div class="footer-col">
      <h2>Çözümler</h2>
      <a href="dijital-donusum">Dijital Dönüşüm</a>
      <a href="bim">BIM</a>
      <a href="simulasyon">Simülasyon &amp; Analiz</a>
      <a href="tasarim-otomasyonu">Tasarım Otomasyonu</a>
      <a href="cam">CAM &amp; İmalat</a>
      <a href="eklemeli-imalat">Eklemeli İmalat &amp; 3D Baskı</a>
      <a href="gorsellestirme">Görselleştirme &amp; Render</a>
      <a href="cozumler">Tüm çözümler</a>
    </div>
    <div class="footer-col">
      <h2>Endüstriler</h2>
      <a href="sektor-mimari">Mimarlık</a>
      <a href="sektor-icmimarlik">İç Mimarlık</a>
      <a href="sektor-insaat">İnşaat &amp; Altyapı</a>
      <a href="sektor-tesisat">Mekanik Tesisat</a>
      <a href="sektor-makine">Makine &amp; Üretim</a>
      <a href="sektor-otomotiv">Otomotiv</a>
      <a href="sektor-medya">Medya &amp; Eğlence</a>
      <a href="sektor-egitim">Eğitim</a>
      <a href="sektor-havacilik">Savunma ve Havacılık</a>
    </div>
    <div class="footer-col">
      <h2>Hizmetler</h2>
      <a href="sanatsal-baski"><span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span></a>
      <a href="danismanlik">Danışmanlık</a>
      <a href="egitimler">Eğitimler &amp; Sertifikasyon</a>
      <a href="designjet-teknik-servis">HP Plotter Teknik Servis</a>
      <a href="yazilim-gelistirme">Yazılım Geliştirme</a>
      <a href="iletisim#form">Teknik Destek</a>
    </div>
    <div class="footer-col">
      <h2>İletişim</h2>
      <a href="mailto:cadbim@cadbim.com.tr">cadbim@cadbim.com.tr</a>
      <a href="tel:+902324643490">0232 464 34 90</a>
      <a href="https://wa.me/905532426737" target="_blank" rel="noopener">WhatsApp: 0553 242 67 37</a>
      <a href="teklif-iste#form">Teklif İste</a>
      <a href="egitimler">Eğitim Kayıt</a>
      <a href="iletisim#form">İletişim Formu</a>
    </div>
  </div>
  <div class="footer-bot">
    <p>© 2026 Cadbim. Tüm hakları saklıdır. · <a href="hakkimizda">Hakkımızda</a> · <a href="basari-oykuleri">Başarı Öyküleri</a> · <a href="blog">Blog</a> · <a href="kvkk">KVKK</a> · <a href="javascript:void(0)" onclick="window.openCookiePrefs&amp;&amp;window.openCookiePrefs()">Çerez Ayarları</a></p>
    <div class="socials">
      <a href="https://www.linkedin.com/company/cadbim/" aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a>
      <a href="https://www.youtube.com/c/CadbimTeknikDestek" aria-label="YouTube"><i class="ti ti-brand-youtube"></i></a>
      <a href="https://www.instagram.com/cadbim_izmir/" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a>
      <a href="https://www.facebook.com/cadbimizmir" aria-label="Facebook"><i class="ti ti-brand-facebook"></i></a>
    </div>
  </div>
</footer>
<script src="mobilenav.js?v=20" defer></script>
<script src="whatsapp-widget.js?v=1" defer></script>
<script src="social-widget.js?v=7" defer></script>
<script src="cookie-consent.js?v=2" defer></script>
</body></html>
"""

def card(icon, title, desc):
    return f'<div class="card"><div class="card-icon"><i class="ti {icon}"></i></div><h3>{title}</h3><p>{desc}</p></div>'

UM_LOGO = "logo"

def cross_card(href, icon, title, desc):
    """"İlgili ürünler ve çözümler" bölümündeki kart. icon == UM_LOGO ise
    UltiMaker ürün ikonu, aksi halde verilen Tabler ikonu kullanılır."""
    if icon == UM_LOGO:
        inner = ('<div class="card-icon" style="background:rgba(255,255,255,.07);">'
                 '<img width="192" height="192" src="assets/logos/products/ultimaker-icon.webp"'
                 ' alt="" style="width:32px;height:32px;object-fit:contain;"'
                 ' loading="lazy" decoding="async"></div>')
    else:
        inner = f'<div class="card-icon" style="background:rgba(0,200,240,.12);"><i class="ti {icon}"></i></div>'
    return (f'    <a href="{href}" class="card">\n'
            f'      {inner}\n'
            f'      <h3>{title}</h3>\n'
            f'      <p>{desc}</p>\n'
            f'    </a>')

CROSS_COMMON = [
    cross_card("ultimaker", UM_LOGO, "UltiMaker Marka Sayfası",
               "Tüm UltiMaker yazıcılarını ve yazılım ekosistemini tek sayfada inceleyin."),
    cross_card("cura", UM_LOGO, "UltiMaker Cura",
               "Hazır baskı profilleri sunan, yaygın kullanılan dilimleme yazılımı."),
    cross_card("digital-factory", "ti-cloud-cog", "Digital Factory",
               "Yazıcı filosunu buluttan yönetme, iş kuyruğu ve uzaktan izleme platformu."),
    cross_card("eklemeli-imalat", "ti-cube-3d-sphere", "Eklemeli İmalat Çözümleri",
               "Yazıcı, malzeme ve yazılımıyla uçtan uca 3D baskı çözümleri."),
]

# Model kartlarından sonra en sona eklenir.
CROSS_MALZEME = cross_card(
    "ultimaker-malzeme", "ti-flask", "Malzeme Kütüphanesi",
    "UltiMaker malzemelerini ve uyumlu print core seçeneklerini keşfedin.",
)

# slug -> (kart başlığı, kart açıklaması) — modeller arası karşılaştırma kartları
COMPARE = {
    "s8": ("UltiMaker S8 ile Karşılaştır", "Daha yüksek baskı hızı sunan S8 ile farkları değerlendirin."),
    "s7": ("UltiMaker S7 ile Karşılaştır", "Air Manager entegrasyonlu S7 ile özellik farklarını değerlendirin."),
    "s5": ("UltiMaker S5 ile Karşılaştır", "Daha büyük baskı hacimli S5 ile farkları değerlendirin."),
    "s3": ("UltiMaker S3 ile Karşılaştır", "Kompakt masaüstü model S3 ile farkları değerlendirin."),
}

def compare_card(key, title=None, desc=None):
    t, d = COMPARE[key]
    return cross_card(f"ultimaker-{key}", UM_LOGO, title or t, desc or d)

MODELS = {}

MODELS["s8"] = dict(
    slug="ultimaker-s8",
    name="UltiMaker S8",
    title="UltiMaker S8 Endüstriyel 3D Yazıcı | Cadbim",
    og_title="UltiMaker S8 | Cadbim",
    meta_desc="UltiMaker S8: Cheetah hareket planlayıcısı, 500 mm/s baskı hızı, 301+ malzeme desteği. Avrupa'da üretilen en hızlı çift malzemeli profesyonel 3D yazıcı. Cadbim yetkili iş ortağı.",
    kicker="S Serisi Amiral Gemisi · En Hızlı Çift Ekstruderli Masaüstü Yazıcı",
    h1="Öncekinden 4 Kat Daha Üretken",
    hero_p="UltiMaker S8, yeni Cheetah hareket planlayıcısı, yüksek akışlı print core'lar ve geliştirilmiş besleme sistemiyle S7'ye kıyasla 4 kat daha yüksek verimlilik sunar — baskı kalitesinden ödün vermeden. Avrupa'da tasarlanıp üretilen, piyasadaki en hızlı çift malzemeli masaüstü profesyonel 3D yazıcı.",
    video_src="https://fast.wistia.net/embed/iframe/k5a3nsn454",
    hero_img="assets/products/ultimaker-web/s8-hero.webp",
    features=[
        ("ti-bolt", "Cheetah Hareket Planlayıcı", "500 mm/s'ye varan hareket hızı, 50.000 mm/s² ivme — S7'ye göre 4 kat verimlilik."),
        ("ti-focus-2", "0.15 mm ± %0.15 Hassasiyet", "Yüksek hızda bile boyutsal doğruluktan ödün vermeyen baskı kalitesi."),
        ("ti-droplet", "Yeni Nesil Print Core'lar", "AA+ ve CC+ quad-chamber tasarımlı print core'lar, 2.5 kat daha yüksek akış."),
        ("ti-layout-grid", "Manyetik Esnek Tabla", "PEI kaplı, 25 mıknatıs ve 4 pimle hizalanan tabla — yapıştırıcısız, kolay parça çıkarma."),
        ("ti-air-conditioning", "Entegre EPA Filtre", "Ultra ince partiküllerin %95'ini süzen kapalı kasa — sağlıklı ve temiz baskı ortamı."),
        ("ti-git-branch", "Çift Ekstruder, 301+ Malzeme", "İki farklı malzemeyi minimum fire ile birleştirin; NFC ile otomatik malzeme tanıma."),
    ],
    usecases=[
        ("ti-settings-automation", "Yüksek Hacimli Prototipleme", "Kısa döngü süreleri ve yüksek tekrarlanabilirlikle Ar-Ge ekiplerinin en yoğun iş yükü."),
        ("ti-shield-check", "Mühendislik & Savunma", "Sıkı toleranslı, izlenebilir üretim gerektiren kritik parçalar için güvenlik odaklı donanım."),
        ("ti-building-factory-2", "Üretim Yardımcıları", "Jig, fikstür ve son kullanım parçalarının hızlı ve tutarlı biçimde yerinde üretimi."),
    ],
    cross_cards=CROSS_COMMON + [compare_card("s7"), CROSS_MALZEME],
)

MODELS["s7"] = dict(
    slug="ultimaker-s7",
    name="UltiMaker S7",
    title="UltiMaker S7 3D Yazıcı | Cadbim",
    og_title="UltiMaker S7 | Cadbim",
    meta_desc="UltiMaker S7: Entegre Air Manager, PEI kaplı esnek tabla, endüktif otomatik seviyeleme ve 280+ malzeme desteği. Cadbim yetkili iş ortağı.",
    kicker="S Serisi · Kur ve Unut",
    h1="Kutudan Çıkar Çıkmaz Hazır",
    hero_p="UltiMaker S5'in sevilen özelliklerini alıp bir adım öteye taşıdık. S7; entegre Air Manager, manyetik esnek tabla ve endüktif otomatik seviyelemesiyle yüksek kaliteli parçaları eskisinden çok daha kolay üretir.",
    video_src="https://www.youtube-nocookie.com/embed/XW6nJvmed9o",
    hero_img="assets/products/ultimaker-web/s7-hero.webp",
    features=[
        ("ti-wind", "Entegre Air Manager", "Kapalı kasa ve tekli cam kapakla ultra ince partiküllerin %95'ini süzer — bağımsız test edilmiştir."),
        ("ti-layout-grid", "Manyetik Esnek Tabla", "PEI kaplı, 25 mıknatıs ve 4 pimle mükemmel hizalama — yapıştırıcısız parça çıkarma."),
        ("ti-radar-2", "Endüktif Otomatik Seviyeleme", "Arka plan gürültüsünden 100 kat güçlü sinyalle sessiz, hassas tabla probu; vidalı kalibrasyona gerek yok."),
        ("ti-file-check", "280+ Malzeme Desteği", "Üretici ve kullanıcılar tarafından binlerce saat test edilmiş malzeme profilleriyle çalışın."),
        ("ti-replace", "S5 ile Dosya Uyumluluğu", "Mevcut S5 baskı dosyalarınız yeniden dilimlemeye gerek kalmadan S7'de çalışır."),
        ("ti-droplet-off", "Taşma Önleyici Sensör", "Yeniden tasarlanan print head olası taşmaları erken tespit eder, güçlü mıknatıslarla kapı kapalı kalır."),
    ],
    usecases=[
        ("ti-building", "Mühendislik Ofisleri", "Az bakım gerektiren, güvenilir günlük prototipleme için düşük operatör yükü."),
        ("ti-school", "Eğitim & Araştırma", "Basit kurulum ve otomatik seviyeleme ile öğrenci ve araştırmacılar için erişilebilir baskı."),
        ("ti-tool", "Üretim Destek Ekipleri", "Fikstür ve aparat üretiminde tutarlı, tekrarlanabilir sonuçlar."),
    ],
    cross_cards=CROSS_COMMON + [
        compare_card("s8"),
        compare_card("s5", desc="S serisinin S5 modeliyle özellik farklarını değerlendirin."),
        CROSS_MALZEME,
    ],
)

MODELS["s5"] = dict(
    slug="ultimaker-s5",
    name="UltiMaker S5",
    title="UltiMaker S5 3D Yazıcı | Cadbim",
    og_title="UltiMaker S5 | Cadbim",
    meta_desc="UltiMaker S5: 330×240×300 mm büyük baskı hacmi, kompozit malzeme uyumlu çift ekstruder, ödüllü dokunmatik arayüz ve 280+ malzeme. Cadbim yetkili iş ortağı.",
    kicker="S Serisi · Kanıtlanmış Büyük Hacimli Platform",
    h1="3D Baskı Hedeflerinizi Büyütün",
    hero_p="UltiMaker S5; dünya standartlarında malzeme uyumluluğu, ödüllü dokunmatik arayüzü ve filament bitiş algılamasıyla daha büyük parçaları kolayca basmanızı sağlar. Binlerce işletmenin güvendiği, kanıtlanmış bir platform.",
    video_src="https://www.youtube-nocookie.com/embed/N_r7UYMQwDk",
    hero_img="assets/products/ultimaker-web/s5-hero.webp",
    features=[
        ("ti-box-multiple", "330×240×300 mm Baskı Hacmi", "S serisinin en büyük baskı alanı — büyük parçaları tek seferde üretin."),
        ("ti-atom-2", "Kompozite Hazır Çift Ekstruder", "Cam veya karbon fiber takviyeli kompozit malzemelerle güçlendirilmiş parçalar üretin."),
        ("ti-device-desktop", "Ödüllü Dokunmatik Arayüz", "Sezgisel arayüzle iş kuyruğu, kalibrasyon ve malzeme yönetimini kolayca yapın."),
        ("ti-file-check", "280+ Malzeme Desteği", "Mühendislik polimerlerinden geri dönüştürülmüş filamentlere, paslanmaz çeliğe kadar geniş yelpaze."),
        ("ti-alert-triangle", "Filament Bitiş Algılama", "Malzeme biterse baskı otomatik durur — iş kaybı ve fire olmadan devam edin."),
        ("ti-git-branch", "Kanıtlanmış Ekosistem Uyumu", "Cura, Digital Factory, Material Station ve print core ailesiyle tam entegrasyon."),
    ],
    usecases=[
        ("ti-building-factory-2", "Endüstriyel İşletmeler", "Büyük hacimli parça ve aparatların güvenilir, tekrarlanabilir üretimi."),
        ("ti-car", "Otomotiv & Ürün Geliştirme", "Kompozit malzemelerle fonksiyonel prototip ve son kullanım parçaları."),
        ("ti-building", "Kurumsal Tasarım Ofisleri", "Çok kullanıcılı ortamlarda büyük ölçekli konsept model ve maket üretimi."),
    ],
    cross_cards=CROSS_COMMON + [compare_card("s7"), compare_card("s3"), CROSS_MALZEME],
)

MODELS["s3"] = dict(
    slug="ultimaker-s3",
    name="UltiMaker S3",
    title="UltiMaker S3 3D Yazıcı | Cadbim",
    og_title="UltiMaker S3 | Cadbim",
    meta_desc="UltiMaker S3: Kompakt masaüstü mühendislik yazıcısı. Kompozite hazır çift ekstruder, otomatik tabla seviyeleme, 190+ malzeme desteği. Cadbim yetkili iş ortağı.",
    kicker="S Serisi · Kompakt Mühendislik Yazıcısı",
    h1="Masaya Sığan Güç",
    hero_p="Masaüstünde rahatça yer bulan UltiMaker S3, cam ve karbon fiber kompozit baskıya hazır. Çözülebilir destek malzemeleriyle karmaşık geometrilerde daha fazla tasarım özgürlüğü sunar.",
    video_src="https://www.youtube-nocookie.com/embed/WV2C6YXMJzc",
    hero_img="assets/products/ultimaker-web/s3-hero.webp",
    features=[
        ("ti-cube", "Kompakt Masaüstü Tasarım", "Küçük ofis ve atölyelere rahatça sığan, güçlü bir mühendislik yazıcısı."),
        ("ti-atom-2", "Kompozite Hazır Çift Ekstruder", "Cam ve karbon fiber takviyeli malzemelerle güçlü parçalar üretmeye hazır."),
        ("ti-adjustments", "Gelişmiş Otomatik Tabla Seviyeleme", "Manuel kalibrasyon derdi olmadan güvenilir ilk katman."),
        ("ti-device-desktop", "Ödüllü Dokunmatik Arayüz", "Sezgisel arayüzle kolay iş takibi ve baskı yönetimi."),
        ("ti-file-check", "190+ Malzeme Desteği", "Dünyanın en gelişmiş filamentleriyle tık ve baskı deneyimi."),
        ("ti-droplet", "Çözülebilir Destek Malzemesi", "PVA gibi çözülebilir desteklerle karmaşık geometrilerde tam tasarım özgürlüğü."),
    ],
    usecases=[
        ("ti-school", "Eğitim & Küçük Ekipler", "Az yer kaplayan, düşük bakım gerektiren giriş seviyesi mühendislik baskısı."),
        ("ti-bulb", "Konsept & Fonksiyonel Prototip", "Fikirden fiziksel modele hızlı geçiş için ideal masaüstü çözüm."),
        ("ti-building-factory-2", "Metal Genişletme Kiti Uyumu", "Metal Expansion Kit ile paslanmaz çelik fonksiyonel parça prototiplemesi."),
    ],
    cross_cards=CROSS_COMMON + [compare_card("s5"), CROSS_MALZEME],
)

for key, m in MODELS.items():
    features_html = "".join(card(i, t, d) for i, t, d in m["features"])
    usecases_html = "".join(card(i, t, d) for i, t, d in m["usecases"])
    cross_html = "\n".join(m["cross_cards"])
    html = TEMPLATE.format(
        meta_desc=m["meta_desc"],
        title=m["title"],
        og_title=m["og_title"],
        slug=m["slug"],
        name=m["name"],
        kicker=m["kicker"],
        h1=m["h1"],
        hero_p=m["hero_p"],
        video_src=m["video_src"],
        hero_img=m["hero_img"],
        features=features_html,
        usecases=usecases_html,
        cross_cards=cross_html,
    )
    out_path = os.path.join(BASE, f"cadbim_ultimaker_{key}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path, len(html), "bytes")
