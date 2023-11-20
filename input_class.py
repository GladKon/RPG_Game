import pygame

pygame.init()
font = pygame.font.Font(None, 36)  # Установка шрифта


class InputField:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color((255, 0, 0))
        self.color_active = pygame.Color((0, 255, 0))
        self.color = self.color_inactive
        self.text = ''
        self.txt_surface = font.render(self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:  # ENTER
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode  # 'a'
                self.txt_surface = font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))