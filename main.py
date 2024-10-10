import pygame as pg
import socket
import threading
import json
import time

from helpers.enums import StateOfGame
from helpers.background import BackGround
from structure.settings import *
from helpers.player import Player
from helpers.users import UserGame
from structure.path import res
from structure.map import TileMap, Camera
from structure.windows import Windows



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Win_x, Win_y))
        pg.display.set_caption(Title)
        pg.display.set_icon(pg.image.load(res / 'images' / 'frog.png'))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {}
        self.clock = pg.time.Clock()
        self.life = True
        self.state = StateOfGame.START_WINDOW.name
        self.data = {}
        self.window = Windows()
        self.visual_info = {'CURRENT_IMAGE': BackGround()}

    def new(self):
        self.all_sprite = pg.sprite.LayeredUpdates()
        for u in self.users:
            if u != self.number:
                self.users[u] = UserGame(self, res / 'images' / 'player_sheet_2.png', (self.users[u][0], self.users[u][1]))
            else:

                self.player = Player(self, res / 'images' / 'player_sheet.png', (self.users[u][0], self.users[u][1]), self.client)
        self.map = TileMap(self, res / 'map' / 'Png.png', res / 'map' / 'Карта.csv', 16)
        self.camera = Camera()

    def _contact_with_server(self):
        while self.life:
            data = self.client.recv(1024)
            data = json.loads(data.decode('utf-8'))
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

    def run(self):
        while self.state != StateOfGame.EXIT.name:
            match self.state:
                case StateOfGame.START_WINDOW.name:
                    self.window.start_window(self)
                case 'INPUT':
                    self.window.window_input(self)
                case 'REGISTRATION':
                    self.window.registration(self)
                case 'MENU':
                    self.window.menu(self)
                case 'ROOM':
                    self.window.room(self)
                case 'PLAYER_CHOOSE':
                    self.window.player_choose(self)
                case 'CHOOSING_HERO':
                    self.window.choosing_hero(self)
                case 'TREE_PLAYER':
                    self.window.tree_player(self)
                case 'TREE_PLAYER1':
                    self.window.tree_player1(self)
                case 'INPUT_ROOM':
                    self.window.input_room(self)
                case 'CREATE_ROOM':
                    self.window.create_room(self)
                case 'GAME_ROOM':
                    self.connect_player()
                    self.window.game_room(self)
                case 'GAME':
                    self.new()
                    self.start_game()

    def connect_player(self):
        self.client.connect(('127.0.0.1', 19452))
        self.client.send(json.dumps(self.data).encode('utf-8'))
        self.number = self.client.recv(1024).decode('utf-8')

        t = threading.Thread(target=self.join_the_game, args=())
        t.start()

    def join_the_game(self):
        self.users = json.loads(self.client.recv(1024).decode('utf-8'))
        self.state = "GAME"

    def _update(self):
        self.all_sprite.update()
        self.camera.update(self.player)

    def _draw(self):
        self.screen.fill(Win_RGB)

        for sprite in self.all_sprite:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pg.display.flip()

    def start_game(self):
        tread = threading.Thread(target=self._contact_with_server)
        tread.start()
        while self.life:
            self._event()
            self._draw()
            self._update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
