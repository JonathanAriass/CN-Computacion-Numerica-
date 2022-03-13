# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:20:15 2022

@author: Jonathan Arias Busto (UO283586)
"""

"""
Modificar el programa del ejercicio anterior de forma que calcule simultáneamente
la aproximación de la función de los 50 valores contenidos en x = np.linspace(-3,3). 
El criterio de parada será ahora que, la máxima diferencia entre dos iteraciones 
consecutivas para todos los puntos (ahora tenemos 50 puntos distintos), 
sea menor que que una tolerancia tol=1.e-8.

Convertir este programa en una función funTanh(x, tol) cuyos argumentos de 
entrada sean el array numpy x que contiene los 50 valores, tol y cuyo argumento 
de salida sea un array numpy y que contenga los valores aproximados de la función 
obtenidos con el polinomio de McLaurin. Utilizar esta función para dibujar 
la función. Dibujar también la función utilizando la función lambda f definida 
a partir de np.tanh(x)
"""

import numpy as np
import matplotlib.pyplot as plt

def funTanh(x, tol=1.e-8):
    #Variables para seno hiperbolico
    polinomioSin = 0
    factorialSin = 1
    pasoSin = 2
    exponenteSin = 1


    # Variables para coseno hiperbolico
    polinomioCos = 1
    factorialCos = 2
    pasoCos = 2
    exponenteCos = 2

    #Variables para la tangente hiperbolica
    polinomioTan = 0

    testparada = False


    while (testparada == False):
        sumandoSin = (x**exponenteSin/(np.math.factorial(factorialSin)))
        #testparadaSin = np.abs(sumandoSin) < tol
        polinomioSin += sumandoSin
        factorialSin += pasoSin
        exponenteSin += pasoSin    
        
        
        sumandoCos = (x**exponenteCos/(np.math.factorial(factorialCos)))
        polinomioCos += sumandoCos
        factorialCos += pasoCos
        exponenteCos += pasoCos
        
        polinomioAnterior = polinomioTan
        polinomioTan = polinomioSin/polinomioCos
        
        testparada = np.max(np.abs(polinomioAnterior - polinomioTan)) < tol
    
    return polinomioTan
        
f = lambda x : np.tanh(x)
        
x = np.linspace(-3,3)
y = funTanh(x)


plt.figure()
plt.plot(x,x*0,'k-')
plt.plot(x,f(x),'y',linewidth=4,label='f')
plt.plot(x,y,'b--',label='f aproximada')
plt.legend()
plt.show()
