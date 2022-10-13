# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:45:23 2020

@author: 15185
""" 
import numpy as np








Ins = [4,  3,  2,  1]
wts = [1, .5, .5, .4]
wht1= [2, 3, 4 ,4, 4]






               

#==============================---FUNCTION---OVER--FASHION--------==========================================#
import random

egg1 = [Ins[0], Ins[1], Ins[2]]

#egg2= [ Nest[0], Nest[1], Nest[2],
       

egg3 = [[ wts[0], wts[1], wts[2], wts[2]],
        [ wts[3], wts[2], wts[1], wts[1]],
        [ wts[2], wts[1], wts[0], wts[0]],
        [ wts[1], wts[2], wts[3], wts[1]]]
        
        
egg = [wht1[0], wht1[1], wht1[2]]

#---ACTIVATIONS
def sigmoid(self):

       return 1/(1+np.exp(self))
   
def sig_deriv(self):
        y = self**2 + 1
        return y 
#----------------

def Ram(x):
    Ram = random.choice(x)
    return Ram


def Depol(Q,R,S):
     P=Ram(Q)*Ram(R)*Ram(S)
     arize= sigmoid(P)
     return P
    
def Thought(self, Tin, Tout, Its):
    Wts= np.array(self)
    for It in range(Its):
        inputs = Tin.astype(float)
        ducknest = np.dot(inputs, Wts)
        output = sigmoid(ducknest)
        #np.shape(a,newshape,order=C)
    error = output - Tout
    print('Error:',error)
    taught = np.dot(Tin, error * sig_deriv(output))
    Wts += taught
    self.clear()
    self.append(taught)
    

ree=Depol(egg1,egg3,egg)
print(ree)

train_in =        np.array([[1,0,1,0], 
                            [1,0,1,0], 
                            [1,0,1,0],
                            [1,0,1,0]])

train_out =       np.array([[1,1,1,9]]) 

Thought(egg3,train_in,train_out,1500)
    
    
    
    

