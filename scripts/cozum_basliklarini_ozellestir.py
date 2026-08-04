"""
Çözüm sayfalarındaki jenerik "Bu Çözüm..." başlıklarını çözümün adıyla yazar.

Gerekçe (Onur, 2026-08-05): "çözüm sayfasındaki başlıklarda sürekli bu çözümü
ifadesi başlama eğilimi var ne o çözüm? İsmini kullanarak etkileyici bir metin
yazmalısın BIM ile kontrolü sağla vs. gibi".

Bir sayfada aynı anda beş yerde "Bu Çözüm/Bu Çözümü" geçiyordu; okur hangi
çözümde olduğunu başlıktan anlayamıyordu.

TÜRKÇE EK NOTU: Çözüm adlarına doğrudan hâl eki getirilmiyor ("BIM'i", "PDM'yi"
gibi kesme+ek varyantları ada göre değişir ve kısaltmalarda telaffuza bağlıdır).
Bunun yerine adı yalın bırakan kalıplar seçildi: "... Hangi Ürünlerle Kuruluyor",
"... Hakkında Merak Edilenler" gibi. Böylece 18 sayfanın hepsinde dilbilgisi
doğru kalır.

Kullanim: python scripts/cozum_basliklarini_ozellestir.py [--dry-run]
"""
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# dosya -> çözümün kısa adı (başlıkta doğal duracak biçimde)
ADLAR = {
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

# eski metin -> yeni metin kalıbı ({ad} çözümün adıyla değişir)
DEGISIM = [
    ("Bu Çözüm Nedir?",                 "{ad} Nedir?"),
    ("Bu Çözümü Ayakta Tutan Ürünler",  "{ad} Hangi Ürünlerle Kuruluyor"),
    ("Sahada Karşılığı Olan Bir Çözüm", "{ad} Hangi Sektörlerde İş Görüyor"),
    ("Bu Çözüm Hakkında Merak Edilenler", "{ad} Hakkında Merak Edilenler"),
    ("Bu Çözümü Nasıl Hayata Geçiriyoruz?", "{ad} Nasıl Hayata Geçiyor?"),
    ("Bu çözümü kurduğumuz sektörler ve iş akışları.",
     "{ad} projelerini yürüttüğümüz sektörler ve iş akışları."),
]


def main():
    toplam = 0
    rapor = []
    for path in sorted(glob.glob(os.path.join(ROOT, "cadbim_*.html"))):
        ad_dosya = os.path.basename(path)
        if ad_dosya not in ADLAR:
            continue
        ad = ADLAR[ad_dosya]
        txt = io.open(path, encoding="utf-8").read()
        orig = txt
        n = 0
        for eski, kalip in DEGISIM:
            yeni = kalip.format(ad=ad)
            # yalnızca etiket içeriği olarak geçenleri değiştir (>metin<)
            hedef = ">" + eski + "<"
            if hedef in txt:
                n += txt.count(hedef)
                txt = txt.replace(hedef, ">" + yeni + "<")
        if txt != orig:
            toplam += n
            rapor.append((ad_dosya, ad, n))
            if not DRY:
                io.open(path, "w", encoding="utf-8", newline="").write(txt)

    for f, ad, n in rapor:
        print(f"  {f:<34}{ad:<28}{n} başlık")
    print(f"\n{len(rapor)} sayfa, {toplam} başlık" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
