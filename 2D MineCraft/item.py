from abc import *
import ccircle

class Item:
    __metaclass__ = ABCMeta

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.size = 16
        self.image = False
        self.color = (1,1,1)

    @abstractmethod
    def update(self, world):
        pass

    def draw(self):
        if not self.image:
            ccircle.drawRect(self.posX - self.size/2, self.posY - self.size/2, self.size, self.size, self.color[0], self.color[1], self.color[2])
        else:
            self.image.draw(self.posX - self.size/2, self.posY - self.size/2, self.size, self.size, self.color[0], self.color[1], self.color[2])