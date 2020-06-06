import time

class Renderer:

    mode = "presentation"
    x = 20
    y = 15
    grid = [["." for x in range(20)] for y in range(15)]
    # grid[yPos][xPos]
    score = 0
    alive = True
    objects = []
    # 0=bush ; 1=bird ; (type, position)

    jumpPhase = 0 # default 1; low 2=9 ; medium 3=8 ; high 4=7 ; max 5=6           ##### all minus 1
    jumps = { 0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:0}
    jumpPos = { 0:0, 1:1, 7:1, 2:2, 6:2, 3:3, 5:3, 4:4 }

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
            #time.sleep(0.2)
            print("score: ", self.score)

    def drawDino(self, sprite):
        startpointX = 17
        startpointY = 9 - self.jumpPos[self.jumpPhase]
        for i in range(4):
            for j in range(3):
                self.grid[startpointY + i][startpointX + j] = sprite[i][j]

    def jump(self):
        self.jumpPhase = self.jumps[self.jumpPhase]
        dino = self.generateDino()
        self.drawDino(dino)

    def getInput(self):
        if self.mode == "presentation":
            input = self.ai()
            return input
        elif self.mode == "play":
            print("TODO")
            # input = getInput() and resolve

    def ai(self):
        if self.grid[11][16] == "X" or self.jumpPhase > 0: #jump
            print("jump now!")
            return "jump"
        elif self.grid[10][16] == "X": #duck
            return "duck"
        elif self.grid[11][16] == "." and self.grid[10][16] == "." and self.jumpPhase == 0:
            print("RUN!")
            return "run"

    def move(self, input):
        print("jumpphase", self.jumpPhase)
        if input == "jump":
            print("You jump")
            self.jump()
        elif input == "duck":
            print("You duck")
            self.duck()
        elif input == "run" and self.jumpPhase == 0:
            print("You run")
            dino = self.generateDino()
            self.drawDino(dino)

    def animate(self):
        for i in range(len(self.objects)):
            if self.objects[i][0] == 0: # falls busch and fresh
                bush = self.getBush()
                position = self.objects[i][1]
                self.drawObstacles(bush, position)

            elif self.objects[i][0] == 1: #falls bird
                bird = self.getBird()
                position = self.objects[i][1]
                self.drawObstacles(bird, position)
            self.objects[i][1] = self.objects[i][1] + 1

    def drawObstacles(self, sprite, xPosition):
        for i in range(3):
            self.grid[i+10][xPosition] = sprite[i]

    def deleteObstacle(self):
        for i in range(len(self.objects)-1):
            if self.objects[i][1] == 20:
                self.objects.pop(i)

    def nextObstacle(self):
        if self.score % 10 == 0:
            self.objects.append([0,0])
            #print("spawn bush ", self.score)
            return
        elif self.score % 5 == 0 and False:
            self.objects.append([1,0])
            #print("spawn bush ", self.score)
            return

    def show(self):
        for m in range(15):
            s = ""
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            print(s)

    def checkLiving(self):
        if self.score == 50:
            self.alive = False

    def duck(self):
         print()

    def getBush(self):
        return [".", "X", "X"]

    def getBird(self):
        return ["X",".","."]

    def generateDino(self):
        dino     = [["X", "X",  "." ],
                    [ "." , "X",  "." ],
                    [ "." , "X", "X"],
                    [ "." , "X",  "." ]]
        #print(dino)
        return dino

    def generateDuckedDino(self):
        duckedDino =   [[  "." ,  "." , "." ],
                        [  "." ,  "." , "." ],
                        [ "X"  ,  "X" , "X" ],
                        [  "." ,  "X" ,  "."]]
        #print(duckedDino)
        return duckedDino

    def drawField(self):
        self.grid = [["." for x in range(20)] for y in range(15)]
        for m in range(self.x):
            self.grid[14][m] = "H"
            self.grid[13][m] = "H"
