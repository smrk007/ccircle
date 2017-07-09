import ccircle
from abc import *

window = ccircle.Window()

'''
Functions:

keyDown
'''

def keyDown(): # Returns string of whatever key is down, None if no key

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in letters:
        if ccircle.isKeyDown(char):
            return char

    etc = ['backspace','enter','esc','space','left','right','up','down']
    for key in etc:
        if ccircle.isKeyDown(key):
            return key

    return None # If no key is down

'''
Classes:

Tile 
noneTile
dirtTile

player
'''
class Tile:
    __metaclass__ = ABCMeta

    def __init__(self, posX, posY):
        self.size = 30
        self.posX = posX
        self.posY = posY
        self.health = 100
        self.color = (0,0,0)
        self.solid = False

    @abstractmethod
    def draw(self):
        window.drawRect(self.posX*self.size, self.posY*self.size, self.size, self.size, self.color[0], self.color[1], self.color[2])
class noneTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
class dirtTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.solid = True
        self.color = (1,1,1)

class Player:

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.color = (1,1,1)

    def move(self, key):
        self.velX = 0
        self.velY = 0
        if key == 'left':
            self.velX = -0.5
        if key == 'right':
            self.velX = 0.5

    def draw(self):
        window.drawCircle(self.posX, self.posY, 15, self.color[0], self.color[1], self.color[2])

# World Initialization
worldSize = 20
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        if i < 10:
            row.append(noneTile(j,i))
        else:
            row.append(dirtTile(j,i))
    world.append(row)

player = Player(30,30)


while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort

    # Physics and

    player.move(keyDown())
    player.posX += player.velX
    player.posY += player.velY

    # Graphics
    for layer in world:
        for tile in layer:
            tile.draw()
    player.draw()

    window.update()