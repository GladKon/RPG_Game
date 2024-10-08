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


def handle_event(event, node):
    # print(node.obj.handle_event(event))
    for obj in node.children:
        handle_event(event, obj)
    if node.obj.handle_event(event):
        node.obj.obj_to_request.create_character(1, 1, 'Mage')


def draw_text(screen, node):
    if hasattr(node.obj, 'draw_text'):
        node.obj.draw_text(screen)
    for obj in node.children:
        draw_text(screen, obj)


obj = MessageToServer()
mage1 = Node(ImageButton(path_to_image / 'img.png', (450, 420), size=(100, 150), obj_to_request=obj))

mage1_1 = Node(ImageSkill(path_to_image / 'img.png', (200, 250), size=(100, 150)))
mage1.children.append(mage1_1)

mage1_2 = Node(ImageSkill(path_to_image / 'img.png', (450, 250), size=(100, 150)))
mage1.children.append(mage1_2)

mage1_3 = Node(ImageSkill(path_to_image / 'img.png', (700, 250), size=(100, 150)))
mage1.children.append(mage1_3)

mage1_1_1 = Node(ImageButton(path_to_image / 'img.png', (200, 80), size=(100, 150)))
mage1_1.children.append(mage1_1_1)

mage1_2_1 = Node(ImageButton(path_to_image / 'img.png', (500, 80), size=(100, 150)))
mage1_2.children.append(mage1_2_1)
mage1_2_2 = Node(ImageButton(path_to_image / 'img.png', (400, 80), size=(100, 150)))
mage1_2.children.append(mage1_2_2)

def handle_event_2(event, node):
    print(node.obj.handle_event(event))
    for obj in node.children:
        handle_event(event, obj)
    if node.obj.handle_event(event):
        node.obj.obj_to_request.create_character(1, 1, 'Archer')

def draw_text_2(screen, node):
    if hasattr(node.obj, 'draw_text'):
        node.obj.draw_text(screen)
    for obj in node.children:
        draw_text(screen, obj)

# obj = MessageToServer()
archer1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (450, 420), size=(100, 150), obj_to_request=obj))

archer1_1 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (200, 250), size=(100, 150)))
archer1.children.append(archer1_1)

archer1_2 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (450, 250), size=(100, 150)))
archer1.children.append(archer1_2)

archer1_3 = Node(ImageSkill(path_to_image / 'idle_test_009.png', (700, 250), size=(100, 150)))
archer1.children.append(archer1_3)

archer1_1_1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (200, 80), size=(100, 150)))
archer1_1.children.append(archer1_1_1)

archer1_2_1 = Node(ImageButton(path_to_image / 'idle_test_009.png', (500, 80), size=(100, 150)))
archer1_2.children.append(archer1_2_1)

archer1_2_2 = Node(ImageButton(path_to_image / 'idle_test_009.png', (400, 80), size=(100, 150)))
archer1_2.children.append(archer1_2_2)

