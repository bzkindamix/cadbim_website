# -*- coding: utf-8 -*-
"""Kart kutularinin tamamini tiklanabilir yapar.

Sorun: urun / endustri / marka / basari oykusu kartlarinda yalnizca <h3>
icindeki baglanti tiklanabiliyordu; kartin govdesine tiklamak hicbir sey
yapmiyordu. Bu betik

    <div class="card"> ... <h3><a href="X" ...>Baslik</a></h3> ... </div>

kaliplarini

    <a href="X" class="card"> ... <h3>Baslik</h3> ... </a>

haline getirir. Kart icinde baska bir <a> varsa (ic ice baglanti gecersiz
HTML uretir) dokunmadan birakir ve raporlar.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OPEN_RE = re.compile(r'<div class="card(?P<extra>[^"]*)"(?P<attrs>[^>]*)>')
TAG_RE = re.compile(r'</?div\b', re.I)
H3_RE = re.compile(
    r'<h3><a href="(?P<href>[^"]+)"(?P<aattrs>[^>]*)>(?P<title>.*?)</a></h3>', re.S)


def close_index(html, start):
    """`start` konumundaki <div ...> etiketinin kapanis </div>'ini bulur."""
    depth = 0
    for m in TAG_RE.finditer(html, start):
        if m.group(0).lower().startswith('</'):
            depth -= 1
            if depth == 0:
                return m.start(), html.index('>', m.start()) + 1
        else:
            depth += 1
    return None, None


def convert(html):
    out = []
    pos = 0
    changed = 0
    skipped = 0
    while True:
        m = OPEN_RE.search(html, pos)
        if not m:
            break
        c_start, c_end = close_index(html, m.start())
        if c_start is None:
            break
        inner = html[m.end():c_start]
        h3 = H3_RE.search(inner)
        if not h3:
            out.append(html[pos:m.end()])
            pos = m.end()
            continue
        # kart govdesinde bagimsiz baska bir <a> varsa dokunma
        rest = inner[:h3.start()] + inner[h3.end():]
        if '<a ' in rest or '<a\n' in rest:
            skipped += 1
            out.append(html[pos:c_end])
            pos = c_end
            continue
        new_inner = inner[:h3.start()] + '<h3>%s</h3>' % h3.group('title') + inner[h3.end():]
        extra = m.group('extra')
        attrs = m.group('attrs')
        new = ('<a href="%s" class="card%s"%s>%s</a>'
               % (h3.group('href'), extra, attrs, new_inner))
        out.append(html[pos:m.start()])
        out.append(new)
        pos = c_end
        changed += 1
    out.append(html[pos:])
    return "".join(out), changed, skipped


def main():
    files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    files += sorted(glob.glob(os.path.join(ROOT, 'post', '*.html')))
    total = tskip = nfiles = 0
    for path in files:
        src = io.open(path, encoding='utf-8').read()
        new, n, sk = convert(src)
        if n:
            io.open(path, 'w', encoding='utf-8', newline='').write(new)
            total += n
            tskip += sk
            nfiles += 1
            print('%-46s %4d kart' % (os.path.basename(path), n)
                  + ('  (%d atlandi)' % sk if sk else ''))
    print('-' * 60)
    print('%d dosyada %d kart tiklanabilir yapildi, %d atlandi.'
          % (nfiles, total, tskip))


if __name__ == '__main__':
    main()
