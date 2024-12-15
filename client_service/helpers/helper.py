import pygame as pg


class SpriteHelper:
    def __init__(self, path, scale = 1):
        self.sheet = pg.image.load(path).convert_alpha()
        w, h = self.sheet.get_size()
        target_size = (int(w * scale), int(h * scale))
        self.sheet = pg.transform.scale(self.sheet, target_size)
        self.w, self.h = self.sheet.get_size()

    def get_image(self, x, y, w, h):
        return self.sheet.subsurface(x, y, w, h)


def password_hard(password):
    bukva = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
             'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    simvol = ['!', '@', '<', '>', '.', '/', '?', ',', ';', ':', '|', '[', ']', '{', '}', '-', '_', '=', '*', '+']

    if len(password) >= 10:
        for i in password:
            if i in bukva:
                for i in password:
                    if i in simvol:
                        return 'True'
                return 'password_simvol'
        return 'password_alfavit'
    else:
        return 'password_short'
