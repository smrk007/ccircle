import ccircle
from item import *

class Tile:
    # __metaclass__ = ABCMeta

    def __init__(self, xSpace, ySpace, window):
        self.size = 30
        self.xSpace = xSpace
        self.ySpace = ySpace
        self.health = 100
        self.color = (135/256, 206/256, 250/256)
        self.solid = False
        self.window = window
        self.type = "tile"

    #@abstractmethod
    def draw(self, shift, sprite):
        if self.type == 'air'
            self.window.drawRect(self.xSpace*self.size + shift[0],
                                self.ySpace*self.size +  shift[1],
                                self.size,
                                self.size,
                                self.color[0],
                                self.color[1],
                                self.color[2],
                                self.getAlpha())
        if self.type == dirt:
            sprite[0].draw(self.xSpace*self.size + shift[0],
                           self.ySpace*self.size + shift[1],
                           self.size,
                           self.size,
                           32,
                           0,
                           16,
                           16)

    def getAlpha(self):
        if self.type == 'air':
            return 0
        return (100+self.health)/200

    def setType(self,tileType):
        if tileType == "dirt":
            self.solid = True
            self.color = [1,1,1]
            self.type = "dirt"
        if tileType == "air":
            self.color = (135/256, 206/256, 250/256)
            self.type = "air"
            self.solid = False

    def update(self, window, objects):
        if self.health < 100:
            if self.type == "air":
                self.health = 100
            self.health += 0.003
        if self.health > 100:
            self.health = 100
        if self.health < 0:
            objects.append(Item((self.xSpace+0.5)*self.size, (self.ySpace+0.5)*self.size, window))
            self.setType('air')
            self.health = 100