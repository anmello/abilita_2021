# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:27:38 2022

@author: anton
"""


def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("the result is ", result)
    finally:
        print("executing finally clause")
    
divide(2,1)

divide(2,0)