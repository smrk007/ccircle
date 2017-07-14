from abc import *
from math import *
import ccircle

class Item:

    def __init__(self, posX, posY, window):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.size = 16
        self.image = False
        self.color = (1,1,1)
        self.window = window

    def update(self, world):
        pass

    def draw(self, shift):
        if not self.image:
            self.window.drawRect(self.posX*30 - self.size/2 + shift[0] + 15,
                             self.posY*30 - self.size/2 + shift[1] + 15,
                             self.size,
                             self.size,
                             self.color[0],
                             self.color[1],
                             self.color[2])
        else:
            self.image.draw(self.posX*30 - self.size/2 + shift[0] + 15,
                            self.posY*30 - self.size/2 + shift[1] + 15,
                            self.size,
                            self.size,
                            self.color[0],
                            self.color[1],
                            self.color[2])