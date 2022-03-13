# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:03:11 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt


"""
Utilizando un bucle while, escribir un programa, que utilizando el desarrollo de
McLaurin para la función f(x)=sen(x), calcule su valor aproximado en el 
punto x0 = np.pi/4. El criterio de parada será que el valor del último sumando 
añadido en valor absoluto es menor que una tolerancia tol=1.e-8 y que el número 
máximo de sumandos es 100, es decir maxNumSum=100. Comparar su valor con el 
valor de la función lambda f. Dar el número de sumandos utilizados.
"""


tol = 1.e-8
polinomio = 0
x0 = np.pi/4
factorial = 1
paso = 2
exponente = 1
aux = 1

testparada = False
i = 0


while (testparada == False and i < 100 ):
    sumando = aux*(x0**exponente/(np.math.factorial(factorial)))
    testparada = np.abs(sumando) < tol
    polinomio += sumando
    factorial += paso
    exponente += paso    
    i = i + 1
    if (aux == -1):
        aux = 1
    else:
        aux = -1
    
    
    
print('Valor de la funcion sin(pi/4) = ', np.sin(np.pi/4))
print('Valor de la aproximacion      = ', polinomio)
print('Numero de iteraciones         = ', i)