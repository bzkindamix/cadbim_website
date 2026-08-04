"""
Anasayfadaki Sektörler ve Çözümler seçim ekranlarına sektör kimliği ekler.

Sorun (mobil): Sektörler 9 tam genişlik satır olarak alt alta diziliyordu
(528px) ve HTML'de yazılı açıklama metni `display:none` ile gizliydi — geriye
yalnız kalın bir isim kalıyordu. Çözümler ise düz metin haplarıydı. İkisinde
de ikon, renk ve hareket yoktu.

Bu script yalnızca HTML tarafını hazırlar: her sektöre kendi vurgu rengini
(--sc), arka plan çizimini (--art) ve ikonunu ekler. Görsel kurallar
index.html içindeki stil bloğuna elle yazılır; masaustu gorunumu degismez.

İkon + renk haritası, sektör sayfalarından kaldırılan üst geçiş şeridinden
(.sec-card, DK-2026-08-04) devralındı; onu da mevcut subset fontta.

Kullanim: python scripts/mobil_sektor_cozum.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SAYFA = os.path.join(ROOT, "index.html")

# anahtar -> (vurgu rengi, tabler ikonu, arka plan cizimi)
SEKTOR = {
    "mimari":     ("#818cf8", "building",         "mimari"),
    "makine":     ("#f59e0b", "settings",         "makine"),
    "medya":      ("#c084fc", "movie",            "medya"),
    "icmimarlik": ("#f472b6", "armchair",         "icmimarlik"),
    "insaat":     ("#22c55e", "crane",            "insaat"),
    "tesisat":    ("#2dd4bf", "air-conditioning", "tesisat"),
    "otomotiv":   ("#ef4444", "car",              "otomotiv"),
    "egitim":     ("#38bdf8", "school",           "egitim"),
    "havacilik":  ("#a5b4fc", "plane",            "havacilik"),
    # yalnizca Cozumler sekmelerinde var
    "sanatsal_baski": ("#f472b6", "palette", None),
}


def sektor_kartlari(txt):
    """#sectorList içindeki 9 bağlantıya renk + çizim + ikon ekler."""
    n = 0

    def rep(m):
        nonlocal n
        bas, anahtar, kalan = m.group(1), m.group(2), m.group(3)
        if anahtar not in SEKTOR or 'class="sec-ic"' in kalan:
            return m.group(0)
        renk, ikon, art = SEKTOR[anahtar]
        stil = '--sc:' + renk + ';--art:url(assets/img/sektor/' + art + '.svg)'
        # mevcut style varsa basina ekle, yoksa yeni style
        if 'style="' in bas:
            bas = bas.replace('style="', 'style="' + stil + ';', 1)
        else:
            bas = bas.rstrip('>') + ' style="' + stil + '">'
        n += 1
        return (bas + '<span class="sec-ic" aria-hidden="true">'
                '<i class="ti ti-' + ikon + '"></i></span>' + kalan)

    # <a href="sektor-x" data-obj="anahtar" ...> ... <b>
    txt = re.sub(
        r'(<a href="sektor-[a-z]+" data-obj="([a-z]+)"[^>]*>)(\s*<b>)',
        rep, txt)
    return txt, n


def cozum_sekmeleri(txt):
    """.soltab-btn düğmelerine renk + ikon ekler."""
    n = 0

    def rep(m):
        nonlocal n
        bas, anahtar, kalan = m.group(1), m.group(2), m.group(3)
        if anahtar not in SEKTOR or 'ti ti-' in bas:
            return m.group(0)
        renk, ikon, _ = SEKTOR[anahtar]
        bas = bas.rstrip('>') + ' style="--sc:' + renk + '">'
        n += 1
        return bas + '<i class="ti ti-' + ikon + '" aria-hidden="true"></i>' + kalan

    txt = re.sub(
        r'(<button class="soltab-btn[^"]*"[^>]*data-tab="([a-z_]+)"[^>]*>)(.)',
        rep, txt)
    return txt, n


def main():
    with open(SAYFA, encoding="utf-8") as f:
        txt = f.read()
    orig = txt

    txt, n1 = sektor_kartlari(txt)
    txt, n2 = cozum_sekmeleri(txt)

    if txt != orig and not DRY:
        with open(SAYFA, "w", encoding="utf-8", newline="") as f:
            f.write(txt)

    print(f"  sektör kartı : {n1}/9")
    print(f"  çözüm sekmesi: {n2}/10")
    print("  (DRY-RUN)" if DRY else "  yazıldı")


if __name__ == "__main__":
    main()
