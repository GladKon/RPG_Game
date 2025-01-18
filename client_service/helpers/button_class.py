import pygame

pygame.init()

font = pygame.font.Font(None, 26)


class Button:
    def __init__(self, text, x, y, w, h, color_base=(65, 105, 225), color_hover=(100, 149, 237), shadow_color=(20, 20, 20), font=font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.color_base = color_base  # Основной цвет кнопки
        self.color_hover = color_hover  # Цвет при наведении
        self.shadow_color = shadow_color  # Цвет тени
        self.current_color = color_base

    def handle_event(self, event):
        """Обрабатывает события кнопки."""
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True

    def draw(self, screen):
        """Рисует кнопку с прямоугольной тенью."""
        mouse = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse)

        # Параметры тени
        shadow_offset = 8 if not is_hovered else 4  # Тень уменьшается при наведении
        shadow_rect = pygame.Rect(self.rect.x + shadow_offset, self.rect.y + shadow_offset, self.rect.width,
                                  self.rect.height)

        # Рисуем тень
        pygame.draw.rect(screen, self.shadow_color, shadow_rect)

        # Цвет кнопки
        self.current_color = self.color_hover if is_hovered else self.color_base
        pygame.draw.rect(screen, self.current_color, self.rect)

        # Текст
        text_surface = self.font.render(self.text, True, (255, 255, 255))  # Белый текст
        text_rect = text_surface.get_rect(
            center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))
        screen.blit(text_surface, text_rect)
