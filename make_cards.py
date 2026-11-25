#!/usr/bin/env python3
"""Render the gallery cards for the README (build-time tool only).

The grader runs main.py alone; this script just draws the two PNG
cards shown in the README gallery: the winning count and the
finalists it beat in the tournament. Uses Pillow, which is present
on the build machine but is NOT needed by the entry itself.
"""

from PIL import Image, ImageDraw, ImageFont

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

BG = (24, 26, 34)
PANEL = (35, 39, 51)
GOLD = (240, 185, 60)
TEXT = (235, 238, 245)
MUTED = (160, 168, 185)


def font(path, size):
    return ImageFont.truetype(path, size)


def winner_card():
    img = Image.new("RGB", (900, 520), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([30, 30, 870, 490], radius=28, fill=PANEL,
                        outline=GOLD, width=4)
    d.text((450, 78), "THE HONEST COUNT", font=font(SANS_BOLD, 34),
           fill=MUTED, anchor="ma")
    d.text((450, 140), "347", font=font(MONO, 190), fill=GOLD, anchor="ma")
    d.text((450, 360), "open browser tabs — counted, not rounded",
           font=font(SANS, 30), fill=TEXT, anchor="ma")
    d.text((450, 408), "prime · oddly exact · deep in hoarder territory",
           font=font(SANS, 26), fill=MUTED, anchor="ma")
    img.save("card-winner.png")


def finalists_card():
    rows = [
        ("317", "runner-up — prime, deep hoard, oddly exact (19/20)"),
        ("412", "semifinalist — past 400, still human (19/20)"),
        ("289", "finalist — the stranger count, fully believable (18/20)"),
        ("213", "semifinalist — 'read it later' x213 (18/20)"),
        ("1", "quarterfinalist — one tab, fierce discipline (18/20)"),
    ]
    img = Image.new("RGB", (900, 520), BG)
    d = ImageDraw.Draw(img)
    d.text((60, 42), "THE FINALISTS 347 OUTLASTED", font=font(SANS_BOLD, 32),
           fill=TEXT)
    y = 110
    for number, note in rows:
        d.rounded_rectangle([50, y, 850, y + 68], radius=14, fill=PANEL)
        d.text((80, y + 34), number, font=font(MONO, 38), fill=GOLD,
               anchor="lm")
        d.text((225, y + 34), note, font=font(SANS, 22), fill=TEXT,
               anchor="lm")
        y += 82
    img.save("card-finalists.png")


if __name__ == "__main__":
    winner_card()
    finalists_card()
    print("cards written")
