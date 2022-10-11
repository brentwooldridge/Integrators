# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:20:32 2021

@author: Teacher
"""

import numpy
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, x):
    return x

sol = solve_ivp(f, t_span = [0, 10], y0 = [0])

print(sol)