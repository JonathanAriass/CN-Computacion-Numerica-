# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:15:39 2022

@author: byjon
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print(np.pi)

# Creacion de un array de int

#print('a =', a)

# El punto indica un float64
b = np.array([1., 2, 3, 4])

# Creacion de una matriz 2x2
c = np.array([[1, 2],[3, 4]]) 
print('c =\n', c)

# Generar una matriz con 0's y 1's
d = np.zeros((2,3))
e = np.zeros((4,5))

# Genera una sucesion de numeros con arange()
f = np.arange(1, 10, 2)

# Linspace hace lo mismo solo que en vez de pasarle la diferencia entre numeros
#le pasamos la cantidad de numero que queremos que tenga el array
g = np.linspace(1, 9, 5)

for n in range(g.size):
    print(g[n])
    
# Cosas utiles
len(g) # Muestra las filas
c+c # Suma las matrices indice por indice
c*c # Multiplica las matrices indice por indice
np.dot(c, c) # Multriplica las matrices de forma algebraica

h = np.arange(10)
h[:3] # Se queda con los 3 primeros elementos
h[0:4:2]
i = [0,4,6]
h[i] # Se queda con las posiciones pasadas a traves del array i

j = np.array([[1, 2, 4],[3, -1, 2]])
j[0,:] # Todas las columnas de la primera fila
print(j[0,:])
print(j[1,:]) # Todas las columnas de la segunda fila
print(j[:,0]) # Todas las filas de la primera columna
print(j[0:2,0:2]) #0 y 1 para las filas y 0 y 1 para las columnas

k = np.arange(10)
l = k
print(l)
l[0] = 5
print(l)
print(k) # CUIDADO QUE LA ORIGINAL TAMBIEN SE MODIFICA

k = np.arange(10)
l = k.copy()
print(l)
l[0] = 5
print(l)
print(k)




# FUNCIONES ELEMENTALES
print(np.sin(np.pi/2))
print(np.sin(0))

print(np.exp(2)) # Exponencial de 2

print(np.arctan(np.inf))




# FUNCIONES
f = lambda x : x**2
print(f(3))

g = lambda x,y : x*y
print(g(2, 6))

def func(x):
    if x > 2:
        return 0
    else:
        return 1
    
print (func(2))
print (func(6))

# Se puede pasar un array como parametro a una funcion
x = np.array([1, 2, 3])
print(f(x))




# IMPIMIR FUNCIONES
x = np.linspace(-3,3,100)
plt.plot(x, f(x))
plt.plot(x, 0*x) # EJE X
plt.grid()
plt.close()

# GENERACION DE MALLAS
xgrid = np.linspace(-1, 1, 20)
ygrid = np.linspace(-1, 1, 20)

X, Y = np.meshgrid(xgrid, ygrid)

g = lambda x,y : x**2 + y**2

plt.figure()
plt.contourf(X, Y, g(X,Y), cmap='jet')
plt.colorbar()
plt.show()
plt.close()

# 3D
"""
fig1 = plt.figure(figsize=(10,5))
ax1 = fig1.gca(projection='3d')
ax1.plot_surface(X, Y, g(X,Y), cmap='jet')
plt.show()
plt.close()
"""


# EJERCICIO 1 (NOCIONES BASICAS)
a = np.array([1,3,7])
b = np.array([[2,4,3],[0,1,6]])
c = np.zeros((3,2))
d = np.ones((3,4))
print(a)
print(b)
print(c)
print(d)

# EJERCICIO 2
a = np.arange(7,16,2)
b = np.arange(10, 5, -1)
c = np.arange(15, -1, -5)
print(a)
print(b)
print(c)
a = np.linspace(7,15,5)
b = np.linspace(10, 6, 5)
c = np.linspace(15, 0, 4)
print(a)
print(b)
print(c)


# EJERCICIO 3
A = np.array([[2,1,3,4],[9,8,5,7],[6,-1,-2,-8],[-5,-7,-9,-6]])
"""
El funcionamiento para obtener alguna parte de una matriz es:
    A[:,:] # Selecciona todo
    A[*1,*2] 
        *1--> (fila inicial):(fila final)
        *2--> (columna inicial):(columna final)
"""

print('Ejercicio 3')
print(A[:,0]) # primera columna
print(A[2,:])
print(A[0:3,0:2])
print(A[2:4,2:4])
print(A[1:3,1:3])
print(A[0:4,1:4])
print(A[1:4,1:3])


print(A[:,:])


# EJERCICIO 4

print ('Ejercicio 4')
f = lambda x : x * np.exp(x)
g = lambda z : z/(np.sin(z)*np.cos(z))
h = lambda x,y : (x * y) / (x**2 + y **2)


print ('f(2) = ',f(2))
print ('g(pi/4) = ', g(np.pi/4))
print ('h(2,4) = ',h(2,4))


# EJERCICIO 5
aux = -(np.pi*2)
aux2 = np.pi*2
print(aux)
b = np.linspace(aux, aux2, 100000)
print(b)
f = lambda x : x * np.sin(3*x)

plt.figure()
plt.plot(b, b*0, 'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(b, f(b), label="Ejercicio 5")
plt.title('x sen(3x)')
plt.show()
