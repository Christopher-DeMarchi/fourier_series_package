import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi, sin
from scipy import integrate

class fourier_series():
    ''' fits a fourier series to any function of x
    Attributes - 
        f_of_x = lambda x: <function>  *with x as the independent variable
        L_1 = beginning of integration
        L_2 = end of integration
    Methods -
        Graph
            Args-
            Harmonic - the harmonic desired to graph  
    '''    
    def __init__(self,f_of_x, L_1,L_2):
        self.f = f_of_x
        self.L_1 = L_1
        self.L_2 = L_2

    def graph(self, harmonic):
        def f(x):
            return x
        def fcos(x,n,L_2):
            return f(x) * np.cos(n * pi * x / self.L_2)

        def fsin(x,n,L_2):
            return f(x) * np.sin(n * pi * x / self.L_2)

        domain = np.linspace(-pi, pi, 50)
        ao = np.ones(domain.size, dtype = float)

        a_0 = (1 / (2*self.L_2)) * integrate.quad(f, self.L_1, self.L_2)[0]
        ans = ao * a_0 

        def a_n(n,L_1,L_2):
            return (1 / self.L_2) * integrate.quad(fcos, self.L_1, self.L_2, args=(n, self.L_2))[0]

        def b_n(n,L_1,L_2):
            return (1 / self.L_2) * integrate.quad(fsin, self.L_1, self.L_2, args=(n, self.L_2))[0]

        for n in range(1, harmonic, 1):
            a = a_n(n,self.L_1,self.L_2)
            b = b_n(n,self.L_1,self.L_2)
            ans = ans + (a * np.cos(n * pi * domain / self.L_2)) + (b * np.sin(n * pi * domain / self.L_2))

        plt.plot(domain,ans)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Fourier Series, {}th Harmonic'.format(harmonic))
        plt.show()

