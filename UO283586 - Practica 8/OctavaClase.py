from gettext import GNUTranslations
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def punto_medio(f, a, b):
    aux = (b-a)*f((a + b)/2)
    return aux

f = lambda x : np.log(x)

x = sym.Symbol('x', real=True) 
f_sim = sym.log(x)
I_exacta = sym.integrate(f_sim,(x,1,3))
print(I_exacta)

I_exacta = float(I_exacta)

print()
print ("El valor aproximado es: ", punto_medio(f,1,3))
print ("El valor real es: ", I_exacta)


def trapecio(f,a,b):
    aux = (b-a)/2 * (f(a) + f(b))
    return aux

print()
print ("El valor aproximado es: ", trapecio(f,1,3))
print ("El valor real es: ", I_exacta)


def simpson(f,a,b):
    aux = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))
    return aux

print()
print ("El valor aproximado es: ", simpson(f,1,3))
print ("El valor real es: ", I_exacta)


def punto_medio_comp(f,a,b,n):
    res = 0
    h = (b-a)/n
    xprev = a
    for i in range(1,n+1):
        x = a + i*h
        xaux = (x+xprev)/2
        res += f(xaux)
        xprev = x
    res = res * h
    return res


print()
print ("El valor aproximado es: ", punto_medio_comp(f,1,3,5))
print ("El valor real es: ", I_exacta)

def trapecio_comp(f,a,b,n):
    h = (b-a)/n
    res = h/2 * (f(a) + f(b))
    puntos = np.linspace(a,b,n)
    aux = 0
    for i in range(1,n):
        x = a + i*h
        aux = aux + f(x)
    res = h * aux + res
    return res

print()
print ("El valor aproximado es: ", trapecio_comp(f,1,3,4))
print ("El valor real es: ", I_exacta)


def simpson_comp(f,a,b,n):
    h = (b-a)/n
    res = h/6
    aux = 0
    xprev = a
    for i in range(1,n+1):
        x = a + i*h
        xi = (x+xprev)/2
        aux = aux + (f(x) + f(xprev) + 4*f(xi))
        xprev = x
    res = res * aux
    return res


print()
print ("El valor aproximado es: ", simpson_comp(f,1,3,4))
print ("El valor real es: ", I_exacta)


def gauss(f,a,b,n):
    [x, w] = np.polynomial.legendre.leggauss(n)
    aux = 0
    for i in range(n):
        y = (b-a)/2*x[i] + (a+b)/2
        aux = aux + w[i]*f(y)
    aux = aux * ((b-a)/2)
    return aux

print()
print ("El valor aproximado es: ", gauss(f,1,3,1))
print ("El valor real es: ", I_exacta)

print()
print ("El valor aproximado es: ", gauss(f,1,3,2))
print ("El valor real es: ", I_exacta)

print()
print ("El valor aproximado es: ", gauss(f,1,3,3))
print ("El valor real es: ", I_exacta)


def grado_de_precision(formula, n):
    
