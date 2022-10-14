# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:40:12 2022

@author: scott baskonbitz
"""

import random
import math
import numpy as np


guess_one = [random.random()]
guesss_two = [random.random()]
guess_three =[random.random()]

wisdom = guess_one[0]+guesss_two[0]+guess_three[0]/3

#crowd = wisdom

print(wisdom)

guess_four = [random.random()]
guess_five = [random.random()]
guess_six = [random.random()]

logic = guess_four[0]+guess_five[0]+guess_six[0]/3

print(logic)

guess_seven = [random.random()]
guess_eight = [random.random()]
guess_nine = [random.random()]

crowd = guess_seven[0]+guess_eight[0]+guess_nine[0]/3

print(crowd)

matrix = np.matrix([wisdom,crowd,logic])
matrix = np.array(matrix)

print(matrix)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

print(sigmoid(matrix))

def derivative(x):
    sigmoid(x) * (1- sigmoid(x))
    
    
print(derivative(matrix))
