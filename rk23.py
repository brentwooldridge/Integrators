# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:32:05 2021

@author: Teacher
"""
from scipy import integrate 
import numpy
from scipy.integrate import RK23
import matplotlib.pyplot as plt

def f(t, x):
    return x

sol = RK23(f, t0 = 0, t_bound = 1, y0 = [0])

print(sol)