import random


class Figure:
    #Массив представляющий собой поле
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
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #Переменная для подсчета очков
    score = 0
    #Переменная которая сообщает закончилась игра или еще идет
    #False - игра еще не закончена
    #True - игра закончилась
    endGame = False

    #Перменными Tu Tr Td Tl обозначаются массивы обозначающие фигуры,
    # где 0 - пусто 1 - заполненно
    Tu = [[0, 1, 0], [1, 1, 1]]
    Tr = [[1, 0], [1, 1], [1, 0]]
    Td = [[1, 1, 1], [0, 1, 0]]
    Tl = [[0, 1], [1, 1], [0, 1]]
    # Переменной T обозначается фигура и массив ее положений
    T = [Tu, Tr, Td, Tl]

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

    Zh = [[1, 1, 0], [0, 1, 1]]
    Zv = [[0, 1], [1, 1], [1, 0]]
    Z = [Zh, Zv]

    Sh = [[0, 1, 1], [1, 1, 0]]
    Sv = [[1, 0], [1, 1], [0, 1]]
    S = [Sh, Sv]

    Lr = [[1, 0], [1, 0], [1, 1]]
    Ld = [[1, 1, 1], [1, 0, 0]]
    Ll = [[1, 1], [0, 1], [0, 1]]
    Lu = [[0, 0, 1], [1, 1, 1]]
    L = [Lr, Ld, Ll, Lu]

    #Список для хранения фигур
    figure = [T, O, I, J, Z, S, L]

    #Обозначает индекс фигуру в массиве figure
    nameFigure = None
    #Обозначает индекс положения фигуры в подмассивах T, O, I, J, Z, S, L
    typeFigure = None
    #Генерируем следующую фигуру
    nameNextFigure = random.randint(0, len(figure) - 1)
    typeNextFigure = random.randint(0, len(figure[nameNextFigure]) - 1)

    #Создаем случайным образом и случайным образом задаем ей положение,
    #так же генерируем следующую фигуру
    def createFigure(self):
        self.nameFigure = self.nameNextFigure
        self.typeFigure = self.typeNextFigure
        self.nameNextFigure = random.randint(0, len(self.figure) - 1)
        self.typeNextFigure = random.randint(0, len(self.figure[self.nameNextFigure]) - 1)

    #Очищаем массив
    def emptyField(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                self.mas[i][j] = 0
        self.score = 0

    #Проверяет собрался ряд или нет
    def checkCompleted(self):
        mas = self.mas
        #Считаем сколько строк собралось
        countScore = 0
        for i in range(0, len(mas)):
            #Флаг который говорит, что строка собралась, если встретим 0 или 1,
            # что означает что строка не полностью собрана, то меняем на False
            flag = True
            for j in range(0, len(mas[i])):
                if mas[i][j] == 0 or mas[i][j] == 1:
                    flag = False
            #Если строка собралась, то удаляем ее, в начало массива
            # добавляем новую пустую строку и считаем ее в перменной countScore
            if flag:
                zeros_list = [0] * len(mas[0])
                mas.pop(i)
                mas.insert(0, zeros_list)
                countScore = countScore + 1

        #Проверяем сколько собралось строк и прибавляем очки
        if countScore == 1:
            self.score = self.score + 100
        elif countScore == 2:
            self.score = self.score + 300
        elif countScore == 3:
            self.score = self.score + 700
        elif countScore == 4:
            self.score = self.score + 1500

    #Делаем шаг вниз и проверяем можно ли его сделать,
    #если нельзя то добавляем новую фигуру
    def stepDown(self):
        indRow = self.indRow + 1
        result = self.isCorrectPosition(indRow, self.indColumn, self.typeFigure)
        #Если фигуру нельзя больше отпустить
        if result == False:
            #Проверяем собрался ли ряд
            self.completedFigure()
            #Проверяем установилась ли фигура
            self.checkCompleted()
            #Создаем новую фигуру и добавляем в начало массива
            self.createFigure()
            self.addFigure()
            #Считаем очки за установленную фигуру
            self.score = self.score + 10
            return
        self.cleanFigure()
        self.drawFigure()

    #Проверяет возможность задать новую позицию фигуре
    #вправо, влево или вниз
    def isCorrectPosition(self, indRow, indColumn, typeFigure):
        mas = self.figure[self.nameFigure][typeFigure]

        #Задаем индексы для массива фигуры
        block_row, block_col = 0, 0

        #Дальше проверяем условия по которым понимаем можно ли сдвинуть фигуру в массиве
        if indColumn < 0 or indColumn + len(mas[0]) > len(self.mas[0]):
            return False

        if indRow < 0 or indRow + len(mas) > len(self.mas):
            return False

        for i in range(indRow, len(mas) + indRow):
            for j in range(indColumn, len(mas[block_row]) + indColumn):
                if mas[block_row][block_col] == 1 and self.mas[i][j] == 2:
                    return False
                block_col = block_col + 1
            block_col = 0
            block_row = block_row + 1

        self.typeFigure = typeFigure
        self.indRow = indRow
        self.indColumn = indColumn
        return True

    #Функция добавляет фигуру в начало массива
    def addFigure(self):
        mas = self.figure[self.nameFigure][self.typeFigure]

        #Задаем столбец и строку в которой отрисуем фигуру, в зависимости от размера фигуры смещаем
        indRow, indColumn = 0, 0
        if len(mas[0]) == 4:
            indColumn = int((len(self.mas[0]) - 1) / 2) - 1
        if len(mas[0]) == 3:
            indColumn = int((len(self.mas[0]) - 1) / 2) - 1
        if len(mas[0]) == 2 or len(mas[0]) == 1:
            indColumn = int((len(self.mas[0]) - 1) / 2)

        #Проверяем можно ли вставить фигуру в начало, если позиция не корректная, то завершаем игру
        result = self.isCorrectPosition(indRow, indColumn, self.typeFigure)
        if result == False:
            self.endGame = True
            return

        # Отрисовываем фигуру
        self.drawFigure()

    #Функция смещает фигуру вправо
    def stepRight(self):
        indColumn = self.indColumn + 1
        result = self.isCorrectPosition(self.indRow, indColumn, self.typeFigure)
        if result == False:
            return

        self.cleanFigure()
        self.drawFigure()

    # Функция смещает фигуру влево
    def stepLeft(self):
        indColumn = self.indColumn - 1
        result = self.isCorrectPosition(self.indRow, indColumn, self.typeFigure)
        if result == False:
            return
        self.cleanFigure()
        self.drawFigure()

    #Фунция рисует фигуру в массиве
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

    #Очищаем поле от положения старой фигуры
    def cleanFigure(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                if self.mas[i][j] == 1:
                    self.mas[i][j] = 0

    #Функция задает окончательное положение фигуре на поле
    def completedFigure(self):
        for i in range(0, len(self.mas)):
            for j in range(0, len(self.mas[i])):
                if self.mas[i][j] == 1:
                    self.mas[i][j] = 2

    #Функция поворачивает фигуру
    def rotateFigure(self):
        #Проверяем можно ли задать фигуре следующее положение, если нельзя возвращаем в первое
        if len(self.figure[self.nameFigure]) > self.typeFigure + 1:
            typeFigure = self.typeFigure + 1
        else:
            typeFigure = 0

        indColumn = self.indColumn
        indRow = self.indRow

        #Каждая фигура и ее варианты имеют свой центр, смещаем координаты для установки на поле
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
            indRow = indRow + 1

        if self.nameFigure == 5 and typeFigure == 1:
            indRow = indRow - 1
            indColumn = indColumn + 1
        if self.nameFigure == 5 and typeFigure == 0:
            indColumn = indColumn - 1
            indRow = indRow + 1

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

    #Выводит массив фигуры в консоль для отладки
    def printFigure(self):
        fig = self.figure[self.nameFigure][self.typeFigure]
        for i in range(0, len(fig)):
            for j in range(0, len(fig[i])):
                print(fig[i][j], end="")
            print()
        print()

    #Выводит массив поля в консоль для отладки
    def printMas(self):
        for i in self.mas:
            for j in i:
                print(j, end=" ")
            print()
        print()
