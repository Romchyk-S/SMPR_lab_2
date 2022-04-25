# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:43:09 2022

@author: romas
"""

import sympy as sp

import get_data as gd

import bayes_values as bv

import geometric as g

import variational as v




p_1 = sp.symbols("p_1")

p_2 = sp.symbols("p_2")

p_var, eff = gd.get_data_from_file("example.txt")

# p_var, eff = gd.get_data_from_file("variant.txt")

p_geom = [p_1, p_2, 1-p_1-p_2]


# Bayes_values_geom = bv.get_bayes_values(p_geom, eff) 

# g.geom_method(Bayes_values_geom, p_1, p_2, "example.txt")


Bayes_values_var = bv.get_bayes_values(p_var, eff)

print(Bayes_values_var)

v.variational_method()