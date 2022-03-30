import numpy as np
import matplotlib.pyplot as plt

"""
    Significado de los argumentos de la funcion:
        - f: funcion
        - g: grado del polinomio aproximado 
        - a: inicio intervalo
        - b: fin intervalo
        - n: numero de nodos
"""
def aprox1(f, g, a, b, n):
    x = np.linspace(a,b,n)
    #rint(x)
    y = f(x)
    #print(y)
    # Construimos la matriz V del sistema 1
    V = np.zeros((n,g+1))
    for i in range(n):
        for j in range(g+1):
            if j==0:
                V[i][j] = 1
            else:
                V[i][j] = x[i]**j
    #print(V)
    T = np.transpose(V)
    #print(T)

    # Obtenemos C que es la matriz de coeficientes
    C = np.dot(T,V)
    # Obtenemos d que es la matriz de terminos independientes del sistema 2
    d = np.dot(T,y)

    p = np.linalg.solve(C,d)

    #print(p)
    p = p[::-1]

    #print("a:", a)

    values = np.linspace(a,b, 50)
    res = np.polyval(p, values)

    #print(res)

    """plt.figure()
    #plt.axis([0,2,0,1])
    plt.plot(values,res, label='funcion aproximada')
    plt.plot(x, y, 'r.', label='nodos')
    plt.legend()
    plt.show()
    plt.close()"""




f = lambda x : np.sin(x)
aprox1(f, 2, 0, 2, 5)

f = lambda x : np.cos(np.arctan(x)) - np.log(x+5)
aprox1(f, 4, -2, 0, 10)



"""
    Ejercicio 2
"""
import pandas as pd

df = pd.read_csv('http://www.unioviedo.es/compnum/laboratorios_py/new/cars.csv',sep=',')

#print(df)

# Obtenemos los diferentes datos de la tabla
hp = df['horsepower']
we = df['weight']

# Calculamos el polinomio aproximado de grado 1
aux = np.polyfit(we, hp, 1)
val = np.polyval(aux, 3000)

# Obtenemos los supuestos valores para la recta de regresion
aux2 = np.polyval(aux,we)

print(aux2)

# Printeamos todos la informacion 
plt.figure()
plt.plot(we, hp, 'b.')
plt.plot(we,aux2, 'r')
plt.show()
plt.close()


print(aux)
print(val)
