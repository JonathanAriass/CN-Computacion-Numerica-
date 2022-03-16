# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:24:58 2022

@author: UO283586
"""

import numpy as np

def derivada(p):
    x = np.zeros(len(p))
    c = len(p)-1
    rang = len(p)-1
    
    for i in range(0,len(p)-1):
        x[i] = p[i] * c
        c = c - 1
    
    return x[:rang]
        
p = np.zeros(7)
T4 = np.array([8., 0, -8, 0 ,1])
result1 = derivada(T4)
result2 = derivada(p)
print("Derivada de P = ", result2)
print("Derivada de T4 = ", result1)

