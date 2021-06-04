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
    __init__(self, ao, an, bn): 
    """ Takes in ao, an, bn in terms of n and x """

    self.ao = ao
    self.an = an
    self.bn = bn

    self.series = ao + an * math.cos(n * x) + bn * math.sin(n * x)

def graph(self, Length = pi, Harmonic):
    x = np.linspace(-Length, Length, 50) #Creates the domain to graph the function over 
    ones_mat = np.ones(x.size, dtype = float) #initializes an array of 1s to fill later in the loop
    function = self.ao * ones_mat

    for n in range(1,Harmonic,1):
        function = self.ao + self.an * np.cos(n * x) + self.bn * np.sin(n * x) #Combines all the constants with the general Fourier series

def Summation_Function(ao,an,bn):
    """ Takes constants of the Fourier Transform and makes them into a summation
    """