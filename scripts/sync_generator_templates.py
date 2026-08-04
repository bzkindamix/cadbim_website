# -*- coding: utf-8 -*-
"""Ureteç sablonlarini guncel referans sayfalardan yeniden turetir.

NEDEN VAR: sync_youtube_blog.py ve gen_ultimaker_s_pages.py sayfayi bir
str.format sablonundan uretir. Site elle bakim gordukce (nav, betik surumleri,
altlik, CSS surumleri...) sablonlar geride kalir; ureteç bir daha calistiginda
aylar oncesinin kalibini geri yazar. Ayrica es zamanli calisan bir dal bu
dosyalari degistirdiginde rebase CAKISMA VERMEZ -- degisiklik sablonun
yeniden yazilan bolgesinin icinde kaldigi icin eski deger sessizce korunur.

BU BETIK NE YAPAR: referans sayfayi okur, degisken kisimlari yer tutucularla
degistirir, sablonu ayni veriyle yeniden derleyip kaynak sayfayla BAYT BAYT
karsilastirir ve ancak dogrulama gecerse betige yazar. Yani sablon her zaman
gercek bir sayfanin birebir kopyasidir; elle yama gerekmez.

KULLANIM:
    python scripts/sync_generator_templates.py            # yaz
    python scripts/sync_generator_templates.py --check    # yalnizca denetle
                                                          # (fark varsa cikis 1)
Referans sayfa degisirse (nav/altlik/surum) bu betigi calistirmak yeterlidir.
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _oku(yol):
    with io.open(os.path.join(BASE, yol), encoding="utf-8") as f:
        return f.read()


def _kes(metin, once, sonra, isaret):
    """`once` ile `sonra` arasindaki parcayi isaretle degistir; parcayi da dondur."""
    i = metin.index(once) + len(once)
    j = metin.index(sonra, i)
    return metin[:i] + isaret + metin[j:], metin[i:j]


# --------------------------------------------------------------------------
# BLOG YAZISI SABLONU  <-  post/3d-gorunum.html
# --------------------------------------------------------------------------
BLOG_REFERANS = "post/3d-gorunum.html"
BLOG_VERI = dict(
    desc="Bu Cadbim Teknik Destek videosunda 3D Görünüm konusu ele alınıyor.",
    title="3D Görünüm",
    tr_date="26 Ekim 2018",
    iso_date="2018-10-26",
    video_id="j3gVA-axUVQ",
    slug="3d-gorunum",
    category="Genel",
    prod_spans="",
    cta_page="autodesk",
)


def blog_sablonu():
    kaynak = _oku(BLOG_REFERANS)
    m = re.search(r'\n  <div class="a-related">.*?\n  </div>\n', kaynak, re.S)
    if not m:
        raise SystemExit(f"{BLOG_REFERANS}: 'İlgili Yazılar' blogu bulunamadi")
    related = m.group(0).strip("\n")
    t = kaynak[: m.start()] + "\n@@RELATED@@\n" + kaynak[m.end():]
    t = t.replace("{", "{{").replace("}", "}}")
    for eski, yeni in (
        (BLOG_VERI["desc"], "{desc}"),
        (BLOG_VERI["title"], "{title}"),
        (BLOG_VERI["tr_date"], "{tr_date}"),
        (BLOG_VERI["iso_date"], "{iso_date}"),
        (BLOG_VERI["video_id"], "{video_id}"),
        (BLOG_VERI["slug"], "{slug}"),
        ('<span class="atag cat">Genel</span>', '<span class="atag cat">{category}</span>'),
        ('<a href="../autodesk" class="btn-p">', '<a href="../{cta_page}" class="btn-p">'),
    ):
        if eski not in t:
            raise SystemExit(f"{BLOG_REFERANS}: beklenen parca yok -> {eski[:60]!r}")
        t = t.replace(eski, yeni)
    t = t.replace(
        '<span class="atag cat">{category}</span>\n    \n  </div>',
        '<span class="atag cat">{category}</span>\n    {prod_spans}\n  </div>',
    )
    sablon = t.replace("@@RELATED@@", "{related}")
    if sablon.format(related=related, **BLOG_VERI) != kaynak:
        raise SystemExit(f"{BLOG_REFERANS}: bayt bayt dogrulama BASARISIZ")
    return sablon


# --------------------------------------------------------------------------
# ULTIMAKER URUN SAYFASI SABLONU  <-  cadbim_ultimaker_s3.html
# --------------------------------------------------------------------------
UM_REFERANS = "cadbim_ultimaker_s3.html"
UM_VERI = dict(
    meta_desc=(
        "UltiMaker S3: Kompakt masaüstü mühendislik yazıcısı. Kompozite hazır çift "
        "ekstruder, otomatik tabla seviyeleme, 190+ malzeme desteği. Cadbim yetkili iş ortağı."
    ),
    title="UltiMaker S3 3D Yazıcı | Cadbim",
    og_title="UltiMaker S3 | Cadbim",
    hero_p=(
        "Masaüstünde rahatça yer bulan UltiMaker S3, cam ve karbon fiber kompozit baskıya "
        "hazır. Çözülebilir destek malzemeleriyle karmaşık geometrilerde daha fazla tasarım "
        "özgürlüğü sunar."
    ),
    kicker="S Serisi · Kompakt Mühendislik Yazıcısı",
    h1="Masaya Sığan Güç",
    video_src="https://www.youtube-nocookie.com/embed/WV2C6YXMJzc",
    hero_img="assets/products/ultimaker-web/s3-hero.webp",
    slug="ultimaker-s3",
    name="UltiMaker S3",
)
# Sira onemli: uzun metinler once, yoksa "UltiMaker S3" once eslesir ve
# baslik/aciklama icindeki gecisleri bozar.
UM_SIRA = ("meta_desc", "title", "og_title", "hero_p", "kicker", "h1",
           "video_src", "hero_img", "slug", "name")


def ultimaker_sablonu():
    kaynak = _oku(UM_REFERANS)
    t = kaynak
    t, cross = _kes(t, '<div class="grid g3" style="margin-top:0;">\n',
                    '\n  </div>\n</section>\n<div class="cta-strip">', "@@CROSS@@")
    t, features = _kes(t, 'ile Neler Yapabilirsiniz?</div></div>\n  <div class="grid g3">',
                       "</div>\n</section>", "@@FEAT@@")
    t, usecases = _kes(t, 'Kimler İçin?</div></div>\n  <div class="grid g3">',
                       "</div>\n</section>", "@@USE@@")
    t = t.replace("{", "{{").replace("}", "}}")
    for anahtar in UM_SIRA:
        deger = UM_VERI[anahtar]
        if deger not in t:
            raise SystemExit(f"{UM_REFERANS}: beklenen parca yok -> {anahtar}")
        t = t.replace(deger, "{%s}" % anahtar)
    for isaret, yer in (("@@CROSS@@", "{cross_cards}"),
                        ("@@FEAT@@", "{features}"),
                        ("@@USE@@", "{usecases}")):
        t = t.replace(isaret, yer)
    if t.format(features=features, usecases=usecases, cross_cards=cross, **UM_VERI) != kaynak:
        raise SystemExit(f"{UM_REFERANS}: bayt bayt dogrulama BASARISIZ")
    return t


HEDEFLER = [
    ("scripts/sync_youtube_blog.py", "POST_TEMPLATE", BLOG_REFERANS, blog_sablonu),
    ("scripts/gen_ultimaker_s_pages.py", "TEMPLATE", UM_REFERANS, ultimaker_sablonu),
]


def main():
    yalnizca_denetle = "--check" in sys.argv
    farkli = 0
    for yol, degisken, referans, uret in HEDEFLER:
        tam = os.path.join(BASE, yol)
        betik = io.open(tam, encoding="utf-8").read()
        bas = degisken + ' = """'
        i = betik.index(bas)
        j = betik.index('"""', i + len(bas)) + 3
        mevcut = betik[i + len(bas): j - 3]
        yeni = uret()
        if mevcut == yeni:
            print(f"guncel   {yol}  ({degisken} <- {referans})")
            continue
        farkli += 1
        if yalnizca_denetle:
            print(f"GERIDE   {yol}  ({degisken} <- {referans})")
            continue
        io.open(tam, "w", encoding="utf-8", newline="").write(
            betik[:i] + bas + yeni + '"""' + betik[j:]
        )
        print(f"YAZILDI  {yol}  ({degisken} <- {referans})")
    if yalnizca_denetle and farkli:
        print(f"\n{farkli} sablon referans sayfadan geride. Duzeltmek icin:")
        print("  python scripts/sync_generator_templates.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
