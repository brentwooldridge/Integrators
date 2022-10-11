# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:02:48 2021

@author: Teacher
"""

from scipy import integrate
import numpy
#from scipy.integrate import bdf
import matplotlib.pyplot as plt

def f(t, x):
    return x

sol = integrate.BDF(f, t0 = 0, t_bound = 1, y0 = [0])

print(sol)