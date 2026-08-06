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
.slide{animation:sl 8s cubic-bezier(.55,0,.45,1) infinite}
@keyframes sl{0%%,6%%{transform:translateX(0)}94%%,100%%{transform:translateX(var(--d,480px))}}
.comb{animation:cb 6s ease-in-out infinite}
@keyframes cb{0%%,100%%{opacity:.45}50%%{opacity:.95}}
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


# Sahne icerigini kadraja ortalayan sahne-bazli donusum (DK-2026-08-03-25).
# Gorunur icerik kutlesi tarayicida piksel taramasiyla olculdu; p' = k*p + (tx,ty).
# egitim ve havacilik bilincli olarak yok: kadraj disina tasan zemin/radar cizgileri
# kompozisyon geregi kenardan kesiliyor, kaydirmak gorseli bozuyor.
OFFSETS = {
    "mimari":     (1.0,  -10, -24),
    "icmimarlik": (0.83,  31,  -9),
    "insaat":     (1.0,    0, -24),
    "tesisat":    (0.85,  93, -38),
    "otomotiv":   (1.0,    0, -32),
    "medya":      (1.0,   -2, -39),
}


def apply_offset(key, svg):
    off = OFFSETS.get(key)
    if not off:
        return svg
    k, tx, ty = off
    mark = '<rect width="%d" height="%d" fill="url(#glow)"/>\n' % (W, H)
    i = svg.index(mark) + len(mark)
    assert svg.endswith(TAIL)
    tr = "translate(%s %s)" % (f(tx), f(ty))
    if k != 1.0:
        tr += " scale(%s)" % f(k)
    return (svg[:i] + '<g transform="%s">\n' % tr
            + svg[i:-len(TAIL)] + "</g>\n" + TAIL)


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
def _bez(p, t):
    mt = 1 - t
    return tuple(mt ** 3 * p[0][i] + 3 * mt * mt * t * p[1][i]
                 + 3 * mt * t * t * p[2][i] + t ** 3 * p[3][i] for i in (0, 1))


def _bez_d(p, t):
    mt = 1 - t
    return tuple(3 * mt * mt * (p[1][i] - p[0][i]) + 6 * mt * t * (p[2][i] - p[1][i])
                 + 3 * t * t * (p[3][i] - p[2][i]) for i in (0, 1))


def _bez_dd(p, t):
    mt = 1 - t
    return tuple(6 * mt * (p[2][i] - 2 * p[1][i] + p[0][i])
                 + 6 * t * (p[3][i] - 2 * p[2][i] + p[1][i]) for i in (0, 1))


def curvature_comb(p, n=30, scale=2600.0, cap=54.0, cls="cy"):
    """Alias/VRED tarzi egrilik taragi: egri boyunca normal yonunde tuyler."""
    spikes, tips = [], []
    for i in range(n + 1):
        t = i / float(n)
        pt = _bez(p, t)
        d = _bez_d(p, t)
        dd = _bez_dd(p, t)
        sp = math.hypot(d[0], d[1]) or 1e-6
        k = abs(d[0] * dd[1] - d[1] * dd[0]) / sp ** 3
        ln = min(cap, 6 + k * scale)
        nx, ny = d[1] / sp, -d[0] / sp      # normal — yuzeyden disari
        tip = (pt[0] + nx * ln, pt[1] + ny * ln)
        tips.append(tip)
        spikes.append('<line x1="%s" y1="%s" x2="%s" y2="%s"/>'
                      % (f(pt[0]), f(pt[1]), f(tip[0]), f(tip[1])))
    out = ('<g class="%s comb" stroke-opacity=".5" stroke-width=".9">%s</g>'
           % (cls, "".join(spikes)))
    out += '<polyline class="%s" points="%s" stroke-opacity=".8"/>' % (cls, pts(tips))
    return out


# --- otomotiv yan gorunus geometrisi -------------------------------------
# Gercekci oranlar: uzunluk 516, yukseklik 150 (0.29), dingil mesafesi 300
# (0.58), tekerlek capi 80 (0.155), uzun kaput + alcak cam alani.
GND, WCY, WR = 330, 290, 40          # zemin, tekerlek merkezi, tekerlek yaricapi
WF, WR_X = 170, 470                  # on / arka tekerlek merkez x
ROCKER = 300                         # marspiyel (govde alt hatti)
BELT = 222                           # kemer hatti (cam alt kenari)

CAR = ("M62 300 "
       "C62 276 66 259 80 249 "          # on tampon / burun
       "L118 237 "
       "C162 228 210 222 248 217 "       # uzun kaput
       "C268 207 288 191 306 179 "       # on cam
       "L372 179 "                       # tavan (kisa — coupe)
       "C424 181 464 199 492 220 "       # fastback arka cam
       "L556 229 "
       "C572 232 578 243 578 261 "       # arka panel
       "L578 300 "
       "H520 A50 50 0 0 0 420 300 "      # arka davlumbaz
       "H220 A50 50 0 0 0 120 300 "      # on davlumbaz
       "Z")
ROOF = [(248, 217), (300, 170), (424, 176), (492, 220)]   # egrilik taragi egrisi


def _wheel(cx, accent):
    o = ('<circle class="ln" cx="%d" cy="%d" r="%d"/>'
         '<circle class="ln2" cx="%d" cy="%d" r="%d"/>'
         '<circle class="ln2" cx="%d" cy="%d" r="9"/>\n'
         % (cx, WCY, WR, cx, WCY, WR - 9, cx, WCY))
    for k in range(5):                       # jant kollari
        ang = k * 2 * math.pi / 5 - math.pi / 2
        x1, y1 = cx + 10 * math.cos(ang), WCY + 10 * math.sin(ang)
        x2, y2 = cx + 29 * math.cos(ang), WCY + 29 * math.sin(ang)
        w = 3.4
        px, py = -math.sin(ang) * w, math.cos(ang) * w
        o += ('<polygon class="ln2" points="%s" stroke-opacity=".4" fill="none"/>'
              % pts([(x1 + px, y1 + py), (x2 + px * .4, y2 + py * .4),
                     (x2 - px * .4, y2 - py * .4), (x1 - px, y1 - py)]))
    # fren diski + kaliper
    o += ('\n<path class="cy" d="M%d %d A21 21 0 0 1 %d %d" stroke-opacity=".55"/>'
          '<path class="cy" d="M%d %d l7 -4 v-9 l-7 -4" stroke-opacity=".55" fill="none"/>\n'
          % (cx - 21, WCY, cx, WCY - 21, cx - 20, WCY - 4))
    return o


def otomotiv():
    a = "#ef4444"
    o = head(a)
    o += '<defs><clipPath id="carclip"><path d="%s"/></clipPath></defs>\n' % CAR
    o += '<g class="float">\n'
    o += '<path class="fl" d="%s"/>\n' % CAR

    # --- Class-A yuzey agi (govdeye kirpilmis izoparametrik egriler) ---
    o += '<g clip-path="url(#carclip)">'
    for x in range(66, 580, 16):
        o += ('<path class="ln2" d="M%d 160 C%d 224 %d 268 %d 312" stroke-opacity=".2"/>'
              % (x, x + 6, x - 6, x))
    for y in range(186, 302, 13):
        o += ('<path class="ln2" d="M56 %d C200 %d 430 %d 590 %d" stroke-opacity=".15"/>'
              % (y, y - 11, y - 7, y))
    o += "</g>\n"
    o += '<path class="ln" d="%s"/>\n' % CAR

    # --- cam alani (A-direk / yan cam / arka ceyrek cam) ---
    g1 = ("M258 214 C276 202 292 188 308 178 L366 178 C374 196 376 208 376 216 Z")
    g2 = ("M386 178 C424 181 456 197 480 216 L386 216 Z")
    for gp in (g1, g2):
        o += ('<path d="%s" fill="#0a1225" fill-opacity=".72"/>'
              '<path class="ln" d="%s" stroke-opacity=".8"/>' % (gp, gp))
    # cam yansimasi
    o += ('\n<path class="cy" d="M272 206 L318 182 M292 210 L340 182" '
          'stroke-opacity=".28" stroke-width="1"/>'
          '<path class="cy" d="M404 192 L436 210" stroke-opacity=".28" stroke-width="1"/>\n')

    # --- karakter hatlari, kapi ayrimi, detaylar ---
    o += ('<path class="cy" d="M104 252 C210 246 380 250 528 262" stroke-opacity=".65"/>'
          '<path class="ln2" d="M92 268 C220 276 400 278 556 272" stroke-opacity=".4"/>'
          '<path class="ln2" d="M220 300 H420" stroke-opacity=".5"/>\n')
    o += ('<path class="ln2" d="M381 176 V300" stroke-opacity=".45"/>'          # B-direk
          '<path class="ln2" d="M256 218 C254 250 254 274 255 298" stroke-opacity=".45"/>'
          '<path class="ln2" d="M484 222 C486 246 487 266 488 288" stroke-opacity=".45"/>'
          '<rect class="ln2" x="344" y="234" width="26" height="7" rx="3.5" fill="none"/>'
          '<path class="ln2" d="M262 210 l-16 -7 l-6 8 l16 6 Z" stroke-opacity=".6"/>\n')
    # far / stop / hava girisi
    o += ('<path class="cy" d="M74 244 L112 238 L110 250 L76 254 Z" stroke-opacity=".7"/>'
          '<path class="cy" d="M566 240 L578 241 L578 254 L564 252 Z" stroke-opacity=".7"/>'
          '<path class="ln2" d="M66 276 L104 272 M68 284 L100 281" stroke-opacity=".45"/>\n')

    o += _wheel(WF, a) + _wheel(WR_X, a)
    o += "</g>\n"

    # --- Class-A denetimi: egrilik taragi + NURBS kontrol poligonu ---
    o += curvature_comb(ROOF, scale=2100.0, cap=46.0) + "\n"
    o += '<polyline class="dim" points="%s"/>' % pts(ROOF)
    for x, y in ROOF:
        o += ('<rect x="%s" y="%s" width="7" height="7" fill="none" '
              'stroke="rgba(255,255,255,.55)" stroke-width="1"/>' % (f(x - 3.5), f(y - 3.5)))
    o += "\n"

    # --- kesit duzlemi ---
    o += ('<g><ellipse class="cy" cx="330" cy="242" rx="17" ry="62" stroke-opacity=".4" '
          'stroke-dasharray="5 5"/>'
          '<line class="dim" x1="330" y1="150" x2="330" y2="344"/>'
          '<text x="338" y="160" fill="rgba(255,255,255,.45)" font-size="10" '
          'font-family="monospace" letter-spacing="1">SEC A-A</text></g>\n')

    # --- olculer: dingil mesafesi + toplam uzunluk ---
    o += ('<path class="dim" d="M170 362 H470 M170 354 V370 M470 354 V370"/>'
          '<path class="dim" d="M62 390 H578 M62 382 V398 M578 382 V398"/>'
          '<line class="dim" x1="62" y1="330" x2="578" y2="330"/>\n')
    for x, y in ((306, 179), (372, 179), (248, 217), (492, 220), (62, 276), (578, 261)):
        o += node(x, y, 2.8)
    o += "\n" + scanline(a, 96)
    return o + TAIL


# --------------------------------------------------------------------------
def medya():
    """Prodüksiyon sahnesi: film kamerası + render viewport + zaman çizelgesi."""
    a = "#c084fc"
    o = head(a)

    # ---------------- film kamerasi ----------------
    o += '<g class="float">\n'
    for rx in (128, 208):                       # iki makara
        o += ('<circle class="ln" cx="%d" cy="146" r="33"/>'
              '<circle class="ln2" cx="%d" cy="146" r="24"/>'
              '<circle class="ln" cx="%d" cy="146" r="8"/>\n' % (rx, rx, rx))
        for k in range(5):
            ang = k * 2 * math.pi / 5 + .4
            o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".38"/>'
                  % (f(rx + 9 * math.cos(ang)), f(146 + 9 * math.sin(ang)),
                     f(rx + 23 * math.cos(ang)), f(146 + 23 * math.sin(ang))))
        o += "\n"
    o += ('<rect class="fl" x="98" y="178" width="152" height="78" rx="9"/>'
          '<rect class="ln" x="98" y="192" width="152" height="78" rx="9" fill="none"/>'
          '<rect class="ln2" x="110" y="190" width="42" height="26" rx="4" fill="none"/>'
          '<path class="ln2" d="M110 232 h64 M110 242 h40"/>\n')
    # vizor + objektif
    o += ('<rect class="ln2" x="206" y="162" width="30" height="18" rx="4" fill="none"/>'
          '<path class="ln" d="M250 196 L292 186 L292 248 L250 238 Z"/>'
          '<circle class="ln" cx="292" cy="217" r="27"/>'
          '<circle class="ln2" cx="292" cy="217" r="17"/>'
          '<circle class="cy blink" cx="292" cy="217" r="7"/>\n')
    o += "</g>\n"
    # tripod
    o += ('<path class="ln2" d="M174 256 V270 M152 270 h44 M174 270 L142 302 '
          'M174 270 L206 302 M174 270 V296 M136 302 h13 M199 302 h13 M167 296 h14"/>\n')

    # ---------------- render viewport ----------------
    o += ('<rect class="fl" x="332" y="100" width="272" height="190" rx="8"/>'
          '<rect class="ln" x="332" y="100" width="272" height="190" rx="8" fill="none"/>'
          '<path class="cy" d="M340 116 V108 h10 M596 108 h-10 M596 108 V116 '
          'M340 274 v8 h10 M596 282 h-10 M596 282 v-8" stroke-opacity=".7"/>'
          '<text x="346" y="276" fill="rgba(255,255,255,.4)" font-size="9" '
          'font-family="monospace" letter-spacing="1.5">RENDER 01</text>\n')
    # zemin perspektif izgarasi
    o += '<g clip-path="url(#vp)">'
    for k in range(-7, 8):
        o += ('<line class="ln2" x1="%d" y1="290" x2="468" y2="212" stroke-opacity=".2"/>'
              % (468 + k * 52))
    for k in range(1, 6):
        yy = 212 + (k ** 1.85) * 3.6
        o += '<line class="ln2" x1="332" y1="%s" x2="604" y2="%s" stroke-opacity=".16"/>' % (
            f(yy), f(yy))
    o += "</g>\n"
    o += ('<defs><clipPath id="vp"><rect x="332" y="100" width="272" height="190" rx="8"/>'
          '</clipPath></defs>\n')
    # telkafes kure (3B varlik)
    scx, scy, sr = 462, 190, 46
    o += '<circle class="ln" cx="%d" cy="%d" r="%d"/>' % (scx, scy, sr)
    for k in range(1, 4):
        o += '<ellipse class="ln2" cx="%d" cy="%d" rx="%s" ry="%d" stroke-opacity=".45"/>' % (
            scx, scy, f(sr * math.cos(k * math.pi / 4)), sr)
    for k in range(1, 4):
        yy = scy - sr + 2 * sr * k / 4.0
        rx = math.sqrt(max(sr * sr - (yy - scy) ** 2, 1))
        o += ('<ellipse class="ln2" cx="%d" cy="%s" rx="%s" ry="%s" stroke-opacity=".45"/>'
              % (scx, f(yy), f(rx), f(rx * .26)))
    o += ('<ellipse class="ln2" cx="%d" cy="252" rx="52" ry="11" stroke-opacity=".3"/>\n'
          % scx)
    # isik kaynagi + isin konisi
    o += ('<circle class="cy" cx="368" cy="124" r="9" stroke-opacity=".8"/>'
          '<path class="cy" d="M368 124 L420 156 M368 124 L432 144" stroke-opacity=".28" '
          'stroke-dasharray="4 4"/>\n')
    for k in range(4):
        ang = k * math.pi / 2 + .78
        o += ('<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".55"/>'
              % (f(368 + 13 * math.cos(ang)), f(124 + 13 * math.sin(ang)),
                 f(368 + 19 * math.cos(ang)), f(124 + 19 * math.sin(ang))))
    o += "\n"
    # render bucket'lari
    for bx, by in ((424, 152), (452, 152), (424, 180), (496, 208)):
        o += ('<rect class="cy blink" x="%d" y="%d" width="28" height="28" '
              'fill="none" stroke-opacity=".75"/>' % (bx, by))
    o += "\n"

    # ---------------- zaman cizelgesi ----------------
    o += '<path class="ln2" d="M40 326 H604" stroke-opacity=".35"/>'
    for k in range(0, 24):
        x = 46 + k * 24
        o += '<line class="ln2" x1="%d" y1="326" x2="%d" y2="%d" stroke-opacity=".28"/>' % (
            x, x, 320 if k % 4 else 314)
    o += "\n"
    clips = [(46, 112), (164, 88), (258, 136), (400, 92), (498, 106)]
    for cx0, cw in clips:
        o += ('<rect class="fl" x="%d" y="338" width="%d" height="26" rx="4"/>'
              '<rect class="ln" x="%d" y="338" width="%d" height="26" rx="4" fill="none" '
              'stroke-opacity=".6"/>' % (cx0, cw, cx0, cw))
    o += "\n"
    # ses kanali + dalga formu
    o += ('<rect class="ln2" x="46" y="370" width="558" height="26" rx="4" fill="none" '
          'stroke-opacity=".35"/>')
    for k in range(38):
        hgt = 3 + 19 * abs(math.sin(k * .78)) * (.3 + .7 * abs(math.cos(k * .29)))
        o += ('<line class="cy" x1="%d" y1="%s" x2="%d" y2="%s" stroke-opacity=".4" '
              'stroke-width=".9"/>' % (58 + k * 14, f(383 - hgt / 2), 58 + k * 14, f(383 + hgt / 2)))
    o += "\n"
    # anahtar kareler
    for kx in (72, 148, 236, 300, 372, 446, 528):
        o += ('<path class="cy" d="M%d 326 l5 5 l-5 5 l-5 -5 Z" fill="%s" '
              'fill-opacity=".55" stroke-opacity=".9"/>' % (kx, CYAN))
    o += "\n"
    # oynatma kafasi
    o += ('<g class="slide" style="--d:520px"><path d="M40 308 h12 l-6 9 Z" fill="%s"/>'
          '<line x1="46" y1="308" x2="46" y2="400" stroke="%s" stroke-width="1.2" '
          'stroke-opacity=".85"/></g>\n' % (CYAN, CYAN))
    for x, y in ((292, 217), (462, 190), (368, 124)):
        o += node(x, y, 2.8)
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


# --------------------------------------------------------------------------
def tesisat():
    """Mekanik tesisat: klima santrali, kanal hatti, difuzorler, borulama."""
    a = "#2dd4bf"
    o = head(a)
    o += '<g class="float">\n'

    # --- klima santrali (AHU) — izometrik govde + fan ---
    ox, oy, s = 150, 240, 1.0
    W_, D_, H_ = 96, 66, 78
    base = [(0, 0), (W_, 0), (W_, D_), (0, D_)]
    b0 = [iso(x, y, 0, ox, oy, s) for x, y in base]
    b1 = [iso(x, y, H_, ox, oy, s) for x, y in base]
    o += '<polygon class="fl" points="%s"/>' % pts(b1 + [b0[3], b0[0], b0[1]])
    o += '<polygon class="ln" points="%s"/>' % pts(b1)
    for i in range(4):
        op = ".85" if i in (0, 3) else ".4"
        o += ('<line class="ln" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity="%s"/>'
              % (f(b0[i][0]), f(b0[i][1]), f(b1[i][0]), f(b1[i][1]), op))
    o += '<polygon class="ln" points="%s" stroke-opacity=".55"/>\n' % pts(b0)
    # on yuzde fan — donen kanat
    fc = iso(W_ * .5, D_, H_ * .52, ox, oy, s)
    fx, fy = fc
    o += ('<ellipse class="ln" cx="%s" cy="%s" rx="21" ry="24"/>'
          '<ellipse class="ln2" cx="%s" cy="%s" rx="13" ry="15"/>' % (f(fx), f(fy), f(fx), f(fy)))
    o += '<g class="spin" style="animation-duration:10s">'
    for k in range(3):
        ang = k * 2 * math.pi / 3
        o += ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-opacity=".7" '
              'stroke-width="1.2" stroke-linecap="round"/>'
              % (f(fx), f(fy), f(fx + 12 * math.cos(ang)), f(fy + 14 * math.sin(ang)), a))
    o += "</g>\n"
    # panel cizgileri + ayaklar
    m1 = iso(W_ * .5, 0, 0, ox, oy, s); m2 = iso(W_ * .5, 0, H_, ox, oy, s)
    o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3"/>'
          % (f(m1[0]), f(m1[1]), f(m2[0]), f(m2[1])))
    for x, y in ((6, 6), (W_ - 6, 6), (W_ - 6, D_ - 6), (6, D_ - 6)):
        p0 = iso(x, y, 0, ox, oy, s)
        o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s"/>'
              % (f(p0[0]), f(p0[1]), f(p0[0]), f(p0[1] + 10)))
    o += "\n"

    # --- ana kanal hatti (dikdortgen kesit, izometrik) ---
    def duct(p0, p1, w=14):
        """Iki 3B nokta arasi kanal — dort paralel ayrit."""
        x0, y0, z0 = p0; x1, y1, z1 = p1
        segs = []
        for dy, dz in ((0, 0), (w, 0), (0, w), (w, w)):
            a0 = iso(x0, y0 + dy, z0 + dz, ox, oy, s)
            a1 = iso(x1, y1 + dy, z1 + dz, ox, oy, s)
            op = ".8" if (dy, dz) in ((0, w),) else (".5" if dz == w else ".35")
            segs.append('<line class="ln" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity="%s"/>'
                        % (f(a0[0]), f(a0[1]), f(a1[0]), f(a1[1]), op))
        return "".join(segs)

    ZD = H_ * .78          # kanal kotu
    o += duct((W_, D_ * .3, ZD), (W_ + 300, D_ * .3, ZD)) + "\n"
    # kesit halkalari (flanslar)
    for t in (60, 150, 240):
        c4 = [iso(W_ + t, D_ * .3 + dy, ZD + dz, ox, oy, s)
              for dy, dz in ((0, 0), (14, 0), (14, 14), (0, 14))]
        o += '<polygon class="ln2" points="%s" stroke-opacity=".5"/>' % pts(c4)
    o += "\n"
    # dikey bransman + difuzor (2 adet)
    for t, drop in ((100, 46), (200, 46)):
        bx0 = W_ + t
        o += duct((bx0, D_ * .3, ZD), (bx0, D_ * .3, ZD - drop), w=14)
        # difuzor: ic ice kareler (tavan menfezi)
        for k, r_ in enumerate((16, 10, 4)):
            q = [iso(bx0 + 7 - r_ / 2 + dx, D_ * .3 + 7 - r_ / 2 + dy, ZD - drop, ox, oy, s)
                 for dx, dy in ((0, 0), (r_, 0), (r_, r_), (0, r_))]
            o += '<polygon class="cy" points="%s" stroke-opacity="%s"/>' % (
                pts(q), (.7, .45, .3)[k])
        o += "\n"
    # akis oklari (kanal ustunde, draw animasyonu)
    fl0 = iso(W_ + 14, D_ * .3 + 7, ZD + 20, ox, oy, s)
    fl1 = iso(W_ + 286, D_ * .3 + 7, ZD + 20, ox, oy, s)
    o += ('<line class="cy draw" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
          % (f(fl0[0]), f(fl0[1]), f(fl1[0]), f(fl1[1])))
    ah = iso(W_ + 286, D_ * .3 + 7, ZD + 20, ox, oy, s)
    o += ('<path class="cy" d="M%s %s l-9 -4 m9 4 l-10 3" stroke-opacity=".7"/>\n'
          % (f(ah[0]), f(ah[1])))

    # --- borulama (alt kot): gidis-donus + vana ---
    for zoff, op in ((6, ".7"), (16, ".45")):
        p0 = iso(W_ + 6, D_ * .95, zoff, ox, oy, s)
        p1 = iso(W_ + 290, D_ * .95, zoff, ox, oy, s)
        o += ('<line class="ln" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity="%s"/>'
              % (f(p0[0]), f(p0[1]), f(p1[0]), f(p1[1]), op))
        for t in (40, 130, 220):
            q = iso(W_ + t, D_ * .95, zoff, ox, oy, s)
            o += '<ellipse class="ln2" cx="%s" cy="%s" rx="2.6" ry="5" stroke-opacity=".55"/>' % (
                f(q[0]), f(q[1]))
    # vana (kelebek)
    v = iso(W_ + 175, D_ * .95, 6, ox, oy, s)
    o += ('<path class="cy" d="M%s %s l-8 -5 v10 Z M%s %s l8 -5 v10 Z" fill="none" '
          'stroke-opacity=".8"/>'
          '<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".6"/>\n'
          % (f(v[0]), f(v[1]), f(v[0]), f(v[1]), f(v[0]), f(v[1] - 5), f(v[0]), f(v[1] - 13)))

    o += "</g>\n"
    # olcu cizgisi + dugumler
    d0 = iso(W_, D_ * .3, ZD + 34, ox, oy, s)
    d1 = iso(W_ + 300, D_ * .3, ZD + 34, ox, oy, s)
    o += ('<line class="dim" x1="%s" y1="%s" x2="%s" y2="%s"/>\n'
          % (f(d0[0]), f(d0[1]), f(d1[0]), f(d1[1])))
    for pt3 in ((W_ * .5, D_, H_ * .52), (W_ + 100, D_ * .3 + 7, ZD - 46),
                (W_ + 200, D_ * .3 + 7, ZD - 46), (W_ + 175, D_ * .95, 6)):
        q = iso(pt3[0], pt3[1], pt3[2], ox, oy, s)
        o += node(q[0], q[1], 2.8)
    o += "\n" + scanline(a, 60)
    return o + TAIL


# --------------------------------------------------------------------------
def icmimarlik():
    """Ic mimarlik: izometrik oda kosesi — kanepe, sehpa, sarkit, tablo, hali."""
    a = "#f472b6"
    o = head(a)
    ox, oy, s = 320, 300, 1.05
    RW, RD, RH = 210, 150, 120        # oda olculeri

    o += '<g class="float">\n'
    # zemin izgara
    for t in range(0, RW + 1, 30):
        p0 = iso(t, 0, 0, ox, oy, s); p1 = iso(t, RD, 0, ox, oy, s)
        o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".16"/>'
              % (f(p0[0]), f(p0[1]), f(p1[0]), f(p1[1])))
    for t in range(0, RD + 1, 30):
        p0 = iso(0, t, 0, ox, oy, s); p1 = iso(RW, t, 0, ox, oy, s)
        o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".16"/>'
              % (f(p0[0]), f(p0[1]), f(p1[0]), f(p1[1])))
    o += "\n"
    # iki duvar (arka kose)
    for wall in ((((0, 0), (RW, 0))), (((0, 0), (0, RD)))):
        (x0, y0), (x1, y1) = wall
        c0 = iso(x0, y0, 0, ox, oy, s); c1 = iso(x1, y1, 0, ox, oy, s)
        c2 = iso(x1, y1, RH, ox, oy, s); c3 = iso(x0, y0, RH, ox, oy, s)
        o += '<polygon class="fl" points="%s"/>' % pts([c0, c1, c2, c3])
        o += '<polyline class="ln" points="%s" stroke-opacity=".7"/>' % pts([c1, c2, c3, c0])
    o += "\n"
    # pencere (sag duvarda: x sabit 0 duvari yerine RW,0 duvari... arka duvar boyunca)
    wx0, wx1, wz0, wz1 = 120, 195, 34, 96
    win = [iso(wx0, 0, wz0, ox, oy, s), iso(wx1, 0, wz0, ox, oy, s),
           iso(wx1, 0, wz1, ox, oy, s), iso(wx0, 0, wz1, ox, oy, s)]
    o += '<polygon points="%s" fill="#0a1225" fill-opacity=".7"/>' % pts(win)
    o += '<polygon class="ln" points="%s" stroke-opacity=".8"/>' % pts(win)
    mid = iso((wx0 + wx1) / 2, 0, wz0, ox, oy, s); mid2 = iso((wx0 + wx1) / 2, 0, wz1, ox, oy, s)
    o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
          % (f(mid[0]), f(mid[1]), f(mid2[0]), f(mid2[1])))
    h1 = iso(wx0, 0, (wz0 + wz1) / 2, ox, oy, s); h2 = iso(wx1, 0, (wz0 + wz1) / 2, ox, oy, s)
    o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
          % (f(h1[0]), f(h1[1]), f(h2[0]), f(h2[1])))
    # cam yansimasi
    g1 = iso(wx0 + 12, 0, wz0 + 10, ox, oy, s); g2 = iso(wx0 + 34, 0, wz1 - 10, ox, oy, s)
    o += ('<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".3"/>\n'
          % (f(g1[0]), f(g1[1]), f(g2[0]), f(g2[1])))
    # tablo (sol duvarda)
    for tx0, tx1, tz0, tz1, op in ((30, 70, 56, 92, ".7"), (82, 106, 62, 86, ".5")):
        fr = [iso(0, tx0, tz0, ox, oy, s), iso(0, tx1, tz0, ox, oy, s),
              iso(0, tx1, tz1, ox, oy, s), iso(0, tx0, tz1, ox, oy, s)]
        o += '<polygon class="ln" points="%s" stroke-opacity="%s"/>' % (pts(fr), op)
    # tablo icine soyut cizgi
    a1 = iso(0, 38, 64, ox, oy, s); a2 = iso(0, 52, 84, ox, oy, s); a3 = iso(0, 64, 68, ox, oy, s)
    o += ('<polyline class="cy" points="%s" stroke-opacity=".5"/>\n'
          % pts([a1, a2, a3]))

    # hali (elips)
    rc = iso(120, 92, 0, ox, oy, s)
    o += ('<ellipse class="ln2" cx="%s" cy="%s" rx="72" ry="30" stroke-opacity=".4"/>'
          '<ellipse class="ln2" cx="%s" cy="%s" rx="56" ry="22" stroke-opacity=".25"/>\n'
          % (f(rc[0]), f(rc[1]), f(rc[0]), f(rc[1])))

    # kanepe (L)
    def isobox(x, y, w, d, h, z=0, op=".8"):
        bb0 = [iso(px, py, z, ox, oy, s) for px, py in
               ((x, y), (x + w, y), (x + w, y + d), (x, y + d))]
        bb1 = [iso(px, py, z + h, ox, oy, s) for px, py in
               ((x, y), (x + w, y), (x + w, y + d), (x, y + d))]
        out = '<polygon class="ln" points="%s" stroke-opacity="%s"/>' % (pts(bb1), op)
        for i2 in range(4):
            out += ('<line class="ln" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".35"/>'
                    % (f(bb0[i2][0]), f(bb0[i2][1]), f(bb1[i2][0]), f(bb1[i2][1])))
        out += '<polygon class="ln2" points="%s" stroke-opacity=".3"/>' % pts(bb0)
        return out
    # oturma + sirt + kolcaklar
    o += isobox(28, 96, 84, 40, 16)                 # oturma
    o += isobox(28, 88, 84, 10, 34)                 # sirt
    o += isobox(20, 88, 10, 48, 24)                 # sol kolcak
    o += isobox(110, 88, 10, 48, 24) + "\n"         # sag kolcak
    # minderler
    m1 = iso(48, 98, 17, ox, oy, s); m2 = iso(68, 98, 17, ox, oy, s)
    o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".4"/>\n'
          % (f(m1[0]), f(m1[1]), f(m2[0]), f(m2[1])))

    # sehpa (yuvarlak, iki elips + ayak)
    tc = iso(150, 118, 0, ox, oy, s)
    tt = iso(150, 118, 22, ox, oy, s)
    o += ('<ellipse class="ln" cx="%s" cy="%s" rx="26" ry="11" stroke-opacity=".8"/>'
          '<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
          '<ellipse class="ln2" cx="%s" cy="%s" rx="8" ry="3.4" stroke-opacity=".5"/>\n'
          % (f(tt[0]), f(tt[1]), f(tt[0]), f(tt[1]), f(tc[0]), f(tc[1]), f(tc[0]), f(tc[1])))

    # sarkit lamba + isik konisi
    lp = iso(150, 118, RH + 26, ox, oy, s)
    lb = iso(150, 118, 78, ox, oy, s)
    o += ('<line class="ln2" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
          '<path class="ln" d="M%s %s l-11 14 h22 Z" fill="none" stroke-opacity=".8"/>'
          % (f(lp[0]), f(lp[1]), f(lb[0]), f(lb[1] - 14), f(lb[0]), f(lb[1] - 14)))
    o += ('<path class="cy blink" d="M%s %s L%s %s M%s %s L%s %s" stroke-opacity=".3"/>\n'
          % (f(lb[0] - 11), f(lb[1]), f(tt[0] - 24), f(tt[1]),
             f(lb[0] + 11), f(lb[1]), f(tt[0] + 24), f(tt[1])))

    # saksi bitkisi (sag on)
    pp = iso(196, 30, 0, ox, oy, s)
    o += ('<path class="ln" d="M%s %s h14 l-2.5 13 h-9 Z" fill="none" stroke-opacity=".6"/>'
          % (f(pp[0] - 7), f(pp[1] - 13)))
    for ang in (-.7, -.2, .35, .8):
        o += ('<path class="ln2" d="M%s %s q %s -14 %s -22" stroke-opacity=".55"/>'
              % (f(pp[0]), f(pp[1] - 13), f(10 * math.sin(ang)), f(16 * math.sin(ang))))
    o += "\n</g>\n"

    # malzeme paleti (sag ust — kumas/renk ornekleri)
    o += '<g>'
    for k in range(4):
        o += ('<rect class="ln2" x="%d" y="%d" width="24" height="24" rx="4" fill="%s" '
              'fill-opacity="%s" stroke-opacity=".5"/>'
              % (516, 58 + k * 32, a, (0.28, 0.16, 0.08, 0.02)[k]))
    o += ('<line class="dim" x1="510" y1="52" x2="510" y2="182"/>'
          '</g>\n')
    # olcu
    d0 = iso(0, 0, RH + 8, ox, oy, s); d1 = iso(RW, 0, RH + 8, ox, oy, s)
    o += ('<line class="dim" x1="%s" y1="%s" x2="%s" y2="%s"/>\n'
          % (f(d0[0]), f(d0[1]), f(d1[0]), f(d1[1])))
    for pt3 in ((150, 118, 78), (0, 50, 92), (157.5, 0, 96), (110, 88, 24)):
        q = iso(pt3[0], pt3[1], pt3[2], ox, oy, s)
        o += node(q[0], q[1], 2.8)
    o += "\n" + scanline(a, 70)
    return o + TAIL


# --------------------------------------------------------------------------
def yapiurunleri():
    """Yapi urunleri & fabrikasyon: civatali celik bagi + nesting kesim plakasi."""
    a = "#f97316"
    o = head(a)
    o += '<g class="float">\n'
    # --- civatali moment baglantisi (kolon + kiris + baglanti plakasi) ---
    cx, cy = 168, 210
    # kolon (dikey I-profil, basit iki flanş + gövde)
    o += ('<path class="ln" d="M%d 40 V%d M%d 40 V%d" />' % (cx - 22, cy + 20, cx + 22, cy + 20)
          + '<path class="ln2" d="M%d 40 H%d M%d %d H%d" stroke-opacity=".5"/>'
          % (cx - 22, cx + 22, cx - 22, cy + 20, cx + 22))
    for yy in range(56, cy, 22):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".22"/>' % (
            cx - 10, yy, cx + 10, yy)
    # kiris (yatay I-profil)
    o += ('<path class="ln" d="M%d %d H560 M%d %d H560" />' % (cx + 24, cy - 16, cx + 24, cy + 16)
          + '<line class="ln2" x1="%d" y1="%d" x2="560" y2="%d" stroke-opacity=".5"/>'
          % (cx + 24, cy, cy))
    for xx in range(cx + 46, 560, 26):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".22"/>' % (
            xx, cy - 10, xx, cy + 10)
    # bagli plaka + civata deseni
    o += ('<rect class="fl" x="%d" y="%d" width="46" height="72" rx="4"/>'
          '<rect class="ln" x="%d" y="%d" width="46" height="72" rx="4" fill="none"/>\n'
          % (cx, cy - 36, cx, cy - 36))
    for bx, by in ((cx + 10, cy - 24), (cx + 36, cy - 24), (cx + 10, cy), (cx + 36, cy),
                   (cx + 10, cy + 24), (cx + 36, cy + 24)):
        o += '<circle class="cy blink" cx="%d" cy="%d" r="3.6"/>' % (bx, by)
    o += "\n</g>\n"

    # --- nesting: sac plaka uzerinde yerlestirilmis parcalar ---
    px0, py0, pw, ph = 380, 60, 220, 300
    o += ('<rect class="ln" x="%d" y="%d" width="%d" height="%d" fill="none"/>'
          % (px0, py0, pw, ph))
    parts = [(px0 + 10, py0 + 10, 70, 46), (px0 + 88, py0 + 10, 46, 46),
             (px0 + 10, py0 + 64, 46, 90), (px0 + 64, py0 + 64, 70, 40),
             (px0 + 64, py0 + 112, 70, 42), (px0 + 142, py0 + 10, 66, 68),
             (px0 + 142, py0 + 86, 66, 66), (px0 + 10, py0 + 162, 130, 50),
             (px0 + 10, py0 + 220, 198, 44), (px0 + 142, py0 + 160, 66, 52)]
    for i, (x, y, w, h) in enumerate(parts):
        o += ('<rect class="ln2" x="%d" y="%d" width="%d" height="%d" fill="%s" '
              'fill-opacity=".07" stroke-opacity=".5"/>' % (x, y, w, h, a))
    # CAM kesim yolu -- ilk parcayi dolasan kesikli cizgi
    cx0, cy0, cw, ch = parts[0]
    path = ('M%d %d H%d V%d H%d Z' % (cx0, cy0, cx0 + cw, cy0 + ch, cx0))
    o += '<path class="cy draw" d="%s" fill="none" stroke-opacity=".8"/>\n' % path
    for x, y, w, h in parts[:4]:
        o += node(x + w / 2.0, y + h / 2.0, 2.2, cls="nd")

    # olcu cizgisi + tarama
    o += ('<path class="dim" d="M%d %d H%d M%d %d V%d M%d %d V%d"/>\n'
          % (px0, py0 - 14, px0 + pw, px0, py0 - 20, py0 - 8, px0 + pw, py0 - 20, py0 - 8))
    o += scanline(a, 60)
    return o + TAIL


def tuketici():
    """Tuketici urunleri: enjeksiyon kalibi kesiti + render viewport isik konisi."""
    a = "#3b82f6"
    o = head(a)

    # --- basit urun siluyeti (sise/kutu govdesi) ---
    body_path = ("M150 300 C150 300 140 240 148 190 C152 160 168 140 176 118 "
                 "C182 100 180 84 176 70 L204 70 C200 84 198 100 204 118 "
                 "C212 140 228 160 232 190 C240 240 230 300 230 300 Z")
    o += '<g class="float">\n'
    o += '<path class="fl" d="%s"/><path class="ln" d="%s"/>\n' % (body_path, body_path)
    for yy in range(140, 296, 20):
        o += '<path class="ln2" d="M154 %d Q190 %d 226 %d" stroke-opacity=".22"/>' % (
            yy, yy - 4, yy)
    o += ('<rect class="ln2" x="172" y="66" width="36" height="10" rx="3" fill="none" '
          'stroke-opacity=".6"/>\n</g>\n')

    # --- enjeksiyon kalibi kesiti (iki yari + ayrim hatti + sprue) ---
    mx, my = 120, 340
    o += ('<path class="ln" d="M%d %d H%d V%d H%d Z" fill="none"/>'
          % (mx, my, mx + 200, my + 50, mx))
    o += '<line class="cy draw" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".7"/>' % (
        mx, my + 25, mx + 200, my + 25)
    o += ('<path class="ln2" d="M%d %d L%d %d L%d %d Z" fill="none" stroke-opacity=".6"/>\n'
          % (mx + 90, my, mx + 110, my, mx + 100, my - 22))
    for xx in (mx + 30, mx + 170):
        o += node(xx, my + 25, 2.4)

    # --- render viewport ---
    vx, vy, vw, vh = 360, 90, 240, 190
    o += ('<rect class="fl" x="%d" y="%d" width="%d" height="%d" rx="8"/>'
          '<rect class="ln" x="%d" y="%d" width="%d" height="%d" rx="8" fill="none"/>\n'
          % (vx, vy, vw, vh, vx, vy, vw, vh))
    for k in range(-4, 5):
        o += '<line class="ln2" x1="%d" y1="%d" x2="%d" y2="%d" stroke-opacity=".18"/>' % (
            vx + vw // 2 + k * 30, vy + vh, vx + vw // 2, vy + vh - 60)
    lx, ly = vx + 60, vy + 40
    o += ('<circle class="cy" cx="%d" cy="%d" r="9" stroke-opacity=".8"/>'
          % (lx, ly))
    for k in range(5):
        ang = k * math.pi / 4 - math.pi / 2
        o += ('<line class="cy" x1="%s" y1="%s" x2="%s" y2="%s" stroke-opacity=".5"/>'
              % (f(lx + 13 * math.cos(ang)), f(ly + 13 * math.sin(ang)),
                 f(lx + 19 * math.cos(ang)), f(ly + 19 * math.sin(ang))))
    scx, scy, sr = vx + vw - 70, vy + vh - 60, 40
    o += '<circle class="ln" cx="%d" cy="%d" r="%d"/>' % (scx, scy, sr)
    for k in range(1, 3):
        o += '<ellipse class="ln2" cx="%d" cy="%d" rx="%s" ry="%d" stroke-opacity=".45"/>' % (
            scx, scy, f(sr * math.cos(k * math.pi / 3)), sr)
    o += '<ellipse class="ln2" cx="%d" cy="%d" rx="46" ry="10" stroke-opacity=".3"/>\n' % (
        scx, scy + sr + 8)
    o += ('<text x="%d" y="%d" fill="rgba(255,255,255,.4)" font-size="9" '
          'font-family="monospace" letter-spacing="1.5">RENDER 01</text>\n' % (vx + 6, vy + vh - 8))

    o += ('<path class="dim" d="M96 76 V300 M96 70 H%d M96 300 H%d"/>\n' % (mx - 4, mx - 4))
    for x, y in ((190, 70), (150, 300), (scx, scy)):
        o += node(x, y, 2.6)
    o += scanline(a, 50)
    return o + TAIL


# DK-2026-08-06-01 NOT: otomotiv() ve havacilik() fonksiyonlari, canlidaki assets/img/sektor/
# otomotiv.svg ve havacilik.svg'den geride kalmis (baska bir oturumda elle/farkli bir
# betikle "aerodinamik akis", "roll" lastik donusu gibi detaylar eklenmis, buradaki kod
# guncellenmemis). __main__ blogunu oldugu gibi calistirmak bu 2 dosyayi ESKI icerikle
# ezer -- oncesinde `git diff assets/img/sektor/` ile kontrol edin, gerekirse
# `git checkout -- assets/img/sektor/otomotiv.svg assets/img/sektor/havacilik.svg`.
BUILDERS = {
    "mimari": mimari,
    "insaat": insaat,
    "makine": makine,
    "otomotiv": otomotiv,
    "medya": medya,
    "egitim": egitim,
    "havacilik": havacilik,
    "tesisat": tesisat,
    "icmimarlik": icmimarlik,
    "yapiurunleri": yapiurunleri,
    "tuketici": tuketici,
}

if __name__ == "__main__":
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    for key, fn in BUILDERS.items():
        path = os.path.join(OUT, "%s.svg" % key)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(apply_offset(key, fn()))
        print("%-12s %6d bytes" % (key, os.path.getsize(path)))
