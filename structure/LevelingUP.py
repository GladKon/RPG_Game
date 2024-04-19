import threading

import pygame as pg
from RPG_Game.helpers.imagebutton import ImageButton
from RPG_Game.helpers.imageskills import ImageSkill


class Node():
    def __init__(self, obj:[ImageButton, ImageSkill]):
        self.obj = obj
        self.children = []




def draw(screen, node, first=True, coords=(0,0)):
    node.obj.draw(screen)

    x1, y1 = node.obj.rect.centerx, node.obj.rect.top - 5
    for obj in node.children:
        draw(screen, obj, False, (x1, y1))

    if not first:
        x2, y2 = node.obj.rect.centerx, node.obj.rect.bottom + 5
        pg.draw.aaline(screen, (255, 0, 0), coords, (x2, y2))


def handle_event(event, node):
    node.obj.handle_event(event)
    for obj in node.children:
        handle_event(event, obj)




mage1 = Node(ImageButton('res/images_for_window/img.png', (300, 600), size=(100, 150)))

mage1_1 = Node(ImageSkill('res/images_for_window/img.png', (150, 400), size=(100, 150)))
mage1.children.append(mage1_1)

mage1_2 = Node(ImageSkill('res/images_for_window/img.png', (300, 400), size=(100, 150)))
mage1.children.append(mage1_2)

mage1_3 = Node(ImageSkill('res/images_for_window/img.png', (450, 400), size=(100, 150)))
mage1.children.append(mage1_3)

mage1_1_1 = Node(ImageButton('res/images_for_window/img.png', (100, 100), size=(100, 150)))
mage1_1.children.append(mage1_1_1)

mage1_2_1 = Node(ImageButton('res/images_for_window/img.png', (300, 100), size=(100, 150)))
mage1_2.children.append(mage1_2_1)
mage1_2_2 = Node(ImageButton('res/images_for_window/img.png', (400, 100), size=(100, 150)))
mage1_2.children.append(mage1_2_2)
# botton8 = Node(ImageButton('res/images_for_window/img.png', (700, 300), size=(100, 150)))
# botton9 = Node(ImageButton('res/images_for_window/img.png', (700, 100), size=(100, 150)))

