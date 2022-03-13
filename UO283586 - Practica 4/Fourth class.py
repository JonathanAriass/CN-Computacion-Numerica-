# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:23:09 2022

@author: Jonathan Arias Busto (UO283586)
"""
import numpy as np
import matplotlib.pyplot as plt


######################################
#       RAIZ DE UNA ECUCACION        #
######################################

f = lambda x : x**5 - 3 * x**2 + 1.6
x = np.linspace(-1, 1.5)
ox = 0*x

#plt.figure()
#plt.plot(x, f(x))
#plt.plot(x, ox, 'k-')
#plt.show()


######################################
#        SEPARACION DE RAICES        #
######################################
#EJERCICIO 1
"""
    f: funcion lamba
    a y b: extremos del intervalo
    n: numero de intervalos a dividir [a,b]
    dx = (b-a)/n
"""
def busquedaIncremental(f, a, b, n):
    intervalosAux = np.zeros((n,2))
    intervalos = np.zeros((n,2))
    contador = 0
    dx = (b-a)/n
    auxLeft = a 
    for i in range(n):
        intervalosAux[i] = [auxLeft,auxLeft+dx]
        if (f(intervalosAux[i][0]) * f(intervalosAux[i][1])) < 0:    
            intervalos[contador]= intervalosAux[i]
            contador += 1
        auxLeft = auxLeft + dx
    return intervalos[:contador,:]

res = busquedaIncremental(f, -1, 1.5, 25)
print("EJERCICIO 1: \n", res)


f2 = lambda x : (x + 2) * np.cos(2*x)

res2 = busquedaIncremental(f2, 0, 10, 100)
print("EJERCICIO 1: \n", res2)


######################################
#         METODO DE BISECCION        #
######################################
#EJERCICIO 2
def biseccion(f, a, b, tol=1.e-6, maxiter=100): 
    cont = 0
    while cont <= maxiter:
        xk = (a + b)/2
        if (f(a)*f(xk))<0:
            b = xk
        elif (f(b)*f(xk))<0:
            a = xk
            
                
        errorA = abs(b-a)
        errorR = abs(b-a)/abs(xk)
        residual = abs(xk)
        cont+=1
            
        if abs(errorA) < tol and abs(f(xk)) < tol:
            break
    return xk, cont


a = res[0][0]
b = res[0][1]
x, iteraciones = biseccion(f,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)
a = res[1][0]
b = res[1][1]

x, iteraciones = biseccion(f,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a = res[2][0]
b = res[2][1]
x, iteraciones = biseccion(f,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)


###########################################
#         METODO DE NEWTON-RAPHSON        #
###########################################
#EJERCICIO 3
def newton(f, df, x0, tol=1.e-6, maxiter=100):
    cont = 1
    while cont <= maxiter:

        xk = x0 - f(x0)/df(x0)
        
        cont+=1
        x0 = xk
        
        if abs(f(xk)) < tol:
            break
        
    return x0, cont
    
        
#f = lambda x : x**5 - 3 * x**2 + 1.6
df = lambda x : 5 * x**4 - 6 * x    

a = res[0][0]
b = res[0][1]
x, iteraciones = newton(f,df,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)
a = res[1][0]
b = res[1][1]

x, iteraciones = newton(f,df,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a = res[2][0]
b = res[2][1]
x, iteraciones = newton(f,df,a,b)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)  