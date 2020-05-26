import time

class Renderer:

    x = 20
    y = 15
    grid = [["." for x in range(20)] for y in range(15)]
    score = 0
    alive = True
    objects = []
    # 0=bush ; 1=bird ; (type, position)

    def start(self):
        while self.alive:
            self.generateField()
            self.nextObstacle()
            self.animate()
            #getInput
            self.generateDino()
            self.show()
            self.checkLiving()
            self.deleteObstacle()
            self.score += 1
            #time.sleep(0.2)
            print("score:", self.score)

    def jump(self):
        return

    def animate(self):
        for i in range(len(self.objects)):
            if i > 1:
                blank = [",", ",", ","]
                self.drawObstacles(blank, i - 1)
            elif self.objects[i][0] == 0: # falls busch
                bush = self.generateBush()
                position = self.objects[i][1]
                print("p ", position)
                self.drawObstacles(bush, position)
                self.objects[i][1] = self.objects[i][1] + 1

            elif self.objects[i][0] == 1: #falls bird
                bird = self.generateBird()
                position = self.objects[i][1]
                self.drawObstacles(bird, position)
                self.objects[i][1] = self.objects[i][1] + 1

    def drawObstacles(self, sprite, index):
        print("xP", self.objects[index][0])
        print("d ", self.objects)
        xPosition = self.objects[index][0]
        for i in range(3):
            self.grid[i][xPosition] = sprite[i]

    def deleteObstacle(self):
        for i in range(len(self.objects)-1):
            if self.objects[i][1] == 19:
                self.objects.pop(i)

    def nextObstacle(self):
        if self.score % 5 != 0:
            return
        elif self.score % 10 == 0:
            self.objects.append([0,0])
            return
        elif self.score % 5 == 0:
            self.objects.append([1,0])
            return

    def show(self):
        for m in range(15):
            s = ""
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            print(s)

    def spawnDino(self, sprite):
        startpointX = 17
        startpointY = 9
        for i in range(4):
            for j in range(3):
                self.grid[startpointY + i][startpointX + j] = sprite[i][j]

    def checkLiving(self):
        if self.score == 40:
            self.alive = False

    def generateDino(self):
        dino     = [["X", "X",  "." ],
                    [ "." , "X",  "." ],
                    [ "." , "X", "X"],
                    [ "." , "X",  "." ]]
        #print(dino)
        self.spawnDino(dino)

    def generateDuckedDino(self):
        duckedDino =   [[  "." ,  "." , "." ],
                        [  "." ,  "." , "." ],
                        [ "X"  ,  "X" , "X" ],
                        [  "." ,  "X" ,  "."]]
        #print(duckedDino)
        self.spawnDino(duckedDino)

    def generateBush(self):
        return [".", "X", "X"]

    def generateBird(self):
        return ["X",".","."]

    def generateField(self):
        for m in range(self.x):
            self.grid[14][m] = "H"
            self.grid[13][m] = "H"