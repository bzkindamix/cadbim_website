"""
Basligi bir urun/marka adi olan kartlarda jenerik ikon yerine gercek logoyu koyar.

Ornek (cadbim_ai_gorsellestirme.html): "Chaos Veras", "Chaos V-Ray & Enscape" ve
"HP Z Workstation" kartlari <i class="ti ti-cube"> gosterirken ayni izgaradaki
komsulari (Cosmos, Corona, Firefly...) gercek logolarini gosteriyordu.

KAPSAM DISI (bilincli): basligi urun adi DEGIL, bir kategori/hizmet olan kartlar
ikonunu korur — ikon orada anlam tasiyor:
  - "Yetkili Teknik Servis" (ti-tool), "Sarf Malzemeleri" (ti-droplet)
  - "Tum Koleksiyon" (ti-box), "Donanim ->", "3D Baski ->"
  - "Malzeme Kutuphanesi" (ti-flask)

Kullanim: python scripts/fix_missing_logos.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

L = "assets/logos"
P = "assets/products"

# (dosya, slug) -> (logo yolu, dogal genislik, dogal yukseklik)
FIX = {
    ("cadbim_ai_gorsellestirme.html", "veras"):            (f"{L}/products/veras.png", 400, 400),
    ("cadbim_ai_gorsellestirme.html", "chaos"):            (f"{L}/products/vray.svg", 120, 120),
    ("cadbim_ai_gorsellestirme.html", "hp-z-workstation"): (f"{L}/hp-blue.png", 300, 300),
    ("cadbim_cura.html", "digital-factory"):               (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_designjet_t600.html", "hp-build-workspace"):  (f"{L}/hp-blue.png", 300, 300),
    ("cadbim_dijital_donusum.html", "nesting"):            (f"{L}/products/nesting.svg", 965, 1024),
    ("cadbim_dijital_donusum.html", "hp-z-workstation"):   (f"{L}/hp-blue.png", 300, 300),
    ("cadbim_dijital_donusum.html", "designjet"):          (f"{L}/hp-blue.png", 300, 300),
    ("cadbim_dijital_donusum.html", "hp-build-workspace"): (f"{L}/hp-blue.png", 300, 300),
    ("cadbim_dijital_donusum.html", "ultimaker"):          (f"{L}/products/ultimaker-icon.webp", 192, 192),
    ("cadbim_eklemeli_imalat.html", "method-xl"):          (f"{P}/ultimaker-method-xl.png", 285, 268),
    ("cadbim_eklemeli_imalat.html", "digital-factory"):    (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_fabrication_camduct.html", "nesting"):        (f"{L}/products/nesting.svg", 965, 1024),
    ("cadbim_factor4.html", "digital-factory"):            (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_ultimaker_s3.html", "digital-factory"):       (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_ultimaker_s5.html", "digital-factory"):       (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_ultimaker_s7.html", "digital-factory"):       (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_ultimaker_s8.html", "digital-factory"):       (f"{P}/ultimaker-digital-factory.png", 371, 331),
    ("cadbim_veras.html", "chaos"):                        (f"{L}/chaos.webp", 1280, 1280),
}

# Sayfalardaki dogru kartlarla ayni kalip
TPL = ('<div class="card-icon" style="background:rgba(255,255,255,.07);">'
       '<img width="{w}" height="{h}" src="{src}" alt="" '
       'style="width:32px;height:32px;object-fit:contain;" loading="lazy" decoding="async"></div>')


def main():
    done, missing = [], []
    by_file = {}
    for (fname, slug), v in FIX.items():
        by_file.setdefault(fname, []).append((slug, v))

    for fname, items in sorted(by_file.items()):
        path = os.path.join(ROOT, fname)
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        for slug, (src, w, h) in items:
            # <a href="slug" ... class="...card..."> hemen ardindan ikonlu card-icon
            pat = re.compile(
                r'(<a\s+href="' + re.escape(slug) + r'"[^>]*class="[^"]*\bcard\b[^"]*"[^>]*>\s*)'
                r'<div[^>]*class="card-icon"[^>]*>\s*<i\s+class="ti [a-z0-9- ]*"[^>]*></i>\s*</div>',
                re.S)
            new, n = pat.subn(lambda m: m.group(1) + TPL.format(w=w, h=h, src=src), txt, count=1)
            if n:
                txt = new
                done.append((fname, slug, src))
            else:
                missing.append((fname, slug))
        if not DRY:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(txt)

    for fname, slug, src in done:
        print(f"  OK   {fname:<34} {slug:<22} -> {src}")
    for fname, slug in missing:
        print(f"  ATLA {fname:<34} {slug:<22} (kalip eslesmedi)")
    print(f"\n{len(done)} kart duzeltildi, {len(missing)} eslesmedi"
          + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
