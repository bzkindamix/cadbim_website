"""
Bölüm başlıklarındaki tekrarları kaldırır ve tonu slogana yaklaştırır.

Tespit (ölçüm): Sitede bölüm başlıkları üç katmanlı — etiket (.slabel),
başlık (.stitle), altyazı (.ssub). Birçok yerde üçü de aynı şeyi söylüyordu;
en yoğun tekrar "İlgili Ürünler" ailesindeydi (94 sayfa). Ayrıca:
  - 11 sayfada ENDÜSTRİ bölümü "İlgili Ürünler" diye etiketlenmişti (yanlış),
  - 26 altyazıda "inceleyin / bulabilirsiniz" gibi arayüz talimatı vardı;
    bu, sitenin ton kuralına aykırı (metin değeri anlatır, yönerge vermez).

İlke: üç katman üç ayrı iş yapar —
  etiket  = bağlam (kısa),
  başlık  = değer/slogan,
  altyazı = somut karşılık.

Kullanim: python scripts/bolum_basliklari_revizyon.py [--dry-run]
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# (eski etiket, eski baslik, eski altyazi) -> (yeni etiket, yeni baslik, yeni altyazi)
# altyazi None ise mevcut altyazi korunur; "" ise altyazi yoktur.
REVIZYON = [
    # --- "İlgili Ürünler" ailesi: etiket başlığı tekrar ediyordu ---
    (("İlgili Ürünler", "İlgili Ürünler ve Çözümler", "Birlikte değerlendirin"),
     ("Portföy", "Cadbim'in Ürün Portföyü Yanınızda",
      "Bu ürünle birlikte kurguladığımız yazılım, donanım ve çözümler.")),

    (("İlgili Ürünler", "Bu Çözümde Kullanılan Cadbim Ürünleri",
      "İlgili yazılım ve donanım sayfaları"),
     ("Portföy", "Bu Çözümü Ayakta Tutan Ürünler",
      "Çözümün her adımında devreye giren yazılım ve donanımlar.")),

    (("Ürünler", "Bu Çözümde Kullanılan Cadbim Ürünleri",
      "İlgili yazılım ve donanım sayfaları"),
     ("Portföy", "Bu Çözümü Ayakta Tutan Ürünler",
      "Çözümün her adımında devreye giren yazılım ve donanımlar.")),

    # --- Endüstri bölümü "İlgili Ürünler" diye etiketlenmişti: yanlış etiket ---
    (("İlgili Ürünler", "Bu Çözüm Hangi Endüstrilerde Kullanılıyor",
      "İlgili endüstri sayfalarını inceleyin"),
     ("Endüstriler", "Sahada Karşılığı Olan Bir Çözüm",
      "Bu çözümü kurduğumuz sektörler ve iş akışları.")),

    (("Endüstriler", "Bu Çözüm Hangi Endüstrilerde Kullanılıyor",
      "İlgili endüstri sayfalarını inceleyin"),
     ("Endüstriler", "Sahada Karşılığı Olan Bir Çözüm",
      "Bu çözümü kurduğumuz sektörler ve iş akışları.")),

    # --- Endüstri sayfalarındaki çözüm şeridi ---
    (("Çözümler", "Bu endüstride kullanılan Cadbim Çözümleri",
      "İlgili çözüm sayfalarında, her çözümde kullanılan ürünleri de bulabilirsiniz"),
     ("Çözümler", "Bu Sektörün İşini Çözen Yaklaşımlar",
      "Her çözüm, birden fazla Cadbim ürününü tek iş akışında birleştirir.")),

    # --- Ürün sayfalarındaki "Keşfet / Bu Ürünle İlgili": içerik hem çözüm
    #     hem endüstri şeridi taşıyor; başlık bunu karşılamıyordu ---
    (("Keşfet", "Bu Ürünle İlgili", ""),
     ("Keşfet", "Bu Ürün Yalnız Çalışmıyor", "")),

    # --- "Kullanım" iki katmanda tekrar ediyordu ---
    (("Kullanım Senaryoları", "Tipik Kullanım Alanları", ""),
     ("Kullanım Senaryoları", "Nerede İşe Yarıyor?", "")),

    # --- Marka şeridi: başlık etiketi tekrar ediyordu, altyazı bilgi taşıyor ---
    (("Markalar", "Bu sektörde çalıştığımız markalar", None),
     ("Markalar", "Arkanızda Yetkili İş Ortakları Var", None)),

]

# Başarı öyküsü bölümleri: bazı sayfalarda "İlgili Ürünler" diye etiketlenmiş
# (yanlış), bazılarında etiket başlığı birebir tekrar ediyordu. Başlık "Başarı
# Öyküleri" olan her bölümün etiketi "Referanslar" olur.
OYKU_ETIKET = re.compile(
    r'(<div class="slabel">)(?:İlgili Ürünler|Başarı Öyküleri|İlgili Öyküler)'
    r'(</div>\s*<div class="stitle"[^>]*>Başarı Öyküleri</div>)')

# Altyazılar: "sonuç alan" yerine neyin iyileştiğini söyleyen ifade.
OYKU_ALTYAZI = [
    (re.compile(r'(<p class="ssub">)(.+?) çözümüyle sonuç alan müşterilerimiz(</p>)'),
     r'\g<1>\g<2> çözümüyle süreçlerinde iyileşme sağlayan müşterilerimiz\g<3>'),
    (re.compile(r'(<p class="ssub">)(.+?) sektöründe Cadbim ile sonuç alan müşterilerimiz(</p>)'),
     r'\g<1>\g<2> sektöründe Cadbim ile süreçlerini iyileştiren müşterilerimiz\g<3>'),
]

# Kalan tekil arayüz talimatları (ton kuralı: yönerge verme, değeri anlat)
ALTYAZI_DUZELT = [
    ("İlgili çözüm ve endüstri sayfalarını inceleyin",
     "Bu ürünün yer aldığı çözümler ve sektörler."),
    ("Sektörünüze özel çözüm kombinasyonlarını inceleyin",
     "Sektörünüze göre bir araya getirdiğimiz çözüm kombinasyonları."),
    ("Her çözüm sayfasında, o alanda kullandığımız ürünleri bulabilirsiniz.",
     "Her çözümün arkasında, o alanda kullandığımız ürünler var."),
]


def kalip(etiket, baslik, altyazi):
    """slabel + stitle (+ ssub) üçlüsünü yakalayan desen.

    Büyük/küçük harf duyarsız: aynı başlık sitede hem "İlgili Ürünler ve
    Çözümler" hem "İlgili ürünler ve çözümler" biçiminde geçiyor.
    """
    p = (r'(<div class="slabel">)' + re.escape(etiket) + r'(</div>\s*'
         r'<div class="stitle"[^>]*>)' + re.escape(baslik) + r'(</div>)')
    if altyazi:
        p += r'(\s*<p class="ssub">)' + re.escape(altyazi) + r'(</p>)'
    return re.compile(p, re.IGNORECASE)


def main():
    toplam = {}
    dosya_sayisi = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        with io.open(path, encoding="utf-8") as f:
            txt = f.read()
        orig = txt

        for (el, bl, al), (ey, by, ay) in REVIZYON:
            # HTML'de & karakteri &amp; olarak geçebilir
            for esc in (lambda s: s, lambda s: s.replace("&", "&amp;")):
                pat = kalip(esc(el), esc(bl), esc(al) if al else None)
                if al:
                    yeni = r'\g<1>' + ey + r'\g<2>' + by + r'\g<3>\g<4>' + ay + r'\g<5>'
                else:
                    yeni = r'\g<1>' + ey + r'\g<2>' + by + r'\g<3>'
                txt, n = pat.subn(yeni, txt)
                if n:
                    toplam[bl] = toplam.get(bl, 0) + n

        for eski, yeni in ALTYAZI_DUZELT:
            txt, n = re.subn(r'(<p class="ssub">)' + re.escape(eski) + r'(</p>)',
                             r'\g<1>' + yeni + r'\g<2>', txt)
            if n:
                toplam[eski[:34]] = toplam.get(eski[:34], 0) + n

        txt, n = OYKU_ETIKET.subn(r'\g<1>Referanslar\g<2>', txt)
        if n:
            toplam["Başarı Öyküleri — etiket"] = toplam.get("Başarı Öyküleri — etiket", 0) + n
        for pat, yeni in OYKU_ALTYAZI:
            txt, n = pat.subn(yeni, txt)
            if n:
                toplam["Başarı Öyküleri — altyazı"] = toplam.get("Başarı Öyküleri — altyazı", 0) + n

        if txt != orig:
            dosya_sayisi += 1
            if not DRY:
                with io.open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(txt)

    for k, v in sorted(toplam.items(), key=lambda x: -x[1]):
        print(f"  {v:>3}x  {k}")
    print(f"\n{dosya_sayisi} sayfa, {sum(toplam.values())} bölüm başlığı"
          + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
