from etc import *
from math import *
from ccircle import *

class Player:

    def __init__(self, posX, posY, window):
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.color = (1,1,1)
        self.size = 10
        self.jump = True
        self.direction = 'right'
        self.target = (0, 0)
        self.window = window
        self.xSpace = 0
        self.ySpace = 0

    def move(self, keys):
        self.velX = 0
        if keys['left'] or keys['a']:
            self.velX = -0.3
            self.direction = 'left'
        if keys['right'] or keys['d']:
            self.velX = 0.3
            self.direction = 'right'
        if (keys['up'] or keys['w']) and self.jump:
            self.velY = -0.3
            self.jump = False
            self.direction = 'up'
        if keys['down']:
            self.direction = 'down'

    def draw(self, shift):

        self.window.drawCircle(self.posX + shift[0], self.posY + shift[1], self.size, self.color[0], self.color[1], self.color[2])

    def update(self, world):
        if self.direction == 'left':
            self.target = (self.posX - 30, self.posY)
        if self.direction == 'right':
            self.target = (self.posX + 30, self.posY)
        if self.direction == 'up':
            self.target = (self.posX, self.posY - 30)
        if self.direction == 'down':
            self.target = (self.posX, self.posY + 30)

        self.move(keyDown())  # Sets an intended velocity
        self.xSpace = int(floor(self.posX / world[0][0].size))
        self.ySpace = int(floor(self.posY / world[0][0].size))

        if ccircle.isKeyDown('space'):
            tX = int(floor(self.target[0] / world[0][0].size))
            tY = int(floor(self.target[1] / world[0][0].size))
            world[tY][tX].health -= 0.3

        # Player X dimension collision and motion
        if self.posX + self.velX < self.xSpace * world[0][0].size + self.size and world[self.ySpace][self.xSpace - 1].solid:
            self.posX = self.xSpace * world[0][0].size + self.size
        elif self.posX + self.velX > (self.xSpace + 1) * world[0][0].size - self.size and world[self.ySpace][self.xSpace+1].solid:
            self.posX = (self.xSpace + 1) * world[0][0].size - self.size
        else:
            self.posX += self.velX

        # Player Y dimension collision and motion
        if self.posY + self.velY < self.ySpace * world[0][0].size + self.size and world[self.ySpace - 1][self.xSpace].solid:
            self.posY = self.ySpace * world[0][0].size + self.size + 1
        elif self.posY + self.velY > (self.ySpace + 1) * world[0][0].size - self.size and world[self.ySpace + 1][self.xSpace].solid:
            self.posY = (self.ySpace + 1) * world[0][0].size - self.size
            self.jump = True
        else:
            self.velY += 0.001

            self.posY += self.velY