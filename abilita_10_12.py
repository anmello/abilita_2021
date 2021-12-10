# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:03:29 2021

@author: anton
"""


import numpy as np
import math 

def somma(a,b):
    c=a+b
    print("the sum is:",c)
    print("the summation is:",type(c))
    d=math.sin(c)
    print("the sin of the sum is: ",d)
    
somma(2,3)

def membership(i):
    v=[1,2,3,4,5]
    if(i in v):
        print("your element is in your list")
        
    else:
        print("no match found")
        
membership(6)

def quadrato(l):
     p=4*l
     a=l*l 
     print("il perimetro è ", p)
     print("\n l'area è: ", a)
         
quadrato(4)

def bool(i):
    
    if(i==0):
        print("False")
        
    else:
        print("True")
        
bool(3)

def slicing(stringa):
    
    var=stringa
    print("the second and the third letter are",var[1:3])
    
slicing('python')

s='python programming'

s=s.replace('a','e',1)
print("la nuova stringa è: ",s)
    