import ccircle
from item import *

class Tile:
    # __metaclass__ = ABCMeta

    def __init__(self, posX, posY, window):
        self.size = 30
        self.posX = posX
        self.posY = posY
        self.health = 100
        self.color = [0,0,0]
        self.solid = False
        self.window = window
        self.type = "tile"

    #@abstractmethod
    def draw(self, shift):
        self.window.drawRect(self.posX*self.size + shift[0],
                             self.posY*self.size +  shift[1],
                             self.size,
                             self.size,
                             self.color[0]*((200+self.health)/300),
                             self.color[1]*((200+self.health)/300),
                             self.color[2]*((200+self.health)/300))

    def setType(self,tileType):
        if tileType == "dirt":
            self.solid = True
            self.color = [1,1,1]
        if tileType == "air":
            self.color = [0,0,0]
            self.solid = False

    def update(self, window, objects):
        if self.health < 100:
            self.health += 0.003
        if self.health > 100:
            self.health = 100
        if self.health < 0:
            objects.append(Item(self.posX, self.posY, window))
            self.setType('air')
            self.health = 100