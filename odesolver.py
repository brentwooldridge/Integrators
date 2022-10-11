# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:08:41 2021

@author: Teacher
"""

from scipy import integrate 
import numpy
from scipy.integrate import OdeSolver
import matplotlib.pyplot as plt

def f(vector, t):
    x = vector[0]
    y = vector[1]
    
    x_dot = x
    y_dot = y 
    return [x_dot, y_dot]

sol = OdeSolver(f, t0 = 0, t_bound = 1, y0 = [0, 1], vectorized = True)

