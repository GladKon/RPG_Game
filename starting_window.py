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
    while running == 'start_window':
        for event in pg.event.get():
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


def button_start_window_menu():
    return 'menu'


def button_start_window_registration():
    return 'registration'


def registration(self, running):
    login_input = InputField(360, 100, 300, 50)
    password_input = InputField(360, 200, 300, 50)
    password_input2 = InputField(360, 300, 300, 50)
    name = font.render('Введите никмейм', True, (0, 10, 0))
    password = font.render('Введите пароль', True, (0, 10, 0))
    password2 = font.render('Подтвертите пароль', True, (0, 10, 0))
    while running != 'menu':
        for event in pg.event.get():
            login_input.handle_event(event)
            password_input.handle_event(event)
            password_input2.handle_event(event)
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 360 < mouse_pos[0] < 660 and 500 < mouse_pos[1] < 550:
                    running = button_registration(login_input.text, password_input.text, password_input2.text)

        self.screen.fill((0, 250, 100))
        self.screen.blit(name, (100, 100))
        self.screen.blit(password, (100, 200))
        self.screen.blit(password2, (100, 300))
        create_button('Зарегистрироваться', 360, 500, 300, 50, self)
        login_input.draw(self.screen)
        password_input.draw(self.screen)
        password_input2.draw(self.screen)
        self.clock.tick(60)
        pg.display.update()
    return running


def button_registration(login_input, password_input, password_input2):
    if password_input == password_input2:
        d = {'name': login_input, 'password': password_input}
        data = requests.post('http://127.0.0.1:5000/registration', data=d)
        print(data.text)
        return_data = json.loads(data.text)
        if return_data == {'response': 'create', 'status': 201}:
            return 'menu'



def menu(self, running):
    while running == 'menu':
        for event in pg.event.get():
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
    return 'game'


def button_menu_exit():
    return 'exit'
