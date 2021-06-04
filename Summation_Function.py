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

def graph(self):

def Summation_Function(ao,an,bn):
    """ Takes constants of the Fourier Transform and makes them into a summation
    """