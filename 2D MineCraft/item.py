import ccircle
from math import *

class Item:

    def __init__(self, posX, posY, window):
        self.posX = int(posX)
        self.posY = int(posY)
        self.velX = None
        self.velY = 0
        self.size = 16
        self.image = False
        self.color = (1,1,1)
        self.window = window

    def update(self, world):
        ySpace = floor(self.posY/30)  # Assuming that the world tiles have a size of 30
        xSpace = floor(self.posX/30)  # Assuming that the world tiles haze a size of 30
        if world[ySpace+1][xSpace].solid and (((self.posY + self.velY) > (ySpace+1)*30) or (self.posY >= (ySpace+1)*30 - self.size/2)):
            self.posY = (ySpace+1)*30 - self.size/2
            self.velY = 0
        else:
            self.posY += self.velY
            self.velY += 0.001



    def draw(self, shift):
        if not self.image:
            self.window.drawRect(self.posX - self.size/2 + shift[0],
                                 self.posY - self.size/2 + shift[1],
                                 self.size,
                                 self.size,
                                 self.color[0],
                                 self.color[1],
                                 self.color[2])
        else:
            self.image.draw(self.posX - self.size/2 + shift[0],
                            self.posY - self.size/2 + shift[1],
                            self.size,
                            self.size)