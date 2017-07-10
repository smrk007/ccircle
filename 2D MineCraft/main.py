import ccircle
from abc import *
from math import *

window = ccircle.Window("2D Minecraft", 450, 450)
center = (225, 225)

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

def camShift(player, center):
    x = center[0] - player.posX
    y = center[1] - player.posY
    return (x,y)

'''
Classes:

Tile 
noneTile
dirtTile

player
'''
class Tile:
    # __metaclass__ = ABCMeta

    def __init__(self, posX, posY):
        self.size = 30
        self.posX = posX
        self.posY = posY
        self.health = 100
        self.color = [0,0,0]
        self.solid = False

    #@abstractmethod
    def draw(self, shift):
        window.drawRect(self.posX*self.size + shift[0],
                        self.posY*self.size +  shift[1],
                        self.size,
                        self.size,
                        self.color[0]*((100+self.health)/200),
                        self.color[1]*((100+self.health)/200),
                        self.color[2]*((100+self.health)/200))

    def setType(self,tileType):
        if tileType == "dirt":
            self.solid = True
            self.color = [1,1,1]
        if tileType == "air":
            self.color = [0,0,0]
            self.solid = False

    def update(self):
        if self.health <= 0:
            self.setType('air')
            self.health = 100

'''
class noneTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
class dirtTile(Tile):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.solid = True
        self.color = (1,1,1)
'''

class Player:

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.color = (1,1,1)
        self.size = 10
        self.jump = True
        self.direction = 'right'
        self.target = (0,0)

    def move(self, keys):
        self.velX = 0
        if keys['left'] or keys['a']:
            self.velX = -0.3
            self.direction = 'left'
        if keys['right'] or keys['d']:
            self.velX = 0.3
            self.direction = 'right'
        if (keys['up'] or keys['w']) and self.jump:
            self.velY = -0.5
            self.jump = False
            self.direction = 'up'
        if (keys['down']):
            self.direction = 'down'

    def draw(self, shift):
        window.drawCircle(self.posX + shift[0], self.posY + shift[1], self.size, self.color[0], self.color[1], self.color[2])

    def update(self):
        if self.direction == 'left':
            self.target = (self.posX - 30, self.posY)
        if self.direction == 'right':
            self.target = (self.posX + 30, self.posY)
        if self.direction == 'up':
            self.target = (self.posX, self.posY - 30)
        if self.direction == 'down':
            self.target = (self.posX, self.posY + 30)

# World Initialization
worldSize = 300
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        if i == 4 and j == 7:
            tile = Tile(j,i)
            tile.setType('dirt')
            row.append(tile)
        elif i == 2 and j == 7:
            tile = Tile(j,i)
            tile.setType('dirt')
            row.append(tile)
        elif i < 5:
            tile = Tile(j,i)
            tile.setType('air')
            row.append(tile)
        else:
            tile = Tile(j,i)
            tile.setType('dirt')
            row.append(tile)
    world.append(row)

player = Player(30,30)


while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort

    # Physics and Interactions
    player.move(keyDown())  # Sets an intended velocity
    xSpace = int(floor(player.posX / world[0][0].size))
    ySpace = int(floor(player.posY / world[0][0].size))

    if ccircle.isKeyDown('space'):
        tX = int(floor(player.target[0] / world[0][0].size))
        tY = int(floor(player.target[1] / world[0][0].size))
        world[tY][tX].health -= 0.1


    # Player X dimension collision and motion
    if player.posX + player.velX < xSpace*world[0][0].size + player.size and world[ySpace][xSpace-1].solid:
        player.posX = xSpace*world[0][0].size + player.size
    elif player.posX + player.velX > (xSpace+1)*world[0][0].size - player.size and world[ySpace][xSpace+1].solid:
        player.posX = (xSpace+1)*world[0][0].size - player.size
    else:
        player.posX += player.velX

    # Player Y dimension collision and motion
    if player.posY + player.velY < ySpace*world[0][0].size + player.size and world[ySpace-1][xSpace].solid:
        player.posY = ySpace*world[0][0].size + player.size + 1
    elif player.posY + player.velY > (ySpace+1)*world[0][0].size - player.size and world[ySpace+1][xSpace].solid:
        player.posY = (ySpace+1)*world[0][0].size - player.size
        player.jump = True
    else:
        player.velY += 0.003

        player.posY += player.velY




    # Graphics

    shift = camShift(player, center)

    leftBound = max(floor(xSpace-center[0]/world[0][0].size), 0)
    rightBound = min(worldSize-1, int(ceil(xSpace + center[0]/world[0][0].size)))
    topBound = max(floor(ySpace-center[1]/world[0][0].size), 0)
    botBound = min(worldSize-1, int(ceil(ySpace + center[0]/world[0][0].size)))

    for i in range(topBound, botBound+1):
        for j in range(leftBound, rightBound+1):
            world[i][i].update()
            world[i][j].draw(shift)
    player.update()
    player.draw(shift)

    window.update()