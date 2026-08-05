"""
Ürün sayfalarındaki jenerik bölüm başlıklarını ürünün adıyla yazar.

Gerekçe (Onur, 2026-08-05): "textler değişecekti çözümlerde birbirini tekrar
eden başlıklar var. tüm sitede bu durum var."

Ölçüm: Önceki turda yazdığım sloganlar sayfadan sayfaya BİREBİR aynıydı —
75 sayfada "Bu Ürün Yalnız Çalışmıyor", 61 sayfada "Cadbim'in Ürün Portföyü
Yanınızda", 16 çözüm sayfasında aynı altyazı. Çözüm sayfalarının başlıkları
DK-85'te adla yazılmıştı ama ürün sayfaları ve altyazılar kapsam dışı kalmıştı.

TÜRKÇE EK NOTU (DK-85'ten devam): Adlara hâl eki getirilmiyor ("Revit'i",
"AutoCAD'i" gibi kesme+ek varyantları ada ve telaffuza göre değişir).
Adı yalın bırakan kalıplar seçildi: "... Nerede Devreye Giriyor",
"... ile Birlikte Çalışanlar" gibi. Böylece tüm sayfalarda dilbilgisi doğru.

Kullanim: python scripts/urun_basliklarini_ozellestir.py [--dry-run] [--adlar]
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SADECE_ADLAR = "--adlar" in sys.argv

# Ürün adı <title>'dan alınır: "Autodesk Revit — BIM ... | Cadbim" -> "Autodesk Revit"
# Marka öneki korunur; atmak "Fusion/Forma" gibi adlarda yanlış çağrışım yapabilir.
def urun_adi(txt):
    m = re.search(r"<title>(.*?)</title>", txt, re.S)
    if not m:
        return None
    ad = m.group(1)
    for ayrac in ("—", "–", "|", ":"):
        ad = ad.split(ayrac)[0]
    ad = re.sub(r"\s+", " ", ad).replace("&amp;", "&").strip()
    # Başlıkta şişirmemek için sondaki parantezli model listesi atılır:
    # "HP DesignJet T200 Serisi (T230/T250)" -> "HP DesignJet T200 Serisi"
    ad = re.sub(r"\s*\([^)]*\)\s*$", "", ad).strip()
    return ad or None


# eski metin -> {ad} kalıbı
DEGISIM = [
    # 75 sayfa: ürünün kullanıldığı çözüm ve endüstri şeridi
    ("Bu Ürün Yalnız Çalışmıyor", "{ad} Nerede Devreye Giriyor"),
    # 61 sayfa: ilgili ürün/çözüm şeridi (başlık + altyazı)
    ("Cadbim'in Ürün Portföyü Yanınızda", "{ad} ile Birlikte Çalışanlar"),
    ("Bu ürünle birlikte kurguladığımız yazılım, donanım ve çözümler.",
     "{ad} kurulumlarında yanına koyduğumuz yazılım, donanım ve çözümler."),
    # 51 + 29 sayfa: kullanım senaryoları
    ("Kimler İçin?", "{ad} Kimler İçin?"),
    ("Nerede İşe Yarıyor?", "{ad} Nerede İşe Yarıyor?"),
    # ikinci tur (aynı ölçümün kalan başlıkları)
    ("Size Uygun Lisans Modeli", "{ad} için Lisans Seçenekleri"),
    ("Neler Yapabiliriz?", "{ad} ile Neler Yapabiliriz?"),
    # NOT: "Seçenekler" (18 sayfa) bilinçli olarak kapsam dışı — model
    # varyantlarını listeliyor ve ürün adı zaten model bilgisini taşıyor.
]

# Çözüm sayfalarındaki tek tip altyazı (DK-85 başlıkları yazmış, altyazı kalmıştı)
COZUM_ALTYAZI = ("Çözümün her adımında devreye giren yazılım ve donanımlar.",
                 "{ad} kurulumunun her adımında devreye giren yazılım ve donanımlar.")
# DK-85'teki çözüm adları
COZUM_ADLARI = {
    "cadbim_ai_gorsellestirme.html":  "AI Destekli Görselleştirme",
    "cadbim_bim.html":                "BIM",
    "cadbim_bim_icerik_uretimi.html": "BIM İçerik Üretimi",
    "cadbim_cam.html":                "CAM",
    "cadbim_dijital_donusum.html":    "Dijital Dönüşüm",
    "cadbim_dijital_ikiz.html":       "Dijital İkiz",
    "cadbim_eklemeli_imalat.html":    "Eklemeli İmalat",
    "cadbim_fabrika_tasarimi.html":   "Fabrika Tasarımı",
    "cadbim_gerceklik_yakalama.html": "Gerçeklik Yakalama",
    "cadbim_gorsellestirme.html":     "Görselleştirme",
    "cadbim_insaat_yonetimi.html":    "İnşaat Proje Yönetimi",
    "cadbim_nesting.html":            "Nesting",
    "cadbim_pdm.html":                "PDM",
    "cadbim_plm.html":                "PLM",
    "cadbim_simulasyon.html":         "Simülasyon",
    "cadbim_tasarim_otomasyonu.html": "Tasarım Otomasyonu",
    "cadbim_tolerans_analizi.html":   "Tolerans Analizi",
    "cadbim_yaratici_icerik.html":    "Yaratıcı İçerik",
}


def main():
    toplam = {}
    dosya = 0
    adlar = []

    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        f = os.path.basename(path)
        t = io.open(path, encoding="utf-8").read()
        orig = t

        ad = COZUM_ADLARI.get(f) or urun_adi(t)
        if not ad:
            continue

        degisti = False
        for eski, kalip in DEGISIM:
            for tag in ('<div class="stitle" role="heading" aria-level="2">',
                        '<p class="ssub">'):
                kapanis = "</div>" if tag.startswith("<div") else "</p>"
                hedef = tag + eski + kapanis
                if hedef in t:
                    t = t.replace(hedef, tag + kalip.format(ad=ad) + kapanis)
                    toplam[eski] = toplam.get(eski, 0) + 1
                    degisti = True

        if f in COZUM_ADLARI:
            eski, kalip = COZUM_ALTYAZI
            hedef = '<p class="ssub">' + eski + "</p>"
            if hedef in t:
                t = t.replace(hedef, '<p class="ssub">' + kalip.format(ad=ad) + "</p>")
                toplam[eski] = toplam.get(eski, 0) + 1
                degisti = True

        if degisti:
            adlar.append((f, ad))
            dosya += 1
            if not (DRY or SADECE_ADLAR):
                io.open(path, "w", encoding="utf-8", newline="").write(t)

    if SADECE_ADLAR:
        for f, a in adlar:
            print(f"  {f:<40}{a}")
        print(f"\n{len(adlar)} sayfa")
        return

    for k, v in sorted(toplam.items(), key=lambda x: -x[1]):
        print(f"  {v:>3}x  {k[:62]}")
    print(f"\n{dosya} sayfa, {sum(toplam.values())} başlık/altyazı"
          + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
