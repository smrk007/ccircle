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
        p1 = (a[0]-b[0])**2
        p2 = (a[1]-b[1])**2
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
        A = 0.9
        K = 1.5
        P = -1.2
        C = 0
        dP = playerPos - targetPos
        dis = dP.length()
        unit = dP.direction()
        weight = A / ((0.1**K)*dis)**P
        return unit.dot(weight)
    else:
        dP = targetPos - playerPos
        return dP.direction()

while True:

    flow = [0, 0]

    (x,y) = con.send('get_pos')
    playerPos = Vector(x,y)

    (x,y) = con.send('get_boss_pos')
    bossPos = Vector(x,y)

    rewardIDs = con.send('get_reward_ids')
    rewardPos = []
    for ID in rewardIDs:
        (x,y) = con.send('get_reward_pos',{'id': ID})
        reward = Vector(x,y)
        rewardPos.append(reward)

    flow = flow + getflow(playerPos, bossPos, True)
    for pos in rewardPos:
        flow = flow + getflow(playerPos, pos, False)

    flowDir = flow.direction()
    vel = flowDir * 50

    con.send('set_velocity', {'vx': vel[0], 'vy': vel[1]})


# Write code to make money and kill the evil cat!
# See readme.txt !