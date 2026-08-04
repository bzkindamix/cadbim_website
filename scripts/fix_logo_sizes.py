"""
Marka/urun logolarinin olcusunu site genelinde normallestirir.

Sorun: logo kutulari buyuk ama icindeki gorsele kucuk sabit sinirlar konmus;
logolar 18-28px araliginda kaliyordu. Referans olcu cadbim_urunler.html
(ana urun katalogu): 44px kutu / 42px logo.

Uc markup varyanti duzeltilir:
  1. .brand-row logo kutusu  : 28px kutu (pad 4-5) -> logo 18-20px
  2. sektor .pcard logo kutusu: 40px kutu (pad 6-7) -> logo 26-28px
  3. .pico icindeki <img>     : max 26px veya sabit 28px

Kullanim: python scripts/fix_logo_sizes.py [--dry-run]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# Bir DIV/SPAN'in hemen ardindan gelen assets/logos/ gorseli — kutulu varyantlar.
BOX_IMG = re.compile(
    r'(<(?:div|span)\b[^>]*?style=")([^"]*)("[^>]*>\s*<img\b[^>]*?assets/logos/[^>]*>)'
)
# .pico kutusunun icindeki gorsel — sinif tabanli varyant.
PICO_IMG = re.compile(r'(<div class="pico"[^>]*>\s*<img\b[^>]*?style=")([^"]*)(")')


def set_px(style, prop, value):
    """style icindeki `prop:<sayi>px` degerini gunceller; yoksa ekler."""
    pat = re.compile(r'(^|;)\s*' + re.escape(prop) + r':\s*\d+px')
    if pat.search(style):
        return pat.sub(lambda m: m.group(1) + prop + ":" + str(value) + "px", style, count=1)
    return style.rstrip(";") + ";" + prop + ":" + str(value) + "px"


def fix_box(style):
    """Logo saran kutuyu buyutur. Degistiyse yeni style, degilse None."""
    w = re.search(r'(?:^|;)\s*width:\s*(\d+)px', style)
    h = re.search(r'(?:^|;)\s*height:\s*(\d+)px', style)
    if not (w and h):
        return None
    box = int(w.group(1))
    if int(h.group(1)) != box:          # kare olmayan kutulara dokunma
        return None
    if box == 28:                        # brand-row
        new_box, new_pad, new_rad = 44, 6, 9
    elif box == 40:                      # sektor pcard
        new_box, new_pad, new_rad = 52, 5, 11
    else:
        return None                      # 44px ve ustu zaten yeterli
    s = set_px(style, "width", new_box)
    s = set_px(s, "height", new_box)
    if re.search(r'(?:^|;)\s*padding:\s*\d+px', s):
        s = set_px(s, "padding", new_pad)
    if re.search(r'(?:^|;)\s*border-radius:\s*\d+px', s):
        s = set_px(s, "border-radius", new_rad)
    return s


def fix_img(style):
    """Gorsele konmus kucuk sabit sinirlari 42px standardina cikarir."""
    s = style
    changed = False
    # max-width/max-height ciftini buyut
    mw = re.search(r'(?:^|;)\s*max-width:\s*(\d+)px', s)
    if mw and int(mw.group(1)) < 42:
        s = set_px(s, "max-width", 42)
        s = set_px(s, "max-height", 42)
        changed = True
    # sabit width/height -> esnek max-* (logo en-boy oranini korusun)
    fw = re.search(r'(?:^|;)\s*width:\s*(\d+)px', s)
    fh = re.search(r'(?:^|;)\s*height:\s*(\d+)px', s)
    if fw and fh and int(fw.group(1)) < 42:
        s = re.sub(r'(?:^|;)\s*width:\s*\d+px', "", s, count=1)
        s = re.sub(r'(?:^|;)\s*height:\s*\d+px', "", s, count=1)
        s = s.strip(";")
        if "max-width" not in s:
            s = s + ";max-width:42px;max-height:42px"
        changed = True
    return s if changed else None


def main():
    total_box = total_img = 0
    touched = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        orig = txt
        nb = ni = 0

        def _box(m):
            nonlocal nb
            new = fix_box(m.group(2))
            if new is None:
                return m.group(0)
            nb += 1
            return m.group(1) + new + m.group(3)

        txt = BOX_IMG.sub(_box, txt)

        def _img(m):
            nonlocal ni
            new = fix_img(m.group(2))
            if new is None:
                return m.group(0)
            ni += 1
            return m.group(1) + new + m.group(3)

        txt = PICO_IMG.sub(_img, txt)

        if txt != orig:
            touched.append((name, nb, ni))
            total_box += nb
            total_img += ni
            if not DRY:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(txt)

    for name, nb, ni in touched:
        print(f"  {name:<32} kutu:{nb:>3}  gorsel:{ni:>3}")
    print(f"\n{len(touched)} sayfa | {total_box} kutu | {total_img} gorsel"
          + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
