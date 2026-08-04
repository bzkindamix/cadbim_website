#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates cadbim_ultimaker_s{8,7,5,3}.html from a shared template + per-model data.
One-off content-generation script; not part of the site runtime."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
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
.nav-logo:hover img{{animation:navLogoDraw .7s cubic-bezier(.4,0,.2,1);}}
@keyframes navLogoDraw{{from{{clip-path:inset(0 100% 0 0);opacity:.35;}}to{{clip-path:inset(0 0% 0 0);opacity:.92;}}}}
.nav-links{{display:flex;align-items:center;gap:1.75rem;list-style:none;}}
.nav-links a{{color:var(--w50);font-size:13px;text-decoration:none;transition:color .2s;}}
.nav-links a:hover,.nav-links a.active{{color:var(--cyan);}}
.nav-cta{{background:var(--cyan)!important;color:var(--navy)!important;padding:9px 20px;border-radius:var(--r);font-weight:700;font-size:13px;}}
.hero{{padding:120px 3rem 72px;position:relative;overflow:hidden;}}
.hero-bg{{position:absolute;inset:0;pointer-events:none;}}
.hero-grid{{position:absolute;inset:0;opacity:.02;background-image:linear-gradient(var(--w10) 1px,transparent 1px),linear-gradient(90deg,var(--w10) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;}}
.crumb{{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--w30);margin-bottom:20px;}}
.crumb a{{color:var(--w30);text-decoration:none;}}.crumb a:hover{{color:var(--cyan);}}
.section{{padding:72px 3rem;}}
.section-alt{{background:var(--navy2);}}
.sh{{margin-bottom:48px;}}
.slabel{{font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:var(--cyan);margin-bottom:8px;}}
.stitle{{font-family:var(--fd);font-size:clamp(1.5rem,2.8vw,2rem);font-weight:700;color:var(--w);margin-bottom:10px;}}
.ssub{{font-size:15px;color:var(--w50);max-width:560px;line-height:1.7;}}
.btn-p{{background:var(--cyan);color:var(--navy);padding:13px 28px;border-radius:var(--r);font-weight:700;font-size:14px;text-decoration:none;font-family:var(--fd);transition:opacity .2s,transform .15s;display:inline-flex;align-items:center;gap:8px;}}
.btn-p:hover{{opacity:.88;transform:translateY(-1px);}}
.btn-g{{background:transparent;color:var(--w80);border:.5px solid var(--w30);padding:13px 28px;border-radius:var(--r);font-size:14px;text-decoration:none;transition:all .2s;display:inline-flex;align-items:center;gap:8px;}}
.btn-g:hover{{border-color:var(--cyan);color:var(--cyan);transform:translateY(-1px);}}
.grid{{display:grid;gap:16px;margin-top:40px;}}
.g2{{grid-template-columns:repeat(auto-fit,minmax(280px,1fr));}}
.g3{{grid-template-columns:repeat(auto-fit,minmax(240px,1fr));}}
.g4{{grid-template-columns:repeat(auto-fit,minmax(200px,1fr));}}
.card{{background:var(--navy3);border-radius:var(--rl);border:.5px solid var(--w10);padding:24px 22px;transition:border-color .2s;}}
.card:hover{{border-color:var(--cbor);}}
.card.hi{{border-color:var(--cbor);}}
.card-icon{{font-size:26px;color:var(--cyan);margin-bottom:14px;}}
.card h3{{font-family:var(--fd);font-size:15px;font-weight:600;color:var(--w);margin-bottom:8px;}}
.card p{{font-size:13px;color:var(--w50);line-height:1.65;}}
.pts{{display:flex;flex-direction:column;gap:5px;margin-top:10px;}}
.pt{{display:flex;align-items:flex-start;gap:7px;font-size:13px;color:var(--w50);}}
.pt i{{font-size:13px;flex-shrink:0;margin-top:2px;}}
.tags{{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;}}
.tag{{font-size:10px;padding:2px 8px;border-radius:4px;border:.5px solid;}}
.cross{{background:rgba(0,200,240,0.04);border:.5px solid var(--cbor);border-radius:var(--rxl);padding:32px;margin-top:16px;}}
.cross h3{{font-family:var(--fd);font-size:15px;font-weight:600;color:var(--w);margin-bottom:6px;}}
.cross .cd{{font-size:13px;color:var(--w50);margin-bottom:16px;}}
.cpills{{display:flex;flex-wrap:wrap;gap:10px;}}
.cp{{display:inline-flex;align-items:center;gap:9px;padding:8px 18px 8px 8px;border-radius:999px;background:var(--navy3);border:.5px solid var(--w10);font-size:13px;color:var(--w50);text-decoration:none;transition:border-color .2s,color .2s,transform .2s,background .2s;}}
.cp:hover{{border-color:var(--cbor);color:var(--w);background:rgba(0,200,240,.06);transform:translateY(-2px);}}
.cp i{{font-size:14px;color:var(--cyan);width:26px;height:26px;border-radius:50%;background:rgba(0,200,240,.13);display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.cp img{{border-radius:50%;background:rgba(255,255,255,.08);padding:3px;flex-shrink:0;}}
.cta-strip{{background:var(--navy3);border:.5px solid var(--cbor);border-radius:var(--rxl);padding:44px;text-align:center;position:relative;overflow:hidden;margin:0 3rem 72px;}}
.cta-strip::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 50% 120%,rgba(0,200,240,.08),transparent 70%);pointer-events:none;}}
.cta-strip h2{{font-family:var(--fd);font-size:clamp(1.4rem,2.5vw,2rem);font-weight:800;color:var(--w);margin-bottom:10px;}}
.cta-strip p{{font-size:15px;color:var(--w50);margin-bottom:28px;}}
.cta-btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}}
footer{{background:#040810;border-top:.5px solid var(--w06);padding:40px 3rem 24px;}}
.fbot{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}}
.fbot p{{font-size:12px;color:rgba(255,255,255,0.2);}}
.socials{{display:flex;gap:10px;}}
.socials a{{width:32px;height:32px;border-radius:var(--r);border:.5px solid var(--w10);display:flex;align-items:center;justify-content:center;color:var(--w30);text-decoration:none;font-size:15px;transition:all .2s;}}
.socials a:hover{{border-color:var(--cyan);color:var(--cyan);}}
@media(max-width:900px){{.nav-links{{display:none;}}.cta-strip{{margin:0 1.5rem 56px;}}}}
@media(max-width:600px){{.section{{padding:52px 1.5rem;}}.hero{{padding:100px 1.5rem 56px;}}}}

.nav-dropdown{{position:relative;}}
.nav-dropdown>a{{display:flex;align-items:center;gap:4px;cursor:pointer;}}
.nav-dropdown-menu{{position:absolute;top:100%;left:0;margin-top:12px;background:var(--navy2,#0a1225);border:1px solid rgba(255,255,255,0.1);border-radius:10px;min-width:230px;padding:8px;opacity:0;visibility:hidden;transform:translateY(-6px);transition:all .18s ease;box-shadow:0 12px 32px rgba(0,0,0,0.5);z-index:1100;}}
.nav-dropdown:hover .nav-dropdown-menu{{opacity:1;visibility:visible;transform:translateY(0);}}
.nav-dropdown-menu a{{display:block;padding:9px 12px;border-radius:6px;font-size:13px;color:rgba(255,255,255,0.7);text-decoration:none;white-space:nowrap;}}
.nav-dropdown-menu a:hover{{background:rgba(0,200,240,0.08);color:#00c8f0;}}
</style>

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
  <link rel="apple-touch-icon" href="favicon.svg">
<link rel="stylesheet" href="assets/css/design-system.css?v=10">
<link rel="stylesheet" href="assets/css/mobile-guardrails.css?v=3">
<link rel="stylesheet" href="assets/css/wide-screen.css?v=1">
</head>
<body>
<nav class="nav">
  <a href="index.html" class="nav-logo"><img src="assets/logos/cadbim-yatay.png" alt="Cadbim"></a>
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
            <div class="nav-dd-label">Tasarım & Mühendislik</div>
            <a href="bim">BIM</a>
            <a href="simulasyon">Simülasyon & Analiz</a>
            <a href="tolerans-analizi">Tolerans Analizi</a>
            <a href="tasarim-otomasyonu">Tasarım Otomasyonu</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Dijital İkiz</div>
            <a href="dijital-ikiz">Dijital İkiz</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Üretim</div>
            <a href="fabrika-tasarimi">Fabrika Tasarımı</a>
            <a href="cam">CAM & İmalat</a>
            <a href="eklemeli-imalat">Eklemeli İmalat & 3D Baskı</a>
            <a href="nesting">Nesting</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Veri & Süreç Yönetimi</div>
            <a href="plm">PLM</a>
            <a href="pdm">PDM</a>
            <a href="insaat-yonetimi">İnşaat Proje Yönetimi</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Görselleştirme & Gerçeklik</div>
            <a href="gorsellestirme">Görselleştirme & Render</a>
            <a href="yaratici-icerik">Yaratıcı İçerik & Tasarım</a>
            <a href="gerceklik-yakalama">Gerçeklik Yakalama</a>
          </div>
          <div class="nav-mega-col">
            <div class="nav-dd-label">Sanatsal Baskı</div>
            <a href="sanatsal-baski"><span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span></a>

          </div>
        </div>
      </div>
    </li>
    <li class="nav-dropdown">
      <a href="endustriler">Endüstriler <i class="ti ti-chevron-down" style="font-size:11px;"></i></a>
      <div class="nav-dropdown-menu">
        <a href="sektor-mimari">Mimarlık</a>
        <a href="sektor-insaat">İnşaat & Altyapı</a>
        <a href="sektor-makine">Makine & Üretim</a>
        <a href="sektor-otomotiv">Otomotiv</a>
        <a href="sektor-medya">Medya & Eğlence</a>
        <a href="sektor-egitim">Eğitim</a>
        <a href="sektor-havacilik">Havacılık & Savunma</a>
      </div>
    </li>
    <li><a href="egitimler">Eğitimler</a></li>
    <li><a href="hakkimizda">Hakkımızda</a></li>
    <li><a href="iletisim">İletişim</a></li>
    <li><a href="kvkk">KVKK</a></li>
    <li><a href="blog">Blog</a></li>
    <li><a href="teklif-iste" class="nav-cta">Teklif Al</a></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-bg" style="background:radial-gradient(ellipse 70% 50% at 20% 0%,rgba(16,185,129,0.12) 0%,transparent 60%);"></div>
  <div class="hero-grid"></div>
  <div style="position:relative;z-index:1;">
    <div class="crumb"><a href="index.html">Anasayfa</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><a href="ultimaker">UltiMaker</a><i class="ti ti-chevron-right" style="font-size:11px;"></i><span style="color:var(--w50);">{name}</span></div>
    <div style="max-width:760px;">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:18px;">
        <div style="width:56px;height:56px;border-radius:12px;background:#10b9811f;border:.5px solid #10b98140;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti {icon}" style="font-size:26px;color:#10b981;"></i></div>
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
  <div style="border-radius:20px;overflow:hidden;border:.5px solid var(--w10);background:#fff;display:flex;justify-content:center;"><img src="{hero_img}" alt="{name} 3D yazıcı" style="max-width:100%;max-height:460px;display:block;" loading="lazy" decoding="async"></div>
</section>

<section class="section section-alt">
  <div class="sh"><div class="slabel">Öne Çıkan Özellikler</div><div class="stitle">{name} ile Neler Yapabilirsiniz?</div></div>
  <div class="grid g3">{features}</div>
</section>
<section class="section">
  <div class="sh"><div class="slabel">Kullanım Senaryoları</div><div class="stitle">Kimler İçin?</div></div>
  <div class="grid g3">{usecases}</div>
</section>

<section data-enrich-brand style="padding:60px 3rem;background:#0a1225;">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:#00c8f0;margin-bottom:8px;">Cadbim Farkı</div>
    <div style="font-family:'Manrope',sans-serif;font-size:clamp(1.3rem,2.4vw,1.7rem);font-weight:800;color:#fff;margin-bottom:8px;">UltiMaker Yatırımınızı Uçtan Uca Sahipleniyoruz</div>
    <p style="font-size:14px;color:rgba(255,255,255,.45);line-height:1.7;margin:0 0 26px;max-width:640px;">Lisans satışı işin başlangıcı — kurulumdan eğitime, destekten yenilemeye tüm yaşam döngüsü tek muhatapta.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-bottom:30px;">
   <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
     <div style="width:36px;height:36px;border-radius:10px;background:#10b9811a;color:#10b981;display:flex;align-items:center;justify-content:center;margin-bottom:12px;"><i class="ti ti-tool" style="font-size:18px;"></i></div>
     <h3 style="font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:#fff;margin:0 0 6px;">Yetkili Servis & Bakım</h3>
     <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">Kurulum, kalibrasyon, orijinal parça ve yıllık bakım anlaşmaları — yazıcınız hep üretimde.</p>
   </div>
   <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
     <div style="width:36px;height:36px;border-radius:10px;background:#10b9811a;color:#10b981;display:flex;align-items:center;justify-content:center;margin-bottom:12px;"><i class="ti ti-flask" style="font-size:18px;"></i></div>
     <h3 style="font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:#fff;margin:0 0 6px;">Malzeme Danışmanlığı</h3>
     <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">300+ malzeme arasından parça gereksiniminize uygun seçim ve doğrulanmış profiller.</p>
   </div>
   <div style="background:#0d1830;border:.5px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px 20px;">
     <div style="width:36px;height:36px;border-radius:10px;background:#10b9811a;color:#10b981;display:flex;align-items:center;justify-content:center;margin-bottom:12px;"><i class="ti ti-school" style="font-size:18px;"></i></div>
     <h3 style="font-family:'Manrope',sans-serif;font-size:14px;font-weight:700;color:#fff;margin:0 0 6px;">Operatör Eğitimi</h3>
     <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">Baskı hazırlığından filo yönetimine ekibinizi üretime hazırlıyoruz.</p>
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
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">3. Kurulum & Eğitim</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Dağıtım, yapılandırma ve rol bazlı kullanıcı eğitimi.</div>
     </div>
   </div>
   <div style="flex:1;min-width:170px;display:flex;gap:10px;align-items:flex-start;">
     <div style="width:30px;height:30px;border-radius:50%;background:#10b9811a;border:1px solid #10b98155;color:#10b981;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="ti ti-headset" style="font-size:14px;"></i></div>
     <div>
       <div style="font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:#fff;margin-bottom:3px;">4. Sürekli Destek</div>
       <div style="font-size:12px;color:rgba(255,255,255,.45);line-height:1.55;">Türkçe teknik destek ve yenileme dönemi hatırlatmaları.</div>
     </div>
   </div></div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="cross">
    <h3>İlgili ürünler ve çözümler</h3>
    <p class="cd">Birlikte değerlendirin</p>
    <div class="cpills">{cross_pills}</div>
  </div>
</section>
<div class="cta-strip">
  <h2>{name} teklifi alın</h2>
  <p>İhtiyacınıza uygun konfigürasyon ve eğitim planını birlikte belirleyelim.</p>
  <div class="cta-btns">
    <a href="teklif-iste" class="btn-p">Teklif İste <i class="ti ti-arrow-right"></i></a>
    <a href="egitimler" class="btn-g">Eğitim Programları</a>
  </div>
</div>
<footer>
  <div class="fbot">
    <p>© 2026 Cadbim — <a href="index.html" style="color:rgba(255,255,255,0.3);text-decoration:none;">Anasayfaya Dön</a> · <a href="kvkk" style="color:rgba(255,255,255,0.3);text-decoration:none;">KVKK</a> · <a href="javascript:void(0)" onclick="window.openCookiePrefs&&window.openCookiePrefs()" style="color:rgba(255,255,255,0.3);text-decoration:none;">Çerez Ayarları</a></p>
    <div class="socials">
      <a href="https://www.linkedin.com/company/cadbim/" aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a>
      <a href="https://www.youtube.com/c/CadbimTeknikDestek" aria-label="YouTube"><i class="ti ti-brand-youtube"></i></a>
      <a href="https://www.instagram.com/cadbim_izmir/" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a>
      <a href="https://www.facebook.com/cadbimizmir" aria-label="Facebook"><i class="ti ti-brand-facebook"></i></a>
    </div>
  </div>
</footer>
<script src="mobilenav.js?v=11" defer></script>
<script src="whatsapp-widget.js?v=1" defer></script>
<script src="social-widget.js?v=1" defer></script>
<script src="cookie-consent.js?v=2" defer></script>
</body></html>
"""

def card(icon, title, desc):
    return f'<div class="card"><div class="card-icon"><i class="ti {icon}"></i></div><h3>{title}</h3><p>{desc}</p></div>'

def cp(href, icon_or_img, label):
    if icon_or_img.startswith("img:"):
        img = icon_or_img[4:]
        inner = f'<img src="{img}" alt="" style="height:13px;width:auto;margin-right:6px;vertical-align:-2px;opacity:.85;filter:brightness(0) invert(1);" loading="lazy" decoding="async">'
    else:
        inner = f'<i class="ti {icon_or_img}"></i>'
    return f'<a href="{href}" class="cp">{inner}{label}</a>'

UM_LOGO = "img:assets/logos/ultimaker.svg"

CROSS_COMMON = [
    cp("ultimaker", UM_LOGO, "UltiMaker Marka Sayfası"),
    cp("cura", UM_LOGO, "UltiMaker Cura"),
    cp("digital-factory", "ti-cloud-cog", "Digital Factory"),
    cp("eklemeli-imalat", "ti-printer-3d", "Eklemeli İmalat Çözümleri"),
]

MODELS = {}

MODELS["s8"] = dict(
    slug="ultimaker-s8",
    name="UltiMaker S8",
    title="UltiMaker S8 Endüstriyel 3D Yazıcı | Cadbim",
    og_title="UltiMaker S8 | Cadbim",
    meta_desc="UltiMaker S8: Cheetah hareket planlayıcısı, 500 mm/s baskı hızı, 301+ malzeme desteği. Avrupa'da üretilen en hızlı çift malzemeli profesyonel 3D yazıcı. Cadbim yetkili iş ortağı.",
    icon="ti-bolt",
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
    cross_pills=CROSS_COMMON + [cp("ultimaker-s7", "ti-arrow-right", "UltiMaker S7 ile Karşılaştır")],
)

MODELS["s7"] = dict(
    slug="ultimaker-s7",
    name="UltiMaker S7",
    title="UltiMaker S7 3D Yazıcı | Cadbim",
    og_title="UltiMaker S7 | Cadbim",
    meta_desc="UltiMaker S7: Entegre Air Manager, PEI kaplı esnek tabla, endüktif otomatik seviyeleme ve 280+ malzeme desteği. Cadbim yetkili iş ortağı.",
    icon="ti-settings",
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
    cross_pills=CROSS_COMMON + [cp("ultimaker-s8", "ti-arrow-right", "UltiMaker S8 ile Karşılaştır"), cp("ultimaker-s5", "ti-arrow-right", "UltiMaker S5 ile Karşılaştır")],
)

MODELS["s5"] = dict(
    slug="ultimaker-s5",
    name="UltiMaker S5",
    title="UltiMaker S5 3D Yazıcı | Cadbim",
    og_title="UltiMaker S5 | Cadbim",
    meta_desc="UltiMaker S5: 330×240×300 mm büyük baskı hacmi, kompozit malzeme uyumlu çift ekstruder, ödüllü dokunmatik arayüz ve 280+ malzeme. Cadbim yetkili iş ortağı.",
    icon="ti-box-multiple",
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
    cross_pills=CROSS_COMMON + [cp("ultimaker-s7", "ti-arrow-right", "UltiMaker S7 ile Karşılaştır"), cp("ultimaker-s3", "ti-arrow-right", "UltiMaker S3 ile Karşılaştır")],
)

MODELS["s3"] = dict(
    slug="ultimaker-s3",
    name="UltiMaker S3",
    title="UltiMaker S3 3D Yazıcı | Cadbim",
    og_title="UltiMaker S3 | Cadbim",
    meta_desc="UltiMaker S3: Kompakt masaüstü mühendislik yazıcısı. Kompozite hazır çift ekstruder, otomatik tabla seviyeleme, 190+ malzeme desteği. Cadbim yetkili iş ortağı.",
    icon="ti-cube",
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
    cross_pills=CROSS_COMMON + [cp("ultimaker-s5", "ti-arrow-right", "UltiMaker S5 ile Karşılaştır")],
)

for key, m in MODELS.items():
    features_html = "".join(card(i, t, d) for i, t, d in m["features"])
    usecases_html = "".join(card(i, t, d) for i, t, d in m["usecases"])
    cross_html = "".join(m["cross_pills"])
    html = TEMPLATE.format(
        meta_desc=m["meta_desc"],
        title=m["title"],
        og_title=m["og_title"],
        slug=m["slug"],
        name=m["name"],
        icon=m["icon"],
        kicker=m["kicker"],
        h1=m["h1"],
        hero_p=m["hero_p"],
        video_src=m["video_src"],
        hero_img=m["hero_img"],
        features=features_html,
        usecases=usecases_html,
        cross_pills=cross_html,
    )
    out_path = os.path.join(BASE, f"cadbim_ultimaker_{key}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path, len(html), "bytes")
