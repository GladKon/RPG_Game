import pygame.image


class ImageButton():
    def __init__(self, path, path_ram, coords, text=''):
        self.font = pygame.font.Font(None, 56)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.image_ram = pygame.image.load(path_ram).convert_alpha()
        self.image_ram = pygame.transform.scale(self.image_ram, (220, 530))
        self.rect = self.image.get_rect(center=coords)
        self.rect_ram = self.image_ram.get_rect(center=(coords[0], coords[1]+20))
        self.text = text
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_cords = (coords[0]-coords[0]//4, coords[1]//2 + coords[1])

        self.font_hover = pygame.font.Font(None, int(56 * 1.2))
        self.text_surface_hover = self.font_hover.render(self.text, True, (255, 255, 255))
        self.text_hover = (coords[0]-coords[0]//4, int((coords[1] // 2 + coords[1]) * 1.1))
        self.hover_image = pygame.transform.scale(self.image, (
        int(self.image.get_width() * 1.1), int(self.image.get_height() * 1.1)))
        self.hover_rect = self.hover_image.get_rect(center=coords)

        self.is_active = False

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_active = True
            if event.type == pygame.MOUSEBUTTONUP:
                return True
        else:
            self.is_active = False

    def draw(self, screen):
        if self.is_active:
            screen.blit(self.hover_image, self.hover_rect)
            screen.blit(self.image_ram, self.rect_ram)
            screen.blit(self.text_surface_hover, self.text_hover)

        else:
            screen.blit(self.image, self.rect)
            screen.blit(self.text_surface, self.text_cords)
