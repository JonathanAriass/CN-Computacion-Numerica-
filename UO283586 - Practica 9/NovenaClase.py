import numpy as np
import matplotlib.pyplot as plt

def sust_regre(U, b):
    res = np.zeros_like(b)
    
    res[len(b)-1] = b[len(b)-1]/U[len(b)-1,len(b)-1]
    for i in range(len(b)-2, -1, -1):
        aux = 0
        bi = b[i]
        for j in range(i+1,len(b)):
            aux = aux + (U[i][j]*res[j])
        res[i] = (bi-aux)/U[i][i]
    return res
    
#%%
print('------------- SISTEMA 1 -------------')
print('--- Datos ---')
U = np.array([[2., 1, 1], [0, 2, 1], [0, 0, 2]])
b = np.array([9., 4, 4])
print('U')
print(U)
print('b')
print(b)
print('--- Solución ---')
print('x')
print(sust_regre(U,b))
#%%
print('------------- SISTEMA 2 -------------')
print('--- Datos ---')
n = 5
np.random.seed(2)           
U = np.random.random((n,n)) 
U = np.triu(U) # Haz cero los elementos bajo la diagonal
b = np.random.random(n)
print('U')
print(U)
print('b')
print(b)
print('--- Solución ---')
print('x')
print(sust_regre(U,b))

#%%
def triang(A,b):
    U = np.copy(A)
    c = np.copy(b)
    
    n = len(b)
    for k in range(n-1):
        for i in range(k+1,n):
            f = U[i][k] / U[k][k]
            c[i] -= f * c[k]
            U[i] -= f * U[k]
    return U, c
#%%
print('------------- SISTEMA 1 -------------')
print('--- Datos ---')
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([2., 4, 6])
print('A')
print(A)
print('b')
print(b)
print('--TRIANGULARIZACIÓN-- ')
U, c = triang(A,b)
print('U')
print(U)
print('c')
print(c)
print(' --SUSTITUCIÓN REGRESIVA--')
print('x')
print(sust_regre(U,c))
#%%        
print('------------- SISTEMA 2 -------------')
print('--- Datos ---')
n = 5
np.random.seed(3)           
A = np.random.random((n,n)) 
b = np.random.random(n)
print('A')
print(A)
print('b')
print(b)
print('--TRIANGULARIZACIÓN-- ')
U, c = triang(A,b)
print('U')
print(U)
print('c')
print(c)
print(' --SUSTITUCIÓN REGRESIVA--')
print('x')
print(sust_regre(U,c))