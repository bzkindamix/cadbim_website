# -*- coding: utf-8 -*-
"""Tabler ikon fontunun site-ozel subset'ini yeniden uretir.

Sitede fiilen kullanilan `ti ti-*` siniflarini (HTML + JS) tarar, Tabler'in
CDN'deki tam setinden yalnizca o ikonlarin glyph'lerini iceren bir woff2 ve
eslesme CSS'i uretir.

Yeni bir ikon kullanildiginda bu betigi calistirmak yeterlidir:

    python scripts/build_icon_subset.py

Cikti:
    assets/fonts/tabler-icons-subset.woff2
    assets/css/tabler-icons-subset.css

Gereksinim: `pip install fonttools brotli` ve internet erisimi.
"""
import io
import os
import re
import sys
import glob
import urllib.request

VERSION = "3.31.0"
CDN = "https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@%s/dist" % VERSION
CSS_URL = CDN + "/tabler-icons.min.css"
TTF_URL = CDN + "/fonts/tabler-icons.ttf"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_OUT = os.path.join(ROOT, "assets", "css", "tabler-icons-subset.css")
FONT_OUT = os.path.join(ROOT, "assets", "fonts", "tabler-icons-subset.woff2")
CACHE = os.path.join(ROOT, ".icon-subset-cache")

# Statik taramanin goremedigi, JS icinde uretilen veya ileride eklenmesi
# muhtemel ikonlar burada elle garanti altina alinir.
EXTRA = {"box", "building", "file", "home", "mail", "phone", "search", "send",
         "tools", "topology-star-3", "x", "gavel", "menu-2", "chevron-down",
         "chevron-right", "arrow-right"}


def fetch(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    if not os.path.isdir(CACHE):
        os.makedirs(CACHE)
    req = urllib.request.Request(url, headers={"User-Agent": "cadbim-build/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as fh:
        fh.write(r.read())
    return path


def used_icons():
    """HTML ve JS dosyalarinda gecen ti-* sinif adlari."""
    found = {}
    files = (glob.glob(os.path.join(ROOT, "*.html"))
             + glob.glob(os.path.join(ROOT, "post", "*.html"))
             + glob.glob(os.path.join(ROOT, "*.js")))
    for p in files:
        s = io.open(p, encoding="utf-8", errors="ignore").read()
        names = set(re.findall(r'ti ti-([a-z0-9-]+)', s))
        names |= set(re.findall(r'["\']ti-([a-z0-9-]+)["\']', s))
        for n in names:
            found.setdefault(n, set()).add(os.path.relpath(p, ROOT))
    return found


def main():
    css_src = io.open(fetch(CSS_URL, os.path.join(CACHE, "tabler.css")),
                      encoding="utf-8").read()
    mapping = dict(re.findall(r'\.ti-([a-z0-9-]+):before\{content:"\\([0-9a-f]{4,6})"\}',
                              css_src))
    if not mapping:
        sys.exit("Tabler CSS'inden codepoint eslemesi cikarilamadi (bicim degismis olabilir).")

    found = used_icons()
    wanted = set(found) | EXTRA
    unknown = sorted(n for n in wanted if n not in mapping)
    names = sorted(n for n in wanted if n in mapping)

    if unknown:
        print("UYARI — Tabler %s setinde karsiligi olmayan sinif(lar):" % VERSION)
        for n in unknown:
            where = ", ".join(sorted(found.get(n, ["(EXTRA listesi)"]))[:3])
            print("  ti-%-22s %s" % (n, where))

    codepoints = sorted({int(mapping[n], 16) for n in names})
    ttf = fetch(TTF_URL, os.path.join(CACHE, "tabler.ttf"))

    from fontTools import subset as ftsubset
    opts = ftsubset.Options()
    opts.flavor = "woff2"
    opts.desubroutinize = True
    opts.layout_features = []
    opts.notdef_outline = False
    opts.hinting = False
    opts.drop_tables += ['FFTM']
    font = ftsubset.load_font(ttf, opts)
    subsetter = ftsubset.Subsetter(options=opts)
    subsetter.populate(unicodes=codepoints)
    subsetter.subset(font)
    ftsubset.save_font(font, FONT_OUT, opts)
    font.close()

    out = [
        "/* Tabler Icons - CADBIM subset (%d ikon, Tabler %s). Tam setin (5000+ ikon)"
        " yerine sadece sitede kullanilan siniflari icerir.\n"
        "   Yeni ikon eklenirse yeniden uret: python scripts/build_icon_subset.py */"
        % (len(names), VERSION),
        '@font-face{font-family:"tabler-icons";font-style:normal;font-weight:400;'
        'src:url("../fonts/tabler-icons-subset.woff2?v=2") format("woff2")}',
        '.ti{font-family:"tabler-icons" !important;speak:none;font-style:normal;'
        'font-weight:normal;font-variant:normal;text-transform:none;line-height:1;'
        '-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;'
        'display:inline-block}',
    ]
    for n in names:
        out.append('.ti-%s:before{content:"\\%s"}' % (n, mapping[n]))
    io.open(CSS_OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")

    print("\nikon: %d  |  font: %.1f KB  |  css: %.1f KB"
          % (len(names), os.path.getsize(FONT_OUT) / 1024.0,
             os.path.getsize(CSS_OUT) / 1024.0))


if __name__ == "__main__":
    main()
