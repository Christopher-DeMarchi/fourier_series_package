from math import cos, pi, sin
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import array as arr
class Series(): 
    """Series parent class
    Attributes - 
        ao
        an
        bn
    Methods - 
        Graph
    """
    def __init__(self, ao, an, bn):
        self.ao = ao
        self.an = an
        self.bn = bn

    def graph(self, Length = pi, Harmonic = 1):
        x = np.linspace(-Length, Length, 50) #Creates the domain to graph the function over 
        ones_mat = np.ones(x.size, dtype = float) #initializes an array of 1s to fill later in the loop
        series = self.ao * ones_mat

        for n in range(1,Harmonic,1):
            series = series + self.an * np.cos(n * x) + self.bn * np.sin(n * x) #Combines all the constants with the general Fourier series