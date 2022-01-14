# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:19:58 2022

@author: anton
"""

print("Inserire un numero intero:")
num = input()
if int(num) in range(5):
    print("Inserire una lettera:")
    lett = input()
    if lett in ['A','B','C']:
        print("I dati immessi sono: ", num, lett)
else:
    print("Riprova")
    

