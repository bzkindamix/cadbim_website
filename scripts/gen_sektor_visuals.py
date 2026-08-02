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
