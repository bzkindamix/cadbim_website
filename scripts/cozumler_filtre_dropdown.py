"""
Çözümler sayfasındaki endüstri filtresini açılır listeye çevirir.

Gerekçe (Onur, 2026-08-05): "endüstri filtrelerini de blogta kullandığımız
stil istiyorum" — 9 çip iki satıra yayılıyordu. Çipler <select>'e dönüşür,
sayfada yüklü olan cbselect bileşeni onu sitenin dilinde açılır listeye
çevirir (ikon + renk + sayaç korunur; native <select> bunları gösteremezdi).

Mevcut filtre mantığı (apply/hash) korunur: liste yalnızca <select>'in
değerini değiştirir, `change` olayı aynı apply() çağrısını yapar.

Kullanim: python scripts/cozumler_filtre_dropdown.py [--dry-run]
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SAYFA = os.path.join(ROOT, "cadbim_cozumler.html")

ESKI_JS = """  var btns=[].slice.call(bar.querySelectorAll('.cz-fbtn'));"""
YENI_JS = """  var sel=bar.querySelector('#czFiltre');"""

ESKI_BTN_GUNCELLE = """    btns.forEach(function(b){
      var on=b.getAttribute('data-f')===f;
      b.classList.toggle('is-on',on); b.setAttribute('aria-pressed',on?'true':'false');
    });"""
YENI_BTN_GUNCELLE = """    if(sel.value!==f){ sel.value=f; sel.dispatchEvent(new Event('cbsel-yansit')); }"""

ESKI_TIK = """  bar.addEventListener('click',function(e){
    var b=e.target.closest('.cz-fbtn'); if(!b) return;
    /* "Tum Cozumler" dugmesi yok: aktif filtreye yeniden basmak filtreyi temizler. */
    apply(b.classList.contains('is-on')?'all':b.getAttribute('data-f'),true);
  });"""
YENI_TIK = """  sel.addEventListener('change',function(){ apply(sel.value,true); });"""


def main():
    t = io.open(SAYFA, encoding="utf-8").read()
    rapor = []

    # 1) Cipleri oku
    ciddi = re.search(r'(<div class="cz-fbtns"[^>]*>)(.*?)(</div>)', t, re.S)
    if not ciddi:
        print("cz-fbtns bulunamadı"); return
    cipler = re.findall(
        r'<button type="button" class="cz-fbtn" data-f="([^"]+)" style="--ic:([^;]+);"[^>]*>'
        r'<i class="ti ([^"]+)"></i>([^<]+)<span>(\d+)</span></button>',
        ciddi.group(2))
    if len(cipler) < 5:
        print(f"çip ayrıştırılamadı (bulunan: {len(cipler)})"); return
    rapor.append(f"{len(cipler)} endüstri çipi okundu")

    # 2) <select> kur — ikon, renk ve sayac veri nitelikleri olarak tasinir
    o = ['<option value="all">Tüm endüstriler</option>']
    for deger, renk, ikon, ad, sayi in cipler:
        o.append('<option value="' + deger + '" data-icon="' + ikon +
                 '" data-color="' + renk + '" data-count="' + sayi + '">' +
                 ad.strip() + '</option>')
    yeni_blok = ('<select id="czFiltre" data-cbsel aria-label="Endüstriye göre süz" '
                 'style="min-width:250px;">' + "".join(o) + '</select>')
    t = t[:ciddi.start()] + yeni_blok + t[ciddi.end():]
    rapor.append("çipler açılır listeye dönüştürüldü")

    # 3) JS'i yeniden bagla
    for eski, yeni, ad in [(ESKI_JS, YENI_JS, "referans"),
                           (ESKI_BTN_GUNCELLE, YENI_BTN_GUNCELLE, "durum güncelleme"),
                           (ESKI_TIK, YENI_TIK, "olay bağlama")]:
        if eski not in t:
            print(f"JS parçası bulunamadı: {ad}"); return
        t = t.replace(eski, yeni, 1)
    rapor.append("filtre JS'i listeye bağlandı (apply/hash mantığı korundu)")

    if not DRY:
        io.open(SAYFA, "w", encoding="utf-8", newline="").write(t)
    for r in rapor:
        print("  " + r)
    print("\ntamam" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
