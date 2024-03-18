import pygame as pg

from RPG_Game.helpers.helper import SpriteHelper
from pygame.math import Vector2
from RPG_Game.structure.Settings import Sloy_player

class User_game(pg.sprite.Sprite):
    speed = 3

    def __init__(self, game, path, pos):
        self._layer = Sloy_player
        super().__init__(game.all_sprite)
        self.name = ''
        # self.sprite_sheet = SpriteHelper(path)
        # self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
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
        pass
        # self._Animation()

    def change_direction(self, d):
        self.direction = d
        self._Animation()


    def _Animation(self, frame_len=100):

        now = pg.time.get_ticks()

        if now - self.last_update > frame_len // self.Sprint:

            if self.direction == 'u':
                self.aimation = self.sprite_W
            elif self.direction == 'd':
                self.aimation = self.sprite_S
            elif self.direction == 'l':
                self.aimation = self.sprite_A
            elif self.direction == 'r':
                self.aimation = self.sprite_D
            else:
                self.aimation = self.sprite_S

            self.image = self.aimation[self.animate]


            self.animate += 1
            if self.animate == 4:
                self.animate = 0

            self.last_update = now

