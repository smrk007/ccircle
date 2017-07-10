import ccircle
from abc import *
from math import floor

window = ccircle.Window()

'''
Functions:

keyDown
'''

def keyDown(): # Returns string of whatever key is down, None if no key

    out = {}

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in letters:
        if ccircle.isKeyDown(char):
            out[char] = True
        else:
            out[char] = False

    etc = ['backspace','enter','esc','space','left','right','up','down']
    for key in etc:
        if ccircle.isKeyDown(key):
            out[key] = True
        else:
            out[key] = False

    return out

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
        self.size = 15
        self.jump = True

    def move(self, keys):
        self.velX = 0
        if keys['left']:
            self.velX = -1.0
        if keys['right']:
            self.velX = 1.0
        if keys['up'] and self.jump:
            self.velY = -2
            self.jump = False


    def draw(self):
        window.drawCircle(self.posX, self.posY, self.size, self.color[0], self.color[1], self.color[2])

# World Initialization
worldSize = 20
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        if i == 4 and j == 7:
            row.append(dirtTile(j,i))
        elif i < 5:
            row.append(noneTile(j,i))
        else:
            row.append(dirtTile(j,i))
    world.append(row)


player = Player(30,30)


while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort

    # Physics and

    player.move(keyDown())  # Sets an intended velocity

    xSpace = int(floor(player.posX / world[0][0].size))
    ySpace = int(floor(player.posY / world[0][0].size))

    # Player X dimension collision and motion
    if player.posX + player.velX < xSpace*world[0][0].size + player.size and world[ySpace][xSpace-1].solid:
        player.posX = xSpace*world[0][0].size + player.size
    elif player.posX + player.velX > (xSpace+1)*world[0][0].size - player.size and world[ySpace][xSpace+1].solid:
        player.posX = (xSpace+1)*world[0][0].size - player.size
    else:
        player.posX += player.velX

    # Player Y dimension collision and motion
    if player.posY + player.velY < ySpace*world[0][0].size + player.size and world[ySpace-1][xSpace].solid:
        player.posY = ySpace*world[0][0].size + player.size
    elif player.posY + player.velY > (ySpace+1)*world[0][0].size - player.size and world[ySpace+1][xSpace].solid:
        player.posY = (ySpace+1)*world[0][0].size - player.size
        player.jump = True
    else:
        player.velY += 0.03

        player.posY += player.velY




    # Graphics
    for layer in world:
        for tile in layer:
            tile.draw()
    player.draw()

    window.update()