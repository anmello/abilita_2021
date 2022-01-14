# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:34:45 2022

@author: anton
"""

#funzione range
v=[2,6,7,8,1]
for i in range(1,5,2):
    print(v[i])
    
#funzione zip
    
a=("Antonio", "Carlo", "Simone")
b=("Alessia","Linda","Marco")
    
x=zip(a,b)
print(tuple(x))

#funzione lambda

somma = lambda x,y: x+y

print(somma(2,3))