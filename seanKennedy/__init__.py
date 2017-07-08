import ccircle
import random

count = 1000
countInternal = count
rate = 0.001
colors = [0,0,0]
color = colors

it = 0

window = ccircle.Window("Let's just get it working!")
while window.isOpen():

    if countInternal == 0:
        colors = [0.1*random.randint(1,10), 0.1*random.randint(1,10), 0.1*random.randint(1,10)]
        countInternal = count
    else:
        countInternal -= 1
    print(countInternal)
    color = [(1-rate)*color[0]+rate*colors[0], (1-rate)*color[1]+rate*colors[1], (1-rate)*color[2]+rate*colors[2]]

    window.clear(color[0],color[1],color[2])
    window.update()