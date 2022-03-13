# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:58:03 2022

@author: Jonathan Arias Busto (UO283586)
"""

"""
Teniendo en cuenta que el desarrollo de McLaurin de la función seno hiperbólico 
es la serie
sinhx=x1/1!+x3/3!+x5/5!+x7/7!+x9/9!+⋯

el coseno hiperbólico
coshx=1+x2/2!+x4/4!+x6/6!+x8/8!+⋯

y que la tangente hiperbólica es
tanh=sinhx/coshx

calcular la tangente hiperbólica de x0=0.5
a partir de los desarrollos del senh y el cosh, usando el mismo número de 
términos (sumandos en el numerador y en el denominador). En el paso uno, 
usa un término para cada desarrollo, en el paso dos, dos sumandos y así 
sucesivamente. Parar cuando la diferencia en valor absoluto entre dos 
aproximaciones sucesivas de la tangente hiperbólica sea menor que 10−4.
"""

import numpy as np

x0 = 0.5

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

tol = 1.e-4 
testparada = False
i = 0


while (testparada == False):
    sumandoSin = (x0**exponenteSin/(np.math.factorial(factorialSin)))
    #testparadaSin = np.abs(sumandoSin) < tol
    polinomioSin += sumandoSin
    factorialSin += pasoSin
    exponenteSin += pasoSin    
    
    
    sumandoCos = (x0**exponenteCos/(np.math.factorial(factorialCos)))
    polinomioCos += sumandoCos
    factorialCos += pasoCos
    exponenteCos += pasoCos
    
    polinomioAnterior = polinomioTan
    polinomioTan = polinomioSin/polinomioCos
    
    testparada = np.abs(polinomioAnterior - polinomioTan) < tol

print('Valor real =  ', np.tanh(x0))
print('Valor aprox = ', polinomioTan)

