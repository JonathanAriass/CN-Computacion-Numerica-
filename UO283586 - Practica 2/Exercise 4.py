# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:28:05 2022

@author: Jonathan Arias Busto (UO283586)
"""

"""
Modificar el programa del ejercicio anterior de forma que calcule simultáneamente 
la aproximación de la función de los 50 valores contenidos en 
x = np.linspace(-np.pi,np.pi). El criterio de parada será ahora que, el máximo 
del último sumando en valor absoluto (ahora tenemos 50 x0

distintas y 50 últimos sumandos distintos), sea menor que que una tolerancia 
tol=1.e-8 y que el número máximo de sumandos es 100, maxNumSum=100.

Convertir este programa en una función funSin(x, tol, maxNumSum) cuyos 
argumentos de entrada sean el array numpy x que contiene los 50 valores, tol y 
maxNumSum y cuyo argumento de salida sea un array numpy y que contenga los
valores aproximados de la función obtenidos con el polinomio de McLaurin. 
Utilizar esta función para dibujar la función. Dibujar también la función 
utilizando la función lambda f definida a partir de np.sin(x)
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.sin(x)

def funSin(x, tol=1.e-8, maxNumSum=100):
    
    factorial = 1.
    #polinomio = 0.
    polinomio = np.zeros_like(x)
    paso = 2.
    testparada = False
    i = 0
    aux = 1.
    exponente = 1.
    sumandoSize = 50
    
    while (testparada == False and  sumandoSize < maxNumSum):
        sumando = aux*(x**exponente/(np.math.factorial(factorial)))
        testparada = np.max(np.abs(sumando)) < tol
        polinomio = polinomio + sumando
        print(polinomio)
        factorial += paso
        exponente += paso    
        i = i + 1
        sumandoSize = sumando.size
        if (aux == -1):
            aux = 1
        else:
            aux = -1
    return polinomio

x = np.linspace(-np.pi,np.pi)

y = funSin(x)
print(y)

plt.figure()
plt.plot(x,x*0,'k-')
plt.plot(x,f(x),'y',linewidth=4,label='f')
plt.plot(x,y,'b--',label='f aproximada')
plt.legend()
plt.show()
