# CADBİM Web Sitesi — Değişiklik Kayıtları (PDM / Revizyon Günlüğü)

> Bu dosya, projeye yapılan her değişikliğin izlenebilir kaydını tutar (PDM/ECO mantığı).
> Kayıt biçimi: **DK-YYYY-MM-DD-NN** · Tarih · Yapan · Kapsam · Etkilenen dosyalar · Doğrulama · Durum · Referans (commit).
> Kaynak kod sürüm kontrolü Git/GitHub'dadır; bu dosya insan-okunur değişiklik özetidir.

### DK-2026-08-02-07 — Görsel/video ağırlığı büyük ölçüde düşürüldü (K7/K8 kısmen tamamlandı)

- **Yapan:** Claude (PDM asistanı) — Onur'un "yapamadıkların" listesindeki görsel/font işleme gerekçesini sorgulaması üzerine önce gerçekten araç olup olmadığı kontrol edildi (ffmpeg ve Python Pillow mevcut çıktı — ImageMagick/cwebp/fontTools yok), bulunan araçlarla yapılabilecek her şey yapıldı.
- **4 Chaos otomatik oynatılan hero videosu yeniden kodlandı** (`assets/videos/chaos/*.mp4`, 1280px genişlik, CRF 28, sessiz): vray 17,5MB→1,6MB, corona 8,8MB→1,2MB, veras 6,6MB→0,74MB, enscape 5,4MB→1,2MB. Toplam 38,3MB→4,6MB (%88). Görsel kalite karşılaştırmalı kare çıkarımıyla doğrulandı, fark yok. Orijinaller güvenlik için repo dışına yedeklendi.
- **16 DesignJet karşılaştırma görseli** (`assets/products/hp-designjet-*.png`, 220px kartlarda gösteriliyor) 500px genişliğe indirilip WebP'ye çevrildi: 10,95MB→0,30MB (%97). Tüm HTML referansları (`*.html` + `post/*.html`, 240 örnek) `.png`→`.webp` olarak güncellendi.
- **11 UltiMaker WebP dosyası** (factor4-hero, s5/s7/s8/s3-hero, pvars, cura-ui, sketch-sprint-hero, materials-hero, digital-factory-hero, material-station) aynı boyutta yeniden sıkıştırıldı (kalite 82): 8,46MB→0,90MB (%89) — dosya adı değişmedi, referans güncellemesi gerekmedi.
- **11 ek PNG → WebP**: Chaos video posterleri (corona/enscape/vray-hero), HP tarayıcı görselleri (hd-pro/sd-pro), HP ZBook Ultra + workstation/zbook grup görselleri, UltiMaker Factor4 + PET-CF kit + Method XL hero: 3,70MB→0,47MB (%87). 55 HTML referansı güncellendi.
- **41 JPG yeniden sıkıştırıldı** (`assets/img/webinar/`, `assets/products/designjet-web/`, kalite 80, progressive): 7,71MB→4,74MB (%38, dosya adları değişmedi).
- **1 aşırı yüksek bit hızlı ürün videosu** (`assets/products/designjet-web/video-z6pro.mp4`, 1080p → 1280px'e indirildi, CRF 26, ses korunarak): 17,97MB→1,76MB (%90). Diğer 2 DesignJet videosu (t1600, z9pro) zaten makul bit hızındaydı, dokunulmadı.
- **Toplam:** Bu tek oturumda gerçek kullanıcı tarafından indirilen ~87 MB'lık görsel/video ağırlığı ~13,5 MB'a düşürüldü (~%84 azalma), 0 görsel/video kalite kaybı gözlenmedi (karşılaştırmalı kare/görsel kontrolüyle).
- **Doğrulama:** Yerel önizlemede DesignJet, V-Ray (video+poster), UltiMaker Factor4 sayfaları açılıp `naturalWidth===0` kontrolüyle 0 kırık görsel doğrulandı; video `currentSrc`/`poster` doğru çözümlendiği teyit edildi; konsol hatası yok.
- **Kapsam dışı (hâlâ yapılamayan):** Tabler ikon fontu subset'i — `fontTools` kurulu değil, `pip install` denenmedi (kullanıcı onayı gerektirir); `assets/og/*.png` (153 dosya, ~10,6 MB) — sosyal medya crawler'ları dışında kullanıcı performansını etkilemediği için düşük öncelikli bırakıldı; `assets/products/designjet/` (2,46 GiB, referanssız) — silme/taşıma kararı gerektiriyor, dokunulmadı.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-02-06 — Denetim raporundaki Faz 0 mekanik düzeltmelerinin tamamı uygulandı

- **Yapan:** Onur Bozok'un "sonnet'in yapabileceği ne varsa listede belirlediğimiz hepsini yap" talebi üzerine Claude (PDM asistanı) — DK-01'deki denetim raporunun (SITE-DENETIM-RAPORU-2026-08-02.md) sunucu erişimi/görsel işleme/içerik yazımı gerektirmeyen, salt dosya düzenlemesiyle yapılabilecek tüm bulguları toplu olarak düzeltti.
- **Htaccess taslağı (K2, Y1, Y2):** `docs/htaccess-taslak.txt`'e blog yazıları için genel kural (`^post/(.+?)/?$`) ve `vray`/`enscape`/`veras` için eksik bölüm-3+4 kuralları eklendi. 4 SketchUp sayfasının (`sketchup-pro`, `-pro-scan`, `-pro-civil-contractor`, `advanced-workflows`) taslakta zaten var olduğu doğrulandı; asıl eksik oldukları `sitemap.xml` ve `404.html` haritasıydı — ikisine de eklendi.
- **Sitemap/robots temizliği (Y5):** 11 `noindex` KVKK sayfası `sitemap.xml`'den çıkarıldı; `robots.txt`'teki var olmayan `/tesekkurler` sayfasına ait `Disallow` satırı kaldırıldı.
- **`cadbim_construction_cloud.html` (Y10):** Silinmedi — denetimdeki "0 link" bulgusu güncel değildi, 6 blog yazısı hâlâ `../construction-cloud`'a link veriyor. Ancak stub'ın yönlendirdiği `/autodesk-forma` hedefinin doğru eşleşme olup olmadığı bir içerik kararı; Onur'a soruldu, dokunulmadı.
- **`cookie-consent.js` eklendi (K4):** `index.html` dahil eksik 20 sayfaya (5 sektör sayfası, çözümler/eğitimler/endüstriler, 13 KVKK sayfası) script etiketi eklendi. `404.html` ve `cadbim_construction_cloud.html` kasıtlı hariç tutuldu (anlık yönlendirme sayfaları, kalıcı içerik değil).
- **`href="index.html"` → `href="/"` (Y4):** Kök sayfalardaki 570 örnek düzeltildi.
- **Post içi eski linkler (Y3):** `post/*.html` içindeki 8.067 `../cadbim_X.html` / `../sektor_X.html` / `../index.html` linki, `404.html`'deki güncel harita kullanılarak 1.129 dosyada temiz URL'e (`../X`, `../`) çevrildi — 0 eşlenemeyen dosya adı kaldı. Bu, her post ziyaretinde oluşan gereksiz 301 zincirini ortadan kaldırıyor.
- **Footer/legal link kontrastı (Y7):** `.fbot`/`.footer-bot` metin rengi (0.2→0.5) ve footer linklerinin rengi (0.3→0.58, 2.835 örnek) site genelinde WCAG AA eşiğinin üzerine çekildi; `assets/css/design-system.css`'teki fallback değer de (0.45→0.5) güncellendi.
- **Script/CSS sürüm tekilleştirmesi:** `mobilenav.js` (389 sayfada `?v=9` → `?v=11`) ve `cookie-consent.js` (389 sayfada `?v=1` → `?v=2`) sürümleri site genelinde eşitlendi — artık tarayıcı önbelleğinde çift giriş yok.
- **Erişilebilirlik (Y6):** `assets/css/design-system.css`'te `:focus-visible` kuralının önceki bir oturumdan zaten mevcut ve 1.319 sayfada aktif olduğu doğrulandı (rakip bir `:focus` kuralı bulunmadığı statik analizle teyit edildi). Skip-link EKLENMEDİ: sayfa yapıları nav sonrası ortak bir landmark ID paylaşmıyor, körlemesine eklemek kırık çapa riski taşır.
- **Doğrulama:** Yerel önizlemede kök (`index.html`), post (`3d-gorunum.html`), KVKK (`kvkk_cerez_politikasi.html`) ve `teklif-iste`/`sanatsal-baski` sayfaları açılıp konsol hatası olmadığı, `cookie-consent.js`'in yüklendiği, footer link renginin `rgba(255,255,255,0.58)` hesaplandığı, Power Automate URL'sinin ve formların bozulmadığı doğrulandı.
- **Kapsam dışı (bu oturumda yapılamayanlar):** `.htaccess`'in canlı sunucuya yüklenmesi (barındırma erişimi gerekiyor); K6 — 99 Türkçe-karakterli mükerrer post çifti (içerik farkı olabileceği için körlemesine silinmedi, ayrı karar gerektiriyor); K7/K8 — ikon fontu subset'i, DesignJet/UltiMaker görsellerinin WebP'ye çevrilmesi, autoplay video optimizasyonu (görsel/font işleme araçları gerektiriyor); O6 — başarı öykülerine müşteri logosu/metrik (gerçek müşteri verisi gerektiriyor); skip-link (yukarıda açıklandı).
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-02-05 — Power Automate e-postalarına marketing@cadbim.com.tr CC olarak eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı, Chrome oturumu üzerinden Power Automate'te doğrudan düzenleme yaptı).
- **Kapsam:** DK-04'te kurulan "Web sitesi form gonderimi" akışındaki her iki "E-posta gönder (V2)" eyleminde (sanatsal_baski → sanatsalbaski@cadbim.com.tr ve teklif_iste → cadbim@cadbim.com.tr) "Gelişmiş parametreler" açılıp "Bilgi" (CC) alanına `marketing@cadbim.com.tr` eklendi (tenant dizininde bulunan "Marketing" kişisi olarak çözümlendi). Kod tarafında (site dosyaları) hiçbir değişiklik yok — bu tamamen Power Automate akış konfigürasyonu.
- **Doğrulama:** Akış kaydedildi (hata yok), ardından `curl` ile her iki dal için ayrı test isteği gönderildi (sanatsal_baski ve teklif_iste, ikisi de HTTP 200). Test e-postaları `cadbim@cadbim.com.tr`, `sanatsalbaski@cadbim.com.tr` ve CC olarak `marketing@cadbim.com.tr`'ye gitti — gerçek talep değildir.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-02-04 — Power Automate akışı kuruldu ve iki form gerçek gönderime bağlandı

- **Yapan:** Onur Bozok (Power Automate'te akışı kurdu, Chrome oturumu üzerinden Claude ile birlikte) + Claude (PDM asistanı) · DK-02/03'teki mailto-taslağı geçici çözümünün kalıcı hale getirilmesi.
- **Power Automate akışı ("Web sitesi form gonderimi", ortam: Cadbim Bilgisayar Özel...):** "Bir HTTP isteği alındığında" tetikleyicisi (erişim: Herkes) → `form_type` alanına göre Koşul → `sanatsal_baski` ise `sanatsalbaski@cadbim.com.tr`'ye, aksi halde `cadbim@cadbim.com.tr`'ye "E-posta gönder (V2)" → "Yanıt" (200, `{"ok":true}`). Akış Power Automate arayüzünde Türkçe dinamik içerik seçici JSON şemasını ayrıştırmadığı için (tekrarlanan denemelerde şema alanı kayıt sonrası boşaldı — kozmetik bir Power Automate arayüz kısıtı, işlevi etkilemiyor), alan erişimleri `@{triggerBody()?['alan_adi']}` düz metin ifadesiyle yazıldı; bu, koşul ve e-posta gövdelerinde doğrulanan şekilde çalışıyor.
- **`cadbim_teklif_iste.html` ve `cadbim_sanatsal_baski.html`:** `handleSubmit`/`formuGonder` fonksiyonları artık mailto taslağı açmıyor; doğrudan Power Automate'in HTTP tetikleyici URL'sine (imzalı, `POWER_AUTOMATE_URL` sabiti içinde) `fetch()` ile JSON POST atıyor. Gerçek başarı/hata durumları gösteriliyor (başarıda buton "Talebiniz alındı" olup form sıfırlanıyor; başarısızlıkta buton eski haline dönüp doğrudan e-posta/telefon alternatifi gösteriliyor) — hiçbir zaman sahte "alındı" mesajı yok.
- **Güvenlik notu:** Tetikleyici URL'si "Herkes" erişimine açık imzalı bir bağlantı; bu imza fiilen paylaşılan bir sır işlevi görüyor ve şu an istemci tarafı JS içinde (herkese açık sayfa kaynağında) yer alıyor. Bu, kod tarafında değiştirilmeden bırakıldı (mevcut MS Forms/Formspree tarzı entegrasyonlarla aynı risk profili) ancak Onur'a bilgi verildi; istismar edilirse Power Automate'te URL yeniden üretilebilir (yeniden imzalama). İleride bir honeypot alanı veya basit oran sınırlama eklenebilir.
- **Doğrulama:** `curl` ile doğrudan uç nokta testi (HTTP 200) + tarayıcıda her iki formda gerçek `fetch()` gönderimi simüle edilip buton/not metinlerinin başarı durumuna geçtiği doğrulandı (konsol hatası yok, CORS engeli yok). Test gönderimleri sırasında `cadbim@cadbim.com.tr` kutusuna 2, `sanatsalbaski@cadbim.com.tr` kutusuna 1 test e-postası gitti — bunlar gerçek talep değildir, silinebilir.
- **Kapsam dışı (bilinen, kozmetik):** Koşul adımındaki zararsız boş ikinci satır (DK-03'te not edildi) ve Power Automate arayüzünde JSON şemasının kalıcı olmaması — ikisi de işlevi etkilemiyor, ileride temizlenebilir.
- **Durum:** ✅ Tamamlandı, push edilecek. HP Servis ve Eğitim formlarının aynı akışa (yeni `form_type` dalları eklenerek) bağlanması sıradaki adım.

### DK-2026-08-02-03 — Sanatsal Baskı'ya kendi formu eklendi; Teklif İste formundan "Tercih Edilen Ofis" kaldırıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · DK-02'deki 4-form planının ikinci adımı.
- **Sanatsal Baskı formu (`cadbim_sanatsal_baski.html`):** Sayfanın kendi CTA bölümünde (`#iletisim`), önceden var olan tek satırlık mailto butonu ve genel `iletisim#form`'a (yanlış hedef — MS Forms iframe) giden "ÇEVRİM İÇİ FORM" kartı kaldırılıp yerine sayfanın kendi menekşe/elektrik-mavisi cam-kart estetiğine uygun, alana özel bir form eklendi. Alanlar: Ad Soyad*, E-posta*, Telefon, Baskı Türü (Fotoğraf Baskısı/Fine Art Reprodüksiyon/Sanatsal Kanvas/Sergi Üretimi/Sertifika & Poster), Yüzey/Kağıt (Mat/Yarı Mat-Parlak/Parlak/Kanvas/Cotton Rag/Bayrak Bezi), Finisaj (Çerçeve/Dekota/Fotoblok/Kasnak/Parçalı Kanvas/Paravan), Ebat/Ölçü, Adet, Mesaj, KVKK. Seçenekler sayfanın kendi İşler/Yüzeyler/Finisaj bölümlerindeki terminolojiden alındı. Gönderim, teklif-iste formundaki gibi dürüst mailto-taslağı yöntemiyle `sanatsalbaski@cadbim.com.tr`'ye gidiyor (sahte "alındı" mesajı yok). Kalan 3 hızlı-iletişim kartı (telefon/WhatsApp/e-posta) korundu. Yeni CSS "R3" revizyon bloğu olarak dosyanın kendi versiyonlama kuralına (R2 bloğu) uyularak eklendi.
- **Teklif İste formu düzeltmesi (`cadbim_teklif_iste.html`):** Onur'un "tercih edilen ofis diye bir seçenek olmamalı" geri bildirimiyle "Tercih Ettiğiniz Ofis" (İzmir/Ankara/Fark etmez) alanı formdan ve `handleSubmit`'in e-posta gövdesi oluşturma mantığından kaldırıldı; "Talep Türü" tek başına tam genişlik aldı.
- **Doğrulama:** Her iki sayfada da form alanları JS ile sayıldı (Sanatsal Baskı: 11 alan; Teklif İste: 8 alan, "ofis" yok), `formuGonder`/`handleSubmit` fonksiyonları simüle edilip hatasız çalıştığı ve sayfanın yönlenmediği doğrulandı, konsol hatası yok, ekran görüntüsüyle görsel uyum kontrol edildi.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-02-02 — Yeni "Teklif İste" sayfası oluşturuldu, nav CTA'sı buraya bağlandı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Denetim raporundaki (DK-2026-08-02-01) dönüşüm bulgularının ilk uygulama adımı.
- **Yeni sayfa:** `cadbim_teklif_iste.html` (temiz URL: `/teklif-iste`) — sitenin tasarım sistemiyle uyumlu, kendi teklif isteme formuna sahip özel sayfa. Alanlar: Ad Soyad*, Şirket, E-posta*, Telefon, Talep Türü (Yazılım/Lisans, HP Workstation/Plotter, UltiMaker, Danışmanlık, Sanatsal Baskı, Yazılım Geliştirme, Diğer — "Eğitim Talebi" ve "Teknik Destek" kasıtlı olarak çıkarıldı, bunların kendi ayrı formları planlanıyor), Tercih Edilen Ofis, Mesaj, KVKK onay kutusu. Hızlı erişim linkleri (telefon/WhatsApp/ofisler) ve tam footer (index.html'deki footer-grid) dahil edildi. `cookie-consent.js` bilinçli olarak eklendi (denetimde K4 bulgusunun tekrarlanmaması için).
- **Gönderim mekanizması (geçici, dürüst):** Backend/CRM entegrasyonu (Power Automate → Dynamics 365) henüz kurulmadığı için form `cadbim_egitimler.html`'deki gibi sahte bir "alındı" mesajı GÖSTERMİYOR (bkz. denetimde K3 bulgusu — o hataya düşülmedi). Gönder'e basınca form verileriyle doldurulmuş bir `mailto:cadbim@cadbim.com.tr` taslağı açılıyor; buton metni bunu doğru şekilde yansıtıyor ("E-posta istemciniz açılıyor..."). Power Automate uç noktası kurulduğunda `handleSubmit` gerçek bir POST'a çevrilecek.
- **Nav CTA yönlendirmesi:** "Teklif Al" linki daha önce `iletisim`'e gidiyordu; artık 1.319 sayfanın tamamında (190 kök + 1.129 post, 3 farklı eski href deseni: `iletisim`, `../iletisim`, `../cadbim_iletisim.html`) `teklif-iste`'ye yönlendirildi (toplu `sed` ile, yalnızca `class="nav-cta"` ile eşleşen link hedeflendi — sayfa içindeki diğer "iletisim" linklerine dokunulmadı).
- **Harita/config güncellemeleri:** `404.html` JS MAP'ine `teklif-iste` eklendi; `docs/htaccess-taslak.txt`'te eski Wix-legacy yönlendirmesi (`/teklif-iste → /iletisim`) kaldırılıp bölüm 3/4'e gerçek sayfa kuralları eklendi; `sitemap.xml`'e `/teklif-iste` (priority 0.8) eklendi; `docs/CANLIYA-GECIS-URL-HARITASI.md`'deki ilgili satır KURAL'dan BIREBIR'e güncellendi.
- **Kapsam dışı (kasıtlı):** Sitedeki diğer ~116 "Teklif İste" CTA'sı (hero butonları, footer linkleri vb.) hâlâ `iletisim#form`'a gidiyor — bu görev yalnızca nav'daki üst-sağ "Teklif Al" butonunu kapsıyordu. `cadbim_iletisim.html` sayfası ve içindeki MS Forms iframe'i değiştirilmedi.
- **Doğrulama:** Yerel önizlemede (`localhost:8420`) sayfa render, form alanları (9/9), mobil hamburger menü, `handleSubmit` fonksiyonu (JS ile simüle edilip hatasız/`preventDefault` çalıştığı, sayfanın yönlenmediği doğrulandı), ve nav-cta hedefinin kök + post sayfalarında doğru güncellendiği kontrol edildi. Konsol hatası yok.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-02-01 — Kapsamlı site denetimi yapıldı ve rapor yayınlandı (kod değişikliği yok)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur'un "siteyi denetle, 20.000 USD'lik bir site gibi görünmesi/çalışması için öneri sun" talebi üzerine.
- **Kapsam:** 1.318 HTML sayfa, 5 JS, 664 varlık dosyası (2,60 GiB), 16.050 iç link üç paralel kolda denetlendi (teknik SEO / performans-varlık / UX-dönüşüm-erişilebilirlik). Hiçbir site dosyası değiştirilmedi; çıktı salt rapor.
- **Öne çıkan kritik bulgular:** (K1) `.htaccess` hâlâ taslakta — tüm temiz URL'ler sunucuda HTTP 404 + JS yönlendirme hilesi; (K2) 1.126 blog URL'si hiçbir rewrite haritasında yok; (K3) eğitim formu veriyi hiçbir yere göndermiyor (sahte onay); (K4) çerez onayı + GA4 ana sayfa dahil 23 sayfada eksik; (K5) tam footer yalnız 3 sayfada; (K6) 99 Türkçe-karakterli mükerrer post çifti; (K7) ilk yükün %73,5'i tabler-icons woff2 (462 KB), gzip/cache yönergesi hiç yok; (K8) DesignJet sayfaları 10–14 MB görsel; (K9) 2,46 GiB referanssız ham varlık site kökünde.
- **Çıktı:** `docs/SITE-DENETIM-RAPORU-2026-08-02.md` — 9 kritik + 12 yüksek + 20 orta/düşük bulgu, güçlü yönler ve 4 fazlık "20.000 USD sınıfı" yol haritası (Faz 0: dağıtım/form/analitik yangın söndürme · Faz 1: performans+SEO · Faz 2: dönüşüm+güven, Dynamics 365 form entegrasyonu · Faz 3: SSG+CI/CD). Rapor ayrıca bulut artifact olarak yayınlandı.
- **Durum:** ✅ Rapor tamamlandı; düzeltmeler Onur'un faz onayını bekliyor.

### DK-2026-08-02-01 — Site genelinde "pill" tarzı çapraz-satış bölümleri kart stiline dönüştürüldü (158 dosya)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, SketchUp sayfasında aynı içeriği iki farklı stille tekrarlayan bölümleri gösterip (DK-2026-08-02 öncesi konuşma) beğendiği kart stilinin ("Entegrasyonlar" bölümü) siteye yaygınlaştırılmasını istedi.
- **Kapsam:** Sitede sayfa sonlarında "İlgili ürünler/çözümler/endüstriler/başarı öyküleri" gibi bilgiyi gösteren `class="cpills"` (hap/pill) tasarımı — küçük yuvarlak linkler — tutarsız ve içerik olarak "zayıf" görünüyordu (Onur'un ifadesiyle). Kart stiline (`card-icon` + `h3` + açıklama cümlesi) dönüştürüldü: `.cross`/`.cross-grid` kutuları kaldırılıp `.sh` (slabel/stitle/ssub) + `.grid g3` desenine, kategori başlıklı gruplarda ise başlık korunup yalnızca `cpills` içeriği `grid g3`'e çevrildi.
- **Ölçek:** 158 dosya, ~1930 kart. Sitede önceden `class="cpills"` içeren tüm dosyalar (129 orijinal + bu oturumda oluşturulan 4 yeni SketchUp sayfası) tek tek işlendi. İş, 6 arka plan ajan dalgasında (HP/ZBook 20 dosya, DesignJet ailesi 22 dosya, ardından kalan 52 dosya 4 paralel pakette: Adobe/Chaos/UltiMaker artıkları, Çözüm/Sektör sayfaları, Autodesk BIM/Reality/Core, Autodesk üretim/fabrication) yürütüldü; ilk dalgadaki bazı ajanlar hesap bazlı API rate-limit'e takılıp yarıda kesildi, limit sıfırlandıktan sonra sadece kalan dosyalarla yeniden başlatıldı.
- **Kart ikonu seçimi:** Öncelik sırası (1) ürüne özel logo (`assets/logos/products/`), (2) marka logosu (`assets/logos/`), (3) hiçbiri yoksa pill'in kendi Tabler ikonu. Jenerik/paylaşılan marka logoları (örn. `chaos.webp` hem Enscape hem V-Ray için, `autodesk-white.svg` her Autodesk ürünü için) mümkün olduğunca ürüne özel logoyla değiştirildi.
- **Kapsam dışı bırakılan (kasıtlı, dokunulmadı):** `.cross`/`.cpills`/`.cp` CSS kuralları (artık kullanılmıyor ama silinmedi — başka bir temizlik görevi); farklı class isimli benzer bloklar (`cross-pills`, `feat-grid`/`feat-card` gibi) — bunlar bu görevin kapsamındaki `cpills` deseniyle karışmasın diye ayrıştırıldı.
- **Doğrulama:** Tüm 158 dosyada `class="cpills"` sıfıra indi (site-geneli grep); her dosyada `<div`/`</div` sayıları eşit (denge bozulmadı); her dosyada referans verilen tüm logo dosyalarının diskte var olduğu doğrulandı (0 eksik asset); tarayıcıda (yerel statik sunucu) 158 dosyanın tamamı fetch edilip her `.card` içindeki linklerin boş/kırık olmadığı ve `.cpills` kalıntısı kalmadığı script ile teyit edildi.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-07-31-01 — SketchUp sayfası hataları düzeltildi + 4 eksik ürün sayfası oluşturuldu

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur'un `cadbim_sketchup.html` canlı önizlemesinde sırayla fark ettiği 3 görsel/içerik hatası üzerine.
- **1) Uydurma hero rozeti:** 31 Temmuz akşamki toplu ikon düzeltmesinde (bkz. commit 441f7e4) `cadbim_sketchup.html` gözden kaçmış, hero'da elle çizilmiş mavi "SU" SVG'si kalmıştı. Kardeş sayfalarla (Go/Studio) tutarlı şekilde gerçek `sketchup-icon.svg` ile değiştirildi.
- **2) "Advanced Workflow" → "Advanced Workflows":** Trimble'ın resmi plan sayfası (sketchup.trimble.com/plans-and-pricing) doğrulandı; resmi isim çoğul "Advanced Workflows". 4 yerde (Planlar kartı, Studio açıklaması, ürün kataloğu kartı) düzeltildi.
- **3) Entegrasyonlar bölümü bozuk ikon kutuları (Onur ekran görüntüsüyle gösterdi):** `.card-icon` kuralı genişlik/yükseklik/flex-ortalama tanımı olmadan yazılmıştı (`cadbim_lumion.html`'de de aynı hata var, ayrı görev olarak flag'lendi: task_6d88e7d9) — arka plan koyu bir çubuk gibi görünüyordu. UltiMaker hub sayfasındaki doğru desene (46×46, flex ortalanmış) göre düzeltildi.
- **4) Gerçek ürün logoları:** Entegrasyonlar bölümünde Chaos Enscape ve Chaos V-Ray aynı jenerik `chaos.webp` şirket logosunu, Revit jenerik `autodesk-white.svg`'yi, Adobe CC jenerik `adobe-logo.svg` wordmark'ını kullanıyordu. Kendi resmi ürün ikonlarıyla (`enscape.svg`, `vray.svg`, `revit.svg`, `adobe.png`) değiştirildi.
- **5) 4 eksik ürün sayfası oluşturuldu:** Ürün kataloğunda SketchUp Pro, Pro Scan, Pro Civil Contractor ve Advanced Workflows'un kendi sayfası yoktu (sadece Go/Studio/Trimble Connect'in vardı) — Onur önce "istemiyorum" dedi, sonra fikrini değiştirip istedi. Go/Studio şablonu temel alınarak `cadbim_sketchup_pro.html`, `cadbim_sketchup_pro_scan.html`, `cadbim_sketchup_pro_civil_contractor.html`, `cadbim_sketchup_advanced_workflows.html` oluşturuldu (hero, özellik/kullanım kartları, "Cadbim Farkı" bloğu, cross-sell, SEO meta + JSON-LD, CTA). İçerik Trimble'ın resmi plan sayfasından doğrulanan bilgilere dayanıyor (Pro Civil Contractor: Trimble Siteworks bağlantılı saha/hafriyat çözümü; Advanced Workflows: Pro Scan + Revit Importer). Hub sayfasındaki (Planlar + Ürün Kataloğu) ilgili kartlar bu 4 sayfaya bağlandı; kataloğun 3 kartındaki jenerik Tabler ikonları (`ti-scan`, `ti-bulldozer`, `ti-stack-2`) gerçek SketchUp logosuyla değiştirildi (Trimble bu alt-tierlar için ayrı resmi logo sağlamıyor).
- **6) `.htaccess` taslağı güncellendi (henüz sunucuda değil):** `docs/htaccess-taslak.txt`'e 4 yeni sayfanın temiz-URL↔dosya eşlemesi (rewrite + `.html`→temiz-URL 301) eklendi; eski Wix yönlendirmesi `/sketchup/sketchup-pro` artık genel hub yerine doğrudan `/sketchup-pro`'ya işaret ediyor.
- **Doğrulama:** Yeni sayfalardaki tüm Tabler ikon sınıfları CSS'te mevcut olduğu doğrulandı; `.card-icon` kutu boyutları tarayıcıda computed-style ile 46×46/flex doğrulandı; Trimble'ın resmi plan sayfası fetch edilerek Pro Scan/Civil Contractor/Advanced Workflows açıklamaları teyit edildi.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-07-29-11 — Blog'da "BIM 360" ve "Fusion Team" eski isimlendirmeleri güncellendi (16 dosya)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · DK-10'da kapsam dışı bırakılıp ayrı göreve (task_0b5f7372) kaydedilen bulgunun tamamlanması.
- **Kapsam:** Autodesk, "BIM 360" ürününü resmi olarak ikiye ayırdı: proje/inşaat yönetimi + model koordinasyonu tarafı **Autodesk Construction Cloud**, ortak veri ortamı (CDE)/dosya paylaşımı/erişim izinleri tarafı **Autodesk Docs** oldu. "Fusion Team" ise Fusion 360'ın eski bulut veri yönetimi özelliğiydi; bugün ayrı bir ürün adı olarak kullanılmıyor, işlev doğrudan Autodesk Fusion'ın bulut veri yönetimi olarak anılıyor.
- **BIM 360 → Docs/Construction Cloud (14 dosya, ~63 occurrence):** Her cümle tek tek okunup bağlamına göre karşılık seçildi — dosya yükleme/erişim izinleri/ekip yönetimi içerikleri **Autodesk Docs**'a (`bim-360-a-dosya-yukleme.html`, `bim-360-bulutta-ekipler-ile-çalışma-ve-erişim-i-zinlerini-yönetme.html`, `bim360-design-...` 2 dosya, `plant-3d-bim-360-design-i-ş-akışı.html`, `plant-3d-revit-navisworks-infraworks-i-ş-akışı.html`), model koordinasyonu/çakışma tespiti içerikleri **Autodesk Construction Cloud**'a (`autodesk-bim-360-bulutta-model-koordinasyonu-ve-çakışma.html`, `autodesk-bim-360-bulutta-tasarım-değişikliklerini-paylaşma.html`, `bim-360-bulutta-model-koordinasyonu.html`), genel/karma proje yönetimi içerikleri her ikisine birden (`autodesk-bim-360-projelerinizi-bulutta-yönetin.html`, `bim-360-ile-proje-olusturmak-ve-hizmetleri-etkinlestirmek.html`, `bim-360-projelerinizi-bulutta-yonetin.html`, `projenin-başarısı-i-çin-yapı-i-nşa-sürecindeki-kayıpların-ortadan-kaldırılması.html`, `uzaktan-çalışan-veya-kalabalık-ekip-üyeleri-için-bulut-tabanlı-tasarım.html`) yönlendirildi. Tarihsel/geçiş bağlamında BIM 360'tan bahseden hiçbir cümleye rastlanmadı (0 cümle bilinçli olarak değiştirilmeden bırakıldı).
- **Fusion Team → Autodesk Fusion'ın bulut veri yönetimi (2 dosya):** `fusion-360-veri-yönetimi-fusion-team.html` (başlık dahil "Fusion Team" adı tamamen kaldırılıp "Autodesk Fusion Veri Yönetimi ve Bulut İş Birliği" olarak yeniden yazıldı) ve `verilerinizi-fusion-360-ile-kolayca-yönetin.html`. Bir cümledeki gereksiz tekrar ("bulut veri yönetimi ... Fusion'ın veri yönetimi ... bulut tabanlı yapıdır") ilk geçişte agent tarafından üretildi, elle "bu yapı üzerinden yürütülür" şeklinde düzeltildi.
- **Kapsam dışı bırakılan (dokunulmadı, kasıtlı):** Aynı konudaki farklı/eski dublicate slug'lı dosyalar (`bim-360-team.html`, `bim-360.html`, `bim-360-design.html`, `bim-360-docs.html`, `bim-360-field.html`, `bim-360-glue-overview-video.html` vb. ASCII-slug'lı ~18 dosya) bu görevin kapsamında değildi — orijinal görev talimatı yalnızca "Fusion 360"tan Türkçe ek uyumlu 129 dosyalık geçişte tespit edilen 16 spesifik dosyayı kapsıyordu; bu diğer dosyalar ayrı bir tarama gerektirir.
- **Doğrulama:** 16 hedef dosyada `grep -r "BIM 360\|Fusion Team"` sıfır sonuç; `div`/`section` etiket dengesi (`<div>`/`</div>`, `<section>`/`</section>` sayıları) `post/*.html` genelinde eşit; diff'ler satır satır okunarak akıcılık/tutarlılık kontrol edildi.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-29-10 — Fabrication/CFD gerçek logoları + Autodesk cross-sell tasarımı + blog'da "Fusion 360" güncellemesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı).
- **1) Eksik logolar (Onur canlı önizlemede fark etti):** 28 Temmuz'da hızlıca eklenen Fabrication CADmep/ESTmep/CAMduct ve CFD ürünleri jenerik Tabler ikonlarıyla (ti-pipe/ti-calculator/ti-cut/ti-wind) kalmıştı — kendi ürün sayfaları dahil, hiçbir yerde gerçek logo yoktu. Autodesk'in resmi sitesinden (autodesk.com/products/fabrication, /cfd) gerçek ürün ikonları çekildi: `assets/logos/products/fabrication.svg` (ESTmep/CADmep/CAMduct — Autodesk bu 3 ürünü tek aile ikonuyla pazarlıyor) ve `assets/logos/products/cfd.png`. Uygulandı: `cadbim_autodesk.html` (4 pcard), `cadbim_aec_collection.html` (3 cpill), `cadbim_simulasyon.html` (1 cpill), `cadbim_fabrication_cadmep/estmep/camduct.html` (hero ikonu + çapraz cpill'ler), `cadbim_cfd.html` (hero ikonu). Karşılıklı çapraz linklerdeki dekoratif özellik ikonları (feat-icon) kasıtlı olarak dokunulmadı (logo değil, süsleme).
- **2) Autodesk "sıkça tercih edilenler" tasarımı (Onur "sıkıcı ve düz" dedi):** `.cross` bölümüne çift radial-gradient glow arka plan + eyebrow etiket ("Ekosistem") eklendi. `.xp` kartları: marka rengine göre `--ac` CSS değişkeni (HP mavi, Chaos kırmızı, UltiMaker turkuaz, Adobe kırmızı), hover'da üstte renkli çizgi kayması + köşeli glow (box-shadow) + logo kutusunun marka rengiyle dolması + ok ikonunun kayıp renklenmesi. Logo kutusu 42→48px büyütüldü.
- **3) Blog'da "Fusion 360" → "Autodesk Fusion":** Onur ürün adının güncel olmadığını fark etti. 129 blog yazısında (`post/*.html`) 1608 geçiş güncellendi: önce "Fusion 360 Manage" → "Fusion Manage" (13, ayrı ürün adı), sonra kalan "Fusion 360" → "Autodesk Fusion" (1595). Yan etki: bazı cümlelerde zaten "Autodesk Fusion 360" yazıyordu, bu da "Autodesk Autodesk Fusion" ikilemesi yarattı — 302 ek düzeltmeyle giderildi. Türkçe ek uyumu (Fusion'ın/'da/'a/'daki) sitenin kendi mevcut kullanım örnekleriyle (`Autodesk Fusion'a` zaten 10 yerde kullanılıyordu) doğrulanarak korundu.
- **Kapsam dışı bırakılan, ayrı göreve çevrilen bulgu:** Blog'da hâlâ eski "BIM 360" (14 dosya) ve "Fusion Team" (2 dosya) isimleri geçiyor — bunlar bağlama duyarlı (tarihsel cümlelerde doğru kalabilir) olduğu için mekanik değiştirilmedi, ayrı arka plan görevine kaydedildi (task_0b5f7372).
- **Doğrulama:** Tüm değiştirilen sayfalarda `div` denge kontrolü tam; tarayıcıda 52 benzersiz ürün ikonunun tamamı 200 OK; `Fusion 360` ve `Autodesk Autodesk` deseni sitede sıfıra indi; cross-sell CSS'i tarayıcıda computed-style ile doğrulandı (--ac değişkeni, 48px logo, gradient arka plan uygulanmış).
- **Durum:** ✅ Üç madde de tamamlandı.

### DK-2026-07-29-09 — ACİL (gerçek kök neden): tüm iç linkler kök-mutlak yerine göreli yapıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · DK-07'deki 404.html düzeltmesi kısmi kalmıştı — Onur ekran görüntüsüyle üst menü/mega-menü linklerinin (durum çubuğunda `https://bzkindamix.github.io/autodesk` göründüğü) hâlâ kırık olduğunu gösterdi.
- **Gerçek kök neden:** DK-03'te iç linkler `href="/autodesk"` gibi **kök-mutlak** yapılmıştı. Kök-mutlak bir link her zaman alan adının KÖKÜNE göre çözülür — sayfanın kendi alt-yolunu (GitHub Pages'te `/cadbim_website/`) YOK SAYAR. Bu yüzden `/autodesk` linki `bzkindamix.github.io/autodesk`'e gidiyordu (proje deposunun tamamen dışında, 404.html'in bile devreye giremeyeceği bir adres). DK-07'deki 404.html yalnızca doğrudan yazdığım tam URL'lerde işe yaramıştı çünkü onlar zaten `/cadbim_website/` içindeydi; sayfa İÇİNDEKİ linkler için hiç işe yaramıyordu.
- **Doğru çözüm:** Kök-mutlak (`/x`) yerine **göreli** linkler kullanmak — bu hem GitHub Pages'in alt-yolunda hem Natro'nun kök alan adında doğru çalışır (tarayıcı her zaman mevcut sayfanın dizinine göre çözer).
  - **178 kök sayfa:** `href="/x"` → `href="x"`, `href="/"` → `href="index.html"` (11.122 değişiklik).
  - **739 blog yazısı (`post/`):** `href="/x"` → `href="../x"`, `href="/"` → `href="../index.html"` (13.304 değişiklik) — bu dosyalar bir alt dizinde olduğu için `../` gerekli.
  - **mobilenav.js + cookie-consent.js:** Bu 2 dosya HEM kök HEM `post/` sayfalarından aynı anda yüklendiği için tek bir sabit yol yazılamazdı — çalışma zamanında `location.pathname`'e bakıp derinliğe göre `""` veya `"../"` öneki hesaplayan `withBase()`/`CBM_BASE` mantığı eklendi; mega-menü, arama sonuçları ve ⌘K komut paleti artık bu fonksiyonu kullanıyor.
  - Cache-buster'lar bir sürüm artırıldı (`cookie-consent.js?v=1→2`, `mobilenav.js?v=9→10`) — mevcut tarayıcı önbellekleri eski (kırık) sürümü tutmasın diye.
- **Doğrulama:** `node --check` ile 2 JS dosyası hatasız; `grep` ile site genelinde `href="/[a-harf]` deseni sıfıra indi (yalnızca mobilenav.js'in veri dizisindeki ham slug'lar kaldı, onlar `withBase()`'den geçiyor); `div` denge kontrolü bozulmadı; localhost'ta çerez linki `kvkk-cerez-politikasi` (önek yok) doğru üretiliyor. **GitHub Pages'te nihai doğrulama push sonrası yapılacak** (yerel statik sunucu 404.html/rewrite davranışını taklit etmiyor).
- **Durum:** ✅ Kod düzeltmesi tamamlandı, push edilecek. ⚠️ Canlı doğrulama bekleniyor.

---

## 2026-07-29

### DK-2026-07-29-08 — Mobil menü "Teklif Al" CTA linki de göreli yapıldı

- **Yapan:** Claude (PDM asistanı) · DK-09'un tamamlayıcısı — `withBase()` geçişinde `mobilenav.js`'teki mobil panelin sabit "Teklif Al" CTA butonu (`href="/iletisim#form"`) atlanmıştı, hâlâ kök-mutlak kalmıştı.
- **Düzeltme:** `withBase("/iletisim#form")` kullanılacak şekilde düzeltildi; cache-buster `mobilenav.js?v=10→11`.
- **Doğrulama:** `node --check mobilenav.js` hatasız; `grep 'href="/'` sitede sıfır sonuç.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-29-07 — ACİL: GitHub Pages önizlemesinde üst menü linkleri 404 veriyordu, düzeltildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur canlı önizlemede (bzkindamix.github.io/cadbim_website/) hangi üst menü linkine tıklarsa tıklasın 404 aldığını bildirdi.
- **Kök neden:** DK-2026-07-29-03'te iç linkler kasıtlı olarak temiz URL'e (`href="/bim"`) çevrilmişti — bu, gelecekteki Natro sunucusunda `.htaccess` ile çözülecek şekilde tasarlanmıştı. Ancak GitHub Pages önizlemesi (a) böyle bir sunucu-taraflı rewrite yapmıyor, (b) alt-yol (`/cadbim_website/...`) üzerinden yayın yapıyor — bu yüzden `/bim` gibi kök-mutlak bir link GitHub Pages'te doğrudan `bzkindamix.github.io/bim`'e gidip 404 veriyordu.
- **Düzeltme:** Kök dizine `404.html` eklendi. GitHub Pages eşleşmeyen her yolda bu dosyayı sunar; sayfa istenen path'i (repo alt-yolu dahil) çözüp 177 sayfalık slug→dosya haritasından gerçek `cadbim_*.html`/`sektor_*.html` dosyasına anında yönlendirir (`location.replace`). Natro'da (kök alan adı) da güvenli çalışır ama orada `.htaccess` zaten sunucu tarafında çözeceği için pratikte devreye girmez.
- **Doğrulama:** `node` ile JSON harita ayrıştırma test edildi (177 kayıt, `bim`→`cadbim_bim.html` gibi doğru eşleşiyor); path-çözme mantığı elle izlendi (github.io alt-yol senaryosu ve kök-alan senaryosu). GitHub Pages'in gerçek 404 davranışı yalnızca canlıda doğrulanabilir — Onur'un push sonrası (GitHub Pages yeniden derlemesi ~1 dakika sürer) sert yenileme ile teyit etmesi gerekiyor.
- **Durum:** ✅ Düzeltme push edildi (commit `d60f1e9`). ⚠️ Canlıda son doğrulama Onur'dan bekleniyor.

### DK-2026-07-29-06 — HP sayfası: katalog ürün görselleri gerçeğiyle değiştirildi + servis başlığı düzeltildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur canlı önizlemeden (bzkindamix.github.io/cadbim_website/cadbim_hp.html) 2 madde istedi.
- **1) Ürün Kataloğu görselleri:** 24 ürün kartından 22'sinde jenerik HP logosu (26×26, `.pico` kutusu) yerine gerçek ürün fotoğrafı kondu (34×34, UltiMaker sayfasındaki mevcut site kuralıyla aynı boyut) — `assets/products/` altındaki mevcut gerçek görseller kullanıldı (ör. T850→`hp-designjet-t850.png`, Z9+ Pro→`hp-designjet-z9pro.png`, HD Pro 2 Tarayıcı→`hp-scanner-hd-pro.png`, Z Workstation→`hp-z-workstation-group.png`, Monitör→`hp-workstations/monitor-724pf.png`). **Build Workspace kartı bilinçli olarak değiştirilmedi** — fiziksel ürün değil bulut/yazılım platformu, zaten gerçek HP logosu kullanıyordu (sahte değildi).
- **2) Başlık düzeltmesi:** "HP Teknik Servis Merkezi" → **"HP DesignJet Plotter Teknik Servisi"** (servis kapsamının yalnızca plotter olduğunu netleştirmek için — sayfadaki alt metin zaten "workstation ve diğer ürünler için servis verilmemektedir" diyordu, başlık artık bununla tutarlı).
- **Doğrulama (localhost, tarayıcı `fetch` ile):** 22 görselin tamamı 200 OK; `div`/`a` etiket dengesi bozulmadı (102/102, 82/82); konsol hatası yok.
- **Durum:** ✅ Her iki madde tamamlandı.

### DK-2026-07-29-05 — mobilenav.js: 5 hayalet arama kaydı temizlendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · DK-2026-07-29-03'te flag'lenen ayrı görev (task_53852110), Onur'un chip'i başlatmasıyla yapıldı.
- **Düzeltmeler (`mobilenav.js` arama/komut paleti veri dizisi):**
  1. `"DesignJet T870" → cadbim_designjet_t870.html` (hiç var olmamış model/sayfa) — satır tamamen silindi.
  2. `"DesignJet Tarayıcılar" → cadbim_designjet_tarayicilar.html` (tekil hayalet sayfa) — gerçek iki sayfayı ayrı ayrı temsil edecek şekilde ikiye bölündü: "DesignJet HD Pro 2 Tarayıcı" → `/designjet-hd-pro`, "DesignJet SD Pro 2 Tarayıcı" → `/designjet-sd-pro`.
  3. `"HP DesignJet T/XL/Z Serisi"` (3 satır, hiç yapılmamış "seri hub" sayfalarına işaret ediyordu) — aynı dizide zaten var olan `"HP DesignJet Ailesi" → /designjet` kaydıyla birebir aynı işlevi gördükleri için 3 satır da tamamen silindi (tekrar önlendi).
- **Kapsam dışı bırakılan:** `nav.nav`/`.nav-links`/`.nav-cta` DOM seçicilerine dokunulmadı (talimat gereği).
- **Doğrulama (localhost, tarayıcı):** `node -e "require('./mobilenav.js')"` ile sözdizimi hatası yok (yalnızca beklenen `document is not defined` runtime hatası, tarayıcı dışı ortamda normal); ana sayfada arama paneli açılıp "designjet" arandı — sonuçların tamamı gerçek `/designjet-*` sayfalarına gidiyor, hiçbir `cadbim_*.html` veya hayalet kayıt kalmadı; konsol hatası yok.
- **Durum:** ✅ 5 hayalet kayıt temizlendi.

### DK-2026-07-29-04 — HP sayfası: sahte logo değişti, partner rozeti küçültüldü, 3 tanıtım şeridi kaldırıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur canlıdaki GitHub Pages önizlemesini (bzkindamix.github.io/cadbim_website/cadbim_hp.html) inceleyip 3 madde istedi.
- **1) Sol üst sahte HP logosu:** Hero'daki 72×72 kutu, elle çizilmiş inline SVG (mavi kare + "hp" yazısı) idi — gerçek HP marka logosu değildi. `assets/logos/hp-logo.png` (gerçek, resmi HP daire logosu, zaten ürün kartlarında kullanılıyordu) ile değiştirildi.
- **2) Sağ üst partner rozeti büyük geliyordu:** `hp-amplify-insignia.png` (gerçek HP Amplify Synergy Partner sertifika rozeti — sahte değil, sadece boyutu orantısızdı) `clamp(190px,18vw,240px)` → `clamp(140px,13vw,170px)` yapıldı (site genelindeki Autodesk/Adobe hero-badge örnekleriyle daha tutarlı).
- **3) 3 tanıtım şeridi kaldırıldı:** "Geniş Format Yazıcılar / HP Designjet Serisi", "İş İstasyonları / HP Z Serisi Workstation", "Bulut Platformu / HP Build Workspace" şeritleri (özet kartlarıyla) tamamen silindi; sayfa artık hero'dan direkt "Ürün Kataloğu" (24 ürün, filtre+arama) bölümüne geçiyor.
- **Doğrulama (localhost):** `section`/`div` etiket dengesi tam (4/4, 102/102); ağ isteklerinde 3 logo da 200 OK; konsol hatası yok; sayfa metni hero→Ürün Kataloğu→Yetkili Servis→cross-sell→CTA sırasıyla akıyor. (Tarayıcı paneli bu oturumda görsel ekran görüntüsü alamadı — metin/ağ/konsol bazlı doğrulandı.)
- **Durum:** ✅ 3 madde de tamamlandı.

### DK-2026-07-29-03 — İç linkler temiz URL formatına çevrildi (922 dosya)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "iç linkler temiz URL formatına çevrilsin" ve "T/XL/Z serisi için ayrı hub yapılmasın, genel /designjet yeterli" kararlarını onayladı.
- **Kapsam:** Site kökündeki 178 sayfa + `mobilenav.js`/`cookie-consent.js` + **`post/` klasöründeki 739 blog yazısı** (toplam 922 dosya) taranıp `href="cadbim_x.html"` / `href="sektor_x.html"` / `href="index.html"` biçimindeki tüm iç linkler gerçek dosya adından üretilen temiz slug'a (`href="/x"`) çevrildi. Fragment/query korunuyor (`cadbim_iletisim.html#form` → `/iletisim#form`).
- **Kendi kendini yakaladığım hata:** İlk geçişte yalnızca kök dizin taranmıştı; `post/` klasörünü unuttuğumu ikinci taramada fark ettim. Ayrıca post sayfaları bir alt dizinde olduğu için linkler `../cadbim_x.html` biçimindeydi — basit metin değişimi `..//x` gibi kırık bir çift-slash üretti; bunu `..//` → `/` toplu düzeltmesiyle giderdim. Düzeltme sonrası site genelinde çift-slash kalmadığı doğrulandı.
- **Kapsam dışı bırakılan (ayrı bulgu):** `mobilenav.js`'teki arama/komut paleti veri listesinde **5 hayalet kayıt** var — var olmayan sayfalara işaret ediyor: `cadbim_designjet_t870.html`, `cadbim_designjet_tarayicilar.html`, `cadbim_hp_designjet_t.html`, `cadbim_hp_designjet_xl.html`, `cadbim_hp_designjet_z.html`. Bunlar mevcut dosya listesiyle eşleşmediği için bu turda dokunulmadı (script sadece gerçek dosyaları çevirdi). Ayrı bir düzeltme gerekiyor — muhtemelen arama sonuçlarında kırık link üretiyorlar.
- **Doğrulama:** 922 dosyada 22.781 değişiklik; dönüşüm sonrası `cadbim_*.html`/`sektor_*.html` deseni (mobilenav.js'teki 5 hayalet hariç) sitede kalmadı; çift-slash 0; `../assets/...` gibi ilgisiz göreli yollar dokunulmadan kaldı; canonical/og:url etiketleri zaten mutlak temiz URL kullandığı için etkilenmedi.
- **Durum:** ✅ İç linkler temiz URL formatına geçti. ⚠️ Ayrı görev: mobilenav.js'teki 5 hayalet arama kaydı temizlenmeli.

### DK-2026-07-29-02 — Host kararı: Natro + .htaccess 301/temiz-URL taslağı üretildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur host olarak **Natro**'yu seçtiğini bildirdi ve Natro'nun `.html` uzantısız çalıştığını gözlemlemiş.
- **Araştırma:** Natro paylaşımlı hosting (Linux/cPanel) `.htaccess`, `mod_rewrite` ve sunucu-taraflı 301 yönlendirmeyi destekliyor (natro.com resmi blog kaynakları ile doğrulandı). Bu, [[cadbim-hosting-url-semasi]]'ndeki "host GitHub Pages olursa 301 yapılamaz" riskini ortadan kaldırıyor — Natro bunu native yapabiliyor.
- **Bulgu (harita düzeltmesi):** `docs/redirects-taslak.csv`'deki 6 hedef URL gerçek dosya adlarıyla uyuşmuyordu (typo/tutarsızlık): `/designjet-z6-pro`→`/designjet-z6pro`, `/designjet-z9-pro`→`/designjet-z9pro`, `/substance-3d`→`/substance3d` (dosya adlarıyla eşleşecek şekilde düzeltildi, 17 satır etkilendi). Ayrıca 3 hedef (`/hp-designjet-t`, `/hp-designjet-xl`, `/hp-designjet-z`) siteye hiç eklenmemiş "seri hub" sayfalarını işaret ediyordu (harita hazırlanırken onaylanmış ama sayfa hiç yapılmamış) — geçici olarak genel `/designjet` kataloğuna yönlendirildi. **Karar (Onur, 2026-07-29):** Ayrı T/XL/Z hub sayfası yapılmayacak, genel `/designjet` kataloğu yeterli — nihai.
- **Üretilen taslak:** `docs/htaccess-taslak.txt` (743 `RewriteRule`, UTF-8 BOM'suz) — 3 blok: (1) https+www kanonik yönlendirme, (2) 388 eski Wix URL → yeni site 301 haritası (CSV'den otomatik üretildi, Türkçe/yüzde-kodlu eski URL'ler `unquote()` ile çözülüp regex-escape edildi — hem düz hem yüzde-kodlu istek formunu kapsar), (3) temiz URL → gerçek dosya iç yeniden yazımı (177 sayfa, adres çubuğu değişmez) + eski `.html` erişimini temiz URL'e 301 ile tekilleştiren tamamlayıcı kural seti.
- **Doğrulama:** Script çıktısı — 665 CSV satırından 388 KURAL, 277 BIREBIR (atlandı); 0 çakışma, 0 kendine-döngü, 0 eksik hedef (düzeltmeler sonrası); dosya adı↔slug eşlemesinde 0 çakışma (178 dosya).
- **Durum:** ✅ Taslak hazır, **henüz sunucuya yüklenmedi**. Bekleyenler: (a) staging/test ortamında deneme, (b) T/XL/Z hub kararı, (c) iç linklerin (`cadbim_*.html` → temiz slug) siteye uygulanıp uygulanmayacağı kararı (aşağıya soruldu).

### DK-2026-07-29-01 — Ürün logosu placeholder kontrolü: eksik logo yok, ölü CSS temizlendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur 21 Temmuz'daki eksik logo listesinin hâlâ güncel olup olmadığını sordu.
- **Bulgu:** `cadbim_designjet.html`, `cadbim_hp.html`, `cadbim_lumion.html`, `cadbim_sketchup.html` dosyalarında `.plogo-ph` CSS kuralı duruyordu ama hiçbir yerde `class="plogo-ph"` kullanımı yoktu — 21 Temmuz'daki 88/88 logo tamamlama turu placeholder'ları zaten gerçek logolarla değiştirmiş, geriye yalnızca kullanılmayan CSS kalmış.
- **Düzeltme:** 4 dosyadaki kullanılmayan `.plogo-ph{...}` CSS kuralı silindi.
- **Not:** `.claude/worktrees/stoic-wing-4f7009/` altında bu 4 dosyanın eski bir kopyası duruyordu (ajan çalışma alanı kalıntısı) — Onur onayıyla `git worktree remove` ile kaldırıldı (bekleyen değişiklik yoktu, veri kaybı olmadı).
- **Durum:** ✅ Eksik ürün logosu yok; ölü CSS temizlendi; kalıntı worktree kaldırıldı.

---

## 2026-07-28

> **Not (geriye dönük toplu kayıt):** Aşağıdaki 12 kayıt, 2026-07-28'de art arda yapılan ~39 commit'i özetler. PDM disiplini o gün için canlı tutulmadı (kayıtlar 2026-07-29'da geriye dönük işlendi); her commit ayrı DK olarak değil, mantıksal iş grupları halinde tek DK'da toplandı. Bundan sonra kayıtlar yine değişiklik anında açılacak.

### DK-2026-07-28-12 — Site geneli temizlik: canonical/sitemap hataları + kullanılmayan sayfa silindi

- **Kapsam:** Başıboş sayfa taraması yapıldı; birden fazla sayfada hatalı canonical URL ve sitemap'te eksik/yanlış girişler düzeltildi. Kullanılmayan `tesekkurler.html` sayfası ve ona ait OG görseli silindi (hiçbir yerden linklenmiyordu).
- **Referans:** `d6155e3`, `1639955`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-11 — Blog verisine cache-busting

- **Kapsam:** Blog verisini çeken fetch çağrılarına cache-busting parametresi eklendi (66 sayfa) — tarayıcı önbelleği yeni/güncellenen yazıları geç göstermesin diye.
- **Referans:** `dac815e`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-10 — Blog migrasyonu tamamlandı: 242 gerçek Wix yazısı + 500 YouTube videosu

- **Kapsam:** Wix'teki tüm gerçek blog yazıları (6 ilk yazı → 91 → +135, toplam 242) yeni blog mimarisine taşındı; ayrıca 500 YouTube videosu blog postuna dönüştürüldü (HP Build Workspace serisi dahil, 8 video). Blog mimarisi (kategori+ürün filtreli hub) kuruldu, "Blog" linki tüm sayfalara eklendi. Video postlarına başlık bazlı profesyonel açıklamalar yazıldı. Blog ürün filtresine Adobe ürünleri + eksik ana ürünler eklendi. Ürün/çözüm/endüstri sayfalarına "ilgili blog içerikleri" widget'ı eklendi, sonradan CTA öncesine taşındı; webinar ürün filtresi eklendi.
- **Sonuç:** Canlıya geçiş haritasındaki **339 GOZDEN-BLOG kalemi kapandı** (bkz. `docs/CANLIYA-GECIS-URL-HARITASI.md` §1 özet tablosu — GOZDEN-BLOG artık 0).
- **Referans:** `6e42cfe`, `5e33ee4`, `a68a5ee`, `66a4b8b`, `3bc3d46`, `4b1678d`, `4d5fbf6`, `83174a4`, `d210a1b`.
- **Durum:** ✅ Blog migrasyonu tamamlandı.

### DK-2026-07-28-09 — YouTube→blog otomasyonu + e-posta bildirimleri

- **Kapsam:** YouTube'daki yeni videoları otomatik blog postuna çeviren bir workflow kuruldu; senkronizasyon sıklığı günde 1'e düşürüldü. Yeni video eklendiğinde Gmail SMTP üzerinden e-posta bildirimi gönderiliyor (alıcılar, özet açıklama, otomasyon/AI etiketi eklendi — bildirim test edildi).
- **Not:** Bu otomasyon canlı bir arka plan işi (cron/scheduled task); repodaki kod bunun tetikleyicisi/şablonu.
- **Referans:** `0164bf9`, `50dd73f`, `d59b210`, `d4ed2a0`, `9dc16f5`, `dc30595`, `7c65a42`, `1777613`, `222145a`, `b552371`.
- **Durum:** ✅ Kuruldu ve çalışıyor.

### DK-2026-07-28-08 — Sosyal medya ikon şeridi

- **Kapsam:** Sitenin sol kenarına sabit, her sayfada görünür bir sosyal medya hesapları ikon şeridi eklendi.
- **Referans:** `0cf79c5`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-07 — Autodesk CFD ürün sayfası + kalan GÖZDEN kalemleri kapatıldı

- **Kapsam:** Autodesk CFD hâlâ satılan bir ürün olduğu için yeni ürün sayfası oluşturuldu (`/cfd`). Bu adımla canlıya geçiş haritasındaki kalan **GOZDEN kalemleri de kapatıldı** (özet tabloda GOZDEN artık 0). Not: `docs/CANLIYA-GECIS-URL-HARITASI.md` §4 detay tablosunda `/etkinlikler` ve `/kampanyalar` satırları hâlâ eski "GOZDEN" etiketiyle görünüyor — özet ile detay arasında küçük bir doküman tutarsızlığı var, sonraki oturumda etiketler senkronize edilmeli.
- **Referans:** `c9ac3e6`.
- **Durum:** ✅ Sayfa eklendi; ⚠️ doküman etiket tutarsızlığı açık.

### DK-2026-07-28-06 — Webinar Takvimi sayfası

- **Kapsam:** Ağustos-Ekim 2026 dönemi için 9 aktif webinarı listeleyen yeni bir Webinar Takvimi sayfası eklendi; webinar kartlarına gerçek davetiye görselleri kondu.
- **Referans:** `109528f`, `17e0f0c`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-05 — Kurumsal metin/ton düzeltmeleri

- **Kapsam:** Site genelinde doğrulanamayan iddialar, açıklanmamış kısaltmalar ve mekanik/robotik ifadeler tarandı ve düzeltildi (kurumsal, resmi Türkçe ton — org. talimatına uygun).
- **Referans:** `fb3ec8e`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-04 — Başarı Öyküleri sayfası (13 vaka)

- **Kapsam:** Autodesk PDF arşivinden gerçek vaka çalışmaları derlenerek Başarı Öyküleri sayfası oluşturuldu ve ürün/çözüm/endüstri sayfalarına bağlandı; ilk 6 yazının ardından 6 yeni vaka daha eklendi (Limtaş, Epig Mimarlık, Demirce, Eltaş, Erdemgiller, BMC) — toplam 13 vaka.
- **Referans:** `3574ee8`, `f545604`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-03 — Fabrication ürün ailesi + Nastran/Point Layout/HP Monitör kararları + canonical düzeltmesi

- **Kapsam:** Fabrication ürün ailesi (CADmep/ESTmep/CAMduct) için ayrı sayfalar eklendi; daha önce açık kalan Nastran ve Point Layout kararları uygulandı. HP Monitör sayfasında hatalı canonical URL ayrıca düzeltildi.
- **Referans:** `0412dbf`, `3db504c`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-02 — VRED ürün sayfası

- **Kapsam:** VRED (Autodesk görselleştirme ürünü) için yeni ürün sayfası eklendi, resmi Autodesk ürün ikonları uygulandı, sayfaya özel OG/sosyal paylaşım görseli üretildi. Canlıya geçiş URL haritası bu yeni sayfayı yansıtacak şekilde güncellendi.
- **Referans:** `eed3abe`, `47d5f3c`, `bda1c35`.
- **Durum:** ✅ Tamamlandı.

### DK-2026-07-28-01 — Analitik/pazarlama entegrasyonları: GA4 düzeltmesi, Meta Pixel, LinkedIn Insight Tag, WhatsApp butonu

- **Kapsam:**
  1. **Kritik düzeltme:** Sitede kullanılan Google Analytics ölçüm ID'sinin sahte/geçersiz olduğu tespit edildi, gerçek GA4 ölçüm kimliğiyle değiştirildi. Çerez tercih panelinde "üretici yanılgısı" (yanlış varsayım) düzeltildi, analitik kategorisi varsayılan açık yapıldı.
  2. Meta Pixel entegre edildi; çerez onayına "Pazarlama" kategorisi eklendi (KVKK/rıza uyumu için).
  3. LinkedIn Insight Tag eklendi (Partner ID 516209).
  4. Sitenin tamamına (169 sayfa) sabit, görünür bir WhatsApp sohbet butonu eklendi.
- **Referans:** `0f9d427`, `95777ff`, `001e01d`, `dbccc91`, `2a3b0e3`.
- **Durum:** ✅ Tamamlandı. Meta Pixel ve LinkedIn Insight Tag ID'leri Onur tarafından 2026-07-29'da teyit edildi (kendisi bağlamış, doğru).

---

## 2026-07-26

### DK-2026-07-26-17 — Yeni sayfa: Adobe Creative Cloud, ilgili çözüm/endüstri/ürünlere entegre edildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "adobe creative cloud'a ait bir ürün sayfası yok bunu oluştur. https://www.adobe.com/tr/creativecloud.html oluştururken bu linki referans al. bunu sitemizdeki adobe sayfasına, ilgili çözümlere ve endüstrilere. diğer ürünlerdeki birlikte kullanılanlar bölümlerine de entegre et."
- **Araştırma:** Adobe'nin resmi Creative Cloud sayfası (adobe.com/tr/creativecloud.html) tarayıcıyla incelendi — 20+ uygulama (Photoshop, Illustrator, Premiere Pro, After Effects, InDesign, Lightroom, Audition, Acrobat Pro), Firefly AI entegrasyonu, 30.000+ Adobe Fonts, 1M+ Adobe Stock varlığı, bulut kütüphaneleri, sürekli güncelleme vurgusu not edildi. **Bireysel/Tek Uygulama planları ve fiyatları bilinçli olarak alınmadı** — Onur'un önceki talimatı gereği ("bireysel planları biz satmıyoruz") sayfa yalnızca Teams/Enterprise çerçevesinde yazıldı, hiçbir fiyat paylaşılmadı (org. politikası: teyitsiz fiyat/kampanya bilgisi resmi çıktıya konulmaz).
- **Yeni sayfa:** `cadbim_creative_cloud.html` — hero, 6 özellik kartı, 8 uygulamalık "Pakette Neler Var" grid'i, 3 kullanım senaryosu, Cadbim Farkı bloğu (VIP/ETLA, Admin Console, eğitim, 4 adım), ilgili çözüm/endüstri/ürün cross-sell'i, CTA. Diğer Adobe ürün sayfalarıyla birebir aynı CSS/yapı (Firefly sayfası temel alındı).
- **Entegrasyon:**
  - `cadbim_adobe.html`: Ürün Kataloğu'ndaki mevcut ama linksiz "Creative Cloud — Tüm Uygulamalar" placeholder kartı artık gerçek sayfaya bağlı.
  - `cadbim_urunler.html`: Aynı şekilde daha önce `cadbim_adobe.html`'e giden "Creative Cloud" kartı yeni sayfaya yönlendirildi.
  - Çözümler: `cadbim_yaratici_icerik.html`'deki "Creative Cloud" pili (önceden yanlışlıkla genel Adobe sayfasına gidiyordu) düzeltildi; `cadbim_gorsellestirme.html`'e yeni bir "Creative Cloud — render son rötuşu" pili eklendi.
  - Endüstriler: Yeni sayfanın kendi "Bu ürünle ilgili" bölümünde Medya & Eğlence, Mimarlık, Eğitim sektörlerine link verildi.
  - **Diğer ürünlerin "Birlikte Çalıştığı Ürünler" bölümleri (10 sayfa):** Photoshop, Illustrator, Premiere Pro, After Effects, InDesign, Lightroom, Adobe Express, Adobe Stock, Substance 3D ve Firefly sayfalarının hepsine "Creative Cloud" pili eklendi (Adobe Marka Sayfası pilinin hemen yanına).
- **Kapsam dışı bırakılan, ayrı göreve çevrilen bulgu:** sektor_medya.html'de Premiere Pro/After Effects/Photoshop kartlarının kendi sayfalarına değil genel cadbim_adobe.html'e gittiği fark edildi — bu, mevcut görevin kapsamı dışında olduğu için ayrı bir arka plan görevi olarak kaydedildi (task_68c5fbe8).
- **Doğrulama (localhost):** Yeni sayfa hatasız açılıyor, 14 görselin hiçbiri kırık değil; cadbim_adobe.html ve cadbim_urunler.html'deki Creative Cloud kartları artık yeni sayfaya gidiyor; 15 dokunulan dosyada div/a/section etiket dengesi tam; JSON-LD geçerli; og:image üretildi (`assets/og/cadbim_creative_cloud.png`) ve sayfanın kendi meta etiketlerine baştan doğru yazıldı.
- **Durum:** ✅ Adobe Creative Cloud artık kendi sayfasına sahip ve siteye tam entegre.

### DK-2026-07-26-16 — Adobe sayfası: yanlış rozet metni, dağınık özellik şeridi, satılmayan Bireysel plan kaldırıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, cadbim_adobe.html'in 3 ekran görüntüsünü paylaşıp: (1) hero'daki "Gold Reseller Partner" rozet metninin yanlış olduğunu, doğrusunun "Gold Reseller - Education - Commercial - Government" olması gerektiğini, yanındaki küçük (görünmeyen) Adobe Gold Reseller logosunun kaldırılmasını; (2) "20+ Creative uygulama / Firefly AI / Acrobat & e-İmza / Teams & Enterprise" şeridinin dağınık (3+1) göründüğünü, daha düzenli olmasını; (3) ayrıca "bireysel planları biz satmıyoruz, bireysel planla ilgili sitede bilgi olmasın" dedi.
- **1) Hero rozet + kırık logo:** `.hero-pill` metni "Gold Reseller Partner" → "Gold Reseller — Education, Commercial, Government" yapıldı (CADBİM'in gerçek 3 Adobe Gold Reseller yetkisi). Yanındaki `assets/img/emb-bc22fd8e82.png` (siyah metinli "Gold Reseller" rozeti, beyaz kartsız — koyu lacivert zemin üzerinde görünmüyordu) tamamen kaldırıldı.
- **2) Özellik şeridi (4 sayfa: Adobe, Autodesk, Chaos, UltiMaker):** `.hero-features` `display:flex;flex-wrap:wrap` → `display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))` yapıldı; mobilenav.js'teki genel satır-dengeleme fonksiyonuna (`v8→v9`) `.hero-features` selector'ü eklendi. Adobe/Chaos/UltiMaker'da 4 öğe → 2+2, Autodesk'te 5 öğe → 3+2 olarak dengeleniyor (önceden 3+1 idi).
- **3) Bireysel plan kaldırıldı:** "Creative Cloud — Bireysel" kartı (hero altındaki Lisans Planları gridinde) tamamen silindi; hero-sub ve CTA-strip paragraflarındaki "Bireysel, " ön eki kaldırıldı. Kalan planlar: Teams, Enterprise, Acrobat Pro.
- **Doğrulama (localhost, JS ile):** Rozet metni doğru, kırık img DOM'da yok; cadbim_adobe.html'de 4 öğe → [2,2], cadbim_autodesk.html'de 5 öğe → [3,2]; kart başlıkları artık yalnızca Teams/Enterprise/Acrobat Pro; "Bireysel" metni dosyada hiç geçmiyor; konsol hatası yok.
- **Durum:** ✅ Adobe sayfası: rozet doğru, özellik şeridi dengeli, Bireysel plan bilgisi tamamen kaldırıldı.

### DK-2026-07-26-15 — Tüm sayfalara sayfaya-özel og:image/twitter:image üretildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "tüm sayfaların google için gözüken başlıklarını, açıklamalarını ve sayfa görsellerini ayarla" → tarama sonrası tek eksik alan olarak "sayfa görselleri" (og:image) çıktı, tüm site tek bir genel `og-image.png` kullanıyordu. Onur "sayfaya özel benzersiz görseller" + "ürün logoları ve resimlerini kullan" seçeneklerini onayladı.
- **Kök kısıt:** Ürün logolarının çoğu (özellikle en büyük grup olan Autodesk ailesi) yalnızca SVG formatında; bu ortamda (Windows, Cairo/rsvg yok) SVG'yi PNG'ye çevirecek güvenilir bir yol bulunamadı (cairosvg/svglib native kütüphane arıyor; tarayıcı-canvas yöntemi bu sandboxta arka plan sekmesi olarak boğuluyor). Onur'un onayıyla **hibrit yaklaşım** uygulandı.
- **Üretim (Python/PIL, 156 sayfa):** Her sayfa için 1200×630 marka kimliğine uygun kart (koyu lacivert zemin + kategori rengine göre glow + ince grid çizgileri + CADBİM logosu + başlık/açıklama/kategori rozeti) otomatik üretildi:
  - **44 sayfada gerçek ürün fotoğrafı/logosu kullanıldı** (PNG/WEBP olarak zaten var olanlar): HP DesignJet/Z Workstation/ZBook aile fotoğrafları, UltiMaker donanım fotoğrafları, Chaos/Lumion/Adobe/Microsoft/Autodesk marka logoları, Anima/Meshmixer/Tinkercad/Trimble Connect ikonları.
  - **Kalan sayfalarda** (çoğunlukla SVG-only Autodesk ürünleri, çözüm/sektör/kurumsal sayfalar) temiz tipografi + kategori renk kodlaması (7 sektör rengi, 16 çözüm rengi, 8 marka rengi kendi paletiyle) korundu.
  - Kategori tanıma başlık metninden + dosya adından otomatik yapıldı (Autodesk/Adobe/HP/Chaos/UltiMaker/SketchUp/Lumion/Microsoft/Sektör/Çözüm/Kurumsal); birkaç istisna (AEC Collection, Trimble Connect, Sketch Sprint vb.) elle override edildi.
  - Görseller `assets/og/<sayfa-adı>.png` olarak kaydedildi (156 dosya, ~12MB toplam).
- **HTML güncelleme:** Her sayfada `<meta property="og:image">`, `<meta name="twitter:image">` (mevcut olan 50 sayfada) VE JSON-LD `"image"` alanı (103 sayfada, Product/Service şemasında) kendi görseline güncellendi. JSON-LD `"logo"` alanı (Organization şeması, 58 sayfa) kasıtlı olarak dokunulmadı — bu CADBİM'in kurumsal logosu, sayfaya özel değil.
- **Kapsam dışı bırakılan not:** cadbim_construction_cloud.html (noindex yönlendirme sayfası) hariç tutuldu — zaten arama motoruna kapalı.
- **Doğrulama:** 34 gerçek asset yolu Python ile mevcut olduğu doğrulandı; üretimden sonra tüm JSON-LD blokları `json.loads` ile geçerli bulundu; örnek görseller (HP DesignJet Z, Chaos, Autodesk Revit, UltiMaker) görsel olarak incelendi — metin/logo çakışması yok, Türkçe karakterler doğru; localhost'ta og:image URL'i fetch ile 200 OK + geçerli PNG doğrulandı.
- **Durum:** ✅ 156 sayfanın tamamında artık kendine özgü, sayfaya uygun bir sosyal/arama önizleme görseli var.

### DK-2026-07-26-14 — Mega menü: "Dijital İkiz & Üretim" iki ayrı gruba bölündü (6 kolon)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "mega menüde üretim ve dijital ikiz çözümlerini 2 farklı çözüm grubu olarak ayır ve göster. ana sayfadaki çözümler şeridi, çözümler ana sayfası ve mega menü çözümler aynı mantıkta eş değer olmalı."
- **Kök neden:** "Dijital İkiz" (cadbim_dijital_ikiz.html — AEC/yapı odaklı operasyonel twin, Autodesk Tandem) ile "Fabrika Tasarımı, CAM & İmalat, Eklemeli İmalat, Nesting" (üretim/imalat odaklı) tek bir "Dijital İkiz & Üretim" grubunda karışık gösteriliyordu; bunlar farklı disiplinler.
- **Çözüm (155 sayfa, mega menü):** Grup ikiye ayrıldı — **"Dijital İkiz"** (yalnızca Dijital İkiz) ve **"Üretim"** (Fabrika Tasarımı, CAM & İmalat, Eklemeli İmalat & 3D Baskı, Nesting). Mega menü artık 5 değil 6 kolon.
- **CSS (design-system.css, paylaşılan, v9→v10):** `.nav-mega-cols` `repeat(5,1fr)`→`repeat(6,1fr)`; `.nav-mega` genişliği 920px→1080px; 1200px kırılma noktası 1300px'e çekildi (6 kolon 3'e düşsün diye erken tetiklenmesin).
- **Kapsam notu:** "sanatsal_baski"/aktif-link varyasyonlu 5 dosya (cam, dijital_ikiz, eklemeli_imalat, fabrika_tasarimi, nesting) `class="active"` içerdiği için toplu perl replace'e uymadı, elle düzeltildi.
- **"Eş değer" notu:** cadbim_cozumler.html (çözümler ana sayfası) zaten tüm 17 çözümü tek düz gridde listeliyor, kategori başlığı yok — bu turda kategori gruplandırması eklenmedi (kapsam dışı bırakıldı, istenirse ayrı bir iş olarak yapılabilir). Ana sayfadaki soltabs widget'ı endüstri bazlı farklı bir eksende çalışıyor; Eklemeli İmalat'ın endüstri panellerindeki tutarlılığı bir önceki kayıtta (DK-13) zaten düzeltilmişti.
- **Doğrulama (localhost, JS ile):** index.html'de 6 nav-dd-label ("Tasarım & Mühendislik, Dijital İkiz, Üretim, Veri & Süreç Yönetimi, Görselleştirme & Gerçeklik, Sanatsal Baskı"); masaüstünde (1600px) grid 6 sütun/1080px; cadbim_dijital_ikiz.html'de active link doğru "Dijital İkiz" kolonunda; konsol hatası yok.
- **Durum:** ✅ Mega menüde Dijital İkiz ve Üretim artık ayrı gruplar.

### DK-2026-07-26-13 — Ana sayfa "Endüstrinize Göre Çözümler" widget'ında yanlış yerleşim düzeltildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "sanatsal baskı çözüm filtresinde eklemeli imalat ve 3d baskı çözümü gözüküyor bu yanlış, bunu doğru çözümün içine taşı, buradan kaldır."
- **Kök neden:** index.html'deki `.soltab-panel[data-panel="sanatsal_baski"]` içinde "Eklemeli İmalat & 3D Baskı" çözüm çipi yanlışlıkla listelenmiş (3D baskı ile sanatsal/fine-art baskının karıştırılması) — bu ikisi alakasız süreçler. Aynı zamanda bu çözümün gerçek endüstrileri olan Otomotiv ve Eğitim panellerinde hiç görünmüyordu (yalnızca Makine ve Havacılık'ta vardı).
- **Çözüm:** "Eklemeli İmalat & 3D Baskı" çipi `sanatsal_baski` panelinden kaldırıldı; `otomotiv` ve `egitim` panellerine eklendi (Makine ve Havacılık'ta zaten doğru şekilde vardı, dokunulmadı). Artık `cadbim_cozumler.html`'deki resmi endüstri eşleşmesiyle (Makine & Üretim, Otomotiv, Eğitim, Havacılık) birebir tutarlı.
- **Doğrulama (localhost, JS ile):** 5 panelin içeriği kontrol edildi — sanatsal_baski artık yalnızca "Sanatsal Baskı Atölyesi" + "HP DesignJet Fine Art" (2 çip); makine/otomotiv/egitim/havacilik'in hepsinde "Eklemeli İmalat & 3D Baskı" mevcut.
- **Durum:** ✅ Sanatsal Baskı filtresi artık yalnızca gerçekten ilgili çözümleri gösteriyor.

### DK-2026-07-26-12 — Ana sayfa marka şeridi: Microsoft için gerçek logo + Chaos/Microsoft sırası değişti

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "ana sayfadaki marka logolarının font büyüklüklerini eşit olacak şekilde logo boyutlarını ayarla" ve ardından "chaos ve microsoftun yerlerini değiştir."
- **Kök neden:** Microsoft kartında gerçek bir logo yoktu — `microsoft-partner-black.png` yalnızca düz siyah "Microsoft Partner" yazısıydı (placeholder), bu yüzden diğer 7 gerçek vektör logonun yanında görsel ağırlığı belirgin şekilde zayıf kalıyordu; asıl sorun boyut değil, logonun kendisiydi.
- **Çözüm:** `assets/logos/products/microsoft.svg`'deki resmi 4 renkli kare işaretini temel alarak PIL ile yeni **assets/logos/microsoft-logo.png** oluşturuldu (kareler + "Microsoft" kelimesi Segoe UI Light ile, şeffaf arkaplan, 669×201). index.html'de görsel kaynağı değiştirildi, `.cred-row1 img[src*="microsoft"]` boyut kuralı diğer logolarla tutarlı olacak şekilde `max-height:46px;max-width:84%` yapıldı.
- **Sıralama:** Onur'un isteğiyle Chaos ve Microsoft'un şeritteki yerleri değiştirildi — yeni sıra: Autodesk, Adobe, HP, Chaos (1. satır) / SketchUp, Lumion, UltiMaker, Microsoft (2. satır).
- **Doğrulama:** Yeni `microsoft-logo.png` dosyası `fetch` ile 200 OK + geçerli PNG (7KB) doğrulandı; DOM sırası JS ile kontrol edildi (Autodesk→Adobe→HP→Chaos→SketchUp→Lumion→UltiMaker→Microsoft). (Not: Browser pane bu oturumda arka planda/gizli kaldığı için `loading="lazy"` görseller hiç yüklenmedi — bu ortam kısıtı, canlı sitede normal şekilde çalışır.)
- **Durum:** ✅ Microsoft artık gerçek bir logo kullanıyor, sıra Onur'un istediği gibi.

### DK-2026-07-26-11 — Çözüm sayfaları sonu: "kullanılan ürünler / endüstriler" bölümleri yeniden tasarlandı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, canlı sitedeki ekran görüntüsünü paylaşıp: "çözümler sayfalarının sonlarındaki bu 2 bölümün görüntüsü hoşuma gitmedi, daha güzel bir düzen olsun."
- **Sorun:** İki ayrı "cross" kartı ("Bu çözümde kullanılan Cadbim ürünleri" ve "Bu çözüm hangi endüstrilerde kullanılıyor") art arda tam genişlikte, aralarında büyük boş dikey boşlukla, içindeki birkaç pil'e kıyasla gereksiz büyük/boş görünüyordu.
- **Çözüm (16 çözüm sayfası):**
  - HTML: iki ayrı `<section>` içindeki `.cross` kartları tek bir `<section>` içinde yeni `.cross-grid` (2 sütunlu grid, masaüstünde yan yana, ≤900px'te tek sütun) ile birleştirildi — büyük dikey boşluk kayboldu, iki kart artık bir bütün gibi görünüyor.
  - CSS: `.cross` arka planı düz `rgba(0,200,240,0.04)` yerine ince bir köşegen gradient (`linear-gradient(160deg,...)` + `var(--navy3)`) aldı; `.cp` pilleri biraz daha sıkı padding + hover'da hafif yukarı kalkma (`translateY(-2px)`) + hafif cyan arka plan aldı; `.cp i` ikonları artık çıplak glif değil, 30×30px yuvarlak köşeli renkli rozet (badge) içinde gösteriliyor — daha modern/profesyonel bir kart hissi.
  - `cadbim_nesting.html`'de yalnızca tek cross bloğu olduğu için birleştirme uygulanmadı (zaten tek sütun, gereksiz), yalnızca yeni `.cp`/`.cross` görsel stili uygulandı.
- **Doğrulama (localhost, JS ile):** cadbim_bim.html — `.cross-grid` 2×580px sütun (masaüstü), 700px'te 1 sütuna düşüyor; `.cp i` rozetleri 30×30px, `rgba(0,200,240,0.12)` arka plan, 9px köşe; `.cpills` satır dengelemesi yeni dar sütun genişliğinde de doğru çalışıyor (8 öğe → 2 sütun → 4 satır×2, hepsi eşit). div/section etiket dengesi 16 dosyada da tam, konsol hatası yok.
- **Durum:** ✅ Çözüm sayfası sonu artık tek, yan yana iki sütunlu, daha kompakt ve modern bir blok.

### DK-2026-07-26-10 — Satır dengeleme .grid.g2/g3/g4 ve inline "İyi Uygulamalar" grid'lerine genişletildi (mobilenav.js v8)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, cadbim_bim.html'in canlı ekran görüntüsünü paylaşıp "Neler Yapabiliriz?" (4+2 dağılan 6 kart) ve "Projelerde Uyguladığımız Standartlar" (4+2 dağılan 6 kutu) bölümlerinin bir önceki satır-dengeleme düzeltmesinden etkilenmediğini bildirdi: "bu sayfada ss verdiğim alanlarda bir önceki promptta söylediğim değişiklikler olmamış... bunu tüm çözüm sayfaları için yap."
- **Kök neden:** Önceki düzeltme yalnızca `.cpills` selector'üne bakıyordu; "Neler Yapabiliriz?" kartları `.grid.g3` class'ını, "İyi Uygulamalar" kutuları ise class'sız, tamamen inline `style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))"` kullanıyor — hiçbiri `.cpills` değil.
- **Çözüm (mobilenav.js, v7→v8):** Satır dengeleme fonksiyonu genelleştirildi — artık `.cpills`, `.grid.g2/.g3/.g4` VE `[style*="minmax(280px,1fr)"]` inline grid'lerinin hepsini tarıyor. Her grid'in ilk ölçümde doğal `grid-template-columns` değeri (class'tan mı geliyor, inline'dan mı fark etmeksizin `element.style.gridTemplateColumns`'un o anki hali) bir WeakMap'e önbelleğe alınıyor; resize'da o doğal değere dönülüp yeniden ölçülüyor, böylece sabit "200px" gibi bir varsayım hardcode edilmek zorunda kalmıyor — her grid kendi min-width'ine göre doğru ölçülüyor.
- **Kapsam:** Paylaşılan JS dosyası olduğu için otomatik olarak tüm 16 çözüm sayfasında (ve aynı `.grid.g3`/inline pattern'i kullanan diğer sayfalarda) devreye giriyor; versiyon 155 dosyada `mobilenav.js?v=7`→`v=8` güncellendi.
- **Doğrulama (localhost, resize+JS ile):** cadbim_bim.html — `.grid.g3` (6 kart) → 3 sütun → [3,3]; inline "İyi Uygulamalar" grid'i (6 kutu) → 3 sütun → [3,3]; `.cpills` (8 ve 2 öğe) hâlâ doğru ([4,4] ve [2]). cadbim_gorsellestirme.html — `.grid.g3` → [3,3]. Konsol hatası yok.
- **Durum:** ✅ Çözüm sayfalarındaki üç farklı grid türü de (cpills, grid g3, inline pratikler) artık aynı satır-dengeleme kuralına tabi.

### DK-2026-07-26-09 — Eşit-kutu + satır dengeleme kuralı site geneline yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "son verdiğim 2 promptu bütün sayfalarda bir stil kuralı olarak uygula" (eşit büyüklükte kutucuklar + satır dengeleme kuralları yalnızca 16 çözüm sayfasına uygulanmıştı).
- **Kapsam genişletmesi:** `.cpills`/`.cp` bileşenini kullanan ama hâlâ eski `display:flex;flex-wrap:wrap` tanımını taşıyan **75 sayfa** (tüm HP DesignJet/ürün ailesi sayfaları, Adobe/Chaos/UltiMaker/SketchUp/Lumion ürün sayfaları, sektör sayfaları — sektor_mimari/insaat/makine/otomotiv/egitim/havacilik — hakkımızda, iletişim, danışmanlık vb.) tarandı; `.cpills` → `display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))`, `.cp` → `min-height:56px` + `padding:14px 16px` + `line-height:1.4`, `.cp i` → `flex-shrink:0` olarak güncellendi. İki farklı `.cp` renk varyantı (rgba literal / CSS değişkeni) ayrı ayrı eşleştirilip güncellendi.
- **Satır dengeleme (mobilenav.js v7):** Zaten paylaşılan dosyada olduğu için CSS artık `display:grid` olan her sayfada otomatik devreye giriyor — ayrıca bir JS değişikliği gerekmedi.
- **Sonuç:** Artık 91 sayfada `.cpills` hem eşit boyutlu kutucuklar hem de satır-dengeli (çift sayıda eşit, tek sayıda ilk satır 1 fazla, küçük sayılar tek satırda) görünüyor.
- **Doğrulama (localhost, JS ile):** cadbim_designjet.html — 6 öğe → 3 sütun → satırlar [3,3]. sektor_mimari.html — 3 öğe → tek satır [3]. 91 dosyanın tamamında `.cpills{display:grid;...}` + `.cp` içinde `min-height:56px` eşleşmesi doğrulandı (eksik kalan yok), konsol hatası yok.
- **Durum:** ✅ Eşit-kutu + satır dengeleme kuralı artık site genelinde tutarlı bir stil kuralı.

### DK-2026-07-26-08 — .cpills grid'i satır bazında dengelendi (mobilenav.js v7)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, bir önceki eşit-kutu düzeltmesinin ekran görüntüsünü paylaşıp 8 öğenin 5+3 dağıldığını gösterdi: "bu sayfalarda kutucuk sayıları 2 satır varsa eşit miktarda ilk satır 5 ikinci satır 3 kutu olmasın ilk satır 4 ikinci satır 4 olsun. eğer kutu sayısı tek sayı ise ilk satır ikinci satırdan 1 fazla kutucuk sahibi olsun."
- **Kök neden:** `.cpills{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}` yalnızca konteyner genişliğine göre kaç sütun sığdığını hesaplıyor, toplam öğe sayısını dikkate almıyor — 8 öğe + container'a sığan 5 sütun → son satırda 3 öğe kalıyor.
- **Çözüm (mobilenav.js, paylaşılan dosya, v6→v7):** Sayfa yüklendiğinde/pencere yeniden boyutlandığında her `.cpills` için: önce auto-fill ile konteynere sığan maksimum sütun sayısı (`maxCols`) ölçülüyor, satır sayısı `rows=ceil(n/maxCols)` hesaplanıyor, ardından sütun sayısı `cols=ceil(n/rows)` olarak yeniden ayarlanıyor (`repeat(cols,1fr)`). Satır-öncelikli (row-major) grid doldurma sırası nedeniyle ilk satır otomatik olarak `cols` kadar (eşit ya da tek sayıda bir fazla), son satır kalanı alıyor — ör. n=8,maxCols=5 → rows=2,cols=4 → 4+4; n=9 → rows=2,cols=5 → 5+4; n=2,3 (tek satıra sığan küçük sayılar) tek satırda eşit genişlikte kalıyor, gereksiz yere 2 satıra bölünmüyor.
- **Kapsam:** mobilenav.js paylaşılan dosya olduğu için düzeltme yalnızca `.cpills` class'ı taşıyan tüm sayfalarda otomatik devreye giriyor (16 çözüm sayfası + `.cpills` kullanan sektör sayfaları); versiyon 155 dosyada `mobilenav.js?v=6`→`v=7` olarak güncellendi.
- **Doğrulama (localhost, resize+JS ile):** cadbim_bim.html — 8 öğe → 4 sütun → satırlar [4,4]; 2 öğe → 2 sütun → tek satır [2]. cadbim_yaratici_icerik.html — 9 öğe → 5 sütun → satırlar [5,4] (ilk satır bir fazla); 3 öğe → tek satır [3]. Konsol hatası yok.
- **Durum:** ✅ `.cpills` grid'i artık satır bazında dengeli; tek sayıda öğede ilk satır bir fazla alıyor.

### DK-2026-07-26-07 — Çözüm sayfaları: hero'daki erken CTA kaldırıldı + cross kutuları eşit boyuta getirildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur, cadbim_bim.html'in canlı ekran görüntüsünü paylaşarak: "çözümler sayfasında cta sı sayfa sonunda olmalı, örnek BIM çözümünde teklif & danışmanlık ctası sayfa sonunda olmalı" ve ardından "bunu tüm çözümler için uygula" dedi. Ayrı bir mesajda çözüm sonu "Bu çözümde kullanılan ürünler / hangi endüstrilerde kullanılıyor" kutularının düzensiz (değişken genişlikte) görünümünü beğenmediğini belirtip "eşit büyüklükte kutucuklar" istedi.
- **1) Hero CTA kaldırma (15 standart çözüm sayfası):** BIM, Simülasyon & Analiz, Tolerans Analizi, Tasarım Otomasyonu, Dijital İkiz, Fabrika Tasarımı, CAM & İmalat, Eklemeli İmalat, Nesting, PLM, PDM, İnşaat Proje Yönetimi, Görselleştirme & Render, Yaratıcı İçerik & Tasarım, Gerçeklik Yakalama & Tarama — hero'daki "Teklif & Danışmanlık" butonu (sayfa sonundaki cta-strip'in birebir tekrarıydı) kaldırıldı; hero artık yalnızca tanıtım metni + rozet, dönüşüm çağrısı yalnızca sayfa sonunda.
- **cadbim_dijital_donusum.html (özel durum):** Hero'da iki buton vardı — "Dijital Dönüşüm Danışmanlığı" (iletişime giden, tekrar eden CTA) kaldırıldı; "Çözüm Haritasını İncele" (#harita'ya kaydıran sayfa-içi gezinme) korundu, CTA değil.
- **cadbim_sanatsal_baski.html hariç tutuldu:** Bu sayfa bambaşka bir bespoke tasarım — hero CTA'ları zaten sayfa-içi anchor'lar (#iletisim, #isler), tekrar eden bir "sayfa sonu CTA" sorunu yok.
- **2) Eşit boy kutucuklar (16 çözüm sayfası, yukarıdaki 15 + dijital_donusum):** `.cpills` `display:flex;flex-wrap:wrap` → `display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))`; `.cp` kutularına `min-height:56px` + `padding:14px 16px` eklendi. Sonuç: "Bu çözümde kullanılan ürünler" ve "hangi endüstrilerde kullanılıyor" pilleri artık düzensiz pill değil, tek tip genişlikte kutucuk gridi.
- **Doğrulama (localhost, JS ile):** cadbim_bim.html — hero'da 0 buton, cta-strip sonda sağlam (2 buton); `.cpills` grid, 8 ürün kutusu da 262px eşit genişlikte. cadbim_dijital_donusum.html — hero'da yalnızca "Çözüm Haritasını İncele" kaldı. 16 dosyada div/a/section etiket dengesi tam, konsol hatası yok.
- **Durum:** ✅ Çözüm sayfalarında CTA yalnızca sayfa sonunda; cross kutuları eşit boyutlu grid.

### DK-2026-07-26-06 — Endüstriler hub'ına "Çözüm & Ürün Haritası" eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur: "endüstri sayfasında o endüstrideki çözümler ve o çözümdeki ürünleri göster."
- **Çözüm:** `cadbim_endustriler.html`'e 7 endüstri kartının altına yeni bir bölüm eklendi: 7 sekmeli (`.ind-tab-btn`) endüstri seçici + her sekmede o endüstriye ait çözüm blokları (`.ind-sol-block`), her blokta çözümün adı + link + içindeki ürünler etiket olarak listeleniyor.
- **Veri kaynağı:** Endüstri↔çözüm eşleşmeleri uydurulmadı — her `sektor_*.html` sayfasının kendi "Bu endüstride kullanılan çözümler" (cross) + "İlgili Çözüm Alanları" (newsol) bölümlerinden derlendi (ör. Mimarlık: BIM, Tasarım Otomasyonu, Görselleştirme & Render, Gerçeklik Yakalama, İnşaat Proje Yönetimi, Yaratıcı İçerik & Tasarım). Çözüm başına ürün etiketleri `cadbim_cozumler.html`'deki `sol-tag` listeleriyle birebir aynı. Sonuç: Mimarlık 6, İnşaat 5, Makine 10, Otomotiv 9, Medya 2, Eğitim 3, Havacılık 4 çözüm bloğu.
- **Doğrulama (localhost, JS ile):** 7 sekme/7 panel mevcut; varsayılan aktif "Mimarlık" 6 blok gösteriyor; "Makine & Üretim" sekmesine tıklanınca panel 10 bloğa (PLM ilk sırada) geçiyor; div/a/button etiket dengesi tam (130/130, 97/97, 7/7); konsol hatası yok.
- **Durum:** ✅ Endüstriler hub'ı artık her sektör için çözüm+ürün detayını sekmeli haritada gösteriyor.

### DK-2026-07-26-05 — Endüstriler ana sayfası (hub) oluşturuldu

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur bildirdi: "endüstriler ana sayfası yok, menüden basınca önce mimarlık sayfasına atıyor."
- **Kök neden:** Nav'daki "Endüstriler" üst-seviye linki (ve ana sayfadaki hero "Endüstriler" butonu) doğrudan `sektor_mimari.html`'e gidiyordu — ayrı bir "tüm endüstriler" liste/tanıtım sayfası hiç yoktu; kullanıcı menüden tıklayınca yanlışlıkla Mimarlık sektör sayfasına düşüyordu.
- **Çözüm:** `cadbim_cozumler.html` (Çözümler hub'ı) kalıbında yeni **cadbim_endustriler.html** oluşturuldu — hero + 7 endüstri kartı (Mimarlık, İnşaat & Altyapı, Makine & Üretim, Otomotiv, Medya & Eğlence, Eğitim, Havacılık & Savunma), her biri ilgili `sektor_*.html` sayfasına linkli, ikon/renk kodları mevcut sektör sayfalarındaki tabs-nav ile birebir eşleşiyor.
- **Site geneli link düzeltmesi (155 dosya):** Nav'daki "Endüstriler" linki → `cadbim_endustriler.html` (154 sayfa + yeni sayfanın kendi nav'ı); 7 `sektor_*.html` sayfasının nav'ındaki `class="active"` varyantı da düzeltildi; bu 7 sayfanın breadcrumb'ındaki statik `<span>Endüstriler</span>` artık gerçek bir link (`<a href="cadbim_endustriler.html">`); index.html hero'daki "Endüstriler" butonu da hub'a yönlendirildi.
- **Doğrulama (localhost):** Nav'dan "Endüstriler" tıklanınca yeni hub sayfası açılıyor, 7 kart da doğru sektör sayfasına gidiyor; sektör sayfasında breadcrumb'daki "Endüstriler" artık tıklanabilir ve hub'a dönüyor; konsol hatası yok; div/a etiket dengesi yeni sayfada 41/41 ve 58/58.
- **Durum:** ✅ Endüstriler artık kendi ana/hub sayfasına sahip; menüden basınca doğrudan Mimarlık'a düşme sorunu giderildi.

### DK-2026-07-26-03 — Filtre hatası, Autodesk/Adobe/DesignJet düzenlemeleri, Sanatsal Baskı entegrasyonu

- **Yapan:** Onur Bozok + Claude (PDM asistanı) — canlı site üzerinden gelen 6 ayrı bulgu/istek.
- **Kök neden bulundu — site geneli filtre görünmezlik hatası:** `mobilenav.js`'deki scroll-reveal motoru `.pgrid .pcard` dahil her elemana `opacity:0` veriyor, yalnızca scroll/resize event'inde `rv-in` ekliyordu. Ürün filtresi tıklaması scroll tetiklemediğinden, filtrelenip yeniden görünür olan kartlar opacity:0'da kalabiliyordu — "filtreler çalışmıyor" hissi. **Düzeltme:** reveal motoruna `MutationObserver` eklendi (style/class değişikliğinde yeniden tarama). TÜM filtrelenebilir kataloglarda (autodesk/adobe/hp/chaos/ultimaker/sketchup/urunler/sektor) aynı hatayı çözüyor. `mobilenav.js` v5→v6, 154 sayfada güncellendi.
- **cadbim_urunler.html:** Autodesk şeridinde uzmanlık-listeli dikey logo → sade yatay logo (dar şerit alanına uygun); HP şeridinde partner rozeti → standart HP logosu; HP Build Workspace kartına logo eklendi (jenerik bulut ikonu yerine); ürün logolarının etrafındaki renkli kutu kaldırıldı, logolar büyütüldü (42px) ve metinle hizalandı — TÜM marka kartlarında.
- **cadbim_autodesk.html:** "Cadbim Farkı" şeridi (6 kutu) tek satıra alındı (feats grid minmax 220→170px) ve Koleksiyonlar'ın üstüne, hero'nun hemen ardına taşındı; section-alt/section alternasyonu yeniden dengelendi.
- **cadbim_adobe.html:** Hero'daki elle çizilmiş sahte üçgen logo → gerçek Adobe logosu; "Creative Cloud" ibaresi (sayfanın CC'ye özel olduğu izlenimi veriyordu) → "Tüm Ürünler & Lisanslama"; title/meta/OG/JSON-LD genel Adobe sayfası çerçevesine güncellendi.
- **cadbim_designjet.html:** "Neden Cadbim?" + "Cadbim Farkı" şeritleri Katalog'un üstüne taşındı. Sayfa sonu "İlgili ürünler ve çözümler" bloğu DesignJet ailesinin kendi alt sayfalarını tekrar listeliyordu (zaten yukarıda gösteriliyor) → "Birlikte kullanılan ürünler ve çözümler" oldu, içerik DesignJet DIŞI gerçek tamamlayıcılara değişti: AutoCAD, Revit, HP Z Workstation, Adobe Acrobat Pro, HP Build Workspace, Sanatsal Baskı Atölyesi.
- **Sanatsal Baskı Atölyesi çözüm entegrasyonu:** Her sayfanın "Çözümler" mega-menüsüne (Görselleştirme & Gerçeklik kolonu) eklendi — 154 sayfa. Ana sayfada Mimarlık ve Medya & Eğlence çözüm sekmesi panellerine chip eklendi; 3D çözüm görselleştiricisine (`cozumSvg`) alias tanımlandı. `cadbim_gorsellestirme.html` ve `cadbim_yaratici_icerik.html`'in "kullanıldığı ürünler" çapraz-satış listelerine eklendi.
- **Doğrulama:** Her değişiklik için ayrı ayrı — section/div/a etiket dengeleri 0 fark, yeni asset/link fetch ile 200 doğrulandı, reveal-fix senaryosu simüle edilerek (mock getBoundingClientRect + MutationObserver) çalıştığı kanıtlandı.
- **Durum:** ✅ 6 commit halinde tamamlandı ve yayınlandı (438bef7, e3c999e, 3f2d98d, 2a3fa02, f1590e9, fd1120d).

### DK-2026-07-26-02 — Ürünler sayfası: marka logoları düzeltmesi (Autodesk/Adobe/HP/Chaos/UltiMaker/SketchUp/Lumion)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur'un 7 maddelik logo denetim talebi.
- **Autodesk:** `cadbim_urunler.html` şeridindeki jenerik `autodesk-primary-white.svg` → resmi **Autodesk Gold Partner** tam-liste beyaz logosu (`autodesk-gold-partner-full-white.png`, DK-21-21'de kullanılan asset).
- **Adobe:** Acrobat Pro kartındaki yanlış jenerik `adobe.png` ikonu → doğru `products/acrobat.svg` (cadbim_adobe.html kataloğuyla artık tutarlı).
- **HP:** `cadbim_urunler.html` ve `cadbim_hp.html`'de 6 ürün grubu kartının tamamı jenerik `hp-blue.png`/`hp-logo.png` kullanıyordu. DesignJet T/XL/Z için mevcut şeffaf ürün fotoğrafları (t1700/xl3600/z9pro) kullanıldı; **Z Workstation** ve **ZBook** için HP'nin resmi nav-menü temsilci görselleri indirilip (rembg ile) şeffaflaştırıldı (`assets/products/hp-z-workstation-group.png`, `hp-zbook-group.png`); Build Workspace (bulut/yazılım, fotoğrafı yok) ayırt edici `ti-cloud-share` ikonuna geçti. **Sıralama:** her iki sayfada da DesignJet → Workstations → Build Workspace olacak şekilde düzeltildi (cadbim_hp.html'de Workstations bölümü önceden Designjet'ten önceydi).
- **Chaos:** Onur'un ilettiği resmi Chaos logo kitlerinden (`Downloads/OneDrive_1_26.07.2026`) her ürüne kendi logosu çıkarıldı — V-Ray ve Vantage için gerçek ürün ikonları, Veras için kırpılmış rozet, Corona/Enscape/Phoenix/Anima/Cosmos için Chaos'un kendi marka renkli "chaos" wordmark sistemi (her ürünün resmi aksan rengi). Chaos ana sayfasındaki (`cadbim_chaos.html`) elle çizilmiş sahte "C/CHAOS" SVG rozeti gerçek Chaos logosuyla değiştirildi. Her pico'nun arka plan rengi ürünün resmi aksan rengine güncellendi.
- **UltiMaker:** ultimaker.com'un resmi nav-menü görselleri indirilip şeffaflaştırıldı — S Serisi (S8/S7/S5/S3 ortak, gerçekte aynı gövde), Factor 4, Method XL, Sketch Sprint, Cura, Digital Factory artık kendi gerçek ürün görselleriyle (`assets/products/ultimaker-*.png`).
- **SketchUp:** Go/Pro/Studio yalnızca lisans kademeleri (Trimble ayrı bir logo yayınlamıyor, doğrulandı) — ikon aynı kalırken her kademenin pico arka planı kendi rozet rengine (GO=gri, PRO=cyan, STUDIO=mor) boyandı, en azından renk koduyla ayırt edilir hale geldi.
- **Lumion:** lumion.com'da her ürünün (Pro/View/Cloud) kendi logosu bulundu (storyblok CDN), kırpılıp şeffaflaştırıldı; `cadbim_urunler.html`'de Lumion/View/Cloud artık kendi logolarıyla (Studio bundle'ı için ayrı resmi logo yok, temel marka işareti korundu).
- **Doğrulama:** Tüm yeni asset'ler (23 dosya) tarayıcıda fetch ile 200 doğrulandı; section/div dengeleri 7 dosyada 0 fark; kırık link/asset taraması 0.
- **Durum:** ✅ Tamamlandı ve doğrulandı.

### DK-2026-07-26-01 — Site geneli IA denetimi: "içerik/ürünler önce, ilgili+CTA sonra" kuralı (marka + endüstri sayfaları)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Önceki session'da DK-2026-07-20-08'de "site geneli denetle" kararı açık kalmıştı; bu turda tamamlandı.
- **Bulgu:** DesignJet'te (DK-08) ve bazı sayfalarda uygulanan "içerik/ürünler önce, ilgili linkler + CTA sonra" mimarisi 11 sayfada ihlal ediliyordu — çapraz-satış/"ilgili" bloğu hero'nun HEMEN ardında, asıl ürün kataloğu/açıklayıcı içerikten ÖNCE duruyordu.
- **Marka sayfaları (5):** adobe, chaos, ultimaker, sketchup, lumion. "X ile birlikte çalışan/sıkça tercih edilenler" bloğu (`.cross`) hero'nun ardından CTA'nın hemen öncesine taşındı. Referans: autodesk ve microsoft sayfaları zaten doğru sıradaydı (dokunulmadı); hp de doğruydu.
- **Endüstri sayfaları (6):** sektor_insaat, sektor_makine, sektor_mimari, sektor_otomotiv — "Bu endüstride kullanılan Cadbim çözümleri" bloğu ürün kataloğundan (`.solutions`) önce duruyordu → kataloğun sonrasına, "İlgili Çözüm Alanları" (`data-newsol`) bloğunun hemen öncesine taşındı. sektor_egitim, sektor_havacilik — ikinci "İlgili çözüm alanları" bloğu "Neler Sunuyoruz" ve "Çalışma Modelimiz" bölümlerinden önce duruyordu → CTA'nın hemen öncesine taşındı (ürün kataloğu bloğu zaten doğru yerdeydi, dokunulmadı). sektor_medya'da bu blok hiç yoktu — değişiklik gerekmedi.
- **Çözüm sayfaları (bim/plm/cam/dijital_ikiz/nesting/insaat_yonetimi/gerceklik_yakalama/simulasyon/pdm):** denetlendi, zaten doğru sırada (önceki turda düzeltilmiş) — değişiklik gerekmedi.
- **Not:** sketchup ve lumion'da cross-sell içeriğiyle sayfa sonundaki "Entegrasyonlar" bölümü kısmen örtüşüyor (SketchUp/Chaos/Revit gibi ortak isimler) ama bilinçli olarak silinmedi — yalnızca sıralama düzeltildi, içerik kararı bu turun kapsamı dışında bırakıldı.
- **Doğrulama:** 11 dosyada section/div dengesi 0 fark; localhost'ta iki örnek sayfa (adobe, sektor_mimari) DOM sırası JS ile doğrulandı; konsol hatası 0; yatay taşma 0; kırık link taraması 0 (yalnızca site genelinde zaten var olan kök-göreli `/favicon.svg` yanlış pozitifi, ilgisiz).
- **Durum:** ✅ Tamamlandı ve doğrulandı.

## 2026-07-22

### DK-2026-07-22-08 — Yeni DesignJet modelleri: T1600 / T2600 MFP Plus Edition (Build Connected)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kaynak:** Onur'un ilettiği resmi HP pazarlama toolkit'i (T1600/T2600 Plus Edition | Build Connected, Nisan 2026 verileri).
- **Yeni sayfalar (2):** `cadbim_designjet_t1600_plus.html` (/designjet-t1600-plus) ve `cadbim_designjet_t2600_plus.html` (/designjet-t2600-plus) — baz sayfalardan cerrahî klon; başlık/meta/JSON-LD, YENİ rozeti, h1+hero, ürün bölümü (broşür yerine **HP Build Workspace** sayfa linki), 6'şar özellik kartı, varyant çipleri (dr Plus dahil), ilgili-ürün pilleri ve CTA yeniden yazıldı. Kaynak-dipnot satırı eklendi (180 baskı/saat = Hızlı mod + Economode; istifleme karşılaştırması 12.000 $ altı, Nisan 2026).
- **Öne çıkanlar:** T1600 Plus — Build Workspace bulut iş akışı, saatte 180 baskı, tam entegre 100 sayfa istifleyici, gömülü Adobe PDF Print Engine, Wolf Pro Security, dr çift rulo. T2600 MFP Plus — ön panelden buluta tarama, **AI vektörizasyon** (raster→CAD, ilk bulut çözümü), **QR bağlantılı sürüm kontrolü** + mobil tarama.
- **Bağlantılar:** baz T1600/T2600 sayfalarına "YENİ — Plus Edition çıktı" duyuru şeridi; hp.html kataloğuna 2 kart (DesignJet T filtresi 9→11, toplam 22→24); T serisi sayfasına 2 pill + tanıtım cümlesi; sitemap +2 URL; mobilenav aramasına 2 kayıt.
- **Bonus düzeltme:** 23 DesignJet sayfasının breadcrumb'ında yapışmış hatalı nav linkleri (HP Workstations / Build Workspace) ve mükerrer "DesignJet" halkası temizlendi.
- **Doğrulama:** localhost — iki sayfada 0 kırık link/asset, YENİ rozeti, 6 özellik kartı, 3 varyant çipi, video, canonical doğru; hp katalog +2 ve "24 ürün"; baz sayfa şeritleri yerinde; div/section dengeleri 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-07 — Atölye şeridi v2: tam genişlik + palet uyumu

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Onur'un iki maddesi:**
  1. **Tam genişlik, çerçevesiz:** Yuvarlatılmış degrade çerçeveli kart kaldırıldı; şerit artık section sarmalayıcısız, kenardan kenara tam bleed bir bant (üst/alt ince w10 çizgiler, section-alt dilinde navy2 zemin + cyan ışımalar, hover'da navy3).
  2. **Palet denetimi:** Ana sayfanın gerçek paleti ölçüldü — yalnız lacivert ailesi + cyan ailesi (#00c8f0/#0ea5e9/#38bdf8) + nötr açık (#e6ebf2). Şeritteki 5 yabancı renk (viyole #8b7cf7, magenta #f26bd8, mavi #3d78ff...) doğrulandı: palette YOK → tamamı temizlendi. Degrade çerçeve/em/tag/marquee vurguları cyan'a; **halka panelleri** palet-içi "baskı" görsellerine yeniden boyandı (cyan güneş, sis, s/b çizgiler, cyan konik, mimari çizgiler, nötr kağıt) — sıcak/viyole tonlar tamamen çıktı.
- **Doğrulama:** Tam bleed (sol 0, genişlik = içerik genişliği 1265), border-radius 0, em/tag cyan (rgb 0,200,240), 6 panel, dosyada yabancı renk kalıntısı 0, taşma 0, div/section dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-06 — Ana sayfaya Sanatsal Baskı Atölyesi şeridi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** index.html'de Çözümler ile Fark (Neden Cadbim) bölümleri arasına, atölye sayfasına yönlendiren tıklanabilir tanıtım şeridi. Ana sayfanın lacivert/cyan diline oturan ama atölye kimliğini taşıyan tasarım:
  - **İridesan degrade çerçeve** (cyan→viyole→magenta, padding-box/border-box tekniği) + köşe ışımaları; hover'da yükselme + viyole gölge.
  - **Mini 3D halka:** atölye sayfasındaki galeri halkasının 6 panelli kompakt versiyonu (saf CSS, 22s dönüş, -10° eğim; mobilde gizli).
  - **Akan kelime şeridi:** alt kenarda GICLÉE · KANVAS · FOTOBLOK · ÇERÇEVE · SERGİ BASKISI · REPRODÜKSİYON (26s döngü).
  - Metin: "Fotoğrafınız, duvarda bir *esere* dönüşür." (degrade em) + rötuş/finisaj özeti + "Atölyeyi keşfedin" oku.
  - Ana sayfanın mevcut `.reveal` animasyon sistemine bağlandı; tüm hareket `prefers-reduced-motion` korumalı.
- **Doğrulama:** localhost 1280/375 — konum doğru (Çözümler→şerit→Fark), hedef link doğru, 6 panel + `aringDon` animasyonu, 12 marquee span, 1169×312 yerleşim, mobilde halka gizli/335px genişlik, yatay taşma 0, div dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-05 — Sanatsal Baskı R2: tek-ekran hero, ray okları, 3+3 finisaj, 3D galeri halkası

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Onur'un 4 maddesi:**
  1. **Hero her cihazda tek ekran:** Display tipografisi genişlik+yükseklik duyarlı ölçeğe alındı — `clamp(2.5rem, min(11.5vw, 15vh), 10.5rem)`; tüm dikey boşluklar (hero padding, h1/h-bottom/h-meta marjları, buton yükseklikleri) vh-clamp'e çevrildi. Doğrulama: 1366×700 → 668/700, 1600×860 → 797/860, 375×812 → 761/812 — hepsi sığıyor.
  2. **Yüzey rayına ok düğmeleri:** başlık satırına ←/→ dairesel butonlar; kart genişliği+16px adımla smooth kaydırma + smooth'un çalışmadığı ortamlar için 320ms zamanlayıcı güvencesi (doğrudan scrollLeft). İki yön de test edildi.
  3. **Finisaj 3+3:** auto-fit yerine sabit `repeat(3,1fr)` (≤900px: 2 sütun, ≤540px: 1). Doğrulama: 2 satır × 3 kutu.
  4. **Girişe 3D animasyon:** Saf CSS **3D galeri halkası** — 8 "baskı paneli" (gradient eserler) `preserve-3d` + `rotateY(n·45°) translateZ()` ile halka dizilimi, 34s sonsuz dönüş, -8° eğim, imleçle ±8° paralaks (pointer:fine + hareket açıkken). Kütüphanesiz, `prefers-reduced-motion`'da statik yelpaze, ≤1180px'te gizli.
- **Ek düzeltme:** 3D panellerin projeksiyonu scrollable alanı genişletiyordu → `html{overflow-x:clip}`. Başlık metni ile halka çakışması gerçek metin genişliğiyle ölçüldü: 1366'da 500px+ boşluk, çakışma yok.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-04 — Sanatsal Baskı: Ankara kaldırıldı, WhatsApp hattı eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Onur'un talebi — bu sayfada Ankara'dan bahsedilmeyecek. "ANKARA HATTI" iletişim kartı (0553 353 99 20) kaldırıldı; yerine **WHATSAPP HATTI — 0554 740 37 57** kartı geldi. Kart `https://wa.me/905547403757` linkiyle, "Merhaba, sanatsal baskı talebim var." ön-dolu mesajıyla WhatsApp'ı açıyor (`target="_blank" rel="noopener"`). Süreç bölümündeki "E-posta ya da WhatsApp" ifadesiyle artık tutarlı.
- **Doğrulama:** Sayfada Ankara/0553 referansı 0; wa.me/905547403757 ve görünür numara doğru.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-03 — Sanatsal Baskı: özel e-posta + metin tonu keskinleştirme

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **E-posta:** Sayfadaki görünür tüm iletişim noktaları **sanatsalbaski@cadbim.com.tr** oldu (CTA butonu + e-posta kartı; 2 mailto + 1 görünür metin). JSON-LD Organization kaydındaki cadbim@ bilinçli korundu — kurum kimliği site genelinde tektir. *Not: yeni adresin posta sunucusunda tanımlanması gerekir.*
- **Metin tonu (38 metin bloğu):** Açıklayıcı ton, kısa-özgüvenli galeri diline çevrildi. Örnekler: hero → "Duvara astığınız şey artık bir çıktı değil — bir eser."; hizmetler başlığı → "Kadrajdan koleksiyona."; rötuş → "Ham dosya girer. Eser çıkar."; yüzeyler → "Doğru kağıt, işin yarısı."; süreç → "Renk doğruluğu pazarlık konusu değil."; finisaj → "Baskı yarısı; sunum diğer yarısı." CTA kartları ve kapanış notu sadeleştirildi; tüm iddialar içerik kaynaklı kaldı (yeni sayı/iddia eklenmedi).
- **Doğrulama:** localhost — 5 yeni ton işaretçisi + sanatsalbaski@ görünür (2 mailto), eski adres görünür metinde 0, sürgü çalışıyor, taşma yok.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-02 — Sanatsal Baskı one-pager'ı Noomo stiline geçirildi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tetikleyici:** Onur'un referansı — noomoagency.com (Awwwards). Canlı siteden tasarım imzaları çıkarıldı: menekşe-siyah zemin (#181520), buz-lavanta metin, elektrik mavisi (#007aff), NeueMachina display tipografisi, iridesan 3D küre.
- **Uyarlama (DK-01'deki galeri/fildişi sürüm yerine):**
  - **Palet:** #131019 menekşe-siyah + buz-lavanta (#e9ecf7) + elektrik mavisi/iridesan degrade (cyan→viyole→magenta). **Tipografi:** Space Grotesk (NeueMachina'nın Google Fonts karşılığı) + Inter.
  - **Hero:** 11.5vw'lik 3 satır display — SANATSAL (dolu) / BASKI (iridesan degrade) / ATÖLYESİ (kontur) — satır-maskeli yükleme reveal'ları; arkada 2 iridesan CSS orb (WebGL küre öykünmesi, blur+drift).
  - **Noomo imzaları:** özel imleç (nokta + gecikmeli halka, data-hover'da büyür; ilk mousemove'a kadar gizli), manyetik butonlar, marquee şerit, dev satır-listesi hizmetler (hover'da degrade dolgu + ok rotasyonu), yatay sürükle-kaydır yüzey rayı, degrade dev sayaçlar, kontur CTA tipografisi (BASKIYA HAZIR MISINIZ?).
  - **Korunanlar:** interaktif rötuş sürgüsü (koyu restil), 4 adım süreç, 6 finisaj kartı, iletişim kartları; içerik birebir.
- **Erişilebilirlik/dayanıklılık:** Tüm hareket `prefers-reduced-motion`'da kapalı; imleç/manyetik yalnız `hover:hover + pointer:fine`; sayaçlarda rAF + zamanlayıcı güvencesi; reveal zaman-eşikli scroll motoru. SEO bloğu (canonical, Service JSON-LD) değişmedi.
- **Doğrulama:** localhost 1280/375 — yapı tam (5 iş + 6 yüzey + 4 adım + 4 sayaç + 6 finisaj + 4 iletişim + 2 orb), Space Grotesk aktif, sürgü %30→%75, marquee 18 span, reveal kademeli (16/36 kısmi), sayaçlar 12/2400/152/100, başlık mobilde sığıyor, ray kaydırılabilir, taşma 0, konsol hatası 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — aşağıda.

### DK-2026-07-22-01 — Sanatsal Baskı Atölyesi: özel tasarım one-pager

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_sanatsal_baski.html` sıfırdan, site genel temasından bilinçli ayrılan **galeri/editoryal estetikte** tek sayfalık tasarımla yeniden yazıldı (Onur'un talebi: "tamamen muhteşem, gerekirse tema dışı"). İçerik canlı cadbim.com.tr/sanatsalbaski + mevcut sayfadan derlendi.
- **Tasarım dili:** Fildişi kağıt zemini + mürekkep siyahı + vermilyon vurgu; Fraunces (optik boyutlu serif) + Inter tipografisi; CSS gren/kağıt dokusu; navy/cyan temadan tam kopuş.
- **Bölümler:** Minimal sabit üst bar → Hero (saf CSS "galeri duvarı": 3 çerçeveli eser + künye plaketi, kademeli yükleme animasyonu) → akan şerit (GICLÉE/KANVAS/FOTOBLOK...) → 5 hizmet satırı (editoryal liste) → 6 yüzey kartı (hover parlaklık süpürmeli doku çipleri) → **interaktif rötuş kıyas sürgüsü** (HAM DOSYA / ATÖLYE ÇIKIŞI) → 4 adımlı süreç (kontur rakamlar) → koyu ekipman bölümü (Z9+ Pro: 12 renk / 2400 dpi / 152 cm / 100+ yıl **animasyonlu sayaçlar**) → sergi alıntısı → 6 finisaj kartı (el çizimi SVG ikonlar) → iletişim (İzmir/Ankara/e-posta/form kartları).
- **Etkileşim/erişilebilirlik:** Sayfaya özel zaman-eşikli scroll-reveal + hero paralaksı + sayaçlar; tümü `prefers-reduced-motion`'da devre dışı (içerik anında görünür). Uppercase metinler literal yazıldı — İ/I sorunu tasarımdan elendi (GICLÉE, FINE ART).
- **SEO:** canonical `/sanatsal-baski` korundu; title/description yenilendi; JSON-LD **Service** şeması eklendi (Organization + WebPage + Breadcrumb ile).
- **Doğrulama:** localhost 1280/375 — yapı sayımları tam (5+6+4+4+6+4 kart/bölüm, 3 çerçeve), logo/Fraunces yüklü, sürgü %25→%80 tepkili, şerit çoğaltıldı (18 span), reveal kademeli (17/41 kısmi kaydırmada), sayaçlar hedefe ulaştı (12/2400/152/100), yatay taşma yok, konsol hatası 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

## 2026-07-21

### DK-2026-07-21-31 — Canlıya geçiş hazırlığı: eski site URL envanteri + 301 haritası

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Canlı cadbim.com.tr (Wix) sitemap index'inden **665 URL** toplandı (24 alt sitemap): 120 ana sayfa, 242 blog yazısı, 97 blog taksonomi, ~206 dinamik koleksiyon öğesi. Yeni site canonical setiyle (153) tam eşleme üretildi:
  - **33 BIREBIR** (aynı slug — 301 gerekmez), **210 KURAL** (kesin 301 hedefi), **83 GOZDEN** (Onur onayı gerekli), **339 GOZDEN-BLOG** (blog kararına bağlı).
  - DesignJet/UltiMaker/Chaos/Adobe koleksiyon öğeleri **model/ürün bazında** eşlendi (ör. /designjet-ofis/hp-designjet-t230 → /designjet-t200).
  - **İçerik adı değişiklikleri tablosu:** Construction Cloud→Autodesk Forma, Fusion 360→Fusion, ShotGrid→Flow Production Tracking, HSMWorks→Fusion, AutoCAD dikey ürünleri→toolset, Nastran/CFD/Point Layout EOL, MakerBot→UltiMaker vb.
  - Strateji notları: GitHub Pages sunucu-taraflı 301 yapamaz → canlıda Cloudflare Pages/Netlify benzeri host şart; Türkçe karakterli eski URL'ler; Search Console süreci; geçiş günü kontrol listesi.
- **Çıktılar:** `docs/CANLIYA-GECIS-URL-HARITASI.md` (rapor) + `docs/redirects-taslak.csv` (665 satır, makine-okunur).
- **Durum:** ✅ Doküman hazır; GOZDEN kalemleri Onur onayı bekliyor.

### DK-2026-07-21-30 — İç sayfalara scroll-reveal animasyon motoru

- **Kapsam:** Ana sayfadaki reveal deneyimi tüm iç sayfalara taşındı. `design-system.css`'e `[data-rv]` stilleri (yalnız `prefers-reduced-motion: no-preference` altında), `mobilenav.js`'e motor eklendi: `.sh/.card/.pgrid .pcard/.feat/.xp/.cross/.cta-strip/.office-card` hedefleri, ebeveyn içi 60ms kademeli gecikme (maks 360ms), ana sayfanın kendi `.reveal`'ı hariç tutulur.
- **Teknik karar:** IntersectionObserver yerine **zaman-eşikli scroll dinleyicisi** (80ms) — tarayıcı panelinde IO/rAF'ın hiç ateşlemediği tespit edildi; scroll+getBoundingClientRect her ortamda deterministik. `window.__rv` teşhis kancası bırakıldı.
- **Cache-bust:** design-system.css v7, mobilenav.js v5 (153 sayfa).
- **Doğrulama:** localhost — revit/autodesk/urunler: ilk görünüm anında, kaydırdıkça kademeli reveal (urunler 89 eleman, 1500px kaydırmada 39 reveal); stagger 0/60/120/180ms ölçüldü.

### DK-2026-07-21-29 — Site geneli kod + SEO denetimi ve düzeltmeleri

- **Denetim (154 dosya):** kırık iç link **0**, kırık asset **0**, duplicate id **0**, div dengesizliği **0**, alt'sız görsel **0**, title/desc mükerrerliği **0** — yapı zaten sağlamdı. Bulunan ve düzeltilenler:
  - **Attribute kıran tırnaklar:** designjet hd_pro/sd_pro description'larında kaçışsız `42"`/`44"` → `&quot;` (3'er meta).
  - **Kısa title'lar:** cozumler, kvkk, tesekkurler zenginleştirildi; **index description** 182→146 karakter.
  - **tesekkurler.html** form-sonrası sayfa → `noindex, follow`.
  - **Sitemap ↔ canonical uyumu:** 6 slug hizalandı (z6pro→z6-pro, factor4→factor-4, substance3d→substance-3d...).
  - **Performans:** 107 sayfada **647 img'e `loading="lazy"`**, 878 img'e `decoding="async"` — nav + hero görselleri bilinçli hariç (LCP koruması).
  - Yönlendirme stub'ına h1.
- **Durum:** ✅ Tamamlandı ve yayınlandı. **Referans:** commit (main) — DK-29/30/31 tek commit.

### DK-2026-07-21-28 — construction_cloud → autodesk_forma yeniden adlandırma + sayfa denetimi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Sayfa içeriği DK-öncesi turlarda "Autodesk Forma"ya çevrilmişti ama **dosya adı/URL** eski kalmıştı. Yapılanlar:
  - `cadbim_construction_cloud.html` → **`cadbim_autodesk_forma.html`** (git mv); canonical/og/JSON-LD 7 URL `/construction-cloud` → `/autodesk-forma`.
  - **Logolar güncellendi:** hero'daki jenerik vinç ikonu → resmi `forma.svg` (56px); "Build & Takeoff" modül kartındaki kask ikonu → `forma.svg`. (Diğer modül kartları zaten resmi SVG'liydi.)
  - **12 referans** güncellendi (8 sayfa + urunler 2 + tandem 4 dahil); `mobilenav.js` arama dizini kaydı "Autodesk Forma" oldu (eski ad arama anahtarı olarak korundu); `sitemap.xml` girdisi `/autodesk-forma` (lastmod 2026-07-21).
  - Eski adrese **yönlendirme stub'ı** bırakıldı (meta refresh + JS replace + canonical + noindex) — eski linkler kırılmaz.
  - Sayfada görünür "Construction Cloud" metni taraması: yalnızca bilinçli "(Eski adı Autodesk Construction Cloud.)" notu var, korunudu.
- **Doğrulama:** localhost — eski URL yeni sayfaya yönlendiriyor; başlık doğru; 3 forma.svg yüklü; taşma yok; site genelinde `construction_cloud` referansı 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.

### DK-2026-07-21-27 — Site geneli İngilizce sözcüklerde büyük-İ (İ→I) denetimi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Sorun:** Sayfalar `lang="tr"` olduğundan `text-transform:uppercase` İngilizce sözcüklerde de noktalı İ üretiyor (Architecture→ARCHİTECTURE, Trimble→TRİMBLE); ayrıca kaynakta yazılı 1 hata (COOKİE).
- **Denetim:** 152 sayfada (a) kaynakta İ içeren tüm sözcükler, (b) uppercase-transform'lu sınıf ve satır-içi stillerin tam metinleri tarandı. `lang="en"` verilmiş öğeler (sektör hero-badge'leri) zaten doğruydu — dokunulmadı. Türkçe sözcükler (LİSANSLAMA, SERİ, VİDEOSU, CADBİM...) bilinçli olarak İ ile bırakıldı.
- **Düzeltmeler (19 dosya, 27 değişiklik; İngilizce sözcükler kaynakta ön-uppercase edildi):** COOKİE→COOKIE (çerez politikası ×2); urunler grup başlıkları (ARCHITECTURE/ENGINEERING/CONSTRUCTION, PRODUCT DESIGN & MANUFACTURING, MEDIA & ENTERTAINMENT) + AMPLIFY rozeti; autodesk hero-pill SERVICE PROVIDER; hp hero-pill AMPLIFY; slabel'ler: ALIAS ×2, CIVIL, FUSION, AMPLIFY Impact ×2; satır-içi etiketler: CREDENTIALS, SPECIALIZATION (hakkimizda), HP CONSTRUCTION (build_workspace), LUMION B.V., MICROSOFT, TRIMBLE (sketchup), ULTIMAKER, HP DESIGNJET (sanatsal_baski), NESTING, FINE ART (designjet); pbrand: TRIMBLE (mimari), ULTIMAKER (makine).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda (DK-27 ve DK-28 tek commit).

### DK-2026-07-21-26 — Filtreli katalog deseni 7 endüstri sayfasına yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Marka sayfalarındaki filtreli katalog mantığı (Tümü+kategori chipleri, isim arama, pcard grid, boş durum) endüstri sayfalarına taşındı:
  - **Sekmeli gezgin dönüşümü (5 sayfa):** mimari (14), insaat (9), makine (15), medya (15), otomotiv (10) — eski `.solutions` sekme yapısı (tek kategori görünür, switchCat JS) kaldırıldı; tüm ürünler tek filtrelenebilir grid'de. Mevcut kategori adları chip oldu; kart içeriği (marka üst-etiketi + isim + rol + ikon) birebir korundu. Ölü switchCat script blokları silindi.
  - **Pill şeridi yükseltmesi (2 sayfa):** egitim (7: Yazılım 4 / 3D Baskı 2 / Donanım 1), havacilik (8: Tasarım & Müh. 3 / Üretim & Sim. 3 / Veri 1 / Donanım 1) — "Bu sektörde kullanılan ürünler" 13px pill şeridi katalog kartlarına dönüştü; açıklamalar hedef ürün sayfalarının meta description'ından otomatik alındı. Kutunun içinde filtre çubuğu sticky değil (statik).
- **Etkilenen dosyalar (7):** sektor_mimari, sektor_insaat, sektor_makine, sektor_medya, sektor_otomotiv, sektor_egitim, sektor_havacilik (+ scratchpad `sektor_catalogs.py`).
- **Doğrulama:** localhost 1280/375 — 7 sayfada toplam 78 kart; tüm chip sayıları kategori toplamlarıyla tutarlı; arama çalışıyor (mimari "revit"→2); 0 gerçek kırık ikon (ilk ölçümdeki 10 "kırık" lazy-load'du, eager doğrulamayla çürütüldü); mobilde tek sütun, chip taşması ve yatay taşma yok; div dengeleri 0; switchCat kalıntısı 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-25 — Filtreli ürün kataloğu 5 marka sayfasına daha yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** Autodesk'te kurulan filtreli katalog deseni (DK-23: fchip kategori filtreleri + isim arama + pgrid/pcard + boş durum) uygun tüm markalara uygulandı:
  - **Adobe (13):** "Creative Cloud Uygulamaları" bölümü katalogla değişti — Paket & Doküman 2 / Grafik & Fotoğraf 4 / Video & Ses 3 / 3D & AI 2 / İçerik & Stok 2.
  - **HP (22):** Designjet Serisi bölümünden sonra YENİ katalog bölümü — tüm model sayfaları tek listede: DesignJet T 9 / XL 2 / Z 5 / Tarayıcı & Tank 3 / İş İstasyonları 2 / Yazılım 1. Model adları ve açıklamaları her modelin kendi sayfasının title/meta'sından otomatik çekildi.
  - **Chaos (8):** "Chaos Ekosistemi" bölümü katalogla değişti — Render 2 / Gerçek Zamanlı 2 / Simülasyon & Animasyon 2 / AI & Varlıklar 2 (Anima ve Cosmos eklendi).
  - **UltiMaker (9):** "Yazıcı Modelleri" bölümü katalogla değişti — 3D Yazıcılar 7 (S8-S3, Factor 4, Method XL, Sketch Sprint) / Yazılım 2 (Cura, Digital Factory).
  - **SketchUp (7):** "SketchUp Pro Ürünleri" bölümü katalogla değişti — Pro Ailesi 4 / Platform & Paketler 3.
- **Kural:** Kendi sayfası olmayan ya da bulunulan sayfaya işaret eden ürünler ok'suz, tıklanmaz kart olarak listelendi (ör. V-Ray/Enscape/Veras, S-serisi modeller, Pro varyantları). **Lumion (4) ve Microsoft (3)** bilinçli kapsam dışı: tüm ürünleri zaten tek bakışta görünüyor, filtre değer katmıyor.
- **Bonus:** cadbim_urunler.html'de Digital Factory kartındaki yanlış ikon (Autodesk logosu) → ultimaker-icon düzeltildi.
- **Doğrulama:** localhost 1280/375 — 5 sayfada kart sayıları ve tüm chip filtreleri doğru (59 kart toplam), 0 kırık ikon, arama çalışıyor (hp "t850"→1), mobilde tek sütun/statik filtre/taşma yok, div dengeleri 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-24 — Site geneli logo-metin dikey hizalama denetimi ve düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tetikleyici:** cadbim_alias.html sürüm kartlarında ürün ikonu ile sürüm rozeti (CONCEPT / SURFACE / AUTOSTUDIO) baseline hizasında kayık duruyordu.
- **Denetim (152 sayfa, statik tarama + tarayıcıda piksel ölçümü):**
  - `img + <span class="cmp-badge">` satır-içi deseni: **4 bulgu** (alias 3, vault_pdm 1) → ikisi birlikte `display:flex;align-items:center;gap:10px` sarmalayıcıya alındı, rozetin `margin-bottom:10px`'i satır içinde sıfırlandı.
  - Öne çıkan kart başlıklarında `align-items:flex-start`: **3 bulgu** (chaos) → `center` yapıldı.
  - `.cp`/`.cross-pill` içi 13px mini logolar (53 dosya, ~130 kullanım): sınıf zaten `display:flex;align-items:center` — tarayıcı ölçümüyle 0.0px merkez farkı doğrulandı, **değişiklik gerekmedi**.
  - Flex dışı `vertical-align` img kullanımı: **0 bulgu**.
- **Doğrulama (localhost, DOM merkez ölçümü):** alias 3/3 rozet 0.0px; vault_pdm PLM BUNDLE 0.0px; chaos 3/3 başlık 0.0px; sketchup .cp örneklemi 5/5 0.0px; div dengeleri değişmedi.
- **Etkilenen dosyalar (3):** cadbim_alias.html, cadbim_vault_pdm.html, cadbim_chaos.html.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-23 — Autodesk sayfası: filtreli tam ürün kataloğu (46 ürün)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_autodesk.html` "Öne Çıkan Ürünler" bölümü (13 kart) yalnızca portföyün bir kısmını gösteriyordu. Ürünler sayfasındaki desenle (fchip + pgrid/pcard) **46 ürünlük tam katalog** ile değiştirildi: kategori filtreleri (Tümü / Koleksiyonlar 3 / Mimarlık & İnşaat 11 / Forma Platformu 4 / Ürün Tasarımı & İmalat 11 / Medya & Eğlence 10 / Genel Araçlar 7) + isimle arama kutusu + "eşleşen ürün yok" boş durumu. Filtre çubuğu masaüstünde yapışkan (sticky), mobilde statik. Kart verisi cadbim_urunler.html Autodesk bölümünden birebir alındı (AutoCAD Web mükerrer kaydı tekilleştirildi).
- **Etkilenen dosyalar:** cadbim_autodesk.html (+ scratchpad `autodesk_catalog.py`).
- **Doğrulama:** localhost 1280/375 — 46 kart, 0 kırık ikon; filtreler doğru sayıyor (AEC 11, M&E 10), arama "maya"→4, boş arama mesajı çalışıyor, sıfırlama 46; mobilde tek sütun, chip taşması yok, yatay taşma yok; div dengesi 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-22 — Marka sayfaları R3 kalite iyileştirmesi (6 sayfa)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam (Onur'un 5 maddesi, tüm marka ana sayfalarına uygulandı):**
  1. **Gold Partner rozeti küçültüldü** — autodesk hero rozeti clamp(200-290px)→clamp(150-200px) (masaüstü 282×429→192×292).
  2. **Hero hızlı-linkleri** — dağınık hap (pill) stili yerine eşit genişlikte gerilen, ikonlu, hover'lı düzenli kutular (`.hf` yeniden; mobil ≤600px varyantı ile). Autodesk/adobe/chaos/ultimaker.
  3. **Koleksiyonlar yan yana** — autodesk'te AEC/PD&M/M&E kartları kayıp grid sarmalayıcısı (`.colgrid`) ile 3 sütuna alındı (sayfadaki kadim -1 div dengesizliği de burada kapandı); resmi collection SVG ikonları + "Koleksiyonu incele →" linki eklendi.
  4. **LOGO placeholder temizliği** — 27 adet kesikli "LOGO" kutusu gerçek ürün logolarıyla değişti: autodesk 13 (resmi Autodesk SVG'leri; bağlantısız Navisworks/InfraWorks/Maya/Forma-platform kartları linklendi; mükerrer "Autodesk Forma" başlığı → "Forma Site Design"), chaos 6 (chaos.webp), ultimaker 5 (ultimaker-icon), microsoft 3 (microsoft.svg).
  5. **"Birlikte sıkça tercih edilenler"** — küçük/okunmaz logolu hap şeritleri yerine `.xgrid` kart modülü (42px logo kutusu + başlık + açıklama + ok); hedef linkler doğru ürün sayfalarına ayrıştırıldı (Z Workstation→hp_z_workstation, Designjet→designjet vb.). Autodesk/adobe/hp/chaos/ultimaker.
- **Partner rozet duvarları:** adobe (3 beyaz kutu → tek şeffaf Adobe Gold Reseller logosu), hp (3 beyaz kutu → tek resmi HP Amplify Synergy insignia, kendi kart tasarımıyla, çerçevesiz).
- **Etkilenen dosyalar (6):** cadbim_autodesk, cadbim_adobe, cadbim_hp, cadbim_chaos, cadbim_ultimaker, cadbim_microsoft (+ scratchpad script `brand_quality_r3.py`). sketchup/lumion/designjet/hp_z_workstation/hp_build_workspace'te bu desenler yok — değişiklik gerekmedi.
- **Doğrulama:** localhost 1280 ve 375 — 6 sayfada 0 kalan placeholder, 0 kırık logo, div dengeleri 0, yatay taşma yok; hf satırları eşit genişlik; koleksiyonlar masaüstünde tek satır/mobilde tek sütun; hp rozeti mobil 190×187 ortalı.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-21 — Autodesk hero: resmi tam-liste Gold Partner logosu (kullanıcı dosyası)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** DK-20'deki sade "AUTODESK Gold Partner" logosu, Onur'un ilettiği **resmi tam-liste** Gold Partner lockup'ı ile değiştirildi (Specialization: Product Design & Mfg., Building Architecture, Media & Entertainment, PLM, Design & Manufacturing Cloud + Value Added Services: Authorized Training Center, Authorized Developer, System Integrator). Şeffaf zeminli beyaz versiyon; çerçeve/kutu yok.
- **Kaynak dosya:** `5070268038-20230407083646.avif` (RGBA, 318×484, şeffaf) → PIL ile 2× LANCZOS → `assets/logos/autodesk-gold-partner-full-white.png` (636×968).
- **Etkilenen dosyalar:** cadbim_autodesk.html (img src + `.hero-badge img` genişlik clamp(200–290px) dikey logoya göre ayarlandı).
- **Doğrulama:** localhost — logo yüklendi (natural 636×968; masaüstü 282×429, hero metniyle 456px hizalı; mobil 200×304 ortalı); yatay taşma yok (1280 ve 375).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-21-20 — Autodesk hero: partner logo karmaşasını tek Gold Partner logosuna indirme

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** `cadbim_autodesk.html` hero'sundaki sağ rozet duvarı (7 kutu: Gold Partner, ATC, Service Provider, D&M Cloud, PD&M, M&E, PLM — beyaz kartlar) kaldırıldı. Yerine tek **Autodesk Gold Partner** logosu, çerçevesiz/beyaz-zeminsiz, koyu hero üzerinde beyaz (ters) versiyon (`autodesk-gold-partner-white.png`).
- **Etkilenen dosyalar:** cadbim_autodesk.html (markup: `.badgewall`→`.hero-badge`; CSS: `.bw-tile`/`.bw-wide` kuralları kaldırıldı, `.hero-badge` eklendi).
- **Doğrulama:** localhost — eski kutu sayısı 0, logo yüklendi (natural 845×215, masaüstü 358×91 / mobil 260×66), sağ sütunda, yatay taşma yok (1280 ve 375).
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit (main) — aşağıda.

### DK-2026-07-20-01 — SEO: prefix'li canonical/og:url/JSON-LD düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:** 29 sayfada canonical, `og:url` ve yapısal veri (JSON-LD `@id`/`url`/breadcrumb) alanlarındaki `/cadbim-<slug>` biçimi hosting'de 404 veriyordu. Sitemap ve canlıda çalışan öneksiz `/<slug>` biçimine hizalandı.
- **Etkilenen dosyalar (29):** cadbim_advance_steel, cadbim_arnold, cadbim_autocad_lt, cadbim_autocad_web, cadbim_autodesk_drive, cadbim_design_review, cadbim_desktop_connector, cadbim_dwg_trueview, cadbim_factory_design, cadbim_featurecam, cadbim_flame, cadbim_flow_production_tracking, cadbim_flow_studio, cadbim_golaem, cadbim_infraworks, cadbim_maya, cadbim_maya_creative, cadbim_meshmixer, cadbim_moldflow, cadbim_motionbuilder, cadbim_mudbox, cadbim_navisworks, cadbim_netfabb, cadbim_powermill, cadbim_powershape, cadbim_recap_pro, cadbim_revit_lt, cadbim_robot_structural, cadbim_tinkercad (her birinde 7 örnek; toplam 203 değişiklik).
- **Yöntem:** Byte düzeyinde `cadbim.com.tr/cadbim-` → `cadbim.com.tr/` değişimi (UTF-8/BOM ve satır sonları korundu).
- **Doğrulama:** Canlı GitHub Pages'te `cadbim_maya.html` → canonical ve og:url `https://www.cadbim.com.tr/maya`; JSON-LD'de prefix kalmadı; 0 kırık görsel. Kalan prefix'li URL taraması: 0.
- **Durum:** ✅ Tamamlandı ve yayınlandı.
- **Referans:** commit `1eabbf9` (main); yayın: GitHub Pages build `built` (2026-07-20).

### DK-2026-07-20-02 — SEO teknik denetimi (dokümantasyon)

- **Kapsam:** 152 sayfa genelinde teknik SEO sağlık taraması yapıldı.
- **Sonuç (güçlü):** title, description, canonical, OG/Twitter, viewport, `lang="tr"`, görsel `alt` (%100), JSON-LD (151/152; `tesekkurler` bilinçli hariç), sitemap (151 URL) + robots — hepsi mevcut ve tutarlı.
- **Tespit edilen hosting davranışı (cadbim.com.tr, canlı test):** Öneksiz temiz URL çalışır (`/autocad`, `/advance-steel`); prefix'li biçim 404; `.html` uzantılı biçim HTTP 400.
- **Durum:** Denetim tamamlandı; DK-...-01 uygulandı.

- **AÇIK KARAR (bekliyor):** İç linkler hâlâ `.html` biçiminde (`href="cadbim_autocad.html"`). Eski site Wix ile yapılmış; temiz URL'ler Wix'ten geliyordu. Wix bırakılınca yeni deploy'un URL davranışı seçilecek host'a bağlı. İç link + canonical + sitemap şeması host netleşince kesinleşecek. Onur onayı bekliyor.

### DK-2026-07-20-03 — Claude Design "son sürüm" paketinin uygulanması

- **Yapan:** Onur Bozok (Claude Design export) + Claude (PDM asistanı)
- **Kaynak:** `C:\Users\o.bozok\Downloads\cadbim web site.zip` (Claude Design bundle, 2026-07-20 10:45; `site/` kökü + README + hash'li/hash'siz asset ikizleri).
- **Kapsam:** Onur'un Claude Design'da tamamladığı güncel sürüm repoya uygulandı. En büyük değişiklik `index.html` (64.7KB → 80.4KB, yenilenmiş ana sayfa); `cadbim_iletisim.html` küçük güncelleme; toplam 81 sayfada içerik değişikliği + `mobilenav.js` güncellendi + `README.md` eklendi.
- **Yöntem:** Zip staging'e açıldı; hash'li ikiz asset'ler (70 dosya) ayıklandı (HTML yalnızca hash'siz adları referans ediyor); `site/*.html`, `mobilenav.js`, hash'siz `assets/*` repoya kopyalandı. Kök SEO dosyaları (`sitemap.xml`, `robots.txt`, `favicon.svg`, `og-image.png`) pakette olmadığından repodakiler korundu. Asset içerikleri repodakiyle birebir aynı çıktı (fiili asset değişikliği yok).
- **Not — canonical:** Paket, DK-...-01'deki canonical düzeltmesini geri alıyordu (`/cadbim-maya` gibi 404 biçimi). Uygulama sonrası düzeltme tekrar geçildi (29 sayfa, öneksiz `/slug`). Kalan prefix'li URL: 0.
- **Doğrulama:** Yerel sunucu (localhost:8420) — ana sayfa ve görsel-yoğun autodesk sayfası; konsol hatası yok, varlıklar 200, gerçek kırık görsel yok (rozetler `loading=lazy`, fetch 200). `index.html` = 80363 byte.
- **Durum:** ✅ Uygulandı ve doğrulandı; commit + push aşağıda.

### DK-2026-07-20-04 — Ana sayfa başlık/açıklama iyileştirmesi + yerel vurgu kaldırma

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam (index.html):**
  - Başlık/og/twitter: "Autodesk & Adobe Gold Partner | İzmir" → **"Autodesk Gold Partner & Tasarım Teknolojileri"** (şehir/ülke ibaresiz). İzmir yerel algısı yaratıyordu; "Türkiye" de gereksiz karakter olduğu için tamamen kaldırıldı.
  - Meta/og/twitter açıklamaları: portföy + hizmet + sektör birleştirildi. **Marka doğruluğu:** yalnızca Autodesk "Gold Partner"; Adobe/HP/Microsoft/Chaos/UltiMaker "yetkili iş ortağı" (önceki metin Adobe'yi de Gold gösteriyordu — düzeltildi).
  - Hero dekoratif koordinatından "— İZMİR" kaldırıldı (statik satır + dinamik JS güncellemesi).
- **Korundu:** JSON-LD adres şeması (faktüel İzmir merkez; yerel SEO/Haritalar) ve görünür "İzmir Merkez Ofis" etiketi (Onur tercihi).
- **Doğrulama:** localhost:8420 — sekme başlığı ve hero koordinatı güncel; İzmir ibaresi hero'da yok.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-05 — Site geneli marka/yerel tarama + Adobe statü düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Tarama sonucu:** "Autodesk & Adobe" dar çerçevesi site geneli DEĞİL — yalnızca `index.html` (footer), `cadbim_hakkimizda.html`, `cadbim_adobe.html`. İzmir 57 sayfada (125 kez) ama çoğu meşru (iletişim adresi, KVKK yasal, footer/schema).
- **Adobe statüsü:** Onur teyit etti → **Adobe Gold Reseller Partner** (sitenin adobe sayfası da öyle diyor). DK-...-04'te ana sayfada Adobe'yi hatalı biçimde "yetkili iş ortağı"na indirmiştim; düzeltildi.
- **Değişiklikler:**
  - `index.html` meta/og/twitter açıklamaları: Adobe → "Autodesk Gold Partner ve Adobe Gold Reseller Partner"; HP/Microsoft/(Chaos)/UltiMaker "yetkili iş ortağı".
  - `cadbim_hakkimizda.html` meta: "İzmir ve Ankara" ibaresi kaldırıldı; Adobe statüsü doğru yazıldı.
- **Dokunulmadı (zaten doğru):** adobe sayfası "Gold Reseller Partner" rozeti, hakkımızda gövde metni, footer "İzmir Merkez Ofis" (Onur tercihi), JSON-LD adres şeması.
- **Doğrulama:** localhost:8420 — ana sayfa meta/og "Adobe Gold Reseller Partner" içeriyor.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-06 — Metin rötuşları: hakkımızda sosyal açıklama + ana sayfa footer

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Kapsam:**
  - `cadbim_hakkimizda.html` og/twitter açıklaması: "Autodesk & Adobe Gold Partner" → "Autodesk Gold Partner, Adobe Gold Reseller Partner" (tam ve doğru statü).
  - `index.html` footer: "Autodesk ve Adobe Gold İş Ortağı." → tam portföy: "Autodesk Gold Partner ve Adobe Gold Reseller Partner; HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağı."
- **Doğrulama:** localhost:8420 — footer metni tam portföyü gösteriyor.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-07 — DesignJet sayfalarına ürün görseli + broşür (BATCH — devam ediyor)

- **Yapan:** Onur Bozok + Claude (PDM asistanı)
- **Amaç:** Sitedeki DesignJet sayfalarında ürün görseli yoktu; ekleniyor.
- **Kaynak kararları (Onur):** Ürün görselleri **HP resmi DAM CDN**'inden (temiz, şeffaf-zemin PNG); broşür PDF'leri **cadbim.com.tr**'den; video HP'den (varsa YouTube gömme). "En iyi çaba batch" — kalite sonra birlikte ayıklanacak.
- **Şablon:** hero altına yeni bölüm — beyaz kartta ürün görseli (`width:100%`/`height:auto`, oran korunur) + "Broşür İndir (PDF)" butonu (`btn-p`); Product JSON-LD `image` alanı ürün görseline güncellenir. Görseller `assets/products/`, PDF'ler `assets/brochures/`.
- **Kapsam (13 birebir eşleşen):** t1600, t2600, t830, t850, t950, t1700, xl3600, xl3800, z6pro, z9pro, z6ps, z9ps, tarayıcılar.
- **Hariç (rapor):** t200/t600 (canlıda ad farkı: T230/T630), t870/z6810/smart_tank (kaynak yok).
- **Kesinleşen kaynak kararları:** Görsel = HP (Onur'un indirdiği HP asset kitleri, `assets/products/designjet/` — gitignore'da); PDF = cadbim.com.tr broşürleri; **Video = CADBİM YouTube kanalı** (iframe embed, repoya video konmaz — mp4'ler 2.5GB, bazıları >100MB); Tarayıcı = `tarayıcılar` sayfası **sd_pro + hd_pro** iki ayrı sayfaya bölünecek (hub yok).
- **Görsel hazırlığı:** 13 model görseli seçildi, 1400px'e küçültüldü, şeffaf PNG'ler beyaz zemine düzleştirilip JPG yapıldı (47–236KB). `assets/products/hp-designjet-*.jpg` + `hp-scanner-{sd,hd}-pro.jpg`.
- **Tamamlanan (11 ürün sayfası, görsel+broşür, yayında):** t1600, t2600, xl3600, z6pro, z9pro, t1700, t830, t200(T230 görseli), t600(T630 görseli), z6ps, z9ps. Commit'ler: f8b9c14, 3d481cb, 07847d3, ac871b8.
- **Tarayıcı bölme ✅:** `cadbim_designjet_tarayicilar.html` silindi; yerine `cadbim_designjet_sd_pro.html` (SD Pro 2, 44" CIS) ve `cadbim_designjet_hd_pro.html` (HD Pro 2, 42" CCD) oluşturuldu. Her biri kendi görseli + cadbim broşürü + scanner'a özgü title/meta/canonical/JSON-LD/hero. sitemap 2 yeni URL (designjet-sd-pro, designjet-hd-pro); designjet.html kategori kartı 2'ye bölündü. Dangling referans yok, eski slug 404.
- **Şeffaf görsel ✅ (Onur "beyaz fonu sevmedim, kesip PNG yap"):** 13 DesignJet sayfasının tamamı beyaz kart yerine **şeffaf ürün PNG + hafif cyan glow**. 9'u şeffaf kaynaktan (folder PNG / HP DAM c-png), 4'ü (xl3600, z6pro, sd-pro, hd-pro) `rembg` (yerel u2netp) ile kesildi. z6pro "SALE" posteri temiz görselle değişti. Görseller 1200px, ~200KB-1MB.
- **Kategori thumbnail ✅:** `cadbim_designjet.html` kataloğunda görseli olan 13 modelin kartındaki jenerik ikon, küçük şeffaf ürün PNG'siyle değiştirildi. HP seri sayfalarında (t/xl/z) ürün galerisi yok (yalnızca çapraz-link), dokunulmadı.
- **HP YouTube videoları ✅:** 9 modele HP resmi tanıtım videosu responsive iframe ile gömüldü (hero altı): t1600, t2600, z6pro, z9pro, t200(T250), t600(T630), xl3600, t830, t1700. z6ps/z9ps ve tarayıcılar için net resmi ürün videosu yok (tutorial/3. taraf) → atlandı.
- **Durum:** ✅ DesignJet medya işi tamam — 13 sayfa şeffaf ürün görseli + broşür, kategori thumbnail'leri, 9 video. Kalan opsiyonel: assetsiz modeller (t850/t950/t870/z6810/xl3800/smart_tank) ve scanner/z-ps videoları.

### DK-2026-07-20-09 — Sürüm yedeği (bulut + local)

- **Bulut:** git tag **`v2026.07.20`** (commit `3f2da76`) oluşturulup GitHub'a push edildi. `main` güncel.
- **Local:** `C:\Users\o.bozok\Downloads\cadbim_site_yedek_2026-07-20.zip` (`git archive HEAD`, ~25MB, 265 dosya) — deploy edilebilir site; .git/.claude/ham-asset (`assets/products/designjet/`) hariç.
- **Kapsananlar:** DesignJet medya (şeffaf görsel+broşür+kategori thumbnail), IA yeniden sıralama+carousel, tarayıcı 2 sayfa, üst menü beyaz. **Videolar kaldırıldı** (yalnızca @HPGraphicArts linkleri beklendiği için — YouTube bana kapalı, Onur linkleri verecek).

### DK-2026-07-20-08 — DesignJet bilgi mimarisi (bölüm sırası) düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur hedef sırayı onayladı.
- **Sorun:** Ürün sayfalarında özellikler, video+çözümler bloklarının ALTINDA kalıyordu ("karmaşa"); kategoride katalog, teklif/çözüm linklerinin altındaydı.
- **Ürün sayfaları (13):** yeni sıra = hero → ürün görseli → **Öne Çıkan Özellikler → Modeller/Varyantlar** → Tanıtım videosu → İlgili çözümler → **Diğer DesignJet Modelleri (kaydırmalı carousel, thumbnail'li)** → Cadbim Farkı → **CTA (Teklif İste + Broşür İndir)**. Python regex ile blok yeniden sıralama; section dengesi doğrulandı.
- **Kategori (`cadbim_designjet.html`):** katalog (ürünler) hero'nun hemen altına; ilgili çözümler/marka linkleri aşağı. Ekran görüntüsüyle doğrulandı.
- **AÇIK — site geneli:** Onur "tüm siteyi bu mantıkla denetle" dedi. Marka (autodesk/adobe/hp/chaos/ultimaker/microsoft/sketchup/lumion), çözüm ve endüstri sayfalarında da "içerik/ürünler önce, ilgili/CTA sonra" denetimi + düzeltmesi yapılacak (çözüm/endüstri sayfaları önceki turda kısmen düzeltilmişti).
- **Durum:** 🔄 DesignJet bitti; site geneli audit kaldı.
- **Not:** z6pro görselinde çıktı "SALE" posteri — ileride değiştirilebilir. Atlananlar: t730 (EOL), t850, t950, t870, z6810, xl3800, smart_tank (kaynak yok).
- **Durum:** 🔄 Tüm sayfalar (13 ürün + 2 scanner) görsel+broşürlü; yalnızca video kaldı.

### DK-2026-07-20-10 — DesignJet: T870 + XL3600 tanıtım videosu gömüldü

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur video linklerini verdi.
- **Kaynak:** Onur iki YouTube linki iletti (HP resmi videolar):
  - `cuvHfdbQaNE` → "HP DesignJet XL 3600 MFP Series. Extreme reliability, compact size." → `cadbim_designjet_xl3600.html`
  - `CNG6QSRUDSQ` → "HP DesignJet T870 A1 Plotter — Versatile large-format 24-inch Printer" → `cadbim_designjet_t870.html`
- **Uygulama:** Her iki sayfada "Modeller & Varyantlar" bölümünden sonra responsive 16:9 iframe (padding-bottom:56.25%, loading=lazy). Gizlilik/KVKK için **`youtube-nocookie.com`** kullanıldı (önceki blokların `youtube.com/embed` yerine).
- **Doğrulama:** Her iki embed URL'i tarayıcıda açıldı — oynatıcı yükleniyor, "video kullanılamıyor" hatası yok, embed'e izin veriliyor. Dosyalarda tek iframe/tek video bölümü (grep ile teyit).
- **Not:** T870 ve XL3600 daha önce "kaynak yok" diye atlanmıştı (DK-08); bu linklerle kapatıldı. Kalan videosuz: t850, t950, z6810, xl3800, smart_tank, z6ps, z9ps, sd_pro, hd_pro.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-20-11 — HP video kaynak politikası + T850 videosu (hp.com yöntemi)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "hp.com yöntemini standart yap, T850'den başla" dedi.
- **Politika kararı:** Video kaynağı standardı belirlendi → `docs/HP-VIDEO-KAYNAK-POLITIKASI.md`. Birincil yöntem: ürünün **resmi hp.com sayfasını tarayıcıda açıp** video ID'sini oradan almak (hp.com ne koyduysa resmi + doğru üründür). Yedek: onaylı HP resmi kanalları whitelist'i. Bayi/3. şahıs (HP Plotter=Resolution GB, ACP techWERK, vb.) ve HPE reddedilir.
- **T850 ✅:** hp.com T850/T870/T950 seri sayfasından resmi video ID `hRa2oRinXyc` ("HP DesignJet T850, T870 and T950... Compact Size. Cutting-Edge Results", kanal: HP) alındı. `cadbim_designjet_t850.html`e "Modeller & Varyantlar" sonrası nocookie iframe ile gömüldü. Embed tarayıcıda test edildi (oynatıcı yüklendi, hata yok).
- **Ek bulgu:** Aynı seri videosu (`hRa2oRinXyc`) T870 + T950'yi de kapsıyor → o sayfalar için de resmi seçenek. T870 şu an Onur'un verdiği `CNG6QSRUDSQ` ile; değiştirilmedi (Onur onayı olmadan dokunulmaz).
- **Doğrulama tuzakları netleşti:** "HP Construction" adında resmi kanal YOK; AEC içeriği ana/bölgesel kanal + hp.com blogda. İsimde "HP" geçen bayi kanalları resmi değil.
- **Durum:** ✅ Politika + T850 tamam. Kalan: t950, z6810, xl3800, smart_tank, z6ps, z9ps, sd_pro, hd_pro (hp.com yöntemiyle sırayla).

### DK-2026-07-20-12 — T950 videosu (seri videosu, T850 ile ortak)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "aynı videoyu 2 ürün içinde kullanabilirsin" dedi.
- **T950 ✅:** hp.com seri videosu `hRa2oRinXyc` (T850/T870/T950'yi birlikte anlatan resmi HP videosu) `cadbim_designjet_t950.html`e gömüldü — T850 ile aynı. Şablon aynı (Modeller sonrası, nocookie, lazy). Video daha önce doğrulanmıştı (oynatıcı yükleniyor).
- **T870 dokunulmadı:** Onur'un verdiği `CNG6QSRUDSQ` ile kalıyor (kendi onayı olmadan değiştirilmez).
- **Durum:** ✅ T950 tamam. Kalan: xl3800, z6ps, z9ps, z6810, smart_tank, sd_pro, hd_pro.

### DK-2026-07-20-13 — DesignJet video batch: hp.com yöntemiyle 7 sayfa daha

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "hepsini yap" dedi.
- **Kapsam:** 15 videosuz DesignJet sayfası hp.com yöntemiyle tarandı (her ürünün resmi hp.com sayfası tarayıcıda açılıp video ID'si oradan alındı).
- **Gömülen (7, nocookie iframe, Modeller sonrası):**
  - t200 → hzxO73kldmc · t600 → 6WzCOBtWuGQ (ikisi de "Simple. Compact. Responsible.", HP)
  - t1600 + t2600 → ZEnzBgbS2yk (hp.com "Build Connected" seri videosu, ortak — Onur "aynı video 2 ürün" onayı)
  - xl3800 → MbASXZgN3tI · z6pro → EgbZf_9Ewjg (ikisi hp.com sayfasından, HP)
  - z9pro → zj8HtwqYn7w (resmi HP "Introducing Z6/Z9 Pro"; hp.com Z9 sayfası self-host, fallback). Embed test edildi.
- **Videosuz bırakılan (7, resmi yok):** t830, t1700, z6810, z6ps, z9ps, sd_pro, hd_pro. Gerekçeler politika dosyasında.
- **Reddedilen bayi videoları (doğrulama tuttu):** "HP DesignJet T830 Product Video" = GDS/Graphic Design Supplies Ltd (bayi); "T1600 & T2600 Product Video" = GOM Australia (bayi). İsim/başlık HP içerse de resmi değil → alınmadı.
- **Not:** t830/t1600/t2600 için hp.com'da temiz tekil ürün videosu yoktu; t1600/t2600'de "Build Connected" seri videosu kullanıldı. z6pro/z9pro daha önce (eski turda) kaldırılan sayfalardı; artık doğru resmi videolarla geri kondu.
- **smart_tank ✅:** hp.com Smart Tank sayfasında YouTube yoktu; resmi **HP Asia** kanalından (whitelist'te onaylı bölgesel resmi kanal) `zsYVMY0h3uU` ("Smart Tank T858 plotter and T908 MFP: HP's First Large Format Ink Tank Printer") alındı, embed test edildi, gömüldü.
- **Durum:** ✅ Batch tamam. Toplam **videolu: 12 sayfa** (t200,t600,t850,t870,t950,t1600,t2600,xl3600,xl3800,z6pro,z9pro,smart_tank). **Videosuz: 7** (t830,t1700,z6810,z6ps,z9ps,sd_pro,hd_pro — resmi video yok).

### DK-2026-07-20-14 — VideoObject schema (SEO) 11 sayfaya eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "VideoObject ekle" onayı.
- **Amaç:** Gömülü videoların Google'da video zengin sonucu (thumbnail+süre) üretebilmesi için schema.org VideoObject yapısal verisi.
- **Yöntem:** Her videonun GERÇEK metadata'sı YouTube watch sayfasından çekildi (uydurma yok): name (resmi başlık), uploadDate, duration (lengthSeconds→ISO8601), thumbnailUrl (i.ytimg.com/hqdefault). embedUrl (nocookie) + contentUrl + publisher=HP.
- **Eklenen (11):** t200, t600, t850, t950, t1600, t2600, xl3600, xl3800, z6pro, z9pro, smart_tank. Video bölümünden sonra ayrı ld+json bloğu. 11'i de JSON parse + zorunlu alan kontrolünden geçti.
- **Kanal doğrulaması (metadata sırasında):** hp.com kaynaklı videoların kanalları teyit edildi — HP, HP Construction Technology (T200/T600/T850-serisi/T1600-T2600), HP WW Studio (XL3600), HP Asia (Smart Tank). Hepsi resmi HP.
- **⚠️ T870 hariç bırakıldı:** T870 videosu (CNG6QSRUDSQ, Onur'un verdiği) kanalı **"Plot it"** = bayi, resmi HP değil. Politikaya aykırı olduğu için VideoObject eklenmedi; Onur'a swap önerisi (hRa2oRinXyc seri videosu T870'i de kapsıyor) sunulacak.
- **Yan bulgu (kapsam dışı):** sd_pro + hd_pro sayfalarının MEVCUT head JSON-LD'sinde önceden var olan JSON syntax hatası (muhtemelen kaçışsız " — 44"/42" ölçüleri). Bu iki sayfanın tüm yapısal verisi bozuk; ayrı düzeltilmeli.
- **Durum:** ✅ 11 VideoObject yayında. Açık: T870 kararı + scanner JSON fix.

### DK-2026-07-20-15 — T870 videosu resmi seriyle değiştirildi + scanner JSON-LD fix

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur her iki kararı onayladı.
- **T870 ✅:** Bayi kanalı videosu (CNG6QSRUDSQ "Plot it") → resmi HP seri videosu `hRa2oRinXyc` ("T850, T870 and T950", HP Construction Technology) ile değiştirildi. Ayrıca VideoObject eklendi. Artık T870 da politikaya uygun ve SEO schema'lı.
- **Scanner JSON fix ✅:** `sd_pro` ve `hd_pro` sayfalarının head JSON-LD `name` alanındaki kaçışsız `"` (44"/42") → `\"` yapıldı. Önceden bu iki sayfanın TÜM structured data'sı Google için geçersizdi; artık geçerli.
- **Doğrulama:** Tüm DesignJet sayfaları JSON parse edildi → 12 geçerli VideoObject, scanner head JSON'ları da parse oluyor, 0 hata.
- **Durum:** ✅ Tamam. Videolu 12 sayfanın tamamı resmi HP + VideoObject'li. Videosuz 7: t830, t1700, z6810, z6ps, z9ps + scanner'lar (sd/hd_pro resmi ürün videosu yok).

## 2026-07-21

### DK-2026-07-21-01 — Autodesk ürün sayfalarına resmi ürün logoları eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur resmi Autodesk ürün ikon paketini verdi (`Downloads/Autodesk Products/Original Format`, 125 `*-product-icons.zip`).
- **Sorun:** Autodesk ürün sayfalarının çoğunda hero'da gerçek ürün logosu yerine jenerik Tabler ikon kutusu vardı (yalnızca 8 sayfada logo vardı: autocad, revit, civil3d, fusion, fusion_manage, inventor, alias, vault_pdm).
- **Yapılan:** İlgili zip'lerden resmi **SVG** ürün ikonları çıkarıldı → `assets/logos/products/*.svg` (35 ikon). Her sayfanın hero rozeti (jenerik `<i class="ti">` kutusu / metin rozeti) resmi ürün SVG'siyle değiştirildi: `<img ... width:56px;height:56px;object-fit:contain>` (şeffaf 3B ikon olduğu için gölge/radius yok, oran korunur).
- **Kapsam (35 sayfa):** 3dsmax, advance_steel, arnold, autocad_lt, autocad_web, autodesk_drive, autodesk_docs, design_review, desktop_connector, factory_design, featurecam, flame, flow_production_tracking, flow_studio, golaem, infraworks, maya, maya_creative, moldflow, motionbuilder, mudbox, navisworks, nesting, netfabb, powermill, powershape, recap_pro, revit_lt, robot_structural, tandem, vehicle_tracking, aec_collection, bim_collaborate_pro, me_collection, pdm_collection.
- **Ayıklama (dokunulmadı):** Adobe (photoshop, illustrator vb.), Chaos (corona, phoenix, vantage, cosmos), UltiMaker/3D baskı (cura, method_xl, factor4, sketch_sprint), Trimble, ANIMA ve çözüm/konsept sayfaları (bim, plm, simulasyon...) — hero'daki "AUTODESK" etiketiyle filtrelendi.
- **İkon bulunamayan (atlandı, sayfa logosuz kaldı):** forma, tinkercad, meshmixer, dwg_trueview — verilen ikon setinde karşılığı yok.
- **Doğrulama:** Yerel sunucuda (localhost:8777) advance_steel, 3dsmax (eski metin rozeti), aec_collection (farklı en-boy) DOM ile kontrol edildi — SVG'ler yükleniyor, 56×56, object-fit:contain, kırık görsel yok. Otomatik tarama: 35 referans = 35 benzersiz ikon, 0 kırık, 0 kullanılmayan.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-02 — Ürün logoları çözüm/collection/endüstri/eğitim sayfalarındaki pill'lere yayıldı

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "bu ürün logolarını çözüm/collection/endüstri/eğitim sayfalarında kullan" dedi.
- **Sorun:** Bu sayfalardaki ürün-link pill'leri (`class="cp"`) Autodesk ürünleri için jenerik `autodesk-white.svg` veya Tabler `ti` ikonu kullanıyordu (marka logosu mantığı vardı: Chaos→chaos.webp, UltiMaker→ultimaker.svg, ama Autodesk ürünleri için tekil logo yoktu).
- **Yapılan:** Autodesk ürününe giden her `cp` pill'inin ikonu, ürünün kendi SVG logosuyla değiştirildi (`assets/logos/products/*.svg`, height:14px). Pill'lerde geçen ama daha önce çıkarılmamış 7 ürün (autocad, revit, civil3d, fusion, fusion_manage, inventor, vault_pdm) SVG'si de eklendi → products klasörü 42 ikon.
- **Kapsam:** 92 pill / 22 sayfa. Collection (aec/me/pdm: 14+11+11), çözüm sayfaları (bim, plm, pdm, simulasyon, cam, dijital_ikiz, nesting, insaat_yonetimi, gerceklik_yakalama, vb.), endüstri (sektor_havacilik/makine/insaat/mimari/otomotiv).
- **Korundu (doğru davranış):** Adobe/Chaos/UltiMaker/SketchUp/Lumion/HP/Microsoft marka logoları; çözüm-konsept (bim, construction_cloud) ve endüstri linkleri; SVG'si olmayan Autodesk ürünleri (forma, tinkercad). Yalnızca `products/<slug>.svg` mevcutsa değiştirildi.
- **Doğrulama:** localhost — aec_collection (18 pill'in 14'ü logo, hepsi yüklü) ve bim (Autodesk ürünleri logo aldı; chaos.webp/ultimaker.svg korundu; sektor_* linkleri ti ikonda kaldı). 0 kırık görsel.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-03 — Forma ürün ikonu autodesk.com'dan eklendi (beyaz)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "Forma'yı beyaza çevirip kullan; Tinkercad/Meshmixer/DWG TrueView aynı kalsın" dedi.
- **Kaynak:** autodesk.com Forma sayfasından resmi `forma-product-icon.svg` (images.ctfassets.net). Orijinal siyah monokrom glif → koyu temada görünsün diye `fill="#ffffff"` yapıldı → `assets/logos/products/forma.svg`.
- **Uygulama:** cadbim_forma.html hero rozeti (jenerik gradient+ti ikonu) → beyaz Forma SVG'si (diğer 35 ürünle aynı bare-icon deseni, 56px). 4 kategorideki forma cp-pill'leri de logoyu aldı (aec_collection ×2, dijital_ikiz ×1).
- **Atlanan (Onur kararı):** Tinkercad (yalnızca yatay wordmark), Meshmixer (kaldırılmış ürün, kalıcı asset yok), DWG TrueView (viewer, ürün ikonu yok) → mevcut Tabler ikonlarında bırakıldı.
- **Not:** Autodesk güncel ürün ikonları sade monokrom glif (ctfassets); zip'teki renkli 3B kutulardan stil farkı var. Forma tek monokrom beyaz ikon olarak duruyor (Onur onayladı).
- **Doğrulama:** localhost — forma hero beyaz glif yüklü (56px, koyu zeminde kontrastlı). products klasörü 43 SVG.
- **Durum:** ✅ Uygulandı ve doğrulandı.

### DK-2026-07-21-04 — Tinkercad + Meshmixer logoları eklendi (Onur'un verdiği)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur logoları İndirilenler klasörüne koydu.
- **Tinkercad:** `tinkercad-lockup-white.svg` (beyaz yatay wordmark) → `assets/logos/products/tinkercad.svg`. cadbim_tinkercad.html hero rozeti (jenerik ti-cube) → wordmark (height:34px). Wordmark olduğu için pill'lere uygulanmadı (metin etiketiyle tekrar olurdu).
- **Meshmixer:** `meshmixer.png` (renkli low-poly kare ikon, 120×120) → `assets/logos/products/meshmixer.png`. cadbim_meshmixer.html hero rozeti → ikon (56px, object-fit:contain, diğer ürünlerle aynı desen).
- **DWG TrueView:** autodesk.com/products/dwg-trueview/overview sayfası tarandı — üründe **logo/ikon yok** (yalnızca arayüz ekran görüntüsü). Alınamadı; sayfa mevcut Tabler ikonuyla kaldı.
- **Doğrulama:** localhost — meshmixer (120×120 PNG, 56px yüklü) ve tinkercad (wordmark 129×34 yüklü). products klasörü 45 asset (43 svg + tinkercad.svg + meshmixer.png; forma dahil).
- **Not:** Tinkercad hero'da wordmark + "Tinkercad" metin etiketi bir miktar tekrar oluşturuyor; istenirse metin etiketi sadeleştirilebilir.
- **Durum:** ✅ Tinkercad + Meshmixer uygulandı. DWG TrueView'da logo yok.

### DK-2026-07-21-05 — DWG TrueView logosu bulundu ve eklendi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ekran görüntüsüyle logonun hero'da olduğunu gösterdi.
- **Düzeltme:** DK-04'te "DWG TrueView'da logo yok" demiştim — yanlıştı. Logo, autodesk.com sayfasında **inline SVG** olarak gömülüydü (img/CDN taraması kaçırmıştı). DOM'da hero eyebrow'un kardeş öğesinde bulundu.
- **Kaynak/uygulama:** Inline SVG (viewBox 965×880, kırmızı "D": #78082A/#E51050/#E85984 + beyaz harf) çıkarıldı → `assets/logos/products/dwg-trueview.svg`. **Zip ikonlarıyla birebir aynı detaylı 3B-kutu stili** — mükemmel uyum. cadbim_dwg_trueview.html hero (jenerik ti-file-search) → ikon (56px). sektor_egitim.html'deki dwg pill'i de logoyu aldı.
- **Doğrulama:** localhost — hero SVG yüklü (164×150 doğal, 56px, object-fit:contain), kırmızı D render oluyor.
- **Durum:** ✅ Eklendi. Böylece 4 eksik ikon da tamamlandı: Forma, Tinkercad, Meshmixer, DWG TrueView.

### DK-2026-07-21-06 — Ürünler sayfası (cadbim_urunler.html) Autodesk ürün logoları

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "ürün logoları eski tip, elindekilerle güncelle" dedi.
- **Sorun:** Ürünler sayfasındaki kartlarda (`.pcard`) jenerik Tabler ikonları (`ti ti-*`) vardı.
- **Yapılan:** Her kartın `.pico` kutusundaki jenerik ikon, ürünün resmi logosuyla değiştirildi (kutu korundu, içine 28px `object-fit:contain` logo). Alias ikonu da zip'ten çıkarıldı (`alias.svg`).
- **Kapsam:** 45 Autodesk ürün kartı (koleksiyonlar dahil). Toplam 88 karttan.
- **Bilerek yapılmadı:** Adobe/Chaos/UltiMaker/Microsoft ürün kartları — bu markaların logoları **koyu zeminde görünmez** (ultimaker.svg çoğunlukla `fill=black`, microsoft %100 siyah). Mevcut renkli Tabler ikonları görünür olduğu için korundu (siyah logo koymaktan iyi). Tinkercad (yatay wordmark, 42px kare kutuya uymaz) ve logosuz olanlar (construction_cloud, anima, digital_factory, trimble_connect, hp_*) da olduğu gibi kaldı.
- **Doğrulama:** localhost — 45 ürün logosu yüklü, 0 kırık, kutu içinde 28×28.
- **Durum:** ✅ Autodesk ürün kartları güncellendi.

### DK-2026-07-21-07 — "Forma" adlandırma karışıklığı düzeltmesi (ürünler sayfası)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ürünler sayfasında "hem Autodesk Forma hem Forma var" karışıklığını sordu.
- **Kök neden (araştırıldı):** Autodesk 2025 rebrand — Construction Cloud → **Autodesk Forma** (endüstri bulutu), Autodesk Docs → **Forma Data Management**. Eskiden tek başına "Autodesk Forma" olan tasarım ürünü → artık **"Forma Site Design"**. Site zaten yeni markalamayı kullanıyordu; tek eksik, tasarım ürününün "Forma" olarak kalmasıydı (şemsiye markayla çakışıyordu).
- **Düzeltme:** cadbim_urunler.html'de `forma.html` kartı **"Forma" → "Forma Site Design"**. Böylece endüstri bulutu ("Autodesk Forma" → construction_cloud) ile tasarım uygulaması ("Forma Site Design" → forma) net ayrışıyor.
- **Doğrulama:** 4 Forma kartı artık ayrı adlarda (Forma Site Design / Autodesk Forma / …Design Collaboration / …Data Management).
- **Açık (opsiyonel):** forma.html sayfasının kendi başlığı/hero'su hâlâ "Forma Building Design"; tam tutarlılık için "Forma Site Design"a çekilebilir (Onur onayı bekliyor).
- **Not:** Önceki turda bu kartları hatalı biçimde "yanlış etiketlenmiş" demiştim — düzeltme: site aslında güncel Autodesk markalamasını kullanıyor.
- **Durum:** ✅ Ürünler sayfası karışıklığı giderildi.

### DK-2026-07-21-08 — Forma tam tutarlılık + ürünler sayfasında gruplama

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "tam tutarlı olsun, Forma grubu yan yana dursun" dedi.
- **forma.html:** "Forma Building Design" → **"Forma Site Design"** (title, meta, og, twitter, JSON-LD — 12 yer). Hero adı "Building Design" → "Site Design" (eyebrow "AUTODESK FORMA" korundu → "Autodesk Forma / Site Design" okunur). Kalan "Building Design" → "Site Design" (2 yer). Artık sayfa baştan sona resmi "Forma Site Design" adını kullanıyor.
- **cadbim_urunler.html:** "Forma Site Design" kartı, diğer 3 Forma kartının (Autodesk Forma / …Design Collaboration / …Data Management) yanına taşındı → **4 Forma ürünü artık yan yana**.
- **Doğrulama:** pcard sayısı 88 (değişmedi), section dengesi 4/4, forma.html'de "Building Design" kalmadı, sıra: InfraWorks → [Forma Site Design, Autodesk Forma, …Design Collaboration, …Data Management] → Vehicle Tracking.
- **Durum:** ✅ Forma adlandırması tutarlı + gruplandı.

### DK-2026-07-21-09 — Autodesk Forma platform yapısı (hub + gruplama)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "Forma grubunu iyi anlatan bir yapı, gerekirse üst sayfada platformu yansıtan" istedi. Onaylar: construction_cloud'u dönüştür + ürünler sayfasında alt-başlık+modüller.
- **Hub (cadbim_construction_cloud.html → Autodesk Forma platformu):**
  - Hero platform seviyesine genişletildi: eyebrow alt satırı "Site Design · Data Management · Design Collaboration · Build · Takeoff"; H1 "AEC Endüstri Bulutu — Tasarımdan Sahaya"; giriş paragrafı Site Design dahil tüm modülleri anlatıyor (+"Eski adı Autodesk Construction Cloud").
  - **Yeni "Platform Modülleri" bölümü:** 4 linkli kart — Forma Site Design → forma, Forma Data Management → autodesk_docs, Forma Design Collaboration → bim_collaborate_pro, Build & Takeoff → insaat_yonetimi. Her kart ürün logolu + "İncele →".
  - Başlık/meta: "İnşaat Yönetim Platformu" → "AEC Endüstri Bulutu" (4 yer: title/og/twitter).
- **Ürünler sayfası (cadbim_urunler.html):** 4 Forma kartı AEC grid'inden çıkarılıp **"Autodesk Forma Platformu"** etiketli ayrı grid'e alındı (Forma logosu + açıklama + "Platforma genel bakış →" construction_cloud'a link). Grup artık net ayrışıyor.
- **Doğrulama:** localhost — hub 4 modül kartı doğru sayfalara linkli, logolar yüklü; ürünler alt-grubu etiketli, 4 kart ayrı grid; 0 kırık. section 6/6, div 147/147, 88 kart korundu.
- **Durum:** ✅ Forma platform yapısı kuruldu.

### DK-2026-07-21-10 — Ürünler sayfası logo tamamlama: Adobe + marka logoları

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ürünün logosu olsun, gerekirse vendor resmi sitesinden al" dedi.
- **Adobe (Onur'un 'adobe logolar' klasöründen):** 9 ürün app ikonu SVG çıkarıldı (photoshop, illustrator, indesign, premiere-pro, after-effects, lightroom, firefly, adobe-express, adobe-stock) + acrobat.svg + adobe.png (Creative Cloud). Ürünler sayfası 9 Adobe kartına uygulandı; adobe.html'de eksik olan **Acrobat kartı** gerçek app ikonuyla güncellendi (diğer 7 zaten inline SVG ikonluydu).
- **Marka logoları (koyu zeminde görünür olanlar):** HP ürünleri (6) → hp-blue.png; Chaos (chaos/corona/vantage/phoenix/cosmos) → chaos.webp; Lumion (lumion/view/cloud) → lumion.png. construction_cloud ("Autodesk Forma") → forma.svg; adobe markası → adobe.png (Creative Cloud).
- **Kalan (vendor fetch gerek — koyu/wordmark/dosya yok):** substance3d, cura, method_xl, sketch_sprint, sketchup, sketchup_go, microsoft, trimble_connect, anima, digital_factory, tinkercad. Sıradaki adımda vendor resmi sitelerinden alınacak.
- **Durum:** 🔄 Ürünler sayfası logo tamamlama — Adobe + görünür markalar bitti; vendor-spesifik olanlar kaldı.

### DK-2026-07-21-11 — Ürünler sayfası: kalan tüm ürün logoları tamamlandı (88/88)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ürünün logosu olsun, gerekirse vendor resmi sitesinden al".
- **Vendor resmi sitelerinden çekilenler (curl):** UltiMaker favicon → ultimaker-icon.webp (cura, method_xl, sketch_sprint, factor4, ultimaker); SketchUp favicon.svg (#0063a3) → sketchup-icon.svg (sketchup, sketchup_go, sketchup_studio); Trimble apple-touch → trimble-icon.png (trimble_connect); AXYZ anima apple-touch → anima-icon.png; Tinkercad app_icon_512 → tinkercad-icon.png.
- **Elle oluşturulan:** microsoft.svg (resmi 4 renkli kare mark — koyu zeminde görünür).
- **Fallback:** substance3d → adobe.png (Creative Cloud). Adobe Substance sitesi SPA olduğu için curl ikon vermedi; geçerli Adobe-markalı ikon konuldu, Substance'a özel ikon bulununca değişecek. digital_factory → autodesk beyaz logo; construction_cloud → forma.svg.
- **Sonuç:** **88/88 ürün kartı logolu, 0 jenerik ikon, 0 kırık referans.** products klasörü 66 asset.
- **Not:** Bazı vendor ikonları favicon kaynaklı (kare, resmi ama app-icon değil). Tarayıcı bu turda kararsızdı; doğrulama dosya-bazlı (tüm img referansları mevcut dosyalara çözümleniyor).
- **Durum:** ✅ Ürünler sayfası logo tamamlama bitti.

### DK-2026-07-21-12 — Ana sayfa hero ekrana sığma düzeltmesi

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur ekran görüntüsüyle ana sayfanın ekrana sığmadığını gösterdi (istatistikler 30+/10.000+/7 alttan kesiliyordu).
- **Teşhis (tarayıcı ölçümü):** Yatay overflow YOK. Sorun dikey: hero içeriği yalnızca 514px ama `min-height:calc(100vh - 132px)` (940px ekranda 808px) + dikey ortalama → 294px boş alan; bu da hero'yu şişirip istatistik bölümünü ekran dışına itiyordu.
- **Düzeltme (index.html):** `.hero` min-height `calc(100vh - 132px)` → `calc(100vh - 260px)`; padding-top 80px → 72px. Boş alan 294→166px azaldı; içerik hâlâ dikey ortada, taşma yok.
- **Doğrulama (localhost, cache-buster):** 940px viewport'ta hero 808→680px, istatistikler tam görünür. 860px viewport'ta hero 606px, içerik sığıyor, istatistik tam görünür, 0 yatay overflow. Mobil/tablet breakpoint'leri (min-height:auto) etkilenmedi.
- **Durum:** ✅ Hero ekrana sığıyor.

### DK-2026-07-21-13 — Ana sayfa hero: küçük viewport/ölçekleme için ek sıkıştırma

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur hard-refresh sonrası hâlâ stats'ın kesildiğini bildirdi.
- **Teşhis:** DK-12 fix'i canlıda mevcuttu (curl+tarayıcı teyit), ama Onur'un ekranında Windows ölçekleme (%125/%150) efektif viewport'u küçültüyor → içerik (514px) + stats hâlâ sığmıyordu. 722px viewport'ta 11px, daha küçükte daha çok kesiliyordu.
- **Düzeltme (index.html hero):** min-height calc(100vh-260px)→calc(100vh-300px); padding-top 72→68; boşluklar sıkıştırıldı (eyebrow mb 22→14, h1 mb 20→14, sub mb 34→22, btns mb 34→8, btns gap 14→12); h1 clamp max 4rem→3.5rem. İçerik 514→~430px.
- **Doğrulama (localhost):** 722px viewport stats alt 647 (tam görünür); 648px viewport stats alt 644 (tam görünür, 4px pay); yatay overflow yok. ~%150 ölçeklemeye kadar sığıyor.
- **Not:** Onur'un gördüğü yarım-kesik büyük olasılıkla eski sürüm cache'iydi (düzeltilmiş sürüm en fazla birkaç px kesiyordu). Kesin çözüm için cache-buster URL (?v=) önerildi.
- **Durum:** ✅ Hero küçük viewport/ölçeklemede de sığıyor.

### DK-2026-07-21-14 — Ana sayfa hero: her ekranda tutarlı (içerik-boyutlu)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "her ekranda aynı olacak şekilde ayarla" dedi.
- **Değişiklik:** `.hero`'dan `min-height:calc(100vh - ...)` (viewport-bağımlı) kaldırıldı → hero artık **içerik-boyutlu, sabit** (padding 88/52). Böylece ekran yüksekliğinden bağımsız her ekranda AYNI hero yüksekliği (~572px), stats hep tutarlı konumda.
- **Doğrulama (localhost, çoklu boyut):** 1040px, 750px → hero 572px, stats tam görünür. 648px (uç %150 ölçekleme) → hero 569px (tutarlı) ama stats 48px altta. Yatay overflow yok. Hero yüksekliği tüm boyutlarda ~sabit (569-572).
- **Not:** Önceki vh-bağımlı yaklaşım küçük ekranda hero'yu küçültüyordu (sığdırıyordu ama ekrandan ekrana değişiyordu). Yeni yaklaşım tutarlılık önceliğinde; gerçek masaüstü viewport'larında (≥750px) stats tam görünür.
- **Durum:** ✅ Hero her ekranda tutarlı.

### DK-2026-07-21-15 — Substance 3D: Adobe sayfasından resmi ikonlar + içerik

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "substance ürününü adobe.com/tr/products/substance3d sayfasındaki gibi (içerik + görseller) istiyorum" dedi.
- **Görseller (adobe.com CDN, curl):** Resmi Substance 3D ikonları çıkarıldı → `assets/logos/products/`: substance3d.svg (ana koleksiyon), substance-painter/sampler/designer/stager/modeler/assets.svg (6 uygulama).
- **cadbim_substance3d.html:** Hero ikonu jenerik ti-texture → gerçek Substance 3D ikonu. Yeni **"Substance 3D Uygulamaları" bölümü** eklendi (cross sonrası): 6 uygulama kartı, her biri resmi app ikonu + Türkçe açıklama (Painter=doku boyama, Sampler=fotoğraftan malzeme, Designer=prosedürel, Stager=sahneleme/render, Modeler=heykel/VR, Assets=kütüphane). İçerik Adobe'nin ürün yapısına göre, CADBİM Türkçesiyle adapte (verbatim kopya değil).
- **cadbim_urunler.html:** substance3d kartı fallback adobe.png → gerçek substance3d.svg.
- **Doğrulama (localhost):** Substance sayfası hero ikonu + 6 app ikonu yüklü, 0 kırık.
- **Durum:** ✅ Substance 3D Adobe sayfasına göre güncellendi (gerçek ikonlar + uygulama bölümü).

### DK-2026-07-21-16 — Tüm ürün sayfalarında bilgi mimarisi: içerik önce, CTA sonda

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur "ürün sayfalarında önce ürünü tanıt; ilgili ürünler/kullanıldığı çözümler ve CTA sonda olsun; şu an hero'da ilk 'Teklif İste' geliyor, tüm ürünler için değiştir" dedi.
- **Yapılan (2 işlem, tüm ürün/marka/sektör sayfaları):**
  1. **Hero CTA kaldırıldı** — hero'daki "Teklif İste / Marka Sayfası / Eğitim" butonları çıkarıldı. 3 farklı hero yapısı ele alındı: Tip A (`display:flex;gap:12px`), Tip B tek-satır ve **çok-satırlı** `hero-btns`, ve microsoft'taki çıplak `btn-p`. Toplam 79 sayfada hero artık yalnızca ürünü tanıtıyor.
  2. **"İlgili ürünler & çözümler" (cross) bölümü sona taşındı** — hero'nun hemen altındaki cross, sayfanın sonuna (cta-strip'ten hemen önce) alındı. 94 sayfada.
- **Yöntem:** Python dönüşümü + her sayfada section/div **denge kontrolü** (delta=0 zorunlu, bozulanlar atlanır). 0 sayfa bozuldu. (autodesk.html'deki -1 div farkı önceden vardı, benim değişikliğim değil.)
- **Doğrulama (localhost):** autocad (emb-logo tipi) ve substance3d (Tip A) — hero'da CTA yok, tek "Teklif İste" yalnızca sondaki cta-strip'te, cross CTA'dan hemen önce, 0 kırık görsel. Yeni sıra: hero(tanıtım) → özellikler/uygulamalar → kullanım → ilgili ürünler(cross) → CTA.
- **Not:** Autodesk sayfalarında 2 cross uç uca gelebiliyor (ilgili ürünler + Cadbim lisans); yapısal sorun değil, istenirse birleştirilir.
- **Durum:** ✅ Tüm ürün sayfaları: içerik önce, CTA sonda.

### DK-2026-07-21-17 — Ürün sayfası sonu: "Bu Ürünle İlgili" modülü (çözüm/endüstri/eğitim)

- **Yapan:** Onur Bozok + Claude (PDM asistanı) · Onur karışık cross'u beğenmedi; "kullanıldığı çözümler ve endüstriler şeritleri + ilgili sayfalara link; eğitimi olan ürünlerde eğitim yönlendirmesi (sadece Autodesk, önce eğitim var mı kontrol et)" istedi. Tasarımı substance3d prototipinde onayladı.
- **Yeni modül (sayfa sonu, cross yerine):** "Keşfet / Bu Ürünle İlgili" başlığı + etiketli 3 grup: **Kullanıldığı Çözümler** (çözüm sayfalarına linkli pill'ler), **Endüstriler** (sektör sayfalarına linkli), **Birlikte Çalıştığı Ürünler** (cross'tan çıkarılan, ürün logolu). + **Eğitim CTA banner'ı**.
- **Eşleştirme:** Ürün→kategori (AEC/M&E/PD&M/PLATFORM/Adobe/Chaos) → kategori-bazlı çözüm+endüstri. Birlikte-ürünler mevcut cross'tan alındı.
- **Eğitim banner'ı:** Yalnızca eğitimi olan Autodesk ürünlerinde (egitimler'deki data-cat'lere göre: autocad, revit, inventor, fusion, civil, media=3ds/maya, aec). 16 sayfada. Banner `cadbim_egitimler.html?cat=<kategori>#katalog`'a gidiyor; egitimler'e URL-param filtre desteği eklendi (o kategoriyi otomatik filtreleyip katalog'a kaydırır). Adobe/HP/vb.'de eğitim banner'ı yok.
- **Kapsam:** 63 sayfa (62 script + substance manuel). cross varsa değiştirildi, yoksa cta-strip öncesi eklendi.
- **Doğrulama:** Denge kontrolü 0 bozulma (autodesk'in -1'i önceden vardı). autocad (çözüm/endüstri linkleri, eğitim→?cat=autocad, modül CTA öncesi, 0 kırık); egitimler?cat=autocad → AutoCAD sekmesi aktif, 4 kurs filtreli. 
- **Durum:** ✅ Tüm ürün sayfalarında yeni ilgili-modülü + koşullu eğitim yönlendirmesi.

### DK-2026-07-21-18 — Mobil arama kapatma + egitimler logo temizliği + HP logosu

- **Yapan:** Onur Bozok + Claude (PDM asistanı).
- **1) Mobil menü/arama kapatılamıyordu:** Kök neden — hamburger `.nav` (z-index:1000) stacking context'i içinde; arama paneli `z-index:2000` hamburger'ı örtüyordu. Çözüm: panelin `.cbm-top` bar'ına görünür **kapat (X) butonu** eklendi (`.cbm-close`), `close()`e bağlandı. Artık ESC + hamburger + kapat butonu ile kapanıyor. (mobilenav.js)
- **2) cadbim_egitimler.html:** Rozet satırından **Adobe Gold Reseller ve HP Amplify** logoları kaldırıldı (Cadbim yalnızca Autodesk ATC eğitimi veriyor). Kalan: Autodesk ATC + Academic Partner.
- **3) Ana sayfa markalar (HP kutusu):** Karmaşık `hp-amplify-insignia.png` → sade resmi **mavi HP logosu** (`HP_Blue_RGB_150_MD.png` → assets/logos/hp-logo.png, 300×300). index.html cred-row.
- **Doğrulama (localhost, mobil+masaüstü):** Mobilde menü açılıp kapat butonuyla kapanıyor; egitimler'de adobe/hp logosu yok; ana sayfa HP kutusu mavi HP logosu yüklü.
- **Durum:** ✅ Üç düzenleme tamam.

### DK-2026-07-21-19 — Nav logosu yatay CADBİM + marka logo boyut dengeleme

- **Yapan:** Onur Bozok + Claude (PDM asistanı).
- **Nav logosu (153 sayfa):** Sol üstteki ikon + "CADBİM" + "Est. 1993" metni kaldırıldı; yerine Onur'un verdiği **yatay CADBİM logosu** (`cadbim logo yatay png.png` → assets/logos/cadbim-yatay.png). Ek metin eklenmedi (Onur talebi). Mevcut `.nav-logo img` CSS'i (height:26px, filter beyaz) korundu → logo beyaz, ~109×26. Hover'da mevcut "draw/reveal" animasyonu (clip-path) uygulanıyor. Görsel 24862px'ten 640px'e küçültüldü (decompression-bomb boyutundaydı).
- **Marka logo boyutları (index.html cred-row):** Kare/baskın logolar (hp/chaos/adobe/microsoft) küçültüldü, sketchup düşürüldü (Onur "çok büyük"), geniş olanlar (ultimaker/lumion) genişletildi. base max-height 66→48 + per-logo `[src*=]` ayarları. Yükseklik aralığı 22-66 → 22-56 (çoğu 44-56).
- **Doğrulama:** localhost 1280px — nav logo 109×26 görünür; marka logoları dengeli. (Not: browser pane bir ara 0×0 viewport'a düştü, ölçümler yanıltıcıydı; düzgün boyutta doğrulandı.)
- **Durum:** ✅ Logo + boyut dengeleme tamam. Animasyon seçeneği Onur'a soruluyor. SketchUp Pro ürünleri + derin mobil cila sıradaki iş.
