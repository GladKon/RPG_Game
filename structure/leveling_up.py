import threading

import pygame as pg
from helpers.imagebutton import ImageButton
from helpers.imageskills import ImageSkill
from structure.path import path_to_image
from structure.request_function import MessageToServer


class Node():
    def __init__(self, obj: [ImageButton, ImageSkill]):
        self.obj = obj
        self.children = []


def draw(screen, node, first=True, coords=(0, 0)):
    node.obj.draw(screen)

    x1, y1 = node.obj.rect.centerx, node.obj.rect.top - 5
    for obj in node.children:
        draw(screen, obj, False, (x1, y1))

    if not first:
        x2, y2 = node.obj.rect.centerx, node.obj.rect.bottom + 5
        pg.draw.aaline(screen, (255, 0, 0), coords, (x2, y2))


def handle_event(event, node, game):
    for obj in node.children:
        handle_event(event, obj, game)
    if node.obj.handle_event(event):
        node.obj.obj_to_request.create_character(game, node.obj.character_id, node.obj.character_name)


def draw_text(screen, node):
    if hasattr(node.obj, 'draw_text'):
        node.obj.draw_text(screen)
    for obj in node.children:
        draw_text(screen, obj)


obj = MessageToServer()
mage1 = Node(ImageSkill(path_to_image / 'img.png', (450, 420), character_id=5,character_name='Mage',
                        text='Способность 1) огненый шар - летит в указанном направлении и наностит определённый урон.'
                             '\nСпособность 2) Ледяной выстрел - летит в указанном направлении -'
                             ' при пападании замораживает противника',
                        image_size=(100, 150), obj_to_request=obj, text_size=(200, 250)))

mage1_1 = Node(ImageSkill(path_to_image / 'img.png', (200, 250),character_name='Fire mage',
                          text='Способность 1) огненный шар - летит в указанном направлении при попадании наносит урон'
                               ' есть шанс поджечь и будет наносится периодический урон.Способность'
                               ' 2) огненная пыль - маг кидает пыль в выбранную область при попадании на противника,'
                               ' если он пудет идти наносится урон ',
                          image_size=(100, 150), obj_to_request=obj))
mage1.children.append(mage1_1)

mage1_2 = Node(ImageSkill(path_to_image / 'img.png', (450, 250),character_name='Ice mage', text='Способность 1) ледяной выстрел - летит в указанную'
                                                                      ' сторону при попадании - замораживает противника, а после замедляет его.'
                                                                      'Способность 2) ледяной меч - появляется меч из льда и наносит урон по области',
                          image_size=(100, 150), obj_to_request=obj))
mage1.children.append(mage1_2)

mage1_3 = Node(ImageSkill(path_to_image / 'img.png', (700, 250),character_name='Darkness mage', text='Способность 1) Разложение - маг кастует скилл по области при попадании'
                                                                      ' будет наносится периодический урон.Способность '
                                                                      '2) Призрак - направленный скилл, который будет наноить периодический урон и показывать'
                                                                      ' игрока , если тот не убежит от него н аопределённое растояние ',
                          image_size=(100, 150), obj_to_request=obj))
mage1.children.append(mage1_3)

mage1_1_1 = Node(ImageSkill(path_to_image / 'img.png', (200, 80), text='Способность 1) призыв лавы - в указанной области появляется лава , которая замедляет'
                                                                        ' и наносит периодический урон в зоне.Способность 2) Извержение - вокруг мага случайным образом'
                                                                        ' будут появлятся маленькие лавовые зоны и наносить периоический урон',
                             image_size=(100, 150), obj_to_request=obj))
mage1_1.children.append(mage1_1_1)
mage1_1_2 = Node(ImageSkill(path_to_image / 'img.png', (50, 80), text='Способность 1) Поджог - поджигает выбранную цель нанося периодический урон.'
                                                                       ' Способность 2) выстрел огня - в указанном направлении летят три огненных шара пролитая наносят урон '
                                                                       'и ставляют горящую землю в , которой наносится урон ',
                             image_size=(100, 150), obj_to_request=obj))
mage1_1.children.append(mage1_1_2)

mage1_2_1 = Node(ImageSkill(path_to_image / 'img.png', (500, 80), text='Способность 1)  Ледяной Дух - призывает духа льда который атакует противников и с шансои может их заморозить.'
                                                                        'Способность 2)  Ледяная волна - призывается волна льда , которая наносит периодический урон урон и замедляет противника',
                            image_size=(100, 150), obj_to_request=obj))
mage1_2.children.append(mage1_2_1)
mage1_2_2 = Node(ImageSkill(path_to_image / 'img.png', (400, 80), text='Способность 1)  Призыв меча - призывает 5 ледяных мечей которые будет наносить урон вокруг мага и их можно будет'
                                                                        ' отправить в противника и они взарвутся и заморозят его.Способность 2)  Ледяная бомба - маг оставляет бомбу , которая взарвётся'
                                                                        ' ессли кней подайдёт противник, она заморозит его и нанесёт определённый урон',
                             image_size=(100, 150), obj_to_request=obj))
mage1_2.children.append(mage1_2_2)
mage1_1_3 = Node(ImageSkill(path_to_image / 'img.png', (700, 80), text='Способность 1) Призыв зомби - призывает зомби который будет нападать на против'
                                                                        ' ника в зоне от мага. Способность 2) Мёртвая земля -  появляется заражённая земля в выбранной'
                                                                        ' области, в ней противнику наносится периодический урон и замедление прапорционально времени существования этой области ',
                             image_size=(100, 150), obj_to_request=obj))
mage1_3.children.append(mage1_1_3)


# def handle_event_2(event, node, game):
#     for obj in node.children:
#         handle_event(event, obj, game)
#     if node.obj.handle_event(event):
#         node.obj.obj_to_request.create_character(game, 1, 'Archer')
#
#
# def draw_text_2(screen, node):
#     if hasattr(node.obj, 'draw_text'):
#         node.obj.draw_text(screen)
#     for obj in node.children:
#         draw_text(screen, obj)



archer1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (450, 420), size=(100, 150), obj_to_request=obj))

archer1_1 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (200, 250), image_size=(100, 150), obj_to_request=obj))
archer1.children.append(archer1_1)

archer1_2 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (450, 250), image_size=(100, 150), obj_to_request=obj))
archer1.children.append(archer1_2)

archer1_3 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (700, 250), image_size=(100, 150), obj_to_request=obj))
archer1.children.append(archer1_3)

archer1_1_1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (200, 80), size=(100, 150), obj_to_request=obj))
archer1_1.children.append(archer1_1_1)

archer1_2_1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (500, 80), size=(100, 150), obj_to_request=obj))
archer1_2.children.append(archer1_2_1)

archer1_2_2 = Node(ImageButton(path_to_image / 'idle_test_009.png', (400, 80), size=(100, 150), obj_to_request=obj))
archer1_2.children.append(archer1_2_2)
