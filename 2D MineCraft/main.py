import ccircle
from tile import Tile
from math import *
from otherCrap import *
from player import *

window = ccircle.Window("2D Minecraft", 450, 450)
center = (225, 225)

# World Initialization
worldSize = 300
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

    # Physics and Interactions
    player.move(keyDown())  # Sets an intended velocity
    xSpace = int(floor(player.posX / world[0][0].size))
    ySpace = int(floor(player.posY / world[0][0].size))

    if ccircle.isKeyDown('space'):
        tX = int(floor(player.target[0] / world[0][0].size))
        tY = int(floor(player.target[1] / world[0][0].size))
        world[tY][tX].health -= 0.3


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
        player.velY += 0.001

        player.posY += player.velY




    # Graphics

    shift = camShift(player, center)

    leftBound = max(floor(xSpace-center[0]/world[0][0].size), 0)
    rightBound = min(worldSize-1, int(ceil(xSpace + center[0]/world[0][0].size)))
    topBound = max(floor(ySpace-center[1]/world[0][0].size), 0)
    botBound = min(worldSize-1, int(ceil(ySpace + center[0]/world[0][0].size)))

    for i in range(topBound, botBound+1):
        for j in range(leftBound, rightBound+1):
            world[i][j].update()
            world[i][j].draw(shift)
    player.update()
    player.draw(shift)

    window.update()