# -*- coding: utf-8 -*-
"""Chaos ve Adobe kaynakli icerigi mevcut cozum/marka sayfalarina yerlestirir.

Kaynaklar (3 Agustos 2026'da chaos.com ve business.adobe.com uzerinden derlendi):
  - chaos.com/architectural-visualization  -> dort sutun + urun rolleri
  - chaos.com "Industry solutions" menusu  -> kullanim alanlari (disiplinler)
  - chaos.com/ai-visualization             -> AI arac seti (ayri cozum sayfasinda)
  - chaos.com "See what's new"             -> guncel surum yenilikleri
  - adobe.com/tr/creativecloud/business/teams.html -> Ekipler icin Creative Cloud
  - adobe.com/tr/creativecloud/business/acrobat-pro.html -> Acrobat Standard / Pro

KAPSAM (Onur 3 Agustos 2026: "adobe marketing cozumlerini satamiyoruz",
"adobe for business endustri ve cozumlerini degil creative ve acrobat tarafina bak"):
Icerik YALNIZCA Adobe'nin Creative Cloud ve Acrobat tarafindan alinmistir.
Adobe Experience Cloud / GenStudio / Experience Manager / Real-Time CDP /
Journey Optimizer / Analytics / Workfront urunlerine hic deginilmez -- bunlar
CADBIM'in Gold Reseller (Commercial / Education / Government) kapsaminda degildir.
Adobe'nin yayinladigi fiyatlar da bilincli olarak alinmamistir (CADBIM kurali:
sitede fiyat gosterilmez).

SURUM NUMARASI KULLANILMAZ (Onur 3 Agustos 2026: "surum numaralari
kullanmaktan kacin"). Icerik yetenek duzeyinde yazilir; boylece her yeni
Chaos/Adobe surumunde sayfanin guncellenmesi gerekmez ve eskimis bilgi
yayinlanmis olmaz.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def strip_block(html, name):
    start, close = '<!-- %s -->' % name, '<!-- /%s -->' % name
    while start in html:
        i = html.index(start)
        j = html.index(close, i) + len(close)
        while j < len(html) and html[j] == '\n':
            j += 1
        html = html[:i] + html[j:]
    return html


def insert_after_section(path, contains, block, marker):
    """`contains` metnini iceren bolumun ARDINA blok ekler."""
    s = io.open(path, encoding='utf-8').read()
    s = strip_block(s, marker)
    i = s.find(contains)
    if i < 0:
        return False, 'baslik bulunamadi: %s' % contains
    si = s.rfind('<section', 0, i)
    depth_end = s.find('</section>', i) + len('</section>')
    s = s[:depth_end] + '\n' + block + s[depth_end:]
    io.open(path, 'w', encoding='utf-8', newline='').write(s)
    return True, None


# --------------------------------------------------------------------------
# 1) Gorsellestirme: kullanim alanlari (Chaos "Industry solutions")
# --------------------------------------------------------------------------
ALANLAR = [
    ('ti-building-arch', u'Mimari Görselleştirme',
     u'Konsept eskizinden satış görseline; fiziksel tabanlı ışık, malzeme ve kamera '
     u'ile gerçeğe en yakın sonuç. V-Ray ve Corona bu alanın endüstri standardı.'),
    ('ti-armchair', u'İç Mimarlık',
     u'Küçük hacimlerde doğru ışık ve malzeme her şeydir. Kumaş, cam ve metal '
     u'davranışının doğru çözülmesi, mobilya ve kaplama seçiminin ekranda kararlaştırılması.'),
    ('ti-tree', u'Peyzaj Görselleştirme',
     u'Bitki örtüsü, mevsim ve büyüme senaryoları; geniş dış mekân sahnelerinin '
     u'proxy nesneler ve dağıtık render ile yönetilmesi.'),
    ('ti-map-2', u'Kentsel Planlama',
     u'Kütle çalışmaları, gölge ve siluet analizleri; imar ve kamuoyu sunumları için '
     u'geniş ölçekli sahnelerin okunur biçimde anlatılması.'),
    ('ti-movie', u'Film & TV VFX',
     u'Prodüksiyonda kanıtlanmış render; binlerce ışık ve milyarlarca poligonun '
     u'kaldırılması, Alembic ve OpenColorIO gibi açık standartlarla hatta oturması.'),
    ('ti-video', u'Sanal Prodüksiyon',
     u'Gerçek zamanlı ışın izlemeli sahne keşfi; kamera açısı ve ışık kararlarının '
     u'çekim öncesinde canlı oturumda alınması.'),
    ('ti-car', u'Otomotiv',
     u'Class-A yüzey denetimi, kaplama ve renk varyantları; stüdyo ve dış ortam '
     u'sunumlarının aynı sahneden türetilmesi.'),
    ('ti-package', u'Ürün Tasarımı',
     u'CAD verisinden pazarlama görseli; ambalaj, malzeme ve etiket denemelerinin '
     u'fotoğraf çekimine gerek kalmadan yapılması.'),
]


def gorsellestirme():
    cards = "".join(
        u'    <div class="card">\n'
        u'      <div class="card-icon" style="background:rgba(245,158,11,.12);color:#f59e0b;">'
        u'<i class="ti %s"></i></div>\n      <h3>%s</h3>\n      <p>%s</p>\n    </div>\n'
        % (ic, t, d) for ic, t, d in ALANLAR)
    block = u'''<!-- cz-alanlar -->
<section class="section cz-sec" style="--cz:#f59e0b;padding-top:0;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Kullanım Alanları</div>
    <div class="stitle">Görselleştirme hangi işte ne anlatır?</div>
    <p class="ssub">Aynı araç seti, disipline göre farklı şeyi kanıtlamak için kurulur —
      hattı işinize göre yapılandırıyoruz.</p>
  </div>
  <div class="grid g3" style="margin-top:0;">
%s  </div>
</section>
<!-- /cz-alanlar -->
''' % cards
    return insert_after_section(
        os.path.join(ROOT, 'cadbim_gorsellestirme.html'),
        u'>Neler Yapabiliriz?<', block, 'cz-alanlar')


# --------------------------------------------------------------------------
# 2) Yaratici Icerik: icerik uretim hatti (Adobe "content supply chain")
# --------------------------------------------------------------------------
HAT = [
    ('ti-clipboard-list', u'01 · Planla ve Standardı Kur',
     u"Marka renkleri, fontlar ve onaylı varlıklar Creative Cloud Libraries'de tek "
     u"yerde durur; her iş sıfırdan değil onaylı bir başlangıçtan açılır. Adobe Fonts "
     u"kapsamındaki 30.000'den fazla font ve paylaşılan Adobe Stock lisansı aynı "
     u"kütüphaneden kullanılır.",
     u'Creative Cloud Libraries · Adobe Fonts · Adobe Stock'),
    ('ti-brush', u'02 · Üret',
     u"20'den fazla uygulamayla tasarım, video ve 3B üretimi; uygulamalara gömülü "
     u"üretken yapay zekâ ile varyantların elle çoğaltılmaması. Tasarımcı olmayan "
     u"ekipler Adobe Express şablonlarıyla marka dışına çıkmadan üretir.",
     u'Photoshop · Illustrator · InDesign · Premiere · Substance 3D · Firefly · Express'),
    ('ti-eye-check', u'03 · Gözden Geçir ve Onayla',
     u'Yorum ve onay dosya adı üzerinden değil içeriğin üzerinde yürür. Paylaşılan '
     u'bağlantıyla inceleme için karşı tarafın oturum açması gerekmez; belge tarafında '
     u'yasal olarak bağlayıcı elektronik imza toplanır.',
     u'Frame.io · Acrobat Pro'),
    ('ti-history-toggle', u'04 · Sürümü Koru, Yeniden Kullan',
     u'180 güne kadar sürüm geçmişiyle eski hâle dönülebilir; kullanıcı başına 1 TB '
     u'bulut depolama varlıkları aranabilir tutar. Aynı görsel her kanal için yeniden '
     u'üretilmez, uyarlanır.',
     u'Creative Cloud (180 gün sürüm geçmişi · 1 TB) · Admin Console'),
]



def yaratici_icerik():
    items = "".join(
        u'    <div class="cz-hat-i">\n'
        u'      <span><i class="ti %s"></i></span>\n'
        u'      <div><h3>%s</h3><p>%s</p><em>%s</em></div>\n    </div>\n'
        % (ic, t, d, tools) for ic, t, d, tools in HAT)
    block = u'''<!-- cz-hat -->
<section class="section cz-sec" style="--cz:#e25922;padding-top:0;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">İçerik Üretim Hattı</div>
    <div class="stitle">İçerik bir dosya değil, bir hattır</div>
    <p class="ssub">Ekipler için Creative Cloud ve Acrobat'ın kurumsal özellikleriyle
      kurulan dört adım: plandan üretime, onaydan yeniden kullanıma. Yalnızca Cadbim'in
      yetkili satıcı olduğu ürünlerle.</p>
  </div>
  <div class="cz-hat">
%s  </div>
</section>
<!-- /cz-hat -->
''' % items
    return insert_after_section(
        os.path.join(ROOT, 'cadbim_yaratici_icerik.html'),
        u'>Neler Yapabiliriz?<', block, 'cz-hat')


# --------------------------------------------------------------------------
# 3) Chaos marka sayfasi: guncel surum yenilikleri
# --------------------------------------------------------------------------
YENILIK = [
    (u'AI Upscaler', u'Chaos Cloud',
     u'Düşük çözünürlüklü render tek tıkla 2x/4x büyütülür, 16K’ya kadar; doku ve '
     u'detay da keskinleşir. Enscape, V-Ray ve Corona kullanıcılarına açık.'),
    (u'AI Material Generator', u'Chaos Cosmos',
     u'Herhangi bir fotoğraf dikişsiz, render’a hazır PBR malzemeye dönüşür; '
     u'malzeme hazırlamanın elle yapılan kısmı ortadan kalkar.'),
    (u'AI Mood Match', u'V-Ray for SketchUp & Rhino',
     u'Referans fotoğrafın ışık koşulları çözümlenip Sun & Sky veya görsel tabanlı '
     u'aydınlatma buna göre kurulur.'),
    (u'Gerçek zamanlı görünüm penceresi', u'Vantage + 3ds Max',
     u'Vantage doğrudan 3ds Max görünüm penceresinde çalışır: fiziksel doğru kamera, '
     u'ışık ve malzemeyle anlık yol izlemeli geri bildirim, dönüştürme gerekmez.'),
    (u'Kalabalık ve trafik animasyonu', u'Anima',
     u'Tam mürettebatlı araçlarda fren ve sinyal ışıkları; bağlam duyarlı kalabalıkların '
     u'yollar boyunca veya etikete göre doğal hareketi.'),
    (u'Geniş platform desteği', u'V-Ray',
     u'3ds Max, Maya, SketchUp, Revit, Rhino, Cinema 4D, Blender ve Unreal; Windows, '
     u'Linux, CPU ve GPU render seçenekleri.'),
]


def chaos():
    cards = "".join(
        u'    <div class="cz-fark-c">\n      <span><i class="ti ti-rocket"></i></span>\n'
        u'      <h3>%s</h3>\n      <p style="color:rgba(255,255,255,.4);font-size:11px;'
        u'text-transform:uppercase;letter-spacing:.8px;margin:0 0 7px;">%s</p>\n'
        u'      <p>%s</p>\n    </div>\n' % (t, sub, d) for t, sub, d in YENILIK)
    block = u'''<!-- cz-yenilik -->
<section class="section cz-sec" style="--cz:#f26d5b;">
  <div class="sh" style="margin-bottom:26px;">
    <div class="slabel" style="color:var(--cz);">Öne Çıkan Yetenekler</div>
    <div class="stitle">Chaos ekosisteminde neler var?</div>
    <p class="ssub">Ekosistem sürekli geliştiği için burada yetenekleri anlatıyoruz;
      hangi ürün ve planda hangisinin bulunduğunu teklif aşamasında birlikte netleştiriyoruz.</p>
  </div>
  <div class="cz-fark">
%s  </div>
</section>
<!-- /cz-yenilik -->
''' % cards
    p = os.path.join(ROOT, 'cadbim_chaos.html')
    s = io.open(p, encoding='utf-8').read()
    s = strip_block(s, 'cz-yenilik')
    anchor = '<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">'
    if anchor not in s:
        return False, 'blog bolumu bulunamadi'
    s = s.replace(anchor, block + '\n' + anchor, 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True, None


# --------------------------------------------------------------------------
# 4) Adobe marka sayfasi: Acrobat tarafi (belge ve onay akisi)
#    Kaynak: adobe.com/tr/creativecloud/business/acrobat-pro.html
#    (Onur: "creative ve acrobat tarafindaki cozum ve endustrilere bak")
# --------------------------------------------------------------------------
ACROBAT = [
    ('ti-file-check', u'Sürüm Karşılaştırma',
     u'Dosyaları Karşılaştır aracı bir PDF’in iki sürümü arasında neyin değiştiğini '
     u'gösterir. Revizyon takibi göz kararına bırakılmaz.'),
    ('ti-signature', u'Yasal Bağlayıcı E-imza',
     u'Mobil dahil tüm aygıtlarda belge imzalama ve imza isteme; alıcıların oturum '
     u'açması gerekmez, yanıtlar tek yerden izlenir.'),
    ('ti-eye-off', u'Redaksiyon',
     u'Hassas bilgi yalnızca gizlenmez, dosyadan kalıcı olarak kaldırılır — teklif ve '
     u'sözleşme paylaşımında kritik.'),
    ('ti-scan', u'Tarama → Aranabilir PDF',
     u'Taranmış basılı belgeler aranabilir ve düzenlenebilir PDF’e çevrilir; eski proje '
     u'arşivi aranabilir hâle gelir.'),
    ('ti-lock', u'PDF Koruma',
     u'İçeriğin kopyalanması, düzenlenmesi veya yazdırılması engellenebilir; paylaşım '
     u'SSL güvenliğiyle yapılır.'),
    ('ti-plug-connected', u'Mevcut Araçlarla Çalışır',
     u'Microsoft 365 ve Dropbox gibi kullandığınız uygulamalarla; Creative Cloud ve '
     u'Adobe Express ile bütünleşir. Adobe Scan ve Acrobat Reader mobil dahil.'),
]


def adobe():
    cards = "".join(
        u'    <div class="cz-fark-c">\n      <span><i class="ti %s"></i></span>\n'
        u'      <h3>%s</h3>\n      <p>%s</p>\n    </div>\n' % (ic, t, d)
        for ic, t, d in ACROBAT)
    block = (u'<!-- cz-acrobat -->\n'
             u'<section class="section cz-sec" style="--cz:#e25922;">\n'
             u'  <div class="sh" style="margin-bottom:26px;">\n'
             u'    <div class="slabel" style="color:var(--cz);">Belge & Onay Akışı</div>\n'
             u'    <div class="stitle">Acrobat: teklif, sözleşme ve proje dokümanı tarafı</div>\n'
             u'    <p class="ssub">Acrobat Standard 40’tan fazla, Acrobat Pro 70’ten fazla '
             u'özellik sunar. Mühendislik ve inşaat ekiplerinde en çok karşılığı olan '
             u'başlıklar:</p>\n'
             u'  </div>\n'
             u'  <div class="cz-fark">\n%s  </div>\n'
             u'</section>\n'
             u'<!-- /cz-acrobat -->\n') % cards
    p = os.path.join(ROOT, 'cadbim_adobe.html')
    s = io.open(p, encoding='utf-8').read()
    s = strip_block(s, 'cz-acrobat')
    anchor = '<section style="padding:64px 3rem;background:#0a1225;" id="blog-related-section">'
    if anchor not in s:
        return False, 'blog bolumu bulunamadi'
    s = s.replace(anchor, block + '\n' + anchor, 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    return True, None


if __name__ == '__main__':
    for name, fn in (('gorsellestirme', gorsellestirme),
                     ('yaratici-icerik', yaratici_icerik),
                     ('chaos', chaos),
                     ('adobe', adobe)):
        ok, err = fn()
        print('%-16s %s' % (name, 'eklendi' if ok else 'ATLANDI: ' + str(err)))
