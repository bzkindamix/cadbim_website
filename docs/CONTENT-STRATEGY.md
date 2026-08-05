# CADBİM İçerik Stratejisi

**Tarih:** 2026-08-05
**Durum:** Taslak — onay bekliyor
**Sonraki adım:** Bu strateji onaylandıktan sonra copy-editing (mevcut sayfa metinlerinin düzenlenmesi) buna göre sıralanacak.

## 1. Hedef ve Kapsam

Birincil hedef: **teklif/lead üretimi + organik arama görünürlüğü.** Marka otoritesi üçüncül bir kazanım olarak kabul edilir, ayrı bir hedef olarak yönetilmez.

Kaynak durumu: İçerik üretimi AI destekli bir ekiple kurulacak (yazan/düzenleyen kişi sayısı sınırlı). Bu yüzden strateji **az sayıda yüksek etkili iş** üzerine kurulu; yeni içerik hacmi büyük ama gözetimsiz üretilmeyecek — her parça bir insan onayından geçecek.

## 2. Mevcut Durum Özeti (site taramasından)

- ~165 ürün/marka sayfası (`cadbim_*.html`), 9 sektör sayfası (`sektor_*.html`), 1 çözümler hub'ı + ~28 çözüm alt sayfası.
- Blog: 1.126 yazı, ama içeriğin büyük kısmı tek cümlelik video açıklaması (ör. "Bu Cadbim Teknik Destek videosunda X ele alınıyor"). 909'u video gömme, 119'u makale. 99 mükerrer Türkçe/ASCII kopya var.
- Ürün/sektör sayfalarının meta title/description'ları özenli ve tutarlı; blogun meta açıklamaları jenerik ve zayıf.
- **Teknik engel:** Temiz URL'ler sunucuda tanımlı değil (JS tabanlı 404-yönlendirme hilesiyle çalışıyor), 1.126 blog URL'si hiçbir yönlendirme haritasında yok. Bu, blog için yazacağımız yeni/iyileştirilmiş içeriğin arama motorlarınca düzgün indekslenmesini engelliyor. **İçerik stratejisi burada bir varsayım yapıyor: bu teknik sorun paralel bir işle (mevcut denetim raporunda zaten kayıtlı) çözülecek.** Çözülmeden yayınlanacak yeni blog içeriği trafiğe dönüşmeyebilir — bu riski görmezden gelmiyoruz, ama içerik planlamasını bloklamıyoruz.

## 3. İçerik Direkleri (Pillars)

Direkler ürün/marka hiyerarşisini yansıtır ([[cadbim-marka-urun-sirasi]]): Autodesk > Adobe > HP plotter > HP workstation > diğerleri. Her direk zaten var olan bir hub sayfasına (ürün/çözüm/sektör sayfası) bağlanır; yeni blog içeriği bu hub'ları besleyen "spoke" olarak yazılır — ayrı bir `/guides` URL yapısı kurulmaz, mevcut blog altında kalır.

1. **BIM & İnşaat/Altyapı (Autodesk)** — Revit, Navisworks, Civil3D, AEC Collection, BIM Collaborate Pro; hub: `cadbim_bim.html`, `sektor_insaat.html`
2. **Makine, Üretim & Ürün Tasarımı (Autodesk)** — Inventor, Fusion, Vault/PDM, CAM, Nesting, Tolerans Analizi; hub: `sektor_makine.html`, `cadbim_pdm.html`
3. **Yaratıcı İçerik & Medya (Adobe + Autodesk 3ds Max/Maya)** — Creative Cloud, Premiere Pro, 3ds Max, Maya; hub: `sektor_medya.html`, `cadbim_creative_cloud.html`
4. **Görselleştirme & Dijital İkiz (Chaos, Lumion, Ultimaker)** — VRay, Lumion, 3D baskı; hub: `cadbim_gorsellestirme.html` (varsa), `cadbim_ultimaker_*`
5. **Büyük Format Baskı (HP DesignJet)** — plotter serisi, sanatsal baskı; hub: `cadbim_sanatsal_baski.html`

Sektör sayfaları (Otomotiv, Havacılık, İç Mimarlık, Eğitim, Tesisat) direk değil, **çapraz-kesit** olarak ele alınır: her sektör sayfası yukarıdaki direklerden ilgili ürünleri harmanlar, kendi başına içerik üretim kaynağı değildir.

## 4. Blog: Seçici İyileştirme Planı

Karar: 1.126 yazının tamamına dokunulmayacak. **Öncelik sırası ile ~50-100 yazı seçilip derinleştirilecek**, geri kalanı olduğu gibi bırakılacak (mükerrer 99 çift ayrı bir teknik iş — denetim raporunda zaten kayıtlı, içerik stratejisinin kapsamı dışında).

**Seçim kriterleri (puanlama):**
- Kategori hacmi ve iş değeri: CAD (407) ve BİM (275) yazıları toplamın %60'ı — buradan direk başına 10-15 "bayrak" yazı seçilir
- Ürün sayfası eşleşmesi: Bir ürün sayfasına (`cadbim_*.html`) doğrudan bağlanabilen yazılar önceliklidir (blog → ürün sayfası → Teklif İste huni mantığı)
- Arama niyeti: "nedir", "nasıl kullanılır", "X vs Y", "hangi sürüm" kalıplarına uyan başlıklar (bkz. §5 alıcı aşaması eşlemesi)
- Format: Sadece video gömme olan yazılar, metne dönüştürülmeye en yakın olanlar önce seçilir (video zaten var, transkript+bağlam eklemek görece düşük efor)

**Seçilmeyen ~1.000 yazı için:** Dokunulmaz, silinmez. Kategori/etiket sayfaları üzerinden toplu erişim sağlanır (blog hub filtreleri zaten bunu yapıyor).

## 5. Alıcı Aşaması Eşlemesi (yeni ve iyileştirilecek içerik için)

| Aşama | Kalıp | Örnek |
|---|---|---|
| Farkındalık | "X nedir", "X'e giriş" | "BIM nedir, inşaat projelerinde ne işe yarar" |
| Değerlendirme | "X vs Y", "hangi ürün" | "Fusion mu Inventor mu: hangisi hangi iş için" |
| Karar | "teklif", "danışmanlık" (fiyat YOK — [[cadbim-fiyat-gosterilmez]]) | "Autodesk lisans danışmanlığı — teklif süreci nasıl işler" |
| Uygulama | "nasıl kurulur", "eğitim" (SADECE Autodesk — [[cadbim-egitim-sadece-autodesk]]) | "Revit'te ilk proje şablonu nasıl kurulur" |

## 6. Öncelikli Konu Örnekleri (aranabilir + paylaşılabilir)

Aranabilir (arama hacmi/niyet odaklı):
- "Revit ile Navisworks arasındaki fark" (Değerlendirme, BIM direği)
- "Inventor'da parametrik tasarım nasıl yapılır" (Uygulama, Üretim direği)
- "AutoCAD LT ile AutoCAD arasındaki fark" (Değerlendirme — sık sorulan bir soru, mevcut ürün sayfalarında zaten kısmen var)
- "HP DesignJet serisi karşılaştırma: hangi model hangi iş için" (Değerlendirme, Baskı direği)

Paylaşılabilir (özgün bakış açısı, veri):
- Müşteri başarı öykülerinin derinleştirilmesi — denetim raporunda "19 başarı öyküsü var ama logosuz/metriksiz" tespiti var; bu, en yüksek paylaşılabilirlik potansiyeline sahip mevcut malzeme. Somut proje/metrik eklenerek (müşteri onayıyla) vaka analizine dönüştürülebilir.
- "1993'ten bugüne" tarzı meta-içerik (kurum tarihi, sektördeki dönüşüm gözlemleri) — CADBİM'in 30+ yıllık konumunu kullanan tek yerde henüz yapılmamış bir açı.

## 7. Uygulanmayacak / Kapsam Dışı

- Fiyat/indirim içeren içerik üretilmez, her CTA "Teklif İste" olur.
- Autodesk dışı ürünler (Adobe, HP, Chaos, Ultimaker vb.) için "eğitim veriyoruz" iddiası taşıyan başlık/metin yazılmaz; webinar farklı bir şey olarak sunulur.
- Ankara ofisi için sınıf eğitimi ima eden içerik yazılmaz (sadece temsilcilik).
- 99 mükerrer blog çiftinin temizliği ve temiz-URL/indeksleme sorunu bu stratejinin kapsamında değil — ayrı teknik iş olarak mevcut denetim raporuna bırakılıyor, ancak yeni içerik yayına alınırken bu riskin hâlâ açık olduğu göz önünde tutulmalı.

## 8. Sonraki Adım

Bu belge onaylandıktan sonra copy-editing aşamasına şu sırayla geçilir:
1. §4'teki kriterlere göre seçilen ~50-100 blog yazısının listesi çıkarılır (Onur onayına sunulur).
2. Seçilen yazılar + ilgili ürün sayfaları copy-editing skill'i ile tek tek işlenir.
3. Yeni içerik (§6) mevcut sayfalar bittikten sonra planlanır.
