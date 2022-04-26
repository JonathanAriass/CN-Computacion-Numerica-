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
print("RES: ", res)
plt.figure()
plt.plot(z,res)
#plt.plot(z,z*0)
plt.show()
plt.close()

def searchVecino(x,y,x0):
    index = 0
    aux = np.inf
    for i in range(len(x)):
        if abs(x[i] - x0) < aux:
            aux = abs(x[i] - x0)
            index = i

        elif abs(x[i] - x0) == aux:
            if y[i] < y[index]:
                index = i
    return index

def nn(x,y,x0):
    res = np.zeros_like(x0)
    res[0] = y[0]
    res[-1] = y[-1]
    for i in range(1,len(x0)-1):
        left = x[i-1]
        right = x[i]
        if (x0[i] == left):
            res[i] = y[i-1]
        elif x0[i] == right:
            res[i] = y[i]
        else:
            vecino = searchVecino(x, y, x0[i])
            res[i] = y[vecino]
        print("RESULTADO: ", res)
            
    plt.figure()
    plt.scatter(x,y, linewidths=9)
    plt.scatter(x0,res, linewidths=1, color='red')
    plt.plot()
    plt.show()

    
   
x = np.array([-1., 0, 2, 3, 5, 6, 7])
y = np.array([1., 3, 4, 3, 2, 2, 1])
x0 = np.array([-1., 1.3, 2.5, 3, 3.2, 5, 6.5, 7])

nn(x,y,x0)



# DIFERENCIAS DIVIDIDAS
"""
    Argumentos de entrada: los nodos x, y del problema de interpolación.
    Argumentos de salida: una matriz que contenga las diferencias divididas.
"""
def dif_div(x,y):
    res = np.zeros((len(x),len(y)))
    
    for i in range(len(y)):
        res[i, 0] = y[i]
    
    for i in range(1, len(x)):
        for j in range(len(y) - i):
            res[j][i] = (res[j+1][i-1] - res[j][i-1])/(x[i+j] - x[j])
    
    b = np.zeros(len(x))
    
    for i in range(len(x)):
        b[i] = res[i, i]
    
    return res
"""    
    Argumentos de entrada: los nodos x, y del problema y un punto (o vector) a evaluar z.
    Argumentos de salida: el valor del polinomio interpolante de Lagrange en z.
"""
#def polinomio_newton(x,y,z):
  
    
  
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])
aux = dif_div(x, y)
print(aux)