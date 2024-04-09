import pygame as pg
import time
from pygame.locals import *

from src.Figure import Figure


class Interface:
    fps = 60
    window_w, window_h = 380, 468
    step_right, step_left, step_down, step_space = 0, 0, 0, 0
    right_time, left_time, down_time, space_time = 0, 0, 0, 0

    def initPygame(self):
        global fps_clock, display_surf, basic_font, big_font
        pg.init()
        fps_clock = pg.time.Clock()

        display_surf = pg.display.set_mode((self.window_w, self.window_h))
        display_surf.fill((158, 173, 134))

        basic_font = pg.font.Font('freesansbold.ttf', 18)
        big_font = pg.font.Font('freesansbold.ttf', 45)

        pg.display.set_caption('Hell TETRIS')

    def start(self):
        self.initPygame()
        self.initInterface()
        pg.display.update()

        figure = Figure()
        figure.createFigure()
        figure.addFigure()
        self.drafNextFigure(figure)
        pg.display.update()
        last_move_down = time.time()
        while True:
            self.updateField(figure.mas)
            if (time.time() - last_move_down > 0.3):
                figure.stepDown()
                pg.display.update()
                last_move_down = time.time()

            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.step_right = True
                        self.right_time = time.time()
                    if event.key == K_LEFT:
                        self.step_left = True
                        self.left_time = time.time()
                    if event.key == K_DOWN:
                        self.step_down = True
                        self.down_time = time.time()
                    if event.key == K_SPACE:
                        self.step_space = True
                        self.space_time = time.time()
                    elif event.type == pg.QUIT:
                        exit()
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.step_right = False
                    if event.key == K_LEFT:
                        self.step_left = False
                    if event.key == K_DOWN:
                        self.step_down = False
                    if event.key == K_SPACE:
                        self.step_space = False

            if self.step_right and time.time() - self.right_time > 0.1:
                figure.stepRight()
                self.right_time = time.time()
            if self.step_left and time.time() - self.left_time > 0.1:
                figure.stepLeft()
                self.left_time = time.time()
            if self.step_down and time.time() - self.down_time > 0.1:
                figure.stepDown()
                self.down_time = time.time()
            if self.step_space and time.time() - self.space_time > 0.1:
                figure.rotateFigure()
                self.space_time = time.time()

            display_surf.fill((158, 173, 134), (300, 10, 70, 20))
            score = basic_font.render(str(figure.score).rjust(6, "0"), 3, (0, 0, 0))
            display_surf.blit(score, (300, 10))

            if figure.endGame == True:
                self.screeSaver()
                figure.emptyField()
                figure.createFigure()
                figure.addFigure()
                figure.endGame = False

            self.drafNextFigure(figure)
            pg.display.update()
            fps_clock.tick(self.fps)

    def initInterface(self):
        # Главное поле
        pg.draw.rect(display_surf, (0, 0, 0), (5, 5, 228, 448), 2)
        self.showEmptyField()
        self.showEmptyFieldNextFigure()
        score = basic_font.render('000000', 3, (0, 0, 0))
        display_surf.blit(score, (300, 10))
        scoreText = basic_font.render('SCORE', 1, (0, 0, 0))
        display_surf.blit(scoreText, (300, 30))
        pg.display.update()

        self.screeSaver()

    def drafNextFigure(self, figure):
        mas = figure.figure[figure.nameNextFigure][figure.typeNextFigure]
        self.showEmptyFieldNextFigure()
        self.updateFieldNextFigure(mas)


    def screeSaver(self):
        timeLoading = time.time()
        countBlock = 0
        countBlockBefore = -1
        while (True):
            if time.time() - timeLoading > 0.02:
                if countBlockBefore < countBlock:
                    for i in range(0, 10):
                        self.fillBlock(countBlock, i)
                    countBlockBefore = countBlock
                    countBlock = countBlock + 1
                if countBlockBefore > countBlock:
                    for i in range(0, 10):
                        self.emptyBlock(countBlock, i)
                    countBlockBefore = countBlock
                    countBlock = countBlock - 1

                if countBlock == 20:
                    countBlockBefore = countBlock
                    countBlock = countBlock - 1
                if countBlock == 0:
                    break
                timeLoading = time.time()

            pg.display.update()
    def showEmptyField(self):
        for i in range(0, 20):
            for j in range(0, 10):
                self.emptyBlock(i, j)

    def showEmptyFieldNextFigure(self):
        for i in range(0, 4):
            for j in range(0, 4):
                self.emptyBlockNextFigure(i, j)

    def updateFieldNextFigure(self, mas):
        for i in range(0, len(mas)):
            for j in range(0, len(mas[i])):
                if mas[i][j] == 1:
                    self.fillBlockNextFigure(i, j)
                else:
                    self.emptyBlockNextFigure(i, j)

    def updateField(self, field):
        for i in range(0, 20):
            for j in range(0, 10):
                if field[i][j] == 1 or field[i][j] == 2:
                    self.fillBlock(i, j)
                else:
                    self.emptyBlock(i, j)

    def emptyBlock(self, indRow, indCol):
        pg.draw.rect(display_surf, (135, 147, 114), (10 + 22 * indCol, 10 + 22 * indRow, 20, 20), 1)
        pg.draw.rect(display_surf, (135, 147, 114), (14 + 22 * indCol, 14 + 22 * indRow, 12, 12))

    def fillBlock(self, indRow, indCol):
        pg.draw.rect(display_surf, (0, 0, 0), (10 + 22 * indCol, 10 + 22 * indRow, 20, 20), 1)
        pg.draw.rect(display_surf, (0, 0, 0), (14 + 22 * indCol, 14 + 22 * indRow, 12, 12))

    def emptyBlockNextFigure(self, indRow, indCol):
        pg.draw.rect(display_surf, (135, 147, 114), (270 + 22 * indCol, 100 + 22 * indRow, 20, 20), 1)
        pg.draw.rect(display_surf, (135, 147, 114), (274 + 22 * indCol, 104 + 22 * indRow, 12, 12))

    def fillBlockNextFigure(self, indRow, indCol):
        pg.draw.rect(display_surf, (0, 0, 0), (270 + 22 * indCol, 100 + 22 * indRow, 20, 20), 1)
        pg.draw.rect(display_surf, (0, 0, 0), (274 + 22 * indCol, 104 + 22 * indRow, 12, 12))


ui = Interface()
ui.start()
