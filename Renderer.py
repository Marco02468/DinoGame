import time

class Renderer:

    x = 20
    y = 15
    grid = [[1 for x in range(20)] for y in range(15)]
    score = 0
    alive = True
    objects = []
    # 0=bush ; 1=bird ; (type, position)

    def __init__(self):
        return

    def jump(self):
        return

    def animate(self):
        for i in range(len(self.objects)):
            self.objects[i][1] = self.objects[i][1] + 1
            self.drawObstacles(self.objects[i])
        return

    def start(self):
        while self.alive:
            self.generateField()
            self.nextObstacle()
            self.animate()
            #getInput
            self.generateDino()
            self.show()
            self.checkLiving()
            self.score += 1
            time.sleep(0.2)
            print("score:", self.score)

    def deleteObstacle(self):
        for i in self.objects:
            if self.objects[i][1] == 0:
                self.objects.pop(self, i)

    def nextObstacle(self):
        if self.score % 10 == 0:
            self.generateBush()
            self.objects.insert(len(self.objects) ,[0, 0])
        elif self.score % 20 == 0:
            self.objects.insert((1, 0))

    def show(self):
        for m in range(15):
            s = ""
            #print("\n")
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            print(s),

    def drawObstacles(self, sprite):
        for m in range(len(self.objects)):
            startpointX = 0 + self.objects[m][1]
            startpointY = 9
            for i in range(4):
                for j in range(3):
                    self.grid[startpointY+i][startpointX+j] = sprite[i][j]

    def spawnDino(self, sprite):
        startpointX = 17
        startpointY = 9
        for i in range(4):
            for j in range(3):
                self.grid[startpointY + i][startpointX + j] = sprite[i][j]

    def checkLiving(self):
        if self.score == 20:
            self.alive = False

    def generateDino(self):
        dino     = [["X", "X",  1 ],
                    [ 1 , "X",  1 ],
                    [ 1 , "X", "X"],
                    [ 1 , "X",  1 ]]
        #print(dino)
        self.spawnDino(dino)

    def generateDuckedDino(self):
        duckedDino =   [[  1 ,  1 ,  1 ],
                        [  1 ,  1 ,  1 ],
                        [ "X", "X", "X"],
                        [  1 , "X",  1 ]]
        #print(duckedDino)
        self.spawnDino(duckedDino)

    def generateBush(self):
        bush = [[ 1, 1],
                ["X",1],
                ["X",1]]
        #print(bush)
        #self.drawObstacle(bush)

    def generateBird(self):
        bush = [["X", "X"],
                [ 1 , 1  ],
                [ 1 , 1  ]]
        #print(bush)
        #self.drawObstacle(bush) return bush

    def generateField(self):
        for m in range(self.x):
            self.grid[14][m] = "-"
            self.grid[13][m] = "-"