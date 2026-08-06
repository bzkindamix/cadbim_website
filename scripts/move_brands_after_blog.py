# -*- coding: utf-8 -*-
"""Sektor sayfalarinda Markalar bolumunu tek satirlik, yalniz-logo seride
donusturur ve Blog bolumunden sonraya (CTA seridinden once) tasir.

Onceki durum: Cozumler'den sonra, isim+urun listesi olan dikey brand-row'lar.
Yeni durum: Blog'dan sonra, sadece logo iceren tek siralik brand-strip.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    "sektor_mimari.html", "sektor_otomotiv.html", "sektor_makine.html",
    "sektor_insaat.html", "sektor_medya.html", "sektor_icmimarlik.html",
    "sektor_tesisat.html", "sektor_egitim.html", "sektor_havacilik.html",
    "sektor_yapi_urunleri.html", "sektor_tuketici_urunleri.html",
]

NAME_HREF = {
    "Autodesk": "autodesk", "Trimble": "sketchup", "Chaos": "chaos",
    "HP": "hp", "Adobe": "adobe", "Lumion": "lumion",
    "UltiMaker": "ultimaker", "Microsoft": "microsoft",
}

BRAND_STRIP_CSS = (
    ".brand-strip{display:flex;align-items:center;justify-content:center;"
    "flex-wrap:wrap;gap:14px;}\n"
    ".brand-strip a{display:flex;align-items:center;justify-content:center;"
    "background:var(--navy3);border:.5px solid var(--w10);border-radius:12px;"
    "height:60px;padding:10px 22px;transition:border-color .18s,transform .18s;}\n"
    ".brand-strip a:hover{border-color:var(--cbor);transform:translateY(-2px);}\n"
    ".brand-strip img{max-height:26px;max-width:110px;width:auto;object-fit:contain;}\n"
)


def process(fname):
    path = os.path.join(ROOT, fname)
    s = io.open(path, encoding="utf-8").read()

    m = re.search(r'<section class="brands">.*?</section>\n', s, re.S)
    assert m, "%s: brands section bulunamadi" % fname
    old_section = m.group(0)

    imgs = re.findall(r"(<img\b[^>]*>)", old_section)
    names = re.findall(r'class="brand-name">([^<]+)<', old_section)
    assert len(imgs) == len(names), "%s: img(%d)/isim(%d) sayisi uyusmuyor" % (
        fname, len(imgs), len(names))

    seen = set()
    links = []
    for img, name in zip(imgs, names):
        href = NAME_HREF.get(name.strip())
        if not href or href in seen:
            continue
        seen.add(href)
        links.append('<a href="%s" aria-label="%s">%s</a>' % (href, name.strip(), img))

    new_section = (
        '<section class="brands brand-strip-sec">\n'
        '  <div class="sh" style="margin-bottom:20px;text-align:center;">\n'
        '    <div class="slabel">Markalar</div>\n'
        '    <div class="stitle" role="heading" aria-level="2">Arkanızda Yetkili İş Ortakları Var</div>\n'
        '  </div>\n'
        '  <div class="brand-strip">' + "".join(links) + '</div>\n'
        '</section>\n'
    )

    # 1) eski bolumu kaldir
    s = s[:m.start()] + s[m.end():]

    # 2) blog script'inden hemen sonra, cta-strip'ten once yeni bolumu ekle
    i = s.index('<div class="cta-strip">')
    s = s[:i] + new_section + s[i:]

    # 3) CSS ekle (ilk </style> kapanisindan once, .ssub tanimindan sonra)
    anchor = ".ssub{"
    ai = s.index(anchor)
    ai_end = s.index("}", ai) + 1
    s = s[:ai_end] + "\n" + BRAND_STRIP_CSS.rstrip("\n") + s[ai_end:]

    io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    return len(links)


if __name__ == "__main__":
    for f in FILES:
        n = process(f)
        print("OK %-30s %d marka logosu" % (f, n))
