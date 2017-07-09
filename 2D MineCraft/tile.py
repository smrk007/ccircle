#import ccircle
from abc import *

class Tile:

    __metaclass__ = ABCMeta


    def __init__(self, posX, posY):
        self.size = 20
        self.posX = posX
        self.posY = posY
        self.health = 100
        self.color = (0,0,0)

    @abstractmethod
    def draw(self):
        # Problem, what really is window...?
        window.draw(self.posX*self.size, self.posY*self.size, self.size, self.size, self.color[0], self.color[1], self.color[2])


class noneTile(Tile):

    def __init__(self, posX, posY):
        super().__init__(posX, posY)

class dirtTile(Tile): pass

