import pygame

pygame.init()

font = pygame.font.Font(None, 20)


class Button:
    def __init__(self, text, x, y, w, h, color_active=(50, 50, 50), color_inactive=(255, 0, 0), font=font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(self.text, True, (255, 255, 255))
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = self.color_inactive
        self.x, self.y, self.w, self.h = x, y, w, h

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.x < mouse_pos[0] < self.rect.x + self.rect.w and self.rect.y < mouse_pos[
                1] < self.rect.y + self.rect.h:
                return True

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (50, 150, 200), (self.x, self.y, self.w, self.h))

        # if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
        #     pygame.draw.rect(screen, (50, 200, 255), (self.x, self.y, self.w, self.h))
        if self.rect.collidepoint(mouse):
            self.color = self.color_active
            pygame.draw.rect(screen, (50, 200, 255), (self.x, self.y, self.w, self.h))
        else:
            self.color = self.color_inactive
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=((self.rect.x + self.rect.w / 2), (self.rect.y + self.rect.h / 2)))
        screen.blit(text_surface, text_rect)