"""
Çözüm sayfalarında "Endüstriler" bloğunu SSS bölümünden sonraya taşır.

Gerekçe (Onur, 2026-08-05): "çözüm sayfalarında ilgili endüstrileri SSS
alanından sonra ekle".

Mevcut yapı: Endüstriler ayrı bir <section> değil; "Portföy" bölümünün içinde
`<div class="sh">` + `<div class="grid g3">` ikilisi olarak duruyor ve hemen
ardından "Referanslar / Başarı Öyküleri" bloğu geliyor. Blok kesilip SSS
bölümünün (`<!-- /cz-faq -->`) hemen ardına, kendi <section>'ı içinde
yerleştirilir.

`grid g3` içinde iç içe `<div>`ler olduğu için kapanış etiketi sayaçla
bulunur — düz regex yanlış yerden keserdi.

Kullanim: python scripts/move_industries_after_faq.py [--dry-run]
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# Sarmalayıcı sayfadan sayfaya değişiyor: `style="margin-top:40px"`,
# `margin-top:56px` ya da düz `<div class="sh">` (bu sonuncusunda blok zaten
# kendi <section>'ı içinde). Hepsini yakalamak için desen kullanılır.
SH = re.compile(r'<div class="sh"[^>]*>')
ETIKET = '<div class="slabel">Endüstriler</div>'
FAQ_SON = '<!-- /cz-faq -->'


def div_sonu(txt, bas):
    """`bas` konumundaki <div>'in kapanış </div>'ini sayarak bulur."""
    i, derinlik = bas, 0
    for m in re.finditer(r'<div\b|</div>', txt[bas:]):
        if m.group(0) == '</div>':
            derinlik -= 1
            if derinlik == 0:
                return bas + m.end()
        else:
            derinlik += 1
    return -1


def main():
    rapor = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        txt = io.open(path, encoding="utf-8").read()
        ad = os.path.basename(path)

        e = txt.find(ETIKET)
        if e < 0 or FAQ_SON not in txt:
            continue
        # etiketi saran .sh bloğunun başı (etiketten geriye en yakın eşleşme)
        onceki = [m.start() for m in SH.finditer(txt, 0, e)]
        if not onceki:
            rapor.append((ad, "sh bulunamadı")); continue
        sh_bas = onceki[-1]
        sh_son = div_sonu(txt, sh_bas)
        # hemen ardından gelen grid
        g_bas = txt.find('<div class="grid', sh_son)
        if g_bas < 0 or g_bas - sh_son > 40:
            rapor.append((ad, "grid bulunamadı")); continue
        g_son = div_sonu(txt, g_bas)
        if g_son < 0:
            rapor.append((ad, "grid kapanışı bulunamadı")); continue

        blok = txt[sh_bas:g_son]
        # bloğu yerinden çıkar (önündeki boşlukla birlikte)
        kalan = txt[:sh_bas].rstrip() + "\n  " + txt[g_son:].lstrip()

        # Blok kendi <section>'ının tek içeriğiyse geriye boş bir section kalır;
        # onu da temizle.
        kalan = re.sub(r'<section[^>]*>\s*</section>\s*', '', kalan)

        # SSS'ten sonra kendi section'ı içinde yeniden ekle
        yeni_bolum = (
            '\n\n<!-- cz-endustriler -->\n'
            '<section class="section">\n  '
            + SH.sub('<div class="sh" style="margin-bottom:26px;">', blok, count=1)
            + '\n</section>\n<!-- /cz-endustriler -->'
        )
        i = kalan.find(FAQ_SON)
        if i < 0:
            rapor.append((ad, "SSS işaretçisi kayboldu")); continue
        i += len(FAQ_SON)
        yeni = kalan[:i] + yeni_bolum + kalan[i:]

        if not DRY:
            io.open(path, "w", encoding="utf-8", newline="").write(yeni)
        rapor.append((ad, "taşındı"))

    for ad, d in rapor:
        print(f"  {ad:<36}{d}")
    tamam = sum(1 for _, d in rapor if d == "taşındı")
    print(f"\n{tamam}/{len(rapor)} sayfa" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
