"""
"İlgili İçerikler" şeridinde yazı tipi blog kartlarına thumbnail ekler.

Sorun (Onur, 2026-08-05): Şeritte video kartları 16:9 thumbnail + başlık
biçiminde görünürken, yazı tipi içerikler görselsiz düz metin kutusu olarak
kalıyordu; aynı satırda iki farklı kart biçimi yan yana duruyordu.

Çözüm: Blog listeleme sayfasındaki (`cadbim_blog.html`) mevcut ve doğru desen
buraya taşınır — ürün logosu, 16:9 kutuda, beyaza çevrilip (brightness/invert)
koyu gradyan üzerine oturtulur. Ürün eşleşmezse Cadbim markası kullanılır;
böylece her kartın thumbnail'ı olur ve şerit tek biçim görünür.

Ürün→logo haritası cadbim_blog.html'deki PRODUCT_ICON ile aynıdır (tek kaynak
olsun diye birebir kopyalandı; ikisi de aynı blog-posts.json'u okuyor).

Kullanim: python scripts/blog_related_thumbs.py [--dry-run]
"""
import glob
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

# Yazı tipi kartın ESKİ hâli (79 sayfada birebir aynı)
ESKI = (
      "      return '<a href=\"post/'+p.slug+'\" style=\"display:block;background:#0d1830;"
      "border-radius:16px;border:.5px solid rgba(255,255,255,.1);padding:20px;text-decoration:none;\">'\n"
      "        + '<div style=\"font-size:10px;color:#00c8f0;text-transform:uppercase;"
      "letter-spacing:1px;margin-bottom:8px;\">'+esc(p.cat)+'</div>'\n"
)

# Yeni hâli: video kartıyla aynı iskelet (16:9 görsel + gövde)
YENI = (
      "      var logo=(p.products||[]).map(function(x){return PRODUCT_ICON[x];}).filter(Boolean)[0];\n"
      "      var gorsel=logo?'assets/logos/products/'+logo:'assets/logos/cadbim-logo.png';\n"
      "      return '<a href=\"post/'+p.slug+'\" style=\"display:block;background:#0d1830;"
      "border-radius:16px;border:.5px solid rgba(255,255,255,.1);overflow:hidden;text-decoration:none;\">'\n"
      "        + '<div style=\"aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;"
      "background:linear-gradient(135deg,#13294a 0%,#101d3a 100%);\">"
      "<img src=\"'+gorsel+'\" alt=\"\" style=\"max-width:44%;max-height:40%;width:auto;height:auto;"
      "object-fit:contain;filter:brightness(0) invert(1);opacity:.7;\" loading=\"lazy\" decoding=\"async\"></div>'\n"
      "        + '<div style=\"padding:16px;\">'\n"
      "        + '<div style=\"font-size:10px;color:#00c8f0;text-transform:uppercase;"
      "letter-spacing:1px;margin-bottom:8px;\">'+esc(p.cat)+'</div>'\n"
)

# Kartın kapanışı: eski sürümde </a> ile bitiyordu, artık gövde <div>'i de kapanmalı
ESKI_SON = ("'<p style=\"font-size:11px;color:rgba(255,255,255,.3);margin:0;\">'"
            "+esc(p.trdate)+'</p></a>';")
YENI_SON = ("'<p style=\"font-size:11px;color:rgba(255,255,255,.3);margin:0;\">'"
            "+esc(p.trdate)+'</p></div></a>';")

# Ürün→logo haritası (cadbim_blog.html ile aynı)
HARITA = """  var PRODUCT_ICON={'Revit':'revit.svg','Revit LT':'revit-lt.svg','Inventor':'inventor.svg','Fusion':'fusion.svg','AutoCAD':'autocad.svg','AutoCAD LT':'autocad-lt.svg','AutoCAD Web':'autocad-web.svg','Alias':'alias.svg','Vault':'vault-pdm.svg','PDM':'vault-pdm.svg','PLM':'fusion-manage.svg','InfraWorks':'infraworks.svg','Forma':'forma.svg','Navisworks':'navisworks.svg','Civil 3D':'civil3d.svg','Advance Steel':'advance-steel.svg','Robot Structural':'robot-structural.svg','CFD':'cfd.png','Factory Design':'factory-design.svg','Fabrication':'fabrication.svg','Maya':'maya.svg','3ds Max':'3dsmax.svg','Recap Pro':'recap-pro.svg','Illustrator':'illustrator.svg','Photoshop':'photoshop.svg','Acrobat':'acrobat.svg','Firefly':'firefly.svg','Adobe Express':'adobe-express.svg','BIM Collaborate Pro':'forma.svg','Autodesk Docs':'forma.svg','Nastran':'inventor.svg'};
"""
HARITA_ANKOR = "  function esc(s){"


def main():
    rapor = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        ad = os.path.basename(path)
        txt = io.open(path, encoding="utf-8").read()
        if "blogRelatedGrid" not in txt:
            continue
        if ESKI not in txt or ESKI_SON not in txt:
            rapor.append((ad, "kalıp eşleşmedi")); continue
        if "PRODUCT_ICON" in txt:
            rapor.append((ad, "zaten uygulanmış")); continue

        yeni = txt.replace(ESKI, YENI, 1).replace(ESKI_SON, YENI_SON, 1)
        yeni = yeni.replace(HARITA_ANKOR, HARITA + HARITA_ANKOR, 1)

        if not DRY:
            io.open(path, "w", encoding="utf-8", newline="").write(yeni)
        rapor.append((ad, "tamam"))

    tamam = sum(1 for _, d in rapor if d == "tamam")
    for ad, d in rapor:
        if d != "tamam":
            print(f"  {ad:<36}{d}")
    print(f"\n{tamam}/{len(rapor)} sayfa" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
