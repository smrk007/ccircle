import ccircle

import math

window = ccircle.Window("Ballz", 480, 480)

class Ballz:

    ballCount = 0

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.radius = 30
        Ballz.ballCount += 1

    def collide(self, object):
        # Detects Collisions and Adjusts Velocity
        # print("This is the distance"+str((self.posX - object.posX)**2 + (self.posY - object.posY)**2))
        if math.sqrt((self.posX - object.posX)**2 + (self.posY - object.posY)**2) < 60:
            self.velX = (self.velX + object.velX) + math.sqrt((self.velX + object.velX)**2 - 4*(self.velX*object.velX))
            self.velX = self.velX/2
            self.velY = (self.velY + object.velY) + math.sqrt((self.velY + object.velY)**2 - 4*(self.velY*object.velY))
            self.velY = self.velY/2

Ballz_List = []
Ballz_List += [Ballz(100, 150)]
Ballz_List += [Ballz(120, 50)]

while window.isOpen():

    window.clear(0,0,0)




    # Physics:

    # Gravity
    for i in Ballz_List:
        i.velY = i.velY + 0.0003
    # Collisions
    for i in range(2):
        for j in range(1,2):
            if i != j:
                Ballz_List[i].collide(Ballz_List[j])
        if Ballz_List[i].posY > 450:
            Ballz_List[i].velY = -Ballz_List[i].velY

    # Motion
    for i in Ballz_List:
        i.posX += i.velX
        i.posY += i.velY

    # Graphics
    for i in Ballz_List:
        window.drawCircle(i.posX, i.posY, i.radius, 1, 1, 1)

    # Debugging
    for i in Ballz_List:
        print(i.posX)
        print(i.posY)
        print(i.velX)
        print(i.velY)
        print()

    window.update()