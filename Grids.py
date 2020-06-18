colors = [
    [0, 1, 1],  # cyan 0
    [1, 1, 0],  # yellow 1
    [1, 0, 1],  # magenta 2
    [0, 0, 1],  # blue 3
    [0.6, 0.15, 0],  # brown 4
    [0, 1, 0],  # green 5
    [1, 0, 0],  # red 6
    [0, 0, 0]  # black 7
]

class Grid():
        def __init__(self, width, height, renderer):
                self.width = width
                self.height = height
                self.renderer = renderer
                self.clear()

        def clear(self):
                self.data = [-1] * self.width * self.height

        def setPixel(self, x, y, val):
                self.data[self.__gridIndex(x,y)] = val

        def getPixel(self, x, y):
                return self.data[self.__gridIndex(x,y)]

        def __gridIndex(self, x, y):
                return x + self.width * y

        def render(self, spritePixels):
                color = [[0, 0, 0]] * len(self.data)

                for i in range(len(self.data)):
                        color[i] = colors[self.data[i]]

                for p in spritePixels:
                        index = self.__gridIndex(p[0], p[1])
                        color[index] = colors[p[2]] + [p[3]]

                        color[index] = [x[0] * (1 - p[3]) + x[1] * p[3] for x in zip(color[index], color[p[2]])]

                self.renderer.render(color)

        def __str__(self):
                r = ""
                for i in range(self.height):
                        r += str(self.data[i*self.width:(i+1)*self.width])+"\n"
                return r