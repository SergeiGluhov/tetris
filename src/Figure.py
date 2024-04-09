# создать фигуру
# добавить фигуру в массив
# повернуть фигуру
# можно ли повернуть фигуру
import random


class Figure:
    mas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]           ]

    score = 0
    endGame = False
    nameFigure = None
    typeFigure = None


    Tu = [[0, 1, 0], [1, 1, 1]]
    Tr = [[1, 0], [1, 1], [1, 0]]
    Td = [[1, 1, 1], [0, 1, 0]]
    Tl = [[0, 1], [1, 1], [0, 1]]
    T = [Tu, Tr, Td, Tl]  # Положение фигур

    Ou = [[1, 1], [1, 1]]
    O = [Ou]

    Iv = [[1], [1], [1], [1]]
    Ih = [[1, 1, 1, 1]]
    I = [Iv, Ih]

    Jl = [[0, 1], [0, 1], [1, 1]]
    Ju = [[1, 0], [1, 1, 1]]
    Jr = [[1, 1], [1, 0], [1, 0]]
    Jd = [[1, 1, 1], [0, 0, 1]]
    J = [Jl, Ju, Jr, Jd]

    Zh =[[1,1,0],[0,1,1]]
    Zv =[[0,1], [1,1], [1,0]]
    Z = [Zh, Zv]

    Sh = [[0,1,1],[1,1,0]]
    Sv = [[1,0],[1,1],[0,1]]
    S = [Sh, Sv]

    Lr = [[1,0],[1,0],[1,1]]
    Ld = [[1,1,1], [1,0,0]]
    Ll = [[1,1],[0,1],[0,1]]
    Lu = [[0,0,1],[1,1,1]]
    L = [Lr, Ld, Ll, Lu]
    figure = [T, O, I, J, Z, S, L]  # Хранит имена фигур

    nameNextFigure = random.randint(0, len(figure) - 1)
    typeNextFigure = random.randint(0, len(figure[nameNextFigure]) - 1)

    def createFigure(self):
        self.nameFigure = self.nameNextFigure
        self.typeFigure = self.typeNextFigure
        self.nameNextFigure = random.randint(0, len(self.figure)-1)
        self.typeNextFigure = random.randint(0, len(self.figure[self.nameNextFigure])-1)

    def emptyField(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                self.mas[i][j] = 0
        self.score = 0
    def checkCompleted(self):
        mas = self.mas
        countScore = 0
        for i in range(0, len(mas)):
            flag = True
            for j in range(0, len(mas[i])):
                if mas[i][j] == 0 or mas[i][j] == 1:
                    flag = False
            if flag == True:
                zeros_list = [0] * len(mas[0])
                mas.pop(i)
                mas.insert(0, zeros_list)
                countScore = countScore + 1

        if countScore == 1:
            self.score = self.score + 100
        if countScore == 2:
            self.score = self.score + 300
        if countScore == 3:
            self.score = self.score + 700
        if countScore == 4:
            self.score = self.score + 1500


    def stepDown(self):
        indRow = self.indRow + 1
        result = self.isCorrectPosition(indRow, self.indColumn, self.typeFigure)
        if result == False:
            self.completedFigure()
            self.checkCompleted()
            self.createFigure()
            self.addFigure()
            self.score = self.score + 10
            return
        self.cleanFigure()
        self.drawFigure()

    def isCorrectPosition(self, indRow, indColumn, typeFigure):
        mas = self.figure[self.nameFigure][typeFigure]

        block_row, block_col = 0, 0

        if indRow < 0:
            #print("Отрисовать нельзя")
            return False

        if indColumn >= 0 and indColumn + len(mas[0]) <= len(self.mas[0]):
            #print("Отрисовать можно")
            pass
        else:
            #print("Отрисовать нельзя")
            return False

        if indRow + len(mas) <= len(self.mas):
            #print("Отрисовать можно")
            pass
        else:
            #print("Отрисовать нельзя")
            return False

        for i in range(indRow, len(mas) + indRow):
            for j in range(indColumn, len(mas[block_row]) + indColumn):
                if mas[block_row][block_col] == 1 and self.mas[i][j] == 2:
                    #print("Вставлять нельзя")
                    return False
                block_col = block_col + 1
            block_col = 0
            block_row = block_row + 1
        #print("Можно вставить")

        self.typeFigure = typeFigure
        self.indRow = indRow
        self.indColumn = indColumn
        return True

    def addFigure(self):
        mas = self.figure[self.nameFigure][self.typeFigure]

        indRow, indColumn = 0, 0
        if len(mas[0]) == 4:
            indColumn = int((len(self.mas[0]) - 1) / 2) - 1
        if len(mas[0]) == 3:
            indColumn = int((len(self.mas[0]) - 1) / 2) - 1
        if len(mas[0]) == 2 or len(mas[0]) == 1:
            indColumn = int((len(self.mas[0]) - 1) / 2)

        result = self.isCorrectPosition(indRow, indColumn, self.typeFigure)
        if result == False:
            self.endGame = True
            return

        # Отрисовываем фигуру
        self.drawFigure()

    def stepRight(self):
        indColumn = self.indColumn + 1
        result = self.isCorrectPosition(self.indRow, indColumn, self.typeFigure)
        if result == False:
            return

        self.cleanFigure()
        self.drawFigure()

    def stepLeft(self):
        indColumn = self.indColumn - 1
        result = self.isCorrectPosition(self.indRow, indColumn, self.typeFigure)
        if result == False:
            return
        self.cleanFigure()
        self.drawFigure()

    def drawFigure(self):
        mas = self.figure[self.nameFigure][self.typeFigure]

        block_row, block_col = 0, 0

        for i in range(self.indRow, len(mas) + self.indRow):
            for j in range(self.indColumn, len(mas[block_row]) + self.indColumn):
                if mas[block_row][block_col] == 1:
                    self.mas[i][j] = 1
                block_col = block_col + 1
            block_col = 0
            block_row = block_row + 1

    def cleanFigure(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                if self.mas[i][j] == 1:
                    self.mas[i][j] = 0

    def completedFigure(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                if self.mas[i][j] == 1:
                    self.mas[i][j] = 2

    # кардинаты зделать
    # кардинату хранить в фигуре
    # функция добавить фигуру в м асив
    # определить кардинаты и хранить их в фигуре
    def rotateFigure(self):
        if len(self.figure[self.nameFigure]) > self.typeFigure + 1:
            typeFigure = self.typeFigure + 1
        else:
            typeFigure = 0

        indColumn = self.indColumn
        indRow = self.indRow

        if self.nameFigure == 0 and typeFigure == 1:
            indColumn = indColumn + 1
        if self.nameFigure == 0 and typeFigure == 2:
            indColumn = indColumn - 1
            indRow = indRow + 1
        if self.nameFigure == 0 and typeFigure == 3:
            indRow = indRow - 1

        if self.nameFigure == 2 and typeFigure == 1:
            indColumn = indColumn - 2
            indRow = indRow + 2
        if self.nameFigure == 2 and typeFigure == 0:
            indColumn = indColumn + 2
            indRow = indRow - 2

        if self.nameFigure == 3 and typeFigure == 0:
            indRow = indRow - 1
        if self.nameFigure == 3 and typeFigure == 2:
            indColumn = indColumn + 1
        if self.nameFigure == 3 and typeFigure == 3:
            indColumn = indColumn - 1
            indRow = indRow + 1

        if self.nameFigure == 4 and typeFigure == 1:
            indRow = indRow - 1
            indColumn = indColumn + 1
        if self.nameFigure == 4 and typeFigure == 0:
            indColumn = indColumn - 1
            indRow = indRow +1

        if self.nameFigure == 5 and typeFigure == 1:
            indRow = indRow - 1
            indColumn = indColumn + 1
        if self.nameFigure == 5 and typeFigure == 0:
            indColumn = indColumn - 1
            indRow = indRow +1

        if self.nameFigure == 6 and typeFigure == 1:
            indRow = indRow + 1
            indColumn = indColumn - 1
        if self.nameFigure == 6 and typeFigure == 2:
            indRow = indRow - 1
        if self.nameFigure == 6 and typeFigure == 0:
            indColumn = indColumn + 1

        result = self.isCorrectPosition(indRow, indColumn, typeFigure)
        if result == False:
            return

        self.cleanFigure()
        self.drawFigure()

    def printFigure(self):
        fig = self.figure[self.nameFigure][self.typeFigure]
        for i in range(0, len(fig)):
            for j in range(0, len(fig[i])):
                print(fig[i][j], end="")
            print()
        print()

    def printMas(self):
        for i in self.mas:
            for j in i:
                print(j, end=" ")
            print()
        print()

