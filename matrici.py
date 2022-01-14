# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 10:09:19 2022

@author: anton
"""


#import numpy as np
#input=np.loadtxt("data.txt", dtype='i',delimiter=',')
#print(input)

#definisco una matrice 2x2
X=[[1,2],[2,1]]
#definisco una matrice 2x4
Y=[[1,0,1,1,],[1,0,0,0]]
#definisco il risultato 2x4
result=[[0,0,0,0],[0,0,0,0]]
#moltiplico le due matrici
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k]*Y[k][j]
for r in result:
    print(r)
    
