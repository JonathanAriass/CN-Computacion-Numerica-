# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:10:30 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt

# POLINOMIOS FUNDAMENTALES DE LAGRANGE

"""
Argumentos de entrada: el índice k del polinomio Fundamental, los nodos x del 
problema de interpolación y un punto (o puntos, vector) donde vamos a calcular 
los valores del polinomio, z.

Argumentos de salida: el valor del k−ésimo polinomio fundamental correspondiente 
a los nodos x en el punto (o puntos, vector) z.
"""

def lagrange_fund(k,x,z):
    cont = 0
    size = len(x)
    num = 1
    den = 1
    res = np.zeros_like(z)
    for aux in range(len(z)):
        for i in range(size):
            if i != k:
                num = (z[aux]-x[i]) * num
                den = (x[k] - x[i]) * den
        
        res[aux] = num/den
        num = 1
        den = 1
        
    return res


x = np.array([-1., 0, 2, 3, 5])

k = 2
z = np.array([1.3, 2.1, 3.2])
yz = lagrange_fund(k,x,z)
print(yz)
    

for i in range(5):
    k = i
    z = np.linspace(-1, 5, 100)
    yz = lagrange_fund(k,x,z)
    plt.figure()
    plt.plot(z,yz)
    plt.plot(z,z*0)
    aux = "L" + str(k)
    plt.title(aux)
    plt.show()
    #print(k, yz) 
    plt.close()
    
    
# EJERCICIO 2
"""
    Argumentos de entrada: los nodos x, y del problema y un punto (o vector) a evaluar z.
    Argumentos de salida: el valor del polinomio interpolante de Lagrange en z.
"""
def polinomio_lagrange(x,y,z):
        res = 0

        for i in range(len(x)):
            yz = lagrange_fund(i, x, z)
            res = yz*y[i] + res
        
        return res

x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])
z = np.linspace(-1,5,100)
res = polinomio_lagrange(x, y, z)
plt.figure()
plt.plot(z,res)
#plt.plot(z,z*0)
plt.show()
plt.close()

x1 = np.array([-1., 0, 2, 3, 5, 6, 7])
y1 = np.array([ 1., 3, 4, 3, 2, 2, 1])
z = np.linspace(-1,7,100)
res = polinomio_lagrange(x1, y1, z)
plt.figure()
plt.plot(z,res)
#plt.plot(z,z*0)
plt.show()
plt.close()


# DIFERENCIAS DIVIDIDAS
"""
    Argumentos de entrada: los nodos x, y del problema de interpolación.
    Argumentos de salida: una matriz que contenga las diferencias divididas.
"""
def dif_div(x,y):
    res = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(x)):
            if i == 0:
                res[i][j] = (y[i] - y[i+1])/(x[i] - x[i+1])
            else:
                res[i][j] = (res[i-1][j] - res[i-1][j+1])/(res[i-1][j] - res[i-1][j+1])
"""    
    Argumentos de entrada: los nodos x, y del problema y un punto (o vector) a evaluar z.
    Argumentos de salida: el valor del polinomio interpolante de Lagrange en z.
"""
def polinomio_newton(x,y,z):
    