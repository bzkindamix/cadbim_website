"""
Blog sayfasındaki çok butonlu filtreyi iki açılır listeye indirir.

Gerekçe (Onur, 2026-08-05): "bloglar sayfasındaki gibi çok butonlu filtre
istemiyorum. 2 roller buton kategori ve ürün" + "arama alanının yanına
yerleştir hemen".

Önce: 8 kategori çipi + 38 ürün çipi = 46 buton, iki ayrı blok hâlinde
sayfanın üstünü kaplıyordu. Sonra: arama kutusunun yanında "Kategori" ve
"Ürün" açılır listeleri.

Seçenekler mevcut çiplerden üretilir — liste editoryal olarak seçilmiş
(blog-posts.json'daki tüm ürünler değil), bu yüzden veriden yeniden
türetmek yerine korunur.

Kullanim: python scripts/blog_filtre_dropdown.py [--dry-run]
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SAYFA = os.path.join(ROOT, "cadbim_blog.html")

STIL = """
    /* Blog filtresi: 46 çip yerine iki açılır liste (DK-2026-08-05-86) */
    .bsel{appearance:none;-webkit-appearance:none;flex:0 1 auto;min-width:150px;
      padding:10px 32px 10px 13px;border-radius:var(--r);background-color:var(--navy3);
      border:.5px solid var(--w10);color:var(--w);font-size:13px;font-family:var(--fb);
      cursor:pointer;line-height:1.2;
      background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2300c8f0' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
      background-repeat:no-repeat;background-position:right 10px center;background-size:15px;}
    .bsel:focus{outline:none;border-color:rgba(0,200,240,.55);}
    .bsel.on{border-color:rgba(0,200,240,.5);background-color:rgba(0,200,240,.12);color:var(--cyan);}
    .bsel option{background:#0d1830;color:#fff;}
    @media(max-width:600px){.bsel{flex:1 1 100%;min-width:0;}}
"""

ESKI_JS_CAT = """  [].slice.call(document.querySelectorAll('#catfilter .fchip')).forEach(function(chip){
    chip.addEventListener('click',function(){
      var temizle=chip.classList.contains('active');
      document.querySelectorAll('#catfilter .fchip').forEach(function(c){c.classList.remove('active');});
      if(!temizle) chip.classList.add('active');
      activeCat=temizle?'all':chip.getAttribute('data-f');
      render(true);
    });
  });
  [].slice.call(document.querySelectorAll('#prodfilter .fchip')).forEach(function(chip){
    chip.addEventListener('click',function(){
      var temizle=chip.classList.contains('active');
      document.querySelectorAll('#prodfilter .fchip').forEach(function(c){c.classList.remove('active');});
      if(!temizle) chip.classList.add('active');
      activeProd=temizle?'all':chip.getAttribute('data-p');
      render(true);
    });
  });
"""

YENI_JS = """  var catSel=document.getElementById('bcat'), prodSel=document.getElementById('bprod');
  function isaretle(sel){ sel.classList.toggle('on', sel.value!=='all'); }
  catSel.addEventListener('change',function(){ activeCat=catSel.value; isaretle(catSel); render(true); });
  prodSel.addEventListener('change',function(){ activeProd=prodSel.value; isaretle(prodSel); render(true); });
"""

ESKI_TOPIC = """    if(topicParam){
      activeProd=topicParam;
      var topicChip=null;
      [].slice.call(document.querySelectorAll('#catfilter .fchip, #prodfilter .fchip')).forEach(function(c){
        if(!topicChip && (c.getAttribute('data-f')===topicParam || c.getAttribute('data-p')===topicParam)) topicChip=c;
      });
      if(topicChip){
        document.querySelectorAll('#catfilter .fchip, #prodfilter .fchip').forEach(function(c){c.classList.remove('active');});
        topicChip.classList.add('active');
      }
    }
"""

YENI_TOPIC = """    if(topicParam){
      /* ?topic= hem kategori hem urun listesinde aranir; hangisinde varsa o secilir */
      activeProd=topicParam;
      var vars=function(sel,v){return [].slice.call(sel.options).some(function(o){return o.value===v;});};
      if(vars(catSel,topicParam)){ catSel.value=topicParam; activeCat=topicParam; activeProd='all'; isaretle(catSel); }
      else if(vars(prodSel,topicParam)){ prodSel.value=topicParam; isaretle(prodSel); }
    }
"""


def main():
    t = io.open(SAYFA, encoding="utf-8").read()
    rapor = []

    # 1) Cip listelerini topla
    kat = re.findall(r'<button class="fchip" data-f="([^"]+)">([^<]+)</button>', t)
    urun = re.findall(r'<button class="fchip prod-chip" data-p="([^"]+)">([^<]+)</button>', t)
    if not kat or not urun:
        print("çip listeleri bulunamadı"); return
    rapor.append(f"{len(kat)} kategori + {len(urun)} ürün çipi okundu")

    def opts(ciftler, bos):
        s = '<option value="all">' + bos + '</option>'
        for deger, etiket in ciftler:
            s += '<option value="' + deger + '">' + etiket + '</option>'
        return s

    # 2) Iki filtre blogunu kaldir
    yeni, n = re.subn(
        r'\s*<div class="filter-block">\s*<div class="filter-label">[^<]*</div>\s*'
        r'<div class="pfilter" id="(?:catfilter|prodfilter)">.*?</div>\s*</div>',
        '', t, flags=re.S)
    if n != 2:
        print(f"filtre blokları kaldırılamadı (bulunan: {n})"); return
    t = yeni
    rapor.append("2 filtre bloğu kaldırıldı")

    # 3) Arama satirina iki listeyi ekle
    eski_satir = ('    <div id="bcount" style="font-size:12px;color:var(--w30);"></div>')
    yeni_satir = (
        '    <select id="bcat" class="bsel" aria-label="Kategoriye göre süz">'
        + opts(kat, 'Kategori') + '</select>\n'
        '    <select id="bprod" class="bsel" aria-label="Ürüne göre süz">'
        + opts(urun, 'Ürün') + '</select>\n'
        '    <div id="bcount" style="font-size:12px;color:var(--w30);margin-left:auto;"></div>')
    if eski_satir not in t:
        print("arama satırı bulunamadı"); return
    t = t.replace(eski_satir, yeni_satir, 1)
    # satirin justify'ini kaldir ki ogeler yan yana aksin
    t = t.replace(
        '<div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:8px;">',
        '<div style="display:flex;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:18px;">', 1)
    rapor.append("iki açılır liste arama kutusunun yanına eklendi")

    # 4) JS'i yeniden bagla
    if ESKI_JS_CAT not in t:
        print("çip JS'i bulunamadı"); return
    t = t.replace(ESKI_JS_CAT, YENI_JS, 1)
    if ESKI_TOPIC not in t:
        print("topic bloğu bulunamadı"); return
    t = t.replace(ESKI_TOPIC, YENI_TOPIC, 1)
    rapor.append("JS açılır listelere bağlandı (?topic= derin bağlantısı dahil)")

    # 5) Stil
    t = t.replace('</style>', STIL + '  </style>', 1)
    rapor.append("stil eklendi")

    if not DRY:
        io.open(SAYFA, "w", encoding="utf-8", newline="").write(t)

    for r in rapor:
        print("  " + r)
    print("\ntamam" + ("  (DRY-RUN)" if DRY else ""))


if __name__ == "__main__":
    main()
