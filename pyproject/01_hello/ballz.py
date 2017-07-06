import ccircle

window = ccircle.window("Ballz", 480, 480)

class Ballz:

    ballCount = 0

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        Ballz.ballCount += 1

    def collide(self, objects):
        # Detects Collisions and Adjusts Velocity



while window.isOpen():

    Ballz_List = []




    window.update()