import pygame as pg
import socket
import threading
import json

from RPG_Game.structure.Settings import *
from RPG_Game.helpers.player import Player
from RPG_Game.helpers.users import User
from RPG_Game.helpers.helper import res
from RPG_Game.structure.map import TileMap, Camera
from RPG_Game.structure.starting_window import start_window, registration, menu, window_input, room, input_room,create_room, game_room


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Win_x, Win_y))
        pg.display.set_caption(Title)
        pg.display.set_icon(pg.image.load(res / 'Images' / 'frog.png'))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.connect(("127.0.0.1", 19450))
        # self.number = self.client.recv(1024).decode('utf-8')
        self.users = {}
        self.clock = pg.time.Clock()
        self.life = True
        self.state = 'START_WINDOW'

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
        while self.state != 'EXIT':
            match self.state:
                case 'START_WINDOW':
                    start_window(self)
                case 'INPUT':
                    window_input(self)
                case 'REGISTRATION':
                    registration(self)
                case 'MENU':
                    menu(self)
                case 'ROOM':
                    room(self)
                case 'INPUT_ROOM':
                    input_room(self)
                case 'CREATE_ROOM':
                    create_room(self)
                case 'GAME_ROOM':
                    game_room(self)




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


