# -*- coding: utf-8 -*-
"""Cozumler mega menusundeki gruplari yeniden kurar (tum sayfalarda).

Eski durum (6 kolon) ve sorunlari:
  - "Dijital Ikiz" ve "Sanatsal Baski" kolonlarinda TEK oge vardi; menu
    genisliginin 1/3'u bos duruyordu.
  - Gruplar disiplin mantigina oturmuyordu: Insaat Proje Yonetimi "Veri &
    Surec Yonetimi"nde, Gerceklik Yakalama "Gorsellestirme"de, Dijital Ikiz
    ise Fabrika Tasarimi ile ayni ise bakmasina ragmen ayri kolondaydi.
  - 6 kolonda her kolon ~170px kaliyor, hem etiketler hem oge adlari iki
    satira sariyordu.

Yeni durum: ustte one cikan "Dijital Donusum", ortada musterinin kendini
tanimladigi 5 disiplin kolonu, altta one cikan "Sanatsal Baski Atolyesi"
(Onur 2026-07-26'da bunun kendi grubu olmasini istemisti; kolon yerine
one cikan satir olarak korunuyor -- daha gorunur, kolon israfi yok).
"""
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GROUPS = [
    (u'Yapı & Altyapı', [
        ('bim', u'BIM'),
        ('bim-icerik-uretimi', u'BIM İçerik & Obje Üretimi'),
        ('insaat-yonetimi', u'İnşaat Proje Yönetimi'),
        ('gerceklik-yakalama', u'Gerçeklik Yakalama'),
        ('dijital-ikiz', u'Dijital İkiz'),
    ]),
    (u'Ürün Tasarımı & Mühendislik', [
        ('simulasyon', u'Simülasyon & Analiz'),
        ('tolerans-analizi', u'Tolerans Analizi'),
        ('tasarim-otomasyonu', u'Tasarım Otomasyonu'),
    ]),
    (u'Üretim & İmalat', [
        ('cam', u'CAM & İmalat'),
        ('eklemeli-imalat', u'Eklemeli İmalat & 3D Baskı'),
        ('nesting', u'Nesting'),
        ('fabrika-tasarimi', u'Fabrika Tasarımı'),
    ]),
    (u'Veri & Süreç Yönetimi', [
        ('plm', u'PLM'),
        ('pdm', u'PDM'),
    ]),
    (u'Görselleştirme & İçerik', [
        ('gorsellestirme', u'Görselleştirme & Render'),
        ('yaratici-icerik', u'Yaratıcı İçerik & Tasarım'),
    ]),
]

OPEN = '<div class="nav-dropdown-menu nav-mega">'
ACTIVE_RE = re.compile(r'<a class="active" href="(?:\.\./)?([a-z0-9\-]+)"')


def close_div(html, start):
    depth = 0
    for m in re.finditer(r'</?div\b', html[start:]):
        if m.group(0).startswith('</'):
            depth -= 1
            if depth == 0:
                return start + m.start() + len('</div>')
        else:
            depth += 1
    return -1


def build(prefix, active):
    def link(slug, label):
        cls = ' class="active"' if slug == active else ''
        return u'            <a%s href="%s%s">%s</a>\n' % (cls, prefix, slug, label)

    cols = []
    for label, items in GROUPS:
        cols.append(u'          <div class="nav-mega-col">\n'
                    u'            <div class="nav-dd-label">%s</div>\n%s'
                    u'          </div>\n'
                    % (label, "".join(link(s, l) for s, l in items)))

    dd_cls = 'nav-dd-feat' + (' active' if active == 'dijital-donusum' else '')
    art_cls = 'nav-dd-feat nav-dd-feat-art' + (' active' if active == 'sanatsal-baski' else '')
    return (
        OPEN + u'\n'
        u'        <a href="%sdijital-donusum" class="%s"><i class="ti ti-sparkles" style="font-size:12px;"></i>Dijital Dönüşüm</a>\n'
        u'        <div class="nav-mega-cols">\n'
        u'%s'
        u'        </div>\n'
        u'        <a href="%ssanatsal-baski" class="%s"><i class="ti ti-brush" style="font-size:12px;"></i><span class="sanatsal-gradient">Sanatsal Baskı Atölyesi</span></a>\n'
        u'      </div>'
        % (prefix, dd_cls, "".join(cols), prefix, art_cls))


def main():
    files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    files += sorted(glob.glob(os.path.join(ROOT, 'post', '*.html')))
    changed = 0
    skipped = 0
    actives = {}
    for path in files:
        s = io.open(path, encoding='utf-8').read()
        i = s.find(OPEN)
        if i < 0:
            skipped += 1
            continue
        j = close_div(s, i)
        old = s[i:j]
        prefix = '../' if os.sep + 'post' + os.sep in path else ''
        m = ACTIVE_RE.search(old)
        active = m.group(1) if m else None
        if active:
            actives[os.path.basename(path)] = active
        new = build(prefix, active)
        if new == old:
            continue
        io.open(path, 'w', encoding='utf-8', newline='').write(s[:i] + new + s[j:])
        changed += 1
    return changed, skipped, actives


if __name__ == '__main__':
    n, sk, act = main()
    print('mega menu yeniden kuruldu : %d dosya' % n)
    print('mega menusu olmayan       : %d dosya' % sk)
    print('aktif isareti korunan     : %d sayfa' % len(act))
    for k in sorted(act)[:6]:
        print('   %-42s -> %s' % (k, act[k]))
