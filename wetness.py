# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:49:45 2022

@author: scott baskonbitz
"""

import math
from math import *
import time as time
import numpy as np
import sys
import random

mos = random.choice([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09])
som = random.choice([0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009])

dor = random.choice([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09])
rod = random.choice([0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009])

self = sys.argv

def sigmoid(x):
    1 / (1+np.exp(-x))
    return x

its = id(self)
wts_1 = [1.0432,1.08646,0.086545]

bio = [math.sqrt(time.time())/100000000]

for its in range(its,10,1000):
    node_1 = (mos+som)*wts_1[0]*bio
    node_2 = (dor+rod)*wts_1[1]*bio
    node_3 = (mos+som)+(dor,rod)*wts_1[2]*bio
    her = sigmoid(node_1)
    inside = sigmoid(node_2)
    wet = sigmoid(node_3)
    done = (wet+inside+her)
    error = error[its]*100000000
    done += np.dot(wts_1)*error







