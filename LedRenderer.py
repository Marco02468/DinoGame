import neopixel
import board

from Renderer2 import Renderer

class LedRenderer(Renderer):
        def __init__(self, width, height):
                Renderer.__init__(self, width, height)
                self.strip = neopixel.NeoPixel(board.D18, self.width * self.height, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)
                self.__computePermutation__()

        def __coord2Index__(self,x,y):
                x = (self.width-1) - x
                if x % 2 == 1:
                        y = (self.height-1) - y
                return y + self.height * x

        def __computePermutation__(self):
                self.permutation = [0]*self.width*self.height
                i = 0
                for y in range(self.height):
                        for x in range(self.width):
                                self.permutation[i] = self.__coord2Index__(x,y)
                                i += 1
        def clear(self):
                for i in range(self.width*self.height):
                        self.strip[i] = (0,0,0)
                self.strip.show()

        def setPixel(self,x,y,rgb):
                i = self._coord2Index(x,y)
                self.strip[i] = (int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))

        def render(self, data):
                for i in range(self.width*self.height):
                        rgb = data[i]
                        self.strip[self.permutation[i]] = (int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
                self.strip.show()