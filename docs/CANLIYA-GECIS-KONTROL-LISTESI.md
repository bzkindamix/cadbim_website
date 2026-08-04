# CADBİM Web Sitesi — Canlıya Geçiş Kontrol Listesi

**Oluşturulma:** 4 Ağustos 2026 · **Hedef:** cadbim.com.tr'nin Wix'ten yeni siteye (statik HTML, host: Natro) SEO kaybı olmadan taşınması.

**İlişkili dokümanlar:**
- `docs/CANLIYA-GECIS-URL-HARITASI.md` — 665 URL'nin eski→yeni eşlemesi, strateji, blog/koleksiyon kararları
- `docs/redirects-taslak.csv` — 665 satırlık ham eşleme tablosu (388 KURAL + 277 BİREBİR)
- `docs/htaccess-taslak.txt` — Natro'ya yüklenecek `.htaccess` taslağı (955 satır: kanonik host, 301 haritası, temiz URL çözümü, güvenlik başlıkları, sıkıştırma/önbellek)
- `docs/SITE-DENETIM-RAPORU-2026-08-02.md` — iç denetim (K/Y/O/D bulguları)
- `docs/DEGISIKLIK-KAYITLARI.md` — tüm değişikliklerin PDM kaydı (özellikle **DK-2026-08-04-39**: dış denetim kapama paketi)

**Nasıl kullanılır:** Kutucuklar Onur tarafından işaretlenir. `[Onur]` etiketli kalemler bir karar/onay gerektirir; `[Teknik]` etiketli kalemler Natro cPanel'de veya tarayıcıda yapılan bir işlemdir. Bu liste tamamlanmadan **canlıya geçilmemelidir** — özellikle Bölüm B (sunucu) atlanırsa site hiçbir temiz URL'i çözemez.

---

## A. Karar Bekleyen Kalemler `[Onur]`

Geçiş tarihinden önce netleşmesi gereken, teknik olarak "doğru" tek cevabı olmayan kalemler.

- [ ] **K9 — `assets/products/designjet/` klasörü (2,5 GiB, 18 dosya, ham basın görseli/videosu).** Hiçbir sayfadan referans almıyor, `.gitignore`'da (repoya girmiyor) ama **yerel diskte duruyor** — FTP/cPanel dosya yöneticisiyle "tüm klasörü yükle" yapılırsa bu 2,5 GiB sunucuya çıkar (deploy edilebilir site kendisi ~250 MB). Karar: (1) klasörü repo dışına taşı (örn. `D:\cadbim-ham-asset\`), (2) veya yükleme sırasında elle hariç tut, (3) veya sil (kaynak dosyalar başka yerde yedekliyse). **Öneri:** (1).
- [ ] **D4 — Marka yazımı: "Cadbim" mi "CADBİM" mi?** Sitede gövde metinlerinde "Cadbim", logoda ve bazı başlıklarda "CADBİM" karışık kullanılıyor. Tek yazım kararlaştırılıp `<title>`/kopya genelinde uygulanmalı (kapsamlı bir bul-değiştir gerektirir, geçiş öncesi veya sonrası yapılabilir — SEO'yu bloklamıyor).
- [ ] **Eski Wix sitesinin arşivi alındı mı?** Geçişten önce eski cadbim.com.tr'nin tam bir yedeği (sayfa görüntüleri + varsa Wix "site dışa aktar" özelliği) alınmalı — geri dönüş ihtiyacı veya eski içerikte referans gerekirse.

> Not (2026-08-04 teyidi): Önceki "GÖZDEN" ve "blog A/B" karar kalemleri **kapatılmıştır** (`docs/CANLIYA-GECIS-URL-HARITASI.md` §5, 2026-07-28). `docs/redirects-taslak.csv`'de artık 0 GÖZDEN satırı var (388 KURAL + 277 BİREBİR, hepsi kararlı). Aşağıdaki bölümler yalnızca teknik/doğrulama adımlarıdır.

---

## B. Sunucu Yapılandırması (Natro) `[Teknik]`

**Bu bölüm atlanırsa site çalışmaz** — şu an yalnızca `docs/htaccess-taslak.txt` içinde bir taslak var, sunucuya hiç yüklenmedi.

- [ ] `docs/htaccess-taslak.txt` bir **staging/test alt alan adında** denendi (örn. `test.cadbim.com.tr` veya cPanel'in geçici alan adı özelliği) — canlıya çıkmadan önce.
- [ ] Test sonrası dosya **UTF-8 (BOM'suz)** kaydedilip `.htaccess` adıyla Natro cPanel dosya yöneticisinden **site köküne** yüklendi.
- [ ] Yükleme sonrası örnekleme: `/autocad`, `/post/3d-gorunum`, `/teklif-iste`, `/designjet-z6pro` gibi 10-15 temiz URL canlıda tarayıcıda **200** ve doğru içerikle açılıyor (uzantısız + `.html`'siz).
- [ ] `.html` uzantılı doğrudan erişim (`/cadbim_autocad.html`) canlıda temiz URL'e **301** ile yönleniyor (çift içerik önleme).
- [ ] Eski Wix URL'lerinden 10-15 örnek (`docs/redirects-taslak.csv`'den rastgele seçilmiş KURAL satırları) canlıda doğru hedefe **301** veriyor.
- [ ] Güvenlik başlıkları canlıda geldi mi: `curl -I https://www.cadbim.com.tr/` çıktısında `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` görünüyor.
- [ ] Sıkıştırma/önbellek çalışıyor mu: `curl -I` çıktısında CSS/JS için `Content-Encoding: gzip` (veya `br`) ve statik varlıklarda `Cache-Control`/`Expires` var.
- [ ] **HSTS henüz AÇILMADI** (taslakta bilinçli yorum satırı) — SSL'in tüm alt alan adlarında sorunsuz çalıştığı en az 1-2 hafta canlıda doğrulandıktan sonra düşük `max-age` ile açılıp kademeli artırılacak. Bu adımı unutma listesine ekle (geçişin kendisini bloklamaz).
- [ ] `www` yönlendirmesi + HTTPS zorlaması aktif (`cadbim.com.tr` → `https://www.cadbim.com.tr`).
- [ ] SSL sertifikası alan adında geçerli (Natro AutoSSL veya eşdeğeri), tarayıcıda kilit ikonu uyarısız.

---

## C. SEO Altyapısı `[Teknik]`

- [ ] `sitemap.xml` (1.209 URL) canlı host'ta `https://www.cadbim.com.tr/sitemap.xml` adresinden **200** dönüyor ve içerik doğru.
- [ ] `robots.txt` canlıda yayında, `Sitemap:` satırı doğru host'u gösteriyor (şu an `Allow: /` — genel izin doğru, staging'deki `noindex` katmanıyla karışmadığı teyit edildi).
- [ ] `sitemap.xml` Google Search Console'a gönderildi.
- [ ] **Search Console'da "Adres Değişikliği" aracı KULLANILMAYACAK** — alan adı aynı kalıyor (sadece host/platform değişiyor), bu araç yalnızca alan adı değişiminde gerekli.
- [ ] Search Console mülk doğrulaması (DNS TXT veya HTML dosyası) yeni host üzerinden teyit edildi.
- [ ] GSC mülkü **"Alan Adı (Domain)" tipinde** doğrulandı (DNS TXT) — www/non-www ve http/https tüm varyantları tek mülkte toplar. Wix döneminden kalan eski bir URL-öneki mülkü varsa onunla çakışmadığı teyit edildi.
- [ ] `canonical` etiketleri örnekleme ile kontrol edildi — artık staging (`bzkindamix.github.io`) değil, gerçek `www.cadbim.com.tr` URL'lerini gösteriyor (bu zaten kod tarafında doğruydu, sadece host değişince canlıda teyit).
- [ ] Geçiş sonrası **URL Inspection → "Dizine eklenmeyi iste"** ana sayfa + öncelikli 10-15 sayfa için yapıldı (yeni host'ta taramayı hızlandırır).
- [ ] Bing Webmaster Tools'a da sitemap gönderimi (opsiyonel ama ücretsiz ek kapsama).

---

## D. Formlar & Entegrasyonlar `[Teknik]`

- [ ] **3 form** (Teklif İste, Sanatsal Baskı, Eğitim) canlı alan adından **gerçek bir test gönderimi** ile denendi — Power Automate uç noktası (`*.powerplatform.com`) yeni domainden CORS/engel almadan çalışıyor mu.
- [ ] Test gönderimleri sonrası `cadbim@cadbim.com.tr` / `sanatsalbaski@cadbim.com.tr` kutularına (CC: `marketing@cadbim.com.tr`) e-posta ulaştı — sonra bu test kayıtları Power Automate/Dynamics tarafında temizlenebilir.
- [ ] GA4 (`G-DTTE7C82NB`) çerez onayından SONRA yükleniyor — canlıda `cookie-consent.js` banner'ı görünüyor, "Kabul Et" sonrası ağ isteklerinde `googletagmanager.com` çağrısı var (tarayıcı geliştirici araçlarıyla teyit).
- [ ] WhatsApp widget'ı (`https://wa.me/905532426737`) canlıda çalışıyor, doğru ön-tanımlı mesajla açılıyor.
- [ ] `cadbim_iletisim.html`'deki harita iframe'i (`maps.google.com`) canlıda CSP'ye takılmadan yükleniyor.

---

## E. İçerik & Görsel Son Kontrol `[Teknik]`

- [ ] Favicon + `apple-touch-icon-180.png` + `site.webmanifest` canlıda doğru gösteriliyor (mobilde "Ana Ekrana Ekle" denenerek).
- [ ] 404 sayfası canlıda var olmayan bir URL'de tetikleniyor ve doğru görünüyor.
- [ ] Ana sayfa + 5 farklı ürün sayfası + 2 blog yazısı **masaüstü ve mobilde** görsel olarak gözden geçirildi (nav, footer, form, görsellerin yüklendiği).
- [ ] YouTube facade'ları (küçük resim + oynat düğmesi) canlıda çalışıyor, tıklayınca `youtube-nocookie.com` videosu açılıyor.
- [ ] Skip-link ("İçeriğe geç") bir sayfada Tab tuşuyla test edildi, görünür oluyor.

---

## F. Yayın Günü — Sıralı İşlem `[Teknik]`

1. [ ] Eski Wix sitesinin son hâli arşivlendi (Bölüm A).
2. [ ] DNS/host bilgileri Natro'ya yönlendirildi (A kaydı / nameserver — Onur'un domain sağlayıcısına göre).
3. [ ] Bu repodaki dosyalar Natro'ya FTP/cPanel dosya yöneticisiyle yüklendi — **`assets/products/designjet/` klasörü HARİÇ TUTULARAK** (K9 kararına göre).
4. [ ] `.htaccess` yüklendi (Bölüm B).
5. [ ] SSL aktif edildi, `https://www.cadbim.com.tr` açılıyor.
6. [ ] Bölüm B/C/D/E'deki tüm doğrulamalar canlıda tekrar edildi.
7. [ ] Eski Wix aboneliği/domain yönlendirmesi kapatılmadan önce **en az 48 saat** yeni site izlendi (bkz. Bölüm G).

---

## G. Yayın Sonrası İzleme

- [ ] **İlk 48 saat:** Sunucu 404 logları (Natro cPanel → "Hata Günlükleri") kontrol edildi; eksik 301 varsa `docs/htaccess-taslak.txt`'e yama eklenip yeniden yüklendi.
- [ ] **İlk hafta:** Google Search Console → Kapsam raporu günlük kontrol; beklenmeyen 404/yönlendirme hatası var mı.
- [ ] **4 hafta:** Search Console kapsama + performans raporu haftalık takip; eski Wix URL'lerinin indeksten düşüp yeni URL'lerin göründüğü teyit edildi.
- [ ] **2 hafta sonra:** HSTS `max-age` düşük değerle açıldı (Bölüm B notu), sorun yoksa 4-6 hafta sonra kalıcı değere yükseltildi.
- [ ] GA4'te gerçek (test olmayan) form gönderimleri ve trafik verisi akıyor mu — 1 hafta sonra kontrol.

---

## H. Geri Alma Planı (Rollback)

- [ ] Natro'da yükleme öncesi cPanel'in kendi yedekleme özelliğiyle (varsa) veya elle bir "önceki durum" notu alındı.
- [ ] `.htaccess` sorun çıkarırsa hızlı geri alma: cPanel dosya yöneticisinden dosyayı silmek siteyi (temiz URL'ler hariç) eski Wix'e değil, "sunucu 404'ü"ne döndürür — bu yüzden asıl geri dönüş planı DNS'i geçici olarak eski barındırmaya çevirmektir (yalnızca domain sağlayıcısı üzerinden mümkünse).
- [ ] Kritik bir form/ödeme akışı bozulursa: Power Automate akışı koda bağlı değil, ayrı bir bulut kaynağı — sitede sorun olsa da e-posta/telefon üzerinden manuel talep alınabileceği not edildi.
