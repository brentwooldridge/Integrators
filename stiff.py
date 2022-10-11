# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:27:20 2021

@author: Teacher
"""
import scipy as sp
from scipy.integrate import ode
import numpy as np

def f(x, t):
    return x

def g(x):
    return x ** f(x)


r = ode(f).set_integrator('vode', method='bdf', with_jacobian=False)
#r.set_initial_value(0.0).set_f_params(1.0).set_jac_params(0.0)
t1 = 10
dt = 1
while r.successful() and r.t < t1:
    r.integrate(r.t+dt)
    print("%g %g" % (r.t, r.y))