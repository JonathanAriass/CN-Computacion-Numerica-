# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:26:07 2022

@author: Jonathan Arias Busto (UO283586)
"""

#################
#  EJERCICIO 2  #
#################
"""Modificar el programa de forma que calcule simultáneamente la aproximación de
 la función de los 50 valores contenidos en x = np.linspace(-1,1). El criterio de
 parada será ahora que, el máximo del último sumando en valor absoluto 
 (ahora tenemos 50 x0 distintas y 50 últimos sumandos distintos), sea menor que 
 que una tolerancia tol=1.e-8 y que el número máximo de sumandos es 100, 
 maxNumSum=100.
Convertir este programa en una función funExp(x, tol, maxNumSum) cuyos argumentos 
de entrada sean el array numpy x que contiene los 50 valores, tol y maxNumSum y 
cuyo argumento de salida sea un array numpy y que contenga los valores aproximados
 de la función obtenidos con el polinomio de McLaurin. Utilizar esta función para
 dibujar la función. Dibujar también la función utilizando la función lambda f
 definida a partir de np.exp(x)"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.exp(x)

def funExp(x, tol, maxNumSum): 
    factorial = 1.
    polinomio = 0.
    
    testParada = False
    
    i=0
    
    
    while (testParada == False and i < maxNumSum):
        sumando = x**i/factorial
        testParada = np.max(np.abs(sumando)) < tol
        polinomio += sumando
        factorial *= i+1
        i = i + 1
         
    return polinomio, i

x = np.linspace(-1,1)
y = f(x)
valores, iteraciones = funExp(x, 1.e-8, 100)

plt.plot(x,valores,'y', linewidth=4, label='f')
plt.plot(x,x*0,'k-')
plt.plot(x,valores, 'b--', label='Aproximación f')
plt.legend()
#plt.axis([-1,1,0,2.5]) #Para ajustar los ejes xMin, xMax, yMin, yMax

print('Valor de la funcion exp(-0.4) = ', np.exp(x))
print('Valor de la aproximacion      = ', valores)
print('Numero de iteraciones         = ', iteraciones)
 