import pygame as pg
import json

from helpers.helper import SpriteHelper
from pygame.math import Vector2
from structure.settings import Sloy_player


class Player(pg.sprite.Sprite):
    speed = 3

    def __init__(self, game, path, pos, client):
        self.game = game
        self.client = client
        self._layer = Sloy_player
        super().__init__(game.all_sprite)
        sprite_sheet = SpriteHelper(path, scale=2)
        self._load_sprite(sprite_sheet)
        self.image = self.sprite_S[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.v = Vector2(0, 0)
        self.last_update = 0
        self.animate = 0
        self.Sprint = 1



    def _load_sprite(self, sprite_sheet):
        w, h = sprite_sheet.w // 4, sprite_sheet.h // 4

        self.sprite_S = [sprite_sheet.get_image(0, 0, w, h), sprite_sheet.get_image(w, 0, w, h),
                         sprite_sheet.get_image(w * 2, 0, w, h), sprite_sheet.get_image(w * 3, 0, w, h)]
        self.sprite_W = [sprite_sheet.get_image(0, h * 3, w, h), sprite_sheet.get_image(w, h * 3, w, h),
                         sprite_sheet.get_image(w * 2, h * 3, w, h), sprite_sheet.get_image(w * 3, h * 3, w, h)]
        self.sprite_D = [sprite_sheet.get_image(0, h * 2, w, h), sprite_sheet.get_image(w, h * 2, w, h),
                         sprite_sheet.get_image(w * 2, h * 2, w, h), sprite_sheet.get_image(w * 3, h * 2, w, h)]
        self.sprite_A = [sprite_sheet.get_image(0, h, w, h), sprite_sheet.get_image(w, h, w, h),
                         sprite_sheet.get_image(w * 2, h, w, h), sprite_sheet.get_image(w * 3, h, w, h)]

    def update(self):
        self._move()
        self._animation()

    def _move(self):
        self.v.update(0, 0)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.v.y = -1
        if keys[pg.K_s]:
            self.v.y = 1
        if keys[pg.K_d]:
            self.v.x = 1
        if keys[pg.K_a]:
            self.v.x = -1

        # if self.v.length() > 1:
        #     self.v.x = 0

        self.v *= (Player.speed * self.Sprint)
        self.rect.center += self.v
        is_tup = False
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_d] or keys[pg.K_a]:
            is_tup = True
        if is_tup:
            X, Y = self.rect.center
            target = {'x': X, 'y': Y, 'N': self.game.number}
            data = json.dumps(target).encode('utf-8')
            self.client.send(data)

    def _animation(self, frame_len=100):

        now = pg.time.get_ticks()

        if now - self.last_update > frame_len // self.Sprint and self.v.length() > 0:

            if self.v.y < 0:
                self.aimation = self.sprite_W
            if self.v.y > 0:
                self.aimation = self.sprite_S
            if self.v.x < 0:
                self.aimation = self.sprite_A
            if self.v.x > 0:
                self.aimation = self.sprite_D

            self.image = self.aimation[self.animate]

            self.animate += 1
            if self.animate == 4:
                self.animate = 0

            self.last_update = now
