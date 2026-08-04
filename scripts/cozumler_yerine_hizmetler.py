"""
Anasayfada Çözümler bölümünü kaldırıp yerine Hizmetler bölümü koyar.

Gerekçe (Onur, 2026-08-05): Sektörler bölümü zaten bir sektör seçicisi;
hemen altındaki Çözümler de 10 sektör sekmesiyle başlayınca arka arkaya iki
seçici çıkıyor ve kalabalık duruyordu. Çözüm sayfaları menüde (Çözümler
açılırında tek tek), hero düğmesinde ve alt bilgide durduğu için anasayfadan
kaldırılmaları erişimi kesmiyor.

Yerine, Hizmetler menüsündeki beş hizmet kart olarak eklenir. Metinler
hizmet sayfalarının kendi meta açıklamalarından alındı (uydurulmadı).

Kullanim: python scripts/cozumler_yerine_hizmetler.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
SAYFA = os.path.join(ROOT, "index.html")

YENI_BOLUM = '''<!-- HİZMETLER -->
<section class="section section-alt" id="hizmetler" style="padding-top:48px;padding-bottom:48px;">
  <div class="section-head reveal">
    <div class="slabel">Hizmetler</div>
    <div class="stitle" role="heading" aria-level="2">Yazılımın Ötesinde, Uçtan Uca Destek</div>
    <p class="ssub">Lisansı teslim edip çekilmiyoruz; kurulumdan eğitime, özel geliştirmeden teknik servise kadar sürecin yanındayız.</p>
  </div>
  <div class="srvgrid reveal">
    <a href="danismanlik" class="srvcard">
      <span class="srv-ic"><i class="ti ti-bulb" aria-hidden="true"></i></span>
      <h3>Danışmanlık</h3>
      <p>BIM içerik üretimi, CAD-ERP entegrasyonu, PLM/PDM projeleri ve CFD/FEA analiz hizmetleri.</p>
      <i class="ti ti-arrow-right srv-ok" aria-hidden="true"></i>
    </a>
    <a href="egitimler" class="srvcard">
      <span class="srv-ic"><i class="ti ti-school" aria-hidden="true"></i></span>
      <h3>Eğitimler &amp; Sertifikasyon</h3>
      <p>Autodesk Yetkili Eğitim Merkezi (ATC): kişiye ve kuruma özel Autodesk eğitimleri, sertifikasyon hazırlığı.</p>
      <i class="ti ti-arrow-right srv-ok" aria-hidden="true"></i>
    </a>
    <a href="yazilim-gelistirme" class="srvcard">
      <span class="srv-ic"><i class="ti ti-code" aria-hidden="true"></i></span>
      <h3>Yazılım Geliştirme</h3>
      <p>Autodesk API, iLogic, AutoLISP ve APS ile özel geliştirme; CAD-ERP entegrasyonları.</p>
      <i class="ti ti-arrow-right srv-ok" aria-hidden="true"></i>
    </a>
    <a href="designjet-teknik-servis" class="srvcard">
      <span class="srv-ic"><i class="ti ti-printer" aria-hidden="true"></i></span>
      <h3>HP Plotter Teknik Servis</h3>
      <p>HP DesignJet plotterlar için arıza ve onarım, periyodik bakım, kurulum, sarf malzeme değişimi.</p>
      <i class="ti ti-arrow-right srv-ok" aria-hidden="true"></i>
    </a>
    <a href="iletisim#form" class="srvcard">
      <span class="srv-ic"><i class="ti ti-headset" aria-hidden="true"></i></span>
      <h3>Teknik Destek</h3>
      <p>Lisans, kurulum ve kullanım sorularınız için Cadbim ekibinden doğrudan destek.</p>
      <i class="ti ti-arrow-right srv-ok" aria-hidden="true"></i>
    </a>
  </div>
</section>
'''

YENI_CSS = '''
/* ==== HİZMETLER KARTLARI (DK-2026-08-05-80) ====
   Çözümler bölümünün yerine geldi. Üstteki sektör ızgarası dokuz ayrı renk
   taşıdığı için burada tek vurgu rengi (cyan) kullanılır — hiyerarşi korunur. */
.srvgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:12px;
  max-width:1180px;margin:0 auto;}
.srvcard{position:relative;display:flex;flex-direction:column;align-items:flex-start;
  padding:20px 18px 44px;border-radius:var(--rl);background:var(--srf);
  border:1px solid var(--w06);text-decoration:none;
  transition:border-color .2s,background .2s,transform .2s;}
.srvcard:hover{border-color:var(--cyan-border);background:rgba(0,200,240,.06);transform:translateY(-3px);}
.srv-ic{display:flex;align-items:center;justify-content:center;width:38px;height:38px;
  border-radius:11px;margin-bottom:13px;color:var(--cyan);background:var(--cyan-dim);
  transition:box-shadow .2s;}
.srv-ic i{font-size:20px;}
.srvcard:hover .srv-ic{box-shadow:0 0 0 1px var(--cyan-border) inset;}
.srvcard h3{font-family:var(--font-d);font-size:15px;font-weight:700;color:var(--white);
  margin:0 0 7px;line-height:1.3;}
.srvcard p{font-size:12.5px;color:var(--w50);line-height:1.6;margin:0;}
.srv-ok{position:absolute;left:18px;bottom:17px;color:var(--cyan);font-size:15px;
  opacity:0;transform:translateX(-4px);transition:opacity .2s,transform .2s;}
.srvcard:hover .srv-ok{opacity:1;transform:translateX(0);}
'''

MOBIL_CSS = '''  /* Hizmetler: mobilde 2 sütun; beşinci kart tek başına kalmasın diye
     satırın tamamını kaplar. */
  .srvgrid{grid-template-columns:1fr 1fr;gap:9px;}
  .srvcard{padding:15px 13px 15px;border-radius:14px;}
  .srvcard h3{font-size:12.5px;}
  .srvcard p{font-size:10.5px;line-height:1.5;}
  .srv-ic{width:32px;height:32px;border-radius:9px;margin-bottom:10px;}
  .srv-ic i{font-size:17px;}
  .srv-ok{display:none;}                     /* dar kartta ok gereksiz */
  .srvgrid>.srvcard:last-child{grid-column:1/-1;}
'''


def main():
    with open(SAYFA, encoding="utf-8") as f:
        txt = f.read()
    orig = txt
    rapor = []

    # 1) Çözümler bölümünü yeni Hizmetler bölümüyle değiştir
    pat = re.compile(
        r'<!-- ÇÖZÜMLER -->\s*<section class="section section-alt" id="cozumler".*?</section>\n',
        re.S)
    txt, n = pat.subn(YENI_BOLUM, txt, count=1)
    rapor.append(("bölüm değişimi", n))

    # 2) Kullanılmayan Çözümler CSS'ini temizle
    for ad, kalip in [
        ("soltabs CSS", r'\.soltabs\{[^\n]*\n(?:\.soltab[^\n]*\n|\.solchip[^\n]*\n|@media\(max-width:(?:1024|900)px\)\{\.soltabs[^\n]*\n)*'),
        # sekme ikonlarının masaüstünde gizlenmesi (artık sekme yok)
        ("sekme ikon kuralı", r'\.soltab-btn>i\{display:none;\}\n'),
        # mobil sekme blogu (bu oturumda eklenmişti)
        ("mobil sekme CSS",
         r'  /\* ÇÖZÜMLER — sekmeler mobilde.*?\.soltabs\.reveal\.in \.soltabs-nav \.soltab-btn:active[^\n]*\n\n'),
    ]:
        txt, k = re.subn(kalip, '', txt, flags=re.S)
        rapor.append((ad, k))

    # 3) Yeni CSS'i .soltabs-all kuralının bulunduğu yere (kaldırılan blok
    #    sonrasına) değil, atolye şeridi yorumundan hemen önce ekle
    ank = '/* ==== SANATSAL BASKI ATÖLYE ŞERİDİ'
    if '.srvgrid{' not in txt and ank in txt:
        txt = txt.replace(ank, YENI_CSS.strip() + '\n\n' + ank, 1)
        rapor.append(("masaüstü CSS", 1))

    # 4) Mobil kuralları 600px bloğuna ekle
    mank = '  .section{padding:56px 1.5rem;}'
    if '.srvgrid{grid-template-columns:1fr 1fr' not in txt and mank in txt:
        txt = txt.replace(mank, MOBIL_CSS + mank, 1)
        rapor.append(("mobil CSS", 1))

    if txt != orig and not DRY:
        with open(SAYFA, "w", encoding="utf-8", newline="") as f:
            f.write(txt)

    for ad, n in rapor:
        print(f"  {ad:<18}{n}")
    print("  (DRY-RUN)" if DRY else "  yazıldı")


if __name__ == "__main__":
    main()
