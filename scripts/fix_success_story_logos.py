"""
Başarı öyküsü kartlarındaki müşteri logolarını okunur hale getirir.

Sorun: `.card-icon` (site genelinde ~10 şablonda tanımlı, 46x46 kare, ikon
GLİFLERİ için tasarlanmış: `color:var(--cyan)`, `font-size:22px`) burada
müşteri logosu resmi taşımak için yeniden kullanılmıştı; içindeki <img>'e
26x26px kare sınır konmuştu. Bu firma logoları (Edvan 267x90, Kutlusan
596x90 gibi) geniş yatay wordmark'lar — kare kutuya `object-fit:contain`
ile sığdırılınca 26x8px, hatta 26x4px'e düşüyor; okunmuyor.

Referans: Ana sayfadaki (`cadbim_basari_oykuleri.html`) `.story-logo` kuralı
zaten doğru deseni kullanıyor: sabit YÜKSEKLİK + `width:auto` + BEYAZ zemin
(saydam PNG/SVG logolar, karanlık zeminde rengi kaybolmasın diye). Bu script
aynı deseni `.card-icon` içindeki başarı öyküsü logolarına da uygular —
paylaşılan `.card-icon` sınıfını GLOBAL olarak değiştirmez (diğer 10+
şablonda ikon glifi için kullanılıyor), yalnızca bu örneklerin satır-içi
style'larını değiştirir.

Kullanim: python scripts/fix_success_story_logos.py [--dry-run]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

PAT = re.compile(
    r'<div class="card-icon" style="background:rgba\(0,200,240,\.12\);">'
    r'(<img src="assets/logos/success-stories/[^"]+" alt="[^"]*")'
    r'\s+style="width:26px;height:26px;object-fit:contain;border-radius:4px;">'
    r'(</div>)'
)


# İki SVG (norm-additive, sistem-teknik-electron) beyaz/açık renkli çizili —
# beyaz zeminde kayboluyorlar. PNG'lerin tamamı koyu/renkli, beyaz zeminde
# okunuyor. Bu ikisi için zemin koyu (kartla uyumlu lacivert) kalır.
ACIK_RENKLI_SVG = {"norm-additive.svg", "sistem-teknik-electron.svg"}


def rep(m):
    img_bas, kapanis = m.groups()
    dosya = re.search(r'success-stories/([^"]+)"', img_bas).group(1)
    if dosya in ACIK_RENKLI_SVG:
        zemin = 'background:#1a2947;border:.5px solid rgba(255,255,255,.14);'
    else:
        zemin = 'background:#fff;'
    return (
        '<div class="card-icon" style="display:inline-flex;width:auto;height:34px;'
        'padding:6px 12px;' + zemin + 'border-radius:8px;">'
        + img_bas +
        ' style="height:100%;width:auto;max-width:118px;object-fit:contain;'
        'display:block;">'
        + kapanis
    )


# İkinci varyant: koyu zeminli "chip" linki (sektor_medya.html) — logo yanında
# firma adı zaten metin olarak okunuyor, bu yüzden beyaz yama gerekmiyor;
# yalnızca kare sınırlaması kaldırılıp doğal en-boy oranıyla büyütülüyor.
PAT_CHIP = re.compile(
    r'(<img src="assets/logos/success-stories/[^"]+" alt="[^"]*")'
    r'\s+style="width:18px;height:18px;object-fit:contain;border-radius:3px;">'
)
REP_CHIP = r'\1 style="height:18px;width:auto;max-width:54px;object-fit:contain;">'


def main():
    toplam = 0
    dosyalar = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        yeni, n = PAT.subn(rep, txt)
        yeni, n2 = PAT_CHIP.subn(REP_CHIP, yeni)
        n += n2
        if n:
            dosyalar.append((os.path.basename(path), n))
            toplam += n
            if not DRY:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(yeni)

    for ad, n in dosyalar:
        print(f"  {ad:<36}{n}")
    print(f"\n{len(dosyalar)} sayfa, {toplam} logo" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
