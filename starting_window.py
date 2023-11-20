import pygame as pg
import sys
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


def window1(self):
    running = 0
    while running == 0:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 200 < mouse_pos[1] < 250:
                    running = button_action_1()
                if 360 < mouse_pos[0] < 660 and 300 < mouse_pos[1] < 350:
                    running = button_action_2()

        self.screen.fill((0, 250, 0))

        self.clock.tick(60)

        create_button('Войти', 430, 200, 100, 50, self)
        create_button('Зарегистрироваться', 360, 300, 300, 50, self)
        pg.display.update()
    return running


def button_action_1():
    return 1


def button_action_2():
    return 2


def window2(self):
    running = 0
    login_input = InputField(360, 300, 300, 50)

    while running == 0:
        for event in pg.event.get():
            login_input.handle_event(event)
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 360 < mouse_pos[0] < 660 and 600 < mouse_pos[1] < 650:
                    pass

        self.screen.fill((0, 250, 100))
        create_button('Зарегистрироваться', 360, 500, 300, 50, self)
        login_input.draw(self.screen)
        self.clock.tick(60)
        pg.display.update()


def window3(self):
    running = 0
    while running == 0:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                if 430 < mouse_pos[0] < 530 and 200 < mouse_pos[1] < 250:
                    running = button_action3_1()
                elif 430 < mouse_pos[0] < 530 and 400 < mouse_pos[1] < 450:
                    running = button_action3_3()

        self.screen.fill((0, 250, 0))

        self.clock.tick(60)

        create_button('Играть', 430, 200, 100, 50, self)
        create_button('Настройки', 400, 300, 160, 50, self)
        create_button('Выход', 430, 400, 100, 50, self)
        pg.display.update()
    return running


def button_action3_1():
    return 3


def button_action3_3():
    return 5
