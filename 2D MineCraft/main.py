import ccircle
import player
from abc import *

window = ccircle.Window()

'''
Classes:

Tile 
noneTile
dirtTile
'''
class Tile:
    __metaclass__ = ABCMeta

    def __init__(self, posX, posY):
        self.size = 20
        self.posX = posX
        self.posY = posY
        self.health = 100
        self.color = (0,0,0)
        self.solid = False

    @abstractmethod
    def draw(self):
        window.draw(self.posX*self.size, self.posY*self.size, self.size, self.size, self.color[0], self.color[1], self.color[2])
class noneTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
class dirtTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.solid = True
        self.color = (1,1,1)

# World Initialization
worldSize = 100
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        if i < 5:
            row.append(noneTile(i,j))
        else:
            row.append(dirtTile(i,j))
    world.append(row)




while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort

    # Physics and


    # Graphics
    for tile in world:
        tile.draw()

    window.update()