from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi, sin
from scipy import integrate

#n = 3 #Harmonic

#passing a function to a class 

L_1 = -1
L_2 = 1

def f(x):
    return x


def fcos(x,n,L_2):
    return f(x) * np.cos(n * pi * x / L_2)

def fsin(x,n,L_2):
    return f(x) * np.sin(n * pi * x / L_2)


domain = np.linspace(-pi, pi, 50)
ao = np.ones(domain.size, dtype = float)

a_0 = (1 / (2*L_2)) * integrate.quad(f, L_1, L_2)[0]

print(a_0)

#a_n = (1 / L_2) * integrate.quad(fcos, L_1, L_2, args=(n, L_2))[0]

#b_n = (1 / L_2) * integrate.quad(fsin, L_1, L_2, args=(n, L_2))[0]

ans = ao * a_0 
print(len(ans))
print(len(domain))

def a_n(n,L_1,L_2):
    return (1 / L_2) * integrate.quad(fcos, L_1, L_2, args=(n, L_2))[0]

def b_n(n,L_1,L_2):
    return (1 / L_2) * integrate.quad(fsin, L_1, L_2, args=(n, L_2))[0]

for n in range(1, 25, 1):
    a = a_n(n,L_1,L_2)
    b = b_n(n,L_1,L_2)
    ans = ans + (a * np.cos(n * pi * domain / L_2)) + (b * np.sin(n * pi * domain / L_2))

#for n in range (1,3):
#    print(np.cos(n*pi*domain/L_2))

plt.plot(domain,ans)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('yay')
plt.show()
