class Renderer:

    x = 20
    y = 15
    grid = [[0 for i in range(20)] for j in range(15)]

    def __init__(self):
        return

    def move(self):
        return

    def start(self):
        self.generateField()
        self.generateDino()
        self.show()

    def show(self):
        for m in range(15):
            s = ""
            #print("\n")
            for n in range(20):
                s += str(self.grid[m][n]) + "\t"
            print(s),

    def spawn(self, sprite):
        startpointX = 17
        startpointY = 9
        for i in range(4):
            for j in range(3):
                self.grid[startpointY+i][startpointX+j] = sprite[i][j]


    def generateDino(self):
        dino     = [[["X"], ["X"], [ 0  ]],
                    [[ 0  ], ["X"], [ 0  ]],
                    [[ 0  ], ["X"], ["X"]],
                    [[ 0  ], ["X"], [ 0  ]]]
        #print(dino)
        self.spawn(dino)

    def generateDuckedDino(self):
        duckedDino =   [[ [ 0  ], [ 0  ], [ 0  ]],
                        [ [ 0  ], [ 0  ], [ 0  ]],
                        [ ["X"], ["X"], ["X"]],
                        [ [ 0  ], ["X"], [ 0  ]]]
        #print(duckedDino)
        self.spawn(duckedDino)

    def generateBush(self):
        bush = [[ [0],[ 0  ],[ 0  ] ],
                [ [0],[ 0  ],[ 0  ] ],
                [ [0],["X"],["X"] ],
                [ [0],["X"],["X"] ]]
        #print(bush)
        self.spawn(bush)

    def generateBird(self):
        bush = [[[0], ["X"], ["X"]],
                [[0], ["X"], ["X"]],
                [[0], [ 0 ], [ 0 ]],
                [[0], [ 0 ], [ 0 ]]]
        #print(bush)
        self.spawn(bush)
        return bush

    def generateField(self):
        for m in range(self.x):
            self.grid[14][m] = "X"
            self.grid[13][m] = "X"