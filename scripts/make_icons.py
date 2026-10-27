"""Generates assets/icon-only.png and assets/splash*.png (run once; CI turns them into Android icons)."""
from PIL import Image, ImageDraw
import os
os.makedirs("assets", exist_ok=True)
BG, FG = (11, 13, 18), (124, 92, 255)

def draw(size, scale):
    im = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(im)
    c, r = size // 2, int(size * scale)
    d.rounded_rectangle((c - r, c - r, c + r, c + r), radius=int(r * .45), fill=FG)
    t = int(r * .55)                                   # play triangle
    d.polygon([(c - t // 2, c - t), (c - t // 2, c + t), (c + t, c)], fill=(255, 255, 255))
    return im

draw(1024, .36).save("assets/icon-only.png")
draw(1024, .36).save("assets/icon-foreground.png")
Image.new("RGB", (1024, 1024), BG).save("assets/icon-background.png")
draw(2732, .10).save("assets/splash.png")
draw(2732, .10).save("assets/splash-dark.png")
