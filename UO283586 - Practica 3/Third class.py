# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:12:47 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt
import time


# EJERCICIO 1
def Horner(p, x0):
    size = len(p)
    q = np.zeros_like(p)
    q[0] = p[0]
    for k in range(1, size):
        q[k] = p[k] + (q[k-1]*x0)
        
    qs = q[:-1]
    ultimo = q[-1]
            
    return ultimo, qs


p0 = np.array([1.,2,1])
x0 = 1.

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.

ul, q = Horner(p0, x0)

print('Ultimo valor: ', str(ul))
print('Qs: ', q)


ul1, q1 = Horner(p1, x1)

print('Ultimo valor: ', str(ul1))
print('Qs: ', q1)


# EJERCICIO 2
def HornerV(p, x):
    size = len(p)
    y = np.zeros_like(x)
    
    for n in range(len(x)):

        q = np.zeros_like(p)
        q[0] = p[0]
        for k in range(1, size):
            q[k] = p[k] + (q[k-1]*x[n])
            
        ultimo = q[-1]
        y[n] = ultimo
            
    return y



p = np.array([1., -1, 2, -3, 5, -2])
x = np.linspace(-1,1)

y = HornerV(p, x)
"""
plt.figure()
plt.plot(x,np.polyval(p,x))
plt.plot(x,0*x,'k')
plt.title('Polinomio P')
plt.show()

plt.figure()
plt.plot(x,y, label='Horner')
plt.plot(x,0*x,'k')
plt.title('Figura con Horner')
plt.show()
"""

# EJERCICIO 3

def DerPol(p, x0):
    size = len(p)
    pol = np.zeros_like(p)
    p1 = p
    factorial = 1.
    for i in range(size):
        horner = Horner(p1,x0)
        value = horner[0]
        pol[i] = value * factorial
        factorial *= i+1
        p1 = horner[-1]
        print('P new= ', p1)
            
    return pol


p = np.array([1., -1, 2, -3,  5, -2])
x0 = 1.

pol = DerPol(p, x0)
print(pol)

r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x1 = -1.

pol2 = DerPol(r, x1)
print(pol2)


# EJERCICIO 4
# A)

def divisores(m):
    div = np.zeros(2*m)
    count = 0
    for i in range(1, m+1):
        if np.remainder(m, i) == 0:
             div[count] = i
             div[count+1] = -i
             count += 2
    return div[:count]

d = divisores(18)
print(d)

# B)
def raices(p):
    r = np.zeros_like(p)
    m = abs(int(p[-1]))
    div = divisores(m)
    cont = 0
    for x0 in div:
        resto, q = Horner(p, x0)
        if resto == 0:
            r[cont] = x0
            cont += 1
            p = q
    return r[:cont]

p0 = np.array([1., 0, -1])
res = raices(p0)
print(res)

p1 = np.array([1., -3, -6, 8])
res = raices(p1)
print(res)


# EJERCICIO 5
def raices2(p):
    r = np.zeros_like(p)
    m = abs(int(p[-1]))
    div = divisores(m)
    cont = 0
    auxBool = True
    for x0 in div:
        while auxBool == True:
            resto, q = Horner(p, x0)
            if resto == 0:
                r[cont] = x0
                cont += 1
                p = q
            else:
                auxBool = False
        auxBool = True
    return r[:cont]
p2 = np.array([1., -5, 1, 17, -22, 8])
res = raices2(p2)
print(res)


# EJERCICIO 6
def HornerVect(p, x):
    size = len(p)
    #y = np.zeros_like(x)
    m = len(x)
    q = np.zeros((m,size))
    q[:,0] = p[0]
    for n in range(len(x)):

        #q = np.zeros_like(p)
        
        for k in range(1, size):
            q[n][k] = p[k] + (q[n][k-1]*x[n])
            
    y = q[:,-1]
            
    return y


p0 = np.array([1.,2,1])
x0 = np.array([1.,-1])
y = HornerVect(p0, x0)
print(y)


p = np.array([1., -1, 2, -3, 5, -2])
x = np.linspace(-1,1,1000000)
startTime = time.time()
y1 = HornerVect(p, x)
executionTime = (time.time() - startTime)
print("Tiempo de ejecucion V6: ", str(executionTime), " s")
print(y1)


startTime = time.time()
y2 = HornerV(p, x)
executionTime = (time.time() - startTime)
print("Tiempo de ejecucion V2: ", str(executionTime), " s")
print(y1)
