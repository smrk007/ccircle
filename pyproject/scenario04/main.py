import ccircle
import connection
from math import *

con = connection.create()
con.send('set_name', {'name': 'smrk007'})

class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def length(self):
        p1 = (self.a)**2
        p2 = (self.b)**2
        return sqrt(p1+p2)

    def __sub__(self, vec2):
        return Vector(self.a - vec2.a, self.b - vec2.b)

    def __add__(self, vec2):
        return Vector(self.a + vec2.a, self.b - vec2.b)

    def dot(self, scalar):
        return Vector(self.a * scalar, self.b * scalar)

    def direction(self):
        return self.dot(1/self.length())

def getflow(playerPos, targetPos, TF):
    A = 0
    K = 0
    P = 0
    C = 0
    if TF: # Boss
        A = 0.00009
        K = 5.5
        P = -1
        C = 0
        dP = playerPos - targetPos
        dis = dP.length()
        unit = dP.direction()
        weight = A / ((0.1**K)*dis)**P
        return Vector(0,0)
    else:
        dP = targetPos - playerPos
        return dP.direction().dot(5)

while True:
    vel = [0,0]
    if ccircle.isKeyDown('left'): vel = [-50,50]
    if ccircle.isKeyDown('right'): vel = [50,50]
    if ccircle.isKeyDown('up'): vel = [-50,-50]
    if ccircle.isKeyDown('down'): vel = [50,-50]
    if ccircle.isKeyDown('space'): con.send('damage_boss')
    con.send('set_velocity', {'vx': vel[0], 'vy': vel[1]})


# Write code to make money and kill the evil cat!
# See readme.txt !