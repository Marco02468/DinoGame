class Test:

    x=20
    y=15

    grid = [[1 for x in range(20)] for y in range(15)]

    def run(self):
        self.generateField()
        self.show()


    def drawObstacles(self, sprite):
        for m in range(len(self.objects)):
            startpointX = 0 + self.objects[m][1]
            startpointY = 9
            for i in range(3):
                for j in range(2):
                    self.grid[startpointY+i][startpointX+j] = sprite[i][j]

    def testSprite(self):
        sprite = [["X", "X"],
                ["X", "X"],
                ["X", "X"]]
        return sprite


    def generateField(self):
        for m in range(self.x):
            self.grid[14][m] = "-"
            self.grid[13][m] = "-"

    def show(self):
        for m in range(15):
            s = ""
            #print("\n")
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            print(s)