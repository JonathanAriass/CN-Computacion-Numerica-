# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#EJERCICIO 1

def cambios_signos(p):
    x = np.zeros(len(p))
    count = 0
    for x0 in p:
        if (x0 != 0):
            x[count] = x0
            count = count + 1
    
    y = np.zeros(count)
    for i in range(len(y)):
        y[i] = x[i]
        
    signo = 1
    counter = 0
    
    for i in range(len(y)):
        if i == 0:
            if y[i] < 0:
                signo = -1
            else:
                signo = 1
        else:
            if signo == 1:    
                if y[i] < 0:
                    signo = -1
                    counter = counter + 1
            else:
                if y[i] > 0:
                    signo = 1
                    counter = counter + 1
    
    return counter



p0 = np.array([32., -32., -14, 17, -3])
p1 = np.array([32., -32., 0, 17, -3])
T4 = np.array([8., 0, -8, 0, 1])
T6 = np.array([32., 0, -48, 0, 18, 0, -1])

result1 = cambios_signos(p0)
result2 = cambios_signos(p1)
result3 = cambios_signos(T4)
result4 = cambios_signos(T6)

print("P0")
print(result1, " raíces reales positivas como máximo")
print("P1")
print(result2, " raíces reales positivas como máximo")
print("T4")
print(result3, " raíces reales positivas como máximo")
print("T6")
print(result4, " raíces reales positivas como máximo")