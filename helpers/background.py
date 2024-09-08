import pygame as pg

from structure.path import path_to_image_background
from structure.settings import Win_x, Win_y


class BackGround:
    def __init__(self):
        self.image_1 = pg.image.load(
            path_to_image_background / 'background_1.png').convert_alpha()
        self.image_1 = pg.transform.scale(self.image_1, (Win_x, Win_y))
        self.image_1.set_alpha(255)

        self.image_2 = pg.image.load(
            path_to_image_background / 'background_2.png').convert_alpha()
        self.image_2 = pg.transform.scale(self.image_2, (Win_x, Win_y))
        self.image_2.set_alpha(0)

        self.image_3 = pg.image.load(
            path_to_image_background / 'background_3.png').convert_alpha()
        self.image_3 = pg.transform.scale(self.image_3, (Win_x, Win_y))
        self.image_3.set_alpha(0)

        self.image_4 = pg.image.load(
            path_to_image_background / 'background_4.png').convert_alpha()
        self.image_4 = pg.transform.scale(self.image_4, (Win_x, Win_y))
        self.image_4.set_alpha(0)

        self.sl_image = [self.image_1, self.image_2, self.image_3, self.image_4]

        self.alpha_level_1 = 255
        self.alpha_level_2 = 0
        self.alpha_level_3 = 0
        self.alpha_level_4 = 0

        self.sl_alpha_level = [self.alpha_level_1, self.alpha_level_2, self.alpha_level_3, self.alpha_level_4]

        self.count = 1


    def change_alpha(self):


        if self.count != len(self.sl_alpha_level):

            if self.sl_alpha_level[self.count-1] == 0:

                self.count += 1

            else:

                self.sl_image[self.count-1].set_alpha(self.sl_alpha_level[self.count-1])
                self.sl_alpha_level[self.count-1] -= 1

                self.sl_image[self.count].set_alpha(self.sl_alpha_level[self.count])
                self.sl_alpha_level[self.count] += 1

        elif self.count == len(self.sl_alpha_level):

            self.sl_image[self.count - 1].set_alpha(self.sl_alpha_level[self.count - 1])
            self.sl_alpha_level[self.count - 1] -= 1

            self.sl_image[0].set_alpha(self.sl_alpha_level[0])
            self.sl_alpha_level[0] += 1


            if self.sl_alpha_level[0] == 255:
                self.count = 1








