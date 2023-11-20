import pygame as pg
from pathlib import Path

class SpriteHelper:
    def __init__(self, path, scale = 1):
        self.sheet = pg.image.load(path).convert_alpha()
        w, h = self.sheet.get_size()
        target_size = (int(w * scale), int(h * scale))
        self.sheet = pg.transform.scale(self.sheet, target_size)
        self.w, self.h = self.sheet.get_size()

    def get_image(self, x, y, w, h):
        return self.sheet.subsurface(x, y, w, h)

res = Path('res')