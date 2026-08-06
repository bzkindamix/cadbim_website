# -*- coding: utf-8 -*-
"""Yeni sektor sayfalari uretir: sektor_yapi_urunleri.html, sektor_tuketici_urunleri.html.

sektor_otomotiv.html iskelet olarak kullanilir (head/CSS/nav/footer/katalog script'i
aynen alinir; nav ve footer bilerek degistirilmez -- Endustriler linkleri ayri bir
sitewide betikle eklenir). Hero, is akisi, cozum kartlari, markalar, urun katalogu
ve SSS bolumleri bu betikteki icerik sozluklerinden yeniden kurulur.

Renk semasi otomotivdeki iki tonlu (500/400) aksan mantigini izler:
  - ef4444 (500, ikon/workflow/FAQ aksani) -> ACC (base)
  - f87171 (400, rozet metni + h1 vurgusu) -> ACC_L (light)
Bu iki hex string'in her yerdeki (alfa/opacity varyantlari dahil) alt-dize
degisimi, otomotiv kopyasindaki tum renk kullanimlarini otomatik tasir.
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "sektor_otomotiv.html")

OLD_BASE = "ef4444"
OLD_BASE_RGB = "239,68,68"
OLD_LIGHT = "f87171"


def rgb(hex6):
    return "%d,%d,%d" % (int(hex6[0:2], 16), int(hex6[2:4], 16), int(hex6[4:6], 16))


# ---------------------------------------------------------------- ikon kutulari
def ico_img(kind, size=52, pad=5):
    if kind == "autodesk":
        inner = ('<img width="997" height="563" src="assets/logos/autodesk-white.svg?v=2" '
                 'alt="Autodesk" style="max-width:100%;max-height:100%;object-fit:contain;" '
                 'loading="lazy" decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "chaos":
        inner = ('<img width="1280" height="1280" src="assets/logos/chaos.webp" alt="Chaos" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" '
                 'decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "ultimaker":
        inner = ('<img width="150" height="22" src="assets/logos/ultimaker.svg" alt="UltiMaker" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;'
                 'filter:brightness(0) invert(1);opacity:.92;" loading="lazy" decoding="async">')
        box = "background:#0d1830;border:.5px solid rgba(255,255,255,0.12);"
    elif kind == "hp":
        inner = ('<img width="300" height="300" src="assets/logos/hp-blue.png" alt="HP" '
                 'style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" '
                 'decoding="async">')
        box = "background:#fff;"
    else:
        raise ValueError(kind)
    return ('<div style="width:%dpx;height:%dpx;border-radius:11px;%sdisplay:flex;'
            'align-items:center;justify-content:center;flex-shrink:0;padding:%dpx;">%s</div>'
            % (size, size, box, pad, inner))


def emb_img(name, size=40):
    return ('<img width="64" height="64" src="assets/img/%s" alt="" '
            'style="width:%dpx;height:%dpx;border-radius:8px;flex-shrink:0;" '
            'loading="lazy" decoding="async">' % (name, size, size))


def pcard(href, brand, title, desc, cat, icon_html):
    return ('      <a href="%s" class="pcard" data-cat="%s">%s<div><div class="pbrand">%s</div>'
            '<h3>%s</h3><p>%s</p></div><i class="ti ti-arrow-right parr"></i></a>'
            % (href, cat, icon_html, brand, title, desc))


def brand_row(icon_html, title, sub):
    return ('<div class="brand-row">\n          %s\n          <div><div class="brand-name">%s</div>'
            '<div style="font-size:11px;color:var(--w30);">%s</div></div>\n        </div>'
            % (icon_html, title, sub))


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
            'sans-serif;font-size:26px;font-weight:800;color:#%scc;">%s</div>\n'
            '    <i class="ti ti-%s" style="font-size:22px;color:#%s;display:block;'
            'margin-bottom:12px;"></i>\n'
            '    <h3 aria-level="2" style="font-family:\'Manrope\',sans-serif;font-size:14px;'
            'font-weight:700;color:#fff;margin:0 0 6px;">%s</h3>\n'
            '    <p style="font-size:12px;color:rgba(255,255,255,.5);line-height:1.6;margin:0;">'
            '%s</p>%s\n  </div>'
            % (acc, acc, acc, num, icon, acc, title, desc, arrow))


def sol_card(href, icon, title, desc):
    return ('    <a href="%s" class="card">\n'
            '      <div class="card-icon" style="background:rgba(0,200,240,.12);">'
            '<i class="ti ti-%s"></i></div>\n'
            '      <h3>%s</h3>\n      <p>%s</p>\n    </a>' % (href, icon, title, desc))


def faq_item(q, a):
    return ('<details class="cz-faq-i"><summary>%s<i class="ti ti-plus"></i></summary>'
            '<div class="cz-faq-a">%s</div></details>' % (q, a))


# ================================================================== ICERIK
SECTORS = {
    "yapiurunleri": {
        "file": "sektor_yapi_urunleri.html",
        "slug": "sektor-yapi-urunleri",
        "acc": "f97316",
        "acc_l": "fb923c",
        "name": "Yapı Ürünleri & Fabrikasyon",
        "crumb": "Yapı Ürünleri & Fabrikasyon",
        "badge": "Building Products &amp; Fabrication",
        "badge_icon": "building-warehouse",
        "title": "Yapı Ürünleri &amp; Fabrikasyon Çözümleri — Cadbim",
        "desc": ("Cadbim Yapı Ürünleri &amp; Fabrikasyon çözümleri — cephe, çelik konstrüksiyon "
                 "ve prefabrik eleman üreticileri için Advance Steel, Inventor ve Nesting ile "
                 "tasarımdan imalata tek veri seti."),
        "h1a": "Yapı Ürünleri &amp; Fabrikasyon için",
        "h1b": "Tasarımdan İmalata Tek Veri Seti",
        "hero_p": ("Cephe, çelik konstrüksiyon ve prefabrik yapı elemanı üreticileri için — "
                   "tasarım modelinden CNC kesime, revizyon kaybı olmadan."),
        "art_alt": "Yapı ürünleri iş akışı — çelik bağlantı detayı ve sac nesting yerleşimi",
        "svc_name": "Yapı Ürünleri &amp; Fabrikasyon Çözümleri",
        "wf_title": "Tasarımdan İmalata Fabrikasyon Akışı",
        "workflow": [
            ("pencil", "Ürün Tasarımı",
             "Inventor ve Revit ile panel, profil ve bağlantı detaylarının modellenmesi."),
            ("box-multiple", "Çelik &amp; Metal Detaylandırma",
             "Advance Steel ile kaynak, cıvata ve imalat detayları otomatik üretilir."),
            ("layout-grid", "Nesting &amp; Malzeme Optimizasyonu",
             "Sac ve levha parçaları, fire oranını düşüren otomatik yerleşimle kesime hazırlanır."),
            ("settings-2", "CAM &amp; CNC İmalat",
             "Fusion CAM ile takım yolu üretimi; kesim ve delik operasyonları tezgâha aktarılır."),
            ("building-factory-2", "Saha Montajı &amp; Teslim",
             "Navisworks ile yapı projesiyle koordinasyon; montaj paftaları ve as-built teslimi."),
        ],
        "sol_cards": [
            ("pdm", "folders", "PDM — Ürün Veri Yönetimi",
             "Panel ve profil revizyonlarını merkezi kasada tutar; imalat ekibi güncel veriyle çalışır."),
            ("plm", "hierarchy-3", "PLM — Ürün Yaşam Döngüsü",
             "Tasarım, tedarik ve imalat aynı ürün ağacına bakar; değişiklik onayları izlenebilir."),
            ("nesting", "layout-grid", "Nesting — Yuvalama",
             "Sac ve levha kesiminde malzeme israfını azaltan otomatik parça yerleştirme."),
            ("cam", "settings-2", "CAM &amp; İmalat",
             "Tasarım revizyonunu takım yoluna otomatik yansıtır; tezgâha göndermeden önce "
             "çarpışmayı gösterir."),
            ("fabrika-tasarimi", "building-factory-2", "Fabrika Tasarımı &amp; Dijital İkiz",
             "Üretim hattı yerleşimini kurulmadan önce sanal ortamda test eder."),
            ("tasarim-otomasyonu", "robot", "Tasarım Otomasyonu",
             "Tekrarlayan panel ve profil varyasyonlarını kural tabanlı otomasyonla üretir."),
            ("bim", "building", "BIM",
             "Yapı ürününüzü, uygulandığı projenin BIM modeliyle koordineli tutar."),
        ],
        "brands": [
            (ico_img("autodesk", 28, 4), "Autodesk", "Advance Steel, Inventor, Fusion, AutoCAD, Vault +3"),
            (ico_img("hp"), "HP", "HP Z Workstation, HP DesignJet"),
        ],
        "chips": [("c0", "Tasarım &amp; Detaylandırma"), ("c1", "İmalat &amp; CAM"),
                  ("c2", "Veri &amp; Süreç Yönetimi"), ("c3", "Koordinasyon"), ("c4", "Donanım")],
        "products": [
            ("pdm-collection", "Autodesk", "PD&amp;M Collection",
             "Inventor, AutoCAD, Fusion, Vault, Nastran, Nesting ve CAM tek pakette", "c0",
             '<div style="width:52px;height:52px;border-radius:11px;background:#0d1830;border:.5px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:5px;"><img width="340" height="310" src="assets/logos/products/pdm-collection.svg" alt="" style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" decoding="async"></div>'),
            ("advance-steel", "Autodesk", "Advance Steel",
             "Çelik konstrüksiyon detaylandırma ve imalat çıktıları", "c0", ico_img("autodesk")),
            ("inventor", "Autodesk", "Inventor",
             "Panel, profil ve bağlantı parçalarının parametrik tasarımı", "c0",
             emb_img("emb-7435829947.png")),
            ("autocad", "Autodesk", "AutoCAD",
             "2D imalat detayları ve şablon çizimleri", "c0", emb_img("emb-d437006e38.png")),
            ("nesting", "Autodesk", "Inventor Nesting",
             "Sac parça yerleşiminde malzeme optimizasyonu", "c1", ico_img("autodesk")),
            ("cam", "Autodesk", "Fusion CAM",
             "3D modelden doğrudan G-code", "c1", emb_img("emb-81b62f7fac.png")),
            ("fusion", "Autodesk", "Fusion",
             "CAD + CAM + Generative Design tek platform", "c1", emb_img("emb-81b62f7fac.png")),
            ("vault-pdm", "Autodesk", "Vault PDM",
             "Revizyon ve versiyon takibi merkezi kasada", "c2", emb_img("emb-08883a2089.png")),
            ("fusion-manage", "Autodesk", "Fusion Manage PLM",
             "Ürün ağacı ve değişiklik yönetimi", "c2", emb_img("emb-d28f96f25f.png")),
            ("autodesk", "Autodesk", "Navisworks",
             "Clash detection ve model koordinasyonu", "c3", emb_img("emb-9ab064fc9a.png")),
            ("hp", "HP", "HP Z Workstation",
             "CAD/CAM ve render performansı", "c4", ico_img("hp")),
            ("hp", "HP", "HP DesignJet",
             "İmalat paftaları için geniş format baskı", "c4", ico_img("hp")),
        ],
        "blog_topic": "Inventor",
        "cta_h2": "Yapı ürünleri projeniz için konuşalım",
        "faq": [
            ("Yapı ürünleri üreticileri için CADBİM hangi kapsamda çözüm sunuyor?",
             "Cephe, çelik konstrüksiyon ve prefabrik eleman üreticileri için tasarım modelinden "
             "imalat detayına, malzeme optimizasyonundan CNC kesime kadar tüm zinciri kapsıyoruz. "
             "Advance Steel ile çelik detaylandırma, Inventor ile panel/profil tasarımı, Nesting "
             "ile sac optimizasyonu ve Fusion CAM ile takım yolu üretimini tek veri seti üzerinden "
             "yürütüyoruz."),
            ("Advance Steel ile Revit arasındaki fark nedir?",
             "Revit, çelik yapıyı mimari/strüktürel modelle koordineli seviyede tutar; Advance "
             "Steel ise aynı yapıyı kaynak, cıvata ve profil kesim detayına indirir — imalat "
             "paftaları ve NC dosyaları buradan çıkar. Tasarım aşamasında Revit, imalat "
             "aşamasında Advance Steel devreye girer; ikisi arasında model verisi kopmadan akar."),
            ("Nesting yazılımı bize ne kazandırır?",
             "Sac ve levha parçalarını otomatik olarak plaka üzerine yerleştirip fire oranını "
             "düşürür; manuel yerleşimle kıyasla malzeme tasarrufu genellikle çift hanelidir. "
             "Parça listesi doğrudan kesim programına aktarılır, yeniden çizim gerekmez."),
            ("Mevcut AutoCAD çizimlerimizle Advance Steel'e geçebilir miyiz?",
             "Evet. Advance Steel, Revit tabanlı çalışır ama mevcut 2D detaylarınız referans "
             "olarak kullanılabilir; geçiş genellikle pilot bir proje üzerinde profil kütüphanesi "
             "ve bağlantı standardı kurulumuyla başlar. Cadbim bu kurulumu ve rol bazlı eğitimi "
             "birlikte planlar."),
            ("İmalat verimliliğini artırmak için hangi ürünü önce almalıyız?",
             "Tasarım-imalat kopukluğu en büyük kayıpsa Advance Steel veya Fusion CAM öncelik "
             "kazanır; malzeme fire oranı sorunsa Nesting daha hızlı geri dönüş sağlar. Cadbim, "
             "mevcut iş akışınızı inceleyip en yüksek etkiyi verecek başlangıç noktasını birlikte "
             "belirler."),
            ("Fabrika içi üretim hattı planlaması da bu kapsamda mı?",
             "Evet. Fabrika Tasarımı &amp; Dijital İkiz çözümümüzle üretim hattı yerleşimini "
             "kurulmadan önce sanal ortamda test ediyor, revizyon maliyetini üretime geçmeden "
             "ortadan kaldırıyoruz."),
        ],
    },
    "tuketici": {
        "file": "sektor_tuketici_urunleri.html",
        "slug": "sektor-tuketici-urunleri",
        "acc": "3b82f6",
        "acc_l": "60a5fa",
        "name": "Tüketici Ürünleri",
        "crumb": "Tüketici Ürünleri",
        "badge": "Consumer Products",
        "badge_icon": "package",
        "title": "Tüketici Ürünleri Çözümleri — Cadbim",
        "desc": ("Cadbim Tüketici Ürünleri çözümleri — Fusion, Inventor, Alias ve UltiMaker ile "
                 "endüstriyel tasarımdan seri üretime konsept-üretim döngüsü."),
        "h1a": "Tüketici Ürünleri için",
        "h1b": "Konseptten Seri Üretime Tek Platform",
        "hero_p": ("Mobilya, beyaz eşya, ambalaj ve elektronik muhafazalar — endüstriyel tasarım, "
                   "mühendislik doğrulama ve üretime geçiş tek platformda."),
        "art_alt": "Tüketici ürünleri iş akışı — enjeksiyon kalıbı kesiti ve render viewport",
        "svc_name": "Tüketici Ürünleri Çözümleri",
        "wf_title": "Konseptten Seri Üretime Ürün Akışı",
        "workflow": [
            ("bulb", "Endüstriyel Tasarım",
             "Alias ve Fusion ile hızlı konsept modelleme ve form çalışması."),
            ("settings-2", "Mühendislik &amp; Detay",
             "Inventor ile mekanizma, montaj ve enjeksiyon parça tasarımı."),
            ("chart-dots-3", "Simülasyon &amp; Doğrulama",
             "Fusion Simulation ile yapısal ve termal doğrulama."),
            ("cube-3d-sphere", "Fiziksel Prototip",
             "UltiMaker ile fonksiyonel prototip ve kullanıcı testi parçaları."),
            ("sun-high", "Pazarlama Görselleştirme",
             "Chaos V-Ray ile katalog ve pazarlama kalitesinde fotogerçekçi render."),
        ],
        "sol_cards": [
            ("plm", "hierarchy-3", "PLM — Ürün Yaşam Döngüsü",
             "Tasarım, tedarik ve üretim aynı ürün ağacına bakar; NPI süreci izlenebilir."),
            ("pdm", "folders", "PDM — Ürün Veri Yönetimi",
             "CAD dosyalarının revizyon geçmişini merkezi kasada tutar."),
            ("simulasyon", "chart-dots-3", "Simülasyon &amp; Analiz",
             "Yapısal ve akış davranışını fiziksel prototipe geçmeden test eder."),
            ("tasarim-otomasyonu", "robot", "Tasarım Otomasyonu",
             "Ürün ailesi varyasyonlarını kural tabanlı otomasyonla üretir."),
            ("eklemeli-imalat", "cube-3d-sphere", "Eklemeli İmalat &amp; 3D Baskı",
             "UltiMaker donanımıyla prototipten fonksiyonel parçaya 3B baskı."),
            ("cam", "settings-2", "CAM &amp; İmalat",
             "Enjeksiyon kalıbı ve CNC parçaları için takım yolu üretimi."),
            ("gorsellestirme", "sun-high", "Görselleştirme &amp; Render",
             "Konsept eskizinden pazarlama görseline fotogerçekçi render hattı."),
        ],
        "brands": [
            (ico_img("autodesk", 28, 4), "Autodesk", "Fusion, Inventor, Alias, Vault +3"),
            (ico_img("chaos"), "Chaos", "Chaos V-Ray"),
            (ico_img("ultimaker"), "UltiMaker", "UltiMaker S8 / S7"),
            (ico_img("hp"), "HP", "HP Z Workstation, HP ZBook"),
        ],
        "chips": [("c0", "Endüstriyel Tasarım"), ("c1", "Mühendislik &amp; Simülasyon"),
                  ("c2", "Görselleştirme"), ("c3", "Prototip &amp; Üretim"), ("c4", "Veri Yönetimi"),
                  ("c5", "Donanım")],
        "products": [
            ("pdm-collection", "Autodesk", "PD&amp;M Collection",
             "Inventor, AutoCAD, Fusion, Vault, Nastran, Nesting ve CAM tek pakette", "c0",
             '<div style="width:52px;height:52px;border-radius:11px;background:#0d1830;border:.5px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:5px;"><img width="340" height="310" src="assets/logos/products/pdm-collection.svg" alt="" style="max-width:100%;max-height:100%;object-fit:contain;" loading="lazy" decoding="async"></div>'),
            ("alias", "Autodesk", "Alias Concept",
             "Hızlı konsept modelleme ve form çalışması", "c0", emb_img("emb-a278c108d7.png")),
            ("fusion", "Autodesk", "Fusion",
             "Endüstriyel tasarım + mühendislik tek platformda", "c0", emb_img("emb-81b62f7fac.png")),
            ("inventor", "Autodesk", "Inventor",
             "Mekanizma, montaj ve enjeksiyon parça tasarımı", "c1", emb_img("emb-7435829947.png")),
            ("simulasyon", "Autodesk", "Fusion Simulation",
             "Entegre FEA ve termal analiz", "c1", emb_img("emb-81b62f7fac.png")),
            ("chaos", "Chaos", "Chaos V-Ray",
             "Katalog ve pazarlama kalitesinde fotogerçekçi render", "c2", ico_img("chaos")),
            ("ultimaker", "UltiMaker", "UltiMaker S8 / S7",
             "Fonksiyonel prototip ve kullanıcı testi parçaları", "c3", ico_img("ultimaker")),
            ("cam", "Autodesk", "Fusion CAM",
             "Enjeksiyon kalıbı ve CNC takım yolu", "c3", emb_img("emb-81b62f7fac.png")),
            ("vault-pdm", "Autodesk", "Vault PDM",
             "CAD dosya yönetimi, versiyon takibi", "c4", emb_img("emb-08883a2089.png")),
            ("fusion-manage", "Autodesk", "Fusion Manage PLM",
             "NPI, BOM, değişiklik yönetimi", "c4", emb_img("emb-d28f96f25f.png")),
            ("hp", "HP", "HP Z Workstation",
             "Render ve simülasyon performansı", "c5", ico_img("hp")),
            ("hp", "HP", "HP ZBook",
             "Mobil endüstriyel tasarım iş istasyonu", "c5", ico_img("hp")),
        ],
        "blog_topic": "Fusion",
        "cta_h2": "Tüketici ürünleri projeniz için konuşalım",
        "faq": [
            ("Tüketici ürünleri geliştirmede CADBİM hangi kapsamda çözüm sunuyor?",
             "Endüstriyel tasarım stüdyosundan mühendislik doğrulamasına, simülasyondan "
             "seri üretime geçişe kadar tüketici ürünü değer zincirinin tamamına yazılım ve "
             "donanım çözümü sunuyoruz. Alias/Fusion ile konsept, Inventor ile mühendislik "
             "ve UltiMaker ile prototip — tek entegre akış."),
            ("Alias ile Fusion arasında hangisini seçmeliyiz?",
             "Alias, serbest form endüstriyel tasarım ve Class-A yüzey için tasarlanmıştır; "
             "estetik onayı bu araçla verilir. Fusion ise tasarımı doğrudan mühendislik, "
             "simülasyon ve CAM'e bağlar — küçük ve orta ölçekli ekiplerde tek platform yeterli "
             "olabilir. Kapsamı ürün karmaşıklığınıza göre birlikte belirleriz."),
            ("UltiMaker ile alınan prototip seri üretim parçasıyla aynı mı davranır?",
             "FFF baskı, fonksiyon ve montaj testine uygun malzeme davranışı verir ama enjeksiyon "
             "parçasının yüzey kalitesi ve nihai mekanik özellikleriyle bire bir örtüşmez. "
             "Prototip; form, montaj ve kullanıcı testi içindir — üretim onayı "
             "fiziksel numune ile birlikte verilir."),
            ("Render'larımızı katalog ve e-ticaret için kullanabilir miyiz?",
             "Evet. Chaos V-Ray ile üretilen görseller, fotoğraf çekimine gerek kalmadan katalog, "
             "e-ticaret ve pazarlama materyali kalitesinde kullanılabilir; ürün henüz üretime "
             "girmeden pazarlama materyali hazırlanabilir."),
            ("PLM/PDM küçük ürün ekiplerinde de gerekli mi?",
             "Ekip büyüklüğünden çok revizyon sıklığı ve tedarikçi sayısı belirleyicidir. Birden "
             "fazla kişi aynı CAD dosyasına dokunuyorsa PDM (Vault), ürün ağacı ve BOM "
             "tedarikçiyle paylaşılıyorsa PLM (Fusion Manage) katkı sağlar. İhtiyaç analiziyle "
             "doğru başlangıç noktasını birlikte belirleriz."),
        ],
    },
}


# ================================================================ BOLUM KURUCULAR
def build_hero(c):
    acc, accl = c["acc"], c["acc_l"]
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
      <div lang="en" class="hero-badge" style="background:rgba(""" + rgb(acc) + """,0.12);border-color:#""" + accl + """40;color:#""" + accl + """;">
        <i class="ti ti-""" + c["badge_icon"] + """" style="font-size:18px;color:#""" + acc + """;"></i>  """ + c["badge"] + """
      </div>
      <h1 class="sec-h1">""" + c["h1a"] + """<br><span style="color:#""" + accl + """;">""" + c["h1b"] + """</span></h1>
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
    cards = "\n".join(sol_card(h, i, t, d) for h, i, t, d in c["sol_cards"])
    return ('<section class="section" style="padding-top:0;">\n'
            '  <div class="sh">\n    <div class="slabel">Çözümler</div>\n'
            '    <div class="stitle" role="heading" aria-level="2">Bu Sektörün İşini Çözen '
            'Yaklaşımlar</div>\n'
            '    <p class="ssub">Her çözüm, birden fazla Cadbim ürününü tek iş akışında '
            'birleştirir.</p>\n  </div>\n'
            '  <div class="grid g3" style="margin-top:0;">\n' + cards + '\n  </div>\n</section>\n')


def build_brands(c):
    rows = "".join(brand_row(icon, t, s) for icon, t, s in c["brands"])
    return ('<section class="brands">\n'
            '  <div class="sh" style="margin-bottom:22px;">\n'
            '    <div class="slabel">Markalar</div>\n'
            '    <div class="stitle" role="heading" aria-level="2">Arkanızda Yetkili İş '
            'Ortakları Var</div>\n'
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
    cards = "\n".join(pcard(*p) for p in c["products"])
    return ('<section class="solutions" id="urun-katalogu">\n'
            '  <div class="sol-header">\n'
            '    <div class="sol-label">Ürünler</div>\n'
            '    <div class="sol-title">' + c["name"] + ' için kullandığımız ürünler</div>\n'
            '  </div>\n'
            '  <div class="pfilter" id="pfilter">\n' + chips + '\n'
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
            "    var temizle=ch.classList.contains('active');\n"
            "    chips.forEach(function(x){x.classList.remove('active');});\n"
            "    if(!temizle) ch.classList.add('active');\n"
            "    f=temizle?'all':ch.getAttribute('data-f'); apply();\n  });});\n"
            "  document.getElementById('psearch').addEventListener('input',function(e){\n"
            "    q=e.target.value.trim().toLowerCase(); apply();\n  });\n})();\n</script>\n")


def build_faq(c):
    items = "".join(faq_item(q, a) for q, a in c["faq"])
    return ('<!-- cz-faq -->\n'
            '<section class="section section-alt cz-sec" style="--cz:#' + c["acc"] + ';">\n'
            '  <div class="sh">\n'
            '    <div class="slabel" style="color:var(--cz);">Sıkça Sorulanlar</div>\n'
            '    <div class="stitle" role="heading" aria-level="2">Bu sektör hakkında merak '
            'edilenler</div>\n  </div>\n'
            '  <div class="cz-faq">' + items + '</div>\n'
            '  <div class="cz-faq-cta">\n    <span>Sorunuz listede yok mu?</span>\n'
            '    <a href="iletisim#form" class="btn-p">Uzmanımıza Sorun '
            '<i class="ti ti-arrow-right"></i></a>\n  </div>\n</section>\n<!-- /cz-faq -->\n')


def faq_plain(a):
    return re.sub(r"<[^>]+>", "", a).replace("&amp;", "&")


# ================================================================== MONTAJ
def build_page(key):
    c = dict(SECTORS[key]); c["key"] = key
    acc, accl = c["acc"], c["acc_l"]
    tpl = io.open(TPL, encoding="utf-8").read()

    head, _, rest = tpl.partition("</nav></header>\n")
    body, _, foot = rest.partition('<footer id="iletisim">')
    head_only = head.split("<body>")[0] + "<body>\n"
    nav = head.split("<body>")[1] + "</nav></header>\n"

    name_plain = c["name"]
    title_plain = c["title"].replace("&amp;", "&")
    desc_plain = c["desc"].replace("&amp;", "&")
    svc_plain = c["svc_name"].replace("&amp;", "&")

    # --- head: renk tonlari (global alt-dize degisimi -- alfa varyantlarini da tasir) ---
    head_only = (head_only.replace(OLD_LIGHT, accl).replace(OLD_BASE, acc)
                 .replace(OLD_BASE_RGB, rgb(acc)))

    # --- head: meta/SEO metin degisimleri (yalniz head_only kapsaminda) ---
    rep = [
        ('content="Cadbim Otomotiv çözümleri — Konsept tasarımdan üretim yüzeyine — otomotiv '
         'stüdyosunun endüstri standardı araçları."', 'content="%s"' % desc_plain),
        ("<title>Otomotiv Çözümleri — Cadbim</title>", "<title>%s</title>" % title_plain),
        ('content="Otomotiv Çözümleri — Cadbim"', 'content="%s"' % title_plain),
        ("sektor-otomotiv", c["slug"]),
        ("sektor_otomotiv.png", "%s.png" % c["file"].replace(".html", "")),
    ]
    for old, new in rep:
        head_only = head_only.replace(old, new)

    # --- head: JSON-LD (json.loads ile guvenli mutasyon) ---
    m = re.search(r'<script type="application/ld\+json">\n(.*?)\n</script>', head_only, re.S)
    assert m, "%s: JSON-LD bulunamadi" % key
    data = json.loads(m.group(1))
    for node in data["@graph"]:
        if node.get("@type") == "WebPage":
            node["name"] = title_plain
            node["description"] = desc_plain
        elif node.get("@type") == "BreadcrumbList":
            node["itemListElement"][2]["name"] = svc_plain
        elif node.get("@type") == "Service":
            node["name"] = svc_plain
            node["description"] = desc_plain
        elif node.get("@type") == "FAQPage":
            node["mainEntity"] = [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": faq_plain(a)}}
                for q, a in c["faq"]
            ]
    new_json = json.dumps(data, ensure_ascii=False, indent=1)
    head_only = head_only[:m.start(1)] + new_json + head_only[m.end(1):]

    # --- govde: Calisma Modelimiz blogu (renk otomatik tasindi, aksan tokenlari zaten degisti) ---
    mm = re.search(r'<section data-enrich[^>]*>(?:(?!</section>).)*?Çalışma Modelimiz.*?\n</section>\n',
                   body, re.S)
    model = mm.group(0).replace(OLD_LIGHT, accl).replace(OLD_BASE, acc)
    m2 = re.search(r'<div class="cta-wrap">.*?\n</div>\n', body, re.S)
    ctawrap = m2.group(0)
    ctawrap = re.sub(r'data-topic="[^"]*"', 'data-topic="%s"' % c["blog_topic"], ctawrap)
    ctawrap = re.sub(r'<h2>[^<]*</h2>', '<h2>%s</h2>' % c["cta_h2"], ctawrap)

    out = (head_only + nav + "\n"
           + build_hero(c) + "\n"
           + build_workflow(c) + "\n"
           + build_solutions(c) + "\n"
           + build_brands(c) + "\n"
           + build_catalog(c) + "\n"
           + model + "\n"
           + build_faq(c)
           + ctawrap
           + '<footer id="iletisim">' + foot)
    path = os.path.join(ROOT, c["file"])
    io.open(path, "w", encoding="utf-8", newline="\n").write(out)
    return path, len(out)


if __name__ == "__main__":
    for key in SECTORS:
        p, n = build_page(key)
        print("OK %-30s %d bayt" % (os.path.basename(p), n))
