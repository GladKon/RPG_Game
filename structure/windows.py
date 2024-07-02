import pygame as pg
import requests
import time

from helpers.button_class import Button
from helpers.helper import password_hard
from helpers.imagebutton import ImageButton
from helpers.imageskills import ImageSkill
from helpers.input_class import InputField, InputPassword
from helpers.list_class import TextList
from helpers.line_break import LineBreak
from structure.leveling_up import mage1, draw, handle_event, draw_text
from structure.request_function import MessageToServer

pg.init()

font = pg.font.Font(None, 36)
Message_To_Server = MessageToServer()


class Windows:

    def start_window(self, game):
        b1 = Button('Войти', 430, 200, 100, 50)
        b2 = Button('Зарегистрироваться', 360, 300, 300, 50)

        while game.state == 'START_WINDOW':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                elif b1.handle_event(event):
                    game.state = 'INPUT'
                    break
                elif b2.handle_event(event):
                    game.state = 'REGISTRATION'
                    break

            game.screen.fill((0, 250, 0))
            game.clock.tick(60)

            b1.draw(game.screen)
            b2.draw(game.screen)

            pg.display.update()

    def registration(self, game):
        b1 = Button('Зарегистрироваться', 340, 400, 300, 50)
        b2 = Button('Назад', 420, 500, 100, 50)

        login_input = InputField(360, 100, 200, 50)
        password_input = InputPassword(360, 200, 200, 50)
        password_input2 = InputPassword(360, 300, 200, 50)

        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        password2 = font.render('Подтвертите пароль', True, (0, 10, 0))
        name_error = font.render('Существующее имя', True, (255, 0, 0))
        password_error = font.render('Разные пароли', True, (255, 0, 0))
        short = LineBreak('Короткий пароль', 1, (100, 0, 0))
        alfavit = LineBreak('Пароль должен содержать латинские буквы', 3, (100, 0, 0))
        slogno = LineBreak('Пароль должен содержать символы', 3, (100, 0, 0))

        running = None
        while game.state == 'REGISTRATION':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    running = password_hard(password_input2.text)
                    if running == 'True':
                        running = Message_To_Server.button_registration(login_input.text, password_input.text,
                                                                        password_input2.text)
                        if running == 'MENU':
                            game.state = 'MENU'
                            break


                elif b2.handle_event(event):
                    game.state = 'START_WINDOW'
                    break
                login_input.handle_event(event)
                password_input.handle_event(event)
                password_input2.handle_event(event)

            game.screen.fill((0, 250, 100))
            game.screen.blit(name, (100, 100))

            if running == 'name_error':
                game.screen.blit(name_error, (600, 110))
            elif running == 'password_error':
                game.screen.blit(password_error, (600, 250))
            elif running == 'password_short':
                short.draw((600, 200), game.screen, 40)
            elif running == 'password_alfavit':
                alfavit.draw((600, 200), game.screen, 40)
            elif running == 'password_simvol':
                slogno.draw((600, 200), game.screen, 40)

            game.screen.blit(password, (100, 200))
            game.screen.blit(password2, (100, 300))

            b1.draw(game.screen)
            b2.draw(game.screen)
            login_input.draw(game.screen)
            password_input.draw(game.screen)
            password_input2.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def window_input(self, game):
        b1 = Button('Войти', 420, 400, 100, 50)
        b2 = Button('Назад', 420, 500, 100, 50)
        login_input = InputField(360, 100, 200, 50)
        password_input = InputPassword(360, 200, 200, 50)

        name = font.render('Введите никмейм', True, (0, 10, 0))
        password = font.render('Введите пароль', True, (0, 10, 0))
        error = font.render('Неверное имя или пароль!', True, (255, 0, 0))
        server_error = LineBreak('На сервере ошибка', 1, (250, 0, 0))
        running = None

        while game.state == 'INPUT':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    running = Message_To_Server.check_users(login_input.text, password_input.text)
                    if running == 'MENU':
                        game.state = 'MENU'
                        game.data['name'] = login_input.text
                        break
                elif b2.handle_event(event):
                    game.state = 'START_WINDOW'
                    break
                login_input.handle_event(event)
                password_input.handle_event(event)

            game.screen.fill((0, 250, 100))
            game.screen.blit(name, (100, 100))

            if running == 'error':
                game.screen.blit(error, (570, 150))
            elif running == 'error_server':
                server_error.draw((570, 150), game.screen, 40)

            game.screen.blit(password, (100, 200))

            b1.draw(game.screen)
            b2.draw(game.screen)
            login_input.draw(game.screen)
            password_input.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def menu(self, game):
        b1 = Button('Играть', 430, 200, 100, 50)
        b2 = Button('Настройки', 400, 300, 160, 50)
        b3 = Button("Выбор персонажа", 400, 400, 160, 50)
        b4 = Button('Выход', 430, 500, 100, 50)

        while game.state == 'MENU':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    game.state = 'ROOM'
                    break
                elif b3.handle_event(event):
                    game.state = 'PLAYER_CHOOSE'
                    break
                elif b4.handle_event(event):
                    game.state = 'EXIT'
                    break

            game.screen.fill((0, 250, 0))

            b1.draw(game.screen)
            b2.draw(game.screen)
            b3.draw(game.screen)
            b4.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def room(self, game):
        b1 = Button('Создать комнату', 400, 200, 220, 50)
        b2 = Button('Войти в комнату', 400, 300, 220, 50)
        b3 = Button('Назад', 430, 400, 100, 50)
        while game.state == 'ROOM':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    game.state = 'CREATE_ROOM'
                    break
                elif b2.handle_event(event):
                    game.state = 'INPUT_ROOM'
                    break
                elif b3.handle_event(event):
                    game.state = 'MENU'
                    break

            game.screen.fill((0, 250, 0))

            b1.draw(game.screen)
            b2.draw(game.screen)
            b3.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def player_choose(self, game):
        i1 = ImageButton('res/images_for_window/img.png', (200, 200), 'Hunter')
        i2 = ImageButton('res/images_for_window/img.png', (700, 200), 'Survival')
        b1 = Button('Назад', 430, 500, 100, 50)


        while game.state == 'PLAYER_CHOOSE':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif i1.handle_event(event):
                    game.state = 'CHOOSING_HERO'
                    break
                elif i2.handle_event(event):
                    pass
                elif b1.handle_event(event):
                    game.state = 'MENU'
                    break

            game.screen.fill((0, 250, 0))

            i1.draw(game.screen)
            i2.draw(game.screen)
            b1.draw(game.screen)


            game.clock.tick(60)
            pg.display.update()


    def choosing_hero(self,game):
        i1 = ImageButton('res/images_for_window/img.png', (150, 200), 'Mage')
        i2 = ImageButton('res/images_for_window/img.png', (450, 200), 'Archer')
        i3 = ImageButton('res/images_for_window/img.png', (750, 200), 'Warrior')
        while game.state == 'CHOOSING_HERO':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif i1.handle_event(event):
                    game.state = 'TREE_PLAYER'
                    break
                elif i2.handle_event(event):
                    pass
                elif i3.handle_event(event):
                    pass
            game.screen.fill((0, 250, 0))

            i1.draw(game.screen)
            i2.draw(game.screen)
            i3.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def tree_player(self, game):
        b1 = Button('Назад', 430, 500, 100, 50)
        while game.state == 'TREE_PLAYER':

            for event in pg.event.get():
                handle_event(event, mage1)
                # displey.handle_event(event)
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break

                elif b1.handle_event(event):
                    game.state = 'MENU'
                    break

            game.screen.fill((0, 250, 0))

            b1.draw(game.screen)
            draw(game.screen, mage1)
            draw_text(game.screen, mage1)

            game.clock.tick(60)
            pg.display.update()

    def input_room(self, game):
        b1 = Button('Назад', 430, 400, 100, 50)
        b2 = Button('Войти', 430, 300, 100, 50)
        name_room = InputField(360, 100, 200, 50)
        password_room = InputField(360, 200, 200, 50)

        name = font.render('Введите название комнаты', True, (0, 10, 0))
        password = font.render('Введите пароль от комнаты', True, (0, 10, 0))

        while game.state == 'INPUT_ROOM':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    game.state = 'MENU'
                    break
                elif b2.handle_event(event):
                    game.data['name_of_room'] = name_room.text
                    game.state = Message_To_Server.connect_to_room(name_room.text, password_room.text,
                                                                   game.data['name'])
                    game.data['CREATER'] = False
                    break
                name_room.handle_event(event)
                password_room.handle_event(event)

            game.screen.fill((0, 250, 0))
            game.screen.blit(name, (300, 50))
            game.screen.blit(password, (300, 150))

            b1.draw(game.screen)
            b2.draw(game.screen)
            name_room.draw(game.screen)
            password_room.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def create_room(self, game):
        b1 = Button('Создать', 430, 350, 100, 50)
        b2 = Button('Назад', 430, 450, 100, 50)

        room_name = InputField(410, 90, 200, 50)
        room_password = InputField(410, 190, 200, 50)
        room_max_player = InputField(470, 290, 50, 50)

        name_room = font.render('Введите имя комнаты', True, (0, 10, 0))
        text_password = font.render('Введите пароль комнаты', True, (0, 10, 0))
        text_max_player = font.render('Максимальное число игроков', True, (0, 10, 0))

        while game.state == 'CREATE_ROOM':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                    break
                elif b1.handle_event(event):
                    game.data['name_of_room'] = room_name.text
                    game.state = Message_To_Server.create_a_room(room_name.text, room_password.text,
                                                                 room_max_player.text)
                    if game.state == 'GAME_ROOM':
                        Message_To_Server.connect_to_room(room_name.text, room_password.text, game.data['name'])
                        game.data['CREATER'] = True
                elif b2.handle_event(event):
                    game.state = 'ROOM'
                room_name.handle_event(event)
                room_password.handle_event(event)
                room_max_player.handle_event(event)

            game.screen.fill((0, 250, 0))
            game.screen.blit(name_room, (100, 100))
            game.screen.blit(text_password, (100, 200))
            game.screen.blit(text_max_player, (100, 300))

            b1.draw(game.screen)
            b2.draw(game.screen)
            room_name.draw(game.screen)
            room_max_player.draw(game.screen)
            room_password.draw(game.screen)

            game.clock.tick(60)
            pg.display.update()

    def game_room(self, game):
        users = Message_To_Server.get_list_of_users(game.data['name_of_room'])

        b1 = Button('Назад', 430, 500, 100, 45)
        b2 = Button('Запустить', 430, 450, 100, 45)
        l1 = TextList(users, (236, 10, 100), 430, 100, 50)
        start = time.time()
        while game.state == 'GAME_ROOM':
            # код нужно улучшить
            if time.time() - start >= 2:
                users = Message_To_Server.get_list_of_users(game.data['name_of_room'])
                l1 = TextList(users, (236, 10, 100), 430, 100, 50)
                start = time.time()
            # конец
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game.state = 'EXIT'
                elif b1.handle_event(event):
                    game.state = 'ROOM'
                elif b2.handle_event(event) and game.data['CREATER']:
                    data = requests.get(f'http://127.0.0.1:5000/room/{game.data["name_of_room"]}/start_game')
                    if data.status_code == 200:
                        game.state = 'GAME'

                game.screen.fill((0, 250, 0))

                b1.draw(game.screen)

                if game.data['CREATER']:
                    b2.draw(game.screen)

                l1.draw(game.screen)

                game.clock.tick(60)
                pg.display.update()
