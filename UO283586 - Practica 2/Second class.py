# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:05:36 2022

@author: Jonathan Arias Busto (UO283586)
"""
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.exp(x)
a = -1.; b = 1. #[a,b]
x = np.linspace(a,b,5)
print(x)

# En este caso estamos vectorizando, por lo que el programa hace por su cuenta
# la funcion de cada elemento
y = f(x)
print(y)

for i in range(4):
    print(i)
    
# crea una funcion con 5 puntos, por lo que la representacion no es lo mas perfecta
plt.figure()
plt.plot(x,y, label='f(5 MALLADO)')
plt.show()
#plt.grid()

# por defecto linspace crea una malla de 50 puntos, y por lo tanto es mas fiel a la funcion
x = np.linspace(a,b)
y = f(x)
#plt.figure()
#plt.plot(x,y)
#plt.show()
#plt.grid()


ox = 0*x

plt.plot(x,y, label = 'f(50 MALLADO)')
plt.plot(x, ox, 'k', label='Eje OX')
plt.title('Ejemplo de personalizacion de graficas')
plt.legend()
plt.grid()
plt.close()




# POLINOMIO DE TAYLOR
"""El polinomio de Taylor trata de aproximar una funcion a traves de un polinomio
de grado 2, a traves de las derivadas de puntos de la funcion original."""

"""Estamos tratando de aproximar la funcion exponencial de 0.5,"""
x0 = 0.5
polinomio = 0.
factorial = 1.

for i in range(4):
    sumando = x0**i/factorial
    polinomio += sumando
    factorial *= i+1
    
print('P3(0.5)  = ', polinomio)
print('np.expo(0.5) = ', np.exp(x0))


# Convertimos el programa en una funcion y probamos un polinomio de grado mayor
def PTaylor(x0, grado):
    polinomio = 0.
    factorial = 1.
    
    for i in range(grado+1):
        sumando = x0**i/factorial
        polinomio += sumando
        factorial *= i+1
    return polinomio


print('PTaylor(0.5, 10)  = ', PTaylor(0.5, 10))
print('np.expo(0.5) = ', np.exp(x0))


#Se puede introducir un array como parametro de la funcion
a = -1.;b = 1.
x = np.linspace(a,b,5)
print('x      = ', x)
print('PTaylor(0.5, 10)  = ', PTaylor(x, 10))
print('np.expo(0.5)      = ', np.exp(x))


"""Ahora haremos una malla de 50 puntos y aplicaremos el algoritmo para asi 
poder ver la diferencia con la grafica real (Exponencial)."""
a = -1.;b = 1.
x = np.linspace(a,b)
ox = 0*x

plt.figure()
plt.plot(x,f(x), label='f(Real)')
plt.plot(x, ox, 'k')
plt.plot(x, PTaylor(x,2), 'r', label='f(PTaylor)')
plt.title('Polinomio de Taylor sobre funcion exponencial')
plt.legend()
plt.grid()
plt.show()
plt.close()


"""Ahora cambiamos el rango de [-1,1] a [-3,3] e iteramso a traves de un bucle
diferentes grados del polinomio de taylor."""
a = -3.;b = 3.
x = np.linspace(a,b)
ox = 0*x

plt.figure()
plt.plot(x,f(x), label='f(Real)')
plt.plot(x, ox, 'k')
plt.axis([-3,3,-5,20]) #Para que se fijen los ejes
for grado in range(1,5):
    plt.plot(x, PTaylor(x,grado), label='f(PTaylor:'+str(grado)+')')
    plt.title('Polinomio de Taylor sobre funcion exponencial')
    plt.legend()
    #plt.pause(1)
plt.grid()
plt.show()

#################
#  EJERCICIO 1  #
#################
"""Utilizando un bucle while, escribir un programa, que utilizando el desarrollo 
de McLaurin para la función f(x)=ex, calcule su valor aproximado en el punto 
x0 = -0.4. El criterio de parada será que el valor del último sumando añadido 
en valor absoluto es menor que una tolerancia tol=1.e-8 y que el número máximo 
de sumandos es 100, es decir maxNumSum=100. Comparar su valor con el valor de 
la función lambda f. Dar el número de sumandos utilizados."""

tol = 1.e-8
tolAux = 0
x0 = -0.4
factorial = 1.
polinomio = 0.

i=0

while (tolAux < tol and i <= 100):
    sumando = x0**i/factorial
    tolAux = np.abs(sumando)
    polinomio += sumando
    factorial *= i+1
    i = i + 1
    
print (i)