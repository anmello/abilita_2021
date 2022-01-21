# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:43:36 2022

@author: anton
"""


import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.0,2.0,0.01)
s=1+np.sin(np.pi*t)
plt.plot(t,s)

plt.xlabel('time (s)')
plt.ylabel('current (mA)')
plt.grid(True)
plt.savefig("prova.png")
plt.show()