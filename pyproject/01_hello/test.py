import ccircle

window = ccircle.Window("Gravity",480,480)


circle = {
    'posX' : 50,
    'posY' : 120,
    'velX' : 0.05,
    'velY': 0
}

while window.isOpen():

    window.clear(0,0,0)

    # Falling Circle Bouncing

    # Collision
    if circle['posY'] > 450:
        print(circle['posY'])
        circle['velY'] = -circle['velY']*0.9
    else:
        circle['velY'] += 0.0003
    if circle['posX'] < 30 or circle['posX'] > 450:
        circle['velX'] = -circle['velX']

    # Friction and Decay
    circle['velX'] = 0.9999*circle['velX']

    # Plotting
    circle['posY'] += circle['velY']
    circle['posX'] += circle['velX']


    window.drawCircle(circle['posX'],circle['posY'],30,1,1,1)

    window.update()