import pygame as pg

pg.init()
font = pg.font.Font('fonts/test_font.ttf', 16)


class LineBreak:
    def __init__(self, text, line, RGB):
        self.text = text
        self.line = line
        self.RGB = RGB
        self.max = text.count(' ')
        self.step = self.max // self.line + 1

    def draw(self, coor, screen, indent=30):

        x, y = coor
        chet = 0
        text = ''
        for simvol in self.text:
            if simvol == ' ':
                chet += 1
            elif chet == self.step:
                chet = 0
                slovo = font.render(text, True, self.RGB)
                screen.blit(slovo, (x, y))
                text = ''
                y += indent
            if chet != self.step:
                text += simvol

        slovo = font.render(text, True, self.RGB)
        screen.blit(slovo, (x, y))


