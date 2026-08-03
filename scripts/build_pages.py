# -*- coding: utf-8 -*-
"""GitHub Pages onizleme kopyasini uretir (_site/).

NEDEN BIR DONUSTURME ADIMI VAR?
Site cadbim.com.tr'nin ALAN KOKUNDE yayinlanmak uzere yazildi; bu yuzden
`/`, `/favicon.svg`, `/feed.xml`, `/site.webmanifest` gibi mutlak yollar
uretimde DOGRUdur. GitHub Pages proje sitesi ise bir ALT DIZINDE
(/cadbim_website/) servis edilir ve ayni yollar orada kirilir:
  /            -> bzkindamix.github.io koku (yanlis site)
  /favicon.svg -> 404
Bu betik `main` dalini uretim icin dogru halde birakip yalnizca onizleme
kopyasinda bu yollari onekler. Boylece canliya gecerken hicbir sey geri
alinmasi gerekmez.

AYRICA: onizleme kopyasindaki her sayfaya `noindex, nofollow` eklenir ki
Google test kopyasini dizine almasin (canli siteyle mukerrer icerik olmasin).
Proje sitelerinde /robots.txt alan kokune ait oldugu icin depo icindeki
robots.txt burada islemez -- bu yuzden meta etiketi kullanilir.
"""
import io
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '_site')
PREFIX = '/cadbim_website/'

# Kopyalanmayacaklar (kaynak/gelistirme dosyalari)
SKIP_DIRS = {'.git', '.github', '.claude', 'scripts', 'docs', '_site',
             '.icon-subset-cache', '__pycache__'}
SKIP_FILES = {'dev_server.py', 'handoff.md', 'README.md', '.gitignore',
              'missing_videos.json', 'new_videos_notify.txt'}

# Onizlemede oneklenecek mutlak yollar (uretimde dogru olduklari icin
# main'de degistirilmezler)
ABS_PATHS = [
    ('href="/"', 'href="%s"' % PREFIX),
    ('href="/favicon.svg"', 'href="%sfavicon.svg"' % PREFIX),
    ('href="/site.webmanifest"', 'href="%ssite.webmanifest"' % PREFIX),
    ('href="/assets/apple-touch-icon-180.png"',
     'href="%sassets/apple-touch-icon-180.png"' % PREFIX),
    ('href="/feed.xml"', 'href="%sfeed.xml"' % PREFIX),
    ('src="/assets/', 'src="%sassets/' % PREFIX),
]

NOINDEX = ('<meta name="robots" content="noindex, nofollow">'
           '<!-- ONIZLEME KOPYASI: canli site cadbim.com.tr -->')


def transform_html(s):
    for a, b in ABS_PATHS:
        s = s.replace(a, b)
    # mevcut robots meta'sini onizleme icin noindex'e cevir, yoksa ekle
    if re.search(r'<meta name="robots"[^>]*>', s):
        s = re.sub(r'<meta name="robots"[^>]*>', NOINDEX, s, count=1)
    elif '<head>' in s:
        s = s.replace('<head>', '<head>\n' + NOINDEX, 1)
    return s


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    n_html = n_other = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel = os.path.relpath(dirpath, ROOT)
        if rel == '.':
            rel = ''
        if rel.split(os.sep)[0] in SKIP_DIRS:
            continue
        target_dir = os.path.join(OUT, rel) if rel else OUT
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        for fn in filenames:
            if fn in SKIP_FILES or fn.endswith('.pyc'):
                continue
            src = os.path.join(dirpath, fn)
            dst = os.path.join(target_dir, fn)
            if fn.lower().endswith('.html'):
                s = io.open(src, encoding='utf-8').read()
                io.open(dst, 'w', encoding='utf-8', newline='').write(transform_html(s))
                n_html += 1
            else:
                shutil.copy2(src, dst)
                n_other += 1

    # Jekyll'i devre disi birak (alt cizgiyle baslayan klasorleri atlamasin)
    io.open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    # Proje sitelerinde bu dosya crawler tarafindan okunmaz; yine de birakiyoruz
    io.open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8', newline='').write(
        'User-agent: *\nDisallow: /\n')
    return n_html, n_other


if __name__ == '__main__':
    h, o = build()
    print('_site uretildi: %d HTML + %d diger dosya' % (h, o))
    # dogrulama: onizlemede kalan kirik mutlak yol var mi
    bad = 0
    for dirpath, dirnames, filenames in os.walk(OUT):
        for fn in filenames:
            if not fn.lower().endswith('.html'):
                continue
            s = io.open(os.path.join(dirpath, fn), encoding='utf-8').read()
            # 404.html'deki data-path baglantilari calisma aninda window.__prefix
            # ile yeniden yazilir (bkz. 404.html alt kismindaki betik) -- muaf.
            s = re.sub(r'<a data-path="[^"]*" href="/[^"]*"', '', s)
            for m in re.finditer(r'(?:href|src)="(/(?!cadbim_website/)[^"]*)"', s):
                bad += 1
                if bad <= 5:
                    print('  KALAN MUTLAK YOL', fn, m.group(1))
    print('onizlemede kalan mutlak yol: %d' % bad)
    sys.exit(1 if bad else 0)
