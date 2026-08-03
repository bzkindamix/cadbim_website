# -*- coding: utf-8 -*-
"""Cozum sayfalari icin vektorel teknik illustrasyon uretir.

gen_sektor_visuals.py ile ayni cizim dili kullanilir: seffaf zemin, ince
hat cizimi, sitenin koyu navy/cyan paleti ve her cozume ait aksan rengi.
Uretilen SVG'ler assets/img/cozum/ altina yazilir; kendi CSS animasyonlarini
tasirlar, <img> ile yuklendiginde de calisir, harici bagimliligi yoktur.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_sektor_visuals import (  # noqa: E402
    CYAN, TAIL, f, head, iso, node, pts, scanline,
)

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "img", "cozum")


# --------------------------------------------------------------------------
# ortak yardimcilar
# --------------------------------------------------------------------------
def box(x, y, w, h, cls="ln", extra=""):
    return ('<rect class="%s" x="%s" y="%s" width="%s" height="%s" rx="3" %s/>'
            % (cls, f(x), f(y), f(w), f(h), extra))


def label(x, y, text, size=9, anchor="start", op=".55"):
    return ('<text x="%s" y="%s" font-family="Manrope,sans-serif" font-size="%d" '
            'fill="#fff" fill-opacity="%s" letter-spacing="1" text-anchor="%s">%s</text>'
            % (f(x), f(y), size, op, anchor, text))


def accent_text(x, y, text, accent, size=9, anchor="start"):
    return ('<text x="%s" y="%s" font-family="Manrope,sans-serif" font-size="%d" '
            'fill="%s" fill-opacity=".85" letter-spacing="1" text-anchor="%s">%s</text>'
            % (f(x), f(y), size, accent, anchor, text))


def arrow(x1, y1, x2, y2, accent, cls="cy", op=".7"):
    ang = math.atan2(y2 - y1, x2 - x1)
    a1 = (x2 - 7 * math.cos(ang - 0.4), y2 - 7 * math.sin(ang - 0.4))
    a2 = (x2 - 7 * math.cos(ang + 0.4), y2 - 7 * math.sin(ang + 0.4))
    return ('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity="%s"/>'
            '<polyline class="%s" points="%s" stroke-opacity="%s"/>'
            % (cls, f(x1), f(y1), f(x2), f(y2), op,
               cls, pts([a1, (x2, y2), a2]), op))


def dim_line(x1, y1, x2, y2):
    return ('<line class="dim" x1="%s" y1="%s" x2="%s" y2="%s"/>'
            % (f(x1), f(y1), f(x2), f(y2)))


def gear(cx, cy, r, teeth, cls="ln"):
    p = []
    ri, ro = r * 0.84, r
    step = math.pi / teeth
    for i in range(teeth):
        a0 = 2 * i * step
        p += [(cx + ri * math.cos(a0), cy + ri * math.sin(a0)),
              (cx + ro * math.cos(a0 + step * .35), cy + ro * math.sin(a0 + step * .35)),
              (cx + ro * math.cos(a0 + step * .65), cy + ro * math.sin(a0 + step * .65)),
              (cx + ri * math.cos(a0 + step), cy + ri * math.sin(a0 + step))]
    return ('<g class="spin"><polygon class="%s" points="%s"/>'
            '<circle class="%s" cx="%s" cy="%s" r="%s"/></g>'
            % (cls, pts(p), cls, f(cx), f(cy), f(r * .3)))


# --------------------------------------------------------------------------
def dijital_donusum():
    """Olgunluk basamaklari + yukselen egri."""
    a = CYAN
    o = head(a)
    steps = [("Cizim", 0), ("Model", 1), ("Veri", 2), ("Otomasyon", 3), ("Ikiz", 4)]
    bw, bd = 92, 54
    o += '<g class="float">\n'
    for name, i in steps:
        x = 60 + i * 108
        y = 300 - i * 42
        top = [(x, y), (x + bw, y - bd * .38), (x + bw + 26, y - bd * .06),
               (x + 26, y + bd * .32)]
        o += '<polygon class="fl" points="%s"/><polygon class="ln" points="%s"/>\n' % (
            pts(top), pts(top))
        # yan yuz
        o += ('<polygon class="ln2" points="%s"/>\n'
              % pts([top[3], top[2], (top[2][0], top[2][1] + 22), (top[3][0], top[3][1] + 22)]))
        o += ('<polygon class="ln2" points="%s"/>\n'
              % pts([top[0], top[3], (top[3][0], top[3][1] + 22), (top[0][0], top[0][1] + 22)]))
        cx, cy = x + bw * .58, y + 2
        o += node(cx, cy, 3.4)
        o += accent_text(x + 4, y + 44, "0%d" % (i + 1), a, 10)
        o += label(x + 24, y + 44, name, 9)
    o += "</g>\n"
    # basamaklari baglayan yukselen egri
    curve = []
    for i in range(0, 5):
        curve.append((60 + i * 108 + 53, 300 - i * 42 + 2))
    o += '<polyline class="cy draw" points="%s" stroke-opacity=".55"/>\n' % pts(curve)
    # arka planda trend
    tp = [(46, 150 - 46 * .0), ]
    tp = [(x, 210 - 118 * (1 - math.exp(-(x - 46) / 190.0))) for x in range(46, 606, 20)]
    o += '<polyline class="ln2" points="%s" stroke-opacity=".22"/>\n' % pts(tp)
    o += dim_line(46, 350, 606, 350) + dim_line(46, 344, 46, 356) + dim_line(606, 344, 606, 356)
    o += label(326, 368, "DONUSUM YOL HARITASI", 9, "middle", ".35")
    o += accent_text(470, 96, "VERI SUREKLILIGI", a, 9)
    o += '<line class="cy" x1="470" y1="104" x2="596" y2="104" stroke-opacity=".4"/>\n'
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def bim():
    """Ayrisik disiplin katmanlari + cakisma isareti."""
    a = "#818cf8"
    o = head(a)
    ox, oy, s = 300, 210, 1.0
    px, py = 190, 128
    corners = [(0, 0), (px, 0), (px, py), (0, py)]
    layers = [("MIMARI", 150), ("MEP", 92), ("STATIK", 34)]

    o += '<g class="float">\n'
    for idx, (name, z) in enumerate(layers):
        p = [iso(x, y, z, ox, oy, s) for x, y in corners]
        o += '<polygon class="fl" points="%s"/><polygon class="ln" points="%s"/>\n' % (
            pts(p), pts(p))
        if name == "STATIK":                       # kiris izgarasi
            for k in range(1, 5):
                x = px * k / 5.0
                b, t = iso(x, 0, z, ox, oy, s), iso(x, py, z, ox, oy, s)
                o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
                    f(b[0]), f(b[1]), f(t[0]), f(t[1]))
            for k in range(1, 4):
                y = py * k / 4.0
                b, t = iso(0, y, z, ox, oy, s), iso(px, y, z, ox, oy, s)
                o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
                    f(b[0]), f(b[1]), f(t[0]), f(t[1]))
        elif name == "MEP":                        # tesisat hatlari
            runs = [[(14, 20), (170, 20), (170, 74)],
                    [(14, 52), (96, 52), (96, 112)],
                    [(40, 108), (170, 108)]]
            for r in runs:
                q = [iso(x, y, z, ox, oy, s) for x, y in r]
                o += '<polyline class="cy draw" points="%s" stroke-opacity=".65"/>' % pts(q)
            for x, y in ((170, 74), (96, 112), (14, 20)):
                q = iso(x, y, z, ox, oy, s)
                o += node(q[0], q[1], 2.8)
        else:                                      # mimari duvarlar
            walls = [[(12, 12), (178, 12), (178, 116), (12, 116), (12, 12)],
                     [(96, 12), (96, 68)], [(96, 68), (178, 68)]]
            for w in walls:
                q = [iso(x, y, z, ox, oy, s) for x, y in w]
                o += '<polyline class="ln2" points="%s" stroke-opacity=".5"/>' % pts(q)
        o += "\n"
        # katman etiketi
        e = iso(px, py * .5, z, ox, oy, s)
        o += accent_text(e[0] + 22, e[1] + 4, name, a, 9)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3"/>\n' % (
            f(e[0] + 4), f(e[1]), f(e[0] + 18), f(e[1]))

    # hizalama eksenleri
    for x, y in corners:
        b = iso(x, y, layers[-1][1] - 14, ox, oy, s)
        t = iso(x, y, layers[0][1] + 14, ox, oy, s)
        o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" '
              'stroke-opacity=".22" stroke-dasharray="3 5"/>' % (f(b[0]), f(b[1]), f(t[0]), f(t[1])))
    o += "\n</g>\n"

    # cakisma isareti (MEP x STATIK)
    c = iso(96, 52, 63, ox, oy, s)
    o += ('<g class="blink"><circle cx="%s" cy="%s" r="13" fill="none" stroke="#f87171" '
          'stroke-opacity=".85" stroke-width="1.4"/>'
          '<path d="M%s %s l8 8 M%s %s l-8 8" stroke="#f87171" stroke-opacity=".85" '
          'stroke-width="1.4" fill="none"/></g>\n'
          % (f(c[0]), f(c[1]), f(c[0] - 4), f(c[1] - 4), f(c[0] + 4), f(c[1] - 4)))
    o += ('<text x="%s" y="%s" font-family="Manrope,sans-serif" font-size="9" '
          'fill="#f87171" fill-opacity=".8" letter-spacing="1">CAKISMA 01</text>\n'
          % (f(c[0] + 20), f(c[1] - 12)))

    # federe model paneli
    o += box(418, 318, 184, 84, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(432, 338, "FEDERE MODEL", a, 9)
    rows = [("Mimari", ".72"), ("Statik", ".55"), ("MEP", ".4")]
    for i, (t, op) in enumerate(rows):
        y = 360 + i * 15
        o += ('<rect x="432" y="%d" width="9" height="9" rx="2" fill="%s" fill-opacity="%s"/>'
              % (y - 7, a, op))
        o += label(448, y, t, 9, "start", ".5")
        o += ('<rect x="524" y="%d" width="62" height="4" rx="2" fill="%s" fill-opacity=".18"/>'
              '<rect x="524" y="%d" width="%d" height="4" rx="2" fill="%s" fill-opacity=".6"/>'
              % (y - 4, a, y - 4, int(62 * (0.9 - i * .16)), a))
    o += "\n" + scanline(a, 70)
    return o + TAIL


# --------------------------------------------------------------------------
def simulasyon():
    """Konsol kirisin FEA agi + gerilme bantlari + yuk oklari."""
    a = "#fbbf24"
    o = head(a)
    x0, y0, w, h = 120, 170, 380, 110

    # ankastre mesnet taramasi
    o += '<line class="ln" x1="%d" y1="%d" x2="%d" y2="%d"/>\n' % (x0, y0 - 16, x0, y0 + h + 16)
    for k in range(-16, h + 17, 12):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".4"/>' % (
            x0 - 12, y0 + k + 12, x0, y0 + k)
    o += "\n"

    # ag (ucta incelen konsol)
    cols, rows = 14, 5
    def prof(i):
        t = i / float(cols)
        return h * (1 - 0.42 * t)
    grid = []
    for i in range(cols + 1):
        hh = prof(i)
        col = [(x0 + i * (w / float(cols)), y0 + (h - hh) / 2.0 + j * hh / rows)
               for j in range(rows + 1)]
        grid.append(col)
    for i in range(cols):
        for j in range(rows):
            p1, p2, p3, p4 = grid[i][j], grid[i + 1][j], grid[i + 1][j + 1], grid[i][j + 1]
            # gerilme: mesnede ve dis liflere yakin yerlerde yuksek
            sx = 1 - i / float(cols)
            sy = abs(j + .5 - rows / 2.0) / (rows / 2.0)
            v = min(1.0, .25 + .5 * sx + .45 * sy * sx)
            col = "#f87171" if v > .72 else (a if v > .5 else "#38bdf8")
            o += ('<polygon points="%s" fill="%s" fill-opacity="%s" stroke="%s" '
                  'stroke-opacity=".35" stroke-width=".6"/>'
                  % (pts([p1, p2, p3, p4]), col, f(0.05 + 0.22 * v), col))
            o += '<line stroke="%s" stroke-opacity=".2" stroke-width=".5" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
                col, f(p1[0]), f(p1[1]), f(p3[0]), f(p3[1]))
        o += "\n"
    # dis kontur
    top = [grid[i][0] for i in range(cols + 1)]
    bot = [grid[i][rows] for i in range(cols, -1, -1)]
    o += '<polyline class="ln" points="%s"/>\n' % pts(top + bot + [top[0]])

    # yuk oklari
    for k in range(6):
        x = x0 + 90 + k * 62
        o += arrow(x, y0 - 52, x, y0 - 8, a, "cy", ".65")
    o += accent_text(x0 + 88, y0 - 62, "F = 2,4 kN", a, 9)

    # deforme sekil (kesikli)
    dp = []
    for i in range(cols + 1):
        t = i / float(cols)
        dp.append((grid[i][rows][0], grid[i][rows][1] + 34 * t * t))
    o += '<polyline class="ln2" points="%s" stroke-opacity=".45" stroke-dasharray="4 5"/>\n' % pts(dp)
    o += accent_text(dp[-1][0] - 74, dp[-1][1] + 18, "deforme", a, 9)

    # legend
    o += label(120, 378, "VON MISES", 9, "start", ".45")
    for i, (c, t) in enumerate([("#38bdf8", "dusuk"), (a, "orta"), ("#f87171", "kritik")]):
        o += ('<rect x="%d" y="370" width="46" height="7" rx="2" fill="%s" fill-opacity=".45"/>'
              % (200 + i * 58, c))
        o += label(200 + i * 58, 392, t, 8, "start", ".35")
    o += dim_line(x0, y0 + h + 40, x0 + w, y0 + h + 40)
    o += label(x0 + w / 2, y0 + h + 56, "L = 1 250 mm", 9, "middle", ".35")
    o += "\n" + scanline(a, 70)
    return o + TAIL


# --------------------------------------------------------------------------
def tolerans_analizi():
    """Tolerans zinciri + normal dagilim ve limitler."""
    a = "#c084fc"
    o = head(a)
    # montaj zinciri
    xs, y = 78, 96
    widths = [96, 74, 118, 88]
    x = xs
    for i, bw in enumerate(widths):
        o += box(x, y, bw, 62, "ln", 'fill="%s" fill-opacity=".05"' % a)
        o += label(x + bw / 2, y + 36, "P%d" % (i + 1), 11, "middle", ".55")
        # olcu zinciri
        o += dim_line(x, y + 78, x + bw, y + 78)
        o += dim_line(x, y + 72, x, y + 84) + dim_line(x + bw, y + 72, x + bw, y + 84)
        o += accent_text(x + bw / 2, y + 96, "%d±0,1" % bw, a, 8, "middle")
        x += bw + 6
    # toplam
    o += dim_line(xs, y - 22, x - 6, y - 22)
    o += dim_line(xs, y - 28, xs, y - 16) + dim_line(x - 6, y - 28, x - 6, y - 16)
    o += accent_text((xs + x) / 2 - 3, y - 32, "STACK-UP  Σ = 376 ± 0,4", a, 9, "middle")
    # bosluk isareti
    o += ('<g class="blink"><line class="cy" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".8"/>'
          '</g>' % (x - 6, y + 8, x + 22, y + 8))
    o += accent_text(x + 4, y + 2, "gap", a, 8)

    # normal dagilim
    bx, by, bw, bh = 96, 330, 400, 108
    o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d"/>\n' % (bx - 10, by, bx + bw + 10, by)
    curve = []
    for i in range(0, 101):
        t = (i / 100.0) * 6 - 3                     # -3..3 sigma
        v = math.exp(-t * t / 2.0)
        curve.append((bx + (i / 100.0) * bw, by - v * bh))
    o += '<path class="fl" d="M%s %s %s L%s %s Z" fill="%s" fill-opacity=".08"/>\n' % (
        f(bx), f(by), " ".join("L%s %s" % (f(px_), f(py_)) for px_, py_ in curve), f(bx + bw), f(by), a)
    o += '<polyline class="ln" points="%s"/>\n' % pts(curve)
    # sigma cizgileri
    for k in (-3, -2, -1, 0, 1, 2, 3):
        px_ = bx + bw * (k + 3) / 6.0
        v = math.exp(-k * k / 2.0)
        o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3" '
              'stroke-dasharray="3 4"/>' % (f(px_), f(by), f(px_), f(by - v * bh)))
        o += label(px_, by + 15, ("%+dσ" % k) if k else "μ", 8, "middle", ".38")
    # LSL / USL
    for px_, t in ((bx + bw * .06, "LSL"), (bx + bw * .94, "USL")):
        o += ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#f87171" stroke-opacity=".6" '
              'stroke-width="1.2"/>' % (f(px_), f(by + 6), f(px_), f(by - bh - 8)))
        o += ('<text x="%s" y="%s" font-family="Manrope,sans-serif" font-size="9" '
              'fill="#f87171" fill-opacity=".75" text-anchor="middle">%s</text>'
              % (f(px_), f(by - bh - 14), t))
    o += accent_text(bx + bw + 24, by - bh + 8, "Cpk 1,42", a, 11)
    o += label(bx + bw + 24, by - bh + 26, "DPMO  8,4", 9, "start", ".45")
    o += label(bx + bw + 24, by - bh + 42, "Yield  %99,2", 9, "start", ".45")
    o += "\n" + scanline(a, 50)
    return o + TAIL


# --------------------------------------------------------------------------
def tasarim_otomasyonu():
    """Kural paneli -> konfigurator -> turetilmis varyantlar."""
    a = "#fbbf24"
    o = head(a)
    # kural paneli
    o += box(48, 92, 196, 220, "ln", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(62, 114, "KURAL / PARAMETRE", a, 9)
    o += '<line class="ln2" x1="62" y1="124" x2="230" y2="124" stroke-opacity=".3"/>\n'
    params = [("uzunluk", "1 200"), ("govde_ad", "6"), ("delik_D", "M12"),
              ("malzeme", "S355"), ("kaplama", "RAL7016"), ("agirlik", "auto")]
    for i, (k, v) in enumerate(params):
        y = 146 + i * 26
        o += label(62, y, k, 9, "start", ".5")
        o += box(160, y - 11, 70, 16, "ln2", 'fill="%s" fill-opacity=".07"' % a)
        o += accent_text(195, y, v, a, 8, "middle")
    o += '<g class="blink">' + node(232, 146, 2.6) + '</g>\n'
    o += ('<text x="62" y="302" font-family="monospace" font-size="9" fill="%s" '
          'fill-opacity=".55">if len &gt; 900 then rib = 3</text>\n' % a)

    # islem carki
    o += gear(300, 200, 30, 12, "ln")
    o += gear(340, 238, 20, 10, "ln2")
    o += arrow(250, 200, 268, 200, a)
    o += arrow(372, 200, 396, 200, a)
    o += accent_text(300, 292, "iLogic", a, 10, "middle")

    # turetilmis varyantlar
    for i, sc in enumerate((0.66, 0.84, 1.0)):
        bx = 412 + i * 68
        bh = 118 * sc
        by = 232 - bh
        o += box(bx, by, 52, bh, "ln", 'fill="%s" fill-opacity=".05"' % a)
        for k in range(1, int(3 + i * 2)):
            yy = by + bh * k / float(2 + i * 2)
            o += '<line class="ln2" x1="%d" y1="%s" x2="%d" y2="%s" stroke-opacity=".35"/>' % (
                bx + 6, f(yy), bx + 46, f(yy))
        o += node(bx + 26, by - 8, 2.6)
        o += label(bx + 26, 250, "V%d" % (i + 1), 9, "middle", ".45")
    o += "\n"
    o += accent_text(412, 292, "OTOMATIK TURETILEN VARYANTLAR", a, 9)
    o += dim_line(412, 302, 600, 302)
    o += label(326, 366, "3 gun → 12 dakika", 10, "middle", ".4")
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def dijital_ikiz():
    """Bina modeli + sensor telemetrisi + operasyon paneli."""
    a = "#5eead4"
    o = head(a)
    ox, oy, s = 172, 214, .82
    px, py = 150, 106
    corners = [(0, 0), (px, 0), (px, py), (0, py)]
    floors = [0, 44, 88, 132, 176]
    o += '<g class="float">\n'
    for i, z in enumerate(floors):
        p = [iso(x, y, z, ox, oy, s) for x, y in corners]
        o += '<polygon class="fl" points="%s"/><polygon class="%s" points="%s"/>\n' % (
            pts(p), "ln" if i in (0, len(floors) - 1) else "ln2", pts(p))
    for x, y in corners:
        b, t = iso(x, y, 0, ox, oy, s), iso(x, y, floors[-1], ox, oy, s)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            f(b[0]), f(b[1]), f(t[0]), f(t[1]))
    o += "\n"
    # sensorler
    sensors = [(30, 24, 44), (118, 30, 88), (58, 86, 132), (128, 82, 44), (86, 52, 176)]
    for sx, sy, sz in sensors:
        q = iso(sx, sy, sz, ox, oy, s)
        o += ('<g class="blink"><circle cx="%s" cy="%s" r="9" fill="none" stroke="%s" '
              'stroke-opacity=".35" stroke-width="1"/></g>' % (f(q[0]), f(q[1]), a))
        o += node(q[0], q[1], 3)
    o += "\n</g>\n"

    # veri akisi
    for k, (sx, sy, sz) in enumerate(sensors[:3]):
        q = iso(sx, sy, sz, ox, oy, s)
        o += arrow(q[0] + 12, q[1], 350, 132 + k * 66, a, "cy", ".4")

    # operasyon paneli
    o += box(360, 72, 242, 300, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(376, 94, "OPERASYON PANELI", a, 9)
    o += '<line class="ln2" x1="376" y1="104" x2="586" y2="104" stroke-opacity=".3"/>\n'
    # cizgi grafik
    lp = [(378 + i * 12, 160 - 26 * abs(math.sin(i / 2.6)) - 4 * ((i * 7) % 5))
          for i in range(18)]
    o += '<polyline class="cy" points="%s" stroke-opacity=".7"/>\n' % pts(lp)
    o += label(376, 182, "Enerji tuketimi ↓ %25", 9, "start", ".5")
    # cubuk grafik
    for i in range(11):
        hh = 12 + ((i * 13) % 34)
        o += ('<rect x="%d" y="%d" width="10" height="%d" rx="2" fill="%s" fill-opacity=".%d"/>'
              % (378 + i * 19, 244 - hh, hh, a, 3 + (i % 4)))
    o += '\n' + label(376, 264, "Varlik kullanim orani", 9, "start", ".5")
    o += '<line class="ln2" x1="376" y1="278" x2="586" y2="278" stroke-opacity=".22"/>\n'
    # telemetri satirlari
    for i, (t, v) in enumerate((("HVAC-03", "22,4 °C"), ("Pompa-11", "4,1 bar"),
                                ("Sayac-A", "318 kWh"))):
        y = 300 + i * 18
        o += node(378, y - 3, 2.4)
        o += label(392, y, t, 9, "start", ".45")
        o += accent_text(586, y, v, a, 9, "end")
    o += "\n" + accent_text(376, 360, "%92", a, 15)
    o += label(412, 360, "varlik calisir durumda", 9, "start", ".45")
    o += "\n" + scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def fabrika_tasarimi():
    """Izometrik fabrika yerlesimi + malzeme akisi."""
    a = "#38bdf8"
    o = head(a)
    ox, oy, s = 320, 92, 1.22
    W_, D_ = 230, 170
    # zemin izgarasi
    for i in range(0, W_ + 1, 23):
        p1, p2 = iso(i, 0, 0, ox, oy, s), iso(i, D_, 0, ox, oy, s)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".16"/>' % (
            f(p1[0]), f(p1[1]), f(p2[0]), f(p2[1]))
    for j in range(0, D_ + 1, 17):
        p1, p2 = iso(0, j, 0, ox, oy, s), iso(W_, j, 0, ox, oy, s)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".16"/>' % (
            f(p1[0]), f(p1[1]), f(p2[0]), f(p2[1]))
    o += "\n"
    outline = [iso(x, y, 0, ox, oy, s) for x, y in
               ((0, 0), (W_, 0), (W_, D_), (0, D_))]
    o += '<polygon class="ln" points="%s"/>\n' % pts(outline)

    def machine(x, y, w, d, h, cls="ln"):
        b = [iso(x, y, 0, ox, oy, s), iso(x + w, y, 0, ox, oy, s),
             iso(x + w, y + d, 0, ox, oy, s), iso(x, y + d, 0, ox, oy, s)]
        t = [iso(px_, py_, h, ox, oy, s) for px_, py_ in
             ((x, y), (x + w, y), (x + w, y + d), (x, y + d))]
        r = '<polygon class="fl" points="%s"/><polygon class="%s" points="%s"/>' % (
            pts(t), cls, pts(t))
        for i in (0, 1, 2, 3):
            r += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
                f(b[i][0]), f(b[i][1]), f(t[i][0]), f(t[i][1]))
        r += '<polyline class="ln2" points="%s"/>' % pts([b[1], b[2], b[3]])
        return r + "\n"

    cells = [(18, 16, 46, 34, 26), (94, 14, 40, 30, 22), (162, 20, 44, 36, 30),
             (22, 74, 40, 30, 18), (96, 76, 52, 34, 24), (170, 82, 38, 28, 20),
             (30, 128, 44, 30, 16), (120, 126, 62, 32, 14)]
    for c in cells:
        o += machine(*c)
    # konveyor / AGV rotasi
    route = [(8, 60), (78, 60), (78, 112), (152, 112), (152, 62), (218, 62)]
    rp = [iso(x, y, 3, ox, oy, s) for x, y in route]
    o += '<polyline class="cy draw" points="%s" stroke-opacity=".7" stroke-width="1.6"/>\n' % pts(rp)
    for x, y in route:
        q = iso(x, y, 3, ox, oy, s)
        o += node(q[0], q[1], 2.6)
    # hareketli tasiyici
    q0 = iso(8, 60, 8, ox, oy, s)
    o += ('<g class="slide" style="--d:210px"><circle cx="%s" cy="%s" r="5" fill="%s" '
          'fill-opacity=".9"/></g>\n' % (f(q0[0]), f(q0[1]), a))
    # olcu
    p1, p2 = iso(0, D_, 0, ox, oy, s), iso(W_, D_, 0, ox, oy, s)
    o += dim_line(p1[0] - 14, p1[1] + 26, p2[0] - 14, p2[1] + 26)
    o += label((p1[0] + p2[0]) / 2 - 22, (p1[1] + p2[1]) / 2 + 42, "60 m", 9, "middle", ".4")
    o += accent_text(34, 52, "MALZEME AKISI", a, 9)
    o += label(34, 70, "cakisma kontrolu · kurulum takvimi", 9, "start", ".38")
    o += scanline(a, 46)
    return o + TAIL


# --------------------------------------------------------------------------
def cam():
    """Is parcasi + takim yolu + G-kodu seridi."""
    a = "#f87171"
    o = head(a)
    ox, oy, s = 250, 210, 1.0
    W_, D_, H_ = 150, 110, 40
    top = [iso(x, y, H_, ox, oy, s) for x, y in ((0, 0), (W_, 0), (W_, D_), (0, D_))]
    bot = [iso(x, y, 0, ox, oy, s) for x, y in ((0, 0), (W_, 0), (W_, D_), (0, D_))]
    o += '<polygon class="fl" points="%s"/><polygon class="ln" points="%s"/>\n' % (
        pts(top), pts(top))
    for i in (1, 2, 3):
        o += '<line class="ln" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            f(top[i][0]), f(top[i][1]), f(bot[i][0]), f(bot[i][1]))
    o += '<polyline class="ln" points="%s"/>\n' % pts([bot[1], bot[2], bot[3]])
    # cep (pocket)
    pk = [iso(x, y, H_, ox, oy, s) for x, y in ((34, 26), (116, 26), (116, 84), (34, 84))]
    o += '<polygon class="ln2" points="%s" stroke-opacity=".5"/>\n' % pts(pk)
    # zigzag takim yolu
    path = []
    y = 32
    left = True
    while y <= 78:
        if left:
            path += [(40, y), (110, y)]
        else:
            path += [(110, y), (40, y)]
        y += 7.5
        left = not left
    tp = [iso(x, yy, H_ + 1, ox, oy, s) for x, yy in path]
    o += '<polyline class="cy draw" points="%s" stroke-opacity=".75"/>\n' % pts(tp)
    # kontur pasosu
    cp = [iso(x, y, H_ + 1, ox, oy, s) for x, y in
          ((30, 22), (120, 22), (120, 88), (30, 88), (30, 22))]
    o += '<polyline class="cy" points="%s" stroke-opacity=".45" stroke-dasharray="4 4"/>\n' % pts(cp)

    # takim
    tip = iso(76, 54, H_ + 2, ox, oy, s)
    o += ('<g class="float"><polygon class="ln" points="%s"/>'
          '<rect class="ln" x="%s" y="%s" width="20" height="46" rx="2"/>'
          '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/></g>\n'
          % (pts([(tip[0] - 7, tip[1] - 30), (tip[0] + 7, tip[1] - 30), (tip[0], tip[1])]),
             f(tip[0] - 10), f(tip[1] - 76), f(tip[0]), f(tip[1] - 76), f(tip[0]), f(tip[1] - 108)))
    o += accent_text(tip[0] + 20, tip[1] - 62, "Ø10 R2", a, 9)

    # eksen gostergesi
    o += ('<g><line class="ln2" x1="72" y1="356" x2="112" y2="336"/>'
          '<line class="ln2" x1="72" y1="356" x2="32" y2="336"/>'
          '<line class="ln2" x1="72" y1="356" x2="72" y2="312"/></g>')
    o += (accent_text(116, 334, "X", a, 9) + accent_text(22, 334, "Y", a, 9)
          + accent_text(68, 306, "Z", a, 9))

    # G-kodu seridi
    o += box(432, 92, 170, 226, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(446, 112, "NC ÇIKTISI", a, 9)
    code = ["G90 G54 G17", "T04 M06", "S9500 M03", "G43 H04 Z25.", "X-32. Y-18.",
            "G01 Z-4.5 F420", "X32. F1150", "Y-10.5", "X-32.", "G00 Z25.", "M09", "M30"]
    for i, ln in enumerate(code):
        o += ('<text x="446" y="%d" font-family="monospace" font-size="9" fill="#fff" '
              'fill-opacity="%s">%s</text>' % (134 + i * 15, ".5" if i % 2 else ".38", ln))
    o += "\n" + ('<rect x="440" y="%d" width="154" height="13" rx="2" fill="%s" '
                 'fill-opacity=".1" class="blink"/>\n' % (124 + 5 * 15, a))
    o += label(432, 340, "3+2 / 5 eksen", 9, "start", ".38")
    o += label(432, 356, "sanal tezgah dogrulamasi", 9, "start", ".38")
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def eklemeli_imalat():
    """3B yazici gantry + katman katman olusan parca + dilimleme onizlemesi."""
    a = "#10b981"
    o = head(a)
    # yazici govdesi
    o += box(66, 78, 300, 268, "ln", 'fill="rgba(255,255,255,.015)"')
    o += '<line class="ln2" x1="66" y1="300" x2="366" y2="300"/>\n'   # tabla
    o += '<line class="ln" x1="86" y1="300" x2="346" y2="300"/>\n'
    # gantry
    o += '<line class="ln" x1="66" y1="128" x2="366" y2="128"/>\n'
    o += ('<g class="slide" style="--d:150px"><rect class="ln" x="150" y="118" width="34" '
          'height="20" rx="3"/><polygon class="ln" points="%s"/></g>\n'
          % pts([(158, 138), (176, 138), (167, 152)]))
    # basilan parca (katmanlar)
    layers_n = 16
    for i in range(layers_n):
        y = 300 - (i + 1) * 8
        t = i / float(layers_n)
        w = 104 - 52 * t - 8 * math.sin(t * 6.2)
        o += ('<rect x="%s" y="%s" width="%s" height="6.4" rx="1.6" fill="%s" '
              'fill-opacity="%s" stroke="%s" stroke-opacity=".45" stroke-width=".6"/>'
              % (f(216 - w / 2), f(y), f(w), a, f(.07 + .12 * (1 - t)), a))
    o += "\n"
    o += accent_text(216, 158, "16 / 240 katman", a, 9, "middle")
    # destek yapilari
    for x in (176, 256):
        o += ('<line class="ln2" x1="%d" y1="300" x2="%d" y2="248" stroke-opacity=".3" '
              'stroke-dasharray="2 3"/>' % (x, x))
    o += "\n"
    o += dim_line(56, 128, 56, 300) + dim_line(50, 128, 62, 128) + dim_line(50, 300, 62, 300)
    o += label(46, 220, "Z", 9, "end", ".4")

    # dilim onizlemesi
    o += box(414, 92, 186, 226, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(430, 112, "DILIMLEME", a, 9)
    for i in range(5):
        cx, cy = 506, 158 + i * 38
        rr = 42 - i * 5
        o += ('<ellipse class="ln2" cx="%d" cy="%d" rx="%d" ry="%d" stroke-opacity=".4"/>'
              % (cx, cy, rr, rr * .3))
        # dolgu hatlari
        for k in range(-2, 3):
            o += ('<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3" '
                  'stroke-width=".8"/>'
                  % (f(cx - rr * .8), f(cy + k * 3.4), f(cx + rr * .8), f(cy + k * 3.4)))
        o += "\n"
    o += label(430, 336, "0,15 mm katman · %20 dolgu", 9, "start", ".4")
    o += accent_text(430, 356, "PLA · PETG · ABS · CF-PA", a, 9)
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def nesting():
    """Sac uzerinde gercek-sekil yuvalama + verim gostergesi."""
    a = "#34d399"
    o = head(a)
    sx, sy, sw, sh = 56, 92, 384, 248
    o += box(sx, sy, sw, sh, "ln", 'fill="rgba(255,255,255,.015)"')
    o += accent_text(sx, sy - 12, "2000 × 1000 · S235 · t=4", a, 9)

    parts = [
        [(14, 14), (110, 14), (124, 62), (72, 96), (14, 70)],
        [(132, 12), (214, 12), (214, 88), (168, 88), (132, 52)],
        [(226, 16), (300, 16), (312, 74), (226, 74)],
        [(320, 14), (372, 14), (372, 104), (320, 104)],
        [(16, 108), (96, 108), (96, 168), (54, 190), (16, 158)],
        [(108, 100), (196, 100), (208, 156), (150, 186), (108, 150)],
        [(228, 90), (306, 108), (310, 172), (240, 178)],
        [(318, 118), (372, 118), (372, 196), (318, 196)],
        [(18, 200), (104, 200), (104, 236), (60, 236), (18, 224)],
        [(120, 198), (206, 210), (198, 236), (120, 236)],
        [(222, 192), (300, 192), (300, 236), (240, 236)],
        [(314, 208), (372, 208), (372, 236), (314, 236)],
    ]
    for i, p in enumerate(parts):
        q = [(sx + x, sy + y) for x, y in p]
        o += ('<polygon points="%s" fill="%s" fill-opacity=".08" stroke="%s" '
              'stroke-opacity=".7" stroke-width="1.1" stroke-linejoin="round"/>' % (pts(q), a, a))
        cx = sum(x for x, _ in q) / len(q)
        cy = sum(y for _, y in q) / len(q)
        o += label(cx, cy + 3, "%02d" % (i + 1), 8, "middle", ".4")
    o += "\n"
    # kesim sirasi
    order = [(sx + 60, sy + 48), (sx + 172, sy + 48), (sx + 264, sy + 44),
             (sx + 346, sy + 58), (sx + 56, sy + 148), (sx + 156, sy + 142),
             (sx + 264, sy + 138), (sx + 344, sy + 156)]
    o += '<polyline class="cy draw" points="%s" stroke-opacity=".35" stroke-dasharray="3 5"/>\n' % pts(order)

    # verim gostergesi
    o += box(468, 120, 136, 136, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(482, 142, "MALZEME VERIMI", a, 9)
    o += ('<circle cx="536" cy="196" r="38" fill="none" stroke="%s" stroke-opacity=".16" '
          'stroke-width="8"/>' % a)
    o += ('<circle cx="536" cy="196" r="38" fill="none" stroke="%s" stroke-opacity=".8" '
          'stroke-width="8" stroke-linecap="round" stroke-dasharray="%s %s" '
          'transform="rotate(-90 536 196)"/>' % (a, f(2 * math.pi * 38 * .87), f(2 * math.pi * 38)))
    o += accent_text(536, 202, "%87", a, 16, "middle")
    o += label(468, 282, "Fire  %13  →  ₺/parca ↓", 9, "start", ".45")
    o += label(468, 300, "12 parça · 1 tabaka · tek kurulum", 9, "start", ".4")
    o += accent_text(468, 322, "DXF → CAM → CNC", a, 9)
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def plm():
    """Yasam dongusu halkasi + BOM agaci + degisim karti."""
    a = "#38bdf8"
    o = head(a)
    cx, cy, r = 196, 200, 100
    o += ('<circle class="ln2" cx="%d" cy="%d" r="%d" stroke-opacity=".3" '
          'stroke-dasharray="5 6"/>\n' % (cx, cy, r))
    phases = ["Fikir", "Tasarim", "Dogrulama", "Uretim", "Servis", "Emeklilik"]
    for i, name in enumerate(phases):
        ang = -math.pi / 2 + i * 2 * math.pi / len(phases)
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        o += ('<circle cx="%s" cy="%s" r="15" fill="%s" fill-opacity=".1" stroke="%s" '
              'stroke-opacity=".6" stroke-width="1.1"/>' % (f(x), f(y), a, a))
        o += accent_text(x, y + 4, "%02d" % (i + 1), a, 9, "middle")
        lx = cx + (r + 30) * math.cos(ang)
        ly = cy + (r + 30) * math.sin(ang)
        anc = "middle" if abs(math.cos(ang)) < .3 else ("start" if math.cos(ang) > 0 else "end")
        o += label(lx, ly + 3, name, 9, anc, ".5")
    o += "\n"
    # donen gosterge
    o += ('<g class="spin"><path class="cy" d="M%d %d a%d %d 0 0 1 %d %d" '
          'stroke-opacity=".8" stroke-width="1.8"/></g>\n'
          % (cx, cy - r, r, r, r * .86, r * .5))
    # merkezde BOM agaci
    o += box(cx - 54, cy - 44, 108, 88, "ln", 'fill="rgba(6,12,26,.88)"')
    o += accent_text(cx - 42, cy - 25, "BOM", a, 9)
    rows = [(0, "Urun A"), (1, "Govde"), (2, "Mil"), (2, "Rulman"), (1, "Kapak")]
    for i, (lvl, t) in enumerate(rows):
        y = cy - 9 + i * 13
        o += ('<line class="ln2" x1="%d" y1="%s" x2="%d" y2="%s" stroke-opacity=".3"/>'
              % (cx - 42 + lvl * 9, f(y - 3), cx - 36 + lvl * 9, f(y - 3)))
        o += label(cx - 32 + lvl * 9, y, t, 8, "start", ".45")
    o += "\n"
    # degisim karti
    o += box(392, 108, 210, 96, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(408, 130, "ECO-2416", a, 10)
    o += label(408, 150, "Mil malzemesi 42CrMo4", 9, "start", ".5")
    for i, (t, st) in enumerate((("Muhendislik", "onayli"), ("Kalite", "onayli"),
                                 ("Satinalma", "bekliyor"))):
        y = 170 + i * 15
        col = a if st == "onayli" else "#fbbf24"
        o += ('<circle cx="414" cy="%s" r="3.4" fill="%s" fill-opacity=".85"/>'
              % (f(y - 3), col))
        o += label(426, y, t, 8, "start", ".45")
        o += ('<text x="586" y="%s" font-family="Manrope,sans-serif" font-size="8" '
              'fill="%s" fill-opacity=".7" text-anchor="end">%s</text>' % (f(y), col, st))
    o += "\n"
    # ERP entegrasyonu
    o += box(392, 226, 210, 76, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(408, 248, "ENTEGRASYON", a, 9)
    for i, t in enumerate(("ERP", "CRM", "CAD")):
        o += box(408 + i * 62, 262, 52, 24, "ln2", 'fill="%s" fill-opacity=".07"' % a)
        o += label(434 + i * 62, 278, t, 9, "middle", ".5")
    o += "\n" + arrow(360, 264, 386, 264, a)
    o += scanline(a, 56)
    return o + TAIL


# --------------------------------------------------------------------------
def pdm():
    """Revizyon agaci + check-in/out + kasa."""
    a = "#34d399"
    o = head(a)
    # revizyon grafigi
    base_y = 150
    xs = [68 + i * 52 for i in range(7)]
    o += '<polyline class="cy" points="%s" stroke-opacity=".7"/>\n' % pts(
        [(x, base_y) for x in xs])
    revs = ["A", "B", "C", "D", "E", "F", "G"]
    for i, x in enumerate(xs):
        o += node(x, base_y, 5 if i == len(xs) - 1 else 3.6, "nd" if i == len(xs) - 1 else "nd blink")
        o += label(x, base_y + 20, "Rev %s" % revs[i], 8, "middle", ".42")
    # dal
    br = [(xs[3], base_y), (xs[4], base_y - 44), (xs[5], base_y - 44), (xs[6], base_y)]
    o += '<polyline class="ln2" points="%s" stroke-opacity=".45"/>\n' % pts(br)
    for x, y in br[1:3]:
        o += node(x, y, 3)
    o += accent_text(xs[4], base_y - 54, "varyant dali", a, 8)

    # dosya kartlari
    files = [("GOVDE-001.ipt", "kilitli", "#fbbf24"),
             ("MIL-014.ipt", "serbest", a),
             ("MONTAJ-A.iam", "kilitli", "#fbbf24"),
             ("TEKNIK-RES.idw", "serbest", a)]
    for i, (name, st, col) in enumerate(files):
        x = 66 + (i % 2) * 214
        y = 226 + (i // 2) * 62
        o += box(x, y, 196, 48, "ln2", 'fill="rgba(255,255,255,.02)"')
        o += ('<rect x="%d" y="%d" width="26" height="26" rx="5" fill="%s" fill-opacity=".12"/>'
              % (x + 12, y + 11, col))
        o += ('<path d="M%d %d v-5 a5 5 0 0 1 10 0 v5" fill="none" stroke="%s" '
              'stroke-opacity=".8" stroke-width="1.2"/>'
              '<rect x="%d" y="%d" width="14" height="10" rx="2" fill="none" stroke="%s" '
              'stroke-opacity=".8" stroke-width="1.2"/>'
              % (x + 20, y + 23, col, x + 18, y + 23, col))
        o += label(x + 48, y + 22, name, 9, "start", ".55")
        o += ('<text x="%d" y="%d" font-family="Manrope,sans-serif" font-size="8" fill="%s" '
              'fill-opacity=".7">%s</text>' % (x + 48, y + 38, col, st))
    o += "\n"
    # kasa
    o += arrow(452, 150, 494, 150, a, "cy", ".5")
    o += ('<circle class="ln" cx="546" cy="150" r="48"/>'
          '<circle class="ln2" cx="546" cy="150" r="37" stroke-opacity=".4"/>'
          '<g class="spin"><line class="cy" x1="546" y1="122" x2="546" y2="178" '
          'stroke-opacity=".55"/><line class="cy" x1="518" y1="150" x2="574" y2="150" '
          'stroke-opacity=".55"/></g>' + node(546, 150, 4) + "\n")
    o += accent_text(546, 218, "TEK KAYNAK", a, 9, "middle")
    o += label(546, 234, "surum · revizyon · yetki", 8, "middle", ".38")
    o += accent_text(66, 372, "CHECK-IN / CHECK-OUT · TAM IZLENEBILIRLIK", a, 9)
    o += dim_line(66, 382, 460, 382)
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def insaat_yonetimi():
    """Santiye + is programi + CDE dokuman akisi."""
    a = "#22c55e"
    o = head(a)
    # zemin
    o += '<line class="ln" x1="30" y1="352" x2="610" y2="352"/>\n'
    # insa halindeki bina
    bx, by, bw = 70, 196, 168
    o += box(bx, by, bw, 156, "ln", 'fill="rgba(255,255,255,.015)"')
    for k in range(1, 5):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (
            bx, by + k * 31, bx + bw, by + k * 31)
    for k in range(1, 4):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".3"/>' % (
            bx + k * 42, by, bx + k * 42, by + 156)
    o += "\n"
    # tamamlanan katlar dolgu
    for k in range(2, 5):
        o += ('<rect x="%d" y="%d" width="%d" height="30" fill="%s" fill-opacity=".07"/>'
              % (bx + 1, by + k * 31 + 1, bw - 2, a))
    o += "\n"
    # kule vinc
    o += ('<g class="ln"><path d="M266 352 V148 M284 352 V148 M266 148 H284"/>'
          '<path d="M196 148 H356 M196 148 L275 132 M356 148 L275 132"/>'
          '<path d="M330 148 V186" stroke-dasharray="4 4"/>'
          '<rect x="318" y="186" width="24" height="15" fill="none"/></g>\n')
    for k in range(150, 352, 24):
        o += '<line class="ln2" x1="266" y1="%d" x2="284" y2="%d" stroke-opacity=".25"/>' % (
            k, k + 24)
    o += "\n"
    # is programi (Gantt)
    o += box(376, 196, 226, 156, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(392, 216, "IS PROGRAMI", a, 9)
    tasks = [(0, 74, "Kazi", 1.0), (22, 66, "Temel", 1.0), (58, 82, "Kaba yapi", .62),
             (104, 62, "Cephe", .0), (128, 58, "MEP", .0), (150, 40, "Ince", .0)]
    for i, (off, wdt, t, done) in enumerate(tasks):
        y = 240 + i * 18
        o += label(392, y + 4, t, 8, "start", ".45")
        o += ('<rect x="%d" y="%d" width="%d" height="8" rx="3" fill="%s" fill-opacity=".14"/>'
              % (456 + off * .74, y - 2, int(wdt * .74), a))
        if done:
            o += ('<rect x="%d" y="%d" width="%d" height="8" rx="3" fill="%s" fill-opacity=".7"/>'
                  % (456 + off * .74, y - 2, int(wdt * .74 * done), a))
    o += '\n<line class="cy" x1="516" y1="232" x2="516" y2="346" stroke-opacity=".6" stroke-dasharray="3 3"/>'
    o += accent_text(516, 228, "bugun", a, 8, "middle")

    # CDE bulutu + dokuman akisi
    o += ('<path class="ln" d="M406 86 a30 30 0 0 1 58 -12 a24 24 0 0 1 44 10 '
          'a22 22 0 0 1 -6 43 H426 a24 24 0 0 1 -20 -41 Z" fill="rgba(255,255,255,.02)"/>\n')
    o += accent_text(462, 80, "CDE", a, 12, "middle")
    o += label(462, 98, "ISO 19650", 8, "middle", ".42")
    o += arrow(248, 190, 398, 124, a, "cy", ".4")
    o += arrow(462, 130, 462, 188, a, "cy", ".4")
    o += label(70, 182, "Model · çizim · saha raporu", 9, "start", ".42")
    o += accent_text(478, 164, "tek dogru kaynak", a, 8)
    # konu isaretleri
    for x, y in ((116, 246), (192, 302), (330, 208)):
        o += ('<g class="blink"><path d="M%d %d a7 7 0 1 0 -0.1 0 Z" fill="none" stroke="%s" '
              'stroke-opacity=".8" stroke-width="1.2"/><circle cx="%d" cy="%d" r="2.4" '
              'fill="%s" fill-opacity=".9"/></g>' % (x, y, "#fbbf24", x, y - 4, "#fbbf24"))
    o += "\n" + scanline(a, 44)
    return o + TAIL


# --------------------------------------------------------------------------
def gorsellestirme():
    """Ic mekan sahnesi + kamera + isik konisi + render bucket'lari."""
    a = "#f59e0b"
    o = head(a)
    # perspektif oda
    vp = (350, 200)
    fr = [(210, 108), (520, 108), (520, 320), (210, 320)]
    bk = [(300, 168), (452, 168), (452, 274), (300, 274)]
    o += '<polygon class="fl" points="%s"/><polygon class="ln" points="%s"/>\n' % (
        pts(bk), pts(bk))
    o += '<polygon class="ln" points="%s"/>\n' % pts(fr)
    for i in range(4):
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".45"/>' % (
            f(fr[i][0]), f(fr[i][1]), f(bk[i][0]), f(bk[i][1]))
    o += "\n"
    # zemin izgarasi (perspektif)
    for k in range(1, 6):
        t = k / 6.0
        y1 = 320 + (274 - 320) * t
        x1 = 210 + (300 - 210) * t
        x2 = 520 + (452 - 520) * t
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".18"/>' % (
            f(x1), f(y1), f(x2), f(y1))
    for k in range(1, 6):
        xf = 210 + (520 - 210) * k / 6.0
        xb = 300 + (452 - 300) * k / 6.0
        o += '<line class="ln2" x1="%s" y1="320" x2="%s" y2="274" stroke-opacity=".18"/>' % (
            f(xf), f(xb))
    o += "\n"
    # mobilya kutlesi
    o += box(330, 236, 78, 32, "ln2", 'fill="%s" fill-opacity=".05"' % a)
    o += box(348, 208, 42, 28, "ln2", 'fill="%s" fill-opacity=".04"' % a)

    # isik kaynagi + koni
    o += ('<circle cx="470" cy="86" r="9" fill="%s" fill-opacity=".8"/>'
          '<g class="comb"><polygon points="%s" fill="%s" fill-opacity=".07"/></g>\n'
          % (a, pts([(470, 92), (346, 300), (500, 300)]), a))
    for k in range(6):
        o += ('<line class="cy" x1="470" y1="94" x2="%d" y2="300" stroke-opacity=".18"/>'
              % (352 + k * 30))
    o += "\n" + accent_text(470, 72, "IES / HDRI", a, 9, "middle")

    # kamera
    o += ('<g class="ln"><rect x="64" y="228" width="46" height="30" rx="4"/>'
          '<polygon points="%s"/><line x1="87" y1="258" x2="87" y2="292"/>'
          '<line x1="70" y1="292" x2="104" y2="292"/></g>\n'
          % pts([(110, 234), (132, 224), (132, 262), (110, 252)]))
    o += ('<line class="ln2" x1="132" y1="243" x2="210" y2="214" stroke-opacity=".3" '
          'stroke-dasharray="4 4"/><line class="ln2" x1="132" y1="243" x2="210" y2="320" '
          'stroke-opacity=".3" stroke-dasharray="4 4"/>\n')
    o += accent_text(64, 314, "35 mm · f/2.8", a, 9)

    # render bucket'lari
    for i, (bxp, byp) in enumerate(((228, 122), (262, 122), (296, 122), (228, 156), (262, 156))):
        o += ('<rect x="%d" y="%d" width="30" height="30" fill="none" stroke="%s" '
              'stroke-opacity=".55" stroke-width="1" class="blink"/>' % (bxp, byp, CYAN))
    o += "\n" + accent_text(228, 112, "RENDER 04 / 32", CYAN, 9)

    # frame buffer seridi
    o += box(66, 336, 468, 44, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += label(80, 362, "Frame Buffer", 9, "start", ".45")
    for i in range(28):
        hh = 6 + ((i * 11) % 24)
        o += ('<rect x="%d" y="%d" width="6" height="%d" rx="1" fill="%s" fill-opacity=".%d"/>'
              % (186 + i * 9, 372 - hh, hh, a, 3 + (i % 5)))
    o += "\n" + accent_text(452, 362, "ACEScg", a, 9)
    o += scanline(a, 56)
    return o + TAIL


# --------------------------------------------------------------------------
def yaratici_icerik():
    """Artboard + katman yigini + bezier + renk paleti + video zaman cizelgesi."""
    a = "#e25922"
    o = head(a)
    # katman yigini
    for i in range(4):
        x, y = 92 + i * 16, 108 + i * 16
        cls = "ln" if i == 3 else "ln2"
        o += box(x, y, 208, 148, cls, 'fill="rgba(6,12,26,.6)"')
    o += "\n"
    # ust artboard icerigi
    ax, ay = 140, 156
    o += ('<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".25"/>'
          % (ax + 14, ay + 96, ax + 194, ay + 96))
    # bezier egrisi + tutamaklar
    o += ('<path class="cy" d="M%d %d C%d %d %d %d %d %d" stroke-opacity=".85" '
          'stroke-width="1.6" fill="none"/>\n'
          % (ax + 16, ay + 84, ax + 60, ay + 6, ax + 128, ay + 132, ax + 190, ay + 34))
    for hx, hy, px_, py_ in ((ax + 16, ay + 84, ax + 60, ay + 6),
                             (ax + 190, ay + 34, ax + 128, ay + 132)):
        o += ('<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".4"/>'
              '<rect x="%d" y="%d" width="6" height="6" fill="%s" fill-opacity=".85"/>'
              % (hx, hy, px_, py_, px_ - 3, py_ - 3, a))
        o += ('<circle cx="%d" cy="%d" r="3.6" fill="none" stroke="%s" stroke-opacity=".9" '
              'stroke-width="1.2"/>' % (hx, hy, a))
    o += "\n"
    o += accent_text(96, 100, "ARTBOARD  1920 × 1080", a, 9)
    # katman etiketleri
    o += accent_text(382, 112, "KATMANLAR", a, 9)
    for i, t in enumerate(("Metin", "Vektor", "Foto", "Zemin")):
        o += label(382, 136 + i * 18, t, 9, "start", ".45")
        o += ('<rect x="366" y="%d" width="8" height="8" rx="2" fill="%s" fill-opacity=".%d"/>'
              % (129 + i * 18, a, 8 - i * 2))
    o += "\n"
    # renk paleti
    o += accent_text(382, 228, "MARKA PALETI", a, 9)
    for i, c in enumerate(("#e25922", "#00c8f0", "#0d1830", "#f59e0b", "#ffffff")):
        o += ('<rect x="%d" y="238" width="26" height="26" rx="5" fill="%s" fill-opacity=".85" '
              'stroke="rgba(255,255,255,.2)" stroke-width=".6"/>' % (382 + i * 31, c))
    o += "\n"
    # tipografi
    o += ('<text x="382" y="300" font-family="Manrope,sans-serif" font-size="22" '
          'font-weight="800" fill="#fff" fill-opacity=".7">Aa</text>')
    o += label(426, 300, "Manrope · 800 / 400", 9, "start", ".42")

    # video zaman cizelgesi
    o += box(66, 322, 508, 62, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += label(80, 366, "TIMELINE", 8, "start", ".4")
    tracks = [(150, 120, ".55"), (280, 96, ".4"), (390, 150, ".3")]
    for i, (tx, tw, op) in enumerate(tracks):
        o += ('<rect x="%d" y="%d" width="%d" height="12" rx="3" fill="%s" fill-opacity="%s"/>'
              % (tx, 332 + i * 15, tw, a, op))
    for i in range(3):
        for k in range(4):
            o += ('<polygon points="%s" fill="%s" fill-opacity=".8"/>'
                  % (pts([(180 + k * 78, 338 + i * 15), (184 + k * 78, 342 + i * 15),
                          (180 + k * 78, 346 + i * 15), (176 + k * 78, 342 + i * 15)]), CYAN))
    o += "\n"
    o += ('<g class="slide" style="--d:390px"><line x1="140" y1="326" x2="140" y2="380" '
          'stroke="%s" stroke-opacity=".8" stroke-width="1.4"/></g>\n' % CYAN)
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def gerceklik_yakalama():
    """Tripod tarayici + radyal tarama + nokta bulutu bina konturu."""
    a = "#fbbf24"
    o = head(a)
    sx, sy = 150, 268
    # tripod + tarayici
    o += ('<g class="ln"><line x1="%d" y1="%d" x2="%d" y2="352"/>'
          '<line x1="%d" y1="%d" x2="%d" y2="352"/>'
          '<line x1="%d" y1="%d" x2="%d" y2="352"/>'
          '<rect x="%d" y="%d" width="30" height="34" rx="5"/>'
          '<circle cx="%d" cy="%d" r="8"/></g>\n'
          % (sx, sy, sx - 30, sx, sy, sx + 30, sx, sy, sx + 4,
             sx - 15, sy - 34, sx, sy - 17))
    o += node(sx, sy - 17, 3)
    # radyal tarama isinlari
    for k in range(16):
        ang = -math.pi * .70 + k * (math.pi * .76 / 15)
        r = 210
        x2 = sx + r * math.cos(ang)
        y2 = (sy - 17) + r * math.sin(ang) * .74
        o += ('<line class="cy draw" x1="%d" y1="%d" x2="%s" y2="%s" stroke-opacity=".22"/>'
              % (sx, sy - 17, f(x2), f(y2)))
    o += "\n"
    o += ('<g class="comb"><path class="cy" d="M%d %d a56 42 0 0 1 112 0" '
          'stroke-opacity=".5"/></g>\n' % (sx - 56, sy - 17))

    # nokta bulutu bina konturu
    outline = [(300, 300), (300, 150), (352, 118), (404, 150), (404, 300)]
    inner = [(322, 300), (322, 196), (382, 196), (382, 300)]
    def cloudify(poly, closed=False, dens=9):
        r = ""
        seq = poly + ([poly[0]] if closed else [])
        for i in range(len(seq) - 1):
            x1, y1 = seq[i]
            x2, y2 = seq[i + 1]
            n = max(2, int(math.hypot(x2 - x1, y2 - y1) / dens))
            for k in range(n + 1):
                t = k / float(n)
                jx = ((i * 37 + k * 53) % 7 - 3) * .5
                jy = ((i * 29 + k * 41) % 7 - 3) * .5
                r += node(x1 + (x2 - x1) * t + jx, y1 + (y2 - y1) * t + jy, 1.5,
                          "nd" if k % 3 else "nd blink")
        return r + "\n"
    o += cloudify(outline)
    o += cloudify(inner)
    # zemin noktalari
    for i in range(60):
        x = 250 + (i * 47) % 300
        y = 300 + ((i * 31) % 40)
        o += node(x, y, 1.2, "nd")
    o += "\n"
    o += ('<polyline class="ln2" points="%s" stroke-opacity=".3" stroke-dasharray="3 4"/>\n'
          % pts(outline))

    # panel
    o += box(452, 96, 152, 172, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(466, 116, "SCAN → BIM", a, 9)
    steps = [("Tarama", "18 durus"), ("Kayit", "3,2 mm"), ("Nokta", "412 M"),
             ("Mesh", "hazir"), ("Revit", "aktarildi")]
    for i, (t, v) in enumerate(steps):
        y = 142 + i * 24
        o += ('<circle cx="470" cy="%d" r="4" fill="%s" fill-opacity=".8"/>' % (y - 4, a))
        if i < len(steps) - 1:
            o += ('<line class="ln2" x1="470" y1="%d" x2="470" y2="%d" stroke-opacity=".3"/>'
                  % (y, y + 16))
        o += label(484, y, t, 9, "start", ".5")
        o += accent_text(590, y, v, a, 8, "end")
    o += "\n"
    o += accent_text(452, 298, "FOTOGRAMETRI · LIDAR", a, 9)
    o += label(452, 320, "mevcut durum → as-built model", 9, "start", ".4")
    o += dim_line(300, 330, 404, 330)
    o += label(352, 346, "as-built", 9, "middle", ".38")
    o += scanline(a, 50)
    return o + TAIL


# --------------------------------------------------------------------------
def bim_icerik_uretimi():
    """Uretim modeli -> sadelestirme -> parametrik BIM objesi (.rfa) + tip katalogu."""
    a = "#818cf8"
    o = head(a)

    # --- sol: detayli uretim modeli
    o += box(38, 96, 186, 176, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(52, 116, "CAD / URETIM MODELI", a, 9)
    cx, cy = 131, 196
    # govde + kanatlar (yogun hat isi = yuksek yuzey sayisi)
    o += box(cx - 52, cy - 40, 104, 80, "ln", 'fill="%s" fill-opacity=".05"' % a)
    for k in range(1, 13):
        x = cx - 52 + k * 8
        o += ('<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".3"/>'
              % (x, cy - 40, x, cy + 40))
    o += "\n"
    # flans + civatalar
    for sx in (cx - 62, cx + 52):
        o += box(sx, cy - 26, 10, 52, "ln")
        for k in range(3):
            o += ('<circle class="ln2" cx="%d" cy="%d" r="2.6" stroke-opacity=".6"/>'
                  % (sx + 5, cy - 16 + k * 16))
    o += "\n"
    # yuvarlatmalar / pah detaylari
    for dx, dy in ((-52, -40), (52, -40), (52, 40), (-52, 40)):
        o += ('<path class="ln2" d="M%d %d q%d 0 %d %d" stroke-opacity=".45"/>'
              % (cx + dx - (6 if dx > 0 else -6), cy + dy,
                 6 if dx > 0 else -6, 6 if dx > 0 else -6, 6 if dy > 0 else -6))
    o += "\n"
    o += label(131, 258, "1 240 yüzey · 38 MB", 9, "middle", ".4")

    # --- orta: sadelestirme
    o += gear(300, 184, 26, 12, "ln")
    o += arrow(232, 184, 268, 184, a)
    o += arrow(332, 184, 372, 184, a)
    o += accent_text(300, 236, "SADELESTIRME", a, 9, "middle")
    o += label(300, 252, "LOD · veri", 9, "middle", ".38")

    # --- sag: BIM objesi
    o += box(382, 96, 220, 176, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(396, 116, "BIM OBJESI  ·  .rfa", a, 9)
    bx, by = 402, 138
    o += box(bx, by, 78, 62, "ln", 'fill="%s" fill-opacity=".07"' % a)
    o += ('<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".4"/>'
          % (bx, by + 31, bx + 78, by + 31))
    # baglanti noktalari (MEP connector)
    for px_, py_ in ((bx, by + 31), (bx + 78, by + 31)):
        o += ('<g class="blink"><circle cx="%d" cy="%d" r="7" fill="none" stroke="%s" '
              'stroke-opacity=".55" stroke-width="1.1"/></g>' % (px_, py_, CYAN))
        o += node(px_, py_, 2.8)
    o += "\n"
    o += label(bx + 39, by + 78, "bağlantı noktaları", 8, "middle", ".38")
    # parametre tablosu
    params = [("Tip", "R-600"), ("Genislik", "600 mm"), ("Malzeme", "Celik"),
              ("Kod", "AC-1180"), ("Guc", "918 W")]
    for i, (k, v) in enumerate(params):
        y = 150 + i * 17
        o += ('<rect x="490" y="%d" width="100" height="13" rx="3" fill="%s" '
              'fill-opacity=".05"/>' % (y - 10, a))
        o += label(495, y, k, 8, "start", ".45")
        o += accent_text(585, y, v, a, 8, "end")
    o += "\n"
    o += label(490, 254, "paylasilan parametreler", 8, "start", ".38")

    # --- alt: tip katalogu
    o += box(38, 296, 564, 96, "ln2", 'fill="rgba(255,255,255,.02)"')
    o += accent_text(52, 316, "TIP KATALOGU", a, 9)
    cols = ["Tip", "G (mm)", "Y (mm)", "Guc (W)", "Agirlik"]
    rows = [["R-400", "400", "600", "612", "9,4 kg"],
            ["R-600", "600", "600", "918", "13,1 kg"],
            ["R-800", "800", "600", "1 224", "16,8 kg"]]
    xs = [56, 176, 266, 356, 456]
    for i, c in enumerate(cols):
        o += label(xs[i], 336, c, 8, "start", ".38")
    o += ('<line class="ln2" x1="52" y1="342" x2="588" y2="342" stroke-opacity=".22"/>\n')
    for r, row in enumerate(rows):
        y = 358 + r * 14
        for i, v in enumerate(row):
            if i == 0:
                o += accent_text(xs[i], y, v, a, 8)
            else:
                o += label(xs[i], y, v, 8, "start", ".45")
    o += "\n"
    o += accent_text(588, 316, "IFC · rfa · IFC4", a, 9, "end")
    o += scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
BUILDERS = {
    "bim-icerik-uretimi": bim_icerik_uretimi,
    "dijital-donusum": dijital_donusum,
    "bim": bim,
    "simulasyon": simulasyon,
    "tolerans-analizi": tolerans_analizi,
    "tasarim-otomasyonu": tasarim_otomasyonu,
    "dijital-ikiz": dijital_ikiz,
    "fabrika-tasarimi": fabrika_tasarimi,
    "cam": cam,
    "eklemeli-imalat": eklemeli_imalat,
    "nesting": nesting,
    "plm": plm,
    "pdm": pdm,
    "insaat-yonetimi": insaat_yonetimi,
    "gorsellestirme": gorsellestirme,
    "yaratici-icerik": yaratici_icerik,
    "gerceklik-yakalama": gerceklik_yakalama,
}


if __name__ == "__main__":
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    total = 0
    for key, fn in sorted(BUILDERS.items()):
        path = os.path.join(OUT, "%s.svg" % key)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fn())
        size = os.path.getsize(path)
        total += size
        print("%-22s %6d bytes" % (key, size))
    print("%-22s %6d bytes" % ("TOPLAM", total))
