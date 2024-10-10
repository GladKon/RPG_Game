import pygame as pg
import pygame.image

from helpers.line_break import LineBreak
from helpers.text_box import TextBox
from structure.path import path_to_font


class ImageSkill():
    def __init__(self, path, coords,character_name='Mage', text='Привет мир и Россия и мы все дружно живём в социалистическом мире', step=3,
                 image_size=(300, 300), obj_to_request=None, text_size=(200, 100)):
        self.character_name = character_name
        self.obj_to_request = obj_to_request
        self.font = pygame.font.Font(path_to_font / 'test_font.ttf', 16)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, image_size)
        self.rect = self.image.get_rect(center=coords)

        # self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_cords = (coords[0] + text_size[1], coords[1] - text_size[1])
        self.text = LineBreak(text, step, (1, 1, 1))

        self.img_rect = (self.text_cords[0], self.text_cords[1], image_size[1] * step, image_size[1] * step)

        self.font_hover = pygame.font.Font(None, int(46 * 1.2))
        self.hover_image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * 1.1), int(self.image.get_height() * 1.1)))
        self.hover_rect = self.hover_image.get_rect(center=coords)
        self.text_box = TextBox(coords[0] + image_size[0]//2, coords[1] - image_size[1]//2, text_size[0], text_size[1], text)

        self.activate = False

    def handle_event(self, event):
        self.text_box.handle_event(event)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONUP and not (event.button == 4 or event.button == 5):
                if self.activate:
                    return True
                else:
                    self.activate = True

        else:
            if event.type == pygame.MOUSEBUTTONUP:
                self.activate = False

    def draw(self, screen):
        if self.activate:
            screen.blit(self.hover_image, self.hover_rect)


        else:
            screen.blit(self.image, self.rect)

    def draw_text(self, screen):
        if self.activate:
            # beakgraund_rect = pg.Rect(self.rect.right, self.rect.top, 330, (len(self.text.spisok) * 35))
            # pg.draw.rect(screen, (155, 150, 200), beakgraund_rect, border_radius=15)
            # pg.draw.rect(screen, (100, 50, 200), beakgraund_rect.inflate(5, 5), 5, border_radius=15)
            #
            # self.text.draw((self.rect.right + 10, self.rect.top), screen)
            self.text_box.draw(screen)
