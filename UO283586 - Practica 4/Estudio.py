# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:51:39 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt


#EJERCICIO 1

def busquedaIncremental(f,a,b,n):
    dx = (b-a) / n
    intervalos = np.zeros((n,2))
    contador = 0
    
    for i in range(n):
        if (f(a)*f(a+dx) < 0):
            intervalos[contador] = [a,a+dx]
            contador = contador + 1
        a = a + dx
    
    return intervalos[:contador,:]


f = lambda x : x**5 - 3 * x**2 + 1.6
x = np.linspace(-1, 1.5)
ox = 0*x

res = busquedaIncremental(f, -1, 1.5, 25)
print("EJERCICIO 1: \n", res)


f2 = lambda x : (x + 2) * np.cos(2*x)

res2 = busquedaIncremental(f2, 0, 10, 100)
print("EJERCICIO 1: \n", res2)



#EJERCICIO 2

def biseccion(f,a,b,tol=1.e-6,maxiter=100):
    count = 0
    while count <= maxiter:
        c = (a+b)/2
        if (f(c)*f(a)) < 0:
            b = c
        elif (f(b)*f(c)) < 0:
            a = c
            
        count = count + 1
        
        if abs(f(c)) < tol and abs(b-a) < tol and (abs(b-a)/abs(b)) < tol:
            break
        
    return c, count;
        
print("\n\nEJERCICIO 2")

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
        
        
        
#EJERCICIO 3

def newton(f,df,x0,tol=1.e-6,maxiter=100):
    count = 0
    xaux = 0
    while count <= maxiter:
        xaux = x0 - (f(x0)/df(x0))
        
        count = count + 1
        
        if abs(f(xaux)) < tol and abs(xaux - x0) < tol:
            break
        
        x0 = xaux
    
    return xaux, count
    

f = lambda x : x**5 - 3 * x**2 + 1.6
df = lambda x : 5 * x**4 - 6. * x    

print("\n\nEJERCICIO 3")

a = res[0][0]
x, iteraciones = newton(f,df,a)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a = res[1][0]
x, iteraciones = newton(f,df,a)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a = res[2][0]
x, iteraciones = newton(f,df,a)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)



#EJERCICIO 4

def raices_bisec(f,a,b,tol=1.e-6,maxiter=100,n=100):
    intervalos = busquedaIncremental(f, a, b, n)
    res = np.zeros(len(intervalos))
    count = 0
    for x0 in intervalos:
        c, iteraciones = biseccion(f,x0[0],x0[1])
        res[count] = c
        
        count = count + 1
    return res
       

print("\n\nEJERCICIO 4")    
f = lambda x : np.cos(x)**2 + x/10
res = raices_bisec(f, -10, 0)
print(res)

f = lambda x : x**5 - 3*x**4 + x + 1.1
res = raices_bisec(f, -1, 3)
print(res)



#EJERCICIO 5
def raices_newton(f,df,a,b,tol=1.e-6,maxiter=100,n=100):
    intervalos = busquedaIncremental(f, a, b, n)
    res = np.zeros(len(intervalos))
    count = 0
    for x0 in intervalos:
        x, iteraciones = newton(f,df,x0[0])
        res[count] = x
        
        count = count + 1
    return res


print("\n\nEJERCICIO 5")
f = lambda x : x**4 + 2*x**3 - 7*x**2 + 3
df = lambda x : 4*x**3 + 6*x**2 - 14*x
res = raices_newton(f, df, -4, 2)
print (res)

f = lambda x : x**6 - 0.1*x**5 - 17*x**4 + x**3 + 73*x**2 - 4*x -68
df = lambda x : 6*x**5 - 0.5*x**4 - 68*x**3 + 3*x**2 + 146*x - 4
res = raices_newton(f, df, -4, 4)
print (res)
