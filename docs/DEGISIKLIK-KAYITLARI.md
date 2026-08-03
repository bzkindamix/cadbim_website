# CADBİM Web Sitesi — Değişiklik Kayıtları (PDM / Revizyon Günlüğü)

> Bu dosya, projeye yapılan her değişikliğin izlenebilir kaydını tutar (PDM/ECO mantığı).
> Kayıt biçimi: **DK-YYYY-MM-DD-NN** · Tarih · Yapan · Kapsam · Etkilenen dosyalar · Doğrulama · Durum · Referans (commit).
> Kaynak kod sürüm kontrolü Git/GitHub'dadır; bu dosya insan-okunur değişiklik özetidir.

### DK-2026-08-04-40 — Sanatsal Baskı: Yüzeyler dokuları ayırt edilir hale getirildi, galeri büyüteci, form UX'i (ok ikonu/koyu menü/yanardöner etiket), 06+07 içerik tekrarı birleştirildi

- **Yapan:** Onur'un art arda dört notu üzerine Claude (PDM asistanı): (1) "Yüzeyler" rayındaki soyut renk kutuları ekran görüntüsünde neredeyse ayırt edilemiyordu — "şunları halletmemişsin"; (2) "Atölyeden" galerisindeki fotoğraflar için "üzerinde gezerken büyüteç çıksa süper olur"; (3) formda "Bilmiyorum — önerinizi isterim" ifadesi kötü, açılır kutularda yön oku yok, açılan menü şeffaf olsun, fontlar yanardöner olabilir; (4) "içerik olarak birbirini tekrar eden bişeyler olmasın, gereksizleri at".
- **1) Yüzeyler dokuları (`.rchip` — 6 malzeme):** Önceki gradyanlar birbirinden neredeyse ayırt edilemiyordu (hepsi ~%5-14 opaklıkta benzer koyu mor tonlar). Her malzemeye kendine özgü, iş mantığına uygun bir görsel imza verildi: **Mat** — parlama animasyonu tamamen kapatıldı (`::after{display:none}`), çünkü matın tanımı budur; **Yarı Mat/Parlak** — yumuşak, bulanık (blur) bir parlaklık; **Parlak** — güçlü, keskin ayna-vurgusu (dinlenirken bile hafif görünür, hover'da güçlenir); **Kanvas** — dokuma ızgarası opaklığı 3 katına çıkarıldı, artık göze çarpıyor; **Cotton Rag** — ilk kez sıcak tonlu (krem/fildişi) kağıt lifi benekleri eklendi, diğer beş malzemeden ayrı bir renk sıcaklığında (fine art kağıdının gerçek ayırt edici özelliği); **Bayrak Bezi & Paravan** — çapraz kumas dokusu belirginleştirildi. Fotoğraf yerine CSS/gradyan tercih edildi: gerçek doku makro fotoğrafı elde yok, sitenin varolan soyut/teknik görsel dili (izometrik SVG çizimler) ile tutarlı, ek HTTP isteği yok.
- **2) Galeri büyüteci (`.glens`):** "Atölyeden" (şimdi birleşik "06 — Finisaj") galerisindeki 6 fotoğrafa, yalnız ince işaretçili (fare) cihazlarda aktif olan bir zoom-lens eklendi — imleç üzerine geldiğinde 2.4x yakınlaştırılmış dairesel bir büyüteç fotoğrafı takip eder (klasik e-ticaret ürün zoom'u). `ince` (hover+fine pointer) deseni sayfanın kendi ray-sürükleme koduyla aynı; dokunmatik/kaba işaretçide devre dışı. **Bulunan hata:** `img.currentSrc` lazy-load nedeniyle ilk hoverda boş dönebiliyordu (görsel henüz yüklenmeye başlamadıysa) → `img.src`'e (her zaman dolu, bu görsellerde srcset yok) düşen bir yedek eklendi.
- **3) Form UX:** (a) 3 selectteki "Bilmiyorum — önerinizi isterim" → sade **"Önerinizi isterim"**; (b) her `<select>`'e sağda çift yönlü ok ikonu eklendi (inline SVG data-URI, dinlenirken `--mut` gri, hover/focus'ta `--acc2` camgöbeği) — `appearance:none` yüzünden tarayıcı okunun kaybolduğu, seçilebilir olduğunun belli olmadığı sorunu giderildi; (c) `color-scheme:dark` + koyu `<option>` arkaplanı eklendi — **sınırlama:** Chrome/Edge native açılır menü panelini OS seviyesinde çizer, tam alfa-şeffaflık (backdrop-blur ile sayfanın görünmesi) hiçbir tarayıcıda mümkün değil; `color-scheme:dark` en azından paneli sitenin koyu temasıyla tutarlı hale getiriyor (Firefox `option` arkaplanını tam onurlandırıyor). Tam özel/şeffaf açılır liste isteniyorsa native `<select>`'in JS ile inşa edilmiş bir listbox'a dönüştürülmesi gerekir — kapsam dışı bırakıldı. (d) Etiketler (AD SOYAD, E-POSTA vb.) sitenin kendi gradyan motifiyle (camgöbeği→mor→macenta, `.quote em` ile aynı) "yanardöner" hale getirildi.
- **4) İçerik tekrarı birleştirildi:** Eski soyut ikon-kartlı "06 — Finisaj" bölümü (Çerçeve, Dekota Kaşe, Fotoblok, Kasnaklı Germe, Parçalı Kanvas, Paravan & Bez — 6 SVG ikon+açıklama) ile hemen altındaki "07 — Atölyeden" fotoğraf galerisi **birebir aynı altı finisaj seçeneğini iki kez** anlatıyordu. İkisi tek bölümde birleştirildi: soyut ikon kartları tamamen kaldırıldı, gerçek fotoğraf galerisi "06 — Finisaj" başlığını (eski başlık "Sergilenmeye hazır teslim" + "Baskı yarısı; sunum diğer yarısı" korundu) devraldı. Artık kullanılmayan `.fin`/`.fcard`/`.fic` CSS kuralları (3 blok) temizlendi.
- **Doğrulama (localhost:8420):** Konsol hatası 0; `.gimg` sayısı 6, `.glens` oluşturma+imaj kaynağı doğrulandı (`img.src` yedeği çalışıyor); select arka plan-imgesi ve `padding-right:38px` uygulanmış; 3 select'in ilk/son seçeneği "Önerinizi isterim"; `06 — FİNİSAJ`/`07` tekrarı grep ile 0 sonuç. **Not:** Bu oturumun tarayıcı paneli arka planda olduğundan (compositing yok) `.glens` opaklık geçişi testte donuk göründü; geçiş özelliğini geçici olarak kapatınca sınıf-tabanlı davranışın doğru olduğu (0→1) doğrulandı — bu saf bir test-ortamı artefaktı (CSS transition, sayfa gerçekten çizilmeden ilerlemiyor), gerçek görünür sekmede sorun beklenmiyor; ekran görüntüsü bu nedenle alınamadı, görsel son teyit Onur'da.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-04-39 — Dış denetim kapama paketi: güvenlik, landmark, WebP, başlık hiyerarşisi, dokunma hedefleri, K6, Y10, post footer (hedef: bağımsız denetimde ~%99)

- **Yapan:** Onur'un "denetim raporundaki açık işleri kapa" + "bu raporla oturumdaki açık iş listesini birleştir" + "hedef bağımsız diğer denetimde %99" + "karar bekleyenler dışında hepsini sormadan hallet" talebi üzerine Claude (PDM asistanı, Fable). 8 ayrı commit'te uygulandı (928e6717…bu kayıt).
- **Güvenlik (dış #2, en düşük skor 75'ti):** `docs/htaccess-taslak.txt`'e tam başlık seti (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy; HSTS notlu/yorumda) + `mod_deflate` + `mod_expires` (IfModule korumalı; HTML no-cache, ?v='li varlıklar 1 yıl). Staging denetimlerinde de puanlansın diye **aynı CSP (frame-ancestors hariç) + referrer policy meta olarak 1.328 sayfaya** eklendi. CSP gerçek dış kaynak envanterinden yazıldı; tarayıcıda GA4 onay akışı, Google Fonts, Power Automate form fetch'i, Wistia/Maps iframe'leri, YouTube facade+nocookie test edildi — **ihlal 0**.
- **Erişilebilirlik (dış #3+#4, skor 78'di):** 1.325 sayfaya `<header>` (nav sarıldı) + `<main id="icerik">` + klavye odağında görünen "İçeriğe geç" skip-link (design-system). Ana sayfada 24px altı dokunma hedefi **26 → 0** (nav/dropdown/footer/yasal linklere görsel değişiklik olmadan padding; footer'da margin→padding kaydırmasıyla dikey ritim korundu).
- **Başlık hiyerarşisi (dış #7 + iç O8):** Site genelinde aşağı-yönlü başlık atlaması **186 sayfa → 0**: footer kolonları h4→h2 (196 sayfa), eğitimler/iletişim/başarı-öyküleri içerik h3→h2, postlarda a-cta/İlgili-Yazılar h3→h2, `.stitle` div'lerine `role="heading" aria-level="2"` (759 öğe), JS blog şablonu h4→h3 (80 sayfa), kalan dizilere jenerik aria-level düzeltmesi (görsel sıfır risk).
- **Performans (dış #5 + iç O12):** Ana sayfadaki tüm görseller artık modern formatta (11/11): 7 PNG logo WebP'ye çevrildi, gösterim boyutuna göre küçültülerek (176KB→50KB) — nav logosu (1.326 sayfa) ve footer logosu (site geneli) dahil; width/height nitelikleri yeni boyutlara güncellendi.
- **K6 (karar kalemiydi, onayla kapatıldı):** 102 Türkçe-karakterli mükerrer post ASCII ikizine birleştirildi: canonical→ikiz + noindex,follow; sitemap'ten 102 URL çıkarıldı (1209 kaldı); `blog-posts.json` 1129→1027; htaccess'e 102 adet 301; `feed.xml` temiz veriden yeniden üretildi.
- **Y10 (karar netleşti):** `/construction-cloud` hedefi `/autodesk-forma` **doğru** — site Forma platformunu ACC'nin halefi olarak modelliyor (Forma Build/Design Collaboration/Data Management). Asıl sorun 2-atlamalı 301 zinciriydi; htaccess'te iki kural da doğrudan `/autodesk-forma`'ya 301'e çevrildi.
- **Hızlı SEO (O2 kısmi + O3):** `Organization.logo` kare `assets/icon-512.png`'ye çevrildi; og:image'sız 229 metin postuna varsayılan og+twitter görseli eklendi (0 eksik kaldı).
- **Post footer (K5'in post ayağı):** 1.129 postun minimal footer'ı tam `footer-grid` ile değiştirildi (İzmir+Ankara, ürün/hizmet/iletişim kolonları h2 başlıklı, KVKK+Çerez Ayarları, 4 sosyal, WebP logo, `../` hrefler). Div dengesi 1.129/1.129 sağlam, tarayıcı doğrulaması temiz.
- **Kapanmayanlar (kayıt için):** K9 (2,46 GiB ham klasör taşıma — Onur kararı), D4 (Cadbim/CADBİM yazım kararı), yayın-günü kalemleri (#1 robots — ana depoda zaten doğru; #6 alan adı; #9 Search Console gönderimi), Y8-Faz2, O1 (664 post meta uzunluğu — içerik işi), O5 (ürün sayfası satır içi form), O7 (404 tasarımı), D5-D8.
- **Durum:** ✅ Paket tamamlandı, push edildi.

### DK-2026-08-04-38.1 — Kayan yazı şeritleri dikişsiz sonsuz döngü (ana sayfa + sanatsal baskı)

- **Yapan:** Onur'un "kayan yazı sonsuz olsun, sonuncunun ardına 1.'yi ekle" talebi üzerine Claude (PDM asistanı, Fable).
- **Kök neden:** Şerit içeriği 2 kopyaydı ve `translateX(-50%)` ile dönüyordu; tek kopyanın genişliği görünüm alanından darsa döngü sınırında boşluk görünüyordu. **Düzeltme:** index'te dizi 8 kopyaya çıkarıldı (yarım ~2.965px); sanatsal baskıda JS artık görünüm alanına göre yeterli (çift sayıda) kopya üretiyor. İki sayfada da `yarım ≥ viewport` doğrulandı — ek yeri artık görünmez.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-04-38 — Sanatsal Baskı: uygulama galerisi (eski siteden), sağ kenar sosyal ray, Proje Baskısı + Tarama hizmetleri

- **Yapan:** Onur'un üç talebi üzerine Claude (PDM asistanı): (1) "cadbim.com.tr'deki şu görselleri al ve bizim sayfaya entegre et ama dokuyu bozmadan"; (2) "cadbim_print Instagram + Facebook + sanatsal baskı WhatsApp'ını site genelindeki tarzda ekranın sağına"; (3) "hizmetlere proje baskısı ve tarama (HD/SD DesignJet'lerle)".
- **1) Uygulama galerisi ("07 — ATÖLYEDEN"):** Eski Wix sayfasındaki (cadbim.com.tr/sanatsalbaski) 9 ürün kartı görseli Wix CDN'den optimize indirildi (900px, q85, ~100-180KB; orijinaller 2-4,6MB'tı) → `assets/img/sanatsal/`. Onur'un "kağıt dokuları hiç belli olmuyor" geri bildirimi üzerine küratörlük: birbirinin tekrarı 3 "yarı mat" kartı çıkarıldı (dosyaları silindi), kalan **6 kart** finisaj odaklı sunuldu (başlık "Finisaj, iş üstünde."; yüzey/doku iddiası metinden çıkarıldı — doku farkı bu görsellerde okunmuyor, finisaj farkı okunuyor). Kartlar sayfanın kart dilinde (bg2 + ln çerçeve + 18px radius, data-rv reveal); 3 sütun / ≤900px'te 2 sütun (mobilde 2 sütun korunur — guardrail tercihi).
- **2) Sol kenar sosyal ray (`#print-rail`):** `social-widget.js` v5 çekmece deseninin sayfaya gömülü kopyası (ilk istekte sağa konumlandı; Onur'un düzeltmesiyle site geneliyle aynı hizaya, sola alındı) — Instagram `cadbim_print` (doğrulandı), Facebook `cadbimizmir` (print'e özel FB sayfası web aramasında bulunamadı; kurumsal sayfa bağlandı, ayrı sayfa varsa değiştirilecek), WhatsApp `wa.me/905547403757`. Dokunmatikte ilk dokunuş rayı açar; reduced-motion'da geçişler kapalı.
- **3) Hizmetler 5 → 7:** "06 Proje Baskısı" (CAD çıktısı, pafta, poster, mat film) ve "07 Tarama Hizmetleri" (HP DesignJet **HD Pro / SD Pro** tarayıcılarla geniş format) eklendi; bsub "Beş disiplin…" → "Yedi hizmet, tek titizlik…". Eski "Teknik çizim mi gerekiyor?" kutusu Proje Baskısı ile mükerrer kalacağından donanım açısına çevrildi ("Kendi makinenizle basmak isterseniz" → DesignJet satış/servis). Marquee'ye PROJE BASKISI + TARAMA, form "Baskı Türü" listesine iki yeni seçenek eklendi.
- **Doğrulama (localhost:8420):** 7 `.wrow`, 6/6 galeri görseli yüklü, ray sağda sabit (z-index 9990), form 8 seçenek, marquee 22 span (11×2 kopya), yatay taşma 0, konsol hatası 0. Tarayıcı paneli arka planda olduğundan ekran görüntüsü alınamadı — görsel son teyit Onur'da.
- **Not:** Bu oturumun görsel indirme işlemi sırasında 9 görselin tamamı paralel oturumun süpürme commit'ine girmişti; bu commit 3 gereksiz görseli siler.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-04-37 — Ray hover'ında kutu değil içindeki logo büyüyor

- **Yapan:** Onur'un "kutular büyüsün istemedim, içindeki 'in' mesela büyüsün" düzeltmesi üzerine Claude (PDM asistanı, Fable).
- **Yapılan (`social-widget.js` v5):** Hover/odaktaki `scale(1.18)` kutudan (`<a>`) kaldırıldı — kutu artık yalnızca dışarı kayıyor, boyutu sabit. Büyüme ikonun kendisine taşındı: `svg`'ye aynı yaylanmalı geçişle `scale(1.3)` (22px → ~29px, 36px kutu içinde taşmadan). `prefers-reduced-motion`'da svg geçişi de kapalı. Cache bust: `?v=4` → `?v=5` (196 sayfa).
- **Doğrulama:** CSSOM'da kutu üzerinde scale kuralı kalmadığı, `a:hover svg { scale(1.3) }` ve svg geçiş kuralının yüklendiği doğrulandı; v5 aktif, konsol hatası 0.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-04-36 — Sosyal medya rayındaki logolar büyütüldü (22px masaüstü / 18px mobil)

- **Yapan:** Onur'un "kutuların içindeki logoları biraz büyüt de daha görünür olsun" talebi üzerine Claude (PDM asistanı, Fable).
- **Yapılan (`social-widget.js` v4):** İkon SVG boyutu masaüstünde 18-19px → **22px** (38px kutuda), mobilde 15px → **18px** (32px kutuda) — CSS kuralıyla merkezi olarak (`#social-rail a svg`). Gömülü (çekmece) durumda görünür kısımda artık daha iri logo okunuyor. Cache bust: `?v=3` → `?v=4` (196 sayfa).
- **Doğrulama:** Yerel önizlemede v4 yüklendi; masaüstü 22px kuralı ve mobil 18px media kuralı CSSOM'da doğrulandı (panel arka planda 0x0 olduğundan canlı ölçüm mobil kırılıma düştü — beklenen davranış, kural seti doğru). Konsol hatası 0.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-04-35 — Sanatsal Baskı sayfası dil cilası: zorlama/"keko" ifadeler inceltildi, havalı-sakin ton korundu

- **Yapan:** Onur Bozok'un "sanatsal baskıda dil biraz keko; havalı olmalı ama 'şey' gibi ifadelerden kaçınmalıyız" talebi üzerine Claude (PDM asistanı).
- **Kriter:** Sayfanın sanat yönetimi (kısa, ritmik, iddialı cümleler) korunur; ancak dolgu sözcükler ("şey"), kendini öven sıfatlar ("prestijli"), tele-alışveriş kalıpları ("HAZIR MISINIZ?") ve sen-kipi kaymaları giderilir.
- **Değişiklikler (`cadbim_sanatsal_baski.html`, 6 satır):**
  - Hero: "Duvara astığınız **şey** artık bir çıktı değil — bir eser." → "**Duvarınıza asılan** artık bir çıktı değil — bir eser."
  - Hero ikincil CTA: "Atölyeyi gör" (sen-kipi) → "Atölyeyi inceleyin".
  - İstatistik: "kıl payı detay" → "kıl inceliğinde detay".
  - Süreç/3: "Renk doğruluğu pazarlık konusu değil." → "Renk doğruluğundan ödün verilmez."
  - Alıntı: "birçok **prestijli** serginin" → "pek çok serginin" (iddia sergi sayısı ve zamanında teslimle zaten kurulu).
  - CTA başlığı: "BASKIYA / HAZIR MISINIZ?" → "BASKIYA / BAŞLAYALIM."
- **Takip (Onur'un 2. tur notları, aynı gün — 5 satır):**
  - "Fiyat" sözcüğü metinlerden çıkarıldı ([[cadbim-fiyat-gosterilmez]] ilkesinin dil düzeyine genişletilmesi): "aynı gün fiyat dönüşü yapalım" → "teklifinizi aynı gün iletelim"; form notu + JS başarı mesajı "Talebinize aynı gün dönüş yapıyoruz…"; WhatsApp kartı "hızlı fiyat alın" → "aynı gün teklif alın"; kapanış notu "fiyat dönüşü aynı gün" → "teklifiniz aynı gün elinizde".
  - "Şehir dışı işler **itinayla paketlenir**" (pideci tabelası çağrışımı) → "Şehir dışı işler, sergilenmeye hazır halde **korumalı ambalajla yola çıkar**."
- **Takip (3. tur, aynı gün — 3 satır):** Onur'un "teklif al yerine ne olabilir?" sorusu üzerine sunulan seçeneklerden "öneri + dönüş + yanıt" karışımı onaylandı ("önerin olsun"). "Teklif" sözcüğü bu sayfanın atölye tonuna yumuşatıldı: CTA girişi "teklifinizi aynı gün iletelim" → "**önerimizi** aynı gün iletelim"; WhatsApp kartı "aynı gün teklif alın" → "aynı gün **dönüş** alın"; kapanış notu "teklifiniz aynı gün elinizde" → "**yanıtımız** aynı gün elinizde". Ana sitedeki "Teklif İste" CTA'sı kurumsal bağlamda korunuyor.
- **Kapsam dışı (bilinçli):** "Ham dosya girer. Eser çıkar.", "Kadrajdan koleksiyona.", "Baskı yarısı; sunum diğer yarısı." gibi sayfanın karakterini kuran kısa cümleler korundu. "KAYDIR" / "SÜRÜKLE / KAYDIR" mikro-etiketleri bu tür sayfalarda tür-standardı görsel ipucu olduğundan bırakıldı. `<head>` meta metinleri zaten kurumsal, dokunulmadı.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-04-34 — Kurumsal ton denetimi: arayüz-talimatı ifadeleri ("üzerine gelin / tıklayın / seçin") açıklayıcı metinlerle değiştirildi

- **Yapan:** Onur Bozok'un "'Alanınızın üzerine gelin…' ve 'endüstrinizi seçin…' gibi profesyonel gözükmeyen ifadeler istemiyorum; siteyi sadece text olarak incele" talebi üzerine Claude (PDM asistanı, marketing:brand-review skill'i ile).
- **Kök neden / kriter:** Bölüm alt metinlerinde kullanıcıya arayüzü nasıl kullanacağını komut kipiyle anlatan mikro-metinler ("üzerine gelin", "tıklayın", "seçin", "sürgüyü kaydırın") kurumsal tonla çelişiyordu. Kriter: metin arayüz işlemini değil, sunulan değeri/içeriği anlatmalı. Kısa CTA buton etiketlerinden "Teklif İste" yerleşik standart CTA olarak korundu; "Hemen Ara" ise Onur'un takip onayıyla değiştirildi (aşağıda).
- **Değişiklikler (32 dosya, 34 satır):**
  - `index.html` (3): Sektör Seçici alt metni → "Yazılım, donanım ve eğitim çözümlerimizi her sektörün kendi iş akışına göre yapılandırıyoruz."; Çözümler alt metni → "Her endüstri için öne çıkan çözüm alanlarını bir arada sunuyoruz."; Akreditasyonlar alt metnindeki "Logoya tıklayarak…" cümlesi kaldırıldı.
  - **19 DesignJet ürün sayfası:** tur ipucu "Detayları görmek için görsel üzerindeki numaralara tıklayın." → "Görsel üzerindeki numaralı noktalar, ürün özelliklerinin detaylarını gösterir."
  - `cadbim_designjet.html`: video bölümü alt metnindeki "— oynatmak için tıklayın" ibaresi kaldırıldı.
  - **3 koleksiyon sayfası** (AEC/M&E/PD&M): "Ürün sayfası olanları tıklayıp inceleyebilirsiniz." → "Ürün sayfası bulunan yazılımların detaylarına bağlantılar üzerinden ulaşabilirsiniz."
  - **6 sektör sayfası** (mimari, makine, otomotiv, insaat, tesisat, icmimarlik): "İlgili çözüm sayfalarını inceleyin — … görün" → "İlgili çözüm sayfalarında, her çözümde kullanılan ürünleri de bulabilirsiniz".
  - `cadbim_autodesk.html`: sen-kipindeki "Yazılımı satın al, hemen eğitime başla — aynı çatı altında." → "Yazılım tedariki ve yetkili eğitimi aynı çatı altında sunuyoruz."
  - `cadbim_sanatsal_baski.html`: "Sürgüyü kaydırın, farka bakın." → "Baskı öncesi ve sonrası arasındaki farkı karşılaştırma görselinde inceleyebilirsiniz."
  - **Takip (Onur onayı):** 3 sayfada (`cadbim_iletisim`, `cadbim_teklif_iste`, `cadbim_designjet_teknik_servis`) hızlı bağlantı etiketi "Hemen Ara" → "Telefonla Ulaşın" → (Onur'un ikinci revizyonuyla) "Telefon".
- **Doğrulama:** Site genelinde `üzerine gelin | tıklayın/tıklayarak/tıklayıp | Endüstrinizi seçin | Sürgüyü kaydırın | satın al, hemen` kalıpları için grep → görünür sayfa metinlerinde **0 eşleşme** (blog yazılarındaki ürün işlevi anlatımları — ör. "tek bir tıklama ile gerber dosyaları" — Autodesk kaynaklı içerik olduğundan kapsam dışı). Tur ipucu statik metindir, JS yalnızca ilk pin seçiminde gizler — davranış değişmedi.
- **Durum:** ✅ Tamamlandı.

### DK-2026-08-03-33 — Beyaz zeminli iç görseller kaldırıldı; eksik ikonlar subset fontuna eklendi

- **Yapan:** Onur Bozok'un "beyaz backgroundlu görsel istemiyorum sitede, ya png yapalım ya da kaldıralım" (karar: *"Adobe gibi marka logosuysa kaldırma, ama iç görsellerdense kaldır"*) ve "ikonsuz kutular var, bunu gider ve tüm site için uygula" talepleri üzerine Claude (PDM asistanı).

**A) Beyaz zeminli görseller**
- **Tarama:** 365 görsel dosyası, her birinin 8 kenar/köşe noktası örneklenerek opak-beyaz zemin tespiti yapıldı. 99 dosya beyaz çıktı; bunların yalnızca **17'si HTML'de fiilen referanslıydı** (kalanı kullanılmayan HP basın-kiti kaynak dosyaları).
- **Karar ayrımı (Onur):** marka logoları kalacak, içerik görselleri kaldırılacak.
  - **Kalan (3):** `meshmixer.png`, `tinkercad-icon.png`, `veras.png` — ürün/marka logoları, dokunulmadı.
  - **Kaldırılan (11 `<img>`):** `gallery-hdpro-2`, `gallery-sdpro-1`, `gallery-t1700-1` (2 sayfada), `gallery-t600-1`, `gallery-t830-1`, `gallery-z6pro-1`, `gallery-z6ps-2`, `gallery-z9pro-1`, `gallery-z9ps-1`, `gallery-z9ps-2`.
  - **Düzen onarımı:** görselin gitmesiyle boşta kalan 2 sütunlu kalıplar tek sütuna alındı — `.sh sh-img2` → `.sh` dönüşümü, ve `cadbim_designjet.html`'de görselden boşalan kenarlıklı kutu ile onu saran `grid-template-columns:1.1fr 1fr` sarmalayıcısı kaldırıldı (aksi halde sayfada boş çerçeveli bir kutu kalıyordu).
  - **Değiştirilen (1):** `graphics-z6pro.jpg` bir kategori banner'ının arka planıydı; kaldırılsa 5'li banner setinde (01-05) tek görselsiz banner kalacaktı. Aynı ürünün koyu zeminli görseli `gallery-z6pro-2.jpg` ile değiştirildi — set tutarlı kaldı.
  - **Video posterleri (3):** `graphics-z6pro-poster`, `office-t1600-poster`, `photo-z9pro-poster` — `<video poster="...">` attribute'ları kaldırıldı; videolar `controls` ile duruyor, önizleme artık beyaz yerine koyu.
- **Doğrulama:** Kullanımdaki beyaz görsel sayısı **17 → 3** (yalnızca kasıtlı bırakılan logolar). Etkilenen 10 DesignJet sayfası masaüstünde (1400px) tarandı: kırık görsel 0, boş kenarlıklı kutu 0, yatay taşma 0. Mobilde (375px) `designjet`, `designjet-t1700`, `designjet-z9ps` kontrol edildi — taşma 0.

**B) İkonsuz kutular**
- **Kök neden:** Site tam Tabler setini değil, `scripts/build_icon_subset.py` ile üretilen bir **subset font** kullanıyor. Sayfalara sonradan eklenen ikon sınıfları subset'e işlenmediği için o kutular boş görünüyordu.
- **Tarama:** 298 farklı `ti-*` sınıfı kullanılıyordu, subset'te 295 vardı → **9 sınıf eksik** (14 kullanım): `ti-rocket`, `ti-signature`, `ti-forms`, `ti-eye-off`, `ti-sun-moon`, `ti-transform`, `ti-table-options`, `ti-tree`, `ti-history-toggle`. Onur'un bildirdiği `bim-icerik-uretimi` sayfasındaki iki boş kart `ti-transform` ve `ti-table-options` idi.
- **Çözüm:** Subset betiği yeniden çalıştırıldı (295 → **303 ikon**, font 56,9 → 57,7 KB); betik "karşılığı olmayan sınıf" uyarısı vermedi, yani 9 ismin tamamı Tabler 3.31.0'da mevcuttu. Font+CSS içeriği değiştiği için sürüm `v=3 → v=4` (CSS'teki @font-face URL'i, 1325 HTML'deki link ve betikteki sabit birlikte).
- **Doğrulama:** kullanılan−tanımlı farkı **0**. Font dosyası fontTools ile açılıp her yeni ikonun codepoint'inin cmap'te bulunduğu teyit edildi ("CSS'te tanımlı ama fontta olmayan: 0"); tarayıcıda `ti-transform` ve `ti-table-options` 22×22 görünür.
- **Not:** Yeni bir ikon sınıfı kullanıldığında `python scripts/build_icon_subset.py` çalıştırılmalı — aksi halde ikon boş görünür.
- **Durum:** ✅ Her iki iş de tamamlandı ve ölçümle doğrulandı.

### DK-2026-08-03-32 — Filtre çipleri ve buton gruplarındaki dağınık mobil dizilim düzeltildi (site geneli kural)

- **Yapan:** Onur Bozok'un "filtredeki dağınık görünüm kötü gözüküyor, boyutlar farklı, buna bir çözüm bul ve benzer problemi tüm sitede gider" + "flex-wrap'li tüm yapıları bul ve düzeltmeleri uygula" talebi üzerine Claude (PDM asistanı).
- **Kök neden:** Filtre/sekme çip grupları `display:flex; flex-wrap:wrap` kullanıyordu; çipler içeriğe göre genişlediği için her satıra farklı sayıda ve farklı genişlikte diziliyor, sağda düzensiz boşluklar bırakıyordu. Ölçülen (375px): `cozumler` → 10 çip **7 satıra** dağılmış, satır içi genişlik farkı **60px**; `endustriler` 70px; `autodesk` 63px; `egitimler` 49px; anasayfa 44px.
- **Tarama:** Sitedeki **45 farklı** `flex-wrap:wrap` selektörü çıkarıldı ve kategorize edildi — (a) filtre/sekme çipleri: eşitlenmeli, (b) CTA/buton grupları: tam genişlik olmalı, (c) küçük etiket/rozet grupları (`.tags`, `.cpills`, `.sol-meta`, `.prod-tags` vb.): sarma doğal, **dokunulmadı**, (d) footer/breadcrumb düzenleri: dokunulmadı.
- **Kural (mobile-guardrails.css, ≤600px):**
  - **R8** — `.cz-fbtns`, `.ind-tabs`, `.catalog-tabs`, `.soltabs-nav`, `.pfilter` → eşit genişlikli **2 sütunlu ızgara**; çipler sola hizalı, sayaç rozetleri `margin-left:auto` ile sağa yaslı (sütunlar hizalı okunuyor); `.pfilter` içindeki arama kutusu `grid-column:1/-1` ile tam satır.
  - **R9** — `.cta-btns`, `.btns`, `.h-ctas` → dikey yığın + tam genişlik + ortalı içerik.
- **Kapsam dışı:** `.filterbar` (cadbim_urunler.html) kasıtlı olarak tek satır + yatay kaydırmadır (`overflow-x:auto`); doğrulamada taşan 5 çipin bu kaydırma kabında olduğu teyit edilip kural dışında bırakıldı.
- **Sonuç (ölçülen):** Tüm çip gruplarında satır içi genişlik farkı **60-70px → 0**; `cozumler` 7 satır → **5 satır**. `.cta-btns` 164/174px → **237/237px**.
- **Doğrulama (localhost:8420, 375px):** 6 filtre kalıbı + `.pfilter` içeren **18 sayfanın tamamı** (15'i arama kutulu, 3'ü — basari-oykuleri/blog/webinar — arama kutusuz varyant, ayrıca doğrulandı) ölçüldü: genişlik farkı 0, çip taşması 0, metin taşması 0, sayfa taşması 0. Masaüstünde (1400px) `.cz-fbtns`/`.ind-tabs`/`.pfilter`/`.cta-btns` hâlâ `display:flex` — kurallar yalnızca mobilde devrede, regresyon yok.
- **Not:** Bu oturumun tarayıcı paneli screenshot üretemedi; doğrulama ölçüm tabanlı yapıldı, görsel son teyit Onur'da.
- **Durum:** ✅ Kural yazıldı, site geneline uygulandı, ölçümle doğrulandı.

### DK-2026-08-03-31 — Çözüm sayfalarındaki marka logoları çerçeveden çıkarıldı ve büyütüldü

- **Yapan:** Onur Bozok'un "çözümler sayfalarında çalıştığımız markaların logoları aşırı küçük, bunları çerçevesiz yapalım ve logoları büyütelim; bu tüm sitede geçerli bir kural olsun" talebi üzerine Claude (PDM asistanı).
- **Kök neden:** `.cz-brand-logo` **38×38px kare** kutuydu ve üstüne `padding:7px` + arka plan + kenarlık vardı → logoya kalan alan yalnızca **24×24px**. Marka logolarının çoğu yatay wordmark olduğu için kare alana sığdırılınca yükseklikleri çöküyordu. Ölçülen gerçek render: **Autodesk 22×2px** (doğal oran 300×31 = 9,7:1 — pratikte görünmez bir çizgi), Adobe 22×12px, HP 22×22px.
- **Kural:** Marka logoları arka planlı/kenarlıklı kare kutulara hapsedilmez; kutu logonun en-boy oranına uyar. `.cz-brand-logo` artık **78×40px, çerçevesiz** (arka plan/kenarlık/padding kaldırıldı); `.cz-brands` ızgarası 210→238px'e genişletilerek metne yer bırakıldı.
- **Sonuç (ölçülen):** Autodesk 22×2 → **78×8** (≈4×), Adobe 22×12 → **74×40** (≈3,4×), HP 22×22 → **40×40**. Kural `design-system.css`'te tek yerde tanımlı olduğu için **19 çözüm sayfasının tamamı** tek değişiklikle güncellendi.
- **Bilinçli olarak kapsam dışı bırakılanlar (kod içinde de belgelendi):**
  - `.pico` (ürün kataloğu, 17 sayfa): ölçüldü — zaten çerçevesiz (şeffaf zemin) ve logolar 42px. Kuralla hizalı, değişiklik gerekmedi.
  - `.xp-logo` (çapraz satış şeritleri, 10 sayfa): önce genel kural uygulandı, sonra **geri alındı**. Sayfadan sayfaya farklı varyantları var: `cadbim_autodesk.html`'de kutu 48px ve arka plan her ürünün **marka rengine göre kodlanmış** (hover'da o renkte parlıyor) — orada arka plan bir "çerçeve" değil, bilgi taşıyan tasarım öğesi. Tek tip kural bu sayfada kutuyu 48→40px küçültüp tasarımı bozuyordu; regresyon fark edilip geri alındı ve gerekçe CSS yorumuna yazıldı.
- **Doğrulama (localhost:8420):** `.cz-brand`/`.xp-logo` içeren 25 sayfa gizli iframe'lerle hem masaüstü (1400px) hem mobil (375px) genişlikte tarandı; her logo için kısa kenar <7px (ezilme), kutuda arka plan/kenarlık (çerçeve), kart ve metin taşması ölçüldü. **Sonuç: 0 ezilme, 0 çerçeve, 0 taşma.** `.xp-logo` geri alma sonrası autodesk 48×48 (marka renkli) ve hp/chaos 42×42 (gri) orijinal değerlerine döndüğü teyit edildi.
- **Not:** Bu oturumun tarayıcı paneli screenshot üretemedi; doğrulama ölçüm tabanlı (`getBoundingClientRect`/`getComputedStyle`) yapıldı, görsel son teyit Onur'da.
- **Durum:** ✅ 19 çözüm sayfası güncellendi, kapsam dışı bırakılanlar gerekçesiyle belgelendi.

### DK-2026-08-03-30 — Mobil düzenleme kuralları kural setine dönüştürüldü ve site geneline uygulandı (`mobile-guardrails.css`)

- **Yapan:** Onur Bozok'un "mobil tarafında yaptığımız düzenlemeleri bir kural silsilesi olarak al ve tüm site için bunu çalıştır" talebi üzerine Claude (PDM asistanı).
- **Bağlam:** Bu turdan önce mobil düzeltmeler sayfa sayfa yapılıyordu (iletişim formu, eğitimler hero'su, hakkımızda grid'leri). Aynı hata sınıfları başka sayfalarda da vardı; tek tek avlamak yerine kalıcı bir kural katmanı oluşturuldu.
- **Yeni dosya:** `assets/css/mobile-guardrails.css` — **1328 HTML dosyasının tamamına** `</head>` hemen öncesine eklendi. Bu konum kritik: sayfa içi `<style>` bloklarından ve `tpl-*.css`'ten sonra yüklendiği için aynı özgüllükteki kuralları ezer.
- **Kural seti:**
  - **R1** — Breadcrumb'lar (`.crumb/.hero-crumb`) mobilde sarar; uzun ürün adları viewport dışına taşıyordu (ör. `hp-zbook`).
  - **R1b** — Satır içi (`style="..."`) çok sütunlu grid'ler mobilde tek sütuna iner. Sınıf tabanlı kuralla ezilemedikleri için `!important` gerekti. 6 örnek vardı; en ağırı `surdurulebilirlik` sayfasında iç içe geçmiş grid yüzünden kartları **45px genişliğe** sıkıştırıyordu.
  - **R2** — Uzun kelimeler (`overflow-wrap:anywhere`) taşma yerine kırılır.
  - **R3** — `img/svg/video/iframe/canvas{max-width:100%}` (global, tek genel kural).
  - **R4** — `.form-row/.form-grid` mobilde tek sütun.
  - **R5** — `.g3/.g4` mobilde **2 sütun** (tek sütun değil) — Onur'un "alt alta kaydır kaydır bitmeyen yapıları istemiyorum, mümkün olduğunca ekrana sıkışsınlar ama okunacak şekilde" talimatı doğrultusunda.
  - **R5b** — Yalnızca ≤340px cihazlarda (Galaxy Fold kapalı) tek sütuna iner; 360-430px arası yaygın telefonlarda 2 sütun korunur.
  - **R6** — Geniş tablolar kabı taşırmak yerine yatay kaydırılır.
  - **R7** — Grid/flex çocuklarına `min-width:0` (içerik kaynaklı taşmayı keser).
  - **Hero istatistik şeritleri** (`.hero-stats/.hstats`) 2'şerli sarar; `dijital-donusum`'da 4 kutu yan yana eziliyordu.
- **Yükleme sırası düzeltmesi:** 9 `sektor_*.html` sayfasında `design-system.css` sayfa içi `<style>`'dan **önce** geliyordu (kaskadda kaybediyordu); `</head>` öncesine taşındı.
- **Doğrulama (localhost:8420):** 197 sayfanın **tamamı** gizli iframe'lerle 375px'te otomatik tarandı — yatay taşma, viewport dışına çıkan öğe ve <115px'e sıkışmış grid sütunu ölçüldü. Denetim, kasıtlı yatay kaydırma şeritlerini (`overflow-x:auto` kabı olan sektör/filtre/model şeritleri) gerçek hatalardan ayırt ediyor. **Sonuç: 0 gerçek hata.** Kalan 2 uyarı kasıtlı tasarım (hakkımızda 3'lü rozet grid'i; sanatsal-baskı dekoratif `orb`/marquee öğeleri). Tablet (768px) ve masaüstü (1400px) regresyon kontrolü yapıldı — taşma yok, görseller normal.
- **Yan kazanç:** Sayfa yükseklikleri kısaldı (2 sütun sayesinde): `bim` 14862→13757px, `designjet` 17097→15943px, `surdurulebilirlik` 5874→5264px.
- **Not:** Bu oturumun tarayıcı paneli screenshot üretemedi; doğrulama ölçüm tabanlı (getBoundingClientRect / getComputedStyle) yapıldı, görsel son teyit Onur'da.
- **Durum:** ✅ Kural seti yazıldı, 1328 dosyaya uygulandı, 197 sayfa taranarak doğrulandı.

### DK-2026-08-03-29 — İletişim sayfasındaki Google Haritası yanlış konumu gösteriyordu; koordinat düzeltildi

- **Yapan:** Onur Bozok'un "iletişim alanında Google Maps'te tam lokasyonumuz gözükmüyor bunu düzelt" talebi üzerine Claude (PDM asistanı).
- **Kök neden:** Sitede kayıtlı koordinat (38.4895, 27.0389) gerçek binadan **boylamda ~2,5 km batıya** kaymıştı. Ayrıca gömülü harita `iframe`'inin `pb=` parametresi elle uydurulmuş sahte bir Google Place ID (`0x14bbd8b2f9e25a9b:0x0`) ve sahte zaman damgası (`4v1234567890`) içeriyordu — Google'ın gerçek "Haritayı Yerleştir" akışından hiç geçmemiş bir string.
- **Doğrulanan gerçek konum:** Yandex Haritalar'da "Cadde Anadolu Kaşarcı Plaza" adıyla, CADBİM'in bu binada yer aldığı teyit edilerek bulundu: **38.490245, 27.067452**. Bağımsız ikinci kaynak (OpenStreetMap/Nominatim) Anadolu Caddesi'nin Çiğli'deki segmentlerini aynı posta kodunda (35620) ve aynı boylam aralığında (27.04–27.07) doğruladı — eski değerin (27.0389) yanlış olduğunu destekledi.
- **Düzeltilen dosyalar:** `cadbim_iletisim.html` (JSON-LD `GeoCoordinates` + harita `iframe` src) ve `index.html` (ana sayfadaki `LocalBusiness` şemasının `GeoCoordinates`'ı) — eski hatalı koordinat sitede yalnızca bu iki dosyada geçiyordu.
- **Yeni harita embed'i:** Sahte `pb=` string'i yerine anahtarsız, güvenilir `https://maps.google.com/maps?q=LAT,LNG(Etiket)&z=16&output=embed` biçimi kullanıldı — pin, iş yeri adı Google'ın kendi dizininde eşleşmese bile her zaman verilen koordinata düşüyor.
- **Doğrulama:** Embed URL'sine doğrudan gidildiğinde Google, verdiğimiz koordinatlardan kendi `pb=` parametresini otomatik türetip yönlendirdi (`!1s38.490245,27.067452!6i16`) — söz dizimini geçerli kabul ettiğini kanıtlıyor. **Not:** Bu oturumun tarayıcı paneli piksel render/screenshot üretemediği için haritanın son halini görsel olarak ekrana getirip gösteremedim; canlıya alındığında Onur'un bir kez göz atıp teyit etmesi iyi olur.
- **Durum:** ✅ Koordinat ve embed URL'si düzeltildi; görsel son teyit Onur'da.

### DK-2026-08-03-28 — Ürün/çözüm/endüstri sayfalarındaki "İlgili İçerikler" widget'ına Blog'a giden filtreli "Tümünü gör" bağlantısı

- **Yapan:** Onur Bozok'un "5 videodan fazlasını görmek isteyenleri blog sayfamıza ilgili filtre ile gönderen bir link olmalı hem ürünlerde hem endüstrilerde hem çözümlerde" talebi üzerine Claude (PDM asistanı).
- **Bağlam:** Önceki turda doğrulanan davranış (YouTube→blog otomatik senkron; ürün/çözüm/endüstri sayfalarında konuya göre en yeni 5 içerik) korunuyor; eksik olan tek şey, 5'in ötesindeki içeriğe ulaşma yoluydu.
- **Kapsam:** `blogRelatedGrid` widget'ını barındıran **79 sayfa** (ürün sayfaları + çözüm sayfaları + 8 `sektor_*.html` endüstri sayfası) — script bloğu tüm dosyalarda bayt-bayt özdeşti (MD5 doğrulandı), tek bir Python betiğiyle (`scripts/` dışı, scratchpad) toplu değiştirildi.
- **Widget tarafı:** Filtrelenmiş+sıralanmış tam liste artık `allMatched` değişkeninde tutuluyor; ekrana basılan `matched` bunun `slice(0,5)`'i. `allMatched.length>5` olduğunda grid'in altına `Tüm N içeriği gör` bağlantısı ekleniyor → `blog?topic=<konu>` (temiz URL şemasıyla uyumlu, relative href).
- **cadbim_blog.html tarafı:** `filtered()` içindeki `prodOk` kontrolüne `|| p.cat===activeProd` eklendi (var olan ürün-chip davranışını bozmadan, artık kategori-tipi konuları da kabul ediyor). Sayfa yüklenince `location.search`'ten `?topic=` okunuyor, `activeProd`'a atanıyor, eşleşen chip (kategori veya ürün filtresinde) varsa görsel olarak aktif işaretleniyor, `render(true)` çağrılıyor.
- **Doğruluk garantisi:** Widget'ın kullandığı eşleştirme (`products.indexOf(topic) || cat===topic`) ile blog.html'e eklenen mantık birebir aynı — yani `?topic=X` her zaman widget'ın `allMatched` listesiyle tam örtüşüyor, ayrı bir bakım noktası yok.
- **Doğrulama (localhost:8420):** 47 benzersiz `data-topic` değeri `blog-posts.json` karşısında taranıp sınıflandırıldı — 0 eşleşen (bölüm gizleniyor, önceden var olan davranış), 1-5 eşleşen (link yok, doğru), 5'in üzeri (link var). Sınır durumu AutoCAD LT (tam 6) canlı test edildi: link doğru metinle çıktı, mobilde (375px) taşma yok. AutoCAD (48) ve sektor-mimari→BIM (299) üzerinden linke gidiş: blog sayfasında doğru sonuç sayısı ve doğru chip vurgusu doğrulandı.
- **Not:** Bazı `data-topic` değerleri (Autodesk Docs, Dynamo, Genel, HP Build Workspace, Netfabb, Robot Structural vb.) blog sayfasındaki mevcut chip listesinde karşılığı yok — filtreleme yine de doğru çalışıyor, sadece o durumda hiçbir chip görsel olarak aktif işaretlenmiyor (kozmetik, işlevi etkilemiyor).
- **Durum:** ✅ 80 dosya (79 widget + cadbim_blog.html) güncellendi ve doğrulandı.

### DK-2026-08-03-27 — Ana sayfa görsel tutarlılık turu: sektör/çözüm sahneleri ortalama, Sanatsal Baskı sıra dengesi, marka rozeti kartları

- **Yapan:** Onur Bozok'un art arda dört bulgusu üzerine Claude (PDM asistanı): (1) ekran görüntüsüyle "bazı endüstri görselleri karenin içine tam ortalanmış değil", (2) "ana sayfadaki marka logolarının olduğu alandaki beyaz arka planlar gözümü tırmalıyor... sitenin genelinden farklı ve kalitesiz görünüyor", (3) "çözümler de görsellerde ortalama problemi var gibi, sanatsal baskı altta tek duruyor", (4) "footer'daki whatsapp ibaresine gerek yok, zaten sağ altta buton var".
- **1) Sektör illüstrasyonları ortalama (Endüstriler paneli, `assets/img/sektor/*.svg`):** Tarayıcıda piksel taraması ile her sahnenin görünür kütle merkezi ölçüldü; icmimarlik ([+41,+29] kayık), tesisat ([-36,+80]), mimari/insaat/otomotiv/medya küçük kaymalarla tespit edildi. `scripts/gen_sektor_visuals.py`'a sahne-bazlı `OFFSETS` sözlüğü + `apply_offset()` eklendi (translate/scale, sahne çıktısına dokunmadan). makine/eğitim/havacılık kasıtlı olarak dışarıda bırakıldı (kompozisyon gereği kenara taşan öğeler var, kaydırmak bozardı). Doğrulama: 6 sahne de [0,0] sapmaya indi.
- **2) Çözümler paneli 3B görüntüleyici (`assets/js/home-3d.js`, `cozumSvg`):** Kök neden farklıydı — statik SVG değil, tarayıcıda canlı çizilen izometrik model; mevcut kod yörünge (orbit) dönüşü sırasında ilk kareye göre hesaplanmış sabit `offX/offY` kullanıyordu, model döndükçe kadraj dışına kayıyordu. `renderObj()` her karede projeksiyon kutusunu yeniden ölçüp merkezliyor artık. Doğrulama: mimari/tesisat/medya sahnelerinde 5 kare boyunca sapma sürekli [0,0].
- **3) Sanatsal Baskı yalnız satırda kalıyordu (10 sekme çipi):** `.soltabs-nav{max-width:700px}` eklendi; genişlik kısıtı çipleri 5+5 dengeli iki satıra böldü (önce 9+1). Ek CSS/JS gerekmedi, gerçek metin genişlikleriyle doğrulandı.
- **4) Marka rozeti kartları (Yetkilendirmeler bölümü, `#hakkimizda .cred-row1`):** Eski tasarım her logoyu büyük beyaz `<a>` kutusuna koyuyordu — sitenin lacivert temasıyla çakışıyordu. Kart arka planı site genelindeki cam-yüzey stiline (`var(--srf)`, ince kenarlık) çevrildi. Autodesk/HP/SketchUp/Lumion/UltiMaker/Microsoft şeffaf-kesim logo oldukları için mono beyaz filtre (`brightness(0) invert(1)`) uygulanabildi. **Adobe ve Chaos hariç tutuldu:** kaynak dosyaları (`adobe-gold-reseller.png`, `chaos-logo-red.svg`) zaten kendi opak/renkli rozet kartı olarak tasarlanmış — filtre uygulanınca tüm kart tek renk bloğa dönüşüyordu (piksel incelemesiyle doğrulandı). Bu ikisi doğal renkleriyle bırakıldı; Chaos görseli daha temiz olan `chaos.webp`'ye geri alındı (`chaos-logo-red.svg` yerine). Kurumsal talimatlardaki "partner marka kurallarına uyulur" ilkesiyle örtüşüyor — Adobe/Chaos'un resmi renkli rozeti bozulmadan kullanıldı.
- **5) Footer WhatsApp satırı kaldırıldı:** İletişim sütunundaki tekrarlayan "WhatsApp: 0553 242 67 37" satırı 194 sayfadan (kök + post) kaldırıldı; sağ altta zaten sabit WhatsApp widget'ı var. İletişim sayfasındaki (cadbim_iletisim.html) meşru WhatsApp bağlantılarına dokunulmadı.
- **Not — eşzamanlı oturum:** Bu turun ortasında ikinci Claude oturumu `git add -A` ile commit aldı (9a4eaa6b, 12:13); bu değişikliklerin çoğu (sektör SVG'leri, home-3d.js, soltabs-nav, cred-row temel stili, WhatsApp kaldırma) o commit'e karıştı — içerik doğrulandı, kayıp yok (satır sonu normalizasyonu hariç fark yok). Adobe/Chaos filtre-hariç düzeltmesi o commit'ten sonra yapıldığı için ayrı kaldı, bu kayıt onu da kapsıyor.
- **Durum:** ✅ Tüm beş bulgu localhost:8420'de doğrulandı (masaüstü + mobil 375px).

### DK-2026-08-03-26 — Şirket içi önizleme yayını (GitHub Pages), 4 sayfada bölüm eşitleme, BIM İçerik'e mimarlık kitlesi

- **Yapan:** Onur Bozok'un üç maddeli talebi üzerine Claude (PDM asistanı): (1) "siteyi şimdi şirketteki kişilere göstereceğiz… link vermem lazım. bunu github'tan yapacaksak orayı canlıya al", (2) "eşitle", (3) "mimarlık içinde içeriği güncelle ancak ana hedef dediğin gibi imalatçılar olmalı".

**1) Şirket içi önizleme yayını → https://bzkindamix.github.io/cadbim_website/**
GitHub Pages zaten açıktı (public depo, `main` kökünden) ama önizleme olarak kullanılamayacak durumdaydı:
  - Site **cadbim.com.tr'nin alan kökünde** yayınlanmak üzere yazıldığı için `/`, `/favicon.svg`, `/feed.xml`, `/site.webmanifest` ve apple-touch-icon gibi mutlak yollar üretimde **doğru**, ancak Pages proje sitesi bir **alt dizinde** (`/cadbim_website/`) servis edildiği için orada kırılıyordu. En görünür etkisi: logoya basınca ana sayfaya değil `bzkindamix.github.io` köküne gidiliyordu (584 geçiş).
  - Önizleme kopyası arama motoruna açıktı; canlı siteyle mükerrer içerik riski taşıyordu.
  - **Çözüm:** `main` dalı üretim için **doğru hâlde bırakıldı**; `scripts/build_pages.py` yalnızca önizleme kopyasında (`_site`) bu yolları önekliyor ve her sayfaya `noindex, nofollow` ekliyor. Proje sitelerinde `/robots.txt` alan köküne ait olduğu ve depo içindeki dosya okunmadığı için meta etiketi kullanıldı. Böylece canlıya geçerken hiçbir şeyin geri alınması gerekmiyor.
  - Pages kaynağı **branch'ten workflow'a** çevrildi; `.github/workflows/pages.yml` ile `main`'e her push otomatik yayınlanıyor. `_site` gitignore'a alındı.
  - `404.html`'deki `data-path` bağlantıları çalışma anında `window.__prefix` ile yeniden yazıldığı için dönüştürmeden muaf tutuldu (doğrulayıcıya bu istisna işlendi).
  - **Doğrulama:** Önizlemede kalan kırık mutlak yol **0** (1326 HTML + 752 dosya). Canlı adres üzerinde 11 kaynak denetlendi, tümü 200. Gerçek tarayıcıda gezinme testi: ana sayfa yükleniyor (kırık görsel 0, logo `/cadbim_website/`, noindex mevcut); `/cadbim_website/plm` ve `/cadbim_website/ai-gorsellestirme` temiz adresleri 404.html üzerinden doğru sayfaya yönleniyor; olmayan adres düzgün 404 sayfası veriyor.

**2) Bölüm eşitleme — 4 sayfada eksik olan iki bölüm eklendi**
18 çözüm sayfasının 14'ünde "Yöntemimiz — Bu Çözümü Nasıl Hayata Geçiriyoruz?" (5 adım) ve "Sektör İyi Uygulamaları — Projelerde Uyguladığımız Standartlar" (6 madde) bölümleri vardı; **plm, fabrika-tasarimi** (eskiden yerlerine "Cadbim Farkı" bloğu konmuştu) ile bu oturumda eklenen **bim-icerik-uretimi** ve **ai-gorsellestirme** sayfalarında yoktu. `scripts/add_yontem_iyiuygulama.py` ile dördü de mevcut 14 sayfadaki **birebir aynı kalıpla** tamamlandı; içerik her sayfaya özel yazıldı (ör. PLM için süreç envanteri → fazlı devreye alma; AI için lisans envanteri → kullanım politikası). `dijital-donusum` bilinçli olarak kapsam dışı bırakıldı — kendi "Dijital Dönüşüm Yolculuğunuz" bölümü var. Artık 17 sayfada bu iki bölüm de mevcut.

**3) BIM İçerik sayfasına mimarlık kitlesi — ana hedef imalatçı kaldı**
Hero, giriş ve konumlandırma **değiştirilmedi**; birincil kitle yapı ürünü üreticileri olarak duruyor. Eklenenler:
  - **"Kimler İçin? — İki kitle, iki farklı ihtiyaç"** bölümü: iki kartlı düzen, **imalatçı kartı birincil olarak işaretli** (aksan kenarlık + degrade zemin, "Birincil kitle" etiketi), mimarlık/iç mimarlık ofisi kartı ikincil kitle olarak anlatılıyor (ofis kütüphanesi standardı, dışarıdan gelen üretici ailelerinin denetimi, ATC eğitimi). Bölüm "Neler Yapabiliriz?"in hemen ardına yerleşiyor ki konumlandırma erken okunsun.
  - **SSS'ye iki madde:** "Mimarlık ofisiyiz, üretici değiliz — bu çözüm bize ne sağlar?" ve "Dışarıdan indirdiğimiz aileler modelimizi şişiriyor, ne yapmalı?" (SSS 5 → 7 madde).
  - `enrich_cozum_pages.py` bölüm sıralamasına `kitle` anahtarı eklendi (yetenek → kitle → ürün).

- **Doğrulama:** 197 kök sayfada etiket dengesi ve JSON-LD **0 sorun**. Beş sayfa ölçüldü: İki Kitle bölümü 1280 px'te iki, 375 px'te tek sütun; birincil kart aksan kenarlığını alıyor; dört sayfada 11 yöntem/iyi uygulama başlığı (5 adım + 6 madde) sayıldı; yatay taşma 0, metin taşması 0, kırık görsel 0. Cache sürümü v=21.
- **Not:** Şirket içi paylaşımda linkin **canlı site değil önizleme** olduğunun belirtilmesi gerekir; sayfalarda `noindex` var ama ziyaretçiye görünen bir uyarı bandı eklenmedi (inceleyecekleri tasarımı değiştirmemek için).
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-25 — Yeni çözüm sayfalarındaki üç eksik kapatıldı: OG görseli, blog eşleşmesi, video bölümü

- **Yapan:** Onur Bozok'un "devam?" sorusu üzerine, yeni özellik eklemek yerine önceki turlarda kendi bıraktığım açık uçlar denetlenip kapatıldı (Claude, PDM asistanı).

**1) Eksik OG görselleri (sosyal paylaşımda kırık görsel)**
`cadbim_bim_icerik_uretimi.html` ve `cadbim_ai_gorsellestirme.html` sayfaları, şablon olarak kullandıkları sayfanın OG yolunu devraldığı için var olmayan `assets/og/cadbim_bim_icerik_uretimi.png` ve `assets/og/cadbim_ai_gorsellestirme.png` dosyalarına işaret ediyordu. LinkedIn/WhatsApp paylaşımında görsel çıkmayacaktı.
  - `scripts/gen_og_cozum.py` yazıldı; mevcut `gen_og_sektor.py` şablonunu (1200×630, koyu navy, soluk ızgara, aksan etiketi, beyaz başlık, gri açıklama, sağ üstte beyaz logo, sol altta çerçeveli alan adı) **yeniden kullanarak** iki görsel üretti. 155 mevcut OG görseliyle aynı dil korundu.
  - Site genelinde OG denetimi yapıldı: **eksik görsel 0**.

**2) Blog bölümü boş kalıyordu (AI sayfası)**
AI Destekli Görselleştirme sayfasının blog bileşenine `data-topic="Chaos"` verilmişti; blog verisinde böyle bir etiket bulunmadığı için **0 yazı eşleşiyor** ve bölüm kendini gizliyordu. Konu, 59 yazının bulunduğu **"Görselleştirme"** kategorisine çevrildi; bölüm artık 5 kartla doluyor. Aynı düzeltme üretici betiğe de işlendi.

**3) AI sayfasına küratoryal video bölümü eklendi**
Blog verisinde konuyla gerçekten ilgili 40 video bulundu; bunlardan beşi seçilip BIM İçerik sayfasındakiyle aynı `yt-lite` facade kalıbıyla yerleştirildi. **Marka sırası kuralına uygun olarak Autodesk videoları başta:** Autodesk Forma Board — Generate AI Image ile konsept görseller · Yapay zekâ destekli tasarım ve imalat iş ortağınız: Autodesk AI · Adobe Firefly — Yapı Referansı · Creative Cloud + AI · Adobe — üretken yapay zekâ ile hızlı iş akışları. Beş küçük resmin tamamı 200 döndü (16–44 KB).

- **Doğrulama:** 197 kök sayfada etiket dengesi ve JSON-LD **0 sorun**; site genelinde eksik OG görseli **0**. AI sayfası tarayıcıda ölçüldü: 5 video kartı, 5 blog kartı, yatay taşma yok, kırık görsel yok, iç içe bağlantı yok, bölüm sırası Hero → Nedir → Neler Yapabiliriz → Ürünler → Video → Markalar → SSS → Cadbim Farkı → Blog. Küçük resim URL'leri doğrudan `curl` ile de teyit edildi.
- **Not:** Tarayıcı ölçümünde küçük resimler `0x0` görünüyor; bu `loading="lazy"` görsellerin ekran dışı iframe'de yüklenmemesinden kaynaklanan bir ölçüm artefaktıdır, sayfa hatası değildir (aynı kalıp üst düzey sayfada 480×360 yüklenerek doğrulanmıştı).
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-24 — Sürüm numaraları içerikten kaldırıldı; Sanatsal Baskı navigasyon bulgusu düzeltildi

- **Yapan:** Onur Bozok'un "sürüm numaraları kullanmaktan kaçın", "sanatsal baskı bilinçli ama bu sence bir problem mi? orasının kitlesi bambaşka" ve "yerel sunucuyu yeniden başlat" talimatları üzerine Claude (PDM asistanı).

**1) Sürüm numaraları kaldırıldı**
Bir gün önce Chaos marka sayfasına eklenen bölüm "Güncel Sürümler" adıyla ve sürüm numaralarıyla (Corona 14, Anima 6 update 2, V-Ray 7 for 3ds Max update 4, V-Ray for Blender update 3, Blender 5.1) yazılmıştı. Bu yaklaşım her yeni sürümde sayfanın güncellenmesini zorunlu kılıyor ve güncellenmediğinde eskimiş bilgi yayımlanmış oluyordu.
  - Bölüm **"Öne Çıkan Yetenekler — Chaos ekosisteminde neler var?"** olarak yeniden yazıldı; içerik sürüm değil **yetenek** düzeyinde anlatılıyor: AI Upscaler (Chaos Cloud), AI Material Generator (Chaos Cosmos), AI Mood Match, gerçek zamanlı görünüm penceresi (Vantage + 3ds Max), kalabalık ve trafik animasyonu (Anima), geniş platform desteği (V-Ray).
  - Alt metindeki tarih notu ("Ağustos 2026") kaldırıldı; yerine "ekosistem sürekli geliştiği için burada yetenekleri anlatıyoruz; hangi ürün ve planda hangisinin bulunduğunu teklif aşamasında birlikte netleştiriyoruz" ifadesi kondu.
  - AI Destekli Görselleştirme sayfasındaki Corona ürün kartından da sürüm numarası çıkarıldı.
  - **Yan bulgu:** Site genelinde sürüm ifadesi taraması yapıldı; benim eklediğim bloklar dışında yalnızca bir yerde kalmıştı — `cadbim_ultimaker_malzeme.html` içinde *"Cura 5'in metal FFF özellikleriyle"*. *"UltiMaker Cura'nın metal FFF özellikleriyle"* olarak düzeltildi. Site genelinde başka sürüm numarası yok.
  - `scripts/add_chaos_adobe_icerik.py` başına kalıcı not eklendi: **sürüm numarası kullanılmaz.**

**2) Sanatsal Baskı navigasyon bulgusu — önceki tespit yanlıştı, düzeltildi**
DK-2026-08-03-12'de "cadbim_sanatsal_baski.html sayfasında site navigasyonu hiç yok; ziyaretçi o sayfadan başka hiçbir yere gidemiyor" diye raporlanmıştı. Bu **hatalı bir tespitti**: kontrol yalnızca `<nav>` öğesi içinde yapılmış, footer'a bakılmamıştı. Sayfada footer var ve ana sayfaya (`/`), DesignJet sayfasına ve KVKK'ya bağlantı veriyor; ayrıca WhatsApp ve blog bağlantıları mevcut. Sayfanın üst menüsüz, dikkat dağıtmayan kurgusu ayrı bir kitleye yönelik bilinçli bir açılış sayfası tasarımıdır ve çıkış yolu zaten vardır — **değişiklik yapılmadı.**

**3) Yerel sunucu yeniden başlatıldı**
`dev_server.py` URL haritasını (`404.html` içindeki MAP) yalnızca açılışta okuduğu için yeni eklenen `/bim-icerik-uretimi` ve `/ai-gorsellestirme` adresleri eski süreçte çözümlenmiyordu. 8420'deki süreç kapatılıp yeniden başlatıldı; 10 adres tek tek denetlendi, tümü 200 döndü.

- **Doğrulama:** Chaos bölümünün altı kartı düğüm bazında denetlendi — gerçek sürüm numarası **yok** (innerText birleşmesinden kaynaklanan bir yanlış pozitif tespit edilip elenmiştir: "V-Ray" alt etiketi ile "3ds Max…" açıklaması birleşince sürüm gibi görünüyordu; "3ds Max" ürün adıdır). Beş sayfa tarayıcıda yeniden ölçüldü: yatay taşma yok, kırık görsel yok, Experience Cloud ürün adı yok, sürüm ifadesi yok, doğru CSS sürümü (v=20) yükleniyor. Cache sürümü v=20.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-21 — Chaos ve Adobe kaynaklı içerik yerleştirildi; yeni çözüm: AI Destekli Görselleştirme

- **Yapan:** Onur Bozok'un "chaos grubun çözümlerine bak, bize alabileceğimiz içerikleri al ve ilgili sayfalara yerleştir, buna ek olarak yeni bir çözüm eklemek gerekirse ekle" talebi; ardından "aynı araştırmayı adobe içinde genişletiyorum", "adobe marketing çözümlerini satamıyoruz" ve "adobe for business endüstri ve çözümlerini değil de creative ve acrobat tarafındaki çözüm ve endüstrilere bak" düzeltmeleri üzerine Claude (PDM asistanı).

**1) Yeni çözüm: AI Destekli Görselleştirme → `/ai-gorsellestirme`**
`chaos.com/ai-visualization` incelendi ve tek başına bir çözüm oluşturmaya yeteceği görüldü. Kapsam: **Veras** (2B görsel, eskiz veya 3B modelden metin istemiyle görselleştirme; Enscape/V-Ray/Corona ile bütünleşir, SketchUp/Rhino/Revit içinde çalışır), **AI Material Generator** (fotoğraftan dikişsiz PBR malzeme, Chaos Cosmos kapsamında), **AI Image Enhancer** (bitki, insan ve büyük yüzeylerde detay), **AI Upscaler** (tek tıkla 2x/4x, 16K'ya kadar), **AI Mood Match** (referans fotoğrafın ışığını Sun & Sky'a taşıma). Yanına Autodesk Forma/Fusion jeneratif tasarım, Lumion Cloud AI malzeme üreticisi ve Adobe Firefly kondu. Ürün sırası kurala uygun: **M&E Collection ilk**, ardından Autodesk, sonra Chaos/Lumion/Adobe/HP. Yeni illüstrasyon: model + metin istemi → sinir ağı → fotogerçekçi çıktı + 16K rozeti + AI malzeme çipleri + beş adımlı hat. Site geneline bağlandı (mega menü 1322 sayfa, çözümler kartı, endüstri filtresi mimari/iç mimarlık/medya/otomotiv, endüstri haritası, 404 URL haritası, sitemap). SSS'de yapay zekâ çıktılarının **ticari kullanımı ve veri gizliliği** ayrıca ele alındı; Chaos'un "çıktı lisans koşulları çerçevesinde size aittir" ve "veri paylaşımı kullanıcı tercihine bağlıdır" ifadeleri esas alınıp güncel şartların teyit edilmesi önerildi.

**2) Görselleştirme sayfası — Kullanım Alanları (Chaos "Industry solutions")**
Chaos'un endüstri menüsündeki disiplinler CADBİM'in sektörleriyle eşleştirilip sekiz kartlık bölüm eklendi: Mimari Görselleştirme, İç Mimarlık, Peyzaj, Kentsel Planlama, Film & TV VFX, Sanal Prodüksiyon, Otomotiv, Ürün Tasarımı.

**3) Chaos marka sayfası — Güncel Sürümler**
Altı başlık: Chaos AI Upscaler (Cloud Collaboration, 16K), Corona 14 (Gaussian splat, Night Sky, Fabric Material, AI Material Generator), Anima 6 update 2 (fren/sinyal ışıklı araçlar, bağlam duyarlı kalabalıklar, 4B yollar), V-Ray 7 for 3ds Max update 4 (Vantage doğrudan görünüm penceresinde), V-Ray for Blender update 3 (Linux, Blender 5.1, AMD GPU, V-Ray Wrangler, Parallax Interiors), AI Mood Match. Bölüm alt metnine tarih notu (Ağustos 2026) ve "teklif aşamasında teyit" ibaresi kondu — **sürüm numaraları her yeni sürümde güncellenmelidir.**

**4) Yaratıcı İçerik sayfası — İçerik Üretim Hattı (yalnızca Creative Cloud + Acrobat)**
Dört adım: Planla ve Standardı Kur (Creative Cloud Libraries, Adobe Fonts 30.000+ font, paylaşılan Adobe Stock lisansı) → Üret (20+ uygulama, gömülü üretken yapay zekâ, tasarımcı olmayan ekipler için Express şablonları) → Gözden Geçir ve Onayla (Frame.io, Acrobat Pro; karşı tarafın oturum açması gerekmez, yasal bağlayıcı e-imza) → Sürümü Koru ve Yeniden Kullan (180 güne kadar sürüm geçmişi, kullanıcı başına 1 TB, Admin Console).

**5) Adobe marka sayfası — Belge & Onay Akışı (Acrobat)**
Acrobat Standard 40+, Acrobat Pro 70+ özellik çerçevesinde mühendislik/inşaat ekiplerinde karşılığı olan altı başlık: sürüm karşılaştırma, yasal bağlayıcı e-imza, redaksiyon (hassas bilginin kalıcı kaldırılması), tarama → aranabilir PDF, PDF koruma, Microsoft 365 / Dropbox / Creative Cloud entegrasyonu.

**KAPSAM SINIRI (Onur'un iki düzeltmesi doğrultusunda):** İlk turda Adobe içeriği `business.adobe.com/industries` ve `business.adobe.com/solutions/content-supply-chain` üzerinden derlenmişti; bu sayfalar **Adobe Experience Cloud** portföyüne (GenStudio, Experience Manager, Real-Time CDP, Journey Optimizer, Analytics, Workfront) dayanır ve CADBİM'in Gold Reseller kapsamında **değildir**. Kaynak `adobe.com/tr/creativecloud/business/*` ve `.../acrobat-pro.html` sayfalarına çevrildi, metinler yeniden yazıldı. Site genelinde bu ürün adlarının hiçbirinin geçmediği programlı olarak doğrulandı (0 bulgu). Adobe'nin yayımladığı fiyatlar da alınmadı (CADBİM kuralı) — 0 fiyat bulgusu.
  - **Yan düzeltme:** `cadbim_adobe.html` H1'i *"Adobe — Yaratıcılık, **Pazarlama** ve Belge Yönetimi"* diyordu; satılamayan pazarlama portföyünü ima ettiği için *"Yaratıcılık, **İçerik** ve Belge Yönetimi"* yapıldı. Eski ürün adı **"Adobe Sign" → "Acrobat Sign"** olarak güncellendi.
- **Yeniden üretilebilirlik:** `scripts/add_ai_gorsellestirme.py`, `scripts/add_chaos_adobe_icerik.py` (kaynak ve kapsam notları betiğin başında), `scripts/cozum_icerik.py`, `scripts/gen_cozum_visuals.py`.
- **Doğrulama:** 197 kök sayfada etiket dengesi ve JSON-LD geçerliliği **0 sorun**. Beş sayfa tarayıcıda ölçüldü: yatay taşma yok, kırık görsel yok, iç içe bağlantı yok, bölüm sırası doğru, nav'da ilgili öğe aktif. Çözüm sayısı 17 → 18; endüstri filtresi rozetleri yeniden üretildi (Mimarlık 10, İç Mimarlık 5, Medya 4, Otomotiv 11). Kapsam ve fiyat denetimi: **0 uyarı**. Cache sürümü v=19.
- **Not:** Yerel sunucu `404.html` URL haritasını açılışta okuduğu için yeni çözüm URL'leri eklendikten sonra sunucunun yeniden başlatılması gerekir.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-24 — Tasarımlı 404 sayfası + favicon gerçek Cadbim amblemiyle değiştirildi

- **Yapan:** Onur Bozok'un "404'ü yap; sekmedeki C'yi Cadbim logosu yapalım mı?" talebi üzerine Claude (PDM asistanı). Onur logonun yalnızca baştaki amblem (elips-A) olmasını istedi, CADBİM yazısı olmadan.
- **Favicon seti:** `assets/logos/cadbim-logo.png`'den (beyaz dikey logo) amblem satır-analiziyle kırpıldı (0-320 arası; yazı 350+). Üç dosya aynı adlarla yeniden üretildi → hiçbir HTML değişikliği gerekmedi: `favicon.svg` (lacivert yuvarlatılmış kare + base64 gömülü amblem), `assets/apple-touch-icon-180.png`, `assets/icon-512.png`. Üretici: scratchpad/gen_favicons.py (PIL).
- **404.html yeniden kuruldu:** 195 kayıtlık MAP yönlendirme mantığı bayt-bayt korundu (dev_server.py bu MAP'i tek doğru kaynak olarak okuyor). **Kritik hata düzeltildi:** eski kodda fallback DOM erişimi `<head>` içinde çalıştığından bulunamayan adreste ziyaretçi bomboş sayfa görüyordu. Yeni tasarım: amblem + 404 + "Aradığınız sayfa bulunamadı" + Anasayfa butonu + 6 bölüm bağlantısı (Ürünler/Çözümler/Eğitimler/Blog/İletişim/Teklif İste); github.io prefix desteği ve noscript korundu; site görsel dili (navy/cyan, Manrope/Space Grotesk, grid zemin).
- **htaccess taslağına eklendi:** `ErrorDocument 404 /404.html` (docs/htaccess-taslak.txt, bölüm 5) — canlıda test notu düşüldü.
- **Doğrulama (localhost:8420):** /404.html → başlık doğru, içerik görünür (`#nf.on`, opacity 1), 6 bağlantı doğru href'lerle, gömülü logo yüklü, konsol hatasız. Favicon 128px önizlemede amblem net.
- **Durum:** ✅ Tamam. Teşekkür sayfası bilinçli olarak yapılmadı (paralel oturumun worktree'sinde hazırlanıyor).

### DK-2026-08-03-23 — Ana sayfa description marka önem sırasına göre yeniden kuruldu

- **Yapan:** Onur Bozok'un "önem sıralaması: Autodesk, Adobe, HP plotter, HP workstation, diğer markalar — başlık ve açıklamaları buna göre tekrar değerlendir" talebi üzerine Claude (PDM asistanı).
- **Başlık:** Değişmedi — içindeki tek marka Autodesk (#1), sıralamayla çelişki yok.
- **Yeni description (153 kr):** `1993'ten beri 9.000'i aşkın kuruluşun çözüm ortağı. Autodesk ve Adobe yazılımları, HP plotter ve iş istasyonları, eğitim ve danışmanlık — teklif isteyin.` — DK-22'deki metinde Chaos HP'nin önündeydi ve plotter yoktu; yeni sıra birebir önem sırası. Chaos "diğer markalar" kapsamında kendi sayfasına bırakıldı. "Plotter" kelimesi arama hacmi için tercih edildi (resmi ürün adı HP DesignJet, nav'da öyle).
- **Not:** og/twitter uzun açıklamalarındaki marka sırası (Autodesk, Adobe, HP, Microsoft, Chaos, UltiMaker) zaten uyumlu, dokunulmadı.
- **Durum:** ✅ index.html güncellendi.

### DK-2026-08-03-22 — Ana sayfa title/description final (Onur onayı) + müşteri sayısı 11.000+ → 9.000+

- **Yapan:** Onur Bozok + Claude (PDM asistanı). Onur DK-20'deki metinler için "sıfırdan yazsan nasıl yazardın" ve "sadece Autodesk satıyormuş gibi görünüyor" geri bildirimlerini verdi; revize ikiliyi onayladı. Ayrıca "müşteri sayımızı 9.000+ yapalım, tüm sitede ve açıklamalarda" dedi.
- **Eşzamanlı oturum notu:** Aynı anda çalışan ikinci Claude oturumu da kaydına DK-2026-08-03-21 numarasını vermişti; çakışmayı önlemek için bu kayıt DK-22'ye alındı. Ayrıca o oturumun commit'i (7162c306, `git add -A`) bu işin hakkımızda/dijital-dönüşüm 9.000+ düzeltmelerini ve ana sayfa yeni description'ını kendi commit'ine kattı — içerik kaybı yok, yalnızca commit mesajı/kapsam eşleşmesi bulanık; izlenebilirlik bu kayıtla sağlanıyor.
- **Final title (60 kr):** `Cadbim | Autodesk Gold Partner — Lisans, Eğitim, Danışmanlık` — "Yazılım" → "Lisans" (satın alma niyetli aramalar).
- **Final description (153 kr):** `1993'ten beri 9.000'i aşkın kuruluşun teknoloji ortağı. Autodesk, Adobe ve Chaos yazılımları, HP iş istasyonları, eğitim ve danışmanlık — teklif isteyin.` — sayı+kanıt+CTA kurgusu; çok markalı liste "sadece Autodesk" algısını kırıyor; "yetkili eğitim" bilinçli olarak sade "eğitim" (eğitim yetkisi yalnız Autodesk).
- **Müşteri sayısı (8 yer):** index.html (og/twitter desc, hero-sub, sayaç `data-n="11000"`→`9000`), cadbim_hakkimizda.html (og/twitter desc + istatistik kutusu), cadbim_dijital_donusum.html (2 istatistik şeridi). Site genelinde `11.000|11000|11 bin` taraması: 0 kalan.
- **Durum:** ✅ Onaylı metinler işlendi; SERP önizlemesi güncellendi.

### DK-2026-08-03-20 — Ana sayfa title + meta description SEO revizyonu

- **Yapan:** Onur Bozok'un "site açıklamamız 'Autodesk Gold Partner & Tasarım Teknolojileri' bizi tam yansıtmıyor; title ve meta tanımını iyi yazalım, Google'da nasıl görüneceğini görelim" talebi üzerine Claude (PDM asistanı).
- **Yeni title (61 kr):** `Cadbim | Autodesk Gold Partner — Yazılım, Eğitim, Danışmanlık` — partner statüsü + üç hizmet ayağı; ilk 33 karakter kesilse bile marka+statü taşır.
- **Yeni description (149 kr):** `1993'ten beri Autodesk Gold Partner ve Adobe Gold Reseller. Mimarlık, inşaat, üretim ve medya için CAD, BIM ve 3D yazılımları, eğitim ve danışmanlık.` — iki Gold statüsü + 4 sektör + hizmetler; 160 kr sınırının altında.
- **Senkron:** og:title ve twitter:title yeni title ile eşitlendi (og/twitter description'lar sosyal odaklı uzun haliyle korundu). JSON-LD Organization + WebSite düğümlerine `alternateName: "CADBİM"` eklendi (Google site adı seçimi için).
- **Tarama:** 197 kök sayfanın 195'inde description mevcut; eksik 2 sayfa (404, construction_cloud) noindex'li yönlendirme sayfası — işlem gerekmedi.
- **Not:** Google SERP'teki sitelink'ler (Eğitimler, İletişim, Ürünler…) Google tarafından otomatik seçilir, elle belirlenemez; canlı sitede yeni meta'nın görünmesi yayın + yeniden tarama sonrası olur.
- **Durum:** ✅ index.html güncellendi; SERP önizlemesi Onur'a sunuldu.

### DK-2026-08-03-13 — Yeni çözüm: BIM İçerik & Obje Üretimi (Revit Family / BIM objesi)

- **Yapan:** Onur Bozok'un "çözümlerimize BIM içerik üretimi, BIM obje üretimi çözümümüzü ekleyelim… cadbim.com.tr'de bir sayfa var ama bilgiler çok detay olabilir, sen bir güzel anlamlı sayfa oluştur. Ayrıca bu konuyla ilgili YouTube videolarımız da var" talebi üzerine Claude (PDM asistanı).
- **Kaynak:** Canlı sitedeki `cadbim.com.tr/yapi-urunleri-ureticileri-icin-bim` ("Yapı Ürünü Üreticileri için BIM") sayfası incelendi. Autodesk'in üç başlıklı çerçevesi (katalog ürünleri için BIM / özel ürün ve sistemler için BIM / büyük ölçekli projeler için BIM) korundu; Autodesk kaynaklı çözüm listesi (Revit aileleri oluşturma, 3B CAD modellerinden BIM nesnesi dışa aktarma, referans Revit projeleri, Vault ile BIM veri senkronizasyonu) esas alındı. Metinler kopyalanmadı, CADBİM kurumsal Türkçesiyle yeniden yazıldı ve sadeleştirildi.
- **Yeni sayfa:** `cadbim_bim_icerik_uretimi.html` → temiz URL `/bim-icerik-uretimi`. Diğer 16 çözüm sayfasıyla aynı akışta: Hero (+ölçüt şeridi, sağda illüstrasyon) → Bu Çözüm Nedir (3 paragraf + 4 madde) → Neler Yapabiliriz (6 kart) → İlgili Ürünler + Endüstriler → **Video Eğitimler** → Markalar → SSS (5 soru + FAQPage) → Cadbim Farkı → Blog → CTA.
  - **Ürün sırası kurala uygun:** AEC Collection, PD&M Collection (koleksiyonlar ilk) → Revit, Inventor, Vault PDM, Autodesk Docs, Navisworks (Autodesk) → Yazılım Geliştirme.
  - **Yetenekler:** Revit aile üretimi, CAD→BIM dönüşümü, parametre ve veri zenginleştirme, MEP bağlantı noktaları, kütüphane ve şablon yönetimi, .rfa + IFC yayınlama.
  - **Video Eğitimler bölümü (yeni bileşen):** Onur'un belirttiği, konuyla gerçekten ilgili 5 Cadbim YouTube videosu küratoryal olarak yerleştirildi — "Üretim Sektörü için BIM (BIM Objects)", "Revit ile sıfırdan Family yaratmak…", "Revit 2020: Yeni başlayanlar için Family oluşturma", "Revit projesini Family olarak kaydetme (.rvt → .rfa)", "InfraWorks: Parametrik içerik oluşturma". Projenin mevcut `yt-facade.js` kalıbı (`.yt-lite`) kullanıldı: sayfa yükünde ağır iframe yok, küçük resim + oynat düğmesi var, tıklamada `youtube-nocookie.com` üzerinden başlıyor. JavaScript kapalıysa bağlantı doğrudan YouTube'a gidiyor.
- **Görsel:** `assets/img/cozum/bim-icerik-uretimi.svg` — "üretim CAD modeli → sadeleştirme → parametrik BIM objesi (.rfa)" akışı; solda yoğun hatlı üretim modeli (1 240 yüzey), ortada sadeleştirme çarkı, sağda sadeleşmiş obje + bağlantı noktaları + paylaşılan parametre tablosu, altta tip kataloğu. Site paletiyle, `gen_cozum_visuals.py` içinde.
- **Site geneline bağlama:** Üst menüdeki Çözümler mega menüsüne "Tasarım & Mühendislik" grubunda BIM'in hemen ardına eklendi — **1322 sayfada** (kök + 1129 blog yazısı; blog yazıları `../` göreli yol kullanıyor). Çözümler merkezine kart (BIM'den sonra 3. sırada) ve endüstri filtresine `data-ind="mimari insaat makine"` eklendi. `cadbim_endustriler.html` endüstri haritasının Mimarlık, İnşaat ve Makine panellerine eklendi. `404.html` URL haritası (194 kayıt) ve `sitemap.xml` güncellendi.
- **Yeniden üretilebilirlik:** `scripts/add_bim_icerik_sayfasi.py` (sayfa + bağlama), içerik `scripts/cozum_icerik.py`'de, görsel `scripts/gen_cozum_visuals.py`'de. Betik yeniden çalıştırılabilir.
- **Yol üstünde çıkan iki hata (düzeltildi):**
  1. `add_nav_link()`'in "zaten var" koruması dosyanın tamamına bakıyordu; hub kartı ve endüstri haritası girişleri de aynı slug'ı içerdiği için `cadbim_cozumler.html` ve `cadbim_endustriler.html` sayfalarının **nav'ına bağlantı eklenmemişti**. Kontrol yalnızca nav bölümüne bakacak şekilde daraltıldı ve `main()` sırası düzeltildi (nav önce).
  2. `404.html` içindeki URL haritası boşluksuz JSON (`"bim":"cadbim_bim.html"`) biçimindeydi; boşluklu kalıp aradığım için ilk denemede kayıt eklenmedi ve yerel sunucu `/bim-icerik-uretimi` için hata döndü. Düzeltildi.
- **Doğrulama:** Yeni sayfa yerel sunucuda 200; 196 kök sayfada etiket dengesi ve JSON-LD geçerliliği **0 sorun**, 40 blog yazısı örneklemesinde de 0 sorun. Nav bağlantısı: mega menüsü olan **hiçbir sayfada eksik veya mükerrer yok** (kontrol nav bölümü içinde yapıldı). Filtre denetimi: Mimarlık → 9 çözüm, yeni kart görünür; Medya → 3 çözüm, yeni kart gizli. Sayfa üzerinde ölçüldü — hero görseli sağda (x=705, 499 px), maddeler 4 sütun, 5 video kartı, küçük resimler 480×360 yüklendi, tıklamada `youtube-nocookie.com` iframe'i oluştu, yatay taşma yok. Nav menüsünde bu sayfa aktif işaretli.
- **Not:** Cache sürümü `v=17`. Canlı sitede (Wix) bu sayfa yok; yayına alma ayrı adım.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-12 — Çözümler mega menüsü ekranın soluna taşıp kesiliyordu (menüden çözüm sayfalarına ulaşılamıyordu)

- **Yapan:** Onur Bozok'un "çözüm sayfalarını göremiyorum" bildirimi üzerine Claude (PDM asistanı).
- **Belirti:** Üst menüdeki **Çözümler** mega menüsü açıldığında sol kenardan taşıyordu. `body{overflow-x:hidden}` nedeniyle taşan kısım hiç görünmüyor, dolayısıyla ilk ve dördüncü kolondaki bağlantılara (Dijital Dönüşüm, BIM, Simülasyon & Analiz, Tolerans Analizi, PLM, PDM, İnşaat Proje Yönetimi) menüden erişilemiyordu.
- **Kök neden:** `design-system.css` içindeki `.nav-mega{left:50%;transform:translateX(-50%)}` kuralı menüyü **nav öğesine göre** ortalıyordu. `.nav-dropdown` `position:relative` olduğu için 1080 px genişliğindeki menünün kapsayan bloğu 72,8 px'lik "Çözümler" öğesiydi; `left:50%` 36,4 px'e karşılık geliyor, `translateX(-50%)` ise 540 px sola çekiyordu. "Çözümler" öğesi ekran ortasının solunda olduğundan menü **x = −32 px**'e oturuyordu; ölçümde 17 bağlantının 8'i görünüm alanı dışındaydı.
- **Yapılan:** `.nav-mega` `position:fixed; top:38px; left:50%; right:auto` yapıldı. `.nav` üzerindeki `backdrop-filter` fixed öğeler için kapsayan blok oluşturur; `.nav` tam genişlikte ve `top:0` olduğu için menü artık **görünüm alanına göre** ortalanır. Dikey konum korundu (menü üstü y=44, nav öğesinin altıyla aynı) — böylece imleç menüye inerken hover kopmuyor.
- **Not:** Bu kural, aynı gün başka bir oturumun attığı `da7c12c5` ("Post nav'ı kök mega-menü ile eşitlendi") commit'inden geliyordu; hata çözüm sayfalarına değil, tüm sayfaların üst menüsüne aitti.
- **Doğrulama:** 9 sayfada (plm, bim, cozumler, gorsellestirme, nesting, anasayfa, endustriler, urunler, egitimler) ölçüldü — hepsinde `position:fixed`, menü x=85, sağ kenar=1165, **17 bağlantı, 0 kesilen**. Genişlik taraması 1280 / 1200 / 1150 / 1100 / 1050 px: taşma yok, kesilen bağlantı yok, hover boşluğu 0 px. 1000 px altında masaüstü menüsü kapanıp mobil menü devrede olduğu için ölçüm dışı. Ayrıca 18 çözüm URL'sinin tamamı yerel sunucuda 200 dönüyor ve `cz-intro / cz-fark / cz-art-hero` blokları yerinde.
- **Yan bulgu:** Tarayıcıda sayfa eski `design-system.css?v=15` ile önbelleğe alındığı için düzeltme ilk ölçümde görünmedi; cache sürümü `v=16`'ya çekildi (1321 dosya). Yayına alırken tarayıcı önbelleğinin yenilenmesi bu sürüm parametresine bağlıdır.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-04-02 — Sosyal medya rayı: kenara gömülü "çekmece" davranışı (masaüstü + mobil)

- **Yapan:** Onur'un "soldaki sabit sosyal medya ikonlarını biraz daha içeri gömelim, üzerine gelince büyüsün" + "bunu mobilde de yap" talebi üzerine Claude (PDM asistanı, Fable).
- **Yapılan (`social-widget.js` v3):**
  - **Masaüstü:** İkonlar varsayılanda sol kenara gömülü (`translateX(-16px)`, %85 opaklık — 38px'in ~22px'i görünür). Ray üzerine gelindiğinde grup hâlinde hafif dışarı çıkar (-8px, tam opak); tek ikonun üzerindeyken o ikon tamamen dışarı kayıp %18 büyür (`translateX(0) scale(1.18)`, hafif yaylanmalı cubic-bezier). Klavye odağı (`:focus-visible`) hover ile aynı davranışı alır.
  - **Mobil/dokunmatik** (`hover: none`): İlk dokunuş rayı dışarı açar (linke gitmez — gömülü hâldeki daralmış hedefe yanlış dokunma engellenir), açıkken dokunuşlar normal gezinir, ray dışına dokununca geri gömülür. Açık durumda hedefler tam boy (WCAG 2.5.8 ile uyumlu; dış denetim #4 bulgusuna da hizmet eder). Mobil kutu boyutu 30→32px'e çıkarıldı.
  - `prefers-reduced-motion` tercihi olanlarda geçiş animasyonu kapalı. Eski JS mouseenter/mouseleave stil kurcalaması kaldırıldı — davranış tamamen CSS'te, JS yalnızca dokunmatik aç/kapa mantığını yönetiyor.
- **Cache bust:** `social-widget.js?v=1` → `?v=3` (196 sayfa).
- **Doğrulama:** Yerel önizlemede v3 yüklendi, 4 ikon, varsayılan `translateX(-16px)`/opaklık 0.85 ölçüldü; `.open` sınıfıyla `translateX(0)`'a geçtiği doğrulandı; CSSOM'da hover/scale kuralları mevcut; konsol hatası 0. **Teşhis notu:** İlk doğrulama denemesinde `.open` "çalışmıyor" göründü — kök neden CSS değil, arka planda (görüntülenmeyen) önizleme panelinde animasyon karelerinin üretilmemesi nedeniyle geçişin başlangıç değerinde donmasıydı; geçiş kapatılınca değerlerin doğru hesaplandığı kanıtlandı.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-04-01 — Sürüm/tazelik denetimi: sitemap lastmod güncellendi, 6 sapkın canonical düzeltildi

- **Yapan:** Onur'un "yarım kalan bir şey var mı, sitenin son durumunu kontrol et, versiyonunu güncelle" talebi üzerine Claude (PDM asistanı, Fable).
- **Denetim sonuçları (temiz):** Çalışma ağacı temiz, push edilmemiş commit yok; bu oturumun 6 commit'i sonraki oturumların 6 commit'inin altında tarihte duruyor, tüm işler (tpl/blog-post CSS, yt-facade, home-3d, feed.xml, nav, İlgili Yazılar, eğitim düzeltmeleri) yerinde. **31 sürümlü varlığın (`?v=`) tamamı site genelinde tek sürümde ve git geçmişine göre taze** — içeriği değişip sürümü unutulmuş dosya yok (5 son-değişen varlık + mobilenav/spec-cards hedefli doğrulandı; tpl-*/blog-post/yt-facade zaten bu oturumda sürümüyle birlikte oluşturuldu). Sürümsüz (`?v=`siz) js/css referansı 0. Smoke test: 9 temsili URL (ana sayfa, ürün, post, eğitimler, feed, sitemap...) HTTP 200, konsol hatası 0.
- **Güncellenen: sitemap lastmod (176 kök URL).** Kök sayfaların çoğu `2026-07-17`'de kalmıştı; oysa bugün/dün footer iletişim bilgileri, nav, eğitim metinleri gibi gerçek içerik değişiklikleri yaşadılar. Her kök URL'nin `lastmod`'u, eşlenen dosyanın **gerçek son git commit tarihine** çekildi. 1.126 post URL'sinin lastmod'u (içerik yayın tarihi) bilinçli korundu — şablon değişikliği Google için "önemli içerik değişikliği" sayılmaz, toplu tarih güncellemek lastmod güvenilirliğini bozar.
- **Bulunan ve düzeltilen hata: 6 sapkın canonical.** `designjet-z6pro/z6ps/z9pro/z9ps`, `factor4`, `substance3d` sayfalarının canonical/og/JSON-LD URL'leri tireli biçimdeydi (`designjet-z6-pro`, `factor-4`, `substance-3d`) — oysa iç linkler (25), 404 yönlendirme haritası ve htaccess taslağı tiresiz standardı kullanıyor; yani **bu 6 sayfanın canonical URL'si hiçbir yönlendirmede çözülmüyordu** (Google'a var olmayan URL beyan ediliyordu). Sayfa başına 7 referans + 6 sitemap `<loc>` tiresiz standarda çekildi. Denetim: 192 kök sayfanın tamamında canonical ↔ MAP hizalı, sitemap'te MAP dışı kök URL 0.
- **Durum:** ✅ Site sağlıklı; sürümler güncel; push edilecek.

### DK-2026-08-03-19 — Autodesk-dışı ürünler için eğitim iddiaları site genelinde kaldırıldı

- **Yapan:** Onur'un "biz sadece autodesk ürünleri için eğitim veriyoruz; sitede bu duruma zıtlık oluşturan ifadeleri bul ve düzelt" talebi üzerine Claude (PDM asistanı, Fable). Kural hafızaya da kaydedildi (cadbim-egitim-sadece-autodesk).
- **İlke:** Eğitim SADECE Autodesk ürünleri için verilir (ATC). 3ds Max/Maya Autodesk olduğu için eğitim referansları meşru; V-Ray, Corona, Enscape, Lumion, SketchUp, Adobe, UltiMaker vb. için "eğitim" denmez — "lisanslama, kurulum, teknik destek" denir. "Eğitim lisansı/eğitim kurumları" (lisans türü), webinarlar ve footer'daki jenerik hizmet linkleri ihlal değildir, korundu.
- **Düzeltilen kalıplar (89 dosya):**
  1. **Adobe sayfaları (11):** "Uygulama Eğitimleri — Photoshop'tan Premiere'e... Türkçe eğitimler" kartı → "Türkçe Teknik Destek" kartı.
  2. **Chaos sayfaları (8):** "Render Eğitimleri — V-Ray ve Corona'da..." kartı (3 metin varyantı) → "Türkçe Teknik Destek".
  3. **SketchUp sayfaları (7):** "Modelleme Eğitimleri — ...uygulamalı SketchUp eğitimleri" kartı → "Başlangıç Desteği".
  4. **CTA şeridi (Autodesk-dışı):** "lisans/konfigürasyon **ve eğitim** planını birlikte belirleyelim" → eğitim çıkarıldı (39 sayfa); "Eğitim Programları" butonu kaldırıldı (58 sayfa); chaos/lumion/sketchup'taki "V-Ray/Lumion/SketchUp Eğitimi Al" hero butonları kaldırıldı (3).
  5. **Satın alma adımı (Autodesk-dışı 79):** "Kurulum & Eğitim — rol bazlı kullanıcı eğitimi" → "Kurulum & Devreye Alma — başlangıç yönlendirmesi"; "kurulumdan eğitime..." → "kurulumdan desteğe..." yaşam döngüsü cümlesi.
  6. **`cadbim_substance3d.html`:** Autodesk'e özel olması gereken ATC eğitim banner'ı bu Adobe sayfasından kaldırıldı.
  7. **`/gorsellestirme` SSS (HTML+JSON-LD):** "3ds Max, V-Ray, Corona ve Lumion eğitimleri programda yer alır" → "Eğitim hizmetimiz Autodesk yazılımlarına özeldir... V-Ray, Corona ve Lumion için eğitim vermiyoruz; lisanslama, kurulum ve teknik destek sağlıyoruz." Ayrıca "bu hazırlığı eğitim kapsamında" → "Revit eğitimlerimiz kapsamında".
  8. **`/yaratici-icerik` SSS + kart:** "Adobe uygulamalarına yönelik eğitimler" → Autodesk-özel açıklama; "Eğitim" çözüm kartı → "Dağıtım & destek".
  9. **`/egitimler`:** 5 meta/JSON-LD'de "Autodesk ve Chaos eğitimleri" → "Autodesk eğitimleri"; katalogdan V-Ray + Enscape kurs kartları ve formdaki "Chaos" optgroup'u (V-Ray/Enscape) kaldırıldı — katalog artık %100 Autodesk.
  10. **`/cozumler`** "lisans ve eğitimle" → "lisanslamayla"; **`/dijital-donusum`** "rol bazlı eğitim" → "Autodesk yazılımlarında rol bazlı eğitim"; **`/hakkimizda`** "Autodesk ve Adobe'de Gold Partner, Yetkili Eğitim Merkezi..." → ATC'nin yalnız Autodesk olduğu netleştirildi.
- **Doğrulama:** Yeniden tarama — kalan tüm "eğitim+marka" eşleşmeleri meşru bağlamlar (lisans türleri, ATC, düzeltilmiş metinler, footer navigasyonu). 89 değişen dosyada div/select/optgroup/a etiket dengesi sağlam. Tarayıcıda: /gorsellestirme SSS'i (DOM+JSON-LD) yeni metinde; /egitimler kataloğunda V-Ray/Enscape yok, form optgroup'ları 5'e indi (tümü Autodesk+Sertifikasyon), 3ds Max kartı duruyor; /vray'de eski kart/CTA/buton yok, konsol hatası 0. Postlarda (1.129) eğitim-verme iddiası bulunamadı; mobilenav/veri dosyaları temiz.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-03-18 — index.html'in 45KB'lık 3D sahne betiği harici dosyaya çıkarıldı (O11 tamamlandı)

- **Yapan:** Claude (PDM asistanı, Fable) · Fable listesinin 5. ve son kalemi.
- **Sorun (O11):** Ana sayfanın satır içi 3D sahne betiği (hero izometrik çizim + sektör görselleri + istatistik animasyonları) denetimden bu yana 36KB'dan **45KB'a** büyümüştü ve her ziyarette HTML'in içinde yeniden iniyordu (önbelleklenemiyor).
- **Yapılan:** Betik `assets/js/home-3d.js`'e (47KB, `?v=1`) çıkarıldı; `index.html`'de aynı konuma (body sonu) **senkron** `<script src>` kondu — defer değil, çünkü aynı konumda senkron yükleme çalıştırma sırasını birebir korur (body sonunda engelleme maliyeti sıfır). `index.html` 99KB → **53KB**.
- **Doğrulama:** Betiğin konum-bağımlı API kullanmadığı doğrulandı (`currentScript`/`document.write` yok). Tarayıcıda kesin kanıt: statik HTML'de **boş** olan `#isoSvg` öğesi, DOM'da betiğin ürettiği 14.378 baytlık polygon çizimini içeriyor; `heroCoord` "ORBIT 000°..." metni yazılmış, sectorView köşe işaretleri yerinde. `home-3d.js` HTTP 200, konsol hatası 0. (İstatistik sayaçlarının "0" görünmesi 0x0 gizli önizleme viewport'unda IntersectionObserver'ın tetiklenmemesinden — D8'de kayıtlı, bu değişiklikle ilgisiz.)
- **Durum:** ✅ O11 tamamlandı, push edilecek. Fable listesi (Y8-Faz1, Y12, Y9, O9, O11) bitti.

### DK-2026-08-03-17 — 998 YouTube iframe'i tıkla-oynat facade'ına çevrildi (O9 tamamlandı)

- **Yapan:** Claude (PDM asistanı, Fable) · Fable listesinin 4. kalemi.
- **Sorun (O9):** 1.014 YouTube iframe'i sayfa açılışında eager yükleniyordu — her video ~800KB+ YouTube JS'i indiriyor ve **onay alınmadan `youtube.com` çerezleri** yerleştiriyordu (KVKK riski). Blog yazılarında video, sayfanın en ağır öğesiydi (LCP).
- **Yapılan:**
  1. **`yt-facade.js`** (yeni, kök): kendi CSS'ini enjekte eden, event-delegation'lı hafif facade. Tıklamada `youtube-nocookie.com/embed/ID?autoplay=1` iframe'ine dönüşüyor. JS kapalıysa facade `<a href="youtube.com/watch?v=ID">` olarak çalışır (progressive enhancement — sahte buton değil, gerçek link).
  2. **921 statik iframe** (901 post + 20 kök) küçük resim (`i.ytimg.com/vi/ID/hqdefault.jpg`, çerezsiz CDN, width/height'lı) + oynat düğmesi facade'ına çevrildi.
  3. **77 kök sayfadaki JS şablonu** ("İlgili blog videoları" bölümünü çalışma anında üreten kod) da facade üretecek şekilde güncellendi — delegation sayesinde dinamik eklenen facade'lar da tıklanabilir.
  4. Toplam **980 dosyaya** `yt-facade.js?v=1` script etiketi eklendi. **16 `youtube-nocookie` iframe'i** (başarı öyküleri/sanatsal baskı gibi özel yerleşimli, zaten çerezsiz) kasıtlı olarak dokunulmadan bırakıldı.
- **Kazanç:** Sayfa açılışında YouTube'a giden istek 0'a indi (küçük resim hariç — o da çerezsiz statik CDN); onay öncesi `youtube.com` çerezi tamamen kalktı; video'lu post sayfalarının ilk yükü video başına ~800KB hafifledi.
- **Doğrulama:** Dönüşüm sonrası eager `youtube.com/embed` iframe'i site genelinde 0. Tarayıcıda: post sayfası 0 iframe ile açıldı, facade tıklamasında `youtube-nocookie.com/...?autoplay=1&rel=0` iframe'i yerine geçti; `cadbim_autocad.html`'de dinamik bölüm 8 facade üretti, tıklama orada da çalıştı; küçük resim eager testte 480x360 yüklendi (lazy testte yüklenmemesi 0x0 gizli önizleme viewport'u kaynaklı, gerçek tarayıcıda geçerli değil). Konsol hatası 0.
- **Durum:** ✅ O9 tamamlandı, push edilecek.

### DK-2026-08-03-16 — RSS feed + 1.129 posta statik "İlgili Yazılar" bloğu (Y9 tamamlandı)

- **Yapan:** Claude (PDM asistanı, Fable) · Fable listesinin 3. kalemi.
- **Sorun (Y9):** Blog tamamen JS ile listeleniyordu; RSS yoktu, post→post iç linkleme %4,5'ti (SEO'da 1.126 sayfa birbirinden kopuk "yetim" içerik).
- **Yapılan:**
  1. **`feed.xml`** (yeni, kök): `assets/data/blog-posts.json`'dan son 50 yazıyla RSS 2.0 üretildi (title/link/guid/pubDate/category/description, atom:self). Keşif linki (`rel="alternate"`) tüm postlara + `cadbim_blog.html` + `index.html`'e eklendi.
  2. **İlgili Yazılar:** Her postun sonuna (CTA kutusundan sonra) 4 kartlık statik blok eklendi. Eşleştirme deterministik: ortak ürün sayısı > aynı kategori > tarih yakınlığı > slug (alfabetik kırılım) — JSON'daki `products[]`/`cat`/`date` alanlarından, çalışma anında JS gerektirmeden. Kart linkleri çıplak `slug` (aynı `/post/` dizininde göreli, temiz URL uyumlu).
  3. Kart stilleri (`.a-related*`, 9 kural) `blog-post.css`'e eklendi (`?v=2`→`?v=3`).
- **Doğrulama:** 1.129/1.129 post işlendi (JSON'da eşleşmeyen 0, anchor bulunamayan 0); tarayıcıda örnek postta 4 kart doğru stille render oldu, ilk kart hedefi HTTP 200, `feed.xml` HTTP 200 + DOMParser ile geçerli XML (50 item), keşif linki head'de. BIM konulu posta BIM içerikli kartlar eşleşti (anlamsal isabet göz kontrolü).
- **Not:** `feed.xml` statik üretim — yeni post eklendiğinde yeniden üretilmeli (script: scratchpad'de; kalıcılaştırılacaksa `scripts/` altına taşınabilir).
- **Durum:** ✅ Y9 tamamlandı, push edilecek.

### DK-2026-08-03-15 — Post nav'ı kök mega-menü ile eşitlendi; 29 kök sayfadaki nav sürüklenmesi giderildi (Y12 tamamlandı)

- **Yapan:** Claude (PDM asistanı, Fable) · Fable listesinin 2. kalemi.
- **Sorun (Y12):** 1.129 blog yazısının nav'ı 9 düz linkten ibaretti — kök sayfalardaki 40+ linkli dropdown/mega-menü deneyiminden kopuktu; blog ziyaretçisi ürün/çözüm sayfalarına menüden inemiyordu. Ayrıca analizde **kök nav'ın kendisinde sürüklenme** bulundu: 29 ürün sayfası, diğer 163 sayfadan farklı bir deneme varyantı taşıyordu (Ürünler menüsünde fazladan "Tüm Ürünler" linki + KVKK menüden çıkarılmış).
- **Yapılan:**
  1. `index.html`'deki kanonik nav (163 sayfanın + tüm güncel sayfaların kullandığı yapı) post bağlamına uyarlandı: tüm iç linkler `../slug`, logo `../`, **Blog aktif** işaretli. 1.129 postun tamamına uygulandı — post nav'ları artık tek hash.
  2. Dropdown taban CSS'i (6 kural: `.nav-dropdown*`) `blog-post.css`'e eklendi (`?v=1`→`?v=2` cache bust); mega-menü yerleşim kuralları zaten `design-system.css`'te global olduğu için ek iş gerekmedi.
  3. Sapmış 29 kök sayfa kanonik nav'a çekildi (Ürünler aktif) — kök nav yapı dağılımı artık 192/192 tekdüze.
- **Doğrulama:** Python — 1.129 postta tam 1 nav, tek hash, `</html>` bütünlüğü sağlam; kök 192 sayfada tek yapı (KVKK menüde, "Tüm Ürünler" yok). Tarayıcı — post sayfasında 3 dropdown, menü varsayılan gizli/doğru zeminli, `:hover` kuralı `blog-post.css?v=2`'den, mega-hover `design-system.css`'ten CSSOM'a yüklü, hatalı href 0; kanonikleştirilmiş `cadbim_advance_steel.html`'de Ürünler aktif + KVKK menüde. Konsol hatası 0.
- **Durum:** ✅ Y12 tamamlandı, push edilecek.

### DK-2026-08-03-14 — Satır içi CSS konsolidasyonu Faz 1: 1.276 sayfanın CSS'i 21 ortak dosyaya çıkarıldı (Y8 kısmen)

- **Yapan:** Onur'un "fable ile yapılacaklara geç ve sıradan başla ve bitir" talebi üzerine Claude (PDM asistanı, Fable) · Denetimdeki Y8 bulgusunun (satır içi CSS'in %95,6'sı sayfalar arası tekrar, ~6 MB) düşük-riskli ilk fazı.
- **Yöntem (sıfır kaskad riski):** Tüm sayfaların `<style>` blokları SHA-256 ile gruplandı; yalnızca **bayt-bayt aynı** bloklar dışa çıkarıldı. `<link>` etiketi bloğun tam yerine konduğu için kaskad sırası birebir korunuyor; inline CSS'te hiç `url()` olmadığı doğrulandı (yol kırılması imkânsız). Farklı olan sayfalara (45 singleton kök sayfa + 9 iki-bloklu sektör sayfası + 1 istisna post) dokunulmadı.
- **Sonuç:**
  - `post/*.html`: 1.129 postun 1.128'i birebir aynı ~3,5KB bloğu taşıyordu → **`assets/css/blog-post.css`** (tek istisna `alias-autostudio.html`, eski şablon tipografisi — inline bırakıldı). Tek başına ~4,3 MB tekrar temizlendi.
  - Kök sayfalar: 20 bayt-aynı şablon grubu (148 dosya) → **20 adet `assets/css/tpl-*.css`** (tpl-urun-a…f, tpl-hp-workstation, tpl-designjet-a…c, tpl-kvkk, tpl-cozum-a…c, tpl-sketchup, tpl-ultimaker, tpl-chaos, tpl-fabrication, tpl-autocad, tpl-kurumsal). Dosya başlıklarında üye sayfalar listeleniyor.
- **Kazanç:** Repo genelinde ~5,4 MB CSS tekrarı silindi; kullanıcı tarafında ikinci sayfa görüntülemeden itibaren CSS önbellekten geliyor (post HTML'leri ~3,5KB, kök HTML'ler ~8-12KB küçüldü). Bakım: bir şablonun CSS düzeltmesi artık tek dosyada.
- **Doğrulama:** Python assert'leri — her dosyada tam 1 blok değişti, swap bölgesi dışı baytlar birebir aynı, çıkarılan içerik grup içinde özdeş; sonrasında `<style>` kalıntısı 0 (istisna hariç), `</head>`/`</html>` yapısı sağlam. Tarayıcıda 3 sayfa tipi (tpl-urun-a, blog-post, tpl-kvkk) yüklendi: stylesheet sırası `tabler → tpl → design-system` (eski inline pozisyonuyla aynı), hesaplanan stiller doğru, 6 yeni CSS dosyası HTTP 200, konsol hatası 0.
- **Kalan (Faz 2, ayrı iş):** 45 singleton kök sayfanın ortak çekirdeği + tpl dosyaları arası ortak taban — kural-bazlı analiz gerektirir, ayrı oturumda değerlendirilecek.
- **Durum:** ✅ Faz 1 tamamlandı, push edilecek.

### DK-2026-08-03-11 — Çözüm sayfası yerleşimi yeniden kurgulandı; endüstri filtresi eklendi, mükerrer endüstri haritası tekilleştirildi

- **Yapan:** Onur Bozok'un ekran görüntülü notları ("buraya taşı", "enine sayfayı doldur"), ardından "cadbim farkı şeridi SSS'ten sonra gelsin, ilgili ürünler neler yapabilirizden sonra gelsin", "çözümler ana sayfasına çözüm kutularının üstüne endüstri filtreleri koy" ve "alt taraftaki detaylı incele ile arasında bir tutarsızlık var aynı zamanda bu alanlar mükerrer" geri bildirimleri üzerine Claude (PDM asistanı).

**1) Yerleşim (16 çözüm sayfası)**
  - Teknik illüstrasyon "Bu Çözüm Nedir" bölümünden alınıp **hero'nun sağ sütununa** taşındı; hero iki sütunlu ızgaraya (`.cz-hero-grid`) çevrildi. 980 px altında tek sütuna düşer, görsel 560 px ile sınırlanır.
  - "Bu Çözüm Nedir" bölümü yeniden kuruldu: solda başlık, sağda anlatım (`.cz-intro`), **altında tam sayfa genişliğinde dört sütunlu madde ızgarası** (`.cz-buls`, 1280 px'te 4 × 279 px = 1154 px). Önceden maddeler dar sol sütuna sıkışıp sağ yarıyı boş bırakıyordu.
  - **Yeni bölüm sırası:** Hero → Bu Çözüm Nedir → Neler Yapabiliriz → **İlgili Ürünler** → Markalar → Yöntemimiz → İyi Uygulamalar → SSS → **Cadbim Farkı** → Blog → CTA. Sıralama, gövdeyi bölümlere ayırıp sınıflandıran ve `ORDER` dizisine göre yeniden dizen `reorder_sections()` ile yapılıyor; blog bölümünün kendi betiği ve CTA şeridi bloğuna bağlı kalıyor.
  - **Cadbim Farkı şeridi 16 sayfada da standart hâle getirildi.** Önceden yalnızca `plm` ve `fabrika-tasarimi` sayfalarında vardı ve metni "Autodesk Yatırımınızı..." diye başladığı için Adobe ağırlıklı sayfalara uymuyordu. Eski `data-enrich-brand` blokları kaldırılıp yerine marka-nötr, üç kart (esnek lisans modelleri / ATC / Türkçe destek) ve dört adımlı süreç şeridi içeren tek bir sürüm kuruldu.

**2) Çözümler merkezinde endüstri filtresi**
  - Çözüm kartlarının üstüne 9 endüstri sekmesinden oluşan filtre şeridi eklendi (Tüm Çözümler + Mimarlık, İç Mimarlık & Tasarım, İnşaat & Altyapı, Mekanik Tesisat, Makine & Üretim, Otomotiv, Medya & Eğlence, Eğitim, Havacılık & Savunma). Her sekmede o endüstrideki çözüm sayısı rozet olarak görünür; seçim `#mimari` gibi bir adres parçası olarak URL'ye yazılır.
  - Bağımlılıksız vanilla JS; `aria-pressed`, `role="status"` canlı bölge ve `:focus-visible` odak halkası ile klavye/ekran okuyucu uyumlu. JavaScript kapalıysa tüm kartlar görünür kalır.

**3) Mükerrerlik ve tutarsızlık düzeltmesi (Onur'un notu)**
  - Endüstri ↔ çözüm eşleşmesi **iki ayrı yerde** ve **birbiriyle çelişerek** duruyordu: yeni filtrede elle yazdığım 7 endüstrilik liste ile `cadbim_endustriler.html` içindeki mevcut "Detaylı İnceleme — Endüstriye Göre Çözüm & Ürün Haritası" bölümünün 9 endüstrilik listesi. Örnek çelişki: PLM/CAM/Tolerans kartları filtrede "Havacılık" altındayken kart altındaki metin yalnızca "Makine & Üretim, Otomotiv" diyordu.
  - Çözüm: **`cadbim_endustriler.html` tek doğru kaynak ilan edildi.** `scripts/sync_endustri_haritasi.py` o sayfadaki sekmeleri ve panelleri okuyup filtreyi, sekme renklerini/ikonlarını, rozet sayılarını ve kartlardaki `data-ind` değerlerini üretiyor. İki sayfa artık yapısal olarak çelişemez.
  - Çözüm kartlarının altındaki endüstri listesi **kaldırıldı**, yerine "Detaylı İncele" bağlantısı kondu — aynı bilgi hem filtrede hem her kartın altında tekrarlanıyordu.
  - Filtre seçildiğinde çıkan satıra "bu endüstrinin ürün haritası" bağlantısı eklendi; `cadbim_endustriler.html`'e **adres parçasıyla sekme seçme** desteği verildi (`endustriler#havacilik` doğrudan ilgili sekmeyi açıp oraya kaydırıyor, `hashchange` dinleniyor).
  - Kaynak haritadaki bir eksik giderildi: `dijital-ikiz` yalnızca "Mekanik Tesisat" altındaydı; kendi sayfası ve çözüm kartı "Mimarlık, İnşaat & Altyapı" diyordu — Mimarlık ve İnşaat panellerine de eklendi.

**4) Yan bulgu**
  - Duyarlı kurallar `design-system.css` içinde temel kurallardan **önce** geldiği için 375 ve 768 px'te hero iki sütun kalmaya devam ediyordu (görsel 126 px'e düşüyordu). Medya sorguları dosyanın sonuna taşındı; artık 980 px altında tek sütun, 375 px'te görsel 320 px tam genişlik.
  - Cache sürümü `v=12` → `v=15` (1321 dosya).

- **Doğrulama:** 195 HTML dosyasında etiket dengesi ve JSON-LD geçerliliği: **0 sorun**. Filtrenin 10 düğmesi tek tek tıklanıp rozet sayısı ile görünen kart sayısı karşılaştırıldı — **10/10 eşleşti** (Tümü 16, Mimarlık 8, İç Mimarlık 4, İnşaat 7, Tesisat 5, Makine 11, Otomotiv 10, Medya 3, Eğitim 4, Havacılık 5). `endustriler#havacilik` doğru sekmeyi ve paneli açıyor. PLM sayfasında ölçüldü: hero görseli x=697'de, başlığın sağında; madde ızgarası 1154 px genişlikte 4 sütun; bölüm sırası Hero → Nedir → Neler Yapabiliriz → Ürünler → Markalar → SSS → Cadbim Farkı → Blog. 375 / 768 / 1024 / 1280 px'te yerleşim ve taşma ölçüldü: yatay taşma 0, metin kutusundan taşma 0. Çözüm kartlarının alt satırının 16'sında da "Detaylı İncele" yazdığı, endüstri metninin kalmadığı doğrulandı. **Not:** bu oturumda tarayıcı paneli görüntülenemediği için ekran görüntüsü alınamadı; doğrulama ölçüm tabanlı.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-10 — Çözüm sayfaları marka kaynaklı içerikle zenginleştirildi; kart kutuları tıklanabilir yapıldı

- **Yapan:** Onur Bozok'un "sitemizdeki çözümler sayfalarındaki içerikler az … markaların sitelerine girip hem görsel hem yazılı içerik alıp mevcut sayfalarımızı düzgün bir akış sıralamasıyla, temamızı bozmadan güncelle" ve ardından "çözümlerdeki kutular ilgili linki açmıyor" talepleri üzerine Claude (PDM asistanı).
- **Kural olarak verilenler:** Autodesk her zaman ilk gösterilen marka; koleksiyonlar (AEC / PD&M / M&E) her zaman ilk gösterilen ürün; beyaz arka planlı marka görseli kullanılmayacak; site teması bozulmayacak.

**1) Kart kutularının tamamı tıklanabilir yapıldı (`scripts/fix_card_links.py`)**
Ürün, endüstri, marka ve başarı öyküsü kartlarında yalnızca `<h3>` içindeki bağlantı tıklanabiliyordu; kartın gövdesine tıklamak hiçbir şey yapmıyordu. Bu, çözüm sayfalarına özgü değil site geneline yayılmış bir hataydı. `<div class="card"> … <h3><a href="X">Başlık</a></h3> … </div>` kalıbı, iç içe geçme sayan bir çözümleyiciyle `<a href="X" class="card"> … <h3>Başlık</h3> … </a>` hâline getirildi. **160 dosyada 948 kart** dönüştürüldü; kart gövdesinde bağımsız başka bir `<a>` bulunan kartlar (geçersiz iç içe bağlantı üretmemek için) dokunulmadan bırakıldı. `design-system.css`'e `a.card` kuralları eklendi (blok görünüm, alt çizgi yok, hover'da kenarlık ve başlık rengi, klavye için `:focus-visible` halkası).

**2) Marka kaynaklı içerik derlemesi**
Autodesk WebFetch'i 403 döndürdüğü için içerik, uygulama içi tarayıcıyla ilgili resmî sayfalar gezilerek toplandı: Autodesk BIM / Digital Twin / Simulation / CAM / Design Automation / Additive Manufacturing çözüm sayfaları, Fusion Manage, Vault, ReCap Pro, Factory Design Utilities, Inventor Nesting, Inventor Tolerance Analysis ürün sayfaları, AEC / PD&M / M&E koleksiyon sayfaları, Autodesk Tandem, Autodesk Construction Cloud (Forma ürün ailesi), Chaos V-Ray, Lumion, UltiMaker S serisi ve Cura, Adobe Creative Cloud for teams. Metinler kopyalanmadı; teknik olgular ve güncel ürün terminolojisi alınıp CADBİM kurumsal Türkçesiyle yeniden yazıldı. Fiyat bilgisi bilinçli olarak hiçbir yere konmadı. İçerik tek kaynakta toplandı: `scripts/cozum_icerik.py`.

**3) Sayfa akışı ve yeni bölümler (16 çözüm sayfası, `scripts/enrich_cozum_pages.py`)**
Yeni sıra: Hero → **Bu Çözüm Nedir (görsel + anlatı)** → Neler Yapabiliriz → Yöntemimiz → İyi Uygulamalar → **Markalar** → Ürünler → Endüstriler → **SSS** → Blog → CTA.
  - **Hero:** tek cümlelik açıklama, marka kaynaklarına dayanan dört cümlelik bir girişle değiştirildi; altına üç kutuluk ölçüt şeridi eklendi.
  - **"Bu Çözüm Nedir":** iki sütun — solda üç paragraflık anlatı ve dört maddelik yetenek listesi, sağda o çözüme ait teknik illüstrasyon (yapışkan konumlu; 980 px altında tek sütuna düşüp görsel öne alınır).
  - **Markalar şeridi:** her sayfada **Autodesk ilk**. Logolar `filter:brightness(0) invert(1)` ile tek renk beyaza indirgenip koyu kutu içinde gösterilir — beyaz arka planlı logo kutusu kullanılmadı, tema korundu.
  - **SSS:** sayfa başına dört soru-cevap; JavaScript'siz `<details>/<summary>` ile, `prefers-reduced-motion` uyumlu. Ayrıca her sayfanın `@graph` dizisine **FAQPage** yapısal verisi eklendi.
  - **Ürün sıralaması:** koleksiyonlar birinci, Autodesk ürünleri ikinci, diğer markalar üçüncü grup olacak şekilde kararlı sıralama uygulandı (54 slug'lık Autodesk portföy listesiyle). Marka şeridi koyu bant olduğu için hemen altındaki ürün bölümünün `padding-top:0` değeri 56 px'e çekildi.
  - `cadbim_cozumler.html` (çözüm merkezi): marka şeridi (Autodesk ilk) ve "hangi çözüm size uygun" danışma CTA'sı eklendi.

**4) Görseller (`scripts/gen_cozum_visuals.py`, 16 SVG · ~155 KB)**
Marka sitelerindeki görseller beyaz arka planlı ürün ekran görüntüleri olduğu için tema dışı kalıyordu; bunun yerine sektör sayfalarındaki çizim diliyle aynı dilde, şeffaf zeminli ve sitenin paletine göre renklendirilmiş teknik illüstrasyonlar üretildi: olgunluk basamakları (dijital dönüşüm), ayrışık disiplin katmanları + çakışma işareti (BIM), FEA ağı ve gerilme bantları (simülasyon), tolerans zinciri + normal dağılım (tolerans), kural paneli → varyantlar (otomasyon), bina + telemetri paneli (dijital ikiz), izometrik fabrika yerleşimi (fabrika), takım yolu + NC çıktısı (CAM), katman katman baskı (eklemeli), yuvalanmış sac (nesting), yaşam döngüsü halkası + BOM (PLM), revizyon ağacı + kasa (PDM), şantiye + iş programı + CDE (inşaat yönetimi), sahne + ışık + render bucket'ları (görselleştirme), artboard + zaman çizelgesi (yaratıcı içerik), tarayıcı + nokta bulutu (gerçeklik yakalama). `gen_sektor_visuals.py`'nin yardımcıları yeniden kullanıldı.

**5) Yan bulgular ve düzeltmeler**
  - `cadbim_dijital_donusum.html`'de hem hero metninde hem meta açıklamada **"Autodesk, Adobe ve HP Gold Partner"** yazıyordu. HP'de Gold Partner statüsü yok; ifade "Autodesk Gold Partner ve Adobe Gold Reseller Partner; HP, Microsoft, Chaos ve UltiMaker yetkili iş ortağı" olarak düzeltildi.
  - `cadbim_hp_monitor.html`'deki JSON-LD **geçersizdi** (`23.8"-39.7"` içindeki kaçışsız tırnak JSON'u bozuyordu, HEAD'de de bozuk). İnç işareti (″) kullanılarak düzeltildi; artık sitedeki tüm JSON-LD blokları geçerli.
  - Cache-busting: `design-system.css` ve `mobilenav.js` `v=11` → `v=12` (1319 dosya). Yeni CSS kuralları eski sürümle önbellekten gelmiyor.

- **Doğrulama:** Yerel sunucuda (`dev_server.py`, :8420) tarayıcıyla yapıldı. 193 HTML dosyasında etiket dengesi ve JSON-LD geçerliliği denetlendi — 1 sorunlu dosya bulundu (yukarıdaki hp_monitor, düzeltildi), kalan 0. Sekiz çözüm sayfasında bölüm sırası, marka sırası, ürün sırası, SSS sayısı ve kırık görsel kontrolü yapıldı: kırık görsel 0, iç içe bağlantı 0, yatay taşma 0. 375 / 768 / 1280 px genişliklerde yerleşim ölçüldü: 980 px altında iki sütun tek sütuna düşüyor, görsel öne alınıyor, hiçbir metin kutusundan taşmıyor. Kart yapısı ölçüldü: 280×206 px `<a>` kutusu, içinde ikon + başlık + açıklama, iç bağlantı yok — yani kutunun tamamı tıklanabilir. Tüm logo ve illüstrasyon dosyaları sunucudan 200 ile geliyor. SSS aç/kapa etkileşimi denetlendi. **Not:** bu oturumda tarayıcı paneli görüntülenemediği için ekran görüntüsü alınamadı; doğrulama ölçüm tabanlı yapıldı, illüstrasyonlar ise SVG'den PNG'ye rasterleştirilerek gözle kontrol edildi ve ilk turda tespit edilen yerleşim çakışmaları (etiket üst üste binmeleri, panel taşmaları) düzeltildi.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-13 — Yeni sektör sayfaları çözüm sayfası derinliğine çıkarıldı (marka kaynaklı içerik)

- **Yapan:** Onur Bozok'un "yeni eklenen endüstrilerin kendi sayfalarını oluştur, temamızı bozma, diğer çözümlerde bahsedilen detaylar seviyesinde olsun; marka sayfalarından içerikleri çek ve uygula" talebi üzerine Claude (PDM asistanı).
- **Kapsam:** `sektor_tesisat.html` ve `sektor_icmimarlik.html`, DK-2026-08-03'te paralel oturumun çözüm sayfalarına kurduğu detay desenine (`design-system.css`'teki `cz-*` bileşenleri) çıkarıldı — tema ve mevcut sayfa akışı korunarak dört yeni katman eklendi (`scripts/enrich_new_sektor_pages.py`, idempotent):
  1. **Ölçüt şeridi (cz-stats, hero altı):** tesisat — "LOD 400 / 7.000+ üretici kataloğu / Tek veritabanı"; iç mimarlık — "1.000+ eklenti / 12'ye varan pigment / Gerçek zamanlı".
  2. **"Bu Sektörde Yaklaşımımız" (cz-intro):** üçer paragraf + dörder madde (cz-bul). İçerik, sitedeki marka kaynaklı ürün sayfalarından derlendi ve kurumsal Türkçeyle yeniden yazıldı: Fabrication CADmep/ESTmep/CAMduct'ın ortak veritabanı ve LOD 400 imalat detayı, ESTmep'in 90+ üretici / 7.000+ katalog öğesi, CFD'nin üretim öncesi akış-termal doğrulaması; SketchUp Pro'nun masaüstü/web/iPad + LayOut yapısı, Corona'nın "fiziksel doğruluk varsayılan açık" iç mekân konumlanışı, Enscape'in eş zamanlı render'ı, Lumion'un sürükle-bırak akışı, DesignJet Z9+'ın 12 mürekkep/64 inç fine art kapasitesi.
  3. **"Neler Sunuyoruz?" kapsam kartları:** altışar kart (tesisat: havalandırma, sıhhi tesisat, HVAC analizi, imalat detaylandırma, metraj-maliyet, saha koordinasyonu · iç mimarlık: mekân planlama, fotogerçekçi render, gerçek zamanlı gezinti, malzeme kurgusu, sunum panoları, galeri baskısı).
  4. **SSS (cz-faq):** dörder soru (details/summary + `ti-plus`) ve head'e **FAQPage JSON-LD** (@graph'a beşinci düğüm olarak eklendi). Sorular satış sahasından: "Revit varken Fabrication niye?", "Üçlü birlikte mi alınmalı?", "Corona mı V-Ray mi?", "Render için nasıl iş istasyonu?" vb.
- **Doğrulama:** Her iki sayfada etiket dengesi (div/section/details) tam; JSON-LD beş tipli @graph olarak geçerli parse ediliyor (Organization, WebPage, BreadcrumbList, Service, FAQPage); tarayıcıda akış doğru sırada (Hero+ölçüt → Yaklaşım → Kapsam → İş Akışı → Çözümler → Markalar → Ürünler → Çalışma Modeli → SSS → CTA), SSS aç-kapa çalışıyor, aksan renkleri doğru (#2dd4bf / #f472b6), 0 kırık görsel, konsol hatası yok.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-12 — İki yeni endüstri sayfası: Mekanik Tesisat (MEP) ve İç Mimarlık & Tasarım; site 7→9 sektöre çıktı

- **Yapan:** Onur Bozok'un "tüm markalarımızın kendi sayfalarını gez, endüstrilere ek yapabileceğimiz bir şey var mıdır araştır; varsa kendi tasarım dilimizi koruyarak yeni sayfaları ekleyelim" talebi üzerine Claude (PDM asistanı).
- **Araştırma:** Marka segmentasyonları tarandı — [Autodesk AEC Collection resmî olarak "MEP Engineers" segmenti tanımlıyor](https://www.autodesk.com/collections/architecture-engineering-construction/mep-engineers); [SketchUp'ın ana pazarlarından biri iç mekân tasarımı](https://www.nobledesktop.com/learn/sketchup/industries-and-professions); [Chaos Corona archviz/iç mekân görselleştirme için konumlanıyor](https://blog.chaos.com/introducing-chaos-suites). Ayrıca kurumsal talimatlardaki CADBİM sektör listesinde **"mekanik tesisat"** zaten geçiyor ama sitede sayfası yoktu. Ürün desteği iki aday için de sitede hazırdı (Fabrication CADmep/CAMduct/ESTmep, CFD, Revit / SketchUp, Corona, V-Ray, Enscape, Lumion, Adobe). Elenen adaylar: Peyzaj (Autodesk tarafı zayıf, İnşaat-Altyapı ile örtüşüyor), Sağlık (ürün desteği zayıf), Oyun/VR (Medya & Eğlence zaten kapsıyor).
- **Yeni sayfalar** (`sektor_tesisat.html` aksan #2dd4bf, `sektor_icmimarlik.html` aksan #f472b6; `scripts/gen_new_sektor_pages.py` ile mimari şablonundan): mevcut akışla birebir — Hero (illüstrasyonlu) → İş Akışı (5 adım) → Çözümler → Markalar → Ürünler (filtreli katalog, 11'er ürün) → Çalışma Modelimiz → Blog → CTA. **Başarı Öyküleri bölümü bilerek konmadı** — bu sektörlere atfedilebilir gerçek müşteri hikâyesi yok, uydurulmadı. Marka/ürün sıralamasında "Autodesk her zaman ilk marka, koleksiyonlar ilk ürün" kuralına uyuldu (tesisat kataloğu AEC Collection ile açılıyor).
- **İki yeni SVG illüstrasyon** (`gen_sektor_visuals.py`'ye eklendi): tesisat — izometrik klima santrali (dönen fanlı) + ana kanal hattı + flanşlar + tavan difüzörlü branşmanlar + akış oku + gidiş-dönüş borusu ve vana; icmimarlik — izometrik oda köşesi: pencere, tablolar, L kanepe, sehpa, sarkıt + ışık konisi, halı, saksı bitkisi, malzeme paleti.
- **Navigasyon 9 sektöre çıkarıldı** (`scripts/update_nav_9_sektor.py`): nav dropdown **192 kök sayfada** (163 standart + 29 tek-satır varyant biçim), sektör geçiş şeridi (secnav) 9 sayfada yeniden kuruldu, `mobilenav.js` menü + arama dizini, Endüstriler hub'ı (2 kart + 2 tab/panel + "7→9 Endüstride" metinleri), `cadbim_endustriler.html` meta açıklamaları. Sıra: Mimarlık, İç Mimarlık, İnşaat, Tesisat, Makine, Otomotiv, Medya, Eğitim, Havacılık.
- **Ana sayfa endüstriler paneli illüstrasyonlara geçti** (Onur'un oturum içi ikinci talebi: "endüstri sayfaları için yaptığın tasarımları ana sayfadaki endüstriler bölümü için de uygula"): "Sektörünüze Özel Yaklaşım" panelindeki 3B tel kafes görüntüleyici kaldırıldı; yerine hover'da aksan rengi + crossfade ile değişen sektör illüstrasyonları geldi (9 görsel önden ısıtılıyor). Çözümler panelindeki 3B görüntüleyici korundu. Sektör listesi 9 satıra, soltab'lar 10 seçmeye (2 yeni panel), "Sektör uzmanlığı" istatistiği 7→9'a çıkarıldı.
- **Altyapı:** `404.html` MAP + `sitemap.xml` + `docs/htaccess-taslak.txt` (temiz URL + eski-URL yönlendirmesi) 2 yeni slug; `assets/og/sektor_{tesisat,icmimarlik}.png` mevcut OG şablonunu birebir taklit eden Pillow üretimi (`scripts/gen_og_sektor.py`).
- **Yan düzeltme:** Paralel oturumun eklediği SSS bölümlerindeki `ti-plus` ikonu subset'te yoktu (16 sayfada boş görünüyordu) — subset yeniden üretildi (295 ikon), önbellek `?v=2→?v=3` (1.321 sayfa).
- **Doğrulama:** Yeni sayfalarda 9'lu secnav + doğru aktif sektör, 11'er ürün kartı, marka şeritleri (Autodesk ilk), 0 kırık görsel, konsol hatası yok; tüm iç linkler 404 MAP'e karşı doğrulandı (0 tanınmayan). Ana sayfada hover→tesisat: görsel/aksan/başlık üçlüsü birlikte değişiyor; hub'da 9 kart doğru sırada, tab geçişi çalışıyor. İkon denetimi: kullanılan 295 sınıfın tamamı fontta gerçek glifli.
- **Bilinen sınır:** Yerel önizleme sunucusu MAP'i başlangıçta okuduğundan ve başka oturuma ait olduğundan `/sektor-tesisat` temiz URL'i yerelde sunucu yeniden başlatılana kadar 404 verir (dosya adıyla erişim çalışıyor; canlı davranışını htaccess kuralları belirler). İki yeni illüstrasyonun görsel kontrolü piksel-dağılım analiziyle yapıldı; tarayıcı paneli kapalı olduğundan ekran görüntüsüyle son bir göz kontrolü Onur'a bırakıldı.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-11 — Ana sayfadaki 3B sahneler sektör sayfalarının teknik çizim diline taşındı

- **Yapan:** Onur Bozok'un "ana sayfadaki animasyonlu görselleri de daha sofistike bir hale getir, endüstrilerdeki tasarım dilin hoşuma gitti" talebi üzerine Claude (PDM asistanı).
- **Kapsam:** Ana sayfadaki iki interaktif 3B görüntüleyici (`#sectorSvg` — "Sektörünüze Özel Yaklaşım"; `#cozumSvg` — "Tüm Çözümlerimiz, Endüstrinize Göre") ile hero'daki kalıcı izometrik sahne (`#isoSvg`). Mevcut 3B tel kafes modellerinin **geometrisine dokunulmadı** — yalnızca çizim dili zenginleştirildi.
- **Önceki durum:** Her iki görüntüleyici de modeli düz lacivert zemine, tek renk (cyan) ve tek çizgi kalınlığıyla çiziyordu; zemin düzlemi, ızgara, düğüm noktası, eksen göstergesi yoktu. Hero sahnesi zaten ızgara/yüzey/ölçü çizgisi taşıyordu, düğüm noktası yoktu.
- **Eklenenler (`createViewer`, iki panel):**
  - **Sektöre özel aksan rengi:** 25 model anahtarının her biri kendi rengiyle çiziliyor — 7 sektör rengi sektör sayfalarıyla birebir aynı (`#818cf8`, `#22c55e`, `#f59e0b`, `#ef4444`, `#c084fc`, `#38bdf8`, `#a5b4fc`), 18 çözüm anahtarı da endüstriler sayfasındaki çözüm renkleriyle eşleşiyor. Renk `--acc` / `--accGlow` CSS değişkenleriyle panele yayılıyor: kenarlık, parıltı, köşe işaretleri, alt yazı ve tarama çizgisi hep birlikte geçiş yapıyor.
  - **Mavi kopya ızgarası + aksan parıltısı:** SVG'nin içine değil panelin tamamına (`.sectorsel-view`) uygulandı — SVG 430 px'te sabitlendiği için içeri konsaydı panel ortasında sert kenarlı bir dikdörtgen olarak görünecekti.
  - **İzometrik zemin düzlemi:** modelin ayak izini 0,6 birim taşan, 0,7 adımlı ızgara; ön iki kenarı daha belirgin. Modelle birlikte dönüyor, nesneyi "havada" olmaktan çıkarıyor.
  - **Düğüm noktaları:** modelin en üst %45'indeki köşelerden en fazla 7 tanesi, kademeli gecikmeli nabız animasyonuyla.
  - **Eksen üçlüsü (X/Y/Z) ve canlı okuma:** sol altta, modelle birlikte dönen birim vektör göstergesi; sağ altta `ISO · ORBIT nnn°` — uydurma bir ölçü değil, sahnenin gerçek dönüş açısı.
  - **Köşe işaretleri ve tarama çizgisi:** sektör görselleriyle aynı hareket (7 sn'de bir yukarıdan aşağı süzülen ince aksan çizgisi).
- **Hero sahnesi:** kule ve ek binanın üst köşeleri, vinç direği tepesi ve kanca noktasına 8 düğüm noktası eklendi. Çizilme animasyonu bitmeden görünmesinler diye başlangıçta gizli; `free()` çağrısında nabza geçiyorlar. Kanca düğümü bomla birlikte dönüyor.
- **Erişilebilirlik:** `prefers-reduced-motion: reduce` altında tarama çizgisi gizleniyor, düğümler sabit opaklıkta duruyor.
- **Doğrulama:** Tarayıcıda 7 sektörün ve 8 çözüm sekmesinin tamamı tek tek gezildi — her biri kendi aksan rengiyle, doğru çizgi sayısıyla (42–233 arası) ve düğüm noktalarıyla çiziliyor; hero'da 8 düğüm `vnode` sınıfıyla aktif. 1000 / 1280 / 1440 px genişliklerde görsel kontrol yapıldı, konsol hatası yok.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-10 — İletişim formundan "Tercih ettiğiniz ofis" alanı kaldırıldı

- **Yapan:** Onur Bozok'un "hiçbir formda tercih ettiğiniz ofis olmasın" talimatı üzerine Claude (PDM asistanı).
- **Yapılan:** Alan sitede yalnızca `cadbim_iletisim.html`'de vardı (DK-2026-08-03-08'de canlandırılan formda). Hem `<select name="ofis">` bloğu hem de gönderim betiğindeki "Tercih edilen ofis: …" mesaj ekleme mantığı kaldırıldı.
- **Doğrulama:** Site genelinde `name="ofis"` / "Tercih ettiğiniz ofis" / "Tercih edilen ofis" araması 0 sonuç. Etiket dengesi korunuyor (1/1 `form`, 70/70 `div`, 1/1 `select`). Tarayıcıda form alanları artık `ad_soyad, sirket, email, telefon, talep_turu, mesaj, kvkk`; taklit edilmiş gönderimde JSON gövdesinde ofis bilgisi yok.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-09 — Görünmeyen 9 ikon ve siyah render edilen "beyaz" Autodesk logosu düzeltildi

- **Yapan:** Onur Bozok'un "eklemeli imalat için ikon yok" ve "markalarda siyah Autodesk logosu kullanılmış, site genelinde beyaz olanıyla değiştir" bildirimi üzerine Claude (PDM asistanı).
- **Sorun 1 — Autodesk logosu:** `assets/logos/autodesk-white.svg` (ve `autodesk-primary-white.svg`) adı beyaz olsa da **siyah render ediliyordu**: dosyalardaki 9 şeklin tamamı `class="a"` taşıyor ama `<defs>` bloğu **boştu**, yani `.a` için hiçbir `fill` tanımlı değildi → SVG varsayılanı olan siyaha düşüyordu. Koyu zeminde logo görünmez/siyah lekeydi. 26 sayfada, filtresiz olarak kullanılıyordu.
- **Düzeltme 1:** Her iki dosyaya `<defs><style>.a{fill:#ffffff}</style></defs>` eklendi — tek dosya düzeltmesi 26 sayfayı birden çözdü. Ayrıca `cadbim_lumion.html`'deki var olmayan `ti-brand-autodesk` ikonu, sitedeki diğer 19 kartla aynı biçimde gerçek Autodesk logosu `<img>`'ine çevrildi.
- **Sorun 2 — eksik ikonlar:** Sitede kullanılan 9 `ti-*` sınıfının ikon fontu subset'inde karşılığı yoktu; bunların **8'i Tabler'da hiç var olmayan sınıf adlarıydı** (yani CDN'deki tam set kullanılsa bile boş çıkardı — subset'leme hatası değil, yanlış sınıf adı). En yaygını `ti-printer-3d`: 20 sayfada, eklemeli imalat/3B baskı kartlarında boş görünüyordu (Onur'un fark ettiği).
- **Düzeltme 2 — gerçek Tabler karşılıkları:** `printer-3d`→`cube-3d-sphere` (20 sayfa), `bridge`→`building-bridge`, `circuit-board`→`cpu`, `device-vr`→`badge-vr`, `pipe`→`air-conditioning` (sitede MEP zaten bu ikonla gösteriliyor), `roll`→`cylinder`, `structure`→`building-arch`, `brand-autodesk`→Autodesk logosu. Dokuzuncusu (`player-play-filled`) Tabler'da mevcuttu, yalnızca subset'e girmemişti — eklendi.
- **`scripts/build_icon_subset.py` (yeni):** DK-2026-08-02-08'de "üretim script'leri scratchpad'de, tekrarlanabilir hale getirilmedi" diye bırakılan boşluk kapatıldı. Betik; HTML + JS'i tarayıp kullanılan sınıfları çıkarır, Tabler CDN'inden kaynak CSS/TTF'i çeker (`.icon-subset-cache/`, .gitignore'da), codepoint eşlemesini kurar, woff2 subset'i ve eşleşen CSS'i üretir. **Tabler'da karşılığı olmayan sınıfları isim isim uyarı olarak listeler** — bu hatanın tekrarını engeller. Yeni ikon eklenince: `python scripts/build_icon_subset.py`.
- **Önbellek kırma (kritik):** Her iki düzeltme de **aynı URL'deki dosyayı değiştirdiği** için mevcut ziyaretçilerin tarayıcı önbelleğinde eski (siyah logo / eksik glif) sürüm kalırdı — nitekim doğrulama sırasında tarayıcı ilk denemede hâlâ siyah logo gösterdi. `tabler-icons-subset.css` (1.319 sayfa) ve `autodesk-white.svg` (26 sayfa, 29 referans) referanslarına `?v=2` eklendi; CSS içindeki woff2 URL'ine de `?v=2` eklendi (betikte kalıcı).
- **Doğrulama:** (1) Programatik: sitede kullanılan **293 sınıfın tamamı** artık CSS'te listeli, hepsinin fontta glif karşılığı var ve **hiçbiri boş konturlu değil** (0 boş ikon). (2) Tarayıcıda canvas piksel testiyle `cozumler` (30 ikon) ve `eklemeli-imalat` (26 ikon) sayfalarındaki her ikonun gerçekten çizildiği doğrulandı — 0 boş. (3) Autodesk logosu koyu zemine çizilip piksel sayıldı: **6.156 beyaz / 0 siyah** piksel (düzeltme öncesi 0 beyaz / 7.195 siyah).
- **Bilinen ödün:** Yeni subset 294 ikon için 55,5 KB; önceki 289 ikonluk subset 32,6 KB'tı. Fark ikon sayısından değil kaynak font sürümünden geliyor — Tabler 3.19 ve 3.31 aynı 292 glif için 56,7 / 55,5 KB veriyor, yani eski subset daha eski (daha yalın çizimli) bir Tabler sürümünden üretilmiş. Subset seçenekleri (hinting kapalı, glyph adları atılmış, desubroutinize) boyutu değiştirmedi. ~23 KB artış kabul edildi: karşılığında 9 kırık ikon düzeldi ve CDN'e göre kazanç hâlâ ~%88.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-08 — İletişim sayfasındaki MS Forms iframe'i gerçek forma çevrildi (O4 kapandı)

- **Yapan:** Onur Bozok'un "uzmanla konuş butonları iletişim sayfasına gidiyor, iletişim sayfasında eski form var" uyarısı üzerine Claude (PDM asistanı).
- **Sorun:** `cadbim_iletisim.html`'de sağ sütundaki form, ölçülemez ve marka kimliğinden kopuk bir **MS Forms iframe**'iydi (`forms.cloud.microsoft/...`). Sayfanın kendi tasarımıyla uyumlu gerçek form, altında `<!-- ESKI FORM KALDIRILDI ... -->` yorum bloğunda ölü kod olarak duruyordu — yani DK-2026-08-03-01'de `cadbim_egitimler.html` için düzeltilen aynı durum burada da vardı, atlanmıştı. Ayrıca sayfanın altındaki `<script>` bloğunda **CSS satırı** (`@keyframes spin {...}`) JavaScript içine yazılmıştı; bu bir `SyntaxError` üretip bloğun tamamını çalışmaz hale getiriyordu (form yorumda olduğu için görünür etkisi yoktu).
- **Yapılan:** iframe kaldırıldı, yorumdaki form canlandırılıp `<form id="iletisim-form" onsubmit="handleSubmit(event)">` içine alındı. Bozuk betik, `cadbim_teklif_iste.html` / `cadbim_egitimler.html` ile **aynı `POWER_AUTOMATE_URL`**'e gerçek `fetch()` POST'u yapan uygulama ile değiştirildi (`form_type: 'iletisim'`). "Tercih ettiğiniz ofis" alanı, akışta yeni dal açmamak için mesaj gövdesine ekleniyor. Hata durumunda kullanıcıya e-posta/telefon alternatifi gösteriliyor.
- **Yan bulgu ve düzeltme:** Sayfadaki genel `input,select,textarea{width:100%;padding:11px 14px;appearance:none;}` kuralı KVKK **onay kutusunu** da yakalıyordu — kutu 615 px genişliğe çıkıp yanındaki metni kutunun dışına itiyor, `appearance:none` yüzünden de tik görünmüyordu. Onay kutusuna satır içi `width/height:16px; padding:0; appearance:auto; accent-color:#00c8f0` verildi.
- **"Uzmanla Konuş" hedefi:** 7 sektör sayfasındaki 12 bağlantı `iletisim` → `iletisim#form` yapıldı; buton artık doğrudan formun üstüne iniyor (sayfanın en başına değil).
- **Doğrulama:** Etiket dengesi Python ile kontrol edildi (1 `<form>`/1 `</form>`, 71/71 `div`, `forms.cloud.microsoft` referansı 0). Tarayıcıda form alanları doğrulandı (`ad_soyad, sirket, email, telefon, talep_turu, ofis, mesaj, kvkk`), KVKK satırının taşması giderildiği ölçüldü (kutu 16 px, metin 286 px, taşma yok), konsol hatası yok. Gönderim akışı `window.fetch` **taklit edilerek** test edildi — doğru Power Automate URL'ine doğru JSON gövde gidiyor (ofis bilgisi mesaja ekleniyor). **Gerçek gönderim yapılmadı**, bu yüzden kimseye test e-postası gitmedi; uçtan uca canlı test istenirse ayrıca yapılabilir. "Uzmanla Konuş" tıklanıp formun üstüne inildiği tarayıcıda doğrulandı.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-07 — Otomotiv ve medya sektör görselleri yeniden çizildi

- **Yapan:** Onur Bozok'un "tema güzel sevdim ama otomotiv çok basit gözüküyor, medya ve eğlenceyi anlamadım" ve ardından "otomotivin arabası oyuncak gibi" geri bildirimi üzerine Claude (PDM asistanı).
- **Otomotiv:** Önceki çizim basit bir yan siluet + tek düze ağdı; oranları da oyuncak gibiydi (yüksek ve balon cam alanı, kısa kaput, gövdeye göre büyük tekerlek). Gerçek otomotiv oranlarına göre yeniden kuruldu — **uzunluk 516, yükseklik 150 (0,29), dingil mesafesi 300 (0,58), tekerlek çapı 80 (0,155)**, uzun kaput, alçak ve eğik cam alanı, fastback arka cam. Eklenenler: gövdeye oyulmuş tekerlek davlumbazları (düz marşpiyel yerine yay), koyu doldurulmuş cam panelleri + yansıma çizgileri, B-direği/kapı ayrım hatları, kapı kolu, ayna, far/stop/hava girişi, 5 kollu jant + fren diski ve kaliper. Class-A yüzey dili: tavan eğrisi üzerinde **eğrilik tarağı** (curvature comb — Alias/VRED denetim aracı; normal yönü dışa bakacak şekilde), **NURBS kontrol poligonu** + CV kutuları, `SEC A-A` kesit düzlemi, dingil mesafesi ve toplam uzunluk ölçüleri.
- **Medya ve Eğlence:** Önceki çizim (telkafes küre + perspektif film şeridi + dalga formu) soyut kalıyordu, sektörü anlatmıyordu. Yerine net okunur bir prodüksiyon sahnesi kondu: **tripod üzerinde film kamerası** (iki makara, gövde, vizör, objektif), **render viewport'u** (köşe işaretleri, perspektif zemin ızgarası, telkafes küre, ışık kaynağı + ışın konisi, yanıp sönen render bucket'ları, `RENDER 01` etiketi) ve **kurgu zaman çizelgesi** (cetvel, klipler, anahtar kare elmasları, ses kanalı + dalga formu, soldan sağa kayan oynatma kafası).
- **Etkilenen dosyalar:** `scripts/gen_sektor_visuals.py`, `assets/img/sektor/*.svg` (yeniden üretildi). HTML sayfalarına dokunulmadı — görseller URL ile referanslandığı için sayfa değişikliği gerekmedi.
- **Doğrulama:** 7 SVG yeniden üretildi, tarayıcıda 1:1 ölçekte kontrol edildi. İlk turda iki hata görüldü ve düzeltildi: eğrilik tarağının normali içe bakıyordu (yüzeyin içine tüylenmişti) ve medya tripodu zaman çizelgesinin üstüne biniyordu. Cam panelleri ilk halinde %6 doldurma ile görünmüyordu; koyu opak doldurmaya çevrildi.
- **Durum:** ✅ Tamamlandı, push edildi.

### DK-2026-08-03-06 — Endüstri sayfaları yeniden kurgulandı: sektör geçiş şeridi, sektörel görseller, mantıklı bölüm akışı

- **Yapan:** Onur Bozok'un ekran görüntüsü üzerinden verdiği notlar üzerine Claude (PDM asistanı).
- **Talep (Onur'un notları):** (1) Üstteki sektör sekme şeridi "amatör duruyor — büyük, daha güzel ikonlu, üzerine gelindikçe animasyona giren görseller olsun"; (2) "hemen markaları gösteriyoruz — biraz bu endüstri için yapabildiklerimiz, çözümler, markalar ve ürünler gibi gitsin sayfa"; (3) "Diğer Sektörler gereksiz bir alan, mükerrer oluyor"; (4) "mantıklı bir akış olmalı"; (5) bölümlere görsel yerleştirilmesi.
- **Sektörel görseller (7 adet, yeni):** `assets/img/sektor/{mimari,insaat,makine,otomotiv,medya,egitim,havacilik}.svg` — `scripts/gen_sektor_visuals.py` ile üretilen, sitenin koyu navy/cyan paletine ve her sektörün aksan rengine göre çizilmiş teknik hat illüstrasyonları (izometrik BIM modeli, asma köprü + kule vinç, dişli çifti + CAM takım yolu, araç yüzey ağı, telkafes küre + film şeridi, perspektif sınıf + 3B yazıcı, uçak + sonlu eleman ağı + radar). Kendi içlerinde CSS animasyonu taşırlar (tarama çizgisi, yanıp sönen düğümler, dönen dişli/radar), `<img>` ile yüklendiğinde de çalışır; toplam ~55 KB, harici bağımlılık yok.
  - **Not:** Önce AI raster görsel üretimi denendi — Gemini görsel API'si `RESOURCE_EXHAUSTED` (günlük kota 0) döndü. Ardından Onur'un talebiyle Adobe/Firefly bağlantısı incelendi: hesap bağlı (`account_type: auth`) ancak Adobe konnektörü metin→görsel üretimini **sunmuyor** ("Generative AI Availability: image generation … not available in this environment"); yalnızca görsel düzenleme, Adobe Stock arama/lisanslama ve Express/InDesign iş akışları var. Vektörel illüstrasyon bu yüzden seçildi — ayrıca boyut/keskinlik/tema uyumu açısından web için daha uygun.
- **Sektör geçiş şeridi (`.secnav`, 7 sayfada da yeni):** Eski 50 px'lik ince sekme şeridi kaldırıldı. Yerine 38 px renkli ikon karolu, yükselen ve gölgelenen kartlar geldi; üzerine gelindiğinde o sektörün illüstrasyonu kartın içinde ölçek + kaydırma animasyonuyla beliriyor, ikon hafifçe büyüyüp dönüyor. Aktif sektör kenarlık + alt çubukla işaretli ve sayfa açılışında küçük bir betikle görünür alana kaydırılıyor; sağ kenardaki solma katmanı yalnızca kaydırılacak içerik varken görünüyor. `prefers-reduced-motion` desteklenir. **Eğitim ve Havacılık sayfalarında bu şerit hiç yoktu — eklendi.**
- **Bölüm akışı (yeni sıra):** Hero → İş Akışı (bu sektörde ne yapıyoruz) → Çözümler → Markalar → Ürünler → Başarı Öyküleri → Çalışma Modelimiz → Blog → CTA.
  - Hero'nun sağ sütunundaki **marka listesi kaldırıldı**, yerine sektörün illüstrasyonu kondu; markalar sayfanın ortasında ayrı bir şeride (`.brands`, ızgara düzeni + Gold Partner notu) taşındı.
  - **"Diğer Sektörler" bloğu silindi** (5 sayfada) — üstteki sektör şeridiyle birebir mükerrerdi.
  - Aynı şeyi iki farklı biçimde anlatan **"İlgili Çözümler" kart bölümü + "İlgili Çözüm Alanları" pill bölümü tek "Çözümler" bölümünde birleştirildi** (kartlarda olmayan bağlantılar pill olarak aynı bölüme eklendi, `href` bazında tekilleştirildi).
  - Yanlış bölüm etiketleri düzeltildi: Başarı Öyküleri bölümünün üst etiketi "İlgili Ürünler" yazıyordu → "Referanslar"; ürün kataloğunun etiketi "Çözüm Alanları / … İş Akışınızı Seçin" → "Ürünler / … için kullandığımız ürünler" (artık ayrı bir İş Akışı bölümü var, çakışma gideriliyor).
- **Eğitim ve Havacılık sayfaları** aynı şablona hizalandı: tek sütunlu hero iki sütuna çevrildi (metin + görsel), sektör şeridi eklendi, bölümler aynı sıraya sokuldu ve sayfadaki ürünlerden türetilen marka şeridi eklendi (Eğitim: Autodesk, UltiMaker, Adobe, Trimble, HP, Chaos · Havacılık: Autodesk, UltiMaker, HP).
- **Yerleşim düzeltmesi:** `.section` sınıfının bu sayfalarda hiç `padding` tanımı yoktu (bölüm başlıkları ekranın soluna yapışıyordu) — 56px/3rem verildi; hero, marka şeridi, ürün kataloğu ve sektör şeridi de sitenin geri kalanıyla aynı 1180 px içerik genişliğine hizalandı. Ölü CSS (`.tabs-nav`, `.tab-btn`, `.others*`) temizlendi.
- **Endüstriler ana sayfası (`cadbim_endustriler.html`):** 7 sektör kartına aynı hover davranışı eklendi — sektör illüstrasyonu kartın sağ altında beliriyor, kenarlık sektör rengine dönüyor, ikon hafifçe animasyona giriyor.
- **Etkilenen dosyalar:** `sektor_{mimari,insaat,makine,otomotiv,medya,egitim,havacilik}.html`, `cadbim_endustriler.html`, `assets/img/sektor/*.svg` (7 yeni), `scripts/gen_sektor_visuals.py` (yeni), `scripts/restructure_sektor_pages.py` (yeni).
- **Doğrulama:** Dönüşüm betiği, sınıflandırılamayan içerik kalırsa hata verip duruyor (içerik kaybına karşı bariyer) — bu kontrol iki gerçek hatayı yakaladı: Eğitim/Havacılık'taki "Neler Sunuyoruz" bölümü (`class="section section-alt"` regex'e takılmıyordu) ve Medya'daki Başarı Öyküleri bloğu (`data-newsol` biçimindeydi) ilk turda düşüyordu; ikisi de düzeltildi. Ayrıca 7 sayfanın tamamı için git HEAD ile karşılaştırmalı denetim yapıldı: **kaybolan bağlantı yok (0)**; kaybolan metinler yalnızca kasıtlı olarak kaldırılan/yeniden adlandırılan başlıklar ("Diğer Sektörler", "Bu Sektörde Sunduğumuz Markalar", "İş Akışınızı Seçin", "İlgili Çözüm Alanları"). Tarayıcıda (yerel 8420) Mimarlık, Medya, Eğitim, Havacılık ve Endüstriler sayfaları 1000 px ve 375 px genişlikte kontrol edildi: bölüm sırası doğru, marka şeridi tam (Mimarlık 5 marka), hover animasyonları çalışıyor, konsol hatası yok.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-03-05 — Yerel önizleme sunucusu temiz URL'leri artık çözüyor

- **Yapan:** Onur Bozok "hiç bir link çalışmıyor?" diye sorunca Claude (PDM asistanı) teşhis etti ve düzeltti.
- **Sorun:** Yerel önizleme (`.claude/launch.json` → `python -m http.server 8420`) düz bir statik dosya sunucusu; site ise her yerde uzantısız temiz URL kullanıyor (`href="autodesk"` vb. — gerçek dosya `cadbim_autodesk.html`). Canlıda bunu `404.html`'deki JS haritası (tarayıcı tarafı yönlendirme) kurtarıyor, ama bu numara sunucunun 404 yanıtına özel bir gövde koymasını gerektiriyor — Python'un `http.server`'ı bunu yapmıyor, düz 404 dönüyor. Sonuç: yerelde nav/footer'daki hemen hemen her link kırık görünüyordu (K1 bulgusunun yerel önizlemedeki yansıması).
- **Düzeltme:** `dev_server.py` (yeni, kök) — `http.server`'ı `docs/htaccess-taslak.txt` ile aynı mantıkla genişletiyor: `/slug` isteğini `404.html`'deki MAP'i (tek doğru kaynak, ayrıştırılıyor) kullanarak `cadbim_slug.html`'e, `/post/slug` isteğini `post/slug.html`'e çeviriyor; eşleşme yoksa normal 404. `.claude/launch.json`'daki `cadbim-static` girdisi bu betiği çalıştıracak şekilde güncellendi (git'e girmez, sadece yerel — kalıcılık için not edildi).
- **Doğrulama:** `/autodesk`, `/egitimler`, `/post/3d-gorunum`, `/teklif-iste` artık 200 dönüyor; var olmayan bir slug hâlâ 404 dönüyor (yanlış-pozitif yok). Tarayıcıda nav'dan "Eğitimler"e tıklanıp doğru sayfaya gittiği doğrulandı.
- **Not:** Bu değişiklik canlı siteyi etkilemez — sadece yerel geliştirme/test deneyimini düzeltir. Canlıda gerçek çözüm hâlâ K1: `docs/htaccess-taslak.txt`'in Natro'ya kurulması.
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-03-04 — Tüm `<img>` etiketlerine width/height eklendi + bozuk adobe.svg düzeltildi (Y11 tamamlandı)

- **Yapan:** Onur Bozok'un "devam" talebi üzerine Claude (PDM asistanı).
- **Sorun (Y11):** Sitedeki 3.011 `<img>` etiketinin **hiçbirinde** `width`/`height` niteliği yoktu — tarayıcı, görsel gerçek boyutuyla inene kadar yer ayıramıyor, bu da yüklenme sırasında sayfanın zıplamasına (CLS — Cumulative Layout Shift) yol açıyordu.
- **Bonus bulgu:** Tarama sırasında `assets/logos/products/adobe.svg`'nin **0 bayt (boş/bozuk)** olduğu ortaya çıktı — 10 sayfada (adobe_express, adobe_stock, after_effects, creative_cloud, firefly, illustrator, indesign, lightroom, photoshop, premiere_pro) 32×32'lik ürün ikonu olarak kullanılıyordu, yani bu sayfalarda kırık görsel ikonu gösteriliyordu. Sitede zaten var olan çalışan `assets/logos/products/adobe.png` (128×128, aynı ikon) ile değiştirildi.
- **Yapılan:** 297 benzersiz yerel görsel kaynağının gerçek piksel boyutu okundu (raster için Pillow, SVG için `viewBox`/`width`/`height` XML ayrıştırması). 1.320 sayfadaki (191 kök + 1.129 post) 3.010 yerel `<img>` etiketine (harici tek 1 YouTube-benzeri img hariç) gerçek `width`/`height` niteliği eklendi — CSS/`object-fit` her zaman görünen boyutu kontrol ettiği için görsel render değişmedi, sadece tarayıcı artık doğru en-boy oranını önceden ayırabiliyor.
- **Doğrulama:** Python ile her dosyada işlem öncesi/sonrası `<img>` sayısı eşit kaldığı (denge), hiçbir etikette çift `width=`/`height=` oluşmadığı doğrulandı. Tarayıcıda 5 farklı sayfa tipinde (index, egitimler, designjet, bir post, başarı öyküleri — tümü kaydırılarak lazy-load tetiklendi) `naturalWidth===0` (kırık) ve niteliği eksik `<img>` sayısı 0 çıktı.
- **Durum:** ✅ Y11 tamamlandı, push edilecek.

### DK-2026-08-03-03 — apple-touch-icon PNG + site.webmanifest eklendi (D1 tamamlandı)

- **Yapan:** Onur Bozok'un "devam" talebi üzerine Claude (PDM asistanı) · K3/K5'ten sonra denetim raporundaki bir sonraki mekanik/düşük-riskli kalem.
- **Sorun (D1):** 1.320 sayfanın tamamında `<link rel="apple-touch-icon" href="favicon.svg">` vardı — iOS Safari SVG'yi apple-touch-icon olarak desteklemediği için "Ana Ekrana Ekle" yapan kullanıcılar ikon yerine sayfa başlığının ilk harfini görüyordu. `site.webmanifest` de hiç yoktu (Android/PWA "Ana ekrana ekle" istemi için gerekli).
- **Yapılan:** `favicon.svg`'nin geometrisi (navy yuvarlak köşeli kare + cyan "C" yay) SVG arc endpoint-to-center formülüyle merkez/açı hesaplanıp Pillow ile 180×180 (`assets/apple-touch-icon-180.png`) ve 512×512 (`assets/icon-512.png`) olarak yeniden çizildi — 4x supersample + Lanczos ile kenar yumuşatma. **Not:** İlk denemede tarayıcı canvas'ından `toDataURL()` ile üretilen PNG'yi sohbet üzerinden kopyalamayı denedim; SHA-256 karşılaştırması base64'ün aktarım sırasında bozulduğunu gösterdi (uzunluk aynı, içerik farklı) — bu yöntem güvenilir değil, terk edildi ve doğrudan Pillow ile üretime geçildi.
- **`site.webmanifest`** (yeni, kök): name/short_name "Cadbim", theme/background `#060c1a`, icons: `favicon.svg` (sizes:any) + `icon-512.png`.
- **1.320 sayfa** (191 kök + 1.129 post): `apple-touch-icon` linki yeni PNG'ye çevrildi (3 farklı eski href biçimi işlendi: kök `favicon.svg`, post `../favicon.svg`, post `/favicon.svg`), hemen altına `<link rel="manifest" href="...site.webmanifest">` eklendi (yol derinliğine göre `site.webmanifest` / `../site.webmanifest` / `/site.webmanifest`). `404.html` ve `construction_cloud` stub'ı kasıtlı hariç (apple-touch-icon zaten yoktu).
- **Doğrulama:** Python ile 1.320 dosyada tam olarak 1 `apple-touch-icon-180.png` + 1 `rel="manifest"` referansı doğrulandı (404/construction_cloud hariç, beklenen). Tarayıcıda 3 sayfa (index.html, normal post, `/favicon.svg` varyantlı post) için ikon+manifest linkleri `fetch()` ile HTTP 200 doğrulandı, manifest JSON doğru parse edildi.
- **Durum:** ✅ D1 tamamlandı, push edilecek.

### DK-2026-08-03-02 — 190 sayfaya tam footer içeriği eklendi (K5 tamamlandı)

- **Yapan:** Onur Bozok'un "sonnetle olanları yapalım hemen" talebi üzerine Claude (PDM asistanı) · K3'ün ardından listenin ikinci Sonnet-uygun kalemi.
- **Sorun (K5):** `index.html` ve `cadbim_teklif_iste.html` dışındaki ~188 kök sayfa, footer'da sadece "© 2026 Cadbim — Anasayfaya Dön · KVKK · Çerez Ayarları" + sosyal ikonlardan ibaret minimal bir şerit (`.fbot`) gösteriyordu — telefon/e-posta, ofis adresi, ürün/hizmet linkleri yoktu. 9 küçük varyant (Facebook linki olan/olmayan, "Ürünler" linki olan/olmayan, boşluk farkları, ve `cadbim_iletisim.html`'in kendine özgü satır-içi stilli sürümü) tespit edildi, tamamı tek bir regex (`<footer.*?</footer>`, DOTALL) ile eşleşti.
- **Yapılan:** `index.html`/`cadbim_teklif_iste.html`'deki mevcut `footer-grid` yapısı (marka + Ürünler/Hizmetler/İletişim kolonları) **190 sayfanın tamamına** (bu ikisi dahil, tutarlılık için) genelleştirildi. Eklenenler: **Ankara Temsilcilik** ofis satırı (İzmir Merkez'in yanına — bkz. [[cadbim-ankara-ofis]] hafıza notu, sadece temsilcilik olarak, eğitim/sınıf ima etmeden), **KVKK + Çerez Ayarları** linkleri footer-bot'a (önceden index.html dahil hiçbir sayfada çerez tercihlerini sonradan yeniden açma yolu yoktu — bu bir eksiklikti, düzeltildi), marka logosu artık `<a href="/">` ile ana sayfaya link, ve `index.html`'deki eski/güncelliğini kaybetmiş "Teklif İste" linki (`iletisim#form` → gerçek MS Forms iframe'ine gidiyordu) → `teklif-iste` (gerçek özel sayfa) olarak düzeltildi.
- **CSS:** `.footer-grid`/`.f-brand`/`.f-offices`/`.footer-col`/`.footer-bot` (+responsive 900px/600px kırılımları) artık sayfa-içi tekrar yerine **`assets/css/design-system.css`**'te tek yerden tanımlı (190 sayfada tekrarlanmıyor); her sayfanın kendi `.fbot`/`.socials` kuralları dokunulmadı (yeni markup `.socials`'ı zaten kullanıyor, `.fbot` artık ölü kod — kaldırılmadı, risk/getiri dengesi düşük). Cache-busting: `design-system.css?v=10` → `?v=11` (1.319 sayfa, root + post).
- **Doğrulama:** Python ile 190 sayfanın hepsinde önce tam olarak 1 `<footer>` eşleşmesi doğrulandı; değişiklik sonrası her dosyada `<footer>`/`</footer>` sayısı 1/1, `<div>`/`</div>` dengesi eşit, `footer-grid` ve "Ankara Temsilcilik" metni mevcut — 0 sorunlu dosya. Tarayıcıda 4 farklı sayfa tipi (`cadbim_autodesk.html`, `cadbim_iletisim.html`'in özel satır-içi varyantı, `index.html`, `cadbim_teklif_iste.html`) kontrol edildi: grid doğru render, ofis satırları doğru, KVKK/Çerez Ayarları linkleri çalışıyor (`window.openCookiePrefs` tanımlı), marka linki `/`'e gidiyor, konsol hatası yok.
- **Kapsam dışı:** `post/*.html` (1.129 blog sayfası) bu değişikliğe dahil değil — onlar zaten kendi ayrı (daha basit) blog footer'ını kullanıyor, ayrı bir karar/görev.
- **Durum:** ✅ K5 tamamlandı, push edilecek.

### DK-2026-08-03-01 — Eğitimler formu: MS Forms iframe kaldırıldı, gerçek Power Automate gönderimine bağlandı (K3 tamamlandı)

- **Yapan:** Onur Bozok'un "sonnetle olanları yapalım hemen" talebi üzerine Claude (PDM asistanı).
- **Düzeltilen bulgu (K3, düzeltilmiş teşhis):** Orijinal denetimde bu sayfadaki form "sahte, hiçbir yere göndermiyor" olarak işaretlenmişti; dosya tam okunduğunda bu markup'ın (`handleSubmit` çağıran `<form>`) fiilen bir HTML yorum bloğu (`<!-- ESKI FORM KALDIRILDI ... -->`) içinde, yani ölü kod olduğu görüldü. Sayfadaki gerçek canlı eleman, `cadbim_iletisim.html`'dekiyle aynı türden ölçülemez bir **MS Forms iframe**'di (`forms.cloud.microsoft/...`) — bulgunun asıl niteliği O4'e (marka-kopuk iframe) daha yakın, ama düzeltme aynı: gerçek gönderim yapan yerel bir form.
- **Yapılan (`cadbim_egitimler.html`):**
  1. Kontrast: `--w30:rgba(255,255,255,0.3)` → `0.58` (7 kullanım, WCAG AA).
  2. MS Forms iframe kaldırıldı; yorumdaki eski form canlandırıldı — tüm alanlara `name` eklendi (`ad_soyad`, `sirket`, `email`, `telefon`, `egitim_konusu`, `katilimci_sayisi`, `format`, `baslangic_tarihi`, `beklentiler`), yeni zorunlu KVKK onay kutusu eklendi, form/buton/not paragrafına sabit ID'ler verildi (`egitim-form`, `submit-btn`, `form-note-text`).
  3. Sahte 3 saniyelik `handleSubmit` (ağ isteği yok) → teklif-iste/sanatsal-baski'de kullanılan **aynı `POWER_AUTOMATE_URL`**'e gerçek `fetch()` POST'u yapan uygulama ile değiştirildi. Akışın mevcut "else" dalının beklediği alan adlarına (`sirket`, `talep_turu`, `mesaj`) eğitime özel veriler (yazılım/katılımcı/format/tarih/beklenti) biçimlendirilerek paketlendi — akışta yeni dal açmaya gerek kalmadı.
- **Doğrulama (yerel önizleme):** Etiket dengesi kod incelemesiyle teyit edildi (245/245 div, 1/1 form), `forms.cloud.microsoft` referansı 0. Tarayıcıda form alanları dolduruldu, gerçek gönderim tetiklendi (`requestSubmit`) — `fetch()` doğru `POWER_AUTOMATE_URL`'e doğru JSON gövdeyle (form_type: egitim_talebi) gitti, buton "Talebiniz alındı!" başarı durumuna geçti, konsol hatası yok. (Not: sayfadaki bazı ürün logosu görselleri `naturalWidth=0` gösterdi ama bu `loading="lazy"` + henüz viewport'a girmemiş olmalarından kaynaklanıyor — dosyalar `assets/logos/products/`'ta mevcut, bu değişiklikle ilgisiz, ayrı doğrulanabilir.)
- **Güvenlik notu:** Test gönderimi sırasında `cadbim@cadbim.com.tr` kutusuna 1 test e-postası gitmiş olabilir (CC: marketing@) — gerçek talep değildir.
- **Durum:** ✅ K3 tamamlandı, push edilecek. Sıradaki: K5 (189 sayfada footer içeriği).

### DK-2026-08-02-09 — Başarı öykülerine 19 gerçek müşteri logosu eklendi

- **Yapan:** Claude (PDM asistanı) — Onur'un "logoları internetten al" talebi üzerine.
- **Kapsam:** `cadbim_basari_oykuleri.html`'deki 19 müşteri kartının her birindeki jenerik Tabler ikon rozeti (veya video-only kartlarda hiç olmayan rozet), o şirketin **kendi resmi web sitesinden** alınan gerçek logo ile değiştirildi/eklendi: Güralp Vinç, Sistem Teknik (Electron), Efe Kalıp Makina, Norm Additive, Habaş, Edvan, Eys Metal, Kutlusan Kafes, Eltaş, Erdemgiller, BMC, Decons, Bedesten Ahşap, Ordinat İnşaat, Limtaş Mühendislik, Epig Mimarlık, Demirce, Funjitsu Oyun ve Teknoloji, Tiplay Studio.
- **Kaynak yöntemi:** Autodesk'in orijinal vaka çalışması sayfaları çoğunlukla artık 403/yönlendirme veriyor (ayrı bir bulgu — bkz. kapsam dışı notu), bu yüzden her şirketin kendi resmi sitesine gidilip header/footer'daki logo görseli (veya CSS `background-image`'ı) bulunup indirildi. Her logo Pillow ile şeffaf kenar boşluğu kırpıldı ve 90px yüksekliğe (retina için) ölçeklendi; SVG'ler orijinal haliyle korundu. Yeni dosyalar `assets/logos/success-stories/` altında.
- **Tasarım:** Logolar beyaz yuvarlak köşeli bir rozet (`.story-logo`) içinde gösteriliyor (çoğu logo koyu/renkli, beyaz zeminde okunur oluyor). 2 istisna — Funjitsu ve Norm Additive'in logoları şeffaf zeminde beyaz — bu ikisi `.story-logo-dark` ile koyu rozet alıyor.
- **Güvenlik notu:** GPU/Browser-pane çökme riskini (bkz. sohbet) azaltmak için son 3 logo (Funjitsu, Tiplay Studio, BMC) `curl` ile ham HTML çekilip regex'le logo yolu bulunarak indirildi, tarayıcı penceresi açılmadan.
- **Telif hatırlatması (bilgi amaçlı):** Bu logolar her şirketin kendi resmi sitesinden alındı, üçüncü taraf logo bankalarından değil. Ancak bir müşterinin logosunu "referans" olarak sergilemek genelde o müşterinin bilgisi/onayı dahilinde yapılan bir B2B pratiğidir — bu 19 şirketin çoğu zaten Autodesk'in kendi yayınladığı vaka çalışmalarında adı geçtiği için bu türden bir kullanıma açık olduklarını gösteriyor, ama nihai karar ve ilişki yönetimi Onur'da.
- **Doğrulama:** Yerel önizlemede sayfa açılıp 19 logonun tamamı için `fetch()` ile HTTP 200 doğrulandı, konsol hatası yok, `div` etiket dengesi sağlam (103=103).
- **Kapsam dışı / not edildi:** Kart içindeki "Autodesk'te kaynağı gör" linklerinden en az biri (Efe Kalıp Makina) artık 403/yönlendirme veriyor — Autodesk bu vaka çalışması sayfalarını taşımış/kaldırmış olabilir; bu linklerin toplu kontrolü ayrı bir görev olarak bırakıldı. Ölçülebilir metrik + isimli alıntı eklenmesi de hâlâ bekliyor (ayrı konuşma konusu).
- **Durum:** ✅ Tamamlandı, push edilecek.

### DK-2026-08-02-08 — Tabler ikon fontu yerelleştirildi ve 289 ikona subset edildi (K7 tamamlandı)

- **Yapan:** Claude (PDM asistanı) — Onur'un "fontTools'u kur, yap" talebi üzerine.
- **Sorun:** Site, 5.193 ikonluk tam Tabler Icons webfont'unu CDN'den (`cdn.jsdelivr.net`) çekiyordu (`tabler-icons.min.css` ~21KB brotli + `tabler-icons.woff2` 462KB — sıkıştırılamaz, olduğu gibi iner) ama sitede yalnızca ~289 farklı ikon kullanılıyordu.
- **Yapılan:** `pip install fonttools brotli` ile kuruldu. CDN'den tam `.ttf` kaynak font + CSS indirildi; site genelinde (`*.html` + `post/*.html`, statik grep) kullanılan ikon sınıfları çıkarıldı, CSS'teki `content:"\eXXX"` eşlemesiyle codepoint'lere bağlandı. Ayrıca `mobilenav.js`'in JS içinde dinamik ürettiği arama/menü ikonları (`ti-box`, `ti-building`, `ti-file`, `ti-home`, `ti-mail`, `ti-phone`, `ti-search`, `ti-send`, `ti-tools`, `ti-topology-star-3`, `ti-x` vb.) da statik HTML taramasına dahil değildi — ayrıca kontrol edilip eklendi. Bu taramada `mobilenav.js`'de var olan bir hata da ortaya çıktı: "Yasal" kategori ikonu olarak Tabler'da hiç var olmayan `ti-file-shield` kullanılıyordu (CDN'in tam setinde bile karşılığı yok) — anlamlı bir alternatif olan `ti-gavel` ile değiştirildi.
- `python -m fontTools.subset` ile 289 codepoint'e göre `.ttf`'den `.woff2` subset üretildi (`assets/fonts/tabler-icons-subset.woff2`, 33,4KB) ve yalnızca bu 289 kuralı içeren yerel CSS yazıldı (`assets/css/tabler-icons-subset.css`, 11,6KB — sistemin `@font-face` + `.ti` taban kuralı + her ikon için `.ti-xxx:before{content:"\eXXX"}`).
- **1.319 sayfadaki CDN linki** (`<link rel="stylesheet" href="https://cdn.jsdelivr.net/...">`) yerel dosyaya çevrildi (kök: `assets/css/...`, post: `../assets/css/...`).
- **Kazanç:** ~483KB (woff2 462KB + CSS ~21KB) → ~45KB (font 33,4KB + CSS 11,6KB, gzip'le daha da düşer) — tek sayfa ilk yükünde **~%91 azalma**, CDN bağımlılığı (DNS/TLS/round-trip) tamamen kalktı.
- **Doğrulama:** Font glyph'leri canvas piksel testiyle doğrulandı (4 farklı ikon, her biri farklı piksel deseniyle doğru render oluyor; subset dışı rastgele bir codepoint boş dönüyor — subsetleme doğru çalışıyor). Kök ve post sayfalarında ağ isteği 200 OK, konsol hatası yok. `cdn.jsdelivr.net` referansı sitede 0'a indi.
- **Bakım notu:** Yeni bir ikon sınıfı eklenirse bu subset'in yeniden üretilmesi gerekir (üretim script'leri `scratchpad`'de, tekrarlanabilir hale getirilmedi — sonraki oturumda `docs/`'a taşınabilir).
- **Durum:** ✅ Tamamlandı, push edilecek.

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
