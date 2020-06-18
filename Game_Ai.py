import time
from TextRenderer import TextRenderer
from Grids import Grid
import random


# from LedRenderer import LedRenderer


class GameAi:
    mode = "presentation"
    x = 20
    y = 15
    grid = [[[0, 0, 0, 0] for x in range(20)] for y in range(15)]
    # grid[yPos][xPos]
    score = 0
    alive = True
    objects = []
    # 0=bush ; 1=bird ; (type, position)

    jumpPhase = 0  # default 1; low 2=9 ; medium 3=8 ; high 4=7 ; max 5=6           ##### all minus 1
    jumps = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 0}
    jumpPos = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 4, 6: 3, 7: 2, 8: 1}

    def start(self):
        while self.alive:
            self.drawField()
            self.nextObstacle()
            self.animate()
            controlls = self.getInput()
            self.move(controlls)
            self.show()
            self.checkLiving()
            self.deleteObstacle()
            self.score += 1
            time.sleep(0.1)
            print("score: ", self.score)
            self.adapter()

    def drawDino(self, sprite):
        startpointX = 17
        startpointY = 9 - self.jumpPos[self.jumpPhase]
        for i in range(4):
            for j in range(3):
                data = [startpointY + i, startpointX + j, sprite[i][j][2], 0]
                # print('data', data)
                self.grid[startpointY + i][startpointX + j] = data

    def jump(self):
        self.jumpPhase = self.jumps[self.jumpPhase]
        dino = self.generateDino()
        self.drawDino(dino)

    def getInput(self):
        if self.mode == "presentation":
            input = self.ai()
            return input
        elif self.mode == "play":
            return
            # input = getInput() and resolve

    def ai(self):
        if self.grid[11][15] == [11, 15, 5, 0] or self.jumpPhase > 0:  # jump
            # print("jump now!")
            return "jump"
        elif self.grid[10][14] == [9, 14, 2, 0] or self.grid[10][15] == [9, 15, 2, 0] or self.grid[10][16] == [9, 16, 2, 0] or self.grid[10][17] == [9, 17, 2, 0] or self.grid[10][18] == [9, 18, 2, 0]:  # duck
            return "duck"
        elif self.grid[11][16] == [11, 16, 7, 0] and self.grid[10][16] == [10, 16, 7, 0] and self.jumpPhase == 0:
            # print("RUN!")
            return "run"

    def move(self, input):
        # print("jumpphase", self.jumpPhase)
        movement = "duck"
        if input == "jump":
            # print("You jump")
            self.jump()
        elif input == "duck":
            # print("You duck")
            dino = self.generateDuckedDino()
            self.duck(dino)
            #movement = "duck"
        elif input == "run" and self.jumpPhase == 0:
            # print("You run")
            dino = self.generateDino()
            self.drawDino(dino)
            #movement = "run"
        #else:
            #self.move(movement)

    def animate(self):
        for i in range(len(self.objects)):
            if self.objects[i][0] == 0:  # falls busch and fresh
                bush = self.getBush()
                position = self.objects[i][1]
                self.drawObstacles(bush, position)

            elif self.objects[i][0] == 1:  # falls bird
                bird = self.getBird()
                position = self.objects[i][1]
                self.drawObstacles(bird, position)
            self.objects[i][1] = self.objects[i][1] + 1

    def drawObstacles(self, sprite, xPosition):
        if sprite == self.getBush():
            for i in range(3):
                sprite[i][1] = xPosition
            for i in range(3):
                self.grid[i + 10][xPosition] = sprite[i]
        elif sprite == self.getBird():
            for i in range(3):
                sprite[i][1] = xPosition + i
            for i in range(3):
                self.grid[i + 10][xPosition] = sprite[i]

    def deleteObstacle(self):
        for i in range(len(self.objects) - 1):
            if self.objects[i][1] == 20:
                self.objects.pop(i)

    def nextObstacle(self):
        obj = [[0, 0], [0, 0], [1, 0]]
        if self.score % 15 == 0:
            self.objects.append(random.choice(obj))
            # print("spawn bush ", self.score)
            return

    def show(self):
        for m in range(15):
            s = ""
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            # print(s)

    def checkLiving(self):
        if self.score == 200:
            self.alive = False

    def duck(self, sprite):
        startpointX = 17
        startpointY = 9
        for i in range(4):
            for j in range(3):
                data = [startpointY + i, startpointX + j, sprite[i][j][2], 0]
                # print('data', data)
                self.grid[startpointY + i][startpointX + j] = data



    def getBush(self):
        return [[12, 0, 5, 0], [11, 1, 5, 0], [10, 1, 5, 0]]


    def getBird(self):
        return [[9, 0, 2, 0], [9, 0, 2, 0], [9, 0, 2, 0]]


    def generateDino(self):
        dino = [[[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 7, 0]],
            [[0, 1, 7, 0], [0, 1, 0, 0], [0, 0, 7, 0]],
            [[0, 0, 7, 0], [0, 1, 0, 0], [0, 1, 0, 0]],
            [[0, 0, 7, 0], [0, 1, 0, 0], [0, 0, 7, 0]]]
    # print(dino)
        return dino


    def generateDuckedDino(self):
        duckedDino = [[[0, 0, 7, 0], [0, 0, 7, 0], [0, 0, 7, 0]],
                  [[0, 0, 7, 0], [0, 0, 7, 0], [0, 0, 7, 0]],
                  [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]],
                  [[0, 0, 7, 0], [0, 1, 0, 0], [0, 0, 7, 0]]]
        # print(duckedDino)
        return duckedDino


    def drawField(self):
        # self.grid = [[[0, 0, 0, 0] for x in range(20)] for y in range(15)]
        for i in range(0, 15):
            for j in range(0, 20):
                self.grid[i][j] = [i, j, 7, 0]

        for m in range(self.x):
            b = [1, 1, 1, 6]
            self.grid[14][m] = [14, m, random.choice(b), 0]
            self.grid[13][m] = [13, m, random.choice(b), 0]


    def adapter(self):
        # l = LedRenderer(15, 20)
        data = []
        for i in range(0, 15):
            for j in range(0, 20):
                data.append(self.grid[i][j])

        r = TextRenderer(15, 20)
        g = Grid(r.width, r.height, r)
        g.render(data)

x = GameAi()
x.start()
