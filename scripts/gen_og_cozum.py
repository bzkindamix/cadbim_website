# -*- coding: utf-8 -*-
"""Yeni cozum sayfalari icin OG gorseli uretir (assets/og/cadbim_*.png).

gen_og_sektor.py icindeki sablonu (1200x630 koyu navy, soluk izgara, aksan
etiketi, beyaz baslik, gri aciklama, sag ustte beyaz logo, sol altta cerceveli
alan adi) aynen yeniden kullanir -- boylece 155 mevcut OG gorseliyle ayni dil
korunur.

Yeni bir cozum sayfasi eklendiginde PAGES listesine bir kayit ekleyip
calistirmak yeterlidir.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_og_sektor import build  # noqa: E402

PAGES = [
    {
        "file": "cadbim_bim_icerik_uretimi.png",
        "acc": (129, 140, 248),
        "label": "BIM İÇERİK & OBJE ÜRETİMİ",
        "title": "BIM İçerik Üretimi",
        "desc": [u"Revit aile üretimi, CAD verisinin BIM objesine dönüşümü,",
                 u"parametre standardı ve .rfa / IFC yayınlama"],
    },
    {
        "file": "cadbim_ai_gorsellestirme.png",
        "acc": (192, 132, 252),
        "label": "AI DESTEKLİ GÖRSELLEŞTİRME",
        "title": "AI Görselleştirme",
        "desc": [u"Metin isteminden konsept görsel, fotoğraftan PBR malzeme,",
                 u"çözünürlük yükseltme — karar sizde, işçilik yapay zekâda"],
    },
]


if __name__ == "__main__":
    for cfg in PAGES:
        p = build(cfg)
        print("OK %-34s %.1f KB" % (os.path.basename(p), os.path.getsize(p) / 1024.0))
