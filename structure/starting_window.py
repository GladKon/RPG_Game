import pygame as pg
import requests
import json
import socket

from RPG_Game.helpers.Booton_class import Button
from RPG_Game.helpers.input_class import InputField


pg.init()

font = pg.font.Font(None, 36)


def create_button(text: str, x, y, w, h, self):
    mouse = pg.mouse.get_pos()

    pg.draw.rect(self.screen, (50, 150, 200), (x, y, w, h))

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(self.screen, (50, 200, 255), (x, y, w, h))

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=((x + w / 2), (y + h / 2)))
    self.screen.blit(text_surface, text_rect)


def start_window(self):
    b1 = Button('Войти', 430, 200, 100, 50)
    b2 = Button('Зарегистрироваться', 360, 300, 300, 50)

    while self.state == 'START_WINDOW':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
            elif b1.handle_event(event):
                self.state = 'INPUT'
                break
            elif b2.handle_event(event):
                self.state = 'REGISTRATION'
                break



        self.screen.fill((0, 250, 0))
        self.clock.tick(60)

        b1.draw(self.screen)
        b2.draw(self.screen)

        pg.display.update()






def registration(self):
        b1 = Button('Зарегистрироваться', 340, 400, 300, 50)
        b2 = Button('Назад', 420, 500, 100, 50)

        login_input = InputField(360, 100, 200, 50)
        password_input = InputField(360, 200, 200, 50)
        password_input2 = InputField(360, 300, 200, 50)

        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        password2 = font.render('Подтвертите пароль', True, (0, 10, 0))
        name_error = font.render('Существующее имя', True, (255, 0, 0))
        password_error = font.render('Разные пароли', True, (255, 0, 0))

        running = None
        while self.state == 'REGISTRATION':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                     runnig = button_registration(login_input.text, password_input.text, password_input2.text)
                     if runnig == 'MENU':
                        self.state = 'MENU'
                        break

                elif b2.handle_event(event):
                    self.state = 'START_WINDOW'
                    break
                login_input.handle_event(event)
                password_input.handle_event(event)
                password_input2.handle_event(event)


            self.screen.fill((0, 250, 100))
            self.screen.blit(name, (100, 100))

            if running == 'name_error':
                self.screen.blit(name_error, (600, 110))
            if running == 'password_error':
                self.screen.blit(password_error, (600, 250))

            self.screen.blit(password, (100, 200))
            self.screen.blit(password2, (100, 300))

            b1.draw(self.screen)
            b2.draw(self.screen)
            login_input.draw(self.screen)
            password_input.draw(self.screen)
            password_input2.draw(self.screen)

            self.clock.tick(60)
            pg.display.update()



def button_registration(login_input, password_input, password_input2):
    if password_input == password_input2:
        d = {'name': login_input, 'password': password_input}
        data = requests.post('http://127.0.0.1:5000/registration', data=d)

        return_data = json.loads(data.text)
        if return_data == {'response': 'create', 'status': 201}:
            return 'MENU'
        else:
            return 'name_error'
    else:
        return 'password_error'





def window_input(self):
        b1 = Button('Войти', 420, 400, 100, 50)
        b2 = Button('Назад', 420, 500, 100, 50)
        login_input = InputField(360, 100, 200, 50)
        password_input = InputField(360, 200, 200, 50)

        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        error = font.render('Неверное имя или пароль!', True, (255, 0, 0))
        running = None

        while self.state == 'INPUT':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    running = button_input(login_input.text, password_input.text)
                    if running == 'MENU':
                        self.state = 'MENU'
                        break
                elif b2.handle_event(event):
                    self.state = 'START_WINDOW'
                    break
                login_input.handle_event(event)
                password_input.handle_event(event)




            self.screen.fill((0, 250, 100))
            self.screen.blit(name, (100, 100))

            if running == 'error':
                self.screen.blit(error, (570, 150))

            self.screen.blit(password, (100, 200))

            b1.draw(self.screen)
            b2.draw(self.screen)
            login_input.draw(self.screen)
            password_input.draw(self.screen)

            self.clock.tick(60)
            pg.display.update()



def button_input(login, password):
    d = {'name': login, 'password': password}
    data = requests.post('http://127.0.0.1:5000/input', data=d)
    return_data = json.loads(data.text)
    if return_data == {'response': 'input', 'status': 200}:
        return 'MENU'
    else:
        return 'error'





def menu(self):
    b1 = Button('Играть', 430, 200, 100, 50)
    b2 = Button('Настройки', 400, 300, 160, 50)
    b3 = Button('Выход', 430, 400, 100, 50)

    while self.state == 'MENU':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
                break
            elif b1.handle_event(event):
                self.state = 'ROOM'
                break
            elif b3.handle_event(event):
                self.state = 'EXIT'
                break

        self.screen.fill((0, 250, 0))

        b1.draw(self.screen)
        b2.draw(self.screen)
        b3.draw(self.screen)

        self.clock.tick(60)
        pg.display.update()






def room(self):
    b1 = Button('Создать комнату', 400, 200, 220, 50)
    b2 = Button('Войти в комнату', 400, 300, 220, 50)
    b3 = Button('Назад', 430, 400, 100, 50)
    while self.state == 'ROOM':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
                break
            elif b1.handle_event(event):
                self.state = 'CREATE_ROOM'
                break
            elif b2.handle_event(event):
                self.state = 'INPUT_ROOM'
                break
            elif b3.handle_event(event):
                self.state = 'MENU'
                break

        self.screen.fill((0, 250, 0))

        b1.draw(self.screen)
        b2.draw(self.screen)
        b3.draw(self.screen)

        self.clock.tick(60)
        pg.display.update()




def input_room(self):
    b1 = Button('Назад', 430, 400, 100, 50)
    b2 = Button('Войти',430, 350, 100, 50)
    name_room = InputField(360, 100, 200, 50)
    password_room = InputField(360, 200, 200, 50)

    name = font.render('Введите название комнаты', True, (0, 10, 0))
    password = font.render('Введите пароль от комнаты', True, (0, 10, 0))

    while self.state == 'INPUT_ROOM':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
                break
            elif b1.handle_event(event):
                self.state = 'MENU'
                break
            elif b2.handle_event(event):
                self.state = inpit_room(name_room.text,password_room.text)
                break
            name_room.handle_event(event)
            password_room.handle_event(event)

        self.screen.fill((0, 250, 0))
        self.screen.blit(name, (100, 100))
        self.screen.blit(password, (200, 100))

        b1.draw(self.screen)
        b2.draw(self.screen)
        name_room.draw(self.screen)
        password_room.draw(self.screen)


        self.clock.tick(60)
        pg.display.update()


def inpit_room(name,password):
    d = {'name': name, 'password': password}
    data = requests.post('http://127.0.0.1:5000/input_room', data=d)
    return 'GAME_ROOM' if data.status_code == 200 else 'INPUT_ROOM'



def create_room(self):
    b1 = Button('Создать', 430, 350, 100, 50)
    b2 = Button('Назад', 430, 450, 100, 50)

    room_name = InputField(410, 90, 200, 50)
    room_password = InputField(410, 190, 200, 50)
    room_max_player = InputField(470, 290, 50, 50)

    name_room = font.render('Введите имя комнаты', True, (0, 10, 0))
    text_password = font.render('Введите пароль комнаты', True, (0, 10, 0))
    text_max_player = font.render('Максимальное число игроков', True, (0, 10, 0))

    while self.state == 'CREATE_ROOM':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
                break
            elif b1.handle_event(event):
                self.state = button_create_room(room_name.text, room_password.text, room_max_player.text)
            elif b2.handle_event(event):
                self.state = 'ROOM'
            room_name.handle_event(event)
            room_password.handle_event(event)
            room_max_player.handle_event(event)


        self.screen.fill((0, 250, 0))
        self.screen.blit(name_room, (100, 100))
        self.screen.blit(text_password, (100, 200))
        self.screen.blit(text_max_player, (100, 300))

        b1.draw(self.screen)
        b2.draw(self.screen)
        room_name.draw(self.screen)
        room_max_player.draw(self.screen)
        room_password.draw(self.screen)

        self.clock.tick(60)
        pg.display.update()




def button_create_room(name, password, max_player = 15):
    d = {'name': name, 'password': password, 'limited': max_player}
    data = requests.post('http://127.0.0.1:5000/create_room', data=d)
    return 'GAME_ROOM' if data.status_code == 201 else 'CREATE_ROOM'

def game_room(self):
    b1 = Button('Назад', 430, 400, 100, 50)
    while self.state == 'GAME_ROOM':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = 'EXIT'
            elif b1.handle_event(event):
                self.state = 'ROOM'

            self.screen.fill((0, 250, 0))

            b1.draw(self.screen)

            self.clock.tick(60)
            pg.display.update()


