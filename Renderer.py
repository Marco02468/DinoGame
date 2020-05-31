import time

class Renderer:

    mode = "presentation"
    x = 20
    y = 15
    grid = [["." for x in range(20)] for y in range(15)]
    score = 0
    alive = True
    objects = []
    # 0=bush ; 1=bird ; (type, position)

    jumpPhase = 0 # default 0; low 1=8 ; medium 2=7 ; high 3=6 ; max 4=5 ; ducked -1
    jumps = {0:1, 1:2, 3:4, 5:6, 6:7, 7:8, 8:0}

    def start(self):
        while self.alive:
            self.generateField()
            self.nextObstacle()
            self.animate()
            self.getInput()
            self.generateDino()
            self.show()
            self.checkLiving()
            self.deleteObstacle()
            self.score += 1
            #time.sleep(0.2)
            print("score: ", self.score)

    def getInput(self):
        if self.mode == "presentation":
            input = self.ai()
        elif self.mode == "play":
            print("TODO")


    def ai(self):
        if self.grid[11][16] == "X": #jump
            return "jump"
        if self.grid[10][16] == "X": #duck
            return "duck"

    def jump(self):
        dino = self.generateDino()
        self.drawDino(dino)

    def drawDino(self, sprite):
        startpointX = 17
        startpointY = 9
        if self.jumpPhase > -1:
            startpointY += self.jumpPhase
            print("jump", self.jumpPhase)
            self.jumpPhase = self.jumps[self.jumpPhase] * -1

        for i in range(4):
            for j in range(3):
                self.grid[startpointY + i][startpointX + j] = sprite[i][j]

    def move(self, input):
        if input == "jump" or self.jumpPhase > 0:
            self.jump()
        elif input == "duck":
            self.duck()

    def animate(self):
        for i in range(len(self.objects)):
            if self.objects[i][0] == 0: # falls busch and fresh
                bush = self.generateBush()
                position = self.objects[i][1]
                self.drawObstacles(bush, position)

            elif self.objects[i][0] == 1: #falls bird
                bird = self.generateBird()
                position = self.objects[i][1]
                self.drawObstacles(bird, position)
            self.objects[i][1] = self.objects[i][1] + 1

    def drawObstacles(self, sprite, xPosition):
        for i in range(3):
            self.grid[i][xPosition] = sprite[i]

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
        if self.score == 40:
            self.alive = False

    def duck(self):
         print()

    def generateDino(self):
        dino     = [["X", "X",  "." ],
                    [ "." , "X",  "." ],
                    [ "." , "X", "X"],
                    [ "." , "X",  "." ]]
        #print(dino)
        self.drawDino(dino)

    def generateDuckedDino(self):
        duckedDino =   [[  "." ,  "." , "." ],
                        [  "." ,  "." , "." ],
                        [ "X"  ,  "X" , "X" ],
                        [  "." ,  "X" ,  "."]]
        #print(duckedDino)
        self.drawDino(duckedDino)

    def generateBush(self):
        return [".", "X", "X"]

    def generateBird(self):
        return ["X",".","."]

    def generateField(self):
        self.grid = [["." for x in range(20)] for y in range(15)]
        for m in range(self.x):
            self.grid[14][m] = "H"
            self.grid[13][m] = "H"

    def generateDino(self):
        dino     = [["X", "X",  "." ],
                    [ "." , "X",  "." ],
                    [ "." , "X", "X"],
                    [ "." , "X",  "." ]]
        #print(dino)
        self.drawDino(dino)

    def generateDuckedDino(self):
        duckedDino =   [[  "." ,  "." , "." ],
                        [  "." ,  "." , "." ],
                        [ "X"  ,  "X" , "X" ],
                        [  "." ,  "X" ,  "."]]
        #print(duckedDino)
        self.drawDino(duckedDino)