# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:12:26 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np

#################
#  EJERCICIO 1  #
#################
"""Utilizando un bucle while, escribir un programa, que utilizando el desarrollo 
de McLaurin para la función f(x)=ex, calcule su valor aproximado en el punto 
x0 = -0.4. El criterio de parada será que el valor del último sumando añadido 
en valor absoluto es menor que una tolerancia tol=1.e-8 y que el número máximo 
de sumandos es 100, es decir maxNumSum=100. Comparar su valor con el valor de 
la función lambda f. Dar el número de sumandos utilizados."""

"""tol = 1.e-8
tolAux = tol
x0 = -0.4
factorial = 1.
polinomio = 0.

i=0

while (tolAux >=  tol and i <= 100):
    sumando = x0**i/factorial
    tolAux = np.abs(sumando)
    print(tolAux)
    polinomio += sumando
    factorial *= i+1
    i = i + 1
    
print(polinomio)
print (i)"""

# OTRA FORMA DE HACERLO CON UN TEST DE PARADA

tol = 1.e-8
tolAux = tol
x0 = -0.4
factorial = 1.
polinomio = 0.

testParada = False

i=0

while (testParada == False and i < 100):
    sumando = x0**i/factorial
    testParada = abs(sumando) < tol
    polinomio += sumando
    factorial *= i+1
    i = i + 1
    
print('Valor de la funcion exp(-0.4) = ', np.exp(x0))
print('Valor de la aproximacion      = ', polinomio)
print('Numero de iteraciones         = ', i)