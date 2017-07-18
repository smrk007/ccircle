from math import *
from random import *

'''
Model must take into account the following features:
Persistence
Frequency
Amplitude
Octaves
Random Seed
'''

def ten_interval(lower, upper, rnge):
    ySpaces = []
    for i in range(10):
        j = i/10
        a = (lower+upper)
        a = a * (j**3)
        b = -(2*lower + upper)
        b = b* (j**2)
        c = lower*j
        val = a+b+c
        ySpaces.append(floor(val*10 + 50))
    return ySpaces

def perlin(rnge):
    '''Will return the 'boundary' for the dirt in each jSpace'''
    ySpaces = []
    gradients = genNoiseGradients(floor(rnge/10)+1)
    for i in range(len(gradients)-1):
        ySpaces += ten_interval(gradients[i],gradients[i+1],rnge)
    return ySpaces

def genNoiseGradients(N): #  Returns a list of N randomly generated slopes
    gradients = []
    for i in range(N):
        gradients.append(atan(pi*uniform(-1,1)))
    return gradients
