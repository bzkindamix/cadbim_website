# -*- coding: utf-8 -*-
"""Sektor sayfalari icin vektorel teknik illustrasyon uretir.

Her sektore ait SVG assets/img/sektor/ altina yazilir. Dosyalar kendi
kendine yeterlidir (ic CSS animasyonlari <img> ile yuklendiginde de calisir),
seffaf zeminlidir ve sitenin koyu paletine gore renklendirilmistir.
"""
import math
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "img", "sektor")
W, H = 640, 420
CYAN = "#00c8f0"


def f(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


def pts(points):
    return " ".join("%s,%s" % (f(x), f(y)) for x, y in points)


def iso(x, y, z, ox=0, oy=0, s=1.0):
    """Basit izometrik projeksiyon."""
    return (ox + (x - y) * 0.866 * s, oy + (x + y) * 0.5 * s - z * s)


def head(accent):
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img">
<defs>
<pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">
<path d="M40 0H0V40" fill="none" stroke="rgba(255,255,255,.05)" stroke-width="1"/>
</pattern>
<radialGradient id="glow" cx="50%%" cy="45%%" r="60%%">
<stop offset="0%%" stop-color="%s" stop-opacity=".18"/>
<stop offset="100%%" stop-color="%s" stop-opacity="0"/>
</radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%%" stop-color="%s" stop-opacity=".55"/>
<stop offset="100%%" stop-color="%s" stop-opacity=".08"/>
</linearGradient>
</defs>
<style>
.ln{fill:none;stroke:%s;stroke-opacity:.75;stroke-width:1.2;stroke-linejoin:round;stroke-linecap:round}
.ln2{fill:none;stroke:%s;stroke-opacity:.32;stroke-width:1;stroke-linejoin:round;stroke-linecap:round}
.cy{fill:none;stroke:%s;stroke-opacity:.7;stroke-width:1.2;stroke-linecap:round}
.fl{fill:%s;fill-opacity:.06}
.nd{fill:%s}
.dim{fill:none;stroke:rgba(255,255,255,.28);stroke-width:.8;stroke-dasharray:3 4}
.blink{animation:bk 3.2s ease-in-out infinite}
.blink:nth-of-type(2n){animation-delay:.5s}
.blink:nth-of-type(3n){animation-delay:1.1s}
.blink:nth-of-type(5n){animation-delay:1.7s}
@keyframes bk{0%%,100%%{opacity:.2}50%%{opacity:1}}
.draw{stroke-dasharray:6 8;animation:dr 5s linear infinite}
@keyframes dr{to{stroke-dashoffset:-56}}
.scan{animation:sc 7s cubic-bezier(.6,0,.4,1) infinite}
@keyframes sc{0%%{opacity:0;transform:translateY(-40px)}12%%{opacity:1}88%%{opacity:1}100%%{opacity:0;transform:translateY(400px)}}
.spin{transform-box:fill-box;transform-origin:center;animation:sp 24s linear infinite}
.spinr{transform-box:fill-box;transform-origin:center;animation:sp 24s linear infinite reverse}
@keyframes sp{to{transform:rotate(360deg)}}
.float{animation:fo 9s ease-in-out infinite}
@keyframes fo{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-9px)}}
</style>
<rect width="%d" height="%d" fill="url(#g)"/>
<rect width="%d" height="%d" fill="url(#glow)"/>
""" % (W, H, W, H, accent, accent, accent, accent, accent, accent, CYAN,
       accent, accent, W, H, W, H)


TAIL = "</svg>\n"


def scanline(accent, y=0):
    return ('<g class="scan"><line x1="40" y1="%d" x2="600" y2="%d" '
            'stroke="%s" stroke-opacity=".5" stroke-width="1"/></g>\n'
            % (y, y, CYAN))


def node(x, y, r=3.0, cls="nd blink"):
    return '<circle class="%s" cx="%s" cy="%s" r="%s"/>' % (cls, f(x), f(y), f(r))


# --------------------------------------------------------------------------
def mimari():
    a = "#818cf8"
    o = head(a)
    ox, oy, s = 320, 250, 1.0
    px, py = 190, 130          # kat plani olculeri
    floors = [0, 38, 76, 114, 152, 190]
    corners = [(0, 0), (px, 0), (px, py), (0, py)]

    o += '<g class="float">\n'
    # kat doseme plaklari
    for i, z in enumerate(floors):
        p = [iso(x, y, z, ox, oy, s) for x, y in corners]
        cls = "ln" if i in (0, len(floors) - 1) else "ln2"
        o += '<polygon class="fl" points="%s"/>' % pts(p)
        o += '<polygon class="%s" points="%s"/>\n' % (cls, pts(p))
    # kolonlar
    cols = [(0, 0), (px, 0), (px, py), (0, py),
            (px / 2, 0), (px, py / 2), (px / 2, py), (0, py / 2), (px / 2, py / 2)]
    for x, y in cols:
        b = iso(x, y, floors[0], ox, oy, s)
        t = iso(x, y, floors[-1], ox, oy, s)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>\n' % (
            f(b[0]), f(b[1]), f(t[0]), f(t[1]))
    # on cephe mullionlari
    for k in range(1, 8):
        x = px * k / 8.0
        b = iso(x, py, floors[0], ox, oy, s)
        t = iso(x, py, floors[-1], ox, oy, s)
        o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".18"/>\n' % (
            f(b[0]), f(b[1]), f(t[0]), f(t[1]))
    # cati hacmi
    r0 = [iso(x * .45 + 45, y * .45 + 35, floors[-1], ox, oy, s) for x, y in corners]
    r1 = [iso(x * .45 + 45, y * .45 + 35, floors[-1] + 30, ox, oy, s) for x, y in corners]
    o += '<polygon class="cy" points="%s"/>' % pts(r1)
    for i in range(4):
        o += '<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".4"/>' % (
            f(r0[i][0]), f(r0[i][1]), f(r1[i][0]), f(r1[i][1]))
    o += "\n"
    # dugum noktalari
    for x, y in corners:
        for z in floors:
            p = iso(x, y, z, ox, oy, s)
            o += node(p[0], p[1], 2.6)
    o += "\n</g>\n"

    # olcu cizgisi
    b = iso(0, py, floors[0], ox, oy, s)
    t = iso(0, py, floors[-1], ox, oy, s)
    o += ('<line class="dim" x1="%s" y1="%s" x2="%s" y2="%s"/>'
          '<line class="dim" x1="%s" y1="%s" x2="%s" y2="%s"/>\n'
          % (f(b[0] - 34), f(b[1]), f(t[0] - 34), f(t[1]),
             f(b[0] - 44), f(b[1]), f(b[0] - 24), f(b[1])))
    o += scanline(a, 90)
    return o + TAIL


# --------------------------------------------------------------------------
def insaat():
    a = "#22c55e"
    o = head(a)
    deck = 250
    o += '<g class="float">\n'
    # kopru tablasi
    o += ('<path class="ln" d="M30 %d H610"/><path class="ln" d="M30 %d H610"/>\n'
          % (deck, deck + 14))
    for x in range(40, 611, 24):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".2"/>' % (
            x, deck, x, deck + 14)
    o += "\n"
    # pilonlar + askı halatlari
    for px_ in (200, 440):
        o += ('<path class="ln" d="M%d %d L%d 86 L%d %d"/>'
              '<line class="ln" x1="%d" y1="118" x2="%d" y2="118"/>\n'
              % (px_ - 26, deck, px_, px_ + 26, deck, px_ - 16, px_ + 16))
        for k in range(1, 7):
            dx = k * 27
            o += ('<line class="cy draw" x1="%d" y1="92" x2="%d" y2="%d" stroke-opacity=".45"/>'
                  '<line class="cy draw" x1="%d" y1="92" x2="%d" y2="%d" stroke-opacity=".45"/>'
                  % (px_, px_ - dx, deck, px_, px_ + dx, deck))
        o += "\n"
        o += node(px_, 86, 3.2)
    # ayaklar
    for px_ in (110, 320, 530):
        o += ('<path class="ln2" d="M%d %d V330 M%d %d V330 M%d 330 H%d"/>'
              % (px_ - 12, deck + 14, px_ + 12, deck + 14, px_ - 20, px_ + 20))
    o += "\n</g>\n"
    # arazi kontur egrileri
    for i, (yb, amp, op) in enumerate([(348, 12, .5), (368, 16, .35), (390, 10, .22)]):
        p = []
        for x in range(20, 625, 20):
            p.append((x, yb + amp * math.sin(x / 70.0 + i * 1.3)))
        o += '<polyline class="ln2" points="%s" stroke-opacity="%s"/>\n' % (pts(p), op)
    # kule vinc
    o += ('<g class="ln"><path d="M556 300 V120 M544 300 V120 M556 120 H544"/>'
          '<path d="M470 120 H614 M470 120 L556 104 M614 120 L556 104"/>'
          '<path d="M508 120 V150" stroke-dasharray="4 4"/>'
          '<rect x="498" y="150" width="20" height="12" fill="none"/></g>\n')
    for k in range(122, 300, 22):
        o += '<line class="ln2" x1="544" y1="%d" x2="556" y2="%d" stroke-opacity=".25"/>' % (k, k + 22)
    o += "\n" + scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def _gear(cx, cy, r, teeth, cls="ln"):
    """Basit dis carki polygonu."""
    p = []
    ri, ro = r * 0.86, r
    step = math.pi / teeth
    for i in range(teeth):
        a0 = 2 * step * i
        for ang, rad in ((a0, ri), (a0 + step * .28, ro),
                         (a0 + step * .72, ro), (a0 + step, ri)):
            p.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return '<polygon class="%s" points="%s"/>' % (cls, pts(p))


def makine():
    a = "#f59e0b"
    o = head(a)
    o += '<g class="float">\n'
    # ana disli
    o += '<g class="spin">%s</g>\n' % _gear(250, 210, 118, 20)
    o += ('<circle class="ln2" cx="250" cy="210" r="86"/>'
          '<circle class="ln" cx="250" cy="210" r="34"/>'
          '<circle class="ln2" cx="250" cy="210" r="20"/>\n')
    for k in range(6):
        ang = k * math.pi / 3
        o += '<circle class="ln2" cx="%s" cy="%s" r="9"/>' % (
            f(250 + 60 * math.cos(ang)), f(210 + 60 * math.sin(ang)))
    o += "\n"
    # kavrayan kucuk disli
    o += '<g class="spinr">%s</g>\n' % _gear(432, 300, 62, 12)
    o += ('<circle class="ln2" cx="432" cy="300" r="42"/>'
          '<circle class="ln" cx="432" cy="300" r="16"/>\n')
    o += "\n</g>\n"
    # eksen cizgileri
    o += ('<path class="dim" d="M110 210 H396 M250 70 V352"/>'
          '<path class="dim" d="M340 300 H520 M432 214 V388"/>\n')
    # takim yolu (CAM)
    p = []
    for i in range(180):
        t = i / 179.0
        rad = 20 + t * 96
        ang = t * 7.4
        p.append((250 + rad * math.cos(ang), 210 + rad * math.sin(ang) * .62))
    o += '<polyline class="cy draw" points="%s" stroke-opacity=".5"/>\n' % pts(p)
    # olcu / tolerans etiketi
    o += ('<g><path class="dim" d="M470 96 H590 M470 90 V102 M590 90 V102"/>'
          '<rect x="498" y="60" width="64" height="22" rx="4" fill="none" '
          'stroke="rgba(255,255,255,.22)" stroke-width=".8"/>'
          '<path class="ln2" d="M508 71 h44 M508 65 v12" stroke-opacity=".4"/></g>\n')
    for x, y in ((250, 210), (432, 300), (250, 92), (368, 210)):
        o += node(x, y, 3)
    o += "\n" + scanline(a, 70)
    return o + TAIL


# --------------------------------------------------------------------------
CAR = ("M78 292 C78 258 96 236 132 226 L186 210 C214 168 258 148 316 148 "
       "C374 148 420 164 452 200 L520 216 C560 226 578 248 578 288 "
       "L578 300 L78 300 Z")


def otomotiv():
    a = "#ef4444"
    o = head(a)
    o += '<defs><clipPath id="carclip"><path d="%s"/></clipPath></defs>\n' % CAR
    o += '<g class="float">\n'
    o += '<path class="fl" d="%s"/><path class="ln" d="%s"/>\n' % (CAR, CAR)
    # yuzey agi — dusey kesit cizgileri
    o += '<g clip-path="url(#carclip)">'
    for x in range(84, 580, 22):
        o += '<path class="ln2" d="M%d 130 C%d 200 %d 240 %d 310" stroke-opacity=".26"/>' % (
            x, x + 6, x - 6, x)
    for y in range(160, 301, 20):
        o += '<path class="ln2" d="M70 %d C240 %d 420 %d 590 %d" stroke-opacity=".2"/>' % (
            y, y - 10, y - 6, y)
    o += "</g>\n"
    # karakter cizgileri
    o += ('<path class="cy" d="M96 262 C220 244 420 244 566 264" stroke-opacity=".55"/>'
          '<path class="ln2" d="M186 210 C260 190 396 190 452 200"/>'
          '<path class="ln2" d="M262 152 V212 M372 150 V208"/>\n')
    # tekerlekler
    for cx in (186, 470):
        o += ('<circle class="ln" cx="%d" cy="300" r="46"/>'
              '<circle class="ln2" cx="%d" cy="300" r="28"/>'
              '<circle class="ln2" cx="%d" cy="300" r="9"/>\n' % (cx, cx, cx))
        for k in range(5):
            ang = k * 2 * math.pi / 5
            o += '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3"/>' % (
                f(cx + 10 * math.cos(ang)), f(300 + 10 * math.sin(ang)),
                f(cx + 27 * math.cos(ang)), f(300 + 27 * math.sin(ang)))
        o += "\n"
    o += "</g>\n"
    o += '<path class="dim" d="M78 340 H578 M78 332 V348 M578 332 V348"/>\n'
    for x, y in ((316, 148), (186, 210), (452, 200), (578, 288), (78, 292)):
        o += node(x, y, 3)
    o += "\n" + scanline(a, 80)
    return o + TAIL


# --------------------------------------------------------------------------
def medya():
    a = "#c084fc"
    o = head(a)
    cx, cy, r = 250, 190, 122
    o += '<g class="float">\n'
    o += '<circle class="ln" cx="%d" cy="%d" r="%d"/>\n' % (cx, cy, r)
    # boylam
    for k in range(1, 6):
        rx = r * math.cos(k * math.pi / 6)
        o += '<ellipse class="ln2" cx="%d" cy="%d" rx="%s" ry="%d"/>' % (cx, cy, f(abs(rx)), r)
    o += "\n"
    # enlem
    for k in range(1, 6):
        yy = cy - r + 2 * r * k / 6.0
        rx = math.sqrt(max(r * r - (yy - cy) ** 2, 1))
        o += '<ellipse class="ln2" cx="%d" cy="%s" rx="%s" ry="%s"/>' % (
            cx, f(yy), f(rx), f(rx * .22))
    o += "\n"
    # render bucket kareleri
    for i, (bx, by) in enumerate([(196, 128), (240, 128), (196, 172), (284, 216)]):
        o += ('<rect class="cy blink" x="%d" y="%d" width="44" height="44" '
              'fill="none" stroke-opacity=".6"/>' % (bx, by))
    o += "\n</g>\n"
    # film seridi (perspektif)
    o += ('<g><path class="ln" d="M392 132 L610 108 L610 288 L392 312 Z"/>'
          '<path class="ln2" d="M392 168 L610 146 M392 276 L610 252"/>\n')
    for k in range(5):
        t = k / 4.0
        y0 = 132 + t * 180
        y1 = 108 + t * 180
        o += '<path class="ln2" d="M%s %s L%s %s" stroke-opacity=".25"/>' % (
            f(392 + t * 218), f(y0 - t * 0), f(392 + t * 218), f(y1))
    for k in range(6):
        yy = 140 + k * 28
        o += ('<rect class="ln2" x="398" y="%d" width="12" height="10" fill="none"/>'
              '<rect class="ln2" x="590" y="%d" width="12" height="10" fill="none"/>'
              % (yy, yy - 22))
    o += "</g>\n"
    # ses dalgasi
    for k in range(22):
        hgt = 8 + 34 * abs(math.sin(k * .7)) * (0.5 + 0.5 * math.cos(k * .3))
        o += ('<line class="cy blink" x1="%d" y1="%s" x2="%d" y2="%s" stroke-opacity=".45"/>'
              % (60 + k * 10, f(372 - hgt / 2), 60 + k * 10, f(372 + hgt / 2)))
    o += "\n" + scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def egitim():
    a = "#38bdf8"
    o = head(a)
    vx, vy = 320, 150
    # perspektif zemin
    for k in range(-6, 7):
        o += '<line class="ln2" x1="%d" y1="420" x2="%d" y2="%d" stroke-opacity=".22"/>' % (
            320 + k * 96, vx, vy + 70)
    for k in range(1, 8):
        yy = vy + 70 + (k ** 1.9) * 4.6
        if yy > 420:
            break
        o += '<line class="ln2" x1="20" y1="%s" x2="620" y2="%s" stroke-opacity=".18"/>' % (f(yy), f(yy))
    o += "\n"
    # tahta / ekran
    o += ('<g class="float"><rect class="fl" x="176" y="60" width="288" height="150" rx="6"/>'
          '<rect class="ln" x="176" y="60" width="288" height="150" rx="6" fill="none"/>'
          '<line class="ln2" x1="176" y1="86" x2="464" y2="86"/>\n')
    # ekranda izometrik kup
    ox, oy = 320, 168
    cube = [(0, 0), (56, 0), (56, 56), (0, 56)]
    bot = [iso(x, y, 0, ox, oy, .9) for x, y in cube]
    top = [iso(x, y, 56, ox, oy, .9) for x, y in cube]
    o += '<polygon class="cy" points="%s"/><polygon class="cy" points="%s"/>' % (
        pts(bot), pts(top))
    for i in range(4):
        o += '<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>' % (
            f(bot[i][0]), f(bot[i][1]), f(top[i][0]), f(top[i][1]))
    o += "</g>\n"
    # sira duzeni
    for row, (yy, wdt, gap) in enumerate([(268, 56, 74), (312, 68, 90), (364, 82, 108)]):
        for col in (-1, 0, 1):
            x = 320 + col * gap - wdt / 2
            o += ('<rect class="ln2" x="%s" y="%s" width="%s" height="%s" rx="3" '
                  'fill="none" stroke-opacity=".4"/>' % (f(x), f(yy), f(wdt), f(wdt * .3)))
        o += "\n"
    # 3B yazici
    o += ('<g class="ln"><rect x="500" y="196" width="112" height="128" rx="6" fill="none"/>'
          '<line x1="500" y1="286" x2="612" y2="286"/>'
          '<line x1="524" y1="196" x2="524" y2="286" stroke-opacity=".35"/>'
          '<line x1="588" y1="196" x2="588" y2="286" stroke-opacity=".35"/></g>\n')
    for k in range(7):
        wdt = 40 - k * 3
        o += ('<line class="cy blink" x1="%s" y1="%d" x2="%s" y2="%d" stroke-opacity=".55"/>'
              % (f(556 - wdt / 2), 282 - k * 7, f(556 + wdt / 2), 282 - k * 7))
    o += '<line class="ln draw" x1="556" y1="206" x2="556" y2="238"/>\n'
    # mezuniyet kepi
    o += ('<g class="ln float"><path d="M40 118 L104 96 L168 118 L104 140 Z"/>'
          '<path d="M62 128 V156 C62 168 146 168 146 156 V128"/>'
          '<path d="M168 118 V150" stroke-opacity=".5"/></g>\n')
    for x, y in ((320, 168), (556, 240), (104, 118)):
        o += node(x, y, 3)
    o += "\n" + scanline(a, 50)
    return o + TAIL


# --------------------------------------------------------------------------
JET_R = [(320, 52), (334, 128), (344, 176), (352, 196),
         (600, 268), (600, 292), (356, 262), (350, 306),
         (416, 344), (416, 360), (330, 340), (322, 372)]


def havacilik():
    a = "#a5b4fc"
    o = head(a)
    right = JET_R
    left = [(640 - x, y) for x, y in reversed(right)]
    body = right + left
    o += '<g class="float">\n'
    o += '<polygon class="fl" points="%s"/><polygon class="ln" points="%s"/>\n' % (
        pts(body), pts(body))
    # govde eksen ve kaburgalar
    o += '<line class="dim" x1="320" y1="46" x2="320" y2="380"/>\n'
    for yy in range(96, 361, 26):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".22"/>' % (
            296, yy, 344, yy)
    o += "\n"
    # kanat FEA agi (bilinear grid + kosegen)
    quad = [(352, 196), (600, 268), (600, 292), (356, 262)]
    n, m = 8, 4

    def bil(u, v):
        p0, p1, p2, p3 = quad
        ax = p0[0] + (p1[0] - p0[0]) * u
        ay = p0[1] + (p1[1] - p0[1]) * u
        bx = p3[0] + (p2[0] - p3[0]) * u
        by = p3[1] + (p2[1] - p3[1]) * u
        return (ax + (bx - ax) * v, ay + (by - ay) * v)

    mesh = []
    for i in range(n + 1):
        mesh.append('<polyline class="ln2" points="%s" stroke-opacity=".3"/>' % pts(
            [bil(i / float(n), j / float(m)) for j in range(m + 1)]))
    for j in range(m + 1):
        mesh.append('<polyline class="ln2" points="%s" stroke-opacity=".3"/>' % pts(
            [bil(i / float(n), j / float(m)) for i in range(n + 1)]))
    for i in range(n):
        for j in range(m):
            p1 = bil(i / float(n), j / float(m))
            p2 = bil((i + 1) / float(n), (j + 1) / float(m))
            mesh.append('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" '
                        'stroke-opacity=".14"/>' % (f(p1[0]), f(p1[1]), f(p2[0]), f(p2[1])))
    inner = "".join(mesh)
    o += inner + "\n"
    o += ('<g transform="translate(640,0) scale(-1,1)">%s</g>\n' % inner)
    o += "</g>\n"
    # radar
    o += '<g opacity=".55">'
    for r in (74, 116, 158):
        o += ('<path class="cy" d="M%s 372 A%d %d 0 0 1 %s 372" stroke-opacity=".28"/>'
              % (f(96 - r), r, r, f(96 + r)))
    o += ('<g class="spin" style="animation-duration:9s"><line x1="96" y1="372" x2="96" y2="214" '
          'stroke="%s" stroke-opacity=".6" stroke-width="1.2"/></g>' % CYAN)
    o += '<line class="dim" x1="-62" y1="372" x2="254" y2="372"/></g>\n'
    for x, y in ((320, 52), (600, 268), (40, 268), (320, 372)):
        o += node(x, y, 3)
    o += "\n" + scanline(a, 40)
    return o + TAIL


BUILDERS = {
    "mimari": mimari,
    "insaat": insaat,
    "makine": makine,
    "otomotiv": otomotiv,
    "medya": medya,
    "egitim": egitim,
    "havacilik": havacilik,
}

if __name__ == "__main__":
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    for key, fn in BUILDERS.items():
        path = os.path.join(OUT, "%s.svg" % key)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fn())
        print("%-12s %6d bytes" % (key, os.path.getsize(path)))
