# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:40:12 2022

@author: UO283586
"""

import numpy as np
import matplotlib.pyplot as plt

def NewtonRaphson(f,df,xk,tol=1.e-6,maxIter=100):
    
    cont = 0
    
    while cont < maxIter:
        xk = xk - (f(xk)/df(xk))
        
        cont = cont + 1
        
        if abs(f(xk)) < tol:
            break
        
    return xk


x = np.linspace(0,2,1000)

f = lambda x : np.sin(2*x + 3) + np.cos(x)
df = lambda x : 2*np.cos(2*x + 3) - np.sin(x)


plt.figure()
plt.plot(x,f(x),label="Funcion f")
#plt.plot(x,df(x), label="derivada f")
plt.plot(x, x*0, 'k-')
plt.legend()
plt.show()

"""
Viendo la grafica podemos observar que hay dos raices en el intervalo [0,2]
por lo que aproximando ambos valores como aparecen en la grafica podemos 
llamar a la funcion NewtonRaphson.
En este caso aproximando a ojo tenemos que:
    raiz1 = 0.5
    raiz2 = 1.75
"""
x1 = 0.5
x2 = 1.75
raiz1 = NewtonRaphson(f,df,x1)
print("Raiz de f para x = 0.5 ==> ", raiz1)
raiz2 = NewtonRaphson(f,df,x2)
print("Raiz de f para x = 1.75 ==> ", raiz2)