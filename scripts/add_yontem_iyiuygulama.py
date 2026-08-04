# -*- coding: utf-8 -*-
"""Eksik "Yontemimiz" ve "Iyi Uygulamalar" bolumlerini ekler.

18 cozum sayfasinin 14'unde bu iki bolum vardi; dortunde yoktu:
  plm, fabrika-tasarimi (eskiden yerine "Cadbim Farki" blogu konmustu)
  bim-icerik-uretimi, ai-gorsellestirme (bu oturumda yeni eklendi)
(dijital-donusum haric tutuldu: kendi "Dijital Donusum Yolculugunuz" bolumu var.)

Uretilen HTML, mevcut 14 sayfadaki blogun BIREBIR ayni kalibidir; yalnizca
aksan rengi ve icerik sayfaya gore degisir. Yeniden calistirilabilir.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sayfa -> (aksan rengi, 5 adim, iyi uygulama maddeleri)
DATA = {
    'plm': ('#38bdf8', [
        (u'Süreç Envanteri',
         u'Değişiklik, onay ve BOM akışınızı olduğu gibi kâğıda döküyoruz; hangi adımın '
         u'e-postada, hangisinin Excel’de yaşadığını işaretliyoruz.'),
        (u'Kapsam ve Faz Planı',
         u'Tüm süreçleri aynı anda devreye almıyoruz. En çok acıtan modülden (genellikle '
         u'değişiklik yönetimi) başlayan fazlı bir plan çıkarıyoruz.'),
        (u'Yapılandırma',
         u'Hazır süreç şablonları kurumunuzun terminolojisine ve onay hiyerarşisine göre '
         u'uyarlanır; alan adları ve durum kodları sizin diliniz olur.'),
        (u'Veri Göçü ve Entegrasyon',
         u'Mevcut ürün ağacı ve parça listeleri aktarılır; ERP bağlantısı API üzerinden '
         u'kurulup çift veri girişi kaldırılır.'),
        (u'Devreye Alma ve Sahiplik',
         u'Rol bazlı eğitim, pilot ürün üzerinden canlıya geçiş ve sistemi kurum içinde '
         u'sahiplenecek kişinin yetiştirilmesi.'),
    ], [
        (u'Tek doğru BOM',
         u'Mühendislik, üretim ve satın alma aynı ürün ağacına bakar; Excel kopyaları emekliye ayrılır.'),
        (u'Değişiklik iz kaydı',
         u'Her revizyonun nedeni, onaylayanı ve tarihi kayıtta kalır; denetimde soru işareti olmaz.'),
        (u'Fazlı devreye alma',
         u'Tek modülle başlanır, kazanç görüldükçe genişletilir; büyük patlama denemesi yapılmaz.'),
        (u'Kurum içi sahip',
         u'Sistem tek kişiye bağlı kalmaz; yapılandırmayı sürdürecek bir sorumlu yetiştirilir.'),
        (u'ERP ile tek yönlü doğruluk',
         u'Hangi verinin hangi sistemde ana kaynak olduğu baştan yazılır; çift doğruluk kaynağı bırakılmaz.'),
        (u'Ölçülebilir hedef',
         u'Değişiklik kapanış süresi ve hatalı sipariş sayısı gibi göstergeler önceden tanımlanır.'),
    ]),

    'fabrika_tasarimi': ('#38bdf8', [
        (u'Mevcut Durumun Yakalanması',
         u'Tesis çizimi yoksa lazer tarama ile mevcut durum alınır; varsa DWG verisi '
         u'temizlenip 3B’ye taşınacak biçimde hazırlanır.'),
        (u'Varlık Kütüphanesi',
         u'Makine ve ekipmanlarınız meta verisiyle birlikte kütüphaneye tanımlanır; '
         u'sonraki projelerde hazır kullanılır.'),
        (u'Yerleşim Senaryoları',
         u'Birden çok yerleşim alternatifi kurulur; malzeme akışı, taşıma mesafesi ve '
         u'erişim payları karşılaştırılır.'),
        (u'Çakışma ve Takvim',
         u'Bina ile ekipman tek modelde birleştirilir; çakışmalar bulunur, kurulum ve '
         u'devreye alma sıralaması planlanır.'),
        (u'Karar ve Uygulama Dosyası',
         u'Seçilen yerleşim için ölçülü plan, 3B görsel ve ekipman listesi teslim edilir; '
         u'saha uygulamasına hazır dosya.'),
    ], [
        (u'Gerçek veriyle başla',
         u'Yeni ekipman tahmini ölçülere değil, taranmış mevcut duruma göre yerleştirilir.'),
        (u'Erişim ve bakım payı',
         u'Yalnızca makine değil, bakım erişimi, forklift güzergâhı ve kapı açılımı da modellenir.'),
        (u'Akış önce, yerleşim sonra',
         u'Yerleşim malzeme akışından türetilir; boş alana makine sığdırma yaklaşımı kullanılmaz.'),
        (u'Tek varlık kütüphanesi',
         u'Ekipmanlar merkezî kütüphaneden gelir; her projede yeniden çizilmez.'),
        (u'Kurulum sıralaması',
         u'Hangi ekipmanın hangi sırayla girmesi gerektiği modelden çıkarılır; saha beklemez.'),
        (u'İşletmeye devir',
         u'Yerleşim modeli dijital ikize temel olacak biçimde bırakılır; teslimle ölmez.'),
    ]),

    'bim_icerik_uretimi': ('#818cf8', [
        (u'Ürün Gamı Analizi',
         u'Hangi ürünler tek ailede toplanabilir, hangileri ayrı durmalı? Parametre '
         u'listesi ve ölçü tabloları üzerinden aile mimarisi kurulur.'),
        (u'LOD ve Veri Şartnamesi',
         u'Her ailenin hangi detay seviyesinde ve hangi parametreleri taşıyacağı yazılı '
         u'olarak tanımlanır; sonradan tartışma çıkmaz.'),
        (u'Pilot Aile',
         u'Önce tek bir ürün ailesi uçtan uca üretilir ve gerçek bir projede denenir; '
         u'onaylanan kalıp tüm gama uygulanır.'),
        (u'Seri Üretim ve Denetim',
         u'Kalan aileler pilot kalıba göre üretilir; her teslim öncesi kontrol listesiyle '
         u'kategori, parametre ve dosya boyutu denetlenir.'),
        (u'Yayınlama ve Bakım',
         u'.rfa ve IFC çıktıları kütüphaneye alınır; ürün değiştiğinde ailenin nasıl '
         u'güncelleneceği ve sürümleneceği kurala bağlanır.'),
    ], [
        (u'Doğru kategori seçimi',
         u'Aile yanlış kategoride kurulursa metraj ve filtreler bozulur; kategori en baştan doğru seçilir.'),
        (u'Sağlam iskelet',
         u'Referans düzlemleri ve kısıtlar önce kurulur; geometri bunlara bağlanır, aile revizyonda dağılmaz.'),
        (u'Tip kataloğu',
         u'Aynı mantığın ölçü varyantları tek ailede toplanır; her ölçü için ayrı dosya üretilmez.'),
        (u'Paylaşılan parametre',
         u'Metraja ve şartnameye girecek veriler paylaşılan parametreyle tanımlanır; proje arası tutarlı kalır.'),
        (u'Dosya boyutu disiplini',
         u'Üretim detayı taşınmaz; mimarın modelini ağırlaştıran aile kullanılmaz.'),
        (u'Teslim kontrol listesi',
         u'Kategori, adlandırma, parametre, bağlantı noktası ve boyut her teslimde tek tek denetlenir.'),
    ]),

    'ai_gorsellestirme': ('#c084fc', [
        (u'Mevcut Hattın Çıkarılması',
         u'Hangi işte hangi motoru kullandığınız ve zamanın nereye gittiği ölçülür; '
         u'otomasyona en değecek adım buradan çıkar.'),
        (u'Lisans Envanteri',
         u'Enscape, V-Ray veya Corona kullanıyorsanız bazı AI araçları zaten '
         u'kapsamınızda olabilir; yeni lisans almadan başlanabilecek yerler işaretlenir.'),
        (u'Pilot İş',
         u'Gerçek bir projede yalnızca yaratıcı karara dokunmayan adımlar denenir: '
         u'çözünürlük yükseltme, malzeme üretimi, detaylandırma.'),
        (u'Kullanım Politikası',
         u'Hangi araç hangi işte kullanılır, çıktı sahipliği ve müşteri gizliliği nasıl '
         u'yönetilir — yazılı hâle getirilir.'),
        (u'Ekip Yetkinliği',
         u'İstem yazma, malzeme üretimi ve son işlem için rol bazlı eğitim; araç '
         u'ekibin alışkanlığına yerleşene kadar takip.'),
    ], [
        (u'Karar insanda kalır',
         u'Yapay zekâ işçiliği devralır; kompozisyon, ışık ve malzeme kararı tasarımcıda kalır.'),
        (u'Dirençsiz adımdan başla',
         u'İlk uygulama çözünürlük yükseltme ve malzeme üretimi gibi kimsenin işini almayan adımlardır.'),
        (u'Final hâlâ fiziksel motorda',
         u'Müşteriye teslim edilen görsel ölçülü ve doğru ışıklı bir motordan çıkar; AI konsepti hızlandırır.'),
        (u'Çıktı ve lisans netliği',
         u'Ticari kullanım koşulları yayına almadan önce güncel şartlarla teyit edilir.'),
        (u'Veri gizliliği',
         u'Müşteri projesinin bulutta işlenip işlenmeyeceği politikada açıkça yazılır.'),
        (u'Ölçülebilir kazanç',
         u'Aynı işin öncesi ve sonrası süresi ölçülür; kazanç tahmin değil veri olur.'),
    ]),
}

STEP = (u'  <div style="flex:1;min-width:180px;position:relative;padding:0 14px 0 0;">\n'
        u'    <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">\n'
        u'      <div style="width:36px;height:36px;border-radius:50%%;background:%(a)s1a;'
        u'border:1px solid %(a)s55;color:%(a)s;display:flex;align-items:center;'
        u'justify-content:center;font-family:\'Manrope\',sans-serif;font-weight:800;'
        u'font-size:13px;flex-shrink:0;">%(no)s</div>\n'
        u'      <div style="flex:1;height:1px;background:linear-gradient(90deg,%(a)s55,%(a)s11);"></div>\n'
        u'    </div>\n'
        u'    <h3 style="font-family:\'Manrope\',sans-serif;font-size:15px;font-weight:700;'
        u'color:#fff;margin:0 0 6px;">%(t)s</h3>\n'
        u'    <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.65;margin:0;">%(d)s</p>\n'
        u'  </div>')

ITEM = (u'  <div style="display:flex;gap:12px;background:#0d1830;'
        u'border:.5px solid rgba(255,255,255,0.08);border-radius:12px;padding:16px 18px;">\n'
        u'    <i class="ti ti-circle-check" style="font-size:18px;color:%(a)s;'
        u'flex-shrink:0;margin-top:1px;"></i>\n'
        u'    <div>\n'
        u'      <h3 style="font-family:\'Manrope\',sans-serif;font-size:14px;font-weight:700;'
        u'color:#fff;margin:0 0 4px;">%(t)s</h3>\n'
        u'      <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.6;margin:0;">%(d)s</p>\n'
        u'    </div>\n'
        u'  </div>')

HEAD = (u'<section data-enrich style="padding:64px 3rem;">\n'
        u'  <div style="max-width:1200px;margin:0 auto;">\n'
        u'    <div style="font-size:11px;letter-spacing:2.5px;text-transform:uppercase;'
        u'color:#00c8f0;margin-bottom:8px;">%(lbl)s</div>\n'
        u'    <div style="font-family:\'Manrope\',sans-serif;font-size:clamp(1.4rem,2.6vw,1.9rem);'
        u'font-weight:800;color:#fff;margin-bottom:8px;">%(ttl)s</div>\n'
        u'    <p style="font-size:14px;color:rgba(255,255,255,.45);line-height:1.7;'
        u'margin:0 0 28px;max-width:640px;">%(sub)s</p>\n'
        u'    <div style="%(wrap)s">\n%(body)s</div>\n'
        u'  </div>\n</section>')


def build(key):
    acc, steps, items = DATA[key]
    yon = HEAD % dict(
        lbl=u'Yöntemimiz', ttl=u'Bu Çözümü Nasıl Hayata Geçiriyoruz?',
        sub=u'Beş adımlı uygulama metodolojimizle sürecin tamamını yönetiyoruz: '
            u'ihtiyaç analizi, kurgu, devreye alma, yaygınlaştırma ve sürdürme.',
        wrap=u'display:flex;flex-wrap:wrap;gap:22px 0;margin-top:8px;',
        body="".join(STEP % dict(a=acc, no='%02d' % (i + 1), t=t, d=d)
                     for i, (t, d) in enumerate(steps)))
    iyi = HEAD % dict(
        lbl=u'Sektör İyi Uygulamaları', ttl=u'Projelerde Uyguladığımız Standartlar',
        sub=u'Yüzlerce kurulumdan damıtılmış, işleyen iyi uygulama setimiz.',
        wrap=u'display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));'
             u'gap:14px;margin-top:8px;',
        body="".join(ITEM % dict(a=acc, t=t, d=d) for t, d in items))
    return u'<!-- cz-yontem -->\n%s\n%s\n<!-- /cz-yontem -->\n' % (yon, iyi)


def apply(key):
    path = os.path.join(ROOT, 'cadbim_%s.html' % key)
    s = io.open(path, encoding='utf-8').read()
    # yeniden calistirilabilirlik
    while '<!-- cz-yontem -->' in s:
        i = s.index('<!-- cz-yontem -->')
        j = s.index('<!-- /cz-yontem -->') + len('<!-- /cz-yontem -->')
        while j < len(s) and s[j] == '\n':
            j += 1
        s = s[:i] + s[j:]
    # SSS bolumunun ONUNE koy: ... Markalar -> Yontem -> Iyi Uygulama -> SSS
    anchor = '<!-- cz-faq -->'
    if anchor not in s:
        return False, 'SSS bolumu bulunamadi'
    s = s.replace(anchor, build(key) + anchor, 1)
    io.open(path, 'w', encoding='utf-8', newline='').write(s)
    return True, None


if __name__ == '__main__':
    for key in DATA:
        ok, err = apply(key)
        print('  %-22s %s' % (key, 'eklendi' if ok else 'ATLANDI: ' + str(err)))
