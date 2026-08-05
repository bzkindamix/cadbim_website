# Copy-Editing & CRO Denetimi — Tüm Ürün/Sektör/Çözüm Sayfaları

**Tarih:** 2026-08-05
**Kapsam:** 191 kök HTML sayfası (203 - 11 KVKK/hukuki sayfası - 1 sitemap yardımcı). Blog (1.126 yazı) bu denetimin kapsamı dışında — [docs/CONTENT-STRATEGY.md](CONTENT-STRATEGY.md) §4'te ayrı ele alınıyor.
**Yöntem:** docs/CONTENT-STRATEGY.md temel alınarak 8 grup halinde (direk/kategori bazlı) incelendi. **Hiçbir dosya değiştirilmedi — bu salt bulgu raporu.**
**Değerlendirme açıları:** her sayfa hem copy-editing (netlik, tutarlılık, marka/ton kuralı ihlalleri) hem CRO (hero netliği, güven sinyalleri, CTA tutarlılığı, §6a çapraz-link kalitesi) perspektifinden okundu.

---

## Yönetici Özeti — Öncelik Sırasına Göre 12 Bulgu

### 🔴 Yüksek öncelik — marka kuralı ihlali / faktüel hata

1. **cadbim_yaratici_icerik.html — Autodesk-dışı eğitim iddiası, kendi içinde çelişkili.** Sayfa 4 yerde "Adobe uygulamaları için eğitim sunmuyoruz" derken, bir özellik kartında "Eğitim: Photoshop, Illustrator, InDesign, Premiere Pro ve After Effects eğitimleri" ve SSS'de "Eğitim ve baskı desteği de veriyor musunuz? Evet…" yazıyor. Doğrudan [[cadbim-egitim-sadece-autodesk]] ihlali, üstelik aynı sayfada kendiyle çelişiyor.
2. **cadbim_gorsellestirme.html — JSON-LD FAQPage 13 kez tekrarlanmış VE tekrarlar birbiriyle çelişiyor.** Bazı kopyalar "V-Ray/Corona/Lumion için eğitim vermiyoruz" derken sonraki kopyalar "Evet… eğitimleri verilir" diyor. Hem teknik hata hem doğrudan marka kuralı ihlali; arama motoruna çelişkili yapılandırılmış veri gidiyor.
3. **cadbim_hp_zbook_ultra_14_g1a.html — yanlış ürün adı.** Meta description/og/twitter/JSON-LD'de 4 kez "HP Zbook Fury G8" geçiyor; gerçek ürün Zbook Ultra 14 G1a (AMD Ryzen AI MAX). Kopyala-yapıştır kaynaklı, arama sonucunda ve sosyal paylaşımda yanlış ürün adı görünüyor.
4. **cadbim_hp.html — HP servis kapsamı title/meta/hero seviyesinde yanıltıcı.** Başlık ve hero "yetkili teknik servis"i Z serisi + ZBook + plotter'ı kapsıyormuş gibi genelliyor; gövdede (satır ~445) servisin SADECE DesignJet'e özgü olduğu belirtiliyor ama üst düzey mesaj düzeltilmemiş. [[cadbim-marka-statuleri]] kuralına (HP servis sadece DesignJet) aykırı algı riski.
5. **JSON-LD FAQPage bloğu ~13-14 kez tekrarlanan diğer sayfalar (teknik/SEO hatası, ayrı ayrı doğrulandı):** cadbim_bim.html, cadbim_bim_icerik_uretimi.html, cadbim_gerceklik_yakalama.html, cadbim_dijital_ikiz.html, cadbim_insaat_yonetimi.html, cadbim_dijital_donusum.html, cadbim_ai_gorsellestirme.html. Muhtemelen aynı "çözüm" şablonundaki bir üretim/script hatası — tek bir kaynak düzeltmesi tüm bu sayfaları çözebilir.

### 🟠 Orta-yüksek öncelik — sistemik tutarsızlık

6. **CTA metni site genelinde iki farklı yerde iki farklı kural izliyor:** Üst navigasyondaki buton her sayfada **"Teklif Al"**, gövde/footer CTA'ları ise çoğunlukla **"Teklif İste"** — aynı `teklif-iste` hedefine gidiyor ama metin tutarsız (191 sayfanın tamamında). Ayrıca **17+ ürün sayfası** ("Teklif İste" hiç yok, sadece "Uzmanımıza Sorun"/"İletişime Geç"/"Ücretsiz Deneme Talebi" kullanıyor): cadbim_cam, nesting, tolerans_analizi, factory_design, fabrika_tasarimi, eklemeli_imalat, netfabb, featurecam, powermill, powershape, pdm, plm, tasarim_otomasyonu, design_review, desktop_connector, dwg_trueview, gorsellestirme, ai_gorsellestirme, simulasyon. Tek bir CTA-şablon düzeltmesi bu grubun tamamını çözebilir.
7. **HP workstation ailesinde yoğun meta description tekrarı (kanibalizasyon riski):** Z1/Z2/Z2m G1i, Z6 G5/Z6 G5 A (farklı mimari olmasına rağmen), Z8 G5/Z8 G5 Fury, ZBook 8 G1i/G2i (14"/16" hepsi), ZBook Power zX G1i/G2i — 21 sayfadan **12'si** komşusuyla neredeyse birebir aynı meta cümlesini paylaşıyor. 21 sayfalık grup içinde en yoğun duplicate-content kümesi burası.
8. **§6a Sanatsal Baskı kararı fiilen uygulanmamış:** 23 DesignJet sayfasının **0'ında** gövde/hero içinde doğal bir cümleyle Sanatsal Baskı'ya değinilmiyor; sadece 4'ünde bir "ilgili çözüm" kartı var (z9pro/z9ps gibi en yüksek örtüşen sayfalarda bile yok). 2026-08-05'te onaylanan strateji kararı ile sahadaki durum arasında doğrudan boşluk.
9. **Hub/ürün sayfası içerik çakışması (SEO'da kendi kendine rekabet):** cadbim_pdm.html ↔ cadbim_vault_pdm.html, cadbim_plm.html ↔ cadbim_fusion_manage.html, cadbim_factory_design.html ↔ cadbim_fabrika_tasarimi.html — üç çift sayfa neredeyse aynı meta description ve konuyu paylaşıyor, hangisinin "hub" hangisinin "ürün sayfası" olduğu net değil.
10. **Footer adres eksikliği sistemik — cadbim_iletisim.html dahil.** Denetlenen 191 sayfanın büyük çoğunluğunda footer sadece "İzmir Merkez Ofis / Ankara Temsilcilik" etiketi gösteriyor, açık adres yalnız JSON-LD şemasında var. En kritik olması gereken **cadbim_iletisim.html'in kendi footer'ında da** aynı eksiklik var (sayfa gövdesinde tam adres var, footer'da yok) — SITE-DENETIM-RAPORU-2026-08-02.md'deki 189-sayfalık bilinen sorunla birebir örtüşüyor, hâlâ kapanmamış.

### 🟡 Orta öncelik — içerik/CRO iyileştirme fırsatı

11. **cadbim_basari_oykuleri.html — kısmi ilerleme:** Önceki denetimde "logosuz" tespit edilmişti, artık **19/19 öyküde logo var** (düzelmiş). Ama "metriksiz" sorunu büyük ölçüde duruyor: sadece **5/19** somut sayısal metrik içeriyor (ör. Norm Additive 3→1 hafta, BMC günler→1 gün), 14'ü hâlâ niteliksel ("kısaldı", "arttı"). [[cadbim-icerik-stratejisi]] §6'da işaretlenen en yüksek paylaşılabilirlik fırsatı hâlâ yarım kalmış.
12. **Jenerik/kopyalanmış çapraz-linkler:** Meshmixer ve Tinkercad'in çapraz-link seti Alias ile birebir aynı (simülasyon/CAM/PDM/otomotiv) — ikisi de maker/eğitim odaklı ürünler için tamamen alakasız. Autodesk M&E ürünlerinde (Arnold, Golaem, Mudbox, MotionBuilder, Flame, Flow Studio) 3 linkli jenerik bir set tekrarlanıyor, doğal iş akışı ortakları (Golaem→Maya, Arnold→Maya/3ds Max) linklenmemiş. Ayrıca 5 hub sayfasında (chaos, lumion, ultimaker, sketchup, microsoft) breadcrumb'daki "Ürünler" linki yanlışlıkla `href="autodesk"`'e gidiyor — bu Autodesk-dışı ürünleri örtük olarak Autodesk'e bağlıyor, marka hiyerarşisi açısından kafa karıştırıcı.

### Diğer tekil bulgular
- **Ton kuralı ihlali** ("seçin/aşağıdan seçin" arayüz talimatı): cadbim_cozumler.html, cadbim_endustriler.html, cadbim_urunler.html — muhtemelen paylaşılan bir filtre komponentinden geliyor.
- **Marka sırası ihlali** ("birlikte tercih edilen" bloklarında Autodesk>Adobe>HP sırası bozulmuş): cadbim_adobe.html (HP, Autodesk'ten önce), cadbim_hp_z_workstation.html (Autodesk listenin sonunda).
- **cadbim_designjet_z6ps.html:** aynı sayfada iki bitişik bölüm ("Adobe PDF Print Engine", "HP Pixel Control") neredeyse birebir tekrar ediyor — sayfa-içi redundancy.
- **cadbim_dwg_trueview.html:** ücretsiz bir ürün için "Abonelik Planları" CTA'sı ve "Lisanslama & Abonelik" dili var — ürünün kendisiyle çelişiyor.
- **cadbim_hakkimizda.html:** Ankara/temsilcilik cümlesi ATC eğitim cümlesiyle aynı paragrafta — yanlış okunursa Ankara'da sınıf eğitimi iması taşıyabilir (düşük risk, netleştirilebilir).

---

## Olumlu Bulgular (korunması gereken örüntüler)

- **Fiyat/₺/TL gerçek rakamı, "Ümit Kılıç" ismi, Ankara'da açık sınıf-eğitimi iması hiçbir sayfada bulunmadı** — bu üç kritik guardrail site genelinde temiz.
- HP DesignJet grubu (24 sayfa) ve Adobe grubu (17 sayfa) copy-editing açısından en temiz iki grup; meta title/description'lar model/ürüne özel yazılmış, jenerik şablon riski düşük.
- cadbim_urunler.html'de marka sırası (Autodesk>Adobe>HP>Chaos>UltiMaker>SketchUp>Lumion>Microsoft) talimatla birebir örtüşüyor — yeni sayfalarda referans alınabilir.
- UltiMaker S3/S5/S7/S8 karşılaştırma kartları modele özel yazılmış, kopyala-yapıştır değil — iyi örnek.
- cadbim_teklif_iste.html formu sade (4 zorunlu alan), düşük sürtünme — iyi CRO pratiği, dokunulmamalı.
- Autodesk-dışı ürünlerde "eğitim veriyoruz" iddiası genel olarak **iyi yönetilmiş** — 3 istisna (yukarıda #1, #2, ve sketch_sprint'teki belirsiz ifade) dışında 188 sayfa temiz.

---

## Grup Bazlı Tam Bulgular (191 dosya, sırayla)

### Grup 1 — BIM & İnşaat Direği (24 dosya, Autodesk AEC)
cadbim_aec_collection, cadbim_autodesk, cadbim_autodesk_docs, cadbim_autodesk_drive, cadbim_autodesk_forma, cadbim_bim, cadbim_bim_collaborate_pro, cadbim_bim_icerik_uretimi, cadbim_civil3d, cadbim_construction_cloud, cadbim_design_review, cadbim_desktop_connector, cadbim_dwg_trueview, cadbim_forma, cadbim_infraworks, cadbim_navisworks, cadbim_revit, cadbim_revit_lt, cadbim_robot_structural, cadbim_advance_steel, cadbim_tandem, cadbim_gerceklik_yakalama, cadbim_dijital_ikiz, cadbim_insaat_yonetimi

En önemli bulgular: cadbim_bim.html ve cadbim_bim_icerik_uretimi.html, cadbim_gerceklik_yakalama.html, cadbim_dijital_ikiz.html, cadbim_insaat_yonetimi.html'de FAQPage 13-14x tekrarı (yukarıda #5). cadbim_design_review.html ve cadbim_desktop_connector.html neredeyse birebir aynı gövde/CTA/çapraz-link seti paylaşıyor (şablon kopyalanmış). cadbim_revit.html'de atık boş `<section>` kalıntısı (satır 385-389) ve "Birlikte Çalıştığı Ürünler" linki eksik. cadbim_autodesk_drive.html ve cadbim_dwg_trueview.html'de "ücretsiz deneme/abonelik" CTA kafa karışıklığı. cadbim_autodesk.html'de marka sırası ihlali. Geri kalan 14 dosya (aec_collection, autodesk_docs, autodesk_forma, bim_collaborate_pro, civil3d, construction_cloud [redirect], forma, infraworks, navisworks, robot_structural, advance_steel, tandem) temiz.

### Grup 2 — Makine, Üretim & Ürün Tasarımı Direği (28 dosya)
cadbim_inventor, cadbim_fusion, cadbim_fusion_manage, cadbim_cam, cadbim_cfd, cadbim_moldflow, cadbim_nesting, cadbim_tolerans_analizi, cadbim_factory_design, cadbim_fabrika_tasarimi, cadbim_digital_factory, cadbim_eklemeli_imalat, cadbim_netfabb, cadbim_featurecam, cadbim_powermill, cadbim_powershape, cadbim_fabrication_cadmep, cadbim_fabrication_camduct, cadbim_fabrication_estmep, cadbim_me_collection, cadbim_pdm, cadbim_pdm_collection, cadbim_vault_pdm, cadbim_plm, cadbim_vehicle_tracking, cadbim_tasarim_otomasyonu, cadbim_method_xl, cadbim_factor4

**En sorunlu grup — 14/28 sayfada "Teklif İste" CTA'sı yok** (yukarıda #6'nın kaynağı): cam, nesting, tolerans_analizi, factory_design, fabrika_tasarimi, eklemeli_imalat, netfabb, featurecam, powermill, powershape, pdm, plm, tasarim_otomasyonu (+ design_review/desktop_connector Grup 1'de). Hub/ürün çakışması (yukarıda #9). Geri kalan 14 dosya (inventor, fusion, cfd, digital_factory, fabrication_cadmep/camduct/estmep, pdm_collection, vehicle_tracking, method_xl, factor4, me_collection, vault_pdm) CTA/copy açısından temiz.

### Grup 3 — Yaratıcı İçerik & Medya: AutoCAD ailesi + Autodesk M&E (21 dosya)
cadbim_autocad, cadbim_autocad_lt, cadbim_autocad_web, cadbim_3dsmax, cadbim_maya, cadbim_maya_creative, cadbim_alias, cadbim_arnold, cadbim_mudbox, cadbim_motionbuilder, cadbim_flame, cadbim_golaem, cadbim_flow_production_tracking, cadbim_flow_studio, cadbim_vred, cadbim_vantage, cadbim_yaratici_icerik, cadbim_recap_pro, cadbim_meshmixer, cadbim_tinkercad, cadbim_sketch_sprint

En önemli bulgu: cadbim_yaratici_icerik.html (yukarıda #1). Jenerik çapraz-link seti 3ds Max/Maya/Arnold/Mudbox/MotionBuilder/Flame/Golaem/Flow Studio'da tekrarlanıyor (yukarıda #12). Meshmixer/Tinkercad'in Alias ile birebir aynı alakasız çapraz-link seti. AutoCAD ailesi (autocad, autocad_lt, autocad_web) ve robot_structural/advance_steel/vred/recap_pro temiz ve iyi örnek.

### Grup 4 — Adobe (17 dosya)
cadbim_adobe, cadbim_creative_cloud, cadbim_photoshop, cadbim_illustrator, cadbim_indesign, cadbim_premiere_pro, cadbim_after_effects, cadbim_audition, cadbim_animate, cadbim_character_animator, cadbim_acrobat_pro, cadbim_adobe_express, cadbim_adobe_stock, cadbim_firefly, cadbim_lightroom, cadbim_fresco, cadbim_substance3d

**En temiz grup.** Eğitim iddiası ihlali bulunamadı (17/17 temiz — "eğitim" geçen yerler hep sektör/içerik-türü bağlamında, CADBİM'in Adobe eğitimi verdiği iddiası yok). Tek bulgu: cadbim_adobe.html'de marka sırası ihlali (yukarıda). cadbim_substance3d.html marka sırasına en uygun örnek (önce Autodesk, sonra Adobe).

### Grup 5 — HP Workstation (21 dosya)
cadbim_hp, cadbim_hp_build_workspace, cadbim_hp_monitor, cadbim_hp_z1_g1i, cadbim_hp_z2_g1i, cadbim_hp_z2m_g1i, cadbim_hp_z4_g5, cadbim_hp_z6_g5, cadbim_hp_z6_g5_a, cadbim_hp_z8_g5, cadbim_hp_z8_g5_fury, cadbim_hp_z_workstation, cadbim_hp_zbook, cadbim_hp_zbook_8_g1i_14, cadbim_hp_zbook_8_g1i_16, cadbim_hp_zbook_8_g2i_14, cadbim_hp_zbook_8_g2i_16, cadbim_hp_zbook_fury_16_18_g1i, cadbim_hp_zbook_power_zx_16_g1i, cadbim_hp_zbook_power_zx_16_g2i, cadbim_hp_zbook_ultra_14_g1a

En önemli bulgular: yanlış ürün adı (#3), HP servis kapsamı belirsizliği (#4), meta description tekrarı kümesi (#7), marka sırası ihlali (cadbim_hp_z_workstation.html). cadbim_hp_zbook_fury_16_18_g1i.html'de de nesil karışıklığı ("G8" ifadesi G1i modelinde). Temiz: hp_monitor, hp_z1_g1i, hp_z4_g5, hp_zbook (hub).

### Grup 6 — HP DesignJet + Sanatsal Baskı (24 dosya)
cadbim_designjet, cadbim_designjet_hd_pro, cadbim_designjet_sarf, cadbim_designjet_sd_pro, cadbim_designjet_smart_tank, cadbim_designjet_t1600(+_plus), cadbim_designjet_t1700, cadbim_designjet_t200, cadbim_designjet_t2600(+_plus), cadbim_designjet_t600, cadbim_designjet_t830, cadbim_designjet_t850, cadbim_designjet_t950, cadbim_designjet_teknik_servis, cadbim_designjet_xl3600, cadbim_designjet_xl3800, cadbim_designjet_z6810, cadbim_designjet_z6pro, cadbim_designjet_z6ps, cadbim_designjet_z9pro, cadbim_designjet_z9ps, cadbim_sanatsal_baski

**Genel olarak en temiz copy-editing grubu** (model-özel meta'lar, tekrar yok). Ana bulgu: §6a Sanatsal Baskı entegrasyonu fiilen yok (#8) — özellikle z9pro/z9ps/z6pro gibi en yüksek örtüşen sayfalarda bile eksik. cadbim_designjet_z6ps.html'de sayfa-içi tekrar. cadbim_sanatsal_baski.html'nin CTA dili ("Projenizi anlatın") diğer 23 sayfadan farklı — kasıtlı olabilir, onay gerektirir.

### Grup 7 — Görselleştirme, Dijital İkiz & Diğer Yazılımlar (31 dosya)
cadbim_chaos, cadbim_vray, cadbim_corona, cadbim_phoenix, cadbim_cosmos, cadbim_enscape, cadbim_veras, cadbim_lumion(+_cloud/_studio/_view), cadbim_ultimaker(+_malzeme/_s3/_s5/_s7/_s8), cadbim_cura, cadbim_sketchup(+5 varyant), cadbim_trimble_connect, cadbim_microsoft, cadbim_anima, cadbim_gorsellestirme, cadbim_ai_gorsellestirme, cadbim_simulasyon

En önemli bulgular: cadbim_gorsellestirme.html (#2), FAQPage tekrarı + eğitim çelişkisi cadbim_ai_gorsellestirme.html'de de var (teknik hata, ama eğitim metni burada tutarlı/doğru). 3 sayfada (gorsellestirme, ai_gorsellestirme, simulasyon) "Teklif İste" hiç yok. 5 hub sayfasında (chaos, lumion, ultimaker, sketchup, microsoft) breadcrumb "Ürünler"→Autodesk hatası (#12). SketchUp/Lumion/UltiMaker varyant aileleri (13 sayfa) beklenenin aksine özgün ve iyi yazılmış — jenerik tekrar riski düşük.

### Grup 8 — Çözümler Hub, Kurumsal, Sektörler (25 dosya — site omurgası)
cadbim_cozumler, cadbim_dijital_donusum, cadbim_endustriler, cadbim_urunler, cadbim_danismanlik, cadbim_yazilim_gelistirme, cadbim_egitimler, cadbim_webinar, cadbim_teklif_iste, cadbim_iletisim, cadbim_hakkimizda, cadbim_basari_oykuleri, cadbim_surdurulebilirlik, cadbim_blog, index.html, 404.html, sektor_egitim, sektor_havacilik, sektor_icmimarlik, sektor_insaat, sektor_makine, sektor_medya, sektor_mimari, sektor_otomotiv, sektor_tesisat

En önemli bulgular: cadbim_dijital_donusum.html'de FAQPage tekrarı, cadbim_iletisim.html'in kendi footer'ında adres eksikliği (#10), cadbim_basari_oykuleri.html metrik durumu (#11), "seçin" ton ihlali (cozumler/endustriler/urunler), nav CTA "Teklif Al" örüntüsü (25/25). 9 sektör sayfasının tamamı birbirinden yeterince farklılaşmış meta'lara sahip (jenerik tekrar riski düşük). cadbim_egitimler.html / cadbim_webinar.html ayrımı net ve doğru. cadbim_teklif_iste.html formu düşük sürtünmeli, iyi.

---

## Sonraki Adım Önerisi

Bu rapor sadece bulgu listesidir, hiçbir değişiklik yapılmadı. Önerilen işlem sırası (etki/efor oranına göre):
1. **Tek-şablon düzeltmeleri (yüksek etki, düşük efor):** JSON-LD FAQPage tekrarı (muhtemelen tek bir script/include hatası), nav CTA "Teklif Al"→"Teklif İste", breadcrumb "Ürünler"→autodesk hatası (5 sayfa).
2. **Marka kuralı ihlalleri (acil, düşük hacim):** cadbim_yaratici_icerik.html, cadbim_gorsellestirme.html, cadbim_hp_zbook_ultra_14_g1a.html, cadbim_hp.html — 4 dosya, yüksek risk.
3. **CTA tutarlılığı (17+ dosya, tek kalıp):** "Uzmanımıza Sorun/Ücretsiz Deneme"→"Teklif İste" standardizasyonu.
4. **HP workstation meta tekilleştirme** (12 dosya).
5. **Sanatsal Baskı §6a entegrasyonu** (4-5 en örtüşen DesignJet sayfası: z9pro, z9ps, z6pro, z6810).
6. **Başarı öyküleri metrik tamamlama** (14 kart).
