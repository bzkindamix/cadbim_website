"""
Çözüm sayfalarının sonundaki "Bu Çözümde Çalıştığımız Markalar" şeridini kaldırır.

Gerekçe (Onur, 2026-08-05): "çözümlerin sonunda bir daha çözümlerde
kullandığımız markalara gerek yok kaldır gitsin tüm çözümlerden". Şerit her
çözüm sayfasında hemen üstteki "Bu Çözümü Ayakta Tutan Ürünler" bölümüyle
aynı bilgiyi (Autodesk/Adobe/HP/Chaos ortaklığı) tekrar ediyordu.

CSS (.cz-brands, .cz-brand*) design-system.css içinde merkezi tanımlı ve
sayfa içi tekrarı yok; HTML bloğu kaldırıldığında ölü CSS kalmaz, bu yüzden
CSS'e dokunulmadı.

Kullanim: python scripts/remove_cz_brands.py [--dry-run]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

BLOK = re.compile(r'\n?<!-- cz-brands -->.*?<!-- /cz-brands -->\n?', re.S)


def main():
    toplam = 0
    dosyalar = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        yeni, n = BLOK.subn("\n", txt)
        if n:
            dosyalar.append((os.path.basename(path), n))
            toplam += n
            if not DRY:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(yeni)

    for ad, n in dosyalar:
        print(f"  {ad:<36}{n}")
    print(f"\n{len(dosyalar)} sayfa, {toplam} şerit" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
