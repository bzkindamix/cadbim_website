"""
Webinar kartlarindaki "Kayit Ol" dugmelerine Teams etkinlik kayit linklerini koyar.

Kaynak: Kerimcan Erengin (D&M) ve Ezgi Uygun (AEC) tarafindan gonderilen
"FY27 Q3 Webinar Programi" e-postalari (28.07.2026). Dokuz webinarin tarihi
sitedeki kartlarla birebir eslesiyor.

Onceki durum: dugmeler kendi iletisim formumuza gidiyordu
(`iletisim?webinar=<slug>#form`). Artik dogrudan Teams kayit sayfasina gider;
dis baglanti oldugu icin yeni sekmede acilir.

Kullanim: python scripts/set_webinar_links.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SAYFA = os.path.join(ROOT, "cadbim_webinar.html")

TENANT = "8434bec9-4ba4-4cb2-b8d4-79b0e8ed07c6"
BASE = "https://events.teams.microsoft.com/event/"

# site slug -> Teams etkinlik kimligi
LINKLER = {
    # AEC (Ezgi Uygun)
    "aec-yapay-zeka":         "e55b1f26-68a0-4b65-b1f1-f6ee037c1ee9",
    "forma-proje-yonetimi":   "a9dd39a8-1d3c-405e-9b20-2064e3ce7b3b",
    "revit-lt-ilk-adim":      "00bd5555-4abf-4dd3-8973-dd3abcd30279",
    "bim-koordinasyon":       "68be3ea3-2ac6-44d9-897c-ff5b4f66e07a",
    # D&M (Kerimcan Erengin)
    "inventor-yapisal-analiz": "5f2c6ac3-319a-4263-ac92-2e7e3c37660f",
    "inventor-yapay-zeka":     "0a482530-7c04-45d8-85ea-207a187f13ac",
    "vault-veri-yonetimi":     "6ec7c569-fdb8-4f95-b6a0-f1eee52287ad",
    "plant3d-tesis-tasarimi":  "ca7dcb9b-f8ee-445c-864f-8410c685a84e",
    "fusion-yapay-zeka":       "20e28cec-f219-4341-a4e7-64cdc228f402",
}


def main():
    with open(SAYFA, encoding="utf-8") as f:
        txt = f.read()
    orig = txt
    yapildi, atlandi = [], []

    for slug, eid in LINKLER.items():
        hedef = BASE + eid + "@" + TENANT
        pat = re.compile(
            r'href="iletisim\?webinar=' + re.escape(slug) + r'#form"(\s+class="wbtn")')
        yeni, n = pat.subn(
            lambda m: 'href="' + hedef + '" target="_blank" rel="noopener"' + m.group(1),
            txt, count=1)
        if n:
            txt = yeni
            yapildi.append(slug)
        else:
            atlandi.append(slug)

    if txt != orig and not DRY:
        with open(SAYFA, "w", encoding="utf-8", newline="") as f:
            f.write(txt)

    for s in yapildi:
        print(f"  OK   {s}")
    for s in atlandi:
        print(f"  ATLA {s} (kalip eslesmedi)")
    print(f"\n{len(yapildi)}/{len(LINKLER)} link yerlestirildi"
          + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
