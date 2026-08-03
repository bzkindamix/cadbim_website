# -*- coding: utf-8 -*-
"""Yeni sektor sayfalari icin OG gorseli uretir (assets/og/sektor_*.png).

Mevcut 7 sektorun OG sablonunu birebir taklit eder: 1200x630 koyu navy zemin,
soluk izgara, aksan renkli etiket + nokta, beyaz baslik + aksan alt cizgisi,
gri aciklama, sag ustte beyaz CADBIM logosu, sol altta cerceveli alan adi.
"""
import io
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "og")
FONTS = r"C:\Windows\Fonts"

PAGES = [
    {
        "file": "sektor_icmimarlik.png",
        "acc": (244, 114, 182),
        "label": "İÇ MİMARLIK & TASARIM",
        "title": "İç Mimarlık Çözümleri",
        "desc": ["Cadbim İç Mimarlık çözümleri — SketchUp, Chaos Corona, V-Ray,",
                 "Lumion ve Adobe ile konseptten fotogerçekçi sunuma"],
    },
    {
        "file": "sektor_tesisat.png",
        "acc": (45, 212, 191),
        "label": "MEKANİK TESİSAT",
        "title": "Mekanik Tesisat Çözümleri",
        "desc": ["Cadbim MEP çözümleri — Revit MEP, Fabrication CADmep/CAMduct,",
                 "Autodesk CFD ve HP donanımıyla modelden imalata"],
    },
]


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def white_logo(path, height):
    """Koyu logoyu beyaza cevirip hedef yukseklige olcekler."""
    img = Image.open(path).convert("RGBA")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 0:
                # koyu pikselleri beyaza tasi, alfayi koru
                lum = (r + g + b) / 3.0
                na = int(a * (1.0 - lum / 255.0)) if lum > 200 else a
                px[x, y] = (255, 255, 255, na)
    scale = height / float(h)
    return img.resize((int(w * scale), height), Image.LANCZOS)


def build(cfg):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (6, 12, 26))
    dr = ImageDraw.Draw(im)

    # hafif capraz aydinlanma (sol ust daha acik)
    for y in range(H):
        for step in ():
            pass
    grad = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(grad)
    for i in range(60):
        alpha = int(26 * (1 - i / 60.0))
        gd.ellipse([-500 + i * 6, -420 + i * 5, 900 - i * 6, 420 - i * 5], fill=alpha)
    im = Image.composite(Image.new("RGB", (W, H), (16, 26, 48)), im, grad)
    dr = ImageDraw.Draw(im)

    # soluk izgara
    for x in range(0, W, 46):
        dr.line([(x, 0), (x, H)], fill=(13, 21, 38), width=1)
    for y in range(0, H, 46):
        dr.line([(0, y), (W, y)], fill=(13, 21, 38), width=1)

    acc = cfg["acc"]
    # etiket + nokta
    f_lbl = font("segoeuib.ttf", 26)
    dr.ellipse([80, 96, 96, 112], fill=acc)
    dr.text((110, 88), cfg["label"], font=f_lbl, fill=acc)

    # baslik + ilk kelime altina aksan cizgisi
    f_ttl = font("segoeuib.ttf", 64)
    dr.text((80, 168), cfg["title"], font=f_ttl, fill=(255, 255, 255))
    first = cfg["title"].split(" ")[0]
    fw = dr.textlength(first[:2], font=f_ttl)
    dr.rectangle([80, 250, 80 + max(fw, 90), 258], fill=acc)

    # aciklama (gri, 2 satir)
    f_desc = font("segoeui.ttf", 30)
    for i, line in enumerate(cfg["desc"]):
        dr.text((80, 288 + i * 40), line, font=f_desc, fill=(158, 168, 188))

    # sag ustte beyaz logo
    logo = white_logo(os.path.join(ROOT, "assets", "logos", "cadbim-yatay.png"), 34)
    im.paste(logo, (W - logo.width - 78, 88), logo)

    # sol altta cerceveli alan adi
    f_dom = font("segoeuib.ttf", 26)
    tw = dr.textlength("cadbim.com.tr", font=f_dom)
    x0, y0 = 80, 538
    dr.rounded_rectangle([x0, y0, x0 + tw + 36, y0 + 48], radius=8,
                         outline=(129, 140, 248), width=2)
    dr.text((x0 + 18, y0 + 8), "cadbim.com.tr", font=f_dom, fill=(129, 140, 248))

    path = os.path.join(OUT, cfg["file"])
    im.save(path, "PNG", optimize=True)
    return path


if __name__ == "__main__":
    for cfg in PAGES:
        p = build(cfg)
        print("OK %-26s %.1f KB" % (os.path.basename(p), os.path.getsize(p) / 1024.0))
