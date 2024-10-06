import pygame.image

from structure.path import path_to_font


class ImageButton():
    def __init__(self, path, coords, text='', size=(150, 200), obj_to_request=None):
        self.obj_to_request = obj_to_request
        self.font = pygame.font.Font(path_to_font/'test_font.ttf', 26)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        # self.image_ram = pygame.image.load(path_ram)
        # self.image_ram = pygame.transform.scale(self.image_ram, (int(self.image.get_width() * 1.1), int(self.image.get_height() * 1.1)))
        self.rect = self.image.get_rect(center=coords)
        # self.rect_ram = self.image_ram.get_rect(center=(coords[0], coords[1]+20))
        self.text = text
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_w, text_h = self.text_surface.get_size()
        self.text_cords = (coords[0]-text_w//2, coords[1]+size[1]//2 )


        self.font_hover = pygame.font.Font(path_to_font/'test_font.ttf', int(26 * 1.2))
        self.text_surface_hover = self.font_hover.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface_hover.get_rect()
        self.text_rect.center = coords[0] , int((coords[1] // 2 + coords[1]) * 1.2)
        self.text_hover = (coords[0] + size[0] // 2, int((coords[1] // 2 + coords[1]) * 1.2))
        self.hover_image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * 1.1), int(self.image.get_height() * 1.1)))
        self.hover_rect = self.hover_image.get_rect(center=coords)

        self.activate = False

    def handle_event(self, event):
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
            # screen.blit(self.image_ram, self.rect_ram)
            screen.blit(self.text_surface_hover, self.text_rect)
        else:
            screen.blit(self.image, self.rect)
            screen.blit(self.text_surface, self.text_cords)
