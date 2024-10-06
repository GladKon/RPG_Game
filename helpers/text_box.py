import pygame


class TextBox:
    def __init__(self, x, y, width, height, text, font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.offset = 0
        self.font = font or pygame.font.SysFont(None, 24)
        self.line_height = self.font.get_linesize()
        self.lines = self.wrap_text()
        self.content_height = len(self.lines) * self.line_height

    def wrap_text(self):
        words = self.text.split(' ')
        lines = []
        line = ''
        for word in words:
            test_line = f"{line} {word}".strip()
            if self.font.size(test_line)[0] <= self.rect.width:
                line = test_line
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        return lines

    def draw(self, screen):
        big_surface = pygame.Surface((self.rect.width+10, self.rect.height+10))
        clip_surface = pygame.Surface((self.rect.width, self.rect.height))
        clip_surface.fill((100, 100, 100))

        y = -self.offset
        for line in self.lines:
            if y + self.line_height > 0 and y < self.rect.height:
                text_surface = self.font.render(line, True, (0, 0, 0))
                clip_surface.blit(text_surface, (0, y))
            y += self.line_height
        screen.blit(big_surface, (self.rect.x-5, self.rect.y-5))
        screen.blit(clip_surface, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.scroll(-1)
            elif event.button == 5:
                self.scroll(1)

    def scroll(self, direction):
        self.offset += direction * self.line_height
        max_offset = max(0, self.content_height - self.rect.height)
        self.offset = max(0, min(self.offset, max_offset))