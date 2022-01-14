# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:03:58 2022

@author: anton
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("And I am", self.age)

p1 = Person("carlo",50)
p2 = Person("antonio",20)
print(p1)
print(p2)
p1.myfunc()