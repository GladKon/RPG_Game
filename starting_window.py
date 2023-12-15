import pygame as pg
import sys
import requests
import json

from input_class import InputField

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


def start_window(self, running):
    if running == 'start_window':
        while running == 'start_window':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = 'exit'
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    if 430 < mouse_pos[0] < 530 and 200 < mouse_pos[1] < 250:
                        running = button_start_window_menu()
                    if 360 < mouse_pos[0] < 660 and 300 < mouse_pos[1] < 350:
                        running = button_start_window_registration()

            self.screen.fill((0, 250, 0))

            self.clock.tick(60)

            create_button('Войти', 430, 200, 100, 50, self)
            create_button('Зарегистрироваться', 360, 300, 300, 50, self)
            pg.display.update()
        return running
    else:
        return running


def button_start_window_menu():
    return 'input'


def button_start_window_registration():
    return 'registration'


def registration(self, running):
    if running == 'registration':
        login_input = InputField(360, 100, 200, 50)
        password_input = InputField(360, 200, 200, 50)
        password_input2 = InputField(360, 300, 200, 50)
        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        password2 = font.render('Подтвертите пароль', True, (0, 10, 0))
        name_error = font.render('Существующее имя', True, (255, 0, 0))
        password_error = font.render('Разные пароли', True, (255, 0, 0))
        while running != 'menu' and running != 'start_window' and running != 'exit':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = 'exit'
                login_input.handle_event(event)
                password_input.handle_event(event)
                password_input2.handle_event(event)
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    if 340 < mouse_pos[0] < 640 and 400 < mouse_pos[1] < 450:
                        running = button_registration(login_input.text, password_input.text, password_input2.text)
                    if 420 < mouse_pos[0] < 520 and 500 < mouse_pos[1] < 550:
                        running = button_registration_back()

            self.screen.fill((0, 250, 100))
            self.screen.blit(name, (100, 100))
            if running == 'name_error':
                self.screen.blit(name_error, (600, 110))
            if running == 'password_error':
                self.screen.blit(password_error, (600, 250))

            self.screen.blit(password, (100, 200))
            self.screen.blit(password2, (100, 300))
            create_button('Зарегистрироваться', 340, 400, 300, 50, self)
            create_button('Назад', 420, 500, 100, 50, self)
            login_input.draw(self.screen)
            password_input.draw(self.screen)
            password_input2.draw(self.screen)
            self.clock.tick(60)
            pg.display.update()
        return running
    else:
        return running


def button_registration(login_input, password_input, password_input2):
    if password_input == password_input2:
        d = {'name': login_input, 'password': password_input}
        data = requests.post('http://127.0.0.1:5000/registration', data=d)

        return_data = json.loads(data.text)
        if return_data == {'response': 'create', 'status': 201}:
            return 'menu'
        else:
            return 'name_error'
    else:
        return 'password_error'


def button_registration_back():
    return 'start_window'


def window_input(self, running):
    if running == 'input':
        login_input = InputField(360, 100, 200, 50)
        password_input = InputField(360, 200, 200, 50)
        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        error = font.render('Неверное имя или пароль!', True, (255, 0, 0))

        while running != 'menu' and running != 'start_window' and running != 'exit':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = 'exit'
                login_input.handle_event(event)
                password_input.handle_event(event)

                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    if 420 < mouse_pos[0] < 520 and 400 < mouse_pos[1] < 450:
                        running = button_input(login_input.text, password_input.text)
                    if 420 < mouse_pos[0] < 520 and 500 < mouse_pos[1] < 550:
                        running = button_input_back()
                        print(running)


            self.screen.fill((0, 250, 100))
            self.screen.blit(name, (100, 100))
            if running == 'error':
                self.screen.blit(error, (570, 150))

            self.screen.blit(password, (100, 200))

            create_button('Войти', 420, 400, 100, 50, self)
            create_button('Назад', 420, 500, 100, 50, self)
            login_input.draw(self.screen)
            password_input.draw(self.screen)
            self.clock.tick(60)
            pg.display.update()
        return running
    else:
        return running


def button_input(login, password):
    d = {'name': login, 'password': password}
    data = requests.post('http://127.0.0.1:5000/input', data=d)
    return_data = json.loads(data.text)
    if return_data == {'response': 'input', 'status': 200}:
        return 'menu'
    else:
        return 'error'


def button_input_back():
    return 'start_window'


def menu(self, running):
    while running == 'menu':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = 'exit'
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 200 < mouse_pos[1] < 250:
                    running = button_menu_game()
                elif 430 < mouse_pos[0] < 530 and 400 < mouse_pos[1] < 450:
                    running = button_menu_exit()

        self.screen.fill((0, 250, 0))

        self.clock.tick(60)

        create_button('Играть', 430, 200, 100, 50, self)
        create_button('Настройки', 400, 300, 160, 50, self)
        create_button('Выход', 430, 400, 100, 50, self)
        pg.display.update()
    return running


def button_menu_game():
    return 'room'


def button_menu_exit():
    return 'exit'


def room(self, running):
    while running == 'room':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = 'exit'
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 200 < mouse_pos[1] < 250:
                    running = button_room_creat()
                elif 430 < mouse_pos[0] < 530 and 300 < mouse_pos[1] < 350:
                    running = button_room_input()
                elif 430 < mouse_pos[0] < 530 and 400 < mouse_pos[1] < 450:
                    running = button_room_back()

        self.screen.fill((0, 250, 0))

        self.clock.tick(60)

        create_button('Создать комнату', 400, 200, 220, 50, self)
        create_button('Войти в комнату', 400, 300, 220, 50, self)
        create_button('Назад', 430, 400, 100, 50, self)
        pg.display.update()
    return running


def button_room_creat():
    return 'create_room'


def button_room_input():
    return 'input_room'


def button_room_back():
    return 'menu'


def input_room(self, running):
    while running == 'input_room':
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = 'exit'
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 400 < mouse_pos[1] < 450:
                    running = button_input_room_back()

        self.screen.fill((0, 250, 0))

        self.clock.tick(60)

        create_button('Назад', 430, 400, 100, 50, self)
        pg.display.update()
    return running


def button_input_room_back():
    return 'room'


def create_room(self, running):
    room_name = InputField(410, 90, 200, 50)
    room_password = InputField(410, 190, 200, 50)
    room_max_player = InputField(470, 290, 50, 50)
    name_room = font.render('Введите имя комнаты', True, (0, 10, 0))
    text_password = font.render('Введите пароль комнаты', True, (0, 10, 0))
    text_max_player = font.render('Максимальное число игроков', True, (0, 10, 0))
    while running == 'create_room':
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = 'exit'
            room_name.handle_event(event)
            room_password.handle_event(event)
            room_max_player.handle_event(event)
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 350 < mouse_pos[1] < 400:
                    running = button_create_room(room_name.text, room_password.text, room_max_player.text)
                elif 430 < mouse_pos[0] < 530 and 450 < mouse_pos[1] < 500:
                    running = button_create_room_back()

        self.screen.fill((0, 250, 0))
        self.screen.blit(name_room, (100, 100))
        self.screen.blit(text_password, (100, 200))
        self.screen.blit(text_max_player, (100, 300))
        room_name.draw(self.screen)
        room_max_player.draw(self.screen)
        room_password.draw(self.screen)
        self.clock.tick(60)
        create_button('Создать', 430, 350, 100, 50, self)
        create_button('Назад', 430, 450, 100, 50, self)
        pg.display.update()
    return running


def button_create_room_back():
    return 'room'


def button_create_room(name, password, max_player = 15):
    d = {'name': name, 'password': password, 'limited': max_player}
    data = requests.post('http://127.0.0.1:5000/create_room', data=d)

    return_data = json.loads(data.text)
    print(return_data)
    if return_data == {'response': 'create', 'status': 201}:
        return 'game_room'

def game_room(self, running):
    while running == 'game_room':
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = 'exit'
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 400 < mouse_pos[1] < 450:
                    running = button_game_room_back()
            self.screen.fill((0, 250, 0))
            self.clock.tick(60)
            create_button('Назад', 430, 400, 100, 50, self)
            pg.display.update()

def button_game_room_back():
    return 'room'