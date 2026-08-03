# -*- coding: utf-8 -*-
"""sektor_tesisat / sektor_icmimarlik sayfalarini cozum sayfasi derinligine cikarir.

Paralel oturumun cozum sayfalarina kurdugu desenle ayni bilesenler eklenir
(hepsi design-system.css'te tanimli cz-* siniflari):
  - hero altina olcut seridi (cz-stats)
  - "Bu Sektorde Yaklasimimiz" metin blogu (cz-intro + cz-buls)
  - "Neler Sunuyoruz?" kapsam kartlari
  - SSS (details/summary + head'e FAQPage JSON-LD)

Icerik, CADBIM'in kendi urun sayfalarindaki marka kaynakli olgulardan derlendi
(fabrication_cadmep/camduct/estmep, cfd, sketchup_pro, corona, enscape, lumion,
designjet_z9pro) — kurumsal Turkce ile yeniden yazildi. Betik idempotenttir.
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "sektor_tesisat.html": {
        "acc": "#2dd4bf",
        "stats": [
            ("LOD 400", "imalat detayında MEP modelleme — Fabrication CADmep"),
            ("7.000+", "üretici katalog öğesiyle gerçek maliyet verisi — ESTmep"),
            ("Tek veritabanı", "tahmin, detay ve imalat aynı model üzerinde"),
        ],
        "intro_label": "Bu Sektörde Yaklaşımımız",
        "intro_title": "Tesisatta model, imalatın kendisidir",
        "intro_ps": [
            "Mekanik tesisatta en pahalı hatalar, çizim ile imalat arasındaki kopukluktan doğar. "
            "Autodesk'in MEP yaklaşımında model yalnızca bir koordinasyon aracı değil, "
            "<strong>imalatın doğrudan girdisidir</strong>: Revit'te kurulan kanal, boru ve "
            "elektrik sistemleri, Fabrication ailesiyle LOD 400 imalat detayına indirilir.",
            "Fabrication CADmep, ESTmep ve CAMduct <strong>ortak bir veritabanını</strong> paylaşır — "
            "maliyet tahmini, detaylandırma ve imalat aynı model üzerinden ilerler; veri yeniden "
            "girilmez, parça yeniden modellenmez. Kanal geometrisi yeniden çizilmeden doğrudan "
            "CNC kesim makinelerine gönderilir.",
            "Hesap tarafında Autodesk CFD, hava ve sıvı akışını üretim öncesinde simüle eder; "
            "basınç kaybı, türbülans ve sıcaklık dağılımı masada doğrulanır. Bu, Navisworks "
            "çakışma rutiniyle birleştiğinde, şantiyede kesip kaynakla çözülecek çarpışmalar "
            "tasarım aşamasında kapanır.",
        ],
        "buls": [
            ("LOD 400 detay",
             "Kanal, boru ve kablo tesisatı imalat detayında modellenir; çakışma riski "
             "şantiyeden önce görünür."),
            ("Ortak veritabanı",
             "CADmep, ESTmep ve CAMduct aynı proje verisini paylaşır — tekrar modelleme ve "
             "veri kaybı olmaz."),
            ("Üretici bazlı maliyet",
             "90'dan fazla üreticinin 7.000'i aşkın katalog öğesiyle gerçek fiyat ve ürün "
             "verisine dayanan tahmin."),
            ("CNC'ye doğrudan çıkış",
             "CAMduct parça geometrisini yeniden çizmeden kesim makinelerine aktarır; sac "
             "kanal imalatı hızlanır."),
        ],
        "scope_title": "Mekanik Tesisat İçin Neler Sunuyoruz?",
        "scope": [
            ("wind", "Havalandırma & Kanal Tasarımı",
             "Revit MEP ile mimari modelle koordineli kanal sistemleri; debi ve kesit bilgisi "
             "modelin içinde taşınır."),
            ("droplet", "Sıhhi Tesisat & Borulama",
             "Gidiş-dönüş hatları, kolon şemaları ve bağlantı detayları tek modelden pafta "
             "üretimiyle belgelenir."),
            ("temperature", "HVAC Analizi",
             "Autodesk CFD ile sıcaklık dağılımı, basınç düşüşü ve ısıl konfor analizi — "
             "üretimden önce, masada."),
            ("settings", "İmalat Detaylandırma",
             "Fabrication CADmep ile spool çizimleri; üretici kütüphanelerinden gerçek "
             "parçalarla LOD 400 model."),
            ("file-text", "Metraj & Maliyet",
             "ESTmep detaylandırma modelinden doğrudan miktar çeker; teklif süresi kısalır, "
             "isabet artar."),
            ("crane", "Saha Koordinasyonu",
             "Navisworks çakışma kontrolü ve BIM Collaborate Pro ile montaj planlaması, pafta "
             "dağıtımı ve as-built."),
        ],
        "faq": [
            ("Revit varken Fabrication ailesine neden ihtiyaç duyayım?",
             "Revit tesisatı tasarım ve koordinasyon seviyesinde modeller; Fabrication CADmep "
             "aynı sistemi üretici parçalarıyla LOD 400 imalat detayına indirir. Taahhüt "
             "tarafında spool çizimi, kesim listesi ve CNC çıkışı gerekiyorsa Fabrication "
             "devreye girer; yalnızca tasarım yapıyorsanız Revit yeterli olabilir. Kapsamı "
             "iş modelinize göre birlikte netleştiririz."),
            ("CADmep, ESTmep ve CAMduct'ı birlikte mi almalıyım?",
             "Zorunlu değil; ancak üçlü aynı veritabanını paylaştığı için birlikte en yüksek "
             "verimi verir. Teklif ağırlıklı çalışan firmalarda ESTmep, imalathanesi olan "
             "firmalarda CAMduct öncelik kazanır. Cadbim ihtiyaç analiziyle doğru başlangıç "
             "noktasını belirler."),
            ("Autodesk CFD'yi kimler kullanmalı?",
             "Klima santrali seçimi, temiz oda, veri merkezi soğutması gibi akışın kritik "
             "olduğu projelerde; sıcaklık dağılımını ve basınç kaybını üretimden önce "
             "doğrulamak isteyen mekanik proje ofisleri ile Ar-Ge ekiplerinde. CAD modelinden "
             "doğrudan analiz ortamına geçilir; geometri yeniden oluşturulmaz."),
            ("Mevcut AutoCAD çizimlerimizle başlayabilir miyiz?",
             "Evet. CADmep, AutoCAD tabanı üzerinde çalışır ve DWG altyapınız korunur; geçiş "
             "genellikle pilot bir proje üzerinde şablon ve kütüphane kurulumuyla başlar. "
             "Cadbim kurulumu, içeriği ve rol bazlı eğitimi tek planda yürütür."),
        ],
    },
    "sektor_icmimarlik.html": {
        "acc": "#f472b6",
        "stats": [
            ("1.000+", "SketchUp eklentisi; LayOut belgeleme ve Trimble Connect dahil"),
            ("12'ye varan", "pigment mürekkeple galeri kalitesinde baskı — DesignJet Z9+"),
            ("Gerçek zamanlı", "Enscape ve Lumion ile anında müşteri sunumu"),
        ],
        "intro_label": "Bu Sektörde Yaklaşımımız",
        "intro_title": "Konsept ile sunum arasındaki mesafeyi kapatıyoruz",
        "intro_ps": [
            "İç mimarlık projelerinde karar, müşteri sunumunda verilir — kazanan, fikrini en "
            "hızlı ve en inandırıcı gösteren ekiptir. SketchUp Pro; masaüstü, web ve iPad'de "
            "çalışan modelleme ortamıyla mekân kurgusunu hızlandırır, <strong>LayOut ile teknik "
            "belgeleme aynı dosyadan</strong> üretilir.",
            "Görselleştirmede Chaos Corona, iç mekân için tasarlanmış render motorudur: "
            "<strong>fiziksel doğruluk varsayılan olarak açıktır</strong> — karmaşık ayar "
            "denizine girmeden doğal ışık ve gerçekçi malzemeyle sonuç alınır; kumaş, deri ve "
            "metal yüzeyler gerçek dünyadan taranmış, fizik tabanlı kütüphaneden gelir. Daha "
            "derin kontrol isteyen stüdyolar aynı ekosistem içinde V-Ray'e geçer.",
            "Sunum tarafında Enscape, SketchUp'ın içinde gerçek zamanlı çalışır — modeldeki her "
            "değişiklik render görünümüne eş zamanlı yansır; Lumion sürükle-bırak sadelikte "
            "atmosferik iç mekân animasyonu üretir. Son adımda panolar HP DesignJet Z ile "
            "galeri kalitesinde basılır.",
        ],
        "buls": [
            ("Üç platformda modelleme",
             "SketchUp Pro masaüstü, web ve iPad'de çalışır; Trimble Connect bulut depolama "
             "dahildir."),
            ("Kutudan çıkan fotogerçekçilik",
             "Corona'da sahneyi kurun, render alın — malzeme ve ışık değişiklikleri anında "
             "görünür."),
            ("Eş zamanlı tasarım-render",
             "Enscape'te SketchUp, Revit veya Rhino'daki her değişiklik render penceresinde "
             "canlı güncellenir."),
            ("Sunumdan baskıya",
             "Photoshop ve InDesign panoları, DesignJet Z'de 12'ye varan pigment mürekkeple "
             "basılır."),
        ],
        "scope_title": "İç Mimarlık İçin Neler Sunuyoruz?",
        "scope": [
            ("armchair", "Mekân Planlama & Yerleşim",
             "SketchUp ile hacim etüdü, mobilya yerleşimi ve alternatif senaryolar; LayOut ile "
             "ölçekli pafta."),
            ("sun-high", "Fotogerçekçi İç Mekân Render",
             "Chaos Corona ve V-Ray ile doğal ışık, doğru malzeme ve stüdyo kalitesinde kare."),
            ("movie", "Gerçek Zamanlı Gezinti & Animasyon",
             "Enscape ile model içinde canlı gezinti ve VR; Lumion ile atmosferik tanıtım "
             "videosu."),
            ("palette", "Malzeme & Doku Kurgusu",
             "Fizik tabanlı malzeme kütüphaneleri; kumaş, ahşap ve metalin ışıkla doğru "
             "ilişkisi."),
            ("file-text", "Sunum Panoları & Portfolyo",
             "Photoshop post-prodüksiyonu ve InDesign ile konsept panoları, teklif ve "
             "portfolyo dosyaları."),
            ("wand", "Galeri Kalitesinde Baskı",
             "Sanatsal Baskı Atölyesi'nde 64 inç genişliğe kadar fine art baskı — kanvas dahil "
             "medya seçenekleri."),
        ],
        "faq": [
            ("Corona mı V-Ray mi seçmeliyim?",
             "Corona, iç mekân görselleştirmede sadelik ve hız için tasarlandı — fiziksel "
             "doğruluk varsayılan açık, sahneyi kurup render alırsınız. V-Ray ışık ve "
             "malzemede daha derin kontrol ister ve büyük ya da karma sahnelerde esneklik "
             "sunar. İkisi de Chaos ekosistemindedir; ekibinizin profiline göre yönlendiririz."),
            ("SketchUp Pro iç mimarlık ofisi için yeterli mi?",
             "Modelleme ve LayOut belgeleme için çoğu ofiste evet; 1.000'den fazla eklentiyle "
             "genişletilir. Tarama verisiyle rölöve (Scan Essentials) veya V-Ray render'ını da "
             "tek pakette isteyen ekipler için SketchUp Studio planı bulunur."),
            ("Render için nasıl bir iş istasyonu gerekir?",
             "Motora bağlıdır: Enscape ve Lumion GPU ağırlıklı çalışır; Corona ve V-Ray "
             "CPU-GPU dengesi ister. HP Z serisinde, kullandığınız yazılıma göre konfigürasyon "
             "öneriyoruz — ne eksik ne fazla."),
            ("Sunum panolarımızı sizde basabilir miyiz?",
             "Evet. Sanatsal Baskı Atölyemizde HP DesignJet Z9+ ile 64 inç genişliğe kadar, "
             "12'ye varan pigment mürekkeple galeri kalitesinde baskı alıyoruz; kanvas dahil "
             "medya seçeneklerini birlikte belirleriz."),
        ],
    },
}


def build_stats(c):
    cells = "".join('<div class="cz-stat"><b>%s</b><span>%s</span></div>' % (b, s)
                    for b, s in c["stats"])
    return ('      <!-- cz-stats -->\n'
            '      <div class="cz-stats" style="--cz:%s;">%s</div>\n'
            '      <!-- /cz-stats -->\n' % (c["acc"], cells))


def build_intro(c):
    ps = "\n".join('        <p class="cz-p">%s</p>' % p for p in c["intro_ps"])
    buls = "".join('<div class="cz-bul"><i class="ti ti-circle-check"></i><div>'
                   '<h3>%s</h3><p>%s</p></div></div>' % (t, d) for t, d in c["buls"])
    return ('<!-- cz-intro -->\n'
            '<section class="section cz-sec" style="--cz:%s;">\n'
            '  <div class="cz-intro">\n'
            '    <div class="cz-intro-h">\n'
            '      <div class="slabel" style="color:var(--cz);">%s</div>\n'
            '      <div class="stitle">%s</div>\n'
            '    </div>\n'
            '    <div class="cz-intro-b">\n%s\n    </div>\n'
            '  </div>\n'
            '  <div class="cz-buls">%s</div>\n'
            '</section>\n'
            '<!-- /cz-intro -->\n' % (c["acc"], c["intro_label"], c["intro_title"], ps, buls))


def build_scope(c):
    cards = "".join(
        '<div class="card"><div class="card-icon"><i class="ti ti-%s" '
        'style="color:%s;"></i></div><h3>%s</h3><p>%s</p></div>'
        % (icon, c["acc"], t, d) for icon, t, d in c["scope"])
    return ('<section class="section section-alt">\n'
            '  <div class="sh"><div class="slabel">Kapsam</div>'
            '<div class="stitle">%s</div></div>\n'
            '  <div class="grid g3">%s</div>\n'
            '</section>\n' % (c["scope_title"], cards))


def build_faq(c):
    items = "".join(
        '<details class="cz-faq-i"><summary>%s<i class="ti ti-plus"></i></summary>'
        '<div class="cz-faq-a">%s</div></details>' % (q, a) for q, a in c["faq"])
    return ('<!-- cz-faq -->\n'
            '<section class="section section-alt cz-sec" style="--cz:%s;">\n'
            '  <div class="sh">\n'
            '    <div class="slabel" style="color:var(--cz);">Sıkça Sorulanlar</div>\n'
            '    <div class="stitle">Bu sektör hakkında merak edilenler</div>\n'
            '  </div>\n'
            '  <div class="cz-faq">%s</div>\n'
            '  <div class="cz-faq-cta">\n'
            '    <span>Sorunuz listede yok mu?</span>\n'
            '    <a href="iletisim#form" class="btn-p">Uzmanımıza Sorun '
            '<i class="ti ti-arrow-right"></i></a>\n'
            '  </div>\n'
            '</section>\n'
            '<!-- /cz-faq -->\n' % (c["acc"], items))


def faq_jsonld(c):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer",
                                "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in c["faq"]
        ],
    }


def enrich(fname):
    c = DATA[fname]
    p = os.path.join(ROOT, fname)
    s = io.open(p, encoding="utf-8").read()
    if "cz-intro" in s:
        print("%s: zaten zengin, atlandi" % fname)
        return

    # 1) hero'ya olcut seridi (butonlarin hemen altina, sol sutun kapanmadan)
    m = re.search(r'(<a href="egitimler" class="btn-g">Eğitim Programları</a>\n      </div>\n)',
                  s)
    assert m, "%s: hero buton blogu bulunamadi" % fname
    s = s[:m.end()] + build_stats(c) + s[m.end():]

    # 2) intro + kapsam, Is Akisi'ndan once
    i = s.index("\n<section data-enrich")
    s = s[:i] + "\n" + build_intro(c) + build_scope(c) + s[i + 1:]

    # 3) SSS, blog+CTA'dan once
    i = s.index('<div class="cta-wrap">')
    s = s[:i] + build_faq(c) + "\n" + s[i:]

    # 4) FAQPage JSON-LD: @graph dizisine ekle
    m = re.search(r'(\n \]\n\}\n</script>)', s)
    assert m, "%s: JSON-LD graph kapanisi bulunamadi" % fname
    block = json.dumps(faq_jsonld(c), ensure_ascii=False, indent=1)
    block = "\n".join("  " + ln for ln in block.splitlines())
    s = s[:m.start()] + ",\n" + block + s[m.start() + 1:]

    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("%s: zenginlestirildi (%d bayt)" % (fname, len(s)))


if __name__ == "__main__":
    for f in DATA:
        enrich(f)
