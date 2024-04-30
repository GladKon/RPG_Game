import pygame as pg

from structure.path import path_to_font

pg.init()
font = pg.font.Font(path_to_font/'test_font.ttf', 16)


class LineBreak:
    def __init__(self, text, line, RGB):
        self.text = text
        self.line = line
        self.RGB = RGB
        self.max = text.count(' ')
        self.step = self.max // self.line + 1
        self.spisok = []

    def draw(self, coor, screen, indent=30):

        # x, y = coor
        # chet = 0
        # text = ''
        # for simvol in self.text:
        #     if simvol == ' ':
        #         chet += 1
        #     elif chet == self.step:
        #         chet = 0
        #         slovo = font.render(text, True, self.RGB)
        #         screen.blit(slovo, (x, y))
        #         text = ''
        #         y += indent
        #     if chet != self.step:
        #         text += simvol
        #
        # slovo = font.render(text, True, self.RGB)
        # screen.blit(slovo, (x, y))

        x, y = coor
        chet = 0
        text = ''
        order = ''
        last = ''
        true = False
        self.spisok = []
        for simvol in self.text:
            if simvol == ' ':
                for i in range(2):
                    if chet <= 15 and chet >= 10:
                        chet = 0
                        slovo = font.render(text, True, self.RGB)
                        self.spisok.append(slovo)
                        screen.blit(slovo, (x, y))
                        text = ''
                        order = ''
                        true = False
                        last = ''
                        y += indent
                    elif chet > 15:

                        chet = len(order)
                        slovo = font.render(last, True, self.RGB)
                        self.spisok.append(slovo)
                        screen.blit(slovo, (x, y))
                        text = order

                        order = ''
                        true = False
                        last = ''
                        y += indent
                    elif i != 1 and chet >= 7:
                        last = text

                        true = True
                    if chet > 15 and last == '':
                        last = text
            if true:
                if not(order == '' and simvol == ' '):
                    order += simvol
            if text == '' and simvol == ' ':
                pass
            else:
                text += simvol
                chet += 1

        slovo = font.render(text, True, self.RGB)
        self.spisok.append(slovo)
        screen.blit(slovo, (x, y))





