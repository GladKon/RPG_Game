import pygame

pygame.init()


class InputField:
    font = pygame.font.Font(None, 36)

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.width = w
        self.color_inactive = pygame.Color((255, 0, 0))
        self.color_active = pygame.Color((0, 255, 0))
        self.color = self.color_inactive
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)
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
                    self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode  # 'a'
                self.txt_surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        width = max(self.width, self.txt_surface.get_width() + 10)
        self.rect.w = width
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


class InputPassword(InputField):
    font = pygame.font.Font(None, 56)

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.text_password = ''

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
                    self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode  # 'a'
                self.text_password = '*' * len(self.text)
                self.txt_surface = self.font.render(self.text_password, True, (0, 0, 0))
