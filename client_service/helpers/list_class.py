import pygame as pg

pg.init()


class TextList:
    def __init__(self, text_line, color, x, y, line_spacing, font=None):
        self.text_list = text_line
        self.color = color
        self.x = x
        self.y = y
        self.line_spacing = line_spacing
        self.font = pg.font.Font(font, 36)

    def draw(self, screen):
        for counter, line in enumerate(self.text_list, start=1):

            draw = self.font.render(str(counter) +')' + ' ' + line, True, self.color)
            screen.blit(draw, (self.x, self.y + self.line_spacing * (counter - 1)))

