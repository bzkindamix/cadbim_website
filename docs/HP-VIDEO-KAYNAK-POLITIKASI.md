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

> Ek not: `hRa2oRinXyc` seri videosu T850 + T870 + T950'yi birlikte anlatıyor; T870/T950 için de geçerli bir resmi seçenek. `hbLl7KoiEqA` (teaser) ve `Yj-cYh12vBs` (multi-size özellik) da aynı hp.com sayfasında yer alan resmi alternatifler.
