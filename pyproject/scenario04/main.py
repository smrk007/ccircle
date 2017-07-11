import ccircle
import connection
from math import *

con = connection.create()
con.send('set_name', {'name': 'smrk007'})

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def getflow(playerPos, targetPos, TF):
    if TF: # Boss
        A = sub(playerPos, targetPos)
        return [1/A[0]**2, 1/A[1]**2]
    else:
        A = sub(targetPos, playerPos)
        return[(A[0]/abs(A[0]))/A[0]**2, (A[1]/abs(A[1]))/A[1]**2]

def unitvector(flow):
    mag = distance((0, 0), flow)
    return dot(flow, 1/mag)

def dot(a, b):
    return [a[0]*b, a[1]*b]

while True:

    flow = [0, 0]

    playerPos = con.send('get_pos')
    print(playerPos)
    bossPos = con.send('get_boss_pos')
    print(bossPos)
    rewardIDs = con.send('get_reward_ids')
    rewardPos = []
    for ID in rewardIDs:
        rewardPos.append(con.send('get_reward_pos',{'id' : ID}))

    flow = add(flow, getflow(playerPos, bossPos, True))
    for pos in rewardPos:
        flow = add(flow, getflow(playerPos, pos, False))

    direction = unitvector(flow)
    vel = dot(direction, 50)

    con.send('set_velocity', {'vx': vel[0], 'vy': vel[1]})


# Write code to make money and kill the evil cat!
# See readme.txt !