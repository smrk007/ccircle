import ccircle
from tile import Tile
from math import *
from etc import *
from player import *
from item import *

window = ccircle.Window("2D Minecraft", 450, 450)
center = (225, 225)

# World Initialization
worldSize = 100
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        if i == 4 and j == 7:
            tile = Tile(j, i, window)
            tile.setType('dirt')
            row.append(tile)
        elif i == 2 and j == 7:
            tile = Tile(j, i, window)
            tile.setType('dirt')
            row.append(tile)
        elif i < 5:
            tile = Tile(j, i, window)
            tile.setType('air')
            row.append(tile)
        else:
            tile = Tile(j, i, window)
            tile.setType('dirt')
            row.append(tile)
    world.append(row)

player = Player(30, 30, window)


while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort
    # Graphics

    shift = camShift(player, center)

    leftBound = max(floor(player.xSpace-center[0]/world[0][0].size), 0)
    rightBound = min(worldSize-1, int(ceil(player.xSpace + center[0]/world[0][0].size)))
    topBound = max(floor(player.ySpace-cente   r[1]/world[0][0].size), 0)
    botBound = min(worldSize-1, int(ceil(player.ySpace + center[0]/world[0][0].size)))

    for i in range(topBound, botBound+1):
        for j in range(leftBound, rightBound+1):
            world[i][j].update()
            world[i][j].draw(shift)
    player.update(world)
    player.draw(shift)

    '''
    for object in objects:
        object.update(world)
        object.draw(shift)
        
    for 
    '''

    window.update()