# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:13:58 2022

@author: Jonathan Arias Busto (UO283586)
"""

import numpy as np
import matplotlib.pyplot as plt


#EJERCICIO 1
print ("EJERCICIO 1")
"""
Metodo de la secante:
    c = b - f(b)*((b-a)/(f(b)-f(a)))
    x0 = x1
    x1 = c
"""

def secante(f,x0,x1,tol=1.e-6,maxiter=100):
    c = 0
    count = 0
    while count <= maxiter:
        c = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        
        x0 = x1
        x1 = c
        
        count = count + 1
        
        if abs(f(c)) < tol and abs(x1-x0) < tol and abs(x1-x0)/abs(x1):
            break
    
    return c, count
    

f = lambda x : x**5 - 3*x**2 + 1.6
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



#FUNCIONES PYTHON PARA CALCULAR RAICES

import scipy.optimize as op

print ("\n\nFUNCIONES PYTHON")

"""
La función newton calcula las raices utilizando el metodo de la secante o Newton,
dependiendo de los parametros pasados.
la funcion bisect calcula las raices usando el metodo de biseccion.
"""
f  = lambda x: np.sin(x) - 0.1*x - 0.1
df = lambda x: np.cos(x) - 0.1

x = np.linspace(-1,20,1000)

plt.figure(figsize=(15,4))
plt.plot(x,f(x))
plt.plot(x,0*x,'k-')
plt.show()
plt.close()

# Al usar la derivada se usa el metodo de Newton
print("\nNewton por Newton")
x0 = np.array([0., 2., 7., 8.])
raices = op.newton(f,x0,fprime=df,tol=1.e-6,maxiter=100)
print(raices)

print("\nNewton por secante")

# Si no le pasamos la derivada se usara el metodo de la secante
races = op.newton(f,x0,tol=1.e-6,maxiter=100)
print(raices)

#Si usamos biseccion necesitamos estimar los valores iniciales
print("\nRaices por biseccion")
x0 = np.array([0., 2., 7., 8.])
x1 = x0 + 1
raices = np.zeros_like(x0)
for i in range(len(raices)):
    raices[i] = op.bisect(f,x0[i],x1[i],xtol=1.e-6,maxiter=100)
    print(raices[i])

x = np.linspace(-1,9)

plt.figure()
plt.plot(x,f(x),x,x*0,'k',raices,raices*0,'ro')
plt.show()



#EJERCICIO 2
print ("\n\nEJERCICIO 2")

"""
Calculo de extremo y puntos de inflexion:
"""
import sympy as sym

x = sym.Symbol('x', real=True)
f_sim = x**2 + sym.log(2*x + 7)*sym.cos(3*x) + 0.1
df_sim = sym.diff(f_sim,x)
df2_sim = sym.diff(df_sim,x)

f = sym.lambdify([x], f_sim,'numpy')
df1 = sym.lambdify([x], df_sim, 'numpy')
df2 = sym.lambdify([x], df2_sim, 'numpy')
print(df2_sim)

a = -2
b = 4
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label="Funcion f")
plt.plot([a,b],[0,0],'k-')
plt.title("Funcion f")
plt.legend()
plt.show()

plt.figure()
plt.plot(x,df1(x),x,x*0,'k')
plt.show()


x5 = np.array([-0.9, 0., 1., 2.3, 2.7])
raices = op.newton(df1,x5,fprime=df2,tol=1.e-6,maxiter=100)
mini = raices[df2(raices) > 0]
maxi = raices[df2(raices) < 0]
print('Extremos\n',raices)


a = -2.
b = 4.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label = 'Función f')
plt.plot([a,b],[0,0],'k-')
plt.plot(mini,f(mini),'go') # Se plotean los minimos
plt.plot(maxi,f(maxi),'ro') # Se plotean los maximo
plt.show()
print('EXTREMOS')
print(x1)


# SEGUNDA DERIVADAD DE F
plt.figure()
plt.plot(x,df2(x))
plt.plot([a,b],[0,0],'k-')
plt.title('Funcion derivada segunda de f')
plt.show()

#Puntos de inflexion
x0 = np.array([-0.5,0.5,1.5,2.5,3.7])
x1 = op.newton(df2,x0,tol=1.e-6,maxiter=100)
print(x1)

# Mostramos en grafica los puntos de inflexion
a = -1
b = 4
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label="Funcion f")
plt.plot([a,b],[0,0],'k-')
plt.plot(x1,f(x1),'bo',label="Puntos de inflexion")
plt.legend()
plt.show()


#EJERCICIO 3
print ("\n\nEJERCICIO 3")



#EJERCICIO 4
print ("\n\nEJERCICIO 4")



#EJERCICIO 5
print ("\n\nEJERCICIO 5")




#EJERCICIO 6
print ("\n\nEJERCICIO 6")
