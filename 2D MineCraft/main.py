import ccircle
import player
import tile

window = ccircle.Window()



# World Initialization
worldSize = 100
world = []
for i in range(worldSize):
    row = []
    for j in range(worldSize):
        row.append(None)
    world.append(row)


while window.isOpen():

    window.clear(0,0,0) # Or maybe I'll have to make it teal, or something of that sort

    # Physics and


    # Graphics
    for tile in environment:
        tile.draw()

    player.draw

    window.update()