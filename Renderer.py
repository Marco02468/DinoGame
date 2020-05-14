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
        self.show()

    def show(self):
        for m in range(self.y):
            print(self.grid[m])

    def spawn(self):
        return

    def generateDino(self):
        dino     = [[["X"], ["X"], [ 0  ]],
                    [[ 0  ], ["X"], [ 0  ]],
                    [[ 0  ], ["X"], ["X"]],
                    [[ 0  ], ["X"], [ 0  ]]]
        return dino

    def generateDuckedDino(self):
        duckedDino =   [[ [ 0  ], [ 0  ], [ 0  ]],
                        [ [ 0  ], [ 0  ], [ 0  ]],
                        [ ["X"], ["X"], ["X"]],
                        [ [ 0  ], ["X"], [ 0  ]]]
        return duckedDino

    def generateBush(self):
        bush = [[ [0],[ 0  ],[ 0  ] ],
                [ [0],[ 0  ],[ 0  ] ],
                [ [0],["X"],["X"] ],
                [ [0],["X"],["X"] ]]
        return bush

    def generateBird(self):
        bush = [[[0], ["X"], ["X"]],
                [[0], ["X"], ["X"]],
                [[0], [ 0 ], [ 0 ]],
                [[0], [ 0 ], [ 0 ]]]
        return bush

    def generateField(self):
        for m in range(self.x):
            self.grid[14][m] = "X"
            self.grid[13][m] = "X"