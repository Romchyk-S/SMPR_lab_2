# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:43:09 2022

@author: romas
"""

import sympy as sp

import re as re

import geometric as g

import bayes_values as bv


def get_data_from_file(file_name):
    
    p = []

    eff = []
    
    f = open(str(file_name))

    for s in f:
        
        s = s.strip().split(" ")
        
        arr = []
        
        i = 0
        
        while i < len(s):
            
            if i == 0:
                
                p.append(float(s[i]))
                
            else:
                
                arr.append(int(s[i]))
            
            i += 1
            
        eff.append(arr)
        
    
    return p, eff

p_1 = sp.symbols("p_1")

p_2 = sp.symbols("p_2")

p_var, eff = get_data_from_file("example.txt")

p_geom = [p_1, p_2, 1-p_1-p_2]




Bayes_values_geom = bv.get_bayes_values(p_geom, eff) 

g.geom_method(Bayes_values_geom)


Bayes_values_var = bv.get_bayes_values(p_var, eff) 
