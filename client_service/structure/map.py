import csv

import pygame as pg

from structure.settings import *


class TileMap():
    def __init__(self, game, path_png, path_csv, image_size):
        data_list = self._csv_to_list(path_csv)
        png_list = self._png_to_list(path_png, image_size)
        load_tile = self._load_tile(game, data_list, png_list)

    def _csv_to_list(self, path_csv):
        with open(path_csv) as f:
            data = csv.reader(f)
            data = list(data)
            return data

    def _png_to_list(self, path_png, image_size):
        png_list = []
        image = pg.image.load(path_png)

        if image_size != Tile_size:
            scale = Tile_size // image_size
            x, y = image.get_size()
            x *= scale
            y *= scale
            image = pg.transform.scale(image, (x, y))

        w, h = image.get_size()

        for y in range(0, h, Tile_size):
            for x in range(0, w, Tile_size):
                t = image.subsurface(x, y, Tile_size, Tile_size)
                png_list.append(t)

        return png_list

    def _load_tile(self, game, data_list, png_list):
        for i, stroka in enumerate(data_list):
            for j, element in enumerate(stroka):
                Tile(game, png_list[int(element)], j, i)


class Tile(pg.sprite.Sprite):

    def __init__(self, game, image, x, y):
        self._layer = Sloy_ground
        super().__init__(game.all_sprite)

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x * Tile_size
        self.rect.y = y * Tile_size


class Camera():
    def __init__(self):
        self.offset = (0, 0)

    def apply(self, entity):
        return entity.rect.move(self.offset)

    def update(self, target):
        x = -target.rect.x + Win_x // 2
        y = -target.rect.y + Win_y // 2

        x = min(x, 0)
        y = min(y, 0)

        x = max(x, -shirina + Win_x)
        y = max(y, -visota + Win_y)

        self.offset = (x, y)
