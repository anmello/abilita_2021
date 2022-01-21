# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:09:54 2022

@author: anton
"""

import numpy as np
a=np.arange(0,2*np.pi,0.1)
y=np.sin(a)

def f(x):
    return np.where(x<0, 0.0, np.exp(x))

print(f(-1))
print(f(5))

#broadcasting
a=np.zeros((2,2))
print(a)
c=np.array([1,2])
print(a+c)

#operazioni su array
x=np.array([1,1,1,1])
x[1:4]=x[1:4]*2
print(x)
y=np.ones([4])
print(y)
z=np.dot(x,y)
print(z)