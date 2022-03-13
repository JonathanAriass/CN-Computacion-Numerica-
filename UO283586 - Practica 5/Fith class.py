# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:15:46 2022

@author: Jonathan Arias Busto
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x : x**5 - 3 * x**2 + 1.6

######################################
#        METODO DE LA SECANTE        #
######################################
def secante(f, x0, x1, tol=1.e-6, maxiter=100):
    cont = 1
    while cont <= maxiter:

        xk = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        
        cont+=1
        x0 = x1
        x1 = xk
        
        if abs(f(xk)) < tol:
            break
        
    return x1, cont


a1 = -0.7
b1 = -0.6
x, iteraciones = secante(f,a1,b1)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a2 = 0.8
b2 = 0.9
x, iteraciones = secante(f,a2,b2)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)

a3 = 1.2
b3 = 1.3
x, iteraciones = secante(f,a3,b3)
print("Raiz aproximada: ", x, " | Numero de iteraciones: ", iteraciones)


######################################
#           FUNCIONES (SciPy)        #
######################################
import scipy.optimize as op

f  = lambda x: np.sin(x) - 0.1*x - 0.1
df = lambda x: np.cos(x) - 0.1

x = np.linspace(-1,20,1000)
"""
plt.figure(figsize=(15,4))
plt.plot(x,f(x))
plt.plot(x,0*x,'k-')
plt.show()
"""
# Si utilizamos la derivada se usara el metodo de Newton
x0 = np.array([0., 2., 7., 8.])
raiz = op.newton(f,x0,fprime=df,tol=1.e-6,maxiter=100)       
print(raiz)

# Si no utilizamos la derivada se usara el metodo de la Secante
x0 = np.array([0., 2., 7., 8.])
raiz = op.newton(f,x0,tol=1.e-6,maxiter=100)       
print(raiz)

# Utilizando el metodo de Biseccion
x0 = np.array([0., 2., 7., 8.])
x1 = x0 + 1
raiz = np.zeros_like(x0)
for i in range(len(raiz)):
    raiz[i]= op.bisect(f,x0[i],x1[i],xtol=1.e-6,maxiter=100)       
    print(raiz[i])
    
x = np.linspace(-1,9)
"""
plt.figure()
plt.plot(x,f(x),x,x*0,'k',raiz,raiz*0,'ro')
plt.show()
"""

################################################
#        EXTREMOS Y PUNTOS DE INFLEXION        #
################################################
import sympy as sym

x = sym.Symbol('x', real=True)
f_sim = x**2 + sym.log(2*x + 7)*sym.cos(3*x) + 0.1
df_sim = sym.diff(f_sim,x)
df2_sim = sym.diff(df_sim,x)

f = sym.lambdify([x], f_sim,'numpy')
df1 = sym.lambdify([x], df_sim, 'numpy')
df2 = sym.lambdify([x], df2_sim, 'numpy')
print(df2_sim)

x = np.linspace(-1,3)

plt.figure()
plt.plot(x,df1(x),x,x*0,'k')
plt.show()


x5 = np.array([-0.9, 0., 1., 2.3, 2.7])
raices = op.newton(df1,x5,fprime=df2,tol=1.e-6,maxiter=100)
print('Extremos\n',raices)

x = np.linspace(-2,4)

plt.figure()
plt.plot(x,f(x),x,x*0,'k',raices,raices*0,'ro')
plt.show()


