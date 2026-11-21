#!/usr/bin/env python3
"""Deterministic newspaper front page for Saturday 21 November 2026."""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (28, 28, 28)
RED = (150, 30, 30)
BLUE = (30, 50, 90)
GREY = (130, 130, 130)
PANEL_BG = (252, 249, 241)
PANEL_EDGE = (205, 199, 182)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, f, maxw):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, label, headline, summary, ill):
    draw.rectangle([x, y, x + w, y + h], fill=PANEL_BG, outline=PANEL_EDGE, width=2)
    draw.text((x + 14, y + 10), label, font=font(FB, 18), fill=RED)
    hf = font(FB, 30)
    ty = y + 42
    for ln in wrap(draw, headline, hf, w - 28):
        draw.text((x + 14, ty), ln, font=hf, fill=BLUE)
        ty += 36
    sf = font(FR, 20)
    ty += 4
    for ln in wrap(draw, summary, sf, w - 28)[:2]:
        draw.text((x + 14, ty), ln, font=sf, fill=INK)
        ty += 26
    ill(draw, x, y, w, h, ty + 4)


def ill_poland(draw, x, y, w, h, iy):
    ix = x + 14
    iw = w - 28
    ih = (y + h - 10) - iy
    by = iy + ih * 0.55
    dash = 14
    cx = ix
    while cx < ix + iw:
        draw.line([cx, by, min(cx + dash, ix + iw), by], fill=INK, width=3)
        cx += dash * 2
    px = ix + iw * 0.22
    py = by - 18
    draw.ellipse([px - 10, py - 10, px + 10, py + 10], fill=RED, outline=INK, width=2)
    draw.polygon([(px - 6, py + 6), (px + 6, py + 6), (px, py + 26)], fill=RED, outline=INK)
    for k in range(3):
        sx = ix + iw * (0.45 + k * 0.16)
        ex = ix + iw * (0.52 + k * 0.16)
        ey = by - 2
        draw.line([sx, iy + 6, ex, ey], fill=INK, width=3)
        ang = math.atan2(ey - (iy + 6), ex - sx)
        for da in (0.5, -0.5):
            ax = ex - 9 * math.cos(ang + da)
            ay = ey - 9 * math.sin(ang + da)
            draw.line([ex, ey, ax, ay], fill=INK, width=3)


def ill_market(draw, x, y, w, h, iy):
    ix = x + 14
    iw = w - 28
    ih = (y + h - 10) - iy
    bx = ix + 8
    bw = iw - 78
    by = iy + ih - 8
    bh = ih - 16
    draw.line([bx, by, bx, by - bh], fill=GREY, width=2)
    draw.line([bx, by, bx + bw, by], fill=GREY, width=2)
    pts = []
    n = 7
    for i in range(n):
        px = bx + bw * i / (n - 1)
        # Steep fall: high on the left, low on the right.
        py = by - bh * (0.85 - 0.12 * i + 0.04 * (i % 2))
        pts.append((px, py))
    draw.line(pts, fill=INK, width=4)
    ex, ey = pts[-1]
    # Red down arrow at the low end (bottom right), pointing down.
    draw.polygon([(ex, ey + 12), (ex - 8, ey - 4), (ex + 8, ey - 4)], fill=RED)
    draw.text((ex + 10, ey - 9), "DOWN", font=font(FB, 18), fill=RED)


def ill_icj(draw, x, y, w, h, iy):
    ix = x + 14
    iw = w - 28
    ih = (y + h - 10) - iy
    cx = ix + iw * 0.42
    top = iy + 8
    bot = iy + ih - 10
    draw.line([cx, top, cx, bot], fill=INK, width=4)
    draw.line([cx - 46, top, cx + 46, top], fill=INK, width=4)
    for s in (-1, 1):
        draw.line([cx + s * 46, top, cx + s * 22, top + 22], fill=INK, width=3)
        draw.line([cx + s * 22, top + 22, cx + s * 22, top + 52], fill=INK, width=3)
        draw.arc([cx + s * 22 - 16, top + 52, cx + s * 22 + 16, top + 84], 0, 360, fill=INK, width=3)
    # gavel on right: short rectangular head + straight handle
    gx = ix + iw * 0.78
    draw.rectangle([gx - 3, bot - 32, gx + 3, bot - 2], fill=INK)
    draw.rectangle([gx - 18, bot - 44, gx + 18, bot - 32], fill=INK)


def ill_eu(draw, x, y, w, h, iy):
    ix = x + 14
    iw = w - 28
    ih = (y + h - 10) - iy
    fw = iw * 0.30
    fh = ih * 0.72
    fy = iy + (ih - fh) / 2
    # Union Jack
    ux = ix + iw * 0.16
    draw.rectangle([ux, fy, ux + fw, fy + fh], fill=(10, 40, 120))
    draw.line([ux, fy, ux + fw, fy + fh], fill=(255, 255, 255), width=4)
    draw.line([ux + fw, fy, ux, fy + fh], fill=(255, 255, 255), width=4)
    draw.line([ux + fw / 2, fy, ux + fw / 2, fy + fh], fill=(255, 255, 255), width=4)
    draw.line([ux, fy + fh / 2, ux + fw, fy + fh / 2], fill=(255, 255, 255), width=4)
    draw.line([ux, fy, ux + fw, fy + fh], fill=(200, 20, 30), width=2)
    draw.line([ux + fw, fy, ux, fy + fh], fill=(200, 20, 30), width=2)
    # EU flag
    ex = ix + iw * 0.54
    draw.rectangle([ex, fy, ex + fw, fy + fh], fill=(0, 51, 153))
    ccx = ex + fw / 2
    ccy = fy + fh / 2
    r = fh * 0.30
    for i in range(12):
        a = math.radians(i * 30 - 90)
        sx = ccx + r * math.cos(a)
        sy = ccy + r * math.sin(a)
        draw.polygon([(sx, sy - 4), (sx + 3, sy + 3), (sx - 3, sy + 3)], fill=(255, 204, 0))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead
    title = "THE WORLD IN ONE PICTURE"
    tf = font(FB, 58)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 40), title, font=tf, fill=INK)
    dl = "SATURDAY, 21 NOVEMBER 2026"
    df = font(FB, 26)
    dw = draw.textlength(dl, font=df)
    draw.text(((W - dw) / 2, 118), dl, font=df, fill=INK)
    draw.line([36, 158, W - 36, 158], fill=RED, width=4)

    # Panels
    margin = 36
    gap = 20
    cw = (W - 2 * margin - gap) / 2
    ch = 320
    top = 176
    p1 = (margin, top, cw, ch)
    p2 = (margin + cw + gap, top, cw, ch)
    p3 = (margin, top + ch + gap, cw, ch)
    p4 = (margin + cw + gap, top + ch + gap, cw, ch)

    draw_panel(draw, p1[0], p1[1], p1[2], p1[3], "EUROPE",
               "MISSILES HIT POLAND",
               "Two Russian missiles, a drone, hit Poland. Poland: provocation; NATO: grave violation.",
               ill_poland)
    draw_panel(draw, p2[0], p2[1], p2[2], p2[3], "MARKETS",
               "WALL STREET SLUMPS",
               "S&P 500 fell 3.7%, Nasdaq lost 5%+. AI and chip shares led the sell-off.",
               ill_market)
    draw_panel(draw, p3[0], p3[1], p3[2], p3[3], "WORLD COURT",
               "COURT: MYANMAR GENOCIDE",
               "The ICJ ruled Myanmar's forces committed genocide against the Rohingya.",
               ill_icj)
    draw_panel(draw, p4[0], p4[1], p4[2], p4[3], "DIPLOMACY",
               "UK-EU LANDMARK DEALS",
               "Burnham signed three agreements at a Brussels summit on food, carbon and youth.",
               ill_eu)

    # Ticker
    ty0 = top + 2 * ch + gap + 14
    draw.rectangle([margin, ty0, W - margin, H - 30], fill=(240, 234, 220),
                   outline=PANEL_EDGE, width=2)
    draw.text((margin + 12, ty0 + 8), "ALSO", font=font(FB, 18), fill=RED)
    flow = (
        "Trump, Xi and Putin left their Shenzhen summit with few results \u2022 "
        "Cyclone Akvan weakened after crossing Odisha \u2022 "
        "Saudi-led coalition destroyed three Houthi missiles \u2022 "
        "Pancreatic cancer pill daraxonrasib hailed as a breakthrough \u2022 "
        "Iran war nears its ninth month \u2022 "
        "JPMorgan, Visa and Mastercard hit by vendor cyberattacks \u2022 "
        "COP31 climate talks in Turkey in final stage"
    )
    tf2 = font(FR, 18)
    tx = margin + 12
    ty = ty0 + 38
    for ln in wrap(draw, flow, tf2, W - 2 * margin - 24):
        draw.text((tx, ty), ln, font=tf2, fill=INK)
        ty += 21

    img.save("/home/hatch/workspace/makefun/news-image-20261121-entry/entry.png")


if __name__ == "__main__":
    main()
