# HP Video Kaynak Politikası (DesignJet & HP ürün sayfaları)

**Amaç:** Sitedeki HP ürün sayfalarına yalnızca **resmi + doğru ürüne ait** tanıtım videosu gömmek. Marka kuralı: bayi/3. şahıs kanalından embed edilmez.

## Birincil yöntem — hp.com kaynaklı (STANDART)

Kanal ismi tahmin etme. HP'nin **kendi ürün sayfasına** koyduğu video, tanım gereği resmidir ve doğru üründür.

1. Ürünün resmi **hp.com** sayfasını **tarayıcıda** aç (WebFetch değil — video JS ile yüklenir).
2. Sayfadaki video **iframe src / videoId**'sini oku → resmi YouTube ID.
3. Embed'i tarayıcıda test et (oynatıcı yükleniyor mu, "unavailable" var mı).
4. Site şablonuyla göm: "Modeller & Varyantlar" bölümünden sonra, responsive 16:9, `youtube-nocookie.com`, `loading="lazy"`.
5. hp.com'da video yoksa → sayfa videosuz bırakılır (yanlış video koymaktansa boş iyidir).

## Yedek ölçüt — onaylı HP resmi kanalları (whitelist)

hp.com'da video bulunmayan durumlar için. Bir kanalın HP'ye ait olduğu 3 kontrolle doğrulanır: (a) doğrulanmış rozet, (b) "Hakkında" hp.com'a link, (c) hp.com sosyal linklerinden erişilebilir olması.

| Kanal | Durum |
|---|---|
| HP (ana, @HPInc) | ✅ Resmi |
| HP India | ✅ Resmi bölgesel |
| HP Asia | ✅ Resmi bölgesel |
| HP UK | ✅ Resmi bölgesel |
| HP Support | ✅ Resmi (destek/ipucu) |
| HP Graphic Arts (@HPGraphicArts) | ✅ Resmi (geniş format) |
| HPE / @hpe | ❌ Farklı şirket (Hewlett Packard Enterprise) — DesignJet ile ilgisiz |
| "HP Plotter" (user/HPPlotter) | ❌ Bayi (Resolution GB Ltd) |
| "ACP techWERK" | ❌ Bayi (ACP TechRent GmbH) |
| Diğer "HP..." adlı bayi/3. şahıs | ❌ Reddet |

**Not:** İsimde "HP" geçmesi resmi olduğu anlamına gelmez. HP Inc ≠ HPE ayrımına dikkat.

## Bilinen resmi video ID'leri (kaydedildikçe)

| Ürün sayfası | Video ID | Kaynak |
|---|---|---|
| designjet_xl3600 | cuvHfdbQaNE | Onur (doğrulandı) |
| designjet_t870 | CNG6QSRUDSQ | Onur (doğrulandı) |
| designjet_t850 | hRa2oRinXyc | hp.com T850/T870/T950 seri sayfası |
| designjet_t950 | hRa2oRinXyc | hp.com seri sayfası (T850 ile aynı — Onur onayladı) |
| designjet_t200 | hzxO73kldmc | hp.com T200 sayfası ("Simple. Compact. Responsible.") |
| designjet_t600 | 6WzCOBtWuGQ | hp.com T600 sayfası ("Simple. Compact. Responsible.") |
| designjet_t1600 | ZEnzBgbS2yk | hp.com T1600/T2600 "Build Connected" seri sayfası (T2600 ile aynı) |
| designjet_t2600 | ZEnzBgbS2yk | hp.com T1600/T2600 "Build Connected" seri sayfası |
| designjet_xl3800 | MbASXZgN3tI | hp.com XL 3800 sayfası ("Introducing XL 3800 MFP") |
| designjet_z6pro | EgbZf_9Ewjg | hp.com Z6 Pro sayfası ("Out Of This World Precision") |
| designjet_z9pro | zj8HtwqYn7w | Resmi HP kanalı ("Introducing Z6 Pro and Z9⁺ Pro"); hp.com Z9 Pro sayfasında YouTube yok (self-host), fallback |
| designjet_smart_tank | zsYVMY0h3uU | Resmi **HP Asia** kanalı ("Smart Tank T858/T908: First Large Format Ink Tank"); hp.com'da YouTube yok, whitelist fallback |

### Videosuz bırakılanlar (resmi HP videosu bulunamadı)

| Ürün | Neden |
|---|---|
| designjet_t830 | hp.com'da YouTube yok; bulunan "T830 Product Video" bayi kanalı (GDS/Graphic Design Supplies) — reddedildi |
| designjet_t1700 | hp.com'da YouTube yok; resmi tekil ürün videosu yok (eski model) |
| designjet_z6810 | hp.com'da YouTube yok (üretim yazıcısı, niş) |
| designjet_z6ps / z9ps | hp.com Z6/Z9 PostScript sayfasında YouTube yok; Pro serisi videosu farklı ürün hattı, konmadı |
| designjet_sd_pro / hd_pro | Tarayıcılar; hp.com'da resmi ürün videosu yok |

> Reddedilen bayi kanalları (kayıt): GDS/Graphic Design Supplies (`HX3rbwWkW50`), GOM Australia (`fNsE5HG7GCY`) — isimde/başlıkta HP geçse de resmi değil.

> Ek not: `hRa2oRinXyc` seri videosu T850 + T870 + T950'yi birlikte anlatıyor; T870/T950 için de geçerli bir resmi seçenek. `hbLl7KoiEqA` (teaser) ve `Yj-cYh12vBs` (multi-size özellik) da aynı hp.com sayfasında yer alan resmi alternatifler.
