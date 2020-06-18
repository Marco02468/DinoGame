import time
from TextRenderer import TextRenderer
from Grids import Grid
from Ressource import Ressource
import random
import pygame


class Game:

    ressource = Ressource()
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
        dino = self.ressource.generateDino()
        self.drawDino(dino)

    # def getInput(self):
    #   if self.mode == "presentation":
    #      input = self.ai()
    #     return input
    # elif self.mode == "play":
    #   return
    #  input = getInput() and resolve

    # def ai(self):
    #   if self.grid[11][16] == [11, 16, 5, 0] or self.jumpPhase > 0:  # jump
    # print("jump now!")
    #      return "jump"
    # elif self.grid[10][16] == [10, 16, 2, 0]:  # duck
    #    return "duck"
    # elif self.grid[11][16] == [11, 16, 7, 0] and self.grid[10][16] == [10, 16, 7, 0] and self.jumpPhase == 0:
    # print("RUN!")
    #   return "run"

    def move(self, input):
        # print("jumpphase", self.jumpPhase)
        if input == "jump" or self.jumpPhase > 0:
            print("You jump")
            self.jump()
            return self.jumpPhase
        elif input == "duck":
            # print("You duck")
            dino = self.ressource.generateDuckedDino()
            self.duck(dino)
            return self.jumpPhase
        elif input == "run" and self.jumpPhase == 0:
            # print("You run")
            dino = self.ressource.generateDino()
            self.drawDino(dino)
            return self.jumpPhase

    def animate(self):
        for i in range(len(self.objects)):
            if self.objects[i][0] == 0:  # falls busch and fresh
                bush = self.ressource.getBush()
                position = self.objects[i][1]
                self.drawObstacles(bush, position)

            elif self.objects[i][0] == 1:  # falls bird
                bird = self.ressource.getBird()
                position = self.objects[i][1]
                self.drawObstacles(bird, position)
            self.objects[i][1] = self.objects[i][1] + 1

    def drawObstacles(self, sprite, xPosition):
        if sprite == self.ressource.getBush():
            for i in range(3):
                sprite[i][1] = xPosition
            for i in range(3):
                self.grid[i + 10][xPosition] = sprite[i]
        elif sprite == self.ressource.getBird():
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
            return

    def show(self):
        for m in range(15):
            s = ""
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"


    def checkLiving(self):
        if self.score == 100:
            self.alive = False

    def duck(self, sprite):
        startpointX = 17
        startpointY = 9
        for i in range(4):
            for j in range(3):
                data = [startpointY + i, startpointX + j, sprite[i][j][2], 0]
                # print('data', data)
                self.grid[startpointY + i][startpointX + j] = data

    def drawField(self):
        for i in range(0, 15):
            for j in range(0, 20):
                self.grid[i][j] = [i, j, 7, 0]

        for m in range(self.x):
            b = [1, 1, 1, 6]
            self.grid[14][m] = [14, m, random.choice(b), 0]
            self.grid[13][m] = [13, m, random.choice(b), 0]

    def isCollision(self):
        pass

    def adapter(self):
        # l = LedRenderer(15, 20)
        data = []
        for i in range(0, 15):
            for j in range(0, 20):
                data.append(self.grid[i][j])

        r = TextRenderer(15, 20)
        g = Grid(r.width, r.height, r)
        g.render(data)

pygame.init()
pygame.display.set_mode((100, 100))
pygame.joystick.init()
x = Game()
jumpPhase = 0
movement = "run"

while x.alive:
    x.drawField()
    x.nextObstacle()
    x.animate()
    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:  # or jumpPhase == 0:
            x.move("duck")
            movement = "duck"
        elif (event.key == pygame.K_SPACE or jumpPhase > 0) and movement == "run":
            print("space")
            jumpPhase = x.move("jump")

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or jumpPhase == 0:
            jumpPhase = x.move("run")
            movement = "run"
    else:
        x.move(movement)

    x.show()
    x.checkLiving()
    x.deleteObstacle()
    x.score += 1
    time.sleep(0.1)
    print("score: ", x.score)
    x.isCollision()

    x.adapter()
