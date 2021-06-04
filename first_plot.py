from math import cos, pi, sin
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import array as arr

# inputs L (pi), f(the equation), harmonics(25)

x = np.linspace(-pi,pi,50)
elems = x.size
ao = np.ones(elems,dtype = float)
f = ((pi**2)/3)*ao

for n in range(1,25,1):
    f = f + ((4*(-1)**n) / n**2)*np.cos(n*x)
    

plt.plot(x,f)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('xtra-zomes')
plt.show()




