# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:53:40 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt


#EJERCICIO 1
"""
p: polinomio 
x0: punto 
"""
def horner(p,x0):
    q = np.zeros_like(p)
    n = len(p)
    q[0] = p[0]
    for i in range(1,n):
        q[i] = p[i] + x0 * q[i-1]
    
    cociente = q[:-1]
    resto = q[-1]
    return cociente, resto

p0 = np.array([1.,2,1])
x0 = 1.

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.

p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.

coeficientes, resto = horner(p0, x0)

print('Coeficientes de Q = ', str(coeficientes))
print('P0[1] = ', resto)


coeficientes1, resto1 = horner(p1, x1)

print('Coeficientes de Q = ', str(coeficientes1))
print('P1[1] = ', resto1)

coeficientes2, resto2 = horner(p2, x2)
print('Coeficientes de Q = ', str(coeficientes2))
print('P2[-1] = ', resto2)



#EJERCICIO 2

def hornerV(p,x):
    n = len(p)
    y = np.zeros_like(x)
    for k in range(len(x)):
        q = np.zeros_like(p)
        q[0] = p[0]
        for i in range(1,n):
            q[i] = p[i] + x[k] * q[i-1]
        
        resto = q[-1]
        y[k] = resto
    return y


p = np.array([1., -1, 2, -3, 5, -2])
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x = np.linspace(-1,1)

y = hornerV(p, x)
y2 = hornerV(r, x)

plt.figure()
plt.plot(x,np.polyval(p,x))
plt.plot(x,0*x,'k')
plt.title('Polinomio P')
plt.show()
plt.close()

plt.figure()
plt.plot(x,y, label='Horner')
plt.plot(x,0*x,'k')
plt.title('Figura con Horner (P)')
plt.show()
plt.close()

plt.figure()
plt.plot(x,y2, label='Horner')
plt.plot(x,0*x,'k')
plt.title('Figura con Horner (R)')
plt.show()
plt.close()



#EJERCICIO 3

def derPol(p,x0):
    factorial = 1.
    res = np.zeros_like(p)
    for i in range(0,len(p)):
        coeficientes, resto = horner(p, x0)
        res[i] = resto * factorial
        factorial *= i+1
        p = coeficientes
    return res

np.set_printoptions(suppress=True) # Quita la notacion exponencial

p = np.array([1., -1, 2, -3,  5, -2])
x0 = 1.

pol = derPol(p, x0)
print(pol)

r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x1 = -1.

pol2 = derPol(r, x1)
print(pol2)




# EJERCICIO 4

def divisores(m):
    count = 0
    div = np.zeros(m*2)
    for i in range(1, m+1):
        if m%i == 0:
            div[count] = i
            count = count + 1
            div[count] = -i
            count = count + 1
    return div[:count]

print(divisores(18))


def raices(p):
    res = np.zeros_like(p)
    x = abs(int(p[-1])) # Almacenamos el termino independiente
    posiblesDivisores = divisores(x)
    count = 0
    for x0 in posiblesDivisores:
        coficientes, resto = horner(p,x0)
        if resto == 0:
            res[count] = x0
            p = coficientes
            count = count + 1
    return res[:count]

"""
def raices(p):
    res = np.zeros_like(p)
    x = abs(int(p[-1])) # Almacenamos el termino independiente
    posiblesDivisores = divisores(x)
    count = 0
    cond = True
    for x0 in posiblesDivisores:
        while cond == True:
            coficientes, resto = horner(p,x0)
            if resto == 0:
                res[count] = x0
                p = coficientes
                count = count + 1
            else:
                cond = False
        cond = True
    return res[:count]
"""
p0 = np.array([1., 0, -1])
res = raices(p0)
print(res)

p1 = np.array([1., -3, -6, 8])
res = raices(p1)
print(res)

p2 = np.array([1., -5, 1, 17, -22, 8])
res = raices(p2)
print(res)

p3 = np.array([1.,0,-24,-30,135,366,320,96]) 
res = raices(p3)
print(res)
