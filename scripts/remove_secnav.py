"""
Sektor (endustri) sayfalarindaki ust "endustri gecis seridi"ni (.secnav) kaldirir.

Serit; sabit basligin (68px) altinda sticky duruyor ve `margin-top:68px` ile
basligi telafi ediyordu. Serit kalkinca bu telafi de kalkacagi icin hero'nun
ust dolgusu basligi temizleyecek sekilde buyutulur:
    masaustu  40px -> 108px   (68 baslik + 40 mevcut bosluk)
    mobil     32px -> 100px   (68 baslik + 32 mevcut bosluk)

Kaldirilanlar: <nav class="secnav">...</nav>, onu izleyen secnavTrack script'i
ve kullanilmayan .secnav / .sec-* CSS kurallari.

Kullanim: python scripts/remove_secnav.py [--dry-run]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# <nav class="secnav"> ... </nav> ve hemen ardindaki secnavTrack script'i
BLOCK = re.compile(
    r'\n?<nav class="secnav".*?</nav>\s*<script>.*?secnavTrack.*?</script>\n?',
    re.S,
)
# Artik kullanilmayan CSS satirlari (her biri kendi satirinda)
CSS_LINE = re.compile(
    r'^[ \t]*(?:\.secnav[\w-]*|\.sec-(?:card|ico|name|bar)[^{,]*)'
    r'(?:[^\n{]*)\{[^\n}]*\}[ \t]*\n',
    re.M,
)
# .sec-* iceren reduced-motion satiri
CSS_RM = re.compile(r'^[ \t]*@media\(prefers-reduced-motion:reduce\)\{\.sec-card[^\n]*\n', re.M)


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "sektor_*.html"))):
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        orig = txt

        txt, n_block = BLOCK.subn("\n", txt)
        txt, n_css = CSS_LINE.subn("", txt)
        txt, n_rm = CSS_RM.subn("", txt)

        # Basligi temizlemek icin hero ust dolgusunu buyut
        txt, n_d = re.subn(r'\.hero\{padding:40px 3rem 56px;\}',
                           '.hero{padding:108px 3rem 56px;}', txt)
        txt, n_m = re.subn(r'\.hero\{padding:32px 1\.5rem 44px;\}',
                           '.hero{padding:100px 1.5rem 44px;}', txt)

        if txt != orig:
            rows.append((name, n_block, n_css + n_rm, n_d, n_m))
            if not DRY:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(txt)

    print(f"{'sayfa':<26}{'serit':>6}{'css':>5}{'hero-d':>8}{'hero-m':>8}")
    for r in rows:
        print(f"{r[0]:<26}{r[1]:>6}{r[2]:>5}{r[3]:>8}{r[4]:>8}")
    print(f"\n{len(rows)} sayfa" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
