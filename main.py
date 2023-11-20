import pygame as pg
import socket
import threading
import json

from Settings import *
from player import Player
from users import User
from helper import res
from map import TileMap, Camera
from starting_window import window1, window2, window3


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Win_x, Win_y))
        pg.display.set_caption(Title)
        pg.display.set_icon(pg.image.load(res / 'Images' / 'frog.png'))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("127.0.0.1", 19450))
        self.number = self.client.recv(1024).decode('utf-8')
        self.users = {}
        self.clock = pg.time.Clock()
        self.life = True

    def new(self):
        self.all_sprite = pg.sprite.LayeredUpdates()

        self.player = Player(self, res / 'Images' / 'player_sheet.png', (100, 100), self.client)
        self.map = TileMap(self, res / 'Map' / 'Png.png', res / 'Map' / 'Карта.csv', 16)

        self.camera = Camera()

    def _resive_soct(self):
        while self.life:
            data = self.client.recv(1024)
            data = json.loads(data.decode('utf-8'))
            if data['N'] not in self.users:
                self.users[data['N']] = User(self, res / 'Images' / 'player_sheet.png', (data['x'], data['y']))
            else:
                x_old, y_old = self.users[data['N']].rect.center
                x_new, y_new = (data['x'], data['y'])
                direction = None
                if x_new < x_old:
                    direction = 'l'
                elif x_new > x_old:
                    direction = 'r'
                elif y_new < y_old:
                    direction = 'u'
                elif y_new > y_old:
                    direction = 'd'
                self.users[data['N']].change_direction(direction)
                self.users[data['N']].rect.center = (data['x'], data['y'])

    def _event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.life = False
            if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
                self.player.Sprint = 1.5
            if event.type == pg.KEYUP and event.key == pg.K_LSHIFT:
                self.player.Sprint = 1

    def start_window(self):
        geme = True
        resultat = 0
        while geme:

            if resultat == 0:
                resultat = window1(self)

            elif resultat == 2:
                resultat = window2(self)

            elif resultat == 1:
                resultat = window3(self)
                if resultat == 3:
                    geme = False
                elif resultat == 5:
                    self.life = False
                    geme = False

    def _update(self):
        self.all_sprite.update()
        self.camera.update(self.player)

    def _draw(self):
        self.screen.fill(Win_RGB)

        for sprite in self.all_sprite:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pg.display.flip()

    def run(self):
        tread = threading.Thread(target=self._resive_soct)
        tread.start()
        while self.life:
            self._event()
            self._draw()
            self._update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.start_window()
    game.new()
    game.run()

# Hello
