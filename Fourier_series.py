from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi, sin
from scipy import integrate

#n = 3 #Harmonic

#passing a function to a class 

L_1 = -pi
L_2 = pi

def f(x):
    return x**2

def fcos(x,n,L_2):
    return f(x) * cos(n * pi * x / L_2)

def fsin(x,n,L_2):
    return f(x) * sin(n * pi * x / L_2)

#f = x**2

y = np.linspace(-pi, pi, 50)
ao = np.ones(y.size, dtype = float)
a_0 = (1 / L_2) * integrate.quad(f, L_1, L_2)[0]

#a_n = (1 / L_2) * integrate.quad(fcos, L_1, L_2, args=(n, L_2))[0]
#b_n = (1 / L_2) * integrate.quad(fsin, L_1, L_2, args=(n, L_2))[0]

ans = ao * a_0 
print(len(ans))
print(len(y))

def a_n(n,L_1,L_2):
    return (1 / L_2) * integrate.quad(fcos, L_1, L_2, args=(n, L_2))[0]

def b_n(n,L_1,L_2):
    return (1 / L_2) * integrate.quad(fsin, L_1, L_2, args=(n, L_2))[0]

for n in range(1, 25, 1):
    ans = ans + (a_0 / 2) + (a_n(n,L_1,L_2) * cos(n * pi * y / L_2)) + (b_n(n,L_1,L_2) * sin(n * pi * y / L_2))
plt.plot(y,ans)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('yay')
plt.show()